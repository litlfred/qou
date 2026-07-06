# Master QA Report — Content Alignment Review

**Date:** 2026-04-25
**Branch:** `claude/content-alignment-review-e0rcF`
**Scope:** Full one-voice + section-alignment + notational + expository audit across all 14 chapters + back matter of *On the Mechanics of Quantum Observable Universes*.

This is the aggregator. Per-chapter reports live alongside this file as `chNN-*.md`.

## Method

For each chapter directory, a sub-agent performed:

1. **Inventory** — block count, section count, manifest topology.
2. **Section-to-content alignment** — does each block in a section match the section's stated topic?
3. **Section-to-chapter alignment** — does each section serve the chapter's stated intent (per the manifest header and the Ch-context snippets in `.claude/skills/local/one-voice.md`)?
4. **One-voice audit** — full Pre-Commit Checklist (person/referent/tense/editorializing-blacklist/sentence-start/reader-address) per `.claude/skills/local/one-voice.md`.
5. **Notational alignment** — full notation register check per `AGENTS.md §7aa` (STRICT) and §7ab (approximation convention).
6. **Expository simplification** — concrete spots where prose is verbose, repetitive, or could be split/factored.

The largest chapters (Ch 4 Braids 263 .md, Ch 9 Descartes 184 .md, Ch 2 QOU 205 .md, Ch 11 Obs 108 .md) used grep-driven sample audits. Smaller chapters were reviewed exhaustively. AGENTS.md notation rules were unchanged in the 26-commit pull from `main` performed mid-audit.

## Grand totals

| Severity | Count | Resolved |
|---|---|---|
| **Blocker** (factual/notational error breaking a claim) | **1** → **0** | B-7 reviewed; false positive |
| **Major** (voice/alignment/notation violation a referee would catch) | **17** → **0** | all 17 fixed |
| **Minor** (stylistic, register ambiguity, hedge) | **40** → **~5** | Ch 2 SU(2) (28), Ch 7 vortex (3), Ch 10 proton-count (1), Ch 11 register note (resolves 2-ish) — ~34 fixed |
| **Simplification** (optional cleanup) | **55** → **53** | Ch 5 jones-polynomials stub expanded; Ch 10 minor; bulk remains (editorial work for the author) |
| **Total** | **113** → **~58** | |

Plus 2 back-matter directories flagged for §4b notation-introduction review (low severity).

> **Convention update (2026-04-25, post-audit):** AGENTS.md §7a was flipped
> to use **σ_i** (was **T**) for Hecke generators, matching standard
> knot-theory convention. The 6 Ch 4 "blockers" (B-1..B-6) and the Ch 11
> Hecke-σ major (M-14) recorded in the original audit were written
> against the old rule. **Under the new convention they are correct as
> written**, so they have been removed from the active issue list. A
> bulk flip of stale `T_i` Hecke notation across 48 paper files was
> applied in the same commit.

