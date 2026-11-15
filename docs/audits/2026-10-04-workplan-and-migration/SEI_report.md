# SEI: SM / Exposition / Infra slices (P4, P5, P6)

Scope: the 507 open beans with slice ∈ {SM, EXPO, INFRA} [M]. Every one has a row in `SEI_mapping.tsv`, which adds the columns `home`, `fa_class`, `orig_slice`, `status` and `title`. The work was read-only, and nothing proposed here edits any math or physics content.

**The keyword pre-split is unreliable.** 63 of the 507 beans belong outside P4–P6 [M]: 35 go to P1, 14 to P2 and 14 to P3. Examples: the colour-tube and 2H-interface binding beans carry the SM slice only because their titles say "colour", and JM commutativity, ArgPrinciple and the hook-length formula carry EXPO. Another 14 go to MIGRATE-CONTENT, which belongs to the MIG analyst; I only mapped them.

Totals by action [M]: reparent 444, close-evidence 23, dup-of 23, needs-owner 8, scrap 3, promote-epic 3, keep 3.

## Proposed tree

**P4 SM / eightfold.** The epic is `qou-8lxd`; its body is empty, but it is already the parent of the T-series.
- S1 colour SU(3) / the 3-dimensional fibre. Use `qou-8p1x` as the story-epic; its scoreboard body is the best statement of the gap. It takes ni4b, 1gix, pa2f, lxh5, 5iaz, 17gn, 8pl1/8p1e/8p1c/8pl3, the colour-cubic beans (ozyt, z03j, vhv6, swqq, an6y, d8de), the G2 leg (uq5x, ctzi) and the owner decision j3w6. 28 beans.
- S2 flavour Cartan / eightfold organisation. Use `qou-20sx`; it is tagged L2 but its subject is flavour. It takes d7h1, the G1-opt1..4 beans, y7vg, eo5q, kl39 and the hypercharge cites.
- S3 SM 26-parameter gap ledger. NEW. It takes the per-parameter GAP beans (CKM, PMNS, v, m_b/m_t, m_tau, m_u/m_d, sin²θ_W).
- S4 three generations. Use `qou-7opd` (T6). It takes xtcl, fk8s, x4qm, skgn and h0zz.
- S5 hadrons / lattice QCD. Use `qou-qpj9` for the meson flux tube, with the G2-opt children k4l2 and 886m. jsx5 and 1puy go here too.
- S6 chapter architecture. Use `qou-vwu9` and its six Phase children. These have been untouched since 2026-08-04, and their paths predate the move from content/ to folio/ (qou-yqko) [M]. Owner: is the 3-chapter plan still wanted?

**P5 Exposition & paper.** NEW epic.
- S1 Milnor drain: `mlnr` (zkzs, fu2h, z1bb).
- S2 one-voice, clarity and trap drain (vbjg, ritv, ujp8, cldt, bni2, d93c…).
- S3 bibliography and references (qou-cite, p3ay, refk, 40kk, 78gl, msc1, w5oq…).
- S4 library intake (b9c3, k1hs, 6xt9, y8kx, hs0c, b6ti, 7t9z, z9f9, zwtc, m1tr…). The sessions `qou-m6sp` and `qou-l2cr` become logs.
- S5 relevance-triage citation drain. NEW. It holds 114 auto-raised beans titled "Cite / Remark interpreting / Cross-check / Apply X at Y", created 2026-08-08 and stale-lined 2026-08-21 [M]. `qou-vslz` becomes a log.
- S6 figures, tables and render QA (i229, iars, df74, os3o, jbbk, 4b6g, rc1i, zdz5).
- S7 chapter structure and running examples (expo, zq1r, j3m4, fwr10/fwr11).

