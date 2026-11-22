# gg_decay — pre-registration (bean qou-a1hh; hypothesis only; nothing wired)

Owner rulings 2026-11-15: "Test neutron decay"; "Try both assignments";
"Allow both [photon-pair orientations], as a hypothesis" (probe-only).

## Objects
- V = σ₀σ₁⁻¹, B = V̄ = σ₀⁻¹σ₁ on 3 strands (gg_two_orientations).
- Nucleon candidates N: the 8 three-vertex words in {V,B}³ (all pass reading 3
  alone), plus V⁶ and B⁶ (for the owner's assignments p=V³/n=V⁶ and reverse).
- Weak vertex (from the weak-vertex thread): W_g = q⁻¹(2σ_g − h)/[2]_q,
  h = q − q⁻¹, g ∈ {0, 1}. Token form (c, d, g) = cσ_g + d.
- τ = convention-D Markov trace on H₃(q): τ(x) = Σ_{μ⊢3 two-row} y_μ χ_μ(x),
  proton q₀, mpmath 70 dps.

## Measurement (no selection)
For every ordered pair (n, p) in N×N and g ∈ {0,1}:
  A(n→p; g) = τ(p⁻¹ · W_g · n).
Reported, not used to choose anything:
1. the matrix A;
2. the direction asymmetry |A(n→p)| − |A(p→n)| for each unordered pair;
3. the owner's two assignments: A(V⁶→V³) vs A(V³→V⁶), both g.

## Checks (must pass, or the run is void)
- D0: W_g² = q⁻² and W_g − σ_g = −h·P_L hold as matrices in both two-row irreps.
- D1: τ(1) = 1.
- D2: ι(W) = −W (algebraic, from ι(σ) = −σ⁻¹); recorded as an identity check
  on matrices: W_g computed from −σ_g⁻¹ equals −W_g.

## Pre-registered expectation (may fail; reported either way)
E1: The set N carries no flavour label by construction, so I expect no pair to be
singled out by A alone; any asymmetry is reported as a measurement, scope (a).
Reading A as a decay rate, or any word as "the neutron", is an interpretation.
