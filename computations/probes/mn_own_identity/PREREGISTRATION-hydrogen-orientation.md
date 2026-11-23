# Pre-registration: does hydrogen neutrality fix the p ↔ n orientation? (2026-11-22)

Context: §40 of `LITERATURE-COMPARISON.md`. In the weight model C²⊗³ (σ = Rc,
Rc = [[q,0,0,0],[0,0,1,0],[0,1,q−1/q,0],[0,0,0,q]], V = σ₀σ₁⁻¹) the assignment "bit 0 = u" is a
label: with X the global bit flip and P the strand reversal, X·V·X = P·V⁻¹·P, T³ → −T³,
K → K⁻¹ (K := q^{2T³}), and every E_n − E_p flips sign. We look for an orientation fixer that does
**not** use any n − p mass: hydrogen neutrality Q_p + Q_e = 0, with **one** charge functional
applied to the nucleon word 𝓑₃ = V³ and to the ruled electron word e = σ₀σ₁σ₀ (closure: Hopf link)
in the same model. Backup electron σ₀³ (trefoil, ruled backup) is a secondary arm only.
No T³ + B/2 import. No CODATA or lattice input. q₀ = `Q_50_DIGIT_STR` (proton pin).

Written completely before any computation in this probe. No code for this probe existed when this
file was written.

## Orientations
- **O₊** (current corpus convention): u = bit 0, proton block W_p = W₂ (two 0-bits), neutron W₁.
- **O₋** (swapped): u = bit 1, proton block = W₁, neutron W₂.
A criterion **fixes** the orientation iff, with Q_e ≠ 0 or Q_e = 0 computed once, exactly one of
F(N, W₂), F(N, W₁) equals −Q_e (within 10⁻⁴⁰ at 60 dps, or exactly in sympy).

## Electron block convention (fixed in advance)
No derived rule assigns the electron a weight block. **Primary:** the electron charge is the
full-space (8-dim) value of the functional. **Secondary (reported, not used to decide):** the
electron's per-block values w = 0..3.

## Candidate functionals (decided before computing)
None of these imports T³ + B/2.

**C1 — spectral log charge.** Q̂(w) := log(w)/2πi, principal branch; charge = trace over the block
(nucleon) / full space (electron). Also the phase-only variant Q̂_arg := Σ Arg(λ)/2π (drops the
|λ| ≠ 1 part).
**C2 — crossing Coulomb charge** ½(n₊ − n₋) (`coulomb-charge.md`): word-level.
**C3 — sign of the K-weighted quantum trace**, s(w, B) := sign Re tr_B(K·w); criterion
s(N, W_p) = −s(e, full).
**C4 — T³-odd functional** tr_B(T³·w) (also tr_B(T³·Q̂(w))), the only family that sees which
block is which by construction.

## Predictions (derived analytically in advance — so they are not independent tests)
Derivation used: XRcX = P₂RcP₂ locally, so Xσ₀X = Pσ₁P, Xσ₁X = Pσ₀P, crossing signs preserved.
Hence **XeX = P(σ₁σ₀σ₁)P = PeP**: the ruled electron word is relabel-invariant up to a
block-preserving conjugation. And XNX = PN⁻¹P.

- **P-sym.** (i) spec(N|W₁) = spec(N⁻¹|W₂); since spec(N|W₂) = {1, e^{±iφ}}, φ = 2π(3t − 1), is
  closed under inversion, the nucleon has identical spectra on W₁ and W₂. (ii) The electron's
  full-space value of any functional built from (Rc, K, T³) is the same in O₊ and O₋, and
  tr(T³·g(e, K)) = 0 for every such g.
- **P-e-spec.** e = Δ (half twist); Δ² = q^{2c(λ)} on irrep λ. Here only (3) (×4, c = 3) and (2,1)
  (×2, c = 0) occur. So e = q³ on the (3) copies and, with det = (q·(−q⁻¹))³ = −1 on (2,1),
  spec(e|(2,1)) = {+1, −1} exactly, at every q.
- **PC1.** tr Q̂(N) = 0 on W₁ and W₂ (Q̂ eigenvalues {0, ±(3t − 1)}) → nucleon value block-blind
  → **unfixed**. Electron: the eigenvalue −1 sits on the branch cut of log, so Q̂(e) is not defined
  without a branch rule (each (2,1) copy gives ±½); the four (3) copies give
  log(q³)/2πi each, i.e. a purely imaginary total 4·3 ln q/(2πi) = −6i ln q/π. Expected Q̂_arg(e) = ±1 (sign = branch choice), and
  Q̂_arg(N) = 0 both blocks → neutrality fails in both orientations (**inconsistent / ill-posed**).
- **PC2.** n₊ − n₋: N gives 0, e gives 3 → Q_N = 0, Q_e = 3/2, block-independent → **unfixed**,
  and neutrality fails in both orientations (0 ≠ −3/2).
- **PC3.** K is a positive scalar on each weight block (q on W₂, q⁻¹ on W₁), and the plain block
  traces of N agree, so s(N, W₂) = s(N, W₁) → **unfixed** whatever s(e) is.
- **PC4.** tr(T³·e) = 0 and tr(T³·Q̂(e)) = 0 on the full space (P-sym ii), so neutrality demands
  Q_p = 0, but tr_{W₂}(T³N) = +½ tr N, tr_{W₁}(T³N) = −½ tr N, both ≠ 0 →
  **inconsistent for both orientations** (neither block is neutral-compatible).
- **Overall prediction:** no candidate in the searched class fixes the orientation. Reason: the
  electron word is relabel-invariant, the nucleon's block spectra are inversion-symmetric, and the
  only block-distinguishing operator (T³, or K's magnitude) is relabel-odd and pairs with an
  electron value of 0.

## What would refute the overall prediction
A candidate with Q_e ≠ 0 for which exactly one of F(N, W₁), F(N, W₂) equals −Q_e. That would fix
the orientation, and the block that matches would be named the proton.

## Honesty clause
Before writing this I knew from §36–§40: under O₊ the 𝒟² arm gives E_n − E_p = +0.171 MeV
(neutron heavier, CODATA sign) and the charge terms are neutron-heavier (opposite to the QED sign).
So I know which orientation each n − p arm "prefers". A criterion that ends up agreeing with the
lattice/CODATA n − p sign **carries no weight if it was chosen for that reason**; the candidates
above were fixed by what is definable on both words without B/2, not by their outcome, and the
predictions above were derived before any number was computed. No candidate will be added after
seeing results without being labelled post hoc.

Precision: exact sympy over ℚ(q) for spectra/traces where possible; mpmath 60 dps for log/eig
at q₀ and q = 1 + 10⁻²⁰. No float64 arithmetic.

**Pre-registration completed: 2026-11-22T09:22:39 (UTC; `date -u` at completion), before any computation for this probe.**
