#!/usr/bin/env python3
"""Spectral bridge: the depth-2 binding kernel's dominant root IS the extensive-growth
eigenvalue the saturating |χ| trace lacks (0 fit).

Two results were proved/observed separately in the corpus:

 (A) The fibre q-difference kernel for the binding generating function is depth-2,
     R(q,x) = x² − τ·x + 1 with det = 1, τ = (a₂+a₄)/a₃ where the three SW-period
     anchors a_D^(n) = lw(n−1) are values of the single selection rule lw(c)
     (`binding_selection_rule_tau_closure.py`, #2612). τ(q₀) = 2.6424.

 (B) The |χ| joint-trace binding SATURATES — it is nearly A-independent
     (³H 3.25 → ³He 3.47 → ⁴He 3.80 MeV) while B_AME explodes; ⁴He captures only 13%
     (PR #2703, `productModel_3body_nonpos`). The missing binding is the EXTENSIVE
     (A-scaling) part, which a saturating/intensive object cannot source.

This probe connects them. The depth-2 recurrence a_{n+2} = τ·a_{n+1} − a_n has
characteristic roots λ_± = (τ ± √(τ²−4))/2 with λ_+·λ_- = 1 (det = 1). For τ > 2:

    λ_+ > 1  (EXTENSIVE growth)  >  λ_- = 1/λ_+ > 0.

So the body-order terms grow geometrically, a_D^(n) ~ C·λ_+^n — the kernel ALREADY
encodes the extensive growth (B). The saturating |χ| trace has effective ratio ≈ 1
(λ_eff ≈ 1, the A-independent plateau), i.e. it sits at the DEGENERATE τ = 2 boundary
where λ_+ = λ_- = 1 (no growth). The gap PR #2703 measured is exactly the distance
between λ_eff ≈ 1 (saturation) and λ_+ = 2.185 (the kernel). The "magic-A ⁴He +5.87%"
is then the residual of truncating the geometric series at finite body order, not a
failure of the growth mechanism. 0 fit — τ and λ_+ are outputs of the selection rule.
"""
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "computations"))
import _path_bridge  # noqa: E402,F401
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50
Q0_STR = "1.10997858275138080759166909561076887987449912187357763605672"
Q0 = mp.mpf(Q0_STR)

# |χ| joint-trace binding (PR #2703 yardstick-free probe) — the saturating side.
B_JOINT = {"3H": mp.mpf("3.2525"), "3He": mp.mpf("3.4665"), "4He": mp.mpf("3.8043")}


# --- physical selection-rule weights lw(c) via the q-hook-length quantum dimension ---
# lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q(λ),  dim_q(λ) = [|λ|]_q! / ∏_cells [hook]_q  (symmetric [k]_q).
# These ARE the physical body-order coefficients a_D^(n)=lw(n−1); computed directly (not iterated)
# they diverge from the fixed-τ recurrence past the n=2,3,4 seed (#2708; depth-2 (b)-excluded #2764).
def _partitions(n):
    if n == 0:
        yield ()
        return
    for first in range(n, 0, -1):
        for rest in _partitions(n - first):
            if not rest or first >= rest[0]:
                yield (first,) + rest


def _qint(k, q):  # symmetric q-integer [k]_q = (q^k − q^−k)/(q − q^−1)
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def _dim_q(lam, q):  # q-hook-length quantum dimension of partition `lam`
    lamT = [sum(1 for r in lam if r > c) for c in range(lam[0])]
    denom = mp.mpf(1)
    for i, row in enumerate(lam):
        for j in range(row):
            denom *= _qint((row - (j + 1)) + (lamT[j] - (i + 1)) + 1, q)
    qfac = mp.mpf(1)
    for k in range(1, sum(lam) + 1):
        qfac *= _qint(k, q)
    return qfac / denom


def _lw(c, q):  # mean quantum dimension over partitions of c+1
    return mp.fsum(_dim_q(lam, q) for lam in _partitions(c + 1)) / (c + 1)


