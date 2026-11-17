---
# qou-zf9n
title: Convention-D migration for the H_3 Gram Lean file and its spectrahedral-phase-collapse consumer
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T19:27:04Z
updated_at: 2026-10-10T07:47:10Z
parent: qou-cdx1
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


## Item 2 — the migration target already exists, and the corpus mislabels it

**FOUND: `QOU.Machinery.H3.gramMatrix (z h : R)`** — the convention-AGNOSTIC
H_3 Gram over a generic CommRing, with `gramMatrix_eq` tying it to the actual
`tr_M` pairing and a sorry-free closed-form determinant

    det G = -(z^2 - hz - 1)^5 * ((h^2+4)z^2 - (h^3+4h)z - 1)

`gramMatrix_det_ne_zero` already excludes `z = q^3/(q^2+1)` by name. So #5502's
`det G(q,z)` over Q(q,z) was a RE-DERIVATION. My corpus-grep missed it because
three different declarations are called `gramMatrix` and I only looked at one.
Recorded rather than glossed.

**This re-frames the migration.** The right end state is not "rename C to *C and
promote D": it is to make `GramMatrixH3Symbolic`'s two hand-written 6x6 tables
SPECIALISATIONS of the general `(z,h)` form, so there is one determinant and one
place where a convention is chosen. That is a bridge lemma
(`gramMatrixD q = QOU.Machinery.H3.gramMatrix (q^3/(q^2+1)) (q - q^-1)`), not a
mass rename — cheaper AND safer than what this bean originally proposed.

**DONE: corrected a wrong identification in that file's docstring** (PR #5618).
It attributed the two quadratic zeros to the `(2,1)` block. Measured exactly
over Q(q):

    z = q^3/(q^2+1)     corank 1   sign (1^3)    radical = q-antisymmetriser
    z = -1/(q(q^2+1))   corank 1   trivial (3)   radical = q-symmetriser
    z = q, z = -1/q     corank 5   (quintic factor)

`(2,1)` has dim 2, so it would cost corank 4, not 1. The theorem is TRUE and
untouched — the proof never used the attribution. But the misreading severs the
link to `y_lambda = 0` for >= 3-row partitions (qou-8iru): `(1^3)` has >= 3 rows
and `(2,1)` does not, so it makes one phenomenon look like two.

The z_D radical from the general form is byte-identical to `gramRadicalD` from
the 6x6 table — two routes, same vector.

REMAINING: the bridge lemma above (item 2 proper); item 3 Delta_lambda drift;
item 4 the A=3 mirror pair.


## Item 2 DONE (PR #5618) — bridged, not renamed

Three sorry-free theorems now tie both hand-written 6x6 tables to
`QOU.Machinery.H3.gramMatrix (z h)`:

    gramMatrixD_eq_general : gramMatrixD q = H3.gramMatrix (q^3/(q^2+1)) (q - q^-1)
    gramMatrix_eq_general  : gramMatrix  u = H3.gramMatrix (u/(u^2+1)) (u^2 - (u^2)^-1)
    gramMatrixD_det_eq_zero_via_general

**The bean asked for the wrong thing and this is the correction.** It proposed
renaming the C declarations and promoting D. Three 6x6 objects existed and
nothing checked they agreed; a rename would have left that gap open. Bridging
closes it -- a future edit to either table that breaks agreement now fails to
compile.

lean-direct exit 0 on the whole file (3m16s, FASTER than the 4m43s baseline);
#print axioms clean on all three; 0 sorry terms. Both bridges verified exactly
in sympy (36/36, both frames) before any Lean was written.

**Reusable tactic finding.** `simp only` with a hand-picked Matrix.cons set
leaves the RHS an unreduced vecCons tower for any index above 1, and TIMES OUT
at 6.4M heartbeats rather than failing cleanly -- so the symptom looks like "too
hard" when it is actually "wrong lemma set". Plain `simp` with the three defs
closes all 36 goals and is an order of magnitude faster.

Two process notes:
  - I dropped `Matrix.head_cons` on an "unused simp argument" linter hint. The
    hint was right for the entry it fired on and wrong for the other 35. A
    per-goal linter verdict is not a per-theorem one.
  - Iterating on the 750-line file cost 9 min/round; extracting the two tables
    into a scratch file cut it to 17-36 s. Do that FIRST, not fourth.

