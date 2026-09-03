---
# qou-cxjq
title: 'ROAST: convention C survives in Lean under a square-root variable — the 2026-08-10 all-clear is false'
status: completed
type: task
priority: normal
created_at: 2026-08-26T05:27:06Z
updated_at: 2026-08-26T16:10:48Z
---

Found by the F1 agent (`qou-39bx`) while tracing where the deuteron's 27%
lives. Verified independently by me before recording.

## The finding

`content/quantum-observable-universe/lean/QOU/Hecke/ClosedFormInterfaceFactors.lean`
lines 14-20, verbatim:

    To avoid `Real.sqrt` (which would cross the substrate->archimedean wall),
    everything is stated in the square-root variable `s` with `q = s^2` [...]
      z = s/(s^2+1) = 1/(s + s^-1)

`s/(s^2+1)` with `q = s^2` IS `sqrt(q)/(q+1)`. **That is convention C**, excised
by owner ruling R1 on 2026-08-15 and again on 2026-08-09.

Meanwhile `QOU/MathlibExt/MarkovBondRule.lean` exports:

    /-- The convention-D Markov parameter `z = q^3/(q^2+1)`. -/
    noncomputable def markovZ (q : R) : R := q ^ 3 / (q ^ 2 + 1)

**Two Lean modules. One name `markovZ`. Opposite conventions. Both live.**

The detector sees NEITHER: `scripts/convention-c-producer-audit.py` reports 7
actionable, all in `computations/`, zero in `.lean`.

## THE ROAST

**1. AGENTS.md states an all-clear that is false, and states it twice.** It
records the 2026-08-10 drain as `0 in .lean/.ts, which the drain did clear`.
It did not clear. A file whose own docstring says "convention C" in plain
English sat there through the drain, through R1, and through every subsequent
count. Every re-measurement since has been reported against a surface that was
never actually scanned.

**2. This is the FOURTEENTH spelling**, and the taxonomy predicted it.
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues thirteen
detector-blind spellings, *four of which were found by detectors written to
catch the previous blind spot*. We knew the class was open and kept quoting the
count anyway.

**3. It hides by CHANGE OF VARIABLE, not change of form.** Every detector to
date greps the shape of `z` in `q`. This one is algebraically identical to C
and lexically shares nothing with it -- no `sqrt`, no `q+1`, no half-power. A
grep-based detector cannot in principle catch it. **The counter-move already
exists in AGENTS.md and we did not apply it**: *"test the ANSWER, not the
source"* -- the Markov peel's deuteron denominator factors as
`192*q^23*(q^2+1)^3` under D, one `(q^2+1)` per peel, and C cannot produce it.
A value cannot be re-spelled.

**4. The specific cost is not hypothetical.** This module *looks* like the
formal backing for the production deuteron number that F1 just spent a session
proving is a parameter-free failure. Its theorems are correct FOR C. If anyone
had cited them as D-backing, the +27% analysis would have been built on a
different convention than the compute it describes.

**5. My own reporting is implicated.** I quoted "7 actionable, zero in .lean"
to the owner earlier this session as a measured fact. It was measured, and the
measurement was against a surface with a hole in it. Measuring carefully with
an instrument you have documented as blind is not the same as measuring.

## Fix, in priority order

1. **Correct the AGENTS.md all-clear.** It is load-bearing -- agents read it and
   stop looking.
2. **Add the square-root-variable spelling to the detector**, and to the
   blindness taxonomy as #14.
3. **Reconcile the two `markovZ` definitions.** Do NOT substitute `s^2 = q` --
   the C theorems are correct for C and need re-deriving, not renaming.
4. **Prefer the answer-shaped test** (`(q^2+1)` divides the denominator) over
   any further source-shaped detector, per AGENTS.md's own guidance.


---

## RESOLVED — headline RETRACTED, two real findings replace it

**The bean's headline is wrong and I am retracting it.** AGENTS.md carries no
convention-C all-clear for `.lean`. Its single "**0** in `.lean`/`.ts`" claim
(line 1491) belongs to the **Λ vs Cl₂ / `Vol(4₁)` naming** guard — a different
defect class, a different drain, tracked as `qou-zdz5`. The convention-C section
quotes the producer audit's 26 and a separate `content/` grep, neither of which
is an `.lean` claim. Two adjacent passages, both about drains reported
"corpus-wide", conflated **by shape rather than subject** — inside a bean whose
whole subject is detector blindness.

**Finding 1 — the detector is Python-only, so no `.lean` count has ever
existed.** `convention-c-producer-audit.py` walks the tree four times and every
one is `rglob("*.py")` (lines 635, 760, 785, 930). Its numbers are correct and
correctly scoped; they are simply not about Lean, and nothing else covers Lean.
So this is an **absent** measurement, not a wrong one — which changes the fix
from "add a pattern to the detector" to "something must scan `.lean`".

**Finding 2 — 7 convention-C Markov-parameter sites across 6 `.lean` files, and
`markovZ` is five declarations spanning both conventions.** Three C
(`markov-trace-factorization`, `QBetaCategoricalPrecisionLadder`,
`HoefsmitV21CosSymmetrization`) against two D (`MarkovBondRule`,
`y-lambda-recipe-from-partition`). One name, opposite values:
`z_C(q₀) = 0.49932…` vs `z_D(q₀) = 0.61268…`.

