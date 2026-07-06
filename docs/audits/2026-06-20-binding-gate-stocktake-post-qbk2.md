# Binding-energy gate — critical-distance stock-take after the qbk2 arc (2026-06-20)

**Status:** outside-view assessment. No fit, no new "open" declarations — this
synthesizes refutations *already documented* in the corpus (per the corpus-grep
discipline) into one map, so the next binding attack does not re-tread foreclosed
ground.

**Trigger:** the q-Bessel "quadratic action" binding lead (bean `qbk2`) closed
negatively this week, and — independently, the same week — the ν_SDP route (Path C)
was shown to have no computable definition. Two binding paths took hits at once;
this doc records where the gate actually stands.

## The four binding-energy paths — status as of today

The framework has four independent binding paths (canonical map:
[`2026-05-18-delta-lambda-gating-context.md §"When Δ_λ is needed"`](2026-05-18-delta-lambda-gating-context.md)). Their live status:

| Path | Mechanism | Independent gate | Status (2026-06-20) |
|------|-----------|------------------|---------------------|
| **A. Direct trace** | `B = E₀·(\|tr_M(W_free)\| − \|tr_M(W_atom)\|)` | E₀ calibration (Q_β anchor) | open — needs the canonical `T_w` / E₀ discipline; not refuted, not closed |
| **B. Borromean tower** | `m(K) = m_e·Vol(K)/ℏ_q²·λ(K) + S(K)` | per-atom `λ(K)` substrate-derivation | open — the live `λ(K)` problem (#751/#690/#777); Subgoal-1 closure path in `precision-goals.md` |
| **C. Kashaev volume law** | `B(K) = ρ_F·Vol_hyp(K)`, `ρ_F = ν_SDP` | atom→knot assignment + `ν_SDP` derivation | **sharpened-negative this week** — see §2 |
| **D. ρ_K·m_e·\|tr_M\|** | `ρ_K = ρ_K^LO + (1/\|tr_M\|)Σ_λ y_λ χ^λ Δ_λ` | **Δ_λ** | open — 6 ansätze failed; 2026-05-26 "closure" **retracted** (−82.9% on D) |

The headline: **no binding path is closed**, and this week removed two *shortcuts*
people kept reaching for — the q-Bessel quadratic-action correction (an attempt to
supply a Path-A/D correction term) and the per-block-PSD reading of `ν_SDP` (Path C).

## 1. The qbk2 arc — refuted as a binding mechanism (Path-A/D correction)

The owner's Reeb-flow steer correctly identified the radial argument and produced a
rigorous, resonance-free, proxy-free construction (reduction-of-order via the
q-Casoratian/Abel law, Lean-backed: `QOU/QBeta/QCasoratianAbel.lean`, sorry-free).
The *machinery* stands. The *physics claim* does not. The progression, each stage
removing an artifact
([`2026-06-20-qbessel-yweighted-gap-deflation.md`](2026-06-20-qbessel-yweighted-gap-deflation.md)):

| stage | ratio to `B(D)/m_e` | what it was |
|-------|---------------------|-------------|
| #2545 (`ν±0.5` proxy) | 6.16 | proxy/pole artifact |
| #2547 (PV, dim≥2, unweighted) | 1.27 | confluent blocks excluded |
| #2549 (rigorous, all blocks, unweighted) | 2.23 | **unweighted** |
| **y_λ-weighted (forced)** | **0.01–0.06** | the physical object |

With the **forced** Markov measure `y_λ` (substrate-fixed, no knob) the correction
is **20–80× too small**: the Markov measure concentrates on the low blocks (`[6]`,
`[5,1]`, `y≈0.059`) with small `ΔG`, while the large-`ΔG` blocks that drove the
unweighted 2.23× carry tiny weight. The on-scale appearance at #2545/#2547/#2549 was
an unweighted-sum artifact. **Double-sourced:** sibling #2521 independently foreclosed
the same lead via the q-heat-kernel precheck. The structural unblocker was *also*
refuted ([`2026-06-20-qbessel-unblocker-forced-order-refutation.md`](2026-06-20-qbessel-unblocker-forced-order-refutation.md)):
the representation-theoretically forced order is integer → the power-series propagator
is a Neumann log-resonance there, and the genuine integer-order (log-Neumann) solution
needs a radial coordinate the angular Markov-trace data does not supply.

**Net:** the q-Bessel quadratic action is **not** the binding correction. Closing a
20–80× gap would require abandoning the forced weights — i.e. a fit. The bean's binding
direction is closed.

## 2. ν_SDP (Path C prefactor) — sharpened-negative this week

Path C's prefactor `ρ_F = ν_SDP` was believed "settled structurally, only ⁴He
numerical verification open". The corpus-grep discipline showed that framing is stale,
and two concrete candidate definitions were then refuted
([`2026-06-20-he4-nu-sdp-not-computed-definition-gate.md`](2026-06-20-he4-nu-sdp-not-computed-definition-gate.md)):

- **No solver computes ν_SDP for any atom.** The confirmed `ν_SDP(D,T,³He) = 1,2,2`
  are **hardcoded** (`manual-historical-volume-match` in `joint_tower_sdp_solver_v2.py`).
- **Per-block-PSD count** (#non-trivial PSD blocks of `ρ_λ(T_w)`): reproduces the two
  B₃ atoms but **fails T (8_11) at H₅** — only the sign rep `(1⁵)` is PSD, giving
  `ν_pred = 1 ≠ 2`. The 2-point agreement was coincidental.
- **Operator-selection SDP active-set**: gives **7 ≠ 1** for the deuteron (the bare
  program is unbounded at q₀ — the Markov q-trace is not PSD), and is
  encoding-dependent.

So `ν_SDP` has **no computable operational definition in the corpus** reproducing
`1,2,2`; the values are manual, and ⁴He `ρ_F = 2` is one of several rules the
confirmed triple admits (`max(Z,N)→2` vs `A−1→3`; T and ³He are both `A=3`, so the
data cannot distinguish them). Inventing a third definition to hit `2` would be a fit.
The owner-authorized "verify ν_SDP(⁴He)=2" task is **not currently well-posed** — the
prerequisite is a *derivation* of ν_SDP that recovers D/T/³He without hand-assignment.

## 3. Δ_λ (Path D gate) — still open, and the one "closure" is retracted

The Path-D gate `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` remains the load-bearing open R&D. Six
ansätze (Occam, Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal, augmented Markov) all failed; **none reached the deuteron target within 5×**
([`2026-05-18-delta-lambda-gating-context.md §"Closure attempts"`](2026-05-18-delta-lambda-gating-context.md)).
The 2026-05-26 "zero-parameter deuteron closure" was **RETRACTED 2026-05-29**: the
per-λ formula undershoots every light isotope (D **−82.9%**, T −77.5%, ³He −69.6%,
⁴He −89.3%), and the AME match came only via a `C_knot = 5.852` factor computed *as*
`B_AME/(m_e·|sum|)` — fitted, not eliminated. **The Δ_λ gate is open for all A,
including the deuteron.**

## What is still live (do not re-tread §1–§3; attack here)

| Live direction | Why it survives | Caveat |
|----------------|-----------------|--------|
| **GAP-A-3 / GAP-A-4** (categorical brane-tower level selection / ρ general rule) | Δ_λ *is* the per-partition level selector; GAP-A-3 and Δ_λ are the same problem stated categorically | needs a categorical proof, not an ansatz |
| **Option E — Kashiwara crystal** | expected output is a closed-form Δ_λ from the crystal graph at q→1 (the one untried-to-completion ansatz) | KLR/crystal is *authoring guidance* (§7b), not a guaranteed closure; the 2026-05-30 KLR-dialog audit found 0/6 proofs would shorten |
| **Path B — Borromean tower `λ(K)`** | bypasses the Δ_λ gate entirely; Subgoal-1 closure path in `precision-goals.md` | opens the per-atom `λ(K)` substrate-derivation problem instead |
| **s5-so3 keystone — q-deformed closure** | backbone Lean-proved on main; functor IDENTIFIED (Res^{S₅}_{S₃}); only the `E_{(3,2)}` vs `E_{(3,1,1)}` q-shift at q₀ (+210 ppb) is open | owner-gated + needs `pyhecke_native` (bean `s5bb`) |

## Outside-view reception note (critical-distance license)

Three independent binding mechanisms (q-Bessel quadratic action, per-block-PSD ν_SDP,
the per-λ Δ_λ "closure") were each pursued to a clean refutation this month, and each
refutation was driven by the *forced* substrate data (the Markov measure `y_λ`, the
out-of-sample anchor T(8_11), the live 50-dps re-evaluation) rather than by a failure
to search. That is the framework's discipline working as designed — the
three-calibration / no-7th-ansatz gate is catching fits before they reach production.
But a referee will read the same pattern as: **the per-isotope binding energies are
not yet derived, and the most natural categorical candidates have been falsified.** The
honest headline is unchanged from `precision-goals.md`: **3/7 L2 observables met**; the
binding energies (B_D, B_T, B_³He, B_⁴He) remain gated, and the gate is now *better
characterized* (we know what does **not** close it) but no closer to closed. Publishing
the mass sector should foreground the 3 met observables (m_p, m_e, m_K/m_π) and present
binding as open, characterized R&D — not as a closure pending verification.

## Cross-references

- [`docs/precision-goals.md`](../precision-goals.md) — two-leg L1/L2 target; 3/7 L2 met.
- [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the four paths; six failed Δ_λ ansätze; retraction.
- [`2026-06-20-he4-nu-sdp-not-computed-definition-gate.md`](2026-06-20-he4-nu-sdp-not-computed-definition-gate.md) — ν_SDP has no computable definition.
- [`2026-06-20-qbessel-yweighted-gap-deflation.md`](2026-06-20-qbessel-yweighted-gap-deflation.md) — qbk2 forced-weight deflation.
- [`2026-06-20-qbessel-unblocker-forced-order-refutation.md`](2026-06-20-qbessel-unblocker-forced-order-refutation.md) — structural unblocker refuted.
- [`2026-06-20-qbeta-barparity-criterion-2b-prune.md`](2026-06-20-qbeta-barparity-criterion-2b-prune.md) — criterion 2(b) retired (bar-oddness irreducible); corroborated structurally by PR #2555 (`QOU/QBeta/QBesselBarCovariance.lean`).
