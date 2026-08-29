/-
  **The variable split** — `σ ≃ Fin n ⊕ Unit` from an ordering `σ ≃ Fin (n+1)`, and the
  transport of `index`, `RothGrowth` and `degreeOf` across it.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/RothOperatorFamily.lean` and through it the rest
  of the arc.

  ═══ WHY THIS EXISTS ═══

  Roth's lemma's statement (`RothLemmaUniform`) carries an ordering `o : σ ≃ Fin m` and one
  degree vector `d : σ → ℕ`.  Its induction step splits off the *last* variable in that
  ordering, and every theorem in `RothOperatorFamily` is written for the split form
  `σ' ⊕ Unit`.  Nothing connected the two.

  ⚠ This is the second time the indexing choice has cost real work, and it is worth setting
  against **correction 7**, which called `Fin m` transport "pure overhead" on the strength of
  `index_rename_equiv` being three lines.  That lemma *is* three lines; what it does not do is
  produce the split, transport the growth condition, or line up `degreeOf`.  The correction was
  right that transport is not deep and wrong that it is free.

  ═══ WHAT IS HERE, AND WHAT IS NOT ═══

  Here: the equivalence, its computation rules, and the transport of the three things the step
  needs.  `index_le_of_rothGrowth_split` applies §13's conclusion to a polynomial presented in
  `o : σ ≃ Fin (n+1)` form.

  ⚠ **Not** here: the integrality step.  The induction hypothesis is about polynomials with
  *integer* coefficients, and the Wronskians it is applied to are rational combinations —
  Gauss's lemma (§6, `RothHeightBound`) is what fixes that, and it is not wired in.  So
  `hres` below remains a hypothesis and this module does not discharge it.
-/
import QOU.Mathlib.RothOperatorFamily
import QOU.Mathlib.RothInductionHypothesis

namespace MvPolynomial

variable {σ : Type*} {R : Type*} [CommRing R]

/-! ### The equivalence -/

/-- `Fin (n+1) ≃ Fin n ⊕ Unit`, sending `Fin.last` to the `Unit` component. -/
def splitLast (n : ℕ) : Fin (n + 1) ≃ Fin n ⊕ Unit :=
  finSuccEquivLast.trans (Equiv.optionEquivSumPUnit.{0} (Fin n))

@[simp] theorem splitLast_castSucc {n : ℕ} (i : Fin n) :
    splitLast n i.castSucc = Sum.inl i := by
  simp [splitLast]

@[simp] theorem splitLast_last (n : ℕ) : splitLast n (Fin.last n) = Sum.inr () := by
  simp [splitLast]

@[simp] theorem splitLast_symm_inl {n : ℕ} (i : Fin n) :
    (splitLast n).symm (Sum.inl i) = i.castSucc := by
  simp [splitLast]

@[simp] theorem splitLast_symm_inr (n : ℕ) :
    (splitLast n).symm (Sum.inr ()) = Fin.last n := by
  simp [splitLast]

/-- The variable equivalence an ordering induces: the last variable becomes the `Unit`
component, and every other variable keeps its position. -/
def splitOrder {n : ℕ} (o : σ ≃ Fin (n + 1)) : σ ≃ Fin n ⊕ Unit :=
  o.trans (splitLast n)

theorem splitOrder_symm_apply {n : ℕ} (o : σ ≃ Fin (n + 1)) (x : Fin (n + 1)) :
    (splitOrder o).symm (splitLast n x) = o.symm x := by
  have h : splitLast n x = splitOrder o (o.symm x) := by
    rw [splitOrder, Equiv.trans_apply, Equiv.apply_symm_apply]
  rw [h, Equiv.symm_apply_apply]

/-- The split-off variable: the last one in the ordering. -/
theorem splitOrder_symm_inr {n : ℕ} (o : σ ≃ Fin (n + 1)) :
    (splitOrder o).symm (Sum.inr ()) = o.symm (Fin.last n) := by
  rw [← splitLast_last n, splitOrder_symm_apply]

/-! ### Transport

A function on `σ` becomes a `Sum.elim` on the split, and everything else follows from that
one rewriting. -/

/-- The left half of a `σ`-indexed function, read through the split. -/
def splitLeft {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) : Fin n → β :=
  fun j => f ((splitOrder o).symm (Sum.inl j))

/-- The right half — a one-element family, the split-off variable. -/
def splitRight {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) : Unit → β :=
  fun u => f ((splitOrder o).symm (Sum.inr u))

theorem split_eq {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) :
    f ∘ (splitOrder o).symm = Sum.elim (splitLeft o f) (splitRight o f) := by
  funext x
  cases x <;> rfl

@[simp] theorem splitRight_unit {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) :
    splitRight o f () = f (o.symm (Fin.last n)) := by
  rw [splitRight, splitOrder_symm_inr]

/-- **The index, transported.**  One rewriting of `index_rename_equiv`. -/
theorem index_splitOrder [DecidableEq σ] {n : ℕ} (o : σ ≃ Fin (n + 1)) (d : σ → ℕ)
    (α : σ → R) (P : MvPolynomial σ R) :
    index d α P
      = index (Sum.elim (splitLeft o d) (splitRight o d))
          (Sum.elim (splitLeft o α) (splitRight o α)) (rename (splitOrder o) P) := by
  rw [index_rename_equiv (splitOrder o).symm d α P, Equiv.symm_symm, split_eq, split_eq]

/-- **The growth condition, transported.** -/
theorem rothGrowth_splitOrder {n : ℕ} (o : σ ≃ Fin (n + 1)) (ω : ℚ) (d : σ → ℕ)
    (hg : RothGrowth o ω d) :
    RothGrowth (splitLast n).symm ω (Sum.elim (splitLeft o d) (splitRight o d)) := by
  have hD : ∀ x : Fin (n + 1),
      Sum.elim (splitLeft o d) (splitRight o d) (splitLast n x) = d (o.symm x) := by
    intro x
    rw [← split_eq]
    exact congrArg d (splitOrder_symm_apply o x)
  intro j k hjk
  rw [Equiv.symm_symm, hD, hD]
  exact hg j k hjk

/-- `splitLeft` in terms of the original ordering: position `j` of `Fin n` is position `j` of
`Fin (n+1)`. -/
@[simp] theorem splitLeft_apply {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β)
    (j : Fin n) : splitLeft o f j = f (o.symm j.castSucc) := by
  rw [splitLeft, splitOrder, Equiv.symm_trans_apply, splitLast_symm_inl]

/-- **`Γ_m` descends to `Γ_{m−1}` on the sub-system** — the piece Lemma 4 asserts exists.

Lemma 4 does not merely conclude an inequality: it produces an ordered system
`b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1}` **with property `Γ_{m−1}`**, and that is what lets the
induction apply its hypothesis at all.  Nothing in this arc supplied it until now — the gap
went unnoticed because every earlier step consumed `Γ_m` and none had to *produce* one.

The sub-system is §13's: the first `m−1` variables, degrees rescaled by `n` (`ρ_h = n·r_h`,
read off §13's body), **heights unchanged** — §13 descends to `b, ρ₁,…,ρ_{m−1}, H₁,…,H_{m−1}`,
the same `H` truncated by one.  All three clauses come across:

* **growth** — restricting the consecutive-pair condition to a prefix loses nothing, and the
  rescaling is `rothGrowth_scale`'s;
* **height** — clause 2 compares every `h` against `h = 1`, so a prefix keeps its own first
  element; raising to the `r`-th power is monotone once `2 ≤ qⱼ`;
* **floor** — `rothHeightFloor` is monotone in the arity, so the *larger* floor `Γ_m` supplies
  implies the smaller one `Γ_{m−1}` asks for.

⚠ Only the arity moves.  `ω` is the same `t⁻¹` throughout, which is what makes this a
single-parameter induction — and is why `rothHeightFloor_mono` needs no hypothesis relating two
different `ω`s.

⚠⚠ **This produces clauses 1–3 and *not* clause 4**, and that is where the remaining work is.
`Γ_M`'s fourth clause is `b ≤ K₁^{(1/M)s₁t}` — a bound on the sub-system's **new height** `b`,
which is the Wronskian's.  Nothing about `Γ_m` can supply it: `Γ_m` constrains `a`, the
*original* height, and `b` is a different number that §13 has to estimate.

