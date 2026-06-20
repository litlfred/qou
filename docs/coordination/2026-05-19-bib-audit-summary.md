# Bibliography Audit Summary — 2026-05-19

End-of-day summary of the bibliography verification + cleanup work on
`claude/detangler-bib-followup-batch-2026-05-19` (branch tip:
`b35a8565e`, 43 commits).

## Headline numbers

| Metric | Count |
|---|--:|
| Total refs in `content/schema/references.ts` | 246 |
| Local PDFs in `uploads/` (on `claude/upload-bib-papers-2026-05-19`) | 38 |
| Verification entries in `content/bib-qa-verifications.json` | 117 (48% of refs tracked) |
| `-- Ref:` lines upgraded from bare URL to specific citation | 654 |
| `validate-bib --cross-check` warnings | 12 (was 149 at start) |

### Verification status distribution

| Status | Count | Meaning |
|---|--:|---|
| `verified-clean` | 37 | Every citation site checked against PDF; no fix needed |
| `fixed` | 3 | boyd (18 §-fixes), jones1987 (142 § + scope), kassel1995 (43 thematic Ch) |
| `partial` | 67 | Title+publisher upgrade; awaiting PDF for full §-verification |
| `paper-mismatch` | 3 | zink2002 (vol prelims not chapter), blitvic2012 (wrong arxiv id), margolus1998 (wrong category prefix — fix queued) |
| `uncited` | 6 | Bib orphans: gromov, bilsonthompson, finster2021/2022/2024, dappiaggi |
| `pending` | 1 | Auto-default for entries not yet examined |

## Infrastructure added

| Path | Purpose |
|---|---|
| `content/bib-qa-verifications.json` | Hand-curated per-paper verification status (the typed sidecar) |
| `content/pipeline/validate-bib.ts` | 5-mode bib correctness audit (--doi / --cross-check / --crossref / --arxiv / --pandoc / --all / --strict) |
| `scripts/gen-bib-papers-list.py` | Scan `references.ts` → `bib-papers-list.txt` for batch intake |
| `scripts/bib-papers-list.txt` | Generated intake list (51 entries currently) |
| `scripts/upload-bib-papers.sh` | Batch download + per-paper commit + SSH push + optional `--pr` |
| `scripts/upload-to-uploads.sh` | Single-file ad-hoc intake |
| `scripts/find-arxiv-mirrors.py` | Deeper search: query arxiv.org for each DOI-only entry, suggest URL field |

## Existing infrastructure updated

| Path | Change |
|---|---|
| `content/pipeline/bib-qa.ts` | +2 QA tags (`has_local_pdf`, `verification_status`); score 0-5 → 0-7 |
| `content/pipeline/export-bibtex.ts` | Emits BibTeX `annotation =` field from verification status |
| `.claude/skills/local/bib-qa.md` | 169 → 380 lines: verification workflow, arxiv mirror check, paper-mismatch class, PDF/HTML rendering of status |
| `.claude/skills/local/editor.md` | New "Bibliography workflow" section pointing at tools |
| `.claude/skills/local/integration-watcher.md` | New §0c (sibling coord), §0d (multiSelect+🟡), §0b (5-min idle trigger) |
| `AGENTS.md` | New rules: multiSelect/🟡 for AskUserQuestion, sibling coord at workplan start, structured branch names, 5-min idle trigger with backlog priority order |
| `.gitignore` | Whitelist `uploads/*` for intake files (was blocked by `*.pdf` global rule) |

## Rendered-bibliography verification marker

After this branch, every `references.ts` entry with a row in
`content/bib-qa-verifications.json` gets a `annotation =` field in
`references.bib` showing its verification status. Example:

```bibtex
@book{boyd-vandenberghe-2004,
  author     = {Boyd, Stephen and Vandenberghe, Lieven},
  title      = {{Convex Optimization}},
  year       = {2004},
  publisher  = {Cambridge University Press},
  annotation = {[Verified+Fixed] 18 fixes by Claude (claude-opus-4-7) 2026-05-19},
}
```

Status symbols: `[Verified]`, `[Verified+Fixed]`, `[Partial]`,
`[Pending]`, `[Uncited]`, `[Paper-Mismatch]`, `[Unfetchable]`.

