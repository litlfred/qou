/-
  **The statement of Roth's lemma**, written down so its hypotheses can be checked against
  named theorems — and the `m = 1` case proved.

  Bean `qou-4lbh`.

  ⚠⚠ `RothLemmaUniform` below is a **`def`, not a theorem.**  Nothing in this repository
  proves it for `m ≥ 2`.  It is a statement, written so that every hypothesis has to
  elaborate and so that the base case has something to be an instance *of*.  Do not cite it
  as though Roth's lemma were formalised.

  ⚠ It is also **not true for every `ω`.**  Property `Γ_m` is a genuine hypothesis of Roth's
  lemma: for `m ≥ 2` and small `ω` the statement is false.  At `m = 1` its growth clause is
  vacuous and the other two are implied by the standing `2 ≤ qⱼ`, which is why
  `rothLemmaUniform_one` holds for *every* `ω`.

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
  height condition is `q₁^{ε d₁} ≥ H(P)`, which lets the exponent vary with `j`; here a single
  `E` serves every `j`, via `∀ j, B ≤ qⱼ^E` and `∀ j, E ≤ ε·dⱼ`.  That is a *stronger*
  hypothesis, so the statement below is *weaker* than the textbook one.  Anyone proving the
  general case should check whether the uniform form still suffices downstream before adopting
  it.

  Bombieri–Gubler's other condition, `qⱼ^{dⱼ} ≥ q₁^{d₁}`, **is** carried: it is Mahler's `Γ_m`
  clause 2 with the logarithms cleared, and `RothGamma.height` is both.  Two independent
  sources agreeing on a clause is better evidence than either reading alone.

  Writing the statement out is also what caught the omission of `degreeOf j P ≤ d j` from an
  earlier draft — the degree bound is what makes `d` a degree vector rather than an arbitrary
  weight, and it is easy to forget because the `m = 1` proof does not use it.
-/
import QOU.Mathlib.RothBaseCase
import Mathlib.Data.Rat.Floor
import Mathlib.Data.Int.Interval

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

    t = d_last / D₁,     D₁ a lower bound on the *other* variables' degrees.

`RothGrowth` makes the degrees decrease along the ordering, so every earlier degree is at
least `ω` times the last one, and `t ≤ 1/ω`.  Choosing `ω ≥ 1/ε` gives `t ≤ ε`.

⚠ The numerator was `d_last + 1` until correction 24, which cost a factor `2` here and
nowhere in §13.  See `RothOperatorFamily.cost_sepW_le`.

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

/-- **`t ≤ 1/ω`** — the row cost of the induction step, bounded by the growth constant alone.

`d_last/d_earlier ≤ 1/ω`, straight from `rothGrowth_mul_le`.  So `ω ≥ 1/ε` forces `t ≤ ε`.

⚠ The `t` here is the *row cost*, a local quantity; do not confuse it with §11's parameter
`t`, against which `ω = 1/t` — under that identification this bound reads `row cost ≤ t`,
which is the shape §13 consumes, on the nose.

