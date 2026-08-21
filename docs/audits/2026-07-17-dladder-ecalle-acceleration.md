# D-ladder Jackson q-Borel / Écalle acceleration — the odd-channel singularity locator

> **🛑 PREMISE CORRECTED 2026-08-09 — the D-ladder is CONVERGENT; there is no
> singularity to locate.** This document is an "odd-channel singularity locator"
> for a series that has no Borel-plane singularity to find. `D(ũ)` is convergent
> with radius `ρ = ũ(q*_ρ) = 0.142799996644689…`, the image of a **`Q_b` zero**
> (`q*_ρ ≈ 1.48989`, the real root > 1 of an irreducible degree-12 factor of the
> `Δ_net` numerator) omitted by the 2026-07-12 search; `κ = 0`. See
> [`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md)
> and registry row **KC22**. There is no instanton action, no Stokes constant,
> and no Écalle resummation to perform.
>
> **A second, independent defect.** The §Context inference — *KC22 closes the
> (q-)holonomic class, **hence** a genuine c₃ closure is transcendental/
> resurgent* — is invalid on its own terms, and would have been invalid **even
> if the ladder had diverged**: non-holonomicity constrains the *algebraic*
> class, not the *growth* class, and only a divergent series can be resurgent.
> Swept corpus-wide in
> [`2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md`](2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md).
> KC22's own closed form `D(w) = φ(w)·log(1 − w/ρ) + ψ(w)` (with `φ`, `ψ`
> algebraic over the degree-12 field) is the counterexample: convergent *and*
> not low-order P-finite.
>
> **What survives.** The acceleration machinery and the per-setting measurements
> stand as data; the gate failure is the expected reading of `κ = 0` rather than
> a finite-`k` artefact. The exact `d_k ∈ ℚ(√3)` data and the 2-adic parity
> grading are untouched (KC22). Nothing was wired; no `c_k` tier changes.

**Date:** 2026-07-17 · **Branch:** `claude/dladder-qborel-acceleration-2026-07-17` ·
**Tier:** exploratory acceleration machinery + measurement (scope-(a); no `c_k`
wired; no fit; no tier change; no instanton action claimed without the gate).

## Context

Unowned item #1 of the
[1ppQ path reassessment](2026-07-17-1ppq-path-reassessment.md): with KC22
closing the entire (q-)holonomic search class for the bar-odd D-ladder, a
genuine c₃ closure — if any — is transcendental/resurgent, and the one route
left is the **Jackson q-Borel / Écalle acceleration of `D(ũ) = Σ d_k ũ^k`**
(d_k ∈ ℚ(√3), exact). Two arms run in parallel:

- **"more terms"** — [`qbeta_dladder_extension_singularity_probe.py`](../../computations/qbeta/qbeta_dladder_extension_singularity_probe.py)
  (separate session) extends the exact d_k toward k≈31 at ORD 63;
- **this arm** — builds the *acceleration machinery* on the committed order
  (ORD 43 → d₁…d₂₁), with core functions taking **any-length exact
  (a_k, b_k) ∈ ℚ² pair lists**, so the extension's terms plug in with no
  edits. The ladder is NOT extended here; the two arms cannot race.

The prior wrong-transform note
([2026-07-13 coupled-recurrence audit §Resummation note](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md))
established: plain `÷k!` Borel over-suppresses the mild q-Gevrey growth; the
Borel–Leroy order scan found the **drifting-index signature** (root-test
slope-zero s\* ≈ 0.20 vs log-fit C ≈ 0.06) and an unresolved singularity
(dlog-Padé ρ ≈ 0.156 vs root-test radius ≈ 0.32 at k=21 — a 2× estimator gap,
honestly reported as "not resolved").

## Method

Formal pre-registration (hypothesis class as the unified two-parameter family
𝓑_{Q,s} with classical Borel–Leroy as the Q → 1 boundary, closure semantics,
and refutation criteria):
[`2026-07-17-dladder-qborel-acceleration.md`](2026-07-17-dladder-qborel-acceleration.md).
This document is the execution record.

Probe: [`qbeta_dladder_ecalle_acceleration_probe.py`](../../computations/qbeta/qbeta_dladder_ecalle_acceleration_probe.py)
(witness [`qbeta-dladder-ecalle-acceleration.witness.json`](../../computations/qbeta/qbeta-dladder-ecalle-acceleration.witness.json)).
The conformal-map + dlog-Padé core is **imported from the merged even-channel
probe** [`qbeta_borel_conformal_pade_probe.py`](../../computations/probes/qbeta_borel_conformal_pade_probe.py)
(ζ = 4A₀w/(1+w)² uniformizes the cut; dlog turns the branch point into a
simple pole; margin-held damped fixed point), not reimplemented.

- **Arm 1 — Borel–Leroy + conformal dlog-Padé.** `b_k = d_k/(k!)^s`, s on a
  fine grid 0…0.40 (step 0.02) bracketing both prior order estimates, plus the
  slope-zero s\* by bisection with an 8-config headline gate.
- **Arm 2 — Jackson q-Borel.** `b_k = d_k / q₀^{t·k(k−1)/2}` for scanned Ramis
  order t ∈ 0…0.50 (+ t\* bisection); q₀ from
  `q-pinning-50-digit.witness.json` — the same source the D-ladder generator
  reads.
- **Arm 3 — parity-split acceleration.** Per the exact 2-adic ℤ/2 grading
  (`v₂(den b_k)=0 ⟺ k odd`; 2 the unique graded prime), the odd-k and even-k
  subseries accelerated separately in the w = ζ² variable, each at its own
  Borel–Leroy order.

**The estimator-consistency gate (pre-stated, tol 15%).** A singularity is
reported as *located* only when the conformal dlog-Padé radius and the
root-test radius agree to |ρ_dlog/ρ_rt − 1| < 0.15 with ≥ 2 independent
(L, M, μ) configs converged — the structural fix for the prior 0.156-vs-0.32
gap. Pre-stated kill criteria: **K1** (gate fails at every (s,t) ⇒ finite-k
shadow persists at ORD 43; scope-(a), not a refutation of resummability);
**K2** (parity estimates diverge ⇒ reported as structure, not failure).

In-script assertions: exact d_k reproduction against the committed
generating-function witness (ℚ equality, all 21 pairs); zero-order transform
identity (s=0, t=0 reproduce the raw series exactly); gate arithmetic
spot-check (the prior 0.156/0.32 pair must fail; a synthetic Li₋₁/₂(2ζ)
branch point at ρ = 1/2 must pass — it does, located to 5 decimal places).

## Results (run 2026-07-17, 342 s wall, 4/4 assertions pass)

| Arm | order scan | slope-zero order | headline gate (8 configs) | ρ_dlog vs ρ_rt |
|---|---|---|---|---|
| 1 — Borel–Leroy `(k!)^s` | s ∈ 0…0.40 (21 pts) | s\* = 0.1865 | **fail** | 0.1283 vs 0.2522 (gap 0.49) |
| 2 — Jackson q-Borel `q₀^{t·k(k−1)/2}` | t ∈ 0…0.50 (11 pts) | t\* = 0.2253 | **fail** | 0.1150 vs 0.2119 (gap 0.46) |
| 3 — parity-split (w = ζ²) — odd (S-carrier) | per-parity s\*_par = 0.0346 | — | **PASS** (gap 0.097) | ρ_ζ = 0.1516 |
| 3 — parity-split — even | per-parity s\*_par = 0.4647 | — | **PASS** (gap 0.132) | ρ_ζ = 0.2543 |

The gate fails at **every** (s, t) grid point and at both slope-zero orders
for the full series — every configuration shows the same ~2× dlog-Padé-below-
root-test signature as the prior k=21 attempt, now demonstrated to be
transform-independent across the whole two-parameter family. Per the
pre-stated rule, **no candidate comparison was run** (no singularity is
reported as located for the full series).

**The parity-split finding (K2, structure not failure).** Each 2-adic parity
subseries, accelerated separately at its own Borel–Leroy order, individually
*passes* the estimator gate — but their back-mapped radii differ by 40%
(|ρ_odd/ρ_even − 1| = 0.404, tol 0.25). The ℤ/2 bar-parity grading
(`v₂(den b_k) = 0 ⟺ k odd`) therefore acts on the **Borel plane** itself:
the full series superposes two singularity structures, which is *why* no
single fixed-order transform can produce one consistent radius. The odd
(S-carrier) subseries — the physically load-bearing half — has the nearer,
cleanly-gated singularity at ρ_ζ ≈ 0.152 (its per-parity slope-zero order
s\*_par ≈ 0.035, i.e. nearly convergent after the parity split). These
per-parity radii are reported as *structural data* for the extension arm,
not as located instanton actions.

## Verdict

**K1 (pre-registered): the finite-k shadow persists at ORD 43 (k = 21) for
the full series** — the estimator-consistency gate fails at every Borel–Leroy
order s ≤ 0.40, every Jackson q-Borel order t ≤ 0.50, and at both slope-zero
orders with the 8-config headline set. Scope-(a): a statement about k = 21
resolution power, not a refutation of resummability or of any singularity
candidate. **K2: the parity-split radii diverge (40%) with both sub-gates
passing** — recorded as the 2-adic bar-parity grading acting on the Borel
plane; the odd/S-carrier singularity at ρ_ζ ≈ 0.152 is the sharpest current
odd-channel datum. The machinery (exact-pair API, both transforms, the gate,
the parity split) is committed and order-agnostic — the extension arm's
k ≈ 31 terms decide whether the full-series gap closes and whether the
per-parity radii stabilize.

**Replication + discrepancy note.** A parallel implementation on this branch
([`2026-07-17-dladder-qborel-acceleration.md`](2026-07-17-dladder-qborel-acceleration.md))
independently confirms the K1 full-series gate failure (double-confirmed,
transform-independent) but reports its parity-split branches *unresolved*,
in tension with this run's per-parity gate passes. Probable cause: shared-s
vs per-parity slope-zero order and ζ- vs ζ²-plane methodology; queued for
adjudication (bean qou-ffxw) — neither parity reading is treated as established.

**Adjudication (2026-07-17, bean qou-ffxw closed).** Probe
[`qbeta_dladder_parity_adjudication_probe.py`](../../computations/qbeta/qbeta_dladder_parity_adjudication_probe.py)
(witness [`qbeta-dladder-parity-adjudication.witness.json`](../../computations/qbeta/qbeta-dladder-parity-adjudication.witness.json))
ran **both** methods on the same exact d_k plus four adversarial controls.
**Verdict: undecidable-at-k21 — but the adversarial worry is partly dismissed
and the discrepancy is diagnosed.** The exact methodological difference is four
ingredients: (i) per-parity slope-zero s\* (this run) vs a shared fixed s-grid
(the sibling; the even branch's optimum s ≈ 0.465 lies *outside* the sibling's
[0, 0.40] grid); (ii) **conformal-mapped** dlog-Padé (this run) vs **raw**
dlog-Padé (sibling); (iii) gap-only gate (this run) vs gap+spread gate
(sibling); (iv) tiny fixed Padé order vs an M-window. Findings: **C4a** — this
run's conformal gate is *not* self-referential (the located singularity is
seed-invariant to ~1e-13 across {0.5,1,1.5,2}×ρ_rt, refuting "it just returns
the root-test seed"); **C4b** — the flip localizes to the **conformal map**:
raw dlog-Padé at *this run's own* per-parity s\* still fails both parities (raw
Padé ≈ 2× below the root-test radius — the sibling's "branch-cut-biased-low"
signature), while the conformal estimator passes; **C3** — this run's real
per-parity radii are stable across orders/margins/truncation (≤ ~10 %). What the
controls **cannot** do at ~10–11 coeffs/parity is *certify* the 40 %-split as
real ℤ/2 structure: on same-length **convergent** branch-point synthetics
(mismatched to the divergent target) the short-series conformal estimator is
biased ~30 % high (C1a) and fails to recover planted distinct parity
singularities (C2). So the sibling's "unresolved" is the raw-Padé low bias and
this run's "per-parity pass" is the conformal cure — but neither reading is
established at k = 21. Deferred to the ORD-63 / k ≈ 31 extension (the specific
question: do the odd/even radii stay 40 % apart or converge?). Ledger:
[`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).

