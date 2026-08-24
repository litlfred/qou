---
# qou-zf9n
title: Convention-D migration for the H_3 Gram Lean file and its spectrahedral-phase-collapse consumer
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T19:27:04Z
updated_at: 2026-08-24T07:02:15Z
---

Found while dispositioning `qou-bm4i` block 5/12 (`prop:gram-matrix-h3-symbolic`).
Branch: claude/rag-document-ingestion-options-orasrw.

## What already landed (do not redo)

`GramMatrixH3Symbolic.lean` now carries BOTH frames, `lean`-direct exit 0, all
eight new declarations sorry-free (`[propext, Classical.choice, Quot.sound]`):

- `markovWeightD`, `markovWeightD_root` — `(q²+1)·z_D − q³ = 0`, the vanishing
  determinant factor, stated in Lean so a later relabel cannot silence it.
- `gramEntryD` / `gramMatrixD` — the 36 canonical entries, rational in `q`.
- `gramEntryD_zero_one` — `G[0,1] = z`, a machine-checkable convention anchor.
- `gramMatrixD_isSymm`, `gramMatrixD_top_left` — the two C results that transfer.
- `gramRadicalD`, `gramRadicalD_ne_zero`, `gramMatrixD_mulVec_radical`,
  `gramMatrixD_det_eq_zero`, `gramMatrixD_not_posDef`.

The C declarations are untouched and now scoped in their docstrings. The
regression guard compares D against D and passes at 2.27e-16; the C−D gap is
retained in the witness as `data`. Derivation + six cross-checks:
`computations/probes/gram_h3_convention_frame_probe.py`.

## What is LEFT, and why it was not done here

### 1. Make `gramMatrix` mean D (the rename)

`lean.ref` on the block still points at `qou:...GramMatrixH3Symbolic.gramMatrix`,
which is the C matrix. The canonical end state is `gramMatrix` = D with the C
one renamed `gramMatrixC`, but that renames ~15 declarations and breaks the one
downstream importer, so it belongs with item 2 rather than half-done here.

### 2. `prop:spectrahedral-phase-collapse` — the claim does not survive D

`QOU/Archimedean/spectrahedral_phase_collapse.lean` is the only Lean importer.
It proves `(gramMatrix u).det = 0` at the supergolden threshold `u³ + u − 1 = 0`
via `detFactor3`, and the block reads that as a *phase transition*: "the Gram
matrix develops a kernel and drops rank at `u = 1/ψ` ... collapses the formal
solution space onto a strictly lower-dimensional face of the Hecke spectrahedron."

Under D the determinant is **identically zero for every `q`**
(`gramMatrixD_det_eq_zero`). So the theorem stays true and becomes **empty**: a
vanishing that holds everywhere singles out no threshold, and there is no
collapse *at* `1/ψ` because there is nowhere it fails to collapse. The physics
reading is what breaks, not the Lean.

This is a scope-(b) structural exclusion and the invariant is the determinant
factorisation, but it is a **claim in a second content block** — deciding what
that block should say instead is authoring, not migration, so it is not done
unilaterally. The honest options look like: retire the block; or re-derive
whether some *other* D-frame object (the Gram on the radical quotient, which
`gram-matrix-dual.witness.json` already carries as `gram_quotient_inverse`)
has a supergolden rank drop, which would be a real result rather than a
relabel.

### 3. Is the supergolden root a C artefact?

Worth settling while in here. `u³ + u − 1` is a factor of the **C**
determinant. Over `ℚ(q,z)` the determinant factors as
`−(z−q)⁵(qz+1)⁵((q²+1)z − q³)(q³z + qz + 1)/q⁸`, so every C-frame "special
value of `u`" is a root of one of those factors *after* substituting
`z = √q/(q+1)`. Whether `1/ψ` is intrinsic or an artefact of that substitution
is answerable directly from the generic form.

## Two cautions for whoever takes this

- **The C results are not wrong and must not be deleted.** They are correct
  theorems about a non-canonical frame; per AGENTS.md a Lean-proved piece is a
  permanent contribution. Scope them, do not remove them.
- **Do not "tidy" the entries.** Splicing the D entries in, a regex that looked
  purely cosmetic stripped numerator parentheses — `(q^7 + q^3) / d` became
  `q^7 + q^3 / d`, a different expression. Six `mulVec` rows went red and Lean
  caught it. Any transformation of these 36 lines needs a re-verify, not an eye.


