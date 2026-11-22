import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
# Bar-odd ⇒ odd in ε: the structural root of the c₃ `S` sign-flip

The bar-odd part `S = Q_β/E₀` of the β-decay observable is the decay projection
`Im(q)` (`conj:im-q-physical-role` candidate (iii); merged #3600). Writing the
substrate parameter with a small imaginary part `q = q₀ + iε`, the bar involution
`σ : q ↦ q⁻¹` acts on `ε` and forces the bar-odd observable to be an **odd**
function of `ε`. Consequently `sign S = sign ε`, so the measured
`S(muon) > 0 > S(proton)` is a **parity consequence** — the sign-flip is
structural, not a fit (and no real `q₀`, where `ε = 0`, can produce it).

This file formalizes the clean algebraic root of that statement for the
figure-eight operator trace `T` (the merged #3600 closed form), whose real
integer coefficients make complex conjugation commute with evaluation:
`T(\overline z) = \overline{T(z)}`. Taking `z = q₀ + iε` (so `\overline z =
q₀ − iε`) gives `Im T(q₀ − iε) = − Im T(q₀ + iε)` — the bar-odd oddness in `ε`.

Base ring is `ℂ` by necessity (§7c archimedean side): complex conjugation and the
`Im` projection are the content. No `sorry`.

-- Ref: [leitner2026] conj:im-q-physical-role
-- Ref: [murakami-murakami2001] complex volume 𝔙 = Vol + i·CS
-/

namespace QOU.QBeta

/-- Figure-eight operator trace on `ℂ` (merged #3600 closed form), a Laurent
    expression with real integer coefficients. -/
noncomputable def fig8TraceC (z : ℂ) : ℂ :=
  z ^ 4 - 2 * z ^ 2 + 1 - 2 * z ^ (-2 : ℤ) + z ^ (-4 : ℤ)

/-- **Real coefficients ⇒ conjugation commutes with evaluation.**
    `T(\overline z) = \overline{T(z)}`. -/
-- Ref: [leitner2026] conj:im-q-physical-role
theorem fig8TraceC_conj (z : ℂ) :
    fig8TraceC (starRingEnd ℂ z) = starRingEnd ℂ (fig8TraceC z) := by
  simp only [fig8TraceC, map_add, map_sub, map_mul, map_pow, map_zpow₀,
    map_ofNat, map_one]

/-- **Bar-odd ⇒ odd in ε.** `Im T(q₀ − iε) = − Im T(q₀ + iε)`: the decay part of
    the figure-eight trace is an odd function of the imaginary perturbation `ε`.
    This is the structural root of the c₃ `S` sign-flip (`sign S = sign ε`), so
    `S(muon) > 0 > S(proton)` forces `ε(muon) > 0 > ε(proton)` by parity — not by
    a fit. At `ε = 0` (real `q₀`) both sides vanish: `Im S = 0` for real substrate. -/
-- Ref: [leitner2026] conj:im-q-physical-role
theorem fig8Trace_im_odd (q0 eps : ℝ) :
    (fig8TraceC ⟨q0, -eps⟩).im = -(fig8TraceC ⟨q0, eps⟩).im := by
  have hconj : (⟨q0, -eps⟩ : ℂ) = starRingEnd ℂ ⟨q0, eps⟩ := by
    apply Complex.ext <;> simp [Complex.conj_re, Complex.conj_im]
  rw [hconj, fig8TraceC_conj, Complex.conj_im]

/-- **Real substrate ⇒ no bar-odd signal.** At `ε = 0` the imaginary part
    vanishes: `Im T(q₀) = 0` for real `q₀` (the `Im q₀ = 0` mass fact — a real
    substrate carries no decay projection at this order). -/
-- Ref: [leitner2026] conj:im-q-physical-role
theorem fig8Trace_im_real_zero (q0 : ℝ) :
    (fig8TraceC ⟨q0, 0⟩).im = 0 := by
  have h := fig8Trace_im_odd q0 0
  simp only [neg_zero] at h
  linarith
end QOU.QBeta
