# Leray DSS profile: a Galerkin search (numerical exploration, not a proof)

Date: 2026-11-21. Branch `claude/leray-dss-galerkin-search-2026-11-21`.
Probe: [`computations/probes/leray_dss_galerkin_search.py`](../../computations/probes/leray_dss_galerkin_search.py)
(mpmath, 60 dps). Seeds: `computations/probes/leray_dss_galerkin_seeds.json`.
Witnesses: `computations/probes/leray-dss-galerkin-search.witness.json` (steady branch and linear
spectrum, all five truncations) and `computations/probes/leray-dss-galerkin-search-22.witness.json`
and `-23.witness.json` (periodic candidates at L2N2 and L2N3).

Context: content block `fluid-dynamics/leray-profile-construction.md` (after #8842) describes a
finite truncation of the Leray system for a discretely self-similar (DSS) profile as a Galerkin
approximation indexed by angular degree and Fourier mode in `s`. It says that the period is not
fixed and that the coefficients are not specified. This note writes the coefficients down for one
concrete Petrov–Galerkin scheme and searches that scheme for nonzero solutions. No content block
was edited. Nothing here may enter a Lean proof.

**Summary.** I found no nonzero solution that survives refinement.
- The truncations do have nonzero **steady** solutions, at every `L ≤ 3` and `N ≤ 5` I tried.
  Each one was re-converged in mpmath to a residual of 1e-53 to 1e-56.
  - They disappear when degree `l = 4` is added: Newton falls to `V = 0` from 80 perturbed
    starts.
  - Their field values do not converge as `N` grows, and the vorticity-form PDE residual stays
    O(1) at every radius.
  - A steady solution in this decay class is excluded by Tsai 1998 in any case.
- **Periodic** solutions (period `S` > 0, steady part plus oscillation) exist in single truncations.
  - At L2N2: `S ≈ 0.830271`. At L2N3: `S ≈ 0.471208`. At L2N4: `S ≈ 1.07`.
  - Each one is converged in the number of Fourier modes `K`.
  - Each one either fails to continue, or continues to a different orbit, when `L` or `N` is
    raised. The period jumps by factors of about 2 and does not converge.
- All of these are reported as Galerkin artefacts.

**Phase 2 (§9).** The negative was re-tested at three further trial scales (`a = 1/2, 2, 4`), at
`L = 4–6` with `N = 3–4` in one parity sector, and in a basis whose periodic modes carry the
log-phase tail `|y|^{−1−2imω}` that a genuine orbit must have. None of these produced a nonzero
solution that persists under refinement. The failures share two mechanisms: steady artefacts
push amplitude into the `|y|⁻¹` tail as `N` grows, and the periodic artefacts depend on a tail
the true problem forbids (they do not continue into the log-phase basis). A Galerkin
(test = trial) scheme has no clean pressure elimination in the periodic sector (§9.2). The
literature (§1) still leaves non-steady DSS with a nonzero `|y|⁻¹` tail open.

**Phase 3 (§10, 60-digit Arb arithmetic).** I rebuilt the search on a trial basis whose mode `m` carries
the tail `(1+ρ)^{−iθmω}` inside the radial factor.

- **Basis.** The fields are exactly divergence-free for every `θ`. The phase-2 log-phase basis was not,
  for poloidal fields (§10.1). The test fields still eliminate the pressure exactly (§10.2).
- **Quadrature.** The radial quadrature (`r = sinh u`, phase-adapted Gauss–Legendre panels) is stable
  to 1e-41 or better under refinement.
- **Orbits B and C.** Continued from `θ = 0`, both pass through folds in `θ`. The runs were stopped at
  the 2 h budget, at `θ ≈ 0.050` (B, after two folds) and `θ ≈ 0.020` (C).
- **Random starts.** 22 starts directly at the admissible tail (`θ = 1`, zonal, L2N2, L2N3, L3N2) found
  no orbit.
- **Refinement.** No candidate existed to refine, so nothing persisted across refinements.
- **Scope.** All of this is scope (a).

**Phase 4 (§11).** Owner-approved continuation of B and C toward `θ = 1`, using pseudo-arclength
continuation with an adaptive step, Arb at 60 dps, and witnesses checkpointed by the probe after
every accepted point.
- **B** (50 points) passes `θ ≈ 0.060`. It then turns and oscillates in the window
  `0.048 ≤ θ ≤ 0.060`, either turning twice at nearby points or retracing its own path; the run
  does not decide which.
- **C** (16 points) folds at `θ ≈ 0.032`, possibly jumps branch near `θ ≈ 0.004`, and rises to
  `θ ≈ 0.059`.
- Both stopped on the 3 h budget. Neither reached `θ = 1`, returned to `θ = 0`, escaped, or
  collapsed to a steady solution, so nothing was refined.
- **Scope.** All of this is scope (a).

## 1. Literature: which classes are already excluded

The library holds no source on self-similar Navier–Stokes. `grep -ai` over `library/INDEX.md`,
`library/*/sections/` and `library/*/ocr/` for `self-similar | Tsai | Nečas | Chae | Wolf | Leray`
returns only unrelated documents (Painlevé, Q-balls, an Oberwolfach knot report).
`folio/references/` holds `necas-ruzicka-sverak1996` and `tsai1998`.

**Phase 2 (same day): the web was reachable, so the two Chae papers and two Bradshaw–Tsai papers
were read at abstract or theorem level.** What was read, and from where:

- Chae–Wolf, arXiv:1610.09464 v2, HTML version, theorem statements read.
- Chae, arXiv:1306.0305, abstract only.
- Bradshaw–Tsai, arXiv:1703.03480 (APDE 2019), introduction read.
- Pineau–Vicol, arXiv:2607.09619, abstract only.
- The Bradshaw–Tsai survey, arXiv:1802.0038, was **not** read: the fetch was rate-limited twice.

| result | what it says about backward DSS | read here |
|---|---|---|
| Nečas–Růžička–Šverák 1996 | no nontrivial steady (self-similar) profile in `L³` | bib entry only |
| Tsai 1998 | steady profiles trivial if in `L^q`, `3 < q ≤ ∞`, or under local energy | bib entry only, scope as quoted by Chae–Wolf |
| Chae, arXiv:1306.0305 | no locally *asymptotically* DSS blow-up when the time-periodic profile lies in `C¹(ℝ; L³ ∩ C²)` | abstract |
| Chae–Wolf, arXiv:1610.09464, Thm 1.1 | a smooth `λ`-DSS solution with `u ∈ C((−∞,0); L^p)`, `3 ≤ p < ∞`, any `λ > 1`, is regular off `(0,0)` and obeys `|u| ≤ C/(√−t + |x|)`. This is regularity, not exclusion | theorem read |
| Chae–Wolf, Thm 1.3 | for each `C* > 0` there is `λ*(C*) > 1` such that a `λ`-DSS solution with `|u| ≤ C*/(√−t+|x|)` and `λ ∈ (1, λ*)` vanishes. No `L^p` hypothesis | theorem read |
| Chae–Wolf, introduction (2017) | "such nonexistence result for the nontrivial discretely self-similar solutions is still not available in the literature" (Navier–Stokes) | read |
| Bradshaw–Tsai, arXiv:1703.03480 | works with forward solutions only, and states "the existence of non-trivial backward DSS solutions remains open" | read |
| Pineau–Vicol, arXiv:2607.09619 (2026) | rotated self-similar / rotated DSS solutions are trivial under a Type I bound, for extreme rotation and for `λ` near 1 | abstract only. Exact spaces not checked |

What this settles about the search class `|V| ~ |y|⁻¹` with nonzero oscillation:

- **Chae (L³) does not apply.** A `|y|⁻¹` tail is not in `L³`.
- **Chae–Wolf Thm 1.1 applies but excludes nothing.**
  - A smooth time-periodic profile with `|V| ≲ (1+|y|)⁻¹` gives `u(t) ∈ L^p` for every `p > 3`, so
    the hypotheses hold.
  - The conclusion is the bound `|V(y,s)| ≤ C/(1+|y|)`. That is exactly the decay class searched
    here, so it is a consistency check, not an exclusion.
- **Chae–Wolf Thm 1.3 excludes `λ ∈ (1, λ*(C*))`.**
  - `λ*` depends on the bound constant `C*` and is not explicit.
  - So the result removes a `C*`-dependent neighbourhood of `λ = 1`, and nothing more.
- **Pineau–Vicol (2026) does not change this, as far as its abstract shows.**
  - It treats the rotated generalisation with `λ` near 1.
  - I did not read its body. I have not checked whether its Type I hypothesis is weaker than the
    `C*/(√−t+|x|)` bound.
- **Net (verified to the level stated above):** no result I read excludes a **non-steady backward DSS
  profile with a nonzero `|y|⁻¹` tail and `λ ≥ λ*(C*)`**. Two sources state the question is open:
  Chae–Wolf in 2017 and Bradshaw–Tsai in 2017/19.
- **Not checked:** whether a post-2019 paper closes it. I made one web search with no hit; that is not
  a literature review. The Bradshaw–Tsai survey (arXiv:1802.0038) is the next thing to read.

Consequences for the search:

1. Every bounded `L²` profile is in `L³`, so a profile with `L²` decay is already excluded for every
   `λ ≠ 1`. Following the retargeting instruction, the search class is **scale-critical decay**
   `|V| ~ |y|⁻¹`, which is weak-`L³` and not `L³`.
2. A smooth **steady** profile with `|V| ≲ (1+|y|)⁻¹` is in `L^q` for every `q > 3`, so Tsai 1998
   excludes it. Any steady solution of a truncation in this class is therefore not an
   approximation of a genuine profile. It is either an artefact or a sign that the scheme is not
   converging.
3. The class not excluded is **non-steady DSS with a nonzero `|y|⁻¹` tail and `λ ≥ λ*(C*)`**.
   See the table above for how far this was verified.
4. The relation between the period and the scale factor is `S = 2 log λ`, so `λ = e^{S/2}`. No
   identification of `S` with any `q`-dependent quantity is made.

## 2. The truncated system

Equation (backward similarity variables `y = x/√(T−t)`, `s = −log(T−t)`):

    ∂_s V − ΔV + ½V + ½(y·∇)V + (V·∇)V + ∇P = 0,   div V = 0.

**Angular part.** The basis is built from real solid harmonics `H` of degree `l = 1..L`, taken
from an exact rational basis of the kernel of Δ on homogeneous degree-`l` polynomials
(`harmonic_basis_rational`).

- Toroidal field: `T[H,R] = R(ρ)(∇H × y)`.
- Poloidal field: `P[H,R] = ∇×∇×(yHR) = S∇H − 2l R'(ρ) H y`.
- Here `ρ = |y|²` and `S = (l+1)R + 2ρR'`.
- Both fields are exactly divergence-free. This was checked symbolically, and the gradients were
  checked by finite differences.

**Trial radial functions.** `R = (1+ρ)^{−p}`, with `p = (l+1)/2 + n` (toroidal) and
`p = l/2 + n` (poloidal), for `n = 0..N−1`.
- The `n = 0` member decays like `|y|⁻¹`, so the trial space is weak-`L³` and is not contained in
  `L³`.
- Members with higher `n` decay faster.

**Test radial functions.** `R = ρ^n e^{−ρ/4}`, for `n = 0..N−1`.
- Every test field is Gaussian and divergence-free, so `∫ψ·∇P = 0` and the pressure drops out.
- `−Δ` is integrated by parts.

The number of unknowns per Fourier mode is `n = 2N(L² + 2L)`. For example, `L = 2, N = 2` gives
`n = 32`.

**Time.** `V = Σ_{|m|≤K} A_m e^{2πims/S}`, with `A_{−m} = Ā_m`, `ω = 2π/S` unknown, and the phase
condition `Im A_1[0] = 0`. The equations:

    (L + iωm M) A_m + Σ_{m1} B(A_{m1}, A_{m−m1}) = 0,   m = 0..K,

where:
- `M_ab = ⟨ψ_a, φ_b⟩`;
- `L_ab = ⟨∇ψ_a : ∇φ_b⟩ + ½⟨ψ_a, φ_b⟩ + ½⟨ψ_a, (y·∇)φ_b⟩`;
- `B_abc = ⟨ψ_a, (φ_b·∇)φ_c⟩`.

The real unknown and equation counts are both `n(2K+1) + 1`. The steady case is `K = 0`.

**Integrals.**
- Angle: exact Gauss–Legendre × uniform rule of sufficient degree.
- Radius: composite Gauss–Legendre on `[0, 28]` with 9 panels and 40 nodes per panel.
- Quadrature error, from raising the radial nodes 40 → 60 per panel:

  | truncation | change in `L` | change in `B` |
  |---|---|---|
  | L1N2 | 1.2e-54 | 1.0e-54 |
  | L2N2 | 1.9e-53 | 1.6e-52 |

  The mpmath systems are therefore resolved to about 52 digits.
- The mpmath and float64 assemblies agree to the float64 floor: about 4e-12 in `M` and `L`, and
  8e-13 in `B` against `|B|max` of about 230.

## 3. The linear spectrum

The pencil `L v = μ M v` has, at every truncation (all five in mpmath):

    spectrum = {1, 3/2, 2, 5/2, …},   min Re μ = 1,   |Im μ| ≤ 1.6e-55 (mpmath, 60 dps).

Reason: the test space consists of polynomials times `e^{−ρ/4}`, and it is invariant under the
formal adjoint `L* = −Δ − ½y·∇ − 1`. That operator is the Ornstein–Uhlenbeck operator in the
weight `e^{|y|²/4}`. Its eigenvalues on degree-`k` fields are `½ + k/2`, and here `k ≥ 1`. So the
truncated linear operator `iωm M + L` is invertible for every real `ω` and every `m`.

- **`V = 0` is linearly isolated for every period `S`, with spectral gap at least 1.**
- No nonzero branch bifurcates from zero.
- Any nonzero solution must have finite amplitude.

The same holds without truncation, by my own hand argument (not formalized, not checked):
1. In a decaying class, taking the divergence gives a harmonic, decaying pressure, so `P = 0`.
2. Each Cartesian component then satisfies `−ΔV + (½ + iωm)V + ½y·∇V = 0`.
3. Angular degree `l` reduces this to Kummer's equation with `a = (l+1)/2 + iωm` and
   `b = l + 3/2`.
4. A solution that is regular at 0 and decays requires `1/Γ(a) = 0`, that is `a ∈ −ℕ`, which is
   impossible since `Re a > 0`.

## 4. Search ranges and counts (float64 exploration; scratch, not committed)

The truncations used were `(L, N) ∈ {(1,1), (1,2), (2,2), (2,3), (2,4), (2,5), (3,2), (3,3), (3,4), (4,2)}`,
with `K ∈ {2, 3, 4}` for the searches and up to `K = 12` for refinement.

Starting periods `S₀ ∈ {0.5, 1.0, 1.386 (λ=2), 2, 3, 4, 6, 8, 12}`, taken in rotation and
**not selected**. `S` is a free unknown in Newton.

Starting amplitudes were log-uniform over 3.5 decades around `‖L‖/‖B‖`. The solver was damped
Gauss–Newton (least squares, because the rotational zero modes make the Jacobian rank-deficient),
with Levenberg–Marquardt as a fallback.

Random-start counts:

| search | truncations | starts each | nonzero converged |
|---|---|---|---|
| steady | L1N2, L2N2..N5, L3N2..N4, L4N2 | 400 (600 at L2N2 in the rational basis) | L2N2: 3 distinct orbits (13 hits); L2N3: 1 orbit; all others: 0 |
| periodic, K=2 | L1N2, L2N2, L2N3, L3N2 | 54 + 270 | 0 (32–50 % converge to `V=0`, the rest fail) |
| periodic, K=3 | L2N2, L2N3, L3N2 | 54 | 0 |
| periodic, K=4 | L2N2, L2N3, L3N2 | 180 | 0 |
| time integration of `M ȧ = −La − B(a,a)` to `s = 40` | L2N2, L2N3, L3N2 | 40 | 68 decay to 0, 52 blow up, 0 other attractors |

On the time integration: the Petrov–Galerkin ODE has no energy identity, so blow-up of the
truncated ODE is possible and tells us nothing about Navier–Stokes.

Newton's failure rate is high, so the random-start results establish only that **no periodic orbit
has a large basin**. They do not establish that no periodic orbit exists.

**Seeded periodic search.** I ran a second search seeded from the complex eigenmodes of the
linearisation at each nonzero steady solution. These steady solutions are all strongly unstable:
the leading eigenvalues of `−M⁻¹J` have real part between 2.5 and 21.6, and many are complex. The
seeded search was 50–100 tries per steady orbit. It found the periodic candidates in §6. It also
returned degenerate "orbits" with `ω → 0`, which are motion along the rotational zero modes; those
were discarded.

## 5. Steady candidates (reported, mpmath re-converged)

All rows were re-converged by Newton at 60 dps. The residual is the 2-norm of the truncated system.
The mpmath system is resolved to about 1e-52.

| orbit | truncation | ‖F‖ (mpmath) | coefficient norm ‖a‖ | float64 continuation |
|---|---|---|---|---|
| class 0 | L2N2 | 7.5e-57 | 68.519 | → L2N3, L2N4, L2N5 converge; → L3N2, L3N3, L3N4 converge with the `l = 3` components identically 0; **→ L4N2 collapses to V = 0** |
| class 0 | L2N3 | 9.1e-56 | 97.513 | |
| class 0 | L2N4 | 2.3e-54 | 762.245 | |
| class 0 | L2N5 | 2.6e-53 | 3083.31 | float64 needed LM (borderline), mpmath clean |
| class 1 | L2N2 | 5.1e-56 | 616.609 | → L2N3 fails; → L3N2 collapses to 0 |
| class 2 | L2N2 | 1.3e-56 | 71.379 | → L2N3, L2N4 converge; → L2N5 fails; → L4N2 collapses to 0 |
| class 2 | L2N3 | 4.7e-56 | 94.573 | |
| class 2 | L2N4 | 2.8e-54 | 739.267 | |

Coefficient norms are not comparable across `N`, because the trial basis is not orthonormal. At
L2N5, the condition number of `M` is about 1e9. The resolution-independent diagnostics below are
float64.

`max|V|` on the sphere of radius `r`, and the tail amplitude `r·max|V|` at `r = 1000`, for class 0:

| N | r=0.5 | r=1 | r=2 | r=4 | r=8 | tail |
|---|---|---|---|---|---|---|
| 2 | 46.8 | 14.9 | 19.4 | 19.2 | 11.3 | 95.5 |
| 3 | 37.3 | 18.5 | 15.8 | 18.6 | 11.4 | 97.6 |
| 4 | 44.4 | 7.36 | 9.15 | 16.1 | 12.2 | 112.0 |
| 5 | 39.5 | 11.95 | 5.14 | 15.1 | 13.3 | 127.7 |

The values do not converge, and the tail grows monotonically.

**Pointwise PDE residual.** I computed the relative residual of the vorticity form
`|curl E| / (|curl (V·∇)V| + |curl ΔV|)`, where `E` is the left-hand side, on 40 directions at
`r = 0.5, 1, 2, 4, 8, 16`. It lies between 0.18 and 0.98 at every `N`, with no downward trend. For
example, at L2N5: 0.94, 0.89, 0.46, 0.39, 0.96, 0.98. The candidates satisfy the Gaussian-weighted
equations and do not satisfy the PDE at any radius.

**Verdict.** These are Galerkin artefacts of a low-resolution truncation, on three independent
grounds:
1. The branch is destroyed by adding `l = 4`. I ran 80 perturbed Levenberg–Marquardt starts from
   both L3N2 orbits at L4N2: 56 converged, all to 0.
2. The field values do not converge in `N`.
3. A steady profile in this decay class is excluded by theorem (§1, item 2).

The reason the `l = 3` components stay 0 is parity: a product of two fields of parity
`(−1)^{l−1}` from `l ≤ 2` has no projection on the `l = 3` test fields for these solutions. The
`l = 4` components are forced.

## 6. Periodic candidates

### Candidate B: L2N2

Seeded from steady class 2. Converged at `K = 3, 4, 6, 8, 12` (float64), with
`S = 0.844655, 0.831339, 0.830273, 0.830271, 0.830271`.
- `λ = e^{S/2} ≈ 1.5148`.
- Mode norms at `K = 8`: `|A_0| = 57.8`, `|A_1| = 42.0`, `|A_2| = 5.4`, `|A_3| = 1.4`, decaying.
- mpmath re-convergence at `K = 6`: converged in 3 Newton steps at 60 dps, residual `1.6e-56`, `S = 0.83027283102169473072` (witness `leray-dss-galerkin-search-22.witness.json`). So the truncated L2N2 K=6 system really has this orbit; what fails is its persistence.

Refinement:
- To L2N3 (K = 6): Newton fails; the residual stalls at 88.
- To L3N2 (K = 6): converges, but onto a **steady** solution (all `A_{m≥1}` = 0).

**The orbit does not survive refinement.**

### Candidate C: L2N3

Seeded from steady class 0. Converged at `K = 3, 4, 6, 8`, with `S = 0.471206, 0.471208,
0.471208, 0.471208`.
- `λ ≈ 1.2659`.
- `|A| = 115.87`, `|A_{m≥1}| = 38.63`.
- mpmath re-convergence at `K = 6`: converged in 4 Newton steps at 60 dps, residual `2.9e-55`, `S = 0.47120797401822507277` (witness `leray-dss-galerkin-search-23.witness.json`). The orbit is real for the truncated L2N3 K=6 system; what fails is its persistence.

Refinement:
- To L2N4 (K = 6): converges to a **different** orbit with `S = 1.072030` and `|A| = 665.3`.
  At `K = 9` it re-converges with `S = 1.072063`, `|A| = 665.49`, `|A_{m≥1}| = 162.51`, residual
  3.9e-9 (float64 only; a 30-dps mpmath attempt is in §9.4 and did not finish, because the L2N4 periodic system costs
  too much there). D is therefore reported as float64 continuation data, not as a verified candidate.
- That orbit continued to L2N5: Newton fails; the residual stalls at 18.6 with `S ≈ 0.881`.
- That orbit continued to L3N4: Newton stalls at a residual of 6.8e-2 with `S ≈ 1.039`, which is
  not converged.
- C continued to L3N3: converges (residual 6.8e-10), but onto a **steady** solution
  (`|A_{m≥1}| = 0`, `|A| = 97.50`).

The sequence of periods 0.830 (N=2), 0.471 (N=3), 1.072 (N=4) does not converge. Each orbit
oscillates about one of the steady artefacts of §5, and those do not converge either.

**Verdict: Galerkin artefacts.** They are resolved in time, not resolved in space, and they do not
persist under refinement in `L` or `N`.

## 7. What this does and does not show

Shown, for this Petrov–Galerkin scheme with trial radial `(1+ρ)^{−p}` (scale 1), Gaussian test
functions `e^{−ρ/4}`, `L ≤ 4`, `N ≤ 5`, `K ≤ 12`, and periods reached from starts in
`S₀ ∈ [0.5, 12]` (`λ₀ ∈ [1.28, 403]`):

- `V = 0` is isolated for every period, with linear gap ≥ 1 (mpmath).
- Every nonzero steady or periodic solution found is a truncation artefact. Each one disappears,
  or turns into something different, under refinement.
- **No nonzero solution was found that persists as `L` and `N` grow.**

This is scope (a): a statement about these truncations. It is **not** "no DSS profile exists".

Not shown, and not tried (updated after phase 2, §9):
- `N ≥ 6` (`M` becomes ill-conditioned at about 1e9 by N5). `L = 5–6` was searched only in the
  parity-odd sector and only at `N = 3`.
- Other test weights than the Gaussian (a test = trial scheme is analysed in §9.2, not run).
- Continuation in an auxiliary parameter, such as a viscosity homotopy from a Hopf point.
- The survey arXiv:1802.0038 (§1) was not read.

The random-start searches converge in roughly 40–60 % of starts. A periodic orbit with a small
basin could have been missed.

## 8. Reproduction and precision

- The committed probe is mpmath end to end. It contains no `float()` and no numpy. It rebuilds each
  system from exact rational harmonics, checks the radial quadrature by doubling, computes the
  linear spectrum, and re-converges every reported candidate by Newton.
- Run: `python3 computations/probes/leray_dss_galerkin_search.py`, about 40 min for all steady
  cases. `LERAY_CASES="2,2"` restricts it to one truncation and writes a suffixed witness.
- The float64 exploration (search, continuation and diagnostics) was run in a scratch directory and
  is **not committed**, per the NO-FLOAT64 rule. Its numbers above are labelled float64. The seed
  file carries only the starting points it produced, as decimal strings.
- I ran `scripts/precision-gates.sh --changed` with `tools/qou-substrate` installed.
  - **Red gates:** q0-anchor flip, q0-anchor refill, reference-literal, witness-value copy and q0
    drift. These concern `q₀` witnesses that this change does not touch. The probe contains no
    `q`.
  - **Moved tree-measuring witnesses:** seven of them. I reverted them and did not commit them, as
    the script instructs.

## 9. Phase 2: robustness of the negative (float64 exploration unless marked)

All runs in this section are float64 in a scratch directory and are not committed, except the
orbit-D re-convergence (§9.4). Every negative here is scope (a): a statement about these
truncations and these starts.

### 9.1 Trial radial scale, `R = (1+ρ/a²)^{−p}`, `a ∈ {1/2, 2, 4}` (`c₂ = a² ∈ {0.25, 4, 16}`)

- Linear spectrum: lowest real part `1.000000` at all three scales, same ladder `{1, 3/2, 2, …}`.
  `V = 0` stays isolated.
- Random periodic starts (27 per system, K=2, `S₀ ∈ [0.5, 12]`), 12 systems
  (3 scales × L2N2, L2N3, L3N2, L3N3): **0** nontrivial periodic orbits.
- Random steady starts (200 per system): nonzero steady solutions at most scales
  (c₂=0.25: 2/2/0/0; c₂=4: 2/3/0/1; c₂=16: 1/3/1/1 distinct, in the order above). Their
  profiles change strongly between truncations, as at scale 1.
- Seeded periodic search from the complex eigenmodes of those steady solutions (K=2) found
  orbits in three systems:
  - c₂=0.25 L2N2: `S ≈ 0.9004` and `S ≈ 6.904`;
  - c₂=16 L2N3: `S ≈ 14.02`, with Fourier-mode norm ~1e4 (near-degenerate);
  - c₂=4 L3N3: `S ≈ 0.449, 0.779, 1.275, 0.802`;
  - c₂=16 L3N2: three hits with `S ≈ 12.7–15.8` and mode norms 1.6e5–5.4e8, i.e. the
    degenerate `ω → 0` class, discarded.
- Refinement of each (K 2→4, then `N+1`, then `L+1` at the same scale):

| orbit | K 2→4 | N+1 | L+1 |
|---|---|---|---|
| c₂=0.25 L2N2, S 0.900 | persists, S 0.900428 | converges with `A₁ = A₃ = 0`: a different, period-halved orbit (S 2.059 ⇒ effective 1.03) | Newton fails (res 1.3e4) |
| c₂=0.25 L2N2, S 6.90 | jumps to S 15.88 | Newton fails (res 2.7e4) | `ω → 0`, degenerate |
| c₂=16 L2N3, S 14.0 | `ω → 0`, degenerate | — | degenerate |
| c₂=4 L3N3, S 0.449 | Newton fails (res 4e-3, not converged) | not run | not run |
| c₂=4 L3N3, S 0.779 / 1.275 / 0.802 | converge with `A₁ = A₃ = 0` (period halved: a different orbit) | not run (CPU) | not run (CPU) |

  None survives the full K→N→L chain. **The scale-1 negative is reproduced at all three scales.**
  The L3N3 rows were not taken to N+1 or L+1 (the c₂=4 L3N4/L4N3 systems were not built in
  the time available); they are reported only as K-unstable or period-halving.

### 9.2 Test = trial (Galerkin) variant: no clean pressure elimination

I analysed this rather than ran it.
- **Steady sector.** Testing against the divergence-free trial fields kills the pressure, and
  every term converges for the `|y|⁻¹`-tailed n=0 members (the worst integrand is
  `|∇φ|² ~ r⁻⁴`, integrable at infinity). A clean Galerkin scheme exists here, but the steady
  problem is already excluded by Tsai 1998, so it adds nothing.
- **Periodic sector, plain basis.** The time-derivative term `iωm⟨φ_a, φ_b⟩` diverges for two
  n=0 tails (`∫ r⁻² r² dr`). The scheme is not defined.
- **Periodic sector, log-phase basis** (below, §9.5): the mass term converges, but the test
  function `f_m φ_a` with `f_m = (c₂+ρ)^{−imω}` is no longer divergence-free:
  `div(f_m φ) = −imω f_m · 2(y·φ)/(c₂+ρ) ≠ 0` for poloidal `φ`. The pressure therefore does
  **not** drop out, and would have to be solved for.

So a Galerkin (test = trial) variant with pressure eliminated by the basis exists only where it
is not needed. In the periodic sector it either diverges or needs the pressure. Not run.

### 9.3 Larger angular truncation `L = 4–6`, `N ≥ 3`, in the parity-odd subspace

The full L5/L6 systems are too large here, so I used the invariant subspace
`V(−y) = −V(y)` (toroidal odd `l`, poloidal even `l`). The steady artefacts at L2N3 and L3N3
lie entirely in it. The reduced L3N3 system matches the corresponding subset of the full
rational system to 1.5e-15 (B tensor), and every reduced system has linear gap `1.000000`.

| system | n | steady (200 starts) | periodic (27 starts, K=3) |
|---|---|---|---|
| L4N3 | 72 | 0 nonzero (81 → 0, 119 fail) | 0 (3 → 0, 24 fail) |
| L4N4 | 96 | 0 nonzero (63 → 0, 137 fail) | 0 (2 → 0, 25 fail) |
| L5N3 | 105 | 0 nonzero (80 → 0, 120 fail) | 0 (9 → 0, 18 fail) |
| L6N3 | 144 | 0 nonzero (61 → 0, 139 fail) | 0 (4 → 0, 23 fail) |

The L3N3 steady artefact, continued into the L4N3, L4N4 and L6N3 subspaces, collapses to
`V = 0` every time. This extends the phase-1 observation (it vanished at `l = 4`) to `l ≤ 6`.
Only this one parity sector was searched at `L ≥ 4`; the even sector was not.

### 9.4 Orbit D re-converged in mpmath

Attempted at 30 dps, but not completed. The probe was run with `LERAY_DPS=30 LERAY_CASES="2,4"`, using the L2N4 K=6 seed from
`leray_dss_galerkin_seeds.json`.
- Both steady L2N4 seeds re-converged, to residuals `7.0e-20` and `6.8e-21`.
- Periodic Newton on D (`n = 64`, 833 real unknowns):
  - it=0: `|F| = 1.529e-7`, `S = 1.07202994758407`.
  - it=1: `|F| = 9.185e-9`, `S = 1.07202994752457`.
- One iteration took about 43 min, because the normal-equation solve runs in pure mpmath.
- The residual fell only by a factor of about 17, which is linear, not quadratic, convergence.
  The likely cause is the Tikhonov shift (`10^{-dps/2}`) in the rank-deficient least-squares
  step. Reaching the 1e-20 stopping tolerance at that rate would take an estimated 6+ hours.
- I stopped the run, so **no -24 witness is committed**.
- Reading: the period moved by `6e-11` while the residual dropped. That is consistent with D
  being a genuine orbit of the truncated L2N4 K=6 system, as B and C were.
- **D is not certified.** It also already fails to persist to L2N5 and L3N4 (§6), so certifying
  it would not change the verdict.

### 9.5 Mechanism shared by the failures

Two mechanisms, one for each sector.

1. **Steady artefacts: amplitude moves into the `|y|⁻¹` tail as `N` grows.** For the steady
   class-0 artefact, the far-field amplitude `r|V|` on the sphere `r = 256`
   (rotation-invariant rms) is `45.6, 48.2, 55.3, 63.3` at `N = 2, 3, 4, 5`, while the core values
   change by factors of 2–3 between truncations. The coefficient norm grows much faster
   (68 → 3083), but that growth is mostly basis ill-conditioning (`cond M` reaches ~1e9 at N5), so
   the field norms are the meaningful measure. Classes 0 and 2 have identical rotation-invariant
   profiles at `N ≥ 3`; they are rotations of one another, not two solutions.
2. **Periodic artefacts: the basis cannot carry the correct oscillating tail.** Away from the core,
   `∂_s + ½ + ½y·∇` annihilates `|y|⁻¹ ω(ŷ, log|y| − s/2)`, so a Fourier mode `m` of a genuine
   profile must decay like `|y|^{−1−2imω}` (log-phase oscillation). The phase-1 trial fields give
   every mode `m ≥ 1` a non-oscillating `|y|⁻¹` tail, leaving an `O(|y|⁻¹)` mismatch at infinity
   that no finite `N` removes. I built a log-phase basis (mode `m` multiplied by
   `(c₂+ρ)^{−imω}`; Jacobian checked against finite differences to 2.3e-10) and continued B and C
   into it by a homotopy `θ: 0 → 1`.
   - C (L2N3): at `θ = 0.05` it falls onto a **steady** solution (all `A_{m≥1} = 0`) and stays there.
   - B (L2N2): Newton fails already at `θ = 0.05` (residual 1.2e3).
   - A direct log-phase search at L2N2 seeded from complex eigenmodes converged only to steady
     solutions.

   So the phase-1 periodic orbits do not continue into the basis that has the right asymptotics.
   This is consistent with their being products of the wrong tail rather than approximations
   of a true orbit. Caveat: the radial quadrature used here (24 nodes) is accurate to ≤1.5e-12
   for `m ≤ 4` but only 1.7e-7 at `m = 5` and 1.3e-4 at `m = 6`. The K=6 log-phase runs are
   therefore only roughly resolved, and none of the log-phase results is in mpmath.

### 9.6 Phase-2 verdict

Across trial scales `a ∈ {1/2, 1, 2, 4}`, angular truncations up to `L = 6` (one parity sector
for `L ≥ 4`), and a basis with the correct log-phase tail, I found **no nonzero DSS
solution that persists under refinement**. The failures share the two mechanisms above. This is
still scope (a); the literature check in §1 leaves non-steady DSS with a nonzero `|y|⁻¹` tail
open.

### 9.7 Precision gates (phase 2)

`scripts/precision-gates.sh --changed` on this branch shows the same five red gates as in
§8: q0-anchor flip, q0-anchor refill, reference-literal, witness-value copy and q0-value drift.
The full script on `origin/main` at `b17e0551c53` shows the **same five red gates**. They come
from main, not from this branch, which touches no `q₀` witness. The seven tree-measuring
witnesses the script rewrote were reverted and are not committed.

## 10. Phase 3: a search built on the log-phase tail (arbitrary precision)

Probe: [`computations/probes/leray_dss_logphase_search.py`](../../computations/probes/leray_dss_logphase_search.py).
Witnesses: `computations/probes/leray-dss-logphase-{validate,homotopyB,homotopyC,random-L2,random-L3N2}.witness.json`,
and `-homotopyB-arc` / `-homotopyC-arc` for the arclength runs (see §10.5 for how each was written).

**Arithmetic.** Every number in this section is computed in Arb/Acb ball arithmetic (python-flint 0.9.0) at
60 decimal digits, with midpoints carried through Newton. It does not use mpmath, for a measured reason:
the container has no `gmpy2`, and pure-Python mpmath at 30 dps cost 43 min per Newton step on orbit D
(§9.4). The same Newton step costs about 15 s in Arb at 60 dps. Arb is at least as precise as mpmath, and
no float64 enters any committed number.

### 10.1 Basis: the tail is in the trial radial function, and the fields stay exactly divergence-free

For Fourier mode `m` of a periodic profile with frequency `ω = 2π/S`, the trial radial factor is

`R_m(ρ) = (1+ρ)^{−q}`, with `q = p + iθmω`.

Here `p = (l+1)/2 + n` for toroidal fields and `p = l/2 + n` for poloidal fields. The fields are built
from `R` by the same constructions as in phase 1:

- toroidal: `R·(∇H × y)`;
- poloidal: `S·∇H − 2l·R'·H·y`, with `S = (l+1)R + 2ρR'`.

Both are divergence-free for **any** complex radial function `R`, so every trial field is exactly
solenoidal for every `θ`. At `θ = 1`, mode `m` decays like `|y|^{−1−2imω}`, which is the tail that the
transport `½ + ½y·∇` forces (§9.5). At `θ = 0` the system is the phase-1 system.

**Correction to phase 2.** The phase-2 log-phase basis (§9.5, item 2) multiplied the whole field by
`f_m = (c₂+ρ)^{−imω}`. For poloidal fields that product is **not** divergence-free; §9.2 recorded the same
defect on the test side. So the phase-2 log-phase homotopy results were obtained outside the solenoidal
class:
- B fails at `θ = 0.05`;
- C falls onto a steady solution at `θ = 0.05`.

Phase 3 replaces them (§10.4). The phase-2 qualitative conclusion, that neither orbit continues to the
admissible tail, is not overturned, but its evidence is now the phase-3 runs.

### 10.2 Pressure

The test fields are the phase-1 Gaussian divergence-free fields `ρⁿe^{−ρ/4}` times the same angular
constructions. They do not carry the log-phase factor. Hence `⟨∇P, ψ⟩ = −⟨P, div ψ⟩ = 0` for every test
field `ψ`. The pressure is eliminated exactly, and no pressure unknown or projection is needed.

### 10.3 Radial quadrature

**Substitution.** `r = sinh u`, so `1+ρ = cosh²u`. The trial phase `θmω·log(1+ρ)` then grows at most like
`2θmω·u`.

**Rule.** Composite Gauss–Legendre on `u ∈ [0, U]`:
- 24 nodes per panel;
- panel width at most `min(¼, 12 rad / (4Kωθ))`;
- `U` chosen so that `ρ_max = 4·ln10·(DPS+15)`. The test Gaussian `e^{−ρ/4}` is then below `10^{−(DPS+15)}`
  at the cut-off, so the neglected tail is below the working precision.

**Stability.** Measured in the validate witness: change of every assembled matrix under refinement at
`θ = 1`. The refinement was 24 → 36 nodes per panel, together with a panel phase of 12 → 8 rad.

| truncation | S | nodes | max |ΔL| (max |L|) | max |ΔS-tensor| (max |S|) |
|---|---|---|---|---|
| L2N2K4 | 0.47 | 1728 → 3852 | 1.5e-46 (2.2e3) | 1.3e-47 (8.7e5) |
| L2N3K3 | 0.8 | 792 → 1728 | 1.0e-44 (1.7e4) | 2.9e-46 (1.6e6) |
| L3N2K3 | 1.0 | 624 → 1404 | 8.5e-42 (3.4e4) | 2.9e-43 (6.7e5) |

All entries are far below the 1e-30 bar. This replaces the phase-2 Q24 rule (1.7e-7 at `m = 5`,
1.3e-4 at `m = 6`).

**Validation at θ = 0.** The new system reproduces the phase-1 mpmath steady solutions (L2N2 and L2N3)
to residuals of 4.9e-46 to 2.8e-45. That floor is set by the 50-digit stored coefficients. Orbit B
re-converges quadratically at K = 4: `|F|` goes 14.1 → 3e-42, with `S = 0.8313389737222178`.

### 10.4 Homotopy θ: 0 → 1 of orbits B and C (K = 4, full space, not axisymmetric)

**Natural-parameter continuation.** Steps of 0.1, halved on failure down to 1/80.

| orbit | θ = 0 | converged | fails at |
|---|---|---|---|
| B (L2N2) | S = 0.8313389737, res 3.1e-42 | θ = 0.025 (S 0.94542), 0.0375 (S 0.96016) | θ = 0.05 |
| C (L2N3) | S = 0.4712083214, res 1.2e-43 | θ = 0.0125 (S 0.53998), 0.025 (S 0.62927) | θ = 0.0375 |

**Correction (commit `25d4d89d8a2`).** That commit's message lists θ = 0.0125 (S = 0.9166) among the natural-parameter points of B. That point came from the first natural step of the *arclength* run. The natural-parameter path recorded in `homotopyB.witness.json` is 0 → 0.025 → 0.0375, failing at 0.05, as in the table above. The history is not rewritten; this note is the correction.

Neither orbit collapses onto a steady solution in the solenoidal basis. That differs from the phase-2
C result, which was obtained in the non-solenoidal basis.

**Pseudo-arclength continuation (secant predictor, `y = (x, Wθ)`, `W = |x(θ=0)|`).** This tells a fold
in `θ` apart from a breakdown.

- **Orbit B.** The branch has a **fold at θ ≈ 0.0446**. After it, `θ` decreases while `|A|` grows:

  | θ | S | \|A\| |
  |---|---|---|
  | 0.0436 | 0.808 | 124 |
  | 0.0368 | 0.659 | 163 |
  | 0.0221 | 0.536 | 220 |

  A **second fold at θ ≈ 0.0202** follows, after which `θ` increases again:

  | θ | S | \|A\| |
  |---|---|---|
  | 0.0229 | 0.694 | 197 |
  | 0.0286 | 0.859 | 164 |
  | 0.0334 | 0.970 | 144 |

  Residuals stay at 1e-38 to 1e-41 along the whole path. The branch passes `θ = 0.05`, where
  natural-parameter continuation failed. At θ = 0.0421 it has S = 1.129 and |A| = 114, and at θ = 0.0501
  it has S = 1.244 and |A| = 92.4, so the amplitude is falling back towards its θ = 0 value. The run was
  stopped at the 2 h compute budget **at θ ≈ 0.0501, after two folds**. It did not reach `θ = 1`, and
  where it goes next is unknown.
- **Orbit C.** The first natural step converged at θ = 0.0125, with S = 0.53998. The first arclength
  corrector failed and was halved. The second step converged at **θ = 0.01986**, with S = 0.58367,
  |A| = 156 and residual 7.2e-43, and no fold so far. Each corrector attempt at L2N3K4 (n = 48 per mode)
  took about 15–20 min, so the run was stopped at the budget after one accepted step.

**Reading, scope (a).** In these truncations, the phase-1 periodic orbits continue into the solenoidal
log-phase family only along a path with folds. Within the 2 h budget, neither path came near the
admissible tail `θ = 1`. This does **not** show that the branch cannot reach `θ = 1`: an S-shaped path
can continue past further folds. Nor does it say anything about orbits that are not connected to B or
C. The cost per arclength step (about 3–4 min at L2N2K4, and far more at L2N3K4) is the reason the
continuation stopped.

### 10.5 Random starts at θ = 1, axisymmetric (zonal) subspace, K = 3

In each start:
- the initial period `S₀` is cycled through {0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12};
- the amplitude is log-uniform;
- the coefficients are random;
- Newton runs at `θ = 1` directly.

| truncation | starts | converged (periodic / steady / trivial) | failed |
|---|---|---|---|
| L2N2K3 zonal | 8 | 0 / 0 / 0 | 8 |
| L2N3K3 zonal | 8 | 0 / 0 / 0 | 8 |
| L3N2K3 zonal | 6 | 0 / 0 / 0 | 6 |

Every start ended with residual 1e6 to 1e15 after 8–21 iterations. With no candidates, the refinement
chain (K, then N, then L) was never triggered. The wall cost was 140–990 s per start. That limited the
number of starts, and it is why N4, L3N3 and full-space random starts were **not** run.

**How the witnesses were written.**
- `validate`, `homotopyB`, `homotopyC`, `random-L2` and `random-L3N2` were written by the probe.
- `homotopyB-arc` and `homotopyC-arc` were **transcribed from the run logs**. Both runs were stopped by
  hand at the 2 h compute budget:
  - B had no time budget;
  - C's `LERAY_TMAX` is checked only between arclength steps, and one L2N3 corrector outlasted it.

  Their `provenance` fields say so, and they carry only the printed digits (θ to 8 digits, S to 16).
  The transcription script is not committed; it copies the log lines with a regular expression.

### 10.6 Phase-3 verdict and what was not run

- **No candidate was found, so nothing persisted across even one refinement.** The stop-and-report
  condition was not triggered.
- Orbits B and C continue into the solenoidal log-phase basis only along folded paths, and were stopped
  at `θ ≤ 0.05`. The random search at the admissible tail found no orbit in 22 starts.
- All of this is **scope (a)**: these truncations, these starts and this budget. No structural exclusion
  is claimed.

**Not run within the budget.**
- N4 systems and L3N3.
- Full-space (non-zonal) random starts.
- Continuation of B and C beyond the reported `θ`.
- S beyond 12.

**Compute bottleneck.** Arb matrix assembly is rebuilt at every Newton step, and once more for each
`ω` and `θ` finite difference. Node counts grow like `Kωθ`.

### 10.7 Precision gates (phase 3)

`scripts/precision-gates.sh --changed` on this branch shows the same five red gates as §9.7:
- q0-anchor flip;
- q0-anchor refill;
- reference-literal;
- witness-value copy;
- q0-value drift.

All five were confirmed red on `origin/main` at `b17e0551c53`. None of the gate output names a file
from this branch. The seven tree-measuring witnesses the script rewrote were reverted.

## 11. Phase 4: pseudo-arclength continuation of B and C toward θ = 1 (arbitrary precision)

Approved by the owner ("Go"). Same probe ([`leray_dss_logphase_search.py`](../../computations/probes/leray_dss_logphase_search.py)),
modes `arcB` (L2N2, K = 4) and `arcC` (L2N3, K = 4). Arb at 60 dps. Budget: 3 h of compute.

### 11.1 Method

- **Continuation.** Secant pseudo-arclength in `y = (x, W·θ)`, with `W = |x(θ = 0)|`. Adaptive step:
  grow ×2 if the corrector needs ≤ 5 iterations, ×1.5 if ≤ 7, ×1 if ≤ 9, otherwise ×0.7. Halve on
  failure. Bounds `ds₀/64 ≤ ds ≤ 32·ds₀`.
- **Corrector.** Full Newton until `|F| < 1e-15(1+|A|)`, then a frozen Jacobian while each iteration
  gains at least 6 digits. At most 10 iterations. Every accepted point has residual 1e-38 to 1e-45.
- **Analytic ω column.** The basis depends on `(θ, ω)` only through `θω`, so
  `∂F/∂ω = (θ/ω)·∂F/∂θ + flat(i·m·M_m·A_m)`. This agrees with the finite-difference column to
  2.3e-26 at `θ = 0.05` and 4.3e-25 at `θ = 0.7`, which is the `O(h)` error of the `h = 1e-30`
  difference. One θ difference per Jacobian therefore gives both columns.
- **Stopping rules.** The run stops at the first of these:
  - (a) reaching `θ = 1` (then Newton at `θ = 1` and the refinement chain `K+1`, `N+1`, `L+1`);
  - (b) turning back to `θ = 0`, or closing on the start point;
  - (c) `|A| > 1e4`, `S < 1e-3` or `S > 1e3`;
  - (d) collapse to a steady solution;
  - the time budget.
- **Witnesses are written by the probe.** It checkpoints `leray-dss-logphase-arc{B,C}.witness.json`
  after every accepted point, and `LERAY_RESUME=1` restarts from the checkpoint. Nothing was
  transcribed from logs.

### 11.2 Results

Neither run reached any outcome (a)–(d). Both stopped on the time budget.

| orbit | accepted points | stop | θ at stop | S at stop | \|A\| at stop | folds in θ (approx.) |
|---|---|---|---|---|---|---|
| B (L2N2K4) | 50 | time budget | 0.051523 | 2.15919 | 48.46 | 0.0448, 0.0203, 0.0601, 0.0480, (0.0503), 0.0483 |
| C (L2N3K4) | 16 | time budget | 0.059359 | 0.85512 | 229.75 | 0.0322, 0.0038 |

**B.**
- B was re-run from `θ = 0`, because the phase-3 point at `θ ≈ 0.0501` had never been saved as a
  state. The new run reproduces phase 3: folds at `θ ≈ 0.0448` and `θ ≈ 0.0203` (`|A|` up to 226),
  and back to `θ = 0.0501` at step 30 (`S = 1.24362`, `|A| = 92.4`).
- Beyond that point it is new. It reaches `θ ≈ 0.0601` (`S = 1.63`, `|A| = 61`), folds, and runs
  back down to `θ ≈ 0.048` with `S` rising to 2.29.
- Steps 42–44 are a **continuation reversal, not a fold**. They retrace steps 37–41. For example,
  step 43 (`θ = 0.05032`, `S = 2.2063`, `|A| = 47.507`) matches `S = 2.2054`, `|A| = 47.514`
  interpolated between steps 38 and 39. The fold recorded at 0.0503 is that artefact.
  Reversal detection was added, and the run resumed backwards from step 44.
- After the resume, B turns again at `θ ≈ 0.04835` (`S ≈ 2.2778`). Steps 51–53 then rise in `θ`
  with `S` falling, to `θ = 0.0515`, `S = 2.159`. This lies close to the sheet B came down on
  (step 44: `θ = 0.0543`, `S = 2.038`).
- So within `0.048 ≤ θ ≤ 0.060`, B either turns twice at nearby points or retraces its own path.
  At step 51 the two sheets differ by about 7e-4 in `S` at matched `θ`. **This run does not decide
  which.**

**C.**
- C folds at `θ ≈ 0.0322` and runs back to `θ = 0.0038` (step 10, `S = 1.3562`, `|A| = 215.8`).
- Step 11 then lands at `θ = 0.0163` (`S = 1.227`). That step was taken before reversal detection
  existed, so a jump to a neighbouring branch is **not excluded**.
- From there `θ` rises steadily: `S` falls from 1.08 to 0.855 and `|A|` holds at about 230, up to
  `θ = 0.0594` at the stop.
- At about 7.5 min per step, reaching `θ = 1` at the current step lengths would take far longer
  than the budget.

**Refinement.** Outcome (a) never occurred, so there was no `θ = 1` candidate and the refinement
chain did not run.

### 11.3 Bugs found and fixed during phase 4

1. **The first chord corrector converged only linearly.** It refreshed the Jacobian only when the
   residual fell by less than a factor of 4. It failed in 14 iterations on B's first step. It was
   replaced by full Newton to 1e-15 followed by a frozen Jacobian (`a2afc68ac5e`).
2. **The step-growth rule shrank steps that should have grown.** It shrank when the corrector
   needed more than 6 iterations, and 60-digit correctors typically need 7. Fixed, and both runs
   resumed from their checkpoints (`1aa7860000b`).
3. **No reversal check.** The secant could flip direction without the run noticing (B, steps
   42–44). The probe now stops with `continuation_reversed_at_theta_…` when the new secant has a
   negative dot product with the previous tangent. `LERAY_REVERSE=1` resumes in the opposite
   direction at `ds_init/4` (`d1d061bb180`).

The misattribution in the `25d4d89` commit message is recorded in §10.4. History was not
rewritten.

### 11.4 What this does and does not show

All of it is scope (a): this continuation, of these two truncations, within a 3 h budget.
- In arbitrary precision, both orbits continue as genuine solutions of their truncated systems
  (residual ≤ 1e-38) up to `θ ≈ 0.05–0.06`. Neither escapes, and neither collapses to `ω = 0`.
- The path from `θ ≈ 0.06` to `θ = 1` was not traced. Nothing here says whether either branch
  reaches `θ = 1`.
- Nothing identifies `S` with any `q`-quantity. No content block was edited.

### 11.5 Precision gates (phase 4)

`scripts/precision-gates.sh --changed` on `f8d2ddac0d5` shows the same five red gates as §10.7,
all pre-existing on `origin/main` at `b17e0551c53`. None of the gate output names a file from this
branch. The seven tree-measuring witnesses the script rewrote were reverted.
