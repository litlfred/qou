import Mathlib.Tactic

namespace QOU.ParticleInteractions

/-! ## Meson scale independence — geometric content

The substantive reason `m_π` cannot be set from `(m_e, q_0)` alone is
geometric: the per-knot mass scale is carried by the **hyperbolic
volume** of the knot/link complement (`m(K) ∝ Vol(K) · ρ(K) / ℏ_q²`),
and the meson's binding topology is the **Hopf link**, whose complement
is a solid torus with hyperbolic volume `0`. The baryon (Borromean)
complement, by contrast, has positive hyperbolic volume `8G ≈ 7.328`.
With a vanishing geometric invariant the meson has no scale-setting
datum derivable from `(m_e, q_0)`; the absolute scale must enter as the
independent calibration input CAL-3 (`P_avg^π`, the pion-sector bar-even channel).

Ref: [leitner2026] prop:meson-scale-independence
-/

/-- Hyperbolic volume of the Hopf-link complement (a solid torus): `0`. -/
def hopfComplementVolume : ℝ := 0

/-- Hyperbolic volume of the Borromean complement `Vol(𝓑₃) = 8G`
    (`G` = Catalan's constant), the baryon geometric mass scale. -/
def borromeanComplementVolume : ℝ := 7.32772

/-- **Meson scale independence (geometric core).**

    The pion mass `m_π` cannot be derived from the substrate parameters
    `(m_e, q_0)` alone. The per-knot mass scale is the product
    `m_e · Vol(K) · ρ(K) / ℏ_q²`; for the meson the binding topology is
    the Hopf link, whose complement has hyperbolic volume `0`, whereas
    the baryon's Borromean complement has strictly positive volume. So
    the geometric invariant that would fix a mass scale from `(m_e, q_0)`
    **vanishes** for the meson — the scale must come from the independent
    calibration `P_avg^π` (CAL-3).

    The Lean content is exactly this geometric obstruction: the meson
    volume is `0` while the baryon volume is positive, so the linear
    volume-scaling map sends the meson's geometric scale to `0`
    independently of `(m_e, q_0)`. -/
-- Ref: [leitner2026] prop:meson-scale-independence
theorem meson_scale_independence :
    hopfComplementVolume = 0
      ∧ 0 < borromeanComplementVolume
      ∧ ∀ m_e ℏq_inv2 : ℝ, m_e * hopfComplementVolume * ℏq_inv2 = 0 := by
  refine ⟨rfl, by norm_num [borromeanComplementVolume], ?_⟩
  intro m_e ℏq_inv2
  simp [hopfComplementVolume]

end QOU.ParticleInteractions
