# Results — link Möbius energy of canonical closed-braid embeddings, flowed

Route 1 of the owner's energy / O'Hara selection question (beans `qou-99qc`,
`qou-pzsi`). qou `origin/main` = `aa914b606a`, scratch worktree
`/home/user/qou-verify-4`, left clean (nothing committed, no witness rewritten).
Pre-registration: `preregistration.md`, written before any candidate energy was
computed. **Numerical evidence only.** No Q_beta, CODATA value or mass number was
used anywhere in this directory, and none appears next to any energy.

Conventions: Freedman–He–Wang normalisation (round circle = 4);
E_tot = E(K1) + E(K2) + 2·E(K1,K2). All flow arithmetic is float64. Final
energies come from a spectral trapezoid rule on the trigonometric interpolant of
the flowed polygon. The M = 8N and M = 16N evaluations agree to ≤ 1.5e-11 in
every run, so quadrature is never the limiting error. The limiting error is the
flow, and it is quoted below.

## 0. Exact topology, and the pre-registered prediction it produced

From `braid_topology.py` (integer and sympy arithmetic only; the Jones polynomial
by Kauffman-bracket state sum, the Alexander polynomial by Burau). The four
two-crossing gluon dressings close to **two** link types, not four:

| class | words | lk | components |
|---|---|---|---|
| A | `gluon_s0_s1`, `gluon_s0_s0` (= `nuc11_interleaved`, same word) | 4 | T(2,3) ∪ unknot |
| B | `gluon_s1_s0`, `gluon_s1_s1` | 3 | T(2,5) ∪ unknot |
| — | `nuc9` | 3 | T(2,3) ∪ unknot |
| — | `nuc11_gen_grouped` | 2 | T(2,7) ∪ unknot |

The words within a class are conjugate. The derivations are in the
preregistration, §0: braid relation, cyclic rotation, and conjugation by Δ.
Their Jones and Alexander polynomials agree. **σ1σ0 and σ0σ1 are different
links** (lk 3 vs 4), which agrees with the corpus. The corpus statement that
*all four* dressings are distinct links holds only for its q-shift-decorated
letters. It does not hold for the geometric closures that any embedding energy
sees.

**Pre-registered method test:** conjugate words start from different canonical
embeddings, so their flowed energies must agree within error.
**Result: it passes.** At N = 256 the class-A words give 295.911 and 295.910
(difference 0.0016). The class-B words give 291.173 and 291.289 (difference
0.116).

## 1. Calibration (gate G1–G4): PASS

| gate | result |
|---|---|
| G1. Corpus integrator `cross_energy(R=1, c=√2, N)` on the round Hopf pair | N=64: 19.739208802178717238; relative deviation from 2π² is 1.3e-24 (N=128: 4e-49) |
| G2. My evaluator: round circle | 4 − 1e-13 |
| G2. Stereographic Hopf fibres, generic pole | E12 = 19.739208802179 (rel. 2e-16), E1 = E2 = 4.000000000000 |
| G3. Random inversion applied to the σ1² and nuc9 embeddings | max relative change of E1, E2, E12 is 3e-13 and 2e-14 |
| G4. Flowed σ1², 2-strand embedding: E12 at N = 64 / 128 / 256 | 19.74649 / 19.74182 / 19.74045, all ≥ 2π² = 19.73921 and decreasing. E1, E2 → 4.0005, 4.0002 |
| G4. Flowed σ0σ0σ1 (Hopf via a 3-strand embedding): E12 | 19.75636 / 19.74345 / 19.74008 |
| Flowed E_tot vs exact 8 + 4π² = 47.47842 | σ1²: 47.4816 (+6.7e-5 relative). 3-strand: 47.4805. Both extrapolate to 47.4798 and 47.4779 |
| Hopf flowed from R/a = 2 and 4.5 (N = 64) | 47.5147 and 47.4888, against 47.5000 at R/a = 3. The initial energies were 96.1, 189.3 and 132.1 |
| Trefoil σ1³ (informational) | 74.522 / 74.471 / 74.421 (flow not N-converged). The literature value ≈ 74.4 is quoted from memory and is not held in the corpus |
| T(2,4) σ1⁴ (informational) | 107.0257, with E12 = 45.040 |

The flow approaches 2π² from above, as the Agol–Marques–Neves bound requires. It
also reaches the same Hopf value from two different canonical embeddings and from
three R/a starts.

## 2. Per-candidate table

lk is the Gauss linking number, checked at every step. "Topology" means the start
and end polygons, plus the evaluated smooth interpolant, each pass the Alexander
certificate (link and each component, at t = −1, 2, 3). The displacement
certificate held at every accepted step, and lk was unchanged. Every run below
preserved link type.

Initial energies are at R/a = 3. E∞ is the N-extrapolation; its error bar is
extrapolation spread + quadrature + a landscape floor of 0.177 (see §4). UB is
the smallest certified smooth-curve value found.