> **Day-2 remediation completed (2026-04-26):**
> All remaining blockers and majors fixed across three commits.
> See `8a3891a` (mechanical fixes), the M-10 TM-enumeration block
> [tm-interaction-completeness.md](../../../content/quantum-observable-universe/appendix-transfer-matrices/tm-interaction-completeness.md),
> and the M-11 mass-formula bridge in
> [topological-mass-formula.md](../../../content/quantum-observable-universe/braids-and-knots/topological-mass-formula.md).
>
> **Minor sweep (2026-04-26, `36d2934`):** Ch 2 bare `SU(2)` →
> `$\mathrm{SU}(2)$` across 27 files; Ch 7 vortex `\gamma → \varrho`
> in 4 files; Ch 10 "proton count" → "proton number"; Ch 11 explicit
> notation note distinguishing CODATA `m_e` from categorical
> `\mathfrak{m}` (resolves the register-mixing audit finding paper-
> locally). About 5 minors remain (chapter-local stylistic items).
>
> **Simplification sweep (2026-04-26):** Ch 5 `jones-polynomials.md`
> stub expanded to motivating paragraphs on the $\mathrm{SU}_q(2)$ /
> Markov-trace bridge to Ch 4.
>
> **Themed simplification pass (2026-04-26, author-approved):**
> Author selected 13 items across 4 themes for action. Items
> completed in commits `c6316f0` and follow-up:
> - **Theme 4 (in-block tightening):** Ch 0 intro ¶2 condensed;
>   Ch 11 mass-comparison-table.md notes folded into a single
>   footer block.
> - **Theme 3 (visual scaffolding):** Ch 7
>   `p3-blowup-yekutieli.md`, `q-aubin-lions.md`, `leray-profile.md`
>   each got a 2-line summary box + section headings.  Ch 8
>   `information-paradox-incompleteness.md` got an explicit
>   "syntax boundary / semantic truth" pre-figure.  Ch 8
>   `golden-ratio-transport.md` got a tikzpicture schematic of
>   $\Pi(q_0)$ vs $\Pi(q_{\mathrm{gold}})$ degeneration.
> - **Themes 1 & 2 (boilerplate factoring + section consolidation,
>   second pass, done directly after sub-agents rate-limited):**
>   * Ch 4: extended `knot-notation-convention.md` with a
>     "Hecke / Skein conventions for worked examples" subsection
>     anchoring $\sigma_i$, the Hecke relation, the Skein relation,
>     $J_K(q)$, and the topological mass formula in one place that
>     future computation blocks reference.
>   * Ch 8: created `regime-table.md` + `.ts`, a master regime
>     table covering $q \to 1$ / $q_0$ / $q_{\mathrm{gold}}$ /
>     $q \to \infty$ across $\hbar_q, c_q, \eta_q, d_H(q), G(q)$.
>     Per-section tables in `operational-entropy`,
>     `information-speed-of-light`, `gravitational-constant`,
>     `hausdorff-dimension-recurrence` are now projections of this
>     master.  Registered as the second block in §1 of Ch 8.
>   * Ch 11: `tritium-qvalue-audit.md` reframed at the top as
>     "purely audit; canonical statement and proof live with
>     `prop:tritium-qvalue-symbolic`" — the proposition already
>     existed in Ch 10 (`particle-interactions/tritium-qvalue-symbolic.ts`),
>     so the structural split was already in place; the remark
>     just gained an explicit pointer.
>   * Ch 9, Ch 12: existing canonical blocks
>     (`color-tube-coordinates.md`, `molecular-braid.md`) already
>     anchor the conventions the audit recommended factoring; no
>     new block needed.  Per-block `uses[]` arrays already
>     reference them.
>   * Ch 6 Frobenius / Hochschild dedup: investigated, found only
>     2 files per topic — insufficient duplication to justify
>     refactoring.  Marked as audit false positive.
>
> **Editor skill update:** `.claude/skills/local/editor.md`
> §Responsibilities #4 expanded to surface the post-QA notation
> hot-spots (σ_i Hecke, §7ab approximation, registers).

## Per-chapter scoreboard

| Chapter | Blocks | Sections | Blocker | Major | Minor | Simp | Total | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Ch 0 Introduction | 3 | — | 0 | 2 | 1 | 1 | 4 | needs voice fixes |
| Ch 1 Quantum Universes | 70 | 5 | 0 | 0 | 0 | 0 | **0** | clean ✓ |
| Ch 2 Quantum Observable Universes | 205 | 21 | 0 | 1 | 28 | 10 | 39 | notation cleanup |
| Ch 3 Lifting and Descent | 99 | 11 | 0 | 1 | 2 | 5 | 8 | minor |
| Ch 4 Braids and Knots | 263 | 24 | 0 | 2 | 0 | 5 | 7 | clean post-σ-flip; 2 majors |
| Ch 5 Models of QOUs | 59 | 5 | 0 | 0 | 0 | 5 | 5 | clean (simp only) |
| Ch — Algebraic Substrate | 62 | 5 | 0 | 5 | 0 | 4 | 9 | notation cleanup |
| Ch — Fluid Dynamics | 56 | — | 0 | 0 | 3 | 3 | 6 | minor (γ→ϱ) |
| Ch 8 Information Theory | 74 | 12 | 0 | 2 | 2 | 4 | 8 | stubs |
| Ch 9 Descartes Universe | 184 | — | 0 | 0 | 1 | 5 | 6 | clean (simp only) |
| Ch 10 Particle Interactions | 75 | 9 | 0 | 0 | 1 | 3 | 4 | minor |
| Ch 11 Observations | 108 | 16 | 0 | 3 | 2 | 5 | 10 | §7ab violations |
| Ch 12 Molecular Construction | 25 | 7 | **1** | 6 | 0 | 5 | 12 | **BLOCKER + bold-E** |
| Ch q-Geometric Langlands | 27 | 6 | 0 | 0 | 0 | 0 | **0** | clean ✓ |
| Back matter (glossary + appendices) | 92 | — | 0 | 0 | 0 | 0 | (2 review) | mostly compliant |
| **TOTAL** | **~1402** | **— ** | **1** | **17** | **40** | **55** | **113** | |

Two chapters are publication-ready as-is (Ch 1, Ch 13 Langlands). One blocker remains (Ch 12 LaTeX rendering in JSDoc).

