import Mathlib.LinearAlgebra.Lagrange

/-!
# QOU.Mathlib.LagrangeCoeffSum — coefficient extraction as a sum over interpolation nodes

Two facts about Lagrange interpolation that Mathlib states only implicitly.

| | |
|---|---|
| `coeff_lagrangeBasis` | the top coefficient of `Lagrange.basis s v i` is `∏_{j ≠ i} (v i − v j)⁻¹` |
| `sum_eval_div_prod_eq_coeff` | for `deg f < |s|`, `∑_i f(v i) / ∏_{j≠i}(v i − v j) = f.coeff (|s| − 1)` |
| `sum_prod_qratio` | `∑_i ∏_{j≠i} (Q·v i − v j)/(v i − v j) = 1 + Q + ⋯ + Q^{|s|−1}` |
| `sum_eq_bracket_mul_of_qratio_scaling` | the same, packaged as the branching identity |
| `sum_prod_qratio_weighted` | the same sum weighted by `Q·v_i/(Q·v_i − v_b)`, which sums to `Q^{|s|}/(Q−1)` |

The second is the algebraic form of "the sum of the residues of `f/∏(X − v j)` over its poles reads
off the top coefficient of `f`".  It is the workhorse: with a well-chosen `f` it turns a sum of
products over nodes into a single coefficient.

## Base ring (§7c)

Generic `[Field F]` — Mathlib's `Lagrange` API needs the inverses.  No ordering, no `ℝ`.

LaTeX label: `lem:lagrange-coeff-sum`
-/

namespace QOU.Mathlib

open Polynomial Finset

variable {F : Type*} [Field F] {ι : Type*} [DecidableEq ι]

/-- The top coefficient of a Lagrange basis polynomial. -/
theorem coeff_lagrangeBasis {s : Finset ι} {v : ι → F} {i : ι}
    (hv : Set.InjOn v s) (hi : i ∈ s) :
    (Lagrange.basis s v i).coeff (s.card - 1) = ∏ j ∈ s.erase i, (v i - v j)⁻¹ := by
  rw [← Lagrange.natDegree_basis hv hi, Polynomial.coeff_natDegree, Lagrange.basis,
    Polynomial.leadingCoeff_prod]
  refine Finset.prod_congr rfl fun j _ => ?_
  rw [Lagrange.basisDivisor, Polynomial.leadingCoeff_mul, Polynomial.leadingCoeff_C,
    Polynomial.leadingCoeff_X_sub_C, mul_one]

/-- **Coefficient extraction as a node sum.**

For a polynomial of degree less than the number of nodes,

`∑_{i ∈ s} f(v i) / ∏_{j ∈ s \ {i}} (v i − v j) = f.coeff (|s| − 1)`.

Proof: `f` equals its own Lagrange interpolant, and the top coefficient of the `i`-th basis
polynomial is `∏_{j ≠ i}(v i − v j)⁻¹`. -/
theorem sum_eval_div_prod_eq_coeff {s : Finset ι} {v : ι → F} (hv : Set.InjOn v s)
    {f : F[X]} (hdeg : f.degree < s.card) :
    ∑ i ∈ s, eval (v i) f / ∏ j ∈ s.erase i, (v i - v j) = f.coeff (s.card - 1) := by
  conv_rhs => rw [Lagrange.eq_interpolate hv hdeg]
  rw [Lagrange.interpolate_apply, Polynomial.finset_sum_coeff]
  refine Finset.sum_congr rfl fun i hi => ?_
  rw [Polynomial.coeff_C_mul, coeff_lagrangeBasis hv hi, Finset.prod_inv_distrib,
    ← div_eq_mul_inv]

/-! ## The `q`-ratio node sum -/

theorem sub_one_mul_geom_sum (Q : F) (n : ℕ) :
    (Q - 1) * ∑ k ∈ Finset.range n, Q ^ k = Q ^ n - 1 := by
  induction n with
  | zero => simp
  | succ m ih => rw [Finset.sum_range_succ, mul_add, ih]; ring

/-- **The `q`-ratio node sum.**

For pairwise distinct nonzero nodes `v i`, `i ∈ s`,

