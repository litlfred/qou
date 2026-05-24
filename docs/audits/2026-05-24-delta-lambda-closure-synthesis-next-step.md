# Δ_λ closure — synthesis of 6+ failed ansätze + next-step proposal

**Date:** 2026-05-24
**Author:** session sweep (post `respects_archimedean_wall` 74→0 drain)
**Audience:** next agent picking up Track A / 1ppb work
**Trigger:** User direction (2026-05-24): "*focus here — Δ_λ closure unlocks the per-isotope binding chain*"
**Companion:** `docs/audits/2026-05-18-delta-lambda-gating-context.md` (canonical reference)

## TL;DR

The per-block binding density Δ_λ(K) is the Track A gating quantity for
1 ppb per-isotope mass prediction (Path D, `M = ρ_K · m_e · |tr_M|`).
Six structural ansätze + 14 closure-v* compute witnesses have all
failed to reach the deuteron target `−4.353 ± 0` (in m_e units) within
a factor of 5×. Per CLAUDE.md, a 7th fit-based ansatz is explicit
anti-pattern; the productive directions are GAP-A-3 (categorical
brane-tower level selection), GAP-A-4 (ρ general rule
`conj:rho-prefactor-structural`), and Option E (Kashiwara crystal
canonical-basis Markov-trace formula).

This doc:

1. **Synthesizes** the 14 prior closure attempts in one table.
2. **Identifies** four structural constraints that have NOT been
   jointly imposed in any prior attempt.
3. **Proposes** three small-scope, testable single-session probes
   that each impose ONE structural constraint and report whether
   the closure tightens — providing concrete diagnostic data for
   the GAP-A-3 / GAP-A-4 / Option E categorical work that follows.
4. **Recommends** a research-grade sequence (weeks-scale work) for
   discharging Option E once the diagnostic probes have constrained
   the design space.

## 1. State of Δ_λ closure (2026-05-24)

### 1.1 The Path D formula (binding-K direct, the gating site)

$$
B(K) \;=\; m_e \cdot \sum_{\lambda \vdash 3A} y_\lambda(q_0) \cdot \chi^\lambda(\mathcal{B}_K) \cdot \Delta_\lambda(K),
$$

with the empirical target for each atom $K$:

$$
\text{target}_K \;:=\; -\frac{B_K^{\mathrm{AME}}}{m_e} \;=\; \sum_\lambda c_\lambda^{(K)} \cdot \Delta_\lambda(K),
\quad c_\lambda^{(K)} := y_\lambda(q_0) \cdot \chi^\lambda(\mathcal{B}_K).
$$

