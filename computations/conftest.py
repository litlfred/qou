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

They were not failing, they were never being collected, which is the quieter
and worse failure. Adding this file fixes them at once: pytest imports
`conftest.py` before any test module, so the insertion below happens first.

**The population, re-measured 2026-10-12 — and this docstring's own figure
was wrong by a naming convention.** It read *"59 of the 86 test files"*, and
a 2026-08-19 triage (PR #5330) "corrected" that to *"47 test files repo-wide,
24 under `computations/`"*. Both counted only `test_*.py`. This tree uses
**both** conventions, and `*_test.py` is the larger half here:

    repo-wide   test_*.py  60   *_test.py  42   combined  102
    computations/                                combined   64

So every figure ever quoted for this file undercounts, and the "correction"
undercut it further. Measure with
`find . \( -name 'test_*.py' -o -name '*_test.py' \)`.

**What a run actually gives, measured 2026-10-12 — the first one on record.**
`python3 -m pytest computations/ --collect-only` collects **100 tests** and
reports **9 collection errors**, none of them a corpus defect: 7 need
`pyhecke_native` (not on PyPI, built with maturin, so absent in a default
container), 1 needs `snappy`, and 1 — `ptolemy/test_guard_rejects_spurious.py`
— opens a data file at import time that has never existed in this repo. See
`docs/audits/2026-10-12-first-pytest-run.md`.

Kept deliberately minimal — path setup only, no fixtures — so it does not
become a place where test behaviour hides.
"""

import sys
from pathlib import Path

_HERE = Path(__file__).parent.resolve()

if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
