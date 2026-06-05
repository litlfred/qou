# Coordination — QA staleness infra + `/integration-backlog all` drain (#1885)

**Branch:** `claude/dreamy-albattani-RKsjx` · **PR:** [#1885](https://github.com/litlfred/qou/pull/1885)
**Goal:** drain the integration-watcher QA backlog; fix lean-compile-audit staleness (SHA-based).

## Scope map (2026-06-05)

| PR | Branch | Scope | Overlap w/ #1885 | Dep | Cherry-pick |
|----|--------|-------|------------------|-----|-------------|
| **#1885** (this) | `claude/dreamy-albattani-RKsjx` | QA pipeline `.ts` (qa-checkers-extended/voice, qa-sweep, lean-compile-audit); 955 proof sidecars → `n/a`; 25 one-voice `.md` (mba + mechanical) | — | — | — |
| **#1871** | `claude/confident-newton-R8lIx` | M=Vol×Density SU(2)/SO(3) symmetry — `mass_vol_density.py`, `_li_2_q_util.py`, `MassVolDensity.lean`, `binding-manybody-jet-filtration.*`, `sw-period-residue-sum.*`, audit docs | **none** (no shared file; adjacent chapters mass-theory / brings-surface) | none | none |

## Classification (skill §2)
- **#1871:** overlap LOW/none, dependency none, cherry-pick none. Coordination point: #1885's `proof-lean-compiles` change (SHA-staleness → `n/a` for stale/missing cache) governs how #1871's **new Lean blocks** are QA'd. Both PRs billing-blocked.

## Comments posted
- #1871: intent + QA-semantics heads-up — https://github.com/litlfred/qou/pull/1871#issuecomment-4634037427

## #1885 own-PR review triage (skill §5)
- 4 threads (Gemini ×1, Copilot ×3) — all **accepted + fixed** in `657e34dc` (path.resolve + containment/`.lean` guard; hashFile reorder; `$schema` `v1|v2` union). 3 marked outdated; no open actionable threads.

## Escalations (skill §6)
- None. Findings consistent across PRs (shared billing-block diagnosis; no contradictory framing).

## main watch (skill §8)
- `origin/main` +18 since divergence (qbeta / gap-a4 activity). No main landing touches #1885's QA-pipeline files. Rebase deferred to `/prepare-merge`.

## Landed in #1885 (final)
- SHA-staleness infra (`lean_sha`, `--stale`, checker `n/a` gate) + Gemini/Copilot review fixes.
- proof axis: 638 stale `proof-lean-compiles` fails → `n/a` (955 sidecars).
- one-voice mechanical: 25 blocks (unicode-crash/emoji/editorializing/status-leak/time-stamped).
- one-voice author-notes: 13 blocks migrated (§4d, provenance → authorNotes / dropped).
- detangler: 5 spurious forward-edges pruned (4 blocks).
- coordination ledger + #1871 intent.

## Deferred work (post-#1885 — needs owner input / different env / larger scope)
1. **detangler reorders (3, quantum-observable-universes)** — `adjoint-trace` + `archimedean-realisations` (remarks → move after the prop they interpret); `braiding-eigenvalue-extraction` (prop → reorder before `prop:tannaka-krein-reconstruction`). Chapter-manifest surgery + forward-ref cascade check. Owner leaned "move rmk forward" — held for approval (manifest edits change reading order).
2. **detangler prop→conj (1)** — `archimedean-functor-uniqueness` → `conj:dilogarithm-archimedean-limit` (genuine dep, 6 mentions, 168 apart). ALSO a §3b conjectural-propagation flag (a proposition downstream of a conjecture). Route to a proof/propagation pass, not a reorder.
3. **detangler-block-tanglement (13)** — block splits / relocations; judgment-heavy.
4. **author-notes — true backlog ≈ 100 (not 14)** — re-sweeping with the current checker surfaced ~86 more blocks whose stale `pass` entries now fail (PR/date provenance accreted since last clean audit). Batch in a follow-up.
5. **un-authorized voice criteria** — `wall-side-correct` (12, critical), `voice-scholarly-default` (7), `voice-statement-no-interpretation` (5). Need judgment; not in this campaign's scope.
6. **compute axis (15) — ENV-BLOCKED** — `compute-witness-exists` (4), `compute-prop-has-probe`/`-consumer` (5+5), `compute-lp-dual-present` (1) all require running Python producers (`lp-duality-check.py`, `probe_he4_*`, …). This container has **no numpy/mpmath/qou_substrate**. Needs a Python-provisioned env.
7. **surreal forward-refs (2)** — `surreal-rate-calculus`, `conway-normal-form` — owner accepted appendix-surreals forward-refs as OK; left as-is.
8. **full sidecar re-sweep** — the committed `qa-checkers` notes-field change re-staled all voice/extended sidecar entries; CI's next full `qa-sweep` is the canonical refresh (will surface item 4's true count).

## Next action
- **`/prepare-merge #1885`** (owner-selected): rebase onto `origin/main` (+18), validate, request Gemini + Copilot reviews. Merge on owner's explicit "merge it" (CI billing-blocked → green-local). Deferred items 1-8 → follow-up branch.
