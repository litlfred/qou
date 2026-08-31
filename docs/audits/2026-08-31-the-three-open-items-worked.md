# The three items handed back: both false classes repaired, the 52 split, and the confinement question settled

**Date:** 2026-08-31 · **Bean:** `qou-z9ws` · **PR:** litlfred/qou#6276

The self-assuming-projection arc closed with three items marked authorial. Worked
here. Two of the three turned out to be decidable by measurement, and the third
splits into three populations with different answers.

---

## 1. Both false classes — and in each, the Lean had invented what was false

This was framed as *"each needs a repair decision: tolerance, corrected
constants, or a corrected relation"*. That framing was wrong for both, and the
source blocks say so.

### 1a. `SkeinMassRelationHolds` — the relation is fine; the *instantiation* was invented

[`observations/skein-mass-relation-proof.md`](../../content/quantum-observable-universe/observations/skein-mass-relation-proof.md)
states the skein relation for the three resolutions of **one crossing**:

> *"At each crossing in the color-exchange diagram of a hadron, the three
> resolutions `L₊`, `L₋` and `L₀` satisfy
> `q𝓜(L₊) − q⁻¹𝓜(L₋) = (q^{1/2} − q^{-1/2})𝓜(L₀)`."*

The Lean substituted the **proton** for `L₊`, the **neutron** for `L₋` and the
**deuteron** for `L₀`. Nothing in the `.md` licenses that: those are three
different bound states, and the deuteron is a bound state *of* a proton and a
neutron, not the smoothing of a crossing between them.

Measured at the file's own constants (mpmath, 40 dps):

| | |
|---|---|
| LHS `q·m_p − q⁻¹·m_n` | 194.516369 |
| RHS `(√q − 1/√q)·m_d` | 195.320153 |
| difference | **0.8038 MeV**, rel **0.41 %** |

against the same file's `row1_proton_matches_CODATA`, which treats `1e-3 MeV` as
agreement — roughly 800×.

**Not a tolerance problem**, established two independent ways:

- the `q` making it exact at these masses is **1.17296190**, a **5.7 %** shift
  from the substrate — which is pinned to sub-ppb;
- the `m_zero` making it exact at `q = 1.1097` is **1867.894 MeV** = `m_d −
  7.72 MeV`, matching no quantity in the framework.

**The docstring's own "numerical verification" did not reproduce.** It recorded
`LHS ≈ 192.83`, `RHS ≈ 192.83`, `|LHS − RHS| < 0.01 ✓`. Both figures are wrong
and the conclusion inverts the real result. A wrong check that reports agreement
is worse than no check.

**Disposition.** Class, projection and `skein_mass_relation_proton_neutron`
removed (no consumers outside the file); replaced by the proved theorem
`skein_pnd_identity_false` carrying the measurements. The general
`SkeinMassRelation` structure is untouched — it is the Hecke relation and is
correct. *Which* triple is the `(L₊, L₋, L₀)` of a colour-exchange crossing is an
open modelling question, deliberately not answered.

### 1b. `DoubleMagicConjecture` — the missing hypothesis was named in its own docstring

`IsDoubleMagic`'s docstring said *"both constituents are **saturated** and
self-conjugate"*. The definition had only the self-conjugacy:

```lean
def IsDoubleMagic (C : Composite) : Prop :=
  isSelfConjugate C.ydZ ∧ isSelfConjugate C.ydN
```

The `.md` opens *"Let `Z, N ∈ 𝔐`"* — both levels drawn from the magic set. So
"double magic" meant "both constituents self-conjugate", with no magic number
anywhere, and the **empty** composite qualified. Saturation restored.

**The second field is removed, for two independent reasons.**

**(1) Its `A ∈ magicLadder` conjunct is not in the `.md` and is false at every
intended instance.** Magic numbers are per-`Z` or per-`N` shell closures; the sum
of two is essentially never one. Of the seven observed double-magic nuclei —
⁴He (A=4), ¹⁶O (16), ⁴⁰Ca (40), ⁴⁸Ca (48), ⁵⁶Ni (56), ¹³²Sn (132), ²⁰⁸Pb (208) —
**not one** has magic `A`. Exhaustively, the only magic pair whose sum is magic
is `8 + 20 = 28` (proved by `decide`).

