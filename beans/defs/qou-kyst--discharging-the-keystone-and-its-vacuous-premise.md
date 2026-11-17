---
# qou-kyst
title: Discharging the keystone conjecture and its one vacuous premise
status: in-progress
pr: 8235
updated_at: 2026-11-17T06:55:36Z
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T08:10:00Z
updated_at: 2026-10-04T15:26:06Z
parent: qou-r9ih
---

The two things above the C1 chain that are open by nature rather than by
neglect. Beaned so they are not mistaken for oversights.

## 1. `conj:qdifference-kernel-prolongation-symbol` — class with no instance

`folio/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.lean`
declares `class QDifferenceKernelIsProlongationSymbol (R) [CommRing R]` and
proves `kernel_is_prolongation_symbol` **from the class field**. There is no
instance anywhere. That is the honest open state for a `conjecture` block
(§3b-tax), not a defect — and `lean.validation: "validated"` is correct, since
the schema defines it as *"built and type-checked successfully"*, a build-status
field. (I flagged this as overstating on 2026-08-08 and retracted it; see
`qou-slpd`.)

**Discharging it means constructing an instance**, i.e. proving the kernel `R`
really is the jet-prolongation operator symbol. Per the block's own 2026-07-20
notes the GGM clause is already **refuted at module level** (Door-i), and the
owner re-scoping decision (F1 rewrite to R1 / F2 mark the GGM clause refuted /
F3 split) is **still open**. Nothing should be attempted on the Lean until that
framing call is made — otherwise the instance would be built against a statement
the corpus has already decided is wrong in part.

**Blocked on: an owner framing decision.** This is the one item in this cluster
that genuinely cannot be unblocked by reading a source.

## 2. `prop:mi-sw-abelianisation` — vacuous, and hard to fix

`QOU/BringsSurface.lean`:

```lean
theorem mi_sw_abelianisation (_bs) (n) (sw_period mi_integral : ℕ → ℝ)
    (fake_flat_abelian : ∀ k, mi_integral k = sw_period k) :
    mi_integral n = sw_period n := fake_flat_abelian n
```

Hypothesis is conclusion; the proof is a projection. Marked `validation:
"trivial"` on 2026-08-08 with an author note and a flag at the declaration.

Discharging it means proving the three steps of its own outline:

1. an SU(2) bundle over `S²` is trivial, so the connection abelianises to U(1);
2. fake-flatness `F_A = B` forces the 2-form datum into the Cartan subalgebra on
   the exceptional divisor `E_c`;
3. the MI integral then reduces to the classical contour integral of `λ_SW^(n)`.

**Realistic assessment: Mathlib cannot support this.** (1) needs principal
bundles and classifying spaces over `S²`; (2) needs nonabelian gauge theory and
Lie-algebra-valued 2-forms; (3) needs Yekutieli's nonabelian multiplicative
integration. None of that exists. The honest options are (a) leave it `trivial`
with the flag, which is where it is now, or (b) restate the block as a
*definition* or an explicit *premise* rather than a proposition, so the corpus
stops carrying a proposition whose Lean is a restatement. **(b) is an owner
call and is the cheap one.**

Relates: `qou-slpd`, `qou-c1ln`, `qou-c1wr`.

## 2026-08-08 — owner said proceed; both items actioned as far as evidence allows

**Keystone — F2 taken, F1/F3 left open.** Of the three re-scoping options, F2
("mark the GGM clause refuted") is the one already carried by evidence, so that
is the one recorded, in a new author note on the block. The refutation is now
machine-checked rather than asserted: `newtonSlopes_c1_ne_ggm` derives both
Newton-polygon slope multisets from the operators' coefficient valuations and
proves they differ, so with RSZ Thm 2.2.1(i) (polygon is a module invariant) and
Thm 2.2.4 (slope multiset preserved by every gauge) **no q-difference-module
identification of C1 with GGM exists**. F1 (rewrite the block to R1) and F3
(split it) are *not* foreclosed — they change the block's title and statement,
which is editorial and still the owner's. The class still has no instance; that
remains the honest open state for the surviving R1 clause.

