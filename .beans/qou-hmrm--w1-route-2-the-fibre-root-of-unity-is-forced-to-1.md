---
# qou-hmrm
title: 'W1 route 2: the fibre root of unity is forced to -1 by squarefreeness, and C1 degenerates there'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T17:48:05Z
updated_at: 2026-09-07T17:48:36Z
---

## The claim being tested

Route 2 of `qou-d8de` (W1) reads, verbatim: *"Root-of-unity fibre monodromy. The
fibre singularity is a root of unity; a q-difference connection may arise naturally
from its local monodromy. Construct the q-D-module from that datum."*

Routes 1's three charts are now all closed (#6695, #6738, #6769), so this is the
live route. Before constructing anything, the formalize-first question: **which root
of unity can that datum actually supply?**

## The structural argument (to be formalized + probed)

1. The branch sextic `D(z) = 16z^6+24z^5+35z^4+50z^3+35z^2+24z+16 = -disc_X P` is
   **squarefree** (already measured, #6769 probe §1: six distinct roots).
2. For a degree-3 cover, the discriminant vanishes to order 1 at a **simple** branch
   (two sheets colliding, ramification index 2) and to order >= 2 at a total branch
   (three sheets, index 3). Squarefree discriminant therefore forces **every finite
   branch point to be simple**.
3. A simple branch point's local monodromy is a **transposition** — order exactly 2.
   So the root of unity the fibre datum supplies is `-1`, and nothing else: never a
   primitive cube root, never anything of higher order.
4. At `q = -1` the quantum integers collapse: `[n]_{-1} = ((-1)^n - 1)/(-2)`, i.e.
   `0` for even `n` and `1` for odd `n`. The C1 carrier
   `[m+2]_q b_{m+2} = b_{m+1} + b_m` then reads `0 = b_{m+1} + b_m` whenever `m` is
   even — a constraint, not a recurrence, leaving `b_{m+2}` undetermined.

If 1-4 hold, the most natural reading of route 2 — "q is the eigenvalue of the local
fibre monodromy" — cannot produce the C1 symbol, and says so structurally rather
than numerically.

## Scope discipline (STRICT, decided before running)

- Scope **(b)** applies only to the identification *q = the local fibre-monodromy
  eigenvalue*, and only with the invariant cited (squarefreeness => simple branches
  => order 2; plus the `[2k]_{-1} = 0` vanishing).
- Every looser reading of route 2 — a q-difference structure that *uses* the
  monodromy representation without setting `q` to its eigenvalue, or one built from
  the monodromy at infinity, or from the S_3 global group rather than a local
  generator — is scope **(a)** at most and stays open. Do not write (b) over them.

## Also to measure (cheap, and it bears on route 3)

Ramification over `z = infinity`, and hence the genus of Sigma by Riemann-Hurwitz.
Six simple finite branch points and a degree-3 cover give `2g-2 = -6 + 6 = 0`,
i.e. `g = 1`, IF infinity is unramified. Whether Sigma is elliptic is not decoration:
it constrains which q-difference structures the curve admits at all, which is exactly
what route 3 (RSZ / Sauloy) would need as input.
