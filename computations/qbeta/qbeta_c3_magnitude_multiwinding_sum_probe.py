#!/usr/bin/env python3
"""qbeta_c3_magnitude_multiwinding_sum_probe.py — the multi-winding even-channel
exponential-bridge SUM (leading truncation) DIVERGES; and the resurgent one-instanton
magnitude ratio is CIRCULAR. Two honest obstructions on the c₃ magnitude wall.

Follow-up to the single-pair MISS (PR #4497, `qbeta_c3_magnitude_exp_bridge_windings`).
That probe ruled out the *distinguished single canonical pair*; the natural next
candidates are (1) a multi-winding SUM over the cusp lattice, and (2) the resurgent
one-instanton prefactor. This probe records honest negatives for both.

Setup (same as #4497): even/cosh channel of 𝔙₄₁ on the cusp winding lattice,
    Re 𝔙₄₁(u_{m,ℓ}) = Vol(4₁) − (3/8)(ln q₀)²·N(m,ℓ),   N(m,ℓ) = (2m+ℓ)·ℓ,
exponential bridge |δf| ~ e^{−Re𝔙/ℏ_q}.

## (1) Multi-winding SUM diverges (leading truncation) — DIV

The cross-form N(m,ℓ)=(2m+ℓ)ℓ is INDEFINITE and UNBOUNDED ABOVE (e.g. N(1,ℓ)=(2+ℓ)ℓ→+∞).
So Re𝔙 = Vol − (3/8)(ln q₀)²·N → −∞ along those windings, and the bridge term
e^{−Re𝔙/ℏ_q} = e^{(3/8)(ln q₀)²·N/ℏ_q − Vol/ℏ_q} → +∞. Hence
    S_sum(q₀) := Σ_{m,ℓ} e^{−Re𝔙(u_{m,ℓ})/ℏ_q}   DIVERGES.
Verified numerically: partial sums over the |m|,|ℓ|≤R box grow super-linearly and the
max single term grows without bound in R.

Scope-(a) reading: the multi-winding even-channel sum, IN THE LEADING QUADRATIC
truncation of the NZ potential, is not a well-defined (convergent) magnitude object.
A convergent realisation requires either the FULL (non-truncated) complex volume —
whose large-|u| growth would restore convergence — or an ad-hoc winding cutoff, and a
cutoff chosen to hit |S_p/S_m|≈4.075 is the Dang–Purcell dense-fit resource. So the
leading-form multi-winding sum is NOT the parameter-free magnitude source. (This is a
statement about the LEADING TRUNCATION, not the full 𝔙₄₁ — the ingredient survives.)

## (2) Resurgent one-instanton magnitude ratio is CIRCULAR — CIRC

The one-instanton census form (PR #4246) is
    N_odd(q) = 𝒜 · e^{−Re𝔙/(πℏ)} · sin(Im𝔙/(πℏ)),  ℏ = log q.
The two anchors have near-identical q₀ (Δ ln q₀ ≈ 1.2e-8), so the prefactor
e^{−Re𝔙/(πℏ)} is essentially equal at both; the magnitude ratio is therefore
    |S_p/S_m| ≈ |sin(Im𝔙_p/(πℏ)) / sin(Im𝔙_m/(πℏ))|.
But Im𝔙 = S is EXACTLY the quantity being solved for (S = Im𝔙(u(q₀))). So the
one-instanton ratio does not independently PREDICT |S_p/S_m| — it re-expresses it in
terms of itself. The magnitude ratio via the resurgent prefactor reduces to the open
argument map u(q₀), confirming #4246's "structurally necessary, quantitatively open."
No independent magnitude is produced. (Recorded as CIRC, not a fresh negative.)

Verdict: two obstructions — leading-form multi-winding sum DIVERGES; resurgent ratio is
CIRCULAR. The c₃ magnitude |S_p/S_m|≈4.075 stays OPEN. No fit; nothing wired.
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

set_compute_dps()  # canonical compute dps; matches WitnessBuilder precisionMetadata
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
VOL41 = +(2 * mp.clsin(2, mp.pi / 3))


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def cross_N(m: int, l: int) -> int:
    return (2 * m + l) * l


def main() -> int:
    print("=" * 78)
    print(" c₃ magnitude: multi-winding SUM (divergence) + resurgent ratio (circularity)")
    print("=" * 78)
    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_mu, S_pr = S(q_mu), S(q_pr)
    ratio_target = abs(S_pr / S_mu)
    L = mp.log(q_mu)
    hbar = 1 - 1 / q_mu

    def ReV(m, l):
        return VOL41 - (mp.mpf(3) / 8) * L ** 2 * cross_N(m, l)

    def term(m, l):
        return mp.e ** (-ReV(m, l) / hbar)

    # (1) partial sums + max term over growing box → divergence signature
    print("\n (1) multi-winding even-channel SUM over |m|,|ℓ|≤R box:")
    sums, maxes = [], []
    Rs = [1, 2, 3, 4, 5, 6, 8, 10]
    for R in Rs:
        s = mp.mpf(0)
        mx = mp.mpf(0)
        for m in range(-R, R + 1):
            for l in range(-R, R + 1):
                t = term(m, l)
                s += t
                mx = max(mx, t)
        sums.append(s)
        maxes.append(mx)
        print(f"   R={R:2d}: partial_sum={mp.nstr(s,6)}  max_term={mp.nstr(mx,6)}")
    # divergence: both the partial sum and the max single term increase monotonically in R
    sum_increasing = all(sums[i + 1] > sums[i] for i in range(len(sums) - 1))
    maxterm_increasing = all(maxes[i + 1] > maxes[i] for i in range(len(maxes) - 1))
    # analytic tail: N(1,R)=(2+R)R → +∞, so term(1,R)=e^{(3/8)L² N/ℏ − Vol/ℏ} → ∞
    tail_growing = term(1, Rs[-1]) > term(1, Rs[0])
    diverges = sum_increasing and maxterm_increasing and tail_growing
    print(f"   ⇒ partial sums increasing: {sum_increasing}; max term increasing: "
          f"{maxterm_increasing}; N-tail e^{{(3/8)L²N/ℏ}}→∞: {tail_growing}")
    print("   ⇒ SUM DIVERGES (leading truncation): cross-form N unbounded above ⇒ "
          "Re𝔙→−∞ ⇒ term→+∞.")

    # (2) resurgent ratio circularity: prefactor near-cancels at Δln q₀≈1.2e-8, ratio ~ sin/sin(Im𝔙)
    dlnq = abs(mp.log(q_pr) - mp.log(q_mu))
    prefactor_ratio = mp.e ** (-(ReV(1, 0)) / (mp.pi * L)) / mp.e ** (-(ReV(1, 0)) / (mp.pi * mp.log(q_pr)))
    prefactor_near_unity = abs(prefactor_ratio - 1) < mp.mpf("1e-6")
    print(f"\n (2) resurgent one-instanton ratio: Δln q₀ = {mp.nstr(dlnq,4)} (tiny) ⇒ "
          f"e^{{−Re𝔙/πℏ}} prefactor ratio ≈ {mp.nstr(prefactor_ratio,10)} (≈1: "
          f"{prefactor_near_unity}).")
    print("   ⇒ |S_p/S_m| ≈ |sin(Im𝔙_p/πℏ)/sin(Im𝔙_m/πℏ)|, but Im𝔙 = S itself ⇒ CIRCULAR")
    print("   (reduces to the open u(q₀); confirms #4246 'quantitatively open').")

    print(f"\n target |S_p/S_m| = {mp.nstr(ratio_target,7)} stays OPEN. No fit; nothing wired.")

    wb = WitnessBuilder("qbeta-c3-magnitude-multiwinding-sum", engine="mpmath")
    wb.set_description(
        "Two honest obstructions on the c₃ magnitude |S_p/S_m|≈4.075 (follow-up to the "
        "single-pair MISS #4497). (1) The multi-winding even-channel exponential-bridge SUM "
        "Σ e^{−Re𝔙/ℏ_q} DIVERGES in the leading NZ truncation: cross-form N=(2m+ℓ)ℓ is "
        "unbounded above ⇒ Re𝔙→−∞ ⇒ terms→+∞ (partial sums + max term grow monotonically "
        "in box radius). A convergent realisation needs the full (non-truncated) 𝔙₄₁ or a "
        "cutoff (fit) — leading-form sum is not a parameter-free magnitude source (scope-(a), "
        "ingredient survives). (2) The resurgent one-instanton ratio is CIRCULAR: at "
        "near-identical anchor q₀ the e^{−Re𝔙/πℏ} prefactors cancel, so |S_p/S_m|≈|sin(Im𝔙_p/πℏ)/"
        "sin(Im𝔙_m/πℏ)| with Im𝔙=S itself — reduces to the open u(q₀), confirming #4246. "
        "Magnitude stays open. No fit; nothing wired; no instance fabricated.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("obstruction_readout", {
        "target_ratio_Sp_over_Sm": mp.nstr(ratio_target, 10),
        "sum_partial_R1": mp.nstr(sums[0], 8),
        "sum_partial_Rlast": mp.nstr(sums[-1], 8),
        "maxterm_R1": mp.nstr(maxes[0], 8),
        "maxterm_Rlast": mp.nstr(maxes[-1], 8),
        "multiwinding_sum_diverges_leading_truncation": bool(diverges),
        "resurgent_prefactor_ratio_near_unity": bool(prefactor_near_unity),
        "resurgent_ratio_is_circular_reduces_to_uq0": True,
        "verdict": ("multi-winding leading-form sum DIVERGES; resurgent ratio CIRCULAR "
                    "(reduces to open u(q₀)); magnitude |S_p/S_m|≈4.075 stays open")})
    wb.add_assertion("multiwinding_leading_sum_diverges", str(bool(diverges)), "True")
    wb.add_assertion("resurgent_prefactor_near_unity_ratio_circular",
                     str(bool(prefactor_near_unity)), "True")
    wb.save()
    print("\nwitness → qbeta-c3-magnitude-multiwinding-sum.witness.json")
    ok = bool(diverges and prefactor_near_unity)
    print("ALL ASSERTIONS PASS (honest obstructions recorded)" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