Rendering targets:
- **LaTeX** — biblatex's `\printfield[brackets]{annotation}` formatter,
  or natbib's `\bibliographystyle{plainnat-annote}` style.
- **HTML** — pandoc citeproc with a CSL template that includes the
  `annote` field (most academic CSL styles do).
- **bib-qa.html dashboard** — already surfaces the full `verification`
  object on each `bib-qa.json` entry.

## Deferred to author judgement

Items the agent surfaced but didn't auto-resolve because they need a
human decision:

### Wrong-work mismatches (Copilot-flagged + agent-found)

| Ref id | Issue | Resolution paths |
|---|---|---|
| `borel1986` | Lean cites Borel-Zagier; entry is Borel-Wallach | (a) replace entry with Borel-Zagier; (b) split into `borel-zagier1986` + `borel-wallach1980` |
| `nakayama1939` | Lean cites "On Frobenius algebras II" vol 42; entry has "I" vol 40 | Replace entry with II (vol 42) or split into a/b |
| `frobenius1903` | Lean cites "Über die Charaktere…" (Crelle); entry has "Theorie der hyperkomplexen…" (Sitzungsb.) | Replace entry metadata |
| `fulton1991` | Lean cites "Representation Theory: A First Course"; entry has "Young Tableaux" | Replace entry metadata |
| `chlouveraki2016` | Lean cites HDR Theorem 6.20; entry has the 2009 LNM monograph | Cite HDR or update lean citations |
| `kashiwara1990` | 3 different DOIs across citation sites; entry resolves to a third | Split into 2-3 keys |
| `wenzl1988` DOI | Sites cite `10.1007/BF01393839`; entry has `10.1007/BF01404457` | Reconcile (different Wenzl 1988 papers) |
| `leitnerpawloski2004` (2 of 3 sites) | Cite "PL inner product" / "PL basis dimension"; entry is "Unital Gröbner Bases" | (a) add new bib entry for the actual cited work, or (b) update the QOU citation key |
| `habiro2002` year | Bib `issued` = 2008; PDF published 2006 | Cosmetic; can leave |

### Uncited orphans (PDFs verified-correct but no QOU citations)

`gromov1982`, `bilsonthompson2005`, `finster2021/2022/2024`,
`dappiaggi2024` — each has a correct PDF in uploads/ and verified
bib metadata, but no `-- Ref:` or `\cite{}` consumer in content/.
Decision pending: keep as forward-ref / remove / find a use site.

### Repeatable misfetches

| Ref id | Symptom | Fix path |
|---|---|---|
| `zink2002` | uploads/zink2002.pdf is the Astérisque volume PRELIMINARY PAGES, not Zink's chapter | Update `references.ts` URL to the chapter's `/item/AST_2002__278__<startpage>_0.pdf` (need volume TOC consultation) |
| `blitvic2012` | arXiv:1205.4003 is "Two-Parameter Non-Commutative CLT" not "The (q,t)-Gaussian process" | Decide whether bib title or URL is wrong |
| `margolus1998` | URL fix queued in commit `87b9771ac` (cond-mat → quant-ph); re-fetch needed | `rm uploads/margolus1998.pdf && bash scripts/upload-bib-papers.sh` |
| `heisenberg1958`, `weil1948` | archive.org `/download/<id>/<id>.pdf` guess pattern returned 401/503 | Need `archive.org/metadata/<id>` lookup to find real filename |
| `turaev2010` | URL `q-alg/9409028` returned 404 on user's last run — may be wrong category | Verify the actual arxiv id (maybe `q-alg/9409025` or different) |

## Sibling coordination during this work

Per the new AGENTS.md sibling-coord rule (commit `eb716c725`), the
following sibling-PR overlaps were observed but not actively
coordinated (sibling agents working on disjoint scopes):

| Sibling PR | Scope | Overlap with this branch |
|---|---|---|
| #779, #780, #782, #787, #788, #789, #790, #792 (merged) | Various detangler / I12-I14 audit / d2a-followup | None — all touched disjoint files |
| #797 (atlas move) | Recursive-atom-knot-atlas relocation | Touched some of the same appendix files but no actual conflict |
| #800-815+ (I1 probe wires, qbeta-followup, co-casimir) | Probe-wire conjectures, c_k closed forms | None |

No critical findings on this branch warranted a sibling-PR
comment per the "make too much noise" qualifier.

## Recovery commands (for the user's machine)