---

## Addendum 2026-08-23 — a third block on the same thread, and a gate blind spot

Found while fixing `prop:markov-trace-axiomatic-closed-form` (bm4i block 6/12,
now corrected: `1.63315 -> 1.88432`, `rho_p 1124.3 -> 974.44`, denominator
`q^{10}(q+1)^3 -> q^7(q^2+1)^2`).

### `prop:markov-trace-antipode-polynomial-symmetry` is unchecked, not checked

Its witness `computations/probes/poly-q-proof.witness.json` carries a q-sweep
of `tr_M_numeric` values, every one of them ~1.63 — the **convention-C** value
for the same word. The block is `status: "verified"`.

That status cannot be caught by `scripts/check-computation-status.py`, because
the witness has **no assertions at all** and therefore no top-level
`allPassed` to disagree with. This is the gate's blind spot and it is the same
unearned-`verified` class as `qou-vfy1`: a witness that asserts nothing can
never fail, so "verified" against it costs nothing to claim.

Two of its recorded fields want a look, stated as pointers rather than
verdicts — they are about a *different* object (PR #546's Plancherel form),
and the claim-shape discipline says not to carry a conclusion across:

- `max_relative_diff_across_q: 7.8879` — a **relative** difference of 7.9,
  i.e. 789 %, sitting in a witness backing a "verified" block with nothing
  asserting on it.
- `anti_self_reciprocal_proved: true` — worth checking against the fact that
  the H_3 longest-element trace is anti-self-reciprocal in **neither**
  convention (measured in the block-6 work). Different object, so this is not
  a contradiction; it is a reason to look.
- `claimed_denominator: "12 * q^10"` — where the `q^{10}` in the block-6
  mislabel plausibly came from. Worth checking whether the two are the same
  provenance.

### Filing matters as much as finding

The block-6 convention mislabel had already been diagnosed **completely and
correctly** by `agent:h00` on 2026-08-22 — same numbers, same reasoning, and
notes proposing exactly the fix that was applied. It sat unfixed because it was
filed under the criterion **`trap-superlative`**, a language-trap check.
Nobody triaging prose traps acts on a convention defect, and nobody grepping
for convention problems looks in a prose criterion. A correct finding in the
wrong drawer is close to no finding.


---

## Addendum 2026-08-23 (2) — an untraced Δ_λ drift, and a mirror pair that does not cancel

From bm4i block 11/12, `prop:mirror-baseline-cancellation`. Two loose ends
deliberately not chased there, both worth someone's attention.

### 1. The upstream Δ_λ residual moved, and nothing recorded it

`delta_lambda_z_coefficient_and_slope.py` carried a docstring table that is
stale in **every row** against its own current output:

    atom   stale dev    current dev
    D        −0.01         +0.63
    T        −0.07         −1.02
    ³He      −1.40         −1.98
    ⁴He      +0.27         −1.70
    ⁶Li     −18.88        −22.69
    ⁷Li     −26.21        −30.79
    ⁷Be     −27.98        −32.56

The witness payload itself has NOT drifted — a re-run reproduces the committed
2026-08-21 numbers byte for byte. So the change happened upstream, in whatever
produces `delta-lambda-canonical-residual.witness.json`, at some point between
the docstring being written and that witness being regenerated. **Nobody
recorded what changed or why.** The docstring is now corrected to print both
columns, but the cause is untraced.

This matters beyond bookkeeping: the stale table is where the "law holds for
A≤4 (|dev| < 0.5)" claim came from, and with the current numbers no light
nucleus is within 0.5. A conclusion outlived the numbers it was drawn from.

### 2. The A=3 mirror pair does not cancel; A=7 does, exactly

Under that same drift the two mirror pairs behaved differently:

| pair | shift, proton-rich | shift, mirror | penalty before → after |
|---|---|---|---|
| ⁷Be / ⁷Li | −4.58 | −4.58 | −1.77 → **−1.77** (invariant) |
| ³He / T   | −0.58 | −0.95 | −1.33 → **−0.95** (moved) |

A=7 is exactly the baseline cancellation this block's proposition predicts:
`f(Z,N) − f(N,Z)` kills the A-only term `β(A)`, so a perturbation to the
baseline cannot move the mirror difference. Seeing that hold to the digit under
an unrelated drift is a nice independent check of the proposition.

A=3 not behaving that way is the interesting part. Either the drift was not
baseline-only at A=3 (i.e. it touched the Z-odd channel there), or T and ³He
were not regenerated together. **Not investigated** — stated as an observation,
not a result, and specifically not as evidence for or against the proposition.

Consequence already recorded in the producer: the proton-excess penalty spread
was quoted as −1.33 vs −1.77 (~33%); it is now −0.95 vs −1.77 (~86%), and the
magnitude is not stable under input drift. That strengthens the existing
"magnitude is NOT a single derivable number" verdict rather than weakening it.


## CORRECTED: two different Gram matrices, and I conflated them (2026-08-23)

An earlier note here claimed main's `35b4923012` (qou-cds2) "generalises" the
n=3 result proved on this branch, reading its corank 1 / 2 at n=3 / n=4 as
rank = #{partitions with at most two rows}. **The arithmetic in that commit is
right; my reading of it as the same object was not.** A sibling on #5592
flagged it and the check confirms them.

There are two Gram matrices here and they agree only at n=3:

| object | dim | corank at n=3,4,5 |
|---|---|---|
| **full NF-basis** Gram (`gramMatrixD`, this branch's Lean) | n! | 1, 10, 78 |
| **partition-indexed** Gram (`pyhecke_n_generic.gram_inverse_n`) | #partitions | 1, 2, 4 |

The tell I missed was in main's own output: it reports `n=3 dim 3`, and my Lean
is `Fin 6`. Different dimension, therefore different matrix — matched on the
topic ("Gram corank at n=3 is 1") without checking the object. That is the
`da-arity-conflation` shape AGENTS.md warns about, arriving as a dimension
rather than a binder.

**The unifying fact, which both measurements do support.** The degenerate
directions are exactly the Wedderburn blocks with >= 3 rows — the blocks where
`y_lambda = 0` under D (qou-8iru). The partition-indexed Gram sees each such
block once; the full NF Gram sees it with multiplicity (dim V_lambda)^2:

    n=3:  1 = 1^2                    n=4:  10 = 3^2 + 1^2
    n=5: 78 = 6^2 + 5^2 + 4^2 + 1^2

and Sum_{lambda >= 3 rows} (dim V_lambda)^2 = n! - Catalan(n), verified for
n = 3,4,5. So the radical of the full Gram is ker(H_n -> TL_n), matching #5592.

At n=3 the branch's Lean radical (-q^3, q^2, q^2, -q, -q, 1) is the three-strand
q-antisymmetriser, i.e. the single partition (1^3) — the one partition of 3 with
>= 3 rows, dim 1, so corank 1^2 = 1 in both objects at once. That coincidence is
what made the conflation look like confirmation.

Three producers do still describe one phenomenon, correctly scoped: Lean exact
over R (det = 0 with an explicit radical, full NF basis, n=3), sympy (exactly
one degenerate direction, indefinite signature, same basis), and numpy general-n
(corank = block count, partition-indexed). The third is a different matrix, not
a generalisation of the first two.


## Progress 2026-08-24 — item 1 of 4 done (PR #5618)

**DONE: `prop:spectrahedral-phase-collapse` scoped to convention C.** The
threshold reading does not survive D; the theorem does, and stays. Probe
`computations/probes/spectrahedral_phase_collapse_frame_probe.py` (7/7, exact
over Q(u)/Q(q), parses the Gram out of the committed .lean so it cannot drift).

Two findings beyond the scoping:

- **The block was understating itself.** On u > 0, det G_C has TWO positive real
  zeros: u = 1/psi (multiplicity 5) and u = 1, i.e. q = 1, the classical limit
  (multiplicity 1). Only the first was in the corpus. The remaining real root
  u = -psi from (u^3+u^2+1)^5 is negative, and both sextic factors are
  real-rootless, so those two are all there are.
- **No collision with `gramMatrix_det_ne_zero`**, which assumes 1 < u: both
  zeros are at or below 1, and the substrate u_0 = 1.0536 is above both.

REMAINING on this bean:
  2. Convention-D migration of the H_3 Gram Lean file itself (the C
     declarations are scoped but still the default the file leads with).
  3. Untraced Delta_lambda residual drift.
  4. The A=3 mirror pair fails to cancel while A=7 cancels exactly.

My judgement on order: item 2 is now the natural next — #5592 has the general-n
TL picture and #5502 landed the n=3 anchor, so the migration has both ends
pinned. Items 3 and 4 are independent of the convention work.
