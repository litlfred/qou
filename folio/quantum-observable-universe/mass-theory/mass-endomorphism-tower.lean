import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Prod
import Mathlib.Tactic.Linarith

/-!
# Mass Endomorphism: Proton–Electron Mass Tower (convention D, `Li₂^q`)

The mass of a vortex with braid representative `β ∈ Bₙ` decomposes into
a descended term (base-level regular-representation trace) and transient
`Li₂^q` corrections, one per generator and one per pair of distinct
generators.

**Two-tier split.** Per the audit
[`docs/audits/2026-05-03-pre-archimedean-proof-audit.md`](../../../docs/audits/2026-05-03-pre-archimedean-proof-audit.md)
§1 Step 18a, the algebraic mass-tower (which lives in `H_n(R, q)` over
`R ⊇ ℤ[q^±1]`) is kept separate from its numerical evaluation at
`q = q₀ ∈ ℝ`.  This file carries two tiers:

  - `QOU.MassEndomorphism.Pre` — pre-Archimedean: polymorphic in the
    ground field `R` (`{R : Type u} [Field R]`); the `q`-dilogarithm
    `Li₂^q` and the Frobenius norm `‖·‖_F` are opaque `R → R` data
    (Habiro / formal-series), and the Markov parameter is
    `z = q³/(q²+1)` (**convention D**, owner ruling 2026-08-15).
  - `QOU.MassEndomorphism` (order tier) — specialised to an ordered
    field (`[Field R] [LinearOrder R] [IsStrictOrderedRing R]`).  The
    Archimedean-side result here is the mass formula's **positivity**:
    under a genuine (`0 ≤ ‖·‖_F`) norm and the bounded-Rogers sign
    `Li₂^q(-x) ≤ 0` for `0 ≤ x`, the mass `𝔪(ϱ)` is `≥ 0`, and `> 0`
    once its descended term is `> 0`.  This is *not* the numerical
    proton–electron ratio — that stays the compute witness
    (`habiro_exact_mass_endomorphism.py`), not a Lean claim.

**Convention D + bounded `Li₂^q`.** The canonical formula (see the
`.md`) is
`𝔪(ϱ) = |∏ V̂ᵢ| − Σᵢ Li₂^q(−|V̂ᵢ|) − Σ z²·Li₂^q(−|V̂ᵢ·V̂ⱼ|)`,
with `z = q³/(q²+1)`.  The bounded symmetric Rogers `Li₂^q` REPLACES
the older Faddeev `Φ_q` truncation, which was **refuted 2026-06-18**
(empirically incompatible with isospin symmetry; massive mirror-nucleus
pathologies).  `li2q` here is abstract — its bounded sign is carried as
the `MassPositivityHyp` hypothesis, not by formalising the series.

Content blocks: prop:mass-endomorphism-tower,
     conj:mass-endomorphism-conjecture,
     thm:topological-mass (decomposition theorem),
     def:hecke-mass-element (categorical definition)
-/

universe u

namespace QOU.MassEndomorphism

/-! ## §1.  Pre-Archimedean tier (formal `R`-valued mass) -/

namespace Pre

variable {R : Type u} [Field R]

/-- Markov parameter `z = q³/(q²+1)` (**convention D**, owner ruling
    2026-08-15), valued in the ground field `R`.  Supersedes the excised
    convention-C form `√q/(q+1)`. -/
noncomputable def markovZD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The pair blow-up sum: `Σ_{i<j} Li₂^q(−‖V i · V j‖_F)` over **all**
    unordered pairs of distinct generators, as in the `.md` boxed formula
    (`0 ≤ i < j ≤ n−2`) and in the producer
    (`computations/habiro/habiro_exact_mass_endomorphism.py`, the loop
    `for i … for j in range(i + 1, n)`).  Until 2026-11-20 this file summed
    only the adjacent pairs `(i, i+1)`; the two agree for at most two
    generators and differ from three on (bean `qou-j11h`). -/
noncomputable def pairSum (frobeniusNorm li2q : R → R) (n : ℕ) (V : Fin n → R) : R :=
  ∑ p ∈ (Finset.univ.filter (fun p : Fin n × Fin n => p.1 < p.2)),
    li2q (- frobeniusNorm (V p.1 * V p.2))

/-- The pre-Arch mass formula, valued in the ground field `R`.

    Each generator's traced volume `V i ∈ R` is supplied as data; the
    Frobenius norm `‖·‖_F : R → R` and the symmetric `q`-dilogarithm
    `Li₂^q : R → R` are also passed in (abstract; no Archimedean `|·|`,
    no series).  Signs and the `z²` pair weight follow the `.md` boxed
    formula (convention D):

      𝔪 = ‖∏ V i‖_F − Σᵢ Li₂^q(−‖V i‖_F)
            − z² · Σ_{i<j} Li₂^q(−‖V i · V j‖_F),   z = q³/(q²+1).

    `V` is indexed by the generators (`Fin n` here is the `n − 1` of the
    `.md`, which counts strands).  The file is trace- and weight-agnostic:
    `V i` is data, so nothing here decides whether the descended term is the
    Markov trace or the regular-representation trace, or which Wedderburn
    weights build `V i`.  The producer uses the regular-representation
    reading with self-normalised `dim_q(λ)²/[3]_q!` weights. -/
