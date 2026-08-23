#!/usr/bin/env python3
"""Compare the INSTALLED pyhecke_native against the Rust source that declares it.

WHY THIS EXISTS
---------------
A compiled wheel is a derived artifact like any other, and it fails the same way
the vendored qou-mass mirror does: the source moves, the copy does not, and the
copy answers with yesterday's code under today's authority. It is worse here,
because nothing about a stale wheel looks stale — it imports, it runs, it
returns numbers.

The measured instance (bean qou-nm6y). The container carried a wheel built
2026-08-09. `gram_inverse` was DELETED from the source on 2026-08-15, and
deliberately: tools/pyhecke-native/src/lib.rs:53 records that with the correct
TR_M[5] the Markov-Gram form is singular under convention D, so a 6x6 inverse
does not exist, and "Python callers of pyhecke_native.gram_inverse now get
AttributeError, which is the intended outcome."

The stale wheel still exported it. So
computations/delta_lambda_full_variance_phase5e_1.py called a function the
source had removed, received a 6x6 "inverse" of a matrix that has none, and
wrote 37 float64 values into its witness. Its try/except — written to catch
exactly the AttributeError a correct build raises — never fired. Twelve
native-backed witnesses were regenerated against that wheel before the gap was
found, and each had to be reverted.

WHAT IT CHECKS
--------------
Every export is registered in one place, the `#[pymodule]` block of
tools/pyhecke-native/src/lib.rs. That block is the authority; `dir()` on the
installed module is the observation. Two directions, and they are NOT
symmetric:

  installed but NOT in source   BLOCKING. A build cannot invent an export, so
                                the only way to see one the source does not
                                declare is a wheel that predates its deletion.
                                This is the gram_inverse case, and it is the
                                dangerous direction: the call SUCCEEDS and
                                returns a wrong number.

  in source but NOT installed   ADVISORY. Ambiguous — a wheel predating an
                                addition looks identical to a feature that did
                                not compile in. `operator_selection_lp` is
                                gated on `clarabel-lp`, whose backend needs the
                                litlfred Clarabel.rs fork (egress-blocked in
                                restricted sandboxes, see
                                .github/workflows/pyhecke-native-wheel.yml), so
                                it is legitimately absent here. Reported with
                                its gate named, never as a failure. A missing
                                UNGATED export is still only advisory: the
                                failure mode is AttributeError, which is loud.

EXIT CODE (--check)
  0  no installed export is undeclared in source  (or the module isn't installed)
  1  at least one is — the wheel is stale, REBUILD BEFORE REGENERATING ANY
     NATIVE-BACKED WITNESS:  bash scripts/build-pyhecke-native.sh

Not installed is not staleness. Producers already guard their imports, and the
native module is optional in several environments, so a missing module exits 0
with a line saying so rather than reddening a gate it cannot evaluate.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB_RS = ROOT / "tools" / "pyhecke-native" / "src" / "lib.rs"

# `m.add_function(wrap_pyfunction!(NAME, m)?)?;` — the registration form used
# for every export. Matched inside the #[pymodule] block only.
_REGISTER_RX = re.compile(r"wrap_pyfunction!\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*,")
_CFG_FEATURE_RX = re.compile(r'#\[cfg\(feature\s*=\s*"([^"]+)"\)\]')
_PYMODULE_RX = re.compile(r"#\[pymodule\]")


def declared_exports(lib_rs: Path) -> dict[str, str | None]:
    """Map export name -> the feature gating it, or None if unconditional.

    Scans forward from `#[pymodule]` to the closing brace at column 0. A
    `#[cfg(feature = "x")]` binds only the single registration line following
    it, which is how lib.rs uses it (one gate, on operator_selection_lp).
    """
    lines = lib_rs.read_text().splitlines()
    start = next(
        (i for i, ln in enumerate(lines) if _PYMODULE_RX.search(ln)), None)
    if start is None:
        raise SystemExit(
            f"no #[pymodule] block in {lib_rs} — the export list cannot be "
            f"read, so staleness cannot be judged")

    exports: dict[str, str | None] = {}
    pending_feature: str | None = None
    for ln in lines[start:]:
        if ln.startswith("}"):          # end of the #[pymodule] fn body
            break
        m_cfg = _CFG_FEATURE_RX.search(ln)
        if m_cfg:
            pending_feature = m_cfg.group(1)
            continue
        m_reg = _REGISTER_RX.search(ln)
        if m_reg:
            exports[m_reg.group(1)] = pending_feature
        pending_feature = None
    return exports


def installed_exports() -> tuple[list[str], str, str] | None:
    try:
        import pyhecke_native as native
    except ImportError:
        return None
    names = sorted(
        n for n in dir(native)
        if not n.startswith("_") and callable(getattr(native, n, None))
    )
    return (names,
            getattr(native, "__version__", "?"),
            getattr(native, "__file__", "?"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the installed wheel exports anything the "
                         "source no longer declares")
    args = ap.parse_args()

    declared = declared_exports(LIB_RS)
    got = installed_exports()

    print("pyhecke-native wheel staleness")
    print(f"  source:    {LIB_RS.relative_to(ROOT)}  "
          f"({len(declared)} registered exports)")

    if got is None:
        print("  installed: NOT IMPORTABLE — nothing to compare, gate skipped.")
        print("  (the native module is optional; producers guard their imports)")
        return 0

    names, version, path = got
    print(f"  installed: {path}")
    print(f"             version {version}, {len(names)} callable exports")
    print()

    undeclared = [n for n in names if n not in declared]
    missing = [n for n in declared if n not in names]

    if undeclared:
        print(f"  ✗ STALE WHEEL — {len(undeclared)} export(s) the source does "
              f"not declare:")
        for n in undeclared:
            print(f"      {n}")
        print()
        print("    A build cannot invent an export. This wheel predates the")
        print("    deletion of the name(s) above, so a call that SHOULD raise")
        print("    AttributeError instead returns a number computed by code")
        print("    the repository has removed.")
        print()
        print("    Rebuild before regenerating ANY native-backed witness:")
        print("        bash scripts/build-pyhecke-native.sh")
    else:
        print("  ✓ every installed export is declared in source")

    if missing:
        gated = [(n, f) for n, f in ((n, declared[n]) for n in missing) if f]
        ungated = [n for n in missing if not declared[n]]
        print()
        if gated:
            print(f"  · {len(gated)} declared export(s) absent, feature-gated "
                  f"(expected when the feature did not compile in):")
            for n, feat in gated:
                print(f"      {n}  [feature: {feat}]")
        if ungated:
            print(f"  ⚠ {len(ungated)} declared export(s) absent and NOT "
                  f"feature-gated — wheel may predate their addition:")
            for n in ungated:
                print(f"      {n}")
            print("    Advisory only: the failure mode is AttributeError, "
                  "which is loud.")

    if args.check and undeclared:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
