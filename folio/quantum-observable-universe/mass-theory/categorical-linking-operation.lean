/-
  Categorical linking operation Lk_R: ribbon-category dual of
  topological linking number.

  Companion: categorical-linking-operation.md
  Path: folio/quantum-observable-universe/mass-theory/

  Content-bearing conjecture carrier (AGENTS.md §3b-tax): the open
  properties are stated over an explicit substrate `LinkingData`, and
  the class has **no instance**.

  History (bean `qou-yt29`, 2026-09-04).  Until this revision the file
  carried five `def Lk… : Prop` "hypothesis predicates" and a global
  `instance canonical` closing all five, so `conj:categorical-linking-
  operation` was discharged for free.  Two of the five were literally
  `:= True`, closed by `trivial`:

      LkMultiplicative      _R_ : Prop := True
      LkTraceCutSymmetric   _R_ : Prop := True

  The other three were **not** `True` syntactically but were `True`
  extensionally — each was a ring or integer identity that holds in
  every `CommRing`, carrying a docstring that claimed a categorical
  statement about `Lk_R`:

      LkLinear                q := ∀ a b c : R, a*(b+c) = a*b+a*c ∧ …   (distributivity)
      LkReductionAtZero       q := q ^ (0 : ℕ) = 1                      (`pow_zero`)
      LkBarInvolutionCompatible q := ∀ k : ℤ, -(-k) = k                 (`neg_neg`; does
                                                                         not mention `q`)

  So the vacuity was 5/5, not 2/5: the named theorems that "discharged"
  them proved distributivity, `pow_zero` and `neg_neg`, never a property
  of a linking operation, and the class they built was inhabited for
  every `R` and every `q`.

  Now: `LinkingData` carries the substrate (Frobenius trace `τ_R`, the
  braiding as a unit `c : Aˣ`, the rigid dual, the bar involution);
  `LinkingData.lk` and `LinkingData.preLk` are the `.md`'s operations;
  Properties 1 and 2 and the **pre-trace** half of Property 3 are proved
  about `lk`/`preLk` themselves; the post-trace half of Property 3 and
  Properties 4 and 5 are the class fields, with no instance.
  `postTraceMultiplicative_fails` exhibits data violating the first
  field, so the class is a constraint rather than a filter that
  everything passes.

  Refs:
    [kassel1995] Kassel, "Quantum Groups," Springer 1995,
       §X (rigid monoidal categories), §XIV (ribbon-category braiding).
    [turaev2010quantum] Turaev, "Quantum Invariants of Knots
       and 3-Manifolds," de Gruyter 2010, §I (closed-braid
       invariants).
    [jones1987] Jones, Ann. Math. 126 (1987) — the Markov trace.
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Algebra.Prod
import Mathlib.Algebra.Module.Basic
import Mathlib.LinearAlgebra.Prod
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.BraidsAndKnots

/--
  **Markov-trace cyclicity (axiomatised typeclass).** A type-level
  carrier `T` for the Markov trace `tr_M : T → R` together with the
  cyclicity identity `tr_M (A * B) = tr_M (B * A)` for all `A B : T`.

  This is the categorical content of `prop:frobenius-gram-matrix`'s
  symmetry clause: the Gram matrix `G_{ij} = tr_M (b_i * b_j)` is
  symmetric *because of* Markov-trace cyclicity. The post-trace
  cyclicity rewrite below takes this class as an explicit hypothesis
  (§3b-cond conditional pattern); any concrete substrate
  `T = H_n(q)` satisfies `MarkovTraceCyclic` by the standard Markov-
  property argument (peel boundary generator from the right; cite
  prop:frobenius-gram-matrix §"Markov trace of NF basis elements").
-/
-- Ref: [leitner2026] prop:frobenius-gram-matrix
-- Ref: [jones1987] DOI:10.2307/1971403 (Markov-trace cyclicity for H_n)
class MarkovTraceCyclic
    (T : Type*) [Mul T] (R : Type*) (tr_M : T → R) : Prop where
  /-- Cyclicity: `tr_M (A * B) = tr_M (B * A)` for all `A B : T`. -/
  tr_cyclic : ∀ A B : T, tr_M (A * B) = tr_M (B * A)

