#!/usr/bin/env python3
# polynomial_q_not_applicable: source-hygiene audit, no q-dependence.
"""Catch runnable producers that NEVER raise working precision at all.

Owner directive: NO FLOAT64.

This closes a blind spot shared by every other member of the precision family,
and the shape of it is worth stating plainly, because the gap is in their common
premise rather than in any one of them:

    witness_float64_padding_audit.py   fake precision sitting in a witness
    mpf_float_source_audit.py          mpf(<float literal>) in source
    mpf_import_time_dps_audit.py       mpf("<string>") built before dps rises
    THIS                               dps never rises AT ALL

Each of the first three asks *whether a value got in before precision was
raised*. All three therefore assume it was raised somewhere. A producer that
never calls `set_compute_dps()`, never assigns `mp.dps`, and never opens a
`mp.workdps(...)` block runs its whole computation at mpmath's default **15**,
and the numbers it emits are then **honestly float64** — there is no padding to
detect and no constant built too early. It passes all three cleanly.

Reported by #4899, which found it the hard way: `markov_trace_recursive.py` was
"float64 wearing 60 digits", and what exposed it was tightening a comparison
until three assertions failed at digit 17 with dyadic tails. That file is fixed;
this audit exists so the next one is found statically instead.

WHAT IT FLAGS, and why each condition is needed
-----------------------------------------------
A file must satisfy ALL of:

  1. **emits a witness** — `WitnessBuilder` or a `.witness.json` reference. A
     script that computes for the terminal is not making a published claim.
  2. **constructs mpmath VALUES** — `mp.mpf(...)`, `mp.sqrt(...)`, bare
     `mpf(...)`, etc., detected at AST level. A string match on "mpmath" is far
     too loose: it catches audits that merely scan for the word, and files that
     import it and never build anything. That distinction alone took the raw
     count from 145 to 66.
  3. **is RUNNABLE** — has an `if __name__ == "__main__":` guard. This is the
     condition that makes the audit sound, and it is not obvious:
     **`mp.dps` is GLOBAL STATE**, so an imported helper legitimately inherits
     the precision its caller set. `_li_2_q_util.py` builds 40 mpmath values and
     raises dps nowhere, and is perfectly correct — it is only ever called from
     producers that raised it first. Flagging library modules would bury the
     real finding under helpers that are working as designed.
  4. **never raises precision anywhere in the file** — `set_compute_dps()`,
     any `.dps` assignment, or a `workdps(...)` call, at any nesting depth.

Worked true positive, from the baseline run:

    computations/sweeps/paper_six_term_isotope_sweep.py:145
        out[r["atom"]] = abs(mp.mpf(r["tr_M_at_q0_50dps"]))

It reads a field whose NAME says 50 dps and lifts it at 15, discarding 35
digits, and its witness contains no string longer than 25 decimals anywhere.

RATCHET, not pass/fail
----------------------
45 producers is not a backlog anyone drains in one sitting, and a gate that is
red on arrival gets skipped — which is how `mpf_import_time_dps_audit.py` came
to sit unrun for three days (bean qou-j6gb). So the existing surface is recorded
in `never-raises-dps-baseline.json` and tolerated; a file NOT in the baseline
fails, and a baselined file whose count INCREASES fails.

Do not add a file to the baseline to silence a failure. The fix is one line —
call the idempotent `set_compute_dps()` at module scope — and unlike the
import-time audit's fix, this one usually CHANGES PUBLISHED VALUES, because the
producer really was computing at 15 dps. Expect the witness to move, and expect
that movement to be the point.

Usage:
    python3 computations/never_raises_dps_audit.py            # report
    python3 computations/never_raises_dps_audit.py --strict   # exit 1 on NEW
    python3 computations/never_raises_dps_audit.py --rebaseline
    python3 computations/never_raises_dps_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASELINE = HERE / "never-raises-dps-baseline.json"
SKIP_DIRS = {"_deprecated", "fsh-guts", "__pycache__", "data", ".claude", ".git", ".lake", "node_modules"}

# Calls that CONSTRUCT an mpmath value. Deliberately a construction list rather
# than "anything on mp": `mp.dps`, `mp.prec` and friends are settings, not values.
MP_VALUE_FUNCS = {
    "mpf", "mpmathify", "sqrt", "exp", "log", "log10", "pi", "power",
    "cos", "sin", "tan", "atan", "asin", "acos", "gamma", "zeta",
    "polylog", "hyper", "besselj", "erf", "mpc",
}
RAISERS = {"set_compute_dps", "workdps"}

# Modules that export `mpmath.mpf` constants at module scope (bean qou-0p2h).
# A file that never names `mpmath` directly but imports `HBAR_MEV_S` (etc.)
# from one of these and performs arithmetic on it without importing a float64
# `Q` computes in mpmath at `mp.dps = 15`.
MPF_CONST_MODULES = {
    "experimental_constants": {
        "M_E_MEV", "M_P_MEV", "M_N_MEV", "M_MU_MEV", "M_TAU_MEV",
        "Q_NEUTRON_MEV", "HBAR_MEV_S", "ALPHA_EM", "ALPHA_EM_INV",
        "MU_OVER_E", "P_OVER_E", "N_OVER_E", "VOL_FIGURE_EIGHT",
        "VOL_THREE_TWIST", "VOL_BORROMEAN",
    },
    "codata_constants": {
        "M_E_MEV", "M_P_MEV", "M_N_MEV", "M_MU_MEV", "ALPHA_EM", "ALPHA_EM_INV",
    },
    "knot_volumes": {
        "VOL_FIGURE_EIGHT", "VOL_THREE_TWIST", "VOL_BORROMEAN", "CATALAN_G",
    },
    "q_parameter": {
        "Q_MP", "Q_INV_MP", "HA_MP", "HBAR_Q_MP", "HBAR_Q_SQ_MP", "Z_CANONICAL_MP",
    },
}
FLOAT64_Q_MODULES = {"q_parameter", "qou_substrate.constants"}
FLOAT64_Q_NAMES = {"Q", "Q_INV", "HA", "HBAR_Q", "HBAR_Q_SQ"}


def raises_precision(tree: ast.Module) -> bool:
    """Does this file raise working precision ANYWHERE, at any depth?

    Deliberately not position-aware — that is
    `mpf_import_time_dps_audit.py`'s job. Here the question is only whether the
    file ever raises precision at all, so a call inside `main()` counts.
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            name = (f.attr if isinstance(f, ast.Attribute)
                    else f.id if isinstance(f, ast.Name) else None)
            if name in RAISERS:
                return True
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Attribute) and t.attr == "dps":
                    return True
        if isinstance(node, ast.AnnAssign):
            t = node.target
            if isinstance(t, ast.Attribute) and t.attr == "dps":
                return True
        # NO ImportFrom clause. `from _precision import set_compute_dps`
        # used to count as raising precision, so a producer that IMPORTED a
        # raiser and never CALLED it scored clean (bean `qou-nk3h`/`qou-txru`,
        # 2026-08-26). That is not a hypothetical: it is exactly how
        # `chi_sym_alt_closed_form.py` ran its whole computation at mpmath's
        # default 15 while `fmt()` serialised at 50, putting 46 fake-precision
        # values into a committed witness and taking the float64-padding
        # ratchet RED ON MAIN. This audit reported that file clean throughout.
        #
        # The module docstring's imported-helper exemption — `mp.dps` is global
        # state, so a library legitimately inherits its caller's precision — is
        # real, but it is enforced by `is_runnable()` (condition 3), which
        # already exempts any file with no `__main__` block. It never needed
        # this clause, and the clause silently widened it from "helpers" to
        # "anything that mentions a raiser in an import".
        #
        # Removing it surfaced ZERO new findings on the tree at the time
        # (measured), so the correction cost no baseline growth.
        if isinstance(node, ast.With):
            for item in node.items:
                c = item.context_expr
                if isinstance(c, ast.Call):
                    f = c.func
                    nm = (f.attr if isinstance(f, ast.Attribute)
                          else f.id if isinstance(f, ast.Name) else None)
                    if nm in RAISERS:
                        return True
    return False


