# Stalled sessions (week of 2026-10-05) → four work streams

Consolidates ~14 session transcripts that stopped on usage limits or on an
unanswered owner question. PR state checked against GitHub on 2026-10-12.

**Already merged (do not redo):** #7686, #7700, #7706 (KZ associator, hexagon,
pentagon), #7708, #7715, #7719 (n-point KZ holonomy), #7721, #7729 (cross-level
Markov), #7731 (REV upper bound K₂), #7732 (Rosso–Jones, coprime torus knots);
cat-harness #156, cat-harness-tools #134.

**Asked to merge, still open:** #7726 (Wigner / C_λ) — owner said "merge 7726".

---

## Stream 1 — Coordinator + infrastructure (this session)

Non-math plumbing, cross-repo, and the merge queue.

| item | state | next action |
|---|---|---|
| #7726 Wigner | owner said merge | `/prepare-merge`, rebase-merge |
| #7698 m7py bean note | waiting "merge" | merge with #7728 or alone |
| Lean docs KG viewer (folio-assistant-sci #21, cache branch `lake-cache/qou-docgen4-v4-24-0`) | owner asked: explain option 2, prefers compatibility with Lean SOPs over avoiding breakage | write the explanation; propose keeping doc-gen4's URL scheme (`lean/QOU/…/X.html` stubs that redirect into the viewer) |
| Library: #7608 (draft), cat-harness-tools #169 | Q1 = **B** (file 3 methodology papers in folio-assistant-sci); Q2 = **A** (re-ingest all qou/library when math-aware tools land) | file the 3 papers to folio-assistant-sci; close/trim #7608; queue re-ingest behind tools |
| Library follow-ups 1–5 (owner picked all) | not started | dry run for split labels; run-in headings >120 chars (`3C1`); 12 schema failures; regen candidates/summary for 4 re-cut papers; `retiredCopy` → fsh-guts + 2 hash mismatches |
| #7586 dead labels (qou-3kni) | group B pending owner (5 citations); ofri relay: atom-word provenance audit + R3 finding | write `docs/audits/2026-10-11-atom-word-provenance.md`, cross-link qou-99qc/vls6/kj4v/brng/9f4h; record R3 rests on a false "IS derived" docstring (do NOT change R3) |
| #7734 qou-egqr | open, non-draft | review & drive to green |
| #7588 / #7583 lean-cache + taxonomy row | open since 10-10 | rebase, merge-ready check |

## Stream 2 — Quantum groups / Drinfeld–Kohno / skein (Lean)

Goal: full-Mathlib proof of KZ ≅ Jimbo for 𝔤𝔩₂/𝔰𝔩₂, no citations left
load-bearing (owner: "start with citation, but also mathlib needed").

| item | state | next |
|---|---|---|
| #7673 Drinfeld–Kohno at q₀ | open; flatness n=3, 2-strand Hecke quadratic, TL dim = Catalan, rigidity lemma proved | gaps: Hecke quadratic n≥3 (local monodromy), Wedderburn split continuous in q, base point ≠ coupling 0 |
| KZ Step 2: dim_q V = [2]_q | started on new branch, unpushed? | ribbon-category curl identities → (q−q⁻¹)dim_q V = a−a⁻¹; bean the "D_ℏ is ribbon" gap |
| #7705 oriented skein OS(z,t) | universal property + strong uniqueness proved; owner picked "Go to the trace", then "dispatch B" (n-dim GL_n vector rep model) | build K^n with Hecke R-matrix as a nondegenerate datum |
| qou-q425 Rosso–Jones | owner order: torus links (gcd>1) → Schur–Weyl trace split → W_{r,j} | two provers were running; check branches, verify, merge |

## Stream 3 — Braid-word selection (γγ, quarks, chirality)

Goal: derive the nucleon / atom words instead of choosing them (qou-ales,
qou-99qc, reading 3 at every level).

| item | state | next |
|---|---|---|
| #7733 γγ climbing n | rigid-shift top closure: no admissible placement ≤ 9 strands | owner asked: (a) a clearer physical + mathematical explanation of the result; (b) bottom closure, and the *other* closure in the corpus — compare all three |
| #7702 qou-ales H₃→H₆→H₉ | open | fold in #7733 result |
| #7718 quark template | open; **quark sign question waiting on owner** | re-frame the question with the six-part frame |
| #7712 qou-h0zz / qou-wqto chirality | Reeb candidate `reebM_x² = −id` proved | grep whether gen-1 state set ↔ Bring cone are connected (transport vs CR geometry) |

## Stream 4 — Binding traces, certificates, bounds

| item | state | next |
|---|---|---|
| qou-5zl1 trace factorisation | Lean agent relaunched; uncommitted `MarkovBondLetter.lean` | 4 steps: tower instance via `heckeIncl` + T2, bond-letter law, disjoint-block multiplicativity, factorisation; reuse IsMarkov n=2,3,4 from #7729 |
| #7612 bond-letter (qou-slz5) | open | land with/under 5zl1 |
| qou-uir6 Ω₂ vs D7 | **owner decision pending** (i/ii/iii; rec. ii+iii) | ruled (ii)+(iii) 2026-10-12: report full-window scan as the result; relabel D numbers as a two-row diagnostic; keep beans open |
| #7728 certificates + tower trace to A=16 | owner picked 1+2+3 | Rust/MPFR port (19F, 20Ne); write `tr_markov_d` from tower probe; Yang–Baxter structure for A=40; note f_pauli truncation-knob finding |
| #7579 Xbot complement (qou-as81) | green, rebased | merge on owner go; then qou-r9a6 (ingest Murota vs prove L♮ criterion) |
| qou-fxym REV lower bound | owner said "go" after #7731 | prove M_n ≥ A√(2n) − O(1) |

---

## Owner decisions still open (one place)

1. ~~**Ω₂ reconciliation (qou-uir6)**~~ — **RULED 2026-10-12: (ii)+(iii)**; relayed to stream 4; beans stay open.
2. **Quark sign (#7718)** — stream 3.
3. ~~**Dead-label group B (#7586)**~~ — **RULED 2026-10-12: point at removal commits**; already done on the branch (`da68fa0a32`, audit 0 dead).
4. ~~**KG viewer publish path**~~ — **RULED 2026-10-12: B** — publish at `gh-pages/STAGING/lean/` (owner: "clean cut to.. STAGING/lean"), no doc-gen4 compatibility stubs (old `lean/…` links will break at the eventual swap). Static `lean/` untouched. Note: this publishes to `gh-pages` despite the 2026-09-27 deprecation ruling in AGENTS.md; the owner picked B with that conflict on the table.
5. **wedderburn-weight-canonical status / qou-ng7j vocabulary** — stream 1.
