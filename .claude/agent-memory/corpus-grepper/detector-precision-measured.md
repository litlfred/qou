# Text heuristics over this corpus's own artifacts — four measured precisions

Detail for the `MEMORY.md` TRAP of the same name. Every figure here was
measured on 2026-09-04 by reading **every** candidate, not by sampling.

## The four

| what was matched | to decide | candidates | true | precision |
|---|---|---|---|---|
| commit **subjects** carrying a completion verb | "is this bean's work done?" | 12 | 2 | **2/12** |
| bean **titles**, token-Jaccard ≥ 0.45 | "are these two beans duplicates?" | ~12 | 1 | bad — *and it MISSED the pair found by reading* |
| Lean **docstrings** claiming a literal value | "does the body compute what the doc says?" | 8 | 1 | **1/8** |
| **grep for a defect's shape** (the corpus's own convention-C audits) | "how much C is left?" | — | — | 26-row blindness taxonomy; see `AGENTS.md` |

The first three were built and measured in one session. The fourth is the
corpus's own long-running instance of the same thing.

## Why they fail — the classes are SEMANTIC, so no regex reaches them

**Completion verbs (2/12):**
- *partial completion* — "ITEM 4 CLOSED"; "item 3 fully closed; the remaining item is …"
- *the verb governs a DIFFERENT bean* named in the same subject
- *the verb is QUOTED or NEGATED and the commit REOPENED the bean* —
  `qou-hok7`: "deuteron-wall **'resummation closed'** is a wrong-transform
  artifact". Scare quotes; a regex cannot see them.
- *deliberately parked* — `qou-mln9`: "Left `todo` deliberately … Closing is
  the author's call." Not stale. The difference is INTENT and lives in the body.

**Duplicate titles (bad both ways):**
- *title templates* dominate the token set — seven `cj*` "Conjecture carrier: X
  (X.lean) — §3b, famous-open" differing only in the declaration
- *a 1.00 title match was still false* — `qou-r3vt` / `qou-ty08` have
  byte-identical titles and are different Lean FILES; the distinguishing field
  is the path, which the title omits
- *it missed the real pair* — `qou-3v8h` / `qou-eu0r` score 0.375 because one
  says "authorNotes is silently dropped on …" and the other "Schema silently
  drops authorNotes on …"

**Docstring value claims (1/8):**
- *doc states the formula, body IMPLEMENTS it* — `writhe`, `Hn`,
  `massSqQuadrupled` (`4 m²` vs `4a + 4bY + c(…)`, which IS 4m² expanded)
- *doc states an INTERMEDIATE value, not the return* —
  `borromeanColorSum_trivTrace`: "Each half-Borromean evaluates to `1` … so the
  sum is `3`", body `3`. **The docstring is entirely correct.**
- *parser leakage* — matched a type signature; ran into the next declaration

## The rule that follows

**A heuristic over an artifact's TEXT cannot decide a question about the
artifact's MEANING.** Use these tools to choose what to OPEN, never to conclude.
Read every candidate before quoting a rate — all three of the above were first
estimated 3-6× too optimistic by their own authors (me), and the estimate was
always made by reading subjects instead of bodies.

**Do not ship a detector whose false positives are CORRECT artifacts.** That is
the decisive test, sharper than the rate: flagging `writhe` and
`borromeanColorSum_trivTrace` trains a reader to distrust docstrings that are
right, which is worse than the defect being hunted.

## The counter-move that DOES work

Ask a question the text cannot lie about.

- **WHEN, not what.** "Has any commit named this bean in the last 12 h?" is a
  date comparison — none of the semantic classes touch it. It correctly flagged
  `qou-bg3w` as claimed by a live session when the completion heuristic could
  not see it at all.
- **Test the ANSWER, not the source.** The Markov peel's deuteron denominator
  factors as `192·q²³·(q²+1)³` — one `(q²+1)` per peel, because `z = q³/(q²+1)`.
  Convention C cannot produce it. A value cannot be stale, mislabelled,
  re-spelled or inherited from a stale record and still factor correctly.
- **Ask git.** `git log -L <line>,<line>:<file>` settled the `hookDim`
  docstring drift in one command, after the detector merely nominated it.
