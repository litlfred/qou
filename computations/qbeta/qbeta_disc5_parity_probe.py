#!/usr/bin/env python3
"""qbeta_disc5_parity_probe.py — the Bring/disc-5 parity test: does the WINDING
PARITY of the braid word carry the S-channel sign flip?

Author steering (2026-07-27): the geodesic/flow picture "is mapped on Bring's
surface"; "odd and even channels ... sinh/cosh should align at this geometry".

WHY disc-5 AND NOT disc-12 (the structural point, derived — this is the whole
reason Bring's surface enters). The [W] probe derived, on the 4₁ CUSP TORUS,

    Im 𝔙₄₁ = (√3/16)(ln q₀)²·[(2m+ℓ)² − 3ℓ²]        (ℤ[√3], disc 12)

whose fundamental unit 2+√3 has norm **+1**. Every power (2+√3)ⁿ therefore has
norm +1: the cusp-torus lattice admits NO parity-driven sign flip — consistent
with [W], where the flip had to come from the winding *slope* instead. Bring's
surface carries the golden order ℤ[φ], φ=(1+√5)/2, whose fundamental unit φ has
norm **−1**, so N(φⁿ) = (−1)ⁿ: a sign flip driven by winding PARITY exists there
and cannot exist on the cusp torus. That contrast is the derived content here.

CHECK (assertions):
  [D1] N(φⁿ) = (−1)ⁿ concretely: L_n² − 5F_n² = 4(−1)ⁿ (Lucas/Fibonacci), while
       the disc-12 analogue x_n² − 3y_n² = +1 for ALL n. Parity flip exists in
       ℤ[φ], provably absent in ℤ[√3].
  [D2] SINH/COSH CHANNEL SWAP BY PARITY (the author's "odd and even channels").
       With x = φⁿ and the proved bar-split barEven(x)=x+x⁻¹, barOdd(x)=x−x⁻¹:
         n even → (barEven, barOdd) = (L_n, F_n√5) = (2cosh nρ, 2sinh nρ)
         n odd  → (barEven, barOdd) = (F_n√5, L_n) = (2cosh nρ, 2sinh nρ)
       i.e. WHICH of the two integer sequences is the cosh and which is the sinh
       SWAPS with the parity of n, ρ = ln φ. Both satisfy the proved holonomy
       hyperbola barEven² − barOdd² = 4.
  [D3] SIGN PREDICTION vs the anchors, parameter-free. The canonical braid words
       are powers of the half-figure-eight w = σ₁σ₂⁻¹ (corpus,
       `fundamental-knots-operator-basis`): 4₁ = w² (muon anchor, n=2, EVEN) and
       Borromean L6a4 = w³ (nucleon/proton, n=3, ODD). The parity rule
       sign S = N(φⁿ) = (−1)ⁿ predicts  muon +, proton −.
       Observed: S(muon) > 0, S(proton) < 0.  ⇒ 2/2, no tuning.
  [D4] HONEST NEGATIVE — magnitudes. |N(φⁿ)| = 1 for every n, so the parity rule
       alone predicts EQUAL magnitudes; the observed |S_proton/S_muon| ≈ 4.075.
       Natural φ-flavoured ratios (φ³, L₃/L₂, F₃/F₂, cosh/sinh ratios at ρ=ln φ)
       all miss by ≫ the 0.1% that would be persuasive. Magnitudes stay OPEN and
       are NOT pursued here — with cusp shapes dense in Teichmüller space
       (Dang–Purcell, library/cuspshapes/CuspShapes.pdf) magnitude-chasing is a fit trap.

SCOPE (stated plainly). [D1] and [D2] are theorems of the quadratic orders and
are Lean-formalised alongside this probe. [D3] is a 2-bit derive-then-check hit:
the sign rule is parameter-free and gets both anchors right. But the LINK from
"winding parity" to "sign of the S-channel" is DERIVED only on the disc-12 cusp
torus ([W]); on Bring's surface it is transported by ANALOGY — the Bring-side
complex-volume computation is not done here. So [D3] is a *conjectural* mechanism
supported by 2 bits, not a derivation. Labelled, not buried. No fit, no c_k, no
instance, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
PHI = (1 + mp.sqrt(5)) / 2
RHO5 = mp.log(PHI)                       # Bring/golden fundamental rapidity
RHO3 = mp.log(2 + mp.sqrt(3))            # cusp-torus fundamental rapidity (= arccosh 2)

# canonical braid words: powers of the half-figure-eight w = σ₁σ₂⁻¹ (corpus)
KNOT_POWER = {"muon (4₁ = w²)": 2, "proton (Borromean L6a4 = w³)": 3}


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def lucas_fib(n: int) -> tuple[int, int]:
    """(L_n, F_n) by integer recursion — no floating point."""
    L0, L1, F0, F1 = 2, 1, 0, 1
    for _ in range(n):
        L0, L1 = L1, L0 + L1
        F0, F1 = F1, F0 + F1
    return L0, F0


def pell3(n: int) -> tuple[int, int]:
    """(x_n, y_n) with x_n + y_n√3 = (2+√3)ⁿ — the disc-12 units."""
    x, y = 1, 0
    for _ in range(n):
        x, y = 2 * x + 3 * y, x + 2 * y
    return x, y


def main() -> int:
    print("=" * 78)
    print(" disc-5 PARITY: does the braid-word winding parity carry the S sign flip?")
    print("=" * 78)
    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_mu, S_pr = S(q_mu), S(q_pr)
    print(f"\n anchors: S(muon) = {mp.nstr(S_mu,7)} (+)   S(proton) = {mp.nstr(S_pr,7)} (−)")
    print(f" ρ₅ = ln φ = {mp.nstr(RHO5,10)}   (Bring/golden)")
    print(f" ρ₃ = ln(2+√3) = arccosh 2 = {mp.nstr(RHO3,10)}   (cusp torus)")

    # ---- [D1] parity flip exists in ℤ[φ], provably absent in ℤ[√3] -----------
    print("\n [D1] norm of the fundamental unit: ℤ[φ] → −1 (flip),  ℤ[√3] → +1 (no flip)")
    print("      n   L_n   F_n   L²−5F² |   x_n   y_n   x²−3y²")
    d1_gold, d1_silver = True, True
    for n in range(0, 8):
        Ln, Fn = lucas_fib(n)
        xn, yn = pell3(n)
        g, s = Ln * Ln - 5 * Fn * Fn, xn * xn - 3 * yn * yn
        d1_gold &= (g == 4 * (-1) ** n)
        d1_silver &= (s == 1)
        print(f"      {n}  {Ln:4d}  {Fn:4d}  {g:6d} | {xn:5d} {yn:5d}   {s:4d}")
    d1 = d1_gold and d1_silver
    print(f"      L_n²−5F_n² = 4(−1)ⁿ : {d1_gold}     x_n²−3y_n² = +1 ∀n : {d1_silver}")
    print("      ⇒ a PARITY-driven sign flip is available on Bring (disc 5) and")
    print("        structurally UNAVAILABLE on the cusp torus (disc 12).")

    # ---- [D2] sinh/cosh channel swap by parity ------------------------------
    print("\n [D2] bar-split of x = φⁿ: which integer sequence is cosh vs sinh SWAPS with parity")
    d2 = True
    print("      n  par   barEven=φⁿ+φ⁻ⁿ   barOdd=φⁿ−φ⁻ⁿ   identified as        hyperbola")
    for n in range(1, 7):
        Ln, Fn = lucas_fib(n)
        x = PHI ** n
        be, bo = x + 1 / x, x - 1 / x
        if n % 2 == 0:
            name, ok = "(L_n, F_n√5)", abs(be - Ln) < mp.mpf("1e-30") and abs(bo - Fn * mp.sqrt(5)) < mp.mpf("1e-30")
        else:
            name, ok = "(F_n√5, L_n)", abs(be - Fn * mp.sqrt(5)) < mp.mpf("1e-30") and abs(bo - Ln) < mp.mpf("1e-30")
        hyp = abs(be * be - bo * bo - 4) < mp.mpf("1e-30")
        d2 &= ok and hyp
        print(f"      {n}  {'even' if n%2==0 else 'odd ':4s}  {mp.nstr(be,9):>14} {mp.nstr(bo,9):>14}   "
              f"{name:14s}  {'✓' if hyp else '✗'}")
    print(f"      all identifications + barEven²−barOdd²=4 (proved) hold: {bool(d2)}")

    # ---- [D3] the parameter-free sign prediction ----------------------------
    print("\n [D3] parity rule  sign S = N(φⁿ) = (−1)ⁿ  vs the anchors (no tuning)")
    obs = {"muon (4₁ = w²)": S_mu, "proton (Borromean L6a4 = w³)": S_pr}
    d3 = True
    for name, n in KNOT_POWER.items():
        pred = (-1) ** n
        got = 1 if obs[name] > 0 else -1
        d3 &= (pred == got)
        print(f"      {name:30s} n={n} {'even' if n%2==0 else 'odd '}  "
              f"predicted {pred:+d}   observed {got:+d}   {'MATCH' if pred==got else 'MISS'}")
    print(f"      ⇒ 2/2 anchors, parameter-free: {bool(d3)}")

    # ---- [D4] honest negative: magnitudes ----------------------------------
    obs_ratio = abs(S_pr / S_mu)
    cands = {
        "|N(φ³)/N(φ²)| (the parity rule itself)": mp.mpf(1),
        "φ³": PHI ** 3,
        "φ": PHI,
        "L₃/L₂": mp.mpf(lucas_fib(3)[0]) / lucas_fib(2)[0],
        "F₃/F₂": mp.mpf(lucas_fib(3)[1]) / lucas_fib(2)[1],
        "cosh(3ρ₅)/cosh(2ρ₅)": mp.cosh(3 * RHO5) / mp.cosh(2 * RHO5),
        "sinh(3ρ₅)/sinh(2ρ₅)": mp.sinh(3 * RHO5) / mp.sinh(2 * RHO5),
        "φ⁵/φ²": PHI ** 3,
    }
    print(f"\n [D4] magnitudes: observed |S_proton/S_muon| = {mp.nstr(obs_ratio,8)}")
    best, best_miss = None, None
    for k, v in cands.items():
        miss = abs(v - obs_ratio) / obs_ratio * 100
        if best_miss is None or miss < best_miss:
            best, best_miss = k, miss
        print(f"      {k:40s} = {mp.nstr(v,8):>10}   miss {mp.nstr(miss,4)}%")
    d4 = best_miss > mp.mpf("0.1")     # nothing lands near the persuasive threshold
    print(f"      best candidate: {best} at {mp.nstr(best_miss,4)}% — ≫ the 0.1% that would")
    print(f"      be persuasive ⇒ magnitudes NOT explained, left OPEN: {bool(d4)}")
    print("      (cusp shapes are dense in Teichmüller space — Dang–Purcell — so")
    print("       magnitude-chasing by knot/cusp selection is a fit trap. Not pursued.)")

    print("\n ⇒ PARITY carries the SIGN (2/2, parameter-free) and Bring's disc-5 order is")
    print("   structurally the ONLY one of the two that can (N(fund. unit) = −1 vs +1).")
    print("   The parity→S-sign LINK is derived on the disc-12 cusp torus and transported")
    print("   to Bring by ANALOGY — conjectural, not a derivation. Magnitudes open.")

    wb = WitnessBuilder("qbeta-disc5-parity", engine="mpmath")
    wb.set_description(
        "disc-5 parity test (#4401, continuation of the [W] winding-lattice probe): does the "
        "braid word's winding PARITY carry the S-channel sign flip, via Bring's golden order "
        "ℤ[φ]? Derived structural contrast: the cusp-torus order ℤ[√3] has fundamental unit "
        "2+√3 of norm +1, so x_n²−3y_n² = +1 for ALL n — no parity flip is available there; "
        "Bring's ℤ[φ] has fundamental unit φ of norm −1, so L_n²−5F_n² = 4(−1)ⁿ — the parity "
        "flip exists on Bring and is structurally impossible on the cusp torus. The bar-split "
        "of x = φⁿ shows the author's odd/even channel structure exactly: which of (L_n, F_n√5) "
        "is the cosh and which the sinh SWAPS with the parity of n, both obeying the proved "
        "barEven²−barOdd²=4. Sign check, parameter-free: canonical braid words are powers of "
        "w = σ₁σ₂⁻¹ (4₁ = w², n=2 even; Borromean L6a4 = w³, n=3 odd), and the rule "
        "sign S = (−1)ⁿ predicts muon + / proton − — matching both observed anchors, 2/2, with "
        "no tuning. HONEST SCOPE: the parity→S-sign LINK is derived only on the disc-12 cusp "
        "torus ([W]); on Bring it is transported by ANALOGY (the Bring-side complex-volume "
        "computation is not done) — a conjectural mechanism supported by 2 bits, not a "
        "derivation. HONEST NEGATIVE: |N(φⁿ)| = 1 ∀n predicts equal magnitudes vs the observed "
        "ratio 4.075; the best natural φ-candidate misses by ≫0.1%. Magnitudes left open and "
        "not pursued — cusp shapes are dense in Teichmüller space (Dang–Purcell), making "
        "magnitude-chasing by knot/cusp selection a fit trap. No fit, no c_k, no instance.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("disc5_parity_readout", {
        "golden_order": "ℤ[φ], φ=(1+√5)/2, fundamental unit norm −1 ⇒ L_n²−5F_n² = 4(−1)ⁿ",
        "cusp_order": "ℤ[√3], fundamental unit 2+√3 norm +1 ⇒ x_n²−3y_n² = +1 ∀n (no parity flip)",
        "rho5_ln_phi": mp.nstr(RHO5, 12),
        "rho3_arccosh2": mp.nstr(RHO3, 12),
        "channel_swap": ("bar-split of φⁿ: n even → (barEven,barOdd)=(L_n,F_n√5); "
                         "n odd → (F_n√5,L_n) — cosh/sinh identity swaps with parity"),
        "braid_powers": "4₁ = w² (n=2, even); Borromean L6a4 = w³ (n=3, odd); w = σ₁σ₂⁻¹",
        "sign_prediction": "muon +, proton − (from (−1)ⁿ)",
        "sign_observed": "muon +, proton −  ⇒ 2/2 MATCH, parameter-free",
        "observed_magnitude_ratio": mp.nstr(obs_ratio, 10),
        "best_phi_candidate": f"{best} misses by {mp.nstr(best_miss,4)}%",
        "verdict": ("parity carries the SIGN (2/2, no tuning) and disc-5 is structurally the "
                    "only one of the two orders that can; parity→S-sign link transported to "
                    "Bring by ANALOGY (conjectural, 2 bits, not a derivation); magnitudes "
                    "OPEN and not pursued (dense-cusp-shape fit trap)")})
    wb.add_assertion("parity_flip_in_disc5_absent_in_disc12", str(bool(d1)), "True")
    wb.add_assertion("cosh_sinh_channel_swap_by_parity", str(bool(d2)), "True")
    wb.add_assertion("sign_rule_matches_both_anchors", str(bool(d3)), "True")
    wb.add_assertion("magnitudes_unexplained_left_open", str(bool(d4)), "True")
    wb.save()
    print("\nwitness → qbeta-disc5-parity.witness.json")
    ok = all([d1, d2, d3, d4])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
