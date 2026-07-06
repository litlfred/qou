> **DEPRECATED on 2026-05-24.** Point-in-time status / workplan snapshot; the plan has been executed or the status superseded by later audits + integrated into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T3 for the deprecation rationale.

# Workplan update — atomic-braid + Markov-trace integration into the ρ_K mass framework

**Date:** 2026-05-09
**Branch:** `claude/workplan-update-rho-k`
**Supersedes (in part):** [`docs/audits/2026-05-05-markov-trace-axiomatic-workplan.md`](2026-05-05-markov-trace-axiomatic-workplan.md)
**Pin:** [1 ppb coordination ledger](../coordination/1ppb.md)

## TL;DR

The 2026-05-05 workplan was scaffolded around the **legacy E₀ mass
formula** $M(K) = E_0 \cdot (T_1 + \dots + T_4) + T_6$ with proton-
only calibration. That scaffold has been superseded by the **ρ_K
assembly** $M(K) = \rho_K \cdot m_e \cdot |\operatorname{tr}_M(K)|$
that landed on `main` in [PR #564](https://github.com/litlfred/qou/pull/564)
(commits `86aaeb51a` / `400c7961d`).

⚠ **The LO ρ_K ansatz is a tautology, not a prediction.** Per
[PR #600's audit](https://github.com/litlfred/qou/pull/600#issue-…)
([`docs/audits/2026-05-09-mass-table-fitting-audit.md`](2026-05-09-mass-table-fitting-audit.md)
§"Δ_λ derivation status"): defining
$\rho_K^{\text{LO}} \equiv (Z\,m_p + N\,m_n) / (m_e\,|\operatorname{tr}_M|)$
makes $|\operatorname{tr}_M|$ cancel in
$M(K) = \rho_K^{\text{LO}} \cdot m_e \cdot |\operatorname{tr}_M|$,
yielding $M_{\text{pred}}^{\text{LO}} = Z\,m_p + N\,m_n$ by
construction. The "0.119 / 0.302 / 0.275 / 0.759 % errors" on
D / T / ³He / ⁴He **are exactly the AME binding energies** —
the LO framework predicts **null binding**.

The real structure lives **per Wedderburn block** in the
$\Delta_\lambda(K)$ corrections, which **derive the binding energy
from substrate**:

$$
  \boxed{\;\;
    M(K) \;=\; m_e \cdot \sum_{\lambda \,\vdash\, 3A}
       y_\lambda(q)\,\chi^\lambda(\beta_K)\,\bigl(1 + \Delta_\lambda(K)\bigr)
  \;\;}
$$

per [`prop:rho-k-h3a-refinement`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md)
with **per-block binding fractions** $\Delta_\lambda(K)$. The
LO ansatz is the limit $\Delta_\lambda \equiv 0$.

The open problem is **deriving $\Delta_\lambda(K)$ categorically as
the binding-energy mass-defect**. PR #613's
[Δ_λ derivation race](https://github.com/litlfred/qou/pull/613) +
PR #600's audit catalogue 5 closure principles tested so far:

| Option | Selector | Outcome |
|---|---|---|
| **Occam** | min \|Δ\| over single-support | underdetermined |
| **B** Frob co-Casimir ([#602](https://github.com/litlfred/qou/pull/602)) | theorem-forced | fails — wrong sign |
| **C** Demazure-fiber | $y_\lambda \cdot D_w / D_{w_0}$ | reproduces $M^{\text{LO}}$ trivially |
| **D** LP shadow prices ([#603](https://github.com/litlfred/qou/pull/603)) | LP dual at min Σ\|Δ\|·w | reproduces Occam |
| **E** crystal-graph weight (in-flight) | Kashiwara crystal at $q \to 1$ | TBD |
| **F** Wenzl-bridge augmented Markov (in-flight) | augment Markov axioms | TBD |

Per the [GAP-A-3 / GAP-A-4 guidance](2026-05-09-gap-a-3-a-4-guidance.md),
the open problem is **GAP-A-3** (brane-tower level $n_*(K)$) and
**GAP-A-4** (per-block $\Delta_\lambda$ structural rule) — not a
seventh closure principle.

This document records:
1. What the ρ_K^full shift means for my prior PRs (#534, #547, #548).
2. Where the recursive axiomatic Markov-trace reducer + verification
   computes from those PRs **still contribute** to deriving
   $\Delta_\lambda(K)$.
3. Concrete next-step proposals aligned with the 1 ppb ledger and
   the GAP-A-4 structural search.

## What changed on main since 2026-05-06

(High-impact merges relevant to mass prediction and the atomic-braid
Markov-trace pipeline.)

| PR | Date | Summary | Touches my work? |
|----|------|---------|-----------------|
| [#564](https://github.com/litlfred/qou/pull/564) | 2026-05-08 | **ρ_K assembly** + 1 ppb plan + 258→0 §3b violators | ⚠ supersedes Strategy-3 mass-table scaffold |
| [#567](https://github.com/litlfred/qou/pull/567) | 2026-05-08 | Crystal R-matrix Sub-lemma 2.1 + AXKIA pole-order witness + CAL-3 / 1ppb CI gates restored | ✓ uses the recursive Markov trace from #547 |
| [#572](https://github.com/litlfred/qou/pull/572) | 2026-05-08 | Hecke-NF cycle-composition + canonical Jones-Markov $y_\lambda$ wire-up + **Path A verified for proton + deuteron**: $\operatorname{ord}_{u=0}(\operatorname{tr}_M) = 18Z + 21N + 1$ | ✓ #547 reducer is one of three independent paths |
| [#586](https://github.com/litlfred/qou/pull/586) | 2026-05-09 | Mathlib Tier-A batch (categorical-linking-operation + hoefsmit-ew-cell-content predicates) | — |
| [#604](https://github.com/litlfred/qou/pull/604) (#608/#614) | 2026-05-09 | Binding-K SDP solver at $H_{3A}$ + factorisation finding | ✓ uses canonical |tr_M| |
| [#613](https://github.com/litlfred/qou/pull/613) | 2026-05-09 | **Δ_λ derivation race** (5 closure principles, all fail/trivialise) + Pentagon-uv-commutation Woronowicz closure | ⚠ rules out 5 of my "test alternative T1 modes" candidates |
| [#615](https://github.com/litlfred/qou/pull/615) | 2026-05-09 | Canonical-convention migration batch 1 (4He chain + deprecation notices) | — |
| [#566](https://github.com/litlfred/qou/pull/566) | 2026-05-09 | Trivial-skeleton audit + 65 class-axiomatised conjectures, tiered A/B/C | — |

## ρ_K vs my Strategy 3 — the structural shift

**Legacy E₀ formula (what PR #548 implemented):**

$$
  M(K) \;=\; E_0 \cdot \bigl(T_1 + T_2 + T_3 + T_4\bigr) + T_6,
  \qquad E_0 \;=\; \frac{M_p^{\text{CODATA}} - T_{6,p}}{T_{1,p} + T_{2,p} + T_{3,p} + T_{4,p}}.
$$

Issues: Strategy-3 mean |err%| = 27.55% across non-proton atoms.
My T1-modes sweep showed even legacy-T1 + my tower terms gave 29%
err — the gap was systemic to E₀-anchoring under atomic-braid T1.

**ρ_K^full per-block decomposition (what landed on main as the
target categorical formula):**

$$
  M(K) \;=\; m_e \cdot \sum_{\lambda \,\vdash\, 3A}
    y_\lambda(q)\,\chi^\lambda(\beta_K)\,\bigl(1 + \Delta_\lambda(K)\bigr).
$$

Equivalently, factoring out $|\operatorname{tr}_M(\beta_K)| =
|\!\sum_\lambda y_\lambda \chi^\lambda(\beta_K)|$:

$$
  \rho_K(q) \;-\; \rho_K^{\text{LO}}(Z, N) \;=\; \frac{1}{|\operatorname{tr}_M(\beta_K)|}
    \sum_{\lambda \,\vdash\, 3A} y_\lambda(q)\,\chi^\lambda(\beta_K)\,\Delta_\lambda(K).
$$

The leading-order ansatz $\rho_K^{\text{LO}} = (Z\,m_p + N\,m_n) /
(m_e\,|\operatorname{tr}_M|)$ is the limit $\Delta_\lambda \equiv 0$.
Three CAL inputs ($m_e$, $m_p$, $m_n$ via $Q_\beta = m_n - m_p - m_e$),
no derived $E_0$.

Per the leading-order verification witness
[`atomic-mass-via-rho-k.witness.json`](../../computations/atomic-mass-via-rho-k.witness.json),
the LO ansatz alone gives:

| atom | $|\operatorname{tr}_M|$ | $\rho_K^{\text{LO}}$ | M_pred (MeV) | LO err% | full-formula gap |
|---|---:|---:|---:|---:|---|
| p | 1.06531 | 1723.59 | 938.27209 | 0.000 | (anchor) |
| n | 0.92323 | 1991.57 | 939.56542 | 0.000 | (anchor) |
| D | 0.38829 | 9453.0  | 1877.838 | 0.119 | $\Delta_\lambda$ closes 0.119% |
| T | 0.10405 | 52828   | 2817.403 | 0.302 | $\Delta_\lambda$ closes 0.302% |
| ³He | 0.20654 | 26609 | 2816.110 | 0.275 | $\Delta_\lambda$ closes 0.275% |
| ⁴He | 0.05535 | (computed) | 3755.675 | 0.759 | $\Delta_\lambda$ closes 0.759% |

Mean MAE on D/T/³He at LO = **0.232%**; including ⁴He = **0.39%**.

**The $\Delta_\lambda(K)$ corrections are the categorically rich
content** — they encode per-Wedderburn-block deviation of the
$\lambda$-block contribution from the constituent piece, and
**must be derived from substrate** to close to 1 ppb. They are
NOT free parameters in the LO sense — the full formula has
$p(3A) - 1$ DOF for $\Delta_\lambda$ per atom (e.g. 11 - 1 = 10
DOF for D, 30 - 1 = 29 DOF for T or ³He, 77 - 1 = 76 DOF for ⁴He),
constrained by a single mass equation, leaving 9-75 DOF
underdetermined per atom without a categorical closure.

The ρ_K^full assembly does NOT need:
- T2 / T3 tower terms (Markov-axiom or li2q),
- T4 Frobenius codim,
- T6 cyclotomic tail (now **diagnostic-only by design** — see
  [`atomic_braid_mass_terms.t6_canonical_MeV`](../../computations/atomic_braid_mass_terms.py)
  docstring: by Mittag-Leffler complementarity per
  [`AUDIT-DEEP-2026-05.md §3.3a`](../../AUDIT-DEEP-2026-05.md), T6's
  cyclotomic principal-part `pp_at_roots(u)` is one of THREE
  complementary pieces of `tr_M(u²)`, not an independent additive
  correction; `markov_trace_recursive.py` returns the full
  `|tr_M|` which already includes it; adding T6 again would
  double-count),
- inter-nucleon Δ_I knot factor a(Z,N),
- full-twist Δ_n² scalar.

**My Strategy-3 ansatz over-engineered the formula.** The correct
scaffolding is per-Wedderburn-block. The legacy "tower terms"
were a coordinate system on the wrong basis; ρ_K^full uses the
canonical Schur-Weyl basis $\{V_\lambda\}_{\lambda \vdash 3A}$.

## What from #534 / #547 / #548 still contributes

Even though Strategy 3's mass-formula scaffold is obsolete, several
deliverables from my prior work remain load-bearing:

### From PR #534 + #547 (recursive axiomatic Markov-trace reducer)

The recursive reducer (`markov_trace_recursive.py`) is one of
**three independent paths** that compute $|\operatorname{tr}_M(K)|$
to 1 ppb agreement (per #572's q-Hecke seminormal closure). The
three paths:

1. **Hoefsmit seminormal** (`hoefsmit_symbolic.py` + `markov_peel`)
2. **Recursive axiomatic** (`markov_trace_recursive.py` from #547)
3. **q-Hecke seminormal via Wenzl bridge** (`wedderburn_jones_markov.py`
   from #572) — agrees to 1e-13 (proton/neutron) / 1e-10 (deuteron)
   float64; mpmath-50dps via #564's `rho_k_h3a_refinement.py` agrees
   to 1.4e-16.

This three-way agreement is a **structural cross-check** that
protects against representation-theoretic bugs (cf. #546's
seminormal `IndexError`). The recursive path also unlocks the
disjoint-product property verification at 50-dps (mpmath-exact
$\Delta < 10^{-50}$).

### From PR #547 (multi-atom anchor + disjoint-product)

The disjoint-product property
$|\operatorname{tr}_M(\alpha \otimes \beta)| = |\operatorname{tr}_M(\alpha)| \cdot |\operatorname{tr}_M(\beta)|$
on commuting clusters is **still an open question for compound
nuclei** (the actual atomic-braid words are NOT disjoint — they
have inter-nucleon crossings). The verification at the disjoint
limit gives a baseline for measuring how much linking matters.

### From PR #548 (Δ_n² verification computes)

[`full_twist_delta_n2_verification.py`](../../computations/full_twist_delta_n2_verification.py)
and [`full_twist_root_of_unity_probe.py`](../../computations/probes/full_twist_root_of_unity_probe.py)
established a **structural finding** on
[`conj:categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/braids-and-knots/categorical-neutrality-saturated-shells.md):
at magic n=2, the Δ_n²-invariant subspace is empty under generic-
or root-of-unity scalar action (q^{c(λ)} = 1 fails for both partitions
of 2). The conjecture must hold via:
- (b) sum-cancellation across blocks, or
- (c) non-scalar Δ_n² action component (e.g. captured in T2/T3).

This restricts the conjecture's mechanism. Per #613's Δ_λ
derivation race (which tested 5 closure principles and found
they all fail/trivialise), this finding likely connects to
**GAP-A-3 / GAP-A-4** as part of the open structural problem.

### From PR #548 (T1 modes sweep)

[`atomic_braid_mass_table_modes_sweep.py`](../../computations/atomic_braid_mass_table_modes_sweep.py)
empirically established that **the legacy E₀ formula's gap was
in tower terms, not T1**. With ρ_K replacing E₀, this analysis
informs which T1 anchor representation to use — ρ_K's leading-
order ansatz uses the canonical GS-NF |tr_M|, but the modes
sweep confirms the atomic-braid alternative gives consistent
values modulo 50-dps (see PR #547 cross-check).

## Open work — aligned to the 1 ppb ledger

The 1 ppb ledger lists 6 open phases (P2-P6, P8). Items where my
prior infra plays:

### P3 — real $H_{3A}$ Wedderburn weights (substantive math, ~2 wk)

**Goal:** refine ρ_K beyond leading-order via H_{3A} Wedderburn
weights, closing the residual 0.119-0.759% errors toward 1 ppb.

**State of art on main (post #613):** 5 closure principles tested:
- Option B (co-Casimir): trivialises
- Option D (LP-shadow): trivialises
- Option F (Wenzl-bridge): fails
- Option G (gg-trajectory + Frobenius pairing): fails
- Occam principle (#564 baseline): the leading-order ansatz, no
  refinement

Per [`docs/audits/2026-05-09-gap-a-3-a-4-guidance.md`](2026-05-09-gap-a-3-a-4-guidance.md):
*"All 5 fail or trivialise — the open problem is genuinely GAP-A-3
/ GAP-A-4 and not the closure principle."*

**Connection to my work:**
- PR #547's disjoint-product check + cross-check infra can be
  extended to verify Path A consistency at $n = 6$ (deuteron),
  $n = 9$ (T/³He), $n = 12$ (⁴He) for any new candidate ρ_K
  refinement.
- #548's Δ_n² verification at $n = 6, 9, 12$ already tabulates
  $c(\lambda)$ and $q^{c(\lambda)}$ data per Wedderburn block —
  this is exactly what GAP-A-4 hypothesis 1 ("orthogonal
  Wedderburn copies") needs to compute multiplicities.

**Concrete next step:** run the GAP-A-4 hypothesis 1 test (count
multiplicity of dominant $\lambda^*$ in isotypic decomposition)
using the existing #547 + #548 verification infra. If hypothesis 1
fails, fall back to hypothesis 3 (isospin multiplicity 2I+1).

### P4‴ — migrate legacy `atomic_braid_mass_table.py` to ρ_K path

**Goal:** my PR #548's `atomic_braid_mass_table.py` still uses the
legacy E₀ formula. It should either:
- Be deprecated (keep the witness for cross-check, drop the formula
  output), OR
- Be rewired to the ρ_K assembly + Path A `atomic_mass_via_rho_k.py`
  on the canonical-convention chain.

**Recommendation:** rewire. The recursive Markov-trace reducer
(`markov_trace_recursive.py`) becomes the |tr_M| input to ρ_K
without changing the witness shape. The T2-T6 machinery in
`atomic_braid_mass_table.py` is the legacy code; remove it.

### P4ⁱᵛ — extend ρ_K table to ⁵Li, ⁶Li, ⁷Li, ⁹Be, ¹²C, ¹⁶O

**Goal:** populate the rest of the mass-table rows. Per #564's
audit, |tr_M| already exists for ⁵Li / ⁶Li in `atomic-tr-m-mpfr-50dps.witness.json`
(merged via #567's CAL-3 + 1ppb CI gates). Also #547's recursive
reducer can compute these directly.

**Connection to my work:**
- The recursive reducer scales to arbitrary $H_n$ with LRU memoisation
  on basis elements (`tr_m_basis_element.cache_info()`). Computing
  ⁵Li at $H_{15}$, ⁶Li at $H_{18}$ is feasible but slow.
- Path A consistency (PR #572 deuteron in $H_6$ took 131 s) suggests
  ⁵Li/⁶Li will be tens of minutes per atom — borderline tractable.

### P5′ — quotient-braid `a(Z, N)` for A ≥ 5 (dissolved)

In the legacy E₀ formula, the quotient-braid Jones factor `a(Z, N)`
was a placeholder for A ≥ 5. In ρ_K^full this question **dissolves
into Δ_λ**: there is no separate inter-nucleon factor; the per-block
$\Delta_\lambda$ corrections subsume it. The empirical question
becomes: do the $\Delta_\lambda$ patterns extend to A ≥ 5?

### P6 — jet-order → SDP wiring (50-500× compute speed-up)

Tracked in #565 (compute-infrastructure audit). Not directly
adjacent to my work, but PR #547's `markov_trace_recursive.py`
+ `gb_filtration_jet_tracker.HeckeElement` could provide a
fast-path for SDP constraint generation.

## Concrete next-step proposals

The central problem is **deriving $\Delta_\lambda(K)$ categorically**.
Each proposal below either:
- proposes a new closure principle for $\Delta_\lambda$ (after the
  5 in PR #613 were ruled out), or
- furnishes empirical structure that constrains the search.

### Proposal 1: empirical $\Delta_\lambda$ tabulation across atoms (in flight)

**Status:** in flight on this branch as
[`delta_lambda_empirical_tabulation.py`](../../computations/delta_lambda_empirical_tabulation.py)
+ caching helpers
[`y_lambda_at_q0_cache.py`](../../computations/y_lambda_at_q0_cache.py)
and
[`chi_lambda_at_q0_cache.py`](../../computations/chi_lambda_at_q0_cache.py).
Coordinated with [PR #600](https://github.com/litlfred/qou/pull/600#issuecomment-4413090489).

**Effort:** 1 PR, ~1 day (cached chi already exists; y_λ cache being
built in parallel).
**Deliverable:** for each $K \in \{D, T, {}^3\!He, {}^4\!He\}$:

1. Load $y_\lambda(q_0)$ from cached
   [`y-lambda-at-q0.witness.json`](../../computations/y-lambda-at-q0.witness.json)
   (built once via parallel `multiprocessing.Pool`; eliminates the
   13-minute symbolic re-evaluation bottleneck).
2. Load $\chi^\lambda(\beta_K)(q_0)$ from cached
   [`chi-lambda-at-q0.witness.json`](../../computations/chi-lambda-at-q0.witness.json)
   (D / T / ³He) or `per_partition` table (⁴He).
3. **Solve the underdetermined system**
   $\sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda = \Delta M / m_e$
   (where $\Delta M = M_{\text{codata}} - (Z m_p + N m_n)$ is the
   binding-energy mass-defect) under four candidate ansätze:
   - **(a) single-block**: $\Delta_\lambda \neq 0$ only for one
     $\lambda^*$, swept over all $\lambda \vdash 3A$. *(Overlaps
     with the existing Occam option in
     [`rho_k_h3a_refinement.py`](../../computations/rho_k_h3a_refinement.py);
     reproduced here for cross-atom pattern check.)*
   - **(b) shell-supported**: $\Delta_\lambda \neq 0$ only for the
     "staircase" $\lambda_{\text{shell}}$ (per
     [`prop:sigma-shell-from-beta-chain-derivation`](../../content/quantum-observable-universe/braids-and-knots/sigma-shell-from-beta-chain-derivation.md)).
     **Net-new** vs the 5 closure principles already tested.
   - **(c) Δ-monotonic**: $\Delta_\lambda \propto c(\lambda)$
     (uses content-sum data from PR #548).
     **Net-new** vs the 5 closure principles already tested.
   - **(d) Δ-isotypic**: $\Delta_\lambda \propto \dim_q(\lambda) /
     [n]_q!$ (Plancherel weight). *(Likely overlaps with the
     Demazure-fiber Option C from PR #613 race; reproduces
     $M^{\text{LO}}$ trivially.)*
4. For each ansatz, report which assignment minimises $\|\Delta\|_2$
   and matches CODATA.
5. **Look for a categorical pattern** across atoms: does the same
   $\lambda^*$ dominate? Does $\Delta_\lambda$ scale with
   $|\!\!\operatorname{tr}_M\!|$ or $A$ in a clean way?

**Why this contributes:** PR #600 catalogued 5 closure principles
that all fail or trivialise on the SUM equation. Ansätze **(b) shell-
supported** and **(c) content-monotonic** are genuinely new and use
data not exploited by Options B/C/D/E/F. If either gives a clean
cross-atom pattern (same $\lambda^*$ recurs, or single $\alpha$
fits all atoms), that's a candidate categorical $\Delta_\lambda$
rule. Negative result also informative — it would close (b) and (c)
and narrow the search to (E), (F), or a sixth principle.

### Proposal 2: GAP-A-4 hypothesis-1 test (isotypic multiplicity)

**Effort:** 1 PR, ~1 day.
**Deliverable:** `gap_a4_hypothesis_1_isotypic_multiplicity.py` +
witness. Tests whether the empirical observation
$\rho(K) \in \{1, 1, 1, 2, 2, 1\}$ for $\{p, n, D, T, {}^3\!He, {}^4\!He\}$
matches the **multiplicity of the dominant Wedderburn block in the
isotypic decomposition of $H_{3A}|_{\beta_K}$**.

For each $K$:
1. Compute the dominant $\lambda^*(K)$ from #572's
   `tr-m-q-hecke-seminormal.witness.json` (top-3 contributions).
2. Use #548's `full_twist_delta_n2_verification.py` data structure
   to count multiplicity of $\lambda^*$ in the isotypic decomposition
   of $H_{3A}$.
3. Compare to observed $\rho$.
4. If hypothesis 1 fails for T/³He, automatically test hypothesis 3
   (isospin multiplicity 2I+1).

**Note:** in ρ_K^full this hypothesis tests the structural integer
prefactor on $\Delta_\lambda$, not on the LO ansatz. The integer
$\rho \in \{1, 2\}$ may instead be a multiplicity factor INSIDE
$\Delta_\lambda$ rather than a separate prefactor.

**Why this contributes:** identifies the integer-multiplicity
structure inside $\Delta_\lambda(K)$. Even if the hypothesis fails,
the multiplicity table is paper-grade data.

### Proposal 3: Path A consistency check at ⁴He via #547 reducer

**Effort:** 1 PR, ~half day (compute may take hours).
**Deliverable:** `per_irrep_pole_helium4_h12.py` + witness
verifying $\operatorname{ord}_{u=0}(\operatorname{tr}_M(\beta_{^4\!He}))
= 18 \cdot 2 + 21 \cdot 2 + 1 = 79$, parallel to PR #572's proton
($H_3$, ord 19) and deuteron ($H_6$, ord 40) verifications. The
⁴He chi cache is already saved in
[`chi-helium-4-h12-numeric.witness.json`](../../computations/chi-helium-4-h12-numeric.witness.json)
(per the GAP-A-3/A-4 guidance), so this is a per-term ord
analysis, not a full χ recomputation.

**Why this contributes:** closes Path A for the next compound
atom in the table. Combined with proton + deuteron, this gives
3-atom evidence for the additive-shift formula
$\operatorname{ord}_{u=0} = 18Z + 21N + 1$. This formula
constrains the per-block $\Delta_\lambda$ structure: any
categorical $\Delta_\lambda$ rule must be consistent with the
overall pole order being $18Z + 21N + 1$.

### Proposal 4: Deprecate / simplify `atomic_braid_mass_table.py`

**Effort:** 1 PR, ~half day.
**Deliverable:** `atomic_braid_mass_table.py` reduced to a
ρ_K-path consumer (drops T2-T6 machinery, uses
`atomic_mass_via_rho_k.py` + `markov_trace_recursive.py`). Witness
schema unchanged (still emits `M_pred`, err_pct per atom) so
downstream consumers don't break. Adds optional emission of the
per-block $\Delta_\lambda$ residuals when `tr-m-q-hecke-seminormal.witness.json`
data is available.

**Note on T6:** the existing `t6_canonical_MeV` import already
returns 0 by design (Mittag-Leffler complementarity, per
[`atomic_braid_mass_terms.py`](../../computations/atomic_braid_mass_terms.py)
docstring). So part of the simplification — dropping the T6
addition — is already in effect via the upstream module; the
remaining work is to drop the T2/T3/T4 layer and switch the
formula to ρ_K^full.

**Note on canonical-convention recipes (PR #615 batch 1):** the
operator-valued canonical chains for p, n, D, ⁴He are now committed
([`atomic-braid-recipe-{p,n,d,4he}-canonical.derivation.json`](../../computations/atomic-braid-recipe-p-canonical.derivation.json)
+ [`build_atomic_braid_recipe_canonical_chain.py`](../../computations/build_atomic_braid_recipe_canonical_chain.py)).
The deprecation should adopt this canonical convention rather
than my Strategy 3's ad-hoc `[1]*7+[2]*4` proton word. T/³He are
not yet in the canonical chain (PR #615 batch 1 only covers
p, n, D, ⁴He) — mark these atoms `compute_status: "tr_M_only"`
in the witness until batch 2 lands.

**Why this contributes:** P4‴ in the 1 ppb ledger; reduces
maintenance burden, removes the misleading mass-table entry that
suggested the legacy E₀ formula was viable, and aligns with the
canonical convention that #615 is rolling out.

### Proposal 5 (lowest priority): Δ_n² + Δ_λ correlation study

**Effort:** 1 PR, ~1 day.
**Deliverable:** correlation matrix between PR #548's $c(\lambda)$
table (full-twist content sums) and the empirical $\Delta_\lambda$
assignments from Proposal 1. Tests whether the structural finding
at magic n=2 (no Δ_n²-invariant block under generic-q scalar
action) connects to the per-block $\Delta_\lambda$ pattern. If
$\Delta_\lambda$ correlates with $c(\lambda)$, that's evidence
for path (c) of the categorical-neutrality conjecture (non-scalar
action component captured in $\Delta_\lambda$).

**Why this is lower priority:** speculative; might or might not
yield a categorical insight. Punt unless Proposal 1 leaves residual
mystery in the per-block pattern.

## Recommendation

**Run Proposal 1 first** (empirical $\Delta_\lambda$ tabulation).
This is the keystone deliverable: it generates the per-atom
$\Delta_\lambda$ assignments under several candidate ansätze and
looks for a categorical pattern. Until we have this data, all
other $\Delta_\lambda$ closure attempts are guesses.

**Run Proposals 2 + 3 in parallel** (GAP-A-4 isotypic
multiplicity + ⁴He Path A). Both feed into Proposal 1's pattern
search: Proposal 2 furnishes the integer-multiplicity structure
inside $\Delta_\lambda$, Proposal 3 furnishes the pole-order
constraint $\operatorname{ord}_{u=0}(\operatorname{tr}_M) = 18Z + 21N + 1$
that any $\Delta_\lambda$ rule must respect.

**Defer Proposal 4** until after the rho_k-h3a refinement work on
main settles — modifying `atomic_braid_mass_table.py` while the
canonical-convention migration is in flight (PR #615 batch 1)
risks merge conflicts.

**Defer Proposal 5** unless Proposal 1 leaves the per-block
pattern unexplained.

## Sibling-PR awareness

Watching `origin/main` via the `local/watch` skill (5-minute poll,
persistent monitor armed at session start). New commits are
integrated into this workplan via the §3 checklist (overlap /
conflict / reuse / act-or-defer).

Active-branch awareness as of 2026-05-09 16:40 UTC:

- **PR #564** (rho_K assembly + 1ppb plan) — merged, foundation
  of this workplan.
- **PR #572** (Hecke-NF + q-Hecke seminormal closure + Path A
  proton/deuteron) — merged, foundation of Proposals 2 + 3.
- **PR #613** (Δ_λ derivation race + Pentagon-uv-commutation
  Woronowicz closure) — merged; rules out 5 closure principles
  for $\Delta_\lambda$ (informs Proposal 1's ansatz space).
- **PR #614** (Binding-K SDP solver + factorisation finding) —
  merged; binding-K SDP at $H_{3A}$ is parallel infrastructure
  to ρ_K^full, may inform Proposal 1.
- **PR #615 batch 1** (canonical-convention migration: 4He +
  deprecation notices) — merged; provides canonical chains for
  p, n, D, ⁴He used in Proposal 4.
- **PR #586** (Mathlib Tier-A batch) — merged; Lean
  formalization track, no direct mass-formula impact.
- **PR #600** (Δ_λ derivation race + audit doc + ρ_K extension to
  Li) — **merged 2026-05-09 ~17:30 UTC**; audit's "LO is tautology"
  finding informed this workplan's TL;DR rewrite (commit `2f421d795`).
  All 5 closure-race options (Occam / B / C / D / F) ruled out;
  Option E (crystal-graph weight) still in flight. Cross-coordination
  on PR #600 (3 comments before merge) documented the 2-row stratum
  finding from this branch.
- **PR #607** (chirality probes + Lean A-1 / A-4 §3b-cond instances)
  — merged 2026-05-09; orthogonal to mass-formula scope.
- **PR #612** (canonical atomic-braid-recipe-{p,n,d} chains +
  perf cascade) — **merged 2026-05-09 ~19:30 UTC**; major impact
  on this branch:
    * `chi-proton-h3.witness.json` and `chi-neutron-h3.witness.json`
      now ship symbolic χ^λ for all 3 partitions of n=3 — enables
      extending Proposal 1 to proton + neutron rows. Done in
      this branch on the post-rebase update.
    * `y_lambda_wenzl_bridge.py` adds in-place `@lru_cache` plus
      lazy-load from `y-lambda-wenzl-bridge-symbolic-witness.json`
      (13× speedup). My `y-lambda-at-q0.witness.json` (270 entries
      at 50-dps, parallel-built via lambdify) remains complementary
      as a STANDALONE numeric snapshot for consumers that want
      instant 50-dps without sympify cost.
    * `hecke_character_symbolic.q_character_on_braid_word` adds
      `atom_cache_label` parameter to read pre-computed χ^λ from
      `chi-{atom}-h{n}.witness.json`. Largely supersedes my
      `chi_lambda_at_q0_cache.py` for the in-cache atoms; my
      script remains useful as a fallback that computes missing
      partitions on-the-fly via `atom_canonical_crossings`.
    * `tr_m_q_hecke_seminormal._y_lambda_cached(n)` provides
      shared in-memory dict cache (T + ³He at n=9 share work).
      Orthogonal to my disk cache.
    * Convention migration `TR_M_AT_Q0 → canonical Wenzl-bridge
      y_λ` (commit `2dfd7c338`): replaces the legacy
      `schur_weyl_weight` (which vanishes on > 2-row partitions)
      with the canonical `y_λ` (full-rank, > 2-row contributions
      non-zero). My consumers already use the canonical path via
      `wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`
      — no breakage. The 2-row dominance finding (83-95%) is
      genuine empirical content under canonical y_λ; under legacy
      it would have been 100% by construction.
- **PR #617** (mass-table no-fits + 50dps cache + LP duals) —
  open; coordinated.
- **PR #618** (Wedderburn pair-vol LP/SDP-EW + alt-Δ_I Weinberg)
  — open; coordinated.

## Cross-references

- 1 ppb ledger: [`docs/coordination/1ppb.md`](../coordination/1ppb.md)
- ρ_K mass-table audit: [`docs/audits/2026-05-08-rho-k-mass-table-audit.md`](2026-05-08-rho-k-mass-table-audit.md)
- GAP-A-3 + GAP-A-4 guidance: [`docs/audits/2026-05-09-gap-a-3-a-4-guidance.md`](2026-05-09-gap-a-3-a-4-guidance.md)
- Path A verification (proton + deuteron): [`docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md`](2026-05-08-per-irrep-pole-18-21-research-note.md)
- Conjecture closure tractability: [`docs/audits/2026-05-09-conjecture-closure-tractability.md`](2026-05-09-conjecture-closure-tractability.md)
- T6 dissolution rationale: [`AUDIT-DEEP-2026-05.md` §3.3a](../../AUDIT-DEEP-2026-05.md) + [`atomic_braid_mass_terms.py:t6_canonical_MeV` docstring](../../computations/atomic_braid_mass_terms.py)
- Canonical recipe chains (PR #615): [`atomic-braid-recipe-{p,n,d,4he}-canonical.derivation.json`](../../computations/atomic-braid-recipe-p-canonical.derivation.json) + [`build_atomic_braid_recipe_canonical_chain.py`](../../computations/build_atomic_braid_recipe_canonical_chain.py)
- My superseded workplan: [`docs/audits/2026-05-05-markov-trace-axiomatic-workplan.md`](2026-05-05-markov-trace-axiomatic-workplan.md)
- My contributing PRs: [#534](https://github.com/litlfred/qou/pull/534) (axiomatic Markov-trace closed form), [#547](https://github.com/litlfred/qou/pull/547) (recursive reducer + multi-atom anchor), [#548](https://github.com/litlfred/qou/pull/548) (Δ_n² verification + T1 modes sweep)
