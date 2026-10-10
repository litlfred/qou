# Pre-registration — link Möbius energy of canonical closed-braid embeddings, flowed

Written 2026-10-10, **before any candidate energy was computed**. Route 1 of the
owner's energy / O'Hara selection question (bean `qou-99qc`, gap bean `qou-pzsi`).
qou checkout: `/home/user/qou-verify-4` at `origin/main` = `aa914b606a`.
Numerical evidence only. No Q_beta, CODATA value or mass number enters any
computation, ordering, table or plot in this directory.

Anything added after this file is first written is marked **POST-HOC** in
`results.md`.

## 0. Exact topology computed before writing this (not an energy)

`braid_topology.py` (pure integer/sympy; output `braid_topology.json`) computes
permutation, components, linking number, per-component self-crossing writhe,
Kauffman-bracket Jones and Burau Alexander polynomials of every closure. It was run
before this file was finalised because the candidate list cannot be stated
sensibly without it. Result (all letters are positive):

| word | components (strands) | lk | component types |
|---|---|---|---|
| nuc9 = (σ0σ1)³σ0σ0σ1 | 2 (1+2) | 3 | unknot + T(2,3) |
| nuc11_interleaved = nuc9·σ0σ0 | 2 (1+2) | 4 | unknot + T(2,3) |
| gluon_s0_s0 = nuc9·σ0σ0 | **identical word** to nuc11_interleaved | | |
| gluon_s0_s1 = nuc9·σ0σ1 | 2 (2+1) | 4 | T(2,3) + unknot |
| gluon_s1_s0 = nuc9·σ1σ0 | 2 (2+1) | 3 | T(2,5) + unknot |
| gluon_s1_s1 = nuc9·σ1σ1 | 2 (1+2) | 3 | unknot + T(2,5) |
| nuc11_gen_grouped = σ0⁷σ1⁴ | 2 (2+1) | 2 | T(2,7) + unknot |

**Exact finding with consequences for this study.** As closed braids,
`gluon_s0_s1 ~ gluon_s0_s0` and `gluon_s1_s0 ~ gluon_s1_s1` are **conjugate**,
hence their closures are **isotopic**:

* with Δ² = (σ0σ1)³ central, nuc9 = Δ²σ0²σ1;
* s0_s1: Δ²σ0²(σ1σ0σ1) = Δ²σ0²(σ0σ1σ0) = Δ²σ0³σ1σ0 ~ (cyclic) Δ²σ0⁴σ1;
  s0_s0: Δ²σ0²σ1σ0² ~ (cyclic) Δ²σ0⁴σ1. Same class.
* s1_s0: Δ²σ0²σ1²σ0 ~ Δ²σ0³σ1²; conjugating by Δ (σ0↔σ1, Δ² fixed) gives
  Δ²σ1³σ0² ~ Δ²σ0²σ1³ = s1_s1. Same class.

Jones and Alexander agree within each pair (and the pairs differ from each other
— e.g. lk 4 vs 3). So among the four two-crossing gluon dressings there are
**exactly two link types**, and **σ1σ0 vs σ0σ1 are distinct links** (lk 3 vs 4,
component T(2,5) vs T(2,3)). The corpus statement "all four 2-crossing candidates
are distinct links" holds for the corpus's *decorated* letters (q-shift
coefficients) — not for the geometric closed braids that an embedding energy sees.
**Any isotopy-class functional, the flowed Möbius infimum included, must give
s0_s1 = s0_s0 and s1_s0 = s1_s1.**

**Pre-registered prediction (a method test):** the flowed estimates for the two
conjugate pairs agree within their error bars even though their *initial*
canonical embeddings differ. If they do not, the flow is not reaching a
parameter-free value and no ranking from it is reported as meaningful.

## 1. Candidate list (verbatim words; generator indices 0-based, all letters positive)

From `computations/qbeta/qbeta_candidate_closures_are_links_probe.py`
(`CANDIDATES`), on n = 3 strands:

1. `nuc9` = [0,1,0,1,0,1,0,0,1]
2. `nuc11_interleaved` = nuc9 + [0,0]
3. `nuc11_gen_grouped` = [0]*7 + [1]*4
4. `gluon_s1_s0` = nuc9 + [1,0]
5. `gluon_s0_s1` = nuc9 + [0,1]
6. `gluon_s1_s1` = nuc9 + [1,1]
7. `gluon_s0_s0` = nuc9 + [0,0] — the same word as 2; run once, reported under both names.

