#!/usr/bin/env python3
"""
LP-dual witness validator — first-class enforcement.

Walks every JSON witness under computations/ and
flags operator-selection / LP / SDP witnesses that lack required
LP-dual fields (per prop:operator-selection-lp § dual program).

Required fields (recursive search inside the witness JSON):
  - y0_star          shadow price of the net constraint
  - y_star           shadow prices of Frobenius positivity constraints
  - active_set       (or active_constraints / active_channels)
  - primal_obj       primal optimum value
  - dual_obj         dual optimum value (= n_target · y0_star)
  - duality_gap      |primal_obj - dual_obj|

Witness files are flagged when their filename or `description` /
`computation` field signals an LP/SDP/operator-selection compute.
This catches the failure mode that motivated this script: scripts
that solve the primal LP but never extract / report the dual,
losing the principled binding-energy interpretation.

Usage (CI):
    python3 computations/lp_dual_witness_validator.py
    → exit 0 if all flagged witnesses include duals; exit 1 otherwise.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from lp_dual_solver import verify_dual_present


# Witness file name patterns or (description / computation) field
# substrings that indicate a NUMERICAL LP / SDP solve where the
# binding-energy / shadow-price interpretation applies.
#
# Tightened (2026-05-02 post-refactor-framework audit): excluded
# overly-broad terms ("confinement-", "sdp" alone, "knot-operator")
# that match SYMBOLIC certificate witnesses or knot-particle
# feasibility probes — these don't compute LP duals (they emit
# filtration certificates or feasibility status, a separate notion).
#
# Only true operator-selection / shadow-price / LP-dual witnesses
# need the primal+dual extraction.
LP_SDP_HINTS = (
    "lp-dual",
    "lp_dual",
    "operator-selection-lp",
    "operator_selection_lp",
    "shadow-price",
    "shadow_price",
    "primal-dual",
    "primal_dual",
    "lp-duality",
    "lp_duality",
)


# Solver-import patterns that indicate a script ACTUALLY solves an LP/SDP.
# A witness is only flagged if its sibling .py imports one of these.
ACTUAL_SOLVER_IMPORTS = (
    "from scipy.optimize import linprog",
    "scipy.optimize.linprog",
    "import cvxpy",
    "from cvxpy",
    "from lp_dual_solver import",
    "import lp_dual_solver",
    "linprog(",
)


def _sibling_script(witness_path: Path) -> Path | None:
    """Find the .py script that emitted this witness.

    Heuristic: same directory, filename obtained by stripping
    .witness.json or -witness.json and adding .py. Try both
    underscore and hyphen variants.
    """
    stem = witness_path.name.removesuffix(".witness.json").removesuffix(
        "-witness.json")
    for variant in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        cand = witness_path.parent / f"{variant}.py"
        if cand.exists():
            return cand
    return None


def _script_imports_solver(script_path: Path) -> tuple[bool, str]:
    try:
        text = script_path.read_text()
    except OSError:
        return False, ""
    for marker in ACTUAL_SOLVER_IMPORTS:
        if marker in text:
            return True, marker
    return False, ""


def _name_or_description_hint(path: Path) -> tuple[str, str] | None:
    """`(field, hint)` if the witness's name or text advertises an LP/SDP
    compute, else None. **Annotation only** — see `is_lp_sdp_witness`."""
    name = path.name.lower()
    for hint in LP_SDP_HINTS:
        if hint in name:
            return ("filename", hint)
    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    # A witness whose top-level JSON is a list (or scalar) has no hint fields.
    if not isinstance(data, dict):
        return None
    for field in ("description", "computation", "audit", "name"):
        v = data.get(field)
        if isinstance(v, str):
            v_low = v.lower()
            for hint in LP_SDP_HINTS:
                if hint in v_low:
                    return (field, hint)
    return None


def is_lp_sdp_witness(path: Path) -> tuple[bool, str]:
    """Returns (is_lp_sdp, reason).

    A witness is flagged iff **its sibling `.py` actually imports an LP/SDP
    solver** (linprog / cvxpy / lp_dual_solver). That is the signal this
    script exists for: its own docstring says the failure mode is "scripts
    that solve the primal LP but never extract / report the dual", and
    whether a script solves is a property of the script.

    **The name/description hint used to GATE this, and that made the check
    miss most of what it was written to catch.** `LP_SDP_HINTS` is ten
    literal strings, and a witness had to contain one of them before its
    sibling was even consulted. Measured 2026-08-22: 71 scripts under
    `computations/` import a real solver; 13 of them emit a same-stem
    witness carrying none of the required dual fields. **The gate flagged
    one.** The twelve it missed include

      - `nucleus-operator-selection-sdp` — an *operator-selection* witness,
        missed because the hint is `operator-selection-lp` and this one ends
        `-sdp`;
      - `three-quark-borromean-lp-sweep`, `two-quark-active-set-mahler-sweep`,
        `benzene-assembly-spine` — no hint substring anywhere in the name;
      - six more in `_deprecated/`.

    So the check was keyed on a naming convention while the property it
    tests is knowable directly. The hint is kept, but only to enrich the
    reason string. A sibling that cannot be resolved is still not flagged —
    unchanged, and deliberate: without the script there is nothing to
    confirm.

    The false positive the old step 1 guarded against — a script whose
    *name* says "dual" without solving anything — is already excluded by
    the solver-import test, which is the guard that was doing the work.
    """
    sibling = _sibling_script(path)
    if sibling is None:
        return False, ""  # no sibling — nothing to confirm against
    has_solver, marker = _script_imports_solver(sibling)
    if not has_solver:
        return False, ""
    hint_match = _name_or_description_hint(path)
    if hint_match is None:
        return True, (f"script imports '{marker}' (no LP/SDP hint in the "
                      f"witness name or description — flagged on the script)")
    field, hint = hint_match
    return True, f"{field} matches '{hint}' + script imports '{marker}'"


# ── float64-backend gate (bean qou/ftuv, 2026-08-23) ─────────────────────
#
# `LpDualResult` / `SdpDualResult` now record WHICH solver served each solve
# (`backend`, `precision_bits`). Before that, `backend="auto"` picked
# clarabel-MPFR or scipy f64 depending on whether a Rust binary happened to be
# built, with nothing printed and nothing recorded — the same producer writing
# witnesses whose residuals differ by ~28 orders of magnitude (3.6e-44 vs
# 1.07e-10 on H_3), indistinguishable afterwards.
#
# This turns that record into a gate: a witness that says it was solved in
# float64 FAILS. It is a RATCHET, not a sweep — a witness with no `backend`
# field at all is reported, never failed, because the corpus predates the
# field and blocking on the backlog would block every unrelated PR. That is
# the same scoping the vacuity ledger gate and `probe-float64-gate` use.
F64_BACKENDS = frozenset({
    "scipy-highs", "scipy", "highs", "cvxpy", "scs", "ecos", "osqp",
})


# Witnesses that record an f64 solve for a MEASURED reason, keyed by basename
# with the reason spelled out. Without this list the gate rewards laundering:
# a producer with a legitimate need for the f64 backend fails, and the cheapest
# way to make it pass is to stop recording `backend` at all — dropping into the
# unannotated bucket, which the gate only reports. An exemption that must be
# named and justified is strictly better than a blind spot that costs nothing
# to enter.
#
# Add an entry only with a measurement behind it, not a preference.
F64_BACKEND_EXEMPT = {
    "rho-k-h3a-gg-trajectory.witness.json": (
        "t = 1/(dim_q · |y·χ|) with a 1e-15 floor spans 1.1 … 1e15, a cost "
        "dynamic range of 15 orders. Clarabel's interior-point method returns "
        "a false `infeasible` on it (all nucleons NaN) where HiGHS's simplex "
        "solves it. Not precision — 167/333/500 bits fail identically — and "
        "not fixable by rescaling, which shifts magnitude but not the ratio "
        "between entries. Measured 2026-08-23, bean `qou/ftuv`."
    ),
}


def _recorded_backends(path: Path) -> tuple[set[str], bool]:
    """`(f64_backends_found, any_backend_recorded)` for one witness."""
    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return set(), False
    found: set[str] = set()
    seen_any = False

    def walk(o):
        nonlocal seen_any
        if isinstance(o, dict):
            for k, v in o.items():
                # `backend`, and the prefixed forms producers use for a
                # second solver in the same row (`sdp_backend`, `lp_backend`).
                if k == "backend" or k.endswith("_backend"):
                    if isinstance(v, str):
                        seen_any = True
                        if v.strip().lower() in F64_BACKENDS:
                            found.add(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    return found, seen_any


def collect_wired_witnesses(repo_root: Path) -> set[str]:
    """Collect wired witness basenames from content block `computation.witness`."""
    wired: set[str] = set()
    content_root = repo_root / "content"
    ts_files = content_root.glob("*/*/*.ts")
    witness_pattern = re.compile(
        r"witness(?:File)?\s*:\s*[\"']([^\"']+\.json)[\"']"
    )
    for ts in ts_files:
        try:
            txt = ts.read_text()
        except OSError:
            continue
        for m in witness_pattern.finditer(txt):
            wired.add(Path(m.group(1)).name)
    return wired


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    strict_wired = "--strict-wired" in argv
    list_wired = "--list-wired" in argv
    root = Path(__file__).parent
    # `root.parent.parent` walked one level ABOVE the repo: this file is at
    # `<repo>/computations/`, so `.parent.parent` is the repo's *parent*.
    # `collect_wired_witnesses` then globbed a `content/` that does not exist,
    # returned an empty set, and `--strict-wired` reported
    # "OK — all 0 flagged wired witnesses include LP dual" — a gate passing
    # because it found nothing to check. Bean `qou/augu`.
    repo_root = root.parent
    wired = collect_wired_witnesses(repo_root) if (strict_wired or list_wired) else set()
    # RECURSIVE. This was `root.glob(...)` — non-recursive — and so scanned
    # only the witnesses sitting directly in `computations/`. The Phase 6
    # subdirectory refactor (2026-06-02, see `computations/_path_bridge.py`)
    # moved compute scripts and their witnesses into cluster directories,
    # and this walk was never updated: measured 2026-08-22, it saw 1410 of
    # the 2697 live witnesses and **1287 were invisible** — 516 in `probes/`,
    # 362 in `qbeta/`, 169 in `deltalambda/`, and so on. A check written
    # before a refactor kept passing by seeing less.
    #
    # `_deprecated/` stays out: those witnesses are retired by design and
    # flagging them would be noise, which is also what the non-recursive
    # walk happened to achieve for that one directory.
    witnesses = sorted(
        w for w in list(root.rglob("*.witness.json")) + list(root.rglob("*-witness.json"))
        if "_deprecated" not in w.parts
    )
    flagged = []
    for w in witnesses:
        is_lp, reason = is_lp_sdp_witness(w)
        if is_lp:
            flagged.append((w, reason))

    print(f"Scanned {len(witnesses)} witness files; "
          f"{len(flagged)} flagged as LP/SDP/operator-selection.")
    if strict_wired or list_wired:
        flagged_wired = [(w, r) for (w, r) in flagged if w.name in wired]
        print(f"Wired LP/SDP flagged subset: {len(flagged_wired)} "
              f"(from {len(wired)} total wired witnesses).")
    print()

    if list_wired:
        print("Flagged LP/SDP witnesses (wired status):")
        for w, reason in flagged:
            status = "wired" if w.name in wired else "audit/orphan"
            print(f"  - {w.name:45s} [{status}] {reason}")
        print()

    # ── float64-backend gate ──────────────────────────────────────────
    f64_solved: list = []
    unannotated = 0
    exempted: list = []
    for w, _reason in flagged:
        bad, seen = _recorded_backends(w)
        if bad and w.name in F64_BACKEND_EXEMPT:
            exempted.append((w, sorted(bad)))
        elif bad:
            f64_solved.append((w, sorted(bad)))
        elif not seen:
            unannotated += 1
    if exempted:
        print(f"ℹ {len(exempted)} flagged witness(es) record a float64 solve "
              "for a measured reason (F64_BACKEND_EXEMPT):")
        for w, bad in exempted:
            print(f"  ·  {w.name}   backend={', '.join(bad)}")
            print(f"     {F64_BACKEND_EXEMPT[w.name]}")
        print()
    if f64_solved:
        print(f"✗ float64 backend: {len(f64_solved)} flagged witness(es) record "
              "a float64 solve:")
        for w, bad in f64_solved:
            print(f"  ✗  {w.name}   backend={', '.join(bad)}")
        print("  Rebuild the MPFR path and re-run the producer:")
        print("    cargo build --release --features clarabel-mpfr \\")
        print("      --bin clarabel-operator-selection-lp   (in tools/hecke-engine)")
        print("  and/or set QOU_REQUIRE_CLARABEL=1 so a missing binary is an")
        print("  error rather than a silent downgrade.")
        print()
    if unannotated:
        print(f"ℹ {unannotated} flagged witness(es) record no backend at all — "
              "produced before the field existed. Reported, not failed: the "
              "gate ratchets on NEW float64 solves.")
        print()

    failures = []
    for w, reason in flagged:
        result = verify_dual_present(w)
        if not result["ok"]:
            failures.append((w, reason, result))

    if strict_wired:
        failures = [f for f in failures if f[0].name in wired]
        scope_msg = "flagged wired witnesses"
    else:
        scope_msg = "flagged witnesses"

    # The float64-backend gate shares the strict scoping: in --strict-wired it
    # blocks only witnesses a content block cites, in --strict everything.
    f64_blocking = (
        [w for w, _ in f64_solved if w.name in wired] if strict_wired
        else [w for w, _ in f64_solved]
    )

    if not failures:
        if strict_wired:
            print(f"OK — all {len([w for w, _ in flagged if w.name in wired])} "
                  "flagged wired witnesses include LP dual.")
        else:
            print(f"OK — all {len(flagged)} flagged witnesses include LP dual.")
        if f64_blocking and (strict or strict_wired):
            print(f"Exit 1 — {len(f64_blocking)} witness(es) record a float64 "
                  "solve (see above).")
            return 1
        return 0

    # Brief failure summary
    severity = "FAIL" if (strict or strict_wired) else "WARN"
    denominator = len([w for w, _ in flagged if w.name in wired]) if strict_wired else len(flagged)
    print(f"{severity} — "
          f"{len(failures)}/{denominator} {scope_msg} missing "
          f"LP dual fields.")
    print()
    print("Sample (first 10):")
    for w, reason, result in failures[:10]:
        sibling = _sibling_script(w)
        print(f"  ✗  {w.name}")
        print(f"     reason:  {reason}")
        if sibling is not None:
            print(f"     script:  {sibling.name}")
        print(f"     missing: {result['missing']}")
    if len(failures) > 10:
        print(f"  ... ({len(failures) - 10} more)")
    print()
    print("To fix: route the LP/SDP solve through")
    print("  computations/lp_dual_solver.py")
    print("which returns BOTH primal and dual via")
    print("  solve_operator_selection_lp() or solve_psd_operator_selection_sdp().")
    print("The result's .to_dict() contains all required fields.")
    print()
    if f64_blocking and (strict or strict_wired):
        print(f"Additionally: {len(f64_blocking)} witness(es) record a float64 "
              "solve (see above).")
        print()
    if strict or strict_wired:
        if strict_wired:
            print("Exit 1 (--strict-wired mode).")
        else:
            print("Exit 1 (--strict mode).")
        return 1
    print("Exit 0 (warn-only mode; pass --strict or --strict-wired to enforce).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
