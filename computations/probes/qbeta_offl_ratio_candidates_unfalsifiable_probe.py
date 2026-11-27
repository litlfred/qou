#!/usr/bin/env python3
"""qbeta_offl_ratio_candidates_unfalsifiable_probe.py — bean qou-offl: a design
constraint on the cone-manifold route, derived before running it.

CONTEXT. qou-rdmr is refuted at scope (a), leaving qou-offl (cone-manifold /
generalized Dehn filling) as the arc's live independent-ϑ leg. The A_ω-free
constraint curve (qbeta_qnnq_afree_theta_constraint_probe.py)

    (L − ϑ_μ²)/(L − ϑ_p²) = S_μ/S_p = r,      L = ln²q₀

gives that route a well-posed acceptance test. Before running any geometry,
this probe asks what SHAPE a candidate must have to be testable at all — the
formalize-first discipline: narrow the search before running it.

THE CLAIM TO TEST. A cone-manifold route could supply either
  (i)  a RATIO ϑ_p/ϑ_μ from some parameter-free geometric quantity, or
  (ii) BOTH ϑ values absolutely.
These are not equally good, and the difference is decisive.

Counting: two anchor equations, three unknowns (A_ω, ϑ_μ, ϑ_p). One extra
scalar closes the system EXACTLY — zero residual, nothing to check. Two extra
scalars over-determine it by one and leave a residual that can fail. So (i) is
unfalsifiable by construction and (ii) is a genuine test.

This probe makes that concrete rather than merely asserting it:

  U1  EXHAUSTIVENESS. Traverse A over [A_crit, ∞) and show the induced ratio
      ρ(A) = ϑ_p/ϑ_μ is a monotone bijection onto (1, ∞). If every ρ > 1 is
      attained by exactly one A, then NO ratio candidate can ever be refuted —
      each merely names a different A. That is the formal content of "(i) is
      unfalsifiable".
  U2  THE DISCRIMINATOR TABLE. For a list of parameter-free geometric ratios
      that a cone-manifold route might plausibly produce, report the A each
      would force. This is emphatically NOT a menu to pick from — it is the
      demonstration that plausible-looking candidates all land near A ≈ 3, so
      a ratio match near 3 is nearly guaranteed and buys almost nothing.
  U3  SENSITIVITY. Quantify that: what band of ρ maps into A ∈ [2.5, 4]? A
      candidate whose ratio falls in that band is "consistent with A ≈ 3" for
      reasons that have nothing to do with it being correct.

Scope (STRICT). Derives no value of A_ω, proposes no ϑ, wires nothing. It is a
NEGATIVE design result: it rules a whole SHAPE of candidate out of contention
on falsifiability grounds, before any geometry is computed. The geometric
quantities in U2 are illustrative inputs, not claims about which is right.

Run: python3 -u computations/probes/qbeta_offl_ratio_candidates_unfalsifiable_probe.py \
       2>&1 | tee /tmp/qbeta_offl_ratio.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
KAPPA = mp.sqrt(3) / 4
# Canonical proton-pinned substrate modulus, READ not typed. The T4 probe's old
# literal 1.11020 was a unit conflation (it solved 2*ln q = h instead of using
# q0); fixed 2026-08-07, which moved the derived theta by -0.60% / -0.05%.
Q0 = Q_MP

VOL_41 = mp.mpf("2.029883212819307")     # figure-eight
VOL_BOR = mp.mpf("7.327724753")          # Borromean rings


def theta_pair(A, L):
    """(ϑ_μ, ϑ_p) at a given A; None if ϑ_μ has gone imaginary."""
    tm2 = L - S_MUON / (KAPPA * A)
    tp2 = L - S_PROTON / (KAPPA * A)
    if tm2 <= 0:
        return None
    return mp.sqrt(tm2), mp.sqrt(tp2)


def A_forced_by_ratio(rho, L):
    """Invert ρ = ϑ_p/ϑ_μ for A.  ρ² = (L − S_p t)/(L − S_μ t), t = 1/(κA)."""
    num = L * (rho**2 - 1)
    den = rho**2 * S_MUON - S_PROTON
    t = num / den
    if t <= 0:
        return None
    return 1 / (KAPPA * t)


def main() -> int:
    print("=" * 78)
    print(" qou-offl — why a RATIO candidate cannot be tested, and what can")
    print("=" * 78)

    L = mp.log(Q0) ** 2
    A_crit = S_MUON / (KAPPA * L)
    print(f"\n  L = ln²q₀ = {mp.nstr(L, 12)}     A_crit = {mp.nstr(A_crit, 10)}")

    # ---- U1: is ρ(A) a monotone bijection onto (1, ∞)? ----
    print("\n[U1] EXHAUSTIVENESS — traverse A and watch the induced ratio:")
    # Sample points DERIVED from A_crit, not hardcoded. The first two used to
    # be the literals "2.0462"/"2.05", tuned to the A_crit of a superseded q0;
    # when q0 was corrected (A_crit 2.046 -> 2.054) they fell BELOW the critical
    # value, were skipped as infeasible, and the exhaustiveness check failed on
    # a sampling artifact rather than on any change to the mathematics. Deriving
    # them keeps the probe correct under any q0.
    As = [A_crit * (1 + mp.mpf("1e-6")), A_crit * (1 + mp.mpf("2e-3"))] + \
         [mp.mpf(x) for x in ("2.2", "2.6", "3.0", "4.0", "8.0", "50.0", "1000.0")]
    prev, monotone, rows = None, True, []
    exact = []           # full-precision (A, rho) pairs for the round-trip
    for A in As:
        a = mp.nstr(A, 8)
        pair = theta_pair(A, L)
        if pair is None:
            continue
        tm, tp = pair
        rho = tp / tm
        exact.append((A, rho))
        rows.append({"A": mp.nstr(A, 10), "rho": mp.nstr(rho, 10)})
        print(f"    A = {a:>9}   ρ = ϑ_p/ϑ_μ = {mp.nstr(rho, 12):>16}")
        if prev is not None and rho >= prev:
            monotone = False
        prev = rho
    rho_hi = exact[0][1]
    rho_lo = exact[-1][1]
    print(f"\n    ρ is monotone decreasing in A: {monotone}")
    print(f"    range covered by the sample: ρ ∈ [{mp.nstr(rho_lo, 8)}, "
          f"{mp.nstr(rho_hi, 8)}]  →  A→∞ gives ρ→1, A→A_crit⁺ gives ρ→∞")
    exhaustive = monotone and rho_lo < mp.mpf("1.02") and rho_hi > mp.mpf("20")
    print(f"    ⇒ every ρ > 1 is attained by exactly one A: {exhaustive}")
    print("      Hence NO ratio candidate can be refuted — each merely names an A.")

    # Round-trip the inversion at FULL precision. Doing it on the 10-digit
    # display strings instead reads ~3e-5, which is the re-parse, not the
    # inversion: near A_crit the map is stiff (ρ ≈ 598), so a 10th-digit
    # perturbation in ρ moves A in the 5th.
    rt = max(abs(A_forced_by_ratio(rho, L) - A) / A for A, rho in exact)
    print(f"    (inversion round-trip max RELATIVE error, full precision: "
          f"{mp.nstr(rt, 4)})")

    # ---- U2: the discriminator table ----
    print("\n[U2] DISCRIMINATOR TABLE — the A each plausible geometric ratio forces.")
    print("     NOT a menu. The point is how tightly they cluster.")
    cands = {
        "Vol(𝔹₃)/Vol(4₁)": VOL_BOR / VOL_41,
        "2√3  (|cusp modulus| of 4₁)": 2 * mp.sqrt(3),
        "cusp count 3/1": mp.mpf(3),
        "√(Vol ratio)": mp.sqrt(VOL_BOR / VOL_41),
        "crossing number 6/4": mp.mpf("1.5"),
        "|disc| 4/3": mp.mpf(4) / 3,
    }
    print(f"     {'candidate ratio':<30} {'ρ':>10}   {'A forced':>10}")
    tbl = []
    for name, rho in cands.items():
        A = A_forced_by_ratio(rho, L)
        s = mp.nstr(A, 8) if A is not None else "none (ρ ≤ 1)"
        tbl.append({"candidate": name, "rho": mp.nstr(rho, 10),
                    "A_forced": s})
        print(f"     {name:<30} {mp.nstr(rho, 8):>10}   {s:>10}")
    near3 = [t for t in tbl if t["A_forced"] != "none (ρ ≤ 1)"
             and mp.mpf(t["A_forced"]) > mp.mpf("2.5")
             and mp.mpf(t["A_forced"]) < mp.mpf("4")]
    print(f"\n     {len(near3)} of {len(tbl)} candidates land in A ∈ [2.5, 4] — "
          f"i.e. 'consistent with A ≈ 3'.")

    # ---- U3: sensitivity band ----
    rho_at_25 = theta_pair(mp.mpf("2.5"), L)
    rho_at_40 = theta_pair(mp.mpf("4.0"), L)
    band_hi = rho_at_25[1] / rho_at_25[0]
    band_lo = rho_at_40[1] / rho_at_40[0]
    print(f"\n[U3] SENSITIVITY — A ∈ [2.5, 4.0] corresponds to "
          f"ρ ∈ [{mp.nstr(band_lo, 8)}, {mp.nstr(band_hi, 8)}].")
    print(f"     Any candidate ratio anywhere in that ~2× band reads as "
          f"'A ≈ 3 within 33%'. A ratio match is therefore weak evidence even "
          f"when the quantity was fixed in advance.")

    verdict = (
        "RATIO-SHAPED CANDIDATES ARE UNFALSIFIABLE — a design constraint on "
        "qou-offl derived BEFORE running any geometry. The channel has two "
        "anchor equations in three unknowns, so one extra scalar closes the "
        "system with zero residual and nothing left to check. U1 makes this "
        "concrete: ρ(A) = ϑ_p/ϑ_μ is a monotone bijection from A ∈ (A_crit, ∞) "
        "onto ρ ∈ (1, ∞), so EVERY ratio above 1 is attained by exactly one A "
        "and no ratio candidate can ever be refuted — it can only NAME an A. "
        "U2 shows the practical damage: plausible parameter-free geometric "
        f"ratios cluster, {len(near3)} of {len(tbl)} landing in A ∈ [2.5, 4], "
        "so a 'match near 3' is close to guaranteed. U3 quantifies it — that "
        "whole A range is a mere ~2x band in ρ. CONSEQUENCE FOR qou-offl: the "
        "route must supply BOTH ϑ values ABSOLUTELY, from a normalization "
        "fixed in advance, not their ratio and not one anchor. Only then is "
        "the system over-determined by one and only then does the A-free curve "
        "produce a residual that can fail. SCOPE: this derives no value of "
        "A_omega, endorses no candidate, and wires nothing; the geometric "
        "ratios are illustrative inputs. It is a negative result about the "
        "SHAPE of an admissible route."
        if exhaustive else
        "INCONCLUSIVE — the exhaustiveness check did not establish the "
        "bijection; inspect the U1 sample.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-offl-ratio-candidates-unfalsifiable", engine="mpmath")
    wb.set_description(
        "Bean qou-offl: a formalize-first design constraint on the "
        "cone-manifold route, derived before running any geometry. The channel "
        "has 2 anchor equations in 3 unknowns, so one extra scalar (a ratio "
        "theta_p/theta_mu) closes it with zero residual and cannot be tested. "
        "Established concretely: rho(A) is a monotone bijection from "
        "A in (A_crit, infinity) onto rho in (1, infinity), so every ratio "
        "above 1 is attained by exactly one A and no ratio candidate is "
        "refutable — it only names an A. Plausible geometric ratios moreover "
        "cluster into A in [2.5, 4], making a 'match near 3' near-guaranteed. "
        "Consequence: qou-offl must supply BOTH theta values absolutely, from "
        "a normalization fixed in advance. Derives no A_omega; endorses no "
        "candidate; wires nothing.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("counting_argument",
                "2 anchor equations, 3 unknowns (A_omega, theta_mu, theta_p); "
                "1 extra scalar closes exactly (no residual), 2 extra scalars "
                "over-determine by 1 (testable residual)")
    wb.add_data("U1_ratio_traverse", rows)
    wb.add_data("U1_monotone", bool(monotone))
    wb.add_data("U1_bijection_onto_gt1", bool(exhaustive))
    wb.add_data("U1_inversion_roundtrip_max_rel_err", mp.nstr(rt, 8))
    wb.add_data("U2_discriminator_table", tbl)
    wb.add_data("U2_count_in_A_2p5_to_4", len(near3))
    wb.add_data("U3_rho_band_for_A_2p5_to_4",
                [mp.nstr(band_lo, 10), mp.nstr(band_hi, 10)])
    wb.add_data("design_constraint_for_offl",
                "supply BOTH theta values absolutely from a normalization fixed "
                "in advance; a ratio, or a single anchor, is untestable")
    wb.add_data("scope",
                "negative design result about the SHAPE of an admissible route; "
                "no A_omega derived, no candidate endorsed, nothing wired")
    wb.add_data("verdict", verdict)
    wb.add_assertion("ratio_map_is_bijection",
                     computed="1" if exhaustive else "0", expected="1",
                     tolerance="0.5",
                     source="rho(A) monotone decreasing, ->1 as A->infinity and "
                            "->infinity as A->A_crit+, hence onto (1, infinity)")
    wb.add_assertion("inversion_roundtrip_exact",
                     computed=mp.nstr(rt, 20), expected="0", tolerance="1e-20",
                     source="A_forced_by_ratio inverts theta_pair on the U1 "
                            "sample at full precision (relative error)")
    wb.save()
    print("  witness -> computations/probes/"
          "qbeta-offl-ratio-candidates-unfalsifiable.witness.json")
    return 0 if exhaustive else 1


if __name__ == "__main__":
    raise SystemExit(main())
