import QOU.Archimedean.lepton_tower_bend_invariant
import Mathlib.Tactic.Linarith

/-!
# QOU.Archimedean.lepton_tower_log_convexity — the additive class is log-CONVEX, so it is excluded too

Companion to `lepton_tower_bend_invariant`, serving bean `qou-htk4`.
Numerical twin:
[`lepton_tower_additive_screening.py`](../../../../../computations/lepton_tower_additive_screening.py).

## The gap this closes

The bend screen in `lepton_tower_bend_invariant` covers the *multiplicative*
class `m_w = C · g^w · f(w)^p`, and its scope note says explicitly that an
**additive interface term** is outside that class and therefore untouched.
That was the last live direction on `qou-htk4`, so it is the one worth
attacking.

It turns out the additive class is excluded too, and by a sharper argument
than the multiplicative one — no plausibility judgement about "the exponent
would have to be large", just an inequality.

## The statement

An additive bridge means the tower is a **sum of geometric modes**: a base
term plus an interface term, each geometric in the winding,

```
  x(w) = c · g^w + d · h^w,        c, d ≥ 0,  g, h > 0.
```

`twoMode_log_convex` says such a tower satisfies

```
  x(w+2)² ≤ x(w) · x(w+4),     i.e.  bend x w ≤ 1.
```

Every positive combination of geometric modes is **log-convex**: its
log-increments *increase*. The observed lepton tower has
`bend = m_μ²/(m_e · m_τ) ≈ 12.295 > 1` — it is log-**concave**, bending the
other way. So no such tower can reproduce it, for any coefficients and any
rates.

## Why it is sharp rather than merely suggestive

The multiplicative screen ruled candidates out by *how large* an exponent
they would need — a judgement call at the margin. This one is a strict
inequality with no free parameters left to argue about: `bend ≤ 1` versus a
measured `12.295`. `not_two_positive_modes_of_bend_gt_one` states the
contrapositive directly.

The proof is the Cauchy–Schwarz mechanism in its sqrt-free Lagrange form —
the difference is a perfect square,

```
  x(w)·x(w+4) − x(w+2)²  =  c·d·g^w·h^w·(g² − h²)².
```

Note what this exhibits: the deficit vanishes exactly when `g = h` (one mode,
`bend = 1`, matching `bend_of_geometric`) or when either coefficient vanishes.
Otherwise it is strictly positive — adding a second positive mode pushes the
tower *further* from log-concavity, never toward it.

## What is and is not covered

Covered: two positive geometric modes, i.e. "canonical term plus interface
term" with both contributing positively — which is the shape an additive
interface bridge would take.

**Not covered, and deliberately not claimed:** (i) more than two modes — the
same Lagrange identity generalises by symmetrising over pairs, but it is not
formalised here; (ii) modes entering with **opposite signs**. Sign-indefinite
combinations escape, exactly as they did for the linear readouts in
`lepton_continuant_positivity` — and for the same reason, since a difference
of exponentials can have a node. That is now the *only* surviving shape in
this direction, in both the multiplicative and additive classes, which is a
useful thing to know.

-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/lepton-continuant-recurrence.md
-/

namespace QOU.Archimedean

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **A positive two-mode tower is log-convex.**

`x(w) = c·g^w + d·h^w` with `c, d ≥ 0` and `g, h > 0` satisfies
`x(w+2)² ≤ x(w)·x(w+4)`.

The proof is the Lagrange form of Cauchy–Schwarz: the deficit is the perfect
square `c·d·g^w·h^w·(g² − h²)²`, so it is not merely non-negative but
*strictly* positive unless the two rates coincide or a coefficient vanishes. -/
theorem twoMode_log_convex (c d g h : K) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (hg : 0 < g) (hh : 0 < h) (w : ℕ) :
    (c * g ^ (w + 2) + d * h ^ (w + 2)) ^ 2
      ≤ (c * g ^ w + d * h ^ w) * (c * g ^ (w + 4) + d * h ^ (w + 4)) := by
  have key :
      (c * g ^ w + d * h ^ w) * (c * g ^ (w + 4) + d * h ^ (w + 4))
        - (c * g ^ (w + 2) + d * h ^ (w + 2)) ^ 2
        = c * d * g ^ w * h ^ w * (g ^ 2 - h ^ 2) ^ 2 := by
    simp only [pow_add]
    ring
  have hcd : 0 ≤ c * d := mul_nonneg hc hd
  have hgw : 0 ≤ g ^ w := le_of_lt (pow_pos hg w)
  have hhw : 0 ≤ h ^ w := le_of_lt (pow_pos hh w)
  have hsq : 0 ≤ (g ^ 2 - h ^ 2) ^ 2 := sq_nonneg _
  have hdef : 0 ≤ c * d * g ^ w * h ^ w * (g ^ 2 - h ^ 2) ^ 2 :=
    mul_nonneg (mul_nonneg (mul_nonneg hcd hgw) hhw) hsq
  linarith

/-- **Hence the bend of a positive two-mode tower is at most `1`.**

Stated in the same `bend` currency as the multiplicative screen so the two
results compose: the observed lepton bend is `≈ 12.295`, and this says the
additive class cannot exceed `1`. -/
theorem bend_le_one_of_two_positive_modes (c d g h : K) (hc : 0 < c)
    (hd : 0 ≤ d) (hg : 0 < g) (hh : 0 < h) (w : ℕ) :
    bend (fun k => c * g ^ k + d * h ^ k) w ≤ 1 := by
  have hbase : ∀ n : ℕ, 0 < c * g ^ n + d * h ^ n := by
    intro n
    have h1 : 0 < c * g ^ n := mul_pos hc (pow_pos hg n)
    have h2 : 0 ≤ d * h ^ n := mul_nonneg hd (le_of_lt (pow_pos hh n))
    linarith
  have hden : 0 < (c * g ^ w + d * h ^ w) * (c * g ^ (w + 4) + d * h ^ (w + 4)) :=
    mul_pos (hbase w) (hbase (w + 4))
  simp only [bend]
  rw [div_le_one hden]
  exact twoMode_log_convex c d g h (le_of_lt hc) hd hg hh w

/-- **Contrapositive — the form the screen is actually used in.**

A tower whose measured bend exceeds `1` is not a positive combination of two
geometric modes, whatever the coefficients and rates.  Applied to the charged
leptons (`bend ≈ 12.295`), this excludes the additive-interface shape without
any appeal to how extreme a fitted parameter would have to be. -/
theorem not_two_positive_modes_of_bend_gt_one (x : ℕ → K) (w : ℕ)
    (hx : 1 < bend x w) :
    ¬ ∃ c d g h : K, 0 < c ∧ 0 ≤ d ∧ 0 < g ∧ 0 < h ∧
      x = fun k => c * g ^ k + d * h ^ k := by
  rintro ⟨c, d, g, h, hc, hd, hg, hh, rfl⟩
  exact absurd (bend_le_one_of_two_positive_modes c d g h hc hd hg hh w)
    (not_le.mpr hx)

end QOU.Archimedean
