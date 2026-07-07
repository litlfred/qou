# Borromean explicit operator — the degree terminus (unifies all routes)

**Date:** 2026-07-07
**Branch:** `claude/aj-conjecture-qou-uz5m6x` (PR #3469)
**Bean:** `n920`
**Supersedes the "next step" of:** the CRT-conditioning audit
(`2026-07-07-borromean-recurrence-reconstruction-conditioning.md`) and the
qZeilberger route-diagnosis (`2026-07-07-borromean-qzeilberger-route-diagnosis.md`).

## The single fact that unifies every attempt

The minimal q-difference recurrence for the Borromean diagonal colored
Jones `J_{B,n}` is **unique** (up to scale and lower-order/shift multiples)
and its coefficients are **intrinsically high-degree in `q`** — the CRT
degree probe (PR #3450) measured a representative coefficient at rational
degree ~126–218. This one fact explains **all** the walls hit:

| Route | Wall | Why (unified) |
|---|---|---|
| Raw CRT reconstruction | ill-conditioned + 5 container restarts | must reconstruct ~deg-126 coeffs — correct complexity, environment-blocked |
| Symbolic `sp.solve` | did not terminate | solving for ~deg-126 rational functions symbolically over the cube summand |
| Fixed-q telescoping | nullity 41–311 | free certificate over-fits at any bounded degree |
| Multi-q telescoping | nullity 150→1159 | **decisive** (below) |

## The decisive experiment (this PR)

`borromean_qzeil_multiq.py` samples the telescoping identity over **varying
q** (killing the fixed-q q0-coincidence objection) and scans the ansatz
q-degree `DQ` at fixed small `(r=5, DX=3, EY=4)`:

| `DQ` | unknowns | nullity | operator-part vectors |
|---|---|---|---|
| 2 | 231 | 150 | 72 |
| 4 | 385 | 289 | 145 |
| 8 | 693 | 570 | 294 |
| 12 | 1001 | 862 | 494 |
| 16 | 1309 | 1159 | 772 |

**Reading.** If a low-degree telescoper existed, the operator-part of the
nullspace would **saturate at 1** once `DQ ≥ its q-degree`. Instead it grows
**~linearly with the ansatz** (≈ unknowns/2). Therefore **no low-degree
qZeilberger telescoper exists**; the genuine minimal recurrence is
intrinsically high-degree, and every bounded-degree telescoping solve
over-fits (the operator-part vectors are all spurious — free-certificate
freedom, the same root cause as the `r*=2` op-projection artifact).

## The correction (important)

The qZeilberger-route audit implied q-Gosper normalization was the clean,
*low-degree*, well-scoped next step. **That framing was wrong.** qZeilberger
does **not** reduce the operator's degree — the minimal recurrence for the
sum is unique, the *same* ~deg-126 object regardless of route. A q-Gosper
implementation would still have to reconstruct those ~deg-126 coefficients
**and** produce a certificate — strictly **harder** than the raw operator
reconstruction, not easier.

## Corrected path to the explicit operator (and thus proof)

The right route is the one already built and committed: the **Rust
multi-prime CRT pipeline** (`tools/borromean-recurrence-crt` +
`borromean_recurrence_crt_driver.py`, PR #3450). It is the correct
complexity for a ~deg-126 reconstruction; its *only* blocker was the compute
**environment** — five container reclaims destroyed successive ~35-min runs.
Run in a **persistent** environment (or with the fixed prime-skip + modal
consensus + checkpoint hardening it already carries), it reconstructs the
explicit operator; the exact-symbolic annihilation gate then upgrades the
specific recurrence from **evidence to proof**, and the `q→1` limit gives
the diagonal Borromean A-polynomial. A qZeilberger certificate can be added
afterward for the Lean-formalizable telescoping proof, but it is a
*follow-on*, not a shortcut.

## Epistemic status (restated)

- **Existence** of a recurrence: q-holonomicity **theorem** (Garoufalidis–Lê
  2005 + diagonal closure). Not ours.
- **The specific minimal recurrence** (order 5, window 13): strong mod-p
  **evidence**, not symbolic proof. Ours.
- **Explicit operator + proof**: open, degree-bound-blocked, path = the
  committed CRT pipeline in a persistent environment.

## Disposition

No wiring, no conjecture-status changes. The existence certificate remains
the standing headline. This audit is the terminus of the explicit-operator
investigation: it identifies the true obstruction (intrinsic operator
degree, not an algorithmic gap) and corrects the route recommendation.