**P6 Platform, tooling & hygiene.** NEW epic. Per the owner's steer it is split by home:
- S1 bean tracker hygiene: `qou-w3yy` (63fo, 2cyi, bstl, y48h, 7sin, og83, fs4r). This reorganisation is its main deliverable.
- S2 witness and producer integrity, qou-only, 147 beans. NEW story with sub-stories:
  - q0Anchor stamping (23)
  - vacuous assertions (9)
  - producerless witnesses (11)
  - provenance fields (5)
  - chi caches (6)
  - LP/SDP duals (6)
  - environment reproducibility (6)
  - WitnessBuilder write path (7)
  - staleness sweeps (26)
  - non-completing producers (3)
  - misc (24)
  The existing epic `qou-v6so` ("WITNESS: substitution/alignment") is a candidate parent, but it is narrower. My recommendation is a NEW "Witness integrity" epic with v6so as one story.
- S3 Lean build cache (52i4, 8jfi, z9bx, lb0f).
- S4 CI, PRs and merge policy for qou, plus the watchers (gwe9, 0hu2, wu80, z8x9, prop3b, the Integration:* beans).
- S5 platform asks owned by folio-assistant (23 beans; see the section below).

## Duplicate clusters

| survivor | merge into it | confidence | basis |
|---|---|---|---|
| qou-6irj | xm91, kx04, ca7s | m/l | all are the witnesses-with-no-q0Anchor population; 6irj names the cause, `wrap_legacy` never stamps |
| qou-26f2 | ploj | h | both are self-comparing assertions; 266 is a superset of 9 |
| qou-7aum | 2r42, w9s3 | h/m | both are the provenance-completeness audit, red at 55 and wired into no gate |
| qou-cdvx | 9ta3, dgpe | m | both are the producerless witness population |
| qou-7tr2 | 30vo, 569e | m | both are the import-cone staleness audit |
| qou-pg2r | m90h | m | the same `_EPHEMERAL_META_FIELDS` fix, for durationSec and ms |
| qou-p30w | 1j39, cmiy | m | the P30 raw-write class |
| qou-2cyi | yw40 | h | the same 13 broken parents (0yqu, krvm) |
| qou-gwe9 | tgus | m | AGENTS.md rule 10 gates are stale |
| qou-h72x | o4zh | m | both hold the same three sin²θ_W numbers |
| qou-8lxd | 40hy | h | 40hy has an empty body |
| qou-mn2t | q5nm | m | the agent-speak criterion |
| f-a folio-assistant-1r0p / -d5f1 | qou-8lgg / qou-mnho | h | the platform bean has the identical or near-identical title |

Two more duplicate patterns:
- **Brief candidates.** `qou-1qug` and `qou-ggdk` are both session cheat-sheet logs, so I demoted both to logs rather than merging them. ggdk's body says all six of its task beans were completed. `qou-ty42` versus `qou-n4r9`: n4r9 states in its own body that it supersedes ty42 as the forward plan. ty42's title, "pin stays df28d02", is now false, because the pin is cb194b1 [M, `.folio-assistant-pin`]. ty42 is not in my slice (it is tagged L2), so it goes to MIG. `miga` is completed.
- **Cite/Remark pairs.** 7 of 111 targets carry both a Cite bean and a Remark bean with identical bodies [M]. Keep both, because they ask for different deliverables, but they should land in one PR.

## Watcher-queue JSON files in `beans/defs/`

There are 12 files [M]. None of them is a bean, and the `beans` CLI ignores `.json`. Their item states:

| file | items | state |
|---|---|---|
| canonical | 4 | all wontfix |
| compute-integration | 65 | 63 wontfix, 2 resolved |
| detangler | 54 | all wontfix |
| proof-integration | 49 | all resolved |
| devils-advocate | 46 | all needs-author |
| qa-agent-drain | 33 | all pending |
| lean-discharge | 14 | 2 open |
| research-queue | 13 | 4 open |
| 1ppq-qbeta | 6 | 2 blocked, 1 in progress |
| paper-todos | 8 | |
| simulator-qa | 2 | |
| status-section-audit | 1 | |