**(2) The `↔` cannot be rescued by a guard.** Adding the saturation makes the `←`
direction safe and breaks `→` at the same empty composite: `κ(∅) = 0` and `∅` is
self-conjugate, but `0 ∉ magicLadder`.

The converse it asserted (*"**only** double-magic compositions reach the
ladder"*) is also a Lean addition the `.md` does not make.

**Also removed: `doubleMagic_implies_condensation`**, described as *"the
algebraic-geometry capstone connecting"* three conjectures. Its body is
`condensation_at_magic hL`; `D`, `[ContentAdditive C]` and `hM` are **all
unused**. The link it appeared to supply is exactly the removed false field, so
the chain cannot be closed by repairing the binders.

`lr_rigidity` — the `.md`'s actual claim — survives as the open conjecture. The
`.md`'s LR-multiplicity-one claim is still not encoded, and that gap is now
stated rather than implied.

### What the two have in common

Both are the same defect: **the `.md` states one thing, the Lean asserts
something stronger the `.md` never claims, and the invention is what is false.**
Neither needed a physics decision; both needed reading the source block.

---

## 2. The 52 vacuous classes are not one population

The question was *"re-encode against parameters, or drop the pseudo-theorems"*.
The answer depends on something not previously measured: **whether the class is
reachable from the content block it backs.**

Per AGENTS.md §0a, a block's `lean.ref` resolves to the **sibling first**, and
only then to `<lakeRoot>/<Decl/Path>.lean`. So a library declaration standing
beside a sibling of the same name is unreachable from its own block.

Measured across `content/`: **867** content-block siblings carry a `qou:`
`lean.ref`; for **137** of them a library file exists at the ref'd path, so the
sibling shadows it. Of those 137, **122 diverge**, **11** are covered by the
library and **4** are identical modulo comments.

**And the direction of the divergence is usually the opposite of what "shadowing"
suggests.** Spot-checking, the library file is typically the thin shell — a
context class plus a `Prop`-valued projection — while the sibling carries the
real mathematics. `fermion_boson_knot_link` is the type case: the library holds
`FermionBosonKnotLinkContext` and a projection, its own docstring conceding
*"the substantive mathematical content is carried by the context-class axioms"*,
while the sibling holds `structure TorusKnotLink`, `theorem fermion_iff_odd` and
`theorem boson_iff_even`.

Splitting the 52 that way:

| bucket | count | what it is | disposition |
|---|---|---|---|
| **A** | **15** | in a library shell a substantive sibling shadows | **drop** — measured dead |
| **B** | **6** | in the content-block sibling itself | **re-encode** — this is what the block resolves to |
| **C** | **31** | in a library module with no shadowing sibling | **re-encode** — reachable |

**Bucket A is decided by measurement, not taste.** Each is dead three ways:
the block resolves to the sibling; the sibling has the real formalisation; and
**nothing imports the module** — zero importers for all 15, not even an
aggregator.

**14 of the 15 are drained in this PR.** Files are gutted rather than deleted:
each keeps its imports and gains a docstring naming its sibling, what that
sibling proves, and the three measurements. Keeping the file means the ref's
second resolution candidate still exists as a real path.

**The 15th, `DecayChannelContext`, is held back and is instructive.** Its
sibling's docstring says the opposite of the pattern:

> *"The **substantive** Lean encoding (the `DecayChannelContext` class plus the
> `decay_channel` conditional result) lives at the **canonical library path**
> `QOU/BraidKnot/UnstableAtom/decay_channel.lean`."*

So the block's prose declares the library canonical while §0a resolution sends
every reader to the sibling. That one needs a real repair (the class is vacuous —
`on_boundary := fun _ => True`), not a drain.

