# β⁻ decay with the e⁻ν̄ pair as ONE non-factorising word (P2)

Bean `qou-99qc` (Q_β functional). Owner, 2026-11-20 20:52: β-decay is an interaction, possibly
with an entangled particle, ultimately a Gröbner–Shirshov calculation. Every no-go of the day
(#8616, #8639, #8661, #8623; hypercharge #8676) assumes nucleon ⊗ leptons **factorise**. This
note tests the opposite premise (P2, owner-selected): the lepton pair is created as one
non-factorising braid word, entangled with the proton.

Leptons are taken from the corpus's own **knot** definitions, not from strand colours (this
sidesteps premise L of #8673):

| object | corpus block | knot | braid word used here |
|---|---|---|---|
| e⁻ | `def:electron-knot` | trefoil T(2,3) | σ³ on 2 strands |
| ν̄ | `def:antineutrino-knot` | mirror unknot T(1,0)^σ | identity on 1 strand |
| ν | `def:neutrino-knot` | unknot | identity on 1 strand |

## 0. PRE-REGISTRATION (written and committed before any number was computed)

### 0.1 What the corpus says about how a lepton pair is made

- `beta-decay-skein` / `antineutrino-knot`: the L₀⁻ smoothing yields `T(2,3) ⊔ T(1,0)^σ` —
  a **disjoint union** (⊔). The corpus never links the pair.
- `two-photon-pair-production`: `γγ → e⁻ ⊔ e⁺`, again ⊔.
- `breit-wheeler-pair-creation-intro`: "fuse into a conjugate electron–positron trefoil pair";
  no linking word given.
- NF(γγ) in H₃ (`docs/audits/2026-11-15-quark-state-gamma-gamma-nf-test.md` §2): the
  coordinate *named* e⁻ is σ₀σ₁σ₀ (the half twist Δ₃).

So **the linking is not a corpus statement**. Any entangling letter is a choice, and this probe
therefore ENUMERATES the minimal family instead of picking one.

### 0.2 Words (all in the Iwahori–Hecke algebra, σᵢ² = hσᵢ + 1, h = q − q⁻¹, exact over ℚ(q))

- Nucleons: `nuc11_interleaved` (`pyhecke.atom.build_atom_nf_exact`, as transcribed in
  `computations/qbeta/qbeta_delta_candidate_census_probe.py`) on 3 strands, for both p and n.
  Caveat carried, not hidden: that element FAILS the confinement SDP under reading 3 (AGENTS.md,
  `qou-99qc`). Secondary: the bare Borromean core β_Bor = (σ₁σ₂⁻¹)³ (the word inside F_Bor),
  which has no neutron partner, so it gives X but not Q.
- Lepton pair on 3 strands: `P_k = σ₁³ · σ₂^{2k}`, k ∈ {−1, 0, +1}. k = 0 is the factorised
  `e⁻ ⊔ ν̄`; k = ±1 links ν̄ once through the trefoil (linking number ±1). The ν̄ orientation
  cannot be reversed inside a braid closure, so it enters only through the sign of k — both signs
  reported.
- Final state on 6 strands: `W_{j,k} = p(σ₁,σ₂) · σ₃^{2j} · σ₄³ · σ₅^{2k}`, j, k ∈ {−1,0,+1}.
  j = 0: pair not linked to the proton. (j, k) = (0, 0): the fully factorised state.
  Placement (proton 1–3, e⁻ 4–5, ν̄ 6, adjacent interfaces) is a choice, stated.

### 0.3 Energy functionals — the SAME one on every object, two channels reported, none chosen

- **(T) trace channel** (the form inside the canonical m_p identity, `canonical_mass.py`):
  `F(β) = |tr_M^D(β)| · [N]_q! / q^N` on N strands, `z_D = q³/(q²+1)`, `tr(1) = 1`;
  `E_T(β) = m_μ · F(β)`, `m_μ = m_e · Vol(4₁)/ℏ_q²`. The corpus defines F only at N = 3 (for
  β_Bor); extending `[N]_q!/q^N` to N = 1, 2, 6 is **my extension, stated as such**. The −12 m_e
  offset of the m_p identity is excluded: it is a recorded FIT (owner 2026-11-18) specific to the
  proton, and applying it uniformly would itself be a choice.
- **(V) volume channel**: `m(K) = m_e · Vol(K) · ρ(K)/ℏ_q²`. Trefoil and unknot are
  non-hyperbolic, Vol = 0 (#8659). Entangled closures: volume NOT computed here (no SnapPy in the
  container) — reported as unevaluated, never as 0.

### 0.4 Pre-registered outputs and decision rules

1. Exact traces in ℚ(q) of every word; cross-check tr(β_Bor) against the Lean closed form
   `(4 + h² − 3h⁴ − h⁶)/(h² + 4)` (`BorromeanMarkovTrace.lean`).
2. `X(j,k) = E(W_{j,k}) − E(p) − E(e⁻) − E(ν̄)`; `ΔX(j,k) = X(j,k) − X(0,0)`.
   "X forced non-zero" = the exact rational function is not identically 0.
   "Entanglement visible" = ΔX not identically 0.
3. `Q(j,k) = E(n) − E(W_{j,k})` — the definition the owner gave.
4. q → 1 limits, and values at the proton pin q₀ (70 dps).
5. CODATA Q_β is a COMPARISON row only. No (j,k), sign or channel is selected by it.
