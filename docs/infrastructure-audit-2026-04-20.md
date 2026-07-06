# Infrastructure Audit — Code vs Paper

*Compiled 2026-04-20 against `docs/derivation-audit-2026-04-20.md`.*

## Scope

Compare what the paper content blocks prescribe vs what the computational modules (`computations/*.py`) actually compute. Flag inconsistencies.

## Summary table

| Paper prescription | Code location | Code behaviour | Status |
|--------------------|---------------|----------------|:------:|
| `prop:categorical-mass-markov`: single-level 𝔪\|_single = \|tr_M(ρ(β))\| | `markov_trace_canonical.py::tr_M_element`, `binding_canonical.binding_canonical` | Computes Markov trace via Hecke reduction + Ocneanu ω. | ✓ |
| `thm:jones-markov-trace`: Markov parameter z = 1/(q^{1/2}+q^{-1/2}) | `mass_endomorphism.py:35` `z_mark = 1.0 / (q0**0.5 + qi0**0.5)` | Matches. | ✓ |
| `prop:mass-endomorphism-tower` single-level: desc + Σ Φ_q + z² Σ Φ_q pair | `canonical_plus_multibrane.py::tower_mass_level` | Matches the equation verbatim (one global Φ_q on aggregated V̂). | ✓ |
| `rem:mass-endomorphism-jet-tower` (updated): **descended at level 0 ONLY**, singletons + pairs **per level** | `canonical_plus_multibrane.py::binding_canonical_plus_multibrane` | **INCLUDES desc term at every jet level** via `tower_mass_level`. Double-counts level-0 holonomy across iterations. | ❌ |
| Updated `𝒫_n = all pairs (i < j)` at every level (justified by `thm:markov-trace-factorization`) | `canonical_plus_multibrane.py::tower_mass_level` with `pair_mode="full"` | **Fixed 2026-04-20 (commit 7a699da)**: `tower_mass_level` and `binding_canonical_plus_multibrane` default both flipped from `"adjacent"` to `"full"`.  `binding_full_pipeline.binding_full` and `unified_lift.binding_unified` were already `"full"`.  All four entry points now consistent. | ✓ |
| Pentagon ascension: no explicit triples | `canonical_plus_multibrane.py` | No triple terms. Matches. | ✓ |
| `prop:tower-binding-energy`: $B = \sum_\lambda w_\lambda \cdot m_e \cdot \sum_i \ln\lvert\Phi_q(\hat{V}_i^\lambda)\rvert$ (three-channel, log form, per-block) | `mass_endomorphism.py::mass_from_tower` | Uses single global Φ_q on aggregated V̂ (NOT per-block, NOT log form). | ❌ |
| `prop:binding-scale-catalan`: α = m_e · 8G ≈ 3.7445 MeV | `canonical_plus_multibrane.py::E_0_BETA_DECAY_MEV = 0.782` | Uses Q_β = 0.782, not Catalan α. Different scale. | ❌ |
| `prop:deuterium-derived-binding`: QED correction (1 − α_EM/2) | `canonical_plus_multibrane.py`, `binding_full_pipeline.py` | Not applied. | ❌ |
| Atom mass: $M(Z,N) = Z m_p + N m_n + Z m_e - B(Z,N)$ | Various probes use different conventions (`universal_three_calibration.py` switched between Σ m_nucleon and framework-consistent free baseline mid-session) | Framework has NO single canonical baseline across modules. | ❌ |

## Inconsistencies — ranked by impact

### 1. Descended term level-counting — HIGH

**Paper** (`rem:mass-endomorphism-jet-tower`, recently revised):
> The **descended** contribution is **not** summed over jet levels. Including a separate descended product at every jet level would double-count the level-0 holonomy.

