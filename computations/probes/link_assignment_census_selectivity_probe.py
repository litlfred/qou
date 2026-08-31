#!/usr/bin/env python3
"""Gap #2 — the 3-body link-volume. The knot assignment carries no information.

WHAT THIS IS ABOUT
------------------
`conj-canonical-knot-id-sdp.md` asserts:

> the joint mass-tower confinement SDP **uniquely selects** the canonical knot
> ... The unique global minimizers are `6_2` for ²H, `8_11` for ³H, and `L6a4`
> for ³He.

and in the same breath records the provenance:

> **Historical volume matching originally proposed these assignments.**
> Finitude of the normal-form candidate set, rigorous SDP search bounds, and
> structural identification of the binding operator `K` are open verification
> requirements.

That volume matching is `B ≈ ρ · m_e · Vol(K)`, with `ρ` an integer the corpus
calls, in `_deprecated/rho_census_wedderburn_experiment.py`, the **"hand-pick
ρ"**. So the identification has two free choices — a knot drawn from a census,
and an integer — fitted against one number per atom.

This probe measures how much the volume match constrains the knot. It does NOT
re-run the literal per-body-order volume route: that is separately REFUTED at
`n = 2` by `binding_wn_link_volume_probe.py` (`Vol(Hopf) = 0` against an
extracted `w_2 = 4.3534`). The question here is prior to that one — whether the
*assignment* the route starts from was ever determined.

THE MEASUREMENT, WITH NO TOLERANCE CHOSEN
------------------------------------------
Picking a tolerance would be picking the answer. So instead each knot's **own
achieved accuracy** sets the window, and we count the census manifolds that do
at least as well:

    N(K) = #{ M in census : |Vol(M) − Vol_target| ≤ |Vol(K) − Vol_target| }
    Vol_target = B_AME / (ρ · m_e)

Against SnapPy's `OrientableCuspedCensus` (212,641) + `HTLinkExteriors`
(180,511) — the same two censuses `m_tau_census_sweep.py` searched, so the
reach is already on the corpus record:

    atom  knot   Vol       B_pred    err      manifolds at least as good
    ------------------------------------------------------------------
    ²H    6_2    4.40083   2.24882   +1.090 %              799
    ³H    8_11   8.28632   8.46860   −0.156 %            1,102
    ³He   L6a4   7.32772   7.48892   −2.969 %           26,843

**The chosen knot is one of between 800 and 27,000 equally good ones.** No
tolerance was chosen; these are ranks. An assignment that is 1-of-26,846 is not
an identification, and `≈ 10 to 15 bits` of unjustified choice is being spent
per atom to make it.

TWO OF THE THREE PICKS MISS THE DOC'S OWN 0.5 %
------------------------------------------------
`6_2` lands at +1.09 % and `L6a4` at −2.97 %. Only `8_11` is inside 0.5 %.
(The doc's 0.5 % is stated of the SDP Frobenius residual, not of the volume, so
this is not a direct contradiction — it is the volume route failing at the
tolerance the same document treats as the standard of a match.)

AND THE ONE PICK WITH A STRUCTURAL REASON IS THE WORST NUMERICALLY
-------------------------------------------------------------------
`L6a4` is the one assignment with an argument independent of its volume:
`binding_link_volumes.py` shows `L6a4 = Borromean`, the same link that defines
the per-nucleon braid `𝓑₃` — "an identification, not a fit", and correctly so.
It is also the pick with the largest volume error (−2.97 %) and by far the
weakest rank (1-of-26,846). Conversely `8_11`, the only pick inside 0.5 %, has
no structural motivation on record at all. The two criteria are not just weak —
they are **anti-correlated across the three atoms**.

WHY THE PSD SDP DOES NOT RESCUE IT
------------------------------------
`binding-link-psd-feasibility-probe.witness.json` records, at `H_3`:

    ²H whole-atom 6_2 .......... False      ← the census pick FAILS
    ²H binding L_H (Hopf) ...... True
    ³He whole-atom L6a4 ........ True
    control: trivial (unknot) .. True       ← so does the UNKNOT

The unknot passing is the decisive entry. PSD-feasibility of `ρ_λ(K)` is a
**necessary** condition that trivial objects satisfy, so as it stands the SDP is
a filter with no demonstrated selective power — it cannot be what "uniquely
selects" anything. And where it has been run on a census pick it *rejects* it:
`6_2` fails at `H_3` with a standard-`(2,1)` eigenvalue of `−0.89` (PR #1698).

WHAT WOULD CLOSE GAP #2
------------------------
The volume route cannot be repaired by a better tolerance — the failure is that
the census is dense at these volumes, so no tolerance separates the candidates.
Selection has to come from an **objective**, not a feasibility test, and the
objective has to be independent of `B_AME` or the `qou-l81w` rule is violated
exactly as it is now. The corpus already has the pieces:

  - the convolution `K_word = atom_word ++ cp_inv_word` (`binding_k_solver.py`),
    which *determines* `K` from the atom word — so the open question is what
    determines `K`, not what determines the knot;
  - a substrate-only cost vector `t = TR_M` and Gram matrix `G` from
    `pyhecke.gram`, with dual-emitting solvers (`solve_operator_selection_lp`,
    `solve_frobenius_dual_lp`) that take no empirical input.

What is missing is the **minimisation over Gröbner–Shirshov normal forms** the
conjecture describes but no witness performs, together with the finitude bound
that would make "unique global minimizer" checkable. Until then the three
assignments should be recorded as hand-picked, not as SDP outputs.

DISCIPLINE
----------
No fit; no tier change; nothing rewired. Volumes are taken from SnapPy 3.3.2 and
cross-checked against the corpus's canonical `knot_volumes.py` registry, so the
census counts and the corpus constants are the same numbers. The verdict is
structural (the census density at these volumes), not scope-limited: enlarging
the search space can only increase the counts.

-- Ref: [manuscript] bean t7qv (Gap #2); conj-canonical-knot-id-sdp.md
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
)
from knot_volumes import (  # noqa: E402
    VOL_6_2_MPF,
    VOL_8_11_MPF,
    VOL_BORROMEAN_MPF,
)

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

set_compute_dps()

# (atom, B_AME, hand-picked ρ, knot name, canonical Vol from knot_volumes.py).
# Every numeric is mpf: SnapPy's census slicing is the ONLY place a float
# appears, and only because `census[lo:hi]` takes binary64 bounds.
PICKS = [
    ("2H",  AME_B_DEUTERON_MEV_VALIDATION, 1, "6_2",  VOL_6_2_MPF),
    ("3H",  AME_B_TRITIUM_MEV_VALIDATION,  2, "8_11", VOL_8_11_MPF),
    ("3He", AME_B_HE3_MEV_VALIDATION,      2, "L6a4", VOL_BORROMEAN_MPF),
]

# Recorded verbatim from binding-link-psd-feasibility-probe.witness.json.
PSD_RECORDED = {
    "2H whole-atom 6_2": False,
    "2H binding L_H (Hopf)": True,
    "3He whole-atom L6a4": True,
    "control: trivial (unknot)": True,
}


def _censuses():
    """SnapPy censuses, or None when SnapPy is absent.

    `m_tau_census_sweep.py` imports SnapPy unguarded; this probe guards so the
    structural half (PSD selectivity, the anti-correlation) still reports in a
    sandbox without it, and says so rather than silently thinning.
    """
    try:
        import snappy  # noqa: PLC0415
    except Exception:
        return None, None
    return snappy, [
        ("OrientableCuspedCensus", snappy.OrientableCuspedCensus()),
        ("HTLinkExteriors", snappy.HTLinkExteriors()),
    ]


def rank_against_census(censuses, vol_target, vol_pick) -> dict:
    """Count census manifolds at least as close to `vol_target` as `vol_pick`.

    The window is set by the pick's own error, so no tolerance is chosen. The
    count includes the chosen manifold itself where the census contains it.

    `vol_target` / `vol_pick` arrive as mpf and are widened by one ulp before
    the float cast, so the binary64 bounds SnapPy requires can only ADD
    manifolds at the edge — the reported count stays a lower bound on the
    candidate set, which is the direction the verdict needs.
    """
    d = abs(vol_pick - vol_target)
    lo = math.nextafter(float(vol_target - d), -math.inf)
    hi = math.nextafter(float(vol_target + d), math.inf)
    out, total = {}, 0
    for name, cen in censuses:
        n = len(list(cen[lo:hi]))
        out[name] = n
        total += n
    out["total"] = total
    return out


def main() -> int:
    snappy, censuses = _censuses()
    rows, assertions = [], []

    print("Gap #2 — does the volume match determine the knot?")
    print()
    print(f"  {'atom':5s} {'knot':6s} {'Vol':>9s} {'Vol_target':>10s} "
          f"{'B_pred':>9s} {'err%':>8s}   manifolds at least as good")
    print("  " + "-" * 78)

    abs_err = {}          # atom -> mpf, kept at compute precision for A3
    for atom, B, rho, knot, vol in PICKS:
        vol_target = B / (M_E_MEV * rho)
        b_pred = rho * M_E_MEV * vol
        err = (b_pred - B) / B * 100
        abs_err[atom] = abs(err)
        row = {
            "atom": atom, "knot": knot, "rho_handpicked": rho,
            "B_AME_MeV": fmt(B), "vol": fmt(vol),
            "vol_target": fmt(vol_target), "B_pred_MeV": fmt(b_pred),
            "err_pct": fmt(err),
        }
        cells = (f"  {atom:5s} {knot:6s} {mp.nstr(vol, 7):>9s} "
                 f"{mp.nstr(vol_target, 7):>10s} {mp.nstr(b_pred, 7):>9s} "
                 f"{mp.nstr(err, 4):>8s}")
        if censuses is not None:
            row["census_at_least_as_good"] = rank_against_census(
                censuses, vol_target, vol)
            n = row["census_at_least_as_good"]["total"]
            print(f"{cells}   {n:,}")
        else:
            print(f"{cells}   (SnapPy unavailable)")
        rows.append(row)

    # ── A1. The volume match does not determine the knot ──────────────
    if censuses is not None:
        counts = {r["atom"]: r["census_at_least_as_good"]["total"] for r in rows}
        worst = min(counts.values())
        ok = worst >= 100
        print()
        print(f"  A1  every pick is out-ranked by >= 100 census manifolds "
              f"(min = {worst:,}) ......... {'PASS' if ok else 'FAIL'}")
        print(f"      counts: " + ", ".join(f"{k} = {v:,}" for k, v in counts.items()))
        print("      => the assignment is 1-of-many, not an identification.")
        assertions.append(("volume_match_does_not_determine_knot", ok,
                           f"min rank {worst}; counts {counts}"))

    # ── A2. Two of three miss the doc's own 0.5 % ─────────────────────
    half = mp.mpf(1) / 2
    outside = [a for a, e in abs_err.items() if e > half]
    ok = set(outside) == {"2H", "3He"}
    print()
    print(f"  A2  picks outside 0.5 %: {outside} ......................... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      6_2 at +1.09 %, L6a4 at −2.97 %; only 8_11 is inside.")
    assertions.append(("two_of_three_picks_miss_half_percent", ok,
                       f"outside 0.5%: {outside}"))

    # ── A3. Structural motivation and numerical accuracy anti-correlate ─
    err = abs_err
    ok = err["3He"] > err["2H"] > err["3H"]
    print()
    print(f"  A3  the one structurally-motivated pick (L6a4 = Borromean = 𝓑₃)")
    print(f"      is the WORST numerically: |err| 3He {mp.nstr(err['3He'], 4)} % "
          f"> 2H {mp.nstr(err['2H'], 4)} % > 3H {mp.nstr(err['3H'], 4)} % ...... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      and 8_11, the only pick inside 0.5 %, has no structural")
    print("      motivation on record. The two criteria disagree.")
    assertions.append(("structure_and_accuracy_anticorrelate", ok,
                       f"|err%| 3He={fmt(err['3He'])} 2H={fmt(err['2H'])} "
                       f"3H={fmt(err['3H'])}"))

    # ── A4. PSD feasibility has no selective power ────────────────────
    ok = (PSD_RECORDED["control: trivial (unknot)"] is True
          and PSD_RECORDED["2H whole-atom 6_2"] is False)
    print()
    print(f"  A4  PSD-feasibility selects nothing: the UNKNOT passes, while")
    print(f"      the census pick 6_2 FAILS ............................ "
          f"{'PASS' if ok else 'FAIL'}")
    print("      (binding-link-psd-feasibility-probe.witness.json; the −0.89")
    print("      standard-(2,1) eigenvalue for 6_2 is PR #1698.)")
    print("      => a necessary condition trivial objects satisfy cannot be")
    print("         what 'uniquely selects' the canonical knot.")
    assertions.append(("psd_feasibility_has_no_selective_power", ok,
                       f"recorded: {PSD_RECORDED}"))

    print()
    print("### VERDICT: the three knot assignments are HAND-PICKED, not derived.")
    print("    The volume criterion is satisfied by 10^3–10^4 census manifolds")
    print("    per atom; the PSD criterion is satisfied by the unknot. Neither")
    print("    is a selection principle. Gap #2 needs an OBJECTIVE over GS")
    print("    normal forms that takes no B_AME input (qou-l81w), plus the")
    print("    finitude bound conj-canonical-knot-id-sdp.md lists as open.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("link-assignment-census-selectivity",
                                engine="snappy" if snappy else "python",
                                output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (Gap #2, bean t7qv): measures how much the volume "
                "criterion B ~ rho*m_e*Vol constrains the 2H/3H/3He knot "
                "assignment. With each knot's OWN achieved accuracy as the "
                "window — no tolerance chosen — 799 / 1,102 / 26,843 SnapPy "
                "census manifolds do at least as well, so the assignment is "
                "1-of-many rather than an identification. Two of the three "
                "picks (6_2 at +1.09%, L6a4 at -2.97%) miss the 0.5% the "
                "conjecture doc treats as a match, and the one pick with an "
                "independent structural reason (L6a4 = Borromean = the "
                "per-nucleon braid) is the worst numerically. The PSD route "
                "does not rescue it: the recorded H_3 run passes the UNKNOT "
                "and fails 6_2. No fit; no wiring; no tier change.")
            wb.add_data("picks", rows)
            wb.add_data("psd_recorded_at_h3", PSD_RECORDED)
            wb.add_data("snappy_version", snappy.version() if snappy else None)
            wb.add_data("census_sizes",
                        {n: len(c) for n, c in censuses} if censuses else None)
            for name, passed, detail in assertions:
                wb.add_assertion(
                    name=name, computed=str(int(bool(passed))), expected="1",
                    tolerance=0, source=detail)
            wb.add_caveat(
                "The census counts are a LOWER bound on the candidate set: "
                "OrientableCuspedCensus + HTLinkExteriors are the two censuses "
                "m_tau_census_sweep.py already searched, and enlarging the "
                "search space can only raise the counts. The verdict is "
                "therefore structural, not scope-limited.")
            wb.add_caveat(
                "The 0.5% in conj-canonical-knot-id-sdp.md is stated of the SDP "
                "Frobenius residual, not of the volume. A2 is the VOLUME route "
                "failing at that tolerance, not a direct contradiction of the "
                "doc's own claim.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
