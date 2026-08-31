/-
# Serre's elliptic curve for Bring's curve has `j = −25/2`

Beans `qou-pdix` (route 5) / `qou-cds1` (branch 3). Companion to
`computations/qbeta/qbeta_bring_elliptic_generator_probe.py`.

Bring's curve — the genus-4 quintic `Σxᵢ = Σxᵢ² = Σxᵢ³ = 0` with automorphism
group `S₅` — has a **naturally associated elliptic curve**. Riera–Rodríguez,
*The period matrix of Bring's curve* (Pacific J. Math. 154 (1992) 179–200), in
the library here, records Serre's result: the Jacobian is isogenous to `E⁴` with

    E :  y² = x³ − 675x − 79650,

and shows the period matrix diagonalises to `(5τ, 5τ, 5τ, τ)`.

This file pins the one exact number in that: `j(E) = −25/2`, from
`j = 1728·4A³/(4A³ + 27B²)`. It is a rational identity, so it is recorded here
rather than left to a floating-point probe — the probe checks it too, but a
transcription of a library value should have a proof next to it.

**Why it matters for route 5, and what it does not settle.** Step 18
(`HolonomySpectrumSignObstruction`) showed the ladder needs an **elliptic**
generator, and Step 19 (`ImQCannotSupplyEllipticGenerator`) refuted `Im(q)` as
the source. An elliptic *curve* is a different and better-motivated candidate: a
flat **unitary** connection on a torus has monodromy in `U(1) × U(1)`, which is
elliptic by construction — so this is the first candidate source that passes the
tier-0 test `D0` in principle.

But `−25/2` is **not** a CM `j`-invariant. Every CM `j` is a rational **integer**
(`0, 1728, −3375, 8000, 54000, −32768, …`), and `−25/2` is not an algebraic
integer at all. So `E` has no complex multiplication, its modular parameter `τ`
has no closed form, and the curve hands the ladder no *derived* phase — which was
the whole appeal of "naturally associated". `not_cm_j_invariant` below records the
half of that which is provable here: `−25/2` is not an integer.

The measured half is in the probe: `τ = 1/2 + 0.933382…i` (with `Re τ = 1/2`
forced, since `j` is real and negative), so the natural holonomy angle
`2π·Re τ = π` is a **sign**, not a tunable phase; and no declared natural phase
lands within a factor of 20 of the required `θ = 0.0565947`.

Scope-(a): a transcription check with its provenance. Nothing derived, proposed,
wired or readmitted; `E` is not adopted as the ladder's source.
-/
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Rat.Cast.Order

namespace QOU.QBeta

/-- The `j`-invariant of `y² = x³ + Ax + B` is `1728·4A³/(4A³ + 27B²)`. For
Serre's curve `A = −675`, `B = −79650` this is exactly `−25/2`. -/
theorem bring_serre_j_invariant :
    (1728 : ℚ) * (4 * (-675) ^ 3) / (4 * (-675) ^ 3 + 27 * (-79650) ^ 2) = -25 / 2 := by
  norm_num

/-- The discriminant denominator is nonzero, so the quotient above is the
`j`-invariant of a genuine elliptic curve rather than a degenerate cubic. -/
theorem bring_serre_nonsingular :
    (4 : ℚ) * (-675) ^ 3 + 27 * (-79650) ^ 2 ≠ 0 := by
  norm_num

/-- **`−25/2` is not an integer**, hence not a CM `j`-invariant: every
complex-multiplication `j` is a rational integer. So Serre's `E` has no CM, its
modular parameter has no closed form, and it supplies no *derived* phase. -/
theorem not_cm_j_invariant : ¬ ∃ n : ℤ, ((-25 : ℚ) / 2) = (n : ℚ) := by
  rintro ⟨n, hn⟩
  have h : (-25 : ℚ) = 2 * (n : ℚ) := by linarith [hn]
  have h3 : (-25 : ℤ) = 2 * n := by exact_mod_cast h
  -- 2 ∣ 25 is false; `2 * n = -25` forces an even number to equal an odd one
  have : (2 : ℤ) ∣ 25 := ⟨-n, by linarith⟩
  norm_num at this

end QOU.QBeta
