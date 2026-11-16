---
# qou-hmrm
title: 'W1 route 2: the fibre root of unity is forced to -1 by squarefreeness, and C1 degenerates there'
status: in-progress
pr: 8194
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T17:48:05Z
updated_at: 2026-10-04T15:14:20Z
parent: qou-frzo
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


## RESULT (2026-09-07) — confirmed, and Sigma turns out to be elliptic

All four steps hold. Lean `QOU.Mass.FibreMonodromyOrderTwo`, sorry-free, generic
`[Field K] [CharZero K]`, `lean -DautoImplicit=false -s 65536` exit 0 first attempt,
axioms clean on all seven declarations. Probe 23/23, exit 0, exact sympy over QQ.

- **No triple root, ever.** `sympy.solve` on the three coefficient equations returns
  `[]`, and the two eliminations reproduce the Lean's `2z^2+z+2` and
  `26z^3+24z^2+24z+26` exactly, with `gcd = 1`. So no TOTAL branch point exists.
- **Every branch point is therefore simple** (D squarefree, multiplicity 1
  throughout), local monodromy a transposition, order exactly 2, root of unity `-1`.
- **C1's own hypothesis is false there.** `qlift_normalized_kernel_exists` assumes
  `forall k >= 1, [k]_q != 0`; `[2]_{-1} = 0`. The carrier does not apply at `q = -1`
  rather than merely degenerating.
- **Control fires.** `X^3 - z` returns triple root `{R: 0, Z: 0}` and `disc = -27z^2`
  (order 2, not 1), so the empty answer above is about the colour cubic, not about
  the searcher.

## The unplanned finding: Sigma is an ELLIPTIC curve, g = 1

The fibre at `z = infinity` is `(Y+1)(Y^2+1)`, `disc = -16` — three distinct sheets,
so the cover is **unramified at infinity**. Riemann-Hurwitz then gives
`2g - 2 = 3*(-2) + 6 = 0`, i.e. **g = 1**. Nothing in the corpus had computed the
genus of Sigma.

Two consequences worth carrying:

1. **Route 3 needs this.** Ramis-Sauloy-Zhang / Sauloy's local classification of
   q-difference modules is stated against a curve whose genus is known; the framework
   import now has its input rather than having to compute it first.
2. **A symmetry #6769 does NOT cover.** That result closes dilations `z -> lambda z`.
   The fibre at infinity coinciding with the fibre at `z = 0` is the palindromic
   `z -> 1/z` symmetry of D appearing geometrically — and `z -> 1/z` is not of the
   form `z -> lambda z`, so it is untouched by the dilation rigidity. If any
   automorphism of Sigma is going to carry a q-structure, that involution is where to
   look next.

## Scope held as declared

Scope (b) is written ONLY over "q = the eigenvalue of the local fibre monodromy".
The looser readings named in the plan above — monodromy representation without
eigenvalue identification, a construction at infinity, the global S_3 — stay open at
scope (a) at most, and the audit says so explicitly. `D_q` is NOT constructed.

Audit: docs/audits/2026-09-07-w1-route2-fibre-monodromy-is-order-two.md



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8194)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/W1SpectralRigidityAndEllipticInvolution.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/w1-spectral-rigidity-and-elliptic-involution.witness.json` (`scriptHash: 5e848ba624fe`, `scriptCommitSha: 62bd8cb179998d43808552b8955ff0b3857febae`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8194 (`b0ca85df1a1275572e6a829fccdff9eb4eff2fe0`).
