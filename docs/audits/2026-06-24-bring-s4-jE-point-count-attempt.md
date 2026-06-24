# `j(Bring/S₄)` via equivariant point-counting — attempt + honest negative

**Date:** 2026-06-24
**Branch:** `claude/clever-volta-uir8ay`
**Status:** Task-2 follow-up to merged #2710. `j(E)` **not obtained**; the one
route #2710 left unblocked (equivariant point-counting) is shown to fail naively
for a precise structural reason, and the *correct* route is sharpened. No fit.
**Probe:** [`computations/substrate/bring_s4_jE_point_count_probe.py`](../../computations/substrate/bring_s4_jE_point_count_probe.py)
**Witness:** [`computations/substrate/bring-s4-jE-point-count.witness.json`](../../computations/substrate/bring-s4-jE-point-count.witness.json)
**Builds on:** [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
(#2710: `Jac(Bring) ~ E⁴`, `E = Bring/S₄` elliptic; `j(E)` flagged as the
"bounded next step", with the symbolic fixed-field and period routes blocked).

## The attempt

`j(E)` identifies `E` once a few Frobenius traces `a_p(E) = p+1−|E(F_p)|` are
known (Hasse: `|a_p| ≤ 2√p`). Point-counting needs neither the fixed field nor
periods, so it is the natural unblocked route. SageMath 10.9 was provisioned
(conda-forge) for this; the counting itself is exact mod-p arithmetic (plain
Python — no Sage dependency).

## The result — naive count fails (structural, predicted)

| p | `|Bring(F_p)|` | `a_p(Bring)` | naive `|E(F_p)|` (S₄-orbits) | naive `a_p(E)` | Hasse |
|---|---|---|---|---|---|
| 7  | 0  | 8   | 0 | 8  | ✗ |
| 11 | 24 | −12 | 1 | 11 | ✗ |
| 13 | 30 | −16 | 2 | 12 | ✗ |
| 17 | 30 | −12 | 2 | 16 | ✗ |
| 19 | 0  | 20  | 0 | 20 | ✗ |
| 23 | 0  | 24  | 0 | 23 | ✗ |
| 29 | 30 | 0   | 2 | 28 | ✗ |
| 31 | 24 | 8   | 1 | 31 | ✗ |

The `Bring(F_p)` counts are **correct** (Hasse-OK for genus 4: `|a_p(Bring)| ≤
8√p`). But the **naive** `|E(F_p)| ≈ #(S₄-orbits of Bring(F_p))` gives `a_p(E) ≈ p`
— a gross Hasse violation at every prime. Reason: `|Bring(F_p)|` is small, so its
S₄-orbits number only 0–2, whereas `|E(F_p)|` should be `~p+1`. The missing
`E`-points come from S₄-orbits in `Bring(F̄_p)` that are Galois-stable **as sets**
but carry **no F_p-rational Bring point** (their points are conjugate over an
extension). The naive count, restricted to orbits with an F_p representative, is
blind to these — so it is a (useless) lower bound, not `|E(F_p)|`.

## The correct route (sharpened next step)

The exact equivariant (Lefschetz) count is

$$
  |E(F_p)| \;=\; \frac{1}{|S_4|}\sum_{g\in S_4}\#\{P\in \mathrm{Bring}(\overline{\mathbb F}_p): \mathrm{Frob}(P)=g\cdot P\},
$$

a sum of **g-twisted** point counts living in `F_{p^{ord(g)}}` (one twisted form
per S₄ conjugacy class). That — or **Magma's** function-field fixed field
`K(Bring)^{S₄}` — is what actually yields `j(E)`. Both are genuine
twisted-form / fixed-field computations, beyond the elementary shortcut; left as
the concrete next step.

## What stands regardless

`j(E)` is a *fixed-curve* datum. The keystone's **structural** results are
independent of it and remain: `Jac(Bring) ~ E⁴` (#2710), the rank-2 W-plane
`= E = Bring/S₄`, the genus-4 → genus-1 reduction (`M` a 2×2 `SL₂`), and the
`[2]_q`-rational, hyperbolic trace target `tr B = 3(3[2]_q²+2)/(4([2]_q+2))`
(this branch's lever-1 sharpening). The owner-gated keystone is still `E(q)` and
`tr M(q₀) = 2.6424`.
