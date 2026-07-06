# α/(4π) — RT 2-loop categorical derivation plan

**Created:** 2026-05-30
**Status:** research-grade, multi-week project
**Prerequisite:** subgoal-1 closure (`em-coupling-bring-zero-mode.md`
update from #1484/#1489)

## Purpose

Provide the **rigorous categorical derivation** of the empirical form
established in PR #1484:

$$\alpha_{EM}^{-1} = q\,[9]_q\,[10]_q + \frac{2}{3\pi} + \alpha_{EM} \cdot \frac{[2]_q}{8\pi} \cdot (1 - h^2 \alpha_{EM}) + O(\alpha^2)$$

Subgoal-1 (achieved to CAL-2 floor per #1489) treats this as a
phenomenological identity. Subgoal-2 (this plan) upgrades it to a
**proven structural identity** by computing each piece from the QOU
categorical Lagrangian via Reshetikhin-Turaev shadow-world calculus.

## Already proven (in framework)

- **Tree term** `q·[9]_q·[10]_q`: `prop:em-coupling-projection`
  (singlet idempotent trace squared over force-carrier complexity).
- **Bring zero-mode shift** `2/(3π)`: `prop:em-coupling-bring-zero-mode`
  (Hodge / Gauss-Bonnet ratio + sphere-volume ratio, PR #1444 merged).

## To be derived (this plan)

Two structural identities:

**Identity 1 (1-loop self-energy coefficient):**
$$F_1 := \frac{[2]_q}{8\pi} = \frac{[2]_q}{\pi \cdot \dim H^1(M_{\text{Bring}})}$$

**Identity 2 (Schwinger correction):**
$$F_2 := -h^2 \cdot \alpha_{EM} \quad (\text{coefficient of } \alpha_{EM}^2 \cdot H)$$

## Identity 1: RT 1-loop self-energy

### Required categorical objects

| Object | What it is | Source |
|---|---|---|
| `M_Bring` | Genus-4 closed hyperbolic surface | `force-carrier-bring-uniqueness` |
| `(C, A, τ)` | Descartes universe over R | `em-coupling-projection` |
| `e_-` | Singlet idempotent in End(A⊗A) | `em-spectral-completeness` |
| `V_F` | Fundamental SU_q(2) representation | (new — to be defined) |
| `dim_q(V_F) = [2]_q` | Quantum dimension of V_F | Standard Hecke |
| `H¹(M_Bring; ℝ)` | First cohomology of M_Bring (dim 2g = 8) | Standard topology |

### Required calculation

The 1-loop self-energy correction to the singlet idempotent's
τ-trace, computed as a Markov-trace insertion in RT shadow-world:

$$\Delta_{1\text{-loop}}(|\text{tr}_\tau(e_-)|^2) = \alpha_{EM} \cdot \frac{[2]_q}{8\pi}$$

**Concrete categorical statement:**

> Let M_Bring → BG be the classifying map. Let V_F ∈ Rep(SU_q(2)) be
> the fundamental representation. Then the categorical 1-loop
> self-energy correction to the photon propagator, computed as the
> RT shadow-world trace of a closed V_F-strand inserted in the
> photon line on M_Bring, equals
>
> $$\Delta = \alpha_{EM} \cdot \frac{\dim_q(V_F)}{\pi \cdot \dim H^1(M_{\text{Bring}}; \mathbb{R})}$$

### Sub-claims to prove

1. **(C1.1)** The categorical photon-fermion-photon vertex factor is
   `Q_q(matter) = [w(K_m)]_q` (per `em-coupling-projection.md` Layer 1).
   For a fundamental fermion (matter loop of writhe 1), this gives `Q_q(V_F) = [1]_q = 1`.
2. **(C1.2)** The Markov-trace closure of a fundamental fermion loop
   inserted between two photon vertices contributes `dim_q(V_F) = [2]_q`.
3. **(C1.3)** The shadow-world measure on the photon zero-mode
   subspace of `End(A⊗A)` gives a `1/(π · dim H¹(M_Bring))` factor
   (parallel to the leading `1/Area = 1/(4π(g-1))` of the zero-mode shift).
4. **(C1.4)** No UV divergence: the categorical sum is finite by RT
   shadow-world finiteness (force-carrier complexity `[9]_q · [10]_q`
   acts as IR/UV regulator).

### What needs new framework infrastructure

- **(I1.1)** A definition `EmFermionLoop : C → C` representing the
  categorical fermion loop in Rep(SU_q(2)).
- **(I1.2)** A definition `RtShadowWorldMeasure` on
  `End_C(A⊗A)`'s zero-mode subspace.
- **(I1.3)** A Lean class `RtOneLoopSelfEnergy` axiomatising the
  identity, with the 4 sub-claims as fields (per §3b-cond
  conditional-class pattern).

## Identity 2: Schwinger correction

### Required calculation

The 2-loop self-energy correction (two fermion-loop insertions on
the photon line) computed as a Markov-trace product:

$$\Delta_{2\text{-loop}} = -\alpha_{EM}^2 \cdot h^2 \cdot \frac{[2]_q}{8\pi}$$

The `h² = (q - q⁻¹)²` factor enters because:
- Each vertex contributes a single `(q - q⁻¹)` insertion (the Hecke
  quadratic identity `σ² = h·σ + 1` evaluated on the matter strand).
- Two vertices give `h²`.
- The `α²` comes from two Q_q charge insertions (each contributing α).

### Sub-claims to prove

1. **(C2.1)** The 2-vertex Hecke quadratic structure contributes
   `h²` at each vertex pair. Sum over 2-loop topologies gives the
   structural `h²` factor.
2. **(C2.2)** UV finiteness extends to 2-loop (same RT shadow-world
   argument).
3. **(C2.3)** Sign of -h²·α follows from the Hecke quadratic
   identity in the antisymmetric (singlet) channel.

### What needs new framework infrastructure

- **(I2.1)** Extension of `EmFermionLoop` to multi-loop insertions.
- **(I2.2)** Lean class `RtTwoLoopSelfEnergy` extending
  `RtOneLoopSelfEnergy` with the h² coefficient identification.

## Estimated effort

| Phase | Description | Effort |
|---|---|---|
| Phase 1 | Define `EmFermionLoop` + verify against H_3 matter probes (#1466) | 1-2 weeks |
| Phase 2 | Define `RtShadowWorldMeasure`, prove (C1.3) | 1-2 weeks |
| Phase 3 | Prove Identity 1 (C1.1-C1.4) | 1 week |
| Phase 4 | Prove Identity 2 (C2.1-C2.3) | 1-2 weeks |
| Phase 5 | Lean formalization (`RtOneLoopSelfEnergy`, `RtTwoLoopSelfEnergy` classes) | 1 week |
| Phase 6 | Conditional-on-class theorem for full cubic identity | 0.5 week |

**Total: 5-7 weeks.**

## Dependencies and constraints

- Must NOT modify the canonical derivation chain
  (`docs/canonical-derivation-cheat-sheet.md`) without owner approval.
- Must NOT introduce empirical CAL-4 calibration (the framework's
  3-calibration discipline forbids it; see AGENTS.md "Precision goals").
- Per `prop:em-coupling-bring-zero-mode` lines 191-205: the rigorous
  derivation requires items 1-4 (3-manifold identification, photon
  zero-mode computation, UV finiteness, 2-loop self-energy). This
  plan extends those 4 items with specific numerical checkpoints
  from #1487.

## Numerical checkpoints (for verification at q_0, 50 dps)

When implemented, each sub-claim must hit:

| Quantity | Expected value at q_0 |
|---|---|
| `dim H¹(M_Bring)` | 8 (integer) |
| `[2]_q at q_0` | 2.010886... |
| `[2]_q / (8π)` | 0.080011... |
| 1-loop coefficient `α · [2]_q/(8π)` | 5.838e-4 |
| `h²` at q_0 | 0.043706... |
| Schwinger factor `-h²·α` | -3.189e-4 |
| Full next-order `α·[2]_q/(8π)·(1-h²·α)` | 5.821e-4 |
| α_EM⁻¹ via cubic solve | 137.035999127 |
| CODATA α_EM⁻¹ | 137.035999084 |
| Residual | +0.31 ppb (CAL-2 limit) |

## Out of scope

This plan addresses **subgoal-2 research-grade** derivation. It does
NOT address:
- Substrate-derivation of q_0 itself (declared out of scope per
  coordination ledger 2026-05-08).
- Absolute α_EM precision below CAL-2 floor (~150 ppb propagated).
- Modifications to the 3-calibration discipline.

Subgoal-1 (100× σ_exp consistent with achieved) is closed via
#1484+#1489+#1491 already; this plan is the rigorous follow-up.

## Reviewer notes

- This is a **plan**, not a derivation. Reviewing it should focus on
  whether the sub-claims are well-posed and whether the numerical
  checkpoints are correct.
- The actual derivation is the multi-week implementation; this doc
  scopes it.
- If pursued, each phase should land as a separate PR with its
  sub-claims as conditional-on-class lemmas (§3b-cond pattern).
