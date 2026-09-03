/-
  **The height of a generalized Wronskian**, composed end to end.

  Bean `qou-4lbh`.

  ⚠ Unlike its two dependencies this module is **not** Mathlib-only: it imports
  `QOU/Mathlib/MvGenWronskian.lean` (for `mvGenWronskian`, `pderivList`, `coeff_pderiv` and
  the two per-entry bounds) and `QOU/Mathlib/MvPolynomialHeight.lean` (for `abs_coeff_det_le`).
  Both of those *are* Mathlib-only, so the three lift together; this one cannot go upstream on
  its own because `mvGenWronskian` is not a Mathlib notion.

  ═══ WHAT THIS CLOSES ═══

  The previous state of this arc was a stack of true lemmas that *looked* like a finished
  argument: an entry height bound, an entry support bound, a determinant bound — and no
  statement anywhere actually bounding a Wronskian.  The note in `SeparatedHeight.lean` said
  so.  `abs_coeff_mvGenWronskian_le` below is that statement:

      H(mvGenWronskian D f)  ≤  m! · (S · (d^L · B))^m

  for `f : Fin m → MvPolynomial σ ℤ` with support sizes at most `S`, degrees at most `d` in
  every variable, heights at most `B`, and operator lists `D i` of length at most `L`.

  Where each factor comes from:

  * `d^L` — each `pderiv` multiplies a coefficient by an exponent, bounded by the degree
    (`abs_coeff_pderiv_le`), and `pderivList` applies at most `L` of them.  `degreeOf` does
    not grow under differentiation (`degreeOf_pderivList_le`), so one `d` serves every step.
  * `S` — the antidiagonal cost of each multiplication in the Leibniz expansion.  Support does
    not grow under differentiation either (`card_support_pderivList_le`), so the entries
    inherit `S` from `f` unchanged.
  * `m!` — the number of permutations.

  ═══ ⚠ WHAT IT DOES NOT GIVE ═══

  This bounds a Wronskian's height in terms of the data of the `f`.  It is **not** Roth's
  lemma, and it is not the induction on the number of variables — that is still open, and is
  now the only structural gap left in the arc.  See bean `qou-4lbh`.
-/
import QOU.Mathlib.MvGenWronskian
import QOU.Mathlib.MvPolynomialHeight
import Mathlib.Data.Nat.Choose.Bounds
import Mathlib.Data.Nat.Factorial.BigOperators

namespace MvPolynomial

variable {σ : Type*}

