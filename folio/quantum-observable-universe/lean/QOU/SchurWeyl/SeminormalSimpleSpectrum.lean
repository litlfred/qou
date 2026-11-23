import QOU.SchurWeyl.QJucysMurphyEigen
import QOU.SchurWeyl.SytContentTuple

/-!
# QOU.SchurWeyl.SeminormalSimpleSpectrum — the `q`-Jucys–Murphy spectrum is simple

**The separation half of general irreducibility** (SW-5, bean `qou-jfr8`).

Two facts combine here, and neither suffices alone:

* **Ram (1997) Thm 4.1** (`SeminormalRep.seminormalRep_qJM`, proved in `QJucysMurphyEigen`):
  each `L_k` acts *diagonally* on the SYT basis, with entry `q^{2·cellContent (cellOf T k)}`.
  Diagonal is not separating — a diagonal matrix with a repeated entry has a whole plane of
  eigenvectors, and any subspace of that plane would be invariant.
* **Separation** (`syt_eq_of_cellContent_eq`, transported from the Okounkov–Vershik stack in
  `SytContentTuple`): distinct tableaux of one shape have distinct *content tuples*.

Together they give what irreducibility actually needs: the map sending a tableau to its **tuple**
of `L_k`-eigenvalues is injective, so the joint eigenspaces of the commuting family
`{L_0, …, L_n}` are the individual coordinate *lines*.  Any subspace invariant under the whole
family is then a span of a subset of the SYT basis — which is the step that reduces irreducibility
to connectivity under admissible swaps.

**Where the genericity hypothesis earns its keep.** Passing from equal eigenvalues
`q^{2c} = q^{2c'}` to equal contents `c = c'` is exactly where `q ^ 2 ≠ 1` is used
(`SeminormalRep.zpow_ne_one`): at a root of unity distinct contents can share an eigenvalue, the
spectrum stops being simple, and this argument — not merely this proof — fails.  That regime is
tracked as bean `qou-4lft`.

Refs:
- [ram1997] Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  https://doi.org/10.1112/S0024611597000373
- [okounkov1996] Okounkov–Vershik — the Gelfand–Tsetlin/content-tuple separation at `q = 1`.

LaTeX label: `lem:seminormal-simple-spectrum`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

variable {μ : YoungDiagram}

/-- **Equal powers force equal exponents**, for a real `q` that is not a root of unity.
`q ≠ 0` with `q ^ 2 ≠ 1` says exactly that over `ℝ`. -/
theorem zpow_injective_of_not_root_of_unity {K : Type*} [Field K] {q : K} (hq0 : q ≠ 0) (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) {a b : ℤ}
    (h : q ^ a = q ^ b) : a = b := by
  by_contra hne
  have hsub : q ^ (a - b) = 1 := by
    rw [zpow_sub₀ hq0, h, div_self (zpow_ne_zero b hq0)]
  exact zpow_ne_one hq2 (sub_ne_zero_of_ne hne) hsub

/-- The diagonal entry of `ρ(L_k)` at `T` is `q^{2·content}` at the cell holding `k+1`. -/
theorem seminormalRep_qJM_diag {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0) (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) (n : ℕ)
    (hN : μ.cells.card = n + 1) (k : ℕ) (hk : k ≤ n) (T : StandardYoungTableau μ) :
    seminormalRep q hq0 hq2 n hN (qJM K q q⁻¹ n k) T T
      = q ^ (2 * cellContent (cellOf T (k + 1))) := by
  rw [seminormalRep_qJM q hq0 hq2 n hN k hk, jmDiagVal, Matrix.diagonal_apply_eq]

/-- **The `q`-Jucys–Murphy spectrum is simple.**  A tableau is determined by its tuple of
`L_k`-eigenvalues in the seminormal representation.

This is what makes the diagonalisation of `seminormalRep_qJM` *useful*: the joint eigenspaces of
the commuting family `{L_0, …, L_n}` are single coordinate lines, so every subspace invariant
under the family is spanned by a subset of the SYT basis. -/
theorem seminormalRep_qJM_spectrum_injective {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0) (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) (n : ℕ)
    (hN : μ.cells.card = n + 1) :
    Function.Injective (fun (T : StandardYoungTableau μ) (k : Fin (n + 1)) =>
      seminormalRep q hq0 hq2 n hN (qJM K q q⁻¹ n k.val) T T) := by
  intro T T' h
  refine syt_eq_of_cellContent_eq T T' (fun j hj1 hjc => ?_)
  -- the label `j` is `k + 1` for `k = j - 1 ≤ n`
  obtain ⟨k, rfl⟩ : ∃ k, j = k + 1 := ⟨j - 1, by omega⟩
  have hk : k ≤ n := by omega
  have hentry : seminormalRep q hq0 hq2 n hN (qJM K q q⁻¹ n k) T T
      = seminormalRep q hq0 hq2 n hN (qJM K q q⁻¹ n k) T' T' :=
    congrFun h ⟨k, by omega⟩
  rw [seminormalRep_qJM_diag q hq0 hq2 n hN k hk T,
    seminormalRep_qJM_diag q hq0 hq2 n hN k hk T'] at hentry
  have := zpow_injective_of_not_root_of_unity hq0 hq2 hentry
  omega

/-- **Content-exponent separation (`qou-yuyz`).** For a generic parameter `q`
(`q ≠ 0`, `NotRootOfUnity q`), equal even powers `q ^ (2 * a) = q ^ (2 * b)`
force equal integer contents `a = b`. -/
theorem zpow_two_mul_injective_of_not_root_of_unity {K : Type*} [Field K] {q : K}
    (hq0 : q ≠ 0) (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) {a b : ℤ}
    (h : q ^ (2 * a) = q ^ (2 * b)) : a = b := by
  have h2 : 2 * a = 2 * b := zpow_injective_of_not_root_of_unity hq0 hq2 h
  omega

end QOU.SchurWeyl
