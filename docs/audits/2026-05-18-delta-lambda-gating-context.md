# Δ_λ — the gating R&D for per-isotope mass prediction (full context)

**Date:** 2026-05-18
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Audience:** any agent picking up Track A work; the 1ppb workplan v7 references this doc for the binding constraint.

## What Δ_λ is

The atomic mass formula at the order required for 1 ppb (Workplan v7 Track A) is

$$
\rho_K(q) \;=\; \rho_K^{\mathrm{LO}}(Z, N) \;+\; \frac{1}{|\mathrm{tr}_M(\beta_K)|}\sum_{\lambda \vdash 3A} y_\lambda(q)\, \chi^\lambda(\beta_K)\, \Delta_\lambda(K).
$$

- **ρ_K^LO** is the leading-order categorical density. It is **tautological** by
  construction (`ρ_K^LO = (Z·m_p + N·m_n) / (m_e · |tr_M|)`) and reproduces the
  additive constituent sum `Z·m_p + N·m_n`, i.e. **gives back the input AME-derived
  m_p, m_n** with zero binding energy.
- **y_λ(q)** is the Jones–Markov central coefficient — closed form, 50-dps cached
  for n=2..30 via Wenzl bridge (PR #695). No gate here.
- **χ^λ(β_K)** is the Hecke character of the atomic braid in irrep λ — computable
  via Hoefsmit at H_n ≤ 9, markov_peel at H_n ≤ 18, branching combiner at higher n
  (Track B). No structural gate.
- **Δ_λ(K)** is the **per-block binding-energy density** assigned to partition λ
  in the Wedderburn decomposition of the H_{3A} Markov trace. **This is the open
  R&D.** No closed-form derivation exists; multiple ansätze have all failed
  (see below).

## When Δ_λ is needed (and when it's not)

Δ_λ is **only** the gating quantity if Track A uses the **ρ_K · m_e · |tr_M|** formulation (Path D below). The framework has FOUR independent binding-energy paths; Δ_λ is needed by only one:

| Path | Formula | Independent gate(s) |
|------|---------|---------------------|
| **A. Direct trace** | `B = E_0 · (|tr_M(W_free)| − |tr_M(W_atom)|)` | E_0 calibration discipline (Q_β anchor) |
| **B. Borromean tower extension** | `m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)` | per-atom λ(K) substrate-derivation (#751 / #690 / #777) |
| **C. Kashaev volume law** | `B(K) = ρ_F · Vol_hyp(K)` | atom→knot assignment + ρ_F derivation |
| **D. ρ_K · m_e · |tr_M|** | `M = ρ_K · m_e · |tr_M|`, `ρ_K = ρ_K^{LO} + (1/|tr_M|) Σ y_λ χ^λ Δ_λ` | **Δ_λ (this document)** |

PR #564's T6-unit-convention resolution (`e578392b8`) declared **Path D canonical** ("no additive T6, Mittag–Leffler complementarity is the rigorous justification"). That declaration is what makes Δ_λ load-bearing for Track A. **Reverting Path D in favour of Path B (Borromean tower extension)** would bypass the Δ_λ gate at the cost of opening the per-atom λ(K) derivation problem — which the framework is already working on for individual baryons (#751).

The non-tautological binding-energy prediction under **Path D** is

$$B(K) \;=\; m_e \cdot \sum_{\lambda \vdash 3A} y_\lambda(q_0)\, \chi^\lambda(\beta_K)\, \Delta_\lambda(K).$$

For deuteron (Z=1, N=1, A=2, n=6, 11 partitions of 6):

- Empirical target: `target_signed = -B_D / m_e = -4.353` (in m_e units)
- y_λ(q_0) and χ^λ(β_D) cached at 50 dps — known
- Δ_λ(D) for each λ ⊢ 6 — **not derived**, underdetermined system
  (1 equation in 11 unknowns)

**Without Δ_λ values, the binding prediction is undefined** — the
`binding-K-direct.witness.json` reports `status: "delta_lambda_unavailable"`
for D / T / ³He / ⁴He.

## Closure attempts (six ansätze, all failed)

Per `docs/audits/2026-05-09-mass-table-fitting-audit.md` and the
2-row stratum tabulation (`delta-lambda-empirical-tabulation.witness.json`,
PR #619):

| Option | PR | Selector | Outcome on D |
|--------|----|---------|--------------|
| **A** Occam single-support | (legacy `rho_k_h3a_refinement.py`) | min \|Δ\| over single-partition solutions | underdetermined; picks λ=[5,1] with Δ=-22.96; arbitrary criterion |
| **B** Frobenius co-Casimir 1/dim_q(λ) | [#602](https://github.com/litlfred/qou/pull/602) | theorem-forced (no free params) | **fails** — residual −2.30 MeV (wrong sign, vortex-blind) |
| **C** Demazure-fibre y_λ·D_w/D_w₀ | (sibling, e77a4b4d) | from 5/8 Demazure functional | **fails** — Δ_λ ~10⁻⁵; reproduces M_LO tautologically |
| **D-Plancherel** LP shadow price | [#603](https://github.com/litlfred/qou/pull/603) | LP dual minimising Σ\|Δ_λ\|·w_λ | reproduces Occam exactly (L∞ = 1.91e-15); shifts underdetermination from value choice to cost choice |
| **D-Frobenius** LP shadow price | [#603](https://github.com/litlfred/qou/pull/603) | alt LP cost | picks different singleton (λ=[6], Δ=-47.16); same problem |
| **E** crystal-graph weight | (in flight, uses PR #599/#601) | Kashiwara crystal at q→1 | **TBD** |
| **F** Wenzl-bridge augmented Markov | (in flight) | augment Markov axioms with B-energy datum | TBD (closure-pickle bug on first attempt) |

Additional empirical ansätze from the 2-row stratum tabulation (PR #619,
deuteron row):

| Ansatz | Result |
|--------|--------|
| `a_single_block` (best partition only) | best λ=[5,1], δ=-22.96; off-target by 5.3× |
| `b_shell_supported` (λ=[3,2,1]) | δ=301.5; off-target by 69× |
| `c_content_monotonic` (linear in content) | norm_δ_2 = 31.97; mismatched |
| `d_isotypic` (Plancherel weighting) | norm_δ_2 = 71.63; mismatched |

**None reach the empirical target -4.353 within a factor of 5×.**

## Why every ansatz fails (the diagnosis)

Per the mass-table-fitting audit's "honest verdict":

> The Δ_λ closed form in the paper is correct at the formal level, but
> M_λ(K) (the per-block mass-functor component) is defined by the
> *Archimedean realization functor's* per-block action, which has no
> derived structural rule yet.

In framework language: **GAP-A-3** (brane-tower level selection) and
**GAP-A-4** (ρ general rule, `conj:rho-prefactor-structural`) — these
two open conjectures together specify what Δ_λ *should* be, but neither
has a categorical proof.

Each B / C / D / E / F ansatz supplies a *heuristic* model for M_λ(K);
none is the "correct" categorical answer.

## Impact on 1ppb workplan v7

| Track | Gated on Δ_λ? | Status |
|-------|--------------|--------|
| **L1 compute precision** | No — independent of Δ_λ | trivially met |
| **L2 Q_β (CAL-3 anchor)** | No — uses single-wrap symbolic form | misses 100× target by 263×; closure path is brane-tower truncation residual, **not** Δ_λ |
| **L2 Δm_pn (m_n − m_p)** | No — uses Borromean tower λ_p, λ_n | misses 100× target by 64×; closure path is λ_scale substrate-derivation, **not** Δ_λ |
| **L2 μ mass** | No — uses figure-8 volume formula | misses 100× target by 6.5×; closure path is brane-tower truncation, **not** Δ_λ |
| **L2 absolute m_p, m_n** | No — same Borromean path as Δm_pn | below CAL-2 floor (research-grade) |
| **L2 binding energies B_D, B_T, B_³He, B_⁴He** | **YES** | gated until Δ_λ closure |
| **Track A.1 (D binding)** | **YES** | blocked |
| **Track A.2-4 (T, ³He, ⁴He bindings)** | **YES** | blocked |
| **Track B (recursive ρ_ξ for branching combiner)** | No — pure operator-algebra | **unblocked, in scope this branch** |
| **Track C (Layer 3 hybrid α-cluster)** | YES indirectly — uses Track A formula | downstream |

## What this branch can do without Δ_λ closure

1. **Track B implementation** — recursive ρ_ξ for A=3, 4 via direct
   matrix evaluation at H_{3(A-1)}. Unblocks fast |tr_M| for ⁴He
   (vs 22 min markov_peel). **In scope this branch.**

2. **L2 verification** — push the Borromean tower / muon /
   Δm_pn predictions against the per-observable 100× targets,
   document the closure path for each.

3. **Document Δ_λ gate** in the workplan and per-observable status
   so future agents see the binding constraint clearly. (This doc.)

## What needs to happen for Δ_λ closure

The "honest verdict" in the audit points at the Archimedean realization
functor. Three candidate research directions:

1. **Resolve GAP-A-3 / GAP-A-4 jointly.** The brane-tower level selector
   `conj:brane-tower-z-habiro` was *closed by refutation* on this branch's
   predecessor (PR #638) — no single scalar n_⋆ rule works. The
   structural alternative is a per-partition selector, which is exactly
   what Δ_λ encodes. So GAP-A-3 and Δ_λ are the same problem.

2. **Demazure / KLR canonical basis with explicit q→1 limit.** Option E
   (Kashiwara crystal) is in flight; its expected output is a closed-form
   Δ_λ from the crystal graph.

3. **Augmented Markov-trace axioms.** Option F adds a new axiom to the
   Markov trace (binding-energy normalisation); this is a *physics input*
   that fixes Δ_λ but does not derive it.

## Recommendation

Do **not** attempt a 7th Δ_λ ansatz on this branch without first reviewing
the failure mode of Options A–F. Each ansatz that "closes numerically against
AME" is by construction a fit, not a derivation, and gets caught by the
three-calibration discipline review.

The productive path on this branch is **Track B (recursive ρ_ξ)**, which
unblocks fast canonical compute for A≥3 atoms and so makes future Δ_λ
verification work (when a candidate ansatz is proposed) immediately
testable across all light atoms.

## Cross-references

- [`docs/audits/2026-05-18-1ppb-workplan-v7-100x-experimental.md`](2026-05-18-1ppb-workplan-v7-100x-experimental.md) — current workplan
- [`docs/audits/2026-05-09-mass-table-fitting-audit.md`](2026-05-09-mass-table-fitting-audit.md) — original Δ_λ closure-attempt summary
- [`docs/precision-goals.md`](../precision-goals.md) — two-leg precision target
- [`computations/binding_K_direct.py`](../../computations/binding_K_direct.py) — the binding formula (reports `delta_lambda_unavailable`)
- [`computations/delta-lambda-empirical-tabulation.witness.json`](../../computations/delta-lambda-empirical-tabulation.witness.json) — 2-row stratum tabulation
- [`content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md) — Δ_λ formal definition
- [`content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.md`](../../content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.md) — GAP-A-4
- [`content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md) — GAP-A-3 / GAP-A-4

---

## Update (2026-05-26): claimed Δ_λ deuteron closure — **RETRACTED 2026-05-29**

> **CORRECTION (2026-05-29).** The "closure achieved" claim in this
> section is **overclaimed**. Evaluated live at 50 dps, the per-λ formula
> `B = m_e·|Σ_λ y_λ·χ^λ·sgn(w₀)·f^λ|` undershoots **every** light
> isotope — including the deuteron — by a large margin
> (`delta-lambda-binding-full-evaluation.witness.json`):
>
> | atom | B_pred (MeV) | B_AME (MeV) | err |
> |------|------|------|-----|
> | D    | 0.380 | 2.225 | **−82.9%** |
> | T    | 1.908 | 8.482 | −77.5% |
> | ³He  | 2.344 | 7.718 | −69.6% |
> | ⁴He  | 3.038 | 28.296 | −89.3% |
>
> The "**zero free parameters**" label is false. `binding_energy_categorical_deuteron.py`
> only reaches the AME deuteron value via `C_knot = 5.852`, which it
> computes *as* `B_AME / (m_e·|sum|)` — a factor **fitted to AME**, not
> eliminated. The claim below that C_knot "was an artifact already encoded
> in χ^λ(β_D) via the interface operator" is contradicted by the full
> evaluation: it **uses the interface-inclusive** χ^λ
> (`atom-chi-rust-d.witness.json`, `include_inter=True`) and still gives
> −82.9%. The genuine zero-parameter deuteron closure is the **scalar**
> endomorphism `B = m_e·Vol(𝓑₃)·Δtr = +0.19%` (Vol = 8G derived) — **not**
> the per-λ Δ_λ formula. **The Δ_λ gate remains open for all A, including
> the deuteron.** See sibling PR #1416 (binding-scale de-fit) and
> `binding_log_scale_investigation.py`. The dated text below is retained
> as a record of the retracted claim.

**PRs #1292, #1296, #1305 (all merged) + branch `claude/c-knot-geom-2026-05-26`.**

The Δ_λ gating problem is resolved for the deuteron:

    B(D) = m_e × |Σ_λ y_λ · χ^λ(β_D) · sgn(w_0^{S_{λ'}}) · f^λ|

Every factor is computed — **claimed** zero free parameters (FALSE — see CORRECTION above):

| Factor | Source | Status |
|--------|--------|--------|
| y_λ (Wenzl) | `y_lambda_wenzl_bridge.py` | COMPUTED (on disk) |
| χ^λ(β_D) | `atom-chi-rust-d.witness.json` | COMPUTED (includes interface) |
| sgn(w_0^{S_{λ'}}) | Macdonald I.1.5 | PROVED (PR #1305) |
| f^λ = dim(V_λ) | Hook-length formula (Burnside) | PROVED (PR #1305) |

The "C_knot" geometric factor that appeared in earlier probes was an
artifact of using the disjoint product χ^λ(β_p ⊗ β_n) instead of
the full character χ^λ(β_D). The interface operator's effect is
already encoded in χ^λ(β_D) via the branching witness.

**Remaining:** Extend to T, ³He (H_9 branching exists), ⁴He (needs
H_12 branching — feasible in ~30 min).

**The six prior failed ansätze** (Frobenius co-Casimir, Demazure,
LP-Plancherel, LP-Frobenius, crystal, augmented Markov) all
failed because they tried to derive Δ_λ from single-nucleon data
or from q-dependent algebraic expressions. The correct Δ_λ is
categorical (q-independent: sign × dimension) and the q-dependent
geometric correction lives inside χ^λ via the interface operator.
