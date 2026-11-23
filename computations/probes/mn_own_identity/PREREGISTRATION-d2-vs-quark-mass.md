# Pre-registration: the 𝒟² muon-scale arm against the quark-mass part of n − p (2026-11-22)

Owner, 2026-11-22: *"Do all"* (option 1 of the §39 reply). Written before computing.

The arm is §35 M1, E_n − E_p = 2 m_μ([3]_q!/q³)(τ_n − τ_p)(𝒟²), m_μ = m_e·Vol(4₁)/ℏ_q², a rational
function of q times m_e·Vol(4₁), exactly as in `mn_muon_scale_probe.out.json`. Nothing new is defined.

Tests (exact sympy, then mpmath 60 dps at q₀):
- D1. Its series in ε = q − 1: leading order and exact leading coefficient as a rational multiple of
  m_e·Vol(4₁). Already visible in the §39 numbers (not a prediction made blind): the value is about
  −2.334 MeV·ε near q = 1, i.e. **negative** at leading order, while it is +0.171 MeV at q₀.
  Prediction: leading order ε¹, coefficient negative, equal to −(rational)·m_e·Vol(4₁) with
  rational ≈ 2.25.
- D2. The real zero q* of the arm in (1, q₀): predicted to exist, between 1.01 and q₀.
- D3. Comparison, printed last and not used for anything: the arm at q₀ against the lattice
  quark-mass part +2.52 MeV (Borsanyi et al. 2015) and against CODATA 1.29333 MeV.

Scope: the arm uses the reuse of the proton identity's normalisation (§35 assumption). No fitting:
no factor is introduced to bring the arm to 2.52.
