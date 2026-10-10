---
# qou-8xb1
title: 'NO-FLOAT64: hecke_characters.build_seminormal_matrices still f64-bound (qou-d8gq fixed only the pyhecke twin)'
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-25T16:38:19Z
updated_at: 2026-10-04T15:11:38Z
parent: qou-9nnz
---

## Found 2026-08-25 while draining the 5 NEW raw-float64 witnesses on main

`qou-d8gq` (completed) fixed the f64-by-allocation defect in
`tools/pyhecke/python/pyhecke/syt_prefix_cache.py::build_seminormal_matrices_cached`:

    M = np.zeros((dim, dim), dtype=_value_dtype(vals))   # dtype follows the values

**Its twin was not fixed.** `computations/hecke/hecke_characters.py::build_seminormal_matrices`
still carries the identical line, and two coercions that make it strictly worse:

    168:  q_local = float(q0) if q is None else float(q)     <-- destroys q AT THE INPUT
    215:  b = float(mp.sqrt(abs(b_sq)))                      <-- computes in mpmath, throws it away
    228:  M = np.zeros((dim, dim))                           <-- the exact line qou-d8gq fixed

Line 168 is the important difference. `qou-d8gq`'s twin lost precision at the
*allocation*, so a dtype-aware container fixed it. This one coerces the caller's
`q` on entry, so **a dtype-aware allocation alone would not help** -- by the time
values are computed there is nothing left to preserve.

