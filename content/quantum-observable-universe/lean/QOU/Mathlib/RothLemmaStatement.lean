/-
  **The statement of Roth's lemma**, written down so its hypotheses can be checked against
  named theorems — and the `m = 1` case proved.

  Bean `qou-4lbh`.

  ⚠⚠ `RothLemmaUniform` below is a **`def`, not a theorem.**  Nothing in this repository
  proves it for `m ≥ 2`.  It is a statement, written so that every hypothesis has to
  elaborate and so that the base case has something to be an instance *of*.  Do not cite it
  as though Roth's lemma were formalised.

  ⚠ It is also **not true for every `ω`.**  The growth condition is a genuine hypothesis of
  Roth's lemma: for `m ≥ 2` and small `ω` the statement is false.  At `m = 1` the condition is
  vacuous, which is why `rothLemmaUniform_one` holds for *every* `ω`.

  `ω`, `ε` and the bound `θ` are all left as parameters, which makes `RothLemmaUniform` a
  **statement schema** rather than a theorem-shaped claim: instantiating `θ` large enough makes
  it easy and uninteresting.  The content is *which* `θ` is achievable, and that is named
  separately by `RothBound` and assembled into `RothLemmaMahler` below — `ω = 1/t`, `ε = t/m`,
  `θ` meeting §14's bound.  Read those two together; neither alone is Roth's lemma.

  ═══ THE DESIGN QUESTION THIS SETTLES ═══

  Bean `qou-4lbh` recorded a choice between indexing the variables by `Fin m` (the ordering
  the growth condition needs comes free) and by `Unit ⊕ τ` (the shape all the separated
  machinery and the base case are already in).  Each entry argued for one and against the
  other, and the second overstated its case.

  **Neither is right.**  Keep the variable type `σ` *general* and carry the ordering as an
  `Equiv σ (Fin m)`.  Then:

  * the growth condition reads off the equiv, so nothing is lost against `Fin m`;
  * the base case instantiates at `σ = Unit` and `RothBaseCase.lean` applies **with no
    transport at all** — `rothLemmaUniform_one` below uses none;
  * the recursion can still split `σ` as `Unit ⊕ τ` for the separated machinery, via
    `index_rename_equiv`.

  The evidence is that `rothLemmaUniform_one` needed no reindexing lemma.  Under a `Fin m`
  formulation it would have needed `Fin 1 ≃ Unit` transport for both index and height.

  ═══ ⚠ HOW THIS DIFFERS FROM THE TEXTBOOK STATEMENT ═══

  This is a **uniform-parameter** variant, not verbatim Bombieri–Gubler 6.3.4.  There the
  conditions are `qⱼ^{dⱼ} ≥ q₁^{d₁}` and `q₁^{ε d₁} ≥ H(P)`, which let the exponent vary with
  `j`; here a single `E` serves every `j`, via `∀ j, B ≤ qⱼ^E` and `∀ j, E ≤ ε·dⱼ`.  That is a
  *stronger* hypothesis, so the statement below is *weaker* than the textbook one.  Anyone
  proving the general case should check whether the uniform form still suffices downstream
  before adopting it.

  Writing the statement out is also what caught the omission of `degreeOf j P ≤ d j` from an
  earlier draft — the degree bound is what makes `d` a degree vector rather than an arbitrary
  weight, and it is easy to forget because the `m = 1` proof does not use it.
-/
import QOU.Mathlib.RothBaseCase

namespace MvPolynomial

/-! ### One more piece of the one-variable dictionary -/