noncomputable def massPoly (frobeniusNorm li2q : R → R) (q : R) (n : ℕ)
    (V : Fin n → R) : R :=
  frobeniusNorm (∏ i, V i)
    - (∑ i, li2q (- frobeniusNorm (V i)))
    - (markovZD q) ^ 2 * pairSum frobeniusNorm li2q n V

end Pre

/-! ## §2.  Order tier — positivity of the mass formula -/

variable {R : Type u} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The hypotheses under which the mass endomorphism is non-negative:
    a genuine (non-negative) Frobenius norm, and the bounded-Rogers sign
    of the symmetric `q`-dilogarithm.  The second field is exactly why
    the bounded `Li₂^q` replaced the Faddeev `Φ_q`: on the physical
    (non-negative-norm) arguments the `Φ_q` face blows up and changes
    sign, whereas `Li₂^q(−x) ≤ 0` for `0 ≤ x`. -/
structure MassPositivityHyp (frobeniusNorm li2q : R → R) : Prop where
  /-- The Frobenius norm is genuinely a norm: non-negative everywhere. -/
  norm_nonneg : ∀ x, 0 ≤ frobeniusNorm x
  /-- Bounded-Rogers sign: `Li₂^q(−x) ≤ 0` on non-negative arguments. -/
  li2q_nonpos_on_neg : ∀ x, 0 ≤ x → li2q (-x) ≤ 0

/-- **The mass endomorphism is non-negative.**  Under `MassPositivityHyp`
    (a genuine norm + the bounded-Rogers dilog sign), the pre-Arch mass
    `Pre.massPoly` is `≥ 0` for every braid data `(q, n, V)`.

    Proof: the descended term `‖∏ V i‖_F ≥ 0`; both `Li₂^q` sums are
    `≤ 0` (each summand `Li₂^q(−‖·‖_F) ≤ 0` since `‖·‖_F ≥ 0`, then
    `Finset.sum_nonpos`); the pair weight `z² ≥ 0` (`sq_nonneg`), so
    `z²·(sum ≤ 0) ≤ 0`; hence `A − B − z²·D ≥ 0` with `A ≥ 0`, `B ≤ 0`,
    `z²·D ≤ 0`. -/
theorem mass_endomorphism_nonneg (frobeniusNorm li2q : R → R)
    (h : MassPositivityHyp frobeniusNorm li2q) (q : R) (n : ℕ) (V : Fin n → R) :
    0 ≤ Pre.massPoly frobeniusNorm li2q q n V := by
  unfold Pre.massPoly
  have hA : 0 ≤ frobeniusNorm (∏ i, V i) := h.norm_nonneg _
  have hB : (∑ i, li2q (- frobeniusNorm (V i))) ≤ 0 := by
    apply Finset.sum_nonpos
    intro i _
    exact h.li2q_nonpos_on_neg _ (h.norm_nonneg _)
  have hD : Pre.pairSum frobeniusNorm li2q n V ≤ 0 := by
    unfold Pre.pairSum
    apply Finset.sum_nonpos
    intro p _
    exact h.li2q_nonpos_on_neg _ (h.norm_nonneg _)
  have hz : 0 ≤ (Pre.markovZD q) ^ 2 := sq_nonneg _
  have hzD : (Pre.markovZD q) ^ 2 * Pre.pairSum frobeniusNorm li2q n V ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hz hD
  linarith

/-- **The mass endomorphism is strictly positive when its descended term
    is.**  Under `MassPositivityHyp`, if the descended trace term
    `‖∏ V i‖_F > 0` then the pre-Arch mass `Pre.massPoly > 0`.  This is
    the strict form of `mass_endomorphism_nonneg`: the two `Li₂^q`
    contributions are still `≤ 0`, so a strictly positive descended term
    dominates. -/
theorem mass_endomorphism_positive (frobeniusNorm li2q : R → R)
    (h : MassPositivityHyp frobeniusNorm li2q) (q : R) (n : ℕ) (V : Fin n → R)
    (hprod : 0 < frobeniusNorm (∏ i, V i)) :
    0 < Pre.massPoly frobeniusNorm li2q q n V := by
  unfold Pre.massPoly
  have hB : (∑ i, li2q (- frobeniusNorm (V i))) ≤ 0 := by
    apply Finset.sum_nonpos
    intro i _
    exact h.li2q_nonpos_on_neg _ (h.norm_nonneg _)
  have hD : Pre.pairSum frobeniusNorm li2q n V ≤ 0 := by
    unfold Pre.pairSum
    apply Finset.sum_nonpos
    intro p _
    exact h.li2q_nonpos_on_neg _ (h.norm_nonneg _)
  have hz : 0 ≤ (Pre.markovZD q) ^ 2 := sq_nonneg _
  have hzD : (Pre.markovZD q) ^ 2 * Pre.pairSum frobeniusNorm li2q n V ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hz hD
  linarith

end QOU.MassEndomorphism