MEASURED (mirroring qou-d8gq's own before-table), shape (3,2,1), dim=16:

    q as f64 : dtype=float64  entry type=float64
    q as mpf : dtype=float64  entry type=float64
    bit-identical output for f64 vs mpf q : True

So passing `q_parameter.Q_MP` to this builder buys nothing, silently.

## Blast radius

102 consumers under `computations/` (72 repo-wide excluding the generated
`qou-mass/_internal/` mirror and tools), of which **65 emit witnesses**. Every
one is float64-bound by construction regardless of the q it passes.

## NOT a drive-by fix -- the coercion is DELIBERATE

The comment at line 377 records why:

    "Normalize q_value to float ONCE here, and use q_f consistently in both the
     q= override AND the h_local computation below -- so callers passing mpmath /
     str / numeric types don't break NumPy dtype handling further down
     (per Copilot review on PR #1861)."

So this is a design decision to protect numpy dtype handling, not an oversight.
Changing it is a real infra change needing its own PR: `_value_dtype`-style
dispatch, an mpf-safe `b = mp.sqrt(...)`, a guard for the scipy sparse path
(scipy rejects `dtype object` -- the su4_1111 defect class), and a check that
all 65 witness-emitting consumers are bit-identical on the f64 path.

`qou-d8gq` already establishes the trade this reopens: honest mpf matmul measured
**642x** slower at dim=162. Correct-and-slow vs fast-and-forbidden is the owner's
call, and it is the same call there.

## Why it surfaced here

`computations/deltalambda/deuteron_interface_handle_curvature_probe.py` is one of
the five NEW raw-float64-dirty witnesses the ratchet flags on main (42 fields).
It calls THIS builder, so it is f64-bound at the source. The other four in that
batch were pure-python/complex and are fixed (ffb57ab2d, 808156bb4, ca3fd097c).

**This one must NOT be "fixed" by wrapping `_precision.fmt` around its outputs.**
That is the float64-padding defect by construction -- `fmt()` renders a 53-bit
value to the full serialization width so it READS as measured while carrying ~15
significant digits, which is the shape `_precision.py`'s own docstring warns
about and the float64-padding ratchet exists to catch. There is no honest quick
fix for this probe; it is blocked on this bean.

## Gate gap (inherited from qou-d8gq, still open)

`numpy_mpmath_dtype_leak_audit.py` is blocking and reports 0 candidates with this
leak live -- its scope is `d_for_ctype` consumers and `hoefsmit_numpy.py`, so it
does not see `np.zeros(...)` allocations that later receive mpf, and it does not
see an input-side `float(q)` coercion at all. A detector keyed on the ALLOCATION
would still miss line 168.


## CORRECTIONS 2026-08-25, from the #5763 exchange — three of my numbers/claims were wrong

**1. Blast radius was inflated. 64/53, not 102/65.** My `grep -rln build_seminormal_matrices computations/` counted `_deprecated/`:

    all matches under computations/            102   <- what I reported
    excluding _deprecated/                      64   <- the real direct-caller count
      ... of those, emitting a witness          53   (WitnessBuilder/write_witness/witness.json)
      ... counting only literal "witness.json"  32

#5763 independently reported 64 direct callers / 55 witness-emitting. The 53-vs-55 gap is
definitional (which emit-idiom you grep for), not a disagreement. **Use 64 / ~53.**

**2. "The coercion is DELIBERATE" attributed the rationale to the wrong line — and the
truth is the opposite.** I wrote that line 168 is documented as intentional, citing the
#1861 Copilot comment. Verified: there are TWO coercions in TWO functions.

    line 168  in build_seminormal_matrices (def at 142)
              comment: "Resolve q (override or module default). Derive amplitude h locally."
              -> NO rationale. UNDOCUMENTED.

    line 381  in chi_lambda_braid (def at 295)
              comment: "...so callers passing mpmath / str / numeric types don't break
                        NumPy dtype handling further down (per Copilot review on PR #1861)."
              -> this is the documented one, and it is CALLER-side.

So the builder's own input coercion carries no recorded justification; only the character
function's does. This strengthens the defect (nothing documents why the builder throws q
away) while weakening my "deliberate design, hands off" framing.

**3. The 642x is MATMUL, not construction — my text was right, my emphasis was not.**
`qou-d8gq`'s 642x is mpf matrix MULTIPLICATION at dim=162. #5763 measured mpf
CONSTRUCTION separately: dim 16 -> 0.7x, dim 35 -> 21.5x, dim 162 -> 9.8x, dim 168 -> 32.4x.
Two independent costs. Construction is ~10-30x; a consumer that constructs AND multiplies
at dim ~162+ still pays the 642x on top.

## RESOLVED by #5763 — additively, which is better than the fix I was weighing

I recorded this as blocked and treated the fix as "modify the builder, 64 consumers, needs
owner sign-off". #5763 took the route I did not consider: **add
`build_seminormal_matrices_mp` alongside, returning `mp.matrix` instead of `np.ndarray`.**
Nothing existing modified, no caller changed, so the thing the #1861 comment protects
(numpy dtype handling in the f64 path) is untouched by construction. Verified there against
the f64 builder across all 11 partitions of 6: max deviation 4.441e-16 (2 ulp).

`deuteron-interface-handle-curvature` IS therefore drained, and the ratchet is NEW 5 -> 0 on
that branch.

**What remains open, and why this bean stays alive:** the f64 builder itself is unchanged, so
every one of the ~64 direct callers still gets float64 unless it opts into the `_mp` variant.
The silent part is the live defect -- passing `Q_MP` to `build_seminormal_matrices` still
returns bit-identical f64 output with no warning. A caller that believes it asked for
precision still does not get it. Options, unranked: raise on an mpf argument, warn, or
dispatch to the `_mp` builder. Any of the three needs the adoption trade in item 3 weighed
per-consumer, which is the owner call this bean was opened for.


## CLOSED 2026-08-25 — the silent path is shut

Two halves, landed separately:

  #5763  added `build_seminormal_matrices_mp` (exact mpmath twin, `mp.matrix`),
         additively -- nothing existing modified, verified to 2 ulp across all
         11 partitions of 6.
  this   makes the float64 builder REFUSE an mpmath `q` instead of silently
         truncating it: `SeminormalPrecisionLoss(ValueError)`, message names
         the twin.

The defect this bean was opened for -- "passing Q_MP returns bit-identical
float64 with no signal" -- is now impossible. A caller either gets precision
(the `_mp` twin) or an error naming it; it can no longer get a wrong number
quietly.

Narrow by design: `str`, `Fraction` and plain numerics still coerce, because
the #1861 rationale records that callers legitimately pass them. Only the
mpmath types are refused.

Verified: zero callers passed an mpf when this landed, so nothing changed
today; float/str/None paths all still build at dim 16 dtype float64; the
qou-mass facade is BYTE-IDENTICAL to main on `compute_tr_M(1,1)`,
`predict('2H')`, `predict('4He')`; vendor mirror regenerated by
`sync-qou-mass-vendor.py`, never hand-edited.

## NOT closed by this, and deliberately left open elsewhere

**Adoption.** All ~64 direct callers still use the float64 builder. That is
not a defect and not silent any more -- it is a per-consumer cost question,
and #5763 measured both halves of it: construction ~10-30x (dim 16 0.7x,
dim 35 21.5x, dim 162 9.8x, dim 168 32.4x) and, separately, `qou-d8gq`'s
642x for mpf matmul at dim 162. Free at small dim, needs weighing at
dim ~162+. Whoever drains a specific probe should decide for that probe.

**My three filed numbers were wrong** and are corrected in the section above:
64/~53 not 102/65; the #1861 comment documents line 381 in `chi_lambda_braid`,
NOT line 168 in the builder, whose coercion has no recorded rationale at all;
and the 642x is matmul, not construction.


## REOPENED then re-closed 2026-08-25 — owner asked "still float? if so, fix"

It was. The first pass only made the builder REFUSE an `mpf`; the caller still
could not get exact arithmetic through it. Now it DISPATCHES on the operand:

    mpf / mpc  in  ->  exact `mp.matrix`  (delegates to the `_mp` twin)
    float/str/None ->  float64 `ndarray`  (unchanged, byte-identical facade)

Same shape `qou-d8gq` landed for the pyhecke twin: the decision follows the
value, not a flag. `sparse=True` + `mpf` refuses -- scipy.sparse has no dtype
for `mpf`, the su4_1111 boundary.

## The default stays float64, and this is the finding worth keeping

Flipping `q=None` to the mpf substrate constant looks like the obvious "fix it"
and is a FALSE one. Measured on `mp.matrix`:

    np.trace(sigma)             -> float64   silently re-truncated
    np.abs(sigma)**2            -> float64   silently re-truncated
    np.eye(d) @ sigma           -> float64   silently re-truncated
    np.sum(np.abs(sigma)**2)    -> float64   silently re-truncated
    sigma @ sigma  (mpmath @)   -> mpf       preserved

Only mpmath's own operator preserves precision. numpy accepts `mp.matrix`
happily and hands back float64 -- it does NOT raise, which is what makes this
dangerous. So flipping the default would leave the ~64 q=None callers producing
float64 results while LOOKING exact: strictly worse than the honest float64
they get today, because the loss would no longer be visible anywhere.

The fourth line is not a toy. `np.sum(np.abs(M)**2)` is exactly what the
deuteron probe's `fro2()` computes -- the probe that started this whole bean.
Had the default been flipped, that probe would have "adopted mpf" and gone on
emitting float64 Frobenius norms.

**Generalisation worth carrying:** exactness must be CARRIED by the consumer,
not merely handed to it. Handing a consumer exact inputs is necessary and not
sufficient; every operation in its chain has to preserve them. This is why
per-consumer opt-in is the right shape and why "make the library exact" is not,
by itself, a fix.

Construction cost measured here: dim 9 6.0x, dim 16 7.1x, dim 162 33.0x
(consistent with #5763). Plus qou-d8gq's 642x for mpf matmul at dim 162.

Also corrected the `_mp` docstring, which still claimed the float64 builder
"cannot be made otherwise without moving numbers for its 64 live callers".
It has been, and without moving them.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
