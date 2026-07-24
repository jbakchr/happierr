from happierr.messages.attribute_error import ATTRIBUTE_ERROR
from happierr.messages.file_not_found import FILE_NOT_FOUND
from happierr.messages.import_error import IMPORT_ERROR
from happierr.messages.index_error import INDEX_ERROR
from happierr.messages.key_error import KEY_ERROR
from happierr.messages.module_not_found import MODULE_NOT_FOUND
from happierr.messages.name_error import NAME_ERROR
from happierr.messages.syntax_error import SYNTAX_ERROR
from happierr.messages.type_error import TYPE_ERROR
from happierr.messages.value_error import VALUE_ERROR


ERROR_GUIDES = {
    "ModuleNotFoundError": MODULE_NOT_FOUND,
    "ImportError": IMPORT_ERROR,
    "SyntaxError": SYNTAX_ERROR,
    "FileNotFoundError": FILE_NOT_FOUND,
    "TypeError": TYPE_ERROR,
    "NameError": NAME_ERROR,
    "ValueError": VALUE_ERROR,
    "AttributeError": ATTRIBUTE_ERROR,
    "KeyError": KEY_ERROR,
    "IndexError": INDEX_ERROR,
}