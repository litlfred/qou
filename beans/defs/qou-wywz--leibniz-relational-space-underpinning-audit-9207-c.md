---
# qou-wywz
title: 'Leibniz Relational Space Underpinning: Audit #9207 Ch.0 Framing & Present Architectural Options to Owner'
status: in-progress
type: task
priority: normal
tags:
    - needs-owner-ok
created_at: 2026-11-23T21:31:07Z
updated_at: 2026-11-24T08:06:18Z
parent: qou-s028
---

Related: qou-u58f, PR #9207. Queued for active analysis (owner override 2026-11-23: ignore 'do not start'). Review how Leibniz relational space underpins QOU across Ch. 0–2 & Ch. 13 (comparing #9207's Ch. 0 trace-radical PII framing against deeper structural options: (1) PII = TL_n(q)/rad(tau_q) & GNS null ideal in Ch. 0 only, (2) relational Reeb/causal step poset & Connes-Rieffel spectral distance d_Connes across Ch. 0 + Ch. 2 + Ch. 13, (3) Barbour-Bertotti / Machian relational configuration quotient contrast without classical phase space). Present full AGENTS.md 6-part AskUserQuestion options to owner before any further math PR.


---
### 2026-11-23 Audit & 4-Option Owner Decision Brief Ready (Worker 30)

- **Branch & commit pushed (no PR opened yet per instruction):** `origin/claude/leibniz-relational-options-audit-20261123` @ `5d6b207b54d`
- **Deliverable:** `docs/audits/2026-11-23-leibniz-relational-space-options.md` (full `AGENTS.md` 6-part cold-reader decision brief + turnkey `AskUserQuestion` chat mirror & JSON payload; zero monograph `.md`/`.ts`/`.lean` or witness edits).
- **Key audit findings on PR #9207 (`b67c7efb137..5a350c1a535`):**
  1. `introduction/intro.md:90-106` (`sec:introduction-overview`) writes `H_n(q)/rad ~= TL_n(q)` without noting `mass-theory/hecke-radical-is-temperley-lieb.md:93-97` (isomorphism not proved in-house), says QOU 'fulfills' Leibniz's programme and 'recovers... metric geometry' without the 4D Lorentzian CR non-claim (`gravity-spacetime/cr-structure-lorentzian-lift.md:13`), and introduces `H_n(q)`/`TL_n(q)` before `sec:introduction-state-space-knots`.
  2. `QOU/InformationTheory/FiniteRieffelQuantumMetric.lean` currently has zero content blocks with `lean.ref` pointing to it (`spacetime-length-distance-layers.ts:9` points to `UnifiedClockScaleLayers.hbarQ_mul_planckTick`), and `gravity-spacetime/lqg-adm-ashtekar-comparison.md:19` lists 'Relational QM' with no citation to Rovelli 1996.
  3. **DOI correction:** `10.1098/rspa.1982.0094` resolves to C. W. Nutt (1982, oil displacement); the live Crossref + `doi.org` Handle-verified (`responseCode = 1`) Barbour–Bertotti (1982) DOI is **`10.1098/rspa.1982.0102`** (*Proc. R. Soc. Lond. A* **382**(1783), 295–306). Rovelli (1996) DOI `10.1007/BF02302261` (`responseCode = 1`) and Earman (1989) MIT Press ISBN `978-0-262-05040-1` also verified.
- **4 Options framed in `docs/audits/2026-11-23-leibniz-relational-space-options.md` §0 (with full What-it-means / Costs / Risks / Commits-to):**
  - **Option 1 (Default if silent):** Keep `#9207` Ch. 0 status quo (`0` files, `0` cost; leaves the 3 Ch. 0 vulnerabilities & uncited RQM row).
  - **Option 2:** Modest Ch. 0 refinement + Earman/Barbour–Bertotti/Rovelli contrasts & 4D Lorentzian non-claim (`intro.{md,ts}` + 3 bib keys; zero Lean/Ch. 2/Ch. 13 edits).
  - **Option 3 (Recommended — judgement):** Cross-chapter spine (Ch. 0 PII -> Ch. 2 `D_nabla` Rieffel Lip-seminorm remark wiring `FiniteRieffelQuantumMetric` -> Ch. 13 CR/LQG relational contrast & `rovelli1996`/`barbour-bertotti1982` citations) + generic-field Lean bridge (`isDualBound_zero_iff_eq` & `finite_dualBound_eq_on_traceRadical`), sequenced after sibling branch `claude/prior-art-doi-verified-pkg-20261123` (`qou-cvu9`).
  - **Option 4:** Relocate Leibniz prose out of Ch. 0 (`intro.md:90-106`) into `information-theory/leibniz-relational-indiscernibility.{md,ts}` beside `rem:spacetime-length-distance-layers`.
- **Blast radius:** Zero numerical/witness/CODATA movement under all 4 options. Waiting on owner card selection (`needs-owner-ok`).
