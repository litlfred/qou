---
# qou-f2pf
title: lp_shadow_price leaves float64 residue on 6 of 20 blocks its docstring says it zeroes
status: in-progress
pr: 8186
type: task
priority: normal
created_at: 2026-09-12T20:16:18Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-9nnz
---

Found while verifying a sibling's convention claim against `binding_energy`'s
own cone (PR #7229, branch `claude/sv7h-binding-scaling-endtoend-2026-09-12`).
Not a blocker for that PR; deliberately NOT fixed there.

## The claim, with its numbers

`computations/hecke_core_legacy.py:328` `lp_shadow_price(lam)` computes

    y_lam = w_lam / d_lam - 1/[k]_q!,   w_lam = d_q(lam)^2 / [k]_q!

Its docstring asserts the subtrahend "zeroes exactly the two one-dimensional
blocks (k) and (1^k) - and nothing else". Measured over the 193 YSN-bearing
entries of `_PARTITION_TABLE` (k = 2..11), there are **20** such blocks and
the subtraction zeroes only **14** of them:

    (6,)   (1^6)    +4.3368087e-19
    (7,)   (1^7)    -2.7105054e-20
    (9,)   (1^9)    -6.3527471e-22

The other 14 are exactly `0`.

## It is NOT a measurement artifact

Checked, because it is the obvious way to be wrong here: the stored values are
`mpf`, not my own `float()` cast. `type(entry['shadow_price']).__name__` is
`mpf`, and the residues above are printed with `mp.nstr`. So this is the corpus
narrowing, not the probe's.

## Where it comes from

`wedderburn_weight` (pyhecke.wedderburn) is `q_dimension(lam)**2 /
q_factorial(n)` and returns `mpf`; `lp_shadow_price`'s `y_0 = 1.0 /
q_factorial(k)` starts from a Python float literal `1.0`, which mpmath
promotes rather than narrows. The residue magnitude (~1e-19 absolute against
neighbouring shadow prices of ~5e-3, i.e. ~1e-16 relative) is the float64
floor, so the narrowing is UPSTREAM, in `q_dimension` or `q_factorial` -
NOT established which, and that is the first thing to measure.

## Why it was not fixed on #7229

`lp_shadow_price` feeds `C_lambda_resolvent_MeV = H_q * y * resolvent * m_e`,
which every binding witness consumes. Carrying `mpf` further up that chain
moves numbers corpus-wide. Under the 2026-09-07 ASK-THE-OWNER directive that
is arguably exemption 1 (it removes a float64 path), but it is not a drive-by
on a PR whose scope is a fallback warning and a timing probe.

## Next honest step

1. Bisect the narrowing: instrument `q_dimension` / `q_factorial` at the three
   failing k (6, 7, 9) and find which returns a float-backed value.
2. Decide whether the docstring or the code is wrong - "zeroes exactly" may
   simply be an over-claim about an approximate cancellation, in which case the
   fix is one sentence, not an mpf migration.
3. Only then consider the chain fix, with the witness blast radius measured
   first.

Do not "fix" this by thresholding the residue to zero. That hides the input.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-9nnz`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.


## Round 51 Progress
- [x] PR https://github.com/litlfred/qou/pull/8186 (`fb4f6926d3f96fd99209ef3cb58128ff0ce2701b`): updated `lp_shadow_price(partition)` in `computations/hecke_core_legacy.py` to return exact `_mp.mpf(0)` whenever `k == 0 or d == 1` (covering all 20 of 20 one-dimensional blocks `(k,)` and `(1^k)` for k=2..11).
