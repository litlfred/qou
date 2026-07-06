# Cross-isotope ρ_K consistency audit

**Date:** 2026-05-25
**Branch:** `claude/brave-mendel-FPxFl`
**Related PR:** [#1272 — γγ-pair-production decomposition](https://github.com/litlfred/qou/pull/1272)
**Status:** Audit-only — combines existing per-atom |tr_M| witnesses
from this session + Track B's recent landings; identifies the
universal closure pattern.

## Premise

The 2026-05-25 session converged on the finding that the
QOU framework's bare-|tr_M| route reproducibly under-predicts masses
by O(10²–10⁴)× across all isotopes. This audit consolidates that
finding into a single cross-isotope table and confirms that **ρ_K
(or equivalently the per-knot `linking_weight`) is the UNIVERSAL
closure piece — not a per-isotope coincidence**.

## The data (just-landed and pre-existing witnesses)

| Object | |tr_M(T_w, q₀)| | Target (MeV) | Bare m_e·|tr_M| (MeV) | ρ_K closure factor | Source |
|---|---:|---:|---:|---:|---|
| **proton** (β_Bor in H_3) | 1.0653 | 938.27 | 0.544 | **1723.59** | [PR #1272 `rho_k_proton_substrate_audit.py`](../../computations/audits/rho_k_proton_substrate_audit.py) |
| **deuteron** (T_w in H_6) | 0.3883 | 1875.6 | 0.198 | **9453.03** | [`rho-k-h3a-crystal.witness.json`](../../computations/rho-k-h3a-crystal.witness.json) |
| **⁴He** (T_w via Phase 5q in H_12) | **0.1539** | 3727.4 | 0.0786 | **47397** | [`atomic-tr-m-helium4-canonical.witness.json`](../../computations/atomic-tr-m-helium4-canonical.witness.json) (commit `d2eeec27`) |
| **c_αα binding** (T_w(7²_1) in H_?) | 0.2086 (Wenzl) | 2.427 | 0.107 | **22.66** | [`c-alpha-alpha-categorical-via-jones-markov.witness.json`](../../computations/c-alpha-alpha-categorical-via-jones-markov.witness.json) (commit `388a5b77`) |
| **tritium ⁸B 8_11** (T_w in H_5/B_5) | (TBD) | (binding) | (TBD) | "pattern confirmed" | [`probe_track_b_phase_2.witness.json`](commit `30e90542`) |

The ρ_K closure factor is **the universal multiplicative gap between
the bare |tr_M|-route and the target observable**. Its magnitude
varies by orders of magnitude per object, but the QUALITATIVE
finding — that |tr_M| alone never suffices — is uniform.

## Track B's perpendicular confirmation (c_αα NEGATIVE finding)

Per [`c_alpha_alpha_categorical_via_jones_markov.py`](../../computations/c_alpha_alpha_categorical_via_jones_markov.py)
(commit `388a5b77`, sibling Track B Phase 4):

> "Phase B-4 c_αα probe (EXPLORATORY — NEGATIVE result). Tests whether
> the substrate-canonical Markov-trace value m_e · |tr_M(T_w(7²_1), q_0)|
> could replace the literature c_αα = m_e · Vol(7²_1) ≈ 2.43 MeV in
> alpha_cluster_recursion.py. Result: bare Markov-trace value is
> ~22.7× smaller than the literature."

This negative finding is the **second-order confirmation** of the
proton/deuteron pattern. The hypothesis "|tr_M| can directly give
mass values" is structurally rejected across at least 4 objects
(p, D, ⁴He, c_αα) and across both Wenzl and q-Schur conventions.

## What the spread says structurally

ρ_K factors range from ~23 (c_αα binding) to ~47397 (⁴He). The
spread is NOT random:

- **c_αα is a BINDING ENERGY** (smaller scale, ~2 MeV)
- **proton/deuteron/⁴He are TOTAL MASSES** (larger scale, hundreds to thousands of MeV)
- The ratio is roughly target-mass / |tr_M|: bigger targets need bigger ρ_K

Per-nucleon ρ_K (for the total-mass cases):

| Object | A | ρ_K | per-nucleon ρ_K | ln(ρ_K) | Δ ln(ρ_K) |
|---|---:|---:|---:|---:|---:|
| proton | 1 | 1724 | 1724 | 7.45 | — |
| deuteron | 2 | 9453 | 4727 | 9.15 | +1.70 |
| ⁴He | 4 | 47397 | 11849 | 10.77 | +1.62 (per A increment) |

Roughly `ρ_K ∝ exp(0.85·A)` — but this is not a closed form, just
a fit. The structural decomposition (`prop:rho-k-graded-expansion`)
gives a closed form **only via per-atom calibration**:

  ρ_K_LO(A) ≈ Z·m_p + N·m_n + Z·m_e  (uses m_p, m_n as INPUTS)
  ρ_K_single-gen(A) ≈ α · Σ ln|V̂_i|  (empirical 0.18%)
  ρ_K_pair-gen(A) ≈ ?  (OPEN — pure binding-energy contribution)

## Key structural insight (added 2026-05-25 from cross-isotope spread)

For heavier atoms (A ≥ 2):
- `ρ_K_LO` USES `m_p` and `m_n` as calibration inputs. This is
  **not "deriving ρ_K from substrate"** — it's plugging in
  CAL-3 anchors.
- The **OPEN substrate-derivation** is only the pair-gen residual,
  which is on the order of **the BINDING ENERGY** (a few MeV for D,
  ~28 MeV for ⁴He, etc.), not the total mass.

For nucleons themselves (A = 1, proton + neutron):
- There is NO LO piece via "free constituents" — the proton/neutron
  ARE the calibration anchors.
- The **ENTIRE ρ_K^𝔭 ≈ 1724** factor is the open structural piece.
- This is qualitatively different from the heavier-atom case.

This explains why prior ρ_K work focused on the deuteron (`rho_k_h3a_*`
witnesses): for A ≥ 2 the structural problem decomposes into a
known piece (LO via Wenzl + nucleon-mass calibration) plus the
small pair-gen residual. **For the proton itself, the whole closure
is open**, which is why PR #1272's γγ-decomposition probe was
trying to localise it inside `linking_weight`.

The Reading-A `−G·h²` proposal (Yekutieli per-cell, 8 ideal octahedra)
is therefore a candidate substrate-form **for the proton's full ρ_K,
not just a binding-energy residual**. The crystal-weight failure
(`rho_k_h3a_crystal.py` WRONG_SIGN) was on the DEUTERON's much
smaller pair-gen residual — different scale, different problem.

## The structural lesson

The framework's open closure problem **is not "match m_p" or "derive
linking_weight" — it is "categorically derive ρ_K for every confined
particle/atom"**. This is the **same universal problem** showing up
under different names:

| Name in the codebase | Universal alias |
|---|---|
| `ρ_K^𝔭 ≈ 1724` (atom-knot-mass-derivation.md) | ρ_K closure for proton |
| `linking_weight(𝓑₃, q₀) ≈ 2.46` (lambda-scale-substrate-form.md) | same — re-parameterised via Vol/ℏ_q² |
| `Δ_λ-pair-gen-canonical-form` (conj:rho-k-pair-gen-canonical-form) | same — per-partition decomposition of ρ_K^pair-gen |
| "c_αα 22.7× shortfall" (PR #1275) | ρ_K closure for the α-α channel |
| "tritium 8_11 bare |tr_M| pattern" (Track B Phase 2) | ρ_K closure for tritium |
| Family A's `+(3/4)h²` vs Reading-A's `−G·h²` | candidate substrate-form of ρ_K^pair-gen for the proton |

**This audit's contribution**: putting them in one table so future
sessions don't re-discover the same closure problem under each
isotope's local name.

## Cross-reference

- [`docs/audits/2026-05-25-non-abelian-stokes-reading-a-exploration.md`](2026-05-25-non-abelian-stokes-reading-a-exploration.md)
  — Reading-A as a candidate substrate-form of ρ_K^pair-gen for the proton
- [`docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md`](2026-05-25-option-e-crystal-weight-delta-lambda.md)
  — Phase 0 workplan for Δ_λ via Kashiwara crystal vertices + KL multiplicities
- [`docs/audits/2026-05-25-track-b-r5-full-sdp-extension-design.md`](2026-05-25-track-b-r5-full-sdp-extension-design.md)
  — Track B's multi-atom SDP cascade (parallel attack on the same ρ_K problem)
- PR #1272 — γγ-decomposition probe + ρ_K substrate audit (this branch)
- PR #1275 — Track B Phase 4 c_αα NEGATIVE finding (commit 388a5b77)
- PR #1274 — Track B Phase 2 tritium 8_11 pattern (commit 30e90542)
- PR #1269 — Track B Phase 1 R5-full Wenzl weights generic H_n (commit a7844326)
- PR #1273 — Track B audit doc (R5-full SDP extension design, commit e6bf299d)

## Numerical landscape of candidate `linking_weight` forms

(Computed in this session, for the proton anchor; target = 2.4519
from `m_p / (m_e · Vol(𝓑₃)/ℏ_q²)` inversion.)

| Form | value @ q₀ | Δ vs target | match | bar-symmetric? | Lean? |
|---|---:|---:|---:|---|---|
| **Sibling Bring+Faddeev** `1/(1−h·q¹⁰)+1/(1−h⁴)−1` | 2.4493 | −0.0026 | **−0.106 %** | **NO** | — |
| **Reading-A** `5/2 − G·h²` | 2.4601 | +0.0082 | +0.33 % | yes | — |
| **Lean tr_M bridge** `5/2 + 4·(tr_M(β_Bor) − 1)` | 2.4943 | +0.0424 | +1.73 % | yes | bridge inconsistency theorems on this branch |
| **Family A** `5/2 + (3/4)·h²` (PROVED) | 2.5327 | +0.0808 | +2.89 % | yes | `lambda-scale-substrate-form.lean` |

The bar-asymmetric Bring+Faddeev form is the **closest match by an
order of magnitude** but contradicts Family A's proved bar-symmetry.
The bar-symmetric average `(1/(1−h·q¹⁰) + 1/(1+h·q⁻¹⁰))/2` lands at
**1.691** (−31 % off target) — i.e. the bar-asymmetry is load-bearing
for the sibling's accuracy.

## Substrate-coincidence diagnostic

Solving `1/(1 − h·q^n) = target_linking_weight` for n at q₀ gives
**n = 10.012** — essentially integer 10. This is either:

1. **Structurally exact** with n = 10 categorically determined
   (sibling's interpretation: 10 = 9 color-pair assignments + 1
   diagonal = 3 ⊗ 3̄ in SU(3)-color), and the residual 1060 ppm is
   higher-Faddeev-kernel correction;
2. **Substrate-q₀ coincidence** at integer n=10 (would fail q-locality
   test under perturbation of q₀);
3. The full `Φ_q(h·q¹¹) = ∏_{k≥1} 1/(1 − h·q^{11−k})` is the right
   bar-asymmetric form, with `1/(1−h·q¹⁰)` only its k=1 factor.

**Faddeev kernel interpretation.** `1/(1−h·q¹⁰)` is the k=1 factor of
the symmetric q-dilogarithm `Φ_q(z) = ∏_{k≥1} 1/(1 − q^{-k}·z)` at
`z = h·q¹¹`. Per `prop:li2q-phiq-bar-symmetrization`, the
bar-symmetric pair of `log Φ_q(z)` is `(log Φ_q(z) + log Φ_{q⁻¹}(z))/2`,
which is what the Archimedean realization functor maps `Li₂^q` to —
NOT the naive numerical bar-average. The sibling's formula may be
the leading Faddeev kernel of a bar-symmetric Archimedean-realized
substrate quantity, with the bar-pair structure entering at q₀ via
the realization functor rather than via `q ↔ q⁻¹` averaging of the
pre-Archimedean form.

## Q-locality dichotomy (session exploration, 2026-05-25 follow-up)

Slope `d(linking_weight)/dq` at q₀ for each candidate form vs the
target's own q-slope (≈ 40.25 from `m_p · ℏ_q²(q) / (8G · m_e)`):

| Form | slope | ratio to target |
|---|---:|---:|
| target itself | 40.25 | 1.00 |
| Family A (PROVED) | 0.57 | 0.014 |
| Lean tr_M bridge | −0.20 | −0.005 |
| Reading-A `5/2−G·h²` | ~0 | ~0 |
| Sibling Bring+Faddeev | 62.74 | 1.56 |
| `1/(1−h²·(q²⁵+q⁻²⁵))` (this session) | 140.99 | 3.50 |

The **target's q-slope** (≈ 40) is much faster than the slow-q-varying
structural forms (Family A, Lean tr_M, Reading-A — all have slope
< 1, essentially independent of q at q₀). Conversely, the
**fast-q-varying** forms (sibling 62.7, N=25 form 141.0) overshoot the
target slope.

**No candidate is both slow-q-varying AND bar-symmetric AND matches
at q₀**:

- The PROVED slow-q-varying forms (Family A, Lean tr_M) cannot track
  the target's q-flow even in principle — they're approximately
  q-invariant.
- The fast-q-varying forms either fail q-locality (sibling Bring+Faddeev
  at q = q₀ ± 1% deviates by 1.05% vs target 0.001% rel change; N=25
  form by 4.2%) or contain bar-asymmetry.

**Interpretation.** Either:

1. The mass formula `m(K) = m_e · Vol(K)/ℏ_q² · linking_weight(q)`
   needs linking_weight to absorb additional q-dependence beyond a
   slow-varying polynomial — the `1/ℏ_q²` divergence as q → 1 makes
   the formula formally degenerate, and a fast-varying linking_weight
   compensates.

2. The right substrate quantity isn't `linking_weight` directly but
   the ρ_K factor that combines linking_weight with other structural
   pieces (per `prop:rho-k-graded-expansion`). ρ_K's q-dependence
   may need to track ℏ_q²-related fast-flow.

3. The full Archimedean realization functor (`prop:li2q-phiq-bar-
   symmetrization`) maps a slow-q-varying pre-Archimedean substrate
   form to a fast-q-varying post-Archimedean (real-valued) form. The
   apparent q-slope mismatch is the realization-functor jump, not
   a categorical inconsistency.

Interpretation (3) is consistent with the framework's own
self-description (see `atom-knot-mass-derivation.md §Post-Archimedean
interpretation`). The session's finding is: **slow-q-varying
substrate forms (Family A, Lean tr_M) cannot match the post-functor
target alone** — the Archimedean realization HAS to contribute
non-trivial q-flow. This is the categorical content the framework
calls the `Φ_q`-Archimedean side, NOT the `Li_2^q`-pre-Archimedean
side.

## Faddeev kernel hypothesis tested

Tested whether `Φ_q(z) = ∏_{k≥1} 1/(1 − q^{-k}·z)` at the
substrate-natural `z = h·q¹¹` gives a categorical form:

- Full product `Φ_q(h·q¹¹)` at q₀ ≈ **1509.87** — way too big.
- `Φ_{q⁻¹}(z)` and bar-conjugate `Φ_{q⁻¹}(z̄)` are astronomically small
  (10⁻⁹⁰¹⁴²) — outside convergence radius.
- Bar-symmetric pair `exp((log Φ_q(z) + log Φ_{q⁻¹}(z̄))/2)` is
  effectively zero (asymmetric explosion of one factor).
- **k=1 leading factor `1/(1−h·q¹⁰)` alone matches to 0.18%** —
  this is the sibling's main term.

So the Faddeev kernel is NOT the right post-Archimedean form for
the FULL linking_weight (its product diverges away from the target).
The k=1 leading factor coincidentally matches near q₀ but its
q-locality fails (slope 1.56× target).

## Concrete next step

Per the consolidated findings:

1. The crystal-weight identification `Δ_λ = c_λ` (gave WRONG_SIGN +
   wrong magnitude in `rho_k_h3a_crystal.py`) needs the
   **vertex-decomposition refinement** of Option E Phase 1:
   `Δ_λ = Σ_w n^w_λ · ρ_w(K)` per the Phase 0 workplan.
2. The Track B Phase 1 R5-full Wenzl weights (`pyhecke_native`,
   commit a7844326) now provide the right `y_λ(q)` building blocks
   for n=3, 5, 12 (proton, tritium, ⁴He). The previous crystal
   probe used a self-rolled Wenzl bridge that may have been the
   normalisation issue causing WRONG_SIGN.
3. A **restart of `rho_k_h3a_crystal.py` using Track B's
   `pn.trace_weights_n`** is a single-session probe that may unblock
   the closure.

The restart probe (`rho_k_h3a_crystal_restart_with_phase1_wenzl.py`)
is **queued as next-session work** — implementing the vertex-level
crystal decomposition correctly requires the canonical-basis trace
infrastructure that Phase 0 of Option E lists as multi-session.
This audit clears the framing for that next-session probe.
