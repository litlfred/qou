import Mathlib.RepresentationTheory.Maschke
import Mathlib.Data.Fintype.Perm

/-!
# QOU.BraidKnot.MaschkeSnSemisimple — the *existence* half of side-2's block decomposition

[`RegularRepBlockTrace`](RegularRepBlockTrace.lean) formalised **side 2** of Identity (B)
conditionally on a single hypothesis bundle `SnWedderburnSpectralData`: a block spectral
decomposition `mulLeft C₂ = Σ_λ ω_λ · π_λ` of the regular representation `k[S_n]`. That bundle
folds together two logically distinct inputs:

1. **Existence** — `k[S_n]` is *semisimple*, so the regular module is a direct sum of simple
   submodules and every submodule has a complement (the projections `π_λ` exist at all).
2. **Identification** — *which* blocks (partitions `λ`), their dimensions (`dim(λ) = #SYT(λ)`,
   block R-dimension `dim(λ)²`), and the scalars `ω_λ = Σ_{c∈λ} c(c)²` by which the central `C₂`
   acts (Schur + the Jucys–Murphy eigenvalue theorem — Okounkov–Vershik).

This file discharges **input 1 unconditionally**, from **Maschke's theorem**
(`Mathlib.RepresentationTheory.Maschke`, which *is* in the pinned Mathlib): for a field `k` whose
characteristic does not divide `|G|` — in particular any `CharZero` field — `k[G]` is a semisimple
ring and every `k[G]`-submodule has a complement. Specialised to `G = S_n = Perm (Fin n)`:

- `sn_isSemisimpleRing`        — `k[S_n]` is a semisimple ring.
- `sn_regular_isSemisimpleModule` — the regular module `k[S_n]` is a semisimple module, i.e. a
  direct sum of simple submodules; equivalently every submodule has a complement (the constructive
  face of "the block projections exist"). A `k[S_n]`-submodule is automatically stable under the
  central element `C₂ ∈ k[S_n]`, so this is exactly the "C₂-invariant subspaces have C₂-invariant
  complements" statement the spectral decomposition is assembled from.

**What remains (input 2, the irreducible gap).** Semisimplicity is now Lean-backed, so the residual
content of `SnWedderburnSpectralData` is purely input 2 — the S_n-specific Okounkov–Vershik
identification. That layer (the partition ↔ irreducible bijection, `dim(λ) = #SYT(λ)`, and
JM-eigenvalue = contents) is **not** in Mathlib and stays the conditional hypothesis. Deriving the
`SnWedderburnSpectralData` *fields* from `sn_isSemisimpleRing` + Schur + the regular-rep
multiplicity theorem (`mult_λ = dim(λ)`, giving the `dim(λ)²` block ranks) is the natural next
increment toward fully discharging the bundle.

## References
- [manuscript] content/.../BraidKnot/RegularRepBlockTrace.lean (`SnWedderburnSpectralData`, side 2)
- [vershik2005] Vershik–Okounkov, "A new approach to the representation theory of the symmetric
  groups II" https://doi.org/10.1007/s10958-005-0421-7
-/

namespace QOU.BraidKnot.MaschkeSnSemisimple

-- `k` lives in `Type` (universe 0): Mathlib's Maschke instance is single-universe
-- (`{k G V : Type u}`), and `G = Perm (Fin n) : Type 0` forces `u = 0`. Every field of
-- interest here (ℚ, ℝ, ℂ) is `Type 0`, so this is not a real restriction.
variable {k : Type} [Field k] [CharZero k] (n : ℕ)

/-- `|S_n| = n!` is nonzero in any characteristic-zero field — the Maschke side condition
(`[NeZero (Fintype.card G : k)]`), supplied here so the semisimplicity instances below resolve. -/
private theorem card_perm_ne_zero : NeZero (Fintype.card (Equiv.Perm (Fin n)) : k) :=
  ⟨Nat.cast_ne_zero.mpr Fintype.card_ne_zero⟩

/-- **Existence, ring form.** The symmetric-group algebra `k[S_n]` over a characteristic-zero field
is a **semisimple ring** (Maschke: `char k = 0 ∤ |S_n|`). This is the ring-level face of input 1 —
the structural prerequisite for the Wedderburn block decomposition that `SnWedderburnSpectralData`
assumes. -/
theorem sn_isSemisimpleRing :
    IsSemisimpleRing (MonoidAlgebra k (Equiv.Perm (Fin n))) := by
  haveI := card_perm_ne_zero (k := k) n
  infer_instance

/-- **Existence, regular-module form.** The regular representation `k[S_n]` is a **semisimple
module** over itself — a direct sum of simple submodules, equivalently every submodule has a
complement. This is the module-level face of input 1: the regular representation does decompose
into irreducible blocks (Maschke), the only open question being *which* blocks (input 2,
Okounkov–Vershik). Because the central `C₂ ∈ k[S_n]` stabilises every `k[S_n]`-submodule, this is
the "C₂-invariant subspaces have C₂-invariant complements" fact from which the block spectral
decomposition `mulLeft C₂ = Σ_λ ω_λ·π_λ` is built. -/
theorem sn_regular_isSemisimpleModule :
    IsSemisimpleModule (MonoidAlgebra k (Equiv.Perm (Fin n)))
      (MonoidAlgebra k (Equiv.Perm (Fin n))) := by
  haveI := card_perm_ne_zero (k := k) n
  infer_instance

end QOU.BraidKnot.MaschkeSnSemisimple
