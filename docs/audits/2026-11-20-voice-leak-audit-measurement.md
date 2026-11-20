# Voice-leak audit: detector, measured rates, and the drain hit list (W14, epic `qou-d4kh`)

Date: 2026-11-20. Branch `claude/voice-leak-checkers-2026-11-20`, PR #8538.
Beans: epic `qou-d4kh`, V1 `qou-9aar` (checkers), V3 `qou-ycjd` (drain).

## 1. What was built

`folio/pipeline/voice-leak-audit.ts` checks the four leak classes of the epic.
`paper-commentary-audit.ts` and the platform voice checkers do not check them.

| class | criterion | what fails |
|---|---|---|
| L1 | `leak-lean-prose` | prose that talks about the formalisation: `Lean`, `Mathlib`, `## Lean …` headings, "proved formally", "formalised in", "machine-checked". The bare word "formalise" is **advisory**, see §3. |
| L2 | `leak-lean-ident` | backticked spans in prose that are identifiers: `fqn`, `lean-file`, `repo-file`, `block-id`, `decl-name`, `typeclass` |
| L3 | `leak-person` | we, our, us, let's, let us, you, your, "the reader". It does not match "I", because that is mostly a Roman numeral. |
| L4 | `leak-reading-order` | (a) a `q` token (`$q$`, `[n]_q`, `\Phi_d`, `SU_q`, Hecke, "archimedean wall") before `sec:substrate-parameter`. This fails in Ch 1 and is advisory in Ch 2 §1–6. An `outro-*` block is exempt. (b) a `](#label)` link to a block later in reading order. This fails in Ch 1–2 and is advisory elsewhere. Links to back matter and to the block's own table sibling are exempt. |

The audit uses one reading order, built by importing the paper and chapter
manifests. The guard is `voice-leak-audit.test.ts` (16 tests).
`paper-commentary-audit.ts` is unchanged except for a header pointer to the new audit.

```
bun run folio/pipeline/voice-leak-audit.ts [--json] [--quiet] [--class L1,L2,L3,L4]
bun test folio/pipeline/voice-leak-audit.test.ts
```

**What is not in this repo.** `qa-checkers-voice.ts` belongs to the
platform (`litlfred/folio-assistant`), and W14 cannot push there. Its
`stripInlineCode` gap is measured below and was not changed.
`scripts/claude-redteam-and-qa.ts` and the epic's own scanner
`computations/audits/monograph_lean_and_voice_leak_audit.py`, with its
witness, **do not exist on `main`**. A code search finds them on no branch.
So the epic's counts (L1 678 / L2 2,540 / L3 1,224 / L4 86) could not be
reproduced. The table in §4 replaces them.

## 2. Before: what the existing checkers caught

Population: 5,388 candidate hits (L1 784, L2 3,250, L3 1,236, L4 118) in
3,666 manifest-listed `.md` blocks. The scan ran before the last two scoping
changes. The table counts a hit as caught when the checker flags the **same
line** for any reason, so these numbers are an upper bound on recall.

| class | `paper-commentary-audit` (line) | platform voice checkers (line) | platform (block fails at all) |
|---|---|---|---|
| L1 | 40 / 784 (5.1 %) | 7 / 784 (0.9 %) | 26 / 397 blocks |
| L2 | 356 / 3,250 (11.0 %) | 45 / 3,250 (1.4 %) | 39 / 713 |
| L3 | 18 / 1,236 (1.5 %) | 15 / 1,236 (1.2 %) | 31 / 684 |
| L4 | 1 / 118 (0.8 %) | 0 / 118 | 0 / 51 |

The platform figures come from the 11 `VOICE_AUTOMATED_CHECKERS`, excluding
unicode-crash and cite-named-theorem, run from the platform-lite checkout
mounted at session start. Most `paper-commentary-audit` line hits in L2 are
backticked `computations/…` paths, which it already flags as `repo-ref`.

## 3. After: measured precision and recall of the new audit

Precision was measured by hand on random samples. Each hit was read in its line context.

| sample | seed | class | true / sampled | false positives |
|---|---|---|---|---|
| 1 (pre-fix) | 20261120 | L1 | 30 / 30 | — |
| 1 | | L2 | 30 / 30 | — |
| 1 | | L3 | 30 / 30 | — |
| 1 | | L4 | 27 / 30 | link to a glossary block; an `outro-` foreshadow of `q`; link to the block's own table. **All three are now exempt.** |
| 2 (post-fix, fresh draw) | 777 | L1 `formalise` only | 16 / 20 | "this formalises 'faster-than-viscous growth'", "the chapter formalises the backbone", "to formalize the full binding scale", one ambiguous. **So `formalise` is advisory.** |
| 2 | | L4 | 30 / 30 by the owner's rule | 5 are "uniqueness is shown in [next proposition]" pointers. A monograph would usually keep these. They are split out as `forward-link-same-section` / `-later-section` so the owner can scope them. |
| 2 | | L2 `decl-name` + `typeclass` | 25 / 25 | — |
| 2 | | L3 | 20 / 20 by the rule | 3 are debatable as voice: "Our universe sits at $q_0$", first person in `introduction/intro.md`, "the reader's context". |

Recall was **not** measured as a full rate. Only a targeted probe was run:
15 random unflagged lines matching a wider L1 vocabulary, and 15 matching a
wider L3 vocabulary.
- **L1:** 5 of the 15 were real leaks, all of them "formalis…" forms. They are now caught, as advisory hits.
- **L3:** 1 of the 15 was a real leak ("the reader"). It is now caught. The other 14 were Roman numerals or matrix identities.

