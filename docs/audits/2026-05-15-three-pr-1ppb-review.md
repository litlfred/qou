# 1 ppb three-PR review (#644 ⊕ #645 ⊕ #652)

**Date:** 2026-05-15
**Branch:** `claude/review-1ppb-prs-EC0ay`
**Author:** review agent (no new compute; relevance + incorporation
plan only)
**Scope:** open PRs [#644](https://github.com/litlfred/qou/pull/644),
[#645](https://github.com/litlfred/qou/pull/645),
[#652](https://github.com/litlfred/qou/pull/652) against the
[1 ppb coordination ledger](../coordination/1ppb.md).

## TL;DR

| PR | Title | Relevance | Verdict | Blocking |
|---:|-------|:---:|--------|----------|
| [#644](https://github.com/litlfred/qou/pull/644) | Plan + Phase 1/2 plumbing | **primary** | merge first | 2 owner decisions |
| [#645](https://github.com/litlfred/qou/pull/645) | H7a Δ_coupling finding + Lean P4 audit | **high** | merge after #644 | cross-anchor needs #644 witness |
| [#652](https://github.com/litlfred/qou/pull/652) | P31-triage Phase B (CODATA literals) | **infra hygiene** | rebase after #644 | mechanical conflicts only |

The honest M1 baseline under substrate $E_0$ is **−98 % MAE** on
$\{p, n, D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ — the prior
−22 % figure was a proton-fit calibration artefact. PR #644 lands
this honest reading; PR #645 lands the first quantitative closure
hint (H7a at +0.169 %).

## Per-PR relevance

### PR #644 — plan + plumbing (primary)

Adds the authoritative phased plan
[`docs/audits/2026-05-12-1ppb-implementation-plan.md`](https://github.com/litlfred/qou/blob/copilot/analyze-audit-reports-and-fix-calculations/docs/audits/2026-05-12-1ppb-implementation-plan.md)
+ the companion
[`2026-05-12-lean-handover.md`](https://github.com/litlfred/qou/blob/copilot/analyze-audit-reports-and-fix-calculations/docs/audits/2026-05-12-lean-handover.md)
+ the M1 status snapshot
[`2026-05-12-m1-mass-table.md`](https://github.com/litlfred/qou/blob/copilot/analyze-audit-reports-and-fix-calculations/docs/audits/2026-05-12-m1-mass-table.md).

| Phase task | Status |
|------------|--------|
| P1.A — substrate $E_0$ reporting mode | ✅ landed |
| P1.B — Markov-pairing chirality (replaces hand-coded `chirality_signs_for_isotope`) | ⚠️ V1 backfill done for {p, n, D, T, ³He}; **owner decision** on V1 vs V2-V4 production wiring |
| P1.C — T4 stragglers → per-3A formula | ✅ landed (`mass_formula_6term_mpfr_50dps.py`, `d_from_scratch.py`) |
| P1.D — per-partition $k_\lambda$ | ✅ landed |
| P1.E — ⁴He Model B knot survey | ✅ survey witness emitted (`model-b-he4-knot-survey.witness.json`); **owner decision** on final knot |
| P2.A — `tower_mode="habiro"` | ✅ landed |
| P2.B — combined router (sub-mode per atom) + audit-trail fix | ✅ landed |
| P3 / P4 | deferred to dedicated PRs |

**P1.E survey ranking (Wenzl-Schur at $q_0$, plausibility window
$\lvert\tau_M\rvert \in [0.05, 0.5]$):**

| rank | knot | $\lvert\tau_M\rvert$ | $T_1 = m_e\lvert\tau_M\rvert$ (MeV) | in window |
|---:|---|---:|---:|:---:|
| 1 | $8_{17}$ | 0.186 | 0.0949 | ✓ |
| 2 | $10_{123}$ | 0.221 | 0.1130 | ✓ |
| 3 | $8_{18}$ | 0.109 | 0.0558 | ✓ |
| 4 | $L6a4$ | 0.998 | 0.5102 | ✗ |

### PR #645 — H7a finding + Lean P4 audit

Two artefacts that depend on #644 but are independently mergeable:

**(A) H7a — first quantitative Phase 3 hint.** At the (2,2)
doubly-magic anchor, 50 dps:

$$
  \Delta_{\mathrm{coupling}}(2,2) \;\approx\; [A-2]_q \cdot E_0 \cdot
  \log\!\bigl(1/h(q_0)\bigr) \qquad (q\text{-integer prefactor})
$$

closes the anchor to **+0.169 %** (~1700 ppm), **4.2× better** than
H1's classical $(A-2)$ prefactor (+0.71 %). H6 (q-dilog/trilog
additive corrections) and H8 (micro-corrections at $m_e$ / $E_0 h$
scale) are refuted at $10^{-3}$ rational-coefficient tolerance. H7b
(q-deformed log) is refuted at +9.6 %.

The q-deformation lives in the **prefactor**, not in the radial
function. Cross-anchor verification at (2,1) ³He=D+p and (1,2)
T=D+n is the next test, and **requires #644 merged** — H7a's
inputs need the proton/neutron Δ_cat columns landed by #644 in
`magic-shell-empirical-instantiation.witness.json`.

**(B) Lean P4 gap-closeability audit.** All 400 QOU `sorry`s
classified into 6 categories. P4.A
(`prop-rigid-monoidal-structural-gap-invariance.canonical`) and
P4.B (`MagicShellCrossCoupling.canonicalCrossCoupling`) are
correctly kept as **§3b-cond conjectural axioms** — the
trivial-skeleton discharge attempt was reverted because it
violated §3b's "one sorry per conjecture" rule.

### PR #652 — P31-triage Phase B (CODATA literal cleanup)

Indirect to the 1 ppb closure but supports the witnessed-values
infra. Migrates 8 hardcoded literals into typed registries:

- audit-script `m_p` / `m_n` → `codata_constants.M_{P,N}_MEV_VALIDATION`
  (`path_b_defect_binding_probe.py`, `path_b_habiro_mass_probe.py`,
  `paper_six_term_isotope_sweep.py:run_atom_with_tower_combined`)
- CAL-2 anchor `m_μ/m_e` → `q_parameter.MASS_RATIO_MU_E[_STR]`
  (`alpha_em_pslq_uniqueness.py`, `derive_m_baryon_volume_form.py`,
  `knot-volumes.py`)
- Adds `canonical_derivation_pipeline_compliance.py` +
  `witness_reproducibility_check.py` (genuine new infra).

P31 hits drop **18 → 10**; `infra_score` stays 0.58. The 10
residuals are mass-table dict literals deferred to Workplan-0b
($m_n = m_p + Q_\beta$ derivation, not import).

## Conflict map (#644 ⊕ #645 ⊕ #652)

| File | #644 | #645 | #652 | Conflict class |
|------|:---:|:---:|:---:|----------------|
| `computations/sweeps/paper_six_term_isotope_sweep.py` | +250 / -12 | — | +11 / -3 | **mechanical** — #652's `M_P_MEV_VALIDATION` import lands cleanly after #644's structural changes |
| `computations/d_from_scratch.py` | +15 / -7 | — | +3 / -1 | **mechanical** — same pattern |
| `computations/probes/delta_coupling_closed_form_probe.py` | added | — | — | none |
| `computations/probe_delta_coupling_leading_form.py` | — | added | — | none |
| `computations/probe_delta_coupling_residual_closure.py` | — | added | — | none |
| `computations/magic-shell-empirical-instantiation.witness.json` | +35 / -11 | consumes | — | **semantic** — #645 reads the columns #644 writes |
| `computations/probes/path_b_habiro_mass_probe.py` | — | — | +11 / -3 | none (only #652) |
| `computations/compute-audit-scan.witness.json` | — | — | +81 / -9 | none (only #652) |

No three-way conflict; pairwise conflicts are mechanical (literal
migration vs structural refactor) and resolved by ordering #652
last.

## Recommended merge order

**#644 → #645 → #652 (rebased)**

1. **#644 first** — lands the plan, the honest M1 baseline, and
   the witnesses #645 reads.
2. **#645 second** — H7a finding can verify cross-anchor on the
   landed proton/neutron Δ_cat columns; Lean P4 audit is
   self-contained.
3. **#652 last** — rebase onto post-#645 main; the literal
   migrations apply cleanly to the structurally-refactored scripts.

## Open owner decisions (block #644 merge)

1. **P1.B canonical mirror convention** — V1, V2, V3, or V4 for
   production wiring of `term5_aK_audit.py`? V1 is the natural
   Hecke choice ($\tau(\beta \beta^{-1})$); V2-V4 are alternative
   mirror-knot conventions with differing physical meaning. The
   V1-vs-heuristic delta is 2.2 % on nucleons / 13-15 % on
   multi-nucleon. V2 backfill alone takes >34 min/atom for
   deuteron under the current symbolic implementation; A ≥ 3 is
   unbounded.
2. **P1.E ⁴He Model B knot** — pick from
   $\{8_{17}, 10_{123}, 8_{18}\}$ (all in the plausibility
   window) or commission a 4-strand survey for the Brunnian
   4-component link. The plan's primary structural candidate
   ($8_{18}$, 4-fold symmetric) sits at the lower edge of the
   window; $8_{17}$ and $10_{123}$ are closer to the geometric
   mean.

## Substrate-derivation gap (blocks #645 Lean §3b-cond promotion)

PR #645's H7a `[A-2]_q · E_0 · log(1/h)` formula is
**empirically calibrated at the (2,2) anchor**, not yet derived
from KLR / Markov-trace primitives. Before any §3b-cond
Pattern-A/B Lean promotion of
`MagicShellCrossCoupling.canonicalCrossCoupling`, a substrate
derivation of the quantum-integer prefactor is required (per
CLAUDE.md §3b-cond requirement 1: class fields encode the
conjecture's content with one `sorry` per conjecture).

## Coordination-ledger updates needed

After this review doc lands, append a 3-row block to
[`docs/coordination/1ppb.md`](../coordination/1ppb.md) under "Ledger"
recording: (i) #644 plan + plumbing landing, (ii) #645 H7a finding +
Lean P4 audit, (iii) #652 P31-triage Phase B + the rebase ordering
discipline established here.

## Anti-patterns confirmed avoided

- ❌ Calibrate $\Delta_{\mathrm{shell}}$ to AME — none of the
  three PRs do this; H7a is empirically tested at one anchor and
  flagged as not-yet-substrate-derived.
- ❌ Hide proton-fit calibration — #644's M1 doc explicitly
  surfaces the −98 % honest baseline and the prior −22 % as a
  calibration artefact.
- ❌ Trivial-skeleton sorry discharge — #645 reverts its own
  attempt after recognising the §3b-cond violation.
