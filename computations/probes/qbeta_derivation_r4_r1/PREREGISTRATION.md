# Pre-registration: Q_β by energy conservation (R4) and as a four-strand γγ process (R1)

Bean `qou-99qc`. Owner (Carl), 2026-11-20 18:30: *"Q_β must be DERIVED, not chosen"*; 18:27: *"We should be able
to algebraically derive the formula for Q_β from the γγ production."* Written **before** any computation below
was run. Photon throughout: **γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹** (ruled; `QOU/Photon.lean`).
Baseline the owner adopted (#8586, D1 = A): the T³ weight split of the z_D trace on V³, Q_β = 0.3254 MeV
(−58.4 %). It is a baseline to explain, not a target.

Nothing here is wired to a scorecard. CODATA appears only in a final comparison column. A miss is a result.

## Fixed inputs (corpus, not chosen here)

* q₀: proton pin (`q_parameter.Q_50_DIGIT_STR`), 70 dps.
* Mass channel: m_N = 2(m_μ·F − 6 m_e), F = |τ(β)|·[3]_q!/q³, m_μ = m_e·Vol(4₁)/ℏ_q² — the identity that pins q₀.
  So the scale per unit trace is S = 2 m_μ [3]_q!/q³ (≈ 945.76 MeV per the 2026-11-20 audit).
* τ = convention-D Markov trace = Tr(K^{⊗3}·)/[2]³ on (C²)^{⊗3} (Jimbo Ř, K = diag(q, q⁻¹), u = e₁).
* β = V³ = (σ₀σ₁⁻¹)³ for both nucleons (γγ + SDP selection, #8564), = γ(0,0,qh)·γ(0,0,−q⁻¹h).
* The (3,1) representation of H₄(q) and its labels A (σ₃ lines Lu, Ld) and B (J₄ lines Ja, Jb)
  from `FlavourDoubletFourStrands.lean`.
* Weak vertex: weakVertex(σ) − σ = −h·P_L(σ) (`WeakVertexLeftProjector.lean`).

## R4 — energy conservation in the mass channel

Q_β := m_n − m_p − m_e, each nucleon mass from the mass channel with a flavour-resolved trace.
Computations, all exact in ℚ(q) and then at q₀:

* R4.1 T³ sectors, normalised like the full trace (by [2]³): τ_p = sector(+½), τ_n = sector(−½).
* R4.2 T³ sectors, each normalised by its own quantum dimension.
* R4.3 Proton = full trace (the pinned object); neutron = its image under u ↔ d.
* R4.4 Label A: partial characters tr(Lu·ρ(V³)) vs tr(Ld·ρ(V³)) in the (3,1) of H₄.
* R4.5 Label B: tr(Ja·ρ(V³)) vs tr(Jb·ρ(V³)).

For each: the relative difference (τ_n − τ_p)/τ_p, and Q_β = S·(|τ_n| − |τ_p|) − m_e where that is defined.
The diagnostic size, (m_n − m_p)/m_p ≈ 1.378e-3, is quoted, never tuned to.
**Expected before running (my prior, recorded so it can be wrong):** R4.1 gives a ratio independent of the
element (a power of q), with the neutron lighter, so Q_β < 0; R4.2 and R4.3 give m_n = m_p, so Q_β = −m_e.

## R1 — the decay as one four-strand object

Γ(φ, ψ) = ρ(γ(φ)·γ(ψ)) in the (3,1) of H₄ (H₃ letters σ₀, σ₁ ↦ H₄ letters σ₁, σ₂).
The d → u transition amplitude is the rank-one sandwich P_u · X · P_d.

* R1.1 Label A: the flip functional λ_A(w) := (Lu·ρ(w)·Ld)/eS on the six normal-form words
  1, σ₀, σ₁, L₋ = σ₁σ₀, L₊ = σ₀σ₁, e⁻ = σ₀σ₁σ₀. Then the γγ amplitude as an explicit polynomial in (φ, ψ, q).
* R1.2 Label B: the H₃ pair alone cannot flip (Ja·Γ·Jb = 0, from `J4_no_mix`); with the strand-4 γγ vertex
  V₄ = σ₂σ₃⁻¹: Ja·Γ·V₄·Jb as a multiple of eJ.
* R1.3 Weak vertex on the left line: P_u · (weakVertex − σ) for the letter whose left line carries P_u.
* R1.4 Specialise to the only derived colour weights, φ = (0, 0, qh), ψ = (0, 0, −q⁻¹h): the e⁻ coefficient,
  λ_A(V³), and the label-B factor.
* R1.5 The round trip tr(P_u·X·P_d·X̄) as the energy object y₃, then Q_β = (h[2]/2)·y₃·E for E ∈ {E₀ (posited),
  S (mass channel)}. Every remaining choice is listed; none is picked by residual.
* Label C (T³): no Hecke element changes T³ (Schur–Weyl; bean `qou-0whz` C2), so the R1 amplitude between
  T³ = −½ and +½ is identically 0. Recorded, not re-proved.

φ₀, φ₁ stay symbolic unless the sibling branch `claude/photon-chiral-weights-derivation-2026-11-20` has landed a
derivation by the time the probe runs (checked 2026-11-20 ~19:00: branch does not exist).

## Formalize-first

Lean file `QOU/QuarkState/DecayGammaGammaFourStrand.lean`, generic `[Field K]`, sorry-free, carrying R1.1–R1.4
and the R4 algebra (sector ratio, equal-dimension normalisation), before the probe is committed.