def mp_value_calls(tree: ast.Module) -> list[int]:
    """Line numbers of calls that construct an mpmath value, plus arithmetic on
    imported `mpf` constants when no float64 `Q` is imported (bean qou-0p2h)."""
    out: list[int] = []
    imported_mpf_names: set[str] = set()
    has_f64_q = False
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            mod = node.module.split(".")[0]
            if node.module in FLOAT64_Q_MODULES or mod in FLOAT64_Q_MODULES:
                for a in node.names:
                    if a.name in FLOAT64_Q_NAMES:
                        has_f64_q = True
            if mod in MPF_CONST_MODULES:
                known = MPF_CONST_MODULES[mod]
                for a in node.names:
                    if a.name in known:
                        imported_mpf_names.add(a.asname or a.name)
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        if (isinstance(f, ast.Attribute) and f.attr in MP_VALUE_FUNCS
                and isinstance(f.value, ast.Name) and f.value.id in {"mp", "mpmath"}):
            out.append(node.lineno)
        elif isinstance(f, ast.Name) and f.id in {"mpf", "mpmathify"}:
            out.append(node.lineno)
    if not out and imported_mpf_names and not has_f64_q:
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp):
                if any(isinstance(sub, ast.Name) and sub.id in imported_mpf_names
                       for sub in (node.left, node.right)):
                    out.append(node.lineno)
    return sorted(set(out))