Per `delta-lambda-empirical-tabulation.witness.json` (PR #619):

| atom | A  | n = 3A | n_partitions | target_signed (m_e units) | ΔM (MeV) |
|------|---:|-------:|-------------:|---------------------------|---------:|
| p    |  1 |    3 |  3 | (constituent — tautological) | 0.000 |
| n    |  1 |    3 |  3 | (constituent — tautological) | 0.000 |
| D    |  2 |    6 | 11 | **−4.353** | −2.225 |
| T    |  3 |    9 | 30 | (TBD — partial χ at H₉) | −8.482 |
| ³He  |  3 |    9 | 30 | (TBD) | −7.718 |
| ⁴He  |  4 |   12 | 77 | (TBD) | −28.296 |

Deuteron is the canonical test target: 11 unknowns, 1 equation,
trivially underdetermined → needs ≥ 10 additional structural
constraints to close.

### 1.2 Closure attempts so far (14 witnesses)

| # | Ansatz | Witness | Result on D | Anti-pattern? |
|---|--------|---------|-------------|---------------|
| 1 | **A** Occam single-support (`a_single_block`) | `delta-lambda-empirical-tabulation` | picks λ=[5,1], Δ=−22.96 (5.3× off); arbitrary | fit-like |
| 2 | **B** Frobenius co-Casimir 1/dim_q(λ) | (PR #602) | residual −2.30 MeV, wrong sign | structural |
| 3 | **C** Demazure-fibre $y_\lambda·D_w/D_{w_0}$ | (sibling `e77a4b4d`) | Δ_λ ∼ 10⁻⁵; reproduces M_LO tautologically | structural |
| 4 | **D-P** Plancherel LP shadow | (PR #603) | reproduces Occam exactly (L∞ = 1.91e−15) | LP-objective fit |
| 5 | **D-F** Frobenius LP shadow | (PR #603) | picks λ=[6], Δ=−47.16; arbitrary | LP-objective fit |
| 6 | `b_padded_staircase` (λ=[3,2,1]) | `delta-lambda-empirical-tabulation` | δ=301.5 (69× off) | fit-like |
| 7 | `c_content_monotonic` (Δ_λ = α·c(λ)) | `delta-lambda-empirical-tabulation` | norm_δ₂ = 31.97; mismatched | structural |
| 8 | `d_isotypic` (Δ_λ = α/dim_q(λ)) | `delta-lambda-empirical-tabulation` | norm_δ₂ = 71.63; mismatched | structural |
| 9 | **v2** combined-pole filter | `delta-lambda-closure-v2-combined-pole` | non-convergent | structural |
| 10 | **v3** crystal-shift-max filter vs unfiltered | `delta-lambda-closure-v3-full-vs-filtered` | non-convergent | structural |
| 11 | **v4** 2-row stratum restriction | `delta-lambda-closure-v4-two-row` | non-convergent | structural |
| 12 | **v5** Frobenius–chirality categorical Δ_λ(K) = χ^λ(β·β_mirror⁻¹) | `delta-lambda-closure-v5-frobenius-chirality` | all 4 atoms report None ratios | structural |
| 13 | **2-row stratum** Δ_λ tabulation | `delta-lambda-2row-stratum` | underdetermined | structural |
| 14 | **categorical-verification** Δ_λ residue via circle | `delta-lambda-categorical-verification` | implementation-incomplete | structural |
| (a) | **E** crystal-graph weight (Option E) | (in flight — Kashiwara) | **TBD** | structural |
| (b) | **F** Wenzl-bridge augmented Markov | (in flight) | TBD (closure-pickle bug) | structural |
| (c) | **JSJ-decomposition Δ_λ phase 3** | `delta-lambda-jsj-phase3` | non-convergent | structural |
| (d) | **q-sweep 2-row** | `delta-lambda-q-sweep-2row` | diagnostic only | n/a |
| (e) | **shift-NF Wenzl probe** | `delta-lambda-shift-nf-wenzl-probe` | diagnostic only | n/a |
| (f) | **two-factor Phase 2** | `delta-lambda-two-factor-phase2` | non-convergent | structural |
| (g) | **z4N Phase 4** | `delta-lambda-z4N-phase4` | non-convergent | structural |
| (h) | **FR-identity Phase 5c** | `delta-lambda-fr-identity-phase5c` | non-convergent | structural |
| (i) | **full-variance Phase 5e-1** | `delta-lambda-full-variance-phase5e-1` | non-convergent | structural |
| (j) | **per-partition shift-NF** | `delta-lambda-via-per-partition-shift-nf` | non-convergent | structural |

**Diagnosis (from `2026-05-09-mass-table-fitting-audit.md`):** the
Δ_λ closed form in the paper is correct at the formal level, but
$M_\lambda(K)$ (the per-block mass-functor component) is defined by
the *Archimedean realization functor's* per-block action, which has
**no derived structural rule yet**. Each ansatz supplies a heuristic
model; none is the correct categorical answer.

## 2. Structural constraints NOT YET jointly imposed

A pattern across the 14 failed attempts: each imposes ONE structural
hypothesis (single-block, content-monotonic, Plancherel weighting,
crystal-shift filter, 2-row restriction, mirror-chirality, JSJ phase,
…). **None has jointly imposed multiple categorical structures whose
intersection would tighten the underdetermined system.**

Four structural constraints derivable from canonical framework
machinery, none of which appear in the existing closure-v* scripts:

### 2.1 Bar-involution invariance (Type-B folding, CLAUDE.md §7b)

Under the bar involution $q \leftrightarrow q^{-1}$, the Type-B fold
of the $\mathfrak{sl}_n$ Cartan datum gives a symmetric crystal whose
GS normal forms are bar-invariant by construction. For Δ_λ this
suggests:

$$
\Delta_\lambda(K) \;=\; \Delta_{\lambda^T}(K)
$$

where $\lambda^T$ is the transpose (conjugate) partition. For
deuteron (n = 6), the 11 partitions pair as:

```
  [6] ↔ [1,1,1,1,1,1]        — 1 pair → 1 constraint
  [5,1] ↔ [2,1,1,1,1]         — 1 pair → 1 constraint
  [4,2] ↔ [2,2,1,1]           — 1 pair → 1 constraint
  [4,1,1] ↔ [3,1,1,1]         — 1 pair → 1 constraint
  [3,3] ↔ [2,2,2]             — 1 pair → 1 constraint
  [3,2,1] ↔ [3,2,1]           — self-conjugate, 0 constraints
```

5 pair constraints + 1 target equation = **6 equations in 11 unknowns**
→ 5 free dimensions remaining. Still underdetermined, but tighter
than 10 free.

### 2.2 Joint multi-atom consistency

If Δ_λ is a UNIVERSAL function of λ (no K-dependence) within
isobars, then D, T, ³He, ⁴He targets give 4 simultaneous equations.
However, atoms have different n = 3A → different partition sets;
the universal hypothesis only makes sense after CONTENT-projection
or REPRESENTATION-projection (e.g. via the branching rule
$\Lambda_n \hookrightarrow \Lambda_{n-1}$).

Concretely: if Δ_λ depends only on the *content sequence* $c(\lambda)$
(not on $\lambda$ itself), then multiple atoms with overlapping
content sequences add joint constraints. For deuteron + tritium:

- D partitions ⊢ 6: contents in $\{[5,3,1,-1,-3,-5], \ldots\}$
- T partitions ⊢ 9: contents in $\{[8,6,4,2,0,-2,-4,-6,-8], \ldots\}$

The overlap in content space could yield ~3-5 joint constraints.

### 2.3 Hook-length integrality

If $\rho(\mathfrak{H}) = \mathrm{round}[\dim_q(\lambda^*)]$ per
`conj:rho-prefactor-structural` (GAP-A-4), then Δ_λ for the
*dominant* $\lambda^*$ must satisfy

$$
y_{\lambda^*}(q_0) \cdot \chi^{\lambda^*}(\mathcal{B}_K) \cdot \Delta_{\lambda^*}(K) \;\approx\; \text{target}_K \cdot \frac{\text{round}[\dim_q(\lambda^*)] - 1}{\text{round}[\dim_q(\lambda^*)]}
$$

(the round-down term captures the "background" from the ρ_K^LO
constituent piece). This isn't a closure of Δ_λ for non-dominant λ,
but pins the **leading-order** Δ_{λ*} once $\lambda^*$ is identified.

### 2.4 Kazhdan–Lusztig classical-limit ⇒ integer Δ_λ

Per `conj:kazhdan-lusztig-classical-limit` + Option E reduction 3:
the brane-tower divergence is regularised by the KL functor sending
each canonical basis $b_w$ to $C_w \in \mathbb{Z}[S_n]$. This
suggests Δ_λ at $q_0$ should be expressible as an **integer
combination of canonical-basis traces** $\chi^{KL}_\lambda$, modulo
the y_λ Wenzl-bridge normalisation. Concretely:

$$
\Delta_\lambda(K) \;\stackrel{?}{=}\; \frac{1}{y_\lambda(q_0)} \cdot \sum_{w \in S_n} n^w_\lambda(K) \cdot \chi^{KL}_w(q_0 \to 1), \qquad n^w_\lambda(K) \in \mathbb{Z}.
$$

This is the **Option E** ansatz in full generality; the integer-
coefficient constraint is the substantive new structure.

## 3. Three proposed single-session diagnostic probes

Each probe imposes ONE of the structural constraints above and
reports whether the joint system tightens. **None of these is a
7th fit-based ansatz** — each imposes a categorical structure
derivable from framework primitives.

### 3.1 Probe-1: bar-invariance LP

```python
# folio-assistant/computations/delta_lambda_bar_invariance_probe.py
# Solves: min ||Δ||_2  s.t.
#   Σ_λ c_λ^(D) · Δ_λ = target_D
#   Δ_λ = Δ_{λ^T} for all λ ≠ λ^T   (5 pair constraints for D)
```

**Diagnostic value:** if the min-||Δ||_2 solution under bar-invariance
matches the empirical Δ_λ values implied by ANY of the categorical
ansätze (B-Frobenius, C-Demazure, …), bar-invariance is consistent
with that ansatz. If no ansatz matches, bar-invariance is an
independent constraint and the joint imposition narrows the design
space.

### 3.2 Probe-2: joint multi-atom under content projection

```python
# folio-assistant/computations/delta_lambda_joint_content_probe.py
# Solves: min ||Δ_c||_2  s.t.
#   Σ_λ c_λ^(D) · Δ_{c(λ)} = target_D       (1 eq)
#   Σ_λ c_λ^(T) · Δ_{c(λ)} = target_T       (1 eq, if χ^λ at H₉ available)
#   Σ_λ c_λ^(³He) · Δ_{c(λ)} = target_³He   (1 eq, same)
# Unknowns: Δ_c indexed by distinct content sequences across atoms.
```

**Diagnostic value:** if the content-indexed Δ_c has many fewer
distinct values than partitions, the system is far more constrained
than the per-partition system. If the joint system has no
solution, the content-projection hypothesis is falsified.

### 3.3 Probe-3: hook-length dominant-λ pin

```python
# folio-assistant/computations/delta_lambda_dominant_pin_probe.py
# Identify λ*(D) via |y_λ · χ^λ| max
# Compute Δ_{λ*}(D) under GAP-A-4 (ρ = round(dim_q(λ*)))
# Solve residual system for non-dominant Δ_λ under min-||·||_2
```

**Diagnostic value:** tests whether the dominant-λ pin (already
half-derivable from `conj:rho-prefactor-structural`) is consistent
with the empirical target, and whether the non-dominant residual
admits a small-norm solution (consistent with the
"non-dominant Δ_λ is suppressed" intuition).

## 4. Research-grade Option E sequence (weeks-scale, NOT this session)

If the three probes above narrow the design space sufficiently, the
Option E (Kashiwara crystal) infrastructure can be built incrementally:

1. **Implement crystal-vertex enumerator** at height 6 for n = 6
   (deuteron's 11 partitions → finite set of crystal vertices).
2. **Compute the Brundan–Kleshchev image** of each partition λ ⊢ 6
   in the KLR algebra R^Λ_α with α the deuteron weight.
3. **Build the canonical-basis trace** $\chi^{KL}_w$ at $q_0 \to 1$
   for each KL basis $b_w \in R^Λ_α$.
4. **Test the integer-combination conjecture** $\Delta_\lambda = \frac{1}{y_\lambda} \sum_w n^w_\lambda \chi^{KL}_w$
   against the (bar-invariant + dominant-pin) constrained system from
   the probes.

Each step is single-PR scope; the sequence is ~weeks of substrate
math + Lean formalisation per CLAUDE.md `compute-author` skill.

## 5. Anti-patterns to avoid (CLAUDE.md + 1ppb-compute-tranche-queue)

- Do **not** introduce a 7th fit-based ansatz (e.g. Δ_λ as polynomial
  in q with free coefficients chosen to match deuteron). The Δ_λ
  closure must come from categorical structure, not from optimising
  fit quality.
- Do **not** drop CAL-3 (Q_β as input). Per author direction
  (2026-05-08), CAL-3 is the standing baseline; "derive Q_β" is
  the Subgoal-2 research-grade question that's been explicitly
  declined.
- Do **not** silently extend the Δ_λ formula to add free
  per-knot terms — that's the path back to ρ_K^LO + ad-hoc K
  corrections (Path A in `2026-05-18-delta-lambda-gating-context.md`),
  which loses Path D's categorical motivation.
- Do **not** treat the v5 (chirality) closure's "None ratios" as
  conclusive. The v5 script may need a different input
  configuration; the structural ansatz (per-(K, λ) Δ_λ via
  mirror-twist) might still be viable.

## 6. Recommendation

The most useful next single-session contribution is **probe-1
(bar-invariance LP)**, because:

- The structural constraint Δ_λ = Δ_{λ^T} is derivable from
  CLAUDE.md §7b (Type-B folding) — no new categorical assumption.
- The LP setup is mechanical (existing `lp_dual_solver.py`
  infrastructure).
- The result is diagnostic regardless of outcome: a positive
  result tightens the design space, a negative result falsifies
  bar-invariance and rules out the Type-B fold as an unconstrained
  closure mechanism.

Probe-2 and probe-3 are sequential follow-ups once probe-1's
diagnostic is in hand.

The full Option E sequence (§4) is weeks-scale substrate math +
Lean formalisation, NOT a single-session task. CLAUDE.md
`compute-author` skill mandates the algebraic-preflight + cross-
check discipline for any new compute touching this area.

## 7. Related

- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — canonical reference
- [`docs/precision-goals.md`](../precision-goals.md) — L1 / L2 split
- [`docs/coordination/1ppb.md`](../coordination/1ppb.md) — coord ledger
- [`docs/coordination/1ppb-categorical-chain.md`](../coordination/1ppb-categorical-chain.md) — categorical-chain status
- [`docs/coordination/1ppb-compute-tranche-queue.md`](../coordination/1ppb-compute-tranche-queue.md) — anti-patterns + tranche queue
- [`conj:rho-prefactor-structural`](../../content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.md) — GAP-A-4
- [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/braids-and-knots/conj-crystal-graph-realization.md) — Option E foundation
- [`conj:kazhdan-lusztig-classical-limit`](../../content/quantum-observable-universe/archimedean-universe/kazhdan-lusztig-classical-limit.md) — Option E regularisation
- [`crystal-basis-resolves-mass-tower-open-problems`](../../content/quantum-observable-universe/archimedean-universe/crystal-basis-resolves-mass-tower-open-problems.md) — Option E proposition
- PR #1127 — Q_β net-ansatz fitting finding (sibling, HIGH-overlap)
