import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Weak-scale factorisation of the β-decay rate (bean `qou-99qc`)

The rate `𝔇 = G² · M2 · mₑ⁵ · f / (2π³)` with the W-exchange relation
`G = s · g² / (8 · m²)`, `s² = 2` (`s` stands for `√2`). Everything is stated over a
generic field `K`; `π` enters as a nonzero parameter `p`, so nothing here is archimedean.

What this file shows, and what it does not:

* `rate_via_W` — once `G` is expressed through `(g, m)`, the rate depends on the weak
  scale only through the dimensionless ratio `mₑ / m`, to the fourth power.
* `rate_ratio_of_scales` — two weak scales give rates in the ratio `(m' / m)⁴`; the rate
  pins the scale at most up to that fourth root, and only once `g` is fixed.
* `normSq_eq` — the derived charged-current factor `(q² − 1)²` equals `q² h²`,
  `h = q − q⁻¹` (the h-term of the strand-tracked crossing, `ChargedCurrentW.lean`).
* `volume_channel_gives_no_fermi_scale` — the canonical volume channel
  `m = mₑ · V · ρ / ℏ²` evaluated at `V = 0` (every torus knot or link, including the
  corpus's β vertex `T_{3,5}` and its conjectural `W = T(2,4)`) returns `0`, and no `G`
  satisfies the W-exchange relation at that scale unless `s · g² = 0`. So that channel
  supplies no W scale. It does **not** say the W is massless: the corpus reading
  (`rem:pion-mass-hyperbolic-threshold`) is that the mass is not derivable from volume.

No physical value of `g`, `m_W` or `G_F` is derived here.
-/

namespace QOU.QuarkState.WeakScaleFactorisation

variable {K : Type*} [Field K]

theorem n32_ne (h2 : (2 : K) ≠ 0) : (32 : K) ≠ 0 := by
  rw [show (32 : K) = 2 ^ 5 by norm_num]; exact pow_ne_zero _ h2

theorem n64_ne (h2 : (2 : K) ≠ 0) : (64 : K) ≠ 0 := by
  rw [show (64 : K) = 2 ^ 6 by norm_num]; exact pow_ne_zero _ h2

/-- The β-decay rate in terms of the Fermi constant `G`. -/
def rate (p G M2 me f : K) : K := G ^ 2 * M2 * me ^ 5 * f / (2 * p ^ 3)

/-- The tree-level W-exchange Fermi constant `G = s g² / (8 m²)` (`s = √2`). -/
def fermiOfW (s g m : K) : K := s * g ^ 2 / (8 * m ^ 2)

/-- With `s² = 2`, `G² = g⁴ / (32 m⁴)`. -/
theorem fermiOfW_sq (s g m : K) (hs : s ^ 2 = 2) (hm : m ≠ 0) (h2 : (2 : K) ≠ 0) :
    fermiOfW s g m ^ 2 = g ^ 4 / (32 * m ^ 4) := by
  unfold fermiOfW
  rw [div_pow, mul_pow, mul_pow, hs]
  have h8 : (8 : K) ≠ 0 := by
    rw [show (8 : K) = 2 * 2 * 2 by norm_num]; exact mul_ne_zero (mul_ne_zero h2 h2) h2
  have h32 := n32_ne h2
  field_simp
  ring

/-- **The rate depends on the weak scale only through `(mₑ / m)⁴`.** -/
theorem rate_via_W (p s g m M2 me f : K) (hs : s ^ 2 = 2) (hm : m ≠ 0) (hp : p ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    rate p (fermiOfW s g m) M2 me f
      = g ^ 4 * M2 * f * me * (me / m) ^ 4 / (64 * p ^ 3) := by
  unfold rate
  rw [fermiOfW_sq s g m hs hm h2]
  have h32 := n32_ne h2
  have h64 := n64_ne h2
  field_simp
  ring

/-- **Two weak scales:** at fixed `g`, the rates are in the ratio `(m' / m)⁴`. -/
theorem rate_ratio_of_scales (p s g m m' M2 me f : K) (hs : s ^ 2 = 2) (hm : m ≠ 0)
    (hm' : m' ≠ 0) (hp : p ≠ 0) (h2 : (2 : K) ≠ 0)
    (hg : g ≠ 0) (hM : M2 ≠ 0) (hf : f ≠ 0) (hme : me ≠ 0) :
    rate p (fermiOfW s g m) M2 me f / rate p (fermiOfW s g m') M2 me f = (m' / m) ^ 4 := by
  rw [rate_via_W p s g m M2 me f hs hm hp h2, rate_via_W p s g m' M2 me f hs hm' hp h2]
  have h64 := n64_ne h2
  field_simp

/-- **The derived charged-current factor:** `(q² − 1)² = q² h²`, `h = q − q⁻¹`. -/
theorem normSq_eq (q : K) (hq : q ≠ 0) : (q ^ 2 - 1) ^ 2 = q ^ 2 * (q - q⁻¹) ^ 2 := by
  field_simp

/-- The canonical volume channel `m = mₑ V ρ / ℏ²`. -/
def volumeMass (me V ρ ħ : K) : K := me * V * ρ / ħ ^ 2

/-- **No W scale from the volume channel on a `Vol = 0` carrier.** At `V = 0` the
channel returns `0`, and then no Fermi constant `G` solves `G · 8 m² = s g²`
unless `s g² = 0`. -/
theorem volume_channel_gives_no_fermi_scale (me ρ ħ s g : K) (hsg : s * g ^ 2 ≠ 0) :
    ¬ ∃ G : K, G * (8 * volumeMass me 0 ρ ħ ^ 2) = s * g ^ 2 := by
  rintro ⟨G, hG⟩
  apply hsg
  rw [← hG]
  unfold volumeMass
  ring

/-- Converse sanity check: at a nonzero scale the relation is solved by `fermiOfW`. -/
theorem fermiOfW_solves (s g m : K) (hm : m ≠ 0) (h2 : (2 : K) ≠ 0) :
    fermiOfW s g m * (8 * m ^ 2) = s * g ^ 2 := by
  unfold fermiOfW
  have h8 : (8 : K) ≠ 0 := by
    rw [show (8 : K) = 2 * 2 * 2 by norm_num]; exact mul_ne_zero (mul_ne_zero h2 h2) h2
  field_simp

end QOU.QuarkState.WeakScaleFactorisation
