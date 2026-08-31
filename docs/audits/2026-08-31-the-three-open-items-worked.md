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
