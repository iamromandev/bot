import sys

from typing import Optional, List, Any


def main(sysargv: Optional[List[str]] = None) -> None:
    return_code: Any = 1
    try:
        print("Lal Lal")
    except Exception:
        pass
    finally:
        sys.exit(1)
    pass
