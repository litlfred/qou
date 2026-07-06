# 1 ppb gap-narrowing plan — post-PR #638 reanalysis

**Date:** 2026-05-11
**Branch:** `claude/close-level-selection-rule-bvMvw` (PR #638, awaiting review)
**Purpose:** plan next-push priorities for narrowing mass-prediction
gap to the **1 ppb target** (`docs/coordination/1ppb.md`); incorporates
findings from this session (PR #638) and concurrent sibling PRs
(#639, #640, merged #487, merged #637).

## Goal recap

**Target:** 1 ppb relative accuracy on QOU mass predictions
$\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}, \ldots, {}^{40}\mathrm{Ca}\}$
**without** deriving $Q_\beta$.

**Three-calibration discipline:** only $m_e$ (CAL-1), $q_0$
(CAL-2), $Q_\beta$ (CAL-3) are calibration anchors. Everything
else — masses, binding energies, $\Delta_{\mathrm{shell}}$ — is
a **prediction** of the framework.

**Hard floor:** $\sim 780$ ppb from CAL-2 uncertainty
($\sigma_{q_0}/q_0 = 1.22$ ppb amplified by
$|\partial \ln E_0/\partial \ln q_0| = 11.09$).

**Current state of best mass-prediction residuals (post-PR-638):**

| Quantity | Best prediction | Residual | Source |
|:---|---:|---:|:---|
| $Q_\beta$ (free neutron) | $0.7836$ MeV | $+0.168\%$ / $+1.31$ keV | PR #639 (Form A single-wrap) |
| $m_p$ via $\rho_K$ leading-order | — | $\sim 0.23\%$ MAE | PR #564 ledger row |
| $m_n$ via Path A T1+T4 | $0.561$ MeV | $-99.9\%$ | PR #640 (substrate-only, no calibration) |
| $B(D)$ via brane-tower | varies $50$–$10^4\%$ | refuted across 6 families | PR #638 closure |
| $B({}^3\mathrm{He})$ | varies $-56\%$ to $+10^6\%$ | refuted; structural gap real | PR #638 + B.1 audit |
| $B({}^4\mathrm{He})$ | $22.80$ MeV (pair-knot) | $-19.4\%$ (closest) | PR #638 family 5 |

The **structural gap** dominates: $Q_\beta$ at $+0.168\%$ is the
sharpest prediction in the framework, yet it's still 6 orders of
magnitude above 1 ppb. The full mass-binding sector has residuals
of $20$–$10^4 \%$ across atoms.

## What we've learned this session (PR #638)

**Closure findings on `conj:brane-tower-z-habiro`:**

1. **No scalar $n_\star$ rule closes** AME light-isotopes uniformly
   (6 probed families, all refuted by $\geq 50\%$ on some atom).
2. **Pair-knot operators $\sigma_{pp}, \sigma_{nn}$ activate at
   magic shells** under LP-dual (gap = 0 strong duality).
3. **Z↔N symmetry of substrate binding is AME-confirmed** at
   $\sim 0.03$ MeV after Coulomb correction.
4. **Additivity of magic-shell stabilization is REFUTED** at +88%
   (Δ_cat(⁴He)/Δ_cat(³He) = 3.76 vs predicted 2.0).
5. **Δ_cat structural-gap values at 50dps**:
   - D: $+2.026$ MeV
   - T: $+8.375$ MeV
   - ³He: $+7.507$ MeV
   - ⁴He: $+28.211$ MeV
6. **Categorical $|\tau(\beta)|$ is convention-independent** —
   the brane-tower regularization is the only convention-dependent
   piece (rigid monoidal Type-B-folded category, prop e830651e).

**Companion sibling findings:**

- **PR #639 per-partition $k_\lambda$**: failure at uniform $k$ is
  dominated by ONE specific partition per atom (D: $[2,2,1,1]$,
  T: $[6,3]$, ³He: $[5,4]$); per-partition truncation $k_\lambda$
  is the canonical refinement.
- **PR #487 (merged)**: $\tau_M$ (Wenzl-bridge canonical) vs
  $\tau_{SW}$ (Schur-Weyl, height $> 2$ kernel) disambiguated.
- **PR #637 (merged) `BraneTowerNStar.lean`**: β-decay-sector
  $n_\star = 2$ from three substrate candidates (Habiro $m_{\max}$,
  Coxeter, generator rank); β-decay closure at $+0.168\%$.
- **PR #640 neutron-mass 50dps chain**: $m_n$ Path A T1+T4 at 999
  ppb residual under substrate-only discipline.

**User insight on optimization:** "GS reduction → use crystal
bases" — the canonical replacement for Gröbner-Shirshov is the
KL / Kashiwara basis (AGENTS.md §7b). Bypasses exponential
algebra-rank growth; opens ¹⁶O / ⁴⁰Ca compute.

## Gap analysis: where the orders of magnitude live

To reach 1 ppb on a binding energy $B(\mathfrak{H})$, we need
relative precision $10^{-9}$. The current residual stack:

| Stage | Contribution | Magnitude (relative) |
|:---|:---|:---:|
| Calibration anchors ($m_e$, $q_0$) | inputs, fixed | $\sim 10^{-9}$ |
| Hard floor (CAL-2 amplified $\partial \ln E_0/\partial \ln q_0$) | propagation | $\sim 7.8 \times 10^{-7}$ |
| Markov trace $\tau(\beta)$ at 50dps | categorical, convention-independent | $\leq 10^{-30}$ |
| Operator-volume regularizer (brane-tower transient) | convention-dependent | **$10^{-1}$ to $10^4$** ← **dominant** |
| Magic-shell $\Delta_{\mathrm{shell}}$ unpredicted | gap to AME | $\sim 7$–$28$ MeV per atom |
| Coulomb correction (mirror nuclei) | $\sim 0.7$ MeV at $A = 3$ | $\sim 10^{-1}$ |

**The dominant blocker is the operator-volume regularizer + Δ_shell
gap** ($10^{-1}$ to $10^4$). All other sources are at or below the
hard floor.

## Strategic gap-narrowing options

To close the $10^4 \times$ gap from current $\sim 0.2\%$ to $1$ ppb,
we need to either:

**(A) Eliminate the structural gap entirely** by closing the
brane-tower formula's $\Delta_{\mathrm{cat}}$ residual.

**(B) Replace the brane-tower formula** with a substrate-derived
expression that directly produces AME values.

**(C) Calibrate** $\Delta_{\mathrm{cat}}$ as a measured input —
but this **violates the three-calibration discipline** and is
explicitly disallowed by the workplan.

Option (C) is off the table. Options (A) and (B) require structural
work; PR #638's six-way refutation + new conjectures point at the
right framework.

### Path (A): Close $\Delta_{\mathrm{shell}}$ from substrate data

`conj:magic-shell-stabilization` proposes that Δ_shell is
substrate-derivable. The closed-form conjecture
(`DeltaCouplingClosedForm` in Lean):

$$
  \Delta_{\mathrm{coupling}}(Z, N)
    \;=\; f\bigl(\tau(\sigma_{\mathrm{shell}})\bigr)
$$

with $f$ a categorical function and $\tau$ the Wenzl-bridge
canonical Markov trace.

**Empirical anchor (extracted, not calibrated):**
$\Delta_{\mathrm{coupling}}(2, 2) = +13.20$ MeV.

**Open work:**
1. Determine $f$ from a categorical/Hecke-algebraic identity.
2. Verify $\Delta_{\mathrm{coupling}}$ predictions at $Z = 8$
   (¹⁶O, $f(\tau(\sigma_{\text{O-shell}}))$ vs AME).
3. Couple with per-partition $k_\lambda$ (#639) for the brane-tower
   transient.

### Path (B): Replace the brane-tower formula

Per-partition $k_\lambda$ (PR #639) does this at the formula level:
non-uniform truncation across Wedderburn blocks regularizes each
atom's tower at the **dominant-partition** level. If the
per-partition rule is structurally determined, the brane-tower
contribution becomes a genuine prediction.

Combined Path (A)+(B): predict $\Delta_{\mathrm{cat}}$ via the
magic-shell layer AND regularize the brane-tower transient via
per-partition $k_\lambda$.

## Prioritized next-push tasks

Ranked by **leverage = (residual closed) / (compute or proof cost)**:

### Priority 0 — Verify the closure direction (high leverage, cheap)

**P0.1.** Compute $\tau(\sigma_{pp})$ and $\tau(\sigma_{nn})$ for
${}^{16}\mathrm{O}$ at 50dps via crystal-bases optimization (per
user's "GS reduction → crystal bases" insight). If
$\Delta_{\mathrm{coupling}}({}^{16}\mathrm{O}) = f(\tau(\sigma_{
\text{O-shell}}))$ matches an empirical extraction, the closed-form
conjecture gains a 3-atom calibration anchor → falsifiable
prediction at ${}^{40}\mathrm{Ca}$ (Z=20 magic). **Compute: hours
under crystal-bases; not feasible under naive GS.** Open
task: crystal-bases `markov_peel` rewrite (queued; see P3).

**P0.2.** Test per-partition $k_\lambda$ rule (PR #639) on
$\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ at uniform vs
per-partition truncation; quantify residual reduction. **Compute:
trivial — reuse eigenvalue spectra from
`probe-phiq-operator-valued.witness.json`.** ⟶ **Cherry-pick from
#639 once merged.**

**P0.3.** Run the **convention-independence test at full 50dps**
via Path C (Wenzl-bridge mpfr) — currently errored in
`probe_tau_three_path_50dps.py` for missing y_lambda mpfr witness
setup. Confirms `prop:rigid-monoidal-structural-gap-invariance` to
50dps. **Compute: 1 hr to set up + 5 min to run.**

### Priority 1 — Structural closure of $\Delta_{\mathrm{shell}}$

**P1.1.** Propose specific closed form for $f$ in
`DeltaCouplingClosedForm`. Categorical candidates (in order of
plausibility):

- $f(t) = c \cdot \log(1/t)$ — Φ_q-like growth on small $t$
- $f(t) = c \cdot (1/t - 1)$ — Φ_q first-pole behavior
- $f(t) = c \cdot \log(\Phi_q^{(\infty)}(t))$ — full q-dilogarithm
- $f(t) = c \cdot $ KLR-canonical-basis dimension count

Test: fit $c$ to the ⁴He anchor (+13.20 MeV); predict ¹⁶O.

**P1.2.** Extend `MagicShellStabilization` to incorporate the
**proton-pair sub-knot** as a categorical Hopf-link element of
$H_n(q)$, not just a 4-letter sub-braid. Use Murphy-central
elements (Type B crystal action). Connects to PR #618-followup
`spin-involution-lp-dual-invariance`.

**P1.3.** Prove that $\Delta_{\mathrm{shell}}$ for non-doubly-magic
$Z = 2$ atoms is well-defined under the cross-shell decomposition.
Probe ⁵Li (Z=3, N=2, A=5, n=15) and ⁶Li (Z=3, N=3, A=6, n=18) for
single-magic-shell stabilization; n=15 may be tractable under
crystal-bases.

### Priority 2 — Brane-tower closure via per-partition rule

**P2.1.** Combine PR #639's per-partition $k_\lambda$ with PR
#638's magic-shell finding: for each magic-shell atom, the
**dominant partition under uniform-k failure** corresponds to a
specific Wedderburn block; check whether $k_\lambda$ for the
dominant partition correlates with the magic-shell-occupancy pattern.

**P2.2.** Cherry-pick from #639's
`per-partition-k-lambda-rule.{md,ts,lean}` after #639 merges;
integrate into `brane-tower-z-habiro.md` §"Refined open question"
as the canonical surviving form.

**P2.3.** Probe the **dominant-partition $k_\lambda$ rule** at
${}^4\mathrm{He}$ — if it matches the empirical residual, the
brane-tower closure path may be complete for the AME light-isotope
sample.

### Priority 3 — Crystal-bases optimization (opens heavy-atom compute)

**P3.1.** Implement crystal-bases (Kashiwara / KL canonical)
reduction in `markov_peel` to replace Gröbner-Shirshov. Reference
implementations: KL polynomial computation in SageMath's Hecke
module + Cherednik–Markin Cherednik algebra Python packages.
**Compute cost:** $\sim 1$ week implementation; **payoff:** opens
$n \leq 60$ compute (⁴⁰Ca at n=120 is the next tier).

**P3.2.** Extend `wedderburn_jones_markov.global_wedderburn_sum_q_
hecke_seminormal` to use crystal-bases paths for the Wedderburn
sum; currently uses Hoefsmit seminormal which is O(d_λ²).

### Priority 4 — Mathlib infrastructure for Lean closure

**P4.1.** Discharge the §3b `sorry` in
`prop-rigid-monoidal-structural-gap-invariance.canonical` via the
proposed `MarkovTraceAxiomatic` Mathlib typeclass. Layer 1
(Jones-Wenzl uniqueness) is the load-bearing piece; Layers 2-3
are done.

**P4.2.** Discharge the `sorry` in
`MagicShellCrossCoupling.canonicalCrossCoupling` via concrete
identity (the canonical instance uses Δ_shell ≡ 0; cross
decomposition is then 0 = 0 + 0 + 0 — should be provable directly
via `simp`).

### Priority 5 — Other AME isotopes (heavy compute, post-crystal-bases)

**P5.1.** Compute $\Delta_{\mathrm{cat}}$ for ⁵Li, ⁶Li, ⁷Li, ⁹Be,
¹²C, ¹⁶O, ⁴⁰Ca — full magic-shell calibration table.

**P5.2.** Test the magic-shell stabilization conjecture's
falsifiable predictions on multi-shell-magic-cycle nuclei (e.g.
⁵⁸Ni at Z=28 magic, ²⁰⁸Pb at Z=82, N=126 doubly magic).

## Quantitative milestones

| Milestone | Residual target | Stage of plan |
|:---|---:|:---|
| **M0** (current) | $\sim 20\%$ on best atom | post-PR-638 closure refutations |
| **M1** | $\sim 1\%$ on doubly-magic ⁴He | per-partition $k_\lambda$ (P2.x) |
| **M2** | $\sim 0.1\%$ on AME light-isotope sample | Δ_shell prediction (P1.x) |
| **M3** | $\sim 0.01\%$ ($10^{-4}$, $100$ ppm) | both Δ_shell + per-partition $k_\lambda$ |
| **M4** | $\sim 10$ ppb | + extend to A ≥ 5 via crystal-bases (P3) |
| **M5** (1 ppb target) | $\sim 1$ ppb | + closed-form $f$ for Δ_coupling (P1.1) |
| **Hard floor** | $\sim 780$ ppb | CAL-2 propagation; cannot improve without CAL-2 precision |

**Critical path to 1 ppb**: M1 → M2 → M3 require P2.x and P1.x.
M4 requires P3 (crystal-bases). M5 is the final closed-form step.

**Estimated next-push scope:** P0.1, P0.2, P0.3, P1.1, P2.2 — a
single PR landing the per-partition cherry-pick + the Wenzl-bridge
mpfr 50dps Path C verification + a closed-form $f$ proposal would
move M0 → M1.

## Coordination dependencies

- **#639 (Q_β spectral bridge + per-partition $k_\lambda$):** must
  land before P2.2 cherry-pick. Their refactor of `BraneTowerNStar.
  RecoversWithRelativeError` is the predicate this branch's
  refutation theorems integrate with via B.3.
- **#640 (neutron mass 50dps):** independent; produces $m_n$
  prediction at 999 ppb — directly contributes to the M3 milestone
  once Δ_shell prediction lands.
- **Main:** #487, #637 merged; #639, #640 still open. Next-push
  PR should rebase onto post-#639-merge `main` to inherit the
  per-partition machinery.

## Anti-patterns to avoid (per AGENTS.md three-cal discipline)

- ❌ **Calibrate** Δ_shell or Δ_coupling to AME — this is fitting,
  not predicting.
- ❌ **Add** ad-hoc per-atom corrections that don't trace to
  substrate data.
- ❌ **Tune** $n_\star$ or $k_\lambda$ per atom without structural
  justification.

All next-push work must satisfy: every numerical input is one of
the three calibration anchors ($m_e$, $q_0$, $Q_\beta$); every
prediction is derived.