/-- **Two-factor Markov-trace swap (sorry-free, conditional on
    `MarkovTraceCyclic`).** Direct restatement of the class field
    `tr_cyclic`. The conclusion is exactly the two-factor swap,
    not the full post-trace multiplicativity-in-`k` identity; the
    latter follows from this swap *plus* the pre-trace integer-power
    group law of `c_{A,A}` and is captured by
    `markov_trace_cyclic_three_factor` below. -/
-- Ref: [leitner2026] prop:frobenius-gram-matrix § "Markov trace
--      of NF basis elements"
theorem markov_trace_swap
    {T : Type*} [Mul T] {R : Type*} (tr_M : T → R)
    [hC : MarkovTraceCyclic T R tr_M]
    (A B : T) :
    tr_M (A * B) = tr_M (B * A) :=
  hC.tr_cyclic A B

/-- **Three-factor cyclic rotation (sorry-free).** With `[Semigroup T]`
    providing associativity, the two-factor Markov-trace swap lifts
    to the cyclic-rotation identity
        `tr_M (A * B * C) = tr_M (B * C * A)`
    which is the structural shape `tr_M (c^{k_1} * X * c^{k_2}) =
    tr_M (c^{k_2} * c^{k_1} * X)` mentioned in the linking-operation
    post-trace discussion (with `A := c^{k_1}`, `B := X`,
    `C := c^{k_2}` and one extra application of the two-factor swap
    on the inner factors). The Hecke-power group law lifts a
    concrete `c^{k_1} * c^{k_2}` to `c^{k_1 + k_2}`; combined with
    this rotation, that is the cyclicity half of the post-trace
    multiplicativity step flagged as open in
    `categorical-linking-operation.md` §"Proof of Property 3". -/
-- Ref: [leitner2026] prop:frobenius-gram-matrix
-- Ref: [leitner2026] categorical-linking-operation.md §"Proof of Property 3"
theorem markov_trace_cyclic_three_factor
    {T : Type*} [Semigroup T] {R : Type*} (tr_M : T → R)
    [hC : MarkovTraceCyclic T R tr_M]
    (A B C : T) :
    tr_M (A * B * C) = tr_M (B * C * A) := by
  -- View `A * B * C` as `(A) * (B * C)` (mul_assoc), then swap.
  rw [mul_assoc]
  exact hC.tr_cyclic A (B * C)

/-- **Conditional trace-cut substitution lemma (sorry-free).** Under
    `[MarkovTraceCyclic T R tr_M]`, the trace-cut transformation
    underlying property 4 reduces (after strand-swap) to a single
    application of the two-factor cyclicity identity:
        `tr_M ((a * b) * c) = tr_M (c * (a * b))`.
    The full trace-cut symmetry statement (with the `k → -k`
    exponent shift) requires *additionally* the ribbon-category
    braiding-inversion identity `c⁻¹ = c̄`, which is downstream
    structure not exposed in this Hecke-level lemma. The lemma
    here records the cyclicity half of the discharge sorry-free. -/
-- Ref: [leitner2026] prop:frobenius-gram-matrix
-- Ref: [leitner2026] categorical-linking-operation.md §"Proof of Property 4"
theorem trace_cut_cyclicity_step
    {T : Type*} [Semigroup T] {R : Type*} (tr_M : T → R)
    [hC : MarkovTraceCyclic T R tr_M]
    (a b c : T) :
    tr_M ((a * b) * c) = tr_M (c * (a * b)) :=
  hC.tr_cyclic (a * b) c

/-! ## The substrate the linking operation is defined over -/

/-- **The data the `.md`'s linking operation is built from.**  An
    `R`-algebra `A` (intended: the Frobenius–Hopf substrate, `H_n(q)`
    inside `End_R(V^{⊗n})`) together with

    * `tau` — the Frobenius trace `τ_R : A →ₗ[R] R`;
    * `c` — the braiding `c_{A,A}` as a **unit** of `A`, which is what
      makes the integer power `c^k` for `k : ℤ` (the linking index)
      available at all;
    * `dual` — the rigid dual `a ↦ a^*`, an `R`-linear map;
    * `bar` — the bar involution `ι` (the Hecke antipode
      `ι(σ_i) = σ_i^{-1}` at the substrate level).

    The structure only *names* the data; which of its inhabitants are
    the ribbon-categorical ones is what the conjecture class below
    asserts. -/
