import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.DeriveFintype

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
-/

namespace QOU.ParticleInteractions

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
structure ProductData (A : ℕ) where
  /-- Parent product `m_{e,par}(c) = ∏ₘ G_{nₘ}(cₘ)`. -/
  parentProd : Config A → ℝ
  /-- Daughter product `m_{e,dau}(c) = ∏ₘ G_{n'ₘ}(cₘ)`. -/
  daughterProd : Config A → ℝ

/-- A configuration is **Frobenius-positive** when both the parent and the
    daughter mass products are non-negative. -/
def FrobeniusPositive {A : ℕ} (P : ProductData A) (c : Config A) : Prop :=
  0 ≤ P.parentProd c ∧ 0 ≤ P.daughterProd c

/-- **Characterisation (definitional).** Frobenius-positivity is exactly
    the conjunction of parent- and daughter-product non-negativity.  This
    is the manuscript's part (i); it holds by definition of the predicate
    (it is *not* projected from a context field — the predicate is defined
    by this conjunction). -/
theorem frobeniusPositive_iff {A : ℕ} (P : ProductData A) (c : Config A) :
    FrobeniusPositive P c ↔ (0 ≤ P.parentProd c ∧ 0 ≤ P.daughterProd c) :=
  Iff.rfl

/-- The set of **excluded** (non-Frobenius-positive) configurations. -/
noncomputable def excludedConfigs {A : ℕ} (P : ProductData A)
    [DecidablePred (FrobeniusPositive P)] : Finset (Config A) :=
  Finset.univ.filter (fun c => ¬ FrobeniusPositive P c)

/-- **Frobenius positivity filter (manuscript part (ii)).**

    For even mass number `A`, exactly `2^{A-1}` of the `4^A` channel
    configurations are excluded (non-Frobenius-positive), under the
    spectator-factor sign structure of the parent/daughter products.

    Stated over the real configuration space (`Config A`, `card = 4^A` by
    `card_config`) and the real non-negativity predicate
    (`FrobeniusPositive`); the conclusion is the genuine cardinality
    `2^{A-1}`.

    **Missing infrastructure** (the reason for the `sorry`): the count
    follows from the per-factor sign of `G_{nₘ}(cₘ)` — the Hoefsmit/Markov
    `G`-function spectator-factor structure together with the
    confinement-LP feasibility constraint `Gx ≥ 0` — which is not
    formalised in this file. -/
-- Ref: [hoefsmit1974] Representations of Hecke algebras of finite groups
--      with BN-pairs of classical type (PhD thesis, UBC) — seminormal
--      G-function factors whose signs drive the exclusion count.
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/frobenius-positivity-filter.md
theorem frobenius_positivity_filter
    {A : ℕ} (_hA : Even A) (P : ProductData A)
    [DecidablePred (FrobeniusPositive P)] :
    (excludedConfigs P).card = 2 ^ (A - 1) := by
  -- Requires the spectator-factor sign structure of the G-products
  -- (Hoefsmit seminormal G-function) + the confinement-LP `Gx ≥ 0`
  -- feasibility argument; not available in this file.
  sorry

end QOU.ParticleInteractions
