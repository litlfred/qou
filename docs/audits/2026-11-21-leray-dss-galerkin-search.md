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
  3.9e-9 (float64 only; D was not re-converged in mpmath, because the L2N4 periodic system costs
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

Not shown, and not tried:
- `L ≥ 5`, or `N ≥ 6` (`M` becomes ill-conditioned at about 1e9 by N5).
- Other trial tail scales, or other test weights.
- Continuation in an auxiliary parameter, such as a viscosity homotopy from a Hopf point.
- Whether the weak-`L³` DSS class with a nonzero `|y|⁻¹` tail is excluded by some result I have not
  checked.

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
