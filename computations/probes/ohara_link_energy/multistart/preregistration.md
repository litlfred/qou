# Pre-registration — multi-start firming of the flowed upper bounds

Written 2026-10-10, **before any new energy value was computed** (owner's
instruction of 2026-10-10: "Multi-start first"). Continues route 1
(`../preregistration.md`, `../results.md`). Numerical evidence only. No Q_beta,
CODATA value or mass number enters any computation, table or ordering here.
Anything added after this file is first written is marked **POST-HOC** in
`results.md`.

## 0. What is fixed (unchanged from route 1)

`../ohara_lib.py` is imported **unchanged**: the energy (FHW normalisation,
round circle = 4; E_tot = E1 + E2 + 2·E12), the spectral evaluator (M = 8N and
16N), the flow functional and L-BFGS Sobolev flow with Möbius-mode projection and
balancing, the topology guard (displacement certificate, turning angle, lk
every step, per-pair resolution guard 0.5 / 5 %), and the Alexander certificate
at start, end and on the fine interpolant. The only new code is start
generation (`ms_lib.py`), the per-class certificate wrapper (which accepts the
components in either order, since a different braid representative can list them
in a different order), and the shape invariant used for clustering.

Class labels follow the owner's message (they are the reverse of route 1's
letters):

| class | link | lk | words in the corpus |
|---|---|---|---|
| nuc9 | T(2,3) ∪ U | 3 | `nuc9` |
| **A** | T(2,5) ∪ U | 3 | `gluon_s1_s0` ≅ `gluon_s1_s1` (route-1 "B") |
| **B** | T(2,3) ∪ U | 4 | `gluon_s0_s1` ≅ `gluon_s0_s0` = `nuc11_interleaved` (route-1 "A") |
| **G** | T(2,7) ∪ U | 2 | `nuc11_gen_grouped` |

Route-1 values to test against (E∞ ± err; UB): nuc9 234.50 ± 0.28 (UB 234.55);
A 291.15 ± 0.4 (UB 291.17); B 295.90 ± 0.32 (UB 295.84); G not converged,
certified UB 316.09.

## 1. Braid representatives (exact topology, computed before this file; no energy)

`ms_words.py` → `ms_words.json`. Every representative below has the same
component count, lk, Kauffman-bracket Jones and Burau Alexander polynomial as the
class's canonical word, and is related to it by an explicit move, so the closure
is isotopic by construction (not merely invariant-equal):

* cyclic rotation (conjugation by a prefix);
* Δ-conjugation σ0 ↔ σ1 (Δ σ_i Δ⁻¹ = σ_{2−i} on 3 strands);
* braid-relation rewrite (σ0σ1)³ → (σ0σ1σ0)² (the same braid Δ², a different word);
* **Markov stabilisation to 4 strands** — `w·σ2` (top) and `shift(w)·σ0` (bottom).
  These are **different braids** (different strand number and length), so their
  canonical embeddings are genuinely different starting curves of the same link.
  For nuc9 the bottom stabilisation puts the extra strand on the unknot
  component, the top one on the trefoil component.

## 2. Starts (K = 14 per link class; `make_plan.py` → `ms_plan.json`)

For each class X ∈ {nuc9, A, B, G}:

| start | kind | details |
|---|---|---|
| s01 | canonical word, R/a = 3 | route-1 start (reproduction) |
| s02 | canonical word | R/a = 2, crossing height ×1.5, slice warp seed 101 |
| s03 | canonical word | R/a = 5, crossing height ×0.6, slice warp seed 102 |
| s04 | canonical word | R/a = 3.5, strong slice warp (Σk|c_k| = 0.85) seed 103 |
| s05 | conjugate word | nuc9: rot by 4; A: `gluon_s1_s1`; B: `gluon_s0_s0`; G: rot by 3 |
| s06 | cyclic rotation | by 7 / 5 / 5 / 9 letters; R/a = 2.5, height ×1.2 |
| s07 | Δ-conjugate word | R/a = 3 |
| s08 | braid-relation rewrite (G: rotation by 9) | R/a = 4, warp seed 104 |
| s09 | **different braid rep**: Markov stabilisation (top), 4 strands | R/a = 3 |
| s10 | **different braid rep**: Markov stabilisation (bottom), 4 strands | R/a = 3 |
| s11, s12 | random orientation-preserving Möbius image of the route-1 best flowed curve | seeds 11, 12 |
| s13, s14 | random smooth perturbation of the route-1 best curve | ε = 0.05, 0.15 (max displacement ε·L_c/2π; Fourier modes 1–6, 1/k decay); redrawn (≤ 30 tries, count reported) until topology certificate + lk hold |