Not included: the sixteen `nuc11_constructed[...]` variants of that probe (not
requested; may be added later as POST-HOC). The corpus's q-shift decorations are
not geometric and are not used.

Calibration words:

* C1 `σ1²` on 2 strands (Hopf link) — the calibration that gates everything.
* C2 `σ0σ0σ1` on 3 strands (Hopf link again, via a stabilised 3-strand embedding)
  — tests that a different canonical embedding of the same link flows to the
  same value.
* C3 `σ1⁴` on 2 strands (T(2,4), lk 2) — informational.
* C4 `σ1³` on 2 strands (trefoil, a knot) — self-energy calibration; literature
  value of the trefoil minimum ≈ 74.4 in this normalisation (Kim–Kusner /
  Kusner–Sullivan numerics; **cited from memory, not held in the corpus**, so
  informational only).

## 2. Energies and normalisation

For a 2-component link L = K1 ∪ K2:

* Self (Möbius / O'Hara j=2 energy, Freedman–He–Wang normalisation):
  E(K) = ∫∫ [ 1/|x−y|² − 1/D(x,y)² ] |dx||dy|, D = shorter arc distance.
  **Round circle = 4.** (Some authors subtract 4, or add it; we do neither.)
* Mutual (Agol–Marques–Neves): E(K1,K2) = ∫∫_{K1×K2} |dx||dy| / |x−y|².
* Total: E_tot = E(K1) + E(K2) + 2·E(K1,K2) — the double integral over L×L with
  no subtraction between components (the cross pairs appear in both orders).
  E1, E2, E12 are reported separately so any other weighting can be recomputed.
* For a knot (C4) only E(K).

Evaluation quadrature ("final energies"): the curve is a smooth periodic
interpolant (FFT trigonometric interpolation of the polygon vertices, or the
analytic embedding sampled densely), sampled at M points per component; the self
integrand is rewritten as

  E(K) = 4 + ∫∫ [ 1/|x(u)−x(v)|² − (π/L)² / sin²(π(S(u)−S(v))/L) ] |x'(u)||x'(v)| du dv

(S = arclength function, L = length), whose integrand is smooth and periodic with
diagonal limit (κ²/12 − (π/L)²/3)|x'|². The constant 4 is exact: the subtracted
kernel is the chord of the round circle of the same length, for which the
bracket vanishes identically. The trapezoid rule on this periodic smooth
integrand converges spectrally; reported digits are those that agree between
M and 2M.

## 3. Canonical closed-braid embedding (a CHOICE; parameters reported)

Braid axis = z-axis. A word of m letters on n strands occupies φ ∈ [0, 2π) in m
equal slots. In the meridian half-plane (r, z), strand position p sits at
r = R + a(p − (n−1)/2), z = 0. In the slot of letter σ_i the strands at
positions i, i+1 rotate about their midpoint by angle π·s(τ), τ ∈ [0,1] the
slot-local time, s the C^∞ smooth step ψ(τ)/(ψ(τ)+ψ(1−τ)), ψ(x)=e^{−1/x}; the
rotation sense is fixed by the letter sign. Point = ((r cos φ, r sin φ, z)).
Each component is the union of the strand passes it consists of.
Default **R/a = 3**; initial-energy parameter sensitivity reported for
R/a ∈ {2, 3, 4.5, 6}. The flowed value is meant to be parameter-free; tested by
flowing C1 and one candidate from R/a = 2 and 4.5 as well (at N = 64).

## 4. Discretisation

Each component resampled to N vertices equally spaced in arclength,
**N ∈ {64, 128, 256} per component**.

Flow functional (vertex-based; exact analytic gradient; float64 throughout the
flow): with h_c = L_c/N,
F = Σ_c h_c² Σ_{i≠j∈c} |x_i−x_j|^{-2} + 2 h_1 h_2 Σ_{i∈1, j∈2} |x_i−y_j|^{-2}.
With equal spacing the subtracted self-kernel is a shape-independent constant, so
F differs from the discrete E_tot by a constant; E_poly (monitor) =
Σ_c [ h_c² Σ_{i≠j} (|x_i−x_j|^{-2} − (π/N)²h_c^{-2}/sin²(π(i−j)/N)) + 4 ] + 2E12.

## 5. Flow

Preconditioned (Sobolev-type) gradient descent: per component, the gradient is
projected to the normal plane at each vertex, Fourier-filtered by
1/(1+(|k|/4)³) (k = mode number), and re-projected; Armijo backtracking on F;
step grows ×1.5 after acceptance. Tangential redistribution toward equal edge
lengths each step (vertex moves along its tangent by 0.5·(ℓ_i − ℓ_{i−1})/2).
Recentre and rescale to fixed total length each step (energy is scale-invariant).

**Topology guard, every step** (step halved until all hold; if the step falls
below 1e-12 the run stops and is reported as stopped by the guard):

1. Displacement certificate: with δ = max vertex displacement of the step
   (normal + tangential), require 2δ < 0.9·d_min, d_min = minimum distance over
   all pairs of non-adjacent segments (same component |i−j| ≥ 2 cyclically, all
   cross-component pairs), and δ < 0.25·(min edge), and max turning angle
   < 150° after the step. Under these, the straight-line homotopy of the polygon
   is an isotopy (no two non-adjacent segments meet; adjacent ones cannot fold).
2. Linking number recomputed exactly (signed crossings of a generic projection
   / 2) — must equal the combinatorial value.
3. Resolution threshold: minimum distance between segments separated by ≥ 4
   indices (or on different components) must stay ≥ 0.5·h_min.

Independent certificate at start and end of every run: Alexander matrix from a
generic projection of the polygon, evaluated exactly at t = −1, 2, 3 (integers),
compared up to units ±t^k with the braid closure's Alexander polynomial, for the
link and for each component separately.

## 6. Convergence criteria

* Stop a run when the relative decrease of E_poly over the last 300 accepted
  steps is < 1e-6, or at the iteration cap (N=64: 6000, N=128: 4000,
  N=256: 3000). A capped run is reported as "capped" — its value is still an
  upper bound for that link type's infimum (on the evaluated smooth curve,
  topology certified), but not a converged one.
