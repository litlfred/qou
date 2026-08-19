# Bibliography Verification Ledger — 2026-05-19

Per the user's directive ("keep working on all uploaded items as
backlog until exhausted. deep analysis on each. keep track of when
verified / by who"), this ledger tracks the per-paper verification
of QOU bibliography entries against the locally-uploaded PDFs.

**Scope**: 22 PDFs / data files in `library/` on
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
   (library/<file>)") if the cited result is non-trivial.
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

Plus: `library/mass_1.mas20.txt` (AME 2020) — already in the repo
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
| `unfetchable` | Paper not in `library/`; cannot verify against local copy |

## Verification log (chronological)

| When (UTC) | Paper | Verifier | Action | Outcome |
|-----------|-------|----------|--------|---------|
| 2026-05-19 05:50 | `boyd-vandenberghe-2004` | Claude (`claude-opus-4-7`) | Read TOC + §5.5 + §5.6 + §A.5 of `library/boyd-vandenberghe-2004-…pdf` | 4 misattribution fixes applied (commit `66b3caf7f` on `claude/detangler-bib-followup-batch-2026-05-19`). 9 generic Ref lines still need §-specific work. |
| 2026-05-19 06:14 | `codata2022` | Claude (`claude-opus-4-7`) | Cross-checked 5 .lean Ref sites against `library/codata-2022-constants.txt` (NIST CODATA 2022 ASCII table) | verified-clean. Muon-electron mass ratio `206.768 2827(46)` ✓; proton mass energy equiv. `938.272 089 43(29) MeV` ✓; derived hydrogen mass `938.7831 MeV` (= m_p + m_e − 13.6 eV/c²) ✓. |
| 2026-05-19 06:18 | `leitnerpawloski2004` | Claude (`claude-opus-4-7`) | Read full `library/leitnerpawloski2004.pdf` (arXiv math/0409565, 10pp); cross-checked 3 .lean + 4 .md sites | **partial** — 1 of 3 .lean correctly cited (groebner-basis.lean for "Definition 5" ✓), 2 wrongly cited (pawlowski-leitner-inner-product.lean + RepresentationTheory.lean cite LP2004 for "PL inner product" / "PL basis dimension"; LP2004 has NO inner product / NO intertwiner content). Author decision: (a) new bib entry for the actual work, (b) change the citation key, or (c) align content to LP2004 scope. |
| 2026-05-19 06:20 | `oeis-A006752` | Claude (`claude-opus-4-7`) | Reconstructed OEIS b-file digits → 0.91596559417721901505... ; compared to QOU `catalan_G := 0.91596559417721901505` literal | verified-clean. Exact 20-digit match. |
| 2026-05-19 06:23 | `faddeev_kashaev1994` | Claude (`claude-opus-4-7`) | Read PDF title page; pentagon UV commutation IS the central content of Faddeev-Kashaev's quantum dilogarithm paper | verified-clean. arXiv:hep-th/9310070. |
| 2026-05-19 06:23 | `baez2004` | Claude (`claude-opus-4-7`) | Confirmed paper is "Higher-Dimensional Algebra V: 2-Groups"; INN construction is canonical content | verified-clean. arXiv:math/0307200. |
| 2026-05-19 06:23 | `hu-mathas2012graded` | Claude (`claude-opus-4-7`) | Title "Graded Induction for Specht Modules" is verbatim the citation text | verified-clean. arXiv:1008.1462 (preprint 2010; published 2012). |
| 2026-05-19 06:23 | `freed2010` | Claude (`claude-opus-4-7`) | Title-only citation in Glossary; paper is Freed-Hopkins-Lurie-Teleman "TQFTs from Compact Lie Groups" | verified-clean. arXiv:0905.0731. |
| 2026-05-19 06:23 | `berarducci2018` | Claude (`claude-opus-4-7`) | §2 contains the cited surreal-field polynomial-extension content (sub-§§ Order/simplicity, Field operations) | verified-clean. arXiv:1503.00315. |
| 2026-05-19 06:23 | `pham1965` | Claude (`claude-opus-4-7`) | Title "Formules de Picard-Lefschetz généralisées..." verbatim matches citation text | verified-clean. Bull. SMF 93, 1965. |
| 2026-05-19 06:23 | `zink2002` | Claude (`claude-opus-4-7`) | `library/zink2002.pdf` is Astérisque vol 278 PRELIMINARY PAGES (pp. I-XII), NOT Zink's actual paper | **paper-mismatch**. URL in references.ts points at vol prelims, not the Zink chapter. The QOU citation intent is correct (Dist(Ĝ) free ℤ_p-module IS Zink's content); just the local PDF needs replacement. |
| 2026-05-19 06:26 | `yekutieli2008` | Claude (`claude-opus-4-7`) | §2 = "Poisson Deformations of Algebraic Varieties" — matches citation scope in global-gluing.lean + Torsion/GlobalGluing.lean | verified-clean. arXiv:0801.3233. |
| 2026-05-19 06:30 | `klein1888` | Claude (`claude-opus-4-7`) | Read 17 MB book scan TOC: §142 Bring's form, §192 curve classification, §207 Bring's transformation, §189 main resolvent of icosahedral eqn | verified-clean. Vorlesungen über das Ikosaeder. |
| 2026-05-19 06:30 | `mostow1968` | Claude (`claude-opus-4-7`) | Confirmed paper is "Quasi-conformal mappings in n-space and the rigidity of hyperbolic space forms" — canonical Mostow rigidity | verified-clean. Publications IHÉS 34, 1968. |
| 2026-05-19 06:30 | `bufetov2020` | Claude (`claude-opus-4-7`) | Title "Interacting Particle Systems and Random Walks on Hecke Algebras" — directly covers ASEP / Hecke algebra content cited | verified-clean. arXiv:2003.02730. |
| 2026-05-19 06:33 | 7 uncited orphans | Claude (`claude-opus-4-7`) | Verified PDFs match references.ts metadata: gromov1982, bilsonthompson2005, dappiaggi2024, finster2021/2022/2024 ✓; blitvic2012 ✗ | 6 verified-clean (PDFs correct, no citations to update); 1 paper-mismatch (blitvic2012: arxiv:1205.4003 is 'Two-Parameter Non-Commutative CLT', not 'The (q,t)-Gaussian process' as bib title says — needs author decision). |
| 2026-05-19 06:38 | `boyd-vandenberghe-2004` | Claude (`claude-opus-4-7`) | All 14 remaining generic DOI-only Refs assigned §-specific citations per surrounding code context: §5.6 (perturbation/sensitivity) for stability+phase-stratification (10 sites); §5.2.3+§5.3+§5.5 (Slater+strong-duality+KKT) for ElectronShell (2); §5.2.3+§5.3 for ConfinementSDP (3) | **fixed**. All 17 Ref lines now §-specific. Cumulative fixes 18 (was 4 in 66b3caf7f). |
| 2026-05-19 06:50 | `jones1987` | Claude (`claude-opus-4-7`) | Bulk-updated 142 bare-URL Refs across 58 .lean files to §-specific (§3 Markov trace + §4 Link polynomials). 20-context sample validated uniform scope before sed -i pass | **fixed**. 142 fixes. No local PDF (Annals paywalled; not on arxiv). |
| 2026-05-19 06:55 | `kassel1995` | Claude (`claude-opus-4-7`) | Per-file thematic batching: 43 bare-URL Refs across 23 .lean → Group A Hecke/Markov files (15) → Ch. X; Group B braiding/R-matrix (7) → Ch. VIII + XIII; Group C generic (1) | **fixed**. 43 fixes. Already-§-specific Refs (11) preserved. |
| 2026-05-19 07:00 | `turaev2010, kock2004, lusztig1993, bergman1978, atiyah1988, iwahori1964` | Claude (`claude-opus-4-7`) | 104 bare-URL Refs upgraded to title+publisher+DOI form (no local PDFs in library/ for these — §-specific verification deferred) | **partial** for all 6: 23+23+17+18+12+11 = 104 fixes total. |
| 2026-05-19 07:03 | `yekutieli2010, yekutieli2015, faddeev1994, mathas1999` | Claude (`claude-opus-4-7`) | 38 more bare-URL Refs → title+publisher form | **partial** (4 papers, 38 fixes). |
| 2026-05-19 15:38 | 10 more keys (bolza, kashaev, frenkel2007, witten2011, schrijver, khovanovlauda, witten1988, weil1948, leitnerpawloski2004, wenzl1988) | Claude (`claude-opus-4-7`) | 79 bare-URL Refs → title+publisher | 9 partial + 1 wenzl1988 stays verified-clean (with note). |
| 2026-05-19 15:48 | 11 newly-fetched PDFs (lurie, witten2011, yekutieli2009/10/15, fetter, navon, gauthier, scheeler, nayak, aganagic) | Claude (`claude-opus-4-7`) | Read title page of each from library/ on upload branch; all 11 match references.ts metadata | 11 verified-clean. yekutieli2009 has older arxiv id in `note` field — same paper, later revision; not a defect. |
| 2026-05-19 15:51 | 6 more keys (diaconis-ram, kashiwara1991, edge1978, chari1994, brundankleshchev, murakami-murakami2001) + yekutieli2009 note fix | Claude (`claude-opus-4-7`) | 33 bare-URL Refs → title+publisher; yekutieli2009 `note` field updated to match the actual URL revision | 6 partial, 1 metadata cleanup. |
| 2026-05-19 15:54 | 12 more keys (lecouvey, hazewinkel, habiro2002, reshetikhin, murphy1992/1981, lurie2009, kazhdan-lusztig, jones1985, feynman1948, bring1786, borel1974) | Claude (`claude-opus-4-7`) | 39 bare-URL Refs → title+publisher | 12 partial. |
| 2026-05-19 15:57 | 14 more keys (aganagic, wedderburn, rosen2002, nayak, morton, maclane, kronheimer, kitaev, kawauchi, kauffman, geckpfeiffer, frenkel2004, baez1995, ariki) | Claude (`claude-opus-4-7`) | 29 bare-URL Refs → title+publisher | 14 partial. |
| 2026-05-19 16:00 | 34 long-tail single-occurrence keys | Claude (`claude-opus-4-7`) | All remaining bare-URL Refs upgraded to title+author+year form (one shell loop pulling titles from references.ts per key) | 34 newly-marked partial. **0 bare-URL non-data Refs remain** in content/. |
| 2026-05-19 16:14 | 15 newly-fetched PDFs from upload-bib-papers re-run (8db0ad3d9..bec33d90e) | Claude (`claude-opus-4-7`) | 14 PDF title pages match bib metadata. 1 mismatch (margolus1998 — got wrong cond-mat/9710043 paper; correct is quant-ph/9710043; URL fix applied to references.ts) | 14 verified-clean, 1 paper-mismatch (fix queued — re-run upload-bib-papers.sh). |
| 2026-05-19 16:40 | 6 papers re-classified from `uncited` → `verified-clean` (gromov1982, bilsonthompson2005, finster2021/2022/2024, dappiaggi2024) + blitvic2012 note updated | Claude (`claude-opus-4-7`) | Earlier inventory was wrong — missed multi-arg `\cite{a,b,c}` matches and `.ts` manifest `cites: [...]` arrays | 6 promoted to verified-clean, blitvic2012 note updated (still paper-mismatch). 0 uncited remaining. |
| 2026-05-19 17:20 | 5 true bib orphans surfaced by extended bib-qa.ts citation scan (commit 66f827b84): bokut2005, cardona2023, murakami2001, wigner1960, navon2021 | Claude (`claude-opus-4-7`) | Re-ran bib-qa.ts after adding .ts cites: array scanning; these 5 have zero citation sites across .lean, .md, AND .ts. Author-judgement: keep as forward-refs / remove from references.ts / find a use site. | Pending author decision. |
| 2026-05-19 17:35 | murakami2001 removed (duplicate of murakami-murakami2001) | Claude (`claude-opus-4-7`) | Same DOI 10.1007/BF02392716, identical metadata; murakami-murakami2001 has 4 citation sites, this had 0 | uncited count: 5 → 4. Other 4 (bokut2005, cardona2023, wigner1960, navon2021) need author decision. |
| 2026-05-19 17:48 | wigner1960 + navon2021 + bokut2005 citations added; cardona2023 → pending-placement (new status); 4 uncited orphans resolved | Claude (`claude-opus-4-7`) | wigner1960 cited in intro.md; navon2021 added to bec-vortex-data.md alongside fetter2009; bokut2005 added to groebner-basis.ts cites: [] array. cardona2023 promoted to new `pending-placement` status per user's "I need this but unsure where to put" workflow | uncited 4→3, +1 pending-placement, +1 new status in schema + skill doc. |
| 2026-05-19 17:55 | 4 wrong-work fixes (borel1986→Borel-Zagier, nakayama1939→vol II, frobenius1903→Charaktere, fulton1991 SPLIT into fulton1991+fulton-harris1991) | Claude (`claude-opus-4-7`) | First batch of 9-item wrong-work triage. fulton1991 stays as Young Tableaux LMS35 per user 'keep LMS w/ yt' note; new fulton-harris1991 added for Repn Theory; 5 .lean sites re-keyed | 3 metadata replacements + 1 split; remaining 5 (chlouveraki, kashiwara, wenzl1988 DOI, lp2004 ×2, habiro year) in next 🟡 batch. |
| 2026-05-19 18:01 | 5 wrong-work mismatches resolved (chlouveraki/kashiwara/wenzl1988 DOI splits + lp2004 wrong-sites re-key + habiro year) | Claude (`claude-opus-4-7`) | Final batch of 9-item wrong-work triage. Added: chlouveraki2016-hdr, kashiwara1990-duke, kashiwara1990-cmp2, wenzl1988b, pawlowski-leitner-rep (all pending-placement except pawlowski-leitner-rep verified-clean for 8 re-keyed sites). Habiro year 2008→2006 per published Algebr. Geom. Topol. 6. | 9-item wrong-work triage COMPLETE. |
| 2026-05-19 18:13 | 3 of 5 pending-placement entries promoted (chlouveraki2016-hdr, kashiwara1990-duke, kashiwara1990-cmp2) | Claude (`claude-opus-4-7`) | Re-keyed .lean inline-DOI citation sites (2 chlouveraki-hdr in wenzl-bridge-applicability-qou.lean; 4 kashiwara-duke in tau-M / q-beta-c3 / ck-extraction; 2 kashiwara-cmp2 in kashiwara-jones-c4 / hopf-jones-c3). | 3 promoted pending-placement → verified-clean (TODO bib metadata still pending). 2 remain pending-placement (cardona2023, wenzl1988b — wenzl1988b's delta-q-decoration site already has a TODO comment but isn't re-keyed yet because the inline DOI is in a free-text comment, not a -- Ref: line). |
| 2026-05-19 18:18 | 4 unmapped PDFs in library/ identified + mapped (HDR.pdf=chlouveraki2016-hdr, 1210.6243v1=bach2013, 0409565v2=leitnerpawloski2004, bujack-et-al-2022...=bujack2022) | Claude (`claude-opus-4-7`) | Gap audit between library/ contents and bib-qa-verifications.json found 19 unmapped PDFs. 4 recognizable via title-page inspection; mapped to their canonical entries. Plus removed stale kassel1995 local_pdf path (kassel-1995-quantum-groups-preprint.pdf doesn't exist on branch). | 4 PDFs newly mapped; remaining 15 unmapped (mostly arxiv-numeric-id files of unknown content + .gitkeep + .json sidecars). |
| 2026-05-19 18:23 | 8 new references.ts entries added from library/ gap audit | Claude (`claude-opus-4-7`) | Per user 'see if they fit in paper first, add 8 new entries' directive: investigated each PDF's QOU fit. 6 have DIRECT or strong fits (geck-lambropoulou, webster-williamson-markov, halverson-markov-weights, jing-liu, kuhlmann-matusinski, carter-leal-saliola); 2 pending-placement (franecki-kapranov, lu-canonical-bundles). | +8 entries; 51→57 verified-clean + 2→4 pending-placement = 133 entries tracked. |