`∑_{i ∈ s} ∏_{j ≠ i} (Q·v i − v j)/(v i − v j) = 1 + Q + ⋯ + Q^{|s|−1}`.

This is the algebraic heart of Pieri's rule at a principal specialisation.  Writing the level-`r`
principal specialisation of `s_μ` as a Vandermonde ratio in `x_i = Q^{μ_i + r − i}`, the ratio
`s_{μ+□ in row i}/s_μ` is exactly the `i`-th summand, and the identity says those ratios sum to
`[r]_Q` — which is the branching identity.  It also explains for free why the non-addable rows may
be summed over harmlessly: if adding a box to row `i` would break the partition, then
`Q·v i = v_{i−1}` and that summand is zero.

**Two hypotheses are artefacts of the proof, not of the statement.**  The identity is a polynomial
identity and holds at `Q = 1` and at `v i = 0` too; `hQ1` and `hv0` are needed because the argument
divides by `Q − 1` and by `v i`.  Both hold in the intended application, where `v i` is a power of
`Q` and `Q` is not a root of unity.

Proof: apply `sum_eval_div_prod_eq_coeff` twice — to `divX f` and to `divX g`, where
`f = ∏_j (X − v j)` and `g = ∏_j (Q·X − v j)`.  The first pins the node sum of
`1/(v i · ∏_{j≠i}(v i − v j))` (the residue at `0`); the second produces the wanted sum plus that
same correction, and the top coefficients `1` and `Q^{|s|}` do the rest. -/
theorem sum_prod_qratio {s : Finset ι} {v : ι → F} (hv : Set.InjOn v s)
    (hv0 : ∀ i ∈ s, v i ≠ 0) {Q : F} (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) :
    ∑ i ∈ s, ∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j)
      = ∑ k ∈ Finset.range s.card, Q ^ k := by
  rcases s.eq_empty_or_nonempty with rfl | hs
  · simp
  have hcard : 1 ≤ s.card := Finset.card_pos.mpr hs
  set f : F[X] := ∏ j ∈ s, (X - C (v j)) with hf
  set g : F[X] := ∏ j ∈ s, (C Q * X - C (v j)) with hg
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
  -- shape of `g`
  have hgfac : ∀ j : ι, (C Q * X - C (v j) : F[X]) = C Q * X + C (-(v j)) := by
    intro j; rw [map_neg]; ring
  have hgfacne : ∀ j : ι, (C Q * X - C (v j) : F[X]) ≠ 0 := by
    intro j h
    have hd := natDegree_linear (a := Q) (b := -(v j)) hQ0
    rw [← hgfac j, h] at hd
    simp at hd
  have hgdeg : g.natDegree = s.card := by
    have h1 : ∀ j ∈ s, (C Q * X - C (v j) : F[X]).natDegree = 1 := by
      intro j _; rw [hgfac j]; exact natDegree_linear hQ0
    rw [hg, natDegree_prod _ _ fun j _ => hgfacne j, Finset.sum_congr rfl h1]
    simp
  have hglead : g.leadingCoeff = Q ^ s.card := by
    have h2 : ∀ j ∈ s, (C Q * X - C (v j) : F[X]).leadingCoeff = Q := by
      intro j _; rw [hgfac j]; exact leadingCoeff_linear hQ0
    rw [hg, leadingCoeff_prod, Finset.prod_congr rfl h2]
    simp
  have hgne : g ≠ 0 := by
    intro h
    rw [h, leadingCoeff_zero] at hglead
    exact pow_ne_zero _ hQ0 hglead.symm
  have hgeval : ∀ i ∈ s, eval (v i) g
      = (Q - 1) * v i * ∏ j ∈ s.erase i, (Q * v i - v j) := by
    intro i hi
    rw [hg, eval_prod, ← Finset.mul_prod_erase s _ hi]
    simp only [eval_sub, eval_mul, eval_C, eval_X]
    ring
  -- the two constant terms agree
  have hc : g.coeff 0 = f.coeff 0 := by
    rw [coeff_zero_eq_eval_zero, coeff_zero_eq_eval_zero, hf, hg, eval_prod, eval_prod]
    simp
  have hcne : f.coeff 0 ≠ 0 := by
    rw [coeff_zero_eq_eval_zero, hf, eval_prod]
    simp only [eval_sub, eval_X, eval_C, zero_sub]
    exact Finset.prod_ne_zero_iff.mpr fun j hj => neg_ne_zero.mpr (hv0 j hj)
  -- `divX` bookkeeping
  have hevalDivX : ∀ (p : F[X]) (x : F), x * eval x (divX p) + p.coeff 0 = eval x p := by
    intro p x
    have h : eval x (X * divX p) + eval x (C (p.coeff 0)) = eval x p := by
      rw [← eval_add, X_mul_divX_add p]
    rw [eval_mul, eval_X, eval_C] at h
    exact h
  have hdivfdeg : (divX f).degree < (s.card : WithBot ℕ) := by
    rw [← hfdeg, ← degree_eq_natDegree hfne]
    exact degree_divX_lt hfne
  have hdivgdeg : (divX g).degree < (s.card : WithBot ℕ) := by
    rw [← hgdeg, ← degree_eq_natDegree hgne]
    exact degree_divX_lt hgne
  have hcoefff : (divX f).coeff (s.card - 1) = 1 := by
    rw [coeff_divX, Nat.sub_add_cancel hcard, ← hfdeg, coeff_natDegree]
    exact hfm
  have hcoeffg : (divX g).coeff (s.card - 1) = Q ^ s.card := by
    rw [coeff_divX, Nat.sub_add_cancel hcard, ← hgdeg, coeff_natDegree, hglead, hgdeg]
  -- the two node values
  have hAf : ∀ i ∈ s, eval (v i) (divX f) = -(f.coeff 0) / v i := by
    intro i hi
    have hvi : v i ≠ 0 := hv0 i hi
    have h : v i * eval (v i) (divX f) + f.coeff 0 = 0 := by
      rw [hevalDivX f (v i)]; exact hfeval i hi
    field_simp
    linear_combination h
  have hAg : ∀ i ∈ s, eval (v i) (divX g)
      = (Q - 1) * (∏ j ∈ s.erase i, (Q * v i - v j)) + -(f.coeff 0) / v i := by
    intro i hi
    have hvi : v i ≠ 0 := hv0 i hi
    have h : v i * eval (v i) (divX g) + f.coeff 0
        = (Q - 1) * v i * ∏ j ∈ s.erase i, (Q * v i - v j) := by
      rw [← hc, hevalDivX g (v i)]; exact hgeval i hi
    field_simp
    linear_combination h
  -- assemble
  have hA := sum_eval_div_prod_eq_coeff hv hdivfdeg
  rw [hcoefff] at hA
  have hB := sum_eval_div_prod_eq_coeff hv hdivgdeg
  rw [hcoeffg] at hB
  have hBsplit : ∑ i ∈ s, eval (v i) (divX g) / (∏ j ∈ s.erase i, (v i - v j))
      = (Q - 1) * (∑ i ∈ s, ∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j))
        + ∑ i ∈ s, eval (v i) (divX f) / (∏ j ∈ s.erase i, (v i - v j)) := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i hi => ?_
    rw [hAg i hi, hAf i hi, Finset.prod_div_distrib, add_div]
    ring
  rw [hBsplit, hA] at hB
  have hQ1' : Q - 1 ≠ 0 := sub_ne_zero.mpr hQ1
  refine mul_left_cancel₀ hQ1' ?_
  rw [sub_one_mul_geom_sum]
  linear_combination hB

