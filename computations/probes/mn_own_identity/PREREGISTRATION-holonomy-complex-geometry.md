# Pre-registration: complex geometry of the holonomy eigenvalue pair (2026-11-21)

Committed before `mn_holonomy_complex_geometry_probe.py` is run. Owner: *"try complex first ..
look at complex Geom"*, falling back to the block trace.

## Object

The (2,1)-block eigenvalues `λ±` of `B₃ = (σ₀σ₁⁻¹)³` on `W_p` (identical on `W_n`, §21), with
`μ± = λ± − 1`. Their characteristic polynomial is `t² + c₁t + 1` (§21), so `λ+λ− = 1`.

## Tests, exact sympy (numbers via mpmath at the CODATA-2022 muon pin, 30 digits)

- G1: `|λ±| = 1` for real `q > 0` wherever the pair is non-real, i.e. `λ± = e^{±iθ}`. Record the
  range of `q > 0` where `|c₁| < 2` (elliptic) vs `|c₁| > 2` (loxodromic, real pair).
- G2: closed forms: `cos θ = −c₁/2`, `|μ| = 2 sin(θ/2)`, `arg μ = (π + θ)/2`, and
  `sin²(θ/2)` as an exact rational function; check whether it factors through `h = q − q⁻¹` and
  `[3]_q = q² + 1 + q⁻²`.
- G3: complex length `ℓ = log λ+`; record whether it is purely imaginary (pure rotation, no
  hyperbolic translation) at the pin.
- G4: leading behaviour of `θ` as `q → 1`.

No comparison with hyperbolic volume, Chern–Simons, or any measured number is made here: those
would be searches for a match. The 12 is not tested, since `|μ| ≤ 2` on the elliptic range makes a
complex `μ` of size 12 impossible there (recorded, not assumed: G1 decides it).
