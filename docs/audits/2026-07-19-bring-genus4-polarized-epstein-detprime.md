# 2026-07-19 — Genus-4 polarized Epstein det'Δ on Jac(Bring): the deferred piece, computed

**Script**: [`computations/alpha_em/bring_genus4_polarized_epstein_detprime_probe.py`](../../computations/alpha_em/bring_genus4_polarized_epstein_detprime_probe.py)
**Witness**: `computations/alpha_em/bring-genus4-polarized-epstein-detprime.witness.json`
**Unblocks**: the `deferred` item of
[`bring_polarized_epstein_determinant_probe.py`](../../computations/alpha_em/bring_polarized_epstein_determinant_probe.py)
([2026-07-18 audit](2026-07-18-bring-polarized-epstein-determinant.md)) — the full
genus-4 Epstein det'Δ at the thin Bring modulus (Im τ₀ = 0.186676), which the
box enumeration `(2R+1)⁸` could not reach ("needs Siegel reduction").

## Method (why it is now computable)

Fincke–Pohst **exact norm-cutoff enumeration**: enumerate precisely the lattice
points with `mᵀHm ≤ Q` (Cholesky-recursive, vectorized). At `Q = 14` the theta
tail is `< e^{−π·14} ≈ 8.5e−20`. This does the job the sibling labelled "Siegel
reduction" — an exact cutoff handles thin quadratic forms directly, no basis
reduction needed. Point counts stay ~10⁴–10⁶ (vs the box's 2.1e8 at R = 5).
Everything else (Chowla–Selberg heat-kernel split, `_gram` convention, τ₀,
scale-free measure `√Vol/√det'Δ`) is **identical to the 2026-07-18 sibling**.

Validation ladder (all machine-checked in the witness):

1. **genus-1 exact**: FP path reproduces `det'Δ = (Im τ)²|η(τ)|⁴` (the sibling's
   anchor) to < 1e−6.
2. **genus-2 diag(5τ₀, τ₀)**: FP agrees with an *independent* factorized-theta
   evaluation (a direct-sum lattice's theta is the product of per-block 2-dim
   thetas — the theta factorizes even though det'Δ does not) to < 1e−6, and
   refines the sibling's box-R=5 value 3.94373 → **3.94937** (the box was
   converging up, as they recorded).
3. **genus-4 diagonal**: FP vs factorized-theta again (8-dim live), rel ~3e−11.
4. **genus-4 polarized M**: cutoff convergence Q=11 vs Q=14 identical to 10
   digits.

## Results (scope-(a); nothing interpreted, nothing wired)

| object | period | measure `√Vol/√det'Δ` |
|---|---|---|
| **principally polarized Jacobian** | τ₀·M, M=[[4,1,−1,1],[1,4,1,−1],[−1,1,4,1],[1,−1,1,4]] (Thm 2.12) | **1.38757991** |
| product/isomorphism target | τ₀·diag(5,5,5,1) (Prop 4.6) | **1.472396e+12** |
| retracted naive per-factor product | — | 8.226 (context only) |

- **The polarization theta-factor is the blow-up killer.** The product-period
  measure blows up (~1.47e12) because the diagonal lattice keeps the bare thin
  `E_{τ₀}` block (shortest vector ≈ 0.285). The integer M-lattice mixes that
  direction away (shortest vector ≈ 1.14): pol/diag ≈ **9.4e−13**. Covolume and
  metric spectrum are polarization-independent (det = 125, spec {1,5,5,5} — the
  2026-07-18 `bring_polarized_jacobian_determinant_probe` result), so this
  ~12-orders separation lives **entirely in the genus-4 theta-factor**, exactly
  where that probe localized it.
- **Cross-session echo**: 1.4724e12 numerically reproduces the "unpolarized
  det'Δ blow-up ≈ 1.47e12" found earlier on the α_EM genus-4 front by a
  different implementation (direct spectrum-sum), consistent with both
  computing the product-period torus. Recorded as an observation.
- **No target matched**: the polarized 1.38758 is not 8π (ratio 0.0552), not
  b₁ = 8 (ratio 0.173), not the retracted 8.226 (ratio 0.169). No candidate
  constant is claimed; per the production-vs-exploratory discipline no
  nearest-constant hunting is recorded beyond these plain ratios.

## Consequence for the α_EM 1/(8π) magnitude leg

The magnitude leg's photon 1-loop boson measure on the principally polarized
Jac(Bring) is now a **computed O(1) number, 1.38758**, replacing both the
retracted per-factor product (8.226) and the product-period blow-up (1.47e12).
Whatever normalization connects the boson measure to the 1/(8π) wall must now
be sought against this value (or against a q-deformed / compact-`*` variant of
this determinant — the fibre-level route flagged on #3941/#3949 remains open
and untouched here). The reciprocal π stays RT/Front-2. No tier change.

## Scope guard

No q₀ anywhere; no 8π manufactured; nothing wired to production; scope-(a)
throughout. The probe is self-contained (numpy + mpmath) and its witness
carries the full assertion list.
