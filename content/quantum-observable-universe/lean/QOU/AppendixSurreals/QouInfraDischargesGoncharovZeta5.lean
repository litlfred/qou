import Mathlib.Tactic
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# QOU.AppendixSurreals.QouInfraDischargesGoncharovZeta5 — conjecture carrier

**§3b-cond class axiomatisation** for content block
[`conj:qou-infra-discharges-goncharov-zeta5`](../../../appendix-surreals/qou-infra-discharges-goncharov-zeta5.md):
*QOU's Hecke-NF + Bring-`S₅` infrastructure discharges Goncharov's depth-3
conjecture at `F = ℚ(ζ₅)`*.

Primary conjecture carrier with **no instance** — the honest open state per
AGENTS.md §3b-tax.

## What changed (bean `qou-ffwk`)

The previous field schema was a scalar plus a field asserting that it vanishes,
inhabited by `⟨0, rfl⟩`. The class chose its own witness, so it asserted nothing
and a downstream hypothesis on it was not a meaningful conditional.

Its docstring's "Content statement (from manuscript)" was also **the conjecture's
own title, repeated** — it recorded no content at all, so the block was the only
source. Fixed here.

## What is encoded: the block's own *reduced target*

The full statement quantifies over motivic cohomology — `K₅^ind(F) ⊗ ℚ ≅
𝔅₃(F) ⊗ ℚ`, the weight-3 Bloch group, the Goncharov 22-term relation, the
regulator into `𝒫₃/𝒫₂`. None of that exists in this library, and neither do
polylogarithms; inventing any of it would assert constructions the corpus does
not have.

The block does not require that, because it states its own reduced form:

> The reduced target for QOU is to prove that `{Li₃(ζ₅ᵏ) : k = 1,2,3,4}` modulo
> the multiplication-formula identity **span exactly this rank-2 image**.

with the rank supplied by Borel: `dim_ℚ K₅^ind(ℚ(ζ₅)) ⊗ ℚ = 2`. That is a
statement of linear algebra over `ℚ` about **four** named elements, and it is
encodable exactly as written.

So the class takes the ambient `ℚ`-space and the four values as caller data, and
asserts the rank. `V` stands for `𝒫₃/𝒫₂` over `ℚ(ζ₅)` and `li3 k` for
`Li₃(ζ₅^{k+1})`; both are parameters because this library builds neither.

## What is deliberately *not* encoded

* **The two routes.** Jones-coincident pair generation and the direct
  construction of `G₂₂(ζ₅)` are *strategies* — the block says "if either route
  succeeds". A carrier that encoded a route would assert a proof method as part
  of the claim.
* **"the only further relation being the 22-term one."** This constrains the
  relation module beyond its dimension. Its dimension is already forced —
  `relations_finrank_eq_two` below derives it — but *which* relations they are
  needs `G₂₂` written down, and that needs polylogarithm identities the library
  does not have. Encoding a placeholder for it would be the defect this bean
  exists to remove.
* **Borel's theorem.** The rank `2` enters as the *content of the conjecture at
  this level*, not as a cited input; the block uses Borel to say what the target
  rank is, and the open question is whether the four `Li₃` values realise it.

## Base ring (§7c)

`ℚ`-linear throughout, with no real-field type anywhere: the target is a
`ℚ`-vector space and the rank is an integer. Nothing is ordered, normed, or
compared against a numerical substrate value. `ζ₅` appears only in prose naming
the arguments, never as a computed quantity.
-/

namespace QOU.AppendixSurreals

open Module

universe v

/-- **Goncharov's depth-3 conjecture at `ℚ(ζ₅)`, in the block's reduced form.**

See
[`conj:qou-infra-discharges-goncharov-zeta5`](../../../appendix-surreals/qou-infra-discharges-goncharov-zeta5.md).

Parameters are the caller's data:

* `V` — the target `ℚ`-space, standing for `𝒫₃/𝒫₂` over `ℚ(ζ₅)`;
* `li3 k` — the value `Li₃(ζ₅^{k+1})` for `k : Fin 4`.

Neither is constructed in this library, so both are supplied rather than built.

An instance **is** the conjecture, for that data. None is provided. -/
class QouInfraDischargesGoncharovZeta5
    (V : Type v) [AddCommGroup V] [Module ℚ V] (li3 : Fin 4 → V) : Prop where
  /-- **The reduced target.** The four `Li₃(ζ₅ᵏ)` span a space of rank exactly
      `2` — Borel's `dim_ℚ K₅^ind(ℚ(ζ₅)) ⊗ ℚ`.

      Rank `2` from four generators is the whole content: it says the
      multiplication-formula identities cut the four values down to Borel's
      rank and no further. -/
  span_finrank_eq_two :
    finrank ℚ (Submodule.span ℚ (Set.range li3)) = 2

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  History: this file previously carried
--     axiom conj_qou_infra_discharges_goncharov_zeta5 : QouInfraDischargesGoncharovZeta5
--     noncomputable instance : QouInfraDischargesGoncharovZeta5 := …
-- i.e. the conjecture was asserted by `axiom` and installed as a global
-- instance, so every downstream hypothesis on it resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- The field schema is now content-bearing as well; see the header.
--
-- Note for `qou-ffwk`'s inventory: that bean greps for the old vanishing
-- field's name, which is deliberately written nowhere in this file — not even
-- in this history — so the file drops out of the grep instead of matching it
-- forever from its own changelog.

namespace QouInfraDischargesGoncharovZeta5

variable {V : Type v} [AddCommGroup V] [Module ℚ V] {li3 : Fin 4 → V}

/-- **Exactly two independent relations** — the multiplication-formula count,
derived rather than assumed.

Four generators spanning rank `2` leave a relation space of rank `2`, by
rank-nullity applied to `Fintype.linearCombination`. The block attributes those
relations to the multiplication formula; the *count* follows from the rank alone
and needs nothing about which relations they are.

This is what makes the single field say something structural rather than merely
numerical. -/
theorem relations_finrank_eq_two [h : QouInfraDischargesGoncharovZeta5 V li3] :
    finrank ℚ (LinearMap.ker (Fintype.linearCombination ℚ li3)) = 2 := by
  have hrange :
      LinearMap.range (Fintype.linearCombination ℚ li3)
        = Submodule.span ℚ (Set.range li3) :=
    Fintype.range_linearCombination ℚ li3
  have hrk := LinearMap.finrank_range_add_finrank_ker
    (f := Fintype.linearCombination ℚ li3)
  rw [hrange, h.span_finrank_eq_two] at hrk
  have hdom : finrank ℚ (Fin 4 → ℚ) = 4 := by simp
  omega

/-! ### Inhabitation depends on the data

Not an `instance`, so typeclass resolution cannot pick it up and silently close
a downstream hypothesis. -/

/-- **Refuted at the trivial family** — the property the old schema lacked
entirely.

Four values that are all `0` span the zero submodule, of rank `0 ≠ 2`. So the
class genuinely constrains the caller's `Li₃` data: a degenerate family fails
it. Under the previous shape `⟨0, rfl⟩` closed the class for every choice of
everything, including this one, so "the four values realise Borel's rank" had
nothing to fail against. -/
theorem not_of_trivial :
    ¬ QouInfraDischargesGoncharovZeta5 V (fun _ => (0 : V)) := by
  rintro ⟨h⟩
  have hrange : (Set.range fun _ : Fin 4 => (0 : V)) = {0} := Set.range_const
  rw [hrange, Submodule.span_singleton_eq_bot.mpr rfl] at h
  simp at h

end QouInfraDischargesGoncharovZeta5

end QOU.AppendixSurreals