**`prop:mi-sw-abelianisation` — restated, no longer vacuous.**
`QOU/BringsSurface.lean` now has `class MISWAbelianisation (sw_period
mi_integral) : Prop` with the abelianisation as its single field, and
`mi_sw_abelianisation` derives the conclusion from `[K : MISWAbelianisation …]`.
This is not cosmetic: the old theorem could be discharged by handing it its own
conclusion, whereas an instance must exhibit the abelianisation. The open state
is now in the *type*. `validation` moved `trivial` → `stub`.

Mathlib still cannot support a real instance (principal bundles over `S²`,
nonabelian gauge theory, Yekutieli multiplicative integration), so no-instance
is expected to persist. What changed is that it is stated rather than disguised
— which was the actual defect.

## 2026-08-08 — F3 confirmed by the owner and implemented

**Block A** `conj:qdifference-kernel-prolongation-symbol` — retitled, and the
`equivalently, the monodromy/Stokes data …` clause **removed** from the
statement. Label unchanged, so no `uses[]` edge moved;
`conj:schwinger-measure-computational-time` depends on the prolongation-symbol
claim alone and is unaffected. Consequences (1)/(2) and the keystone paragraph
never used the refuted clause and are untouched.

**Block B** `conj:c1-ggm-bar-parity-faces` — new, carrying the Door-iv/v
terminus as its own falsifiable claim: the tensor square is anisoclinic with
slopes `{+1,0,−1} ⊃ {+1,−1}`, agrees with the Stokes carrier as a graded module
with its Stokes data, and the sole residual is the diagonal `ℤ/2` character
`(−1)^m`. It gives `doorV_parity_no_identity` its **first content-block home** —
that theorem is real (a non-negative-cone argument, not a near-match) and had
no block referencing it.

### One-voice fix, owner-flagged mid-implementation

The first draft of both blocks used branch jargon — "the binding module C1",
"GGM eq-49" — in the **paper** prose. That is audit/agent vocabulary and does
not belong in the manuscript voice. Rewritten to define the objects instead of
labelling them:

* `𝒦` — the rank-2 module of the binding q-lift recurrence
  `[m+2]_q b_{m+2} = b_{m+1} + b_m`, i.e. of
  `L_𝒦 = (q²x−1)σ² − (q−1)σ − (q−1)` with `x = q^m`, pure isoclinic of slope ½.
* `𝒢` — the module of `y_{m+2} − (2−q^{m+1})y_{m+1} + y_m = 0`, the Stokes
  carrier of the resurgent colored-Jones series, cited to
  `[garoufalidis-gu-marino2021]` rather than to "GGM eq-49".

Same treatment applied to `prop:c1-theta-zero-locus-and-pole-divisor`, which had
inherited "the ramified C1 operator". **Rule going forward: `.md` is the
manuscript and carries no branch labels (C1, C2, GGM, Door-i…, Route A…);
`authorNotes` is the working channel and they are fine there.**

### Still open, unchanged

`QDifferenceKernelIsProlongationSymbol` has no instance — the honest state for
the surviving claim. `MISWAbelianisation` likewise. Neither F1 nor F3 was ever
going to change that; the split only stops the block asserting something the
corpus has refuted.

## Progress Update (PR #8235)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8235` at `83fd5b4cb41e61d75f72ddd82bda505e34bd92f4`).
- **Lean Formalization**: `QOU.QBeta.ThimbleDecompositionAndSymmetricPolytopeBrick.qdifference_prolongation_symbol_commutator_obstruction_identity` (Decomposition of the q-difference prolongation symbol E_M - q*M_E, classical limit at q = 1, and nonvanishing obstruction on a commutative shadow.)
- **80-dps Witness**: `computations/probes/thimble-decomposition-and-symmetric-polytope-brick.witness.json` (`scriptHash: e55db77fb2bb`, `scriptCommitSha: 6020aea5785046b552772c9a42fc52ac2db9f3a2`).
