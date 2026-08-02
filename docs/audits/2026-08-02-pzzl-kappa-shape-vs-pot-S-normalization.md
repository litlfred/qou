# qou-pzzl — the κ_shape vs κ_pot split for `S` is the open question, not a typo

**Date:** 2026-08-02. **Status:** audit / precise pinning. No edit applied —
the reconciliation is gated on `qou-yh67` / `qou-qnnq`. Companion to the arc
ledger `docs/coordination/2026-08-02-c3-odd-aomega-unification.md`.

## The two live normalizations of the same observable `S`

The bar-odd decay observable `S = Q_β/E₀` (the order-`u²` leak of the deformed
figure-eight complex volume) is normalized **two incompatible ways** in the
corpus:

| Site | Formula | Reading |
|---|---|---|
| `QOU/QBeta/ArgUPhaseBranchSelection.lean` (`nzImVolume`, lines 58–59); `NZBarEvenVolumeFace` | `S = κ_shape·r²·cos(2φ)`, `κ_shape = √3/2`, from `𝔙 = Vol + i·κ_shape·u²` ("full-potential normalisation") — **no `A_ω` factor** | `A = κ_shape/κ_pot = 2` (the NZ-½ / dropped-half reading) |
| `QOU/QBeta/PhiBSArgumentIdentification.lean` (`SDeformedVolumeChannel`, `S_eq`, lines 199–201) | `S_K(q₀) = A_ω · Im 𝔙(u(q₀))`, `𝔙 = Vol + i·CS`, `κ_pot = √3/4`, `A_ω = 3` for 4₁ | `A = A_ω = 3` (the reduced-Stokes reading) |

Since `κ_shape = 2·κ_pot` (proved: `ObservableComplexVolumeVsFullPotential.lean`,
`imFullPotential = 2·imComplexVolume`), the two give:

```
ArgU:  S = 2·κ_pot·u²        (prefactor 2)
PhiBS: S = A_ω·κ_pot·u² = 3·κ_pot·u²   (prefactor 3)
```

They **disagree by a factor of `A_ω/2 = 3/2`** for the identical observable.

## Why it is NOT a mechanical typo

The two prefactors are exactly the two candidate answers to the arc's single
open question (see the ledger):

- **`A = 2`** — the observable is the *full NZ potential* `Φ = 2𝔙`; the NZ ½ is
  dropped; `c = √2`. (ArgU's normalization.)
- **`A = 3`** — the observable is the *complex volume* `𝔙` dressed by a
  *reduced Stokes integer* `A_ω = 3`. (PhiBS's normalization.)

The empirical anchor **cannot decide between them**: the measured
`A ≈ 2.054` sits at the precision ceiling (`σ_A ≈ 40%` at the ppb q₀-pin;
`BoostFactorNZNormalization.lean`), where `{2, Vol(4₁), q₀+q₀⁻¹, …}` are all
indistinguishable. Numerically `2.054` is nearer `2` (ArgU); structurally the
keystone finding says the Stokes integer `A_ω = 3` is **q-exact with no
resurgent tail** (`StokesSymmetryConstant.symmetryConstant_const`,
`StokesSymmetryConstantQZero.lean`, PR #4554), favouring `3` (PhiBS). That
tension **is** the open problem — it is not resolvable by editing one file to
match the other.

## Disposition (do NOT silently fix)

- **Do not** edit either site to match the other. Whichever is "wrong" is
  determined by the resolution of `qou-yh67` (does the fibre→observable functor
  apply `κ_shape` or `κ_pot·A_ω`?), which is itself the keystone
  `qou-qnnq` / A_ω-internal-derivation gap.
- When `qou-yh67` resolves, the fix is mechanical: one prefactor family is
  retired, the other becomes canonical, and the `S_eq` channel identity is
  re-stated consistently across `ArgUPhaseBranchSelection` /
  `NZBarEvenVolumeFace` / `PhiBSArgumentIdentification`.
- Until then both readings are conditional (`SDeformedVolumeChannel` is already
  a §3b class carrying `A_ω` as an unfixed field), so neither is a production
  claim — the inconsistency is contained, not leaking to a wired observable.

**Bean:** `qou-pzzl` (kept open, re-scoped to "reconcile after qou-yh67").
