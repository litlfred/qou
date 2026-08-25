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

## Per-file disposition of the remaining 17 (read 2026-08-07)

All 17 were read. **None is a second `hoefsmit`-style gratuitous `ℝ`.**
The shortlist was built from the *absence* of an archimedean token, and
that heuristic has a high false-positive rate: a file can be genuinely
archimedean through a typeclass (`|·|`, division-with-ordering), through
an imported structure whose fields are `M → ℝ`, or through the *meaning*
of its quantities (an L-value, a Bloch–Wigner volume) without ever
naming `Real.*` locally.

| file | disposition | why |
|---|---|---|
| `QBirchSwinnertonDyer.lean` | ACK | `L_value_at_one`, `reeb_period` — L-functions and periods are analytic objects |
| `ZeqNRhoCorrection.lean` | ACK | carries `0 <` ordering + `Real.Basic`; existing `sorry` is cited |
| `KnotFactorAmphicheiral.lean` | **VACUOUS** | see below — not a §7c issue |
| `algebraic-quantum-volume.lean` | ACK | `tracedVolume_pos : ∀ i, 0 < tracedVolume i` is an ordering hypothesis |
| `q-harmonic-form.lean` | ACK | module docstring already says *"Archimedean realisation"*; ack must reach the `.md` |
| `q-torsion-leaf.lean` | ACK | **already correct** — q-side over `R_q = LaurentPolynomial`, archimedean side over `ℝ`; the wall is respected |
| `CategoricalDqSquared.lean` | ACK | `[CategoryTheory.Linear ℝ C]` inherited from `CategoricalQExtDeriv`; genericising is an upstream refactor, not a local edit |
| `B1Figure8RowTheorem.lean` | ACK | `bloch_wigner_4_1` is a Bloch–Wigner dilogarithm value — genuinely transcendental |
| `Cl3Zeta5OrbitSum.lean` | GENERIC-*able* | rational identity in a formal `zeta3`, proof is `field_simp; ring` — but `cl3OrbitSumPredicted` is `ℝ`-typed upstream in `QOU.Infra.Polylogarithm`, so the fix is not local |
| `confinement_frobenius_reciprocity.lean` | ACK | ordering + cited `sorry` |
| `per-braid-mass-tower.lean` | ACK | `|trM W|` needs `abs`; `Φ_q` is the quantum dilogarithm |
| `q-beta-q-eq-one-shadow-gate.lean` | ACK | q=1 shadow evaluation is archimedean by construction |
| `QHeckeSeminormalCharacterClosure.lean` | ACK | records *numerical* agreement of two compute paths — inherently archimedean |
| `ReebBundleComplementEqualsVolume.lean` | ACK | JSJ-graded hyperbolic volume |
| `rj_canonical_inner_product.lean` | ACK | **lives under `QOU/Archimedean/`** — see gap 2 |
| `wedderburn-as-noncomm-fourier.lean` | ACK | `tr : carrier → ℝ`, Plancherel weights |
| `PlancherelViaRecipe.lean` | **VACUOUS** | concludes `(1 : ℝ) = 1`; already in `lean-vacuity-review-ledger.json` |

So the honest summary of the 18-candidate shortlist is: **1 genuine §7c
violation (fixed, `hoefsmit`), 1 fix that is real but non-local
(`Cl3Zeta5OrbitSum`, blocked upstream), 14 legitimately archimedean
needing only an acknowledgement, and 2 that are not base-ring problems
at all but vacuous proofs.**

## Two structural gaps in the criterion

**Gap 1 — RETRACTED (2026-08-07, same day).** An earlier revision of
this document, and PR #4703's description, claimed that the 118
library-tree findings had *nowhere* to put the acknowledgement, because
`q-usage-audit.ts` calls `checkWallSide(undefined, file)` with no `md`
and no `ts`. **That was wrong, and the conclusion drawn from it — that
only 6 of the 17 were fixable — was wrong too.** Two corrections, both
read off the checker source rather than inferred:

