---
# qou-h59j
title: 'VS-1 (Pipeline): Subdirectory Witness Resolution in liquid-values.ts, :val[...] Markdown Site Rendering, and ValueRegistry Repair'
status: todo
type: task
priority: high
created_at: 2026-11-19T07:06:02Z
updated_at: 2026-11-21T06:50:00Z
parent: qou-v6so
---

## Audit Provenance

Grounded in `computations/audits/paper-status-variable-substitution-and-staleness-audit.witness.json` (`computations/audits/paper_status_variable_substitution_and_staleness_audit.py`), linked to `qou-v6so` and `qou-trd0`.

## Defects Identified by the End-to-End Audit

1. **Flat-directory restriction in `liquid-values.ts` (`../folio-assistant/cat-harness-tools/pipeline/liquid-values.ts`):**
   - `resolveLiquidValues` currently resolves `join(dir, "${entry}.witness.json")` with a segment regex forbidding `/` inside `<entry>`, so witnesses located in subdirectories (`computations/qbeta/`, `computations/probes/`, `computations/deltalambda/`, `computations/audits/`) cannot be addressed via `{{ qou.computations... }}`.
2. **`:val[...]` token leakage in rendered Markdown/site output (`render-markdown.ts`):**
   - `render-markdown.ts` invokes `resolveLiquidValues(mdContent)` ONLY and never calls `renderValue` / `substituteValuesInMath`, whereas the LaTeX renderer (`render-latex.ts`) runs both. Consequently, the `4` `:val[...]` occurrences in `folio/quantum-observable-universe/knots-particles-confinement/proton-from-confinement.md` and `folio/quantum-observable-universe/information-theory/benzene-huckel-categorical.md` leak raw `:val[...]` tokens into rendered Markdown/site pages.
3. **Broken and unaligned entries in `folio/values/registry.ts` (`68` entries across `17` witnesses):**
   - **Broken entry (`1`):** `rho_q` references `computations/q-pinning-50-digit.witness.json` at path `derived_50_digit.rho_q`, which does not exist in `q-pinning-50-digit.witness.json`.
   - **Admitted placeholders (`5` with `needsReview: true`):**
     - `inv_alpha` -> `computations/alpha-em-4pi-fixed-point-solve.witness.json` (`data.CODATA_alpha_inv`, substituting the CODATA input rather than derived $\alpha_{\mathrm{EM}}^{-1}$!)
     - `c_q`, `eta_q`, `chi_q`, `d_H` -> all point to `derived_50_digit.q` in `computations/q-pinning-50-digit.witness.json` as placeholders.
   - **Unused entries (`64 / 68`):** Only `4` of the `68` registered `:val[...]` names are used anywhere in `.md` files (`35 / 3,683` manuscript `.md` files use any dynamic substitution at all: `33` via Liquid `{{ qou... }}` and `2` via `:val[...]`).

## Required Deliverables

1. Update `liquid-values.ts` so `{{ qou.computations.<subdir>.<entry>... }}` (or slash/dot-separated subdirectory paths under `computations/`) resolves witnesses inside `computations/qbeta/`, `computations/probes/`, `computations/deltalambda/`, and `computations/audits/`.
2. Wire `:val[...]` resolution (`substituteValuesInMath` / `renderValue`) into `render-markdown.ts` (or migrate the remaining 2 `.md` files from `:val[...]` to `{{ qou.computations... }}`).
3. Fix `rho_q` and the 5 `needsReview: true` entries (`inv_alpha`, `c_q`, `eta_q`, `chi_q`, `d_H`) in `folio/values/registry.ts` to point to their true derived Wave-2 witness fields.


## 2026-11-20 W13 (#8526, PR #8539)

Deliverables 1+2 are PLATFORM code (cat-harness-tools); patch written + tested (32 pass) and committed as docs/audits/2026-11-20-vs1-liquid-subdir-and-markdown-val.platform.diff — needs landing in the platform repo, then a pin bump. Benzene :val migrated to Liquid (fixed a doubled 'kcal/mol kcal/mol' in the PDF); 1 :val .md remains (confinement table, keys not Liquid-legal). Deliverable 3 (registry): no reader for rho_q/c_q/eta_q/chi_q/d_H; owner ask on #8526. Stays todo.

## 2026-11-21 platform PR opened (session_01VQDpPcnLs1rPy7pJe86d5t)

Deliverables 1+2: the W13 diff is applied as litlfred/cat-harness-tools#2479 (head 8d6f863). It applies cleanly to cat-harness-tools main. Tests ran on the qou-pinned tree with the patch applied: 32/32 on the three touched suites, and pipeline/ 668 pass / 2 fail. The same 2 corpus-index failures occur without the patch. The PR waits for the merge manager.
Pin-bump chain: qou's .folio-assistant-pin and build.yml `uses:` name a folio-assistant sha, not a cat-harness-tools sha. So after #2479 merges, folio-assistant's index.lock.json must re-pin cat-harness-tools past it. Only then can qou bump to that folio-assistant sha. Known break: build.yml `uses:` names publish.yml, which folio-assistant deleted in 0c5468ac46. Deliverable 3 still waits on the owner ask on #8526.