**The mechanism claim also needed correcting.** The bean says a grep-based
detector "cannot in principle" catch this. True of **3** of the 7 (the
square-root-variable forms). The other **4 write `Real.sqrt q` in plain sight**.
The surface is unscanned, not invisible-in-principle.

**Worth carrying forward:** the Tier-2 migration that replaced `Real.sqrt q`
with a generic `markovZ (u : R)`, `u² = q`, **removed the square root — its
stated goal — and left the convention untouched and harder to see**. A migration
can deepen the blindness while succeeding at its own purpose.

**My own measurement discipline, recorded because it nearly shipped.** A first
shape-narrowed grep returned **66 files**. That was a topic-locator, not a
convention detector — most hits are a golden-ratio threshold, a residue
evaluation, or `q_half − 1/q_half`, which is `h` and not `z`. Every one of the 7
was opened and read before being tabled. Do not quote 66.

**Landed:** AGENTS.md convention-C section records the Python-only scope, the
measured Lean surface, and the non-existence of any `.lean` all-clear here or
elsewhere in the document. Taxonomy entry **#14** added — *"the file extension:
the tree the tool walks"* — the first entry that is an absent measurement rather
than a wrong one.

**Still open** (fix steps 2–4, not done here):
- Something must scan `.lean` for the Markov shape, including the
  `u/(u²+1)` / `s/(s²+1)` forms. **Not** the producer audit — wrong tool, wrong
  tree.
- Reconcile the five `markovZ` declarations. Re-derive under D; do **NOT**
  substitute `s² = q` — the C theorems are correct for C.
- Answer-shaped test (`(q²+1)` divides the Markov-peel denominator) for the 3
  disguised sites; plain grep suffices for the other 4.

**Not claimed:** that the C theorems are wrong, or that any production number is.
`ClosedFormInterfaceFactors` *looks* like formal backing for the production
deuteron figure, but no citation of it as D-backing has been demonstrated — that
is the hazard, and it is unmeasured.

Audit: `docs/audits/2026-08-26-convention-c-in-lean-and-the-markovz-overload.md`.


---

## Step 3 STARTED (owner said go). The structural gate is proved; migration under way.