- 191 items cite `content/quantum-observable-universe/…` paths, which are stale since content/ moved to folio/ [M]. All `reviewed_up_to` shas are the same two commits.
- **Do they duplicate beans?** Partly. The four `Integration:*` beans (trmo, yjxk, 1j39, ns57) restate queue finding classes whose items are wontfix or resolved, so I marked them dup-of-queue. Only 16 queue items cite any bean id at all [M], so the queues and the beans are otherwise unlinked.
- **Recommendation:** move the queues out of `beans/defs/`, because they are watcher state rather than work-plan items. Turn the open items into beans only where they are actionable: the devils-advocate items (46 needs-author), lean-discharge (2), research-queue (4) and 1ppq-qbeta (2 blocked). That is an owner call, because it moves files.

## Work that has landed but whose bean is still open (23 close-evidence)

- **qou-utbr:** the commit "qou-utbr: .beans/ -> beans/defs/ + beans/beans.json" is on main, `.beans/` is gone, and the residual skill-path edits are in **PR #7484**, which is unmerged.
- **qou-sm2c and qou-w02s:** qou.json and qou.config.json exist, and the feedbackDir fix is at qou.config.json:11-12. `folio.config.json` still exists; PR #7484 deletes it. qou-yf1y stays in progress until #7484 merges.
- **qou-29i6:** harness.json and harness.config.json are gone [M].
- **qou-x3be:** the key is already in its target block [M]. Ten more relevance-triage beans outside my slices also have their key present: jdxo, 91qi, o6x4, 0otg, jps5, 26ew, hkaq, uoge, 09yi, akg0.
- **qou-ed8a:** the diagnosis is recorded. It still needs a green lake build on main confirmed before closing.
- **qou-7br7, 83g1, cq2n, f9th:** each one's title is its own retraction.
- **Platform landed:** z9bx, lb0f, keu7, 4w5b, grph, 969b, f4el, h8i0, ntb2, ddo8, ehgk, mn2t. These are listed in the next section.

## Stalled claims

89 of the 91 in-progress beans in scope have had no update since 2026-09-20 [M]. "In progress" no longer carries information here. By area: P6 36, P1 20, P2 10, P5 9, P4 8, P3 6. Examples include mlnr (2026-07-06), w5tg (06-23), 60iz (06-26), qou-52i4 (08-15) and every SM in-progress bean.

**Proposal:** reset them all to todo, keeping a holder note, as one bulk hygiene step. This is mechanical and decided by date, but it needs the owner's approval.

## Platform beans: home and class (owner steer)

Of the 507, 39 are platform-touching [M]. 37 are filed `home=fa:<instance>` and 2 stay `home=qou` with a platform class (qou-p3ay, qou-prop3b).

- **fa-landed (13)**, all cat-harness:
  - lake-cache trace and gutted-cache detection: `cat-harness/scripts/lake-cache.sh` (count_traces, own_oleans_expected) closes z9bx and lb0f.
  - retry-backoff.md plus `src/core/retry.ts` closes 4w5b.
  - bean-coordination.md:398 (checkout -B) closes keu7.
  - review-heatmap.md:75 (uses-graph hash) closes grph.
  - qa-checkers-extended.ts:1939-2012 (multi-paper) closes 969b.
  - bib-verification.ts:222 (relevance in the ledger) closes f4el.
  - tabular-metadata.md, asset-extraction.md, document-intake.md (sha256) and filing-dublin-core.md close h8i0, ntb2, ddo8 and ehgk.
  - the voice-agent-speak criterion closes mn2t and q5nm.
- **fa-open (11).** The f-a homes are:
  - folio-assistant-1r0p ← qou-8lgg
  - folio-assistant-d5f1 ← qou-mnho
  - margin-marker render criterion (k8q6)
  - refs-prose-mentions criterion (noj1)
  - relevance UI card (172h)
  - sibling-assumption detector (sibdup)
  - stale-summary detector (3wc5)
  - migrate-uploads keying (cvx9)
  - beans CLI slug drift (uoad; the beans CLI is third-party, hmans/beans)

  These two belong in **folio-assistant-sci**:
  - `checkBaseRingMinimal` is math-specific but lives in cat-harness (mfps).
  - MATH_BLOCK_KINDS ownership (7ko6; mapped to MIG).