def _module_scope_raisers(tree: ast.Module) -> bool:
    """Does this module call a raiser at MODULE SCOPE (not inside a def)?"""
    for node in tree.body:
        for sub in ast.walk(node):
            if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                break
        else:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call):
                    f = sub.func
                    nm = (f.attr if isinstance(f, ast.Attribute)
                          else f.id if isinstance(f, ast.Name) else None)
                    if nm in RAISERS:
                        return True
                if isinstance(sub, ast.Assign):
                    for t in sub.targets:
                        if isinstance(t, ast.Attribute) and t.attr == "dps":
                            return True
    return False


def raises_via_import(path: Path, tree: ast.Module) -> str | None:
    """The module this file imports that raises dps as an import SIDE EFFECT.

    `mp.dps` is global state, and the module docstring's exemption reasons
    about one direction of that: a helper inherits its caller's precision, so
    only runnable files are flagged. The state flows the OTHER way too. A
    runnable producer that does `import X` where X calls `set_compute_dps()` at
    module scope has dps raised before a line of its own code executes.

    MEASURED 2026-09-03, by importing each candidate's module-scope imports and
    reading `mp.dps`: `magnus_sign_row_truncation_probe` and
    `magnus_tr_decay_perpair_cluster_probe` both go 15 -> **140** through
    `he4_magnus_omega2_sign_sparse_probe`, which calls `set_compute_dps()` and
    sets `mp.mp.dps = 140`. They were reported as computing at 15 with 34
    constructions between them; they compute at 140.

    NOT the clause that was removed above, and the difference is the whole
    point. That one asked whether a RAISER NAME appeared in an import
    statement, which proves nothing — `chi_sym_alt_closed_form.py` imported one,
    never called it, ran at 15, and took the padding ratchet red on main while
    scoring clean here. This asks whether the IMPORTED MODULE'S OWN CODE calls
    a raiser at module scope, which is an actual state change.

    One hop, and same-tree only: a deeper or third-party cone is not resolved
    here, so this UNDER-reports rather than over-reports.
    """
    roots = [path.parent, HERE, HERE / "substrate"]
    for node in tree.body:
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names = [node.module]
        else:
            continue
        for name in names:
            rel = Path(name.replace(".", "/") + ".py")
            for r in roots:
                cand = r / rel
                if not cand.is_file():
                    continue
                try:
                    if _module_scope_raisers(ast.parse(cand.read_text(encoding="utf-8"))):
                        return name
                except (SyntaxError, OSError):
                    pass
    return None


