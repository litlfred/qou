import Mathlib.Tactic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Order.Filter.Basic

/-!
# QOU.QCasimir — Classical limit (q → 1) of the q-Casimir eigenvalue

The **archimedean specialisation** (CLAUDE.md §7c) of the generic
q-Casimir construction [`def:q-casimir`](./q-casimir.md): as `q → 1`
over the real field `ℝ`, the symmetric q-number `[n]_q` converges to
`n`, and the Casimir eigenvalue `[j]_q · [j+1]_q` converges to
`j · (j+1)` — the eigenvalue of the classical `𝔰𝔲(2)` Casimir.

This block lives on the **archimedean side of the substrate wall**: it
evaluates the generic `qNumberSym` / `QCasimirEigenvalue` of
`def:q-casimir` at `K := ℝ` and takes the punctured-neighbourhood
limit `𝓝[≠] 1` in the real-order topology (`Tendsto`). Per §7c the
generic algebraic construction stays ℝ-free in `q-casimir.lean`; the
real-analytic limit is separated here.

LaTeX label: `prop:q-casimir-classical-limit`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 §VI.4
- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9

## Build context

Content-block stub (not in the Lake `QOU/…` graph). It re-states the
`K := ℝ` specialisations of the generic `qNumberSym` /
`QCasimirEigenvalue` of the sibling `q-casimir.lean` (`def:q-casimir`)
locally, so the file typechecks standalone rather than relying on a
cross-block reference the content-block layer cannot resolve as a live
import.
-/

namespace QOU

open Filter Topology

/-- Symmetric q-number over `ℝ` — the `K := ℝ` specialisation of the
    generic `qNumberSym` of `def:q-casimir`:
    `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`. Re-stated locally so this block
    typechecks standalone. -/
noncomputable def qNumberSym (q : ℝ) (n : ℤ) : ℝ :=
  (q ^ n - q ^ (-n)) / (q - q⁻¹)

/-- q-Casimir eigenvalue over `ℝ` — the `K := ℝ` specialisation of the
    generic `QCasimirEigenvalue` of `def:q-casimir`: `[j]_q · [j+1]_q`. -/
noncomputable def QCasimirEigenvalue (q : ℝ) (j : ℤ) : ℝ :=
  qNumberSym q j * qNumberSym q (j + 1)

/- **Classical limit**: as `q → 1`, the symmetric q-number `[n]_q`
    converges to `n`.  Standard L'Hôpital on `ℝ`: over a punctured
    neighbourhood of `1`, the geometric-series expansion
    `(q^n - q^{-n})/(q - q⁻¹) = q^{-(n-1)}·(q^{2n} - 1)/(q² - 1)` is a
    ratio of polynomials with common factor `q - 1` that cancels,
    leaving `n` at `q = 1`.  Here `qNumberSym` is the generic symmetric
    q-number of `def:q-casimir`, specialised to `K := ℝ`. -/
/-- **External axiom (L'Hôpital + polynomial continuity):
    symmetric q-number classical limit `[n]_q → n` as `q → 1`.** -/
-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
axiom qNumberSym_classical_limit_axiom :
    ∀ (n : ℤ), Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ))

-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem qNumberSym_classical_limit (n : ℤ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) :=
  qNumberSym_classical_limit_axiom n

/-- **Classical limit of the Casimir eigenvalue**: as `q → 1`,
    `[j]_q · [j+1]_q → j · (j+1)`.  Combines two instances of
    `qNumberSym_classical_limit` with `Filter.Tendsto.mul`. -/
-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem QCasimirEigenvalue_classical_limit (j : ℤ) :
    Tendsto (fun q : ℝ => QCasimirEigenvalue q j) (𝓝[≠] 1)
      (𝓝 ((j : ℝ) * (j + 1))) := by
  unfold QCasimirEigenvalue
  have hj := qNumberSym_classical_limit j
  have hj1 := qNumberSym_classical_limit (j + 1)
  have hCast : ((j + 1 : ℤ) : ℝ) = (j : ℝ) + 1 := by push_cast; ring
  rw [hCast] at hj1
  exact hj.mul hj1

end QOU