REMAINING on this bean: item 3 (Delta_lambda residual drift), item 4 (the A=3
mirror pair that fails to cancel while A=7 cancels exactly). Neither touches the
convention work, so this bean's convention thread is now closed.


## Where the missing 83.5% can live — a structural bound (not an ansatz)

With `rho_w_crystal_vertex_trace` fixed (the 8.9e-7 residual was a hardcoded
muon q; now 1.4e-49 — bean qou-2joi), the shortfall is a clean measurement and
can be characterised.

**The closure sum is supported on the Temperley-Lieb quotient.** `y_lambda`
vanishes on every partition with >= 3 rows, so those blocks enter
`sum_lambda y_lambda * Delta_lambda * sgn * f^lambda` multiplied by EXACTLY
zero. At n=6, 7 of 11 partitions contribute nothing; only (6), (5,1), (4,2),
(3,3) survive.

That is a scope-(b) structural exclusion with an exact named invariant: **no
per-block weight on a >= 3-row partition can change this sum.** It bounds where
a seventh ansatz could act without proposing one — and it explains the shape of
the six refutations rather than adding to them.

Scope stated precisely: this excludes contributions THROUGH THIS FORMULA. A
separate additive super-pairwise term is untouched, so this is evidence FOR the
AGENTS.md expectation, not against it.

**And the surviving sum is cancellation-dominated.** The four terms:

    (6)     +0.179891    25.1% of total
    (5,1)   -1.269689   177.0%      <- larger than the total by itself
    (4,2)   +0.693688    96.7%
    (3,3)   -0.321336    44.8%
    ----------------------------
    total   -0.717445

sum|term| = 2.4646 against |total| = 0.7174 — a **3.435x cancellation**. So
16.48% capture is NOT "we collected a sixth of the terms"; it is large
alternating terms nearly cancelling and leaving a residue ~6x too small. Any
reweighting of the four survivors fights that cancellation.

