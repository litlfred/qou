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

### 0.5 Amendment (written AFTER family A was computed — flagged as post-hoc)

Family A (the clasps σ₂^{2j}, σ₄^{2k} of §0.2) turned out to factorise exactly at the trace
level (§1.2). Three further families were therefore added. They were chosen for a
**structural** reason (to find out which words the trace can see at all), before any of their
numbers existed, and none was selected by a value:

- **B** (729 words): the trefoil σ₃³ with proton clasps σ₂^{2a} and ν̄ clasps σ₄^{2d} inserted
  *between* its three crossings, a, d ∈ {−1,0,1}³.
- **C** (27 words): the clasp replaced by the pure braid `A = σ₂σ₁²σ₂⁻¹` (the e⁻ strand loops
  proton strand 2, passing strand 3), interleaved the same way.
- **D** (12 words): the full twist Δ^{2t}, t = ±1, on {proton strands 2–3, e⁻ strand} or on
  {all three proton strands, e⁻ strand}, then σ₃³ and σ₄^{2k}. Δ² is central in its braid
  group, so it prefers no strand order.

## 1. Results

Producer: `computations/qbeta/qbeta_entangled_lepton_pair_probe.py`; witness
`computations/qbeta/qbeta-entangled-lepton-pair.witness.json` (19 assertions, all pass;
proton pin, 70 dps). Lean: `QOU/QBeta/EntangledLeptonPairTrace.lean` (sorry-free).

### 1.1 Exact traces (convention D, ℚ(q))

| word | tr_D | q → 1 | q₀ |
|---|---|---|---|
| e⁻ = σ₀³ | (q⁶+q²−1)/(q(q²+1)) = (h²+1)z + h | 1/2 | 0.848527 |
| ν̄ (1 strand) | 1 | 1 | 1 |
| β_Bor | Lean closed form, checked | 1 | 0.998562 |
| p = nuc11(p) | (q⁴+1)(q¹⁸−3q¹⁶+…−1)/(4q⁹(q²+1)²) | 1/2 | 0.629328 |
| n = nuc11(n) | (q⁴+1)(q¹⁴−3q¹²+…−1)/(4q⁹) | 1/2 | 0.475134 |

### 1.2 What the trace can see (the main finding)

1. **Clasp factor (Lean, sorry-free).** For any 2-strand element x, tr(x·σ₁^{±2}) = λ± tr(x)
   with λ₊ = 1 + hz = (q⁴+1)/(q²+1), λ₋ = 1 + h² − hz = (q⁴+1)/(q²(q²+1)). The minimal linked
   pair σ₀³σ₁^{±2} is a non-factorising **word** whose trace is λ± · tr(e⁻): the trace does not
   know which particle the ν̄ is linked to.
2. **One-strand attachment is nucleon-blind (exact, 9 + 729 + 27 words).** In families A, B and
   C, tr(W)/tr(nucleon) is the same rational function for p, n and β_Bor in every word. For A and
   B this is the multiplicativity of the Markov trace under connected sum (the lepton word meets
   the nucleon braid on a single strand; Jones 1987, `jones1987`). For C the blindness is
   **measured**, not proved; I did not identify the mechanism.
3. **Interleaving makes the pair itself non-factorising.** Of the 27 family-B words with no proton
   clasp, 20 have tr ≠ tr(e⁻)·∏λ — the ν̄ is genuinely entangled with the e⁻ — but the
   proton still factors out.
4. **Only a braid on ≥ 2 nucleon strands is nucleon-sensitive.** All 12 family-D words are
   nucleon-sensitive. With ν̄ unlinked (k = 0) the trace cross term
   C = tr(W) − tr(p)tr(e⁻)tr(ν̄) carries the exact factor **q⁶ − 1 = q³·h·[3]_q**, so it vanishes at
   q → 1 and is order h; with k = ±1 that factor is absent. Values at q₀: C ∈ [−0.344, +1.225].

So, **is the cross term forced non-zero?** At the trace level: forced **zero** for every word
attaching the leptons through one nucleon strand (scope (b), invariant: Markov-trace
multiplicativity on connected sums, A and B); non-zero but O(h) for the full-twist words.

### 1.3 Energies — the two channels

**(T) trace channel**, `E = m_μ |tr| [N]_q!/q^N`, used uniformly (m_μ(q₀) = 105.6584 MeV):

| object | E_T at q₀ (MeV) |
|---|---|
| p (nuc11) | 297.598 |
| n (nuc11) | 224.682 |
| e⁻ | 146.329 |
| ν̄ | **95.190** (= m_μ/q₀) |

- The strand factor gives one bare strand m_μ/q₀ = 95 MeV, against `def:neutrino-knot`
  ("carries no topological mass").
- E_T(n) − E_T(p) = **−72.92 MeV**: in this channel the neutron is lighter than the proton
  before any lepton is added.
- Strand factors at q₀: [1]!/q = 0.901, [2]!/q² = 1.632, [3]!/q³ = 4.476, [6]!/q⁶ = **448.53**.
  So X(0,0) = m_μ(c₆ t_p t_e − c₃ t_p − c₂ t_e − c₁) is non-zero for the **factorised** state;
  at q → 1, X(0,0)/m_μ → 720/4 − 3 − 1 − 1 = 175, and m_μ itself diverges like 1/ℏ_q².
- Over all 777 six-strand words, X ∈ [8.45·10³, 8.28·10⁴] MeV and Q = E(n) − E(W) ∈
  [−8.3·10⁴, −8.8·10³] MeV. CODATA Q_β = 0.782333 MeV (comparison only).

Scope (a): this channel, **extended uniformly by me** to N = 1, 2, 6, does not produce Q_β in any
of the 777 words; the miss is four to five orders of magnitude and its sign is wrong. The defect
is the strand factor, which makes E non-additive on disjoint unions; that factor is defined by the
corpus only at N = 3.

**(V) volume channel**, `m = m_e Vol ρ/ℏ_q²`: e⁻ and ν̄ get 0 (non-hyperbolic), so the channel
assigns the electron no mass, while `def:electron-knot` makes m_e the CAL-1 input. The proton in
this channel is the deprecated form (966 or 406 MeV, `canonical_mass.py`). Volumes of the entangled
closures were **not computed** (no SnapPy in the container) and are unevaluated, not zero. With
two of the four objects at 0 and the nucleon form deprecated, this channel cannot define Q here.

### 1.4 Derived vs chosen

| item | status |
|---|---|
| e⁻, ν̄ knots; Markov trace convention D; λ± ; trace blindness for A, B | derived (corpus + Lean / exact) |
| nucleon words nuc11 (fail confinement SDP reading 3, `qou-99qc`) | corpus word, not ruled in |
| every linking letter (families A–D) | **chosen** — the corpus writes the pair only as ⊔ |
| strand factor [N]!/q^N at N ≠ 3; omission of the −12 m_e fit | **chosen** (my extension) |
| families B–D | added after A was computed (§0.5), for structure, not for value |

### 1.5 Side observation

The NF(γγ) coordinate labelled e⁻ (σ₀σ₁σ₀, the half twist Δ₃) closes to the **Hopf link**
(σ₁σ₂σ₁ ~ σ₂σ₁², Markov-destabilise to σ₁²), not the trefoil of `def:electron-knot`. The label
is a coordinate name, not a knot identification.
