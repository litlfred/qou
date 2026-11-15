#!/usr/bin/env python3
"""The set of files git tracks — so a ratchet counts the CORPUS, not the disk.

WHY THIS EXISTS
---------------
`y_lambda_conflation_audit`'s check D walked the tree and counted every
`*.witness.json` it found. Several of those are **gitignored** local caches
(`.gitignore:230` covers `computations/chi-*-at-q<8 hex>-50dps.witness.json`),
so the ratchet counted files no other machine has: it read 55 when the audit
was written, 56 an hour after a sibling regenerated one chi cache, and would
read something else again in CI. A ratchet whose number depends on which
producers you happen to have run is not a gate — it is red for whoever ran the
producer last and green everywhere else, which is the "checker goes quiet"
failure `scripts/precision-gates.sh` warns about, reached through
nondeterminism rather than neglect. Seven of that baseline's 55 entries turned
out to be untracked caches.

WHY IT IS SHARED RATHER THAN COPIED
-----------------------------------
The session that found this had just spent its length on
`intra_ordering_structural_assembly_audit`, whose whole subject is a one-line
helper the corpus transcribed a dozen times instead of calling. Copying this
into the second audit would have been the same mistake in the same hour.

THE PATH-JOIN THAT MAKES IT SUBTLE
----------------------------------
`git -C <subdir> ls-files` prints paths relative to **<subdir>**, not to the
repo root. The first attempt joined those onto the repo root, matched almost
nothing, and reported check D as 0 with "drained: 55" — a clean sweep that was
really a filter excluding the entire corpus, one `--rebaseline` away from
zeroing a live ratchet. Hence `--full-name` (paths from the repo root),
`rev-parse --show-toplevel` for the base, and the self-membership assertion
below: a filter that excludes everything must fail LOUDLY, never read as clean.
"""
from __future__ import annotations

import os
import subprocess
import sys

_UNSET = object()
_CACHE: dict[str, object] = {}


def tracked_files(anchor: str, *, verify: str | None = None) -> set[str] | None:
    """Absolute paths git tracks in `anchor`'s repo, or None if undeterminable.

    `anchor`   any path inside the checkout (a directory or a file).
    `verify`   a path the caller KNOWS is tracked, usually its own `__file__`.
               If it is missing from the result the paths did not line up, and
               this returns None with a warning rather than a filter that
               silently drops everything.

    Callers treat None as "scan everything, and say so" — degrading to the
    unfiltered behaviour loudly beats scanning nothing quietly.
    """
    anchor = os.path.abspath(anchor)
    base = anchor if os.path.isdir(anchor) else os.path.dirname(anchor)
    key = f"{base}\0{verify or ''}"
    if key in _CACHE:
        got = _CACHE[key]
        return None if got is _UNSET else got            # type: ignore[return-value]

    result: set[str] | None
    try:
        top = subprocess.run(
            ["git", "-C", base, "rev-parse", "--show-toplevel"],
            capture_output=True, check=True, timeout=60,
        ).stdout.decode("utf-8", "replace").strip()
        #: LIST FROM `top`, NOT FROM `base`. `git ls-files` restricts its
        #: listing to the CURRENT DIRECTORY's subtree, and `--full-name` only
        #: changes how the paths are spelled, not which ones are listed. Run
        #: from `computations/audits` it returned 260 entries — that directory
        #: alone — so every source outside it read as untracked and the caller
        #: filtered its whole corpus away. This is the SECOND time that
        #: collapse happened while writing this helper (the first was a bad
        #: path join), which is why `verify` exists and why it must name a file
        #: OUTSIDE the anchor directory to be worth anything.
        out = subprocess.run(
            ["git", "-C", top, "ls-files", "-z", "--full-name"],
            capture_output=True, check=True, timeout=60,
        ).stdout.decode("utf-8", "replace")
        result = ({os.path.join(top, p) for p in out.split("\0") if p}
                  if top else None)
    except (OSError, subprocess.SubprocessError):
        result = None

    if result is not None and verify is not None:
        if os.path.abspath(verify) not in result:
            print(f"  ⚠ tracked-path resolution failed ({len(result)} entries, "
                  f"{os.path.basename(verify)} absent) — scanning the working "
                  f"directory instead", file=sys.stderr)
            result = None

    _CACHE[key] = _UNSET if result is None else result
    return result