Route-1 best curves used as seeds: nuc9 `nuc9_N256_ext`, A `gluon_s1_s0_N256`,
B `gluon_s0_s1_N256_ext`, G `nuc11_gen_grouped_N128`.

"Slice spacing": braid-time angle φ_b is placed at φ_g = φ_b + Σ_{k=1..3} c_k
sin(kφ_b + θ_k), Σk|c_k| < 1 (a circle diffeomorphism), default Σk|c_k| = 0.6.
"Twist amplitude": crossing height z scaled by the given factor.

**Calibration controls in the same batch, same code**: Hopf σ1² (2 strands),
Hopf σ0σ0σ1 (3 strands), Hopf Möbius image of the route-1 flowed Hopf; trefoil
σ1³ (2 strands), trefoil σ0³σ1 (3 strands, stabilised). Pass criteria as route 1
G4: Hopf E12 ≥ 2π² and within 0.1 % of 2π² at N = 256, E_tot within 0.1 % of
8 + 4π²; trefoil reported against ≈ 74.4 **which is quoted from memory and is
not in the qou library (searched 2026-10-10) — unverified, informational**.

## 3. Resolution schedule and stopping rule

* Braid starts: N = 64 (cap 6000, rel. tol 1e-6) → 128 (cap 4000, 1e-6) → 256
  (cap 3000, **1e-8**), continuation by Fourier resample, certificate re-checked
  after each resample. Curve starts (Möbius/perturbed): 128 → 256, same caps/tols.
  The two finest N of route 1 (128, 256) are therefore used by every start.
* Stopping: route-1 rule — relative decrease of E_poly over the last 300 accepted
  steps below tol, or cap, or guard/step-underflow (reported as such).
* **Phase 2 (N = 512)**: continuation from N = 256 (cap 2000, tol 1e-8) for the
  lowest start of every class, and for G for the lowest start of each of its
  (up to 3) lowest clusters. Calibration: Hopf c1 also to 512.
* Reported per start: E_tot(N) at M = 16N for every N, E1, E2, E12, stop reason,
  iterations, guard rejects, certificates, quadrature difference (8N vs 16N).

## 4. What "agree" and "distinct minimum" mean

* Shape invariant (Möbius-quotiented): the flowed curve mapped to S³ by inverse
  stereographic projection, conformally balanced (arclength centre of mass at the
  origin), resampled by S³ arclength (512 points/component), and the 1 %…99 %
  quantiles of pairwise chordal distances in each self block (ordered by
  decreasing self energy) and the cross block. Distance d_shape = max |Δquantile|.
  E1, E2, E12 are individually Möbius-invariant and are used too.
* Two starts are in **the same minimum** iff |ΔE_tot| ≤ 0.4 and |ΔE12| ≤ 0.4
  and d_shape ≤ 0.05 (all at N = 256). Clusters: single linkage. Only starts whose
  N = 256 run ended "converged" are clustered; others are listed as unconverged.
  The number of **distinct local minima found** per class is the cluster count.
* The 0.4 tolerance is ≈ 2× route-1's measured landscape floor (0.177); the
  shape tolerance 0.05 is a guess fixed now and the full d_shape matrix is
  published so a reader can re-cluster.
* **Conjugate-word test**: the min E over starts of each word in a class must
  agree within 0.4, or the difference must be attributed to different clusters
  (different shape invariant). Equal shape with |ΔE| > 0.4 is a method failure.

## 5. Class value and error bar

* **Upper bound** UB = the smallest certified E_tot(N), N ∈ {256, 512}, over all
  starts (smooth curve, topology certified, quadrature agreeing).
* **Estimate** = E_tot at the finest N of the best start; **error** =
  max(|E(512) − E(256)| of that start, the spread (max − min) of E(256) within
  its cluster) + quadrature difference.
* **Lowered beyond error**: a class's previous best is lowered beyond its error
  bar iff new UB < (route-1 E∞ − route-1 err).
* Pair separated iff |gap| > err_1 + err_2 (route-1 criterion).

## 6. G (gen_grouped) convergence

G is run with the same plan plus phase 2 at N = 512. In addition (diagnostic,
not a candidate value): on the flowed G curves, E_poly(N) is compared with the
spectral E at N = 128, 256, 512, 1024 (same curve resampled) to measure whether
the discrete flow functional tracks the continuum one. **G is "converged"** iff
its best start's |E(512) − E(256)| ≤ 0.5 AND the N = 512 run stops "converged"
AND ≥ 2 starts land in the lowest cluster. Otherwise the report says which
condition failed and why.

## 7. Not done / unchanged

No change to energy, normalisation, calibration or guard. Existence of minimisers
for these 2-component links is open (Freedman–He–Wang Thm B is for prime knots);
every value is an upper bound from a local minimum of a guarded flow.
