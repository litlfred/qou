# Handover: Leray ODE Simulator

## Context

Chapter 7 (Fluid Dynamics of the Brane), §4, block `prop:leray-profile`
establishes that the self-similar blowup profile reduces to a single
nonlinear radial ODE for the fundamental mode (j = 1/2):

```
ν(R'' + 2R'/r - λ·R/r²) + R/2 + rR'/2 = N·R·R'
```

where:
- ν > 0: classical viscosity
- λ = [1/2]_q · [3/2]_q ≈ 0.75 at q = 1.110
- N: Clebsch-Gordan coupling coefficient for 1/2 ⊗ 1/2 → 0

Boundary conditions:
- r → 0: R(r) ~ r (linear vanishing, regularity exponent ℓ = 1)
- r → ∞: R(r) = O(r^{-5/2}) (L² integrability)

## Task

Build an interactive simulator (Pyodide/HTML) that:

1. **Solves the shooting problem**: sweep R'(0) to find the value(s)
   where the solution decays at infinity instead of blowing up.

2. **Visualises the profile**: plot R(r) for the successful shot(s),
   showing the self-similar blowup velocity profile.

3. **Parameter exploration**: sliders for ν, q (which sets λ via the
   q-Casimir), and the coupling N.

4. **Convergence check**: show that as q → 1, the profile approaches
   a classical (non-q-deformed) Leray profile.

## Mathematical details

### The q-Casimir at j = 1/2

Using [n]_q = (q^n - q^{-n})/(q - q^{-1}):

```
λ(q) = [1/2]_q · [3/2]_q
     = (q^2 + q^{-2} - q - q^{-1}) / (q - q^{-1})^2
```

At q = 1.110: λ ≈ 0.75
At q = 1: λ → 1·2/4 = 3/4 (classical j(j+1) = 3/4)

### The Clebsch-Gordan coefficient

The 1/2 ⊗ 1/2 → 0 channel has coupling:
```
N = √(2) · [2]_q^{-1/2}
```
where [2]_q = (q² - q⁻²)/(q - q⁻¹) = q + q⁻¹.

### Numerical method

Standard shooting:
1. Set R(ε) = ε, R'(ε) = s (the shooting parameter), for small ε > 0.
2. Integrate the ODE outward using RK4 or scipy.integrate.solve_ivp.
3. Monitor R(r) as r → ∞. Most values of s give R → ±∞.
4. Find s* where R decays. This is the blowup profile.

The ODE has a singularity at r = 0 (the λ/r² term). Start
integration at r = ε ≈ 0.01, not r = 0.

### Expected output

A nontrivial R(r) with:
- R(r) > 0 for r ∈ (0, r₀) (positive near origin)
- R(r₀) = 0 at some finite r₀ (first zero)
- R(r) oscillating and decaying for r > r₀

The number of zeros corresponds to the vortex intensity level j.
The fundamental profile (no zeros before decay) gives the electron.

## Files

- Content block: `ch10-fluid-dynamics/leray-profile.md`
- Lean structures: `lean/QOU/GaugeFieldFluidDynamics.lean` §15
  (TruncatedLerayProfile, regularity_exponent, fusion_half_half)
- Simulator should go in: `folio-assistant/simulators/leray-ode/`
- Use the `simulator` skill + `local/simulator` for implementation

## Dependencies

- Pyodide (Python in browser) for ODE solving
- scipy.integrate.solve_ivp (available in Pyodide)
- matplotlib or plotly for visualisation
- The `sim:` block type in the content schema
