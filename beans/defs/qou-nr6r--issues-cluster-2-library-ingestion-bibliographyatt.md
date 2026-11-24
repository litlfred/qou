---
# qou-nr6r
title: 'Issues-Cluster-2: Library Ingestion, Bibliography/Attestations & Exposition/Citation Drains (16 Open GitHub Issues)'
status: in-progress
type: task
priority: high
created_at: 2026-11-23T20:55:54Z
updated_at: 2026-11-24T00:59:37Z
parent: qou-xip2
---

Actionable GitHub Issues cluster (`16` open issues on `litlfred/qou`).

### Resolution & Closure Protocol
- Do NOT close any GitHub issue on partial progress (`Part of #...`); only close once 100% of stated deliverables have merged to `origin/main` with exact PR + commit SHA citations.
- **Special Guard on `#9154`:** Do NOT close `#9154` until BOTH Bilson-Thompson–Hackett–Kauffman 2009 `references.ts` registration (`#9157`) AND Chester–Arsiwalla–Kauffman 2025 (`arXiv:2501.03260`) library section ingestion have landed on `origin/main`.

### Open Issues in This Cluster
- **`#9154`**: Ingest two helon/preon papers into the library (Bilson-Thompson–Hackett–Kauffman 2009; Chester–Arsiwalla–Kauffman 2025) *(paired open PRs: #9157, #9095)* — **Note:** BHK 2009 library files landed in #9184, but BHK references.ts registration (#9157) AND Chester-Arsiwalla-Kauffman 2025 (arXiv:2501.03260) library section ingestion remain open!
- **`#9094`**: Add braid-preon and QSP prior art to knots-and-particles intro *(paired open PRs: #9095)*
- **`#8826`**: Drain exposition chapter beans (expo-chapter, wave 1)
- **`#8816`**: Paper structure drain: statement reports, dangling links, notation (wave 1)
- **`#8814`**: Drain citation and library intake beans (qou-1qhv direct items)
- **`#8806`**: Bean drain: interpret citation remarks (P5.CITE, cite-remarks list)
- **`#8803`**: Interpret exposition remarks: P5.EXPO bean drain (qou-aqfj)
- **`#8802`**: Bean drain: cite and cross-check exposition blocks (expo-cite-xcheck, 47 beans)
- **`#8034`**: Braids-and-knots QA findings: owner-ruled statement fixes
- **`#7897`**: Ingest the 15 queued uploads from 2026-11-15 (947381c1, 890d9e21)
- **`#7803`**: Library: re-cut 382 entries that only gain headings
- **`#7539`**: Folio site: 3 rendered-content QA findings on quantum-observable-universe
- **`#7535`**: Bibliography: library-link sync drops valid links; move bib checks into attestations
- **`#7528`**: Bibliography and references migration onto the platform (C9)
- **`#7427`**: uploads/ → library/ ingest pipeline: slug-named folders, Dublin Core records, L1 KG, remote assets, node-level citations
- **`#7298`**: Knot-energy library gap: ingest O'Hara 1991 / Freedman–He–Wang 1994 (blocked on owner upload) — and verify the ohara1991 DOI


## 2026-11-23 Backlog Drain Batch 2 Audit (`claude/backlog-drain-batch2-20261123`)
- **Closed 6/16 genuinely 100%-resolved GitHub issues on `litlfred/qou` with exact file + PR + commit SHA citations:**
  1. **#8034** -> closed citing PR #8035 (`93cc4bbea332b5d920a6b5d283def80f6e199b3c`, all 5 owner-ruled braids-and-knots fixes).
  2. **#7897** -> closed citing PR #7884 (`55dfc921067d334575a41af3c42db429988f5fa2`, all 12 `947381c1` + 3 `890d9e21` + `erlijman-wenzl` library ingests + `folio-assistant#3149` routing).
  3. **#7803** -> closed citing PR #7925 (`a483e4c1498f9aa6c8faa0ce6e9551f6c3a27ebb`, superseding #7805 with 688/736 library re-ingests + section citation remapping).
  4. **#7539** -> closed citing `qou#7540` (`52b90d1be0f015dc11d95c2e7b17eb88f78c5d65`), `folio-assistant#2227` (`9922966dd75a7e9e43420a3ff37685ad60ce4ab9`), and `qou#7544` (`a828a9f03227049535257cc4e1f3dd8e3144bc3a`).
  5. **#7535** -> closed citing `qou#7536` (`58b65541072d9742a44eaa6d410fc61e1d19c526`), `folio-assistant#2232`, and `qou#7544` (`a828a9f03227049535257cc4e1f3dd8e3144bc3a`).
  6. **#7298** -> closed citing `qou#7311` (`58941e013677a2b79bc370681ada23baa6353bb4`), `qou#7315` (`712b506a11`), `qou#7316` (`d2924e6f6b`), and `qou#7299` (`03ed1c3c8e`); also marked mechanical intake bean `qou-6xt9` `completed`.
- **Kept Open & Cross-Linked 10/16 Issues to Tracking Beans (0 partial closures):**
  - **#9154** (GUARDED): `library/arxiv-0903.1376v1` in `1b436f74c26`; open on BHK `references.ts` (#9157) + CAK 2025 `arXiv:2501.03260` (#9095) -> `qou-nr6r`, `qou-sf0s`, `qou-1qhv`.
  - **#9094**: open PR #9095 -> `qou-nr6r`, `qou-mub3`.
  - **#8826**: Wave 1 #8900 (`a683319a7bf`) merged; open child beans -> `qou-mub3` (`qou-1aof`, `qou-cb98`, `qou-cite`, `qou-o001`, `qou-uyud`).
  - **#8816**: Wave 1 #8825 (`eff74b7212b`) merged; open child beans -> `qou-q4oa` (`qou-x78p`).
  - **#8814**: Wave 1 #8818 (`b2ba35b007f`) merged; open child beans -> `qou-1qhv` (`qou-2hc7`, `qou-b5ly`, `qou-qyms`, `qou-sf0s`, `qou-tk1r`).
  - **#8806**: Wave 1 #8828 (`8573752790d`) merged; open items -> `qou-qh3w`, `qou-1qhv`.
  - **#8803**: Wave 1 #8832 (`cf14745ac3b`) merged (27/66); remaining ~39 -> `qou-aqfj`.
  - **#8802**: Waves 1+2 #8883 (`078a6c14bf5`) merged (~40/47); remaining 7 -> `qou-hjnx`, `qou-c9uj`, `qou-1rgm`, `qou-njry`, `qou-udpt`, `qou-jncu`, `qou-xugx`.
  - **#7528**: B1/B2/B3/B4/B5 + rulings 1/2/4 merged; open on B6 (`references.bib` retirement) + T12 -> `qou-8tlx`, `qou-oumk`.
  - **#7427**: Phase 1 (`qou-ehgk`, `qou-l2cr`) completed; open on Phase 2 orphan slugs + `grounds[]` + BPMN -> `qou-ziag`.
