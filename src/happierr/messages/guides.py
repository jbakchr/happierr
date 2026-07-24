from happierr.messages.file_not_found import FILE_NOT_FOUND
from happierr.messages.import_error import IMPORT_ERROR
from happierr.messages.module_not_found import MODULE_NOT_FOUND
from happierr.messages.syntax_error import SYNTAX_ERROR


ERROR_GUIDES = {
    "ModuleNotFoundError": MODULE_NOT_FOUND,
    "ImportError": IMPORT_ERROR,
    "SyntaxError": SYNTAX_ERROR,
    "FileNotFoundError": FILE_NOT_FOUND,
}