* Continuation: N=128 starts from the flowed N=64 curve (Fourier resample), N=256
  from the flowed N=128 curve; topology re-certified after each resample.
* Final value E_fin(N): spectral evaluation of the flowed curve's trigonometric
  interpolant at M = 8N and 16N per component; digits reported are those that
  agree.
* Extrapolation: fit E_fin(N) = E∞ + c·N^{−p} through the three N; error bar =
  max(|E_fin(256) − E∞|, spread of E∞ between p free and p ∈ {1,2} two-point
  fits), plus quadrature error. **E∞ is a flowed estimate / upper-bound trend,
  never "the infimum".** The rigorous-in-spirit statement is the upper bound
  min_N E_fin(N) (a smooth curve of the right link type, certified).
* A pair is **separated** only if |E∞(A) − E∞(B)| > err(A) + err(B).

## 7. Calibration (gate — if it fails, STOP and report)

* G1 corpus integrator `mobius_cross_energy_hopf_calibration.cross_energy(R, c, N)`
  on the round Hopf configuration of its family (R = 1, c = √2: the second
  circle is orthogonal to every sphere through the first, i.e. a Möbius image of
  the (unit circle, z-axis) pair = stereographic Hopf fibres) — relative
  deviation from 2π² < 1e-8.
* G2 my evaluator: round circle self = 4 to < 1e-10; stereographic projection of
  two orthogonal Hopf fibres from a generic pole: E12 = 2π² to < 1e-8, E1 = E2 = 4.
* G3 Möbius invariance: a random inversion applied to the initial σ1² and nuc9
  embeddings changes E1, E2, E12 by < 1e-6 relative.
* G4 flowed C1 (σ1², 2-strand canonical embedding): E12(N) ≥ 2π² for every N and
  decreasing toward it, with E∞(E12) within 1 % of 2π², and E1, E2 → 4 within
  1 %. Same for C2 from its 3-strand embedding.

## 8. What will be reported

`results.md`, `results.json`: calibration table; per-candidate table (word |
components | lk | initial E (E1, E2, E12, E_tot) | flowed E_fin(N) for each N |
E∞ ± err | stop reason | topology preserved?); initial-energy parameter
sensitivity; pairwise-separation verdict for every candidate pair (esp. σ1σ0 vs
σ0σ1); limitations; next step. Ordering by E_tot is reported as an ordering
only; no candidate is selected.
