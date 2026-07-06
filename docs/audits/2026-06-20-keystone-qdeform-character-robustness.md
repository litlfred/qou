# Crack #2 — the (2,1)/h⁴ cancellation is robust to q-deformation

**Date:** 2026-06-20
**Branch:** `claude/keystone-qdeform-character-robustness-2026-06-20`
**Status:** Negative / closing result — the q-deformed-Wenzl escape is refuted at the character level
**Follows:** [#2516](https://github.com/litlfred/qou/pull/2516) (branching-shift first crack)
**Script:** [`scripts/keystone_qdeform_character_robustness.py`](scripts/keystone_qdeform_character_robustness.py)

## The open path being closed

Probe #2516 showed the h⁴-bearing `(2,1)` block enters both the muon `(3,2)↓S₃`
and electron `(3,1,1)↓S₃` branchings with the **same classical multiplicity 2**,
so it cancels exactly in the μ/e difference. It left one escape hatch:

> any non-null shift must come from the **q-deformed Wenzl projector weights**
> breaking the (2,1) symmetry.

This crack tests that escape directly, at the character level.

## Test and result

For the 3-strand Borromean braid $\beta = (\sigma_1^{-1}\sigma_2)^3$ (strands 4,5
spectators), compute the honest H₅ ambient-block characters
$\chi_\mu^{H_5}(\beta)$ and compare to the classical-multiplicity prediction
$\sum_{\nu\vdash3} m(\nu;\mu)\,\chi_\nu^{H_3}(\beta)$, sweeping $q$ so $h^4$ runs
from $\sim10^{-4}$ to $\sim0.9$.

| $q$ | $h^4$ | $\chi_{(3,2)}^{H_5}$ | $\chi_{(3,1,1)}^{H_5}$ | $\chi_{(3,1,1)}-\chi_{(3,2)}$ |
|-----|-------|-----|-----|-----|
| 1.05 | 0.00009 | 4.999453 | 5.999453 | **1.000000** |
| 1.10998 ($q_0$) | 0.00191 | 4.988372 | 5.988372 | **1.000000** |
| 1.30 | 0.07936 | 4.479100 | 5.479100 | **1.000000** |
| 1.60 | 0.90369 | −2.140264 | −1.140264 | **1.000000** |

- $\chi_\mu^{H_5}(\beta)$ equals the classical-multiplicity sum **exactly** —
  $\max|\Delta| = 8.9\times10^{-16}$ (machine precision) over all $q$.
- $\chi_{(3,1,1)}^{H_5}(\beta) - \chi_{(3,2)}^{H_5}(\beta) = \chi_{(1,1,1)}^{H_3}(\beta) = 1$
  **identically** ($|\Delta| = 0$), independent of $h$ — even at $h^4\approx0.9$.

## Why (structural)

Generic-$q$ Iwahori–Hecke branching $H_3 \subset H_5$ carries the **same
multiplicities** as the symmetric group $S_3 \subset S_5$ (the Hecke algebra at
generic $q$ has the same representation theory / Young-lattice branching as
$S_n$). The $q$-deformation therefore lives **only** in the shared $H_3$
characters $\chi_\nu^{H_3}(\beta)$, which appear identically in both ambient
blocks and cancel in the difference. The $(2,1)$ channel — and with it the
entire $h^4$ content $\chi_{(2,1)} = 2 - 3h^4 - h^6$ — drops out for **every**
$q$.

## Verdict

The q-deformed-Wenzl-weight escape **does not** rescue an $h^4$-driven muon
shift at the character level. Combining with #2516:

1. At the **multiplicity** level the $(2,1)$/$h^4$ channel cancels (#2516).
2. At the **q-deformed character** level it still cancels, robustly, for all $q$
   (this doc).

So the operator-valued branching mechanism — in **both** its multiplicity form
and its q-deformed-character form — cannot produce the muon shift through the
Borromean $h^4$ channel. The only surviving μ/e asymmetry is the H₅ **Markov
block-weight ratio** $W_{(3,2)}/W_{(3,1,1)} \approx 3.68$ at $q_0$ — order-unity,
not bar-even — i.e. the owner-gated geometric-$W_\lambda$ frontier
([#2488](https://github.com/litlfred/qou/pull/2488)), which is refuted-by-size
as a candidate for the 210 ppb (sub-ppm, anchor-shift-artifact) effect.

This narrows the keystone's remaining live question precisely: any generation
splitting from `conj:s5-so3-fiber-action` must originate in the geometric
construction of the $W_\lambda$ weights themselves, **not** in any projector /
branching / character evaluation of the knot — those are now exhausted and null
on the $h^4$ channel. No fit was introduced.
