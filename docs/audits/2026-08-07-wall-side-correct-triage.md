# `wall-side-correct` triage — 159 critical findings

Date: 2026-08-07. Source: `qa-sweep --only wall-side-correct` over
`content/quantum-observable-universe` at `a20044fe` (2959 blocks;
1054 pass, 1745 n/a-no-lean, 159 fail, 1 fresh-skip).

The criterion (CLAUDE.md §7c) is critical: algebraic Lean must not
mention `ℝ` / `Real.*` / `linarith` / ordering; archimedean Lean must
declare `ℝ` **and** carry a §7c acknowledgement in the block `.md` or
the `.ts` `authorNotes`.

## Failure modes

| mode | count |
|---|---|
| ARCH-unacked (archimedean markers, no §7c acknowledgement) | 129 |
| MIXED (`ℝ` and generic-`R` coexisting in one file) | 30 |
| **total** | **159** |

| location | count |
|---|---|
| library tree (`lean/QOU/**`) | 118 |
| block sibling | 41 |

The library-tree majority matters: those files have no `.md`/`.ts` of
their own, so the acknowledgement the checker looks for can only live
on whichever block's `lean.ref` resolves to them. A library module that
is legitimately archimedean and referenced by no block therefore has
nowhere to record the acknowledgement — a structural gap in the
criterion, not necessarily a defect in the file.

## Strongest violation candidates (18)

Files containing `ℝ` but **no** archimedean construct at all (no
`Real.*`, no ordering, no `linarith`/`positivity`, no `Complex`, no
analysis). For these the `ℝ` is a candidate gratuitous specialisation
of content that would state over a generic `{R : Type*}`.

Machine-generated shortlist — each still needs individual review; the
absence of an archimedean *token* is evidence, not proof, that the
statement is algebraic.

| block | `ℝ`× | mode | file |
|---|---|---|---|
| `conj:q-birch-swinnerton-dyer` | 4 | MIXED | `content/quantum-observable-universe/lean/QOU/QBirchSwinnertonDyer.lean` |
| `conj:z-eq-n-rho-correction` | 23 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/BraidKnot/ZeqNRhoCorrection.lean` |
| `cor:knot-factor-amphicheiral` | 4 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorAmphicheiral.lean` |
| `def:algebraic-quantum-volume` | 2 | ARCH-unacked | `content/quantum-observable-universe/mass-theory/algebraic-quantum-volume.lean` |
| `def:q-harmonic-form` | 3 | ARCH-unacked | `content/quantum-observable-universe/quantum-observable-universes/q-harmonic-form.lean` |
| `ex:q-torsion-leaf` | 6 | MIXED | `content/quantum-observable-universe/quantum-observable-universes/q-torsion-leaf.lean` |
| `prf:categorical-dq-squared` | 5 | MIXED | `content/quantum-observable-universe/lean/QOU/CategoricalDqSquared.lean` |
| `prop:b1-figure-8-row-theorem` | 1 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/AppendixSurreals/B1Figure8RowTheorem.lean` |
| `prop:cl3-zeta5-orbit-sum-identity` | 1 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/BraidKnot/Cl3Zeta5OrbitSum.lean` |
| `prop:confinement-frobenius-reciprocity` | 9 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean` |
| `prop:hoefsmit-binding-amplitude` | 1 | MIXED | `content/quantum-observable-universe/braids-and-knots/hoefsmit-binding-amplitude.lean` |
| `prop:per-braid-mass-tower` | 5 | ARCH-unacked | `content/quantum-observable-universe/mass-theory/per-braid-mass-tower.lean` |
| `prop:q-beta-q-eq-one-shadow-gate` | 15 | ARCH-unacked | `content/quantum-observable-universe/mass-theory/q-beta-q-eq-one-shadow-gate.lean` |
| `prop:q-hecke-seminormal-character-closure` | 2 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/BraidKnot/QHeckeSeminormalCharacterClosure.lean` |
| `prop:reeb-bundle-complement-equals-volume` | 2 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/BraidsKnots/ReebBundleComplementEqualsVolume.lean` |
| `prop:rj-canonical-inner-product` | 10 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/Archimedean/rj_canonical_inner_product.lean` |
| `prop:wedderburn-as-noncomm-fourier` | 5 | ARCH-unacked | `content/quantum-observable-universe/mass-theory/wedderburn-as-noncomm-fourier.lean` |
| `prop:wedderburn-trace-identity` | 2 | ARCH-unacked | `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/PlancherelViaRecipe.lean` |

## Resolved in this pass (1 of 18)

`prop:hoefsmit-binding-amplitude`
(`content/quantum-observable-universe/braids-and-knots/hoefsmit-binding-amplitude.lean`)
— every declaration is q-deformation combinatorics (`q ± q⁻¹`, `[2]_q`,
`[3]_q`) and every proof is `field_simp` + `ring`; the only hypotheses
are `q ≠ 0` / `q ≠ 1`. No ordering, radical, or archimedean tactic
appears, and the block `.md` independently states the identities are
"exact in q, independent of the substrate parameter". Regenericised to
`{R : Type*} [Field R]`, dropping `import Mathlib.Data.Real.Basic`.

Verified `lean`-direct (not `lake build`, which would evict the
restored oleans): exit 0, sorry-free, ~25 s against the 6990-olean
Mathlib cache.

## Not addressed

The remaining 17 shortlist candidates and the 141 other findings.
Each needs its own read — the ARCH-unacked majority is likely resolved
by *adding* the §7c acknowledgement rather than by changing Lean, which
is a documentation edit, but that judgement is per-file and was not
made here.
