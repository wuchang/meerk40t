class KernelError(Exception):
    pass


class KernelImportAbort(ImportError, KernelError):
    """
    MkImportAbort should be used as follows in plugins that import an optional prerequisite Pypi package:

    try:
        import wx
    except ImportError as e:
        raise Mk40tImportAbort("wx") from e
    """


class CommandMatchRejected(Exception):
    """
    Exception to be raised by a registered console command if the match to the command was erroneous
    """


class MalformedCommandRegistration(Exception):
    """
    Exception raised by the Kernel if the registration of the console command is malformed.
    """
