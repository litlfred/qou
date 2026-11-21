import Mathlib.Data.Int.Basic
import Mathlib.Tactic

/-!
# QOU.Archimedean.genus_maximal_descent

Canonical Lean declaration for content block at
[`quantum-observable-universe/archimedean-universe/genus-maximal-descent.ts`](quantum-observable-universe/archimedean-universe/genus-maximal-descent.ts).

The `lean.ref` URI `qou:QOU.Archimedean.genus_maximal_descent` resolves to
`genus_maximal_descent` below.

The genus value is **derived**, not projected (pattern B): the Descartes
condition `χ(A) = −6` and Riemann–Roch (`2(1 − g) = χ`) together *force*
`g = 4` by integer arithmetic.  The genuine open input is the
Riemann–Roch identity itself, carried as an explicit hypothesis on the
categorical Euler characteristic; the genus is then computed from it.
The Hurwitz automorphism bound `|Aut(Σ_g)| ≤ 84(g − 1)` is the standard
Hurwitz theorem and is carried as a named hypothesis.
-/

namespace QOU.Archimedean

/-- Riemann–Roch on the descent curve `M₀`: `χ = 2(1 − g)` for the
    categorical Euler characteristic `χ` and the genus `g`.  This is the
    genuine geometric input — given it, the genus is determined. -/
theorem genus_of_riemann_roch {χ : ℤ} {g : ℕ}
    (hrr : χ = 2 * (1 - (g : ℤ))) (hdescartes : χ = -6) : g = 4 := by
  have : (2 : ℤ) * (1 - (g : ℤ)) = -6 := by rw [← hrr, hdescartes]
  have hg : (g : ℤ) = 4 := by linarith
  exact_mod_cast hg

/-- **Genus from maximal descent** (manuscript claims (i)–(ii)).

Let `(C, A, τ)` be a quantum observable universe satisfying the Descartes
condition `χ(A) = −6`.  If geometric descent produces a compact
one-complex-dimensional base `M₀`, then Riemann–Roch `χ = 2(1 − g)`
forces the genus `g = 4` — the maximal genus consistent with the Hurwitz
bound `|Aut(Σ_g)| ≤ 84(g − 1) = 252`.

* (i) the genus is `4` — **derived** from `χ = −6` via Riemann–Roch;
* (ii) the Hurwitz bound `aut_order ≤ 84 (g − 1)` holds (the standard
  Hurwitz theorem, carried as the hypothesis `hhurwitz`).

`χ`, the categorical Euler characteristic, and the Riemann–Roch identity
are the genuine inputs; the genus value is computed, not assumed. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/genus-maximal-descent.ts
theorem genus_maximal_descent {χ : ℤ} {g aut_order : ℕ}
    (hrr : χ = 2 * (1 - (g : ℤ))) (hdescartes : χ = -6)
    (hhurwitz : aut_order ≤ 84 * (g - 1)) :
    g = 4 ∧ aut_order ≤ 84 * (g - 1) :=
  ⟨genus_of_riemann_roch hrr hdescartes, hhurwitz⟩

end QOU.Archimedean
