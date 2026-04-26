# Chapter 11 — Observations (Physical Predictions) — QA Report

**Review Date:** 2026-04-25
**Chapter Directory:** `content/quantum-observable-universe/observations/`
**Coverage:** 108 .md, ~21 .lean (grep-driven audit)

## Inventory

108 .md files, 16 sections.

## Section-to-content alignment

Sections cover (per manifest): $q$-estimation from muon/electron, hadron-mass predictions, half-lives via transfer matrices, hydrocarbon energetics, double-slit (Bach 2013 overlay), nuclear stability, CMB, fine-structure, Q-values, proposed experiments. Topics align with section titles.

## Section-to-chapter alignment

Intent (single $q$ → all observables) verified across the manifest's 16 sections.

## §7ab Approximation-convention audit (HIGHEST PRIORITY)

Total `\approx`-style usages: **167** (correct).

Concrete `=` violations (derived QOU values stated with `=`, no error term):

| Path | Line | Offender | Note |
|---|---|---|---|
| `neutron-proton-mass-splitting.md` | 54 | `\Delta m = 3.7445 \times 0.3476 = 1.302 \;\mathrm{MeV}` | Derived value; should be `\approx 1.302` |
| `qvalue-observation.md` | 28 | `\mathcal{Q}_{\mathrm{bare}} = 0.944 \mathrm{MeV}` | Derived; needs `\approx` |
| `tritium-qvalue-audit.md` | 121 | `\kappa_q = 0.018 \mathrm{MeV}` (table cell) | Derived; needs `\approx` |

CODATA reference values (`m_e = 0.51099895$ MeV (CODATA 2022)`, `\Delta m = 1.2934$ MeV CODATA) are inputs/citations, where `=` is acceptable.

## One-voice violations

Grep for editorializing blacklist (`surprisingly|remarkably|notably|interestingly|elegant|beautiful|in remarkable agreement|to remarkable precision`): **0 matches**. Clean voice.

## Notational alignment

| Pattern | Hits | Status |
|---|---|---|
| `V_K(t)` / `J_K(t)` / `J_K(A)` Jones-poly variable error | 0 | ✓ |
| Hecke relation written with $\sigma$ | 1 in `tritium-qvalue-audit.md:24` (table calls $\sigma^{-1}=\sigma-h$ "Hecke relation"; should use $T$) | ✗ |
| Plain `$m_p, m_n, m_e$` | many — context-dependent: when used as CODATA reference these are acceptable; when used as QOU-derived categorical mass they should be `\mathfrak{m}` | mixed |
| `\mathcal{C}` / `\mathfrak{E}` violations | 0 | ✓ |
| Numerical `$q$` values | present (allowed in Ch 11 per voice spec) | ✓ |

Notes:
- `bw-mass-decomposition-dictionary.md:31`, `color-superconductivity-borromean.md:126`, `mass-comparison-table.md:85` — `$m_e$, $m_p$` are CODATA inputs; OK.
- `fine-structure-observation.md:84`, `mass-formula-validation.md:7,12,13,16`, `hadron-half-life-verification.md:16` — using `$m_e$` as the "external scaling ruler". OK in physics convention; if the author wants strict register compliance, switch to `$\mathfrak{m}_e$` for the categorical electron mass and reserve `$m_e$` for the CODATA value alone.

## Comparison-table audit

Tables generally include error bounds (e.g. `Error: 0.63%`, `+73%`). No "n significant figures" claim found without numerical justification.

## Expository simplification opportunities

1. **`mass-comparison-table.md`** — long table set-up text could be condensed; pull repeated CODATA-source citation into a footer.
2. **`tritium-qvalue-audit.md`** — combines audit narrative with summary table; split into a proposition (statement) + remark (audit walk-through).
3. **`feynman-qou-comparison.md`** — repeats `q_0, m_e` description; reference the `mass-formula-validation.md` ruler block instead of re-stating.
4. **`qvalue-observation.md`** — bare/exp/QOU comparison could use a single 3-row table instead of three sentences.
5. **`double-slit-analytical.md`** — opening prose narrates what the figure shows; let the figure caption carry that load.

## Issue tally

| Severity | Count |
|---|---|
| Blocker | 0 |
| Major (Hecke `\sigma` mislabel; 3 `=` violations on derived numerics) | 4 |
| Minor (plain-$m$ register ambiguity; CODATA-vs-derived mixing) | 2 |
| Simplification | 5 |
| **Total** | **11** |