- **fa-superseded (2, folio-assistant-sci):** 52i4 and 8jfi, which seed the old lake-cache branch. The f-a script measured that very cache as trace-gutted (775 traces / 7268 oleans), and the lake-cache family is moving to sci (f-a bean folio-assistant-9io2).
- **qou-adoption (20).**
  - z8x9: qa-sweep is now a folio_init template.
  - gwe9 and tgus: adopt f-a's prepare-merge.
  - p3ay: no export-bibtex caller.
  - supr: the qa-reports branch.
  - u0qy, 6cm9, prop3b: re-measure at pin cb194b1.
  - The migration beans go to MIG.

## Owner decisions needed

1. **Stalled claims.** Bulk-reset the 89 stalled in-progress beans to todo?
2. **Watcher queues.** Move the 12 queue JSONs out of `beans/defs/`, and promote which open items to beans?
3. **Eightfold chapters.** Is qou-vwu9's 3-chapter architecture still the plan?
4. **qou-6nd0.** Adjudicate the 57 C→D witness value changes (sign flips first). This is a values call.
5. **qou-99qc.** The Δ prose and epsNPq disagree, so one of them is wrong.
6. **Placeholders.** qou-0mty ("Bean ether for later"), wpvo ("Evaluate blocks 6-10") and qou-ybls need saying what they meant, or scrapping.
7. **Other.** j3w6 (condition 5, the eightfold fundamental) and hfiw (Model G timing) were already marked owner-gated.

## Where empirical claims risk entering formal ones

- **qou-h72x / o4zh:** sin²θ_W at "0.127 % best-of-74" is a search-selected numerical match. Track it as empirical and never as a proposition.
- **qou-fth5:** "117 manuscript physics claims" is parented under qou-vkmt (Mathlib class-field debt). Empirical claims should not count as Lean debt; reparent it.
- **qou-1puy:** lattice QCD. Its own title says "EMPIRICAL-tier cross-check until DERIVED". Keep the empirical cross-check out of the Lean target statement.
- **qou-0gbx:** the (1+ℏ_q³) factor is posited, not derived. It must not be cited as derived.
- **qou-4e5k:** the prose says three tr_M paths agree to machine ε, but two witnesses differ by 1.4e-4. The author must restate it; an agent should not.
- **qou-xtcl:** the T(2,9) exclusion is a formal lemma. Its reading as "the three generations" is an identification and should stay separate from the theorem.
- **tqcp:** θ_QCD < 10⁻¹⁰ is tied to a ColorSectorCPEven instance. Confirm that the bound is not baked into the class.

## Open PRs in my areas (from open_prs.txt)

- **MIG:** #7484, #7453, #7451, #7494.
- **P5:** #7146 (library ingest), #5861 (barrett1993 citation).
- **P6.**
  - P6.S1: #7170 (bstl READ QUEUE drained; qou-bstl is still todo, so close it on merge) and #7392.
  - P6.S2: #7318 (float64 producers), #6025 (joint-tower witness truncation), #6878 (vacuity witness refresh), #6307 (symbolic perf), #7482 and #7477 (precision-gate triage).
  - P6.S4: #5330 and #4845 (stale-PR triage drafts, which overlap qou-0hu2), #7435 and #7402.

## Skill gaps

1. **Bean ↔ PR ↔ commit landing check.** There is no tool that says "a commit naming this bean id is on main, but the bean is open". I grepped `main_subjects.txt` by hand. This is the f-a `bean-coordination` §"Closing a bean whose work has already landed" applied as a sweep, and qou-bstl asks for exactly this.
2. **Duplicate detection.** Clusters were found by reading titles. A title/body similarity pass across the store would have found 6irj/xm91/kx04 mechanically, and f-a has `LSI` near-pair work.
3. **Platform-landed lookup.** There is no index from a qou capability ask to the f-a skill or file that answers it, so every check was a grep across cat-harness.
4. **Relevance-triage beans have no "landed" check.** A Cite bean could verify its own key in its target block; I scripted this (`sei_work/sei_citecheck.py`).
5. **Slice keywords.** The pre-split misfiled about 12 % of the beans in my slices (63 of 507). A bean-classification skill should use the parent chain and the files the body references, not title keywords.
