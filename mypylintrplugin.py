# Adding custom check classes

import ast
from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages


class CustomFlaskDebugChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-flask-debug-checker"
    msgs = {
        "W9901": (
            "Possible Flask Debug Mode: Do not enable debug mode in production! THIS IS MY CUSTOM MESSAGE",
            "flask-debug-mode",
            "This message is shown when Flask's debug mode is enabled in production.",
        ),
    }

    @check_messages("flask-debug-mode")
    def visit_call(self, node):
        if (
            node.func.as_string() == "app.run"
            and "debug" in [kw.arg for kw in node.keywords]
        ):
            self.add_message("flask-debug-mode", node=node)

class CustomEvalChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-eval-checker"
    msgs = {
        "W9909": (
            "THIS IS MY CUSTOM MSG FOR USE OF EVAL FUNCTION",
            "eval-function",
            "This message is shown when the 'eval' function is used.",
        ),
    }

    @check_messages("eval-function")
    def visit_call(self, node):
        if node.func.as_string() == "eval":
            self.add_message("eval-function", node=node)

class CustomWeakHashChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-weak-hash-checker"
    msgs = {
        "W9903": (
            "Avoid using weak cryptographic hashing algorithms for sensitive data.",
            "weak-crypto-hash",
            "This message is shown when weak cryptographic hashing algorithms are used for sensitive data.",
        ),
    }

    @check_messages("weak-crypto-hash")
    def visit_call(self, node):
        weak_crypto_algorithms = ["md5", "sha1"]
        if (
            node.func.as_string() == "hashlib.new"
            and len(node.args) > 0
            and node.args[0].s in weak_crypto_algorithms
        ):
            self.add_message("weak-crypto-hash", node=node)

class CustomCredentialsChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-credentials-checker"
    msgs = {
        "W9904": (
            "Avoid hard-coding credentials in the source code.",
            "hard-coded-credentials",
            "This message is shown when hard-coded credentials are found in the source code.",
        ),
    }

    @check_messages("hard-coded-credentials")
    def visit_assign(self, node):
        if (
            isinstance(node.value, ast.Str)
            and "password" in node.value.s.lower()
            and "username" in node.value.s.lower()
        ):
            self.add_message("hard-coded-credentials", node=node)

class CustomExecChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-exec-checker"
    msgs = {
        "W9905": (
            "Avoid using 'exec' function. It can be a security risk.",
            "exec-function",
            "This message is shown when the 'exec' function is used.",
        ),
    }

    @check_messages("exec-function")
    def visit_call(self, node):
        if node.func.as_string() == "exec":
            self.add_message("exec-function", node=node)


class CustomOpenChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-open-checker"
    msgs = {
        "W9906": (
            "Avoid using the 'open' function. It can be a security risk.",
            "custom-open-function",
            "This message is shown when the 'open' function is used.",
        ),
    }

    @check_messages("custom-open-function")
    def visit_call(self, node):
        if node.func.as_string() == "open":
            self.add_message("custom-open-function", node=node)


class CustomDropnaChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-dropna-checker"

    def visit_call(self, node):
        func_name = node.func.as_string()
        if func_name == "DROPNA":
            self.add_message("custom-dropna", node=node, args="Avoid using 'DROPNA'. Use more appropriate function names.")

class CustomCodeChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)

    name = "custom-code-checker"

    def visit_call(self, node):
        func_name = node.func.as_string()
        custom_messages = {
            "ARANGE": "Avoid using 'ARANGE'. Use 'range' or 'numpy.arange' instead.",
            "DROPNA": "Consider handling missing data more explicitly. Avoid using 'DROPNA'.",
            "ZEROS_ONES": "Avoid using 'ZEROS_ONES'. Use 'numpy.zeros' or 'numpy.ones' instead.",
            "MERGE": "Avoid using 'MERGE'. Use 'pandas.merge' instead.",
            "HEAD_TAIL": "Avoid using 'HEAD_TAIL'. Use more descriptive names.",
            "APPLY": "Avoid using 'APPLY'. Use more descriptive function names."
        }

        if func_name in custom_messages:
            self.add_message("custom-code", node=node, args=custom_messages[func_name])

    def visit_tryfinally(self, node):
        self.add_message("custom-finally", node=node, args="Avoid using 'finally' blocks. Consider alternative solutions.")

    def visit_import(self, node):
        imported_module = node.names[0].name
        if imported_module == "requests":
            self.add_message("custom-import-requests", node=node, args="Be cautious when using 'requests' for making HTTP requests. Use it responsibly.")
    
    def visit_assign(self, node):
        if isinstance(node.value, ast.Str):
            variable_name = node.target.name
            value = node.value.s
            if "MAGIC_NUMBER" in value:
                self.add_message("custom-magic-number", node=node, args="Avoid using 'MAGIC_NUMBER'. Use named constants instead.")




def register(linter):
    linter.register_checker(CustomFlaskDebugChecker(linter))
    linter.register_checker(CustomEvalChecker(linter))
    linter.register_checker(CustomWeakHashChecker(linter))
    linter.register_checker(CustomCredentialsChecker(linter))
    linter.register_checker(CustomExecChecker(linter))
    linter.register_checker(CustomOpenChecker(linter))
    linter.register_checker(CustomDropnaChecker(linter))
    linter.register_checker(CustomCodeChecker(linter))
