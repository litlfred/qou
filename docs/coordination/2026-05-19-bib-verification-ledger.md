# Bibliography Verification Ledger — 2026-05-19

Per the user's directive ("keep working on all uploaded items as
backlog until exhausted. deep analysis on each. keep track of when
verified / by who"), this ledger tracks the per-paper verification
of QOU bibliography entries against the locally-uploaded PDFs.

**Scope**: 22 PDFs / data files in `uploads/` on
`claude/upload-bib-papers-2026-05-19` (intake from
`scripts/upload-bib-papers.sh` per
`scripts/bib-papers-list.txt`).

**Authoritative status data** (machine-queryable): see
[`content/bib-qa-verifications.json`](../../content/bib-qa-verifications.json).
Loaded by `content/pipeline/bib-qa.ts` and surfaced as QA tag #7
(`verification_status`) in the standard `bib-qa.json` report
consumed by `folio-assistant/ui/bib-qa.html`. The JSON file is
the source of truth for per-paper `status`, `verified_at`,
`verified_by`, `fixes_applied`, `fix_commit`. The tables below
are a human-readable mirror; when they disagree, **the JSON data
wins**. Update the JSON first, then refresh this markdown.

**Verifier**: Claude (Anthropic AI assistant) — model
`claude-opus-4-7`, working in the Claude Code on the web web
environment for repo `litlfred/qou`.

**Verification protocol** (per paper):

1. Extract PDF from `origin/claude/upload-bib-papers-2026-05-19`
   to `/tmp/<id>.pdf` via `git show`.
2. Read TOC + identify subsections via `pdftotext -layout`.
3. For each citation site in QOU (`-- Ref: [<id>]` in `.lean`
   files or `\cite{<id>}` in `.md` files), verify that the cited
   section/theorem/page exists in the paper AND covers the
   claimed result.
4. Update the QOU `-- Ref:` description with the specific
   verified `§ N.M` or `Theorem N.M` reference, plus a
   verification note ("Verified against the local PDF
   (uploads/<file>)") if the cited result is non-trivial.
5. Record the outcome in this ledger (verified-clean,
   misattribution-fixed, paper-doesn't-contain-claim, etc.).

## Per-paper status

| # | Paper | Sites | Status | Notes | Commit |
|---|-------|------:|--------|-------|--------|
| 1 | `boyd-vandenberghe-2004` | 11 .lean (17 Ref lines) | **partial** — 4 misattributions fixed | §5.5.3→§5.5.2 (typo), §5.5.4→§5.5.2+alizadeh (wrong subsection), Thm 5.5→§5.2.3+§5.3 (non-existent number), §A.5.3→§A.5.5 (wrong topic). 9 generic Ref lines remain (DOI-only, need §-specific updates). | `66b3caf7f` |
| 2 | `codata2022` | 5 .lean | pending | NIST constants — values lookups, not theorem citations. Verification = value match against the data table. | — |
| 3 | `leitnerpawloski2004` | 3 .lean + 4 .md | pending | Formal groups paper (UGB chapter). | — |
| 4 | `yekutieli2008` | 2 .lean + 2 .md | pending | Twisted deformation quantization. | — |
| 5 | `zink2002` | 1 .lean + 1 .md | pending | Display of formal p-divisible group. | — |
| 6 | `freed2010` | 1 .lean + 1 .md | pending | Topological QFTs from compact Lie groups. | — |
| 7 | `berarducci2018` | 1 .lean | pending | Surreal numbers, derivations and transseries. | — |
| 8 | `faddeev_kashaev1994` | 1 .lean | pending | Quantum dilogarithm. | — |
| 9 | `baez2004` | 1 .lean | pending | Higher-dimensional algebra V: 2-groups. | — |
| 10 | `hu-mathas2012graded` | 1 .lean | pending | Graded induction for Specht modules. | — |
| 11 | `klein1888` | 1 .lean + 1 .md | pending | Vorlesungen über das Ikosaeder. 17 MB scan. | — |
| 12 | `pham1965` | 1 .lean | pending | Picard-Lefschetz formulas. | — |
| 13 | `oeis-A006752` | 1 .lean | pending | Catalan's constant. Numeric data; verify value. | — |
| 14 | `mostow1968` | 0 .lean + 2 .md | pending | Quasi-conformal mappings + rigidity of hyperbolic. | — |
| 15 | `bufetov2020` | 0 .lean + 1 .md | pending | Random walks on Hecke algebras. | — |
| 16 | `gromov1982` | 0 .lean + 0 .md | **uncited** | Bib entry orphan; in references.ts but never cited. Decision pending: keep / remove / find use. | — |
| 17 | `bilsonthompson2005` | 0 .lean + 0 .md | **uncited** | Topological preon model. Decision pending. | — |
| 18 | `finster2021` | 0 .lean + 0 .md | **uncited** | Causal fermion systems — wave functions. Decision pending. | — |
| 19 | `finster2022` | 0 .lean + 0 .md | **uncited** | Causal fermion systems — baryogenesis. Decision pending. | — |
| 20 | `finster2024` | 0 .lean + 0 .md | **uncited** | Causal fermion systems — collapse theory. Decision pending. | — |
| 21 | `dappiaggi2024` | 0 .lean + 0 .md | **uncited** | Holographic mixing + Fock dynamics of causal fermion systems. Decision pending. | — |
| 22 | `blitvic2012` | 0 .lean + 0 .md | **uncited** | The (q,t)-Gaussian process. Decision pending. | — |

Plus: `uploads/mass_1.mas20.txt` (AME 2020) — already in the repo
from an earlier intake; verifies CODATA mass values used in QOU's
mass-formula predictions. Status: **assumed verified** by the
existing canonical-derivation pipeline (`canonical_mass_table.py`,
PR #781) which round-trips against this exact file.

## Status keys

| Key | Meaning |
|-----|---------|
| `pending` | Not yet examined |
| `verified-clean` | Every citation site checked; descriptions match paper content; no fix needed |
| `partial` | Some citations verified + fixed; others still need work |
| `fixed` | Misattributions resolved; ready to PR |
| `uncited` | Paper is in `references.ts` but has zero `-- Ref:` / `\cite` consumer; awaits author decision (keep/remove/find-use) |
| `paper-mismatch` | The local PDF does not match the metadata in `references.ts` (different work) — escalate to user |
| `unfetchable` | Paper not in `uploads/`; cannot verify against local copy |

## Verification log (chronological)

| When (UTC) | Paper | Verifier | Action | Outcome |
|-----------|-------|----------|--------|---------|
| 2026-05-19 05:50 | `boyd-vandenberghe-2004` | Claude (`claude-opus-4-7`) | Read TOC + §5.5 + §5.6 + §A.5 of `uploads/boyd-vandenberghe-2004-…pdf` | 4 misattribution fixes applied (commit `66b3caf7f` on `claude/detangler-bib-followup-batch-2026-05-19`). 9 generic Ref lines still need §-specific work. |
| 2026-05-19 06:14 | `codata2022` | Claude (`claude-opus-4-7`) | Cross-checked 5 .lean Ref sites against `uploads/codata-2022-constants.txt` (NIST CODATA 2022 ASCII table) | verified-clean. Muon-electron mass ratio `206.768 2827(46)` ✓; proton mass energy equiv. `938.272 089 43(29) MeV` ✓; derived hydrogen mass `938.7831 MeV` (= m_p + m_e − 13.6 eV/c²) ✓. |