/-- **Branching, for any weight family whose box-addition ratio is the `q`-ratio.**

If `w i` — the weight of "`μ` with a box added in row `i`" — is `W`, the weight of `μ`, times the
`i`-th `q`-ratio, then `∑_i w i = [|s|]_Q · W`.  That is the branching identity, and this is the
form in which `sum_prod_qratio` delivers it.

The hypothesis `hw` is the one remaining input, and it is a genuine sub-hypothesis rather than a
restatement of the conclusion: it is the classical fact that the level-`r` principal specialisation
is the Vandermonde ratio in the shifted parts `x_i = Q^{μ_i + r − i}`, from which the box-addition
ratio follows because adding a box to row `i` sends `x_i ↦ Q·x_i` and fixes every other `x_j`.
Establishing `hw` for `QBeta.WenzlWeight.schurPrincipal` — equivalently, the `q`-analogue of the
Frame–Robinson–Thrall hook-length identity relating `∏_c (1 − Q^{h(c)})` to the `x_i` — is what
still stands between this and general-`r` branching for the corpus weight.  Tracked on bean
`qou-j7ln`; it is *not* stated here as a `sorry`. -/
theorem sum_eq_bracket_mul_of_qratio_scaling {s : Finset ι} {v : ι → F} (hv : Set.InjOn v s)
    (hv0 : ∀ i ∈ s, v i ≠ 0) {Q : F} (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (w : ι → F) (W : F)
    (hw : ∀ i ∈ s, w i = (∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j)) * W) :
    ∑ i ∈ s, w i = (∑ k ∈ Finset.range s.card, Q ^ k) * W := by
  rw [Finset.sum_congr rfl hw, ← Finset.sum_mul, sum_prod_qratio hv hv0 hQ0 hQ1]