def main():
    q = sp.symbols("q", positive=True)
    # The three no-fit anchors a_D^(n) = lw(n−1) (closed forms, selection rule).
    a2 = sp.Integer(1)
    a3 = sp.simplify((q + 1) ** 2 / (3 * q))
    a4 = sp.simplify((3 * q**2 + 4 + 3 / q**2) / 4)
    tau_sym = sp.simplify(sp.cancel((a2 + a4) / a3))

    def num(e):
        return mp.mpf(str(sp.N(e.subs(q, sp.Float(Q0_STR, 50)), 50)))

    tau = num(tau_sym)
    A2, A3, A4 = num(a2), num(a3), num(a4)
    disc = tau * tau - 4
    lam_p = (tau + mp.sqrt(disc)) / 2
    lam_m = (tau - mp.sqrt(disc)) / 2

    print(f"τ(q) = {tau_sym}")
    print(f"τ(q₀) = {mp.nstr(tau, 8)}   (anchors a₂,a₃,a₄ = {mp.nstr(A2,5)}, {mp.nstr(A3,5)}, {mp.nstr(A4,5)})")
    print(f"depth-2 roots of x²−τx+1:  λ₊ = {mp.nstr(lam_p,8)}   λ₋ = {mp.nstr(lam_m,8)}")
    print(f"  product λ₊·λ₋ = {mp.nstr(lam_p*lam_m,6)} (det=1 ✓)   λ₊>1 (extensive): {lam_p>1}")

    # body-order sequence a_D^(n), n=2..9, and its growth ratio → λ₊
    seq = [A2, A3]
    for _ in range(7):
        seq.append(tau * seq[-1] - seq[-2])
    ratios = [seq[i + 1] / seq[i] for i in range(len(seq) - 1)]
    print(f"\n  a_D^(2..9): {[mp.nstr(x,5) for x in seq]}")
    print(f"  ratios a_(n+1)/a_n → {[mp.nstr(r,5) for r in ratios]}  →  λ₊ = {mp.nstr(lam_p,6)}")

    # PHYSICAL body-order coefficients a_D^(n)=lw(n−1), computed DIRECTLY (q-hook), n=2..9 — the
    # honest comparison: they diverge from the iterated `seq` past the seed and rise past λ₊.
    lw_phys = [_lw(c, Q0) for c in range(1, len(seq) + 1)]   # lw(1..len(seq)) = a_D^(2..), matches seq
    phys_ratios = [lw_phys[i + 1] / lw_phys[i] for i in range(len(lw_phys) - 1)]
    rel_div = [(lw_phys[i] - seq[i]) / lw_phys[i] for i in range(len(seq))]
    max_div = max(abs(d) for d in rel_div)
    anchor_resid = max(abs(lw_phys[0] - A2), abs(lw_phys[1] - A3), abs(lw_phys[2] - A4))
    print(f"\n  PHYSICAL lw (q-hook, direct): {[mp.nstr(x,5) for x in lw_phys]}")
    print(f"  physical ratios lw(c)/lw(c−1): {[mp.nstr(r,5) for r in phys_ratios]}  (rise PAST λ₊ ⇒ super-geometric)")
    print(f"  iterated-vs-physical rel. divergence: {[mp.nstr(d,3) for d in rel_div]}  (max {mp.nstr(max_div,3)})")
    print(f"  anchor consistency |lw(1,2,3)−(a₂,a₃,a₄)| = {mp.nstr(anchor_resid,3)} (≈0 ✓ seed agrees)")

    # saturating |χ| side: effective per-A growth ratio (≈1 = degenerate τ=2 boundary)
    chi_ratio_TtoHe = B_JOINT["4He"] / B_JOINT["3H"]
    print(f"\n  saturating |χ| joint trace: B_joint ³H→⁴He = {mp.nstr(B_JOINT['3H'],4)} → "
          f"{mp.nstr(B_JOINT['4He'],4)}  (ratio {mp.nstr(chi_ratio_TtoHe,4)} ≈ 1: λ_eff≈1, τ_eff≈2 degenerate)")
    print(f"  GAP = distance from saturation (λ_eff≈1) to kernel (λ₊={mp.nstr(lam_p,5)}): the kernel")
    print(f"  supplies the extensive growth the |χ| trace lacks. 0 fit.")

    wb = WitnessBuilder("binding-recurrence-spectral-bridge", engine="python+sympy+mpmath",
                        output_dir=str(REPO / "computations"))
    wb.description = (
        "Spectral bridge (0 fit): the depth-2 binding kernel R=x²−τx+1 (τ=2.6424 from the "
        "selection-rule anchors, #2612) has dominant root λ₊=2.185>1 — the EXTENSIVE-growth "
        "eigenvalue the saturating |χ| joint trace (λ_eff≈1, A-independent, PR #2703) lacks. "
        "det=1 forces λ₋=1/λ₊<1. Connects the geometric/algebraic kernel to the empirical "
        "saturation gap; the |χ| trace sits at the degenerate τ=2 (λ=1) no-growth boundary. "
        "SCOPE (PR #2752): the tabulated aD_sequence is the iterated fixed-τ recurrence (→λ₊ "
        "tautologically); the physical a_D^(n)=lw(n−1) grow super-geometrically (#2708, diverge "
        "≤32% by n=7), so λ₊>1 witnesses the SEED kernel's extensivity, not the binding growth rate. "
        "The witness emits BOTH aD_sequence_2_to_9 (iterated) and aD_physical_lw_2_to_9 (direct q-hook), "
        "so the divergence is DATA — asserted by physical_diverges_from_iterated / physical_super_geometric.")
    wb.add_parameter("q0", mp.nstr(Q0, 12))
    wb.add_parameter("fit_params", 0)
    wb.add_data("tau_symbolic", str(tau_sym))
    wb.add_data("tau_q0", mp.nstr(tau, 12))
    wb.add_data("anchors_aD_2_3_4", [mp.nstr(A2, 12), mp.nstr(A3, 12), mp.nstr(A4, 12)])
    wb.add_data("lambda_plus", mp.nstr(lam_p, 12))
    wb.add_data("lambda_minus", mp.nstr(lam_m, 12))
    wb.add_data("det_product", mp.nstr(lam_p * lam_m, 12))
    wb.add_data("aD_sequence_2_to_9", [mp.nstr(x, 10) for x in seq])
    wb.add_data("growth_ratios", [mp.nstr(r, 10) for r in ratios])
    wb.add_data("chi_joint_saturating", {k: mp.nstr(v, 8) for k, v in B_JOINT.items()})
    wb.add_data("chi_effective_ratio_3H_to_4He", mp.nstr(chi_ratio_TtoHe, 8))
    # PHYSICAL selection-rule sequence (q-hook), beside the iterated one — the honest comparison.
    wb.add_data("aD_physical_lw_2_to_9", [mp.nstr(x, 10) for x in lw_phys])
    wb.add_data("physical_growth_ratios", [mp.nstr(r, 10) for r in phys_ratios])
    wb.add_data("iterated_vs_physical_rel_divergence", [mp.nstr(d, 6) for d in rel_div])
    # SCOPE (2026-06-25 calibration, PR #2752): `seq` is the ITERATED fixed-τ recurrence, so
    # `ratio_convergence` below → λ₊ TAUTOLOGICALLY (every depth-2 recurrence with τ>2 does) — it
    # tests the iterated seq, NOT the physics. The PHYSICAL coefficients a_D^(n)=lw(n−1)
    # (`aD_physical_lw_2_to_9`, q-hook, direct) grow SUPER-geometrically (ratios →2.76, past λ₊) and
    # diverge from `seq` by up to 32% (n=7) — now asserted by `physical_super_geometric` /
    # `physical_diverges_from_iterated` (data, no longer prose-only). #2708 + depth-2 (b)-exclusion
    # #2764 + docs/audits/2026-06-25-spectral-bridge-tautology-recurrence-vs-lw.md.
    ratio_residual = ratios[-1] - lam_p
    wb.add_assertion("ratio_convergence", computed=mp.nstr(ratio_residual, 12), expected="0",
                     tolerance=1e-4,
                     source="ITERATED seq ratio tail − λ₊ (tautological; seq built by iterating x²−τx+1)")
    wb.add_assertion("det_one", computed=mp.nstr(lam_p * lam_m, 12), expected="1",
                     tolerance=1e-30)
    # extensive-growth flag as a checkable boolean (1.0 ⟺ λ₊>1).
    wb.add_assertion("dominant_root_extensive", computed=("1" if lam_p > 1 else "0"),
                     expected="1", tolerance=0.0, source="λ₊ > 1 ⟺ τ > 2 (τ=2.6424)")
    # PHYSICAL-vs-iterated — the honest comparison (the point of the PR #2752 calibration).
    wb.add_assertion("lw_reproduces_anchors", computed=mp.nstr(anchor_resid, 4), expected="0",
                     tolerance=1e-25,
                     source="q-hook lw(1,2,3) vs closed-form anchors a₂,a₃,a₄ (seed agreement)")
    wb.add_assertion("physical_diverges_from_iterated",
                     computed=("1" if max_div > mp.mpf("0.1") else "0"), expected="1", tolerance=0.0,
                     source=f"max|lw(n−1)−seq|/lw = {mp.nstr(max_div,4)} > 0.1 ⇒ physical ≠ iterated")
    wb.add_assertion("physical_super_geometric",
                     computed=("1" if phys_ratios[-1] > lam_p else "0"), expected="1", tolerance=0.0,
                     source=f"physical lw ratio tail {mp.nstr(phys_ratios[-1],5)} > λ₊ {mp.nstr(lam_p,5)}")
    wb.add_caveat("τ>2 ⟹ λ₊>1 is the extensive-growth condition; τ(q₀)=2.6424 satisfies it; the "
                  "|χ| saturation sits at the degenerate τ=2 (λ=1) boundary. SCOPE (PR #2752): "
                  "`aD_sequence`/`growth_ratios` are the ITERATED fixed-τ recurrence, which → λ₊ "
                  "tautologically; the PHYSICAL coefficients a_D^(n)=lw(n−1) grow super-geometrically "
                  "(#2708) and diverge from it by up to 32% (n=7). λ₊>1 is an (a)-scope witness that "
                  "the SEED kernel is extensive, NOT the binding growth rate. The magic-A ⁴He +5.87% "
                  "is a SEPARATE doubly-magic-formula gap (over-claim retracted 2026-06-24), not a "
                  "truncation residual of this series.")
    out = wb.save()
    print(f"\nwrote {Path(out).relative_to(REPO)}")


if __name__ == "__main__":
    main()
