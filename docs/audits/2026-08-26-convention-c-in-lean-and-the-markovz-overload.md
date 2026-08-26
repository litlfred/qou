# Convention C in Lean, and the `markovZ` overload

**Bean:** `qou-cxjq`. **Status:** the bean's headline claim is **retracted**; two
real findings replace it, one of them broader than what the bean recorded.

## RETRACTED — AGENTS.md does not state a convention-C all-clear for `.lean`

The bean says:

> AGENTS.md records the 2026-08-10 drain as clearing `.lean` to zero — that is
> wrong.

It is not wrong, because it is not about convention C. AGENTS.md contains
exactly one "**0** in `.lean`/`.ts`" claim, at line 1491, and it belongs to the
**Λ vs Cl₂ / `Vol(4₁)` naming** guard — the `2Λ(π/3)` vs `2·Cl₂(π/3)`
coefficient-vs-name defect. Different class, different drain, different tracker
(`qou-zdz5`).

The convention-C section of AGENTS.md quotes `convention-c-producer-audit.py`'s
**26 actionable** and, separately, a `content/` grep from 2026-08-24 (12 matches,
5 live). Neither is an `.lean` all-clear. **Two adjacent passages, both about
drains that reported "corpus-wide", conflated by their shape rather than their
subject** — which is the same failure mode the corpus-grep discipline exists to
prevent, committed inside a bean whose subject is detector blindness.

## Finding 1 — the detector is Python-only, so no `.lean` count has ever existed

[`scripts/convention-c-producer-audit.py`](../../scripts/convention-c-producer-audit.py)
walks the tree four times and every one is `base.rglob("*.py")` (lines 635, 760,
785, 930). There is no `.lean` path anywhere in it.

So its number is not a wrong measurement of the Lean surface — it is **not a
measurement of the Lean surface at all**, and it never claimed to be. It is a
*producer* audit, and producers are Python. The gap is that nothing else covers
`.lean` either, so the Lean surface has simply never been counted.

This is a weaker claim than the bean's and a more useful one: the fix is not "add
a pattern to the detector", it is "something must scan `.lean`".

## Finding 2 — 7 convention-C Markov-parameter sites live in `.lean`, under 3 spellings

Hand-verified from a shape-narrowed grep; each row was opened and read. (A first
pass matching `Real.sqrt q` broadly returned **66 files** — a topic-locator, not
a convention detector: most are a golden-ratio threshold, a residue evaluation,
or `q_half − 1/q_half`, which is `h`, not `z`. That 66 is not a count of
anything and is recorded here only so nobody re-derives it.)

| file | declaration | form | verdict |
|---|---|---|---|
| `mass-theory/markov-trace-factorization.lean:29` | `QOU.Archimedean.markovZ` | `1/(q_half + 1/q_half)` | **C**, unlabelled |
| `mass-theory/y-lambda-recipe-from-partition.lean:143` | `markovZ` | `q³/(q²+1)` | **D** ✓ labelled |
| `lean/QOU/MathlibExt/MarkovBondRule.lean:84` | `markovZ` | `q³/(q²+1)` | **D** ✓ labelled |
| `lean/QOU/BraidKnot/HoefsmitV21CosSymmetrization.lean:186,189` | `markovZ`, `markovZ_real` | `u/(u²+1)`, `u := √q` | **C**, √-variable |
| `…HoefsmitV21…:196` | `markovZ_legacy` | `1/(√q + 1/√q)` | **C**, `@[deprecated]` ✓ honest |
| `lean/QOU/BraidKnot/QBetaCategoricalPrecisionLadder.lean:43` | `markovZ'` | `1/(√q + 1/√q)` | **C**, unlabelled |
| `lean/QOU/BraidKnot/MarkovAxiomsPrimitive.lean:63,75` | `markovZax`, `markovZax_real` | `u/(u²+1)`, `u := √q` | **C**, documented |
| `lean/QOU/Hecke/ClosedFormInterfaceFactors.lean:18` | `z` | `s/(s²+1)`, `q = s²` | **C**, documented |
| `knots-particles-confinement/knot-particle-generation.lean:95` | `pairSkeinMass` | `÷ (√q + 1/√q)` | **C**, unlabelled |

