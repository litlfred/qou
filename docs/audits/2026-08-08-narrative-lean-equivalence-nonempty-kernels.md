# Narrative ↔ Lean equivalence: `Nonempty X` kernels (Class A)

**Date:** 2026-08-08
**Skill:** [`local/proof-narrative-lean-equivalence`](../../.claude/skills/local/proof-narrative-lean-equivalence.md)
**Beans:** `qou-g4x1` (the AppendixSurreals family), this doc (the corpus sweep)
**Scope:** first run of this skill's Phase 1 across the paper, as far as I can tell.

## Why this sweep happened

While draining the axiom-triage queue (`qou-i6cn`) I found six conjecture
classes in `AppendixSurreals/Conjectures.lean` whose entire formal kernel was
`Nonempty <placeholder type>` — e.g. `BigBangHeatDeath` and `HahnSubstrate`
both reduce to `Nonempty K`, making the two conjectures *indistinguishable as
formal statements*.

That is Class A (stub weakening) in this skill's taxonomy, but in a form no
existing detector sees: there is no `sorry`, no `True`, no unsound quantifier,
and **the statement is true**. The mismatch is between the `.md` and the
`.lean`, which no syntactic checker can catch.

The obvious question was whether the pattern is confined to that file.

## Method

918 blocks in `content/quantum-observable-universe` carry the full
`.ts` + `.md` + `.lean` triple. Too many to read, so I scanned for the crisp
mechanical signature instead:

> a `theorem`/`lemma`, or a `class`/`structure` **field**, whose *entire*
> content is `Nonempty X`.

Comments stripped first (a docstring quoting a declaration is otherwise read
as source — a trap that has now bitten three separate scans in this session).
`.lake/packages` excluded, and `have`/`haveI`/`letI` local bindings excluded —
those are ordinary proof plumbing and dominate an untuned scan (376 raw hits
→ 14 real ones).

**A `Nonempty X` kernel is not automatically a defect.** It is a defect
exactly when `X` is inhabited by construction — a placeholder, or a structure
with no constraining fields. So each hit needs the second question: *is the
type substantive?*

## Findings — 14 hits, 4 in content blocks

### The four content-block hits are all Class A

Each pairs a substantive narrative claim with a degenerate witness. In every
case **the author documented it in a comment** — the defect is not dishonesty,
it is that a degenerate witness sits under a headline theorem name.

| block | Lean kernel | witness |
|---|---|---|
| `predicted-spectra/categorical-proton-exists` | `Nonempty CategoricalProton` | `⟨skein_uu := 0, skein_ud := 0⟩` |
| `predicted-spectra/categorical-neutron-exists` | `Nonempty CategoricalNeutron` | `⟨skein_ud := 0, skein_dd := 0⟩` |
| `knots-particles-confinement/hadron-exists` | `Nonempty Hadron` | two `unknot` constituents, `θ = φ = 0` |
| `lifting-and-descent/quantum-characteristic-classes-exists` | `Nonempty QuantumCharacteristicClass` | `⟨level 0, ObstructionSpace ℤ, κ = 0⟩` |

**Worked case — `CategoricalProton.exists`.** The structure is

```lean
structure CategoricalProton where
  skein_uu  : ℝ
  skein_ud  : ℝ
  mass      : ℝ := skein_uu + 2 * skein_ud
  chirality : ℤ := 1
```

Four fields, **no properties**: no positivity, no relation to the Borromean
braid, no crossing energy, no Frobenius stability. So `Nonempty` is provable
by *any* assignment.

The docstring claims:

> *"The Borromean braid B₃(u,u,d) + LP-optimal Hopf gluon L₋ yields a
> canonical `CategoricalProton` term with negative crossing energy and
> Frobenius stability."*

The Lean proves that a **zero-mass degenerate proton** exists. The author's
own comment says so: *"Trivial witness: skein_uu = skein_ud = 0 (degenerate
proton with zero mass …). The intended Borromean B₃(u,u,d) × L₋ witness is
sharper but requires the Hecke NF reduction infrastructure."*

Note what is *unstatable* here, not merely unproved: the structure has no
field for crossing energy or Frobenius stability, so those two claims cannot
be expressed against it at all. Adding a witness would not help; the type has
to grow first.

`hadron-exists` is the most vivid: the witnessing "hadron" is two unknots.

### The ten library hits

Six are the `AppendixSurreals/Conjectures.lean` family already analysed in
`qou-g4x1` (three `Nonempty` kernels among them, two of which are the same
field). The remaining four —
`Archimedean/JetOrderIndependence`, `ArchimedeanUniverse`, `Elaboration`,
`Torsion/Descent`, `MathlibExt/SDP`, `mass-theory/confinement-nf-partial-proof`,
`quantum-universes/quantum-universe` — are `Nonempty` *fields inside larger
structures* (`fibre_nonempty`, `exceptional_nonempty`, `nonempty : Nonempty Λ`).

Those are **legitimate**: a non-degeneracy side-condition on a structure that
carries real content elsewhere is exactly what such a field is for. Not
findings. Listing them so the next run does not re-triage them.

## Disposition

**Do not "fix" these by strengthening the witness.** For
`categorical-proton-exists` there is no stronger witness available — the
structure cannot express the properties the narrative claims. The repair is,
in order:

1. Give `CategoricalProton` / `CategoricalNeutron` / `Hadron` fields that
   carry their defining properties (crossing energy, Frobenius stability, the
   Borromean relation).
2. *Then* the existence theorem becomes a real obligation, and the intended
   Borromean witness is the thing that discharges it.

Step 1 is the formalisation project; step 2 falls out of it. Both need the
Hecke NF reduction infrastructure the comments already name as the blocker,
so this is correctly *blocked*, not merely undone.

**Do not delete the theorems.** As with the seven in `qou-g4x1`: for what the
statements currently say, the proofs are correct. Deleting them would
misrepresent trivial statements as open conjectures.

## Recommendation for the skill

Add the `Nonempty X` kernel as a named Class A sub-signature, with the
triage rule that makes it usable:

- strip comments before scanning (else docstrings are read as source),
- exclude `.lake` and `have`/`haveI`/`letI` (376 raw → 14 real),
- flag only where `X` is a placeholder or a property-free structure,
- treat `Nonempty` **fields inside content-bearing structures** as fine.

Without the last two rules the signal is unusable; with them it found four
headline blocks in one pass.
