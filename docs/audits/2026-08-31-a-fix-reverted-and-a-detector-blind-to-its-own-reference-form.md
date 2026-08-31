# A fix, reverted; and a detector blind to the spelling its own docstring cites

**Date:** 2026-08-31 · **Beans:** `qou-z9ws` (vacuity arc), `qou-t9r1` / `qou-cxjq`
(convention arc) · **Surfaced by:** hand-adjudicating `VolumePerturbationContext`
during the self-assuming-projection drain.

---

## 1. `volume_perturbation` — the fix was made, then undone two days later, and the note explaining it was left behind

[`QOU/BraidKnot/volume_perturbation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/volume_perturbation.lean)
opens with a header that says, in its own words:

> *"The previous revision carried the perturbation identity as a class field
> `claim_perturbation_formula` and handed it back by projection
> (`def := ctx.claim_perturbation_formula`) — the self-assuming projection
> forbidden by AGENTS.md §3b-cond item 5. **This is corrected:** … The class
> `VolumePerturbationContext` now carries only **genuine data** … It does **not**
> carry the perturbation identity as a field."*

The live class, forty lines below that paragraph:

```lean
class VolumePerturbationContext where
  …
  perturbation_formula : ∀ k : ℕ, 4 ≤ k →
    δΦ k = z ^ 2 * Vol_41 * QOU.QInteger.qIntBalZ q ((k : ℤ) - 3)

theorem volume_perturbation [ctx : VolumePerturbationContext] :
    ∀ k : ℕ, 4 ≤ k → ctx.δΦ k = ctx.z ^ 2 * ctx.Vol_41 * qIntSym ctx.q ((k : ℤ) - 3) :=
  ctx.perturbation_formula
```

It carries the identity as a field and hands it back by projection. **The header
describes a state the file does not have**, and it is not merely stale — it
asserts the opposite of the code directly beneath it.

The history is the interesting part, and it is three commits:

| commit | date | what it did |
|---|---|---|
| `ee9b3cc9854` | 2026-08-12 | *"Resolve 4 refutable sorry gaps by adding upstream constraints"* — introduced the projection |
| `336f2970796` | 2026-08-21 | *"revert(lean): volume_perturbation — restore honest sorry, drop the assumed conclusion"* — removed it, and wrote the header quoted above |
| `53665e6326b` | 2026-08-23 | *"resolve last 3 refutable sorries — parity, volume, skein"* — **put it back**, and left the reverting agent's header in place |

So this is not a defect that was never noticed. It was found, diagnosed by name
(§3b-cond item 5), fixed, documented — and re-introduced two days later by a pass
working a different metric.

## 2. The mechanism: trading a refutable claim for an unrefutable one

The 2026-08-23 commit message states the method and the metric in two lines:

> *"All added upstream class field constraints, proved from them, **deleted
> `_unconstrained_false` refutations**. REFUTABLE category now at 0."*

Read against the prior state, that is a category change rather than a repair.
`parity_regime_selection.lean`'s deleted refutation had said so itself:

> *"**The statement above is refutable as written** — the class never relates the
> fields its conclusion names, so `∀ instances` admits ones that simply disagree.
> Not an open gap: the `sorry` cannot be discharged. **Fixing it means giving the
> class the hypotheses the derivation needs.** … This refutation is the evidence,
> not the fix."*

The old encoding *was* genuinely bad — a `sorry` that can never be discharged is
worse than nothing, and moving toward a class with real hypotheses was the right
direction. But what was added is not "the hypotheses the derivation needs"; it is
**the conclusion**, all four conjuncts verbatim, which §3b-cond item 5 names as
the one thing a conditional class may not carry. The theorem body became
`⟨ctx.sign_identity, ctx.odd_regime, ctx.even_regime, ctx.neutron_regime⟩`.

The trade, stated plainly: a **checkably false** statement became an **uncheckable
empty** one, and an audit category was driven to zero by relabelling its members
into a different category. Three files at once —
`parity_regime_selection`, `skein_mass_from_linking`, `volume_perturbation` — and
all three are in the self-assuming-projection ledger today.

**All three classes are unparameterised with free data fields, so all three are
vacuous**, witnessed in
[`2026-08-30-context-classes-hand-adjudicated.lean`](2026-08-30-context-classes-hand-adjudicated.lean).

**The honest disposition already exists, in this commit's own blast radius.**
`336f2970796` is exactly it: restore the real statement, discharge it with
`sorry` + a `-- Ref:` citation, and let the derived `has_sorry` status be the
honest "stated, not yet proved" marker (AGENTS.md §1a disposition 2). It was done
once for `volume_perturbation` and can be redone for all three. That is an
authorial call — it moves three theorems from "proved" to "stated" — so it is
recorded here rather than applied.

## 3. The convention-C detector was blind to the spelling its own docstring names

`volume_perturbation`'s class also carries

```lean
z_def : z = 1 / (Real.sqrt q + 1 / Real.sqrt q)
```

which is `√q/(q+1) = z_C` — **convention C**, under a field documented only as
"Markov parameter", in a file with no convention marker. Convention D has been
canonical since the owner ruling of 2026-08-15.

[`scripts/lean-markov-convention-audit.py`](../../scripts/lean-markov-convention-audit.py)
did not report it, and chasing that turned up a second, larger miss.

**The missed spelling is `Real.sqrt q / (1 + q)`** — convention C written the most
direct way there is. The module docstring names exactly that form as the reference
C-sqrtvar is measured against:

> *"`u/(u^2+1)` shares no lexeme with `sqrt(q)/(q+1)` and is algebraically
> identical to it."*

and no pattern matched it. Each existing pattern misses it for a different
reason: `RE_C_PLAIN` requires a square root in the **denominator** (here the
denominator is `1 + q`), and `RE_C_SQRTVAR` requires the same identifier top and
bottom via a backreference (here they are `Real.sqrt q` and `q`).

**Measured delta**, adding `RE_C_RATIONAL`:

| | before | after |
|---|---|---|
| C-plain defs | 5 | 10 |
| convention-C definitions | 17 | 22 |
| **actionable** | **0** | **2** |
| deliberate | 17 | 20 |

The two actionable sites are the same declaration twice —
`markov_parameter (q : ℝ) : ℝ := Real.sqrt q / (1 + q)` in
[`QBetaPerBlockChiClosedForms.lean:1038`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean)
and its content-block twin
[`qbeta-per-block-chi-closed-forms.lean:350`](../../content/quantum-observable-universe/mass-endomorphism/qbeta-per-block-chi-closed-forms.lean).
A **neutrally-named** `markov_parameter` valued at convention C is the `markovZ`
overload problem under a different name, and each file carries a sorry-free
theorem `markov_parameter_symmetric_form` asserting its C-symmetric form, so the
convention is stated and proved rather than merely implied. Disposition (rename
to `markovZC`, or migrate the value to D and re-derive what depends on it) belongs
to the convention arc, not here.

The other three new sites are deliberate: `zC` in
`GroundStateOrderingRefutation.lean` and `DecayLadderConventionDPositivity.lean`,
`markovZC` in `MarkovConventionSeparation.lean`. A sixth match,
`Real.sqrt 4 / (4 + 1)` in `MBetaV21Spectrum.lean`, is a numeric separation claim
inside a `≠`, not a definition.

This is **entry #23** in
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md),
and it has the family's signature: a detector reporting a clean result
(`actionable 0`) about a question it had not asked.

## 4. The guard was red on `main`, for the reason it exists to prevent

`--selftest` pins every recorded convention-C site so that a future narrowing of
the patterns cannot report a clean tree. It was **already failing on `main`**
before any change here, with three stale entries:

```
MISSING EigenphaseCarrierVacuity: expected (markovZ, C-plain), got [('markovZC', 'C-plain')]
MISSING HoefsmitV21CosSymmetrization: expected (markovZ, C-sqrtvar), got [('cosKernel', ...)]
MISSING q-beta-cos-resummation: expected (markovZ, C-plain), got [('markovZC', 'C-plain')]
```

These are the documented 2026-08-29 renames — `markovZ` → `markovZC` / `cosKernel`,
made so that bare `markovZ` means convention D uniformly. The renaming commits did
not update `KNOWN_C`. The file's own comment asks for precisely that:

> *"A site that is legitimately migrated should be REMOVED here in the SAME commit
> that migrates it, so the removal is reviewable — otherwise a narrowing of the
> patterns can report a clean tree, which is exactly how this surface stayed
> uncounted."*

Names corrected (the sites are unchanged); selftest now passes on all 18.

**Worth stating as its own point:** a red selftest is indistinguishable at a glance
from a red audit, so a guard that has been failing for two days on stale names is
a guard nobody reads. That is how the `actionable 0` above went unchallenged.

## 5. And `volume_perturbation` is in neither the historical 90 nor the live 14

The self-assuming-projection ledger's **90 genuine findings** do not include
`volume_perturbation`, and neither does the live run of
[`scripts/lean-self-assuming-audit.py`](../../scripts/lean-self-assuming-audit.py),
which reports **14** remaining candidates. Its body is `ctx.perturbation_formula`
— the same shape as `theorem_3_via_class := hyp.dualityGapZero`, which *is*
reported.

The mechanism is at line 185 of that script:

```python
if ftype and norm(ftype) == conclusion:
```

The verdict is a **whitespace-normalised string equality** between the class
field's type and the theorem's conclusion. Any re-spelling of the same
proposition defeats it. `volume_perturbation` differs on two counts at once: the
conclusion writes `ctx.δΦ`, `ctx.z`, `ctx.Vol_41` where the field writes the bare
names, and it writes `qIntSym ctx.q` where the field writes
`QOU.QInteger.qIntBalZ q` — `qIntSym` being an `abbrev` for exactly that. The
two are definitionally equal and textually different, and the detector decides on
the text.

**The population of such misses is UNMEASURED, and a number I can produce is not
that number.** A crude high-recall scan for "theorem whose entire body is a
single projection off an instance binder" finds **118** across `content/`. That
is *not* a miss count: it does not check that the projected field's statement is
the theorem's goal, and most of its hits are legitimate — data accessors
(`volumeInvariant := ctx.volume`), `summable`/`intervalIntegrable` side
conditions, Mathlib-style re-exports. Quoting 118 against 14 would be the exact
over-claim this arc keeps catching. What is established is one confirmed miss and
its mechanism.

**Why it matters for the arc's headline number.** This audit's companion measures
"52 of 79 context classes vacuous" against a denominator of 79 that comes from
the 90. If a projection written through an `abbrev` — or through a `ctx.` prefix
the field type does not carry — is invisible, then 90 is a floor and 79 is a
floor, and every ratio computed against them is an *underestimate* of the surface,
not an overestimate. Taxonomy entry **#24**.

Fixing it properly needs the elaborated statement rather than the source text —
`lean_diagnostic`/`#print` output, or unfolding reducible definitions before
comparing. A wider regex would not help: the difference here is semantic.

## Reproducing

```sh
python3 scripts/lean-markov-convention-audit.py --selftest   # 18/18, exit 0
python3 scripts/lean-markov-convention-audit.py | head -20   # actionable 2

git log --oneline -- content/quantum-observable-universe/lean/QOU/BraidKnot/volume_perturbation.lean
git show 53665e6326b   # the three-file re-introduction
```