/-- **Iterated differentiation does not enlarge the support.**  The list form of
`card_support_pderiv_le`. -/
theorem card_support_pderivList_le [DecidableEq σ] (l : List σ) (g : MvPolynomial σ ℤ) :
    (pderivList l g).support.card ≤ g.support.card := by
  induction l generalizing g with
  | nil => simp [pderivList]
  | cons j l' ih =>
      rw [pderivList_cons]
      exact le_trans (card_support_pderiv_le j (pderivList l' g)) (ih g)

/-- **`H(pderivList l g) ≤ d^{|l|} · H(g)`** when every `degreeOf j g ≤ d`.

Each step costs one factor `d`, and crucially the *same* `d` works at every step: `degreeOf`
does not grow under differentiation, so the degree bound assumed for `g` is inherited by every
intermediate derivative.  Without that the bound would degrade along the list. -/
theorem abs_coeff_pderivList_le [DecidableEq σ] {g : MvPolynomial σ ℤ} {d B : ℤ}
    (hd1 : 1 ≤ d) (hB0 : 0 ≤ B)
    (hd : ∀ j, (degreeOf j g : ℤ) ≤ d) (hB : ∀ n, |coeff n g| ≤ B)
    (l : List σ) (n : σ →₀ ℕ) :
    |coeff n (pderivList l g)| ≤ d ^ l.length * B := by
  induction l generalizing n with
  | nil => simpa [pderivList] using hB n
  | cons j l' ih =>
      have hdeg : ((degreeOf j (pderivList l' g) : ℕ) : ℤ) ≤ d := by
        refine le_trans ?_ (hd j)
        exact_mod_cast degreeOf_pderivList_le j l' g
      have hstep := abs_coeff_pderiv_le (g := pderivList l' g)
        (B := d ^ l'.length * B) (fun m => ih m) j n
      rw [pderivList_cons]
      refine le_trans hstep ?_
      have h0 : (0 : ℤ) ≤ d ^ l'.length * B :=
        mul_nonneg (pow_nonneg (le_trans zero_le_one hd1) _) hB0
      calc ((degreeOf j (pderivList l' g) : ℕ) : ℤ) * (d ^ l'.length * B)
          ≤ d * (d ^ l'.length * B) := mul_le_mul_of_nonneg_right hdeg h0
        _ = d ^ (l'.length + 1) * B := by rw [pow_succ]; ring

/-- **The height of a generalized Wronskian:**

    H(mvGenWronskian D f)  ≤  m! · (S · (d^L · B))^m

for `f : Fin m → MvPolynomial σ ℤ` whose supports have size at most `S`, whose degrees in
every variable are at most `d`, and whose heights are at most `B`, with each operator list
`D i` of length at most `L`.

This is the composite the arc had been assembling in pieces.  Each matrix entry is
`pderivList (D i) (f j)`, so `abs_coeff_pderivList_le` bounds its height by `d^{|D i|}·B ≤ d^L·B`
and `card_support_pderivList_le` keeps its support at `S`; `abs_coeff_det_le` then does the
Leibniz expansion.

The hypotheses `1 ≤ S`, `1 ≤ d`, `0 ≤ B` are not restrictive — any bound can be raised to meet
them — and they are what let the result be stated as a clean power rather than a product of
per-index factors. -/
theorem abs_coeff_mvGenWronskian_le [DecidableEq σ] {m L : ℕ} {S d B : ℤ}
    (hS1 : 1 ≤ S) (hd1 : 1 ≤ d) (hB0 : 0 ≤ B)
    (D : Fin m → List σ) (f : Fin m → MvPolynomial σ ℤ)
    (hS : ∀ j, ((f j).support.card : ℤ) ≤ S)
    (hd : ∀ i j, (degreeOf i (f j) : ℤ) ≤ d)
    (hB : ∀ j n, |coeff n (f j)| ≤ B)
    (hL : ∀ i, (D i).length ≤ L)
    (n : σ →₀ ℕ) :
    |coeff n (mvGenWronskian D f)| ≤ (m.factorial : ℤ) * (S * (d ^ L * B)) ^ m := by
  classical
  have hd0 : (0 : ℤ) ≤ d := le_trans zero_le_one hd1
  have hentryS : ∀ i j, ((mvWronskianMatrix D f i j).support.card : ℤ) ≤ S := by
    intro i j
    rw [mvWronskianMatrix_apply]
    refine le_trans ?_ (hS j)
    exact_mod_cast card_support_pderivList_le (D i) (f j)
  have hentryB : ∀ i j, ∀ n, |coeff n (mvWronskianMatrix D f i j)| ≤ d ^ L * B := by
    intro i j n
    rw [mvWronskianMatrix_apply]
    refine le_trans (abs_coeff_pderivList_le hd1 hB0 (fun k => hd k j) (hB j) (D i) n) ?_
    exact mul_le_mul_of_nonneg_right (pow_le_pow_right₀ hd1 (hL i)) hB0
  have hdet := abs_coeff_det_le hS1 (mul_nonneg (pow_nonneg hd0 L) hB0)
    (mvWronskianMatrix D f) hentryS hentryB n
  rw [mvGenWronskian]
  rwa [Fintype.card_fin] at hdet

/-! ### Non-vacuity guard

`abs_coeff_mvGenWronskian_le` carries eight hypotheses.  This instantiates all of them at
once — `m = 1`, `f = X`, `D = ![[]]`, `S = d = B = 1`, `L = 0` — so the theorem cannot be
true merely because its premises are unsatisfiable. -/

example (n : Unit →₀ ℕ) :
    |coeff n (mvGenWronskian (fun _ : Fin 1 => ([] : List Unit))
        (fun _ => (X () : MvPolynomial Unit ℤ)))|
      ≤ ((1 : ℕ).factorial : ℤ) * (1 * (1 ^ 0 * 1)) ^ 1 := by
  refine abs_coeff_mvGenWronskian_le (S := 1) (d := 1) (B := 1) (L := 0)
    le_rfl le_rfl zero_le_one _ _ ?_ ?_ ?_ (fun _ => le_rfl) n
  · intro j; simp [support_X]
  · intro i j; simp [degreeOf_X]
  · intro j m; rw [coeff_X']; split_ifs <;> simp

/-! ### The `D i j` shape — the height side's missing composite

⚠ **This is correction 5's pattern again, on the other chain.**  There the *index* side had no
counterpart to a height composite; here the *height* side has none to an index composite.

`abs_coeff_mvGenWronskian_le` above is for `D : Fin m → List σ` — one operator list per **row**,
applied to a different function per column.  Mahler §13's determinant is a different shape:
`D : Fin r → Fin r → List σ`, a different operator for each **entry**, all applied to the same
`P`.  The index side has that composite (`sum_max_le_index_det`,
`QOU/Mathlib/WronskianIndex.lean`); the height side did not, and the gap went unnoticed for the
same reason as last time — each side looked complete from its own end.

The composite itself is short: `abs_coeff_det_le` for the determinant, and
`card_support_pderivList_le` / `abs_coeff_pderivList_le` for the entries. -/

/-- **`H(det (∂_{D i j} P)) ≤ r! · (S · (d^L · B))^r`.**

The height counterpart of `sum_max_le_index_det`, for the matrix Mahler §13 actually forms:
one operator list per *entry*, all applied to a single `P`. -/
theorem abs_coeff_det_pderivList_le [DecidableEq σ] {r L : ℕ} {S d B : ℤ}
    (hS1 : 1 ≤ S) (hd1 : 1 ≤ d) (hB0 : 0 ≤ B)
    (D : Fin r → Fin r → List σ) (P : MvPolynomial σ ℤ)
    (hS : ((P.support.card : ℕ) : ℤ) ≤ S)
    (hd : ∀ j, (degreeOf j P : ℤ) ≤ d)
    (hB : ∀ n, |coeff n P| ≤ B)
    (hL : ∀ i j, (D i j).length ≤ L)
    (n : σ →₀ ℕ) :
    |coeff n (Matrix.of fun i j => pderivList (D i j) P).det|
      ≤ (r.factorial : ℤ) * (S * (d ^ L * B)) ^ r := by
  have hdL : (0 : ℤ) ≤ d ^ L * B :=
    mul_nonneg (pow_nonneg (by linarith) L) hB0
  have h := abs_coeff_det_le (S := S) (B := d ^ L * B) hS1 hdL
    (Matrix.of fun i j => pderivList (D i j) P)
    (fun i j => le_trans (by
      exact_mod_cast card_support_pderivList_le (D i j) P) hS)
    (fun i j m => le_trans (abs_coeff_pderivList_le hd1 hB0 hd hB (D i j) m)
      (mul_le_mul_of_nonneg_right (pow_le_pow_right₀ hd1 (hL i j)) hB0))
    n
  simpa using h


/-- **The height bound made uniform in the family.**

`abs_coeff_det_pderivList_le` needs a bound `L` on the operator lists' lengths.  For the
family the induction step actually forms — `D i j = (Dx i)⊞(Dy j)` with `Dx`, `Dy` of bounded
order — that bound is available from `r` alone: `|Dx i| ≤ i < r` and `|Dy j| ≤ j < r`, so every
entry's list has length at most `2r`.

⚠ This is what makes `hres` assemblable.  `hres` quantifies over the families realising a
separated representation, so its auxiliary data — the height bound `B` in particular — has to
be chosen **before** the family is known.  A bound depending on the individual `D i j` would
be useless there; one depending only on `r` and `P` is not. -/
theorem abs_coeff_det_sepFamily_le {τ : Type*} [DecidableEq σ] [DecidableEq τ]
    [DecidableEq (σ ⊕ τ)] {r : ℕ} {S d B : ℤ}
    (hS1 : 1 ≤ S) (hd1 : 1 ≤ d) (hB0 : 0 ≤ B)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (hDx : ∀ i, (Dx i).length ≤ (i : ℕ)) (hDy : ∀ j, (Dy j).length ≤ (j : ℕ))
    (P : MvPolynomial (σ ⊕ τ) ℤ)
    (hS : ((P.support.card : ℕ) : ℤ) ≤ S)
    (hd : ∀ j, (degreeOf j P : ℤ) ≤ d)
    (hB : ∀ n, |coeff n P| ≤ B)
    (n : (σ ⊕ τ) →₀ ℕ) :
    |coeff n (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det|
      ≤ (r.factorial : ℤ) * (S * (d ^ (2 * r) * B)) ^ r := by
  refine abs_coeff_det_pderivList_le hS1 hd1 hB0
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P hS hd hB (fun i j => ?_) n
  have hi := i.isLt
  have hj := j.isLt
  have h1 := hDx i
  have h2 := hDy j
  simp only [List.length_append, List.length_map]
  omega


/-! ### ⚠⚠ Correction twenty-one — this file bounds the wrong operator

§7 (doc pp. 85–86) bounds the auxiliary polynomial by a **majorant**,
`A ≪ a(1+x₁)^{r₁}…(1+x_m)^{r_m}`, differentiates it, and reads off

    A_{j₁…j_m} ≪ a·binom(r₁,j₁)…binom(r_m,j_m)·(1+x₁)^{r₁−j₁}…(1+x_m)^{r_m−j_m}
    binom(r,j) ≤ 2^r,   so   Δ_{μν}A ≪ 2^{r₁+…+r_m}·a·∏(1+x_h)^{r_h}
    W ≪ n!·{2^{Σ r_h}·a·∏(1+x_h)^{r_h}}^n

**The binomial with no `j!` is the tell.**  For an ordinary derivative the coefficient factor is
`j!·binom(i,j)` (see `coeff_pderiv_iterate` below); Mahler's is `binom(r_h,j_h)` alone.  So his
`Δ` is the **divided (Hasse) derivative**, and `mvGenWronskian` — a fold of `MvPolynomial.pderiv`
— is not it.

The two determinants differ by the scalar `(∏_i (Dx i)!)·(∏_j (Dy j)!)`, because the operator on
entry `(i,j)` splits as a row part and a column part.  That is free for the *index*
(`index_C_mul`) and free for the dependence criterion.  It is **not** free for the height, and
§12 spends its budget `2^{(2m+1)ρ₁}` exactly — clause 3 is calibrated to equality at the floor —
so there is nothing to absorb it with.

That is why `abs_coeff_det_sepFamily_le`'s `d^{2n²}` does not fit §12's `2^{2nΣr_h}`: **the
`d^{2n²}` is the factorials, not a loose estimate.**

The lemma below is the first stone of the repair: the exact coefficient formula for iterated
`pderiv`, from which the factorial separates cleanly and §7's `2^{d}` appears.

⚠ It rests on `MvGenWronskian.coeff_pderiv`, which this arc already had.  A first draft of this
section re-proved that lemma from scratch — the **second** self-duplication in this session (the
first was `map_pUnitAlgEquiv`, already present as `pUnitAlgEquiv_map`).  The `beans` discipline's
"check before you create" applies to lemmas too, and a duplicate type-checks.
-/

/-- **The coefficient of an iterated partial derivative**, exactly:

    coeff n (∂ⱼ^k g) = (n_j + 1)(n_j + 2)⋯(n_j + k) · coeff (n + k·eⱼ) g

The product is `k!·binom(n_j + k, k)`.  **The `k!` is exactly what separates `∂^k` from the
divided derivative**, and `binom(n_j+k, k) ≤ 2^{n_j+k}` is §7's `2^r`. -/
theorem coeff_pderiv_iterate {R : Type*} [CommRing R] [DecidableEq σ] (j : σ) (k : ℕ)
    (g : MvPolynomial σ R) (n : σ →₀ ℕ) :
    coeff n ((pderiv j)^[k] g)
      = (∏ i ∈ Finset.range k, ((n j + 1 + i : ℕ) : R))
          * coeff (n + Finsupp.single j k) g := by
  classical
  induction k generalizing n g with
  | zero => simp
  | succ k ih =>
      rw [Function.iterate_succ_apply', coeff_pderiv, ih]
      have hnj : (n + Finsupp.single j 1 : σ →₀ ℕ) j = n j + 1 := by simp
      have hadd : n + Finsupp.single j 1 + Finsupp.single j k = n + Finsupp.single j (k + 1) := by
        rw [add_assoc, ← Finsupp.single_add, Nat.add_comm 1 k]
      rw [hnj, hadd, ← mul_assoc]
      congr 1
      rw [Finset.prod_range_succ']
      push_cast
      rw [mul_comm]
      congr 1
      · exact Finset.prod_congr rfl fun i _ => by ring
      · norm_num

/-- The multi-index a list of variables differentiates by: `listIdx [x,y,x] = 2·e_x + e_y`. -/
noncomputable def listIdx : List σ → (σ →₀ ℕ)
  | [] => 0
  | j :: l => Finsupp.single j 1 + listIdx l

@[simp] theorem listIdx_nil : listIdx ([] : List σ) = 0 := rfl

@[simp] theorem listIdx_cons (j : σ) (l : List σ) :
    listIdx (j :: l) = Finsupp.single j 1 + listIdx l := rfl

/-- The integer `∂^l` multiplies the coefficient at `n` by.

Defined by the recursion `∂ⱼ` itself performs — `coeff n (∂ⱼ f) = (nⱼ+1)·coeff (n+eⱼ) f` — so
`coeff_pderivList` below is an immediate induction.  In closed form it is
`∏_h (n_h + t_h)!/(n_h)!` with `t = listIdx l`, hence `Fac(l)·∏_h binom(n_h+t_h, t_h)` where
`Fac(l) = ∏_h (t_h)!`; that factorisation is what correction twenty-one needs and is **not yet
proved** — see the note below. -/
noncomputable def listFactor : List σ → (σ →₀ ℕ) → ℕ
  | [], _ => 1
  | j :: l, n => (n j + 1) * listFactor l (n + Finsupp.single j 1)

@[simp] theorem listFactor_nil (n : σ →₀ ℕ) : listFactor ([] : List σ) n = 1 := rfl

@[simp] theorem listFactor_cons (j : σ) (l : List σ) (n : σ →₀ ℕ) :
    listFactor (j :: l) n = (n j + 1) * listFactor l (n + Finsupp.single j 1) := rfl

/-- **The coefficient of an iterated partial derivative along a list, exactly.**

    coeff n (∂^l g) = listFactor l n · coeff (n + listIdx l) g

The generalisation of `coeff_pderiv_iterate` from one variable to a list, and the handle the
rest of correction twenty-one hangs on: both the divisibility `Fac(l) ∣ listFactor l n` and the
bound `listFactor l n ≤ Fac(l)·2^{Σ d_h}` are statements about `listFactor` alone, with the
polynomial gone. -/
theorem coeff_pderivList [DecidableEq σ] {R : Type*} [CommRing R] (l : List σ)
    (g : MvPolynomial σ R) (n : σ →₀ ℕ) :
    coeff n (pderivList l g) = ((listFactor l n : ℕ) : R) * coeff (n + listIdx l) g := by
  induction l generalizing n with
  | nil => simp
  | cons j l ih =>
      have hcons : pderivList (j :: l) g = pderiv j (pderivList l g) := rfl
      rw [hcons, coeff_pderiv, ih, listFactor_cons, listIdx_cons, ← add_assoc, ← mul_assoc]
      push_cast
      ring

/-- **`listFactor` at a single variable** agrees with `coeff_pderiv_iterate`'s product.

The bridge that lets the one-variable bound be reused: `∂ⱼ^k` is `∂^l` for the constant list. -/
theorem listFactor_replicate (j : σ) (k : ℕ) (n : σ →₀ ℕ) :
    listFactor (List.replicate k j) n = ∏ i ∈ Finset.range k, (n j + 1 + i) := by
  induction k generalizing n with
  | zero => simp
  | succ k ih =>
      rw [List.replicate_succ, listFactor_cons, ih, Finset.prod_range_succ']
      have hnj : (n + Finsupp.single j 1 : σ →₀ ℕ) j = n j + 1 := by simp
      rw [hnj, Nat.mul_comm]
      congr 1
      exact Finset.prod_congr rfl fun i _ => by omega

/-- **`listFactor` in closed form**, as a product over the variables.

    listFactor l n = ∏_h ∏_{i<t_h} (n_h + 1 + i),   t = listIdx l

⚠ The interleaving is invisible: `∂ⱼ` applied when `n` has already been shifted by `e_h` for
`h ≠ j` still sees the same `n_j`, so the factors for each variable are consecutive regardless
of the order the list interleaves them.  That is why a *list* factor equals a *multiset* one.

`s` is any `Finset` containing the list's variables — no `Fintype σ` needed, and the caller
picks whatever ambient finset is convenient. -/
theorem listFactor_eq_prod [DecidableEq σ] (s : Finset σ) (l : List σ) :
    (∀ h ∈ l, h ∈ s) → ∀ n : σ →₀ ℕ,
      listFactor l n = ∏ h ∈ s, ∏ i ∈ Finset.range ((listIdx l) h), (n h + 1 + i) := by
  induction l with
  | nil => intro _ n; simp
  | cons j l ih =>
      intro hs n
      have hjs : j ∈ s := hs j (by simp)
      have hl : ∀ h ∈ l, h ∈ s := fun h hh => hs h (List.mem_cons_of_mem _ hh)
      rw [listFactor_cons, ih hl,
        ← Finset.mul_prod_erase s (fun h => ∏ i ∈ Finset.range ((listIdx l) h),
          ((n + Finsupp.single j 1 : σ →₀ ℕ) h + 1 + i)) hjs,
        ← Finset.mul_prod_erase s (fun h => ∏ i ∈ Finset.range ((listIdx (j :: l)) h),
          (n h + 1 + i)) hjs,
        ← mul_assoc]
      congr 1
      · have hnj : (n + Finsupp.single j 1 : σ →₀ ℕ) j = n j + 1 := by simp
        have htj : (listIdx (j :: l)) j = (listIdx l) j + 1 := by
          simp [listIdx_cons, Finsupp.add_apply]
          omega
        rw [hnj, htj, Finset.prod_range_succ', Nat.mul_comm]
        congr 1
        exact Finset.prod_congr rfl fun i _ => by omega
      · refine Finset.prod_congr rfl fun h hh => ?_
        have hne : h ≠ j := (Finset.mem_erase.mp hh).1
        have hz : (Finsupp.single j 1 : σ →₀ ℕ) h = 0 :=
          Finsupp.single_eq_of_ne hne
        have h1 : (n + Finsupp.single j 1 : σ →₀ ℕ) h = n h := by
          rw [Finsupp.add_apply, hz, Nat.add_zero]
        have h2 : (listIdx (j :: l)) h = (listIdx l) h := by
          rw [listIdx_cons, Finsupp.add_apply, hz, Nat.zero_add]
        rw [h1, h2]

/-- **`listFactor` factors as `Fac(l)·Binom`** — the whole content of correction twenty-one, in
one equation.

    listFactor l n = (∏_h t_h!) · (∏_h binom(n_h + t_h, t_h)),    t = listIdx l

The left factor is the discrepancy with Mahler's divided derivative; the right is what §7 bounds
by `2^{Σ r_h}`.  Everything else follows. -/
theorem listFactor_eq_factorial_mul [DecidableEq σ] (s : Finset σ) (l : List σ)
    (hs : ∀ h ∈ l, h ∈ s) (n : σ →₀ ℕ) :
    listFactor l n
      = (∏ h ∈ s, ((listIdx l) h).factorial) * ∏ h ∈ s, (n h + (listIdx l) h).choose ((listIdx l) h) := by
  rw [listFactor_eq_prod s l hs n, ← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun h _ => ?_
  rw [show (fun i => n h + 1 + i) = (fun i => (n h + 1) + i) from rfl,
    ← Nat.ascFactorial_eq_prod_range, Nat.ascFactorial_eq_factorial_mul_choose]

/-- **The factorial part divides.**  This is what makes the divided derivative *integral*, and
hence what lets `det` be divided by `(∏_i (Dx i)!)(∏_j (Dy j)!)` and stay in `ℤ[x]`. -/
theorem listFac_dvd_listFactor [DecidableEq σ] (s : Finset σ) (l : List σ)
    (hs : ∀ h ∈ l, h ∈ s) (n : σ →₀ ℕ) :
    (∏ h ∈ s, ((listIdx l) h).factorial) ∣ listFactor l n :=
  ⟨_, listFactor_eq_factorial_mul s l hs n⟩

/-- **§7's bound, for a list of variables.**

    listFactor l n ≤ (∏_h t_h!) · 2^{Σ_h d_h}      whenever  n_h + t_h ≤ d_h

The `2^{Σ_h d_h}` is §7's `2^{r₁+…+r_m}` exactly — its source is `binom(N,k) ≤ 2^N`, which is
the same inequality Mahler writes as `binom(r,j) ≤ Σ_j binom(r,j) = 2^r`. -/
theorem listFactor_le [DecidableEq σ] (s : Finset σ) (l : List σ) (hs : ∀ h ∈ l, h ∈ s)
    (n : σ →₀ ℕ) (d : σ → ℕ) (hd : ∀ h, n h + (listIdx l) h ≤ d h) :
    listFactor l n ≤ (∏ h ∈ s, ((listIdx l) h).factorial) * 2 ^ (∑ h ∈ s, d h) := by
  rw [listFactor_eq_factorial_mul s l hs n]
  refine Nat.mul_le_mul_left _ ?_
  calc ∏ h ∈ s, (n h + (listIdx l) h).choose ((listIdx l) h)
      ≤ ∏ h ∈ s, 2 ^ (d h) :=
        Finset.prod_le_prod' fun h _ =>
          le_trans (Nat.choose_le_two_pow _ _) (Nat.pow_le_pow_right (by norm_num) (hd h))
    _ = 2 ^ (∑ h ∈ s, d h) := by rw [Finset.prod_pow_eq_pow_sum]

/-- **The factorial divides every coefficient of `∂^l g`.**

So `∂^l = Fac(l)·(divided derivative)` at the level of coefficients, which is precisely the
statement that Mahler's `Δ` is integral and this arc's `∂^l` is `Fac(l)` times it. -/
theorem listFac_dvd_coeff_pderivList [DecidableEq σ] (s : Finset σ) (g : MvPolynomial σ ℤ)
    (l : List σ) (hs : ∀ h ∈ l, h ∈ s) (n : σ →₀ ℕ) :
    ((∏ h ∈ s, ((listIdx l) h).factorial : ℕ) : ℤ) ∣ coeff n (pderivList l g) := by
  rw [coeff_pderivList]
  exact Dvd.dvd.mul_right (Int.natCast_dvd_natCast.mpr (listFac_dvd_listFactor s l hs n)) _

/-- **§7's coefficient bound for `∂^l`** — the replacement for `abs_coeff_pderivList_le`.

    |coeff n (∂^l g)| ≤ (∏_h t_h!) · 2^{Σ_h d_h} · B

Against the old `d^{|l|}·B`, this separates the factorial and leaves §7's `2^{Σ r_h}`.  Dividing
through by `∏_h t_h!` — legitimate by `listFac_dvd_coeff_pderivList` — gives the divided
derivative's bound, which is the one §12's budget is calibrated for. -/
theorem abs_coeff_pderivList_le' [DecidableEq σ] (s : Finset σ) {g : MvPolynomial σ ℤ}
    {d : σ → ℕ} {B : ℤ} (hB0 : 0 ≤ B) (l : List σ) (hs : ∀ h ∈ l, h ∈ s)
    (hd : ∀ h, degreeOf h g ≤ d h) (hB : ∀ n, |coeff n g| ≤ B) (n : σ →₀ ℕ) :
    |coeff n (pderivList l g)|
      ≤ ((∏ h ∈ s, ((listIdx l) h).factorial : ℕ) : ℤ) * 2 ^ (∑ h ∈ s, d h) * B := by
  classical
  rw [coeff_pderivList, abs_mul]
  have hfac : (0 : ℤ) ≤ ((∏ h ∈ s, ((listIdx l) h).factorial : ℕ) : ℤ) * 2 ^ (∑ h ∈ s, d h) := by
    positivity
  by_cases hz : coeff (n + listIdx l) g = 0
  · rw [hz, abs_zero, mul_zero]
    exact mul_nonneg hfac hB0
  · have hmem : (n + listIdx l) ∈ g.support := mem_support_iff.mpr hz
    have hle : ∀ h, n h + (listIdx l) h ≤ d h := by
      intro h
      have h1 := monomial_le_degreeOf h hmem
      rw [Finsupp.add_apply] at h1
      exact le_trans h1 (hd h)
    have hPr : |((listFactor l n : ℕ) : ℤ)|
        ≤ ((∏ h ∈ s, ((listIdx l) h).factorial : ℕ) : ℤ) * 2 ^ (∑ h ∈ s, d h) := by
      rw [abs_of_nonneg (by positivity)]
      exact_mod_cast listFactor_le s l hs n d hle
    refine le_trans (mul_le_mul hPr (hB _) (abs_nonneg _) hfac) (le_of_eq ?_)
    ring

@[simp] theorem listIdx_append (l₁ l₂ : List σ) :
    listIdx (l₁ ++ l₂) = listIdx l₁ + listIdx l₂ := by
  induction l₁ with
  | nil => simp
  | cons j l ih => rw [List.cons_append, listIdx_cons, listIdx_cons, ih, add_assoc]

/-- **The row and column factorials divide the combined one.**

`m!·n! ∣ (m+n)!` per variable, so `Fac(l₁)·Fac(l₂) ∣ Fac(l₁ ++ l₂)`.  ⚠ No disjointness of the
two lists' variables is needed — that is the point of using divisibility rather than the
equality that *would* need it. -/
theorem listFac_mul_dvd_listFac_append [DecidableEq σ] (s : Finset σ) (l₁ l₂ : List σ) :
    (∏ h ∈ s, ((listIdx l₁) h).factorial) * (∏ h ∈ s, ((listIdx l₂) h).factorial)
      ∣ ∏ h ∈ s, ((listIdx (l₁ ++ l₂)) h).factorial := by
  rw [← Finset.prod_mul_distrib]
  refine Finset.prod_dvd_prod_of_dvd _ _ fun h _ => ?_
  rw [listIdx_append, Finsupp.add_apply]
  exact Nat.factorial_mul_factorial_dvd_factorial_add _ _

/-- **A row/column-factorising divisor of every entry divides the determinant.**

If `C (a i · b j)` divides entry `(i,j)`, then `C ((∏ a)·(∏ b))` divides `det` — because every
permutation term picks one entry per row and one per column, so `∏_i a i · b (σ i)` is
`(∏ a)(∏ b)` **independently of `σ`**.

This is what makes correction twenty-one's repair possible at all: the discrepancy between `∂^l`
and Mahler's `Δ^l` is a row factor times a column factor, and a determinant is exactly the
shape that turns such a thing into a single scalar. -/
theorem C_dvd_det_of_dvd_entries {ι : Type*} [Fintype ι] [DecidableEq ι]
    (M : Matrix ι ι (MvPolynomial σ ℤ)) (a b : ι → ℤ)
    (h : ∀ i j, C (a i * b j) ∣ M i j) :
    C ((∏ i, a i) * (∏ j, b j)) ∣ M.det := by
  classical
  rw [Matrix.det_apply]
  refine Finset.dvd_sum fun p _ => ?_
  have hsplit : (C ((∏ i, a i) * (∏ j, b j)) : MvPolynomial σ ℤ)
      = ∏ i, (C (a (p i) * b i) : MvPolynomial σ ℤ) := by
    rw [← map_prod, Finset.prod_mul_distrib, Equiv.prod_comp p a]
  have hprod : C ((∏ i, a i) * (∏ j, b j)) ∣ ∏ i, M (p i) i := by
    rw [hsplit]
    exact Finset.prod_dvd_prod_of_dvd _ _ fun i _ => h (p i) i
  rcases Int.units_eq_one_or (Equiv.Perm.sign p) with hs | hs <;> rw [hs] <;>
    simpa using hprod

/-- **§7's constant divides the separated family's determinant.**

    (∏_i Fac(Dx i)) · (∏_j Fac(Dy j))  ∣  det (∂^{Dx i ⊞ Dy j} P)

so the quotient — Mahler's `W`, built from divided derivatives — is an **integral** polynomial.
That quotient is the object §12 measures, its index is the same (`index_C_mul`: scaling does not
move the index), and its height is `2^{Θ(n² log n)}` smaller, which is exactly the gap correction
twenty-one identified between this arc's `mvGenWronskian` and Mahler's `W`. -/
theorem C_listFac_dvd_det_sepFamily {τ : Type*} [DecidableEq σ] [DecidableEq τ]
    [DecidableEq (σ ⊕ τ)] {r : ℕ} (s : Finset (σ ⊕ τ))
    (Dx : Fin r → List σ) (Dy : Fin r → List τ) (P : MvPolynomial (σ ⊕ τ) ℤ)
    (hx : ∀ i, ∀ h ∈ (Dx i).map Sum.inl, h ∈ s)
    (hy : ∀ j, ∀ h ∈ (Dy j).map Sum.inr, h ∈ s) :
    C ((∏ i, ((∏ h ∈ s, ((listIdx ((Dx i).map Sum.inl)) h).factorial : ℕ) : ℤ)) *
        (∏ j, ((∏ h ∈ s, ((listIdx ((Dy j).map Sum.inr)) h).factorial : ℕ) : ℤ)))
      ∣ (Matrix.of fun i j =>
          pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det := by
  refine C_dvd_det_of_dvd_entries _ _ _ fun i j => ?_
  have hmem : ∀ h ∈ (Dx i).map Sum.inl ++ (Dy j).map Sum.inr, h ∈ s := by
    intro h hh
    rcases List.mem_append.mp hh with h1 | h1
    · exact hx i h h1
    · exact hy j h h1
  rw [C_dvd_iff_dvd_coeff]
  intro n
  refine dvd_trans ?_ (listFac_dvd_coeff_pderivList s P _ hmem n)
  exact_mod_cast Int.natCast_dvd_natCast.mpr (listFac_mul_dvd_listFac_append s _ _)

/-- **`abs_coeff_prod_le` with per-factor bounds.**

`|coeff n (∏ Fᵢ)| ≤ S^{#s} · ∏ βᵢ` when `|coeff · Fᵢ| ≤ βᵢ`.  The uniform version is the case
`βᵢ ≡ B`; the point of the general one is that a *factorised* per-entry bound survives the
determinant expansion, which a uniform one cannot express.

⚠ Unlike `abs_coeff_prod_le`, this needs **no `1 ≤ S`** — the empty product is `1` and the bound
is `S^0·1 = 1`, so nothing forces `S` up.  A first draft carried `1 ≤ S`, copied from the uniform
version's signature without checking; the linter caught it.  That is the sixth unused hypothesis
this arc has acquired by transcribing a proof *route* rather than the proof. -/
theorem abs_coeff_prod_le' {ι : Type*} [DecidableEq ι] {S : ℤ}
    (F : ι → MvPolynomial σ ℤ) (β : ι → ℤ) :
    ∀ s : Finset ι, (∀ i ∈ s, ((F i).support.card : ℤ) ≤ S) →
      (∀ i ∈ s, ∀ n, |coeff n (F i)| ≤ β i) → ∀ n : σ →₀ ℕ,
      |coeff n (∏ i ∈ s, F i)| ≤ S ^ s.card * ∏ i ∈ s, β i := by
  classical
  intro s
  induction s using Finset.induction_on with
  | empty => intro _ _ n; simpa using abs_coeff_one_le n
  | @insert a t ha ih =>
      intro hS hB n
      rw [Finset.prod_insert ha, Finset.prod_insert ha, Finset.card_insert_of_notMem ha]
      have hSa : ((F a).support.card : ℤ) ≤ S := hS a (Finset.mem_insert_self a t)
      have hBa : ∀ m, |coeff m (F a)| ≤ β a := hB a (Finset.mem_insert_self a t)
      have hSt : ∀ i ∈ t, ((F i).support.card : ℤ) ≤ S :=
        fun i hi => hS i (Finset.mem_insert_of_mem hi)
      have hBt : ∀ i ∈ t, ∀ m, |coeff m (F i)| ≤ β i :=
        fun i hi => hB i (Finset.mem_insert_of_mem hi)
      refine le_trans (abs_coeff_mul_le hBa (fun m => ih hSt hBt m) n) ?_
      have hβa : (0 : ℤ) ≤ β a := le_trans (abs_nonneg _) (hBa 0)
      have hrest : (0 : ℤ) ≤ S ^ t.card * ∏ i ∈ t, β i :=
        le_trans (abs_nonneg _) (ih hSt hBt 0)
      calc ((F a).support.card : ℤ) * (β a * (S ^ t.card * ∏ i ∈ t, β i))
          ≤ S * (β a * (S ^ t.card * ∏ i ∈ t, β i)) :=
            mul_le_mul_of_nonneg_right hSa (mul_nonneg hβa hrest)
        _ = S ^ (t.card + 1) * (β a * ∏ i ∈ t, β i) := by rw [pow_succ]; ring

/-- **`abs_coeff_det_le` with a row-times-column per-entry bound.**

    |coeff n (det M)| ≤ (#ι)! · S^{#ι} · (∏ aᵢ)(∏ bⱼ)      when  |coeff · (M i j)| ≤ aᵢ·bⱼ

The mirror of `C_dvd_det_of_dvd_entries` on the size side, and for the same reason: every
permutation term picks one entry per row and one per column, so `∏_i a_{p i}·b_i` is
`(∏a)(∏b)` independently of `p`.

Together the two say that a determinant whose entries carry a factorised row/column constant
is *that constant* times something both integral and small — which is exactly the relationship
between this arc's `mvGenWronskian` and Mahler's `W`. -/
theorem abs_coeff_det_le' {ι : Type*} [Fintype ι] [DecidableEq ι] {S : ℤ}
    (M : Matrix ι ι (MvPolynomial σ ℤ)) (a b : ι → ℤ)
    (hS : ∀ i j, ((M i j).support.card : ℤ) ≤ S)
    (hB : ∀ i j, ∀ n, |coeff n (M i j)| ≤ a i * b j)
    (n : σ →₀ ℕ) :
    |coeff n M.det|
      ≤ ((Fintype.card ι).factorial : ℤ) * S ^ (Fintype.card ι) * ((∏ i, a i) * ∏ j, b j) := by
  classical
  have hsm : ∀ (p : Equiv.Perm ι) (q : MvPolynomial σ ℤ),
      |coeff n (Equiv.Perm.sign p • q)| = |coeff n q| := by
    intro p q
    rw [Units.smul_def, coeff_smul, smul_eq_mul, abs_mul]
    rcases Int.units_eq_one_or (Equiv.Perm.sign p) with h | h <;> rw [h] <;> simp
  have hterm : ∀ p : Equiv.Perm ι,
      |coeff n (Equiv.Perm.sign p • ∏ i, M (p i) i)|
        ≤ S ^ (Fintype.card ι) * ((∏ i, a i) * ∏ j, b j) := by
    intro p
    rw [hsm]
    have h := abs_coeff_prod_le' (σ := σ) (fun i => M (p i) i) (fun i => a (p i) * b i)
      Finset.univ (fun i _ => hS (p i) i) (fun i _ => hB (p i) i) n
    rw [Finset.card_univ] at h
    refine le_trans h (le_of_eq ?_)
    congr 1
    rw [Finset.prod_mul_distrib, Equiv.prod_comp p a]
  rw [Matrix.det_apply, coeff_sum]
  refine le_trans (Finset.abs_sum_le_sum_abs _ _) ?_
  refine le_trans (Finset.sum_le_card_nsmul _ _ _ (fun p _ => hterm p)) ?_
  rw [Finset.card_univ, Fintype.card_perm, nsmul_eq_mul, mul_assoc]

theorem listIdx_map_inl_apply_inr {τ : Type*} (l : List σ) (y : τ) :
    (listIdx (l.map (Sum.inl : σ → σ ⊕ τ))) (Sum.inr y) = 0 := by
  induction l with
  | nil => simp
  | cons a t ih =>
      rw [List.map_cons, listIdx_cons, Finsupp.add_apply, ih,
        Finsupp.single_eq_of_ne (by simp), Nat.zero_add]

theorem listIdx_map_inr_apply_inl {τ : Type*} (l : List τ) (x : σ) :
    (listIdx (l.map (Sum.inr : τ → σ ⊕ τ))) (Sum.inl x) = 0 := by
  induction l with
  | nil => simp
  | cons a t ih =>
      rw [List.map_cons, listIdx_cons, Finsupp.add_apply, ih,
        Finsupp.single_eq_of_ne (by simp), Nat.zero_add]

/-- **`Fac` splits across the `x`/`y` join** — here as an *equality*, because the two lists live
in disjoint variables.

`listFac_mul_dvd_listFac_append` gives only divisibility and needs no disjointness; the size side
needs the equality, and the separated family supplies it. -/
theorem listFac_append_map {τ : Type*} [DecidableEq σ] [DecidableEq τ] [DecidableEq (σ ⊕ τ)]
    (s : Finset (σ ⊕ τ)) (l₁ : List σ) (l₂ : List τ) :
    (∏ h ∈ s, ((listIdx ((l₁.map Sum.inl) ++ (l₂.map Sum.inr))) h).factorial)
      = (∏ h ∈ s, ((listIdx (l₁.map (Sum.inl : σ → σ ⊕ τ))) h).factorial) *
        (∏ h ∈ s, ((listIdx (l₂.map (Sum.inr : τ → σ ⊕ τ))) h).factorial) := by
  rw [← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun h _ => ?_
  rw [listIdx_append, Finsupp.add_apply]
  cases h with
  | inl x => rw [listIdx_map_inr_apply_inl, Nat.add_zero, Nat.factorial_zero, Nat.mul_one]
  | inr y => rw [listIdx_map_inl_apply_inr, Nat.zero_add, Nat.factorial_zero, Nat.one_mul]

/-- **§12's height estimate, for the divided-derivative Wronskian.**

The determinant of `∂^{Dx i ⊞ Dy j} P` is `C·W` with `W` **integral** and

    |coeff n W| ≤ r! · S^r · (2^{Σ_h d_h} · B)^r

With `S ≤ ∏_h (d_h + 1) ≤ 2^{Σ_h d_h}` that reads `r!·2^{2r·Σ_h d_h}·B^r` — **§12's
`b = 2^{2n(r₁+…+r_m)}·n!·a^n`, exactly.**

`W` is Mahler's `W`: the same determinant built from divided derivatives.  Its index is the
determinant's (`index_C_mul`), so nothing the index calculus proves is lost, and its height is
smaller by the `C` that correction twenty-one identified — `2^{Θ(r² log r)}`, which §12's budget
has no room for. -/
theorem exists_divided_wronskian {τ : Type*} [DecidableEq σ] [DecidableEq τ]
    [DecidableEq (σ ⊕ τ)] {r : ℕ} (s : Finset (σ ⊕ τ)) {S B : ℤ} {d : (σ ⊕ τ) → ℕ}
    (hB0 : 0 ≤ B) (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (P : MvPolynomial (σ ⊕ τ) ℤ)
    (hx : ∀ i, ∀ h ∈ (Dx i).map Sum.inl, h ∈ s)
    (hy : ∀ j, ∀ h ∈ (Dy j).map Sum.inr, h ∈ s)
    (hS : ((P.support.card : ℕ) : ℤ) ≤ S)
    (hd : ∀ h, degreeOf h P ≤ d h) (hB : ∀ n, |coeff n P| ≤ B) :
    ∃ W : MvPolynomial (σ ⊕ τ) ℤ,
      (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det
        = C ((∏ i, ((∏ h ∈ s, ((listIdx ((Dx i).map Sum.inl)) h).factorial : ℕ) : ℤ)) *
             (∏ j, ((∏ h ∈ s, ((listIdx ((Dy j).map Sum.inr)) h).factorial : ℕ) : ℤ))) * W ∧
      ∀ n, |coeff n W| ≤ (r.factorial : ℤ) * S ^ r * (2 ^ (∑ h ∈ s, d h) * B) ^ r := by
  classical
  set ax : Fin r → ℤ :=
    fun i => ((∏ h ∈ s, ((listIdx ((Dx i).map Sum.inl)) h).factorial : ℕ) : ℤ) with hax
  set ay : Fin r → ℤ :=
    fun j => ((∏ h ∈ s, ((listIdx ((Dy j).map Sum.inr)) h).factorial : ℕ) : ℤ) with hay
  set K : ℤ := 2 ^ (∑ h ∈ s, d h) * B with hK
  obtain ⟨W, hW⟩ := C_listFac_dvd_det_sepFamily s Dx Dy P hx hy
  refine ⟨W, hW, ?_⟩
  intro n
  have hmem : ∀ i j, ∀ h ∈ (Dx i).map Sum.inl ++ (Dy j).map Sum.inr, h ∈ s := by
    intro i j h hh
    rcases List.mem_append.mp hh with h1 | h1
    · exact hx i h h1
    · exact hy j h h1
  have hent : ∀ i j, ∀ m,
      |coeff m (pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P)| ≤ ax i * (ay j * K) := by
    intro i j m
    have h := abs_coeff_pderivList_le' s hB0 _ (hmem i j) hd hB m
    rw [listFac_append_map s (Dx i) (Dy j)] at h
    rw [hax, hay, hK]
    push_cast at h ⊢
    linarith
  have hSupp : ∀ i j,
      (((Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P) i
        j).support.card : ℤ) ≤ S := by
    intro i j
    exact le_trans (by exact_mod_cast card_support_pderivList_le _ P) hS
  have hdet := abs_coeff_det_le' (σ := σ ⊕ τ)
    (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P)
    ax (fun j => ay j * K) hSupp hent n
  rw [Fintype.card_fin] at hdet
  have hprod : (∏ j, ay j * K) = (∏ j, ay j) * K ^ r := by
    rw [Finset.prod_mul_distrib, Finset.prod_const, Finset.card_univ, Fintype.card_fin]
  rw [hprod] at hdet
  have haxpos : ∀ i, (0 : ℤ) < ax i := by
    intro i
    have h : (0 : ℕ) < ∏ h ∈ s, ((listIdx ((Dx i).map Sum.inl)) h).factorial :=
      Finset.prod_pos fun h _ => Nat.factorial_pos _
    simp only [hax]
    exact_mod_cast h
  have haypos : ∀ j, (0 : ℤ) < ay j := by
    intro j
    have h : (0 : ℕ) < ∏ h ∈ s, ((listIdx ((Dy j).map Sum.inr)) h).factorial :=
      Finset.prod_pos fun h _ => Nat.factorial_pos _
    simp only [hay]
    exact_mod_cast h
  have hcpos : (0 : ℤ) < (∏ i, ax i) * ∏ j, ay j :=
    mul_pos (Finset.prod_pos fun i _ => haxpos i) (Finset.prod_pos fun j _ => haypos j)
  rw [hW, coeff_C_mul, abs_mul, abs_of_pos hcpos] at hdet
  refine le_of_mul_le_mul_left ?_ hcpos
  calc ((∏ i, ax i) * ∏ j, ay j) * |coeff n W|
      ≤ (r.factorial : ℤ) * S ^ r * ((∏ i, ax i) * ((∏ j, ay j) * K ^ r)) := hdet
    _ = ((∏ i, ax i) * ∏ j, ay j) * ((r.factorial : ℤ) * S ^ r * K ^ r) := by ring

/-! ### The support bound the budget consumes

`exists_divided_wronskian` takes `S` as an upper bound on `P.support.card`, and `height_budget`
wants that same `S` below `2^{Σd}`.  Both are met by `S := 2^{Σd}` itself, and the reason is
elementary: a monomial in the support has every exponent at most the corresponding `degreeOf`,
so the support injects into `∏ (d h + 1)` boxes, and `k + 1 ≤ 2^k`. -/

/-- **A polynomial's support is bounded by the box its degrees cut out.**

Stated over an arbitrary coefficient semiring: nothing in the proof is arithmetic, it is a
statement about which multi-indices can occur.  It was written against `ℤ` for §12's budget and
generalised when Roth's theorem's step 2 needed the same count over `ℝ`. -/
theorem card_support_le_prod_succ [Fintype σ] [DecidableEq σ]
    {R : Type*} [CommSemiring R]
    {P : MvPolynomial σ R} {d : σ → ℕ} (hd : ∀ h, degreeOf h P ≤ d h) :
    P.support.card ≤ ∏ h, (d h + 1) := by
  classical
  have hinj : Function.Injective (fun n : σ →₀ ℕ => (fun h => n h : σ → ℕ)) :=
    fun a b hab => Finsupp.ext (fun h => congrFun hab h)
  have hsub : P.support.image (fun n : σ →₀ ℕ => (fun h => n h : σ → ℕ))
      ⊆ Fintype.piFinset (fun h : σ => Finset.range (d h + 1)) := by
    intro f hf
    simp only [Finset.mem_image] at hf
    obtain ⟨n, hn, rfl⟩ := hf
    rw [Fintype.mem_piFinset]
    intro h
    rw [Finset.mem_range]
    exact Nat.lt_succ_of_le (le_trans (monomial_le_degreeOf h hn) (hd h))
  calc P.support.card
      = (P.support.image (fun n : σ →₀ ℕ => (fun h => n h : σ → ℕ))).card :=
        (Finset.card_image_of_injective _ hinj).symm
    _ ≤ (Fintype.piFinset (fun h : σ => Finset.range (d h + 1))).card :=
        Finset.card_le_card hsub
    _ = ∏ h, (d h + 1) := by rw [Fintype.card_piFinset]; simp

/-- **The box, in the budget's currency.**  `∏ (d h + 1) ≤ 2^{Σ d h}`, term by term. -/
theorem prod_succ_le_two_pow_sum [Fintype σ] (d : σ → ℕ) :
    ∏ h, (d h + 1) ≤ 2 ^ (∑ h, d h) := by
  classical
  rw [← Finset.prod_pow_eq_pow_sum]
  exact Finset.prod_le_prod' (fun h _ => Nat.lt_two_pow_self)

/-- **`S := 2^{Σd}` serves both lemmas** — `exists_divided_wronskian`'s `hS` and
`height_budget`'s `hS`, with `hS1 : 1 ≤ S` free. -/
theorem card_support_le_two_pow_sum [Fintype σ] [DecidableEq σ]
    {R : Type*} [CommSemiring R]
    {P : MvPolynomial σ R} {d : σ → ℕ} (hd : ∀ h, degreeOf h P ≤ d h) :
    ((P.support.card : ℕ) : ℤ) ≤ 2 ^ (∑ h, d h) := by
  exact_mod_cast le_trans (card_support_le_prod_succ hd) (prod_succ_le_two_pow_sum d)

/-- **§12's budget closes** — and by exactly one factor of `r₀·d_first`.

`exists_divided_wronskian` gives `|coeff W| ≤ r₀!·S^{r₀}·(2^{Σd}·a)^{r₀}`.  §11's clause 4 wants
`b ≤ 2^c·a^{r₀}` with `c ≤ (2m+1)·(r₀·d_first)` — which is `rothGammaFull_descend`'s
`(2n+3)·(r₀·d (o.symm 0))` at `m = n + 1`.  The two meet:

    S^{r₀} ≤ 2^{r₀Σd},   (2^{Σd}·a)^{r₀} = 2^{r₀Σd}·a^{r₀},   so   b ≤ r₀!·2^{2r₀Σd}·a^{r₀}
    Σd ≤ (n+1)·d_first                      gives  2r₀Σd ≤ (2n+2)·r₀·d_first
    r₀! ≤ r₀^{r₀} ≤ (d_last+1)^{r₀} ≤ 2^{r₀·d_first}

and `(2n+2) + 1 = 2n+3`.  So the factorial is what the last unit of the budget pays for, and
there is nothing else to spend it on — §12's `2^{2n(r₁+…+r_m)}·n!·a^n` names both terms.

⚠ `d_last + 1 ≤ 2^{d_first}` is the only place the growth ordering is used, and it is used only
through `d_last ≤ d_first`.  The `+1` survives because `k + 1 ≤ 2^k`, not because of any
estimate on the degrees' ratio — so a *degenerate* growth constant would not break this step,
only the row cost. -/
theorem height_budget {n r₀ sd dfirst dlast : ℕ} {S a : ℤ}
    (hr₀ : r₀ ≤ dlast + 1) (hsum : sd ≤ (n + 1) * dfirst) (hdf : dlast ≤ dfirst)
    (hS1 : 1 ≤ S) (hS : S ≤ 2 ^ sd) (ha : 1 ≤ a) :
    (r₀.factorial : ℤ) * S ^ r₀ * (2 ^ sd * a) ^ r₀
      ≤ 2 ^ ((2 * n + 3) * (r₀ * dfirst)) * a ^ r₀ := by
  have ha0 : (0 : ℤ) ≤ a := le_trans zero_le_one ha
  have hS0 : (0 : ℤ) ≤ S := le_trans zero_le_one hS1
  -- the factorial, absorbed into a single `2^{r₀·d_first}`
  have hfacN : r₀.factorial ≤ 2 ^ (r₀ * dfirst) := by
    calc r₀.factorial ≤ r₀ ^ r₀ := Nat.factorial_le_pow r₀
      _ ≤ (2 ^ dfirst) ^ r₀ := by
          refine Nat.pow_le_pow_left ?_ r₀
          calc r₀ ≤ dlast + 1 := hr₀
            _ ≤ dfirst + 1 := by omega
            _ ≤ 2 ^ dfirst := Nat.lt_two_pow_self
      _ = 2 ^ (r₀ * dfirst) := by rw [← pow_mul, mul_comm]
  have hfac : ((r₀.factorial : ℕ) : ℤ) ≤ 2 ^ (r₀ * dfirst) := by exact_mod_cast hfacN
  -- the two `2^{r₀sd}` factors
  have hSpow : S ^ r₀ ≤ 2 ^ (r₀ * sd) := by
    calc S ^ r₀ ≤ ((2 : ℤ) ^ sd) ^ r₀ := pow_le_pow_left₀ hS0 hS r₀
      _ = 2 ^ (r₀ * sd) := by rw [← pow_mul, mul_comm]
  have hsplit : ((2 : ℤ) ^ sd * a) ^ r₀ = 2 ^ (r₀ * sd) * a ^ r₀ := by
    rw [mul_pow, ← pow_mul, mul_comm sd r₀]
  -- the exponent arithmetic
  have hexp : r₀ * dfirst + (r₀ * sd + r₀ * sd) ≤ (2 * n + 3) * (r₀ * dfirst) := by
    have h1 : r₀ * sd ≤ r₀ * ((n + 1) * dfirst) := Nat.mul_le_mul_left _ hsum
    nlinarith [h1]
  calc (r₀.factorial : ℤ) * S ^ r₀ * (2 ^ sd * a) ^ r₀
      = ((r₀.factorial : ℕ) : ℤ) * S ^ r₀ * (2 ^ (r₀ * sd) * a ^ r₀) := by rw [hsplit]
    _ ≤ (2 : ℤ) ^ (r₀ * dfirst) * 2 ^ (r₀ * sd) * (2 ^ (r₀ * sd) * a ^ r₀) := by
        refine mul_le_mul (mul_le_mul hfac hSpow (pow_nonneg hS0 r₀) (by positivity)) le_rfl
          (by positivity) (by positivity)
    _ = (2 : ℤ) ^ (r₀ * dfirst + (r₀ * sd + r₀ * sd)) * a ^ r₀ := by
        rw [← pow_add, ← mul_assoc, ← pow_add, add_assoc]
    _ ≤ (2 : ℤ) ^ ((2 * n + 3) * (r₀ * dfirst)) * a ^ r₀ := by
        refine mul_le_mul_of_nonneg_right (pow_le_pow_right₀ (by norm_num) hexp) (by positivity)

/-- **§12's height estimate and §11's clause 4, joined.**

Everything §13's descent needs from the height theory, in the shape `rothGammaFull_descend`
consumes it: an integral `W` with `det = C c · W`, `c > 0`, and

    |coeff W| ≤ 2^{(2n+3)·(r₀·d_first)} · a^{r₀}

which is `b ≤ 2^{c'}·a^{r₀}` with `c' = (2n+3)·(r₀·d_first)` — clause 4 exactly.

The three inputs are the degree bound, the height bound `a`, and the ordering facts
`r₀ ≤ d_last + 1` (Mahler's `n ≤ r_m + 1`), `Σd ≤ (n+1)·d_first` and `d_last ≤ d_first`.  `S` is
taken to be `2^{Σd}` itself, which `card_support_le_two_pow_sum` supplies and `height_budget`
accepts with `le_rfl`.

⚠ `c > 0` rather than `c ≠ 0` — it is a product of factorials, and the sign is free.  The
consumers only need non-vanishing (`index_C_mul`), but positivity is what the proof produces
and there is no reason to weaken it. -/
theorem exists_divided_wronskian_budget {τ : Type*} [Fintype σ] [Fintype τ]
    [DecidableEq σ] [DecidableEq τ] [DecidableEq (σ ⊕ τ)]
    {r₀ n dfirst dlast : ℕ} {a : ℤ} {d : (σ ⊕ τ) → ℕ}
    (ha : 1 ≤ a) (Dx : Fin r₀ → List σ) (Dy : Fin r₀ → List τ)
    (P : MvPolynomial (σ ⊕ τ) ℤ)
    (hdeg : ∀ h, degreeOf h P ≤ d h) (hB : ∀ m, |coeff m P| ≤ a)
    (hr₀ : r₀ ≤ dlast + 1) (hsum : ∑ h, d h ≤ (n + 1) * dfirst) (hdf : dlast ≤ dfirst) :
    ∃ (W : MvPolynomial (σ ⊕ τ) ℤ) (c : ℤ), 0 < c ∧
      (Matrix.of fun i j =>
          pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det = C c * W ∧
      ∀ m, |coeff m W| ≤ 2 ^ ((2 * n + 3) * (r₀ * dfirst)) * a ^ r₀ := by
  classical
  have ha0 : (0 : ℤ) ≤ a := le_trans zero_le_one ha
  obtain ⟨W, hW, hWB⟩ := exists_divided_wronskian (Finset.univ : Finset (σ ⊕ τ))
    (S := 2 ^ (∑ h, d h)) ha0 Dx Dy P
    (fun i h _ => Finset.mem_univ h) (fun j h _ => Finset.mem_univ h)
    (card_support_le_two_pow_sum hdeg) hdeg hB
  refine ⟨W, _, ?_, hW, fun m => le_trans (hWB m) ?_⟩
  · exact mul_pos
      (Finset.prod_pos fun i _ => by
        exact_mod_cast Finset.prod_pos fun h _ => Nat.factorial_pos _)
      (Finset.prod_pos fun j _ => by
        exact_mod_cast Finset.prod_pos fun h _ => Nat.factorial_pos _)
  · exact height_budget hr₀ hsum hdf (one_le_pow₀ (by norm_num)) le_rfl ha

/-- **§7's coefficient bound in one variable, sharp.**

    |coeff n (∂ⱼ^k g)| ≤ k! · 2^d · B      whenever  degreeOf j g ≤ d  and  |coeff · g| ≤ B

Compare `abs_coeff_pderivList_le`, which gives `d^k·B`.  The two agree in shape only when `k` is
small: the sharp form separates `k!` — the **whole** discrepancy with Mahler's divided
derivative — and leaves a binomial, which `Nat.choose_le_two_pow` sends to `2^d`.  That `2^d` is
§7's `2^{r_h}`, and it is what makes §12's budget `2^{(2m+1)ρ₁}` come out.

⚠ Sharp in `k`, and that is the point: at `k ≈ d` the crude bound is `d^d` where this is
`k!·2^d ≈ (d/e)^d·2^d`. Neither dominates for all `k`, but only this one has the factorial
*visible*, so only this one lets the divided derivative be recovered by dividing it out. -/
theorem abs_coeff_pderiv_iterate_le [DecidableEq σ] {g : MvPolynomial σ ℤ} {d : ℕ} {B : ℤ}
    (hB0 : 0 ≤ B) (j : σ) (hd : degreeOf j g ≤ d) (hB : ∀ n, |coeff n g| ≤ B) (k : ℕ)
    (n : σ →₀ ℕ) :
    |coeff n ((pderiv j)^[k] g)| ≤ (k.factorial : ℤ) * 2 ^ d * B := by
  classical
  rw [coeff_pderiv_iterate, abs_mul]
  have hfac : (0 : ℤ) ≤ (k.factorial : ℤ) * 2 ^ d := by positivity
  by_cases hz : coeff (n + Finsupp.single j k) g = 0
  · rw [hz, abs_zero, mul_zero]
    exact mul_nonneg hfac hB0
  · have hmem : (n + Finsupp.single j k) ∈ g.support := mem_support_iff.mpr hz
    have hle : n j + k ≤ d := by
      have h1 := monomial_le_degreeOf j hmem
      simp only [Finsupp.add_apply, Finsupp.single_eq_same] at h1
      omega
    have hchoose : ((n j + k).choose k) ≤ 2 ^ d :=
      le_trans (Nat.choose_le_two_pow _ _) (Nat.pow_le_pow_right (by norm_num) hle)
    have hprodN : (∏ i ∈ Finset.range k, (n j + 1 + i))
        = k.factorial * ((n j + k).choose k) := by
      rw [← Nat.ascFactorial_eq_prod_range, Nat.ascFactorial_eq_factorial_mul_choose]
    have hPrle : |∏ i ∈ Finset.range k, ((n j + 1 + i : ℕ) : ℤ)|
        ≤ (k.factorial : ℤ) * 2 ^ d := by
      rw [abs_of_nonneg (Finset.prod_nonneg fun i _ => by positivity), ← Nat.cast_prod, hprodN]
      exact_mod_cast Nat.mul_le_mul_left k.factorial hchoose
    refine le_trans (mul_le_mul hPrle (hB _) (abs_nonneg _) hfac) (le_of_eq ?_)
    ring

/-! ### Next

The height side of Roth's lemma is now closed end to end: a bound on the auxiliary
polynomial's data gives a bound on its Wronskian (here), which the separated factorization
carries down to each factor (`abs_coeff_le_of_mul_separated` in
`QOU/Mathlib/SeparatedHeight.lean`).

⚠ What remains is **structural, not quantitative**: assembling the induction on the number of
variables — the statement of Roth's lemma itself, and the argument that recurses from `m` to
`1` and `m−1`.  No further height machinery is known to be needed for it, but that claim
should be checked against the assembly rather than assumed; this bean has mis-predicted the
location of the remaining cost three times already. -/

end MvPolynomial
