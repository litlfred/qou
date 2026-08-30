import QOU.Mathlib.LagrangeCoeffSum

/-!
# QOU.Mathlib.LagrangeCornerNodeSum — the corner node sum

A third member of the `LagrangeCoeffSum` family. Where `sum_prod_qratio` weights each node by `1`
and `sum_prod_qratio_weighted` weights it by the seminormal entry `Q·v_i/(Q·v_i − v_b)`, this one
weights it by the **constant-numerator** ratio `(Q − 1)/(Q·v_i − v_b)`, and the sum is `1`:

    ∑_{i ∈ s} (∏_{j ≠ i} (Q·v_i − v_j)/(v_i − v_j)) · (Q − 1)/(Q·v_i − v_b)  =  1      (`v_b = 1`)

This is the node-coordinate form of the **Pieri corner identity** — the one identity the Macdonald
hook telescope's Pieri step `(P)` reduces to. In the intended instantiation `v_i = Q^{β_i}` for the
β-numbers of a partition padded with one empty row, so the padded row contributes the node
`v_b = Q^0 = 1`, and `i` ranges over the rows admitting a box.

## Why `v b = 1` is a hypothesis and not decoration

The identity is **false** without a node equal to `1`: at `|s| = 2` with free nodes the sum is

    (v₀Q² − v₀Q + v₁Q² − v₁Q − Q² + 1)/(v₀v₁Q² − v₀Q − v₁Q + 1),

which is not `1`. The node at `1` is exactly the addable corner in the new bottom row, so the
identity is *about* shapes that may grow a row — dropping that corner from the sum breaks it.

## Where the `q`-dependence goes

The whole `Q`-dependence sits in the coefficients `c₁ … c_{|s|−1}` of `∏_{j≠b}(Q·X − v_j)`, and the
Lagrange vanishing annihilates every one of them: only `c₀`, which is `Q`-free, survives. That is
why the right-hand side is a bare `1` for every `Q`, and it is the reason the `q`-deformed statement
is no harder than its `q = 1` shadow rather than harder.

## Base ring (§7c)

Generic `[Field F]`, inherited from `LagrangeCoeffSum`. No ordering, no `ℝ`, nothing archimedean.
-/

namespace QOU.Mathlib

open Polynomial Finset

variable {F : Type*} [Field F] {ι : Type*} [DecidableEq ι]

/-- **The corner node sum.**

`∑_{i ∈ s} (∏_{j≠i} (Q·v_i − v_j)/(v_i − v_j)) · (Q − 1)/(Q·v_i − v_b) = 1`, for a distinguished
node `b` with `v b = 1`.

**`hne` is not decoration**, exactly as in `sum_prod_qratio_weighted`: without it a term is `0/0`,
since `Q·v_i = v_b` kills the ratio's `j = b` numerator factor and the weight's denominator at once.
In the instantiation `v_i = Q^{β_i}` it is discharged by addability — `β_b = β_i + 1` is precisely
what it means for row `i` *not* to admit a box.

