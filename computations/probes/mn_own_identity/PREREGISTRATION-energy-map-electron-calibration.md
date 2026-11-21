# Pre-registration: energy scale for the 𝒟² trace, fixed by CAL-1 on the electron (before computing)

Date 2026-11-21. Written and committed before `mn_energy_map_electron_probe.py` is run.

**What the corpus has (searched first).**
- E₀ = m_e/(q(q − 1)) is a *definition* (`CategoricalLagrangianTwoTermBridge.hadronicScale`; the
  neutron–proton splitting proof block says "(H_α) is an assumption; no derivation on record").
- `docs/audits/2026-11-21-qbeta-np-error-budget.md` §12–§14 exclude every monotone map of the
  Markov trace ε for the one-sided Q_β reading. That is about ε, not about tr(𝒟²).
- No block converts tr(𝒟²) to MeV.

**Assumption (stated, not derived).** The energy is linear in the 𝒟² trace: E(X) = λ·T(𝒟_X²),
with one λ for every state.

**What is then derivable.** λ, *including its sign*, is fixed by the one state whose energy is a
ruled calibration: the electron (CAL-1, E = m_e > 0). The electron is σ₀σ₁σ₀ (owner ruling). Then
λ = m_e / T(𝒟_e²), and E(n) − E(p) = m_e · [T(𝒟_n²) − T(𝒟_p²)] / T(𝒟_e²). No other constant enters.

**Connection, extended by the mass-identity reading (§27).** The mass identity's all-zero state
is ∏c(ℓ_j)·1 = q^{writhe}·1. So the Temperley–Lieb part of hol is hol − q^{wr}·1. For V³
(writhe 0) this is hol − 1. For the electron σ₀σ₁σ₀ (writhe 3) it is X_e − q³·1. This is used
for the electron, and it is the same rule as for the nucleons, not a new choice.
𝒟_X = q⁻¹∇_X + (1 − q⁻¹)T³ on (ℂ²)^⊗3, Ř as in §21.

**Two trace arms, both reported, neither selected.**
- **P (plain):** nucleons, the plain trace on W_p, W_n (as in §25). Electron: the plain trace
  on the whole 8-dimensional space.
- **K (ruled quantum trace, owner 2026-11-20):** T(M) = Tr(K^{⊗3}·M)/[2]_q³ on the whole space.
  Nucleons are restricted to W_p and W_n with the same weighting (K = q on W_p, q⁻¹ on W_n),
  and the electron uses the whole space.

**Report.** For each arm: the symbolic T(𝒟_e²), λ's sign, the symbolic E(n) − E(p) in units of
m_e, and its value at the proton pin q₀. A CODATA comparison is printed only afterwards. If
T(𝒟_e²) ≤ 0 or is 0, report that the calibration fails or flips the sign; do not repair it.
Linearity is the stated assumption, and a miss is a scope-(a) negative for linear maps under
this calibration.

Exact sympy; the pin evaluation uses mpmath at 60 dps. No float64.
