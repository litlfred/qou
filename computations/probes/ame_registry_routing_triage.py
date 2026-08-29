#!/usr/bin/env python3
"""Triage AME-literal → codata_constants registry routes: SAFE (byte-exact) vs UNSAFE.

Bean fvxq ("route remaining inline mass literals through the codata_constants
registry"). The atomic-mass registry exports landed on main (PR-#539b82f125:
`M_*_ATOMIC_MEV_VALIDATION`, `AME_B_*_MEV_VALIDATION`). The remaining inline-literal
tail is NOT a uniform mechanical sweep: the registry's canonical value strings differ
at the last digit(s) from many corpus literals. Routing a mismatched literal would
SILENTLY CHANGE the value — a value-preservation violation.

  ⚠ THE REGISTRY MOVED AGAIN AFTER THIS SCRIPT WAS WRITTEN. This docstring used to
  cite `AME_B_HE4 = 28.295673` and deuteron `2.224566`. Commit 03c25e8db ("the
  canonical binding reference was hand-typed and 7 of 11 were wrong", owner: "ame
  data is in corpus") switched `_ame_binding_mev` from `binding_energy_total_keV`
  — derived, and computed in float64 by vendor_ame2020.py — to the quoted
  `binding_energy_per_A_keV` column. The canonical values today are
  `AME_B_HE4 = 28.2956624` and deuteron `2.2245662`, so the corpus literals that
  were byte-exact BEFORE that commit are now in the UNSAFE class. The SAFE/UNSAFE
  split below is computed from `dir(codata_constants)` at runtime and is therefore
  always current; only this prose had gone stale.

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

# Fraction bounded at 15 digits ON PURPOSE. A hand-typed AME literal is at
# most ~12 significant figures (the widest registry value is
# 938.78307479441, 11 decimals). An unbounded pattern also matched
# witness_float64_padding_audit.py's own self-test fixture --
#   "8.4817962000000015621026250300928950309753417968750000000000"
# -- which is a padded-float64 EXAMPLE, not a literal anyone typed. The
# triage then wrote it into its own witness, where the padding audit
# correctly flagged it: a roadmap reporting the example of a bug as an
# instance of a different bug.
_NUMONLY = re.compile(r'^\d{1,5}\.\d{3,15}$')


def _literals(txt: str):
    """Yield every AME-range literal that is CODE, via tokenize.

    The regex this replaced scanned raw text, so a value written in a comment
    or a docstring counted as a routable site. That inflates both halves of
    the roadmap: prose is not work. tokenize separates them exactly --
      COMMENT           -> skip, always prose
      STRING            -> keep ONLY if the whole string is the number, which
                           is the `mp.mpf("8.4817962")` form; anything else is
                           prose that happens to contain digits
      NUMBER            -> keep, a bare literal
    """
    import io
    import tokenize as _tk
    try:
        toks = list(_tk.generate_tokens(io.StringIO(txt).readline))
    except (_tk.TokenError, IndentationError, SyntaxError):
        return
    for t in toks:
        if t.type == _tk.COMMENT:
            continue
        if t.type == _tk.STRING:
            body = t.string.strip("\"'")
            if _NUMONLY.match(body):
                yield body
        elif t.type == _tk.NUMBER:
            if _NUMONLY.match(t.string):
                yield t.string


def _in_range(v: float) -> bool:
    return (1.5 < v < 45) or (1800 < v < 12000)   # AME binding MeV or atomic-mass MeV


def main() -> int:
    # rglob, NOT glob. This used to scan `computations/*.py` only, with a
    # comment reasoning that substrate/ is a subdir and therefore excluded --
    # but that also hid probes/, deltalambda/, phase5/ and sweeps/, which is
    # where most of the tail actually lives. Same defect the q0 manifest had:
    # "the producer lookup was root-only, so half the corpus was invisible".
    files = [q for q in HERE.parent.rglob("*.py")
             if "_deprecated" not in q.parts and "_internal" not in q.parts
             and q.name != "codata_constants.py"]
    safe: dict[str, set] = {}
    unsafe: dict[str, set] = {}
    for p in files:
        fn = p.name
        txt = p.read_text(encoding="utf-8")
        for lit in _literals(txt):
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
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"\n  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
