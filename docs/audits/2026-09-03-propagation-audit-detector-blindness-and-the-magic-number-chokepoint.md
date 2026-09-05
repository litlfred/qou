# The conjectural-propagation audit was over-reporting, and the residue is one edge

**Date:** 2026-09-03 · **Beans:** `qou-prop3b` · **PRs:** litlfred/folio-assistant#162, litlfred/qou (this branch)

## Summary

Two findings, one mechanical and one about content.

1. **The audit's `lean.ref` resolver was wrong, and it made three conjectures
   look un-axiomatised that already carried the exact `class` it was looking
   for.** Fixed in folio-assistant#162. Violators 34 → **29**;
   class-axiomatised conjectures 147 → **165**.
2. **The remaining 29 are real, and 17 of them funnel through a single
   `uses[]` edge into a conjecture whose own narrative refutes its own
   title.** That conjecture must *not* be class-axiomatised; doing so would
   launder a measured negative into a Lean hypothesis that discharges 17
   provable blocks.

## 1. The resolver defect

`isClassAxiomatised` resolved a conjecture block's Lean two ways: the sibling
`.lean`, then `<lakeRoot>/<Decl/Path>.lean`. Route (2) appends the
**declaration name** as a final path segment — but a `lean.ref` is a
*namespace-plus-declaration* path, not a file path, so it resolves only when
the file is named after the declaration it holds.

Measured on `content/quantum-observable-universe` (3516 blocks): route (2)
resolved to a **non-existent file for all seven** conjectures then reported as
blocking.

| conjecture | route (2) resolved to | reality |
|---|---|---|
| `gs-graded-markov-trace-existence` | `QOU/IwahoriHecke/MarkovTrace/GradedMarkovTraceExistence.lean` — absent | **`class` at `QOU/IwahoriHecke/MarkovTrace.lean:93`** |
| `kashaev-surreal` | `QOU/AppendixSurreals/KashaevSurreal.lean` — absent | **`class` at `QOU/AppendixSurreals/Conjectures.lean:463`** |
| `tower-geometric-lower-bound` | `QOU/Mass/LevelSelection/TowerGeometricLowerBound.lean` — absent | **`class` at `QOU/Mass/LevelSelectionLogarithmic.lean:48`** |
| `magic-numbers-from-q` | `QOU/AtomicMass/magic_numbers_from_q.lean` — absent | `QOU/AtomicMass/MagicNumbersFromQ.lean`, genuinely no class |
| `b1-hyperbolic-rows-theorem` | absent | `QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean`, genuinely no class |
| `shell-transition-knot` | absent | declaration `stability_pairs_correct` not located anywhere in the Lake tree |
| `im-q-physical-role` | absent | genuinely no class |

The fix adds route (c) — locate the file that actually *declares* the ref's
final segment by searching the package's Lake root. That is candidate (3), the
grep fallback, of the resolution order `AGENTS.md` §0a already specifies; the
audit implemented only (1) and (2).

**The number moved far less than the false-positive count, and that is the
point.** Those three conjectures accounted for **22 conjecture-instances** but
only **5 violator blocks**, because most affected blocks are independently
blocked by a genuinely un-axiomatised conjecture in the same cone. This is a
correction to the audit's *reasons*, not a way to make a number go down.

## 2. What the remaining 29 actually rest on

| blocking conjecture | violators |
|---|---:|
| `conj:magic-numbers-from-q` | **17** |
| `conj:b1-hyperbolic-rows-theorem` | 7 |
| `conj:shell-transition-knot` | 4 |
| `conj:im-q-physical-role` | 1 |

**All 17 reach `conj:magic-numbers-from-q` through exactly one edge.**
`conj:diagrammatic-double-magic-lr-fusion` is the *only* block in the corpus
listing it in `uses[]`. Every one of the 17 paths ends:

```
… -> conj:diagrammatic-double-magic-lr-fusion -> conj:magic-numbers-from-q
```

Two representative full paths:

