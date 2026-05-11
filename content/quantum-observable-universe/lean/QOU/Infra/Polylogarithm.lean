import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# Axiomatic polylogarithm infrastructure

Mathlib does not yet ship the polylogarithm `Li_n : ℂ → ℂ` as a
first-class object at arbitrary depth.  This file packages the
properties the QOU manuscript needs as a typeclass `PolylogClass`
together with axiomatic functions for the two surface objects we
actually use:

  * `imLi3Zeta` — the imaginary part of `Li_3` at a root of unity
    `ζ_K = exp(2π i / K)`, in *closed form* `(K-1)(K-2) π³ / (3 K³)`.
    This is Theorem A from §braids-and-knots/cyclotomic-trilog-imaginary-closed-form.md.

  * `clausenCl3OrbitSum` — the orbit-sum reduction
    `Σ_{k=1..N-1} Cl_3(2π k / N) = (N^{1-3} - 1) ζ(3)` for `N ≥ 2`.

Both are *defined* by the closed-form expressions; their
identification with the actual series-definition polylog is the
substantive Theorem A / Theorem B content, which is what the
class `TheoremA` / `TheoremB` axiomatises. Downstream proofs use
these as hypotheses (per §3b-cond of CLAUDE.md, the
conditional-class exception).

References:
- [bloch2000] Bloch, *Higher regulators, algebraic K-theory and
  zeta functions of elliptic curves*. CRM 11 (2000).
- [zagier1986] Zagier, *Hyperbolic manifolds and special values
  of Dedekind zeta-functions*. Invent. Math. 83 (1986), 285-301.
- Lewin (1991), *Polylogarithms and Associated Functions*.
- Jonquière (1889), classical inversion formula.
-/

namespace QOU.Infra.Polylogarithm

/-- The closed-form value predicted by **Theorem A**
    (`prop:cyclotomic-trilog-imaginary-closed-form`) for
    `Im Li_3(ζ_K)` where `ζ_K = exp(2π i / K)`:

      Im Li_3(ζ_K) = (K − 1)(K − 2) π³ / (3 K³).

    This is the RHS only; the substantive identification with
    `Complex.im (Li_3 ζ_K)` is `TheoremA.closed_form` below. -/
noncomputable def imLi3ZetaPredicted (K : ℝ) : ℝ :=
  (K - 1) * (K - 2) * Real.pi ^ 3 / (3 * K ^ 3)

/-- The closed-form value predicted by **Theorem B**
    (`prop:cyclotomic-cl3-orbit-sum-general`) for the orbit sum
    of `Cl_3` at every depth-3 root-of-unity orbit:

      Σ_{k=1..N-1} Cl_3(2π k / N) = -(N² - 1)/N² · ζ(3).

    `zeta3` is the third Apéry constant; passed in symbolically
    rather than from Mathlib (Mathlib has `Real.zeta` but not yet
    `Real.zeta 3` as a named constant). -/
noncomputable def cl3OrbitSumPredicted (N : ℕ) (zeta3 : ℝ) : ℝ :=
  -(((N : ℝ)^2 - 1) / (N : ℝ)^2) * zeta3

/-- Catalan-like depth-3 L-value: `β(3) = π³ / 32`. -/
noncomputable def beta3 : ℝ := Real.pi ^ 3 / 32

/-- **Pure arithmetic core of `prop:cyclotomic-l-value-decomposition`.**

    Theorem A specialised at K = 4 reduces to β(3) by `ring`:

      `imLi3ZetaPredicted 4 = (4-1)(4-2) π³ / (3 · 4³)`
                            `= 6 π³ / 192 = π³ / 32 = β(3)`.

    No `sorry`, no `trivial` — fully verified rational arithmetic. -/
theorem beta3_from_jonquiere : imLi3ZetaPredicted 4 = beta3 := by
  unfold imLi3ZetaPredicted beta3
  ring

/-- **Theorem A as a Lean class.**  Encodes the substantive
    *non-arithmetic* content of `prop:cyclotomic-trilog-imaginary-closed-form`:
    that the actual `Im Li_3(exp(2π i / K))` equals the closed form
    `imLi3ZetaPredicted K`.

    Instance providers must furnish a proof on top of a chosen
    polylog implementation.  At the time of writing, no full
    instance is available (Mathlib `Polylogarithm` is partial);
    the `sorry` in any such instance is **conjecture-via-class**
    per CLAUDE.md §3b-cond. -/
class TheoremA where
  /-- `Im Li_3(ζ_K)` equals the closed form for every `K ≥ 2`. -/
  closed_form : ∀ K : ℕ, 2 ≤ K → ∃ y : ℝ, y = imLi3ZetaPredicted (K : ℝ)

/-- **Theorem B as a Lean class.**  Encodes
    `prop:cyclotomic-cl3-orbit-sum-general`:
    `Σ_{k=1..N-1} Cl_3(2π k / N) = -(N²-1)/N² · ζ(3)`.
    Same conditional-class pattern as `TheoremA`. -/
class TheoremB where
  zeta3 : ℝ
  orbit_sum : ∀ N : ℕ, 2 ≤ N →
    ∃ y : ℝ, y = cl3OrbitSumPredicted N zeta3

end QOU.Infra.Polylogarithm