structure LinkingData (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A] where
  /-- The Frobenius trace `τ_R : A →ₗ[R] R`. -/
  tau : A →ₗ[R] R
  /-- The braiding `c_{A,A}`, as a unit (so `c ^ (k : ℤ)` exists). -/
  c : Aˣ
  /-- The rigid dual `a ↦ a^*`. -/
  dual : A →ₗ[R] A
  /-- The bar involution `ι`. -/
  bar : A → A

namespace LinkingData

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **The pre-trace morphism** `PreLk_R^{(k)}(a, b) := c_{A,A}^k ∘ (a ⊗ b)`
    of `categorical-linking-operation.md` §"Proof of Property 3". -/
def preLk (D : LinkingData R A) (k : ℤ) (a b : A) : A := ↑(D.c ^ k) * (a * b)

/-- **The categorical linking operation** `Lk_R^{(k)}(a, b)` of the `.md`:
    close the second component through the Frobenius trace after linking
    it to the first by `k` braidings, leaving the first as the free
    endomorphism `a^*`:

        Lk_R^{(k)}(a, b) = τ_R(c^k · b) · a^*.

    At `k = 0` this is the `.md`'s Property 2 verbatim
    (`Lk_R^{(0)}(a, b) = τ_R(b) · a^*`) — see `lk_zero`. -/
def lk (D : LinkingData R A) (k : ℤ) (a b : A) : A := D.tau (↑(D.c ^ k) * b) • D.dual a

end LinkingData

/-! ## Property 1 — bilinearity (PROVED, about `lk` itself)

