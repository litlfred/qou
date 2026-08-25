-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Nucleon Hecke element: product of Borromean braid and typed crossings

/-- The nucleon Hecke element for a flavor triple (f₁, f₂, f₃):
    𝔑(f₁,f₂,f₃) = 𝓑₃ · C(f₁,f₂;σ₀) · C(f₁,f₃;σ₀) · C(f₂,f₃;σ₁)

    After Groebner-Shirshov reduction, each nucleon has exactly 6 terms
    (one per S₃ basis element). -/
structure NucleonHeckeElement where
  /-- Flavor assignment: proton = (u,u,d), neutron = (u,d,d). -/
  flavors : Fin 3 → Bool  -- True = up, False = down
  /-- NF coefficients after reduction (6 basis elements). -/
  nfCoeffs : Fin 6 → Int

/-- Proton flavor assignment: (up, up, down). -/
def protonFlavors : Fin 3 → Bool
  | 0 => true   -- up
  | 1 => true   -- up
  | 2 => false  -- down

/-- Neutron flavor assignment: (up, down, down). -/
def neutronFlavors : Fin 3 → Bool
  | 0 => true   -- up
  | 1 => false  -- down
  | 2 => false  -- down

/-- The proton and neutron have different flavor assignments. -/
theorem proton_ne_neutron : protonFlavors ≠ neutronFlavors := by
  intro h
  exact Bool.noConfusion (congrFun h 1)
