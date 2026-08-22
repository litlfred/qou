---
# qou-lwyo
title: 'QOU run-validate is RED as of 2026-08-21: a correct de-laundering deleted a definition''s Lean sibling, and lake build cannot see it'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:53:13Z
updated_at: 2026-08-22T09:11:19Z
---

`bun run scripts/run-validate.ts content/quantum-observable-universe` exits
**non-zero** on current `main`. One error, four warnings; UGB and Fred2005 are
both **0**. Verified on a pristine `origin/main` worktree, so it is not a
branch artifact.

```
✗ [qou-motivic-galois-instance]: Definition "def:qou-motivic-galois-instance"
  requires Lean formalization. Expected sibling file:
  .../mass-endomorphism/qou-motivic-galois-instance.lean
  (or Lake-tree resolution from lean.ref
   "qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar")
```

## The cause is a good commit, and that is the point

`73a21ac34a` (2026-08-21 20:08) deleted
`mass-endomorphism/qou-motivic-galois-instance.lean` because it had **three
type mismatches, a bare `axiom` on line 87, and had never compiled**. It also
demoted `almost_everywhere_nontrivial` from a `MotivicGaloisCharacter` class
field to a standalone theorem, so instances stop being forced to "either prove
it or launder an axiom". That is textbook de-laundering and it should stay.

The block is a **`definition`**, where the Lean sibling is *enforced*. Deleting
the sibling made the `lean.ref` unresolvable, and the whole paper's content
validation went red.

**The commit's verification could not have caught it.** It records
`lake build QOU.LiftingDescent: exit 0, 3139 jobs, sorry-free` — correct, and
blind to this: the broken thing is a **content-pipeline** constraint, not a Lean
one, and the deleted file was never in the Lean build to begin with. Two
verification surfaces, and the failure landed in the one that was not run.

This is the mirror of the sibling-masking hazard recorded on `qou-2u26`: there,
a co-located sibling stub **hides** a dead library ref from every gate; here,
**deleting** the sibling exposes one, paper-wide and immediately.

## Repointing is not available — I checked

The obvious cheap fix is to aim the ref at the replacement. It does not exist.
`lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean` declares
**five theorems** about the perpetual obstruction —
`galois_trace_not_unit`, `perpetual_obstruction_from_trace`,
`qou_proton_perpetual_obstruction`, `qou_deuteron_perpetual_obstruction`,
`perpetual_obstruction_from_collapse_invariant` — and **zero `instance`**.

The block is titled *"QOU `MotivicGaloisCharacter` instance via Habiro
$\to \mathrm{Frob}_p$"*. None of those five is that instance. Pointing the ref
at one would put a block's label on a declaration proving something else — the
mislabelling failure `qou-2u26` is already tracking, committed deliberately.

Dropping the `lean` field does not work either: the constraint is on a
*definition having resolvable Lean*, not on the field being present, so the
error persists.

## What is actually left

