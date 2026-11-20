# Pre-registration: Q_β as an energy from U_q(gl₂) structure outside H_n

Bean `qou-99qc`. Owner (Carl, 2026-11-20 ~20:15): derive Q_β as an energy, consistent with the
q-dependent rate, nothing chosen. Written before the probe was run.

**Disclosure.** While designing this I estimated two numbers by hand: 2·ln q₀·E₀ ≈ 0.88 MeV and
the lepton-strand split h·E₀/[2] ≈ 0.44 MeV. So those two cells are not blind. No other value
below was computed before this file was committed. CODATA Q_β = 0.78233341 MeV is read only in
the last block of the probe.

## Setting (all from the corpus)

- Convention-D Markov trace = U_q(sl₂) quantum trace Tr(K^{⊗n}·)/[2]ⁿ, K = diag(q, q⁻¹)
  (bean `qou-99qc` 2026-11-19; #8586).
- Proton = T³ = +½ weight space, neutron = T³ = −½; K^{⊗3} = q on W_p, q⁻¹ on W_n.
- Amplitude: n⊗ν → e⁻⊗p block = (q²−1)·Δ²(E) (#8638); T⁺ = Δ²(E).
- Every H₃ operator has the same spectrum on n and T⁺n (#8639 `hecke_energy_transport`).
- E₀ = m_e/(q(q−1)) (order zero) or /(1−ℏ²) (tower, canonical); posited (`qou-mkm8`).

## Candidates and what each would need to give a derived Q_β

**(a) Cartan / Bohr.** Claim to test: (q²−1)·T⁺ = Ad_K(T⁺) − T⁺ with K = Δ²(K) (exact).
So the amplitude's q-dependence is e^{λ·ΔH} − 1 with ΔH = 2, λ = ln q: the transition carries
Cartan charge 2. Energies then follow only after a scale S is fixed:
 a1 linear-K gap h = q − q⁻¹ (the #8586 factor without tr_W/[2]³),
 a2 log-K gap 2λ,
 each × S ∈ {m_e, E₀⁰, E₀^tower}. **Prior:** none of these is forced. The charge 2 is derived;
the scale and the choice log vs linear are not. Reported as a table, none selected.

**(b) Twist / Casimir.** θ and every central element of U_q(gl₂) commute with T⁺, so by the
eigenvalue-transport lemma they take the same value on n and p, and on e⁻ and ν. **Prior:**
Q_β-contribution = 0 from n→p, and no twist energy can separate m_e from m_ν. Scope (b),
invariant: centrality + T⁺n ≠ 0.

**(c) Four strands.** n⊗ν and p⊗e⁻ lie in the same weight space (2,2) of V^{⊗4}, and E⊗F commutes
with K⊗K (Δ(K) = K⊗K grouplike). **Prior:** every K-weighted 4-strand split is 0 → Q_β = 0
for the whole process; any energy additive and linear in the Cartan weight is conserved, so
Q_β = 0. A non-zero Q_β needs different coefficients on quark and lepton strands, which is one
free number. Also computed: the lepton strand alone under the #8586 functional,
ε_ℓ = (q⁻¹ − q)/[2], and whether (3-strand split) − (lepton split) reproduces the kinematic
identity Q_β = (m_n − m_p) − m_e. Prior: it does not follow from the 4-strand trace (K weights
multiply, they do not add).

**(d) E₀ as the K-grading unit.** Test whether E₀·g(q) = m_e for g any K-eigenvalue gap of the
lepton doublet (h, 2λ, q−1, q²−1). Prior: E₀ q(q−1) = m_e is a definition, and q(q−1) is the
gap between the K-eigenvalues q² and q, which no doublet carries. Negative expected.

## Checks the probe must pass
C1 Ad_K identity on the 8-dim three-strand module, exact. C2 E⊗F commutes with K⊗K on 4
strands, exact. C3 weight of n⊗ν equals weight of p⊗e⁻. C4 twist/Casimir equal on n and p
(numerical spectrum of Casimir on V^{⊗3}, exact). C5 lepton-split closed form. C6 table at 70
dps, proton q₀. C7 CODATA comparison last.