**Buckets B and C are not this.** They are reachable, and dropping them would
remove what the block resolves to. They need the other disposition: re-encode so
the claim constrains a caller-supplied parameter rather than data the instance
chooses. That is per-class work, and it is what remains.

---

## 3. The confinement block: the library model is canonical

This was handed back as *"two competing models, and which is canonical isn't
mine to pick"*. Having measured, it is not a judgement call — three independent
criteria agree.

| | sibling (`ConfinedParticleTy`) | library (`ConfinedParticle`) |
|---|---|---|
| **fidelity to the `.md`** | `opaque confined` with no link to anything | `HasSDPRegularity.confined_iff_feasible` — exactly the `.md`'s *"strict feasibility predicate of the confinement SDP"* |
| **structure** | class fields **are** the conclusions, projected | class fields are **hypotheses**; `phase_locus_open` rewrites through `confined_iff_feasible` and applies openness of a different set |
| **use** | **2 files** — the two shadowing siblings themselves | **9 files** — `DressedParticle`, `ConfinementCategory`, `ElectronShell`, `ShellClosureStability`, `LevelSufficiency`, … |

The library also states the `.md`'s three claims as three theorems (openness,
μ-constancy on components, σ_F on components). Neither Lean encodes the `.md`'s
claim 2 (real-algebraic stratification, each stratum a principal-minor zero
locus) or claim 5 (phase transitions) — a gap in both.

**Correcting my own earlier statement.** I wrote that this "isn't mine to pick".
That was right before measuring and wrong after: the `.md` names the SDP
feasibility link that only one model has.

**What is NOT done here.** Making the block resolve to the library means removing
the sibling, and the sibling is not removable as-is: it defines
`ConfinedParticleTy` and the opaque triple, which the *other* confinement sibling
(`confinement-category.lean`) also uses. So the two siblings form a parallel
mini-model, and unpicking it is a content change touching two blocks and their
`.qa.json`s. Recorded with the evidence rather than half-done.

---

## Verification

- `lean`-direct throughout, olean cache restored, **no `lake build`**.
- `HadronicMass.lean`, `LRFusion.lean`, all 14 gutted shells, and the converted
  refutation file: exit 0, 0 errors.
- All 14 sibling paths cross-checked against the independently computed shadow
  map — 0 mismatches.
- `check-sidecars.sh` clean.

**Trap recorded.** `lean`-direct on a source file does **not** update its olean,
so an audit file importing a module you just edited keeps seeing the **old**
definition — and its proof fails in a way that looks like your repair is broken.
Rebuilt the one affected olean with `lean … -o <path>.olean` (single importer),
never `lake build`, which would evict the restore.

---

## Second tranche: bucket B drained, bucket A completed, and a measurable work list

Worked after the three items above, same bean, same PR.

### Bucket B — all six re-encoded

Each moved the objects the claim is about from **class fields** to
**parameters**, so a `[C …]` binder constrains what the caller brought. Four
of the six also gained a genuine derivation where there had been a
projection.

| block | what the class let the instance choose | what is now derived |
|---|---|---|
| `prop:r-matrix-braiding-structure` | `V3`, `comp`, `R12`, `R13`, `R23`, `Rcheck1`, `Rcheck2` — measured: `V3 := ℕ`, `comp := (·*·)`, `2, 3, 5` discharges YBE by `ring` | nothing; the two claims are **named** and not asserted (§1a disposition 3) |
| `prop:helicity-conservation` | `Hq`, all seven scalars, all three claims | the writhe/twist split **and** conservation, which follows from it |
| `prop:core-levi-form` | seven scalars plus md conclusions (b), (d) | (b) exactly, `1 ≤ cond`, and the aspect bound from md (d) |
| `conj:cpt-d6-d7-d8-closure` | `ClosedBraid`, `markovTrace`, `cptComposite` | closure **from its three components** |
| `prop:crystal-basis-…-open-problems` | one `Prop` field and its own proof | that discharging the three computations settles three problems |
| `conj:shared-denominator-cusp-holonomy` | the cusp shape, existentially | the matched shape is non-real, so the bare seed is not the cusp shape |

