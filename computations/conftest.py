"""pytest bootstrap for `computations/`.

Every test module here starts with `import _path_bridge` (the Phase-6 shim
that puts `substrate/` on the path), and the probe modules they exercise
import their siblings by bare name — `q_parameter`, `_precision`,
`wedderburn_jones_markov`, and so on. That works when a script is run
directly from this directory, because Python puts the script's own
directory on `sys.path`.

Under pytest it did not. With no `conftest.py` and no pytest config
anywhere in the repo, `computations/` never reached `sys.path`, so
collection died on the very first import:

    ModuleNotFoundError: No module named '_path_bridge'

That took out **59 of the 86 test files** — they were not failing, they
were never being collected, which is the quieter and worse failure. Adding
this file fixes all of them at once: pytest imports `conftest.py` before
any test module, so the insertion below happens first.

Kept deliberately minimal — path setup only, no fixtures — so it does not
become a place where test behaviour hides.
"""

import sys
from pathlib import Path

_HERE = Path(__file__).parent.resolve()

if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