**Same phenomenon as the Gram radical, seen from the weights.**
`gramMatrixD_det_eq_zero` (PR #5618, sorry-free) has the q-antisymmetriser —
the (1^3) block, the unique >= 3-row partition of 3 — spanning its radical. The
general-n form `sum_(>=3 rows) dim^2 = n! - Catalan(n)` is verified exactly for
n = 3,4,5,6 and matches PR #5592's TL_n rank. Four faces of one fact:
Gram radical / y_lambda = 0 / TL quotient / closure support.

Probe: `computations/probes/delta_lambda_closure_tl_support_probe.py`, 5/5.


## CORRECTION + root cause: all of it is N = 2

I framed the TL support as a discovered structural constraint on Delta_lambda.
It is exact, but I had the CAUSE wrong, and the cause weakens the claim.

`y_lambda_su_n(n, q, N)` vanishes exactly when `len(lambda) > N` — the ordinary
vanishing of the Schur function `s_lambda(x_1..x_N)` in N variables. Measured at
N = 2,3,4,6 on partitions of 6: surviving partitions go 4 -> 7 -> 9 -> 11, and
the longest surviving column is always exactly N. The producer calls it with
**N = 2**.

So "supported on the Temperley-Lieb quotient" is not a fact about Delta_lambda.
**TL_n IS the SU(2) quotient**, and the support restriction is what choosing
N = 2 means. The exclusion holds, but it is contingent on that modelling choice,
not intrinsic — a materially weaker statement than the one I made.

**And the Gram singularity is the same fact.** Verified symbolically:

    z_D = q^3/(q^2+1) = q^N/[N]_q  at N = 2      ([2]_q = (q^2+1)/q)

Convention D's Markov weight IS the SU(2) parameter. So these six, which I had
been treating as related-but-distinct, are one statement:

  1. z_D is a root of the H_3 Gram determinant                  (PR #5618)
  2. the radical there is the q-antisymmetriser = the (1^3) block
  3. y_lambda = 0 for len(lambda) > 2                           (qou-8iru)
  4. corank = sum_(>=3 rows) dim^2 = n! - Catalan(n)
  5. TL_n is the quotient                                       (PR #5592)
  6. the Delta_lambda closure is supported on <= 2 rows

All six = **N = 2**.

**This does NOT license tuning N.** Choosing N to close the 83.5% gap would be a
seventh fitted ansatz and is exactly what the standing rule forbids. What it
settles is that the SUPPORT question is answered and is not where the closure
lives — which is a negative result, and the useful kind.

Also measured: the cancellation is NOT a forced identity. The ratio moves
1.7x -> 26x over q in [1.02, 2], so no q-independent relation forces the
near-cancellation at q_0; the 3.435x is a property of the anchor, not the
algebra. Scope (a).

Probe updated: `delta_lambda_closure_tl_support_probe.py`, 7/7.


## Item 4 RESOLVED — the mirror penalty is two different quantities

Both hypotheses in the earlier note are now settled.

**"T and 3He were not regenerated together" — REFUTED.**
`delta-lambda-canonical-residual.witness.json` is a single run: one computedAt,
one commitSha, one scriptHash. Every row was regenerated together.

**"The drift was not baseline-only at A=3" — RIGHT, with an exact mechanism.**
Since `Delta_lambda = B_AME / B_pred`,

    penalty = log_q[B_AME(pr)/B_AME(mir)] - log_q[B_pred(pr)/B_pred(mir)]
                     `-- experiment --'            `-- the model --'

The `10A-5` baseline cancels IDENTICALLY, so that half of
`prop:mirror-baseline-cancellation` holds for both pairs by algebra, not luck.
The decomposition reproduces both recorded penalties.

    pair         experiment    model      penalty   dominated by
    3He / T       -0.904361  +0.047047   -0.951407  EXPERIMENT (95%)
    7Be / 7Li     -0.410183  +1.358988   -1.769170  THE MODEL  (77%)

**So the "proton-excess penalty" is not one quantity across A.** At A=3 it
essentially measures the experimental mirror asymmetry — the A=3 mirror energy
comes out -0.76375 MeV, the textbook Coulomb-dominated value — with the model
contributing 5%. At A=7 it is dominated by the model's own 15.2% asymmetry in
B_pred.

That explains the drift asymmetry with no appeal to regeneration order: B_AME
is fixed, so a B_pred change moves only the model half. Multiplicatively
uniform across a pair -> cancels (A=7, invariant); non-uniform -> does not
(A=3, moved).

**The model's mirror asymmetry is sign-backwards at BOTH pairs** — B_pred has
the proton-rich member MORE bound, experiment has it LESS. That is expected,
not a defect: `B_pred = E_0*(tr_M(W_free) - tr_M(W_atom))` carries no EM term
at all, so its asymmetry is purely topological. What is new is the SIZE —
negligible at A=3, dominant and wrong-signed at A=7.

Scope (a). Does not bear on the A=3 mirror-split mechanism of
`docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md`, which
targets the EM-active channel and records the derived Coulomb/strong ratio
`tanh(ln q_0) ~ 0.10396`. That audit asks what should supply the missing piece;
this measures what the penalty is made of.

STRENGTHENS the existing "magnitude is NOT a single derivable number" verdict
and sharpens it: the two penalties are not the same physical quantity, so no
single derivation should be expected to produce both.

Probe: `computations/probes/mirror_penalty_decomposition_probe.py`, 5/5.

Noted in passing, not chased: `delta_lambda_canonical_residual.py` does
`float(r["B_MeV"])` and imports `math` — a float64 path in a producer, which
the precision discipline forbids. It bounds the precision of everything above.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carrier M6 (qou-2cof) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

A content block of kind `theorem` whose statement opens 'Theorem (convention
C).' with its own section saying the reading does not survive D. Honestly
scoped, and the live question -- may a `theorem` block stand on an excised
convention? -- is an owner call. One of the 23 paper-side residuals today's
scan flagged.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


---

## 2026-10-10 — ITEM 3 SETTLED: the supergolden root IS a convention-C artefact, by exact division

Re-audit of the C→D migration tracker (session epic `qou-am5t`). This bean's
item 3 said the question was *"answerable directly from the generic form"*. It
is, and the answer is unambiguous. Probe:
[`computations/probes/gram_h3_supergolden_is_convention_c_artefact_probe.py`](../../computations/probes/gram_h3_supergolden_is_convention_c_artefact_probe.py)
— **6/6 checks, exit 0**, witness
`computations/probes/gram-h3-supergolden-is-convention-c-artefact.witness.json`.

### The answer

Taking the generic factorisation this bean records,
`det = −(z−q)⁵(qz+1)⁵((q²+1)z − q³)(q³z + qz + 1)/q⁸`, and substituting each
convention's `z`:

| factor | under C (`q = u²`, `z_C = u/(u²+1)`) | under D (`z_D = q³/(q²+1)`) |
|---|---|---|
| `(z − q)` | **`−u(u³ + u − 1)/(u²+1)`** | `−q/(q²+1)` — **no positive root** |
| `(qz + 1)` | `(u³ + u² + 1)/(u²+1)` — no positive root | `(q²−q+1)(q²+q+1)/(q²+1)` — none |
| `((q²+1)z − q³)` | `−u(u−1)(u⁶+u⁵+2u⁴+u³+u²+u+1)/(u²+1)` | **`0` identically** |
| `(q³z + qz + 1)` | `(u+1)(u⁶−u⁵+u⁴−u³+2u²−u+1)/(u²+1)` | `q⁴+1` — none |

**The supergolden cubic is the numerator of `(z − q)` under convention C,
exactly.** Dividing `numer(z_C − q) = −u(u³+u−1)` by `u³+u−1` gives quotient
`−u` and remainder **0** in `ℚ[u]`. That is the whole verdict, and it is an
exact polynomial identity — not a numerical zero.

**Under D the same factor is nowhere zero.** `z_D − q = −q/(q²+1)`, whose
numerator `−q` has no positive root; at `q = (1/ψ)²` it is `−0.3826…`.

**The two frames' det-vanishings have DISJOINT mechanisms**, which is the part
that settles the physics reading:

- **C** vanishes through `(z−q)⁵` at `u = 1/ψ ≈ 0.6823278038280193…`.
- **D** vanishes through `((q²+1)z − q³) ≡ 0` — the Markov-parameter relation
  itself, i.e. `markovWeightD_root`, the declaration this bean records as
  added "so a later relabel cannot silence it". Under C *that same factor*
  vanishes on `u > 0` only at `u = 1`, i.e. `q = 1`, the classical point —
  **not** the supergolden value.

So neither threshold is the other's image. `1/ψ` is the root that writing `z`
in convention C creates in the factor `(z − q)`; it has no D-frame counterpart.

### Why the verdict does NOT rest on the obvious numerical check

Evaluating `z_C − q` at a float64 root of `u³+u−1` returns `5.55e-17`. That is
the floor of float64, and reporting it as agreement would be precisely the
practice AGENTS.md forbids — *"never report a float64 agreement as exact,
identical, or to N digits"*. The probe records it only to say why it is not
the evidence. The evidence is check 1's exact division.

### Scope: (a), NOT (b) — and this is the part that matters for item 2

This is **not** a structural exclusion of a supergolden feature anywhere in
the framework. It is the narrower claim that *this* threshold, in *this*
determinant, is an artefact of *this* substitution.

**But it does change the standing of item 2's second option.** This bean
offers, as an honest disposition of `prop:spectrahedral-phase-collapse`,
re-deriving "whether some other D-frame object (the Gram on the radical
quotient, which `gram-matrix-dual.witness.json` already carries as
`gram_quotient_inverse`) has a supergolden rank drop, which would be a real
result rather than a relabel." That search is still permitted — nothing here
forbids it — but an agent taking it should know it is **looking for a new
result, not recovering an old one**: the supergolden value is not a
frame-independent feature of the Gram determinant, so there is no prior reason
to expect it to reappear. Expecting it would be selection against a target the
measurement has just removed.

### What this does NOT settle, and is not mine to settle

- **Item 1 (the `gramMatrix` → `gramMatrixC` / `gramMatrixD` rename)** —
  untouched. ~15 declarations and one downstream importer; it belongs with
  item 2 as this bean says.
- **Item 2 (what the content block should say instead)** — untouched. That is
  authoring in a second content block and is an owner call. The measurement
  above is an input to it, not a decision.
- The **convention-C theorems are correct theorems about a non-canonical
  frame** and are not touched. Per AGENTS.md a Lean-proved piece is a
  permanent contribution; this probe scopes a *reading*, not a proof.
- The probe **consumes** the generic factorisation from this bean and
  `gram_h3_convention_frame_probe.py`; it does not re-derive the determinant.

### Status

Staying `todo`: items 1 and 2 are open and both need the owner. Item 3 is
closed with a probe and a witness.

Reproduce:

```sh
python3 computations/probes/gram_h3_supergolden_is_convention_c_artefact_probe.py
```

## Round 76 Progress (2026-11-17T12:02:46Z)
- Advanced in PR `litlfred/qou#8337` (branch `feat/round76-torusmass-pinchoct-gramsig-motivic-spectrahedral-43c1`, head `df1ab810bdd422f72dc74878dc341f5f55564271`).