| word | comps | lk | initial E1, E2, E12, E_tot | flowed E_tot, N = 64 / 128 / 256 | E∞ ± err | UB | stop reasons | topology |
|---|---|---|---|---|---|---|---|---|
| nuc9 | U + T(2,3) | 3 | 24.13, 204.74, 159.35, **547.58** | 234.929 / 234.716 / 234.609 | **234.50 ± 0.28** | 234.55 | conv / conv / conv | preserved |
| nuc11_interleaved = gluon_s0_s0 | U + T(2,3) | 4 | 40.45, 246.25, 199.27, **685.24** | 297.837 / 296.068 / 295.911 | **295.90 ± 0.32** | 295.91 | conv / conv / conv | preserved |
| gluon_s0_s1 | T(2,3) + U | 4 | 238.89, 36.27, 197.32, **669.81** | 296.644 / 295.867 / 295.910 | **295.92 ± 0.21** | 295.84 | conv / conv / conv | preserved |
| gluon_s1_s0 | T(2,5) + U | 3 | 284.20, 26.02, 180.31, **670.84** | 294.353 / 291.390 / 291.173 | **291.16 ± 0.38** | 291.17 | guard / conv / conv | preserved |
| gluon_s1_s1 | U + T(2,5) | 3 | 29.12, 280.39, 173.66, **656.83** | 292.031 / 291.738 / 291.289 | **291.14 ± 0.48** | 291.29 | conv / conv / guard | preserved |
| nuc11_gen_grouped | T(2,7) + U | 2 | 341.24, 17.51, 165.30, **689.34** | 325.074 / 316.088 / 322.017 | 324 ± 4 (**not N-converged**) | 316.09 | guard / guard / conv | preserved |

Flowed breakdown at N = 256 (E_knotted component, E_unknot, E12):

| word | values |
|---|---|
| nuc9 | 84.67, 6.92, 71.51 |
| class A | 86.6–86.7, 12.3–12.6, 98.4 |
| class B | 139.0–139.3, 7.2, 72.3–72.5 |
| gen_grouped | 197.3, 12.1, 56.3 |

**Initial energy depends strongly on the embedding parameter and does not rank
consistently.** E_tot at R/a = 2 / 3 / 4.5 / 6, from `initial_sensitivity.json`:

| word | E_tot |
|---|---|
| nuc9 | 578.7 / 547.6 / 606.3 / 706.9 |
| nuc11_interleaved | 796.4 / 685.2 / 697.5 / 774.7 |
| gluon_s0_s1 | 757.7 / 669.8 / 690.9 / … |
| nuc11_gen_grouped | 814.4 / 689.3 / 698.2 / … |

At R/a = 3 the initial energies of the two class-A words differ by 15, and the
initial order of the dressings differs from the flowed order. The initial energy
of the canonical embedding is therefore **not** a usable functional.

The flowed value is close to parameter-free. nuc9 flowed from R/a = 2, 3 and 4.5
gives 234.75, 234.93 and 234.78 at N = 64; the spread is 0.18.

## 3. Pairwise separation (flowed E∞, criterion |gap| > err_A + err_B)

| pair | gap | combined err | verdict |
|---|---|---|---|
| **σ1σ0 vs σ0σ1** (gluon_s1_s0 vs gluon_s0_s1) | 4.77 | 0.58 | **SEPARATED** — σ1σ0 lower |
| gluon_s1_s1 vs gluon_s0_s1 | 4.78 | 0.68 | SEPARATED |
| gluon_s1_s0 vs nuc11_interleaved (= s0_s0) | 4.74 | 0.70 | SEPARATED |
| gluon_s1_s1 vs nuc11_interleaved | 4.76 | 0.79 | SEPARATED |
| gluon_s0_s1 vs nuc11_interleaved (= s0_s0) | 0.03 | 0.52 | **NOT separated** — same link, as predicted |
| gluon_s1_s0 vs gluon_s1_s1 | 0.02 | 0.85 | **NOT separated** — same link, as predicted |
| nuc9 vs every 11-letter word | ≥ 56 | ≤ 4.4 | separated |
| nuc11_gen_grouped vs every other word | ≥ 28 | ≤ 4.6 | separated (provisional, see §4) |

The flowed ordering is:

nuc9 (234.5) < {σ1σ0 ≅ σ1σ1} (291.15) < {σ0σ1 ≅ σ0σ0 = nuc11_interleaved} (295.9) < nuc11_gen_grouped (≈ 316–324)

**This is an ordering only. Nothing is selected.**

The ranking is order-sensitive, as the owner asked: σ1σ0 and σ0σ1 have the same
multiset and the same writhe, and they rank differently. It is order-sensitive
**only through the link type**, though, so it cannot split conjugate words. Among
the four two-crossing dressings it resolves exactly two classes.

