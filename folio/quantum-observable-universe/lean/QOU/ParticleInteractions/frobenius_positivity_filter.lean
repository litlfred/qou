import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.DeriveFintype
import Mathlib.Tactic.Ring

/-!
# QOU.ParticleInteractions.frobenius_positivity_filter

Lean statement for content block
[`prop:frobenius-positivity-filter`](../../../quantum-observable-universe/particle-interactions/frobenius-positivity-filter.md).

**Statement (manuscript).**  For even mass number `A`, a channel
configuration `c ∈ {triv, conf, unconf, sign}^A` is *Frobenius-positive*
iff both the parent product `m_par = ∏ₘ G_{nₘ}(cₘ)` and the daughter
product `m_dau = ∏ₘ G_{n'ₘ}(cₘ)` are non-negative.  Exactly half of the
configurations — `2^{A-1}` out of `4^A` — are excluded (non-positive).

**Disposition (honest sorry).**  The two parts have different status:

  * The *characterisation* `FrobeniusPositive c ↔ (0 ≤ parentProd c ∧
    0 ≤ daughterProd c)` is the *definition* of Frobenius-positivity in
    terms of the parent/daughter products and holds `by rfl`/`Iff.rfl`
    against the predicate as defined below — it is recorded as a `def`.

  * The *count* `(excludedConfigs).card = 2^(A-1)` is the genuine
    combinatorial claim.  Establishing it requires the spectator-factor
    sign structure of the products `G_{nₘ}(cₘ)` (which fixes, per added
    cell, the sign of each factor and hence the parity of the product),
    i.e. the Hoefsmit/Markov-trace `G`-function machinery and the
    confinement-LP feasibility argument `Gx ≥ 0` — none of which is
    present in this file.  The proposition is therefore stated faithfully
    over real types (a `Fintype` configuration space, a real non-negativity
    predicate, a real cardinality conclusion) and closed with `sorry`.

This replaces the previous self-assuming `class … Context` whose fields
*were* the manuscript conclusions (`claim_i_positivity_condition`,
`claim_ii_exclusion_count`) with a `theorem … := ⟨ctx.…, ctx.…⟩`
projection (forbidden by AGENTS.md §1a / §3b-cond rule 5).

## Base ring (§7c)

The proved core (`parity_odd_card`, `frobenius_positivity_filter`) lives
entirely in `ZMod 2` and `Finset` and mentions no scalars at all. The only
scalars are the parent/daughter Hoefsmit `G`-function products, and the sole
thing asked of them is `0 ≤ ·`; so they take values in a generic ordered
commutative ring and the substrate evaluation is `R := ℝ`.
-/

namespace QOU.ParticleInteractions

variable {R : Type*} [CommRing R] [PartialOrder R]

/-- The four crossing channels of a single nucleon factor:
    trivial, confined, unconfined, sign. -/
inductive Channel
  | triv
  | conf
  | unconf
  | sign
deriving DecidableEq, Fintype

/-- A channel configuration for a mass-`A` decay is an assignment of a
    `Channel` to each of the `A` factors. -/
abbrev Config (A : ℕ) := Fin A → Channel

/-- There are `4^A` channel configurations.  (Real, sorry-free fact about
    the configuration space — the "out of `4^A`" half of the count.) -/
theorem card_config (A : ℕ) : Fintype.card (Config A) = 4 ^ A := by
  rw [Fintype.card_fun, Fintype.card_fin]
  rfl  -- `Fintype.card Channel = 4`

/-- The parent / daughter mass products are real-valued functions of the
    configuration (`m_par = ∏ₘ G_{nₘ}(cₘ)`, `m_dau = ∏ₘ G_{n'ₘ}(cₘ)`).
    Their precise definition is the Hoefsmit/Markov `G`-function product;
    here they are carried as data so the positivity predicate and the
    exclusion count below are stated over the *actual* products. -/
structure ProductData (R : Type*) [CommRing R] [PartialOrder R] (A : ℕ) where
  /-- Parent product `m_{e,par}(c) = ∏ₘ G_{nₘ}(cₘ)`. -/
  parentProd : Config A → R
  /-- Daughter product `m_{e,dau}(c) = ∏ₘ G_{n'ₘ}(cₘ)`. -/
  daughterProd : Config A → R

/-- A configuration is **Frobenius-positive** when both the parent and the
    daughter mass products are non-negative. -/
def FrobeniusPositive {A : ℕ} (P : ProductData R A) (c : Config A) : Prop :=
  0 ≤ P.parentProd c ∧ 0 ≤ P.daughterProd c

/-- **Characterisation (definitional).** Frobenius-positivity is exactly
    the conjunction of parent- and daughter-product non-negativity.  This
    is the manuscript's part (i); it holds by definition of the predicate
    (it is *not* projected from a context field — the predicate is defined
    by this conjunction). -/
theorem frobeniusPositive_iff {A : ℕ} (P : ProductData R A) (c : Config A) :
    FrobeniusPositive P c ↔ (0 ≤ P.parentProd c ∧ 0 ≤ P.daughterProd c) :=
  Iff.rfl