Two of these were **false claims about epistemic status**, not merely thin:

- The CPT file said the conjecture was *"axiomatised as a Lean class with no
  instance"*. `ClosedBraid := Unit`, `markovTrace := fun _ => 0`,
  `cptComposite := id` inhabits it.
- The cusp-holonomy file **and its `.md`** said the class *"deliberately has
  no instance"* and that requiring `Im z > 0` made *"any real-constant
  witness impossible"*. The field concluded `∃ z : ℂ, GeometricShape z`,
  unlinked to the root index, which is provable at `z = i` — verified by
  compiling the instance, `lean`-direct exit 0. Excluding real constants
  excluded the wrong constant.

Two more findings worth keeping:

- **`core_levi_cond_aspect_bound` was redundant, and its docstring said the
  opposite** — described as *"carrying the `O(ℏ_q²)` correction as an
  explicit bound"*, when the class already asserted `cond = max λ/min λ` and
  `(a⊥/a∥)² = λ∥/λ⊥` **exactly**, forcing equality. The "bound" was
  `0 ≤ C₀ℏ_q²` wearing an absolute value.
- **`newton_seed_completeness` was statement-identical to the theorem above
  it** — same binders, same conclusion, character for character — while its
  docstring claimed *"the algebraic denominator zeros are valid
  Newton–Raphson seed values"*. No seed, no iteration and no convergence
  appears in that type. Removed.

### Bucket A completed at 15/15

`DecayChannelContext` was held back because its sibling declared the library
path canonical. Both halves of that were wrong: §0a resolution sends the ref
to the **sibling**, which declared `decay_channel_unique` and **no**
`decay_channel`; and the library class carried ten data fields plus all three
sub-claims, with `on_boundary := fun _ => True` and `q_1 := 1, q_2 := 0`
making two of them vacuous. The sibling now declares `decay_channel`, and
**sub-claim (iii) is the intermediate value theorem** — *"stable at `q₁`,
unstable at `q₂` implies `∃ q* ∈ [q₁, q₂]` with `E(λ*, q*) = 0"* is exactly
what the manuscript's own paragraph argues — proved rather than assumed.

### The remaining work is 46 projections, measured

[`scripts/sap-projection-liveness.py`](../../scripts/sap-projection-liveness.py)
parses each ledger-flagged declaration's body and asks whether it is still
`:= ctx.field`. On this branch:

| | |
|---|---|
| genuine `proof-no-self-assuming-projection` entries | 90 |
| still bare projections | **46** — 31 library, 15 sibling |
| no longer a bare projection | 23 |
| declaration removed | 21 |

**The obvious liveness check is wrong, and this is why the script exists.**
Asking *"does the declaration name still occur in the file?"* reports **81 of
81 files still live** on this very tree — because a repaired file keeps the
name the ref points at, and a *gutted* file mentions the name in the
docstring explaining what was removed. That check answers "is the string
present", which is a different question. It was run and believed before being
caught.

**Quote the unit.** The ledger counts declarations; the bucket table above
counts classes. `bucket C = 31` agrees with the library figure by
coincidence of size, but `bucket B = 6` was six vacuous *classes* in
siblings against fifteen sibling *projections* here. Neither number
corrects the other.

**And a clean run would not prove the surface is clear.** The body parser
recognises `:= ctx.field`, `:= inst.field args` and `:= by exact ctx.field`,
and nothing else — a projection wrapped in `⟨…⟩`, `Iff.intro`, or a longer
`by`-block reads as repaired. It under-reports, which is the safe direction
for a drain and the wrong direction for an all-clear.

### Tool fix

`scripts/lean-context-class-inhabitation-probe.py` crashed with an
`AttributeError` out of a worker thread whenever a class signature failed to
parse, **aborting the entire sweep**. A full-tree run stopped after 76
verdicts and the only sign was a traceback at the end of the log. Unparsed
signatures now raise `Unsupported` and are reported as per-class skips.
