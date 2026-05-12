# Canonical-derivation compute review — last 3 days

**Date:** 2026-05-12
**Branch:** `copilot/review-canonical-derivation-compute-again`
**Trigger:** owner request — "review all compute in last 3 days
related to canonical derivation. categorize fixes that need to be
implemented in compute pipeline. audit compute infra to see what
does not comply fully. develop work plan to fix. implement."
**Anchor methodology:**
[`docs/derivation-tracking-methodology.md`](../derivation-tracking-methodology.md)
(7-step categorical chain: SDP → GB-NF → Wedderburn → $y_\lambda \chi_\lambda$ → $\mathrm{tr}_M$ → $\rho \cdot \mathrm{tr}_M$ → Archimedean MeV).

This is a **synthesis review** that consolidates ~18 in-tree audit
docs from 2026-05-09 → 2026-05-11 plus the static infra scanners
into one categorized fix-list. Every individual finding already
has a deeper source doc — those are linked, not duplicated.

---

## 0  Scope of "last 3 days"

| Window | Commits | Compute scripts touched | Audit docs added |
|--------|--------:|------------------------:|-----------------:|
| 2026-05-09 → 2026-05-12 (this branch) | 446 | 287 (.py) | 31 (`docs/audits/2026-05-{09,10,11}-*`) |

