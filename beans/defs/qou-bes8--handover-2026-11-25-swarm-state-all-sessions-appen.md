---
# qou-bes8
title: 'Handover 2026-11-25: swarm state (all sessions append here)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T16:25:07Z
updated_at: 2026-11-25T16:38:07Z
---

Owner, 2026-11-25, verbatim: "all handovefr notes should go into common .md (bean) all agents work on for their session (that should also be part of process)" and "your token use for the week is getting low, there are skills for handover, please make sure you and siblings start preparing".

ONE common handover ledger for the 2026-11-25 swarm. Every session appends ONE section with: session id + role; process/task; done (PRs/beans); in flight (branch, head sha, PR); next step; blockers; route to resume cold. Append with beans update <id> --body-append, then push with branch-store.ts push --id beans; on conflict re-read and retry.

## coordinator (session_01EucfRmMzrEARLFNgZfhwsQ)
- Site: #9396 (platform layer, Documents landing) merged ae92875; #9433 KG node regen merged 9686001; publish-main-local --deploy from 9686001 running in scratchpad qou-layer worktree (QA page pushed a9a583cd).
- Pins (owner consent): folio-assistant-sci 78f3321 (#222+#221), folio-assistant-core e2beef4 (#874+#875), cat-harness-tools 5593bb6. Re-pin to merge commits when #221/#222/#874/#875 merge.
- Open for owner: cat-harness#1405 merge (handoff envelope); Zenodo GitHub toggle (2a) then first release.
- Background agent: KG-node pre-merge gate PR (in flight).
- Children: photon session_01EucfRopy82qV7K5FpozNB9; holography session_01EucfRpmx5vQ5s5BZrP4uTV (#9428); q-NS session_01EucfRp1HyniH3qQb1YGVWb (qou-0nqs); BPMN process session_01EucfRqJQewHVJR2mVqcuaB (folio-assistant-sci); compute session_01EucfRmFaPKg5KbjjmxSBwx; merge manager session_01EucfRm2khmNLbMgiuTA6UZ (grant to 22:00Z).


### compute/derivation child — session_01EucfRmFaPKg5KbjjmxSBwx (stability epic qou-s028), 2026-11-25T16:3xZ
MERGED today: #9409 #9414 (LR fix + consumer), #9411 (interactive-sibling process), #9416/#9417/#9418 (probe-d attribution, withdrawal, ruling), #9421 (probe-d cone on the log law, scoped to the superseded letter), #9423 (Lean QOU.Nuclear.LogFormUniqueness: continuous extensive binding = -c log r).
OPEN: #9426 draft (gamma-gamma deuteron probes; Phase A 408/422 admissible bonds, B -0.16..7.67 MeV; card-1 selection V(2)^3 gives 0.0063 MeV = -99.7 %; head 963c58bc0b4 + Phase B child pushes). #9420 draft (a-K LP-dual face, analysis). #9424 (sibling; ruled tower E0, head f1c5d61dbbf5, merge main first).
BEANS: qou-xj4p (deuteron, open: binding unexplained), qou-fu8c (intervals delegated), qou-63be (new: Chmutov-Lando mutant check, not started), qou-of4i (sibling).
CHILDREN: session_01EucfRmaNiqxRg52fQZeNVB (Phase B + card 2), session_01EucfRq7fzfsm3Q1DZg9UTS (LP intervals, card 3), session_01EucfRqaU3YESdx7nHnDgpD (E0, done), session_01EucfRntKGFoPCof8huHo3z (deep binding-error budget).
OWNER CARDS 2026-11-25 recorded in owner-rulings.md on #9426: (1) bond scope decided after table, then 'go' = pure-junction cheapest; (2) p vs n: A+B+D; (3) LP duals as intervals; (4) ruled tower E0.
NEXT: qou-63be (cheap grep); collect child results; flip #9426 ready once Phase B is in.


### deuteron-overshoot child — session_01EucfRqaU3YESdx7nHnDgpD (bean qou-of4i, epic qou-s028), 2026-11-25T16:30Z
PR #9424 draft, branch claude/deuteron-overshoot-loci-2026-11-25, head f1c5d61dbbf5, pushed, tree clean, 68 behind main (merge main first; possible conflicts on the binding-log-free-energy and probe-d witnesses).
DONE: both loci measured. The +27.4 % is on the superseded letter; on the gg word the deuteron is unbound (qou-brng). Lean UniversalScaleMinimax (one-scale floor) and BondScaleUniversality (trace-only => one scale), lean-direct exit 0. Owner card 4 'ruled tower E0' applied: E0 4.227483, 2H +28.62 %. Precision gates NEW 0.
OPEN: owner decision on the 4 other order-zero log-law probes (framed on qou-of4i). qou-of4i stays open (Rule 13a).


## 2026-11-25 holography / q-NS research child (session_01EucfRpmx5vQ5s5BZrP4uTV)
- role: research child under the coordinator (session_01EucfRmMzrEARLFNgZfhwsQ). PRs: litlfred/qou#9428 (draft) and litlfred/qou-private#2.
- task: essay review (holography / q-NS) with library intake and incorporation; DEC probe qou-k5jb; generalisation routes 1-6.
- done:
  - 11 papers ingested: PDFs and full text in qou-private#2, metadata in public qou.
  - exact Bring {5,4} probe: Betti (1,8,1); dim ker Delta_1 = 8; gaps 2 and 5-sqrt5; Z2 code [[60,8]] with systoles 6/4.
  - sorry-free Lean obstructions.
  - audit with verdicts and the 14-paper usability table.
  - paper remark rem:tv-rt-string-net-root-of-unity-only.
  - DEC probe: exact checks E1-E5 pass; pure coexact data transfers energy into the 8 harmonic modes.
- in flight: final DEC probe run, with a dt-halving convergence check on the energy identity, then the witness commit.
- next: routes qou-mqfl, qou-0lqx, qou-xg15, qou-zwz6, qou-7k15, qou-wm01; then qou-sscx.
- blockers: owner to rule whether sections/ and candidates.json are derived KG (public) or full text (private). The 20 PDFs on public main wait for the coordinator's go.
- route: Lean via lean-direct -DautoImplicit=false; exact or mpmath only; PDFs to qou-private.

## Photon research child — session_01EucfRopy82qV7K5FpozNB9 (2026-11-25)
- **Role:** research child, research swarm front (photon / Hecke / Bring). Coordinator session_01EucfRmMzrEARLFNgZfhwsQ; merge manager session_01EucfRm2khmNLbMgiuTA6UZ.
- **Done:** PRs #9415, #9427, #9430, #9431, all merged. Owner ruling 2026-11-25 'Term-by-term, same scope as now' recorded; the Borromean photon weights are derived (neutral_selects_corpus).
- **In flight:** generic L(5)=6 (qou-80x0); the inaudible radical for H_4/H_5 (qou-wt0l).
- **Next:** see the HANDOVER entries in qou-80x0 and qou-wt0l.
- **Blockers:** .jsonld nodes for 8 photon blocks were never generated (the light platform emits the wrong @context); details in qou-amon. No Lean model of H_n(q) for n>=4.
- **Resume cold:** read qou-80x0, qou-wt0l, qou-amon and audit docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md §12–§15.

## q-NS literature child (session_01EucfRp1HyniH3qQb1YGVWb) — 2026-11-25T16:32Z
- Role: research child (coordinator session_01EucfRmMzrEARLFNgZfhwsQ).
- Task: qou-0nqs + formalise fluid/holography literature in q-NS. Epic qou-i6e2.
- Done: PR #9434 (draft): QOU/FluidDynamics/DECNavierStokes.lean sorry-free, lean-direct exit 0 (energy equality, vorticity eq, harmonic circulation, mass/circulation conservation, enstrophy decay conditional on gap, nelson_consistency, nu_q=O(q-1)); audit docs/audits/2026-11-25-qns-literature-formalisation.md (15-row table). qou-0nqs verdict: modelling choice; owner decision 1/2/3 framed in the audit.
- In flight: none.
- Next: qou-gd5s (regularity route for nu_q), qou-lke8, qou-hr80, qou-dvfy, qou-9lxj, qou-tgq7, qou-jv2n (Lean paper statement + content blocks).
- Blockers: owner ruling on qou-0nqs wording; qou-hr80 waits on #9430 (BringRegularMap).
- Route: olean cache restore per AGENTS.md Step 0, then lean -DautoImplicit=false -s 65536.

## Handover — binding error budget (session_01EucfRntKGFoPCof8huHo3z, 2026-11-25T16:32Z)
Bean qou-rf43 (in-progress). Draft PR #9436, branch claude/binding-error-budget-2026-11-25, head 281e13fb9. Audit docs/audits/2026-11-25-binding-error-budget.md: on the ruled inputs the light nuclei bind by keV. Ranked contributions: bond word (~350x on 2H), missing positive b3 (qou-brng), nucleon-block sign flip, topology; scale, pin, convention, functional and numerics about 1%. Owner decision §6 pending (ACCURACY.md K_A rows use E_osc = 10.09 E0). Next: check how #9221 chose E_osc (open entry 3).


- compute child (session_01EucfRmFaPKg5KbjjmxSBwx) update 16:5xZ: qou-63be done -> PR #9435 (mutant volume fix + Chmutov-Lando citation), ready.

## Merge manager (session_01EucfRm2khmNLbMgiuTA6UZ) — 2026-11-25 16:30Z
- Role: merge manager for litlfred/qou. Owner grant until 2026-11-25T22:00Z; owner-rulings rows from 2026-11-24 and 2026-11-25.
- Process/task: verify each PR on its head (lean-direct sweep on the restored cache, #print axioms, probe re-runs, precision gates, jsonld --check), then merge, then rebuild and publish the PDF.
- Done: 17 PRs merged. The list with main SHAs is in bean qou-au0d. Most recent is #9431 → 52f9f88dfcd.
- In flight: #9424 (head f1c5d61dbbf5): verifying now.
- Next:
  - #9432 once cat-harness#1405 merges.
  - PDF rebuild for #9430/#9431 once the coordinator's gh-pages publish is done.
- Blockers:
  - cat-harness#1405 is outside the grant.
  - The merge API intermittently returns 500/502. Re-read main ~30 s after a 5xx before retrying.
- Resume cold: read bean qou-au0d (queue + traps). Restore the cache with scripts/lean-cache-restore.sh. Shadow builds go under --shadow /home/user/lean-shadow (container-local). Run scripts/setup-folio-assistant.sh to match the pin before gen-block-jsonld --check.

- [q-NS child, 16:55Z] qou-4k93: Yekutieli bridge proved (DEC vorticity = abelian specialisation of Yekutieli face holonomy), PR #9434. Next: content blocks for qou-lke8/dvfy/9lxj; global non-abelian Stokes on Bring open.

- 2026-11-25 ~16:45Z update (session_01EucfRpmx5vQ5s5BZrP4uTV): DEC probe qou-k5jb finished, witness 12/12 committed. Moved the 17 public PDFs in PR #9439 (draft): deletions plus pointers. All 17 are already byte-identical in qou-private main. check:l1-complete is unaffected. BLOCKED: restoring the 11 papers' sections/ to public was denied by the session's safety classifier, because the owner's direct instruction to this session was 'full texts stay in qou-private' and the 'B Public' answer reached it only as a relay. Waiting for the owner to confirm directly.

- 16:40Z rf43 (session_01EucfRntKGFoPCof8huHo3z): finished open entry 3. The ACCURACY.md K_A ²H +1.81% headline is the G2×V2 cell in the E_osc chart, chosen from a pre-registered 6 models × 4 charts grid. In the E0 chart the same model gives −89.9%. The γγ-bond rows (V3) give 0.08–1.4 keV, the same as the trace pipeline. PR #9436 head a26745ea7. Recommendation in §6 is now Option 1 (add a scope note to the scorecard); waiting on the owner.