That relocates what this arc had been calling "the height chain, which
`theta_one_le_of_gamma` consumes".  It is not a lemma feeding that theorem — it is
`Γ_{m−1}`'s own clause 4, and `theta_one_le_of_gamma` consumes it *because* the sub-system
has `Γ_{m−1}`.  So the open item is: **produce clause 4 for the Wronskian**, which is
`WronskianHeight`'s business and the one genuinely unbuilt piece left. -/
theorem rothGamma_descend {n : ℕ} (o : σ ≃ Fin (n + 1)) (ω : ℚ) (hω : 0 ≤ ω)
    (d : σ → ℕ) (Kh : σ → ℤ) {r : ℕ} (hr : r ≠ 0) (hq : ∀ j, 2 ≤ Kh j)
    (hg : RothGamma o ω d Kh) :
    RothGamma (Equiv.refl (Fin n)) ω (fun k => r * splitLeft o d k) (splitLeft o Kh) where
  growth := by
    intro j k hjk
    have h := hg.growth j.castSucc k.castSucc (by simpa using hjk)
    have hrQ : (0 : ℚ) < (r : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hr
    simp only [Equiv.refl_symm, Equiv.refl_apply, splitLeft_apply] at *
    push_cast at *
    nlinarith
  height := by
    intro j k hj
    have h := hg.height j.castSucc k.castSucc (by simpa using hj)
    have h0 : (0 : ℤ) ≤ Kh (o.symm j.castSucc) ^ d (o.symm j.castSucc) :=
      pow_nonneg (le_trans (by norm_num) (hq _)) _
    simp only [Equiv.refl_symm, Equiv.refl_apply, splitLeft_apply]
    calc Kh (o.symm j.castSucc) ^ (r * d (o.symm j.castSucc))
        = (Kh (o.symm j.castSucc) ^ d (o.symm j.castSucc)) ^ r := by rw [← pow_mul, mul_comm]
      _ ≤ (Kh (o.symm k.castSucc) ^ d (o.symm k.castSucc)) ^ r := pow_le_pow_left₀ h0 h r
      _ = Kh (o.symm k.castSucc) ^ (r * d (o.symm k.castSucc)) := by rw [← pow_mul, mul_comm]
  floor := by
    intro j hj
    have h := hg.floor j.castSucc (by simpa using hj)
    simp only [Equiv.refl_symm, Equiv.refl_apply, splitLeft_apply]
    refine le_trans ?_ h
    exact_mod_cast rothHeightFloor_mono hω (Nat.le_succ n)

/-- **§11's descent lemma, in full** — all four clauses of `Γ_{m}` from `Γ_{m+1}`.

This is what Lemma 4 asserts exists and what `rothGamma_descend` supplies only three quarters
of.  The sub-system is §11's: first `n` variables, degrees rescaled by `r` (`ρ_h = r·s_h`),
heights unchanged, and the new coefficient bound `b` bounded by `2^c·a^r` — which is
`b = 2^{2r∑s}·r!·a^r` with `c` absorbing the first two factors.

Where each clause comes from:

* **1–3** as in `rothGamma_descend`; clause 3a is now a `ℕ` inequality and descends by
  monotonicity of `q·(M−1)M(2M+1)` in `M`, with no ceiling in the way.
* **4** is `height_descend_pq`, and its hypothesis `hF` is *literally* `Γ_{n+1}`'s `floorExp`:
  `q·((n+1−1)(n+1)(2(n+1)+1)) = q·(n(n+1)(2n+3))`.  The two were derived independently — one
  from §11's height chain, one from §11's floor clause — and they are the same inequality.

⚠ `hc : c ≤ (2n+3)·(r·s₁)` is the one hypothesis about the *construction* rather than about
`Γ`: it says the accumulated `2`-power in `b` is what §11 says it is.  Discharging it is
`WronskianHeight`'s business. -/
theorem rothGammaFull_descend {n : ℕ} (o : σ ≃ Fin (n + 1)) (p q F : ℕ)
    (d : σ → ℕ) (Kh : σ → ℤ) (a b : ℤ) {r c : ℕ} (hr : r ≠ 0)
    (ha0 : 0 ≤ a) (hb0 : 0 ≤ b)
    (hg : RothGammaFull o p q F d Kh a)
    (hb : b ≤ 2 ^ c * a ^ r)
    (hc : ∀ j : Fin (n + 1), (j : ℕ) = 0 → c ≤ (2 * n + 3) * (r * d (o.symm j))) :
    RothGammaFull (Equiv.refl (Fin n)) p q F
      (fun k => r * splitLeft o d k) (splitLeft o Kh) b where
  growth := by
    intro j k hjk
    have h := hg.growth j.castSucc k.castSucc (by simpa using hjk)
    have hrQ : (0 : ℚ) < (r : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hr
    simp only [Equiv.refl_symm, Equiv.refl_apply, splitLeft_apply] at *
    push_cast at *
    nlinarith
  height := by
    intro j k hj
    have h := hg.height j.castSucc k.castSucc (by simpa using hj)
    have h0 : (0 : ℤ) ≤ Kh (o.symm j.castSucc) ^ d (o.symm j.castSucc) :=
      pow_nonneg (le_trans (by norm_num) (hg.two_le _)) _
    simp only [Equiv.refl_symm, Equiv.refl_apply, splitLeft_apply]
    calc Kh (o.symm j.castSucc) ^ (r * d (o.symm j.castSucc))
        = (Kh (o.symm j.castSucc) ^ d (o.symm j.castSucc)) ^ r := by rw [← pow_mul, mul_comm]
      _ ≤ (Kh (o.symm k.castSucc) ^ d (o.symm k.castSucc)) ^ r := pow_le_pow_left₀ h0 h r
      _ = Kh (o.symm k.castSucc) ^ (r * d (o.symm k.castSucc)) := by rw [← pow_mul, mul_comm]
  floorExp := by
    have h := hg.floorExp
    have hmono : q * ((n - 1) * n * (2 * n + 1)) ≤ q * (n * (n + 1) * (2 * n + 3)) :=
      Nat.mul_le_mul_left _ (Nat.mul_le_mul (Nat.mul_le_mul (Nat.sub_le _ _) (Nat.le_succ n))
        (by omega))
    have hsimp : (n + 1 - 1) * (n + 1) * (2 * (n + 1) + 1) = n * (n + 1) * (2 * n + 3) := by
      simp only [Nat.add_sub_cancel]; ring
    rw [hsimp] at h
    exact le_trans hmono h
  floor := by
    intro j hj
    have h := hg.floor j.castSucc (by simpa using hj)
    simpa using h
  heightBound := by
    intro j hj
    have hjc : (j.castSucc : ℕ) = 0 := by simpa using hj
    have ha := hg.heightBound j.castSucc hjc
    have hK := hg.floor j.castSucc hjc
    have hFe := hg.floorExp
    have hsimp : (n + 1 - 1) * (n + 1) * (2 * (n + 1) + 1) = n * (n + 1) * (2 * n + 3) := by
      simp only [Nat.add_sub_cancel]; ring
    rw [hsimp] at hFe
    simp only [Equiv.refl_symm, Equiv.refl_apply, splitLeft_apply]
    exact height_descend_pq ha0 hb0 hK rfl ha hb (hc j.castSucc hjc) hFe
  two_le := fun j => by simpa [splitLeft] using hg.two_le _
  degPos := fun k => Nat.mul_ne_zero hr (hg.degPos _)

/-- **§13's `Θ₁ ≤ t` for the split-off variable** — the `y` side of `Φ_m ≤ Ψ_m`.

§13 needs `Φ_m = Θ_{m−1} + Θ₁ ≤ Θ_{m−1} + t = Ψ_m`, i.e. `Θ₁ ≤ t` for the *one-variable*
system carrying the split-off degree.  `isRothTheta_le_of_gamma_one` turns §11's case (i) into
exactly that, so all this has to do is produce case (i)'s clause `b^q ≤ K_M^{(r₀·d_M)·p}` for
the **last** variable, where `rothGammaFull_descend` produced it for the first.

That direction is the easy one, and for a reason worth naming: clause 2 says the *first*
variable's `K^d` is the **smallest**, so the last variable's clause is implied by the first's.
Raising `K_1^{d_1} ≤ K_M^{d_M}` to `r₀·p` and prefixing `b^q ≤ b^{n·q}` closes it.

⚠ `1 ≤ n` is used twice and both times essentially: for `q ≤ n·q`, and because at `n = 0` the
descended system has no first variable to read clause 4 off.  §13 assumes `m ≥ 2`, which is
`n ≥ 1` here — the same hypothesis correction 22 had to add to `RothLemma4` for a different
reason. -/
theorem isRothTheta_right_le_t {n : ℕ} (hn : 1 ≤ n) (o : σ ≃ Fin (n + 1)) {p q F : ℕ}
    (hq : q ≠ 0) {d H : σ → ℕ} {a b : ℤ} {r₀ : ℕ} (hr₀ : r₀ ≠ 0) (hb1 : 1 ≤ b)
    (hg : RothGammaFull o p q F d (fun j => (H j : ℤ)) a)
    (hdesc : RothGammaFull (Equiv.refl (Fin n)) p q F (fun k => r₀ * splitLeft o d k)
        (splitLeft o (fun j => (H j : ℤ))) b)
    {Θ₁ : ℚ}
    (hΘ₁ : IsRothTheta b (fun _ : Unit => r₀ * splitRight o d ()) (splitRight o H) Θ₁) :
    Θ₁ ≤ (p : ℚ) / (q : ℚ) := by
  classical
  have hn0 : 0 < n := hn
  have hHB := hdesc.heightBound (⟨0, hn0⟩ : Fin n) rfl
  simp only [Equiv.refl_symm, Equiv.refl_apply, splitLeft_apply] at hHB
  have hht := hg.height ((⟨0, hn0⟩ : Fin n).castSucc) (Fin.last n) rfl
  have hL0 : (0 : ℤ) ≤ (H (o.symm ((⟨0, hn0⟩ : Fin n).castSucc)) : ℤ)
      ^ d (o.symm ((⟨0, hn0⟩ : Fin n).castSucc)) :=
    pow_nonneg (by exact_mod_cast Nat.zero_le _) _
  have hstep1 : b ^ q ≤ b ^ (n * q) :=
    pow_le_pow_right₀ hb1 (Nat.le_mul_of_pos_left q hn0)
  have hstep2 : ((H (o.symm ((⟨0, hn0⟩ : Fin n).castSucc)) : ℤ))
        ^ (r₀ * d (o.symm ((⟨0, hn0⟩ : Fin n).castSucc)) * p)
      ≤ ((H (o.symm (Fin.last n)) : ℤ)) ^ (r₀ * d (o.symm (Fin.last n)) * p) := by
    calc ((H (o.symm ((⟨0, hn0⟩ : Fin n).castSucc)) : ℤ))
          ^ (r₀ * d (o.symm ((⟨0, hn0⟩ : Fin n).castSucc)) * p)
        = ((H (o.symm ((⟨0, hn0⟩ : Fin n).castSucc)) : ℤ)
            ^ d (o.symm ((⟨0, hn0⟩ : Fin n).castSucc))) ^ (r₀ * p) := by
          rw [← pow_mul]; congr 1; ring
      _ ≤ ((H (o.symm (Fin.last n)) : ℤ) ^ d (o.symm (Fin.last n))) ^ (r₀ * p) :=
          pow_le_pow_left₀ hL0 hht _
      _ = ((H (o.symm (Fin.last n)) : ℤ)) ^ (r₀ * d (o.symm (Fin.last n)) * p) := by
          rw [← pow_mul]; congr 1; ring
  have hclause : b ^ q
      ≤ ((splitRight o H () : ℕ) : ℤ) ^ ((r₀ * splitRight o d ()) * p) := by
    rw [splitRight_unit, splitRight_unit]
    exact le_trans hstep1 (le_trans hHB hstep2)
  refine isRothTheta_le_of_gamma_one hΘ₁ ?_ hq ?_ hclause
  · exact Nat.mul_ne_zero hr₀ (by rw [splitRight_unit]; exact hg.degPos _)
  · have := hg.two_le (o.symm (Fin.last n))
    rw [splitRight_unit]
    exact_mod_cast this


/-! ### Lemma 4 and Roth's Lemma, in `Θ_m` form

Every statement in this arc so far bounds the index of one polynomial.  With `Θ_m` characterised
and known to exist, the source's own two statements can finally be written.

**Lemma 4** (§13, read verbatim): let `m ≥ 2` and let `a; r₁,…,r_m; H₁,…,H_m` have property
`Γ_m`.  Then there exists a system `b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1}` with `Γ_{m−1}` such that
`Θ_m ≤ t + 2·max(Ψ_m, √Ψ_m)` where `Ψ_m = Θ_{m−1} + t`.

**Roth's Lemma** (§14): if the system has `Γ_m` then `Θ_m ≤ c_m·t^{2^{−(m−1)}}`.

⚠ Both are `def`s, and **both are now proved**: `RothLemma4` at every arity `n ≥ 1`
(`rothLemma4_of_one_le`, below — it needs `exists_family_index_le_w_of_rothGrowth_split`, so it
is stated after it), and `RothLemmaTheta` at `m = 1` outright (`rothLemmaTheta_one`) and at
every `m ≤ M` for which the `s`-ladder exists in `ℚ` (`rothLemmaTheta_of_seq`).  The implication
between them is `rothBound_succ_of_lemma4`, §14's induction step in `Θ` language.

Correction 23's encoding restriction survives in `rothLemmaTheta_of_seq` — `t` has to be a
`2^{M−1}`-th power in `ℚ` — and is **removed** in `QOU/Mathlib/RothRealLadder.lean`, whose
`rothLemmaTheta_all` holds at every arity with no hypothesis.  What is kept here is the `ℝ`-free
route; `rothLemmaTheta_three` is a self-contained instance of it.

⚠ This paragraph has now been wrong **three times**, in three different directions: it read
"neither is proved" after `rothLemmaTheta_one` landed (correction 17), then "`RothLemma4` is not
proved at any arity" after `rothLemma4_of_one_le` landed, and each time the build had no
opinion.  A docstring that names what is open is a *claim about the whole file* and ages the
moment anything below it changes; nothing mechanical checks it, so it has to be re-read on every
landing that could falsify it. -/

/-- **Lemma 4**, stated.  `w` encodes `max(Ψ, √Ψ)` root-free as `w ≤ Ψ ∨ w² ≤ Ψ`.

⚠⚠ **Correction twenty-five: the disjuncts were `=`, and that made this `def` unsatisfiable.**
The admissible `w` under `=` are `Ψ` and — only when `Ψ` is a square in `ℚ` — `±√Ψ`, so in the
regime where the `√` branch is the operative one (`Ψ < 1`, which is the regime §14 runs in) the
statement demands a rational square root of `Θ' + t` that nothing produces.  Under `≤` the
admissible `w` are exactly `w ≤ max(Ψ, √Ψ)`, so this existential says precisely what §13 says,
and `w := max(0, (Θ − t)/2)` is the witness §13's second branch hands over.

⚠ The consumers never needed the equality: `rothConstant_step_lemma4` uses `w ≤ Ψ` and
`w² ≤ Ψ`, and `radicand_weaken` uses `S/n ≤ w²`.  So the `=` was strictly a tax on the
producer, and it went unpaid for as long as nothing tried to produce one — correction 9's
lesson again.
⚠⚠ **Correction twenty-two: checked against correction twenty, and it was defective.**

Correction twenty's *first* half — `K₁ ≥ 2` — is fixed for free by `RothGammaFull`'s new `two_le`
clause.  The *second* half is not, and it bites here at `n = 0` (arity `1`, where the source's
Lemma 4 does not apply at all — §13 assumes `m ≥ 2`).

At `n = 0` the sub-problem lives on `Fin 0`, where every index is `0` — `idxWeight` sums over an
empty support — so `IsRothTheta b ρ H' Θ'` forces `Θ' = 0` (and `b ≥ 1`, else `R(b;ρ)` is empty
and the attainment clause fails).  Then `w = Θ' + t = t` or `w² = t`.  With `q = 0` Lean's `ℚ`
makes `t = p/0 = 0`, so `w = 0` and the conclusion demands `Θ ≤ 0`.  But:

    σ = Unit, n = 0, p = 1, q = 0, F = 0, a = 100, r ≡ 1, H ≡ 2

satisfies every `RothGammaFull` clause — `growth` vacuous at one variable, `height` `2 ≤ 2`,
`floorExp` `0 ≤ 0`, `floor` `2⁰ = 1 ≤ 2`, `heightBound` `100^0 = 1 ≤ 2¹`, `two_le` `2 ≤ 2`,
`degPos` `1 ≠ 0` — while `Θ = 1`, attained at `A = 2x − 1`, `κ = 1/2` (height `max(1,2) = 2`),
whose translate is `2x`.  So `1 ≤ 0` is demanded.

Fixed the same way as `RothLemmaTheta`: carry §14's opening `0 < t ≤ 1`.  With `q ≥ p ≥ 1` the
`n = 0` case then asks only `Θ ≤ 3t`, which `rothLemmaTheta_one`'s `Θ ≤ t` supplies. -/
def RothLemma4 (σ : Type*) (n p q F : ℕ) : Prop :=
  0 < p → p ≤ q →
  ∀ (o : σ ≃ Fin (n + 1)) (a : ℤ) (r H : σ → ℕ) (Θ : ℚ),
    RothGammaFull o p q F r (fun j => (H j : ℤ)) a →
    IsRothTheta a r H Θ →
    ∃ (b : ℤ) (ρ H' : Fin n → ℕ) (Θ' w : ℚ),
      RothGammaFull (Equiv.refl (Fin n)) p q F ρ (fun j => (H' j : ℤ)) b ∧
      IsRothTheta b ρ H' Θ' ∧
      (w ≤ Θ' + (p : ℚ) / (q : ℚ) ∨ w ^ 2 ≤ Θ' + (p : ℚ) / (q : ℚ)) ∧
      Θ ≤ (p : ℚ) / (q : ℚ) + 2 * w

/-- **`1/2` is not a square in `ℚ`** — elementary, via denominators.

`(w²).den = w.den²` and `(1/2).den = 2`, so a solution would need a natural number whose
square is `2`.  No analysis, no irrationality file: this is the whole obstruction correction 25
is about, and it is visible entirely inside `ℚ`. -/
theorem not_isSquare_half : ¬ ∃ w : ℚ, w ^ 2 = 1 / 2 := by
  rintro ⟨w, hw⟩
  have hden : (w ^ 2).den = w.den ^ 2 := Rat.den_pow w 2
  rw [hw] at hden
  have h2 : ((1 : ℚ) / 2).den = 2 := by norm_num
  rw [h2] at hden
  have hle : w.den ≤ 2 := by nlinarith [w.den.zero_le, hden]
  interval_cases h : w.den <;> omega

/-- **Correction 25, made concrete** — §13's conclusion holds at numbers the `=` encoding of
`max(Ψ, √Ψ)` cannot express, and the `≤` encoding expresses exactly.

Take `Ψ = 1/2`, `t = 0`, `Θ = 7/5`.  §13's second branch is `(Θ − t)² ≤ 4Ψ`, and here that is
`49/25 ≤ 2` — true, so this is a situation §13 genuinely produces (it is the literal shape
`RothInductionStep.index_le_or_sq_of_det_bound` hands back).  Then:

* **no** rational `w` has `w = Ψ ∨ w² = Ψ` together with `Θ ≤ t + 2w` — the first disjunct
  gives `t + 2w = 1 < 7/5`, and the second asks for a rational square root of `1/2`;
* `w = 7/10` has `w² = 49/100 ≤ 1/2` and `Θ ≤ t + 2w` with equality.

So the change from `=` to `≤` is not a loosening of Lemma 4 — it is the difference between a
statement Lemma 4 can prove and one it cannot. -/
theorem lemma4_le_encoding_needed :
    ((7 : ℚ) / 5 - 0) ^ 2 ≤ 4 * (1 / 2)
      ∧ (¬ ∃ w : ℚ, (w = 1 / 2 ∨ w ^ 2 = 1 / 2) ∧ (7 : ℚ) / 5 ≤ 0 + 2 * w)
      ∧ ∃ w : ℚ, (w ≤ 1 / 2 ∨ w ^ 2 ≤ 1 / 2) ∧ (7 : ℚ) / 5 ≤ 0 + 2 * w := by
  refine ⟨by norm_num, ?_, ⟨7 / 10, Or.inr (by norm_num), by norm_num⟩⟩
  rintro ⟨w, hw | hw, hθ⟩
  · rw [hw] at hθ; norm_num at hθ
  · exact not_isSquare_half ⟨w, hw⟩

/-- **Roth's Lemma**, stated in `Θ_m` form: `Γ_m` forces `Θ_m ≤ c_m·t^{2^{−(m−1)}}`,
with the conclusion in `RothBound`'s root-free shape.

**This is the shape the induction actually uses**, and §12 settles that it is: at the point
where the induction hypothesis is invoked, Mahler writes

> `J(U; ρ₁,…,ρ_{m−1}; κ₁,…,κ_{m−1}) ≤ Θ_{m−1}(b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1})`,
> `J(V; ρ_m; κ_m) ≤ Θ₁(b; ρ_m; H_m)`

— both by the **definition** of `Θ` (`U ∈ R(b;ρ)`, `κ ∈ Q(H)`), with no exponent condition
anywhere.  The `Γ` clauses enter separately: §11's descent proves `Γ_{m−1}` for the descended
system, and *that* is what lets the induction bound `Θ_{m−1}`.

⚠⚠ **Correction nineteen: `RothLemmaUniform` cannot serve as the induction hypothesis.**  It
fuses the two — membership in `R(b;ρ)×Q(H)` and `Γ` — into one `∀`-statement sharing a single
`E` with `∀ j, B ≤ Kh j ^ E` and `∀ j, E ≤ ε·d j`.  §11 states clause 4 only at `h = 1`
(`b ≤ K₁^{(1/M)s₁t}`); clause 2 (`K_h^{s_h} ≥ K₁^{s₁}`) propagates it as `b ≤ K_h^{ε s_h}`, an
exponent that **varies with `h`**.  A single `E ≤ ε·min_h d_h` does not follow — `E ≤ ε s_h`
makes `K_h^E ≤ K_h^{ε s_h}`, the wrong direction.  So `RothLemmaUniform` is true but unusable
at its point of use, exactly like the pre-correction-18b form was.  `RothLemmaTheta` has no `E`
and is what §12 invokes.

⚠⚠ **Correction twenty: this was false at `m = 1`, and the counterexample is small.**
`RothGammaFull` encodes `Γ_M`'s case (ii), which requires `M ≥ 2`; at `M = 1` the source uses
case (i), `M = 1, K₁ ≥ 2, b ≤ K₁^{s₁t}`.  Nothing in case (ii) forces `K₁ ≥ 2` when `m = 1`,
because clause 3a reads `q·((1−1)·1·3) ≤ F·p`, i.e. `0 ≤ 0`, leaving `F = 0` admissible and
clause 3b saying only `1 ≤ K₁`.  Take

    σ = Unit,  m = 1,  p = 1,  q = 2  (t = 1/2),  F = 0,  a = 1,  r ≡ 1,  H ≡ 1.

Every clause holds: growth is vacuous at one variable, `height` is `1 ≤ 1`, `floorExp` is
`0 ≤ 0`, `floor` is `2^0 = 1 ≤ 1`, `heightBound` is `1^2 = 1 ≤ 1^1 = 1`.  And `Θ = 1`, attained
at `A = x − 1`, `κ = 1` (height `max(1,1) = 1`, so `κ ∈ Q(1)`), whose translate is `x`.  The
conclusion `RothBound 1 (1/2) 1` asks `1 ≤ 1/2`.

Fixed by the `two_le` clause on `RothGammaFull` and by carrying §14's opening `0 < t ≤ 1` —
which `RothLemmaMahler` already carried and this did not.  `q = 0` is the second half of that:
it makes `t = 0` in `ℚ` while `heightBound` degenerates to `1 ≤ K₁^{r₁p}`, so `Θ ≤ 0` is
demanded and false (take `a = 100`, `H = 2`, `A = 2x − 1`, `κ = 1/2`, giving `Θ ≥ 1`). -/
def RothLemmaTheta (σ : Type*) (m p q F : ℕ) : Prop :=
  0 < p → p ≤ q →
  ∀ (o : σ ≃ Fin m) (a : ℤ) (r H : σ → ℕ) (Θ : ℚ),
    RothGammaFull o p q F r (fun j => (H j : ℤ)) a →
    IsRothTheta a r H Θ →
    RothBound m ((p : ℚ) / (q : ℚ)) Θ

/-- **Roth's lemma at `m = 1`, in `Θ` form** — `RothLemmaTheta` discharged at the base.

Straight from `isRothTheta_le_of_gamma_one`: `RothGammaFull`'s `heightBound` at `m = 1` is
`a^{1·q} ≤ K₁^{r₁p}`, which is §11's case (i) cleared of its exponent, and `two_le` supplies
case (i)'s `K₁ ≥ 2`.  `rothBound_one` turns `Θ ≤ t` into `RothBound 1 t Θ`.

This is the first instance of `RothLemmaTheta` proved, and it is the value `rothConstant_chain`
needs to start from: correction eleven traced `c_m = 2^{m+1} − 3` to the base case rather than
the recurrence, and `c₁ = 1` is exactly `Θ₁ ≤ t`. -/
theorem rothLemmaTheta_one {p q F : ℕ} : RothLemmaTheta Unit 1 p q F := by
  intro hp hpq o a r H Θ hg hΘ
  have hq : q ≠ 0 := by omega
  have hu : o.symm 0 = () := Subsingleton.elim _ _
  have hH : 2 ≤ H () := by exact_mod_cast hg.two_le ()
  have hclause : a ^ q ≤ ((H () : ℤ)) ^ (r () * p) := by
    have h := hg.heightBound 0 rfl
    rwa [hu, one_mul] at h
  exact (rothBound_one _ _).mpr
    ⟨hΘ.nonneg, isRothTheta_le_of_gamma_one hΘ (hg.degPos ()) hq hH hclause⟩

/-- **`RothLemmaTheta` transports along a type equivalence.**

Composing the equivalence into the ordering (`e.symm.trans o`) and into the degree, height and
point data is all it takes, once `RothGammaFull` and `IsRothTheta` transport. -/
theorem RothLemmaTheta.rename_equiv {σ τ : Type*} [DecidableEq σ] [DecidableEq τ] (e : σ ≃ τ)
    {m p q F : ℕ} (h : RothLemmaTheta τ m p q F) : RothLemmaTheta σ m p q F := by
  intro hp hpq o a r H Θ hg hΘ
  exact h hp hpq (e.symm.trans o) a (r ∘ e.symm) (H ∘ e.symm) Θ (hg.rename_equiv e)
    (hΘ.rename_equiv e)

/-- **The base case at `Fin 1`.**  `rothLemmaTheta_one` proves it at `Unit`; `finOneEquiv`
carries it across.

⚠ This closes a gap `rothLemmaTheta_iterate` used to carry as a hypothesis.  It was worth
carrying rather than hiding: the two propositions really are different, and the transport needed
`index_rename_equiv` plus new transports for `InRothPolySet`, `InRothFracSet` and
`RothGammaFull`.  "The variable type is incidental" is true and is still four lemmas. -/
theorem rothLemmaTheta_one_fin {p q F : ℕ} : RothLemmaTheta (Fin 1) 1 p q F :=
  RothLemmaTheta.rename_equiv finOneEquiv rothLemmaTheta_one

/-- **§14's induction step in `Θ` language** — Lemma 4's conclusion plus the sub-problem's
`RothBound` gives the next one.

Both levels sit at the *same* `t`: level `n` uses the variable `s²` and level `n+1` uses `s`,
and `(s²)^{2^{n−1}} = s^{2^n}`.  That is what makes this a single-parameter induction.

The three inputs are exactly Lemma 4's: the sub-problem's bound `RothBound n t Θ'`, the
`max(Ψ, √Ψ)` disjunct, and `Θ ≤ t + 2w`.  ⚠ The leading term is `t`, not `s` — Lemma 4 leads
with the row cost — and `t ≤ s` is what lets `rothConstant_step_lemma4` accept it. -/
theorem rothBound_succ_of_lemma4 {n : ℕ} (hn : 1 ≤ n) {s t Θ Θ' w : ℚ}
    (hs0 : 0 ≤ s) (hs1 : s ≤ 1) (ht : t = s ^ (2 ^ n)) (hΘ0 : 0 ≤ Θ)
    (hsub : RothBound n t Θ')
    (hw : w ≤ Θ' + t ∨ w ^ 2 ≤ Θ' + t)
    (hΘ : Θ ≤ t + 2 * w) :
    RothBound (n + 1) t Θ := by
  subst ht
  have hpow : (s ^ 2) ^ (2 ^ (n - 1)) = s ^ (2 ^ n) := by
    rw [← pow_mul]
    congr 1
    have hn1 : n - 1 + 1 = n := by omega
    calc 2 * 2 ^ (n - 1) = 2 ^ (n - 1 + 1) := by rw [pow_succ]; ring
      _ = 2 ^ n := by rw [hn1]
  have hs2 : (0 : ℚ) ≤ s ^ 2 := sq_nonneg s
  have hsub' : Θ' ≤ ((rothConstant n : ℚ)) * s ^ 2 :=
    ((rothBound_pow_iff (m := n) (s := s ^ 2) (θ := Θ') hs2).mp (by rwa [hpow])).2
  have h2 : (2 : ℕ) ≤ 2 ^ n := by
    calc (2 : ℕ) = 2 ^ 1 := by norm_num
      _ ≤ 2 ^ n := Nat.pow_le_pow_right (by norm_num) hn
  have hts2 : s ^ (2 ^ n) ≤ s ^ 2 := pow_le_pow_of_le_one hs0 hs1 h2
  have hsq : s ^ 2 ≤ s := by nlinarith
  have hts : s ^ (2 ^ n) ≤ s := le_trans hts2 hsq
  have hΨ : Θ' + s ^ (2 ^ n) ≤ ((rothConstant n : ℚ) + 1) * s ^ 2 := by nlinarith
  have hstep := rothConstant_step_lemma4 (θ := Θ) hn hs0 hs1 hΨ hw (by linarith)
  have hfin : RothBound (n + 1) (s ^ (2 ^ (n + 1 - 1))) Θ :=
    (rothBound_pow_iff hs0).mpr ⟨hΘ0, by simpa using hstep⟩
  simpa using hfin

/-- **§14's recursion, one step** — `RothLemma4` at arity `n+1` plus `RothLemmaTheta` at `n`
gives `RothLemmaTheta` at `n+1`.

This is the induction the whole arc has been building toward, and with the pieces in place it is
four lines: Lemma 4 hands over a sub-problem with `Γ_{n}` and its own `Θ'`, the induction
hypothesis turns that `Θ'` into a `RothBound`, and `rothBound_succ_of_lemma4` does §14's
arithmetic.

⚠ **`s` is a hypothesis, and that is correction twenty-three showing through.**
`rothBound_succ_of_lemma4` needs a *rational* `s` with `t = s^{2^n}`, because the root-free
encoding cannot take square roots.  For the recursion to run from `1` to `m` one needs such an
`s` at every level, i.e. `t` a `2^{m−1}`-th power in `ℚ`.  §14 has no such restriction — over `ℝ`
every `t ≥ 0` has the roots — so this is an artifact of the encoding, and removing it means
proving the step in `ℝ` and transferring back.  Not done; the hypothesis is explicit so that the
restriction is visible at every use rather than buried. -/
theorem rothLemmaTheta_succ {σ : Type*} {n p q F : ℕ} (hn : 1 ≤ n)
    (h4 : RothLemma4 σ n p q F) (hIH : RothLemmaTheta (Fin n) n p q F)
    {s : ℚ} (hs0 : 0 ≤ s) (hs1 : s ≤ 1) (hts : (p : ℚ) / (q : ℚ) = s ^ (2 ^ n)) :
    RothLemmaTheta σ (n + 1) p q F := by
  intro hp hpq o a r H Θ hg hΘ
  obtain ⟨b, ρ, H', Θ', w, hg', hΘ', hw, hle⟩ := h4 hp hpq o a r H Θ hg hΘ
  have hsub : RothBound n ((p : ℚ) / (q : ℚ)) Θ' :=
    hIH hp hpq (Equiv.refl (Fin n)) b ρ H' Θ' hg' hΘ'
  exact rothBound_succ_of_lemma4 hn hs0 hs1 hts hΘ.nonneg hsub hw hle

/-- **§14's recursion, iterated** — `RothLemma4` at every arity from `1` to `M−1`, plus the base
case, gives `RothLemmaTheta` at every `m ≤ M`.

The square-root sequence is `s` with `s 0 = t` and `s (n+1)² = s n`, so `s n ^ {2^n} = t` at
every level — the `s` each application of `rothLemmaTheta_succ` needs.  Correction twenty-three
is exactly the observation that such a rational sequence exists only for `t` a `2^{M−1}`-th
power; bounding the range to `n < M` is what makes it exist at all.

⚠ A first draft of *this* theorem left `hsq` unbounded — reproducing correction twenty-three's
own defect one commit after fixing it, which is worth recording because it says something about
the failure mode: the unbounded form is what one writes by default, and nothing objects until
someone asks whether the hypothesis is satisfiable.

⚠ The base case is `rothLemmaTheta_one_fin` — `rothLemmaTheta_one` (proved at `Unit`, because
the `m = 1` chain runs through `pUnitAlgEquiv`) carried to `Fin 1` by `RothLemmaTheta.rename_equiv`.
An earlier version took it as a hypothesis, because the transport did not exist; it does now. -/
theorem rothLemmaTheta_iterate {p q F M : ℕ} {s : ℕ → ℚ}
    (hs0 : ∀ n, 0 ≤ s n) (hs1 : ∀ n, s n ≤ 1)
    (hsq : ∀ n, n + 1 < M → s (n + 1) ^ 2 = s n) (hs00 : s 0 = (p : ℚ) / (q : ℚ))
    (h4 : ∀ n, 1 ≤ n → n < M → RothLemma4 (Fin (n + 1)) n p q F) :
    ∀ m, 1 ≤ m → m ≤ M → RothLemmaTheta (Fin m) m p q F := by
  have key : ∀ n, n < M → s n ^ (2 ^ n) = s 0 := by
    intro n
    induction n with
    | zero => intro _; simp
    | succ k ih =>
        intro hk
        have h2 : (2 : ℕ) ^ (k + 1) = 2 * 2 ^ k := by ring
        rw [h2, pow_mul, hsq k (by omega), ih (by omega)]
  intro m hm
  induction m, hm using Nat.le_induction with
  | base => intro _; exact rothLemmaTheta_one_fin
  | succ n hn ih =>
      intro hnM
      have hlt : n < M := by omega
      exact rothLemmaTheta_succ hn (h4 n hn hlt) (ih (by omega)) (hs0 n) (hs1 n)
        ((key n (by omega)).trans hs00).symm

/-- **Non-vacuity of the iteration's square-root sequence** — and the concrete shape of
correction twenty-three's restriction.

Reaching arity `M` needs `M − 1` successive rational square roots, so `t` must be a
`2^{M−1}`-th power.  At `M = 3` and `t = 1/16 = (1/2)^{2²}` the sequence is
`1/16, 1/4, 1/2` and stops exactly where it is needed.

⚠ One more root — `M = 4` at the same `t` — would need `√(1/2)`, which is irrational.  So the
witness is at the boundary: it exists **because** the range is bounded, and the unbounded form
correction twenty-three removed had no non-constant instance at all. -/
theorem rothLemmaTheta_iterate_seq_witness :
    ∃ s : ℕ → ℚ, (∀ n, 0 ≤ s n) ∧ (∀ n, s n ≤ 1) ∧
      (∀ n, n + 1 < 3 → s (n + 1) ^ 2 = s n) ∧ s 0 = (1 : ℚ) / ((16 : ℕ) : ℚ) := by
  refine ⟨fun n => if n = 0 then 1 / 16 else if n = 1 then 1 / 4 else 1 / 2, ?_, ?_, ?_, ?_⟩
  · intro n; dsimp only; split_ifs <;> norm_num
  · intro n; dsimp only; split_ifs <;> norm_num
  · intro n hn
    have hn2 : n < 2 := by omega
    interval_cases n <;> norm_num
  · norm_num

/-- **Non-vacuity of the induction step.**  `n = 1`, `s = 1/4`, so `t = 1/16`; sub-problem
bound `Θ' = 1/16` (tight for `RothBound 1`), `Ψ = w = 1/8`, `Θ = 5/16`.

⚠ Three hypotheses hold with **equality** — `Θ' = t`, `w = Ψ`, and `Θ = t + 2w` — so the
witness sits on the boundary of what the step allows, not comfortably inside it. -/
theorem rothBound_succ_of_lemma4_witness : RothBound 2 (1 / 16 : ℚ) (5 / 16) :=
  rothBound_succ_of_lemma4 (n := 1) (s := 1 / 4) (t := 1 / 16) (Θ := 5 / 16)
    (Θ' := 1 / 16) (w := 1 / 8)
    le_rfl (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    ((rothBound_one _ _).mpr ⟨by norm_num, by norm_num⟩)
    (Or.inl (by norm_num)) (by norm_num)

/-- **Non-vacuity of the full descent** — the largest hypothesis stack in this arc, satisfied.

Arity `2 → 1`, `t = 1` (`p = q = 1`), `F = 10`, `K = 1024 = 2^F`, `d ≡ 1`, `a = 1`, `r = 1`,
`c = 5`, `b = 32`.  ⚠ As with `height_descend_pq_witness`, several hypotheses hold with
**equality** — `2^F = K`, `q·(n(n+1)(2n+3)) = F·p`, `c = (2n+3)ρ₁`, `b = 2^c·a^r` — because
clause 3's calibration leaves no room. -/
theorem rothGammaFull_descend_witness :
    RothGammaFull (Equiv.refl (Fin 1)) 1 1 10
      (fun k => 1 * splitLeft (Equiv.refl (Fin 2)) (fun _ : Fin 2 => 1) k)
      (splitLeft (Equiv.refl (Fin 2)) (fun _ : Fin 2 => (1024 : ℤ))) 32 :=
  rothGammaFull_descend (Equiv.refl (Fin 2)) 1 1 10 (fun _ => 1) (fun _ => 1024) 1 32
    (r := 1) (c := 5) one_ne_zero (by norm_num) (by norm_num)
    { growth := by intro j k hjk; norm_num
      height := by intro j k _; exact le_rfl
      floorExp := by norm_num
      floor := by intro j _; norm_num
      heightBound := by intro j _; norm_num
      two_le := fun _ => by norm_num
      degPos := fun _ => one_ne_zero }
    (by norm_num) (by intro j _; norm_num)

/-- **Non-vacuity of the descent**, and a demonstration that clause 3 bites.

`n + 1 = 2`, `d ≡ 1`, `r = 1`, `ω = 1`.  ⚠ The heights cannot be `2`: at arity `2` the
floor is `2^⌈1·(1·2·5)⌉ = 2^10 = 1024`, so `Γ_2` demands `H₁ ≥ 1024`.  That is worth exhibiting
rather than describing — every other witness in this arc got away with `q = 2`, and clause 3 is
the one hypothesis that makes that impossible. -/
theorem rothGamma_descend_witness :
    RothGamma (Equiv.refl (Fin 1)) 1
      (fun k => 1 * splitLeft (Equiv.refl (Fin 2)) (fun _ : Fin 2 => 1) k)
      (splitLeft (Equiv.refl (Fin 2)) (fun _ : Fin 2 => (1024 : ℤ))) :=
  rothGamma_descend (Equiv.refl (Fin 2)) 1 (by norm_num) (fun _ => 1) (fun _ => 1024)
    one_ne_zero (fun _ => by norm_num)
    { growth := by intro j k hjk; norm_num
      height := by intro j k _; exact le_rfl
      floor := by intro j _; norm_num [rothHeightFloor] }

/-- ⚠ **`Γ_2` really does exclude `q = 2`** — the floor at arity 2 is `1024`. -/
theorem rothHeightFloor_two : rothHeightFloor 2 1 = 1024 := by
  norm_num [rothHeightFloor]

/-- **The split-off variable comes last** — the hypothesis `index_le_of_rothGrowth_*` needs. -/
theorem splitLast_hlast (n : ℕ) (k : Fin n) :
    (((splitLast n).symm (Sum.inl k) : Fin (n + 1)) : ℕ) + 1
      ≤ (((splitLast n).symm (Sum.inr ()) : Fin (n + 1)) : ℕ) := by
  rw [splitLast_symm_inl, splitLast_symm_inr, Fin.coe_castSucc, Fin.val_last]
  exact k.isLt

/-- **`degreeOf`, transported.** -/
theorem degreeOf_splitOrder [DecidableEq σ] {n : ℕ}
    (o : σ ≃ Fin (n + 1)) (P : MvPolynomial σ R) (x : σ) :
    degreeOf (splitOrder o x) (rename (splitOrder o) P) = degreeOf x P :=
  degreeOf_rename_of_injective (splitOrder o).injective x

/-- **`degreeOf`, transported, read at a left index.** -/
theorem degreeOf_splitOrder_inl [DecidableEq σ] {n : ℕ}
    (o : σ ≃ Fin (n + 1)) (P : MvPolynomial σ R) (x : Fin n) :
    degreeOf (Sum.inl x) (rename (splitOrder o) P)
      = degreeOf ((splitOrder o).symm (Sum.inl x)) P := by
  have h := degreeOf_splitOrder o P ((splitOrder o).symm (Sum.inl x))
  rwa [Equiv.apply_symm_apply] at h

/-- **`degreeOf`, transported, read at the right index.** -/
theorem degreeOf_splitOrder_inr [DecidableEq σ] {n : ℕ}
    (o : σ ≃ Fin (n + 1)) (P : MvPolynomial σ R) (y : Unit) :
    degreeOf (Sum.inr y) (rename (splitOrder o) P)
      = degreeOf ((splitOrder o).symm (Sum.inr y)) P := by
  have h := degreeOf_splitOrder o P ((splitOrder o).symm (Sum.inr y))
  rwa [Equiv.apply_symm_apply] at h

/-! ### §13 for a polynomial presented with an ordering -/

/-- **§13's conclusion, for a polynomial given as `o : σ ≃ Fin (n+1)` plus one degree vector.**

This is the shape `RothLemmaUniform` uses.  Everything about the `σ' ⊕ Unit` split is handled
internally; the caller states degrees, growth and the index bound entirely in terms of `σ`.

⚠ `hres` is still phrased on the **renamed** polynomial, and deliberately: that is what the
induction actually produces, since the sub-problems live on the split.  Hiding the rename here
would only move the transport into the caller.

⚠ It also carries the two non-vanishing hypotheses — see the tenth correction in
`QOU/Mathlib/RothOperatorFamily.lean`.  Without them the hypothesis is unsatisfiable, because
the all-empty operator family is bounded-order, realises the same representation, and has a
vanishing Wronskian for `r ≥ 2`. -/
theorem index_le_of_rothGrowth_split {K : Type*} [Field K] [CharZero K] [DecidableEq σ]
    {n : ℕ} (o : σ ≃ Fin (n + 1)) (ω : ℚ) (hω : 1 ≤ ω) (d : σ → ℕ)
    (hg : RothGrowth o ω d) (hd0 : d (o.symm (Fin.last n)) ≠ 0)
    {D₂ : ℕ} (hD₂ : D₂ ≠ 0) (hd₂ : D₂ ≤ d (o.symm (Fin.last n)))
    (α : σ → K) (P : MvPolynomial σ K) (hP : P ≠ 0)
    (hdeg : degreeOf (o.symm (Fin.last n)) P ≤ d (o.symm (Fin.last n)))
    (εU εV : ℚ) (hε : 0 ≤ εU + εV)
    (hres : ∀ (r : ℕ) (φ : Fin r → MvPolynomial (Fin n) K) (ψ : Fin r → MvPolynomial Unit K)
        (Dx : Fin r → List (Fin n)) (Dy : Fin r → List Unit),
      0 < r → (∀ i, (Dx i).length ≤ (i : ℕ)) → (∀ j, (Dy j).length ≤ (j : ℕ)) →
      rename (splitOrder o) P
          = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (Fin n ⊕ Unit) K)
              * rename Sum.inr (ψ k) →
      mvGenWronskian Dx φ ≠ 0 → mvGenWronskian Dy ψ ≠ 0 →
      index (fun j => r * splitLeft o d j) (splitLeft o α) (mvGenWronskian Dx φ)
          ≤ ((εU : ℚ) : WithTop ℚ) ∧
        index (fun j => r * splitRight o d j) (splitRight o α) (mvGenWronskian Dy ψ)
          ≤ ((εV : ℚ) : WithTop ℚ))
    (θ q : ℚ) (hθt : 1 / ω ≤ θ) (hq0 : 0 ≤ q)
    (hq : ((d (o.symm (Fin.last n)) : ℚ) + 1) * (εU + εV) ≤ q ^ 2 * (D₂ : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index d α P) :
    θ ≤ 1 / ω + 2 * max (εU + εV) q := by
  classical
  have hPne : rename (splitOrder o) P ≠ 0 := fun h =>
    hP (rename_injective _ (splitOrder o).injective (by rw [h, map_zero]))
  refine index_le_of_rothGrowth_of_rescaled_bounds (splitLast n).symm ω hω
    (splitLeft o d) (splitRight o d) (rothGrowth_splitOrder o ω d hg)
    (splitLast_hlast n) ?_ hD₂ ?_ (splitLeft o α) (splitRight o α)
    (rename (splitOrder o) P) hPne ?_ εU εV hε hres θ q hθt hq0 ?_ ?_
  · rwa [splitRight_unit]
  · intro u
    cases u
    rwa [splitRight_unit]
  · rw [splitRight_unit]
    have : degreeOf (splitOrder o (o.symm (Fin.last n))) (rename (splitOrder o) P)
        = degreeOf (o.symm (Fin.last n)) P :=
      degreeOf_rename_of_injective (splitOrder o).injective _
    rw [show (Sum.inr () : Fin n ⊕ Unit) = splitOrder o (o.symm (Fin.last n)) by
      rw [splitOrder, Equiv.trans_apply, Equiv.apply_symm_apply, splitLast_last], this]
    exact hdeg
  · rwa [splitRight_unit]
  · rwa [← index_splitOrder]

/-- **§13 in Lemma 4's shape, transported** — the family exposed, the `w` disjunction, and
everything stated in terms of `σ`, `o` and `d`.

This is the form `RothLemma4` consumes.  Compared with `index_le_of_rothGrowth_split`:

* the realising family comes **back** rather than being quantified over, because the descended
  system depends on the representation length `r` (see
  `RothOperatorFamily.exists_family_index_le_of_rothGrowth`);
* the conclusion is the `w` disjunction, with no `q` and no junction condition;
* the degree bounds are stated against `splitLeft o d` / `splitRight o d`, which is what
  `InRothPolySet` gives the caller, rather than against `P`'s own `degreeOf`.

⚠ `hdegAll` replaces the single `hdeg` of the earlier form.  It is not a strengthening in
practice — `A ∈ R(a; r)` bounds every degree — and the split-off variable's bound alone would
not give the `φ` and `ψ` degree clauses that the induction hypothesis needs. -/
theorem exists_family_index_le_w_of_rothGrowth_split {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {n : ℕ} (o : σ ≃ Fin (n + 1)) (ω : ℚ) (hω : 1 ≤ ω) (d : σ → ℕ)
    (hg : RothGrowth o ω d) (hd0 : d (o.symm (Fin.last n)) ≠ 0)
    (α : σ → K) (P : MvPolynomial σ K) (hP : P ≠ 0)
    (hdegAll : ∀ x, degreeOf x P ≤ d x) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial (Fin n) K) (ψ : Fin r → MvPolynomial Unit K)
      (Dx : Fin r → List (Fin n)) (Dy : Fin r → List Unit),
      0 < r ∧ r ≤ d (o.symm (Fin.last n)) + 1 ∧
      (∀ i, (Dx i).length ≤ (i : ℕ)) ∧ (∀ j, (Dy j).length ≤ (j : ℕ)) ∧
      (∀ k x, degreeOf x (φ k) ≤ splitLeft o d x) ∧
      (∀ k y, degreeOf y (ψ k) ≤ splitRight o d y) ∧
      rename (splitOrder o) P
          = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (Fin n ⊕ Unit) K)
              * rename Sum.inr (ψ k) ∧
      mvGenWronskian Dx φ ≠ 0 ∧ mvGenWronskian Dy ψ ≠ 0 ∧
      ∀ Φ θ : ℚ, 0 ≤ Φ →
        index (splitLeft o d) (splitLeft o α) (mvGenWronskian Dx φ)
            + index (splitRight o d) (splitRight o α) (mvGenWronskian Dy ψ)
            ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ) →
        1 / ω ≤ θ →
        ((θ : ℚ) : WithTop ℚ) ≤ index d α P →
        ∃ w : ℚ, (w ≤ Φ ∨ w ^ 2 ≤ Φ) ∧ θ ≤ 1 / ω + 2 * w := by
  classical
  have hPne : rename (splitOrder o) P ≠ 0 := fun h =>
    hP (rename_injective _ (splitOrder o).injective (by rw [h, map_zero]))
  have hd0' : splitRight o d () ≠ 0 := by rwa [splitRight_unit]
  have hdeg : degreeOf (Sum.inr ()) (rename (splitOrder o) P) ≤ splitRight o d () := by
    rw [degreeOf_splitOrder_inr, splitRight, splitOrder_symm_inr]
    exact hdegAll _
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hdφ, hdψ, hPeq, hWx, hWy, hmain⟩ :=
    exists_family_index_le_w_of_rothGrowth (splitLast n).symm ω hω
      (splitLeft o d) (splitRight o d) (rothGrowth_splitOrder o ω d hg)
      (splitLast_hlast n) hd0' (splitLeft o α) (splitRight o α)
      (rename (splitOrder o) P) hPne hdeg
  rw [splitRight_unit] at hcard
  refine ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, ?_, ?_, hPeq, hWx, hWy, ?_⟩
  · intro k x
    refine le_trans (hdφ k x) ?_
    rw [degreeOf_splitOrder_inl]
    exact hdegAll _
  · intro k y
    refine le_trans (hdψ k y) ?_
    rw [degreeOf_splitOrder_inr]
    exact hdegAll _
  · intro Φ θ hΦ0 hfac hθt hθ
    exact hmain Φ θ hΦ0 hfac hθt (by rwa [← index_splitOrder])

/-! ### Lemma 4, proved

Everything §13 needs is now in place, and the assembly is what puts it together.  The pieces,
in the order the proof uses them:

* `IsRothTheta`'s **attainment** clause gives the realising pair `(A, κ)` — this is why §9's
  finiteness had to be proved rather than assumed;
* `exists_family_index_le_w_of_rothGrowth_split` runs §13 on `map A` and hands back the
  separated representation, fixing the length `rr`;
* `exists_divided_wronskian_budget` bounds the divided Wronskian at that `rr`, in §11's
  currency `b ≤ 2^{(2n+3)(rr·d₁)}·a^{rr}`;
* `rothGammaFull_descend` turns `Γ_{n+1}` into `Γ_n` for the descended system;
* `exists_isRothTheta` names its `Θ'`, and `isRothTheta_right_le_t` gives `Θ₁ ≤ t`;
* the two `_div` halves of `hres` (correction 26) bound the Wronskians against `Θ'` and `Θ₁`,
  and `factor_bound_of_rescaled` turns that into §13's `J(W) ≤ n·Φ`;
* and §13's `w` comes back with `Φ = Θ' + Θ₁ ≤ Θ' + t = Ψ`, which is the weakening the
  conclusion wants.

⚠ **`Θ ≤ t` is a separate case, and it has to be.**  §13's inequality needs `t ≤ θ` — there is
nothing to bound otherwise — so `index_le_or_sq_of_det_bound` carries that hypothesis, and the
assembly cannot discharge it.  It does not need to: when `Θ ≤ t` the conclusion holds with
`w := 0`, and the first disjunct `0 ≤ Θ' + t` is free.  ⚠ That branch would **not** be available
under correction 25's old `=` encoding, which requires `w = Ψ` or `w² = Ψ` exactly and admits
`w = 0` only when `Ψ = 0`.

⚠ `1 ≤ n` is Mahler's `m ≥ 2`, and it enters through `isRothTheta_right_le_t` alone. -/

/-- **Lemma 4 (§13), proved.**

`Γ_{n+1}` produces a descended system with `Γ_n` and `Θ_{n+1} ≤ t + 2·max(Ψ, √Ψ)` where
`Ψ = Θ_n + t`.  No hypothesis beyond `0 < p ≤ q`, `1 ≤ n`, and `Γ_{n+1}` itself. -/
theorem rothLemma4_of_one_le {σ : Type*} [DecidableEq σ] {n : ℕ} (hn : 1 ≤ n) {p q F : ℕ} :
    RothLemma4 σ n p q F := by
  classical
  intro hp hpq o a rd H Θ hg hΘ
  haveI : Fintype σ := Fintype.ofEquiv _ o.symm
  have hq0 : 0 < q := lt_of_lt_of_le hp hpq
  have hpQ : (0:ℚ) < (p:ℚ) := by exact_mod_cast hp
  have hqQ : (0:ℚ) < (q:ℚ) := by exact_mod_cast hq0
  have ht0 : (0:ℚ) ≤ (p:ℚ)/(q:ℚ) := le_of_lt (div_pos hpQ hqQ)
  have hω : (1:ℚ) ≤ (q:ℚ)/(p:ℚ) := by
    rw [le_div_iff₀ hpQ, one_mul]; exact_mod_cast hpq
  have hinv : 1 / ((q:ℚ)/(p:ℚ)) = (p:ℚ)/(q:ℚ) := by rw [one_div, inv_div]
  obtain ⟨-, A, κ, hA, hκ, heq⟩ := hΘ
  have ha1 : 1 ≤ a := by
    obtain ⟨m0, hm0⟩ := support_nonempty.mpr hA.1
    exact le_trans (Int.one_le_abs (mem_support_iff.mp hm0)) (hA.2.2 m0)
  have ha0 : (0:ℤ) ≤ a := le_trans zero_le_one ha1
  have hdegAll : ∀ x, degreeOf x (map (algebraMap ℤ ℚ) A) ≤ rd x := fun x =>
    le_trans (degreeOf_map_le _ x A) (hA.2.1 x)
  have hAQ0 : map (algebraMap ℤ ℚ) A ≠ 0 := fun hz =>
    hA.1 (map_injective (algebraMap ℤ ℚ) (algebraMap ℤ ℚ).injective_int
      (by rw [map_zero]; exact hz))
  have hd0 : rd (o.symm (Fin.last n)) ≠ 0 := hg.degPos _
  obtain ⟨rr, φ, ψ, Dx, Dy, hrr, hcard, hDx, hDy, hdφ, hdψ, hPeq, hWx, hWy, hmain⟩ :=
    exists_family_index_le_w_of_rothGrowth_split o ((q:ℚ)/(p:ℚ)) hω rd hg.growth hd0
      κ (map (algebraMap ℤ ℚ) A) hAQ0 hdegAll
  -- the renamed integral polynomial
  have hArn : InRothPolySet a (rd ∘ (splitOrder o).symm) (rename (splitOrder o) A) :=
    InRothPolySet.rename_equiv (splitOrder o) hA
  have hP'map : map (Int.castRingHom ℚ) (rename (splitOrder o) A)
      = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (Fin n ⊕ Unit) ℚ) * rename Sum.inr (ψ k) := by
    rw [map_rename]; exact hPeq
  have hdegP' : ∀ h, degreeOf h (rename (splitOrder o) A)
      ≤ Sum.elim (splitLeft o rd) (splitRight o rd) h := by
    intro h
    cases h with
    | inl x => rw [degreeOf_splitOrder_inl]; exact hA.2.1 _
    | inr y => rw [degreeOf_splitOrder_inr]; exact hA.2.1 _
  -- the largest degree
  have hi0 : (0 : ℕ) < n + 1 := Nat.succ_pos n
  have hle_first : ∀ k : Fin (n + 1), rd (o.symm k) ≤ rd (o.symm ⟨0, hi0⟩) := by
    intro k
    have h := rothGrowth_antitone hω hg.growth (k : ℕ) (⟨0, hi0⟩ : Fin (n + 1)) k (by simp)
    exact_mod_cast h
  have hsum : ∑ h, Sum.elim (splitLeft o rd) (splitRight o rd) h
      ≤ (n + 1) * rd (o.symm ⟨0, hi0⟩) := by
    rw [Fintype.sum_sum_type]
    have h1 : ∑ k : Fin n, splitLeft o rd k ≤ n * rd (o.symm ⟨0, hi0⟩) := by
      calc ∑ k : Fin n, splitLeft o rd k ≤ ∑ _k : Fin n, rd (o.symm ⟨0, hi0⟩) :=
            Finset.sum_le_sum (fun k _ => by rw [splitLeft_apply]; exact hle_first _)
        _ = n * rd (o.symm ⟨0, hi0⟩) := by simp
    have h2 : ∑ _u : Unit, splitRight o rd _u ≤ rd (o.symm ⟨0, hi0⟩) := by
      simpa [splitRight_unit] using hle_first (Fin.last n)
    have h3 : (n + 1) * rd (o.symm ⟨0, hi0⟩)
        = n * rd (o.symm ⟨0, hi0⟩) + rd (o.symm ⟨0, hi0⟩) := by ring
    rw [h3]
    exact Nat.add_le_add h1 h2
  -- §12's height estimate, in §11's currency
  obtain ⟨W, cc, hcc0, hdet, hWB⟩ :=
    exists_divided_wronskian_budget (n := n) (dlast := rd (o.symm (Fin.last n)))
      (dfirst := rd (o.symm ⟨0, hi0⟩)) ha1 Dx Dy (rename (splitOrder o) A)
      hdegP' hArn.2.2 hcard hsum (hle_first _)
  have hb1 : (1 : ℤ) ≤ 2 ^ ((2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩))) * a ^ rr :=
    one_le_mul_of_one_le_of_one_le (one_le_pow₀ (by norm_num)) (one_le_pow₀ ha1)
  have hb0 : (0 : ℤ) ≤ 2 ^ ((2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩))) * a ^ rr :=
    le_trans zero_le_one hb1
  -- §11's descent
  have hdesc := rothGammaFull_descend o p q F rd (fun j => (H j : ℤ)) a
      (2 ^ ((2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩))) * a ^ rr)
      (r := rr) (c := (2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩)))
      hrr.ne' ha0 hb0 hg le_rfl (by
        intro j hj
        have : j = (⟨0, hi0⟩ : Fin (n + 1)) := Fin.ext (by simpa using hj)
        rw [this])
  -- the two `Θ`s of the descended system
  have hH1 : ∀ j : σ, 1 ≤ H j := by
    intro j
    have h2 := hg.two_le j
    have : (2 : ℤ) ≤ (H j : ℤ) := h2
    omega
  obtain ⟨Θ', hΘ'⟩ := exists_isRothTheta
    (2 ^ ((2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩))) * a ^ rr)
    (fun k => rr * splitLeft o rd k) (splitLeft o H) hb1 (fun h => hH1 _)
  obtain ⟨Θ₁, hΘ₁⟩ := exists_isRothTheta
    (2 ^ ((2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩))) * a ^ rr)
    (fun u => rr * splitRight o rd u) (splitRight o H) hb1 (fun h => hH1 _)
  have hΘ₁t : Θ₁ ≤ (p : ℚ) / (q : ℚ) :=
    isRothTheta_right_le_t hn o hq0.ne' hrr.ne' hb1 hg hdesc hΘ₁
  -- the two halves of `hres`, against the divided Wronskian
  have hxhalf := index_rescaled_wronskian_le_theta_div (splitLeft o rd)
    (2 ^ ((2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩))) * a ^ rr) (splitLeft o H)
    (splitLeft o κ) Θ' hΘ' (fun h => hκ _) Dx Dy φ ψ (rename (splitOrder o) A)
    hP'map hWx hWy (fun j k => hdφ k j) W hcc0.ne' hdet hWB
  have hyhalf := index_rescaled_wronskian_le_right_theta_div (σ := Fin n) (splitRight o rd)
    (2 ^ ((2 * n + 3) * (rr * rd (o.symm ⟨0, hi0⟩))) * a ^ rr) (splitRight o H)
    (splitRight o κ) Θ₁ hΘ₁ (fun h => hκ _) Dx Dy φ ψ (rename (splitOrder o) A)
    hP'map hWx hWy (fun j k => hdψ k j) W hcc0.ne' hdet hWB
  have hfac := factor_bound_of_rescaled hrr.ne' (splitLeft o rd) (splitRight o rd)
    (splitLeft o κ) (splitRight o κ) Dx Dy φ ψ Θ' Θ₁ hxhalf hyhalf
  have hΦ0 : (0 : ℚ) ≤ Θ' + Θ₁ := add_nonneg hΘ'.nonneg hΘ₁.nonneg
  by_cases hcase : Θ ≤ (p : ℚ) / (q : ℚ)
  · exact ⟨_, _, _, Θ', 0, hdesc, hΘ', Or.inl (by linarith [hΘ'.nonneg]), by linarith⟩
  · push_neg at hcase
    obtain ⟨w, hw, hle⟩ := hmain (Θ' + Θ₁) Θ hΦ0 hfac
      (by rw [hinv]; exact le_of_lt hcase) (le_of_eq heq.symm)
    rw [hinv] at hle
    exact ⟨_, _, _, Θ', w, hdesc, hΘ',
      hw.imp (fun h => by linarith) (fun h => by linarith), hle⟩

/-! ### §14, with Lemma 4 discharged

`rothLemmaTheta_iterate` carried `h4` as a hypothesis at every arity below `M`.
`rothLemma4_of_one_le` supplies it, so the recursion runs on the `s`-sequence alone. -/

/-- **Roth's Lemma in `Θ` form, unconditional on Lemma 4.**

⚠ The `s`-ladder here is correction 23's encoding restriction: `t` has to be a `2^{M−1}`-th
power in `ℚ`.  **`QOU/Mathlib/RothRealLadder.lean` removes it** — `rothLemmaTheta_all` holds at
every arity for every `p, q, F`, by taking the roots in `ℝ` where they exist.  This form is kept
because it is `ℝ`-free, and because `rothLemmaTheta_three` is a self-contained instance. -/
theorem rothLemmaTheta_of_seq {p q F M : ℕ} {s : ℕ → ℚ}
    (hs0 : ∀ n, 0 ≤ s n) (hs1 : ∀ n, s n ≤ 1)
    (hsq : ∀ n, n + 1 < M → s (n + 1) ^ 2 = s n) (hs00 : s 0 = (p : ℚ) / (q : ℚ)) :
    ∀ m, 1 ≤ m → m ≤ M → RothLemmaTheta (Fin m) m p q F :=
  rothLemmaTheta_iterate hs0 hs1 hsq hs00 (fun _ hn _ => rothLemma4_of_one_le hn)

/-- **An instance with nothing left open**: `t = 1/16 = (1/2)^{2²}`, so the ladder
`1/16, 1/4, 1/2` lives in `ℚ` and §14 runs to `M = 3`.

⚠ This is the arc's first statement of Roth's Lemma with **no hypothesis at all** beyond the
arity bound — no `Γ` to supply, no Lemma 4 to assume, no `s`-sequence to produce. -/
theorem rothLemmaTheta_three {F : ℕ} :
    ∀ m, 1 ≤ m → m ≤ 3 → RothLemmaTheta (Fin m) m 1 16 F := by
  obtain ⟨s, hs0, hs1, hsq, hs00⟩ := rothLemmaTheta_iterate_seq_witness
  exact rothLemmaTheta_of_seq hs0 hs1 hsq (by simpa using hs00)

/-! ### Next

The transport is done; `index_le_of_rothGrowth_split` states §13's conclusion entirely in
terms of `σ`, `o` and `d`.

⚠ What still stands between this and the recursion is **integrality**, not indexing.  The
induction hypothesis (`RothLemmaUniform`) is about polynomials with *integer* coefficients;
the Wronskians `hres` speaks of are rational combinations of the representation's factors.
Gauss's lemma is what reconciles them — §6 of the source does exactly this, and
`RothHeightBound` has the Gauss step — but it is **not wired in**, so `hres` remains a
hypothesis.

That is the next piece, and it is the last one before the induction can be written. -/

end MvPolynomial
