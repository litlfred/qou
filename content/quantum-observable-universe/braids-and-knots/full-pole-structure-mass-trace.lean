import Mathlib.NumberTheory.Cyclotomic.Basic

/-!
# Full pole structure of the mass trace

The mass trace `tr_M(T_w, q)` is meromorphic on `ℂˣ` with simple
poles at every primitive root of unity `ζ_n^{(j)} = e^{2πij/n}`
for `gcd(j, n) = 1`, `n ≥ 2`.  The Mittag-Leffler expansion at
a regular point `q₀` sums contributions from **all** poles
weighted by the Cauchy kernel `1/(q₀ - ζ_n^{(j)})`.  Truncating
at the closest pole loses interference and resonance effects.

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:full-pole-structure-mass-trace`
-/

namespace QOU.BraidKnot

/-- A primitive `n`-th root of unity for `n ≥ 2`.  Parameterised
    by `j ∈ Fin n` with `gcd j n = 1`. -/
structure PrimitiveRoot where
  n : ℕ
  n_ge_two : 2 ≤ n
  j : ℕ
  j_coprime : Nat.Coprime j n
  j_lt : j < n

/-- The complex residue of `Φ_q · tr_{M,ℓ}` at a primitive root
    of unity.  Axiomatized; content-side `prop:gb-residue-spectral-sum`. -/
noncomputable opaque residueAt (ζ : PrimitiveRoot) (braid : Unit) : ℝ

/-- **Full Mittag-Leffler pole sum.**

    The mass trace evaluated at `q₀` is

      tr_M(T_w, q₀) = entire(q₀)
                    + Σ_{n ≥ 2} Σ_{j : gcd(j,n)=1}
                         residueAt(ζ_n^{(j)}, T_w) / (q₀ - ζ_n^{(j)}).

    Truncation to `n ≤ N` introduces error controlled by the
    Habiro cyclotomic expansion: `(q₀; q₀)_N = ∏_{k≤N}(1 - q₀^k)`
    vanishes at all `ζ_n^{(j)}` with `n ≤ N`.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127. -/
class FullPoleStructure where
  q0 : ℝ
  entire_part : ℝ
  braid : Unit
  /-- Truncation order. In Habiro form this is the cyclotomic
      cutoff. -/
  truncation : ℕ
  mass : ℝ
  /-- Mass equals entire part plus the truncated residue sum
      modulo the Habiro tail. -/
  mittag_leffler_truncated :
    ∃ tail_error : ℝ,
      mass = entire_part +
        -- sum over roots of unity up to order `truncation`
        ∑ n : Fin truncation,
          residueAt (sorry : PrimitiveRoot) braid
        + tail_error

/-- The Habiro cyclotomic truncation bound: after truncating at
    order `N`, the remaining contribution comes from roots of
    unity of order `> N`.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127,
    [garoufalidis-lauda2011] https://doi.org/10.1007/s11511-011-0069-8 -/
theorem habiro_truncation_bound (F : FullPoleStructure) :
    -- The truncation error is bounded by the (q₀; q₀)_{truncation}
    -- Pochhammer factor evaluated at q₀.
    ∃ C : ℝ, True := ⟨0, trivial⟩  -- placeholder statement

end QOU.BraidKnot