/-- The set of **excluded** (non-Frobenius-positive) configurations. -/
noncomputable def excludedConfigs {A : ℕ} (P : ProductData R A)
    [DecidablePred (FrobeniusPositive P)] : Finset (Config A) :=
  Finset.univ.filter (fun c => ¬ FrobeniusPositive P c)

/-! ## §2  The exclusion count over the sign-pattern space

The manuscript claims `2^{A-1}` excluded configurations.  The honest carrier of
that count is **not** the full `4^A` configuration space (over which the count
is `P`-dependent and false for generic `P` — an all-positive product excludes
nothing; see
[`docs/audits/2026-07-05-frobenius-positivity-filter-lean-overgeneralization.md`](../../../../../docs/audits/2026-07-05-frobenius-positivity-filter-lean-overgeneralization.md)),
but the **`2^A` per-factor sign-pattern space** `Fin A → ZMod 2`, on which the
exclusion is governed by the *odd total parity* of the per-factor signs
(product `∏ₘ G(cₘ)` is negative ⟺ an odd number of factors are negative).  On
that space the count is a clean, unconditional combinatorial fact — exactly half
the parity-vectors are odd — proved here sorry-free. -/

/-- **Parity count (provable core).** Exactly half — `2^{A-1}` — of the `2^A`
    per-factor sign-patterns `Fin A → ZMod 2` have odd total parity
    `∑ᵢ sᵢ = 1`.

    Proof: drop the last coordinate.  Any tail `t : Fin (A-1) → ZMod 2` extends
    to a *unique* odd-parity vector (the head is forced to `1 − ∑ t`), so the
    odd-parity set is in bijection with `Fin (A-1) → ZMod 2`, which has
    cardinality `2^{A-1}`. -/
theorem parity_odd_card (A : ℕ) (hA : 1 ≤ A) :
    (Finset.univ.filter (fun s : Fin A → ZMod 2 => ∑ i, s i = 1)).card
      = 2 ^ (A - 1) := by
  classical
  obtain ⟨B, rfl⟩ : ∃ B, A = B + 1 := ⟨A - 1, (Nat.succ_pred_eq_of_pos hA).symm⟩
  simp only [Nat.add_sub_cancel]
  -- `2^B = card (Fin B → ZMod 2)`.
  have h2B : (2 : ℕ) ^ B = (Finset.univ : Finset (Fin B → ZMod 2)).card := by
    rw [Finset.card_univ, Fintype.card_fun, Fintype.card_fin, ZMod.card]
  rw [h2B]
  -- Bijection `{s : ∑ s = 1} ≃ (Fin B → ZMod 2)` via `s ↦ tail s`, inverse
  -- `t ↦ cons (1 − ∑ t) t`.
  refine Finset.card_bij'
    (fun s _ => Fin.tail s)
    (fun t _ => Fin.cons (1 - ∑ i, t i) t)
    ?_ ?_ ?_ ?_
  · -- forward lands in `univ`
    intro s _; exact Finset.mem_univ _
  · -- inverse lands in the odd-parity filter
    intro t _
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    rw [Fin.sum_univ_succ, Fin.cons_zero]
    simp only [Fin.cons_succ]
    ring
  · -- left inverse: `cons (1 − ∑ tail) (tail s) = s`
    intro s hs
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hs
    have hhead : (1 : ZMod 2) - ∑ i : Fin B, Fin.tail s i = s 0 := by
      have hs' := hs
      rw [Fin.sum_univ_succ] at hs'
      simp only [Fin.tail]
      exact (eq_sub_of_add_eq hs').symm
    dsimp only
    rw [hhead, Fin.cons_self_tail]
  · -- right inverse: `tail (cons h t) = t`
    intro t _
    exact Fin.tail_cons _ _

/-- **Frobenius positivity filter — corrected, proved (manuscript part (ii)).**

    *Conditional on the sign-mechanism characterisation* `hchar` (a
    configuration is excluded ⟺ its per-factor sign-pattern `signOf c` has odd
    total parity — the Hoefsmit spectator-factor structure), exactly `2^{A-1}`
    of the `2^A` sign-patterns are excluded, for `A ≥ 1`.

    The hypothesis `hchar` carries the *mechanism* (the physical input); the
    `2^{A-1}` count is then **derived** from `parity_odd_card` (no `sorry`).
    This replaces the previous unconditional statement over the `4^A`
    configuration space, which was false for generic `ProductData` (see the
    audit doc referenced above). -/
-- Ref: [hoefsmit1974] Representations of Hecke algebras of finite groups
--      with BN-pairs of classical type (PhD thesis, UBC) — seminormal
--      G-function factors whose signs drive the exclusion parity.
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/frobenius-positivity-filter.md
theorem frobenius_positivity_filter
    {A : ℕ} (hA : 1 ≤ A)
    (excludedSign : (Fin A → ZMod 2) → Prop) [DecidablePred excludedSign]
    (hchar : ∀ s, excludedSign s ↔ ∑ i, s i = 1) :
    (Finset.univ.filter excludedSign).card = 2 ^ (A - 1) := by
  rw [Finset.filter_congr (fun s _ => by rw [hchar s])]
  exact parity_odd_card A hA

end QOU.ParticleInteractions
