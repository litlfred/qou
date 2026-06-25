# Witness staleness from comment-only commits — cosmetic, corpus-scale, and Hecke-unsafe to bulk-refresh

**Date:** 2026-06-25
**Status:** advisory / trap-marker. No code change. Records why a tempting *"refresh the stale
witnesses"* sweep is both **low-value** and **dangerous**, so the next agent does not trip the
ct80 rake.

## Finding

A single **comment-only** commit — `fix(cite): chlouveraki2016hdr → chlouveraki2016-hdr` (a
bibliography key inside a `-- Ref:` / cite comment) — left **~1165 witnesses flagged "stale"** by
the `scriptCommitSha`-drift discipline (AGENTS.md idle item 4):

| class | count | in-sandbox-refreshable? |
|---|---:|---|
| total stale (`scriptCommitSha` ≠ producer's last commit) | 1165 | — |
| direct-Hecke importers (`pyhecke`/`hecke_core`/`markov`/…) | 194 | ❌ needs `pyhecke_native` |
| "pure-mpmath" by import-grep | 962 | ⚠ **NOT reliably** — see trap |
| of those, caused by the one cite-fix | **962** | — |

**The values are unchanged.** Verified on `full_twist_delta_n2_verification` (pure-mpmath):
re-running drifts **only** `scriptCommitSha`, `commitSha`, `computedAt`, `durationMs` — **`scriptHash`
(content hash) does *not* drift**, and no data/assertion value changes. The witnesses are numerically
correct; only the git-pointer provenance lags by one comment-only commit.

## The trap — why a bulk-refresh is *dangerous*, not merely low-value

The "pure-mpmath" label above is **import-grep only**: it screens the producer's *own* import lines
and does **not** catch *transitive* Hecke dependencies. `canonical_isotope_witness.py` — which recurs
many times in the 962 — is the counter-example: no direct `pyhecke` import, but it transitively
reaches the Hecke/Markov trace, and **re-running it without `pyhecke_native` silently falls back
`mpf → f64`**. That is exactly the **ct80** regression ([#2747](https://github.com/litlfred/qou/pull/2747)),
where 143 m_e-dependent witnesses were regenerated, caught dropping 50-dps → f64, and reverted. A
blind 962-witness refresh replays that disaster at ~7× scale.

## Disposition

1. **Cosmetic / low priority.** `scriptCommitSha` drift from a *comment* change is not a correctness
   issue; the committed numbers are right. It is not a hard CI gate (prepare-merge auto-refreshes only
   the 4 self-emitting audit witnesses).
2. **If refreshed at all → full-env mechanical regen** (`pyhecke_native` + 50-dps), like ct80/#2747 —
   *not* an in-sandbox or idle-drain task. Do **not** trust the import-grep "pure-mpmath" label;
   run-and-verify each (the witness diff must be **provenance-only**) or it f64-regresses.
3. **Infra avenue (observed):** the drift here was in `scriptCommitSha` only; **`scriptHash` (content
   hash) was stable.** A staleness detector keyed on `scriptHash` rather than `scriptCommitSha` would
   not false-flag comment-only producer edits, removing the bulk of this 1165-witness false-positive
   footprint at the source.

## Method

`scriptCommitSha` (witness) vs `git log -1 --format=%H -- <producer>`; direct-Hecke filter via
import-grep on the producer; provenance-only confirmation via re-run + `git diff` of the witness JSON
(must touch no data/assertion value, no precision-digit loss).

## Cross-refs

- ct80 / [#2747](https://github.com/litlfred/qou/pull/2747) — precedent f64-regression + the guarded
  full-env runner (`regen_me_witnesses_batch.py`) that is the safe path.
- AGENTS.md §idle item 4 (refresh stale sidecars + witnesses) — this note scopes the *witness* half:
  comment-only-induced staleness is cosmetic and Hecke-unsafe to refresh in-sandbox.