What a negative here does not show: the probes only searched
vocabulary I thought of. A leak in other words ("the carrier", "the
formal statement" with no Lean word) is not covered.

## 4. Hit list on `main` `917b69399` (failing hits only)

5,220 failing hits in 1,328 of 3,666 blocks (L1 666, L2 3,250, L3 1,236, L4 68).
Advisory hits are not counted: 118 L1 `formalise`, 50 Ch-2 premature-`q`,
and 979 forward links outside Part I.

| chapter | L1 | L2 | L3 | L4 | total | blocks |
|---|---:|---:|---:|---:|---:|---:|
| `mass-theory` | 197 | 1123 | 78 | 0 | 1398 | 306 |
| `mass-endomorphism` | 51 | 368 | 87 | 0 | 506 | 81 |
| `predicted-spectra` | 78 | 293 | 123 | 0 | 494 | 100 |
| `stochastic-mechanics` | 79 | 167 | 11 | 0 | 257 | 34 |
| `observations` | 11 | 105 | 96 | 0 | 212 | 83 |
| `appendix-surreals` | 23 | 116 | 72 | 0 | 211 | 60 |
| `information-theory` | 18 | 88 | 101 | 0 | 207 | 75 |
| `appendix-mass-binding-algorithms` | 6 | 171 | 4 | 0 | 181 | 20 |
| `notation` | 15 | 107 | 58 | 0 | 180 | 7 |
| `brings-surface` | 11 | 95 | 40 | 0 | 146 | 42 |
| `eightfold-way` | 32 | 110 | 2 | 0 | 144 | 15 |
| `braids-and-knots` | 45 | 66 | 18 | 0 | 129 | 36 |
| `fluid-dynamics` | 5 | 75 | 42 | 0 | 122 | 39 |
| `quantum-observable-universes` | 3 | 17 | 67 | 20 | 107 | 72 |
| `lifting-and-descent` | 3 | 10 | 94 | 0 | 107 | 43 |
| `knots-particles-confinement` | 7 | 48 | 50 | 0 | 105 | 47 |
| `nuclear-interactions` | 7 | 34 | 59 | 0 | 100 | 52 |
| `quantum-universes` | 4 | 10 | 22 | 48 | 84 | 33 |
| `glossary` | 17 | 49 | 12 | 0 | 78 | 23 |
| `molecular-construction` | 9 | 26 | 36 | 0 | 71 | 36 |
| `climax-volume-mass` | 5 | 28 | 22 | 0 | 55 | 15 |
| `q-geometric-langlands` | 1 | 20 | 29 | 0 | 50 | 24 |
| `appendix-knot-periodic-table` | 4 | 36 | 8 | 0 | 48 | 3 |
| `appendix-qvalues` | 4 | 37 | 4 | 0 | 45 | 13 |
| `appendix-surreals-archimedean` | 4 | 22 | 15 | 0 | 41 | 10 |
| `models-of-qous` | 0 | 2 | 35 | 0 | 37 | 24 |
| `appendix-standard-model` | 13 | 15 | 4 | 0 | 32 | 11 |
| `introduction` | 1 | 0 | 25 | 0 | 26 | 4 |
| `index-of-definitions` | 13 | 7 | 0 | 0 | 20 | 1 |
| `organic-chemistry` | 0 | 0 | 8 | 0 | 8 | 5 |
| `gravity-spacetime` | 0 | 0 | 7 | 0 | 7 | 4 |
| `appendix-knot-operations` | 0 | 5 | 0 | 0 | 5 | 3 |
| `measurement-observation` | 0 | 0 | 4 | 0 | 4 | 4 |
| `appendix-transfer-matrices` | 0 | 0 | 2 | 0 | 2 | 2 |
| `appendix-knot-operations-archimedean` | 0 | 0 | 1 | 0 | 1 | 1 |

**By sub-kind.**
- **L1:** `lean-word` 485, `mathlib` 83, `lean-heading` 40, `proof-assistant` 29, `formalised-in` 25, `formally` 3, `discharges-axiom` 1.
- **L2:** `block-id` 1,052, `decl-name` 1,007, `fqn` 452, `repo-file` 379, `typeclass` 234, `lean-file` 126.
- **L3:** `we` 1,169, `our` 56, `the reader` 4, `us` 3, `ours` 2, `you` 2.
- **L4:** premature-`q` 29, all in Ch 1; forward links 39 (cross-chapter 15, later section 11, same section 13).

**Mechanically fixable subset.** 926 of the 1,052 `block-id` hits, in
388 files, are the visible text of a link to that same label
(``[`rem:x`](#rem:x)``). The replacement text is the target block's
`title`, which is fixed by the corpus.

The full list can be regenerated deterministically with `--json`, so it is
not committed.

## 5. A discrepancy with the bean record

Beans `qou-ig2d` (V0) and `qou-x4nh` (V2) are `completed` (2026-11-19).
They say Ch 1 and Ch 2 were drained to "0 L1, 0 L2, 0 L3". They also say
`frobenius-hopf-substrate` was moved into `quantum-universes/` and that
`SemisimpleBlockData` was factored out of `QuantumUniverse`.

On `main` `917b69399` none of this holds:
- Ch 1 still has L1 4 / L2 10 / L3 22.
- Ch 2 still has L1 3 / L2 17 / L3 67.
- `ls quantum-universes | grep frobenius-hopf` finds nothing.
- `grep -r SemisimpleBlockData lean/QOU` finds nothing.

No branch or PR carrying that work was found: I searched branch names
dated 2026-11-18…20 and PR search terms. The work may exist in an unpushed
container. The beans were reopened to `todo`, each with a note.
