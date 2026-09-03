---
# qou-ju3e
title: 'DEFECT: GBResidueSpectralSum is a second zero-Prop-field carrier, in mass-theory'
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:27:51Z
updated_at: 2026-08-30T09:25:26Z
---

`content/quantum-observable-universe/mass-theory/gb-residue-spectral-sum.lean:87`

Found while fixing the same defect in `QOU/IwahoriHecke/MarkovTrace.lean`
(`GradedMarkovTraceExistence`, PR #6055). This is a **second instance of the same
class**, in a different chapter, and it was not swept into that PR because it is
mass-theory content rather than the Hecke cluster.

```lean
class GBResidueSpectralSum (R : Type*) [CommRing R] [LinearOrder R] where
  descended   : R
  levelBound  : ℕ
  q           : R
  roots       : Fin levelBound → RootOfUnity R
  gradedTrace : Fin levelBound → R
  ...
```

**Measured: zero `Prop` fields.** Every field is data — a ring element, a natural, a
function into `R`. So the class asserts nothing, and any tuple of the right shape
inhabits it. That is `proof-no-empty-prop-carrier` under AGENTS.md §3b-tax.

Its docstrings promise properties the fields do not encode — `gradedTrace` is
described as *"the value of `tr_M` descended to `J^ℓ / J^{ℓ+1}`"*, but nothing in the
class relates it to `tr_M`, to the filtration, or to `descended`. That is
`proof-claims-unencoded`.

**Not yet measured, and the first thing to do:** whether anything downstream takes
`[GBResidueSpectralSum]` as a hypothesis and concludes something. If so, those
conclusions are conditional on a class that constrains nothing, and the conditional
buys nothing — the shape of the `MarkovTrace` defect. The two greps run so far found
only docstring mentions in `QOU/BraidKnot/GBResidueSpectralSum.lean`; a real consumer
scan has **not** been run, so do not read that as "no consumers".

**The fix that worked on the sibling defect**, for reference: give the class `Prop`
fields carrying the properties its docstrings name (there: additivity, cyclicity, and
agreement with the trace at level 0); delete any instance that trivially inhabits it;
and prove one lemma showing the class now *buys* something, so the rebuild is not
itself decorative. Expect the honest outcome to be a content-bearing class with **no
instance** — which is what §3b-tax says an unproved primary should look like.

Do NOT fabricate content to make an instance exist.


---

## 🛑 RETRACTED — the headline claim of this bean is FALSE (corrected 2026-08-30, same session)

**What I asserted:** *"Measured: zero `Prop` fields. Every field is data … So the class
asserts nothing, and any tuple of the right shape inhabits it. That is
`proof-no-empty-prop-carrier`."*

**What is actually true:** the class has a `Prop` field, and it is the central one.

```lean
  spectral_decomposition :
    mass = |descended| + ∑ ℓ : Fin levelBound, residue ℓ
```

That is the content of `prop:gb-residue-spectral-sum`, stated in the class. The
`proof-no-empty-prop-carrier` classification is **wrong** and is withdrawn.

### How the measurement failed

The grep behind the claim was

```
sed -n '87,140p' "$f" | grep -nE "^\s+\w+ : .*(=|≤|<|∀|∃|Prop)"
```

which requires `name :` **and** the Prop-shaped body on the *same line*. This field
spans two: the name and colon on one, `mass = …` on the next. Zero hits, and I read
zero hits as zero fields. Re-measured with a parser that pairs each field name with
everything up to the next field, the field is found immediately.

That is the multi-line blind spot from the detector-blindness taxonomy, committed while
writing a bean *about* a detector-visible defect class. **Absence of a grep hit is not
absence of the thing** — the rule this corpus states for source `## Status` notes
applies to my own greps.

### What the defect actually is — weaker, and different in kind

Not vacuity. Two things survive, both `proof-claims-unencoded` rather than
`proof-no-empty-prop-carrier`:

1. **The docstrings promise relationships no field encodes.** `gradedTrace ℓ` is
   documented as *"the value of `tr_M` descended to `J^ℓ / J^{ℓ+1}`"* and `residue ℓ`
   as *"the cyclotomic projection of `Φ_q · gradedTrace ℓ`"* — but nothing relates
   `residue` to `gradedTrace`, or either to `tr_M` or the filtration. They are
   independent free functions that the prose says are computed from one another.
2. **The one `Prop` field constrains a field the class itself supplies.** `mass` is a
   free field, so any tuple inhabits the class: choose the six data fields freely, set
   `mass := |descended| + ∑ residue ℓ`, and discharge `spectral_decomposition` by
   `rfl`. So the constraint is a *definition of `mass`* wearing the shape of a
   constraint — it says one field is named consistently with the others, not anything
   about the world.

Point 2 is a genuine observation and is why the class is still trivially inhabitable,
but it is **not** the same finding as "asserts nothing", and it does not license the
fix recipe this bean originally proposed.

### Contamination — where else the wrong claim went

- This bean's original body (above, now superseded by this section).
- **PR #6055's body**, *Not done here*: "`GBResidueSpectralSum` in `mass-theory/` has
  zero `Prop` fields too." — corrected.
- The end-of-turn report to the owner making the same claim — corrected in-session.

Nothing was changed in `gb-residue-spectral-sum.lean` on the strength of it; the error
was caught before any edit. Had it not been, the fix would have added a `Prop` field to
a class that already had the right one.

### What is still worth doing here

Encode the two documented relationships (point 1), or weaken the docstrings to match
what the fields actually say. Both are honest; the first is better. **Do not** add a
`spectral_decomposition`-shaped field — it is already there.

Still unmeasured, as before: whether anything downstream takes
`[GBResidueSpectralSum]` as a hypothesis and concludes something.


---

## RESOLVED 2026-08-30

Fixed what survived the retraction. Commit: *"the field docstrings now say what the
fields encode, and what they do not"*.

- **`gradedTrace`** and **`residue`** docstrings now mark their intended meanings as
  **INTENDED and NOT ENCODED**, and name the infrastructure the module header already
  defers (GS filtration, Habiro ring). In particular the `residue` docstring now says
  outright that nothing relates it to `gradedTrace`, despite the prose having claimed
  one is computed from the other.
- **`spectral_decomposition`**'s docstring now records what it buys: it constrains
  `mass`, but `mass` is itself a free field, so any tuple inhabits the class — set
  `mass := |descended| + ∑ residue ℓ` and discharge by `rfl`.

Docs only; the Lean is unchanged and compiles (exit 0). Encoding the relationships for
real needs the deferred infrastructure, so this is honesty about the gap, not a
weakening of anything.

**Sidecar refreshed** via `qa-sweep` (the `.lean` edit drifted `source_hashes.lean`);
mechanical criteria re-run, agent-judgement ones marked `needs-agent` as expected.

### Found while here, and deliberately NOT touched: `spectral_sum_finite`

```lean
theorem spectral_sum_finite (S : GBResidueSpectralSum R) :
    ∃ N, ∀ ℓ ≥ N, ∀ (h : ℓ < S.levelBound), S.residue ⟨ℓ, h⟩ = 0 ∨ ℓ < S.levelBound
```

proved by `Or.inr h` — the second disjunct **is** the hypothesis, so the goal is
`P ∨ P` given `P`. A genuine tautology under §"No trivial trues".

Left alone for two reasons, both checked:

1. **It is a *knowing* tautology.** The content block's own `.md` says so:
   *"Cast as a tautology over the compact domain `Fin levelBound` … The substantive
   claim is that `levelBound` correctly represents the confinement level."* That is
   exactly the honest labelling the discipline asks for.
2. **It is the `lean.ref` of `conj:gs-spectral-sum-finite`.** Deleting it breaks a
   content block, which is not a drive-by fix.

The real content — that residues vanish above the confinement level — is carried by the
*type* `Fin levelBound`, so there is nothing left for a theorem to say. If anyone wants
this cleaned, the move is to retire the block or restate it around what `levelBound`
means, not to patch the proof.