/-! ## The weighted node sum

The Markov property needs the `q`-ratio sum **weighted** by one more factor — the seminormal
(Hoefsmit) entry, which in node coordinates is `Q·v_i/(Q·v_i − v_b)` for a distinguished node `b`.
Remarkably the weighted sum is no harder: the extra factor cancels the `j = b` term of the ratio's
numerator, and what is left is `sum_eval_div_prod_eq_coeff` applied to a **degree `|s|−1`**
polynomial — no `divX` subtraction, and, unlike the branching case, no separate treatment of `i = b`.
-/

/-- **The weighted `q`-ratio node sum.**

`∑_{i ∈ s} (∏_{j≠i} (Q·v_i − v_j)/(v_i − v_j)) · Q·v_i/(Q·v_i − v_b) = Q^{|s|}/(Q − 1)`.

The weight is exactly what the seminormal entry contributes to the Markov condition, and the whole
sum collapses to the top coefficient of `∏_{j ≠ b}(Q·t − v_j)`, which is `Q^{|s|−1}`.

**`i = b` needs no special case.**  For `i ≠ b` the weight's denominator cancels the `j = b` factor
of the numerator; at `i = b` that factor is absent but the weight is the constant `Q/(Q−1)`, and the
two land on the same expression.  I first thought this case broke the uniform shape — it does not,
and the appearance that it did came from including the `j = i` factor, which the ratio's numerator
does not have.

