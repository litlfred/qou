import Mathlib.Tactic

/-!
# The Markov/Jones stabilisation factor is EXTENSIVE (linear in strand count)

L2-closure attack option **A1**
(`docs/audits/2026-08-07-l2-closure-attack-options-non-em-terms.md` §3),
formalised at the level at which it is actually algebraic — and **not** one step
further.

The raw Ocneanu/Markov trace on the braid group `B_n` becomes a **link
invariant** only after multiplying by the Jones/HOMFLY **stabilisation factor**
`N(q)^{n-1}` — the power of the loop value `N(q)` that the Markov moves force so
that a stabilisation move (adding a strand closed up with a single crossing) does
not change the invariant. That factor is exactly what makes the invariant
*intensive*: independent of how many strands the braid happens to be written on.

Its logarithm is therefore `(n-1)·log N(q)` — **linear in the strand count `n`**,
i.e. **extensive**. This file proves the ring-level content of that statement:
the factor accrues exactly one constant factor of `N(q)` per added strand
(`markovStabFactor_succ`), and merging an `m`-strand with an `n`-strand system
multiplies the two factors and one extra `N(q)` (`markovStabFactor_merge`) — the
signature of a volume-like (extensive) accumulation, in contrast to an
*intensive* isotopy invariant whose per-strand ratio is `1`
(`markovStabFactor_not_intensive`).

**SCOPE — this is the STRUCTURE only; the magnitude is deliberately left open.**
Whether the coefficient `log N(q)` (times the electron scale) matches the nuclear
volume term `a_V` is a *prediction*, free to fail — and at the Jones
specialisation `N = 2` the audit measures it `5.4×` short (§3 caveat). Nothing
here identifies strand count with mass number, wires a value, or fits: it proves
only that the *discarded normalisation is extensive*, which is precisely the
object both proved constraints — the intensive/extensive split and the pairwise
cap `ρ_A ≤ C(A,2)` — say is the missing (non-2-body, volume) term. Sorry-free.

-- Ref: [manuscript] docs/audits/2026-08-07-l2-closure-attack-options-non-em-terms.md §3 (A1)
-- Ref: [jones1987] V. Jones, "Hecke algebra representations of braid groups and
--       link polynomials," Ann. of Math. 126 (1987)
-/

namespace QOU.Mass.MarkovStabFactor

/-- The Jones/HOMFLY **stabilisation factor** on `n` strands: the power
    `N(q)^{n-1}` of the loop value `N(q)` that the Markov moves force in order to
    turn the raw Ocneanu trace into a link invariant. Parameterised by the loop
    value `Nq` alone — the extensivity structure below is independent of its exact
    form (`-(q^{1/2}+q^{-1/2})`, `[N]_q`, …). -/
def markovStabFactor {R : Type*} [CommRing R] (Nq : R) (n : ℕ) : R := Nq ^ (n - 1)

/-- **One constant factor of `N(q)` per added strand.** For `n ≥ 1`,
    `stab(n+1) = stab(n)·N(q)`. The per-strand *ratio* is the constant `N(q)`,
    independent of `n` — the defining property of an **extensive** accumulation
    (an *intensive* isotopy invariant would have ratio `1`). -/
theorem markovStabFactor_succ {R : Type*} [CommRing R] (Nq : R) {n : ℕ} (hn : 1 ≤ n) :
    markovStabFactor Nq (n + 1) = markovStabFactor Nq n * Nq := by
  unfold markovStabFactor
  have h : (n + 1) - 1 = (n - 1) + 1 := by omega
  rw [h, pow_succ]

/-- **Merge law (extensivity).** Combining an `m`-strand with an `n`-strand
    system multiplies their stabilisation factors and one extra `N(q)`:
    `stab(m)·stab(n)·N(q) = stab(m+n)`. Equivalently the exponents satisfy
    `(m-1)+(n-1)+1 = (m+n)-1`, so `log stab` accumulates `+log N(q)` per merge —
    the volume-like (extensive) growth that a link-invariant normalisation is
    designed to cancel. -/
theorem markovStabFactor_merge {R : Type*} [CommRing R] (Nq : R) {m n : ℕ}
    (hm : 1 ≤ m) (hn : 1 ≤ n) :
    markovStabFactor Nq m * markovStabFactor Nq n * Nq = markovStabFactor Nq (m + n) := by
  unfold markovStabFactor
  have h : (m + n) - 1 = (m - 1) + (n - 1) + 1 := by omega
  rw [h, pow_add, pow_add, pow_one]

/-- **Extensive, not intensive.** For a nontrivial loop value `N(q) ≠ 1` the
    factor genuinely depends on strand count: `stab(n+1) ≠ stab(n)` (`n ≥ 1`). An
    intensive isotopy invariant is by definition `n`-independent; the
    stabilisation factor is not, so normalising it away removes exactly this
    `n`-dependent (extensive) piece — the term the corpus has been hunting. -/
theorem markovStabFactor_not_intensive {R : Type*} [Field R] (Nq : R)
    (hNq1 : Nq ≠ 1) (hNq0 : Nq ≠ 0) {n : ℕ} (hn : 1 ≤ n) :
    markovStabFactor Nq (n + 1) ≠ markovStabFactor Nq n := by
  rw [markovStabFactor_succ Nq hn]
  intro hc
  have hpos : markovStabFactor Nq n ≠ 0 := pow_ne_zero _ hNq0
  have h1 : markovStabFactor Nq n * Nq = markovStabFactor Nq n * 1 := by rw [mul_one]; exact hc
  exact hNq1 (mul_left_cancel₀ hpos h1)

/-- **Closed form of the accumulated log-exponent.** Over `A` strands the
    stabilisation exponent is `A - 1`, an affine function of `A` with unit slope:
    `exponent(A+1) - exponent(A) = 1` for `A ≥ 1`. This is the arithmetic core of
    "extensive" — a constant nonzero increment per strand, versus the `0`
    increment of an intensive invariant. -/
theorem markovStabFactor_exponent_affine {A : ℕ} (hA : 1 ≤ A) :
    ((A + 1) - 1) - (A - 1) = 1 := by omega

end QOU.Mass.MarkovStabFactor
