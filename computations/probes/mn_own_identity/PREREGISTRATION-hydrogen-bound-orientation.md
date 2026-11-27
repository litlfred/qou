# Pre-registration: does hydrogen as ONE bound word fix the p ↔ n orientation? (2026-11-22)

Owner, 2026-11-22: *"1"* (option 1 after §41: look for an orientation fixer beyond n = 3, with
hydrogen as one bound word). Written and committed before any number for this probe is computed.

## Setup
C²⊗⁶, strands 0..5, σ_i = Rc on strands (i, i+1), Rc = [[q,0,0,0],[0,0,1,0],[0,1,q−1/q,0],[0,0,0,q]].
- Proton: N = (σ₀σ₁⁻¹)³ on strands 0–2 (the Borromean core V³).
- Electron: e = σ₃σ₄σ₃ on strands 3–5 (ruled electron word; Hopf closure is not used here).
- Bond: G = (σ₂σ₃⁻¹)³, the same V³ shape on strands 2–4. Reason for this choice, fixed in
  advance: by `borromeanV3A_eq_switched_photon_product`, V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h), a γγ
  product in the ruled photon 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹. It is a choice of bond, not derived
  from a bound-state rule. No other bond is tried.
- Bound word W_L = N · e · G (proton LEFT). Control W_R: electron on 0–2 (σ₀σ₁σ₀), proton on 3–5
  ((σ₃σ₄⁻¹)³), same bond G (proton RIGHT).
- T³ = (#0 − #1)/2 over all six strands; T³_p, T³_e over strands 0–2, 3–5; K = q^{2T³}.
- Π_O: diagonal projector onto states whose proton strands carry w zeros; O₊: w = 2, O₋: w = 1.

## Functionals (fixed in advance; no T³ + B/2 import, no CODATA)
- **B1** F₁(O) = tr(T³ · W · Π_O).  **B2** F₂(O) = tr(T³ · K · W · Π_O).
- **B3** (reported, not used to decide): the proton-strand and electron-strand shares
  tr(T³_p W Π_O), tr(T³_e W Π_O).
Neutrality in orientation O means F(O) = 0 (exactly in ℚ(q), or |F| < 10⁻⁴⁰ at 60 dps).
A spectral charge (log W) is **not** used: the bond mixes proton and electron strands, so the
proton-weight subspace is not W-invariant and a per-orientation spectrum is undefined.

## Decision rule
The orientation is **fixed** iff exactly one of F(O₊), F(O₋) is zero, for B1 or B2, **and** the
same orientation is selected by W_L and W_R (a fixer that depends on putting the proton left is
fixing the placement convention, not the label).

## Predictions (derived in advance)
- **P1 (q = 1).** Rc is the swap, σ⁻¹ = σ, so N = 1 on strands 0–2, G = 1 (a 3-cycle cubed), and
  W = transposition of strands 3 and 5. The fixed states have s₃ = s₅; the electron strands then
  contribute 0 to T³, and K = 1. So F₁ = F₂ = Σ_{fixed, w} T³_p = +6 (O₊), −6 (O₋).
  **Neutrality fails in both orientations at q = 1.**
- **P2 (relabel).** X σ_i X = P σ_{4−i} P (P = strand reversal on 6 strands). So F_O₋(W_L) is minus
  the O₊ value of the index-reversed word with the proton moved to strands 3–5. At q ≠ 1 this need
  not equal −F_O₊(W_L): the sum S(q) := F(O₊) + F(O₋) measures how far binding breaks the relabel
  symmetry. Prediction: S(1) = 0; S(q₀) sign and size not predicted.
- **P3 (q₀).** By continuity from ±6 and the small deformation (h ≈ 0.209), F(O±) stay near ±6
  and neither is zero. **Overall prediction: not fixed (neither orientation neutral).**
- What would refute it: exactly one of F(O±) vanishing at q₀ for W_L and for W_R.

## Honesty clause
As in `PREREGISTRATION-hydrogen-orientation.md`: I know which orientation each n − p arm
prefers. Nothing here is chosen for its n − p outcome. The only new quantity this probe adds,
whatever the verdict, is S(q), the bound-word breaking of the relabel symmetry.

Precision: exact sympy over ℚ(q) for the 64 × 64 traces; mpmath 60 dps at q₀ (`Q_50_DIGIT_STR`)
and q = 1 + 10⁻²⁰. No float64.
**Pre-registration completed: 2026-11-22T09:32:43 (UTC), before any computation for this probe.**
