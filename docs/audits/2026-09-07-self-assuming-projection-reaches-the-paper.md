# The self-assuming projection reaches the paper — and the class surface is honest

**Date:** 2026-09-07 · **Bean:** `qou-9yt9` · **PR:** litlfred/qou#6987

Follow-on to the axiom tranche of #6933 (twenty-one axioms removed: eleven
false, eight vacuous, one shadowing, one collapsing). That tranche drained the
`axiom` surface. This one asks the same two questions of the **conditional
class** surface, which no axiom gate can see, and gets opposite answers.

## The two questions, and the answers

| | axiom surface (#6933) | class surface (this) |
|---|---|---|
| **Is it vacuous?** — would Lean close it unaided | 8 of 112 yes | **0 of 27 yes** |
| **Does it reach the paper?** | not measured | **8 content blocks** |

The class surface is **not** vacuous, and that is the useful negative. Its
problem is *visibility*.

## Why a conditional class is invisible

    class C (args) : Prop where
      field : P
    theorem P_holds (args) [hi : C args] : P := hi.field

Zero axioms, zero sorries. `#print axioms` on `P_holds` is clean.
`scripts/lean-axiom-guard.py` counts nothing; the vacuity detectors see a
theorem with a real proof term. The unproved assertion has moved into the
**signature**, where no axiom gate looks.

`scripts/lean-cited-not-proved-audit.py` already knows this — it is the third
of its three categories, and its own docstring calls it *"the category a reader
is most likely to mistake for a proof."* Its live figures, re-measured today at
`<working tree>` (3711 files):

    REAL `sorry` TERMS         10   (10 cited, 0 uncited)
    REAL `axiom` DECLARATIONS 112   (110 cited)
    CLASSES                   992 declared, 344 inhabited, 648 with NO instance

So the class category is ~6× the axiom category. Nothing here re-derives that;
it was already measured, and re-deriving it is what the corpus-grep checklist
exists to prevent. What follows is what was *not* measured.

## 1. The class hypotheses are not vacuous barriers

`scripts/lean-class-hypothesis-vacuity-probe.py` — the class analogue of
`lean-axiom-provability-probe.py`. For each self-assuming candidate: delete the
instance binder naming the class, replace the body with a short tactic block,
compile. Exit 0 means Lean proves the conclusion outright and the class was
standing in for nothing.

**Result: 0 of 27 scored candidates provable.** `FAIL=27, SKIP=14, NOBASE=0`.

Read the direction correctly. A PASS is a proof; a FAIL is evidence of nothing
— the tactic list is deliberately short, because a long one turns the probe
into an unbounded proof search whose failures say nothing. So this is **not**
"the 27 claims are hard". It is "none of them is trivially free", which is what
distinguishes them from the eight vacuous axioms of #6933.

Two properties of the measurement, both load-bearing:

- **Every probe compiles the file UNCHANGED first.** A file that is red before
  the probe touches it — a missing olean, a red import — would fail in the
  direction that reads as *"the class is load-bearing"*, which is the
  comfortable answer. `NOBASE=0` says no verdict here is environmental.
- **The 14 SKIPs are a coverage statement, not a gap.** They are the
  explicit-structure-argument idiom (`theorem f (S : Bundle) : P := S.field`),
  which has no instance binder to delete. That idiom is also the one that does
  **not** hide: an explicit argument must be supplied by name at the call site,
  while an instance binder is inferred silently. The probe covered the hiding
  form and skipped the visible one.

## 2. Eight paper claims are backed by a projection

`scripts/lean-self-assuming-content-join.py` joins the 41 self-assuming
declarations against every `lean.ref` in `content/`.

**8 content blocks of provable kind** — 1 `theorem`, 6 `proposition`, 1
`corollary`, **zero `conjecture`** — have a projection as their formal backing.
Seven carry no §3b-cond item-3 conditional-banner signal.

| block | kind | md | banner |
|---|---|---|---|
| `categorical-self-duality` | proposition | 32 w | no |
| `quantum-observable-universe-exists` | proposition | 41 w | no |
| `strong-multiplicativity` (fred2005) | theorem | 55 w | no |
| `electron-period-base` | proposition | 79 w | no |
| `jet-prolongation-C` | corollary | 86 w | no |
| `flavor-dressed-mass-from-substrate-split` | proposition | 120 w | no |
| `categorical-jet-prolongation` | proposition | 212 w | **yes** |
| `sw-period-residue-sum` | proposition | 730 w | no |

### The banner column is phrasing, not honesty

`sw-period-residue-sum` scores **no** and its `.md` is the most carefully
scoped narrative in the set: it states what the enclosed pole set $E$ is, why
$E$ is not identifiable under the classical-jet rule, that the branch locus is
bar-symmetric so the unit circle is inadmissible, which prolongation remains
open, and it cites the beans (`qou-6v5l`, `qou-qx7j`). The regex is looking for
a banner *form* it does not use.

**Nothing is repaired on the strength of this table.** It is a candidate list
for reading, which is the same contract the underlying audit states for itself.

### Read one before you trust the list — `quantum-observable-universe-exists`

It looked like the sharpest case: a 41-word proposition asserting that
*"Setting $\mathbf{C} = \mathbf{Rep}(U_q(\mathfrak{sl}_2))$, $A =
\mathcal{O}_q(\mathrm{SU}(2))$, and $\tau$ the forgetful functor realizes the
axioms explicitly"*, whose Lean assumes `Nonempty (…)` and projects it.

It is not an over-claim. The block carries
`proofs: ["prf:quantum-observable-universe-exists"]`, and that proof block is a
worked narrative proof — the construction, four cited axiom lemmas
(`lem:qou-exists-axiom-1..4`), Woronowicz's Haar state, Chari–Pressley, Kassel
— concluding *"under the Chern-class hypothesis"*, with Tannaka–Krein named as
background and explicitly not re-proved. The Lean file's own docstring is
equally scrupulous: it records that the hypotheses are ring conditions rather
than a field, why `∀ k, [Field k]` was both too strong and too weak, and that
the remaining work is the Drinfeld–Jimbo representation category itself.

So this is the corpus's ordinary, honest posture: **proved in narrative against
cited literature, not proved in Lean, because the category is not in Mathlib.**
What is genuinely missing is one sentence on the *proposition's* `.md` saying
so. That is a follow-up, and it is a `.md` repair, not a Lean one.

## Corrections made before shipping, both mine

- **The join first reported 9, not 8.** It matched on the declaration's last
  name segment and paired `prop:quantum-universe-exists` with
  `QuantumObservableUniverse.exists_instance`. Both declarations are real and
  distinct — `QuantumUniverse.exists_instance` is at
  `quantum-universe-exists.lean:43` and is not self-assuming at all. The join
  now matches fully-qualified names. A defect would have been reported in a
  clean block.
- **"14 single-field classes are item-5 violations" was too strong**, and was
  the framing this tranche started from. Reading three of them
  (`SkeinMultisetInvariant`, `HasStrongDuality`, `FiberAdjointInvolutionContext`)
  shows honest §3b-cond carriers: documented openness, literature citations,
  and in the third case a docstring recording a *prior* repair of exactly the
  degenerate `∃ inv, True` shape. Field count does not decide this.

## What is not established

- That the 27 FAILs are hard. See the direction note above.
- That the seven no-banner blocks are over-claims. One was read and is not.
- Anything about the 648 uninhabited classes beyond the count, which is not
  new here.

## Files

- `scripts/lean-class-hypothesis-vacuity-probe.py` (new)
- `scripts/lean-self-assuming-content-join.py` (new)
- `scripts/lean-self-assuming-audit.py` (detector fixes landed in `e674c94003`)