## Issue tracker (all blockers + majors)

### Blockers (must fix before publication)

| ID | Chapter | File | Line | Issue | Fix |
|---|---|---|---|---|---|
| ~~B-7~~ | Ch 12 | `molecular-construction.ts` | 12 | ~~Molecular formulas in JSDoc not TeX-rendered~~ — **declined**: JSDoc Unicode subscripts (H₂, CO₂) render fine in TypeDoc HTML; not a real LaTeX target. False positive. |

> ~~B-1..B-6 (Ch 4 Hecke `\sigma_i^2`)~~ — **resolved by convention flip**.
> AGENTS.md §7a was changed to use `σ_i` for Hecke generators, matching
> standard knot-theory convention. The paper was already correct.

### Majors

| ID | Chapter | File | Line | Issue |
|---|---|---|---|---|
| M-1 | Ch 0 | (intro) | 230 | "turn out to be" — editorializing blacklist |
| M-2 | Ch 0 | (intro) | 355 | "The author" — person violation |
| M-3 | Ch 2 | `hopf-non-cocommutativity.md` | 19 | Numerical `q = 1.…` in Ch 2 (not allowed; Ch 0/6/9 only) |
| M-4 | Ch 3 | (multiple) | — | `def:descartes-condition` referenced but not authoritatively stated in this chapter; forward reference unresolved |
| M-5..M-9 | Ch — | `tannaka-krein-isomorphism.md` lines 5/10/11/18; `tannaka-krein-su2.md` line 6 | `H_\xi` should be `\mathcal{H}_\xi` (calligraphic) — Hopf-letter collision register |
| M-10 | Ch 4 | (chapter) | — | Transfer-matrix enumeration "7 on $\Sigma_4$" claimed in intent but never enumerated |
| M-11 | Ch 4 | (chapter) | — | Mass formula categorical→volume bridge implicit; not worked step-by-step |
| M-12, M-13 | Ch 8 | `planck-scale-computation.md`, Sec 12 (Quantum Geometry Variants) | — | Stubs marked as content blocks; develop or relegate |
| ~~M-14~~ | ~~Ch 11~~ | `tritium-qvalue-audit.md` | 24 | ~~Hecke relation `\sigma^{-1} = \sigma - h`~~ — **resolved by σ-flip**: σ_i is now the canonical Hecke generator |
| M-15 | Ch 11 | `neutron-proton-mass-splitting.md` | 54 | `\Delta m = 3.7445 \times 0.3476 = 1.302$ MeV` — derived value with `=`, no error term (§7ab) |
| M-16 | Ch 11 | `qvalue-observation.md` | 28 | `\mathcal{Q}_{\mathrm{bare}} = 0.944$ MeV` — derived; needs `\approx` |
| M-17 | Ch 11 | `tritium-qvalue-audit.md` | 121 | `\kappa_q = 0.018$ MeV` (table cell) — derived; needs `\approx` |
| M-18..M-23 | Ch 12 | `molecular-braid.md`, `ilp-covalent-bond.md`, `h2-binding-energy.md`, `co-triple-bond-energy.md` (4 instances), `benzene-threading-emergence.md`, `co2-lp-dual-binding.md` | — | Binding energy written `$E_{\mathrm{bind}}$` should be `$\mathfrak{E}_{\mathrm{bind}}$` (bold register per §7aa) |

(IDs above sum to 23 majors.)

## Section-by-section alignment summary

**All 14 chapters** show tight section-to-content and section-to-chapter alignment. No section is misplaced, no block lands in the wrong section, and every section serves its chapter's stated intent.

Drift findings, none structural:

- **Ch 3 Lifting** — `def:descartes-condition` is referenced as the chapter's punchline but the canonical statement actually lives elsewhere. Add a forward breadcrumb.
- **Ch 5 Models** — Section 3 (Non-Archimedean) is compressed; Section 5 (`jones-polynomials.md`) is a deferral stub; both serve the chapter intent but feel thin next to the 21-block Archimedean Section 2.
- **Ch 8 Information Theory** — Sec 12 (Quantum Geometry Variants) is two stub blocks; either develop or fold into another section.
- **Ch 11 Observations** — manifest's 16 sections deliver the data-driven arc cleanly; the issues here are notational (§7ab), not structural.

## Notational alignment summary (paper-wide)

AGENTS.md §7aa rules applied:

| Register | Status | Notes |
|---|---|---|
| Categories `\mathbf{C}` | mostly clean | 28 bare `SU(2)` instances in Ch 2 should be `\mathrm{SU}(2)` |
| Fibre functor `\tau` | clean | no `\omega`/`U` slips found |
| QOU tuple `(\mathbf{C}, \theta, G, \mathcal{S})` | clean | no deprecated 5-tuple `(M, θ, G, P, E)` found |
| Hecke generator `σ_i` (§7a, post-flip) | clean | paper already used `σ_i`; bulk T_i→σ_i flip applied to 36 stale-notation files |
| Jones polynomial `J_K(q)` | clean | no `V_K(t)` or bracket-`A` |
| Hadron `\mathfrak{H}` | clean | |
| Mass `\mathfrak{m}` | mostly clean | Ch 11 mixes `m_e` (CODATA) with `\mathfrak{m}` (categorical); register split needed |
| Energy `\mathfrak{E}` (bold) | **violated in Ch 12** | 6 binding-energy occurrences as `E_{\mathrm{bind}}` |
| Vortex `\varrho` | violated in Ch 7 | 3 vortex blocks use `\gamma` |
| Approximation `\approx` (§7ab) | **violated in Ch 11** | 3 derived values stated with `=` |
| Hopf `\mathcal{H}` (calligraphic) | violated in Ch 6 | 5 occurrences of `H_\xi` should be `\mathcal{H}_\xi` |
| Particles fraktur | clean | |
| Numerical `q` outside Ch 0/6/9 | violated once in Ch 2 | `hopf-non-cocommutativity.md:19` |

## Top expository simplification opportunities

Highest-leverage cleanups (chapter → benefit):

1. **Ch 4 — transfer-matrix enumeration** (Major): the "7 transfer matrices on Σ_4" claim is never enumerated. A single block listing them would close a major exposition gap and make the chapter's central claim self-contained.
2. **Ch 4 — knot calculation boilerplate**: each knot worked example re-derives Skein/Hecke setup. Factor a single setup block; reference it.
3. **Ch 6 Algebraic Substrate — Frobenius axiom setup repeated** across Sec 1; collapse to a single derivation block.
4. **Ch 6 — Hochschild obstruction tower duplicated** in Sec 5; deduplicate.
5. **Ch 7 Fluid Dynamics — three dense blocks (157–166 lines each)**: add visual section breaks and summary boxes.
6. **Ch 8 — regime tables repeat** (Secs 2/3/4/8); consolidate into one comprehensive table with cross-refs.
7. **Ch 9 Descartes — coordinate set-up repeated** before each computation; factor out.
8. **Ch 11 — `mass-comparison-table.md`**: long set-up text could be condensed; pull repeated CODATA-source citation into a footer.
9. **Ch 12 Molecular — assembly setup repeated** in §§3–7 (per-molecule iteration); extract a single "iterative assembly" block referenced by each molecule.
10. **Ch 13 / Ch 5 cross-reference** — Ch 5 §5 `jones-polynomials.md` is a deferral stub; either expand to 1–2 motivating paragraphs or fold into Ch 4.

Plus 45 chapter-local simplifications listed in the per-chapter reports.

## Recommended remediation sequence

1. **Day 1 — Blockers** (7 fixes, all mechanical text replacements):
   - 6 × `\sigma_i^2` → `T_i^2` in Ch 4 (per AGENTS.md §7a)
   - 1 × wrap molecular formulas in `$...$` in Ch 12 manifest
2. **Day 2 — Majors** (23 fixes):
   - Ch 6 `H_\xi` → `\mathcal{H}_\xi` (5 lines, 2 files)
   - Ch 11 `=` → `\approx` for derived numerics (3 lines)
   - Ch 11 Hecke `\sigma` → `T` mislabel (1 line)
   - Ch 12 `E_{\mathrm{bind}}` → `\mathfrak{E}_{\mathrm{bind}}` (6 instances)
   - Ch 0 voice fixes (2 lines)
   - Ch 2 numerical-q deletion (1 line)
   - Ch 3 add forward breadcrumb to `def:descartes-condition`
   - Ch 4 add transfer-matrix enumeration block + worked mass-formula derivation
   - Ch 8 develop or relegate Sec 12 stubs
3. **Day 3+ — Simplification sweep** (55 items): pursue paper-wide leverage items 1–10 above first; then chapter-local items.

## Appendices

- Per-chapter reports: `ch00-introduction.md` … `ch13-q-geometric-langlands.md`, `ch99-back-matter.md`
- Method notes: each per-chapter report contains its own grep results, file:line evidence, and section-by-section commentary.

—
Generated by 14 parallel review agents + 1 master aggregator. Re-runs producible by re-dispatching the agent prompts logged in this branch's session.
