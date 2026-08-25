#!/usr/bin/env python3
"""mu3_frechet_perblock_probe.py — the per-block Fréchet test on the μ₃ sign door.

THE QUESTION. `Mu3BlockwiseExclusion.lean` (merged #4651) proves:

  * `Δ²` is linear over Wedderburn blocks: `Δ²g = Σ_λ Δ²(block λ)`;
  * a submodular total **forces** a block with its own `Δ²_λ < 0`
    (`submodular_needs_interfering_block`);
  * in damping coordinates a block is submodular **iff** its joint damping factor falls
    strictly below the **Fréchet–Hoeffding lower bound**, `r_ab < r_a + r_b − 1`
    (`block_submodular_iff_below_frechet`), which is strictly stronger than beating
    multiplicative damping (`interfering_block_beats_multiplicative`).

So the sign of the per-block `Δ²_λ` **is** the per-block Fréchet test. This probe measures
it, block by block, on the operator #4404 measured (the H₉ `|χ|`-joint-trace over the two
ADJACENT chain bonds), for both A=3 isotopes.

THE FACTORISATION THAT MATTERS.  A block contributes `g_λ = y_λ·|χ_λ|`, so

    Δ²_λ  =  y_λ · Δ²|χ|_λ

and the two factors answer *different* questions:

  * `Δ²|χ|_λ` is the **geometry** — the Fréchet test proper. Damping ratios
    `r = |χ|_a/|χ|_∅` are weight-independent (the `y_λ` cancels), so the Fréchet slack
    `r_ab − (r_a + r_b − 1)` is a statement about the character alone.
  * `y_λ` is the **Wedderburn weight**, and at n = 9, q₀ it is **NOT sign-definite**:
    10 of the 30 weights are negative. This probe reports that explicitly, because the
    Lean escape-closure `reweight_cannot_open_door` assumes `w_λ ≥ 0` and therefore does
    **not** apply to this spectrum.

So a block can push the total submodular in two structurally different ways — submodular
geometry carried by a positive weight, or supermodular geometry carried by a negative
weight — and only the first is a Fréchet violation. Reporting them as one number would
conflate a geometric fact with a bookkeeping sign.

GATES (fail loudly, no fitting):
  * linearity self-check: `Σ_λ Δ²_λ` must equal the total `Δ²g` computed the old way;
  * factorisation self-check: `y_λ·Δ²|χ|_λ` must reproduce `Δ²_λ` blockwise;
  * baseline: `c₃ = −E₀·Δ²g` must reproduce #4404's committed −1.769 (T), −1.405 (³He).

No Δ_λ, no μ₃ fitted, nothing wired: this measures signs and reports them either way.

NOTATION.  The `c3` in this file is the **cluster** coefficient `cl₃ = −E₀·Δ²g` (MeV-valued),
NOT the Q_β precision-ladder `c_k`.  Prose and docs write `cl₃`; the variable names and witness
keys still read `c3` because they are a cross-probe data contract (see bean `qou-f7je`).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0))
q0f = float(Q0)
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
H = float(q0 - 1 / q0)
# EXPERIMENTAL-LAYER ANCHOR (owner directive 2026-08-07).  y_lambda is computed LIVE at the
# proton-pinned q0 rather than read from `y-lambda-at-q0.witness.json`, which is built at the
# IDEAL 3-CAL muon pin.  Mixing the two layers inside one Delta^2 g was a real defect --
# quantified in `mu3_anchor_consistency_probe.py` (11.54 ppb apart = the mu-p substrate
# tension; ~1e-7 relative on Delta^2 g, no conclusion changed).  Both y_lambda and chi are now
# evaluated at the SAME experimental anchor.  Scoped to this probe: this is NOT a migration of
# the ~840 muon-q0 computations/ witnesses, which stay canonical per AGENTS.md.
_Y9 = y_lambda_at_q0_mpmath(9, q0)

TOL = mp.mpf("1e-20")


def chi_dict(word):
    """Per-Wedderburn-block |χ_λ(w)| — the GEOMETRY, stripped of the weight y_λ."""
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(9, factors, q0f)
    return {tuple(s): abs(mp.mpf(repr(chi))) for s, chi in cp if tuple(s) in _Y9}


def classify(chi2, ra, rb, rab):
    """Regime label for a block, on the GEOMETRY only (weight handled separately)."""
    if ra is None:
        return "degenerate"                       # |χ|_∅ = 0, no damping coordinates
    if not (0 <= ra <= 1 and 0 <= rb <= 1):
        return "amplifying"                       # a bond raises |χ|; outside the Lean class
    return "frechet-violating" if chi2 < 0 else "frechet-obeying"


def main() -> int:
    print("=" * 92)
    print(" Per-block Fréchet test on the μ₃ sign door (adjacent H₉ joint-trace)")
    print("=" * 92)
    print(f" E₀ = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}   h = {H:.6f}")
    n_neg_y = sum(1 for v in _Y9.values() if v < 0)
    # The verdict follows the COUNT. It used to be appended unconditionally, so
    # under convention D it read "0 with y_λ < 0 → NOT weight-non-negative",
    # contradicting the number printed immediately before it.
    _wnn = "IS" if n_neg_y == 0 else "is NOT"
    print(f" Wedderburn weights at n=9: {len(_Y9)} blocks, {n_neg_y} with y_λ < 0"
          f"  → the spectrum {_wnn} weight-non-negative")

    expect_c3 = {"T": -1.769, "3He": -1.405}
    results, all_gates = {}, True
    tally_all = {}

    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        ifaces = {x[2]: x for x in full if x[2] % 3 == 2}
        ga, gb = sorted(ifaces)

        def chi_of(subset):
            return chi_dict([x for x in full if x[2] % 3 != 2 or x[2] in subset])

        c_e, c_a, c_b, c_ab = chi_of(set()), chi_of({ga}), chi_of({gb}), chi_of({ga, gb})
        blocks = sorted(set(c_e) & set(c_a) & set(c_b) & set(c_ab))

        rows, d2_sum, fact_ok = [], mp.mpf(0), True
        for lam in blocks:
            y = _Y9[lam]
            chi2 = c_ab[lam] - c_a[lam] - c_b[lam] + c_e[lam]        # geometry
            d2 = y * chi2                                            # contribution
            # factorisation gate: recompute d2 the weighted way
            d2_direct = (y * c_ab[lam] - y * c_a[lam] - y * c_b[lam] + y * c_e[lam])
            fact_ok = fact_ok and abs(d2 - d2_direct) < TOL
            d2_sum += d2
            if c_e[lam] > 0:
                ra, rb, rab = c_a[lam] / c_e[lam], c_b[lam] / c_e[lam], c_ab[lam] / c_e[lam]
                slack = rab - (ra + rb - 1)          # Fréchet slack; <0 ⟺ submodular geometry
            else:
                ra = rb = rab = slack = None
            rows.append((lam, y, chi2, d2, ra, rb, rab, slack, classify(chi2, ra, rb, rab)))

        # ---- GATE 1: linearity (the Lean `secondDiff_sum`) ----
        tot_e = sum(_Y9[l] * c_e[l] for l in blocks)
        tot_a = sum(_Y9[l] * c_a[l] for l in blocks)
        tot_b = sum(_Y9[l] * c_b[l] for l in blocks)
        tot_ab = sum(_Y9[l] * c_ab[l] for l in blocks)
        d2_total = tot_ab - tot_a - tot_b + tot_e
        lin_ok = abs(d2_sum - d2_total) < TOL

        # ---- GATE 2: baseline c₃ reproduces #4404 ----
        c3 = -E0 * d2_total
        base_ok = abs(float(c3) - expect_c3[name]) < 0.01
        all_gates = all_gates and lin_ok and base_ok and fact_ok

        tally = {}
        for r in rows:
            tally[r[8]] = tally.get(r[8], 0) + 1
        tally_all[name] = tally
        viol = [r for r in rows if r[8] == "frechet-violating"]
        negw = [r for r in rows if r[1] < 0]
        negw_push = [r for r in negw if r[3] < 0]   # negative weight pushing total submodular

        print(f"\n── {name} ── blocks={len(rows)}  Δ²g(total)={float(d2_total):+.6f}"
              f"  c₃={float(c3):+.4f} MeV (expect {expect_c3[name]:+.3f})")
        print(f"   gates: linearity {'OK' if lin_ok else 'FAIL'} |"
              f" factorisation {'OK' if fact_ok else 'FAIL'} |"
              f" baseline c₃ {'OK' if base_ok else 'FAIL'}")
        print(f"   geometry regimes: " + ", ".join(f"{k}={v}" for k, v in sorted(tally.items())))
        print(f"   → Fréchet-VIOLATING geometry (|χ| submodular, damping regime): {len(viol)}")
        print(f"   → negative-weight blocks: {len(negw)}, of which {len(negw_push)} push the"
              f" total submodular (Δ²_λ<0 via y_λ<0, NOT a Fréchet violation)")
        hdr = (f"   {'λ':<20}{'y_λ':>12}{'Δ²|χ|':>13}{'Δ²_λ':>13}"
               f"{'r_a':>9}{'r_b':>9}{'r_ab':>9}{'slack':>12}  regime")
        print(hdr)
        for lam, y, chi2, d2, ra, rb, rab, slack, reg in sorted(rows, key=lambda r: r[3]):
            def f(x):
                return f"{float(x):>9.5f}" if x is not None else f"{'--':>9}"
            sl = f"{float(slack):>12.3e}" if slack is not None else f"{'--':>12}"
            mark = "  ← VIOLATES" if reg == "frechet-violating" else ""
            print(f"   {str(lam):<20}{float(y):>+12.4e}{float(chi2):>+13.4e}"
                  f"{float(d2):>+13.4e}{f(ra)}{f(rb)}{f(rab)}{sl}  {reg}{mark}")

        results[name] = {
            "n_blocks": len(rows),
            "n_negative_weight": len(negw),
            "n_negative_weight_pushing_submodular": len(negw_push),
            "regime_tally": tally,
            "n_frechet_violating_geometry": len(viol),
            "frechet_violating_blocks": [str(r[0]) for r in viol],
            "d2_total": mp.nstr(d2_total, 20),
            "c3_MeV": mp.nstr(c3, 20),
            "linearity_ok": bool(lin_ok),
            "factorisation_ok": bool(fact_ok),
            "baseline_ok": bool(base_ok),
            "per_block": [
                {"lambda": str(r[0]), "y": mp.nstr(r[1], 20),
                 "d2_chi": mp.nstr(r[2], 20), "d2": mp.nstr(r[3], 20),
                 "r_a": (mp.nstr(r[4], 20) if r[4] is not None else None),
                 "r_b": (mp.nstr(r[5], 20) if r[5] is not None else None),
                 "r_ab": (mp.nstr(r[6], 20) if r[6] is not None else None),
                 "frechet_slack": (mp.nstr(r[7], 20) if r[7] is not None else None),
                 "regime": r[8]}
                for r in sorted(rows, key=lambda r: r[3])],
        }

    any_viol = any(results[k]["n_frechet_violating_geometry"] > 0 for k in results)
    print("\n" + "=" * 92)
    print(" RESULT")
    if any_viol:
        print("  * Fréchet-VIOLATING blocks EXIST and are named: the interfering block whose")
        print("    existence Mu3BlockwiseExclusion.submodular_needs_interfering_block requires")
        print("    is realised in this operator's own spectrum. The TOTAL still sums")
        print("    supermodular, so this does NOT by itself open the μ₃ door.")
    else:
        print("  * No block has submodular geometry in the damping regime.")
    if n_neg_y:
        print(f"  * The spectrum is NOT weight-non-negative (y_λ < 0 on {n_neg_y} of "
              f"{len(_Y9)} blocks), so the")
        print("    Lean escape-closure `reweight_cannot_open_door` (which assumes w_λ ≥ 0) does")
        print("    NOT apply here: re-weighting is not foreclosed on this spectrum.")
    else:
        print(f"  * The spectrum IS weight-non-negative ({n_neg_y} of {len(_Y9)} blocks "
              f"carry y_λ < 0), so the")
        print("    hypothesis of the Lean escape-closure `reweight_cannot_open_door` (w_λ ≥ 0)")
        print("    is SATISFIED here and the closure applies: re-weighting IS foreclosed on")
        print("    this spectrum. This INVERTS the conclusion this probe reported while the")
        print("    ≥3-row weights were convention-C nonzero — flagged, not wired.")
    print("=" * 92)

    w = WitnessBuilder("mu3-frechet-perblock", engine="pyhecke_native",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("linearity_gate", 1 if all_gates else 0, 1)
    w.add_assertion("frechet_violator_found", 1 if any_viol else 0,
                    1 if any_viol else 0)
    w.add_parameter("q0", mp.nstr(q0, 20))
    w.add_parameter("E0_MeV", mp.nstr(E0, 20))
    w.add_data("results", results)
    w.add_data("n_negative_y_lambda_at_9", n_neg_y)
    if n_neg_y:
        w.add_caveat(
            f"y_λ is NOT sign-definite at n=9 ({n_neg_y} of {len(_Y9)} weights negative), so "
            "a block's Δ²_λ<0 may come from submodular geometry OR from supermodular "
            "geometry carried by a negative weight. Only the former is a Fréchet violation; "
            "the two are reported separately. Consequently the Lean lemma "
            "reweight_cannot_open_door (hypothesis w_λ ≥ 0) does not apply to this spectrum."
        )
    else:
        w.add_caveat(
            f"y_λ IS sign-definite at n=9 ({n_neg_y} of {len(_Y9)} weights negative), so "
            "every Δ²_λ<0 is submodular geometry and the negative-weight ambiguity above "
            "does not arise. The hypothesis of reweight_cannot_open_door (w_λ ≥ 0) is "
            "SATISFIED, so that lemma applies and re-weighting is foreclosed on this "
            "spectrum. This inverts what this probe reported while the ≥3-row weights were "
            "convention-C nonzero; it is recorded as a consequence of the convention-D "
            "row cap, not as an independent derivation, and nothing is wired to it."
        )
    w.add_caveat(
        "Measurement only. No Δ_λ closure, no μ₃ value fitted, nothing wired to production."
    )
    w.set_description(
        "Per-block Fréchet test of the μ₃ sign door on the adjacent H₉ |χ|-joint-trace. "
        "Mu3BlockwiseExclusion.lean proves Δ² is linear over Wedderburn blocks and that a "
        "block is submodular iff its joint damping falls below the Fréchet–Hoeffding lower "
        "bound r_a+r_b−1; the per-block Δ²|χ|_λ sign is therefore exactly the per-block "
        "Fréchet test on the geometry. Gated on (i) linearity Σ_λΔ²_λ = Δ²g, (ii) the "
        "factorisation Δ²_λ = y_λ·Δ²|χ|_λ, and (iii) the #4404 baseline c₃ = −1.769 (T) / "
        "−1.405 (³He). No fit, nothing wired."
    )
    w.save()

    return 0 if all_gates else 1


if __name__ == "__main__":
    raise SystemExit(main())
