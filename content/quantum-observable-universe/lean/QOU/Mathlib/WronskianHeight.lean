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
