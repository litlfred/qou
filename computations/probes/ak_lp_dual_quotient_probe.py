#!/usr/bin/env python3
"""Does re-posing the a_K operator-selection LP on H_n/rad recover a_K?

ANSWER: NO — and the more useful finding is that it never did.

`qou-fu8c` recorded that `aK_via_lp_dual_full` degenerates under convention D:
the solve returns `primal_obj = 0`, `y0* = -0.0` on all six atoms, so
`a_K = 1 + (chirality dual sum)/|y0*|` does not exist and the producer emits
`null`. The bean asked whether restricting the LP to the two-row quotient — the
blocks convention D leaves alive — makes `y0*` nonzero and recovers `a_K`.

It makes `y0*` nonzero. It does not recover `a_K`. And checking the convention-C
history shows the LP was never recovering it, so this is not a convention-D
regression.

## The mechanism, exactly

The LP (`pyhecke.lp_dual_solver.solve_operator_selection_lp`, the canonical
entry point named in AGENTS.md §"LP / SDP duals") is

    min  t^T x   s.t.  Σ x_i = n_target,  G x >= 0,  x_i >= -M

read off its own `A_eq = ones(1,d)`, `b_eq = [n_target]`, `A_ub = -G`,
`b_ub = 0`; and the caller passes `t = |contrib|`, `G = diag(|contrib|)`,
`n_target = tr_M`. Because `G` is the diagonal of `t`, the inequality is just
`x_i >= 0` wherever `t_i > 0`, and the program collapses to

    min Σ t_i x_i  s.t.  Σ x_i = n_target,  x_i >= 0

whose optimum is "put all of `n_target` on the cheapest column". So

    y0*  =  min_i |contrib_i|                                        (exactly)

That is the whole content of the dual. Verified numerically below against the
solver's own `y0_star`.

Convention D sets `contrib = y_λ·χ^λ = 0` on every `ℓ(λ) >= 3` block, which
makes those columns **zero-cost and unconstrained** (`t_i = 0`, and their `G`
row reads `0 >= 0`). The LP then routes the entire net constraint through a
column that costs nothing: `primal_obj = 0`, `y0* = 0`. That is the CORRECT
answer to the LP as posed — the program has become vacuous, not broken.

## Why "it worked under C" is the wrong reading

Under convention C those blocks carried small nonzero weights, so
`min_i |contrib_i|` was small-but-positive and `a_K` came out finite. Finite is
not correct. From the committed convention-C witness:

    atom        y0*         a_K^dual        a_K^closed   dual_vs_C_ppm
    proton      0.016814      58.7344         1.000000        5.8e+07
    neutron     0.020715      47.1283         1.000000        4.6e+07
    deuteron    0.000008      1.06e+06        1.209060        8.7e+11
    tritium     0.000000      4.51e+08        0.956294        4.7e+14
    helium-3    0.000000      6.84e+08        0.956294        7.2e+14
    helium-4    0.000000      1.51e+11        0.914498        1.6e+17

The probe's own `dual_vs_C_ppm` field — which exists to measure exactly this —
was reporting up to **17 orders of magnitude** of disagreement and reading as a
successful run, because the producer exits 0 regardless.

So the honest description of what convention D did here is: it turned a wrong
number into no number. The pathology is continuous — as the `ℓ(λ) >= 3` weights
approach their true value of zero, `min_i |contrib_i| -> 0` and `a_K -> ∞`.
Convention D is that limit, reached exactly.

## What the quotient buys

Dropping the radical columns removes the zero-cost escape, so `y0*` becomes the
smallest LIVE contribution and `a_K` is defined again. It also improves the
agreement by ~8 orders of magnitude at helium-4. It does not close it.

Scope, per the (a)/(b) rule: **scope (a)**. This refutes the LP *as posed* —
objective `t = |contrib|` against a plain sum-to-target constraint — on the
quotient. It does **not** exclude an operator-selection LP as the route to
`a_K`; §"Next" names the untested reformulation.

## A separate defect found on the way

`aK_via_lp_dual_full.solve_atom_lp` documents its own constraint as

    #  s.t.  Σ_λ contrib_λ · x_λ = tr_M_atom    (reproduce trace)

The solver enforces `Σ_λ x_λ = n_target`. The contributions never enter the
constraint at all, only the objective — so the LP has never imposed trace
reproduction, under either convention. Reported as `trace_constraint_imposed:
false`; NOT silently repaired here, because changing the constraint changes what
the probe means and that belongs in its own change.

audit_only. Reads committed chi caches; adds no anchor and no fit.
"""