**`i = b` needs no special case.** For `i ≠ b` the weight's denominator cancels the `j = b` factor
of the numerator; at `i = b` that factor is absent and the weight is `(Q−1)/(Q·1 − 1) = 1`, and the
two land on the same expression `eval (v i) h / (v i · ∏_{j≠i}(v i − v j))`. -/
theorem sum_prod_qratio_corner {s : Finset ι} {v : ι → F} (hv : Set.InjOn v s)
    (hv0 : ∀ i ∈ s, v i ≠ 0) {Q : F} (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) {b : ι} (hb : b ∈ s)
    (hvb : v b = 1) (hne : ∀ i ∈ s, i ≠ b → Q * v i - v b ≠ 0) :
    (∑ i ∈ s, (∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j)) * ((Q - 1) / (Q * v i - v b)))
      = 1 := by
  classical
  have hQ1' : Q - 1 ≠ 0 := sub_ne_zero.mpr hQ1
  have hcard : 1 ≤ s.card := Finset.card_pos.mpr ⟨b, hb⟩
  set f : F[X] := ∏ j ∈ s, (X - C (v j)) with hf
  set h : F[X] := ∏ j ∈ s.erase b, (C Q * X - C (v j)) with hh
  -- the Vandermonde weights are nonzero
  have hD : ∀ i ∈ s, (∏ j ∈ s.erase i, (v i - v j)) ≠ 0 := by
    intro i hi
    refine Finset.prod_ne_zero_iff.mpr fun j hj => sub_ne_zero.mpr ?_
    obtain ⟨hji, hjs⟩ := Finset.mem_erase.mp hj
    exact fun hc => hji (hv hjs hi hc.symm)
  -- shape of `f`
  have hfm : f.Monic := monic_prod_of_monic _ _ fun j _ => monic_X_sub_C _
  have hfdeg : f.natDegree = s.card := by
    rw [hf, natDegree_prod_of_monic _ _ fun j _ => monic_X_sub_C _]
    simp
  have hfne : f ≠ 0 := hfm.ne_zero
  have hfeval : ∀ i ∈ s, eval (v i) f = 0 := by
    intro i hi
    rw [hf, eval_prod]
    exact Finset.prod_eq_zero hi (by simp)
  -- shape of `h`
  have hfac : ∀ j : ι, (C Q * X - C (v j) : F[X]) = C Q * X + C (-(v j)) := by
    intro j; rw [map_neg]; ring
  have hfacne : ∀ j : ι, (C Q * X - C (v j) : F[X]) ≠ 0 := by
    intro j hzero
    have hd := natDegree_linear (a := Q) (b := -(v j)) hQ0
    rw [← hfac j, hzero] at hd
    simp at hd
  have hhdeg : h.natDegree = s.card - 1 := by
    have h1 : ∀ j ∈ s.erase b, (C Q * X - C (v j) : F[X]).natDegree = 1 := by
      intro j _; rw [hfac j]; exact natDegree_linear hQ0
    rw [hh, natDegree_prod _ _ fun j _ => hfacne j, Finset.sum_congr rfl h1]
    simp [Finset.card_erase_of_mem hb]
  have hhlead : h.leadingCoeff = Q ^ (s.card - 1) := by
    have h2 : ∀ j ∈ s.erase b, (C Q * X - C (v j) : F[X]).leadingCoeff = Q := by
      intro j _; rw [hfac j]; exact leadingCoeff_linear hQ0
    rw [hh, leadingCoeff_prod, Finset.prod_congr rfl h2]
    simp [Finset.card_erase_of_mem hb]
  have hhne : h ≠ 0 := fun hz => by
    rw [hz, leadingCoeff_zero] at hhlead
    exact pow_ne_zero _ hQ0 hhlead.symm
  have hheval : ∀ i : ι, eval (v i) h = ∏ j ∈ s.erase b, (Q * v i - v j) := by
    intro i
    rw [hh, eval_prod]
    exact Finset.prod_congr rfl fun j _ => by simp
  -- the two constant terms differ by a sign, because `v b = 1`
  have hh0 : h.coeff 0 = ∏ j ∈ s.erase b, (-(v j)) := by
    rw [coeff_zero_eq_eval_zero, hh, eval_prod]
    exact Finset.prod_congr rfl fun j _ => by simp
  have hf0 : f.coeff 0 = ∏ j ∈ s, (-(v j)) := by
    rw [coeff_zero_eq_eval_zero, hf, eval_prod]
    exact Finset.prod_congr rfl fun j _ => by simp
  have hcoeff_rel : h.coeff 0 = -(f.coeff 0) := by
    rw [hf0, hh0, ← Finset.mul_prod_erase s (fun j => -(v j)) hb, hvb]
    ring
  have hfcne : f.coeff 0 ≠ 0 := by
    rw [hf0]
    exact Finset.prod_ne_zero_iff.mpr fun j hj => neg_ne_zero.mpr (hv0 j hj)
  -- `divX` bookkeeping
  have hevalDivX : ∀ (p : F[X]) (x : F), x * eval x (divX p) + p.coeff 0 = eval x p := by
    intro p x
    have hx : eval x (X * divX p) + eval x (C (p.coeff 0)) = eval x p := by
      rw [← eval_add, X_mul_divX_add p]
    rw [eval_mul, eval_X, eval_C] at hx
    exact hx
  -- every summand is the `h`-residue term
  have hterm : ∀ i ∈ s,
      (∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j)) * ((Q - 1) / (Q * v i - v b))
        = eval (v i) h / (v i * ∏ j ∈ s.erase i, (v i - v j)) := by
    intro i hi
    have hvi : v i ≠ 0 := hv0 i hi
    have hDi := hD i hi
    rw [Finset.prod_div_distrib, hheval i]
    by_cases hib : i = b
    · subst hib
      rw [hvb]
      field_simp
    · have hbe : b ∈ s.erase i := Finset.mem_erase.mpr ⟨fun hc => hib hc.symm, hb⟩
      have hie : i ∈ s.erase b := Finset.mem_erase.mpr ⟨hib, hi⟩
      have hnum : (∏ j ∈ s.erase i, (Q * v i - v j))
          = (Q * v i - v b) * ∏ j ∈ (s.erase i).erase b, (Q * v i - v j) :=
        (Finset.mul_prod_erase _ _ hbe).symm
      have hnum' : (∏ j ∈ s.erase b, (Q * v i - v j))
          = (Q * v i - v i) * ∏ j ∈ (s.erase b).erase i, (Q * v i - v j) :=
        (Finset.mul_prod_erase _ _ hie).symm
      have hnez := hne i hi hib
      have hcomm : (s.erase b).erase i = (s.erase i).erase b := by
        ext x; simp only [Finset.mem_erase]; tauto
      rw [hnum, hnum', hcomm]
      have hself : Q * v i - v i = (Q - 1) * v i := by ring
      rw [hself]
      field_simp
  -- split the residue term into the two Lagrange sums
  have hAf : ∀ i ∈ s, eval (v i) (divX f) = -(f.coeff 0) / v i := by
    intro i hi
    have hvi : v i ≠ 0 := hv0 i hi
    have hx : v i * eval (v i) (divX f) + f.coeff 0 = 0 := by
      rw [hevalDivX f (v i)]; exact hfeval i hi
    rw [eq_div_iff hvi]
    linear_combination hx
  have hsplit : ∀ i ∈ s, eval (v i) h / (v i * ∏ j ∈ s.erase i, (v i - v j))
      = eval (v i) (divX h) / (∏ j ∈ s.erase i, (v i - v j))
        + eval (v i) (divX f) / (∏ j ∈ s.erase i, (v i - v j)) := by
    intro i hi
    have hvi : v i ≠ 0 := hv0 i hi
    have hDi := hD i hi
    have h1 : v i * eval (v i) (divX h) + h.coeff 0 = eval (v i) h := hevalDivX h (v i)
    have h3 : v i * eval (v i) (divX f) = h.coeff 0 := by
      rw [hAf i hi, hcoeff_rel]; field_simp
    have hnum : eval (v i) h = (eval (v i) (divX h) + eval (v i) (divX f)) * v i := by
      linear_combination -h1 - h3
    rw [hnum]
    field_simp
  -- the two Lagrange sums: `divX h` is too low a degree to register, `divX f` is monic
  have hHdeg : (divX h).degree < (s.card : WithBot ℕ) := by
    refine lt_of_lt_of_le (degree_divX_lt hhne) ?_
    rw [degree_eq_natDegree hhne, hhdeg]
    exact_mod_cast Nat.sub_le _ _
  have hHcoeff : (divX h).coeff (s.card - 1) = 0 := by
    rw [coeff_divX, Nat.sub_add_cancel hcard]
    exact coeff_eq_zero_of_natDegree_lt (by rw [hhdeg]; omega)
  have hFdeg : (divX f).degree < (s.card : WithBot ℕ) := by
    rw [← hfdeg, ← degree_eq_natDegree hfne]
    exact degree_divX_lt hfne
  have hFcoeff : (divX f).coeff (s.card - 1) = 1 := by
    rw [coeff_divX, Nat.sub_add_cancel hcard, ← hfdeg, coeff_natDegree]
    exact hfm
  have hH := sum_eval_div_prod_eq_coeff hv hHdeg
  rw [hHcoeff] at hH
  have hF := sum_eval_div_prod_eq_coeff hv hFdeg
  rw [hFcoeff] at hF
  calc (∑ i ∈ s, (∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j)) * ((Q - 1) / (Q * v i - v b)))
      = ∑ i ∈ s, (eval (v i) (divX h) / (∏ j ∈ s.erase i, (v i - v j))
          + eval (v i) (divX f) / (∏ j ∈ s.erase i, (v i - v j))) :=
        Finset.sum_congr rfl fun i hi => by rw [hterm i hi, hsplit i hi]
    _ = (∑ i ∈ s, eval (v i) (divX h) / (∏ j ∈ s.erase i, (v i - v j)))
          + ∑ i ∈ s, eval (v i) (divX f) / (∏ j ∈ s.erase i, (v i - v j)) :=
        Finset.sum_add_distrib
    _ = 1 := by rw [hH, hF]; ring