The 4.8 gap between the classes comes from a trade. Class B carries the costlier
knotted component, T(2,5) at ≈ 139 against T(2,3) at ≈ 87. But its cross energy
is lower: lk 3 gives ≈ 72.3 and lk 4 gives ≈ 98.4. The net favours σ1σ0.

## 4. Limitations (read before citing any number)

1. **Upper bounds, not infima.** Every value is the energy of an explicit smooth
   curve of the stated link type: certified topology, spectral quadrature.
   Whether a minimiser exists for these links is **open**; FHW Theorem B covers
   prime knots only. Gradient flow from one canonical embedding finds a local
   minimum. A lower configuration elsewhere in the isotopy class is not excluded,
   and no global search was done.
2. **The error bars are partly post-hoc.** The pre-registered error was the
   extrapolation spread plus the quadrature error. The 0.177 landscape floor was
   added after seeing the data: it is the largest disagreement among runs that
   must agree (conjugate pairs at N = 256, R/a starts at N = 64).
   Post-hoc extended N = 256 flows (stop at 1e-8, `runs_posthoc/`) moved values
   by ≤ 0.1:

   | word | extended N = 256 value |
   |---|---|
   | class A | 295.84, 295.94 |
   | class B | 291.32, 291.38 |
   | nuc9 | 234.55 |
   | Hopf | 47.4848 |

   This is consistent with the floor. Several N-sequences are non-monotone
   (gluon_s0_s1, gluon_s1_s1), so the N-extrapolation itself is weak. The
   class-A vs class-B verdict rests on a gap of ≈ 4.8 against run-to-run scatter
   of ≲ 0.2, not on the extrapolation.
3. **nuc11_gen_grouped is under-resolved.** The resolution guard stopped its
   N = 64 and N = 128 flows, and the N = 256 flow ended *above* the N = 128
   curve (322.0 vs 316.1). The discrete functional is not tracking the continuum
   one for the tight T(2,7) component. Its value is a certified upper bound,
   316.09, and nothing finer. Its separation from the rest is provisional,
   although the gap is ≥ 28.
4. **Deviations from the pre-registration (implementation; POST-HOC).** All of
   these were introduced while debugging the Hopf calibration, before the
   candidate production runs. During that debugging, short development flows on
   nuc9 and gluon_s1_s0 (N = 64) were run and their energies were seen. They are
   not reported here.
   - The discrete flow drifted along the Möbius orbit into configurations where
     the discretisation under-counts, and E_poly went below 8 + 4π². To stop it:
     - the descent direction is projected off the 10 infinitesimal Möbius motions;
     - every 100 steps an orientation-preserving Möbius re-representative is
       applied (balanced S³ preimage). It is accepted only if lk, the Alexander
       certificate and the spectral energy (to 1e-3) are all unchanged.
     The energy is exactly Möbius-invariant, so neither change alters what is
     being minimised.
   - The optimiser is L-BFGS in the Sobolev-preconditioned, normal-projected
     metric, rather than plain preconditioned descent.
   - The flow functional gains its trapezoid diagonal (curvature) term. The
     monitor's subtraction kernel uses the regular-N-gon chord.
   - The resolution guard is per pair: distance / max(edge) ≥ 0.5, or no worse
     than 5 % if the canonical start is already below 0.5. Calibration runs used
     1.0, and that threshold never triggered.
   - The convergence test uses a running minimum.
   - The p-free extrapolation is accepted only for p > 0.5.
   - A one-letter mirror fix: the first re-representative was a reflection, which
     flips lk; it is now a rotation.
5. **Not covered:** the sixteen `nuc11_constructed[...]` words; the 1-letter
   dressings σ1^±1, which change the component count to 3; and any role for the
   corpus's q-shift decorations, which no geometric embedding can see.
6. float64 throughout the flow. The trusted digits are about 3–4 significant
   figures for the 11-letter words and 5–6 for the Hopf calibration.

## 5. Next step

1. Before any owner use, test for lower minima: multi-start flows per link type
   (random Möbius images, perturbed starts, other closed-braid representatives
   such as the stabilised or destabilised forms). Also run gen_grouped at N = 512.
2. If the owner wants a selection rule from this, the open decision is whether
   an isotopy-class functional is acceptable. It provably ties conjugate words:
   `gluon_s0_s1` with `nuc11_interleaved`, and `gluon_s1_s0` with `gluon_s1_s1`.
   If those words must be told apart, no embedding energy can do it, and the
   distinction has to come from the non-geometric decorations.

## Files

- `preregistration.md`
- `braid_topology.py` → `braid_topology.json`
- `ohara_lib.py` — embedding, spectral evaluator, guarded flow, certificates
- `calibrate.py` → `calibration_G1_G3.json`
- `run_candidate.py` → `runs/*.json`, `curves/*.npz`
- `initial_sensitivity.py` → `initial_sensitivity.json`
- `posthoc_extend.py` → `runs_posthoc/`
- `analyse.py` → `results.json`
- `logs/`
- `test_flow.py`, `diag*.py` — development only
