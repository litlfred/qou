import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Archimedean.lepton_continuant_recurrence — Morgan–Voyce continuant
  normal form of `σ₀ⁿ` in `H_2(q)`

**Proposition** ([`prop:lepton-continuant-recurrence`]).

In `H_2(q)` the generator `σ₀` satisfies the Hecke relation
`σ₀² = h·σ₀ + 1` (`h = q − q⁻¹`).  The Gröbner–Shirshov normal form of
the `(2,n)`-torus braid `σ₀ⁿ = T_{2,n}` is

    σ₀ⁿ = a_n · 𝟏 + b_n · σ₀,

with `a_{n+1} = b_n` and `b_{n+1} = h·b_n + b_{n-1}` (the Morgan–Voyce
continuant), `b_0 = 0`, `b_1 = 1`.

The single-generator subalgebra `R[σ₀]/(σ₀² − h σ₀ − 1) ⊆ H_2(q)` is
commutative, so the statement is formalised over a generic commutative
ring `R` for the element `s = σ₀` (§7c: no `ℝ`; holds over any `R`).
The normal form is **derived** by induction from the Hecke relation —
not assumed.

-- Ref: [manuscript] prop:lepton-continuant-recurrence
-/

namespace QOU.Archimedean

variable {R : Type*} [CommRing R]

/-- Morgan–Voyce continuant `b_n`: `b 0 = 0`, `b 1 = 1`,
    `b (n+2) = h·b(n+1) + b n`. -/
def mvB (h : R) : ℕ → R
  | 0 => 0
  | 1 => 1
  | (n + 2) => h * mvB h (n + 1) + mvB h n

/-- The companion sequence `a_n`: `a 0 = 1`, `a (n+1) = b n`
    (i.e. `a_{n+1} = b_n`). -/
def mvA (h : R) : ℕ → R
  | 0 => 1
  | (n + 1) => mvB h n

/-- Coupled form of the continuant: `b_{n+1} = a_n + h·b_n`
    (equivalently `b_{n+1} = h·b_n + b_{n-1}` since `a_n = b_{n-1}`). -/
theorem mvB_succ (h : R) (n : ℕ) :
    mvB h (n + 1) = mvA h n + h * mvB h n := by
  cases n with
  | zero => simp [mvA, mvB]
  | succ m => simp only [mvA, mvB]; ring

/-- **Continuant recurrence for the lepton tower `T_{2,n} = σ₀ⁿ`**
    ([`prop:lepton-continuant-recurrence`]).

    Given the Hecke relation `s² = h·s + 1` for `s = σ₀`, the
    Gröbner–Shirshov normal form is `sⁿ = a_n·𝟏 + b_n·s`, **derived** by
    induction on `n` from the relation (so `a_{n+1} = b_n` and
    `b_{n+1} = h·b_n + b_{n-1}`).  The proof reads off the normal form;
    it does not assume it. -/
-- Ref: [manuscript] prop:lepton-continuant-recurrence
theorem lepton_continuant_recurrence (h s : R) (hs : s ^ 2 = h * s + 1)
    (n : ℕ) : s ^ n = mvA h n + mvB h n * s := by
  induction n with
  | zero => simp [mvA, mvB]
  | succ m ih =>
      rw [pow_succ, ih, mvB_succ]
      -- `mvA h (m+1)` reduces to `mvB h m` definitionally:
      show (mvA h m + mvB h m * s) * s
          = mvB h m + (mvA h m + h * mvB h m) * s
      linear_combination (mvB h m) * hs

/-- The **net coefficient** `net(T_{2,n}) = a_n + b_n` (sum of all normal
    form terms). -/
def mvNet (h : R) (n : ℕ) : R := mvA h n + mvB h n

end QOU.Archimedean
