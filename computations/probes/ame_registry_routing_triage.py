#!/usr/bin/env python3
"""Triage AME-literal → codata_constants registry routes: SAFE (byte-exact) vs UNSAFE.

Bean fvxq ("route remaining inline mass literals through the codata_constants
registry"). The atomic-mass registry exports landed on main (PR-#539b82f125:
`M_*_ATOMIC_MEV_VALIDATION`, `AME_B_*_MEV_VALIDATION`). The remaining inline-literal
tail is NOT a uniform mechanical sweep: the registry's canonical value strings differ
at the last digit(s) from many corpus literals (e.g. registry `AME_B_HE4 = 28.295673`
vs the corpus-ubiquitous `28.295674`; deuteron `2.224566` vs `2.22456607` /
`2.22456612`). Routing a mismatched literal would SILENTLY CHANGE the value — a
value-preservation violation.

This script classifies every AME-range decimal literal in `computations/*.py`
(excluding `_deprecated/` and the registry module itself) as:

  • SAFE   — the literal STRING exactly equals a registry value string ⇒ routing is
             value-preserving (`mp.mpf("8.481798")` → `AME_B_TRITIUM_MEV_VALIDATION`).
  • UNSAFE — within ~5e-6 relative of a registry value but NOT byte-exact ⇒ routing
             would change the value; needs a value-reconciliation decision (is the
             registry value canonical, or is the corpus literal? owner/sibling call),
             NOT a mechanical route.

Pure string/value comparison — no compute deps, runs anywhere. This is the routing
roadmap for the fvxq tail; the SAFE list is the value-preserving work, the UNSAFE
list is the decisions that must precede routing.

Output: ame-registry-routing-triage.witness.json
"""
from __future__ import annotations

import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "substrate"))
import codata_constants as c  # noqa: E402

# Registry value-string → export-name (atomic masses + AME binding energies).
REG = {}
for nm in dir(c):
    if nm.endswith("_VALIDATION") and ("ATOMIC" in nm or "AME_B" in nm):
        try:
            REG[str(c.__dict__[nm])] = nm
        except Exception:
            pass

_LIT = re.compile(r'"(\d{1,5}\.\d{3,})"|mp\.mpf\("(\d{1,5}\.\d{3,})"\)|(?<![\w.])(\d{1,5}\.\d{4,})(?![\w.])')


def _in_range(v: float) -> bool:
    return (1.5 < v < 45) or (1800 < v < 12000)   # AME binding MeV or atomic-mass MeV


def main() -> int:
    files = [f for f in glob.glob("computations/*.py")
             if "_deprecated" not in f and "substrate/" not in f]
    safe: dict[str, set] = {}
    unsafe: dict[str, set] = {}
    for f in files:
        fn = f.split("/")[-1]
        txt = Path(f).read_text()
        for m in _LIT.finditer(txt):
            lit = m.group(1) or m.group(2) or m.group(3)
            if lit is None:
                continue
            v = float(lit)
            if not _in_range(v):
                continue
            if lit in REG:
                safe.setdefault(fn, set()).add((lit, REG[lit]))
            else:
                for rs, nm in REG.items():
                    if abs(v - float(rs)) / float(rs) < 5e-6:
                        unsafe.setdefault(fn, set()).add((lit, nm, rs))
                        break

    n_safe_routes = sum(len(v) for v in safe.values())
    n_unsafe = sum(len(v) for v in unsafe.values())
    print(f"AME-literal → registry routing triage")
    print(f"  registry value strings: {len(REG)}")
    print(f"  SAFE (byte-exact, value-preserving): {n_safe_routes} routes in {len(safe)} files")
    print(f"  UNSAFE (near, value-change — decision needed): {n_unsafe} in {len(unsafe)} files")
    print(f"\n  SAFE files (route value-preservingly):")
    for fn in sorted(safe):
        print(f"    {fn:46} {sorted(l for l, _ in safe[fn])}")

    witness = {
        "computation": "ame-registry-routing-triage",
        "kind": "infrastructure-triage",
        "description": (
            "Classifies inline AME-range literals in computations/*.py as SAFE "
            "(byte-exact to a codata_constants registry export → value-preserving "
            "route) vs UNSAFE (near but not exact → routing changes the value). The "
            "registry's last-digit conventions differ from many corpus literals, so "
            "the fvxq tail is not a uniform sweep. SAFE = the routing work; UNSAFE = "
            "value-reconciliation decisions that must precede any route."
        ),
        "registry_value_strings": REG,
        "safe_routes": {fn: sorted([list(t) for t in v]) for fn, v in sorted(safe.items())},
        "unsafe_near_matches": {fn: sorted([list(t) for t in v]) for fn, v in sorted(unsafe.items())},
        "counts": {"safe_routes": n_safe_routes, "safe_files": len(safe),
                   "unsafe_near_matches": n_unsafe, "unsafe_files": len(unsafe)},
        "note": ("Routing + per-file run-verification (the fvxq value-preservation "
                 "discipline) is infra-gated in some sandboxes: many target files import "
                 "pyhecke_native (buildable, ~42s) or have pre-existing runtime errors. "
                 "This triage (pure string compare) runs anywhere and is the roadmap."),
        "bean": "fvxq", "sibling": "claude/fvxq-atomic-mass-registry-2026-06-21",
    }
    out = HERE.parent / "ame-registry-routing-triage.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\n  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
