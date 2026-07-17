# D-ladder Jackson q-Borel / Écalle acceleration — the odd-channel singularity locator

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

## Results

<!-- RESULTS_TABLE -->

## Verdict

<!-- VERDICT -->

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