/-- **The corner identity, for any weight family whose box-addition ratio is the corner
`q`-ratio.**

If `w i` — the weight attached to the corner in row `i` — is the corner `q`-ratio at node `i`,
then `∑_i w i = 1`. This is the form in which `sum_prod_qratio_corner` delivers the Pieri step,
and it is the exact analogue of `sum_eq_bracket_mul_of_qratio_scaling` for the branching sum.

`hw` is a genuine sub-hypothesis and not a restatement of the conclusion: it says that adding a
box in row `i` multiplies the weight by the node ratio, which is the `q`-analogue of the
Frame–Robinson–Thrall hook identity in node coordinates and is **not** proved here. Establishing
it is what still stands between this and the general Pieri step (P); the same input is what
`sum_eq_bracket_mul_of_qratio_scaling` names as its own remaining gap. Measured — over 13 shapes
at three padding lengths, `computations/pieri_corner_node_identity_probe.py` fact 2 — the
identity it needs is

    ∏_{c ∈ λ} (1 − q^{h(c)})  =  ∏_i (q;q)_{β_i} / ∏_{j<l} (1 − q^{β_j − β_l}),

whose classical shadow `prodHooks_mul_betaProdGap` is already proved on the list layer. -/
theorem sum_eq_one_of_corner_ratio_scaling {s : Finset ι} {v : ι → F} (hv : Set.InjOn v s)
    (hv0 : ∀ i ∈ s, v i ≠ 0) {Q : F} (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) {b : ι} (hb : b ∈ s)
    (hvb : v b = 1) (hne : ∀ i ∈ s, i ≠ b → Q * v i - v b ≠ 0) (w : ι → F)
    (hw : ∀ i ∈ s, w i = (∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j))
        * ((Q - 1) / (Q * v i - v b))) :
    ∑ i ∈ s, w i = 1 := by
  rw [Finset.sum_congr rfl hw]
  exact sum_prod_qratio_corner hv hv0 hQ0 hQ1 hb hvb hne

end QOU.Mathlib