from __future__ import annotations

import json
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate"),
           str(REPO / "tools" / "pyhecke" / "python"),
           str(REPO / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402

#: (Z, N, chi-cache) — mirrors aK_via_lp_dual_full.ATOM_CHI.
ATOMS = [
    ("proton", 1, 0, "chi-proton-h3-at-q0-50dps.witness.json"),
    ("neutron", 0, 1, "chi-neutron-h3-at-q0-50dps.witness.json"),
    ("deuteron", 1, 1, "chi-deuteron-h6-at-q0-50dps.witness.json"),
    ("tritium", 1, 2, "chi-tritium-h9-at-q0-50dps.witness.json"),
    ("helium-3", 2, 1, "chi-helium-3-h9-at-q0-50dps.witness.json"),
    ("helium-4", 2, 2, "chi-helium-4-h12-at-q0-50dps.witness.json"),
]


def is_self_conjugate(lam: list) -> bool:
    """λ = λ'. Transpose via column heights, so it needs no padding."""
    if not lam:
        return True
    conj = [sum(1 for part in lam if part > i) for i in range(lam[0])]
    return conj == list(lam)


def a_K_closed(A: int) -> float:
    """The closed form this LP is supposed to reproduce.

    Duplicated from `aK_via_lp_dual_full` rather than imported: that module
    runs a full solve at import and writes a witness, which a probe must not
    trigger as a side effect of reading one function.
    """
    from q_parameter import HA as h  # noqa: PLC0415
    if A in (1, 2):
        return 1.0 if A == 1 else 1.0 + float(h)
    if A == 3:
        return 1.0 - float(h) * float(h)
    if A == 4:
        return (1.0 - float(h) * float(h)) ** 2
    return float("nan")


def solve(contribs, target, keep=None):
    """Run the operator-selection LP over `keep` (default: every column)."""
    idx = list(range(len(contribs))) if keep is None else list(keep)
    t = np.array([abs(float(contribs[i])) for i in idx], dtype=float)
    res = solve_operator_selection_lp(t, np.diag(t), float(target),
                                      backend="scipy")
    return idx, t, res


def main() -> int:
    rows = []
    # Upstream hash records for every chi cache consumed, captured as they are
    # read and attached to the builder below.
    #
    # Reading a witness with a bare `json.loads(path.read_text())` bypasses
    # WitnessBuilder's upstream tracking, so `witness_dependency_drift.py` has
    # no edge from this witness to the caches it depends on and cannot tell
    # when one of them goes stale underneath it. That matters here more than
    # usual: this probe's entire result is a statement about the contribution
    # values in those six caches, so a silent upstream change would invalidate
    # the verdict with nothing to detect it. (Copilot review, PR #5025.)
    _UP: list = []
    for atom, Z, N, fname in ATOMS:
        A = Z + N
        doc = record_upstream(COMP / fname, _UP)
        per = doc["by_partition"]
        target = mp.mpf(doc["tr_M_at_q0"])
        contribs = [mp.mpf(r["contribution"]) for r in per]
        live = [i for i, r in enumerate(per) if mp.mpf(r["y_lambda"]) != 0]

        _, _, amb = solve(contribs, target)
        idx, t_q, quo = solve(contribs, target, keep=live)

        chir = sum(quo.y_star[j] for j, i in enumerate(idx)
                   if not is_self_conjugate(list(per[i]["partition"]))
                   and j in quo.active_set)
        y0 = quo.y0_star
        aK = 1.0 + chir / abs(y0) if abs(y0) > 1e-12 else None
        aKc = a_K_closed(A)
        ppm = ((aK / aKc - 1) * 1e6
               if aK is not None and aKc == aKc and aKc else None)

        # y0* == min_i |contrib_i| over the summed columns, claimed in the
        # module docstring. Checked rather than asserted.
        y0_predicted = float(min(t_q)) if len(t_q) else float("nan")

        # Two serialisation regimes, deliberately kept apart:
        #
        # * SOLVER OUTPUT nests under the exact field names the raw-float64
        #   audit's LP_DUAL_F64_FIELDS carve-out recognises (`y0_star`,
        #   `primal_obj`, `duality_gap`, …). Those are f64 by construction —
        #   scipy's linprog returns f64 and there is no mpf source to carry —
        #   so the owner-approved carve-out is the honest home for them, and
        #   nesting uses it as designed rather than widening any list.
        # * THE PROBE'S OWN RESULTS go through `_precision.fmt`, per the
        #   audit's instruction. They are f64-derived, so `fmt` on a float
        #   emits the shortest exact repr and fabricates no digits.
        #
        # The distinction is the same one the carve-out itself draws: it
        # excuses the solver's numbers and deliberately does NOT hide the
        # probe's conclusions.
        rows.append({
            "atom": atom, "Z": Z, "N": N, "A": A,
            "blocks_total": len(per),
            "blocks_live": len(live),
            "blocks_radical": len(per) - len(live),
            # `y_star`, `active_set` and `dual_obj` added 2026-08-22 (bean
            # `qou/augu`): the LP-dual contract asks for six fields and this
            # emitted three, so `lp_dual_witness_validator.py` read the
            # witness as reporting no dual. All three were already in hand —
            # `chir` above sums `quo.y_star` over `quo.active_set` — so the
            # verdict rested on numbers the witness did not carry. They are
            # solver output under the canonical names, hence inside the same
            # `LP_DUAL_F64_FIELDS` carve-out as their three siblings.
            "ambient": {"y0_star": amb.y0_star,
                        "y_star": list(amb.y_star),
                        "active_set": list(amb.active_set),
                        "primal_obj": amb.primal_obj,
                        "dual_obj": amb.dual_obj,
                        "duality_gap": amb.duality_gap},
            "quotient": {"y0_star": y0,
                         "y_star": list(quo.y_star),
                         "active_set": list(quo.active_set),
                         "primal_obj": quo.primal_obj,
                         "dual_obj": quo.dual_obj,
                         "duality_gap": quo.duality_gap},
            "y0_star_equals_min_contrib": bool(
                abs(y0 - y0_predicted) <= 1e-9 * max(1.0, abs(y0_predicted))),
            # float64-intentional: these are LP DUAL variables straight from
            # the solver, which works in double precision. There is no exact
            # route to a number the solver only ever computed as a double.
            # float64-intentional: LP dual, solver works in double precision.
            "min_live_contrib": fmt(y0_predicted),
            # float64-intentional: LP dual, solver works in double precision.
            "chirality_dual_sum": fmt(float(chir)),
            "a_K_via_lp_dual_quotient": fmt(aK) if aK is not None else None,
            "a_K_closed": fmt(aKc),
            "quotient_vs_closed_ppm": fmt(ppm) if ppm is not None else None,
            # Kept as plain floats for the print/summary path below; not
            # serialised (stripped before the witness is built).
            "_aK": aK, "_ppm": ppm, "_y0q": y0, "_y0a": amb.y0_star,
        })

    ambient_all_degenerate = all(abs(r["_y0a"]) <= 1e-12 for r in rows)
    quotient_all_defined = all(r["_aK"] is not None for r in rows)
    y0_identity_holds = all(r["y0_star_equals_min_contrib"] for r in rows)
    worst_ppm = max(abs(r["_ppm"]) for r in rows)
    quotient_recovers_aK = worst_ppm < 1.0  # 1 ppm would be agreement

    # Private display-only keys never reach the witness.
    for r in rows:
        for k in ("_aK", "_ppm", "_y0q", "_y0a"):
            r.pop(k, None)

    payload = {
        "computation": "ak-lp-dual-quotient-probe",
        "description": (
            "Re-poses the a_K operator-selection LP on H_n/rad (the blocks "
            "convention D leaves alive) and asks whether that recovers a_K. It "
            "makes y0* nonzero and a_K defined, but does NOT recover a_K — and "
            "the convention-C history shows the LP never did, missing by up to "
            "1.6e17 ppm. audit_only; no anchor, no fit."),
        "audit_only": True,
        "markov_convention": "D",
        "tier": "structural-exact (decidable; LP optimum is an argmin, no fit)",
        "result": {
            "verdict": (
                f"Quotient restriction makes a_K DEFINED but does NOT recover "
                f"it: worst |quotient vs closed| = {worst_ppm:.3e} ppm. The LP "
                f"reduces to y0* = min_i |contrib_i| (verified on all "
                f"{len(rows)} atoms), so the dual carries no operator-selection "
                f"content. Convention C missed by up to 1.6e17 ppm, so this is "
                f"NOT a convention-D regression — D turned a wrong number into "
                f"no number. Scope-(a): refutes the LP AS POSED (t = |contrib| "
                f"against a sum-to-target constraint); does NOT exclude an "
                f"operator-selection LP as the route to a_K."),
            "trace_constraint_imposed": False,
            "trace_constraint_note": (
                "aK_via_lp_dual_full documents 'Σ_λ contrib_λ·x_λ = tr_M_atom "
                "(reproduce trace)' but the solver enforces Σ_λ x_λ = n_target. "
                "The contributions enter the objective only, so trace "
                "reproduction has never been a constraint, under either "
                "convention. Not repaired here — it changes what the probe "
                "means."),
            "convention_C_history": {
                "note": ("from the committed convention-C witness, before this "
                         "campaign; a_K^dual vs a_K^closed"),
                # Quoted as strings, not JSON numbers: these are transcribed
                # from a superseded committed witness, so they are a record of
                # what that file said, not values this run computed. Emitting
                # them as floats would also make this witness the campaign's
                # only NEW raw-float64 offender, over four numbers that are
                # pure provenance.
                "proton": {"a_K_dual": "58.7344", "ppm": "5.7734367e7"},
                "helium-4": {"a_K_dual": "1.505430126057708e11",
                             "ppm": "1.64618234282323584e17"},
            },
            "rows": rows,
        },
        "context": {
            "axis": "a_K operator-selection LP under convention D",
            "bean": "qou-fu8c",
            "related": ["qou-w8zz (same repair shape: Gram inverse on the "
                        "quotient)", "qou-m7py (Rust gram.rs coupling)"],
        },
    }

    # Assertions go through `add_assertion`, NOT into `payload`.
    # `wrap_legacy` skips every key in `_RESERVED_LEGACY_KEYS` — which includes
    # `assertions` and `allPassed` — and `build()` recomputes them from the
    # builder. So a payload-supplied assertion list is silently DROPPED and the
    # witness is emitted with `assertions: []` and `allPassed: true`, vacuously
    # true because nothing was registered. This probe hit exactly that: its
    # headline check (`quotient_recovers_a_K_closed`) is FALSE, and the first
    # witness it wrote still claimed allPassed. Registering them properly is
    # what makes the failure visible.
    builder = WitnessBuilder.wrap_legacy(
        "ak-lp-dual-quotient-probe", payload,
        script_path=__file__, engine="python+scipy+mpmath",
    ).add_upstream_records(_UP)
    for name, ok in (
        ("ambient_lp_degenerate_under_D", ambient_all_degenerate),
        ("quotient_lp_gives_defined_aK", quotient_all_defined),
        ("y0_star_equals_min_live_contribution", y0_identity_holds),
        # The point of the probe. Registered so a future run that DOES close it
        # flips to passed instead of the result going unnoticed.
        ("quotient_recovers_a_K_closed", quotient_recovers_aK),
    ):
        builder.add_assertion(name, computed="1" if ok else "0", expected="1",
                              tolerance="0", unit="boolean",
                              source="ak_lp_dual_quotient_probe")
    out = builder.save()

    print("=== a_K LP dual: ambient vs quotient (H_n/rad) ===")
    print(f"{'atom':10s} {'A':>2s} {'live':>5s} {'rad':>4s} {'y0*_amb':>9s} "
          f"{'y0*_quot':>10s} {'a_K_quot':>12s} {'a_K_closed':>10s} {'ppm':>12s}")
    for r in rows:
        ak = r["a_K_via_lp_dual_quotient"]
        ppm_s = r["quotient_vs_closed_ppm"]
        print(f"{r['atom']:10s} {r['A']:>2d} {r['blocks_live']:>5d} "
              f"{r['blocks_radical']:>4d} {r['ambient']['y0_star']:9.6f} "
              f"{r['quotient']['y0_star']:10.6f} "
              f"{(f'{float(ak):12.4f}' if ak is not None else '       degen')} "
              f"{float(r['a_K_closed']):10.6f} "
              f"{(f'{float(ppm_s):12.3e}' if ppm_s is not None else '         n/a')}")
    print()
    print(f"  y0* == min_i |contrib_i| on all atoms : {y0_identity_holds}")
    print(f"  quotient recovers a_K (<1 ppm)        : {quotient_recovers_aK}"
          f"   worst {worst_ppm:.3e} ppm")
    print(f"  trace constraint actually imposed     : False  (docstring says otherwise)")
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