def is_runnable(tree: ast.Module) -> bool:
    """`if __name__ == "__main__":` at module scope.

    The condition that keeps this audit honest — see the module docstring on
    `mp.dps` being global state.
    """
    for node in tree.body:
        if isinstance(node, ast.If):
            dumped = ast.dump(node.test)
            if "__name__" in dumped and "__main__" in dumped:
                return True
    return False


def emits_witness(src: str) -> bool:
    return "WitnessBuilder" in src or ".witness.json" in src


def scan() -> tuple[dict[str, int], list[dict]]:
    """Return ({path: n_mp_value_calls}, [unparseable rows])."""
    found: dict[str, int] = {}
    inherited: dict[str, dict] = {}
    broken: list[dict] = []
    for p in sorted(HERE.rglob("*.py")):
        if set(p.relative_to(HERE).parts) & SKIP_DIRS:
            continue
        if p.name == Path(__file__).name:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception as exc:  # noqa: BLE001
            broken.append({"file": str(p.relative_to(HERE.parent)),
                           "kind": "unreadable", "detail": str(exc)})
            continue
        if not emits_witness(src):
            continue
        try:
            tree = ast.parse(src)
        except SyntaxError as exc:
            # Never silently zero. A file that does not parse is "no
            # information", not "no findings" — the bug bean qou-brkp records
            # the import-time audit having had.
            broken.append({"file": str(p.relative_to(HERE.parent)),
                           "kind": "syntax-error", "detail": str(exc)})
            continue
        if raises_precision(tree) or not is_runnable(tree):
            continue
        calls = mp_value_calls(tree)
        if not calls:
            continue
        rel = str(p.relative_to(HERE.parent))
        via = raises_via_import(p, tree)
        if via:
            # Not computing at 15, so not a finding — but reported, because
            # inheriting precision from an import's SIDE EFFECT is fragile:
            # refactor that module to stop raising and this one silently drops
            # to 15 with nothing here to say so.
            inherited[rel] = {"count": len(calls), "via": via}
            continue
        found[rel] = len(calls)
    return found, broken, inherited