⚠ This used to be stated with numerator `d_last + 1` and conclusion `2/ω`, the `2` being
`1 + 1/d_last ≤ 2`.  Both are true, and the loose one is what the arc carried for eleven
commits; §13's row term is `(μ-1)/r_{m-1}` with `μ ≤ n ≤ r_m + 1`, so the numerator the
source uses is `r_m`, not `r_m + 1`.  Correction 24. -/
theorem rothGrowth_row_cost_le {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {ω : ℚ} {d : σ → ℕ}
    (hω : 1 ≤ ω) (hg : RothGrowth o ω d) {j k : Fin m} (hjk : (j : ℕ) + 1 ≤ (k : ℕ))
    (hdk : d (o.symm k) ≠ 0) :
    (d (o.symm k) : ℚ) / (d (o.symm j) : ℚ) ≤ 1 / ω := by
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


/-! ### `Θ_m` — the quantity Roth's lemma is actually about

⚠ Everything in this arc up to here bounds the index of **one** polynomial.  Roth's lemma is
about `Θ_m`, which §8 defines as the **least upper bound** of `J(A; r₁,…,r_m; κ₁,…,κ_m)` taken
over two sets:

* `R(a; r₁,…,r_m)` — non-zero integer polynomials of degree `≤ rₕ` in `xₕ` and height `≤ a`;
* `Q(H₁,…,H_m)` — systems of `m` rationals `κₕ = Pₕ/Qₕ` in lowest terms with
  `max(|Pₕ|,|Qₕ|) ≤ Hₕ`.

§9's content is that **both sets are finite**, so the lub is *attained*; that `Θ_m` is
non-decreasing in `a`; and that `0 ≤ Θ_m ≤ m`.

⚠ **This arc previously recorded §9 as "Siegel's lemma plus a counting argument, the biggest
unbuilt piece".  That is wrong** — Siegel's lemma is nowhere in §9.  What §9 needs is
finiteness of two explicitly bounded sets and attainment of a maximum over them, which is
elementary.  The mis-estimate came from reading a section *title* ("The upper bound `Θ_m(…)`")
and inferring its content.

`IsRothTheta` below characterises `Θ_m` rather than constructing it: the value is pinned
(`IsRothTheta.unique`), so anything satisfying the predicate is *the* `Θ_m`.

**Existence is proved** — `exists_isRothTheta`, from `finite_rothPolySet` and
`finite_rothFracSet` plus non-emptiness.  An earlier version of this paragraph called it an
undischarged obligation; it no longer is. -/

/-- `R(a; r₁,…,r_m)` — non-zero integer polynomials of degree `≤ rₕ` in `xₕ`, height `≤ a`. -/
def InRothPolySet {σ : Type*} (a : ℤ) (r : σ → ℕ) (A : MvPolynomial σ ℤ) : Prop :=
  A ≠ 0 ∧ (∀ h, degreeOf h A ≤ r h) ∧ ∀ n, |coeff n A| ≤ a

/-- `Q(H₁,…,H_m)` — systems of rationals **of height exactly** `Hₕ`.

⚠⚠ **Correction sixteen: this was `≤`, and that made `RothLemmaTheta` false.**  §9 says
"systems … **of heights** `Hₕ = max(|Pₕ|,|Qₕ|)`" — an equality.  With `≤` the set is larger,
so `Θ_m` is a supremum over more, and §10's bound fails outright: at `H = 100`, `a = 2`,
`r = 1`, the point `κ = 1/1` has height `1 ≤ 100` and `A = x − 1` has index `1`, against
`log a/(r log H) = log 2 / log 100 ≈ 0.15`.  With the equality, `κ` must have height `100`, so
`A` would need `|lead| ≥ 100 > a` and the index is `0`.

The failure mode is the arc's familiar one — a *weakened hypothesis* makes the statement
stronger, and a statement stronger than the source's is one the source will not prove.  Same
shape as `Γ_m`'s missing clauses, in a definition landed three turns ago.

⚠ Mahler also requires `(Pₕ, Qₕ) = 1`; Lean's `ℚ` is always in lowest terms, so that clause is
carried by the type rather than stated. -/
def InRothFracSet {σ : Type*} (H : σ → ℕ) (κ : σ → ℚ) : Prop :=
  ∀ h, max (κ h).num.natAbs (κ h).den = H h

/-- **`Θ_m` characterised** — the least upper bound of `J(A; r; κ)` over `R(a;r) × Q(H)`, and
attained.  §9's finiteness is what makes the second clause available. -/
def IsRothTheta {σ : Type*} (a : ℤ) (r H : σ → ℕ) (Θ : ℚ) : Prop :=
  (∀ A κ, InRothPolySet a r A → InRothFracSet H κ →
      index r κ (map (algebraMap ℤ ℚ) A) ≤ ((Θ : ℚ) : WithTop ℚ)) ∧
  (∃ A κ, InRothPolySet a r A ∧ InRothFracSet H κ ∧
      index r κ (map (algebraMap ℤ ℚ) A) = ((Θ : ℚ) : WithTop ℚ))

/-- **The characterisation pins the value.**  So `IsRothTheta` may be carried as a hypothesis
without ambiguity, and any later construction agrees with it. -/
theorem IsRothTheta.unique {σ : Type*} {a : ℤ} {r H : σ → ℕ} {Θ Θ' : ℚ}
    (h : IsRothTheta a r H Θ) (h' : IsRothTheta a r H Θ') : Θ = Θ' := by
  obtain ⟨hub, A, κ, hA, hκ, heq⟩ := h
  obtain ⟨hub', A', κ', hA', hκ', heq'⟩ := h'
  have h1 : ((Θ : ℚ) : WithTop ℚ) ≤ ((Θ' : ℚ) : WithTop ℚ) := heq ▸ hub' A κ hA hκ
  have h2 : ((Θ' : ℚ) : WithTop ℚ) ≤ ((Θ : ℚ) : WithTop ℚ) := heq' ▸ hub A' κ' hA' hκ'
  exact le_antisymm (by exact_mod_cast h1) (by exact_mod_cast h2)

/-- **`0 ≤ Θ_m`** — the index is a sum of non-negative terms, and `Θ_m` is attained. -/
theorem IsRothTheta.nonneg {σ : Type*} {a : ℤ} {r H : σ → ℕ} {Θ : ℚ}
    (h : IsRothTheta a r H Θ) :
    0 ≤ Θ := by
  obtain ⟨-, A, κ, -, -, heq⟩ := h
  have hle : ((0 : ℚ) : WithTop ℚ) ≤ index r κ (map (algebraMap ℤ ℚ) A) := by
    refine Finset.le_inf fun i _ => ?_
    exact_mod_cast idxWeight_nonneg r i
  rw [heq] at hle
  exact_mod_cast hle

/-- ⚠ **`IsRothTheta` is satisfiable as stated** — a degenerate but genuine instance.

At `r ≡ 0` every `idxWeight` term is `(i j)/0 = 0`, so `idxWeight` vanishes identically and the
index of *any* non-zero polynomial is `0`.  Both clauses then hold with `Θ = 0`, attained at
`A = 1`, `κ ≡ 0`.

⚠ **Superseded by `exists_isRothTheta`**, which gives inhabitation at every admissible
parameter.  Kept because it is what was available before that: a cheap check that the
two-clause `∀`/`∃` definition is not self-contradictory.  This arc has landed such a definition
before — correction 10's `hres` was unsatisfiable and looked fine — and at the time this was
the only evidence there was. -/
theorem isRothTheta_degenerate {σ : Type*} :
    IsRothTheta (1 : ℤ) (fun _ : σ => 0) (fun _ : σ => 1) 0 := by
  have hidx : ∀ (κ : σ → ℚ) (P : MvPolynomial σ ℚ), P ≠ 0 →
      index (fun _ : σ => 0) κ P = ((0 : ℚ) : WithTop ℚ) := by
    intro κ P hP
    have hne : (translate κ P).support.Nonempty :=
      support_nonempty.mpr ((translate_eq_zero_iff κ).not.mpr hP)
    have hw : ∀ i : σ →₀ ℕ, idxWeight (fun _ : σ => 0) i = 0 := by
      intro i; unfold idxWeight; simp
    unfold index
    rw [show (fun i => ((idxWeight (fun _ : σ => 0) i : ℚ) : WithTop ℚ))
        = (fun _ : σ →₀ ℕ => ((0 : ℚ) : WithTop ℚ)) from funext fun i => by rw [hw i]]
    exact Finset.inf_const hne _
  classical
  have hmap : ∀ B : MvPolynomial σ ℤ, B ≠ 0 → map (algebraMap ℤ ℚ) B ≠ 0 := by
    intro B hB h
    exact hB (map_injective (algebraMap ℤ ℚ) (algebraMap ℤ ℚ).injective_int
      (by rw [map_zero]; exact h))
  have hdeg1 : ∀ h : σ, degreeOf h (1 : MvPolynomial σ ℤ) = 0 := by
    intro h; rw [← C_1]; exact degreeOf_C _ _
  constructor
  · intro A κ hA hκ
    rw [hidx κ _ (hmap A hA.1)]
  · refine ⟨1, fun _ => 0, ⟨one_ne_zero, fun h => ?_, fun n => ?_⟩, fun h => ?_,
      hidx _ _ (hmap 1 one_ne_zero)⟩
    · rw [hdeg1 h]
    · rw [coeff_one]; split_ifs <;> norm_num
    · norm_num

/-! ### §9's finiteness, and the existence of `Θ_m`

Both `R(a;r)` and `Q(H)` are finite, so the least upper bound defining `Θ_m` is attained and
`IsRothTheta` is inhabited.  That discharges the obligation the section above left open.

⚠ Neither half has a ready-made Mathlib lemma.  For the polynomial side the closest thing is
`MvPolynomial.finite_setOf_bounded` in `Mathlib/RingTheory/MvPolynomial/Basic.lean`, which is
**private** and carries a uniform degree bound rather than a per-variable one.  For the rational
side there is nothing at all: `Finsupp.fintype` needs a finite codomain and `ℚ` is not one, so
the finiteness has to come from the height bound via `Rat.ext`. -/

/-- **The exponent box is finite.**  Over a finite variable type, the monomials whose exponent
in each variable `j` is at most `r j` form a finite set.

⚠ `Finite σ` is essential as soon as some `r j ≠ 0`: over an infinite `σ` the box for `r ≡ 1`
contains every squarefree monomial, of which there are infinitely many. -/
theorem finite_setOf_forall_le {σ : Type*} [Finite σ] (r : σ → ℕ) :
    {i : σ →₀ ℕ | ∀ j, i j ≤ r j}.Finite :=
  (Set.Finite.pi' fun j => Set.finite_Iic (r j)).preimage DFunLike.coe_injective.injOn

/-- **Bounded degree plus bounded height is a finite set of polynomials.**

⚠ Stated *without* `A ≠ 0`, which is the honest form: nothing in the argument uses it.  ⚠ And
with no sign hypothesis on `a`: for `a < 0` the height clause is unsatisfiable and the set is
empty, which is finite for a reason the proof never has to distinguish. -/
theorem finite_setOf_degreeOf_le_coeff_le {σ : Type*} [Finite σ] (a : ℤ) (r : σ → ℕ) :
    {A : MvPolynomial σ ℤ | (∀ h, degreeOf h A ≤ r h) ∧ ∀ n, |coeff n A| ≤ a}.Finite := by
  classical
  set E : Set (σ →₀ ℕ) := {i : σ →₀ ℕ | ∀ j, i j ≤ r j} with hEdef
  haveI : Finite ↥E := (finite_setOf_forall_le r).to_subtype
  have hsupp : ∀ A : MvPolynomial σ ℤ, (∀ h, degreeOf h A ≤ r h) →
      ∀ i, i ∉ E → coeff i A = 0 := by
    intro A hA i hi
    by_contra hc
    exact hi fun j => le_trans (monomial_le_degreeOf j (mem_support_iff.mpr hc)) (hA j)
  refine Set.Finite.of_injOn
    (f := fun A : MvPolynomial σ ℤ => fun i : ↥E => (coeff (i : σ →₀ ℕ) A + a).toNat)
    (t := {g : ↥E → ℕ | ∀ i, g i ∈ Set.Iic (2 * a).toNat}) ?_ ?_
    (Set.Finite.pi' fun _ => Set.finite_Iic (2 * a).toNat)
  · intro A hA i
    have h := abs_le.mp (hA.2 (i : σ →₀ ℕ))
    simp only [Set.mem_Iic]
    omega
  · intro A hA A' hA' h
    ext n
    by_cases hn : n ∈ E
    · have h1 := abs_le.mp (hA.2 n)
      have h2 := abs_le.mp (hA'.2 n)
      have hcoe := congrFun h ⟨n, hn⟩
      simp only at hcoe
      omega
    · rw [hsupp A hA.1 n hn, hsupp A' hA'.1 n hn]

/-- **`R(a; r)` is finite.** -/
theorem finite_rothPolySet {σ : Type*} [Finite σ] (a : ℤ) (r : σ → ℕ) :
    {A : MvPolynomial σ ℤ | InRothPolySet a r A}.Finite :=
  (finite_setOf_degreeOf_le_coeff_le a r).subset fun _ hA => ⟨hA.2.1, hA.2.2⟩

/-- **Rationals of bounded height form a finite set.**

A rational is determined by `(num, den)` (`Rat.ext`), and the bound confines that pair to
`Icc (-n) n ×ˢ Iic n`.  ⚠ The finiteness comes entirely from the height bound, not from the
type. -/
theorem finite_setOf_rat_height_le (n : ℕ) :
    {q : ℚ | q.num.natAbs ≤ n ∧ q.den ≤ n}.Finite := by
  have hinj : Set.InjOn (fun q : ℚ => (q.num, q.den))
      {q : ℚ | q.num.natAbs ≤ n ∧ q.den ≤ n} := by
    intro p _ q _ h
    exact Rat.ext (congrArg Prod.fst h) (congrArg Prod.snd h)
  refine Set.Finite.of_finite_image ?_ hinj
  refine Set.Finite.subset
    (Set.Finite.prod (Set.finite_Icc (-(n : ℤ)) (n : ℤ)) (Set.finite_Iic n)) ?_
  rintro y ⟨q, ⟨hq1, hq2⟩, rfl⟩
  simp only [Set.mem_prod, Set.mem_Icc, Set.mem_Iic]
  exact ⟨⟨by omega, by omega⟩, hq2⟩

/-- **`Q(H₁,…,H_m)` is finite** — it is exactly the `Set.pi` of the bounded-height sets. -/
theorem finite_rothFracSet {σ : Type*} [Finite σ] (H : σ → ℕ) :
    {κ : σ → ℚ | InRothFracSet H κ}.Finite := by
  refine Set.Finite.subset
    (Set.Finite.pi fun h : σ => finite_setOf_rat_height_le (H h)) ?_
  intro κ hκ h _
  have := hκ h
  constructor
  · exact le_trans (le_max_left _ _) (le_of_eq this)
  · exact le_trans (le_max_right _ _) (le_of_eq this)

/-- `R(a; r)` is non-empty as soon as `1 ≤ a`: the constant polynomial `1` works.

⚠ `1 ≤ a` is not merely convenient, it is **necessary** — a non-zero `A` has a non-zero
coefficient, so `1 ≤ |coeff n A| ≤ a`. -/
theorem exists_inRothPolySet {σ : Type*} (a : ℤ) (r : σ → ℕ) (ha : 1 ≤ a) :
    ∃ A : MvPolynomial σ ℤ, InRothPolySet a r A := by
  classical
  refine ⟨1, one_ne_zero, fun h => ?_, fun n => ?_⟩
  · rw [← C_1, degreeOf_C]
    exact Nat.zero_le _
  · rw [coeff_one]
    split_ifs
    · simpa using ha
    · simpa using le_trans zero_le_one ha

/-- `Q(H)` is non-empty as soon as every `H h` is at least `1`: take `κ h = Hₕ`, an integer,
whose numerator is `Hₕ` and whose denominator is `1`.

⚠ `1 ≤ Hₕ` is necessary — every rational has `den ≥ 1`, so its height is at least `1`.
⚠ With correction sixteen the witness can no longer be `κ ≡ 0`: that has height `1`, which is
the required height only when `Hₕ = 1`. -/
theorem exists_inRothFracSet {σ : Type*} (H : σ → ℕ) (hH : ∀ h, 1 ≤ H h) :
    ∃ κ : σ → ℚ, InRothFracSet H κ := by
  refine ⟨fun h => ((H h : ℤ) : ℚ), fun h => ?_⟩
  have hn : (((H h : ℤ) : ℚ)).num = (H h : ℤ) := by simp
  have hd : (((H h : ℤ) : ℚ)).den = 1 := by simp
  rw [hn, hd, Int.natAbs_natCast]
  exact max_eq_left (hH h)

/-- **`Θ_m` exists** once both sets are finite and non-empty.

The index of any `A ∈ R(a;r)` at any `κ` is a genuine rational rather than `⊤`: `index = ⊤`
happens only for the zero polynomial, and `A ≠ 0` survives `map (algebraMap ℤ ℚ)`.  So the
index is a `WithTop ℚ`-valued function on a finite non-empty product, which attains a maximum;
untopping it gives a rational satisfying both clauses — the upper bound from maximality, the
attainment from the maximiser.

⚠ No `Fintype σ` and no positivity on `r`: `index ≠ ⊤` follows from `A ≠ 0` alone through
`index_eq_top_iff`, so the route via `index_le_card` (which needs both) is not required. -/
theorem exists_isRothTheta_of_finite {σ : Type*} (a : ℤ) (r H : σ → ℕ)
    (hfinA : {A : MvPolynomial σ ℤ | InRothPolySet a r A}.Finite)
    (hfinK : {κ : σ → ℚ | InRothFracSet H κ}.Finite)
    (hneA : {A : MvPolynomial σ ℤ | InRothPolySet a r A}.Nonempty)
    (hneK : {κ : σ → ℚ | InRothFracSet H κ}.Nonempty) :
    ∃ Θ : ℚ, IsRothTheta a r H Θ := by
  classical
  obtain ⟨p, hps, hmax⟩ :=
    Set.exists_max_image _ (fun p : MvPolynomial σ ℤ × (σ → ℚ) =>
      index r p.2 (map (algebraMap ℤ ℚ) p.1)) (hfinA.prod hfinK) (hneA.prod hneK)
  have hne_top : ∀ (A : MvPolynomial σ ℤ) (κ : σ → ℚ), A ≠ 0 →
      index r κ (map (algebraMap ℤ ℚ) A) ≠ ⊤ := by
    intro A κ hA h
    refine hA (map_injective (algebraMap ℤ ℚ) (algebraMap ℤ ℚ).injective_int ?_)
    rw [map_zero]
    exact (translate_eq_zero_iff κ).mp ((index_eq_top_iff r κ).mp h)
  obtain ⟨hpA, hpK⟩ := hps
  have htop : index r p.2 (map (algebraMap ℤ ℚ) p.1) ≠ ⊤ := hne_top _ _ hpA.1
  refine ⟨(index r p.2 (map (algebraMap ℤ ℚ) p.1)).untop htop, ?_, ?_⟩
  · intro A κ hA hκ
    rw [WithTop.coe_untop]
    exact hmax (A, κ) ⟨hA, hκ⟩
  · exact ⟨p.1, p.2, hpA, hpK, (WithTop.coe_untop _ htop).symm⟩

/-- **§9's existence obligation, discharged.**

⚠ The hypotheses are only `1 ≤ a` and `1 ≤ Hₕ`, and both are **necessary** rather than
convenient: `a ≤ 0` empties `R(a;r)` and `Hₕ = 0` empties `Q(H)`, and an empty set has no
maximum to attain.  Nothing about finiteness is assumed — it is proved.

This is what the section above said was "an undischarged obligation … known satisfiable
because the two sets are finite".  It is now discharged, so `IsRothTheta` is a characterisation
of something that exists, and `IsRothTheta.unique` makes it *the* `Θ_m`. -/
theorem exists_isRothTheta {σ : Type*} [Finite σ] (a : ℤ) (r H : σ → ℕ)
    (ha : 1 ≤ a) (hH : ∀ h, 1 ≤ H h) :
    ∃ Θ : ℚ, IsRothTheta a r H Θ :=
  exists_isRothTheta_of_finite a r H (finite_rothPolySet a r) (finite_rothFracSet H)
    (exists_inRothPolySet a r ha) (exists_inRothFracSet H hH)

/-! ### Transport along a type equivalence

The variable *type* is incidental — `RothLemmaTheta σ m` and `RothLemmaTheta τ m` say the same
thing when `σ ≃ τ` — but they are different propositions, and `rothLemmaTheta_iterate` needs the
base case at `Fin 1` while `rothLemmaTheta_one` proves it at `Unit`.

`index_rename_equiv` (`QOU.Mathlib.RothIndex`) already carries the index across; these carry the
two membership predicates, and hence `IsRothTheta`.  ⚠ The height side really is free, as that
module's docstring predicted: `coeff_rename_mapDomain` matches coefficients across a renaming, so
the sup-norm bound transports with no arithmetic at all. -/

theorem InRothPolySet.rename_equiv {σ τ : Type*} [DecidableEq σ] [DecidableEq τ] (e : σ ≃ τ)
    {a : ℤ} {r : σ → ℕ} {A : MvPolynomial σ ℤ} (h : InRothPolySet a r A) :
    InRothPolySet a (r ∘ e.symm) (rename e A) := by
  obtain ⟨h0, hd, hc⟩ := h
  refine ⟨fun hz => h0 (rename_injective _ e.injective (by rw [hz, map_zero])), ?_, ?_⟩
  · intro k
    have hk := degreeOf_rename_of_injective (p := A) (f := (e : σ → τ)) e.injective (e.symm k)
    rw [Equiv.apply_symm_apply] at hk
    rw [hk]
    exact hd _
  · intro n
    have hn : Finsupp.mapDomain (e : σ → τ) (Finsupp.mapDomain (e.symm : τ → σ) n) = n := by
      rw [← Finsupp.mapDomain_comp]
      simp
    rw [← hn, coeff_rename_mapDomain _ e.injective]
    exact hc _

theorem InRothFracSet.rename_equiv {σ τ : Type*} (e : σ ≃ τ)
    {H : σ → ℕ} {κ : σ → ℚ} (h : InRothFracSet H κ) :
    InRothFracSet (H ∘ e.symm) (κ ∘ e.symm) := fun k => h (e.symm k)

/-- **`IsRothTheta` transports along a type equivalence.**  The value `Θ` is unchanged — it is a
supremum over sets the equivalence matches up. -/
theorem IsRothTheta.rename_equiv {σ τ : Type*} [DecidableEq σ] [DecidableEq τ] (e : σ ≃ τ)
    {a : ℤ} {r H : σ → ℕ} {Θ : ℚ} (h : IsRothTheta a r H Θ) :
    IsRothTheta a (r ∘ e.symm) (H ∘ e.symm) Θ := by
  classical
  obtain ⟨hub, A₀, κ₀, hA₀, hκ₀, heq⟩ := h
  have hcomp : ∀ {α : Type} (f : σ → α), (f ∘ (e.symm : τ → σ)) ∘ (e : σ → τ) = f := by
    intro α f; funext j; simp
  constructor
  · intro A κ hA hκ
    have hA' : InRothPolySet a r (rename (e.symm : τ → σ) A) := by
      have hx := hA.rename_equiv e.symm
      rwa [Equiv.symm_symm, hcomp r] at hx
    have hκ' : InRothFracSet H (κ ∘ (e : σ → τ)) := by
      have hx := hκ.rename_equiv e.symm
      rwa [Equiv.symm_symm, hcomp H] at hx
    have hb := hub _ _ hA' hκ'
    have hmr : rename (e.symm : τ → σ) (map (algebraMap ℤ ℚ) A)
        = map (algebraMap ℤ ℚ) (rename (e.symm : τ → σ) A) := (map_rename _ _ _).symm
    rw [index_rename_equiv e, hcomp r, hmr]
    exact hb
  · refine ⟨rename e A₀, κ₀ ∘ (e.symm : τ → σ), hA₀.rename_equiv e, hκ₀.rename_equiv e, ?_⟩
    have hmr : rename (e.symm : τ → σ) (map (algebraMap ℤ ℚ) (rename (e : σ → τ) A₀))
        = map (algebraMap ℤ ℚ) A₀ := by
      rw [← map_rename, rename_rename, Equiv.symm_comp_self, rename_id_apply]
    rw [index_rename_equiv e, hcomp r, hcomp κ₀, hmr]
    exact heq

/-! ### §10 — the base case in `Θ` form

`index_le_of_abs_coeff_le` bounds the index of **one** polynomial at **one** point.  `Θ₁` is a
supremum over `R(a;r) × Q(H)`, and §9's *attainment* clause is exactly what turns the one into
the other: the supremum is realised at some pair, so a bound holding at every pair holds at the
realising one, and therefore at `Θ₁`.

⚠ Attainment is doing real work here, not bookkeeping.  A supremum that is merely a least upper
bound would need the pointwise bound *plus* a limiting argument; because `R(a;r)` and `Q(H)` are
finite (`finite_rothPolySet`, `finite_rothFracSet`), it is a maximum and one instantiation
suffices.  That is why §9 had to come before §10.

⚠ **`InRothPolySet`'s degree clause is not used.**  §10's estimate consumes only the height
bound `|coeff n A| ≤ a`; the degrees `r` enter through `idxWeight` as *weights*, not as a
constraint on `A`.  Worth recording because it is the one place in this arc where a clause of
the ambient definition turns out to be genuinely inert — everywhere else, a hypothesis that
looked droppable was load-bearing. -/

section BaseCaseTheta

open Polynomial

/-- **`IsRothTheta`'s realising pair, transported to `ℤ[X]`.**

Everything §10 needs about the maximising `(A, κ)`, in the one-variable dictionary: a
polynomial, a point in lowest terms, the height identity `max(|p|,|q|) = H`, the coefficient
bound, and the index *equal* to `Θ`.

Coprimality and `0 < q` are not hypotheses anywhere — Lean's `ℚ` carries `reduced` and a
positive denominator by construction, which is why `InRothFracSet` needs no coprimality clause
even though §9 states one.

Extracted so that the unpowered and powered `Θ` bounds share it; they differ only in which
index theorem they call. -/
theorem exists_polynomial_of_isRothTheta {a : ℤ} {r H : Unit → ℕ} {Θ : ℚ}
    (hΘ : IsRothTheta a r H Θ) :
    ∃ (P : ℤ[X]) (p q : ℤ), P ≠ 0 ∧ 0 < q ∧ IsCoprime p q ∧
      max |p| |q| = ((H () : ℤ)) ∧ (∀ n, |P.coeff n| ≤ a) ∧
      index (fun _ : Unit => r ()) (fun _ : Unit => ((p : ℚ) / (q : ℚ)))
          (((pUnitAlgEquiv ℚ).symm (P.map (algebraMap ℤ ℚ))) : MvPolynomial Unit ℚ)
        = ((Θ : ℚ) : WithTop ℚ) := by
  obtain ⟨-, A, κ, hA, hκ, heq⟩ := hΘ
  obtain ⟨hA0, -, hAc⟩ := hA
  refine ⟨pUnitAlgEquiv ℤ A, (κ ()).num, (((κ ()).den : ℤ)), ?_, ?_, ?_, ?_, ?_, ?_⟩
  · exact fun h => hA0 ((pUnitAlgEquiv ℤ).injective (h.trans (map_zero _).symm))
  · exact_mod_cast (κ ()).pos
  · rw [Int.isCoprime_iff_gcd_eq_one]
    simpa [Int.gcd] using (κ ()).reduced
  · rw [Int.abs_eq_natAbs, Int.abs_eq_natAbs, Int.natAbs_natCast, ← Nat.cast_max, hκ ()]
  · intro n
    rw [coeff_pUnitAlgEquiv]
    exact hAc _
  · have hmap := symm_map_pUnitAlgEquiv A
    have hκeq : (fun _ : Unit => (((κ ()).num : ℚ) / ((((κ ()).den : ℤ)) : ℚ))) = κ := by
      funext u
      cases u
      push_cast
      exact Rat.num_div_den _
    have hreq : (fun _ : Unit => r ()) = r := by
      funext u
      cases u
      rfl
    rw [hmap, hκeq, hreq]
    exact heq

/-- **§10 in `Θ` form: `a ≤ H^e` and `H ≥ 2` give `Θ₁ ≤ e/r`.**

Mahler states this as `Θ₁(a; r; H) ≤ log a / (r log H)`; `e` is a root-free stand-in for
`log a / log H`, kept exponential because the recursion amplifies any rounding
(`two_sqrt_expands`).

⚠ `2 ≤ H` is necessary, not cosmetic: at `H = 1` the right-hand side of Mahler's form is
infinite and the estimate is empty. -/
theorem isRothTheta_le_of_pow_le {a : ℤ} {r H : Unit → ℕ} {Θ : ℚ}
    (hΘ : IsRothTheta a r H Θ) (hr : r () ≠ 0) (hH : 2 ≤ H ()) (e : ℕ)
    (hae : a ≤ (H () : ℤ) ^ e) :
    Θ ≤ (e : ℚ) / (r () : ℚ) := by
  obtain ⟨P, p, q, hPne, hq0, hco, hheight, hPc, hidx⟩ := exists_polynomial_of_isRothTheta hΘ
  have hbound := index_le_of_abs_coeff_le hq0 hco hr hPne e (a := a)
    (by rw [hheight]; exact_mod_cast hH) hPc (by rw [hheight]; exact hae)
  rw [hidx] at hbound
  exact_mod_cast hbound

/-- **§10 in `Θ` form, powered: `a^Q ≤ H^S` gives `Θ₁ ≤ S/(Q·r)`.**

The shape `Γ₁` delivers.  §11's clause (i) is `b ≤ K₁^{s₁t}` for rational `t = p/q`; clearing
the exponent gives `b^q ≤ K₁^{s₁p}` with no rounding anywhere. -/
theorem isRothTheta_le_of_pow_pow_le {a : ℤ} {r H : Unit → ℕ} {Θ : ℚ} {Qe S : ℕ}
    (hΘ : IsRothTheta a r H Θ) (hr : r () ≠ 0) (hQe : Qe ≠ 0) (hH : 2 ≤ H ())
    (hae : a ^ Qe ≤ (H () : ℤ) ^ S) :
    Θ ≤ (S : ℚ) / ((Qe : ℚ) * (r () : ℚ)) := by
  obtain ⟨P, p, q, hPne, hq0, hco, hheight, hPc, hidx⟩ := exists_polynomial_of_isRothTheta hΘ
  have hbound := index_le_of_pow_abs_coeff_le hq0 hco hr hPne hQe (a := a)
    (by rw [hheight]; exact_mod_cast hH) hPc (by rw [hheight]; exact hae)
  rw [hidx] at hbound
  exact_mod_cast hbound

/-- **`Γ₁` closes the base case: `Θ₁ ≤ t`.**

§11's clause (i) is `M = 1, K₁ ≥ 2, b ≤ K₁^{s₁t}`.  With correction eighteen's reading
(`K₁ = H₁`, `b = a`, `s₁ = r₁`) and `t = p/q`, that is `a^q ≤ H^{r·p}`, and §10 turns it into
`Θ₁ ≤ t` exactly.

⚠ **This is where §10's `P^j` half is load-bearing.**  The `Q^j` half alone gives
`Θ₁ ≤ log a/(r log q)`, and clause (i) then only bounds that by `t·log H/log q ≥ t` — the wrong
side of `t`, by exactly the factor the two halves differ in.  The arc carried the `q`-form for
a long time and could not close the base case; the reason was this factor, not any missing
recursion. -/
theorem isRothTheta_le_of_gamma_one {a : ℤ} {r H : Unit → ℕ} {Θ : ℚ} {p q : ℕ}
    (hΘ : IsRothTheta a r H Θ) (hr : r () ≠ 0) (hq : q ≠ 0) (hH : 2 ≤ H ())
    (hclause : a ^ q ≤ (H () : ℤ) ^ (r () * p)) :
    Θ ≤ (p : ℚ) / (q : ℚ) := by
  have h := isRothTheta_le_of_pow_pow_le hΘ hr hq hH hclause
  have hrQ : ((r () : ℚ)) ≠ 0 := Nat.cast_ne_zero.mpr hr
  have hqQ : ((q : ℚ)) ≠ 0 := Nat.cast_ne_zero.mpr hq
  have heq : (((r () * p : ℕ) : ℚ)) / ((q : ℚ) * ((r () : ℚ))) = (p : ℚ) / (q : ℚ) := by
    push_cast
    field_simp
  rwa [heq] at h

/-- **Validation — the hypotheses are jointly satisfiable, and non-degenerately.**

`isRothTheta_degenerate` satisfies `IsRothTheta` with `r ≡ 0` and `H ≡ 1`, which fails *both*
of this theorem's side conditions, so satisfiability of `IsRothTheta` alone would not rule out
vacuity.  `exists_isRothTheta` supplies an instance at `a = 2`, `r = 1`, `H = 2`, where both
hold, and the theorem then gives `Θ₁ ≤ 1`.

⚠ **Not proved here:** the value is in fact *exactly* `1`, so the bound is attained rather than
slack — `A = 2x − 1` lies in `R(2; 1)`, `κ = 1/2` lies in `Q(2)`, and `translate (1/2) A = 2x`
has index `1`.  That witness is a computation in `MvPolynomial`'s support, and it is recorded
rather than formalised.  Stated as a remark precisely so it is not read later as a theorem. -/
example : ∃ Θ : ℚ, IsRothTheta (2 : ℤ) (fun _ : Unit => 1) (fun _ : Unit => 2) Θ ∧ Θ ≤ 1 := by
  obtain ⟨Θ, hΘ⟩ := exists_isRothTheta (2 : ℤ) (fun _ : Unit => 1) (fun _ : Unit => 2)
    (by norm_num) (fun _ => by norm_num)
  refine ⟨Θ, hΘ, ?_⟩
  simpa using isRothTheta_le_of_pow_le hΘ one_ne_zero (by norm_num) 1 (by norm_num)

end BaseCaseTheta

/-- `R(a; r)` only grows with `a`. -/
theorem InRothPolySet.mono {σ : Type*} {a a' : ℤ} {r : σ → ℕ} {A : MvPolynomial σ ℤ}
    (haa : a ≤ a') (h : InRothPolySet a r A) : InRothPolySet a' r A :=
  ⟨h.1, h.2.1, fun n => le_trans (h.2.2 n) haa⟩

/-- **`Θ_m` is non-decreasing in `a`** — §9's second property.

`Θ_m` is *attained* at some `A ∈ R(a;r)`, and `R(a;r) ⊆ R(a';r)`, so the larger problem's upper
bound applies to that very `A`.  ⚠ Attainment is doing the work: without it one would have to
compare two suprema, and the inclusion alone would not suffice to transfer a witness. -/
theorem IsRothTheta.mono_height {σ : Type*} {a a' : ℤ} {r H : σ → ℕ} {Θ Θ' : ℚ}
    (haa : a ≤ a') (h : IsRothTheta a r H Θ) (h' : IsRothTheta a' r H Θ') : Θ ≤ Θ' := by
  obtain ⟨-, A, κ, hA, hκ, heq⟩ := h
  have hle := h'.1 A κ (hA.mono haa) hκ
  rw [heq] at hle
  exact_mod_cast hle

/-- `map` along a ring hom cannot raise a degree — its support only shrinks. -/
theorem degreeOf_map_le {σ R S : Type*} [CommSemiring R] [CommSemiring S] (f : R →+* S)
    (j : σ) (A : MvPolynomial σ R) : degreeOf j (map f A) ≤ degreeOf j A := by
  rw [degreeOf_le_iff]
  intro m hm
  exact monomial_le_degreeOf j (support_map_subset f A hm)

/-- **`Θ_m ≤ m`** — §9's third property, and the last of the three.

Needs `degreeOf_translate` (via `RothIndex.index_le_card`): the index is an infimum over the
*translated* support, so `Γ`'s degree bound on `A` reaches it only because translation
preserves degree.  That is why this could not be stated before `degreeOf_translate` existed. -/
theorem IsRothTheta.le_card {σ : Type*} [Fintype σ] {a : ℤ} {r H : σ → ℕ} {Θ : ℚ}
    (hr : ∀ j, r j ≠ 0) (h : IsRothTheta a r H Θ) : Θ ≤ (Fintype.card σ : ℚ) := by
  obtain ⟨-, A, κ, hA, -, heq⟩ := h
  have hA0 : map (algebraMap ℤ ℚ) A ≠ 0 := fun hz =>
    hA.1 (map_injective (algebraMap ℤ ℚ) (algebraMap ℤ ℚ).injective_int
      (by rw [map_zero]; exact hz))
  have hdeg : ∀ j, degreeOf j (map (algebraMap ℤ ℚ) A) ≤ r j := fun j =>
    le_trans (degreeOf_map_le _ j A) (hA.2.1 j)
  have hle := index_le_card r κ _ hr hA0 hdeg
  rw [heq] at hle
  exact_mod_cast hle

/-- **`Θ_m ≤ m` in the arc's arity language.**

`IsRothTheta.le_card` bounds by `Fintype.card σ`; everywhere else in this arc the arity is
carried by an ordering `o : σ ≃ Fin m`, and those agree. -/
theorem IsRothTheta.le_arity {σ : Type*} [Fintype σ] {m : ℕ} (o : σ ≃ Fin m)
    {a : ℤ} {r H : σ → ℕ} {Θ : ℚ} (hr : ∀ j, r j ≠ 0) (h : IsRothTheta a r H Θ) :
    Θ ≤ (m : ℚ) := by
  have hcard : Fintype.card σ = m := by rw [Fintype.card_congr o, Fintype.card_fin]
  simpa [hcard] using h.le_card hr

/-! ### Property `Γ_m` — all three clauses

`RothGrowth` above is only the **first** of `Γ_m`'s three clauses.  The arc carried it alone for
a long time, which made every statement here *stronger* than the source's: dropping a
hypothesis strengthens a theorem, and a theorem stronger than the one the source proves is one
nothing in the source will discharge.  The other two are reinstated below. -/

/-- **Mahler's height floor**, `Γ_m`'s third clause: `K₁ ≥ 2^{(1/t)(m−1)m(2m+1)}`.

⚠⚠ **Correction eighteen: `K_h` is the HEIGHT `H_h`, not the denominator.**  This definition
was called `rothDenomFloor` and its clause "the first *denominator*".  §11 fixes the reading
beyond argument — after defining `Γ_M` abstractly on `b, s₁,…,s_M, K₁,…,K_M` it says:

> By way of application, let `m ≥ 2`; let the ordered system of numbers `a, r₁,…,r_m, H₁,…,H_m`
> have the property `Γ_m`

so `b = a`, `s_h = r_h`, and `K_h = H_h`.  §13's descent confirms it: the new system is
`b, ρ₁,…,ρ_{m−1}, H₁,…,H_{m−1}` — the same heights, truncated — and its clauses are written
`ρ_h log H_h ≥ ρ₁ log H₁` and `H₁ ≥ 2^{(1/t)(m−1)m(2m+1)}`, in `H` throughout.

The exponent `ω·(m−1)m(2m+1)` is rational, so this rounds it **up** (`Nat.ceil`).  That makes
the clause stronger than the source's and hence every statement carrying it weaker — the safe
direction for a hypothesis being reinstated, since it cannot let a claim here outrun §14's. -/
def rothHeightFloor (m : ℕ) (ω : ℚ) : ℕ :=
  2 ^ ⌈ω * (((m - 1) * m * (2 * m + 1) : ℕ) : ℚ)⌉₊

/-- At one variable the floor is `1`, so it constrains nothing beyond `Γ₁`'s own `K₁ ≥ 2`. -/
theorem rothHeightFloor_one (ω : ℚ) : rothHeightFloor 1 ω = 1 := by
  norm_num [rothHeightFloor]

/-- **The floor is monotone in the arity.**

This is what lets `Γ_m` hand its floor clause down to `Γ_{m−1}`: the sub-system asks for a
*smaller* floor than the system supplies, because `(m−1)m(2m+1)` grows with `m`.  Without it
the descent (`RothVariableSplit.rothGamma_descend`) would have nothing to discharge clause 3
with. -/
theorem rothHeightFloor_mono {m m' : ℕ} {ω : ℚ} (hω : 0 ≤ ω) (h : m' ≤ m) :
    rothHeightFloor m' ω ≤ rothHeightFloor m ω := by
  have hA : (m' - 1) * m' * (2 * m' + 1) ≤ (m - 1) * m * (2 * m + 1) :=
    Nat.mul_le_mul (Nat.mul_le_mul (Nat.sub_le_sub_right h 1) h) (by omega)
  have hQ : ω * (((m' - 1) * m' * (2 * m' + 1) : ℕ) : ℚ)
      ≤ ω * (((m - 1) * m * (2 * m + 1) : ℕ) : ℚ) :=
    mul_le_mul_of_nonneg_left (by exact_mod_cast hA) hω
  exact Nat.pow_le_pow_right (by norm_num) (Nat.ceil_mono hQ)

/-- **Property `Γ_m`** (§11) — clauses 1–3 of case (ii).

⚠ **`Γ_M` is a disjunction with four clauses, not a conjunction of three.**  §11 defines
`b, s₁,…,s_M, K₁,…,K_M` to have `Γ_M` if **either**

    (i)   M = 1,  K₁ ≥ 2,  b ≤ K₁^{s₁t};

    (ii)  M ≥ 2  and  simultaneously
          1.  max(s₂/s₁, …, s_M/s_{M−1}) ≤ t      — `growth`, `RothGrowth` with `ω = 1/t`
          2.  s_h·log K_h ≥ s₁·log K₁  (h = 1..M) — `height`, written multiplicatively
          3.  K₁ ≥ 2^{(1/t)(M−1)M(2M+1)}          — `floor`
          4.  b ≤ K₁^{(1/M)s₁t}                   — ⚠ **not a field here**

An earlier version of this docstring said "all three clauses", which is wrong twice over.
Where the rest lives:

* **clause 4** is `RothLemmaUniform`'s height condition — `∀ j, B ≤ qⱼ^E` with `E ≤ ε·dⱼ` and
  `ε = t/m`, which is `b ≤ K₁^{(1/M)s₁t}` in uniform form.  It is carried, just not here.
* **case (i)** is the `m = 1` specialisation.  At `m = 1` the three fields below are vacuous or
  trivial (`rothHeightFloor 1 ω = 1`), and `RothLemmaUniform`'s standing `2 ≤ qⱼ` supplies
  `K₁ ≥ 2`.  So the aggregate matches, but this structure alone is **not** `Γ₁`.

Clause 2 is stated as `K₁^{s₁} ≤ K_h^{s_h}`, the same inequality with the logarithms cleared —
which is **exactly** Bombieri–Gubler 6.3.4's condition `qⱼ^{dⱼ} ≥ q₁^{d₁}`.  §11 runs it over
`h = 1,…,M`; Theorem 1 states it for `h = 2,…,m`.  The two agree, since `h = 1` is trivial, and
the `∀ j k, (j : ℕ) = 0 → …` encoding below covers both.

⚠ `K_h ≥ 2` is a **consequence** of `Γ_M`, not a hypothesis — §11 derives it, along with
`s₁ ≥ … ≥ s_M` and `∑ s_h ≤ M·s₁`.  `rothGamma_first_two_le` recovers the first of those here.
`RothLemmaUniform` assumes `2 ≤ qⱼ` outright, which is therefore redundant rather than
additional.

Both indexed clauses are written `∀ j, (j : ℕ) = 0 → …` rather than through `o.symm 0`, so that
`m = 0` needs no side condition rather than no `Fin 0` element. -/
structure RothGamma {σ : Type*} {m : ℕ} (o : σ ≃ Fin m) (ω : ℚ) (d : σ → ℕ) (Kh : σ → ℤ) :
    Prop where
  /-- Clause 1: consecutive degrees drop by at least a factor `ω = 1/t`. -/
  growth : RothGrowth o ω d
  /-- Clause 2: the first variable's `K^s` is the smallest.  `s_h·log K_h ≥ s₁·log K₁`. -/
  height : ∀ j k : Fin m, (j : ℕ) = 0 →
    Kh (o.symm j) ^ d (o.symm j) ≤ Kh (o.symm k) ^ d (o.symm k)
  /-- Clause 3: the first **height** is at least `2^{ω(m−1)m(2m+1)}`.  See correction
  eighteen at `rothHeightFloor`: `K_h` is `H_h`, not `Q_h`. -/
  floor : ∀ j : Fin m, (j : ℕ) = 0 → (rothHeightFloor m ω : ℤ) ≤ Kh (o.symm j)

/-- **`K₁ ≥ 2` is forced by clause 3** once `m ≥ 2` and `ω > 0`.

The floor's exponent `ω·(m−1)m(2m+1)` is then at least `10ω > 0`, so its ceiling is at least
`1` and the floor is at least `2`. -/
theorem rothHeightFloor_two_le {m : ℕ} {ω : ℚ} (hm : 2 ≤ m) (hω : 0 < ω) :
    2 ≤ rothHeightFloor m ω := by
  have hA : 0 < (m - 1) * m * (2 * m + 1) := by
    have : 1 ≤ m - 1 := by omega
    have : 1 ≤ m := by omega
    positivity
  have hpos : 0 < ω * (((m - 1) * m * (2 * m + 1) : ℕ) : ℚ) := by
    have : (0 : ℚ) < (((m - 1) * m * (2 * m + 1) : ℕ) : ℚ) := by exact_mod_cast hA
    positivity
  have hceil : 1 ≤ ⌈ω * (((m - 1) * m * (2 * m + 1) : ℕ) : ℚ)⌉₊ := Nat.ceil_pos.mpr hpos
  calc (2 : ℕ) = 2 ^ 1 := by norm_num
    _ ≤ rothHeightFloor m ω := Nat.pow_le_pow_right (by norm_num) hceil

/-- **`K₁ ≥ 2` is a consequence of `Γ_m`, not a hypothesis** — §11 says so, and this is the
first index's case.  `RothLemmaUniform`'s standing `2 ≤ qⱼ` is therefore redundant at `j = 0`
rather than additional. -/
theorem rothGamma_first_two_le {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {ω : ℚ} {d : σ → ℕ}
    {Kh : σ → ℤ} (hm : 2 ≤ m) (hω : 0 < ω) (hg : RothGamma o ω d Kh)
    (j : Fin m) (hj : (j : ℕ) = 0) : 2 ≤ Kh (o.symm j) :=
  le_trans (by exact_mod_cast rothHeightFloor_two_le hm hω) (hg.floor j hj)

/-- **Property `Γ_M`, case (ii), in full** — all four clauses, in the `t = p/q` idiom.

`RothGamma` above carries clauses 1–3 with `ω : ℚ` and leaves clause 4 to `RothLemmaUniform`.
This is the faithful object: `t = p/q`, so `ω = 1/t = q/p`, and both of the clauses that had a
rational exponent become `ℕ` inequalities with nothing rounded.

* **clause 3** is `2^F ≤ K₁` together with `q·(M−1)M(2M+1) ≤ F·p`, which is
  `K₁ ≥ 2^{(1/t)(M−1)M(2M+1)}` cleared of division.  No `Nat.ceil`, so no slack to lose.
* **clause 4** is `b^{Mq} ≤ K₁^{s₁p}`, which is `b ≤ K₁^{(1/M)s₁t}` raised to `Mq`.

⚠ Still case (ii) only; `Γ₁` is case (i) and is not this. -/
structure RothGammaFull {σ : Type*} {m : ℕ} (o : σ ≃ Fin m) (p q F : ℕ)
    (d : σ → ℕ) (Kh : σ → ℤ) (b : ℤ) : Prop where
  /-- Clause 1, with `ω = 1/t = q/p`. -/
  growth : RothGrowth o ((q : ℚ) / (p : ℚ)) d
  /-- Clause 2: the first variable's `K^s` is the smallest. -/
  height : ∀ j k : Fin m, (j : ℕ) = 0 →
    Kh (o.symm j) ^ d (o.symm j) ≤ Kh (o.symm k) ^ d (o.symm k)
  /-- Clause 3a: the floor's exponent is large enough, cleared of division. -/
  floorExp : q * ((m - 1) * m * (2 * m + 1)) ≤ F * p
  /-- Clause 3b: the first **height** is at least `2^F`. -/
  floor : ∀ j : Fin m, (j : ℕ) = 0 → (2 : ℤ) ^ F ≤ Kh (o.symm j)
  /-- Clause 4, raised to `m·q` so that it is integral. -/
  heightBound : ∀ j : Fin m, (j : ℕ) = 0 →
    b ^ (m * q) ≤ Kh (o.symm j) ^ (d (o.symm j) * p)
  /-- §11's derived list: `K₁ ≥ 2, K₂ ≥ 2, …, K_M ≥ 2`.

  ⚠⚠ **Correction twenty.**  This clause was absent, and its absence made `RothLemmaTheta`
  **false at `m = 1`** — see the counterexample recorded there.  At `m ≥ 2` it is a
  *consequence* of clauses 3a/3b (`(m−1)m(2m+1) ≥ 10 > 0` forces `F ≥ 1`, so `2 ≤ 2^F ≤ K₁`,
  and clause 2 carries it along), so adding it costs case (ii) nothing.  At `m = 1` those
  clauses are vacuous, and §11 states `K₁ ≥ 2` outright — it is the middle conjunct of case (i),
  `M = 1, K₁ ≥ 2, b ≤ K₁^{s₁t}`.  `RothGammaFull` encodes case (ii) only, so at `m = 1` it was
  not `Γ₁`. -/
  two_le : ∀ j, 2 ≤ Kh j
  /-- §11's standing setting: `s₁,…,s_M, K₁,…,K_M` are **positive** integers.

  ⚠ Also absent, and also unsafe in the same direction: without it `d j = 0` is admitted, where
  `idxWeight` reads `n/0 = 0` in `ℚ` and the index collapses.  A hypothesis structure missing a
  clause is a *weaker* hypothesis, hence a *stronger* theorem — the shape this arc has now got
  wrong four times. -/
  degPos : ∀ j, d j ≠ 0

/-- **`RothGammaFull` transports along a type equivalence.**

Every clause is stated through `o.symm j`, so reindexing the variable type composes the
equivalence into the ordering and leaves the content alone. -/
theorem RothGammaFull.rename_equiv {σ τ : Type*} {m p q F : ℕ} (e : σ ≃ τ)
    {o : σ ≃ Fin m} {d : σ → ℕ} {Kh : σ → ℤ} {b : ℤ}
    (h : RothGammaFull o p q F d Kh b) :
    RothGammaFull (e.symm.trans o) p q F (d ∘ e.symm) (Kh ∘ e.symm) b where
  growth := by
    intro j k hjk
    simpa using h.growth j k hjk
  height := by
    intro j k hj
    simpa using h.height j k hj
  floorExp := h.floorExp
  floor := by
    intro j hj
    simpa using h.floor j hj
  heightBound := by
    intro j hj
    simpa using h.heightBound j hj
  two_le := fun k => h.two_le _
  degPos := fun k => h.degPos _

/-- **From a `p/q` power bound to an `E : ℕ` one** — the bridge between the arc's two height
idioms, with the rounding as an explicit hypothesis.

`RothGammaFull`'s clause 4 is `b^{Mq} ≤ K₁^{s₁p}`; `RothBaseCase.index_le_of_abs_leadingCoeff_le`
wants `|lead| ≤ K^e` with `e : ℕ`.  This converts one to the other given `S ≤ Q·e`, which is
`e ≥ S/Q` written without a ceiling — the same device as `height_descend_exp`'s `j`. -/
theorem le_pow_of_pow_le_pow {x y : ℤ} {Q S e : ℕ} (hQ : Q ≠ 0) (hy : 1 ≤ y)
    (h : x ^ Q ≤ y ^ S) (he : S ≤ Q * e) : x ≤ y ^ e := by
  have hy0 : (0 : ℤ) ≤ y := le_trans zero_le_one hy
  refine le_of_pow_le_pow_left₀ hQ (by positivity) ?_
  calc x ^ Q ≤ y ^ S := h
    _ ≤ y ^ (Q * e) := pow_le_pow_right₀ hy he
    _ = (y ^ e) ^ Q := by rw [← pow_mul, mul_comm]

/-- **`Γ_M` in full implies the three-clause form** — so `RothGammaFull` feeds everything
`RothGamma` feeds, at `ω = q/p`.

The only content is clause 3: `rothHeightFloor m (q/p)` rounds `(q/p)(m−1)m(2m+1)` **up**, while
`floorExp` says `F` is already at least that value, so the ceiling is at most `F` and the
rounded floor is at most `2^F`. -/
theorem RothGammaFull.toRothGamma {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {p q F : ℕ}
    {d : σ → ℕ} {Kh : σ → ℤ} {b : ℤ} (hp : p ≠ 0)
    (hg : RothGammaFull o p q F d Kh b) :
    RothGamma o ((q : ℚ) / (p : ℚ)) d Kh where
  growth := hg.growth
  height := hg.height
  floor := by
    intro j hj
    refine le_trans ?_ (hg.floor j hj)
    have hpQ : (0 : ℚ) < (p : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hp
    have hA : ((q * ((m - 1) * m * (2 * m + 1)) : ℕ) : ℚ) ≤ ((F * p : ℕ) : ℚ) := by
      exact_mod_cast hg.floorExp
    have hceil : ⌈(q : ℚ) / (p : ℚ) * (((m - 1) * m * (2 * m + 1) : ℕ) : ℚ)⌉₊ ≤ F := by
      rw [Nat.ceil_le, div_mul_eq_mul_div, div_le_iff₀ hpQ]
      push_cast at hA ⊢
      linarith
    show ((rothHeightFloor m ((q : ℚ) / (p : ℚ)) : ℕ) : ℤ) ≤ (2 : ℤ) ^ F
    unfold rothHeightFloor
    push_cast at hceil ⊢
    exact pow_le_pow_right₀ (by norm_num) hceil

/-! ### ⚠ Why `RothGamma` is not retired here

`RothGammaFull.toRothGamma` makes the full object strictly richer, so `rothGammaFull_descend`
already feeds everything `RothGamma` feeds.  Retiring `RothGamma` and putting `RothGammaFull`
into `RothLemmaUniform` looks mechanical and is **not**.

`RothLemmaUniform`'s height condition is `∀ j, B ≤ qⱼ^E` with `E : ℕ`, and the base case is
built on it: `RothBaseCase.index_le_of_abs_leadingCoeff_le` takes `|lead| ≤ q^e` and returns
`index ≤ e/d`.  Clause 4 is `b^{Mq} ≤ K₁^{s₁p}` — a different encoding, and swapping it in means
`RothBaseCase` needs a variant taking a power bound.

`le_pow_of_pow_le_pow` is the bridge, and it shows what the variant would cost: from
`b^{Mq} ≤ K^{s₁p}` one gets `b ≤ K^e` for any `e` with `s₁p ≤ Mq·e`, so the smallest usable `e`
is `⌈s₁p/(Mq)⌉` and the base case then yields `index ≤ ⌈s₁p/(Mq)⌉/d` rather than
`s₁p/(Mqd)`.  ⚠ The excess is at most `1/d`.

Whether `1/d` is affordable is **not obvious and not checked**: `d` is a large degree, so it is
small — but clause 3's calibration is exactly tight (`height_descend_pq_witness` sits on the
boundary in four hypotheses at once), and this arc has now twice found that "small slack in a
tight place" is where the constants stop working.  That is the thing to check before migrating,
not after. -/

/-- **Rescaling the degree vector preserves `Γ_m`** — the companion to `rothGrowth_scale`.

The induction step measures its sub-problems against `r·d`, and all three clauses survive.
Clause 2 does so because raising `K₁^{s₁} ≤ K_h^{s_h}` to the `r`-th power is monotone once the
heights are non-negative, which `2 ≤ Kh j` supplies; clause 3 does not mention `d` at
all. -/
theorem rothGamma_scale {σ : Type*} {m : ℕ} {o : σ ≃ Fin m} {ω : ℚ} {d : σ → ℕ} {Kh : σ → ℤ}
    {r : ℕ} (hr : r ≠ 0) (hq : ∀ j, 2 ≤ Kh j) (hg : RothGamma o ω d Kh) :
    RothGamma o ω (fun j => r * d j) Kh where
  growth := rothGrowth_scale hr hg.growth
  height := by
    intro j k hj
    have h := hg.height j k hj
    have h0 : (0 : ℤ) ≤ Kh (o.symm j) ^ d (o.symm j) :=
      pow_nonneg (le_trans (by norm_num) (hq _)) _
    calc Kh (o.symm j) ^ (r * d (o.symm j))
        = (Kh (o.symm j) ^ d (o.symm j)) ^ r := by rw [← pow_mul, mul_comm]
      _ ≤ (Kh (o.symm k) ^ d (o.symm k)) ^ r := pow_le_pow_left₀ h0 h r
      _ = Kh (o.symm k) ^ (r * d (o.symm k)) := by rw [← pow_mul, mul_comm]
  floor := hg.floor

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

/-- **Roth's lemma at `m = 1`, in the arc's own encoding: `Γ₁ ⟹ RothBound 1 t Θ₁`.**

`rothBound_one` unfolds `RothBound 1 t θ` to `0 ≤ θ ∧ θ ≤ t`, so this is `isRothTheta_le_of_gamma_one`
paired with `IsRothTheta.nonneg`.  Its value is that it is the shape `rothBound_chain` and
`rothConstant_chain` consume: the base case now enters the recursion as a `RothBound`, not as a
statement about `index` that something else would have to translate.

⚠ **`t` is the exact bound at `m = 1`, and that is what pins `c₁ = 1`.**  `rothConstant_rec`
does not determine the constant — `rothConstant_chain` needs a starting value, and correction
eleven traced `c_m = 2^{m+1} − 3` to the base case rather than to the recurrence.  This theorem
is that starting value, now proved from `Γ₁` rather than assumed. -/
theorem rothBound_one_of_gamma_one {a : ℤ} {r H : Unit → ℕ} {Θ : ℚ} {p q : ℕ}
    (hΘ : IsRothTheta a r H Θ) (hr : r () ≠ 0) (hq : q ≠ 0) (hH : 2 ≤ H ())
    (hclause : a ^ q ≤ (H () : ℤ) ^ (r () * p)) :
    RothBound 1 ((p : ℚ) / (q : ℚ)) Θ :=
  (rothBound_one _ _).mpr ⟨hΘ.nonneg, isRothTheta_le_of_gamma_one hΘ hr hq hH hclause⟩

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

⚠⚠ **Correction twelve: an earlier version of this docstring claimed the reading was "forced
by the answer".  It is not, and the claim is withdrawn.**

What it said was: §13's `t` is a *row cost* and §11's is the parameter, `Ψ_m = Θ_{m−1} + t`
closes to `2c+3` only under the parameter reading, so the constant identifies the reading.
The second clause is false.  §14's own display splits the same total differently — leading
term `s` (the row cost weakened), and `2√(c+1)` bounded by the cruder `2c+2` — and lands on
`2c+3` as well:

    §14:        1     + (2c+2)  =  2c+3
    this proof: (c+1) + (c+2)   =  2c+3

`rothConstant_step_source` below proves that route, so the agreement is a **checked fact** and
not an assertion.  Two distinct splits reaching the same constant means reproducing the
constant discriminates nothing.

So: the hypotheses here are **stated, not derived**.  The theorem is true whatever `Ψ` and `u`
mean, and which quantity §14's `Ψ_m = Θ_{m−1} + t` refers to remains an unverified
reconstruction.  That is the honest status, and the previous docstring overstated it.

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

/-- **§14's own split of the same step** — a different route to the same constant.

The source's display leads with the row cost (weakened from `t` to `s`) rather than with `Ψ`,
and bounds `2√(c+1)` by the crude `2c+2` where `rothConstant_step` uses the sharper `c+2`.
Both land on `2c+3`; this is the checked half of correction twelve.

⚠ Note this route needs **no** `s ≤ 1`.  `rothConstant_step` does, for `s² ≤ s`.  (Getting
`Ψ ≤ (c+1)s²` in the first place needs it either way, so nothing is gained — but the
difference is real and shows the two splits are not notational variants of one argument.) -/
theorem rothConstant_step_source {m : ℕ} (hm : 1 ≤ m) {s Ψ u θ : ℚ}
    (hs0 : 0 ≤ s)
    (hΨ : Ψ ≤ ((rothConstant m : ℚ) + 1) * s ^ 2)
    (hu : u ^ 2 ≤ 4 * Ψ)
    (hθ : θ ≤ s + u) :
    θ ≤ (rothConstant (m + 1) : ℚ) * s := by
  have hc0 : (0 : ℚ) ≤ (rothConstant m : ℚ) := Nat.cast_nonneg _
  have hus : u ≤ (2 * (rothConstant m : ℚ) + 2) * s := by
    refine le_of_pow_le_pow_left₀ two_ne_zero (by nlinarith) ?_
    nlinarith [sq_nonneg ((rothConstant m : ℚ) * s),
      mul_nonneg hc0 (sq_nonneg s)]
  have hrec : ((rothConstant (m + 1) : ℕ) : ℚ) = 2 * (rothConstant m : ℚ) + 3 := by
    rw [rothConstant_rec m hm]; push_cast; ring
  rw [hrec]
  linarith

/-- `c_m ≥ 1` for `m ≥ 1` — Mahler states this as a standing fact in §14's computation. -/
theorem rothConstant_one_le {m : ℕ} (hm : 1 ≤ m) : 1 ≤ rothConstant m := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hm
  have h : (2 : ℕ) ^ 2 ≤ 2 ^ (1 + k + 1) := Nat.pow_le_pow_right (by norm_num) (by omega)
  simp only [rothConstant]
  omega

/-- **§14's step exactly as printed** — Lemma 4's shape, and the faithful one.

Lemma 4 (§13's packaged conclusion, now **read**) is

    Θ_m ≤ t + 2·max(Ψ_m, √Ψ_m),      Ψ_m = Θ_{m−1} + t,

given property `Γ_m`, and it **produces** a system with `Γ_{m−1}`.  ⚠ No side condition.

§14 then bounds both branches of that max by the *same* quantity `(c+1)s`, which is why the
`max` disappears and why the constant is what it is:

* `Ψ ≤ c·s² + t ≤ c·s + s = (c+1)s`, using `s² ≤ s` and `t ≤ s`;
* `√Ψ ≤ (c+1)s`, because `Ψ ≤ (c+1)s² ≤ (c+1)²s²` — the crude `c+1 ≤ (c+1)²`, valid since
  `c ≥ 1` (`rothConstant_one_le`, which is Mahler's own standing hypothesis).

Leading `t ≤ s` contributes `1`, the max contributes `2(c+1)`, total `2c+3`.

`w` is `max(Ψ, √Ψ)`, encoded root-free as `w ≤ Ψ ∨ w² ≤ Ψ`.  ⚠ `0 ≤ w` is deliberately **not**
required, though the max satisfies it: without it the second disjunct also admits `−√Ψ`, and a
smaller `w` only makes `s + 2w` smaller, so the theorem is stronger without it.  Same reason
`0 ≤ u` came off `rothConstant_step`.  Callers instantiate at the real max, where it holds.

⚠⚠ **The twenty-fifth correction is the `≤` in that disjunction; it used to be `=`.**  The two
encodings are not interchangeable, and the `=` one is not the faithful reading of
`θ ≤ t + 2·max(Ψ, √Ψ)`:

* with `≤`, the admissible `w` are exactly `w ≤ max(Ψ, √Ψ)`, so `∃ w` with `θ ≤ t + 2w` says
  precisely `θ ≤ t + 2·max(Ψ, √Ψ)`;
* with `=`, the admissible `w` are `Ψ` and — **only when `Ψ` is a square in `ℚ`** — `±√Ψ`.

So the `=` form silently demands that `Ψ` be a rational square whenever the `√` branch is the
operative one, which is the regime the recursion actually runs in (`Ψ < 1`).  Nothing supplies
that: `Ψ = Θ_{m−1} + t` with `Θ_{m−1}` an infimum over a finite set of indices and `t = p/q`.
The producer of this disjunction is `RothVariableSplit.RothLemma4`, which is why the `def`
moved with it.

⚠ Note what the `=` form cost and what it did not.  Nothing proved was false — this theorem is
true either way, and *stronger* now that its hypothesis is weaker.  The damage was entirely on
the other side of the arrow: `RothLemma4` had to **produce** a `w`, and could not.  A hypothesis
nobody has had to discharge is indistinguishable from an unsatisfiable one — correction 9's
lesson, and this is its fourth instance in the arc.

⚠ This covers what `rothConstant_step_source` does not — that one's `u² ≤ 4Ψ` is the `√Ψ`
branch alone, which is the max only when `Ψ ≤ 1`. -/
theorem rothConstant_step_lemma4 {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {m : ℕ} (hm : 1 ≤ m) {s Ψ w θ : K}
    (hs0 : 0 ≤ s) (hs1 : s ≤ 1)
    (hΨ : Ψ ≤ ((rothConstant m : K) + 1) * s ^ 2)
    (hw : w ≤ Ψ ∨ w ^ 2 ≤ Ψ)
    (hθ : θ ≤ s + 2 * w) :
    θ ≤ (rothConstant (m + 1) : K) * s := by
  have hc1 : (1 : K) ≤ (rothConstant m : K) := by exact_mod_cast rothConstant_one_le hm
  have hc0 : (0 : K) ≤ (rothConstant m : K) + 1 := by linarith
  have hsq : s ^ 2 ≤ s := by nlinarith
  have hws : w ≤ ((rothConstant m : K) + 1) * s := by
    rcases hw with h | h
    · calc w ≤ Ψ := h
        _ ≤ ((rothConstant m : K) + 1) * s ^ 2 := hΨ
        _ ≤ ((rothConstant m : K) + 1) * s := mul_le_mul_of_nonneg_left hsq hc0
    · refine le_of_pow_le_pow_left₀ two_ne_zero (mul_nonneg hc0 hs0) ?_
      calc w ^ 2 ≤ Ψ := h
        _ ≤ ((rothConstant m : K) + 1) * s ^ 2 := hΨ
        _ ≤ (((rothConstant m : K) + 1) * s) ^ 2 := by
            nlinarith [sq_nonneg s, mul_nonneg hc0 (sq_nonneg s)]
  have hrec : ((rothConstant (m + 1) : ℕ) : K) = 2 * (rothConstant m : K) + 3 := by
    rw [rothConstant_rec m hm]; push_cast; ring
  rw [hrec]
  linarith

/-- **§14's step with the base case perturbed by `δ`** — what the `1/d` rounding costs.

If the base case yields `Θ₁ ≤ t + δ` instead of `Θ₁ ≤ t` — which is exactly what migrating
`RothLemmaUniform` onto clause 4's `p/q` form would produce, with `δ = 1/d` — then `Ψ` is
bounded by `(c+1)s² + δ` rather than `(c+1)s²`, and the step's conclusion picks up `2v` where
`v = √δ`.

Both branches of the max still land on `(c+1)s + v`:

* `w = Ψ ≤ (c+1)s² + v² ≤ (c+1)s + v`, using `s² ≤ s` and `v² ≤ v`;
* `w² = Ψ ≤ (c+1)s² + v² ≤ ((c+1)s + v)²`, since `(c+1)² ≥ c+1` and the cross term is
  non-negative.

⚠ **The perturbation does not fit inside the constant.**  `2c+3` is what both branches give
with the crude bounds already exactly tight at `c = 0`, so there is no smaller admissible
constant to trade against `2v`.  The invariant would have to widen from `θ ≤ c_m·s` to
`θ ≤ c_m·s + κ` and the recursion be re-derived for `κ` — a different theorem, not a looser
constant in this one. -/
theorem rothConstant_step_perturbed {m : ℕ} (hm : 1 ≤ m) {s Ψ w v θ : ℚ}
    (hs0 : 0 ≤ s) (hs1 : s ≤ 1) (hv0 : 0 ≤ v) (hv1 : v ≤ 1)
    (hΨ : Ψ ≤ ((rothConstant m : ℚ) + 1) * s ^ 2 + v ^ 2)
    (hw : w ≤ Ψ ∨ w ^ 2 ≤ Ψ)
    (hθ : θ ≤ s + 2 * w) :
    θ ≤ (rothConstant (m + 1) : ℚ) * s + 2 * v := by
  have hc1 : (1 : ℚ) ≤ (rothConstant m : ℚ) := by exact_mod_cast rothConstant_one_le hm
  have hsq : s ^ 2 ≤ s := by nlinarith
  have hvq : v ^ 2 ≤ v := by nlinarith
  have hws : w ≤ ((rothConstant m : ℚ) + 1) * s + v := by
    rcases hw with h | h
    · nlinarith
    · refine le_of_pow_le_pow_left₀ two_ne_zero (by nlinarith) ?_
      nlinarith [h, sq_nonneg s, mul_nonneg (le_trans zero_le_one hc1) (sq_nonneg s),
        mul_nonneg (mul_nonneg (by linarith : (0:ℚ) ≤ (rothConstant m : ℚ) + 1) hs0) hv0]
  have hrec : ((rothConstant (m + 1) : ℕ) : ℚ) = 2 * (rothConstant m : ℚ) + 3 := by
    rw [rothConstant_rec m hm]; push_cast; ring
  rw [hrec]
  linarith

/-! ### ⚠⚠ The `1/d` slack does **not** survive the recursion, however small it is

Iterating `rothConstant_step_perturbed` gives a recursion for the accumulated slack.  Writing
`Θ_m ≤ c_m·s_m + κ_m` with `s_m = t^{2^{−(m−1)}}`, and using `s_{m+1}² = s_m`:

    Ψ_{m+1} = Θ_m + Θ₁ ≤ c_m·s_{m+1}² + κ_m + t + δ ≤ (c_m + 1)·s_{m+1}² + (κ_m + δ),

so the step applies with `v² = κ_m + δ` and yields `κ_{m+1} = 2·√(κ_m + δ)`.

⚠ **That map expands.**  `2√x > x` exactly when `0 < x < 4` (`two_sqrt_expands` below), so from
any `κ₁ ≥ 0` and **any** `δ > 0` the sequence increases strictly and converges to the fixed
point `2 + 2√(1+δ) ≈ 4`.  A bound of `≈ 4` on an index is worthless — Roth's indices are far
below 1.

At `δ = 0` the recursion has the other fixed point, `κ = 0`, and stays there: that is the
unperturbed argument working.  So the question "is `1/d` small enough?" has the answer **no,
and smallness is not the issue** — the recursion amplifies any positive perturbation to the
same place.

**Consequence for the migration.**  Do not put `RothLemmaUniform` on clause 4's `p/q` form via
the rounded bridge.  `le_pow_of_pow_le_pow`'s `S ≤ Q·e` is affordable only with `e` chosen so
that no rounding occurs at all; a `RothBaseCase` variant taking the power bound *directly* —
`|lead|^Q ≤ q^S` giving `index ≤ S/(Q·d)` with no ceiling — is the only version worth building.

⚠ Recorded because the previous entry costed this at "at most `1/d`" and called affordability
"not obvious".  It is obvious once the recursion is written down, and the answer is the
opposite of the one smallness suggests. -/

/-- **The slack recursion expands**: `2√x > x` for `0 < x < 4`, root-free.

`y = 2√x` is `y ≥ 0 ∧ y² = 4x`. -/
theorem two_sqrt_expands {x y : ℚ} (hx : 0 < x) (hx4 : x < 4) (hy : 0 ≤ y)
    (h : y ^ 2 = 4 * x) : x < y := by
  nlinarith [sq_nonneg (x - y), sq_nonneg x]

/-- **And `4` is its fixed point** — so the amplification stops only where the bound is useless. -/
theorem two_sqrt_fixed : ((4 : ℚ)) ^ 2 = 4 * 4 := by norm_num

/-- ⚠ **At `m = 2` the unperturbed hypothesis has no room at all.**

`Ψ ≤ (c+1)s²` is reached from `Θ_{m−1} ≤ c·s²` and `t ≤ s²`, and `t = s^{2^{m−1}}`, so at
`m = 2` that reads `t = s²` — an **equality**.  Any `δ > 0` added to the base case exceeds the
budget immediately, which is why `rothConstant_step_perturbed` has to carry `v` in its
conclusion rather than absorb it. -/
theorem two_pow_one_eq_two : (2 : ℕ) ^ (2 - 1) = 2 := by decide

/-- **§14's induction, as pure arithmetic** — the chain, closed.

Given the step at every level, `Θ_n ≤ c_n·s_n` propagates from the base case all the way up.
The sequence `sq` is `s_n`, each the square root of the previous (`sq (n+1)² = sq n`), which is
what `rothBound_pow_iff` needs at each level and what keeps the whole chain at a single `t`.

⚠ **`t ≤ sq n` at every level is a real hypothesis, not bookkeeping.**  It is what lets `Ψ`
absorb the additive `t`, and it is exactly `t ≤ s^{2^k}` for the relevant `k` — true because
`0 ≤ s ≤ 1`, but it has to be supplied.

⚠ **The chain needs the `s_n` to exist as rationals.**  For a general rational `t` they do not:
`s_n = t^{2^{−(n−1)}}` is irrational in general.  So this closes the induction exactly for `t`
that is a perfect `2^{m−1}`-th power of a rational — which is a genuine restriction, and the
price of staying in `ℚ`.  Going to `ℝ` for the exponent is the alternative; it is not taken. 
⚠⚠ **Correction twenty-three: the ranges used to be unbounded, and that made this vacuous.**

`hsq` read `∀ n, sq (n + 1) ^ 2 = sq n` — for **every** `n`.  Iterating, `sq 1 = sq (k+1)^{2^k}`
for every `k`, so `sq 1` is a `2^k`-th power **in `ℚ`** for every `k`.  Writing `sq 1 = a/b` in
lowest terms, each `a` and `b` is then a `2^k`-th power for every `k`, so every prime exponent in
them is divisible by every `2^k` and hence zero: `sq 1 = 1` (or `0`, forcing `sq ≡ 0` and
`t ≤ 0`).  At `sq 1 = 1` the whole sequence is `1` and the conclusion is `Θ n ≤ c_n`, with **no
`t` in it at all** — not §14's `Θ_m ≤ c_m·t^{2^{−(m−1)}}`.

So the only instance was the constant one the witness below exhibits, and the witness's own note
— "the interesting instances have `sq n = s^{2^{m−n}}`" — describes a sequence that is not
defined for `n > m` and therefore never satisfied `hsq`.

Bounding the ranges to `n < M` fixes it: only `M` successive square roots are needed, so
`sq 1 = t` may be any `2^{M−1}`-th power of a rational, which is what an application choosing its
own `t` would supply anyway.

⚠ The arithmetic above is elementary but **is not formalised here**.  A Lean witness would need
the irrationality of `√2` (`Mathlib.Data.Real.Irrational`), whose `.olean` is not in this
project's built Mathlib closure, so importing it would mean compiling that module.  Recorded as
an argument, not as a theorem.

⚠ The restriction to perfect powers is an artifact of the **root-free rational encoding**, not
of §14 — over `ℝ` every non-negative `t` has a `2^k`-th root and the restriction vanishes.
Removing it in `ℚ` means proving the step by passing to `ℝ` and back, which the inequalities all
support (they are field-generic) but which is not done here.
-/
theorem rothConstant_chain {M : ℕ} {sq Θ w : ℕ → ℚ} {t : ℚ}
    (hs0 : ∀ n, 0 ≤ sq n) (hs1 : ∀ n, sq n ≤ 1)
    (hsq : ∀ n, n < M → sq (n + 1) ^ 2 = sq n)
    (ht : ∀ n, t ≤ sq n)
    (hbase : Θ 1 ≤ (rothConstant 1 : ℚ) * sq 1)
    (hw : ∀ n, n < M → w n ≤ Θ n + t ∨ (w n) ^ 2 ≤ Θ n + t)
    (hstep : ∀ n, n < M → Θ (n + 1) ≤ t + 2 * w n) :
    ∀ n, 1 ≤ n → n ≤ M → Θ n ≤ (rothConstant n : ℚ) * sq n := by
  intro n hn
  induction n, hn using Nat.le_induction with
  | base => intro _; exact hbase
  | succ n hn ih =>
      intro hnM
      have hlt : n < M := by omega
      have hΨ : Θ n + t ≤ ((rothConstant n : ℚ) + 1) * sq (n + 1) ^ 2 := by
        rw [hsq n hlt]
        linarith [ht n, ih (by omega)]
      exact rothConstant_step_lemma4 (θ := Θ (n + 1)) hn (hs0 (n + 1)) (hs1 (n + 1)) hΨ
        (hw n hlt) (by linarith [hstep n hlt, ht (n + 1)])

/-- **The chain in `RothBound` shape.**  Same hypotheses, conclusion converted by
`rothBound_pow_iff` at each level. -/
theorem rothBound_chain {M : ℕ} {sq Θ w : ℕ → ℚ} {t : ℚ}
    (hs0 : ∀ n, 0 ≤ sq n) (hs1 : ∀ n, sq n ≤ 1)
    (hsq : ∀ n, n < M → sq (n + 1) ^ 2 = sq n)
    (ht : ∀ n, t ≤ sq n) (hΘ0 : ∀ n, 0 ≤ Θ n)
    (hbase : Θ 1 ≤ (rothConstant 1 : ℚ) * sq 1)
    (hw : ∀ n, n < M → w n ≤ Θ n + t ∨ (w n) ^ 2 ≤ Θ n + t)
    (hstep : ∀ n, n < M → Θ (n + 1) ≤ t + 2 * w n) :
    ∀ n, 1 ≤ n → n ≤ M → RothBound n (sq n ^ (2 ^ (n - 1))) (Θ n) := fun n hn hnM =>
  (rothBound_pow_iff (hs0 n)).mpr
    ⟨hΘ0 n, rothConstant_chain hs0 hs1 hsq ht hbase hw hstep n hn hnM⟩

/-- ⚠ **Why the chain is parameterised by `s` and not by `t` alone.**

The obvious attempt is to run the induction directly on `RothBound`'s squared form, never
naming `s`.  Writing `k = 2^{n−1}`, one has `Θ'^k ≤ c_n^k·t` and wants `Θ^{2k} ≤ c_{n+1}^{2k}·t`
from `Θ ≤ t + 2w`, `w² = Θ' + t`.  Bounding `(a+b)^k ≤ 2^k(a^k + b^k)` twice and using `t ≤ 1`
gives

    Θ^{2k} ≤ 4^k·(8^k·(c_n^k + 1) + 1)·t,

whose leading behaviour is `(32·c_n)^k`, so the route needs `32·c_n ≤ (2c_n + 3)^2`.  At
`c_n = 1` that is `32 ≤ 25` — **false**, and `c₁ = 1`, so it fails at the very first step.

⚠ This does **not** prove no root-free route exists; it shows the natural crude one loses too
much.  That is the same `√`-slack failure as everywhere else in this arc, and it is why the
chain above names `s`. -/
theorem crude_chain_fails : ¬ (32 * 1 ≤ (2 * 1 + 3) ^ 2) := by decide

/-- **Non-vacuity of the chain**, at the constant sequence `sq ≡ 1`, `t = 1`.

⚠ Degenerate on purpose: `sq ≡ 1` satisfies `sq (n+1)² = sq n` and `t ≤ sq n` trivially, so
this checks that the seven hypotheses can hold together at all.  The interesting instances have
`sq n = s^{2^{m−n}}` for a small `s`, where the chain is not constant. -/
theorem rothConstant_chain_witness :
    ∀ n, 1 ≤ n → (fun _ : ℕ => (1 : ℚ)) n ≤ (rothConstant n : ℚ) * 1 := by
  intro n hn
  have := rothConstant_one_le hn
  have : (1 : ℚ) ≤ (rothConstant n : ℚ) := by exact_mod_cast this
  simpa using this

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

/-- **§13's conclusion feeds §14's step** — the junction, with every linking hypothesis named.

`RothInductionStep.index_le_two_mul_max_of_det_bound` ends at `θ ≤ t + 2·max(S/r, q)`.  That is
`rothBound_step`'s `θ ≤ Ψ + u` with `u = 2·max(S/r, q)`, provided `t ≤ Ψ` — which holds because
§14's `Ψ = Θ_{m−1} + t` and `Θ_{m−1} ≥ 0` — and provided both branches of the max are bounded
by `√Ψ`, which is what `A² ≤ Ψ` and `q² ≤ Ψ` say without naming a root.

`A` is `S/r` at the call site; it is left abstract because nothing here needs it to be a
quotient. -/
theorem rothBound_of_max_form {m : ℕ} (hm : 1 ≤ m) {s t θ A q Ψ : ℚ}
    (hs0 : 0 ≤ s) (hs1 : s ≤ 1) (hθ0 : 0 ≤ θ)
    (hΨ : Ψ ≤ ((rothConstant m : ℚ) + 1) * s ^ 2)
    (htΨ : t ≤ Ψ) (hA : A ^ 2 ≤ Ψ) (hq : q ^ 2 ≤ Ψ)
    (hθ : θ ≤ t + 2 * max A q) :
    RothBound (m + 1) (s ^ (2 ^ m)) θ := by
  have hmax : (max A q) ^ 2 ≤ Ψ := by
    rcases max_choice A q with h | h <;> rw [h] <;> assumption
  exact rothBound_step hm hs0 hs1 hθ0 hΨ (u := 2 * max A q) (by nlinarith) (by linarith)

/-- ⚠ **The junction squeezes `q` from both sides**, and that is the whole numeric content.

§13 needs `S ≤ q²·rr` — a **lower** bound on `q²`, since `q` is its rational stand-in for
`√(S/rr)`.  `rothBound_of_max_form` needs `q² ≤ Ψ` — an **upper** bound.  Together they force

    S ≤ Ψ·rr,

and that single inequality is what the §13 → §14 junction reduces to.  The bean for this arc
had said the assembly "terminates in a numeric condition"; this is that condition, isolated to
one place rather than diffused through the recursion.

⚠ It is necessary, not sufficient: a rational `q` with `S/rr ≤ q² ≤ Ψ` exists whenever
`S/rr < Ψ` (rational squares are dense), but at equality it exists only if `Ψ` is a rational
square.  The strict form is what a caller should establish; that density argument is not
proved here. -/
theorem le_mul_of_max_form_squeeze {S rr q Ψ : ℚ} (hrr : 0 ≤ rr)
    (hSq : S ≤ q ^ 2 * rr) (hqΨ : q ^ 2 ≤ Ψ) : S ≤ Ψ * rr := by
  nlinarith

/-- **What the junction's condition becomes at the call site** — the numeric requirement, made
fully explicit.

`RothOperatorFamily.index_le_of_rothGrowth_of_factor_bound` carries §13's hypothesis in the
form `(d₂ + 1)·Φ ≤ q²·D₂`, where `Φ` bounds each factor's index, `d₂` is the split-off
variable's degree and `D₂ ≤ d₂` a floor for it.  `rothBound_of_max_form` adds `q² ≤ Ψ`.
Chaining them through `le_mul_of_max_form_squeeze` gives `(d₂ + 1)·Φ ≤ Ψ·D₂`, and with §14's
`Ψ = Θ_{m−1} + t = Φ + t` that rearranges to exactly the hypothesis below.

⚠ **It is a largeness requirement on the split-off degree, not a bookkeeping identity.**  At
the best case `D₂ = d₂` it reads `Φ ≤ t·d₂` (`factor_bound_le_of_split_degree_eq`).

What `Φ` is, precisely: `RothInductionStep.factor_bound_of_rescaled` bounds the two
Wronskians' summed index at the *unscaled* degrees by `r·(εU + εV)`, so the arc's `Φ` is
`εU + εV` — the **sum** of the two halves' bounds, hence `Φ ≤ 2Θ_{m−1}`, not `Θ_{m−1}`.  The
`r` is the rescaling factor and cancels against §13's `S/r`; it is not a row count entering
the size of `Φ`.  Since `Θ_{m−1} ≤ c_{m−1}·t^{2^{−(m−2)}}` is for small `t` much larger than
`t`, `d₂` must be at least `Φ/t`.

⚠⚠ **Superseded** — the requirement does not arise at the source's `n` normalisation, which
§13 reaches from the `r_m` one by a proved weakening (`radicand_weaken`).  See corrections
fourteen and fifteen below; fourteen got the *reason* wrong and fifteen repairs it, but the
conclusion that this requirement is an artifact stands.  Kept because this arc keeps its
corrections visible rather than deleting them.

⚠⚠ **Correction thirteen: this is a cost of the arc's own §13 formulation, not a hypothesis of
Roth's lemma.**  §13's packaged conclusion is Mahler's **Lemma 4**, now read:

    Θ_m ≤ t + 2·max(Ψ_m, √Ψ_m),      Ψ_m = Θ_{m−1} + t,

given `Γ_m`, and producing a system with `Γ_{m−1}`.  Its `max` is over **one** quantity and its
square root — no `/n`, no `/r_m`, and **no side condition**.  The arc's
`index_le_two_mul_max_of_det_bound` instead has `max(S/r, q)` with `S ≤ q²·rr`, which is where
`(d₂ + 1 − D₂)·Φ ≤ t·D₂` comes from.

So the requirement below is real for the arc's route and must be discharged, but it is **not**
an extra hypothesis of Roth's lemma: whatever `S ≤ q²·rr` costs is discharged from `Γ_m` inside
§13's proof.  ⚠ That proof body has not been read, so *how* is still open — this says only that
it is not a gap in the theorem.  The previous version of this docstring presented the condition
as the arc's open parameter question; that framing was wrong.

`Γ_m`'s clauses 2 and 3 are still what any discharge must use, and this remains the first point
in the arc where they are needed — nothing earlier needed them, which is exactly why they went
missing for so long.

⚠ Neither positivity of `Φ` nor of `D₂` is a hypothesis — the rearrangement is linear in the
monomials.  Same reason `0 ≤ u` came off `rothConstant_step`. -/
theorem factor_bound_le_of_split_degree {Φ t D₂ : ℚ} {d₂ : ℕ}
    (h : (((d₂ : ℚ) + 1) - D₂) * Φ ≤ t * D₂) :
    ((d₂ : ℚ) + 1) * Φ ≤ (Φ + t) * D₂ := by nlinarith

/-- **The best case `D₂ = d₂`**, where the requirement is simply `Φ ≤ t·d₂`. -/
theorem factor_bound_le_of_split_degree_eq {Φ t : ℚ} {d₂ : ℕ} (h : Φ ≤ t * (d₂ : ℚ)) :
    ((d₂ : ℚ) + 1) * Φ ≤ (Φ + t) * (d₂ : ℚ) :=
  factor_bound_le_of_split_degree (by nlinarith)

/-! ### ⚠⚠ Corrections fourteen and fifteen: the radicand, and reading one display alone

**Correction fourteen, as first written, was wrong, and correction fifteen withdraws it.**
Both are kept: what fourteen got right survives, and *how* it went wrong is the more useful
record.

**What fourteen said.**  §13's packaged display is

    J(A) ≤ t + 2·max( (1/n)·J(W) , √( (1/n)·J(W) ) )

— both branches over the same quantity.  Correction 9 had transcribed the second as
`√(J(W)/r_m)`.  Fourteen concluded that correction 9 mis-transcribed a subscript, and that the
arc's side condition `S ≤ q²·rr` was an artifact of that error.

**⚠ Correction fifteen: correction 9 was not a mis-transcription.**  Display (2) on p. 95 reads

    J(A) ≤ t + √( (2/r_m)·J(W) ) ≤ t + 2·√( (1/n)·J(W) )    if n > N,
    because  n ≤ r_m + 1,  r_m/2 ≥ (r_m/(r_m+1))·(n/2) ≥ (1/2)·(n/2) = n/4.

So **both** forms are the source's: `r_m` is the sharp intermediate — and it is what this arc's
own arithmetic derives, independently — while `n` is the packaged weakening, reached by a
*proved step* using `n ≤ r_m + 1`.  Correction 9 transcribed the sharp form; correction
fourteen read the packaged one and called the other an error.

**What survives.**  Fourteen's operative conclusion — that the side condition can be moved to
the `n` normalisation and collapses there — is right, for a better reason than it gave.  It is
not that `r_m` was wrong; it is that the source supplies the conversion and **this arc already
has its hypothesis**: `RothOperatorFamily`'s `hrle : r ≤ d₂ + 1` is exactly `n ≤ r_m + 1`.
What was missing is the weakening itself, landed below as `radicand_weaken`.

⚠ **The methodological point, which is the part worth keeping.**  Correction fourteen was made
from *one display*, read without the derivation above it.  Correction 9 was made from the
derivation without the packaging below it.  Both were confident; both were partial; each was
the other's blind spot.  Reading a display is not reading a proof — what settles a form is the
*passage between* two displays, and neither correction looked there.

Two things §13's body confirms rather than corrects, both exactly as this arc had them:

* `Φ_m = Θ_{m−1}(b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1}) + Θ₁(b; ρ_m; H_m)` — the **sum of the two
  halves**, which is the arc's `Φ = εU + εV`;
* `J(W) ≤ n·Φ_m` — which is `RothInductionStep.factor_bound_of_rescaled` verbatim, `n` being
  the arc's `r`.

So the junction condition `S ≤ Ψ·rr`, at `rr = r` and `S = r·Φ`, is just `Φ ≤ Ψ`; and since
`Ψ_m = Θ_{m−1} + t` while `Φ_m = Θ_{m−1} + Θ₁`, that is exactly `Θ₁ ≤ t` — which §13 proves
from `Γ_m`.  The "largeness requirement on the split-off degree" was an artifact; getting to
the `n` normalisation that shows it is what `radicand_weaken` supplies. -/

/-- **Mahler's weakening of the radicand**, display (2) on p. 95: `√((2/r_m)·S) ≤ 2·√(S/n)`.

This is the step that carries §13 from its sharp intermediate — radicand `(2/r_m)·S`, which is
also what this arc's own `le_two_mul_max_of_sum_le` derives — to the packaged form with
radicand `S/n`.  The source's chain is
`r_m/2 ≥ (r_m/(r_m+1))·(n/2) ≥ (1/2)·(n/2) = n/4`; all it actually needs is **`n ≤ 2·r_m`**,
which `n ≤ r_m + 1` and `r_m ≥ 1` give at once.

Root-free: `v` stands for the left square root and `w` for `√(S/n)`.

⚠ `hw` is `S/n ≤ w²`, not `S/n = w²` — correction 25.  The `=` form demands that `S/n` be a
square in `ℚ`, which nothing supplies, and only the `≤` direction is used.  `0 ≤ S` was
previously *derived* from the equality and so has to be assumed now; it is free at every call
site (`S` is a bound on an index). -/
theorem radicand_weaken {S rm n v w : ℚ}
    (hn : 0 < n) (hrm : 1 ≤ rm) (hnrm : n ≤ rm + 1) (hS : 0 ≤ S)
    (hv : v ^ 2 ≤ 2 / rm * S) (hw : S / n ≤ w ^ 2) (hw0 : 0 ≤ w) :
    v ≤ 2 * w := by
  have hrm0 : (0 : ℚ) < rm := lt_of_lt_of_le zero_lt_one hrm
  have hdiv : 2 / rm ≤ 4 / n := by
    rw [div_le_div_iff₀ hrm0 hn]
    linarith
  refine le_of_pow_le_pow_left₀ two_ne_zero (by linarith) ?_
  calc v ^ 2 ≤ 2 / rm * S := hv
    _ ≤ 4 / n * S := mul_le_mul_of_nonneg_right hdiv hS
    _ = 4 * (S / n) := by ring
    _ ≤ 4 * w ^ 2 := by linarith
    _ = (2 * w) ^ 2 := by ring

/-- **`Φ ≤ Ψ` reduces to `Θ₁ ≤ t`.**  `Φ_m = Θ' + Θ₁` and `Ψ_m = Θ' + t`, so the two differ
only in the `y`-side term. -/
theorem factor_le_of_theta_one_le {Θ' Θ₁ t : ℚ} (h : Θ₁ ≤ t) : Θ' + Θ₁ ≤ Θ' + t := by linarith

/-- **The junction condition at the source's normalisation** — free, given `Φ ≤ Ψ`.

`S = r·Φ` and `rr = r`, so `S ≤ Ψ·rr` is `r·Φ ≤ Ψ·r`.  No largeness requirement, no condition
on the split-off degree.  Contrast `factor_bound_le_of_split_degree` above, which is what the
mis-transcribed `r_m` cost. -/
theorem le_mul_of_factor_le {Φ Ψ r : ℚ} (hr : 0 ≤ r) (h : Φ ≤ Ψ) : r * Φ ≤ Ψ * r := by
  nlinarith

/-- **§13's discharge of `Θ₁ ≤ t` from `Γ_m`**, with the logarithms carried as variables.

§10 gives `Θ₁(b; ρ_m; H_m) ≤ log b / (ρ_m log H_m)`.  Then `Γ_m` clause 2 — `r_m log H_m ≥
r₁ log H₁`, hence `ρ_m log H_m ≥ ρ₁ log H₁` since `ρ_h = n·r_h` — lets the denominator be
replaced, and §11's `b ≤ H₁^{(1/(m−1))ρ₁t}` bounds the numerator.  What comes out is
`t/(m−1) ≤ t`, using `m ≥ 2`.

⚠ `logb`, `L₁`, `Lm` stand for `log b`, `log H₁`, `log H_m`; nothing here is about logarithms,
only about the inequalities they satisfy.  That keeps the step in `ℚ` and matches how the rest
of this arc handles the height chain.

⚠ **`0 ≤ log b` is not a hypothesis, and the reason is worth naming.**  The source's route
replaces the denominator first — `log b/(ρ_m log H_m) ≤ log b/(ρ₁ log H₁)` — and *that* needs
`log b ≥ 0`.  The proof below never forms that quotient: it bounds `log b` above and multiplies
through, so the positivity never arises.

That is the fourth hypothesis this arc has written down and then found unused (`0 ≤ u`,
`0 ≤ Φ`/`0 ≤ D₂`, `0 ≤ w`, and now this), and all four came from transcribing the *paper's*
proof route rather than the route Lean actually takes.  Worth watching for: the linter is
catching a specific habit, not random slack. -/
theorem theta_one_le_of_gamma {m : ℕ} (hm : 2 ≤ m) {ρ₁ ρm L₁ Lm logb t : ℚ}
    (hpos : 0 < ρ₁ * L₁) (hge : ρ₁ * L₁ ≤ ρm * Lm) (ht : 0 ≤ t)
    (hb : logb ≤ ρ₁ * t * L₁ / ((m : ℚ) - 1)) :
    logb / (ρm * Lm) ≤ t := by
  have hp2 : 0 < ρm * Lm := lt_of_lt_of_le hpos hge
  have hm1 : (1 : ℚ) ≤ (m : ℚ) - 1 := by
    have : (2 : ℚ) ≤ (m : ℚ) := by exact_mod_cast hm
    linarith
  have hnum : (0 : ℚ) ≤ ρ₁ * t * L₁ := by nlinarith
  have h2 : ρ₁ * t * L₁ / ((m : ℚ) - 1) ≤ ρ₁ * t * L₁ := div_le_self hnum hm1
  rw [div_le_iff₀ hp2]
  nlinarith

/-! ### §11's height step — `Γ_m`'s clause 4 descending to `Γ_{m−1}`'s

§11 defines the sub-system's height explicitly:

    b = 2^{2n(r₁+…+r_m)} · n! · a^n,      ρ_h = n·r_h,

and proves `b, ρ₁,…,ρ_{m−1}, H₁,…,H_{m−1}` has `Γ_{m−1}`.  Clause 4 of that is the one part
`rothGamma_descend` cannot get from `Γ_m` alone, since it constrains the *new* height.  Here is
the source's chain, in logs so that everything stays in `ℚ`
(`Λ = log 2`, `L = log H₁`, `A = log a`, `B = log b`):

    n ≤ r_m + 1 ≤ r₁ + 1 ≤ 2^{r₁},  hence  n! ≤ n^n ≤ 2^{n r₁} = 2^{ρ₁};
    a ≤ H₁^{(1/m)r₁t};   r₁ + … + r_m ≤ m r₁;
    therefore  b ≤ 2^{2n·m r₁}·2^{ρ₁}·a^n ≤ 2^{(2m+1)ρ₁}·H₁^{(1/m)ρ₁t} ≤ H₁^{(1/(m−1))ρ₁t}.

Both lemmas below are stated multiplied through by `m` or `m−1`, so no division appears. -/

/-- **The calibration step** — and where `Γ_m`'s clause 3 finally earns its exponent.

⚠ The gap between the two exponents is `1/(m−1) − 1/m = 1/(m(m−1))`, so absorbing the
accumulated `2^{(2m+1)ρ₁}` needs `H₁^{ρ₁t/(m(m−1))} ≥ 2^{(2m+1)ρ₁}`, i.e.

    t·log H₁  ≥  m(m−1)(2m+1)·log 2,

which is clause 3 — `K₁ ≥ 2^{(1/t)(m−1)m(2m+1)}` — with **nothing to spare**.  That is why the
floor's exponent is `(1/t)(m−1)m(2m+1)` and not some rounder constant: `m(m−1)` cancels the
exponent gap and `(2m+1)` matches what `2^{2mρ₁}·2^{ρ₁}` accumulates.

This arc carried clause 3 for several turns without any use for it, and recorded twice that it
was "the first place clauses 2 and 3 have to be used".  This is that place, and the fit is
exact rather than generous. -/
theorem height_descend_step {m : ℕ} (hm : 2 ≤ m) {ρ₁ t L Λ B : ℚ}
    (hρ : 0 ≤ ρ₁)
    (hfloor : ((m : ℚ) - 1) * (m : ℚ) * (2 * (m : ℚ) + 1) * Λ ≤ t * L)
    (hB : (m : ℚ) * B ≤ (m : ℚ) * (2 * (m : ℚ) + 1) * ρ₁ * Λ + ρ₁ * t * L) :
    ((m : ℚ) - 1) * B ≤ ρ₁ * t * L := by
  have hm2 : (2 : ℚ) ≤ (m : ℚ) := by exact_mod_cast hm
  have hM0 : (0 : ℚ) < (m : ℚ) := by linarith
  have hM1 : (0 : ℚ) ≤ (m : ℚ) - 1 := by linarith
  have h1 := mul_le_mul_of_nonneg_left hB hM1
  have h2 := mul_le_mul_of_nonneg_left hfloor hρ
  refine le_of_mul_le_mul_left ?_ hM0
  nlinarith [h1, h2]

/-- **The assembly** — `b = 2^{2n∑r}·n!·a^n` bounded, in logs.

`Fac` stands for `log n!`, bounded by `ρ₁·Λ` through `n! ≤ n^n ≤ 2^{n r₁}`; `sumR` for
`r₁ + … + r_m`, bounded by `m·r₁`; and `A` for `log a`, bounded by clause 4 of `Γ_m`. -/
theorem height_descend_assemble {m : ℕ} {n r₁ ρ₁ sumR t L Λ A Fac B : ℚ}
    (hm2 : (2 : ℚ) ≤ (m : ℚ)) (hn : 0 ≤ n) (hΛ : 0 ≤ Λ) (hρ : ρ₁ = n * r₁)
    (hb : B ≤ 2 * n * sumR * Λ + Fac + n * A)
    (hfacn : Fac ≤ ρ₁ * Λ)
    (hsum : sumR ≤ (m : ℚ) * r₁)
    (ha : (m : ℚ) * A ≤ r₁ * t * L) :
    (m : ℚ) * B ≤ (m : ℚ) * (2 * (m : ℚ) + 1) * ρ₁ * Λ + ρ₁ * t * L := by
  subst hρ
  have hM0 : (0 : ℚ) ≤ (m : ℚ) := by linarith
  nlinarith [mul_le_mul_of_nonneg_left hb hM0,
    mul_le_mul_of_nonneg_left hsum (by positivity : (0 : ℚ) ≤ 2 * n * Λ * (m : ℚ)),
    mul_le_mul_of_nonneg_left ha hn,
    mul_le_mul_of_nonneg_left hfacn hM0]

/-- **Clause 4's multiplicative half, log-free** — the arc's `E : ℕ` idiom rather than logs.

`RothLemmaUniform` already avoids rational exponents by writing the height condition as
`B ≤ qⱼ^E` with `E : ℕ` and `E ≤ ε·dⱼ`.  Clause 4 in that idiom is `a ≤ K^E`, and §11's chain
becomes: `b ≤ 2^c·a^n` with the `2^c` absorbed into `K^j` through clause 3's `2^F ≤ K`.

Everything stays in `ℤ`.  `F` is `rothHeightFloor`'s exponent and `j` the number of powers of
`K` needed to swallow `2^c`; the arithmetic that says `j` is small enough is
`height_descend_step`, in `ℚ`. -/
theorem height_descend_exp {a b K : ℤ} {F j c n E : ℕ}
    (ha0 : 0 ≤ a) (hF : (2 : ℤ) ^ F ≤ K)
    (ha : a ≤ K ^ E) (hb : b ≤ 2 ^ c * a ^ n) (hc : c ≤ F * j) :
    b ≤ K ^ (j + n * E) := by
  have h2F : (0 : ℤ) ≤ 2 ^ F := by positivity
  have hK0 : (0 : ℤ) ≤ K := le_trans h2F hF
  have h1 : (2 : ℤ) ^ c ≤ K ^ j := by
    calc (2 : ℤ) ^ c ≤ 2 ^ (F * j) := pow_le_pow_right₀ (by norm_num) hc
      _ = ((2 : ℤ) ^ F) ^ j := by rw [pow_mul]
      _ ≤ K ^ j := pow_le_pow_left₀ h2F hF j
  have h2 : a ^ n ≤ K ^ (n * E) := by
    calc a ^ n ≤ (K ^ E) ^ n := pow_le_pow_left₀ ha0 ha n
      _ = K ^ (n * E) := by rw [← pow_mul, mul_comm]
  calc b ≤ 2 ^ c * a ^ n := hb
    _ ≤ K ^ j * K ^ (n * E) :=
        mul_le_mul h1 h2 (by positivity) (by positivity)
    _ = K ^ (j + n * E) := by rw [← pow_add]

/-! ### ⚠ Where the two halves of the descent do not meet

`rothGamma_descend` gives clauses 1–3 over `ℕ` degrees and `ℤ` heights;
`height_descend_exp` gives clause 4's multiplicative content over `ℤ`; `height_descend_step`
gives its arithmetic over `ℚ`.  Joining them needs `j` — the number of powers of `K` that
swallow `2^c` — to be a **natural number** lying in

    (2m+1)ρ₁ / F   ≤   j   ≤   ρ₁t / (m(m−1)),

and clause 3 makes those two endpoints *equal* in the tight case (that is what "calibrated with
nothing to spare" means).  An interval of length zero between two non-integers contains no
integer, so no choice of `j` need exist.

⚠ **This is intrinsic to the arc's `E : ℕ` device, not a gap in the source.**  §11 uses real
exponents, where `j` is simply `ρ₁t/(m(m−1))` and no rounding arises.  The arc bought
`ℚ`-only arithmetic by rounding exponents up, and clause 3 is exactly tight, so the rounding
has nowhere to go.

Two ways out: carry real exponents for the height chain alone, or write `t = p/q` and state
clause 4 as `b^{Mq} ≤ K₁^{s₁p}`, which is integral and exact.  **The second is taken** —
`height_descend_pq` below — and it closes with nothing left over, because every inequality in
the chain becomes an `ℕ` one and the tightness that blocks the rounded route costs nothing
there.  `height_descend_exp` above is kept as the rounded form, since it is what the arc's
existing `E : ℕ` idiom produces and the contrast is the point. -/

/-- **Clause 4's descent, integral and exact** — `t = p/q`, so nothing is rounded.

Clause 4 `b ≤ K₁^{(1/M)s₁t}` raised to the power `Mq` is `b^{Mq} ≤ K₁^{s₁p}`, which is a
statement about integers.  Descending from arity `m+1` to `m`, §11's chain becomes a chain of
`ℕ`-exponent inequalities and closes **exactly**, with no interval for `j` to fall out of:

    b^{m(m+1)q} ≤ 2^{c·m(m+1)q}·(a^{(m+1)q})^{nm} ≤ K^{ρ₁p}·K^{ρ₁pm} = (K^{ρ₁p})^{m+1},

the middle step needing `c·m(m+1)q ≤ F·ρ₁p`, which is `c ≤ (2m+3)ρ₁` and clause 3's
`q·m(m+1)(2m+3) ≤ F·p` multiplied together.  Both are `ℕ` inequalities, so the tightness that
blocked the rounded route costs nothing here.

⚠ This is the route the section above recommends and does not take.  It is taken here. -/
theorem height_descend_pq {a b K : ℤ} {m n c F p q r₁ ρ₁ : ℕ}
    (ha0 : 0 ≤ a) (hb0 : 0 ≤ b) (hKF : (2 : ℤ) ^ F ≤ K)
    (hρ : ρ₁ = n * r₁)
    (ha : a ^ ((m + 1) * q) ≤ K ^ (r₁ * p))
    (hb : b ≤ 2 ^ c * a ^ n)
    (hc : c ≤ (2 * m + 3) * ρ₁)
    (hF : q * (m * (m + 1) * (2 * m + 3)) ≤ F * p) :
    b ^ (m * q) ≤ K ^ (ρ₁ * p) := by
  have h2F : (0 : ℤ) ≤ 2 ^ F := by positivity
  have hK0 : (0 : ℤ) ≤ K := le_trans h2F hKF
  have hKp : (0 : ℤ) ≤ K ^ (ρ₁ * p) := by positivity
  have hcN : c * (m * (m + 1) * q) ≤ F * (ρ₁ * p) := by
    calc c * (m * (m + 1) * q) ≤ ((2 * m + 3) * ρ₁) * (m * (m + 1) * q) :=
          Nat.mul_le_mul_right _ hc
      _ = ρ₁ * (q * (m * (m + 1) * (2 * m + 3))) := by ring
      _ ≤ ρ₁ * (F * p) := Nat.mul_le_mul_left _ hF
      _ = F * (ρ₁ * p) := by ring
  have h2 : (2 : ℤ) ^ (c * (m * (m + 1) * q)) ≤ K ^ (ρ₁ * p) := by
    calc (2 : ℤ) ^ (c * (m * (m + 1) * q)) ≤ 2 ^ (F * (ρ₁ * p)) :=
          pow_le_pow_right₀ (by norm_num) hcN
      _ = ((2 : ℤ) ^ F) ^ (ρ₁ * p) := by rw [pow_mul]
      _ ≤ K ^ (ρ₁ * p) := pow_le_pow_left₀ h2F hKF _
  have hA : a ^ (n * (m * (m + 1) * q)) ≤ K ^ (ρ₁ * p * m) := by
    calc a ^ (n * (m * (m + 1) * q)) = (a ^ ((m + 1) * q)) ^ (n * m) := by
          rw [← pow_mul]; congr 1; ring
      _ ≤ (K ^ (r₁ * p)) ^ (n * m) := pow_le_pow_left₀ (by positivity) ha _
      _ = K ^ (ρ₁ * p * m) := by rw [← pow_mul, hρ]; congr 1; ring
  have hstep : (b ^ (m * q)) ^ (m + 1) ≤ (K ^ (ρ₁ * p)) ^ (m + 1) := by
    calc (b ^ (m * q)) ^ (m + 1) = b ^ (m * (m + 1) * q) := by
          rw [← pow_mul]; congr 1; ring
      _ ≤ (2 ^ c * a ^ n) ^ (m * (m + 1) * q) := pow_le_pow_left₀ hb0 hb _
      _ = 2 ^ (c * (m * (m + 1) * q)) * a ^ (n * (m * (m + 1) * q)) := by
          rw [mul_pow, ← pow_mul, ← pow_mul]
      _ ≤ K ^ (ρ₁ * p) * K ^ (ρ₁ * p * m) := mul_le_mul h2 hA (by positivity) hKp
      _ = (K ^ (ρ₁ * p)) ^ (m + 1) := by rw [← pow_add, ← pow_mul]; congr 1; ring
  exact le_of_pow_le_pow_left₀ (Nat.succ_ne_zero m) hKp hstep

/-- **Non-vacuity of the exact descent, at the calibration boundary.**

`a = 1`, `b = 32`, `K = 1024 = 2^10`, `m = n = r₁ = ρ₁ = 1`, `c = 5`, `F = 10`, `p = q = 1`
(so `t = 1`).  ⚠ **Three of the hypotheses hold with equality**: `2^F = K`, `c = (2m+3)ρ₁`, and
`q·m(m+1)(2m+3) = F·p`.  The witness sits exactly where clause 3's calibration puts it, which
is the concrete form of "nothing to spare". -/
theorem height_descend_pq_witness : (32 : ℤ) ^ (1 * 1) ≤ (1024 : ℤ) ^ (1 * 1) :=
  height_descend_pq (a := 1) (b := 32) (K := 1024) (m := 1) (n := 1) (c := 5)
    (F := 10) (p := 1) (q := 1) (r₁ := 1) (ρ₁ := 1)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num)

/-- **Non-vacuity of the height step.**  `m = 2`, `ρ₁ = 1`, `Λ = 1`, `t = 1`, `L = 30`,
`B = 15`: clause 3 reads `1·2·5·1 = 10 ≤ 30` and the conclusion `1·15 ≤ 30`.

⚠ `L = 30` against `Λ = 1` is not slack — at `m = 2` clause 3 demands `H₁ ≥ 2^{10}`, and
`rothHeightFloor_two` says the same.  The witness is at the boundary of what `Γ₂` allows. -/
theorem height_descend_step_witness : (((2 : ℕ) : ℚ) - 1) * 1 ≤ (1 : ℚ) * 1 * 30 :=
  height_descend_step (m := 2) le_rfl (ρ₁ := 1) (t := 1) (L := 30) (Λ := 1) (B := 1)
    (by norm_num) (by norm_num) (by norm_num)

/-- **Non-vacuity of the junction.**  `m = 1`, `s = 1/4`, `Ψ = 1/8`, `t = 1/16`, `A = q = 1/4`,
`θ = 1/16 + 1/2 = 9/16`; the conclusion is `RothBound 2 (1/16) (9/16)`, a real bound. -/
theorem rothBound_of_max_form_witness : RothBound 2 ((1 / 4 : ℚ) ^ (2 ^ 1)) (9 / 16) :=
  rothBound_of_max_form (m := 1) (s := 1 / 4) (t := 1 / 16) (A := 1 / 4) (q := 1 / 4)
    (Ψ := 1 / 8) le_rfl (by norm_num) (by norm_num) (by norm_num)
    (by norm_num [rothConstant_one]) (by norm_num) (by norm_num) (by norm_num) (by norm_num)


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
its own overstates what it says.

⚠⚠ **Correction eighteen, second consequence: the point and `Γ`'s parameter are different
objects.**  This `def` used to quantify one function `qd : σ → ℤ` and use it *both* as the
denominator of the point (`index d (fun j => pn j / qd j)`, `IsCoprime (pn j) (qd j)`) **and**
as `Γ_m`'s `K_h` (`RothGamma o ω d qd`, `B ≤ qd j ^ E`).  §11 says `K_h = H_h = max(|P_h|,|Q_h|)`,
and `H ≥ Q` with equality only when the denominator dominates, so the two readings are not
interchangeable.

The old form was **not false** — it is a theorem with a *stronger* hypothesis (`B ≤ Q^E`
implies `B ≤ H^E`) and hence a weaker statement.  What it could not be is *fed from `Γ_m`*,
which supplies only `B ≤ H^E`.  Since the induction consumes this schema at `m − 1` and `Γ`
is what the induction carries, the old form was unusable at exactly the point of use.

Now: the point is a rational `κ : σ → ℚ` (Lean's `ℚ` supplies lowest terms and a positive
denominator, so no coprimality clause is needed — §9 states one and the type carries it), and
`Kh` is pinned to its **height** by the second hypothesis.  Compare `InRothFracSet`, which
took the same shape after correction sixteen.

⚠ The `m = 1` proof now goes through `index_le_of_abs_coeff_le` rather than
`index_le_of_abs_leadingCoeff_le` — i.e. through **both** halves of §10.  It has to: the
`Q^j` half alone cannot bound `B` by a power of the *height*. -/
def RothLemmaUniform (σ : Type*) (m : ℕ) (ω ε θ : ℚ) : Prop :=
  ∀ (o : σ ≃ Fin m) (d : σ → ℕ) (κ : σ → ℚ) (Kh : σ → ℤ) (P : MvPolynomial σ ℤ) (B : ℤ) (E : ℕ),
    (∀ j, d j ≠ 0) →
    (∀ j, max |(κ j).num| |(((κ j).den : ℤ))| = Kh j) →
    RothGamma o ω d Kh →
    P ≠ 0 →
    (∀ j, degreeOf j P ≤ d j) →
    (∀ n, |coeff n P| ≤ B) →
    (∀ j, 2 ≤ Kh j) →
    (∀ j, B ≤ Kh j ^ E) →
    (∀ j, (E : ℚ) ≤ ε * (d j : ℚ)) →
    index d κ (map (algebraMap ℤ ℚ) P) ≤ ((θ : ℚ) : WithTop ℚ)

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

All three of `Γ_m`'s clauses are carried, via `RothGamma` inside the schema.  They were not,
for most of this arc's life, which made its statements **stronger** than what §14 proves — a
theorem stronger than the source's is one nothing in the source will discharge.

⚠ `0 < t ≤ 1` is Theorem 1's opening hypothesis and was missing here until §14 was read in
full; §14's computation uses it twice (`s² ≤ s` and `t ≤ s`).  Carried now. -/
def RothLemmaMahler (σ : Type*) (m : ℕ) (t : ℚ) : Prop :=
  0 < t → t ≤ 1 →
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
  rintro o d κ Kh P B E hd hheight - hP - hB hq hBq hE
  have hd0 : d () ≠ 0 := hd ()
  have hdQ : (0 : ℚ) < (d () : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hd0
  set P' : Polynomial ℤ := pUnitAlgEquiv ℤ P with hP'
  have hP'0 : P' ≠ 0 := fun h => hP ((pUnitAlgEquiv ℤ).injective (h.trans (map_zero _).symm))
  have hcoeff : ∀ n, |P'.coeff n| ≤ B := by
    intro n
    rw [hP', coeff_pUnitAlgEquiv]
    exact hB _
  have hq0 : (0 : ℤ) < (((κ ()).den : ℤ)) := by exact_mod_cast (κ ()).pos
  have hco : IsCoprime ((κ ()).num) (((κ ()).den : ℤ)) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    simpa [Int.gcd] using (κ ()).reduced
  have hmain := index_le_of_abs_coeff_le hq0 hco hd0 hP'0 E (a := B)
    (by rw [hheight ()]; exact hq ()) hcoeff (by rw [hheight ()]; exact hBq ())
  rw [hP', symm_map_pUnitAlgEquiv] at hmain
  have hdfun : (fun _ : Unit => d ()) = d := by
    refine _root_.funext fun u => ?_; cases u; rfl
  have hafun : (fun _ : Unit => (((κ ()).num : ℚ) / ((((κ ()).den : ℤ)) : ℚ))) = κ := by
    refine _root_.funext fun u => ?_
    cases u
    push_cast
    exact Rat.num_div_den _
  rw [hdfun, hafun] at hmain
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
theorem rothLemmaMahler_one {t : ℚ} : RothLemmaMahler Unit 1 t := fun ht _ =>
  ⟨t, (rothBound_one t t).mpr ⟨ht.le, le_rfl⟩, rothLemmaUniform_one _ _ _ (by simp)⟩

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
    (fun _ => 1) (fun _ => ((1 : ℤ) : ℚ) / ((2 : ℤ) : ℚ)) (fun _ => 2) 1 1 0
    (fun _ => one_ne_zero) ?_ ?_ one_ne_zero ?_ ?_ ?_ ?_ ?_
  · intro j
    norm_num
  · exact
      { growth := by intro j k hjk; omega
        height := by intro j k _; exact le_rfl
        floor := by intro j _; rw [rothHeightFloor_one]; norm_num }
  · intro j
    have h : degreeOf j (1 : MvPolynomial Unit ℤ) = 0 := by
      rw [← C_1]; exact degreeOf_C _ _
    omega
  · intro n; rw [coeff_one]; split_ifs <;> simp
  · intro j; norm_num
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
