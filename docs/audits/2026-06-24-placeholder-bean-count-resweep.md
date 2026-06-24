# Placeholder-bean count resweep — the "N placeholders" titles are badly inflated; **0 uncited `sorry` corpus-wide**

**Date:** 2026-06-24
**Branch:** `claude/placeholder-bean-count-hygiene-2026-06-24`
**Method:** `scripts/count-actionable-placeholders.ts` (the honest counter — distinguishes a real
un-cited `sorry` token in compiled Lean from `sorry`-in-comments, `-- Ref:`-cited conjecture
`sorry`s, and `.md` prose) run per bean scope. No fit; mechanical.

## Finding

The `Resolve N placeholders/TODOs in <scope>` beans carry **raw grep counts** in their titles
(`sorry`/`TODO`/`placeholder` substrings anywhere, including doc-comments, the word "sorry-free",
`-- Ref:`-cited conjecture sorries, and `.md` prose). The **honest actionable** count — un-cited
`sorry`s (real §1 violations) + bare `TODO`/`FIXME`/`XXX` markers — is a small fraction, and the
**uncited-`sorry` count is `0` across the entire corpus** (the last one, in
`observations/n-v-tower-depth-ninety.lean`, was de-vacuified in #2736).

| bean | title claims | honest actionable | uncited `sorry` | remaining = |
|------|:---:|:---:|:---:|---|
| `95jh` BraidKnot | 213 | **5** | 0 | intentional TODO markers (witness-deps, QBeta order-3..7) — drained #2656 |
| `b3pe` Archimedean | 87 | **3** | 0 | TODO/FIXME markers |
| `ekb8` Interactions | 17 | **0** | 0 | nothing actionable |
| `zslh` mass-theory | 103 | **0** | 0 | nothing actionable |
| `mlt7` mass-endomorphism | 15 | **1** | 0 | one TODO marker |
| `xj99` quantum-observable-universes | 7 | **0** | 0 | nothing actionable |
| `ldup` unital-groebner-bases | 29 | **4** | 0 | TODO/FIXME markers |
| `doth` schema | 25 | **7** | 0 | TODO/FIXME markers |
| `i6p9` qou/lean (root, recursive) | 10 | **16** | 0 | `MathlibExt` `-- TODO upstream:` notes (intentional) + others |
| `ixx4` MathlibExt.lean | 6 | **6** | 0 | all `-- TODO upstream:` notes on **proved** lemmas (intentional) |

Titles sum to ~510 "placeholders"; the honest actionable total is **~42 TODO/FIXME markers and
0 uncited `sorry`s**, and every marker inspected so far is an **intentional** documentation note
(`-- TODO upstream:` on a proved `MathlibExt` lemma; Helium3/Tritium/Deuteron witness-deps;
QBeta order-3..7 research notes) — *not* a missing proof or a stub.

## Implication for future sessions

- **Do not chase the title counts.** Run `scripts/count-actionable-placeholders.ts <scope>` first;
  the honest number is what matters. `--list` gives the per-file breakdown.
- **The Lean-discipline backlog (uncited `sorry`s) is empty** corpus-wide. The remaining
  `TODO/FIXME` are intentional markers; removing them destroys upstream-tracking / witness-dep
  / research information and should **not** be done to "drain a count."
- These beans can be closed or re-titled to their honest counts by the owner (agents do not close
  beans — owner-only per AGENTS.md §4a). This doc is the durable record so the inflated titles are
  not re-attempted.

## Secondary glitch — duplicate bean files

`doth`, `mlt7`, and `zslh` each have **two** `.beans/*.md` files (e.g.
`doth--resolve-25-placeholders-todos-in-schema.md` *and*
`doth--resolve-25-placeholderstodos-in-schema.md` — slug variant `placeholders-todos` vs
`placeholderstodos`). Same bean ID, two files. Flagged for owner cleanup (not deduped here to
avoid breaking bean tracking).

## References

- `scripts/count-actionable-placeholders.ts` — the honest counter (its header documents the
  false-positive classes it excludes).
- #2736 — de-vacuified the last uncited `sorry` (`observations/n-v-tower-depth-ninety.lean`).
- #2656 / `docs/audits/2026-06-23-placeholder-bean-resweep.md` — the prior 95jh resweep (213 → 7).
