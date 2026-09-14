# Sibling/library divergence: what the 340 actually are

**Date:** 2026-09-14 · **Beans:** `qou-9yt9` · **Scope:** triage only — nothing renamed, no Lean changed.

Follow-up to #7345 (namespace stack) and #7351 (declaration offset), which together
took `lean-sibling-library-divergence-audit.py` from 148 to 207 distinct
(sibling, library) file pairs. This is the triage of what it now reports.

## The headline: the top-ranked findings are all LEGITIMATE

Every case at the top of the script's own epistemic ranking, examined by hand,
turns out to be a **declared, documented choice** rather than drift. The residual
hazard is real but narrower than the count suggests, and it is about **name
sharing**, not about two files disagreeing by accident.

| rank | count | verdict |
|---|---|---|
| `divergent-axiom` | **0** | — |
| sibling ASSUMES, library does not | **2** | both legitimate, see below |
| `divergent` | 340 | see "what the 340 are" |
| `duplicate` (identical, suppressed from the listing) | 217 | benign |

## The 2 "sibling assumes" cases — both declared

**`QOU.BraidKnot.confined`** — the sibling declares it `opaque`, and says why:
*"The confinement predicate `confined` and the per-phase invariants `mu` / `sigmaF`
are `opaque` (their closed form is the numerical SDP solution at each `q`, not
available in Lean)."* The library's `confined` takes `[HasConfinementWitness P]` —
a different signature, so these are not even the same object.

**`QOU.AlgebraicSubstrate.HqBiFiltration.BiFiltration`** — sibling
`opaque BiFiltration (q) (n) (lam) : Type` against library
`structure BiFiltration (A) [Ring A]`. The sibling's own docstring already records
that the full version *"requires non-opaque `BiFiltration`"*.

Both are honest deliberate abstractions. **Verdict: legit.**

## What the 340 are — the comparison is over-broad, measurably

The script compares the text from each declaration **to the next declaration**, so a
declaration identical in both files reads as divergent whenever its *neighbour*
differs. Re-measured with each declaration bounded at its own end (first
non-indented, non-blank line):

    identical declaration      246
    DIFFERENT DEFINITION       245
    same claim, different proof 66

against the span method's 217 identical / 340 divergent. So the reported 340 is
**not** 340 divergences, and the useful split is definition-differences (which
change meaning) from proof-differences (which do not).

🛑 **This refinement is NOT implemented in the script.** It is recorded here as a
measurement and a proposal. Two earlier attempts at it produced wrong numbers —
one reported a 473/84 split that was an artifact of the offset bug #7351 fixed —
so it wants a careful implementation with its own regression check, not a quick
patch.

## The substantive finding: one NAME, incompatible ground rings

Three names carry more than one body, and the ground ring is load-bearing (§7c):

| name | declarations | distinct bodies |
|---|---|---|
| `QOU.R_q` | 46 | 42× `LaurentPolynomial ℤ`, **2× `RatFunc ℚ`**, 1× `Archimedean.R_q`, 1× `noncomputable` variant |
| `QOU.q_param` | 34 | 32× `LaurentPolynomial.T 1`, **2× `RatFunc.X`** |
| `QOU.Information.R_q` | 5 | 3× **`ℝ`**, 2× `LaurentPolynomial ℤ` |

**Every minority variant is deliberate and documented**, which is why this is a
hazard rather than a bug:

- `RatFunc ℚ` — `braids-and-knots/quantum-su2.lean` and its library counterpart
  `lean/QOU/BraidKnot/CasimirShared.lean`, both headed *"Casimir cluster — ground
  ring `R_q = ℚ(q) = RatFunc ℚ`"*. The pair agrees with itself; it disagrees with
  the other 44.
- `Information.R_q := ℝ` — *"Ground ring: archimedean specialisation `R_q := ℝ`
  (AGENTS.md §7c). The numerical substrate value `q₀ ≈ 1.1097` lives in `ℝ`."*
  This is §7c being **observed correctly**, not violated. I suspected a wall
  violation before reading it; it is the opposite.

**What remains true anyway.** Two modules declaring one fully-qualified name can
never both be imported, and under §0a a `lean.ref` to `QOU.R_q` resolves to
whichever file wins candidate 1 — so which ground ring a reader lands on depends
on where they entered. AGENTS.md already records that a `QOU.Archimedean.R_q`
collision took 180 modules off the verified corpus (beans `qou-lksc`, `qou-kfcl`),
so this shape has cost the corpus before.

**Not renamed here**, per the standing instruction: which of `LaurentPolynomial ℤ`
and `RatFunc ℚ` should own the bare name `QOU.R_q` is an authorial call about the
Casimir cluster's scope, not a cleanup.

## Method note

Counts are reproducible with `python3 scripts/lean-sibling-library-divergence-audit.py`
on `main`. Quote **file pairs** rather than name-level findings when comparing runs:
a corrected name shows up as one lost plus one gained and is not a change.