**Code** (`canonical_plus_multibrane.py:binding_canonical_plus_multibrane`):
```python
for n in range(1, n_brane_levels + 1):
    V_a = lift_V_markov(V_atom_0, n)
    V_f = lift_V_markov(V_free_0, n)
    m_a = tower_mass_level(V_a, pair_mode=pair_mode, ...)
    m_f = tower_mass_level(V_f, pair_mode=pair_mode, ...)
    delta = m_f - m_a
    tower_term += delta
```

`tower_mass_level` returns `desc + single + cross`, so the descended term **is** re-added at every level. This double-counts the level-0 holonomy at levels 1+ with ℏ_q² damping, masking but not eliminating the overcount.

**Fix**: strip the desc term from `tower_mass_level` calls inside the level loop; compute desc once at level 0 and treat levels 1+ as singleton+pair only.

### 2. Three-Wedderburn-channel binding — HIGH

**Paper** (`prop:tower-binding-energy`):
$$B(Z,N) = \sum_{\lambda \in \{\text{sym,std,alt}\}} w_\lambda \cdot m_e \cdot \sum_{i=0}^{A-2} \ln|\Phi_q(\hat{V}_i^\lambda)|$$

**Code** (`mass_endomorphism.py::mass_from_tower`):
```python
Vf = w_sym * sp + w_std * Vs + w_alt * ap   # aggregate first
single = sum(Phi_q(abs(v["full"])) for v in vols)  # Φ_q on aggregate
```

The code does **aggregate-then-Φ_q** (single global Φ_q), whereas the paper prescribes **per-block Φ_q then weighted sum with log**.

**Impact evidence**: this branch's `per_block_phi_q.py` attempted the paper-correct form and found the sym block saturates the Φ_q pole — so the paper's formula as written is **not computable** at q₀ with the current Hecke conventions.

**Resolution required**: either:
  (a) Paper is wrong — the per-block formula diverges; the algebraically correct computation is the aggregate form already in the code.
  (b) Code is wrong — needs different normalisation of per-block V̂ to stay in Φ_q's domain.
  (c) Both are right at different scales — paper formula applies to atomic binding at the log scale, code's formula applies to particle masses. They should coexist.

### 3. E_0 calibration conflict — HIGH

**Paper lists multiple scales**:
- `prop:binding-scale-catalan`: α = m_e · 8G ≈ **3.7445 MeV** for binding
- Derivation doc implicitly uses E_0 = Q_β = **0.782 MeV** for nuclear transitions
- `pair-production-nf.witness.json` implies a third scale ~**4.15 MeV** for pair thresholds

**Code uses at least four separate E_0**:
- `canonical_plus_multibrane.py:E_0_BETA_DECAY_MEV = 0.782`
- `multi_level_jet_sum.py:E_0_PROTON_TOWER_MEV = 7.96e-4` (m_p / cat mass)
- `pair-production-nf.py:E0 = 4.15`
- Various `alpha_em` and `alpha` constants scattered

**No file uses α = m_e · 8G directly**. The Catalan prescription from `prop:binding-scale-catalan` is not implemented.

**Fix**: introduce `q_parameter.py::ALPHA_BINDING = M_E_MEV * 8 * CATALAN_G` as the canonical binding scale, audit all E_0 uses, align with paper.

### 4. QED correction not applied — MEDIUM

**Paper** (`prop:deuterium-derived-binding`):
> $B_\text{phys} = B_\text{strong} \cdot (1 - \alpha_\text{EM}/2)$
> Deuterium: 2.2248 MeV vs AME 2.2246 MeV (0.008%)

**Code**: no `canonical_plus_multibrane` / `binding_full_pipeline` call applies the `(1 - α_EM/2)` factor. The D results we quote (0.018%, 22 keV) would tighten to the 0.008% claimed in the paper if the QED factor were added.

**Fix**: wire `alpha_em` from `hecke_core.py` into the binding calibration step.

### 5. Baseline convention inconsistency across probes — LOW-MEDIUM