**`hne` is not decoration.**  Without it a term can be `0/0`: `Q·v_i = v_b` makes the ratio's
numerator vanish *and* the weight's denominator vanish, and the two sides then disagree.  In the
intended application `s` indexes the rows that admit a box, where `β_b = β_i + 1` is impossible
precisely because row `i` admits one — so the hypothesis is discharged by addability, and the
degenerate case is the one the corner identity excludes by summing over addable cells only. -/
theorem sum_prod_qratio_weighted {s : Finset ι} {v : ι → F} (hv : Set.InjOn v s)
    (hv0 : ∀ i ∈ s, v i ≠ 0) {Q : F} (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) {b : ι} (hb : b ∈ s)
    (hne : ∀ i ∈ s, i ≠ b → Q * v i - v b ≠ 0) :
    (∑ i ∈ s, (∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j)) * (Q * v i / (Q * v i - v b)))
      = Q ^ s.card / (Q - 1) := by
  classical
  have hQ1' : Q - 1 ≠ 0 := sub_ne_zero.mpr hQ1
  have hcard : 1 ≤ s.card := Finset.card_pos.mpr ⟨b, hb⟩
  -- the interpolated polynomial, of degree `|s| − 1`
  set h : F[X] := ∏ j ∈ s.erase b, (C Q * X - C (v j)) with hh
  have hfac : ∀ j : ι, (C Q * X - C (v j) : F[X]) = C Q * X + C (-(v j)) := by
    intro j; rw [map_neg]; ring
  have hfacne : ∀ j : ι, (C Q * X - C (v j) : F[X]) ≠ 0 := by
    intro j hzero
    have hd := natDegree_linear (a := Q) (b := -(v j)) hQ0
    rw [← hfac j, hzero] at hd
    simp at hd
  have hdeg : h.natDegree = s.card - 1 := by
    have h1 : ∀ j ∈ s.erase b, (C Q * X - C (v j) : F[X]).natDegree = 1 := by
      intro j _; rw [hfac j]; exact natDegree_linear hQ0
    rw [hh, natDegree_prod _ _ fun j _ => hfacne j, Finset.sum_congr rfl h1]
    simp [Finset.card_erase_of_mem hb]
  have hlead : h.leadingCoeff = Q ^ (s.card - 1) := by
    have h2 : ∀ j ∈ s.erase b, (C Q * X - C (v j) : F[X]).leadingCoeff = Q := by
      intro j _; rw [hfac j]; exact leadingCoeff_linear hQ0
    rw [hh, leadingCoeff_prod, Finset.prod_congr rfl h2]
    simp [Finset.card_erase_of_mem hb]
  have hne0 : h ≠ 0 := fun hz => by
    rw [hz, leadingCoeff_zero] at hlead
    exact pow_ne_zero _ hQ0 hlead.symm
  have hdegree : h.degree < (s.card : WithBot ℕ) := by
    rw [degree_eq_natDegree hne0, hdeg]
    exact_mod_cast Nat.sub_lt (Finset.card_pos.mpr ⟨b, hb⟩) one_pos
  -- termwise: every summand is `Q/(Q−1)` times a residue term
  have hterm : ∀ i ∈ s,
      (∏ j ∈ s.erase i, (Q * v i - v j) / (v i - v j)) * (Q * v i / (Q * v i - v b))
        = Q / (Q - 1) * (eval (v i) h / ∏ j ∈ s.erase i, (v i - v j)) := by
    intro i hi
    have hvi : v i ≠ 0 := hv0 i hi
    have hev : eval (v i) h = ∏ j ∈ s.erase b, (Q * v i - v j) := by
      rw [hh, eval_prod]
      exact Finset.prod_congr rfl fun j _ => by simp
    rw [Finset.prod_div_distrib, hev]
    by_cases hib : i = b
    · subst hib
      have hself : Q * v i - v i = (Q - 1) * v i := by ring
      rw [hself]
      field_simp
    · -- peel the `j = b` factor out of both products
      have hbe : b ∈ s.erase i := Finset.mem_erase.mpr ⟨fun hc => hib hc.symm, hb⟩
      have hie : i ∈ s.erase b := Finset.mem_erase.mpr ⟨hib, hi⟩
      have hnum : (∏ j ∈ s.erase i, (Q * v i - v j))
          = (Q * v i - v b) * ∏ j ∈ (s.erase i).erase b, (Q * v i - v j) :=
        (Finset.mul_prod_erase _ _ hbe).symm
      have hnum' : (∏ j ∈ s.erase b, (Q * v i - v j))
          = (Q * v i - v i) * ∏ j ∈ (s.erase b).erase i, (Q * v i - v j) :=
        (Finset.mul_prod_erase _ _ hie).symm
      have hswap : (s.erase i).erase b = (s.erase b).erase i := Finset.erase_right_comm
      rw [hnum, hnum', hswap]
      have hdne : (∏ j ∈ s.erase i, (v i - v j)) ≠ 0 :=
        Finset.prod_ne_zero_iff.mpr fun j hj => sub_ne_zero.mpr fun hc =>
          Finset.ne_of_mem_erase hj (hv (Finset.mem_of_mem_erase hj) hi hc.symm)
      have hself : Q * v i - v i = (Q - 1) * v i := by ring
      have hnb : Q * v i - v b ≠ 0 := hne i hi hib
      rw [hself]
      field_simp
  rw [Finset.sum_congr rfl hterm, ← Finset.mul_sum,
    sum_eval_div_prod_eq_coeff hv hdegree, ← hdeg, coeff_natDegree, hlead]
  field_simp
  rw [← pow_succ']
  congr 1
  omega

end QOU.Mathlib