Write the instance: `frobenius_at : Nat.Primes → Mhat` for the QOU substrate,
from the Habiro evaluation $\mathrm{Frob}_p = f(u)|_{u=\zeta_{2p}}$. The
computational side already exists —
[`habiro_frobenius_probe.py`](https://github.com/litlfred/qou/blob/main/computations/probes/habiro_frobenius_probe.py)
plus a 57 KB witness, marked `status: "verified"` on the block. Formalising it
is real mathematics and **must not be discharged with a trivial instance**;
that is exactly what `73a21ac34a` removed.

Until it is written, the honest state is that a `definition` wired into the
paper asserts a Lean instance nobody has built, and the red is the corpus
correctly saying so. Two blocks depend on it — `…-per-cell` (`example`) and
`…-verification` (`remark`) — both non-provable kinds, so no §3b propagation
breach.

**Decision for the owner.** Either (a) it gets formalised, or (b) the red is
accepted as a standing honest signal and every branch keeps stepping over it.
It is nine hours old, not nine days; but it is paper-wide, and it is already
being reported as inherited noise in at least three separate sessions —
including twice by me before I read the commit.

## Follow-on

The narrative's own status note is now stale in the other direction: the `.md`
says *"Lean status (2026-08-12): the co-located `.lean` file … has been
deleted"*, describing an **earlier** round. The file `73a21ac34a` deleted today
is a different one, and the note reads as if today's deletion were already
accounted for. Worth a line when this is next touched.


## The label test was run, and it agrees

The decisive test from `qou-2u26` — *does any Lean declaration carry the
block's own `\label`?* — is the one that repaired `thm:su2-emergence`,
`def:mass-identity`, `def:ns-regular-qou` and `prop:descent-eigenspaces`, each
time by finding the right declaration hiding under a wrong name. Run here:

```
grep -rln 'def:qou-motivic-galois-instance' --include=*.lean content/
→ (no matches)
```

**No `.lean` anywhere under `content/` carries this block's label** — not the
library tree, not any chapter directory. So the one route that has produced a
cheap repoint four times produces nothing here, which is the expected answer if
the declaration genuinely does not exist rather than merely being misnamed.

That closes the three cheap dispositions: no resolvable ref target (the named
decl was deleted), no label-carrying decl to repoint to, and no relief from
dropping the field. Writing the instance is what is left.


---

## The disposition above is wrong — writing the instance would be laundering

I recorded "what is left is writing `frobenius_at : Nat.Primes → Mhat`" as the
remaining work. **That is the third wrong disposition I have given this block,
and this one would have made things worse rather than merely wasting time.**
Read the class:

```lean
class MotivicGaloisCharacter
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)]
    [MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat) where
  frobenius_at : Nat.Primes → Mhat
```

**One data field. Zero Prop fields. No law of any kind.** So
`⟨fun _ => 0⟩` inhabits it, and *any* instance is vacuous by construction —
nothing constrains `frobenius_at` to be a Habiro evaluation, a Frobenius
eigenvalue, or anything at all. Writing the instance the block asks for is
exactly the move `73a21ac34a` set out to eliminate.

It was not always so. At `73a21ac34a^` the class carried a second field:

```lean
  almost_everywhere_nontrivial :
    ∃ N : ℕ, ∀ p : Nat.Primes, (p : ℕ) ≥ N → ¬IsUnit (frobenius_at p)
```

That was its **only** law, and removing it was right on its own terms — the
perpetual obstruction is now a theorem (`perpetual_obstruction_from_collapse_invariant`,
Route A, sorry-free), not an axiom instances must fill. The side effect went
unnoticed: the class it left behind asserts nothing.

The docstring has not caught up either. It still says the fields encode local
Frobenius characters *"satisfying a compatibility with the realization tower of
the substrate"* — a property that is **not encoded**, which is the
`proof-claims-unencoded` shape in AGENTS.md §3b-tax.

## A second consequence, in the downstream theorem

`motivic_perpetual_obstruction`
([`MotivicPerpetualObstruction.lean:47`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstruction.lean))
takes the class as a hypothesis and **never uses it**:

```lean
theorem motivic_perpetual_obstruction
    … [hχ : MotivicGaloisCharacter K0 Mhat Target motiveA]
    (trace : Nat.Primes → ℤ) (N : ℕ)
    (h_bound : ∀ p, (p : ℕ) ≥ N → 1 < (trace p).natAbs) :
    ∃ S : Finset ℕ, ∀ p, (p : ℕ) ∉ S → ¬IsUnit (trace p) :=
  perpetual_obstruction_from_trace trace N h_bound
```

`hχ` appears in the binder and nowhere else. `perpetual_obstruction_from_trace`
takes no instance argument — checked. And the conclusion is about the free
variable `trace : Nat.Primes → ℤ`, which is **never linked** to
`hχ.frobenius_at : Nat.Primes → Mhat`: different types, no map between them, no
hypothesis relating them.

So the docstring's claim — *"For a substrate carrying a `MotivicGaloisCharacter`
whose Frobenius eigenvalues satisfy a trace-growth bound … the Frobenius
eigenvalue is not a unit"* — is not what is proved. What is proved is that an
integer-valued function eventually exceeding 1 in absolute value is eventually
not a unit, which holds for **any** integer function and mentions no motivic
structure. `K0`, `Mhat`, `Target`, `MotivicSubstrate`, `motiveA` and
`MotivicGaloisCharacter` are all decoration on that statement.

This may be deliberate — the class as a context marker rather than an
assumption. But a theorem whose prose says it is *about* a structure, while its
statement is independent of that structure, is the mismatch, not the binder.

## Revised disposition

Not "write the instance". In order:

1. **Give the class a law, or stop calling it a carrier.** Either encode the
   realization-tower compatibility the docstring already promises, or drop the
   promise from the docstring and accept that this is a data bundle, not an
   axiomatisation. Until then no instance can mean anything, and the `definition`
   block's paper-wide red is the corpus correctly refusing to accept a claim
   nothing backs.
2. **Decide what `motivic_perpetual_obstruction` is for.** Either link `trace`
   to `hχ.frobenius_at` through a hypothesis so the theorem earns its name, or
   drop the inert binders and let it be the arithmetic lemma it is.
3. Only then does an instance become the remaining work.

Both are design calls on another session's file (`73a21ac34a`, beans qou-f7na /
qou-janl, neither of which exists in `.beans/`). Recorded, not acted on.

`73a21ac34a` remains a good commit — it removed a file with three type
mismatches and a bare axiom that had never compiled. These are consequences it
did not notice, and its `lake build` could not have shown either: a law-free
class compiles, and an unused hypothesis compiles.
