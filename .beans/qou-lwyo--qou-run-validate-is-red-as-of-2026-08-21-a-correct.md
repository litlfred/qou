---
# qou-lwyo
title: 'QOU run-validate is RED as of 2026-08-21: a correct de-laundering deleted a definition''s Lean sibling, and lake build cannot see it'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:53:13Z
updated_at: 2026-08-22T22:59:28Z
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


## Scoping pass 2026-08-22 — the instance is NOT closeable in a session, and the probe backing it has three defects

Corpus-grep run first (all five paths). `QOU.LiftingDescent.QOUInstance` exists
**nowhere** in the tree — only in the block's own `lean.ref`. A multiline grep for
any `MotivicGaloisCharacter` instance finds exactly one, the `ℤ` trivial witness
added on #5462. So the item is genuinely open; nothing has quietly closed it.

(Note on method: my first grep for instances was line-based and found **zero**,
because the declaration spans two lines. Same instrument-blindness class as the
`re.MULTILINE` miss earlier today. The multiline re-run is the real number.)

### Why it cannot be closed here

The class now demands two fields, not one (#5462):

    frobenius_at : Nat.Primes → Mhat
    frobenius_realize_ne_zero : ∀ p, Nontrivial (Target (Place.finite p)) →
                                  sub.realize (Place.finite p) (frobenius_at p) ≠ 0

A genuine QOU instance therefore needs, in Lean: the **Habiro ring** (inverse
limit of `ℤ[q]/(q;q)_n` — not in Mathlib), the evaluation ring hom to
`ℤ[ζ_{2p}]`, the atomic Markov trace as an element of it, and non-vanishing
**for all p**. Items 1-3 are infrastructure; item 4 is the content the deleted
axiom was laundering.

**The tempting shortcut is banned and I am recording it so nobody re-derives it.**
Wrapping the Habiro data in a `HabiroFrobeniusData` structure and projecting the
instance out of it satisfies §3b-cond items 1-4 and **fails item 5**: the carrier
would hold the *conclusion* (`frobenius_at` + its non-vanishing) rather than the
*hypotheses*, making the instance a vacuous self-assuming projection. That is the
same laundering `73a21ac34a` removed, under a different spelling.

### What the cited probe actually establishes

`computations/probes/habiro_frobenius_probe.py` → 5 atoms × 9 primes
(p ∈ {2,3,5,7,11,13,17,19,23}).

**Good, and directly relevant to the new Prop field:** `frob_num` is **nonzero at
45/45**. The non-vanishing `frobenius_realize_ne_zero` demands is empirically
supported everywhere it has been measured — for 9 primes, not ∀ p.

**Defect 1 — the probe reads a `_deprecated/` witness.** Its input resolves to
`computations/_deprecated/habiro-coefficients-atomic-fast.witness.json`, while
live per-atom witnesses exist for exactly those five atoms
(`habiro-coefficients-{proton,neutron,deuteron,tritium,helium-3}.witness.json`)
plus a live aggregate at `computations/habiro/habiro-coefficients-atomic.witness.json`.
The block's `.ts` carries `computation.status: "verified"` on that chain.

**And re-pointing is not a free fix** — the deprecated file is *deeper*, not merely
older:

| atom | deprecated | live |
|---|---|---|
| proton | 10 | 9 |
| deuteron | 14 | 13 |
| tritium | 19 | 16 |
| ³He | 20 | 16 |
| neutron | 9 | 9 |

Fewer coefficients means the Pochhammer mechanism covers fewer primes. Which
generation is canonical is an owner/author call, not a mechanical repoint.

**Defect 2 — the witness's headline hides the test that fails.**
`summary.step2_all_atoms_compatible: true` is the **numerator-only** test
(`is_exact and num_trace_is_integer`). The same script also computes
`step2_full_trace_passed` (`is_exact and full_trace_is_integer and denom_unit`),
which is **False at 45/45** — every atom, every prime — and the top-level
`summary` does not surface it at all. A reader of `summary` concludes
compatibility; the stronger test never passes.

The failure is **structured, not noise**. For the proton, `frob_full` is missing
at p=3 (`denominator vanishes mod Phi_{2p}`); at the other eight primes the full
Galois trace is a **half-odd-integer**: −4/3, −1/4, then 1/2, −5/2, 3/2, −7/2,
5/2, −9/2 at p = 7,11,13,17,19,23. So at every prime past the Pochhammer range the
obstruction is a uniform factor of 2 — `2·Tr(full)` is an odd integer. That looks
like a normalisation, and is worth a probe of its own before anyone reads
`step2_full_trace_compatible: false` as a refutation.

**Defect 3 (cosmetic, but it misleads) — the `.md`'s stated finiteness mechanism
fires at only 3 of 9 primes.** The block says *"(u;u)_m vanishes for m ≥ 2p. This
forces the sum to terminate"*. With 10 proton coefficients that holds for p ≤ 5
(2p ≤ 10); at p ≥ 7 the witness records `exact_via:
habiro_expansion_terminated_cleanly` instead. Both routes are valid — but the
`.md` presents one as *the* reason and it is not what fires at two-thirds of the
primes.

### A hazard I raised and then refuted myself

I flagged the probe's disjunction

    terminated_clean = record.get("expansion_terminated_clean")
                    or record.get("reconstruction_matches")

as laundering a weaker tolerance-based flag under a termination-shaped name —
sharpened by the fact that the deprecated file carries only the first key and the
live files carry only the second, so a currency fix would swap which disjunct
fires. **That concern is wrong.** Reading the producer
(`_habiro_coefficient_extract.py:220-222`): `recon_matches = (diff == 0)` with
`diff = sp.expand(reconstruct(coeffs, u) - p_u)` — **exact symbolic** equality with
zero remainder, not agreement to tolerance. A nonzero `a_m` beyond the listed
range would break it. So `reconstruction_matches` is at least as strong as
`expansion_terminated_clean` and the `or` is sound.

Recorded because I reached the wrong conclusion by inferring semantics from a
field *name* — the precise error class the arity-conflation rule exists for —
and only caught it by opening the producer.

### Next honest step

Not a repoint and not an instance. Either (a) settle which Habiro generation is
canonical and refresh the probe, or (b) probe the uniform factor-of-2 in the full
Galois trace, which is the one lead here with a visible pattern. The Lean
instance stays open behind the Habiro-ring infrastructure.


**Correction to the Defect-3 paragraph above (same session):** the "uniform factor
of 2 / `2·Tr(full)` is an odd integer" claim is **proton-only and wrong as
written** — the neutron is uniformly 4 and the composites run 8→128. Corrected
measurement and the (better) replacement finding — the obstruction is 2-adic at
every prime except p = 2 — are on `qou-iph3`.
