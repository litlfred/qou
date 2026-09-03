/-
# Why an octonionic `SU(3)` must be a stabiliser, not a generator identification

There are two routes in the literature from the octonions to an `SU(3)`, and they
are not variants of one another — one of them cannot work, for a reason that is
pure linear algebra.

**Route B as this chapter uses it (Günaydin–Gürsey).** `SU(3)` appears as the
subgroup of `G₂ = Aut(𝕆)` stabilising one imaginary unit. It acts *on*
`Im(𝕆)`, which decomposes as `ℝ ⊕ ℂ³`. The real dimensions balance:
`1 + 2·3 = 7`. Nothing in this file bears on that route.

**The other route: identify the generators with the units.** Several papers set
`λ_a ↔ e_a` for the Gell-Mann matrices and the imaginary octonion units, and
read off an `SU(3)`. This file proves that no such identification can be
faithful, by two independent obstructions:

* `no_faithful_generator_identification` — a **dimension** count. `su(3)` is
  8-dimensional over `ℝ`; `Im(𝕆)` is 7-dimensional. There are only seven units
  to receive eight generators, so any linear identification has a kernel.

* `cartan_not_independent_on_one_unit` — a **rank** count, which bites even
  where the dimension count might be dodged. `su(3)` has rank 2: it needs two
  independent commuting generators (`I₃` and the hypercharge `Y`). If both are
  sent to multiples of a single imaginary unit, they are linearly dependent, so
  the rank-2 Cartan has collapsed to a line.

The second is the sharper of the two because it is what actually happens. The
generator identification runs out of units at `λ₈` and sends **both** `λ₃` and
`λ₈` into `span{e₃}`; every one of `I₃`, `U₃`, `V₃`, `Y` then lands on the same
line.

## Provenance — the observation is not new here, the theorem is

Both obstructions were already recorded in prose, on two of the papers, by the
2026-08-25 upload triage
(`docs/audits/2026-08-25-octonion-division-algebra-upload-triage.md`): *"maps
eight `su(3)` generators onto seven octonion imaginaries by reusing `e₃`, which
is not injective and not a Lie-algebra map"*, and *"`λ₈ ∝ λ₃` collapses the
Cartan to rank 1, destroying `A₂`"*. This file does not rediscover that. What
it adds is that the observation is now (a) machine-checked and (b) stated as a
**class exclusion** over arbitrary linear maps, rather than as a defect of two
particular papers — so a third paper doing the same thing is excluded without
being read.

See `docs/audits/2026-08-26-octonionic-su3-two-routes.md` for the worked
instance, including the source's own claim — self-contradictory on its own
equations — that `I₃`, `U₃`, `V₃` and `Y` are linearly independent.

## What this does NOT prove

It does not establish that the Günaydin–Gürsey decomposition is correct; that
remains a citation (bean `qou-8pl3`, Route B gap (i)). It does not say anything
about whether an octonionic `SU(3)` serves as flavour or as colour (gap (ii)).
It excludes **one route-class** — generator identification — as a scope-(b)
structural exclusion, with the justifying invariants named: dimension and rank.
-/
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas

namespace QOU.Eightfold

section Dimension

variable {K V W : Type*} [DivisionRing K]
  [AddCommGroup V] [Module K V] [AddCommGroup W] [Module K W]

/-- **The dimension obstruction.** A linear map into a space of strictly smaller
finite dimension is never injective.

Applied below with `V = su(3)` (dimension 8) and `W = Im(𝕆)` (dimension 7). -/
theorem no_injective_of_finrank_lt [Module.Finite K W] (f : V →ₗ[K] W)
    (h : Module.finrank K W < Module.finrank K V) : ¬ Function.Injective f := by
  intro hf
  exact absurd (LinearMap.finrank_le_finrank_of_injective hf) (not_le.mpr h)

end Dimension

section Rank

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- **The rank obstruction.** Two vectors that are multiples of a common vector
are linearly dependent — with no side condition on the multipliers at all.

This is the collapse of a rank-2 Cartan onto a single imaginary unit: if `I₃` and
the hypercharge `Y` are both sent to multiples of `e₃`, they cannot be
independent, whatever the multipliers are.

No nonvanishing hypothesis is needed. The obvious relation `b·(a • x) − a·(b • x)`
is nontrivial only when `a` or `b` is nonzero, but the degenerate case is not an
exception: if both vanish the pair is `(0, 0)`, and a family containing `0` is
never independent either. Stating it without the hypothesis is therefore both
stronger and closer to the fact being used. -/
theorem not_linearIndependent_of_common_line (x : V) (a b : K) :
    ¬ LinearIndependent K ![a • x, b • x] := by
  intro h
  have hz : b • (a • x) + (-a) • (b • x) = 0 := by module
  obtain ⟨-, hna⟩ := LinearIndependent.pair_iff.mp h b (-a) hz
  have ha : a = 0 := neg_eq_zero.mp hna
  obtain ⟨h1, -⟩ := LinearIndependent.pair_iff.mp h 1 0 (by simp [ha])
  exact one_ne_zero h1

/-- The rank obstruction, stated for the two Cartan generators by name: whenever
both are carried onto the same imaginary unit `u`, they are dependent, and the
rank-2 Cartan of `su(3)` has collapsed to a line. -/
theorem cartan_not_independent_on_one_unit (u : V) (cI cY : K)
    (I₃ Y : V) (hI₃ : I₃ = cI • u) (hY : Y = cY • u) :
    ¬ LinearIndependent K ![I₃, Y] := by
  subst hI₃; subst hY
  exact not_linearIndependent_of_common_line u cI cY

end Rank

/-- **The concrete dimension count.** `su(3)` has dimension 8 as a real Lie
algebra and `Im(𝕆)` has dimension 7, so no identification of the eight Gell-Mann
generators with the seven imaginary units is faithful.

Stated over a generic division ring rather than `ℝ`, per the base-ring
convention: nothing archimedean is used, and the count is what does the work.
The hypothesis is not decoration — swap the two dimensions and the statement is
false, since `K⁷ → K⁸` admits plenty of injections. -/
theorem no_faithful_generator_identification {K : Type*} [DivisionRing K]
    (f : (Fin 8 → K) →ₗ[K] (Fin 7 → K)) : ¬ Function.Injective f := by
  refine no_injective_of_finrank_lt f ?_
  rw [Module.finrank_fin_fun, Module.finrank_fin_fun]
  norm_num

end QOU.Eightfold