**PR [#5828]. Branch restarted from main** — #5812 merged, so per the merged-PR
rule this is a fresh change on the same branch name (force-with-lease over
already-merged history only).

### The gate: conventions C and D are separated by the KERNEL'S RANGE

Both are built from one kernel `g u = u/(u²+1)` (the generic Tier-2 `markovZ`):

    z_C q = √q/(q+1)   = g(√q)
    z_D q = q³/(q²+1)  = q² · g(q)

`g` is bounded by `1/2` (from `0 ≤ (u−1)²`); `z_D q − 1/2` has numerator
`(q−1)(2q²+q+1)`, so `z_D q > 1/2` for every `q > 1`. Hence **for every q > 1 no
real `u` at all satisfies `g u = z_D q`** — D is outside the kernel's range, not
at a different point of it. They touch only at `q = 1`.

`QOU/BraidKnot/MarkovConventionSeparation.lean`, 9 declarations, `lean`-direct
exit 0, `#print axioms` = `[propext, Classical.choice, Quot.sound]` on all six
theorems, no `sorryAx`.

**Three consequences, in increasing order of work saved:**
1. *"Never substitute `s² = q`"* is now a **theorem**, not a caution.
2. **The Tier-2 migration baked C in structurally.** I had recorded it as
   "removed the square root and left C harder to see". It is stronger: the shape
   it migrated to has real range `[−1/2, 1/2]`, which **excludes** D for every
   `q > 1`. The generic form is not convention-neutral.
3. **The 9 `C-sqrtvar` sites cannot be repaired by re-instantiating** — the
   definition *shape* must change, from `g` to `q²·g q`.

### DESIGN DECISION — never mutate `markovZ` in place to mean D

The tempting migration is to edit each definition's body from C to D and stop.
**That is the defect this whole bean is about**, one turn later: it would
silently change what every existing theorem *name* means, which is exactly how
five `markovZ` declarations came to span two conventions. So:

- **A site with no dependent statements** may be migrated in place — but the
  convention must be **named in the docstring**, never left to be inferred from
  the formula.
- **A site whose theorems depend on it** does NOT get an in-place body swap. The
  C object keeps its name and its theorems (they are correct **for C**); D is
  introduced under a **distinct** name; convention-sensitive results are
  re-derived rather than renamed.

### Progress

Site 1/14 — `mass-theory/skein-polynomial-transfer-matrix.lean`
`tracedVolumeFromMatrix`. Chosen first as the pattern-setter because it is the
minimal case: **zero references anywhere in the tree**, and none of the file's
three theorems mentions it, so nothing silently changes meaning. Migrated in
place with the convention named and the separation theorem cited.

13 sites remain (5 `C-sqrtvar`, 8 `C-plain`), ~3,600 lines and ~115 theorems.
This is genuinely multi-tranche work; the count is measured by
`scripts/lean-markov-convention-audit.py --selftest`, which will drop as sites
land and whose `KNOWN_C` must be edited in the same commit that migrates a site.


## RESOLVED 2026-08-26 — actionable convention-C definitions in Lean: 14 -> 0

PR #5828 (branch `claude/isotope-mass-binding-dashboard-kdvhz6`).

**Step 1-2 (measure).** 22 convention-C *definitions* across 18 files, against
24 in convention D — roughly half the Markov-parameter definitions in the Lean
tree. Quote `defs`, not sites: the scanner reports 150 sites, but a `q³/(q²+1)`
in a proof *mentions* a convention while one in a `def` body *defines* it.
Triage 14 actionable / 8 deliberate. New instrument:
`scripts/lean-markov-convention-audit.py` (the Python producer audit is four
`rglob("*.py")` calls and structurally cannot do this).

**Step 3 (the gate, formalize-first).** `QOU/BraidKnot/MarkovConventionSeparation.lean`,
9 declarations sorry-free. Both conventions are built from one kernel
`g u = u/(u²+1)`: `z_C = g(√q)`, `z_D = q²·g(q)`. `g` has real range
`[−1/2, 1/2]`; `z_D − 1/2` has numerator `(q−1)(2q²+q+1)`, so `z_D > 1/2` for
every `q > 1`. Hence **no real `u` at all** gives `g u = z_D q` above `q = 1`
(`no_kernel_instantiation_is_conventionD`). Consequences: "never substitute
`s² = q`" is a theorem; the 2026-08-03 Tier-2 migration baked C in
*structurally* (the generic shape it migrated to cannot reach D); and a
`C-sqrtvar` site needs a SHAPE change, not a re-instantiation.

**Step 4 (migrate).** 13 sites migrated, `lean`-direct exit 0 and axiom-clean
on each. One scoped deliberate-C with its reason (`q-beta-cos-resummation` —
its result needs `z` bar-even, which D is not). One left C by design
(`BorromeanCanonicalTraceDerivation`, below).

### What was learned, beyond the count

- **D removes work.** It eliminates every `Real.sqrt` from the canonical Markov
  tower; `z_pos` collapses to `positivity`, and a deferred rpow-normalisation
  bridge collapsed to `field_simp; ring`.
- **Theorems do not survive; proofs do not need patches.** Bar parity is the
  recurring casualty: `z_C` bar-EVEN, `z_D` bar-COVARIANT of weight −4
  (`z_D(1/q) = z_D(q)/q⁴`). Killed the bar-antisymmetry result in
  `q-beta-cos-resummation` and the named `markovZ_bar` in
  `ClosedFormInterfaceFactors`. Independently corroborated from the p-n side by
  `qou-1oxx`.
- **Two defects found that the convention change did NOT cause.**
  (1) `ClosedFormInterfaceFactors` called `z − h/2` "the bar-invariant average"
  using "bar" for two different involutions (`q ↦ q⁻¹` vs crossing reversal
  `σ ↦ σ⁻¹`); it is invariant under NEITHER convention for the first, so the
  epithet was wrong under C too. (2) Taxonomy #15: the detector could not see
  `instance` field assignments, hiding `markovTraceTower_canonical` — the
  canonical tower. The count went UP, 17 -> 18.

### The last site: deliberate, not migrated

`BorromeanCanonicalTraceDerivation.zMarkov` stays C. The file derives the C
value so `conventionD_ne_conventionC` has something to compare against; its
`wden`/`wnum*` are the solution of the 3×3 Markov system at THAT `z`. Fixed at
the source (the definition now announces itself) rather than by widening the
scanner. Taxonomy #8/#16: intent stated in a module header or on a downstream
consumer is outside a walk-back window by construction.

**A near-miss recorded in full** (`docs/audits/2026-08-15-detector-blindness-taxonomy.md`
entry 8): that file's "convention D" is given as the TL/Jones weight triple, and
reading `1/[2]` off its shape gives `q/(q²+1) = 0.49729`, not D's `0.61269` —
a complete Lean-backed argument that the corpus uses "convention D" for two
different objects, with a live mis-citation in `qou-mass` downstream. **It is
wrong.** The `z` those weights actually imply, against the character values the
file itself uses, is `(q³+q)/(q+q⁻¹)² = q³/(q²+1)` — exactly D. Verified in
exact sympy both directions before writing anything down. Nothing in the corpus
is wrong.

### Not closed by this bean

- `qou-cds1` — the `c_k` ladder's NUMERICAL re-derivation under D lives in the
  Python producers (`qbeta_ck_cache.py`). `QBetaCategoricalPrecisionLadder` now
  *compiles* under D, which is much weaker than it sounds. Every `c_k`
  conclusion stays C-conditional.
- `ClosedFormInterfaceFactors` is still written in `s` with `q = s²`. That
  apparatus existed solely to spell `√q` without `Real.sqrt`; D has no square
  root, so it is vestigial. Rewriting 22 theorems in `q` is a separate change.