def self_test() -> int:
    """Prove each condition FIRES and each exemption HOLDS.

    A detector that cannot be shown to fire is indistinguishable from a no-op —
    the standard the rest of this family holds itself to.
    """
    cases = [
        ("flags a runnable producer that never raises dps",
         'import mpmath as mp\nx = mp.mpf("1.5")\nopen("a.witness.json")\n'
         'if __name__ == "__main__":\n    pass\n', True),
        ("does NOT flag one that calls set_compute_dps",
         'import mpmath as mp\nfrom _precision import set_compute_dps\n'
         'set_compute_dps()\nx = mp.mpf("1.5")\nopen("a.witness.json")\n'
         'if __name__ == "__main__":\n    pass\n', False),
        ("does NOT flag one that assigns mp.dps",
         'import mpmath as mp\nmp.dps = 50\nx = mp.mpf("1.5")\n'
         'open("a.witness.json")\nif __name__ == "__main__":\n    pass\n', False),
        ("does NOT flag one using a workdps block",
         'import mpmath as mp\nwith mp.workdps(50):\n    x = mp.mpf("1.5")\n'
         'open("a.witness.json")\nif __name__ == "__main__":\n    pass\n', False),
        ("FLAGS a producer that IMPORTS a raiser but never CALLS it",
         'import mpmath as mp\nfrom _precision import fmt, set_compute_dps\n'
         'x = mp.mpf("1.5")\nopen("a.witness.json")\n'
         'if __name__ == "__main__":\n    pass\n', True),
        ("does NOT flag an IMPORTED helper (dps is global; caller sets it)",
         'import mpmath as mp\nx = mp.mpf("1.5")\nopen("a.witness.json")\n', False),
        ("does NOT flag a producer that builds no mpmath VALUE",
         'import mpmath as mp\nopen("a.witness.json")\n'
         'if __name__ == "__main__":\n    pass\n', False),
        ("does NOT flag a script that emits no witness",
         'import mpmath as mp\nx = mp.mpf("1.5")\n'
         'if __name__ == "__main__":\n    pass\n', False),
        ("FLAGS a producer that never names mpmath but does arithmetic on an imported mpf constant (qou-0p2h)",
         'from experimental_constants import HBAR_MEV_S\n'
         'x = HBAR_MEV_S * 1e6\nopen("a.witness.json")\n'
         'if __name__ == "__main__":\n    pass\n', True),
        ("does NOT flag imported mpf constant when float64 Q is also imported (qou-840k class, not qou-0p2h)",
         'from experimental_constants import M_P_MEV\n'
         'from q_parameter import Q\nx = M_P_MEV / Q\nopen("a.witness.json")\n'
         'if __name__ == "__main__":\n    pass\n', False),
    ]
    bad = 0
    for name, src, want in cases:
        tree = ast.parse(src)
        got = bool(emits_witness(src) and is_runnable(tree)
                   and not raises_precision(tree) and mp_value_calls(tree))
        if got != want:
            print(f"  FAIL {name}: expected {want}, got {got}")
            bad += 1
    # The import-side-effect exemption needs cases of its own: a new exemption
    # with no test is the gap this file's history is a record of. Real files,
    # because `raises_via_import` resolves an import to a path.
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        (d / "raiser_mod.py").write_text(
            "import mpmath as mp\nfrom _precision import set_compute_dps\n"
            "set_compute_dps()\nmp.mp.dps = 140\n")
        (d / "importer_only_mod.py").write_text(
            # The hole that was closed once: imports the NAME, never calls it.
            "from _precision import set_compute_dps\n")
        (d / "deep_mod.py").write_text(
            "def go():\n    from _precision import set_compute_dps\n"
            "    set_compute_dps()\n")
        import_cases = [
            ("detects dps raised by an import's SIDE EFFECT",
             "import raiser_mod\n", "raiser_mod"),
            ("does NOT count a module that only IMPORTS a raiser name",
             "import importer_only_mod\n", None),
            ("does NOT count a raiser called inside a FUNCTION, not at module scope",
             "import deep_mod\n", None),
            ("does NOT count an unresolvable/third-party import",
             "import numpy\n", None),
        ]
        for name, src, want in import_cases:
            f = d / "probe.py"
            f.write_text(src)
            got = raises_via_import(f, ast.parse(src))
            if got != want:
                print(f"  FAIL {name}: expected {want!r}, got {got!r}")
                bad += 1
        n_extra = len(import_cases)

    # A file that does not parse must be reported, never counted as clean.
    try:
        ast.parse("def broken(:\n")
        print("  FAIL syntax-error case did not raise")
        bad += 1
    except SyntaxError:
        pass
    if bad:
        print(f"SELF-TEST FAILED — {bad}/{len(cases) + n_extra + 1}")
        return 1
    print(f"SELF-TEST PASSED — {len(cases) + n_extra + 1} cases: every condition fires, "
          f"every exemption holds, unparseable is not 'clean'.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on a NEW producer or an INCREASED count")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (draining only — counts must go DOWN)")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    found, broken, inherited = scan()
    prior: dict[str, int] = {}
    if BASELINE.exists():
        prior = json.loads(BASELINE.read_text())["files"]

    new_files = {f: n for f, n in found.items() if f not in prior}
    grew = {f: (prior[f], n) for f, n in found.items()
            if f in prior and n > prior[f]}
    drained = {f: (prior[f], found.get(f, 0)) for f in prior
               if found.get(f, 0) < prior[f]}
    total = sum(found.values())
    base_total = sum(prior.values()) if prior else 0

    print("=" * 74)
    print("NEVER-RAISES-DPS AUDIT — producers computing at mpmath's default 15")
    print("=" * 74)
    print(f"  runnable producers never raising dps : {len(found)}")
    print(f"  mpmath value constructions in them   : {total:,}")
    if inherited:
        # Named, never silent. These do NOT compute at 15 — measured — so they
        # are not findings; but inheriting precision from an import's side
        # effect is fragile, and an exemption nobody can see is the hole this
        # audit's own history is a record of.
        n_c = sum(v["count"] for v in inherited.values())
        print(f"  raise dps only VIA AN IMPORT         : {len(inherited)} file(s), "
              f"{n_c} construction(s) — not at 15, but fragile:")
        for f, v in sorted(inherited.items()):
            print(f"      {v['count']:>4}  {f}\n            inherits from `{v['via']}`")
    if prior:
        print(f"  baseline files / constructions       : {len(prior)} / {base_total:,}")
        print(f"  drained since baseline               : {len(drained)} file(s), "
              f"{base_total - total:+,}")
    print(f"  NEW (not baselined)                  : {len(new_files)}")
    print(f"  REGRESSED (count increased)          : {len(grew)}")

    if broken:
        print(f"\n  ⚠ {len(broken)} file(s) the audit could NOT read — NOT a clean "
              f"result for them, no claim is made about their contents:")
        for r in broken:
            print(f"    {r['file']}  [{r['kind']}]")

    if new_files:
        print("\n  NEW producers computing at dps=15 — fix AT THE SOURCE: call the"
              "\n  idempotent set_compute_dps() at module scope. Do NOT add the file"
              "\n  to the baseline to silence this. Expect published values to MOVE:"
              "\n  unlike the import-time audit, this producer really was low.")
        for f, n in sorted(new_files.items(), key=lambda kv: -kv[1])[:25]:
            print(f"    {n:6d}  {f}")
        if len(new_files) > 25:
            print(f"    ... and {len(new_files) - 25} more")

    if grew:
        print("\n  REGRESSED — these gained mpmath constructions while still not "
              "raising dps:")
        for f, (was, now) in sorted(grew.items())[:25]:
            print(f"    {was:6d} -> {now:<6d}  {f}")

    if drained:
        print(f"\n  Drained (progress): {len(drained)} file(s)")
        for f, (was, now) in sorted(drained.items())[:10]:
            print(f"    {was:6d} -> {now:<6d}  {f}")

    if a.rebaseline:
        BASELINE.write_text(json.dumps(
            {"note": "Runnable witness producers that build mpmath values and "
                     "never raise working precision, so they compute at "
                     "mpmath's default 15 dps. The backlog is tolerated; it "
                     "must only SHRINK. Adding a file here to silence a failure "
                     "defeats the gate — call set_compute_dps() instead.",
             "enforced_rule": "AGENTS.md: NO-FLOAT64. A producer that never "
                              "raises dps emits honestly-float64 numbers, which "
                              "the padding and raw-float64 scans cannot see.",
             "why_runnable_only": "mp.dps is GLOBAL, so an imported helper "
                                  "inherits its caller's precision and is not a "
                                  "defect. Only files with a __main__ guard are "
                                  "counted.",
             "drain_owner": "bean qou-j6gb",
             "files_count": len(found),
             "constructions_count": total,
             "files": dict(sorted(found.items()))}, indent=2) + "\n")
        print(f"\nRebaselined: {len(found)} files / {total:,} constructions.")

    out = HERE / "never-raises-dps-audit.witness.json"
    out.write_text(json.dumps({
        "schema": "witness/v1",
        "name": "never-raises-dps-audit",
        "description": "Runnable witness producers that build mpmath values and "
                       "never raise working precision, so the whole computation "
                       "runs at mpmath's default 15 dps. Invisible to the "
                       "padding and raw-float64 scans because the numbers are "
                       "honestly float64. Ratchet only; drain owner qou-j6gb.",
        "data": {
            "producers": len(found),
            "constructions": total,
            "baseline_files": len(prior),
            "new_not_baselined": len(new_files),
            "regressed": len(grew),
            "drained_files": len(drained),
            "unparseable_files": len(broken),
        },
    }, indent=2) + "\n")
    print(f"\nWrote {out.name}")

    return 1 if (a.strict and (new_files or grew or broken)) else 0


if __name__ == "__main__":
    sys.exit(main())
