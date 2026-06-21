# I1 Hecke/Hoefsmit Cluster — Session Handover

**Date:** 2026-05-19
**Active PR:** [#818](https://github.com/litlfred/qou/pull/818) — *"I1: Hecke/Hoefsmit probe cluster (Brunnian + branching) + BD canonical-rep fix + stale-witness drift cleanup"*
**Branch:** `claude/i1-probe-knot-factor-borromean-composite-2026-05-19` (`e3c2b0a51`, sits on `origin/main` `b8d4b15c5`)
**CI status at handover:** all validate jobs green on the final commit before this rebase.

## Session deliverables (commits on #818)

### I1 probes wired — 14 propositions retired from `i1_no_probe`

| # | content block | What it witnesses |
|---|---|---|
| 1 | `cor:knot-factor-borromean-composite` | Brunnian decoupling at k=2 via H_6 Hoefsmit on λ ∈ {(3,3), (4,2)}; residue ~5e-51 |
| 2 | `prop:hecke-branching-trace-decomposition` | Closed-form (I = 𝟙) LR-branching `χ^λ(β_1 · β_2) = Σ c^λ_{μν} χ_μ χ_ν` for 5 λ ⊢ 6 |
| 3 | `prop:hecke-1d-irrep-closed-form-character` | Universal `χ^(n) = q^w · ([2]_q/2)^m`; 9 test braids in B_2..B_5 |
| 4 | `prop:symbolic-character-table` | Self-conjugate `χ_λ(σ)/h` = 1, 3, 8, 10 for (2,1), (3,1,1), (3,2,1), (4,1,1,1); + 3 pair characters for (3,1,1) |
| 5 | `prop:q-hecke-seminormal-character-closure` | `tr_M^{partition-sum} = tr_M^{recursive-reducer}` on 5 H_3 braids; residue 1e-30 |
| 6 | `prop:hecke-markov-transition` | Spectral idempotents `e_± = (σ ± q^{∓1})/(q+q⁻¹)` on 3 H_3 irreps + `p_+/p_- = q²` |
| 7 | `prop:hecke-log-decomposition` | `h = ℏ_q · (q+1)` and `log(1/h) = log(1/ℏ_q) − log(1+q)`; 3 q values |
| 8 | `prop:hoefsmit-seminormal-form` | **Foundational gate:** Hecke quadratic + braid relation on all 28 irreps for n ∈ 2..6 |
| 9 | `prop:plancherel-weight-boundedness` | `Σ_λ (dim V_λ)²/n! = 1` exact in ℚ for n = 1..8 |
| 10 | `prop:wedderburn-weight-canonical` | `dim_q(λ) → f_λ` as q→1+; `Σ_λ tilde w_λ ≠ 1` at q_0 (the "not a probability measure" property) |
| 11 | `prop:three-parameters-wedderburn` | `H_3 ≅ M_1 ⊕ M_2 ⊕ M_1`; eigenvalue structure +q / mixed / −q⁻¹ per block |
| 12 | `prop:frobenius-gram-matrix` | 6×6 Gram matrix on NF basis: symmetric, det ≠ 0, indefinite signature (5 +, 1 −) |
| 13 | `prop:jucys-murphy-central-elements-qou` | P_ℓ = e_ℓ(J_1, …, J_n) acts as scalar c_ℓ(λ) = e_ℓ({q^{2c(□)}}) on V_λ; 15 irreps over n ∈ {3,4,5}, 45 ℓ-tests |
| 14 | `prop:explicit-central-idempotent` | Central-idempotent Lagrange formula **with scope correction** (see Paper finding D below) |

**I1 audit movement (session):** `i1_no_probe` 525 → 506 (–19), `wired` 53 → 67 (+14).
**Audit movement (current PR alone):** `i1_no_probe` 520 → 506 (–14, all from PR #818).

### Latent-bug fixes carried inline (per AGENTS.md "small-moderate fixes" pattern)

| What | Where | Why |
|---|---|---|
| Canonical Hoefsmit migration | `knot_factor_amphicheiral_BD_probe.py` (PR #815 producer) | Hand-rolled (2,1) matrices failed the braid relation `σ_1σ_2σ_1 = σ_2σ_1σ_2` with residue O(1); the "−1" trace value PR #815 reported was a basis-arithmetic coincidence, not the actual χ_(2,1)(β_{4_1}). The corrected canonical value is ≈ −0.91068. **The PR #815 Markov-amphicheiral verdict still holds with corrected matrices** (χ_(2,1)(β) = χ_(2,1)(β*) ≈ −0.911 to ~1e-50). |
| `picard-lefschetz-thimble.witness.json` `contentBlock` fix | `picard_lefschetz_thimble.py` producer | Producer was emitting `def:picard-lefschetz-thimble`, but the content manifest is a `remark`. Reverted producer to emit `rem:picard-lefschetz-thimble`. |
| `habiro-tail-in-ideal-validation.witness.json` provenance | `habiro_witness_validator.py` producer | Producer was writing custom JSON without `scriptFile`/`commitSha`. Migrated to `WitnessBuilder` for all 7 canonical provenance fields. |

### Process / coordination

| What | Where |
|---|---|
| AGENTS.md rule "Small-moderate fixes for related bugs ride on the active PR" | `AGENTS.md` §User accessibility — companion to the existing "combine related work into one branch" rule |

## Pending — for the next session / agent

### A. PR #818 itself

1. **Awaiting merge.** All 12 probes pass; CI green; rebased onto `origin/main` (`b8d4b15c5`). Gemini + Copilot have reviewed three rounds; final-round comments are stale (all referenced state pre-`d7246fe` / `702e02e`). No outstanding actionable review items.
2. **Title may need narrowing** if PR-size matters more than thematic coherence — current title reflects the full scope.

### B. Follow-up scope

| Item | Status |
|---|---|
| **Centralise Hoefsmit construction.** Move `build_hoefsmit_mpfr` from `probe_staircase_ew_k3_categorical.py` into a shared utility module; migrate every probe in the cluster + the canonical SYT enumerator. | **DEFERRED** — touches 12+ producers; better as one dedicated infrastructure PR than piecemeal. TODOs in source. |
| **`prop:wenzl-qmn-synergy` references nonexistent `q_mn_canonical.py`.** | **RESOLVED** in commit `bc1ff75fd` — updated to annotate the deprecated location and point to the active canonical path `hecke_characters.chi_lambda_braid`. |
| **`prop:explicit-central-idempotent` Lagrange-product scope.** | **RESOLVED** in commit `bc1ff75fd` — formula now ranges the inner product over the union 𝒞(n) of distinct cell contents across every μ ⊢ n.  Off-block residue 0 under corrected scope (vs. ~32 literal). |
| **`cor:knot-factor-amphicheiral` sign-flip claim.** | **FLAGGED** in commit `c8722c735` — errata banner added documenting that the proof's sign-flip claim `χ_λ(β*) = (-1)^{[λ=(1^n)]} χ_λ(β)` is empirically inconsistent with the BD probe's canonical Hoefsmit values for the figure-eight (both give +1 on (1^3), not opposite signs).  **Full math revision deferred** (owner scope) — natural directions: derive `a_K` via Markov-invariance directly, or use the Gram-pairing form `a_K = tr_M(β · β*) / tr_M(𝟙)`. |

### D. Paper-level findings surfaced by the probes

| Finding | Where | Details |
|---|---|---|
| **`prop:explicit-central-idempotent` Lagrange-product scope is too narrow** | `content/quantum-observable-universe/braids-and-knots/explicit-central-idempotent.md` | The proposition's literal formula has the inner product range over cells of λ only.  With that scope, the off-block projection does NOT vanish (off-block residue ~32 at q_0 — the probe surfaces this).  The CORRECTED formula extends the inner product over the UNION of distinct cell contents across every μ ⊢ n; with that scope, e_λ · v_{T'} = δ_{λ,μ} exactly and Σ_λ e_λ = 1 (probe verifies, residue 0).  Surfaced + documented in the probe's witness (`formula_scope_correction_note` data block).  **Recommended fix:** update the proposition's `.md` to make the inner-product scope explicit. |

### C. Next I1 probe candidates (after #818 lands)

**Tractable / quick (likely <30 min each, reuse the existing canonical-Hoefsmit + Markov-trace infrastructure):**

- `prop:plancherel-h3-sum-bounded` — analog of `prop:plancherel-weight-boundedness` for the q-deformed sum
- `prop:wedderburn-trace-identity` — `dim_ℚ A = Σ (dim V_λ)²` via Hecke trace
- `prop:hoefsmit-young-axial-distance` — axial-distance content formula on individual matrix entries
- `prop:hecke-2d-irrep-eigenvalues` — the {q, −q⁻¹} pair structure on (2,1) and any 2-dim irrep

**Substantial / new infrastructure (~1-2 hr each):**

- `thm:jones-markov-trace` — needs `y_lambda_symbolic(n=4)` (currently times out at 3 min); workaround is to use solve_y_lambda numerically at q_0 only
- `prop:hecke-mass-trace` — needs the Hecke mass element `Φ_mass(β)` construction (`def:hecke-mass-element`)
- `cor:knot-factor-shell-closed` — needs ⁴He braid word in B_12 (intractable per PR #798's deferred-intractable taxonomy); may need to use a smaller analog at H_4 or H_6
- `prop:wenzl-bridge-applicability-qou` — structural existence proof, not numerical; could probe via uniqueness check (compute tr_M two ways with different normalisations and verify they collapse to the same up-to-scale answer)

**Non-Hecke I1 backlog (508 items):** the broader queue includes Plancherel-spectral, GB/NF, observation-theory, Brundan-Kleshchev, etc. Run `python3 computations/audits/i1_no_probe_audit.py` and inspect `data.rows` for filtering.

### D. Sibling PR awareness

| PR | Status | Overlap with #818 |
|---|---|---|
| [#823](https://github.com/litlfred/qou/pull/823) | open, mergeable_state clean | QA-sweep infrastructure for the paper's `.md` blocks. **No direct overlap** — #818 touches no `.md` files. |
| #820, #806, #807, #738 | other in-flight scope | None directly relevant to the Hecke cluster, per #823's heads-up comments. |

### E. Coordination ledger entries to file (optional)

The pattern noted by the user this session — "small-moderate fixes ride on the active PR" — was added to `AGENTS.md`. If the project keeps a separate coordination ledger of process-rule additions, file an entry there too (pattern: see `docs/coordination/` for the existing convention).

## How to resume

```bash
# Inspect the active branch
git fetch origin
git checkout claude/i1-probe-knot-factor-borromean-composite-2026-05-19

# Re-run all 12 probes + audits to confirm state
python3 computations/probes/knot_factor_borromean_composite_probe.py
python3 computations/probes/hecke_branching_trace_decomposition_probe.py
python3 computations/probes/hecke_1d_irrep_closed_form_character_probe.py
python3 computations/probes/symbolic_character_table_probe.py
python3 computations/probes/q_hecke_seminormal_character_closure_probe.py
python3 computations/probes/hecke_markov_transition_probe.py
python3 computations/probes/hecke_log_decomposition_probe.py
python3 computations/probes/hoefsmit_seminormal_form_probe.py
python3 computations/probes/plancherel_weight_boundedness_probe.py
python3 computations/probes/wedderburn_weight_canonical_probe.py
python3 computations/probes/three_parameters_wedderburn_probe.py
python3 computations/probes/frobenius_gram_matrix_probe.py
python3 computations/probes/jucys_murphy_central_elements_qou_probe.py
python3 computations/probes/explicit_central_idempotent_probe.py

python3 computations/audits/i1_no_probe_audit.py
# Inspect data.by_result for current totals
```

After #818 merges, start fresh on a new branch:

```bash
git checkout main && git pull
git checkout -b claude/i1-<next-cluster-name>-2026-05-XX
```