/-- `pUnitAlgEquiv` commutes with coefficient maps. -/
theorem pUnitAlgEquiv_map {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    (Q : MvPolynomial Unit R) :
    pUnitAlgEquiv S (map φ Q) = Polynomial.map φ (pUnitAlgEquiv R Q) := by
  induction Q using MvPolynomial.induction_on' with
  | monomial s r => simp
  | add p q hp hq => simp only [map_add, hp, hq, Polynomial.map_add]

/-- The shape `index_le_of_abs_leadingCoeff_le` expects, recovered from a plain
`MvPolynomial Unit ℤ`. -/
theorem symm_map_pUnitAlgEquiv (Q : MvPolynomial Unit ℤ) :
    (pUnitAlgEquiv ℚ).symm ((pUnitAlgEquiv ℤ Q).map (algebraMap ℤ ℚ))
      = map (algebraMap ℤ ℚ) Q := by
  rw [← pUnitAlgEquiv_map (algebraMap ℤ ℚ) Q]
  exact (pUnitAlgEquiv ℚ).symm_apply_apply _

/-! ### The statement -/

/-- The growth condition on the degree vector, read along a chosen ordering of the variables:
consecutive degrees drop by at least a factor `ω`. -/
def RothGrowth {σ : Type*} {m : ℕ} (o : σ ≃ Fin m) (ω : ℚ) (d : σ → ℕ) : Prop :=
  ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → ω * (d (o.symm k) : ℚ) ≤ (d (o.symm j) : ℚ)

/-! ### What the growth condition buys: the row cost

`RothGrowth` is the one parameter condition the arc carries, and until now nothing used it.
Here is what it is for.

The induction step splits off the **last** variable in the ordering and its row cost is

    t = (d_last + 1) / D₁,     D₁ a lower bound on the *other* variables' degrees.

`RothGrowth` makes the degrees decrease along the ordering, so every earlier degree is at
least `ω` times the last one, and `t ≤ 2/ω`.  Choosing `ω ≥ 2/ε` gives `t ≤ ε`.

**This was the arc's own reconstruction, and §11 has since confirmed it.**  Property `Γ_m`'s
first clause reads `max(s₂/s₁, …, s_M/s_{M−1}) ≤ t`, i.e. `s_h ≥ s_{h+1}/t` — which is
`RothGrowth o ω d` with `ω = 1/t`.  So the facts proved below are facts about the source's
condition, not only about this arc's definition of it, and the caveat this paragraph used to
carry is withdrawn.  (The reading is recorded under "the eleventh correction" below; §11 is
garbled in the PDF's OCR layer and had to be read from the page scans.) -/

/-- Under `RothGrowth` with `ω ≥ 1`, degrees are non-increasing along the ordering. -/
theorem rothGrowth_antitone {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {ω : ℚ} {d : σ → ℕ}
    (hω : 1 ≤ ω) (hg : RothGrowth o ω d) :
    ∀ (n : ℕ) (j k : Fin m), (k : ℕ) = (j : ℕ) + n →
      (d (o.symm k) : ℚ) ≤ (d (o.symm j) : ℚ) := by
  intro n
  induction n with
  | zero =>
      intro j k h
      have hjk : j = k := Fin.ext (by omega)
      rw [hjk]
  | succ p ih =>
      intro j k h
      have hklt := k.isLt
      have hlt : (j : ℕ) + 1 < m := by omega
      have h1 : ω * (d (o.symm ⟨(j : ℕ) + 1, hlt⟩) : ℚ) ≤ (d (o.symm j) : ℚ) :=
        hg j ⟨(j : ℕ) + 1, hlt⟩ rfl
      have h2 : (d (o.symm k) : ℚ) ≤ (d (o.symm ⟨(j : ℕ) + 1, hlt⟩) : ℚ) :=
        ih ⟨(j : ℕ) + 1, hlt⟩ k (by show (k : ℕ) = ((j : ℕ) + 1) + p; omega)
      nlinarith [Nat.cast_nonneg (α := ℚ) (d (o.symm ⟨(j : ℕ) + 1, hlt⟩))]

/-- **Every earlier degree is at least `ω` times any later one.**

The single-step condition plus antitonicity; this is the form the row cost needs, because the
degree floor `D₁` ranges over *all* the non-split variables, not just the adjacent one. -/
theorem rothGrowth_mul_le {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {ω : ℚ} {d : σ → ℕ}
    (hω : 1 ≤ ω) (hg : RothGrowth o ω d) {j k : Fin m} (hjk : (j : ℕ) + 1 ≤ (k : ℕ)) :
    ω * (d (o.symm k) : ℚ) ≤ (d (o.symm j) : ℚ) := by
  have hklt := k.isLt
  have hlt : (j : ℕ) + 1 < m := by omega
  have h1 : ω * (d (o.symm ⟨(j : ℕ) + 1, hlt⟩) : ℚ) ≤ (d (o.symm j) : ℚ) :=
    hg j ⟨(j : ℕ) + 1, hlt⟩ rfl
  have h2 : (d (o.symm k) : ℚ) ≤ (d (o.symm ⟨(j : ℕ) + 1, hlt⟩) : ℚ) :=
    rothGrowth_antitone hω hg ((k : ℕ) - ((j : ℕ) + 1)) ⟨(j : ℕ) + 1, hlt⟩ k
      (by show (k : ℕ) = ((j : ℕ) + 1) + ((k : ℕ) - ((j : ℕ) + 1)); omega)
  nlinarith [le_trans zero_le_one hω]

/-- **`t ≤ 2/ω`** — the row cost of the induction step, bounded by the growth constant alone.

`(d_last + 1)/d_earlier ≤ 2/ω`: the `+1` costs a factor `2` because `d_last ≥ 1`, and `ω` comes
straight from `rothGrowth_mul_le`.

So `ω ≥ 2/ε` forces `t ≤ ε`.  ⚠ The `t` here is the *row cost*, a local quantity; do not
confuse it with §11's parameter `t`, against which `ω = 1/t` — under that identification this
bound reads `row cost ≤ 2t`, which is the shape §13 consumes. -/
theorem rothGrowth_row_cost_le {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {ω : ℚ} {d : σ → ℕ}
    (hω : 1 ≤ ω) (hg : RothGrowth o ω d) {j k : Fin m} (hjk : (j : ℕ) + 1 ≤ (k : ℕ))
    (hdk : d (o.symm k) ≠ 0) :
    ((d (o.symm k) : ℚ) + 1) / (d (o.symm j) : ℚ) ≤ 2 / ω := by
  have hωpos : (0 : ℚ) < ω := lt_of_lt_of_le zero_lt_one hω
  have hdk1 : (1 : ℚ) ≤ (d (o.symm k) : ℚ) := by
    exact_mod_cast Nat.one_le_iff_ne_zero.mpr hdk
  have hmul := rothGrowth_mul_le hω hg hjk
  have hdj : (0 : ℚ) < (d (o.symm j) : ℚ) := by nlinarith
  rw [div_le_div_iff₀ hdj hωpos]
  nlinarith

/-- **Rescaling the degree vector preserves the growth condition.**

The induction step measures its sub-problems against `r · d` rather than `d` (the source's
`p_h = n·r_h`), so the growth condition has to survive that rescaling.  It does, and for the
obvious reason: the factor `r` appears on both sides. -/
theorem rothGrowth_scale {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {ω : ℚ} {d : σ → ℕ} {r : ℕ}
    (hr : r ≠ 0) (hg : RothGrowth o ω d) : RothGrowth o ω (fun j => r * d j) := by
  intro j k hjk
  have h := hg j k hjk
  have hrQ : (0 : ℚ) < (r : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hr
  show ω * ((r * d (o.symm k) : ℕ) : ℚ) ≤ ((r * d (o.symm j) : ℕ) : ℚ)
  push_cast
  nlinarith


/-! ### ⚠ The eleventh correction: `c_m = 2^{m+1} − 3`, and the conclusion is not linear in `t`

§11 and §14 have now been **read from the page scans** rather than from the PDF's OCR layer,
which garbled exactly these two sections.  Three findings, two of them corrections.

**1. `RothGrowth` *is* the source's condition.**  Property `Γ_M`'s first clause is

    max(s₂/s₁, s₃/s₂, …, s_M/s_{M−1}) ≤ t,

i.e. `s_h ≥ (1/t)·s_{h+1}` — which is `RothGrowth o ω d` with **`ω = 1/t`**.  The arc
reconstructed that condition from what the row-cost bound needed, and the reconstruction was
right.  ⚠ Every "this is a fact about `RothGrowth` as this arc defines it, not established as
the source's" caveat in this arc can now be dropped.

**2. ⚠ `c_m = 2^{m+1} − 3`, not `2^m − 3`.**  §14 derives `c_m = 2c_{m−1} + 3` from `c₁ = 1`,
which closes to `2^{m+1} − 3` — see `rothConstant_rec` and `rothConstant_one` below, where the
recurrence and the closed form are checked against each other rather than asserted.  The value
this arc had been carrying was wrong; it was never asserted, which is the only reason that
cost nothing.

⚠ **It is the base case, not the recurrence, that pins the constant** — and getting that
backwards is how the wrong value survived.  `c_m = 2c_{m−1} + 3` has general solution
`A·2^m − 3`, so **both** `2^m − 3` and `2^{m+1} − 3` satisfy it (`two_pow_sub_three_rec`
below checks the first one does).  Only `c₁ = 1` selects `A = 2`, and the old value fails
exactly there: `2^1 − 3 = −1 ≠ 1` (`two_pow_sub_three_ne_one`).  A check against the
recurrence alone would have passed the wrong constant.

**3. ⚠ The conclusion is `Θ_m ≤ c_m · t^{2^{−(m−1)}}` — the exponent, not a linear factor.**
That is what iterating §13's *square-root* branch produces: each step halves the exponent, so
after `m − 1` steps `t` has become `t^{2^{−(m−1)}}`.  For small `t` this is **much larger**
than `t`.

⚠ **Consequence for `RothLemmaUniform` below.**  Its conclusion is `index ≤ m·ε`, linear in
the small parameter.  Mahler's is not, and no linear-in-`ε` invariant can absorb a square root
taken once per induction step — so the recursion could never have closed on this statement's
shape.  The module header already warned it was "false for small `ω` when `m ≥ 2`" on other
grounds; this says *what the right shape is*, which the warning did not.

Fixing that is the next piece of work and is deliberately **not** done in this commit: it
changes the statement every downstream theorem is aimed at, and is worth doing once, against
the read text, rather than twice. -/

/-- **Mahler's `c_m`, closed form.**  §14 gives the recurrence `c_m = 2c_{m−1} + 3` with
`c₁ = 1`; this is its solution. -/
def rothConstant (m : ℕ) : ℕ := 2 ^ (m + 1) - 3

/-- The base case `c₁ = 1`. -/
theorem rothConstant_one : rothConstant 1 = 1 := by decide

/-- **The recurrence the closed form must satisfy**, checked rather than asserted.

⚠ This is necessary but **not** sufficient to identify the constant: the recurrence's general
solution is `A·2^m − 3`, so the discarded value `2^m − 3` satisfies it too
(`two_pow_sub_three_rec`).  `rothConstant_one` is what does the separating. -/
theorem rothConstant_rec (m : ℕ) (hm : 1 ≤ m) :
    rothConstant (m + 1) = 2 * rothConstant m + 3 := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hm
  simp only [rothConstant]
  have h : 3 ≤ 2 ^ (1 + k + 1) := by
    calc (3 : ℕ) ≤ 2 ^ 2 := by norm_num
      _ ≤ 2 ^ (1 + k + 1) := Nat.pow_le_pow_right (by norm_num) (by omega)
  have hpow : 2 ^ (1 + k + 1 + 1) = 2 * 2 ^ (1 + k + 1) := by ring
  omega

/-- ⚠ **The discarded value satisfies the recurrence.**  Landed as the record of the eleventh
correction, so the wrong constant stays visible rather than being quietly replaced — and so
that the reason it survived stays visible with it.  Stated over `ℤ`: at `m = 0` the value
`2^0 − 3` is negative, and `ℕ` subtraction would truncate the counterexample away. -/
theorem two_pow_sub_three_rec (m : ℕ) : (2 : ℤ) ^ (m + 1) - 3 = 2 * ((2 : ℤ) ^ m - 3) + 3 := by
  ring

/-- ⚠ **… and fails the base case, which is what actually rules it out.**  §14's `c₁ = 1` is the
only part of the derivation that distinguishes `2^{m+1} − 3` from `2^m − 3`. -/
theorem two_pow_sub_three_ne_one : (2 : ℤ) ^ 1 - 3 ≠ 1 := by decide

/-- `c₂ = 5`, the first value where the two closed forms disagree. -/
theorem rothConstant_two : rothConstant 2 = 5 := by decide

/-- **The bound §14 actually proves**, written without roots.

Mahler's conclusion is `Θ_m ≤ c_m · t^{2^{−(m−1)}}`.  The index is `ℚ`-valued and that bound
is irrational in general, so `RothBound m t θ` states the equivalent inequality obtained by
raising both non-negative sides to the power `2^{m−1}`:

    0 ≤ θ    and    θ^{2^{m−1}} ≤ c_m^{2^{m−1}} · t.

Equivalent, not weaker: `index ≤ c_m·t^{2^{−(m−1)}}` holds iff some rational `θ` satisfies
`RothBound m t θ` and bounds the index, by density of `ℚ`.

The root-free form is also the shape the recursion is already in.  §13's branch is a *square
root*, so the arithmetic this arc proved for it — `sq_index_le_of_det_bound`,
`sq_mul_le_two_mul_of_sum_le` — is stated squared; raising §14's conclusion to a power is
what makes the two meet.

⚠ Only `1 ≤ m` is meaningful.  At `m = 0` the truncated `m − 1` and `rothConstant 0 = 0`
collapse this to `θ ≤ 0`. -/
def RothBound (m : ℕ) (t θ : ℚ) : Prop :=
  0 ≤ θ ∧ θ ^ (2 ^ (m - 1)) ≤ (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * t

/-- At one variable the bound is `θ ≤ t`, which is §14's base case `Θ₁ ≤ t`. -/
theorem rothBound_one (t θ : ℚ) : RothBound 1 t θ ↔ (0 ≤ θ ∧ θ ≤ t) := by
  simp [RothBound, rothConstant_one]

/-- At two variables the bound is `θ² ≤ 25t`, i.e. `θ ≤ 5√t`. -/
theorem rothBound_two (t θ : ℚ) : RothBound 2 t θ ↔ (0 ≤ θ ∧ θ ^ 2 ≤ 25 * t) := by
  norm_num [RothBound, rothConstant_two]

/-- Anything smaller than an admissible bound is admissible. -/
theorem RothBound.mono {m : ℕ} {t θ θ' : ℚ} (h : RothBound m t θ) (h0 : 0 ≤ θ')
    (hle : θ' ≤ θ) : RothBound m t θ' :=
  ⟨h0, le_trans (pow_le_pow_left₀ h0 hle _) h.2⟩

/-! ### ⚠ The root bound and the linear bound are not the same shape

At `m = 2` and `t = 1/100`, §14 admits `θ = 1/2`, while `m·t = 1/50` is twenty-five times
smaller.  So a conclusion `index ≤ m·ε` — the shape `RothLemmaUniform` carried until now — is
far **stronger** than what §14 proves, and no amount of work on the recursion was going to
reach it.  That is the eleventh correction's operative consequence, exhibited rather than
argued. -/

theorem rothBound_two_half : RothBound 2 (1 / 100 : ℚ) (1 / 2) := by
  rw [rothBound_two]; norm_num

theorem two_mul_lt_rothBound_two_witness : (2 : ℚ) * (1 / 100) < 1 / 2 := by norm_num

/-! ### The arithmetic of §14's induction step

All `ℚ`, nothing about polynomials — this is the half of the induction that `rothConstant_rec`
was only the shadow of, and it is where the constant `2c_{m−1} + 3` is actually produced.

Write `s = t^{2^{−(m−1)}}`, so §14's conclusion `Θ_m ≤ c_m·t^{2^{−(m−1)}}` reads `Θ_m ≤ c_m·s`.
`rothBound_pow_iff` says that is **exactly** `RothBound m (s^{2^{m−1}}) θ`, so the root-free
definition loses nothing: it is the source's inequality written in the variable the source's
own exponent produces, and the step can be done linearly in `s`. -/

/-- **`RothBound` at a perfect power is a linear bound.**

With `t = s^{2^{m−1}}` — the substitution `s = t^{2^{−(m−1)}}` read backwards — `RothBound m t θ`
says exactly `θ ≤ c_m·s`. -/
theorem rothBound_pow_iff {m : ℕ} {s θ : ℚ} (hs : 0 ≤ s) :
    RothBound m (s ^ (2 ^ (m - 1))) θ ↔ (0 ≤ θ ∧ θ ≤ (rothConstant m : ℚ) * s) := by
  have hn : (2 : ℕ) ^ (m - 1) ≠ 0 := (Nat.two_pow_pos _).ne'
  have hc : (0 : ℚ) ≤ (rothConstant m : ℚ) := Nat.cast_nonneg _
  have hcs : (0 : ℚ) ≤ (rothConstant m : ℚ) * s := mul_nonneg hc hs
  constructor
  · rintro ⟨h0, h⟩
    exact ⟨h0, le_of_pow_le_pow_left₀ hn hcs (by rw [mul_pow]; exact h)⟩
  · rintro ⟨h0, h⟩
    exact ⟨h0, by rw [← mul_pow]; exact pow_le_pow_left₀ h0 h _⟩

/-- **§14's induction step, root-free** — and where `c_m = 2c_{m−1} + 3` comes from.

The source's step is `Ψ_m = Θ_{m−1} + t`, then §13's recursive inequality
`Θ_m ≤ Ψ_m + 2·max(Ψ_m/n, √(Ψ_m/r_m))`.  Here `u` stands for that whole `2·max(…)` term, and
the only thing the step needs of it is `u² ≤ 4Ψ` — which both branches satisfy, since `n`,
`r_m ≥ 1` and `Ψ ≤ 1` make `max(Ψ/n, √(Ψ/r_m)) ≤ √Ψ`.  Carrying it as `u` with a squared
hypothesis keeps the whole step inside `ℚ`, which is also the shape `RothRecursionArith` is in.

The two contributions:

* `Ψ ≤ (c+1)s² ≤ (c+1)s`, using `s ≤ 1` — this is where `Θ_{m−1} ≤ c·s²` and `t ≤ s²` combine;
* `u ≤ (c+2)s`, because `((c+2)s)² − 4(c+1)s² = c²s² ≥ 0`.

Sum: `(2c+3)s`.  ⚠ Note the second bound is the *crude* one, `2√(c+1) ≤ c+2`, and it is
**exactly tight at `c = 0`**.  So §14's constant is not slack that a sharper argument could
shave; it is what this inequality gives.

⚠ **The hypotheses are stated, not derived** — this theorem is true whatever `Ψ` and `u` mean,
and the reading above is a reconstruction of which quantity §14's displays refer to.  It is
corroborated rather than read: §13's `t` is a *row cost* and §11's `t` is the parameter, and
`Ψ_m = Θ_{m−1} + t` closes to `2c+3` only if that `t` is the parameter.  Under the other
reading — row cost, bounded by `2t` via `rothGrowth_row_cost_le` — the same computation gives
`2c+4`, which is not §14's constant.  So the reading is forced by the answer, which is weaker
evidence than reading it and is worth saying.

⚠ **`0 ≤ u` is not a hypothesis**, though the quantity it stands for is non-negative.  The
squared bound alone gives `u ≤ (c+2)s`: a negative `u` clears a non-negative right-hand side
outright.  Dropped rather than carried, because this arc has twice found that a hypothesis
nobody has to discharge is indistinguishable from a false one (corrections 9 and 10) — the
linter flagging it unused is the same signal arriving cheaply. -/
theorem rothConstant_step {m : ℕ} (hm : 1 ≤ m) {s Ψ u θ : ℚ}
    (hs0 : 0 ≤ s) (hs1 : s ≤ 1)
    (hΨ : Ψ ≤ ((rothConstant m : ℚ) + 1) * s ^ 2)
    (hu : u ^ 2 ≤ 4 * Ψ)
    (hθ : θ ≤ Ψ + u) :
    θ ≤ (rothConstant (m + 1) : ℚ) * s := by
  have hc0 : (0 : ℚ) ≤ (rothConstant m : ℚ) := Nat.cast_nonneg _
  have hsq : s ^ 2 ≤ s := by nlinarith
  have hΨs : Ψ ≤ ((rothConstant m : ℚ) + 1) * s := by nlinarith
  have hus : u ≤ ((rothConstant m : ℚ) + 2) * s := by
    refine le_of_pow_le_pow_left₀ two_ne_zero (by nlinarith) ?_
    nlinarith [sq_nonneg ((rothConstant m : ℚ) * s)]
  have hrec : ((rothConstant (m + 1) : ℕ) : ℚ) = 2 * (rothConstant m : ℚ) + 3 := by
    rw [rothConstant_rec m hm]; push_cast; ring
  rw [hrec]
  linarith

/-- **The induction step in `RothBound` shape** — the obligation the recursion has to meet.

From the sub-problem's bound and §13's inequality, the assembled bound satisfies `RothBound` at
the next arity.  This is the statement an `m ≥ 2` proof has to reach; everything else in the
arc feeds `Ψ` and `u`. -/
theorem rothBound_step {m : ℕ} (hm : 1 ≤ m) {s Ψ u θ : ℚ}
    (hs0 : 0 ≤ s) (hs1 : s ≤ 1) (hθ0 : 0 ≤ θ)
    (hΨ : Ψ ≤ ((rothConstant m : ℚ) + 1) * s ^ 2)
    (hu : u ^ 2 ≤ 4 * Ψ)
    (hθ : θ ≤ Ψ + u) :
    RothBound (m + 1) (s ^ (2 ^ m)) θ := by
  have h := rothConstant_step hm hs0 hs1 hΨ hu hθ
  have hb : RothBound (m + 1) (s ^ (2 ^ ((m + 1) - 1))) θ :=
    (rothBound_pow_iff hs0).mpr ⟨hθ0, h⟩
  simpa using hb

/-- **Non-vacuity of the step.**  `m = 1`, `s = 1/4`, `Ψ = 1/8`, `u = 1/2`, `θ = 5/8`: every
hypothesis holds and the conclusion is a real bound.  ⚠ A finite witness tests vacuity, not
usefulness — this arc has said so before (correction 9) and it is still true here. -/
theorem rothBound_step_witness : RothBound 2 ((1 / 4 : ℚ) ^ (2 ^ 1)) (5 / 8) :=
  rothBound_step (m := 1) (s := 1 / 4) (Ψ := 1 / 8) (u := 1 / 2) (θ := 5 / 8)
    le_rfl (by norm_num) (by norm_num) (by norm_num)
    (by norm_num [rothConstant_one]) (by norm_num) (by norm_num)


/-- **Roth's lemma, uniform-parameter form** — the statement *schema*.

Read: an integer polynomial of degree at most `dⱼ` in `xⱼ`, of height at most `B`, cannot have
index larger than `θ` at a rational point `(pⱼ/qⱼ)` whose denominators are large compared
to `B`.

⚠ A `def`, not a theorem: only `m = 1` is proved (`rothLemmaUniform_one`).  ⚠ False for small
`ω` when `m ≥ 2`.  ⚠ A uniform-`E` variant of the textbook statement.  See the module header
for all three.

⚠ **The bound `θ` is a parameter, so this is a schema and not a claim.**  Taking `θ` large
makes it trivially true.  Roth's lemma is the instance in `RothLemmaMahler` below, where `ω`,
`ε` and `θ` are all tied to the single parameter `t` the source uses.  Quoting this `def` on
its own overstates what it says. -/
def RothLemmaUniform (σ : Type*) (m : ℕ) (ω ε θ : ℚ) : Prop :=
  ∀ (o : σ ≃ Fin m) (d : σ → ℕ) (pn qd : σ → ℤ) (P : MvPolynomial σ ℤ) (B : ℤ) (E : ℕ),
    (∀ j, d j ≠ 0) →
    RothGrowth o ω d →
    P ≠ 0 →
    (∀ j, degreeOf j P ≤ d j) →
    (∀ n, |coeff n P| ≤ B) →
    (∀ j, 2 ≤ qd j) →
    (∀ j, IsCoprime (pn j) (qd j)) →
    (∀ j, B ≤ qd j ^ E) →
    (∀ j, (E : ℚ) ≤ ε * (d j : ℚ)) →
    index d (fun j => ((pn j : ℚ) / (qd j : ℚ))) (map (algebraMap ℤ ℚ) P)
      ≤ ((θ : ℚ) : WithTop ℚ)

/-- **Roth's lemma as Mahler states it** (§14, Theorem 1), assembled from the schema.

The source carries one small parameter `t` and ties everything to it:

* property `Γ_m`'s first clause is `RothGrowth` with `ω = 1/t` (see `RothGrowth` above);
* its height clause `a ≤ H₁^{(1/m) r₁ t}` is, in uniform form, `ε = t/m`;
* §14's conclusion is `Θ_m ≤ c_m·t^{2^{−(m−1)}}`, i.e. `RothBound m t θ`.

The bound is existential because it must be *uniform* in all the data — one `θ` serving every
`o, d, p, q, P, B, E` — which is what the source proves and what the `∃` outside
`RothLemmaUniform`'s own `∀`s expresses.

⚠ Still a `def`.  Nothing in this repository proves it for `m ≥ 2`; `rothLemmaMahler_one` is
the only instance discharged.

⚠ `Γ_m` has two further clauses this does not carry — `s_h log K_h ≥ s₁ log K₁` and
`K₁ ≥ 2^{(1/t)(m−1)m(2m+1)}`.  They are hypotheses of the source's theorem, so omitting them
makes this **stronger** than what §14 proves, and any proof attempt for `m ≥ 2` will have to
add them back rather than discover it can do without. -/
def RothLemmaMahler (σ : Type*) (m : ℕ) (t : ℚ) : Prop :=
  ∃ θ : ℚ, RothBound m t θ ∧ RothLemmaUniform σ m t⁻¹ (t / (m : ℚ)) θ

/-- **The `m = 1` case of Roth's lemma**, as an instance of the statement above.

Holds for **every** `ω`, because the growth condition is vacuous when there is only one
variable — there is no consecutive pair.

⚠ The `degreeOf` hypothesis is not used: at one variable the height bound alone suffices.
That is why it was easy to omit from a draft of the statement, and why it is worth stating
that its absence there was an error rather than an economy.

Everything comes from `RothBaseCase.lean`; **no reindexing lemma appears**, which is the
evidence for the design choice argued in the module header. -/
theorem rothLemmaUniform_one (ω ε θ : ℚ) (hεθ : ε ≤ θ) : RothLemmaUniform Unit 1 ω ε θ := by
  classical
  rintro o d pn qd P B E hd - hP - hB hq hco hBq hE
  have hd0 : d () ≠ 0 := hd ()
  have hdQ : (0 : ℚ) < (d () : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hd0
  set P' : Polynomial ℤ := pUnitAlgEquiv ℤ P with hP'
  have hP'0 : P' ≠ 0 := fun h => hP ((pUnitAlgEquiv ℤ).injective (h.trans (map_zero _).symm))
  have hlead : |P'.leadingCoeff| ≤ qd () ^ E := by
    have hcoe : P'.leadingCoeff = coeff (Finsupp.single () P'.natDegree) P := by
      rw [Polynomial.leadingCoeff, hP', coeff_pUnitAlgEquiv]
    rw [hcoe]
    exact le_trans (hB _) (hBq ())
  have hmain := index_le_of_abs_leadingCoeff_le (p := pn ()) (q := qd ()) (hq ()) (hco ())
    hd0 hP'0 E hlead
  rw [hP', symm_map_pUnitAlgEquiv] at hmain
  have hdfun : d = fun _ : Unit => d () := by
    refine _root_.funext fun u => ?_; cases u; rfl
  have hafun : (fun j : Unit => ((pn j : ℚ) / (qd j : ℚ)))
      = fun _ : Unit => ((pn () : ℚ) / (qd () : ℚ)) := by
    refine _root_.funext fun u => ?_; cases u; rfl
  rw [hdfun, hafun]
  refine le_trans hmain ?_
  rw [WithTop.coe_le_coe]
  have h2 := mul_le_mul_of_nonneg_right (hE ()) (le_of_lt (inv_pos.mpr hdQ))
  rw [mul_assoc, mul_inv_cancel₀ hdQ.ne', mul_one] at h2
  rw [div_eq_mul_inv]
  exact le_trans h2 hεθ

/-- **§14's base case, `Θ₁ ≤ t = c₁t`**, discharged.

This is the one instance of `RothLemmaMahler` this repository proves.  At one variable the
growth condition is vacuous and `ε = t/1 = t`, so the schema's `m = 1` case supplies `θ = t`
directly — and `rothBound_one` says that is exactly what §14 asks for. -/
theorem rothLemmaMahler_one {t : ℚ} (ht : 0 ≤ t) : RothLemmaMahler Unit 1 t :=
  ⟨t, (rothBound_one t t).mpr ⟨ht, le_rfl⟩, rothLemmaUniform_one _ _ _ (by simp)⟩

/-! ### The hypotheses are jointly satisfiable

A universally quantified statement can be true because nothing satisfies its hypotheses.  This
exhibits data that does: one variable, `P = 1`, `d = 1`, `p/q = 1/2`, `B = 1`, `E = 0`, `ε = 1`.
Every hypothesis holds and the conclusion is a real bound (`index ≤ 1`), not `⊤`. -/
example :
    index (fun _ : Unit => 1) (fun _ : Unit => ((1 : ℤ) : ℚ) / ((2 : ℤ) : ℚ))
        (map (algebraMap ℤ ℚ) (1 : MvPolynomial Unit ℤ))
      ≤ ((1 : ℚ) : WithTop ℚ) := by
  refine rothLemmaUniform_one 0 1 1 le_rfl
    (⟨fun _ => 0, fun _ => (), fun _ => Subsingleton.elim _ _,
      fun _ => Subsingleton.elim _ _⟩ : Unit ≃ Fin 1)
    (fun _ => 1) (fun _ => 1) (fun _ => 2) 1 1 0 (fun _ => one_ne_zero) ?_ one_ne_zero ?_ ?_ ?_ ?_ ?_ ?_
  · intro j k hjk; omega
  · intro j
    have h : degreeOf j (1 : MvPolynomial Unit ℤ) = 0 := by
      rw [← C_1]; exact degreeOf_C _ _
    omega
  · intro n; rw [coeff_one]; split_ifs <;> simp
  · intro j; norm_num
  · intro j; exact isCoprime_one_left
  · intro j; norm_num
  · intro j; norm_num

/-! ### Next

⚠ **`m ≥ 2` is entirely open.**  What exists is the machinery the induction step consumes —
`RothInductionStep` for the separated factorisation, `WronskianHeight` / `WronskianIndex` for
the Wronskian's height and index, `BoundedOrderWronskian` for non-vanishing, and this module's
base case to terminate it.  What does not exist is the induction: the construction of the
separated representation and the recursion itself.

The choice of `ω(m, ε)` is no longer open — §11 pins `ω = 1/t` and `ε = t/m`, and
`RothLemmaMahler` records that.  What replaces it as the open parameter question is `Γ_m`'s
two omitted clauses, which the `m ≥ 2` proof will have to reinstate.

The step the recursion needs, in the new shape: from `RothBound (m−1) t θ'` for the two
sub-problems, derive `RothBound m t θ` for the assembled bound.  That is where
`rothConstant_rec` earns its place — it is the arithmetic half of exactly that step. -/

end MvPolynomial