1. **The library-tree files are reached through a referring block that
   does have `.md`/`.ts`.** "Library-tree" describes where the `.lean`
   lives, not whether a block points at it. `qa-sweep` calls
   `checkWallSide(p.md, p.lean, p.ts)`, where `p.lean` is the resolved
   library module and `p.md`/`p.ts` are the *referring block's*
   siblings. Example: `lean/QOU/BraidKnot/ZeqNRhoCorrection.lean` ←
   `mass-theory/z-eq-n-rho-correction.ts`. So the acknowledgement has a
   home, and `acknowledged()` is reachable.
2. **The `checkWallSide(undefined, file)` call cannot produce an
   unfixable finding.** The archimedean-without-acknowledgement branch
   is guarded `if (hasRealType && (mdReadable || tsReadable) && …)`, so
   with neither sibling readable it does not fire at all. That entry
   point is a standalone file scan, not the source of the 129
   ARCH-unacked findings.

**Consequence: every ARCH-unacked finding is fixable today** by adding a
§7c note to the referring block's `.ts` `authorNotes`. This pass drained
all 11 shortlist blocks that route through a referring manifest —
verified **10/10 pass** with `scripts/check-wall-side.ts --block`
(`knot-factor-amphicheiral` excluded from the count, see the caveat
below). Together with the 6 sibling-mode blocks drained earlier, the
whole 18-candidate shortlist is now acknowledged or fixed.

*Harness caveat.* `--block` mode resolves `lean.ref` by trying
progressively shorter decl-path prefixes. For
`QOU.BraidKnot.knot_factor_amphicheiral` that lands on
`lean/QOU/BraidKnot.lean` (the module file) rather than
`lean/QOU/BraidKnot/KnotFactorAmphicheiral.lean`, so that one row checks
a different file than intended and its PASS should not be relied on. The
pipeline's own resolver is the authority; this harness approximates it.

**Gap 2 (still open, but no longer a blocker) — the `Archimedean/` path is already a declaration.** 167
`.lean` files sit under a `QOU/**/Archimedean/**` path. That directory
*is* the wall-side declaration, yet the criterion still reports them as
"archimedean but unacknowledged". Treating the path as an implicit
acknowledgement would remove a large block of the 129 ARCH-unacked
findings without touching a single file. With Gap 1 retracted this is a
convenience, not a prerequisite: the drain works today. Still worth doing
so the remaining count reflects real defects.

## What the shortlist actually surfaced

Two of the 18 are not base-ring problems but **vacuous proofs**, and
chasing them found a third vacuity shape live in 15 files corpus-wide:

- `PlancherelViaRecipe.lean` — `theorem plancherel_via_recipe : (1 : ℝ) = 1`,
  under a docstring claiming the Markov-trace normalisation
  `Σ_λ d_λ y_λ(q) = 1`. Already known
  (`docs/audits/lean-vacuity-review-ledger.json`).
- `KnotFactorAmphicheiral.lean` — `∃ a : ℝ, a = 1 - w·h²` proved
  `⟨_, rfl⟩`, with **both** hypotheses underscore-marked unused. **Not**
  in any prior vacuity audit.

The second led to a corpus scan for `∃ x, x = e := ⟨e, rfl⟩` — provable
for any `e`, therefore contentless. **17 occurrences in 15 files, 17/17
rfl-witness.** Detector and full list:
[`2026-08-07-lean-vacuous-existential-audit.md`](2026-08-07-lean-vacuous-existential-audit.md),
[`scripts/lean-vacuous-existential-audit.py`](../../scripts/lean-vacuous-existential-audit.py).

## Still not addressed

The 141 findings outside the shortlist, and the acknowledgement edits
for the 6 files that can carry one. Gap 2 should be settled first —
fixing the criterion is cheaper than hand-draining findings it should
not be reporting.
