import os
from aqt import mw
from aqt.qt import *
from anki.hooks import addHook
from aqt.utils import tooltip

ADDON_NAME = "Extract to TXT"
DEFAULT_OUTPUT_PATH = os.path.join(os.path.expanduser("~"), "output.txt")

def extract_to_txt(nids):
    output_path = get_output_path_from_config()
    if not output_path:
        return

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            previous_deck_id = None
            for nid in nids:
                note = mw.col.getNote(nid)
                deck_id = note.cards()[0].did
                if deck_id != previous_deck_id:
                    if previous_deck_id is not None:
                        f.write("\n")
                    f.write(f"[Deck: {mw.col.decks.get(deck_id)['name']}]\n")
                    previous_deck_id = deck_id
                for name, field in zip(note.model()["flds"], note.fields):
                    field_content = field if field else "*empty*"
                    f.write(f"[{name['name']}]\n{field_content}\n")
                f.write("\n")
        tooltip("Extraction completed.")
    except OSError as e:
        error_message = "Failed to create the output file:\n"
        if "Permission denied" in str(e):
            error_message += "Please specify a file path, not a directory."
        elif "No such file or directory" in str(e):
            error_message += "The specified directory does not exist."
        else:
            error_message += str(e)
        QMessageBox.critical(mw, "Error", error_message)

def get_output_path_from_config():
    config = mw.addonManager.getConfig(__name__)
    output_path = config.get("01_output_path")
    if not output_path:
        return None
    output_path = os.path.expanduser(output_path)
    return output_path

def select_output_path():
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.AnyFile)
    file_dialog.setAcceptMode(QFileDialog.AcceptSave)
    file_dialog.setDefaultSuffix("txt")
    file_dialog.setOption(QFileDialog.DontUseNativeDialog, False)

    if file_dialog.exec_():
        selected_file = file_dialog.selectedFiles()[0]
        mw.addonManager.writeConfig(ADDON_NAME, {"01_output_path": selected_file})

def on_browser_menu(browser):
    a = QAction("Extract to TXT File", browser)
    a.triggered.connect(lambda _, browser=browser: extract_to_txt(browser.selectedNotes()))
    browser.form.menu_Notes.addSeparator()
    browser.form.menu_Notes.addAction(a)

def on_config_button_clicked():
    config_dialog = ConfigDialog()
    config_dialog.exec_()

def on_setup_menus():
    main = mw.app.activeWindow()
    if main:
        tools_menu = main.menu_Tools
        config_action = QAction("Extract to TXT Configuration", tools_menu)
        config_action.triggered.connect(on_config_button_clicked)
        tools_menu.addAction(config_action)

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Extract to TXT Add-on Configuration")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.path_edit = QLineEdit()
        self.path_edit.setText(get_output_path_from_config() or DEFAULT_OUTPUT_PATH)
        layout.addWidget(QLabel("Output File Path:"))
        layout.addWidget(self.path_edit)

        button_box = QDialogButtonBox()
        save_button = button_box.addButton(QDialogButtonBox.Save)
        save_button.clicked.connect(self.save_config)
        layout.addWidget(button_box)

    def save_config(self):
        output_path = self.path_edit.text()

        if not output_path:
            QMessageBox.warning(self, "Warning", "Please specify a file path.")
            return

        if os.path.isdir(output_path):
            QMessageBox.warning(self, "Warning", "Please specify a file path, not a directory.")
            return

        try:
            with open(output_path, "w") as f:
                pass
        except OSError as e:
            error_message = "Failed to create the output file:\n"
            if "Permission denied" in str(e):
                error_message += "Please specify a file path, not a directory."
            elif "No such file or directory" in str(e):
                error_message += "The specified directory does not exist."
            else:
                error_message += str(e)
            QMessageBox.critical(self, "Error", error_message)
            return

        mw.addonManager.writeConfig(ADDON_NAME, {"01_output_path": output_path})
        self.close()

# Connect the hooks
addHook("browser.setupMenus", on_browser_menu)
addHook("profileLoaded", on_setup_menus)