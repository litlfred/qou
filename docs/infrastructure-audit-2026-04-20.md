# Infrastructure Audit — Code vs Paper

*Compiled 2026-04-20 against `docs/derivation-audit-2026-04-20.md`.*

## Scope

Compare what the paper content blocks prescribe vs what the computational modules (`folio-assistant/computations/*.py`) actually compute. Flag inconsistencies.

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

### 1. Descended term level-counting — HIGH — **RESOLVED 2026-04-20**

**Paper** (`rem:mass-endomorphism-jet-tower`, recently revised):
> The **descended** contribution is **not** summed over jet levels. Including a separate descended product at every jet level would double-count the level-0 holonomy.

Derivation added: **`prop:descended-level-zero`** — iterated
descent idempotence $\hat\tau_n^2 = \hat\tau_n$ collapses the
descended trace at every jet level to the same base-level
holonomy $\mathfrak{m}(\varrho_0) = |\prod_i \hat V_i^{(0)}|$.
Summing it per level overcounts by
$\sum_{n=1}^N \hbar_q^{2n} \cdot \mathfrak{m}(\varrho_0)
\approx 0.01 \cdot \mathfrak{m}(\varrho_0)$ at $q_0$ (≈1% of
every binding prediction).

**Code fix applied** (branch `claude/improve-mass-calculations-oE5aA`):
added `include_desc: bool = True` parameter to `tower_mass_level`
in `canonical_plus_multibrane.py`; updated all level-loop call
sites to pass `include_desc=False` (level 0's descended
contribution is handled by the canonical Markov-trace term).
Call sites updated:

- `canonical_plus_multibrane.py::binding_canonical_plus_multibrane` (main path)
- `canonical_plus_multibrane.py::_binding_cached` (CLI path, both closed-form and truncated branches)
- `binding_fast_pipeline.py::binding_fast` (level loop)
- `binding_full_pipeline.py::binding_full` (level-1 call)
- `unified_lift.py::binding_unified` (jet loop)
- `kahler_lift.py` CLI (both demo loops)
- `binding_full_content_pair.py::tower_mass_level_content` + caller

### 2. Three-Wedderburn-channel binding — HIGH — **RESOLVED 2026-04-20 (option c)**

**Paper** (`prop:tower-binding-energy`):
$$B(Z,N) = \sum_{\lambda \in \{\text{sym,std,alt}\}} w_\lambda \cdot m_e \cdot \sum_{i=0}^{A-2} \ln|\Phi_q(\hat{V}_i^\lambda)|$$

**Root cause of prior saturation claim**: the branch's
`per_block_phi_q.py` implemented the **wrong form** — it
computed `Φ_q(V̂)` per block (which diverges at the pole
$|V̂| \to q^-$) rather than the paper's `ln|Φ_q(V̂)|`
(which has only isolated logarithmic singularities at
$V̂ = q^k$, and admits the paper's stated "analytic
continuation past $|V̂| = q$").

**Resolution**: option (c) — paper formula is computable in its
**log form** via $\ln|\Phi_q(v)| = -\sum_{k\ge 1} \ln|1 - q^{-k}v|$,
analytically continued past $q$ by $|1 - q^{-k}v| = q^{-k}v - 1$
when $q^{-k}v > 1$.  Isolated pole hits at $V̂ = q^k$ (e.g.
$V̂^{\text{sym}} = q$ at pp inter-nucleon crossings, $V̂^{\text{sym}} = q^3$
at electron trefoil) handled via **principal-value
regularization**: drop the zero-measure factor $|1 - q^{-k}v|^{-1}$
at the pole index from the product.

**New module**: `binding_per_block_log.py` — implements
`ln_abs_phi_q(v, pole_mode='principal')` and
`binding_per_block_log(cross, n_strands, apply_qed=True)`.
Sanity check on {D, T, ³He, ⁴He} matches the paper's
`full-tower-mass.witness.json` table within expected
precision (D: 0.15%, T: 0.08%, ³He: 0.07%, ⁴He: 0.34%).
QED correction $(1 - \alpha_{\text{EM}}/2)$ applied per
`prop:deuterium-derived-binding`.

Paper's aggregate form (`mass_endomorphism.mass_from_tower`)
and per-block log form now **coexist** as two separate
pipelines:

- **Aggregate** (`mass_from_tower`): particle masses (m_p, m_n, m_e, γγ)
- **Per-block log** (`binding_per_block_log`): nuclear binding B(Z,N)

The two scales differ because the paper's B-formula uses
$m_e \cdot w_\lambda$ coefficients whereas the particle-mass
formula uses a single $E_0$; combining them requires the
three-calibration scheme the user is pursuing.

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

**Fix**: document a single baseline convention in `folio-assistant/computations/README.md` or a module docstring, then align all probes.

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