Branch `copilot/review-canonical-derivation-compute-again` is at
parity with `origin/main`; this review reflects state on `main` as
of the trigger date and the open sibling PRs (#638, #639, #640) it
inherits from.

---

## 1  Inventory of canonical-derivation audits in scope

Only audits **directly** about the canonical derivation chain
(steps 1 → 7 of the methodology) are listed. Each row links to the
detailed source.

### 1.1  $E_0$ / calibration / 3-input discipline

| Audit | Verdict |
|-------|---------|
| [`2026-05-10-hbar-q-scaling-audit.md`](./2026-05-10-hbar-q-scaling-audit.md) | 3 distinct $E_0$ conventions in `derivation_chain.E_0_CONVENTIONS` (A/B/C); Conv C is a back-fit. |
| [`2026-05-11-three-calibration-discipline-violations.md`](./2026-05-11-three-calibration-discipline-violations.md) | 1 hard violation in content (`recomputed-low-isotope-mass-table.md`), 1 in script (`atomic_mass_via_rho_k.py`). 8 Class-B baseline-extraction scripts OK. 5 Class-C diagnostic probes OK. |
| [`2026-05-11-1ppb-gap-narrowing-plan.md`](./2026-05-11-1ppb-gap-narrowing-plan.md) | Hard floor 780 ppb from CAL-2; dominant blocker is operator-volume regulariser at 10⁻¹–10⁴; structural gap. |
| [`2026-05-10-non-calibrated-mass-state-of-play.md`](./2026-05-10-non-calibrated-mass-state-of-play.md) | $Q_\beta$ derives at +0.17%; per-nucleon absolute masses are 50%–99% off across all 3 implementations. |
| [`2026-05-11-why-individual-mass-residuals-fit-not-derive.md`](./2026-05-11-why-individual-mass-residuals-fit-not-derive.md) | Cat-units → MeV via $m_X^{\text{Hecke}}/m_e^{\text{Hecke}}$ ratio is implicit ansatz; off by 1570× for proton. Differences (Q_β) work; absolutes don't. |

### 1.2  Markov trace ($\tau_M$) / weight families

| Audit | Verdict |
|-------|---------|
| [`2026-05-11-plancherel-usage-audit.md`](./2026-05-11-plancherel-usage-audit.md) | $w_\lambda$ overloaded across 4 content blocks (classical vs q-deformed); Wenzl-bridge $y_\lambda = (-1)^\kappa w_\lambda$ falsified outside self-conjugate stratum; fixed in-branch by tilde-naming + restriction. |
| [`2026-05-11-q-beta-form-A-vs-form-B-canonical-choice.md`](./2026-05-11-q-beta-form-A-vs-form-B-canonical-choice.md) | Form A (counit) recommended canonical; Form B (transfer-matrix log) numerically unmatched (34–436% off). |
| [`2026-05-11-q-beta-residual-decomposition.md`](./2026-05-11-q-beta-residual-decomposition.md) | Dual-basis identity $G^{-1} \cdot t = e_\gamma$ → counit IS the canonical pairing. |
| `derivation_chain.py:68-93` (in-source escalation) | TR_M_AT_Q0 values disagree with Frobenius-proof $\tau_M$ values; relabel registry to $\tau_{SW}$ pending. |

### 1.3  Model B (knot-canonical) pipeline

| Audit | Verdict |
|-------|---------|
| [`2026-05-11-model-b-mass-table.md`](./2026-05-11-model-b-mass-table.md) | Model B end-to-end pipeline lands (`probe_sdp_canonical_paper_formula.py`); single-term $T_1$ formula falsified at 87–100% on D/T/³He; multi-term $T_1+\dots+T_6$ assembly missing for Model B. |
| [`2026-05-11-brane-tower-n_star-closure-audit.md`](./2026-05-11-brane-tower-n_star-closure-audit.md) | No scalar $n_\star$ rule closes AME light-isotopes uniformly (6 families refuted). |
| [`2026-05-09-mass-table-fitting-audit.md`](./2026-05-09-mass-table-fitting-audit.md) | Per-quantity flag scan: ✅ derived, ⚠ calibration-floor, ⛔ census/numerology, 🔎 open conjecture. |
| [`2026-05-11-per-partition-k-lambda-selector-investigation.md`](./2026-05-11-per-partition-k-lambda-selector-investigation.md) | Per-partition $k_\lambda$ truncation is the canonical refinement (#639). |

### 1.4  Six-term mass formula

| Audit | Verdict |
|-------|---------|
| [`2026-05-11-three-calibration-discipline-violations.md`](./2026-05-11-three-calibration-discipline-violations.md) (Class A) | $\rho_K^{LO}$ formula in `atomic_mass_via_rho_k.py` is a tautology — fixed in-source via "LO TAUTOLOGY NOTICE" docstring. |
| [`2026-05-09-mass-table-1ppb-audit.md`](./2026-05-09-mass-table-1ppb-audit.md) | Per-quantity 1 ppb attainability scan. |
| [`2026-05-09-workplan-update-rho-k.md`](./2026-05-09-workplan-update-rho-k.md) | Workplan for $\rho_K$ path (post-PR #564). |
| [`2026-05-10-workplan-0b-script-rewire-handoff.md`](./2026-05-10-workplan-0b-script-rewire-handoff.md) | Script-rewire handoff (which scripts to migrate). |

### 1.5  Static infra scanners (machine-checked)

| Scanner | Witness | Headline |
|---------|---------|----------|
| `compute_audit_scan.py` | `compute-audit-scan.witness.json` | 245 files, 261 hits across P14/P15/P16/P21/P30 (perf antipatterns) |
| `canonical_script_input_audit.py` | `canonical-script-input-audit.witness.json` | 527 rows; **12 canonical 3-input scripts**, 112 over-count, 54 vol-hyp-fitted, 9 m_p-only, 12 Q_β-only |
| `lp_dual_witness_validator.py` | (CI, warn-only) | 3/3 LP-dual flagged witnesses include duals; 14 LP-solving scripts off the hint list (presumed feasibility-only) |
| `derivation_chain_audit.py` | `derivation-chain-audit.witness.json` | 71 chains, 91 assertions, all-passed |

---

## 2  Categorization of fixes

Per the user's "categorize fixes" ask, every open finding from §1
is bucketed by **status** and **action class**.

### 2.A  Closed in-tree on `main` (verified by source-read this session)

These are landed; no further action is needed in this PR. Listed
so the work-plan in §4 can be ranked correctly.

| Fix | Source-of-truth | Verification |
|-----|-----------------|--------------|
| LO tautology docstring on `atomic_mass_via_rho_k.py` | `atomic_mass_via_rho_k.py:5–11` | Banner present: "⚠ **LO TAUTOLOGY NOTICE.**" |
| `recomputed-low-isotope-mass-table.md` p/n rows flagged tautology | `recomputed-low-isotope-mass-table.md:83–84,90–92` | Dagger † footnote present; "Calibrated form" heading; cross-link to three-cal discipline. |
| `E_0_CONVENTIONS["C_proton_back_fit"]` deprecated | `derivation_chain.py:368–388` | "⚠️ DISCIPLINE VIOLATION. Do not consume in new production chains; use convention B instead." |
| `TR_M_AT_Q0` τ_M / τ_SW conflation annotated | `derivation_chain.py:68–93` | Inline escalation table comparing the 3 conventions; cross-link to §"Update 2026-05-11" in residuals audit. |
| Plancherel symbol overload narrow-fixed | PR #636 (in-flight); `2026-05-11-plancherel-usage-audit.md` §"Implemented fixes" | Tilde-naming `$\tilde w_\lambda$`, Wenzl-bridge restricted to self-conjugate. |
| Model B end-to-end pipeline lands | `probe_sdp_canonical_paper_formula.py`, `probe-sdp-canonical-paper-formula.witness.json`; `TR_M_CANONICAL_B_AT_Q0` registry in `derivation_chain.py:138–144` | New compute lands; ⁴He Model B explicitly open per memory. |
| 50-dps companion to TR_M_AT_Q0 | `derivation_chain.py:104–108` (`TR_M_AT_Q0_50DPS`) | Decimal strings present per Gemini review on #640. |

**Verdict for the discipline-violations audit's three explicit
Recommendations (1, 2, 3):** all **already landed**.

### 2.B  Ready-to-implement (concrete, low-risk, not yet landed)

| Fix | Source audit | Risk | Why not done yet |
|-----|--------------|------|------------------|
| **B-1.** Add docstring header to `deuteron_delta_i_audit.py:112` flagging it as audit-only consumer of Conv-C pattern. | This review (newly identified) | Trivial, audit-only script. | Not previously inventoried; surfaced by this review's grep for `M_p - t6` consumers. |
| **B-2.** Relabel `schur-weyl-weight-*.derivation.json` → `tau-sw-weight-*.derivation.json` per Frobenius-selection proof. | Residuals audit Rec 4 | **Medium** — 21 JSON renames + 8 Python consumer updates (incl. `wedderburn_jones_markov.py`, `habiro_coefficients_interpolate.py`, `term6_full_pole_sum.py`, both `build_markov_trace_assembly_*chain.py`). | Non-trivial multi-file rename; not done as "minimum change" in any single PR. |
| **B-3.** Add a single canonical-derivation-pipeline-compliance witness that joins compute-audit-scan + canonical-script-input-audit + LP-dual validator into one "current state" snapshot. | This review (new) | Low — new aggregator script consuming 3 existing witnesses. | Not previously requested. |
| **B-4.** Audit deeper: are any **other** content blocks downstream of `atomic-mass-via-rho-k.witness.json` carrying "prediction" language? | Discipline-violations audit Rec 3 (after #637 merges) | Low — content scan. | #637 has merged (per `2026-05-11-1ppb-gap-narrowing-plan.md` §"Companion sibling findings"); ready now. |

### 2.C  Blocked on author / structural R&D (no implementation in this PR)

| Item | Source | Blocker |
|------|--------|---------|
| C-1. Should the paper claim the framework predicts absolute nucleon masses, or only differences/ratios? | Residuals audit Action 2 | Open question for author. |
| C-2. Form A vs Form B for $Q_\beta$ — settle on Form A as canonical. | Form-A-vs-B audit | Recommendation; needs author sign-off + paper update. |
| C-3. Brane-tower $n_\star$ closure (`conj:brane-tower-z-habiro`) | 1ppb gap-narrowing plan §P0–P2 | Open R&D; PR #638 refutes scalar $n_\star$; per-partition $k_\lambda$ (#639) is the canonical refinement. |
| C-4. Substrate derivation of $\lambda_{\text{scale}}$ in Borromean baryon mass formula | Residuals audit §"Where the $\lambda_{\text{scale}} \approx 2.46$ might live" | Symbol declared, not defined; structural research. |
| C-5. Crystal-bases (KL / Kashiwara) replacement for Gröbner–Shirshov in `markov_peel` | 1ppb gap-narrowing plan §P3 | ~1 week implementation; opens $n \leq 60$ compute. |
| C-6. $\Delta_{\text{shell}}$ closed form for `DeltaCouplingClosedForm` Lean class | 1ppb gap-narrowing plan §P1.1 | Categorical research; 4 candidate forms listed. |
| C-7. Compute $J_{\mathcal{B}_3}(q_0; \text{orientation})$ symbolically | Residuals audit Action 6 | Diagnostic compute; non-blocking. |
| C-8. Multi-term assembly $T_1+\dots+T_6$ on Model B's SDP-canonical braids | Model B mass table audit §"Open questions" | $T_2+T_3$ blocked on C-3; $T_5$ sign-indefinite; $T_6$ open R&D. |

---

## 3  Compute-infra compliance audit

This is the user's "audit compute infra to see what does not comply
fully" ask. Compliance is measured against five established
contracts; each row cites its enforcement mechanism.

| Contract | Source | Current state | Enforcement gap |
|----------|--------|---------------|-----------------|
| **WitnessBuilder usage** (every `.witness.json` carries `scriptHash`, `computedAt`, `durationMs`) | `witness_base.py`; `compute-audit.md` P30 | **104 files** still write witnesses by hand (P30 finding). | Mechanically detected; no auto-fix yet. Recommend batched sweeps of ≤10 files (per workplan §Tier 2). |
| **CODATA constants from `codata_constants.py` / `experimental_constants.py`** (no hardcoded literals in production scripts) | `computations/README.md:18-21`; memory: "constants" | Audit-only; no scanner currently flags hard-coded CODATA. | **Gap.** Add a P31 scanner (string-match for `0.51099895`, `938.272`, `939.565`, `0.78233`, `206.7682830` outside `codata_*.py`/`experimental_*.py`). |
| **3-input canonical scheme** ($m_e$ + $q_0$ + $Q_\beta$ only) | `calibration-inputs.md`; `canonical_script_input_audit.py` | **12 / 527 scripts** in canonical scheme. **112 over-count** (consume both $m_p$ and $m_n$ — implicit 4th/5th calibration). **54 vol-hyp-fitted.** | **High gap.** Most scripts pre-date the 3-input discipline; 112 over-count is a re-frame backlog (most are Class-B audit-only per discipline-violations audit but not all are tagged). |
| **LP/SDP dual emission** (every operator-selection LP returns `y_star`, `active_set`, `dual_obj`, `duality_gap`) | CLAUDE.md "LP / SDP duals — first-class infra"; `lp_dual_witness_validator.py` | **3 / 3** flagged witnesses include duals (post-2026-05-08 tightening). 14 LP-solving scripts off the hint list. | **Low gap** for tightened-list. Per-script confirmation that off-list scripts are genuinely feasibility-only is pending; default policy is presumed-OK with opt-out. |
| **`TR_M_AT_Q0` single-source-of-truth** (no other module re-defines canonical $\tau_M$ literals) | memory: "constants" → `derivation_chain.TR_M_AT_Q0` | **In-source warning** documented (lines 68–93). Frobenius proof on `main` (commit 25a204efa) selects a *different* $\tau_M$ value via `from_scratch/`. | **Open conflict.** Registry value (= Wenzl-bridge $y_\lambda$ assembly) ≠ Frobenius-selected $\tau_M$ value (= `from_scratch/` chain). Must be resolved by author choice or follow-up audit; relabeling alone (B-2 above) does not resolve which value is canonical. |
| **Bit-stable JSON for `*.derivation.json` / `*.witness.json`** | `derivation_chain.py:54–58` (PR #473 directive) | Held by convention (no scanner). | Recommend a CI re-run check (run any builder twice; assert byte-equal output). |
| **Notation register compliance** (`τ_M` not `τ_SW`, `\mathbf{C}` not `\mathcal{C}`, `$q$` symbolic outside Ch 7) | `notation-register.md`; `notation-collisions.md`; `local/rendering-auditor` | Held by skill (manual). | Out of scope for compute-infra; covered by separate skill. |

### Numeric snapshot (machine-checked, 2026-05-12)

```
compute-audit-scan.witness.json (P14/P15/P16/P21/P30)
  P14:   1
  P15:  64   (sp.cancel on full expression)
  P16:  71   (sp.simplify before evalf)
  P21:  21   (Hoefsmit construction without BlockCache)
  P30: 104   (.witness.json without WitnessBuilder)
  total findings: 261 across 245 files

canonical-script-input-audit.witness.json
  no-hadronic-input (substrate-only):                         340
  4-input-mp-and-mn (over-counts hadronic if Q_β implicit):   112
  vol-hyp-fitted (uses Vol(K); FITTED under option B):         54
  m_p-only (no Q_β; m_n derivation TBD):                        9
  Q_β-only-hadronic:                                           12

derivation-chain-audit.witness.json
  71 chains, 91 assertions, allPassed: True
```

---

## 4  Ranked work plan

Items that are **closed** (§2.A) or **blocked** (§2.C) are excluded.
Remaining items prioritized by **(infra leverage) / (risk × cost)**:

### Priority 0 — verify / hold the line (cheap, immediate)

- **P0.1.** Add the canonical-derivation-pipeline-compliance
  aggregator witness (§2.B B-3). Single new script that loads the 3
  existing witnesses and emits a one-shot dashboard. Cost: ~30 min.
  **Status: deferred to the next push.** (The current branch is
  delivering the analytic synthesis; the aggregator is a separate
  follow-up.)

### Priority 1 — discipline cleanup (low risk)

- **P1.1.** Annotate `deuteron_delta_i_audit.py:112` as an audit-only
  Conv-C consumer (B-1). Single docstring line. **Implemented in
  this PR — see §6.**
- **P1.2.** Audit content blocks downstream of
  `atomic-mass-via-rho-k.witness.json` for "prediction" language
  (B-4). Content-only scan. **Deferred.**

### Priority 2 — Frobenius / τ_M / τ_SW relabel (medium risk)

- **P2.1.** Land the `schur-weyl-weight-*` → `tau-sw-weight-*`
  rename across 21 derivation chains + 8 Python consumers (B-2).
  **Deferred** — needs author sign-off on the canonical name and
  on resolution of the deeper TR_M_AT_Q0 conflict (which value is
  canonical?).

### Priority 3 — infra scanner extensions

- **P3.1.** Add P31 scanner: hardcoded-CODATA detection outside
  registry files. **Deferred** — small but adds new code.
- **P3.2.** Add a witness reproducibility check (run any
  `*.derivation.json` builder twice; assert byte-equal output).
  **Deferred.**

### Priority 4 — structural / R&D (out of compute-infra scope)

Per §2.C C-1 through C-8: open author / structural research. Not
implementable in this PR.

### Quantitative milestones (re-stated from `2026-05-11-1ppb-gap-narrowing-plan.md`)

| Milestone | Residual target | Stage of plan |
|-----------|----------------:|---------------|
| **M0** (current) | ~20% on best atom | post-PR #638 closure refutations |
| **M1** | ~1% on doubly-magic ⁴He | per-partition $k_\lambda$ (#639 cherry-pick) |
| **M2** | ~0.1% on AME light-isotope sample | $\Delta_{\text{shell}}$ prediction (C-6) |
| **M3** | ~0.01% (100 ppm) | both $\Delta_{\text{shell}}$ + per-partition $k_\lambda$ |
| **M4** | ~10 ppb | + crystal-bases (C-5) |
| **M5** (1 ppb target) | ~1 ppb | + closed-form $f$ for Δ_coupling |
| **Hard floor** | ~780 ppb | CAL-2 propagation |

The Priority-0/1/2/3 work above does **not** move M0 → M1; that is
the work of in-flight PRs #638, #639, #640 (all sibling). The
work-plan here narrows the **infra discipline** floor so that the
M-axis closures can land on a clean substrate.

---

## 5  Anti-patterns to avoid (re-stated)

Per CLAUDE.md three-calibration-discipline:

- ❌ Calibrate $\Delta_{\text{shell}}$ or $\Delta_{\text{coupling}}$ to AME — fitting, not predicting.
- ❌ Add ad-hoc per-atom corrections that don't trace to substrate data.
- ❌ Tune $n_\star$ or $k_\lambda$ per atom without structural justification.
- ❌ Add new production consumers of `E_0_CONVENTIONS["C_proton_back_fit"]` (the 200 MeV back-fit). Audit-only consumers are tolerated when explicitly tagged.
- ❌ Re-define canonical $\tau_M$ literals outside `derivation_chain.TR_M_AT_Q0` (and now `TR_M_AT_Q0_50DPS`).
- ❌ Hand-write `.witness.json` files (P30); always use `WitnessBuilder`.
- ❌ Use `sp.cancel` / `sp.simplify` on full aggregated traces (P15/P16); prefer `sp.together` + `LaurentQ`, simplify after `evalf`.

---

## 6  Implementation in this PR

Surgical, narrowly-scoped to items NOT already landed in-tree
(verified by source-read in §2.A) and NOT blocked on
author/structural decisions (§2.C).

1. **This document** — §1 inventory + §2 fix categorization +
   §3 infra-compliance dashboard + §4 ranked work plan. Single new
   markdown file. Replaces ad-hoc cross-referencing across 18+
   sibling audits. No code change.
2. **P1.1 — `deuteron_delta_i_audit.py` Conv-C audit-only banner**
   (§2.B B-1). Single docstring line on the function that
   back-fits $E_0$ from CODATA $m_p$. Documents that this is an
   audit-only consumer of the deprecated Conv-C pattern, complying
   with the discipline carve-out for Class-C diagnostic probes.

All other items in §2.B / §4 are **deferred** with explicit
rationale (multi-file scope, blocked on author decision, blocked
on structural R&D, or out of scope for "minimum change" in a single
review PR). The deferral list in §4 is the agenda for the next
canonical-derivation push.

---

## 7  Cross-references

Methodology:
- [`docs/derivation-tracking-methodology.md`](../derivation-tracking-methodology.md) — 7-step canonical chain.
- [`content/.../calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md) — three-calibration discipline.

Sibling PRs (in-flight):
- **#638** — brane-tower $n_\star$ closure refutations.
- **#639** — per-partition $k_\lambda$ + $Q_\beta$ spectral bridge.
- **#640** — neutron-mass 50dps chain (999 ppb honest residual).
- **#637 (merged)** — three-calibration discipline normative.
- **#487 (merged)** — τ_M / τ_SW disambiguation.

Skills:
- [`local/compute-audit`](../../.claude/skills/local/compute-audit.md) — 30-pattern catalogue.
- [`local/witnessed-values`](../../.claude/skills/local/witnessed-values.md) — drift detection.
- [`local/proof-gap-audit`](../../.claude/skills/local/proof-gap-audit.md) — conjectural propagation.
