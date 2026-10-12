# Results: Bring loop energy (preregistration-energy.md)

To reproduce, run `python3 -u bring_loop_energy_probe.py`. It writes `results_energy.json`, uses mpmath at 30 dps, exits 0, and passes all 7 checks.

## Pre-registered result

| word | Bring length | simple? | primitive? | E (Möbius) | E_sinh |
|---|---|---|---|---|---|
| gluon_s1_s0 | 4.6031833095 | yes (0 crossings) | yes | 0 | 0 |
| gluon_s1_s1 | 4.6031833095 | yes | yes | 0 | 0 |
| nuc11_gen_grouped | 6.3676503714 | yes | yes | 0 (< 1e-32) | 0 (< 1e-32) |
| nuc9, gluon_s0_s1, gluon_s0_s0 | — | no loop | — | undefined (§3) | undefined |

- **Grid values.** For class A, every grid size (N = 120, 240, 480) and both kernels give exactly 0. For gen_grouped the values are 9.4e-33, 2.3e-33 and 5.9e-34. They fall as 1/N², which is the signature of a fixed set of grid points sitting on a rounding-level tie, so they are zero (see below).
- **Verdict under the pre-registration: a tie. Route 2's energy ranks nothing.**
  - Both loops have E = 0. Neither ever comes closer to itself, by a path through the surface, than it is along the loop.
  - §2 says opposite orders across kernels mean "no ranking". Here there is no order at all, under either kernel.
- **What the zero means.** E is 0 exactly when, for every pair of points on the loop, the shortest path between them on the surface is the arc along the loop. Both loops pass that test, so this energy cannot tell them apart. This is a weakness of the chosen energy on a compact surface, recorded rather than repaired: any fix decided now would be chosen after seeing the result.

## Checks

All pass:
- the kernel set is the same with enumeration slack 1 and slack 2;
- the loop's own translation is in the kernel;
- the axis stabiliser has only translation lengths 0 and L, so the loop is primitive;
- the conjugate pair gives the same E.

## POST-HOC (not pre-registered; not used to rank)

- **Self-approach margin.** This is min over loop pairs of (d_X − δ), computed with `margin_diag.py`, N = 60, from the same enumerated kernel.
  - Class A: margin **1.3534**. The nearest return of the loop to itself by another route is 3.6550, against a largest possible arc distance of L/2 = 2.3016.
  - gen_grouped: margin **0 to 29 digits** (−1.5e-29). Antipodal points of the loop are joined by a second path of length exactly L/2 = 3.1838 that leaves the loop.

  So gen_grouped sits exactly on the boundary where this energy would switch on, while class A has room to spare. Agreement to 29 digits suggests an exact symmetry of Bring's surface exchanging the two halves of the gen_grouped loop. That is **not proved**.

  The margin was not pre-registered, so it **may not be used to select a word**. To use it, it would first have to be pre-registered as an energy and then evaluated on new candidates.
- **Enumeration bug, found and fixed during the run.** Near-zero matrix entries printed as different strings (`1e-30` vs `-2e-31`), so one group element got several keys. The first run reported 91 kernel elements for gluon_s1_s0 instead of 83, and never finished for gluon_s1_s1. This affected counting only, not any distance. It was fixed in 6604ad9fba before the numbers above were produced.
