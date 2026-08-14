import Mathlib.Tactic

/-!
# qns-unit-layers — the two unit layers of the q-NS classical limit

Lean sibling of [`def:qns-unit-layers`](qns-unit-layers.md) (Option C of
the rescaling decision, owner-selected 2026-08-14; audit
`2026-08-14-qns-model-to-pde-uniformity-decomposition.md` §5).

The **substrate layer** carries the q-ladder as-is: wavenumbers
`[n]_q`, viscosity `ν_q = (q−1)/(2q)` (vanishing as `q → 1⁺`).  The
**physical (`c_q`) layer** rescales lengths and times by the canonical
substrate scale `c_q = 1/(q−1)` — an existing derived quantity, not a
new degree of freedom — via `X = c_q·x`, `T = c_q·t`, velocity
unrescaled.  Under this map:

- `k_phys = (q−1)·k_sub` (the ladder becomes a continuum grid of
  spacing `q−1`),
- `Ω_phys = (q−1)²·Ω_sub`,
- `ν_phys = c_q·ν_q = 1/(2q)` — **exactly**, an algebraic identity
  (`nu_phys_eq`), within `(q−1)/2` of the fixed value `1/2`
  (`nu_phys_near_half`).  The physical layer is a *fixed-viscosity*
  Navier–Stokes frame; the substrate layer is a vanishing-viscosity
  (Euler-type) frame.

All statements are field algebra over a generic linearly ordered field
(§7c).  The never-straddle rule and the layer-tagging convention live
in the `.md`.
-/

namespace QOU.FluidDynamics

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

namespace QnsUnitLayers

/-- The canonical substrate scale `c_q = 1/(q−1)` (the corpus's
    existing derived quantity; the layer conversion factor). -/
def cQ (q : K) : K := 1 / (q - 1)

/-- The substrate-layer q-ladder viscosity `ν_q = (q−1)/(2q)`. -/
def nuSub (q : K) : K := (q - 1) / (2 * q)

/-- The physical-layer viscosity: `ν_phys = c_q · ν_q`
    (the `X = c_q·x`, `T = c_q·t` rescaling with velocity unrescaled
    multiplies the viscosity by `c_q`). -/
def nuPhys (q : K) : K := cQ q * nuSub q

/-- Physical wavenumber: `k_phys = (q−1)·k_sub` (lengths scale by
    `c_q`, so wavenumbers scale by `1/c_q = q−1`). -/
def kPhys (q kSub : K) : K := (q - 1) * kSub

/-- Physical enstrophy weight: `Ω_phys = (q−1)²·Ω_sub` (the `k²`
    weight converts with the square of the wavenumber factor —
    the `ε²` weight the SF5 probe reports). -/
def omegaPhys (q omegaSub : K) : K := (q - 1) ^ 2 * omegaSub

/-- **The physical viscosity is exactly `1/(2q)`** — an algebraic
    identity, not a limit: `c_q·ν_q = (1/(q−1))·((q−1)/(2q)) = 1/(2q)`.
    The physical layer is a fixed-viscosity frame. -/
theorem nu_phys_eq (q : K) (hq : q ≠ 1) : nuPhys q = 1 / (2 * q) := by
  unfold nuPhys cQ nuSub
  have h : q - 1 ≠ 0 := sub_ne_zero.mpr hq
  field_simp

/-- **The physical viscosity is within `(q−1)/2` of `1/2`**: for
    `q = 1 + ε` with `ε > 0`,
    `1/2 − ν_phys = ε/(2(1+ε)) ≤ ε/2` and `ν_phys < 1/2`.  So the
    physical frame's viscosity converges to the fixed value `1/2` at
    rate `ε/2` — no vanishing-viscosity degeneration in this layer. -/
theorem nu_phys_near_half (ε : K) (hε : 0 < ε) :
    nuPhys (1 + ε) < 1 / 2 ∧ 1 / 2 - nuPhys (1 + ε) ≤ ε / 2 := by
  have hq : (1 : K) + ε ≠ 1 := by
    intro h
    exact absurd (by linarith : ε = 0) (ne_of_gt hε)
  rw [nu_phys_eq (1 + ε) hq]
  have h2 : (0 : K) < 2 * (1 + ε) := by positivity
  constructor
  · rw [div_lt_div_iff₀ h2 (by norm_num : (0 : K) < 2)]
    linarith
  · rw [div_sub_div _ _ (by norm_num : (2 : K) ≠ 0) (ne_of_gt h2)]
    rw [div_le_div_iff₀ (by positivity) (by norm_num : (0 : K) < 2)]
    ring_nf
    nlinarith

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- The enstrophy conversion is definitionally the squared wavenumber
    conversion: `(k_phys)²·e = (q−1)²·(k_sub²·e)` — layer conversion
    commutes with forming enstrophy densities. -/
theorem kPhys_sq_mul (q kSub e : K) :
    (kPhys q kSub) ^ 2 * e = (q - 1) ^ 2 * (kSub ^ 2 * e) := by
  unfold kPhys
  ring

end QnsUnitLayers

/-- Resolving declaration for `lean.ref`
    `qou:QOU.FluidDynamics.qns_unit_layers`: the two-layer convention
    is well-formed — the conversions are mutually consistent and the
    physical layer has fixed viscosity.  Conjoins the two structural
    facts: `ν_phys = 1/(2q)` exactly, and the enstrophy weight
    converts by `(q−1)²`. -/
theorem qns_unit_layers (q : K) (hq : q ≠ 1) :
    QnsUnitLayers.nuPhys q = 1 / (2 * q) ∧
    (∀ kSub e : K, (QnsUnitLayers.kPhys q kSub) ^ 2 * e
      = (q - 1) ^ 2 * (kSub ^ 2 * e)) :=
  ⟨QnsUnitLayers.nu_phys_eq q hq, fun kSub e => QnsUnitLayers.kPhys_sq_mul q kSub e⟩

end QOU.FluidDynamics