```
def:three-calibration-discipline
  -> prop:calibration-cohomology-alignment
  -> prop:prolonged-periods-fixed-depth
  -> prop:binding-genfun-qdifference
  -> conj:binding-manybody-eq-jet-filtration
  -> prop:magic-A-binding-formula
  -> conj:diagrammatic-double-magic-lr-fusion
  -> conj:magic-numbers-from-q

thm:binding-closure-conditional
  -> conj:binding-manybody-eq-jet-filtration
  -> prop:magic-A-binding-formula
  -> conj:diagrammatic-double-magic-lr-fusion
  -> conj:magic-numbers-from-q
```

## 3. Why `conj:magic-numbers-from-q` must NOT be class-axiomatised

Its title, until this PR, read *"Wedderburn nuclear character signal at $q_0$
is **elevated at the magic numbers**"*. Its own scope section records three
measurements against exactly that reading, each obtained by re-running the
producer over the full range $Z \le 32$ rather than at the magic $Z$ alone:

- **The sign of $\delta^2\Phi$ is a parity test.** Over $Z = 3 \ldots 31$ at
  $K = 10$, $\delta^2\Phi(Z) > 0$ holds precisely when $Z$ is even, with no
  exceptions. Every magic number is even, so the positivity property is
  satisfied by every even $Z$ and distinguishes none of them.
- **The magic numbers are not maxima.** The local maxima over even $Z$ are
  $Z \in \{4, 12, 16\}$ — none magic — and the global maximum is $Z = 12$.
  The magic $Z = 8$ ranks sixth of the fourteen even $Z$ in range.
- **No $q$ repairs it.** Sweeping $1 < q < \varphi$ (49 points, $K = 8$),
  $Z = 20$ and $Z = 2$ are local maxima at **no** sampled $q$; the parity
  property itself holds only for $q \lesssim 1.16$.

The block's own conclusion: *"What survives is the construction and its
$q$-dependence, not the identification."*

So a `class` carrier here would have to encode *some* content, and the only
sharply-stated content available is the identification the block itself
measured and refuted. Writing that as a Lean `class` and then discharging 17
provable blocks against it is the laundering `AGENTS.md` §1a bans — the audit
number would fall from 29 to 12 while the corpus got *less* honest.

Note also that the audit checks only **half** of §3b-cond. §3b-cond requires
both a class *and* an explicit `[Instance]` hypothesis on each downstream
block's Lean. Satisfying only the half a detector can see is the definition of
audit-dodging.

### What was done instead

The title is corrected to the block's own opening sentence — *the signal is
conjectured to carry nuclear shell structure* — which is the claim that
survives its scope section. No body text changed. An `authorNotes` caveat
records the retitle and this determination.

### What is left open

Two dispositions would genuinely clear the 17, and both are content decisions
rather than refactors:

- **State the surviving conjecture precisely enough to axiomatise.** The block
  says *"whether some other functional of the same Hoefsmit data carries shell
  structure is open"*. An existential over unspecified functionals is not a
  class field; someone has to name the functional class.
- **Retarget the choke-point edge.** `conj:diagrammatic-double-magic-lr-fusion`
  is stated for $Z, N \in \mathfrak{M}$ — the *empirical* magic set — and for
  the support of the categorical mass on a single self-conjugate partition,
  which it gets from `prop:categorical-neutrality-saturated-shells`. It is not
  obvious that it needs the $q$-derivation of $\mathfrak{M}$ at all. If it
  does not, the edge is mis-aimed and all 17 clear at once. Deciding that is a
  physics judgement about what the LR-fusion conjecture quantifies over.

Neither is attempted here.

## 4. Correction to my own earlier measurement

An earlier pass in this session reported "34 → 29, five detector false
positives" and attributed the mechanism to *"a Lean namespace is not a
directory"*. The count was right and the mechanism was not sharp enough: the
resolver appends the **declaration name** as a path segment, which misses every
conjecture whose declaration lives in a file named after its module. That
applies to **all seven** blocking conjectures, not five — the five is the
number of *blocks* that clear, which is much smaller for the reason in §1.

A second self-correction: a hand-rolled regex graph built during this
investigation reported `NO PATH` from every one of the 17 to the conjecture.
That was the parser, not the graph — re-run through the audit's own
`loadBlocksUnder`, every path resolves. Paths in §2 are from the authoritative
loader.