Between session modules:
- `universal_three_calibration.py` started with `B = Σ m_nucleon − m_atom`, updated mid-session to `B = m_free_atom_braid − m_atom_braid`.
- `canonical_plus_multibrane.py::binding_canonical_plus_multibrane` uses `|tr_M_free| − |tr_M_atom|` in categorical units.
- `recursive_three_calibration.py` uses `(c_free − c_atom)` per channel.

These are all **different** definitions of "free baseline". Cross-witness comparisons (as in the session summary) are therefore apples-to-oranges unless explicitly aligned.

**Fix**: document a single baseline convention in `computations/README.md` or a module docstring, then align all probes.

## Items where code is AHEAD of paper

- `thm:markov-trace-factorization` is referenced in the updated jet-tower block but I did not find an explicit `.md` for it — the code's `pair_mode="full"` anticipates this theorem. If the theorem block is missing, it should be added to close the chain.

## SDP / positron probes — NOT integrated into main pipeline

The following modules exist as standalone probes but are **not imported** by `binding_full_pipeline.py → canonical_plus_multibrane.py → mass_from_tower`:

- `positron_lifted_sdp.py` (this branch) — explicit e⁻/e⁺ SDP variables
- `electron_chiral_probe.py` (this branch) — positron dressing + projection
- `pair_factorisation_probe.py` (main) — traced V̂_{ij}
- `content_weighted_pair_probe.py` (main) — SYT-content pair weights
- `multi_level_sdp.py`, `sdp_on_shadows.py`, `sdp_cross_channel.py`, `misdp_cross_channel.py` (main) — SDP formulations

The pipeline used to produce `binding-fast-pipeline.witness.json` uses a **single global Φ_q on the Plancherel-aggregated V̂** with no explicit positron variables, no SDP lifting, no character-traced pairs.  All the probe findings on this session's branch are **diagnostic** — they confirmed the existing aggregate pipeline is algebraically optimal and that explicit positron / SDP-lifted formulations don't improve predictions.  If any should be promoted from probe to production, that's a separate follow-up.

## Recommended sequence to fix before next session

1. **Add `thm:markov-trace-factorization` block** if missing — the updated jet-tower remark references it.
2. **Strip descended from level-1+ in `binding_canonical_plus_multibrane`** — matches the corrected jet-tower prescription. Expected impact: small (descended is already small at levels 1+ due to ℏ_q^(2n) damping), but gets sign semantics right.
3. **Audit E_0 scales** — introduce canonical `ALPHA_BINDING = m_e · 8G`, track where each of the 4+ scales is used, align with paper.
4. **Decide on per-block Φ_q vs aggregate Φ_q** — requires paper update or code convention change. Impact on all mass predictions.
5. **Apply QED correction** for binding — expected to tighten D from 0.018% → 0.008%.
6. **Document baseline convention** centrally.

## Files likely affected

Code:
- `mass_endomorphism.py` (per-block vs aggregate Φ_q)
- `canonical_plus_multibrane.py` (desc term level-counting, E_0)
- `binding_full_pipeline.py` (QED correction, E_0)
- `multi_level_jet_sum.py` (E_0 naming convention)
- `q_parameter.py` (add ALPHA_BINDING)
- `hecke_core.py` (align alpha_em usage)

Paper:
- `braids-and-knots/mass-endomorphism-tower.md` (update to match level-counting if needed)
- Possibly a new `thm:markov-trace-factorization.md` block

## Recommendation

Open a tracking issue on main summarising these five inconsistencies. Each is resolvable in a small focused PR. None is architecturally earth-shaking — all are alignment / convention issues rather than framework redesigns.

The session summary's headline "0.018% on D" uses the code-as-is, so it's **self-consistent within the code** but doesn't match the paper's claim of 0.008% (which assumes QED correction).

Most urgent: **inconsistency #1 (descended level-counting)** and **#4 (QED)** — both are small fixes that should bring predictions into closer alignment with the paper's stated claims.
