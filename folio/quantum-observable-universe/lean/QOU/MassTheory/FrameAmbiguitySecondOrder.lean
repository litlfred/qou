/-
# The bar-odd-tier resummation is ambiguous at **second order** — why `r = g₂−1` is a frame artifact

The deuteron binding is organised as `B = E₀ · C(q₀)`, `E₀ = μ₀ ℏ_q [3]_q[4]_q` (the naive q-Casimir),
with a total correction `C` split into a bar-odd tier `t = (v−v⁻¹)/[2]_v` and a bar-even tier `h²`.
The *frame* is the choice of how to resum the bar-odd tier into `C`. Two equally-motivated choices —

```
C_inv = 1/(1 − t)      (geometric / propagator resummation)
C_lin = 1 + t          (first-order / additive)
```

agree at first order (`1 + t + O(t²)`) but their difference is **exactly second order** in `t`:

```
C_inv − C_lin = t² / (1 − t).
```

This file proves that identity (a `Field` identity, §7c generic `R`), and its consequence: the
bar-even coefficient `g₂`, being extracted at order `h²` *after* dividing out the bar-odd frame,
inherits this `O(t²)` ambiguity. Since `t = O(h)`, the frame difference is `O(h²)` — the **same order
as the whole bar-even signal `g₂·h²`**. Hence `r = g₂ − 1` is not frame-invariant: its value depends
on the bar-odd resummation convention (empirically it swings `~12×` its own size across natural
frames, `deuteron_g2_frame_artifact_probe.py`).

**What survives frame choice** is the prediction *through* `O(t)` (equivalently `O(h)`): every frame
agrees there, giving `B(deuteron)` to `~0.3–0.8%`. The sub-`0.1%` figure and the specific value
`g₂ = 1.0087` require picking one `O(t²)`-resummation and are therefore **not** frame-independent.

This file does not derive `B`; it machine-checks the second-order frame ambiguity that makes `r`
ill-posed and pins the frame-independent content to first order.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.MassTheory.FrameAmbiguity

variable {R : Type*} [Field R]

/-- Geometric (propagator) resummation of the bar-odd tier. -/
def Cinv (t : R) : R := 1 / (1 - t)

/-- First-order (additive) form of the bar-odd tier. -/
def Clin (t : R) : R := 1 + t

/-- **The two resummations agree at first order and differ at exactly second order:**
`1/(1−t) − (1+t) = t²/(1−t)`. The frame ambiguity is `O(t²)`, never `O(t)`. -/
theorem frame_diff_second_order (t : R) (ht : t ≠ 1) :
    Cinv t - Clin t = t ^ 2 / (1 - t) := by
  unfold Cinv Clin
  have h1t : (1 : R) - t ≠ 0 := sub_ne_zero.mpr (fun h => ht h.symm)
  field_simp
  ring

/-- **The bar-even coefficient inherits the `O(t²)` frame difference.** With the bar-even tier
extracted as `g = (C − 1)/h²` after using bar-odd frame `C`, the two frames differ by
`(Cinv − Clin)/h² = t²/((1−t) h²)`. Since `t = O(h)`, this is `O(1)` in `h` — the same size as `g`
itself, so `g` (hence `r = g − 1`) is **not** frame-invariant. -/
theorem g_frame_difference (t hsq : R) (ht : t ≠ 1) (hh : hsq ≠ 0) :
    (Cinv t - 1) / hsq - (Clin t - 1) / hsq = t ^ 2 / ((1 - t) * hsq) := by
  unfold Cinv Clin
  have h1t : (1 : R) - t ≠ 0 := sub_ne_zero.mpr (fun h => ht h.symm)
  field_simp
  ring

/-- **First-order (frame-invariant) content.** Both frames reduce to `1 + t` modulo `O(t²)`:
their difference vanishes to first order, so the prediction *through* `O(t)` is frame-independent.
Stated as: the linearisations coincide (`Clin` is the common first-order part, and `Cinv − Clin` has
no constant or linear term — it is `t²·(1/(1−t))`). -/
theorem common_first_order (t : R) (ht : t ≠ 1) :
    Cinv t - Clin t = t ^ 2 * (1 / (1 - t)) := by
  rw [frame_diff_second_order t ht]; ring

end QOU.MassTheory.FrameAmbiguity