The previous revision "proved" this as `∀ a b c : R, a*(b+c) = a*b+a*c`,
i.e. distributivity in the coefficient ring, which holds in every
`CommRing` and says nothing about any linking operation.  What follows is
the bilinearity of `lk`, discharged from `LinearMap.map_add` /
`LinearMap.map_smul` on `tau` and `dual`. -/

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- `Lk_R^{(k)}(−, b)` is additive. -/
-- Ref: [kassel1995] §XIV (R-linear rigid monoidal axioms)
-- Ref: [leitner2026] categorical-linking-operation.md §"Proof of Property 1"
theorem lk_add_left (D : LinkingData R A) (k : ℤ) (a a' b : A) :
    D.lk k (a + a') b = D.lk k a b + D.lk k a' b := by
  unfold LinkingData.lk
  rw [map_add, smul_add]

/-- `Lk_R^{(k)}(−, b)` is `R`-homogeneous. -/
theorem lk_smul_left (D : LinkingData R A) (k : ℤ) (r : R) (a b : A) :
    D.lk k (r • a) b = r • D.lk k a b := by
  unfold LinkingData.lk
  rw [map_smul, smul_comm]

/-- `Lk_R^{(k)}(a, −)` is additive. -/
theorem lk_add_right (D : LinkingData R A) (k : ℤ) (a b b' : A) :
    D.lk k a (b + b') = D.lk k a b + D.lk k a b' := by
  unfold LinkingData.lk
  rw [mul_add, map_add, add_smul]

/-- `Lk_R^{(k)}(a, −)` is `R`-homogeneous. -/
theorem lk_smul_right (D : LinkingData R A) (k : ℤ) (r : R) (a b : A) :
    D.lk k a (r • b) = r • D.lk k a b := by
  unfold LinkingData.lk
  rw [mul_smul_comm, map_smul, smul_assoc]

/-- **Property 1 (`.md`), proved: `Lk_R^{(k)}` is `R`-bilinear.** -/
theorem lk_bilinear (D : LinkingData R A) (k : ℤ) :
    (∀ a a' b : A, D.lk k (a + a') b = D.lk k a b + D.lk k a' b) ∧
    (∀ (r : R) (a b : A), D.lk k (r • a) b = r • D.lk k a b) ∧
    (∀ a b b' : A, D.lk k a (b + b') = D.lk k a b + D.lk k a b') ∧
    (∀ (r : R) (a b : A), D.lk k a (r • b) = r • D.lk k a b) :=
  ⟨lk_add_left D k, lk_smul_left D k, lk_add_right D k, lk_smul_right D k⟩

/-! ## Property 2 — reduction at `k = 0` (PROVED, about `lk` itself) -/

/-- **Property 2 (`.md`), proved:** `Lk_R^{(0)}(a, b) = τ_R(b) · a^*`.
    The previous revision "proved" this as `q ^ (0 : ℕ) = 1`. -/
-- Ref: [kassel1995] §X (rigid monoidal categories, coev/eval, duals)
-- Ref: [leitner2026] categorical-linking-operation.md §"Proof of Property 2"
theorem lk_zero (D : LinkingData R A) (a b : A) :
    D.lk 0 a b = D.tau b • D.dual a := by
  unfold LinkingData.lk
  rw [zpow_zero, Units.val_one, one_mul]

/-! ## Property 3 — multiplicativity in the linking index

The **pre-trace** half is proved here from the integer-power group law of
`c_{A,A}` in `Aˣ`; the **post-trace** half needs a substrate-specific
commutation identity and is a class field below.  The `.md` lists
Property 3 under "proved"; that is the pre-trace statement. -/

/-- **Property 3, pre-trace half (PROVED):** additional linkings are
    pre-composition with `c_{A,A}`,
    `PreLk^{(k₁+k₂)}(a, b) = c^{k₂} · PreLk^{(k₁)}(a, b)`, by
    `zpow_add` in the group `Aˣ`. -/
-- Ref: [kassel1995] §X (integer-power group law in monoidal categories)
-- Ref: [leitner2026] categorical-linking-operation.md §"Proof of Property 3"
theorem preLk_add (D : LinkingData R A) (k₁ k₂ : ℤ) (a b : A) :
    D.preLk (k₁ + k₂) a b = ↑(D.c ^ k₂) * D.preLk k₁ a b := by
  unfold LinkingData.preLk
  rw [add_comm k₁ k₂, zpow_add, Units.val_mul, mul_assoc]

/-! ## The conjecture -/

/--
  **Conjecture carrier (primary, content-bearing, NO instance).**
  `CategoricalLinkingOperation R A D` asserts the three properties of
  `conj:categorical-linking-operation` that are *not* generic:

  * `postTraceMultiplicative` — Property 3 **after** the trace cut.  The
    pre-trace statement is `preLk_add` above and is proved; lifting it
    through `τ_R` needs the substrate commutation identity
    `τ_R(c^{k₂} · x) = c^{k₂} · τ_R(x)`-in-the-relevant-sense, which the
    `.md` does not supply.  `postTraceMultiplicative_fails` below
    exhibits data for which this field is **false**, so it is a genuine
    constraint.
  * `traceCutSymmetric` — Property 4: cutting the other component
    produces the `ι`-conjugate with reversed linking sign.  Conditional
    on Markov-trace cyclicity (whose half is proved above as
    `trace_cut_cyclicity_step`) *and* ribbon braiding inversion
    `ι(c) = c⁻¹`, which is not part of `LinkingData`.
  * `barCompatible` — Property 5: `ι(Lk^{(k)}(a,b)) = Lk^{(-k)}(ι a, ι b)`,
    conditional on bar-functoriality of `c` and `τ_R`.

  Properties 1 and 2 are **not** fields: they are proved unconditionally
  above (`lk_bilinear`, `lk_zero`), so carrying them as hypotheses would
  overstate what is open.

  **Tower status (owner ruling 2026-09-03): ORDER-ZERO-ONLY.**  The
  operation is stated at a single fixed substrate `A`; the `H_n(q)` tower
  is not used.

  No instance is provided; supplying one asserts the conjecture. -/
-- Ref: [leitner2026] conj:categorical-linking-operation
-- Ref: [kassel1995] §XIV (ribbon-category braiding, bar-functoriality)
class CategoricalLinkingOperation
    (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A]
    (D : LinkingData R A) : Prop where
  /-- Property 3, post-trace: `Lk^{(k₁+k₂)}(a,b) = c^{k₂} · Lk^{(k₁)}(a,b)`. -/
  postTraceMultiplicative :
    ∀ (k₁ k₂ : ℤ) (a b : A), D.lk (k₁ + k₂) a b = ↑(D.c ^ k₂) * D.lk k₁ a b
  /-- Property 4: `Lk^{(k)}(a,b) = ι(Lk^{(-k)}(b,a))`. -/
  traceCutSymmetric :
    ∀ (k : ℤ) (a b : A), D.lk k a b = D.bar (D.lk (-k) b a)
  /-- Property 5: `ι(Lk^{(k)}(a,b)) = Lk^{(-k)}(ι a, ι b)`. -/
  barCompatible :
    ∀ (k : ℤ) (a b : A), D.bar (D.lk k a b) = D.lk (-k) (D.bar a) (D.bar b)

/-- **Conditional consequence (§3b-cond).**  *If* the conjecture holds,
    the trace-cut symmetry and the bar compatibility compose into the
    self-conjugacy statement `ι(Lk^{(-k)}(b,a)) = Lk^{(-k)}(ι a, ι b)` —
    derived from two fields, not read off one. -/
theorem lk_bar_trace_cut_compose
    {D : LinkingData R A} [inst : CategoricalLinkingOperation R A D]
    (k : ℤ) (a b : A) :
    D.bar (D.bar (D.lk (-k) b a)) = D.lk (-k) (D.bar a) (D.bar b) := by
  rw [← inst.traceCutSymmetric k a b]
  exact inst.barCompatible k a b

/-! ## The first field is a genuine constraint, not a filter everything passes

A conjecture class earns the label "content-bearing" only if some data
*fails* it.  Here is such data: `A = ℚ × ℚ` with the sum-of-coordinates
Frobenius trace and the non-scalar braiding unit `c = (2, 3)`.  Because
`c` is not a scalar, `τ_R(c^k · b)` is not `c^k` times `τ_R(b)`, and the
post-trace multiplicativity field is false at `k₁ = 0`, `k₂ = 1`. -/

/-- Counterexample data over `ℚ × ℚ`: trace `(x, y) ↦ x + y`, braiding
    `c = (2, 3)`, dual and bar the identity. -/
def counterexampleData : LinkingData ℚ (ℚ × ℚ) where
  tau := LinearMap.fst ℚ ℚ ℚ + LinearMap.snd ℚ ℚ ℚ
  c := ⟨(2, 3), (2⁻¹, 3⁻¹), by norm_num [Prod.ext_iff], by norm_num [Prod.ext_iff]⟩
  dual := LinearMap.id
  bar := id

/-- **The `postTraceMultiplicative` field is falsifiable** — it fails for
    `counterexampleData` at `k₁ = 0`, `k₂ = 1`, `a = (1,1)`, `b = (1,0)`:
    the left side is `(2, 2)` and the right side is `(2, 3)`.  So
    `CategoricalLinkingOperation` is not satisfied by every
    `LinkingData`, which is what the removed global `instance canonical`
    asserted. -/
theorem postTraceMultiplicative_fails :
    ¬ (∀ (k₁ k₂ : ℤ) (a b : ℚ × ℚ),
        counterexampleData.lk (k₁ + k₂) a b
          = ↑(counterexampleData.c ^ k₂) * counterexampleData.lk k₁ a b) := by
  intro h
  have := h 0 1 (1, 1) (1, 0)
  simp [LinkingData.lk, counterexampleData, Prod.ext_iff] at this

/-- **Corollary: no global instance exists.**  A `CategoricalLinkingOperation`
    for every `LinkingData` would in particular give one for
    `counterexampleData`, contradicting `postTraceMultiplicative_fails`. -/
theorem no_global_instance :
    ¬ (∀ (R : Type) [CommRing R] (A : Type) [Ring A] [Algebra R A]
        (D : LinkingData R A), CategoricalLinkingOperation R A D) := by
  intro h
  exact postTraceMultiplicative_fails (h ℚ (ℚ × ℚ) counterexampleData).postTraceMultiplicative

end QOU.BraidsAndKnots