```bash
# Pull the latest bib branch
git checkout claude/detangler-bib-followup-batch-2026-05-19 && git pull

# Re-fetch the corrected margolus paper
rm -f uploads/margolus1998.pdf
bash scripts/upload-bib-papers.sh

# Regen references.bib + bib-qa.json with current verification status
cd content
bun run export-bibtex
bun run pipeline/bib-qa.ts
cd ..

# Run the full validate-bib audit (network required; --cross-check works offline)
cd content && bun run validate-bib --all --strict || true
cd ..

# Find more arxiv mirrors for the remaining 188 candidates
python3 scripts/find-arxiv-mirrors.py --min-cites 3
```

## Next-batch backlog

1. **Re-run arxiv-mirror search** with the v2 resilient script
   (commit `f3dce18a0`) to find 40-75 more papers; apply URLs to
   references.ts; re-run upload to fetch.
2. **Triage the 9 deferred wrong-work items** above — each needs the
   author to pick a resolution path.
3. **Triage the 6 uncited orphans** — keep / remove / find use.
4. **The 12 remaining `validate-bib --cross-check` warnings** —
   mostly author-judgement items already deferred.
5. **PR**: open one for `claude/detangler-bib-followup-batch-2026-05-19`
   when ready (43 commits, all rebase-clean and validator-clean).

## 2026-05-20 follow-up sweep (post-merge cleanup)

After resolving the merge from `origin/main` (commit `60c9f9f42`),
a follow-up tranche of bib + infrastructure cleanup landed on the
same branch. Capstone status:

| Metric (2026-05-20) | Value |
|---|--:|
| Total refs in `references.ts` | 252 (was 246) |
| Verification entries tracked | 134 (was 117 → 48% → 53% of refs) |
| `validate-bib --cross-check` | **0 / 0 / 0** (was 12 warn) |
| `validate.ts` issues | **0** (was 5 stale) |
| `validate-refs` errors / warnings | **0 / 0** (was 3 / 10 post-merge) |
| `validate-refs` info items | 14 (was 36; rest deferred) |
| Conjectural-propagation violators | **0** (1728 blocks, 9/9 banner) |
| Dangling remarks | **0** |
| Glossary | regenerated, 29 entries |

### Commits added post-merge (10)

1. `36627d399` — fix kazhdan-lusztig prefix
2. `d4f274bae` — clear 5 validate.ts cross-ref + val-block warnings
3. `672dc65d1` — clear 3 broken cite keys (khovanov × 3) + 10 missing
   container-title warnings (arxiv preprints → `type: "article"`)
4. `37c6d09b1` — extend `validate-references.ts` to scan `.ts` cites
   arrays + `.lean` docstring bracket citations (closes the gap that
   misclassified 16 wired entries as orphans)
5. `20737a05a` — sync 88 missing cite keys across 58 manifests
   (mechanical .md `\cite{}` → `.ts cites[]` sync)
6. `a1d28f502` — multi-witness for deuterium-derived-binding (clears
   the last val-block-computation warning)
7. `6671bb083` — surface cardona2023 + blitvic2012-clt into existing
   prose (4 → 2 uncited orphans; remaining 2 are genuinely
   pending-placement)
8. `5c9cd28cf` — regenerate stale glossary.json
9. `695fb6406` — refresh conjectural-propagation + conditional-class
   banner audit witnesses

### Truly remaining backlog (defer-to-author)

- **2 uncited orphans**: `franecki-kapranov-1999`, `lu-1999-canonical-bundles`
  — no QOU citation site after full-tree grep. Sit in references.ts as
  future-work candidates; remove or surface when intent clarifies.
- **12 entries lacking DOI**: `suslin1991`, `bring1786`, `collatz1937`,
  `iwahori1964`, `young1901`, `mostow1968`, `gromov1982`, `kerov1996`,
  `pham1965`, `borel1986`, `frobenius1903`, `nakayama1939` — Crossref
  API blocked in sandbox; DOIs deferred until author or external
  network access available.
- **67 `partial` entries**: paywalled, no PDF for §-specific verification.
- **1077 / 1893 blocks lacking QA sidecar** (one-voice / fit /
  framework / wall criteria, new in PR #821). Bulk-generate via
  `qa-sweep.ts` in a separate dedicated session — too large for
  this tranche.