## What the extension's k≈31 terms will decide

The machinery is order-agnostic: rerunning this probe on the extension arm's
exact pairs directly measures whether (a) the estimator gap **shrinks** with k
(finite-k shadow → a clean gate pass and a located odd-channel Borel
singularity, comparable against the pre-named candidates), or (b) the gap
**persists** (structural q-Gevrey drift → the honest resummation is the
genuine Écalle multi-stage acceleration / Φ_b state integral, and fixed-order
transforms of any kind are the wrong lens). Either outcome is decisive for how
the odd-channel program proceeds.

## Cross-references

- Reassessment: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md) (§Non-duplicative options, item 1).
- Attack specs: [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md) §1 (the running "more terms" arm).
- Wrong-transform + drifting-index record: [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md).
- Prior Leroy scan witness: [`qbeta-dladder-qborel-leroy-resummation.witness.json`](../../computations/qbeta/qbeta-dladder-qborel-leroy-resummation.witness.json).
- 2-adic grading witness: [`qbeta-dladder-padic-graded-prime.witness.json`](../../computations/qbeta/qbeta-dladder-padic-graded-prime.witness.json).
- Conformal core: [`qbeta_borel_conformal_pade_probe.py`](../../computations/probes/qbeta_borel_conformal_pade_probe.py) (C1 of the Borel/alien-calculus audit).
- KC21/KC22: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md); S-scales: [`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md).
