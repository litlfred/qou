import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.MeanInequalities
import Mathlib.Tactic

/-!
# QOU.OneDim.TLIsXXZChain — the production trace's algebra is the 1D XXZ chain

**What this settles.** The corpus already proves that the production Markov
trace is the `SU_q(2)` / Temperley–Lieb one: `FibreDimensionForcesTL.lean`
derives `z · [N]_q = q ^ N` from a fibre of quantum dimension `[N]_q`, which at
`N = 2` is convention D (`z_D = q³/(q²+1)`), and `MarkovTraceTLUniqueness.lean`
closes the converse. Neither says what the Temperley–Lieb algebra *is* as a
mechanics.

This file supplies that step. Writing `e` for a Temperley–Lieb generator on two
neighbouring sites of `(R²)^{⊗n}`, the operator identity

    -2 • e = (XX + YY + Δ • ZZ) - Δ • I - ((q - q⁻¹)/2) • (sz₁ - sz₂)

holds with `Δ = (q + q⁻¹)/2`; summing over `i` and telescoping the boundary
term gives the **open `U_q(sl₂)`-symmetric XXZ chain** on `n` sites. So the
algebra the shipped pipeline computes in is a one-dimensional spin chain.

**What is proved here, and what is delegated.** In the basis `(↑↑, ↑↓, ↓↑, ↓↓)`
that matrix identity has five entries, three of which are `0 = 0`. The two that
carry content are the scalar identities `twoMul_eq` / `twoInv_eq` below — the
statement that the anisotropy and the Hecke parameter `h = q - q⁻¹` recombine
to `2q` and `2q⁻¹` on the two singlet-channel diagonal entries. Those are the
file's algebraic content and are proved here, over a generic field (AGENTS.md
§7c — no `ℝ`, no ordering, nothing archimedean).

The matrix assembly itself is verified numerically at `mp.dps = 60`, at both
documented `q₀` pins, in
`computations/onedim/tl_is_the_xxz_chain_probe.py` (17/17), which also carries
the provenance caution: **the boundary sign was recalled wrong on first
attempt**, and the coefficients are solved from the matrix entries rather than
remembered.

**The regime claim** (`one_lt_anisotropy`) needs an ordering and so is stated
over `ℝ`, after the substrate→archimedean wall, in its own section.

-- Ref: [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-/

namespace QOU.OneDim

section Algebraic

variable {R : Type*} [Field R] {q : R}

/-- The Temperley–Lieb loop weight `δ = q + q⁻¹`, i.e. the balanced quantum
integer `[2]_q`. This is the norm `⟨w, w⟩` of the `q`-deformed singlet
`w = q^{1/2}|↑↓⟩ - q^{-1/2}|↓↑⟩`, hence the scalar in `e² = δ • e`. -/
def tlLoop (q : R) : R := q + q⁻¹

/-- The XXZ anisotropy, `Δ = δ/2`. Over `ℝ` with `q > 0` this is `cosh (log q)`. -/
def xxzAnisotropy (q : R) : R := tlLoop q / 2

/-- The Hecke parameter `h = q - q⁻¹`, the right-hand side of the Hecke
relation `σ² = h·σ + 1`. It is the coefficient of the boundary term that makes
the chain `U_q(sl₂)`-symmetric rather than `SU(2)`-symmetric. -/
def heckeH (q : R) : R := q - q⁻¹

/-- **Content of the `|↑↓⟩` diagonal entry.** The anisotropy and the Hecke
parameter recombine to `2q`: this is why the TL generator's `(↑↓,↑↓)` entry is
`q` and not something requiring a further constant. -/
theorem twoMul_eq (hq : q ≠ 0) :
    2 * xxzAnisotropy q + heckeH q = 2 * q := by
  unfold xxzAnisotropy tlLoop heckeH
  field_simp
  ring

/-- **Content of the `|↓↑⟩` diagonal entry**, the partner of `twoMul_eq`: the
same two quantities recombine to `2q⁻¹` with the opposite sign on `h`. The two
together are the whole non-trivial content of the two-site matrix identity. -/
theorem twoInv_eq (hq : q ≠ 0) :
    2 * xxzAnisotropy q - heckeH q = 2 * q⁻¹ := by
  unfold xxzAnisotropy tlLoop heckeH
  field_simp
  ring

/-- The anisotropy is the half-sum, stated so downstream files need not unfold. -/
theorem xxzAnisotropy_eq (q : R) : xxzAnisotropy q = (q + q⁻¹) / 2 := rfl

/-- `δ` and `h` determine `q`: their half-sum is `q`. Records that no
information is lost in passing from the Hecke presentation to the chain
presentation — the map is invertible, not a projection. -/
theorem tlLoop_add_heckeH (hq : q ≠ 0) : (tlLoop q + heckeH q) / 2 = q := by
  unfold tlLoop heckeH
  field_simp
  ring

end Algebraic

section Archimedean

/-! ### The regime claim

This section needs an ordering, so it is stated over `ℝ` and sits after the
substrate→archimedean wall (AGENTS.md §7c). -/

/-- **The substrate is in the massive (Ising-like) regime.** For real `q > 0`
with `q ≠ 1`, the XXZ anisotropy exceeds `1`.

This is what makes Bethe strings *stable bound states* rather than scattering
states: `Δ > 1` is the gapped, Ising-like phase of the XXZ chain, whereas
`|Δ| < 1` is the massless phase where no such bound states survive.

It carries **no calibration input and no free parameter**: the conclusion
follows from `q ≠ 1` alone, so it is forced by the substrate being a genuine
deformation rather than fitted to reproduce anything. The numerical value at
`q₀` is `Δ - 1 ≈ 5.448e-3`, agreeing between the two documented pins to
~1.2 ppb (measured in the probe cited above) — so the verdict does not depend
on which pin is used. -/
theorem one_lt_anisotropy {q : ℝ} (hpos : 0 < q) (hne : q ≠ 1) :
    1 < xxzAnisotropy q := by
  have hq : q ≠ 0 := ne_of_gt hpos
  have hne' : q - 1 ≠ 0 := sub_ne_zero.mpr hne
  have hsq : 0 < (q - 1) ^ 2 := by positivity
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  -- multiplying `q + q⁻¹ > 2` through by `q > 0` is exactly `(q - 1)² > 0`
  have key : (2 : ℝ) < q + q⁻¹ := by nlinarith [hsq, hinv, hpos]
  unfold xxzAnisotropy tlLoop
  linarith

/-- Contrapositive form: an anisotropy at or below `1` forces `q = 1`, i.e. the
undeformed (classical) point. There is no real `q ≠ 1` giving a massless chain,
so the massless phase is unreachable from a real substrate parameter — it
requires `|q| = 1`, which the corpus's `q₀ ≈ 1.10998` is not. -/
theorem eq_one_of_anisotropy_le {q : ℝ} (hpos : 0 < q)
    (h : xxzAnisotropy q ≤ 1) : q = 1 := by
  by_contra hne
  exact absurd h (not_le.mpr (one_lt_anisotropy hpos hne))

end Archimedean

end QOU.OneDim
