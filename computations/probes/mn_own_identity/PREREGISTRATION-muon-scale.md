# Pre-registration: n − p on the muon scale, and the degree-0 term as a potential (2026-11-22)

Owner (thread, 2026-11-22): *"Try preregister muin scale. Degree 0 if negative is considered as a
potential energy."* Written before any number in this test is computed. It reuses only exact
forms already on record (§28 Δ_D, §31 Δ_S) and the proton identity's own normalisation.

## Definitions (fixed before computing)

- 𝒟, ∇ = hol − q^{writhe}·1, hol = V³, the weight blocks W_p and W_n, and the static term
  S = QPair·hol are all exactly as in §28 and §31. The quark charges are the adopted (+⅔, −⅓),
  so every S arm is conditional on the owner's 2026-11-22 ruling that qᵢ must be derived.
- **Potential reading (owner ruling 2026-11-22, agent's reading).** ℒ = T − V. The degree-0 part
  of ℒ′ = 𝒟² + S is −V, so it enters the energy as −S. The energy functional is
  𝓔(X) = 𝒟_X² − S_X.
- **Muon-scale map (mirror of the proton identity).** The identity is m_p = 2 m_μ F_Bor − 12 m_e,
  with F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ and tr_M the convention-D trace. By `wholeTrace_eq_trM`,
  the proton sector's share of tr_M(X) is q·tr_{W_p}(X)/[2]³, and the neutron's is
  q⁻¹·tr_{W_n}(X)/[2]³. So the map is
  E_N(X) = 2 m_μ · ([3]_q!/q³) · τ_N(X), with τ_p = q·tr_{W_p}/[2]³ and τ_n = q⁻¹·tr_{W_n}/[2]³.
  m_μ = m_e·Vol(4₁)/ℏ_q² (the CAL-2 relation), so the ℏ_q⁻² pole is part of the map.
  This is one map and no alternative is tried. It reuses the identity's normalisation for an
  operator (𝒟², S) that is not β_Bor; that reuse is an assumption.
- q₀ is the proton pin, and m_e, Vol(4₁) = 2·Cl₂(π/3) come from `qou_substrate.constants`.
  Exact sympy throughout, mpmath at 60 dps. No float64.

## Arms

- **M1:** 𝒟² only, E_n − E_p = 2 m_μ([3]!/q³)(τ_n − τ_p)(𝒟²).
- **M2:** the potential reading, 𝓔 = 𝒟² − S, on the same map.
- **E-pot:** §31's electron-calibrated linear map, re-run with −S instead of +S (both trace
  arms, the electron's S is 0 as before).

## Predictions (before computing)

1. M1: positive (neutron heavier), about +0.17 MeV, i.e. about 13 % of CODATA. It vanishes at
   q = 1 (the n − p is O(h³), and the pole is O(h⁻²), so the result is O(h)).
2. M2: positive, about +105 MeV, i.e. about 80 times CODATA. It does not vanish at q = 1, because
   S has no 𝒟 factor.
3. E-pot: positive, about +54.4 keV (plain) and +49.1 keV (K), i.e. §31 with its sign flipped.
4. Scope: if these hold, each arm is a scope (a) result for its own map. M2's failure would
   come from S, whose charges are not derived.

The CODATA m_n − m_p = 1.29333 MeV is printed after the numbers, for comparison only.
