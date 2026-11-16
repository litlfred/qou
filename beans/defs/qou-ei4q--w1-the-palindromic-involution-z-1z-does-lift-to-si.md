---
# qou-ei4q
title: 'W1: the palindromic involution z -> 1/z DOES lift to Sigma, and it is the elliptic involution'
status: in-progress
pr: 8194
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:35:46Z
updated_at: 2026-10-04T15:11:12Z
parent: qou-frzo
---

## Result (2026-09-08) — POSITIVE, then a wider prune

**The involution lifts.** `z^3 * P(X/z, 1/z) = P(X, z)` for every `z != 0`, so
`iota~ : (X,z) |-> (X/z, 1/z)` carries Sigma to Sigma. It is an involution, and it
is the **first nontrivial automorphism of Sigma the corpus records**. Lean
`QOU.Mass.PalindromicInvolutionLift.colorCubic_inv_lift`, sorry-free.

Not new: the palindromy of `D` itself, used since 2026-05-19 at the coefficient
level (`w = z + 1/z` -> reciprocal cubic `16w^3+24w^2-13w+2`, three Galois
orbits). New: that it lifts to the CURVE.

**It is the elliptic involution.** 4 fixed points (all 3 over `z=1`, `X=0` over
`z=-1`, none over `0`/`infinity` which it swaps), both fibres unramified
(`D(1)=200`, `D(-1)=4`). Sigma has genus 1 (#7114), so Riemann-Hurwitz gives
`2*1-2 = 2(2g'-2) + 4`, `g' = 0`: `Sigma/iota~ ~ P^1`. And the corpus's own
`w = z + 1/z` IS that quotient coordinate on the base -- it has been computing on
the quotient for months without recording it.

**And the prune got WIDER than #6769.** Fixed points of a Moebius map solve a
quadratic, so three of them force the identity, so `Stab(B)` embeds in `S_6` and
every base automorphism preserving `B` has order <= 6 -- FINITE, for any
squarefree sextic. `q_0 > 1` has infinite order. So **no base automorphism of
`P^1` supplies the W1 q-shift**, not merely no dilation. This SUBSUMES #6769
rather than sitting beside it.

Explicit count (120 dps, labelled numerical, NOT exact): `Stab(B) = {id, iota} =
Z/2`, margin 119 orders of magnitude, realised permutations `id` and
`(0 1)(2 5)(3 4)` -- `iota` acting freely on the roots, as it must since
`D(+-1) != 0`.

**Scope.** (b) for "a base automorphism supplies the q-shift", with the invariants
cited. NOT excluded: a q-difference structure not arising from a base automorphism
at all; route 3 (RSZ/Sauloy), now supplied with a genus AND a distinguished
involution; anything from the monodromy representation. `D_q` is NOT constructed.

Prose-only, as in #6769/#7114: the covering-space step, and the finiteness of
`Stab(B)` (elementary, measured in T9a, but needs Moebius machinery Mathlib lacks).

Audit: `docs/audits/2026-09-08-w1-palindromic-involution-lifts-and-is-elliptic.md`.
Probe 32/32. Lean 16 decls, no `sorryAx`, verified from SOURCE (both dependencies
rebuilt first -- one olean predates its source by a month, the other did not exist).

Rides along: a fix to `scripts/lean-shadow-verify.sh`, which picked a 2-olean tree
over the restored 2442-olean one because a SessionStart `lake build` was filling
the paper package while it ran.

STAYS in-progress: W1 (`qou-d8de`) is open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8194)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/W1SpectralRigidityAndEllipticInvolution.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/w1-spectral-rigidity-and-elliptic-involution.witness.json` (`scriptHash: 5e848ba624fe`, `scriptCommitSha: 62bd8cb179998d43808552b8955ff0b3857febae`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8194 (`b0ca85df1a1275572e6a829fccdff9eb4eff2fe0`).