> **UNDERCOUNT CORRECTED the same day.** The table above is hand-verified and
> **incomplete**: it reports 7 sites across 6 files. A scanner written for fix
> step 2 — [`scripts/lean-markov-convention-audit.py`](../../scripts/lean-markov-convention-audit.py),
> which does what `convention-c-producer-audit.py` structurally cannot — measures
> **22 convention-C Markov-parameter *definitions* across 18 files**, against 24
> in convention D. Roughly half the Markov-parameter definitions in the Lean tree
> are C. Quote the scanner, not the table; the table is kept as the record of
> what hand-verification found and missed.
>
> **Three measurement errors of my own, in the scanner, each caught before it
> shipped a number** — recorded because each is a way this audit could have been
> wrong in the direction of *reassuring*:
>
> 1. **Scanning `.lake/`.** An unfiltered `rglob` walks Mathlib and every other
>    dependency: 11206 files, 112 "D" sites, almost all somebody else's code.
>    Measuring the harness, not the corpus. Excluded → 3193 files.
> 2. **Counting theorem statements as definitions.** A `q³/(q²+1)` inside a proof
>    *mentions* the convention; one inside a `def` body *defines* it. Together
>    they inflate the total several-fold and hide which sites are load-bearing.
>    The scanner now reports both and says to quote `defs`: 150 sites total, 45
>    definitions.
> 3. **A 3-line window that fixed one miss and broke four verdicts.** Added to
>    catch `pairSkeinMass`, whose denominator wraps to the next line; it then
>    swallowed neighbouring docstrings and misclassified four other sites.
>    Reverted, with the multi-line case recorded as a known limitation rather
>    than hacked around — it needs an expression parser, not a wider window.
>
> **Not all 22 are defects.** Three are named `_legacy` and carry deprecation
> attributes; several (`zC`, `zCsub`, and the `MarkovZClassicalCoincidence` /
> `BraidImageEigenphaseExclusion` sites) are **deliberate** convention-C
> comparison objects — the Lean analogue of the Python audit's declared-C bucket.
> Separating actionable from deliberate is triage that has **not** been done.

**Triage, also reproducible** (`--selftest` output, same script): of the 22,
**14 actionable / 8 deliberate**. `deliberate` means the site *announces itself*
— a `_legacy` name, an `@[deprecated]`, or a docstring saying convention-C /
comparison / historical. The 8 are three `_legacy` shims, two `gramEntry` sites,
`zC`, `zCsub`, and `EigenphaseCarrierVacuity.markovZ` (docstring: *"Convention-C
Markov parameter, as spelled in the content block"*, reproduced verbatim for a
vacuity proof). **Deliberate is evidence of intent, not a clean bill** — a
deliberate C object can still be cited as though it were D.

The split was **13/9 before a spot-check**, and the fix is worth recording
because it moved in the direction that matters. A bare `legacy` docstring marker
classified `markovZN` as deliberate — but its docstring reads *"Use this in new
code instead of `markovZN_legacy`"*, naming the legacy shim in order to steer
readers **away** from it. A live convention-C definition was being marked
already-handled. Bare `legacy` is now not a marker; a genuinely legacy
declaration carries `@[deprecated]` or `_legacy` in its own name, both still
matched.

**`markovZ` is five declarations across two conventions** — three C (in three
different spellings) and two D — plus `markovZax`, `markovZ'`, `markovZ_real`,
`markovZ_legacy` and `markovZW`/`markovZD`. One reader, one name, opposite
values: `z_C(q₀) = 0.49932…` against `z_D(q₀) = 0.61268…`.

## Correcting the bean's mechanism claim too

The bean says the hiding is "change of variable, not change of form", and that
"a grep-based detector cannot in principle catch it". That is true of **3** of
the 7 (`markovZ (u)`, `markovZax (u)`, `ClosedFormInterfaceFactors`'s `s`). The
other **4 write `Real.sqrt q` in plain sight** and are trivially greppable.

So the Lean surface is not invisible-in-principle. It is unscanned. Those are
different problems with different fixes, and only the smaller one needs the
answer-shaped test.

## What is already mitigated

`markovZ_legacy` carries `@[deprecated … (since := "2026-08-03")]` pointing at
`docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md`, and both √-variable
declarations document their substitution explicitly in their docstrings. The
corpus knew about part of this and was migrating it. What is missing is that the
migration's target (`markovZ (u)` with `u² = q`) **is still convention C** — the
Tier-2 move removed `Real.sqrt`, which was its stated goal, and did not change
the convention.

That is worth stating plainly: **a migration that makes a convention-C definition
generic-over-a-field makes it harder to see, not less C.**

## What is NOT claimed

- **Not** that the C theorems are wrong. They are correct **for C**, as the bean
  says. Reconciling them means re-deriving under D, not substituting `s² = q`.
- **Not** that any production number is wrong. `ClosedFormInterfaceFactors`
  *looks* like formal backing for the production deuteron figure, but no
  citation of it as D-backing has been demonstrated — that is the hazard, and it
  is unmeasured here.
- **Not** a count of the `.lean` C surface beyond the Markov parameter. Other
  convention-C quantities may exist in Lean; this audit narrowed to `z`.

## Fix, re-prioritised

1. ~~Correct the AGENTS.md all-clear~~ — **there is none**; instead, record that
   the producer audit is Python-only so `.lean` is uncounted. Done in this PR.
2. Something must scan `.lean` for the Markov-parameter shape, including the
   `u/(u²+1)` / `s/(s²+1)` square-root-variable forms. Not the producer audit —
   wrong tool, wrong tree.
3. Reconcile the five `markovZ` declarations. Re-derive under D; do **not**
   substitute `s² = q`.
4. Prefer the answer-shaped test (`(q²+1)` divides the Markov-peel denominator)
   for the 3 disguised sites; plain grep suffices for the other 4.
