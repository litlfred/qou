# Q_β c_k generating-function hypothesis — scoping within the canonical derivation chain

**Date:** 2026-06-04
**Branch:** [`claude/qbeta-ck-keystone-attack-2026-06-04`](https://github.com/litlfred/qou/tree/claude/qbeta-ck-keystone-attack-2026-06-04) — PR [#1824](https://github.com/litlfred/qou/pull/1824)
**Status:** SCOPING + PROBES IMPLEMENTED (§6 probe sketches 6.a/6.b/6.c/6.d are now implemented on this PR — see the "Implementation status" note in §6)
**Author prompt:** *"perhaps an ODE or PDE coming from Lagrangian or Dirac. scope the specific context of the problem w/in the derivation [cheat] sheet"*

## TL;DR

The c_k precision-ladder coefficients live at the **Step 10 → Step 11** boundary of [`canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md): they are the Taylor coefficients of `Δ(net(T_w))(u)` around `u = 0` at `q = q_0`, where `T_w` is the canonical confinement element produced by Step 10 SDP. The +1.7% SDP-extraction bias on the proved c_2 = −1 (see PR #1824 item 1) is the **finite-rung truncation bridge error** between the algebraic ladder (Lean) and the joint-fit numerical extraction (SDP).

**Hypothesis (user-suggested)**: the c_k are NOT independent integers but the **Taylor coefficients of a single generating function** `F(u, q)`, with three candidate categorical origins — Chern-Simons perturbation, q-difference ODE (Dirac-like), or cosh-avatar closed form (precedent: the `P_m(h) = cosh((2m+1)η)/(2 cosh η)` trace-polynomial closed form already on main).

This document scopes the hypothesis precisely within the canonical chain and proposes a probe per candidate.

## 1. Where the c_k live in the canonical chain

From the cheat sheet (rows 49 + 145):

| Step | Math | Status | Owner |
|---|---|---|---|
| **10. Confinement SDP** | `T_w` canonical from joint mass-tower SDP; `min ‖tr_M(T_w) · 𝔈₀ − B_tgt‖` over GB-NF | 🟢 derived | `lp_dual_solver.py` |
| **11. β-decay Q_β** | `Q_β = |Δ(net(T_w))| · 𝔈₀`; free neutron: `Δ(net) = h(h-2)/2 ≈ −0.1883` | 🟢 derived; **`c_k` truncation** ← the gap | `qbeta_*.py`, `1ppq-qbeta.md` ledger |

So `T_w` is the **algebraic source object** (Step 10). The c_k ladder is the **expansion of `Δ(net(T_w))(u)` around u=0** at archimedean q_0 (Step 11). The truncation gap is what the precision-ceiling audit (PR #1805) hit at ~4 sig figs.

**The c_k question is precisely**: what is the structural form of the function `f_T(u, q) := Δ(net(T_w(u, q)))` such that its Taylor coefficients are exactly the c_k?

## 2. Why a generating function is the natural framing

### 2.a Precedent already in the cheat sheet — `P_m(h)` cosh avatar

Per cheat-sheet §3 line 258 (Phase 5b synthesis):

```
P_m(h) = Σ_{j=0}^{m} C(m+j, 2j)/2 · h^{2j}
       = (q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q)
```

At substrate `q_0 ∈ ℝ_{>0}` with `η_0 = log q_0`:

```
P_m(h_0) = cosh((2m+1) η_0) / (2 cosh η_0)
```

This is a closed-form **generating-function-style closed form** for an infinite family of Taylor expansions of `tr_M(σ_1^{2m})`. It is the **hyperbolic-cos avatar** of the bar-symmetric kernel; at a root of unity it becomes the trigonometric Chebyshev ratio.

**By analogy**, the c_k ladder should plausibly have a cosh-avatar closed form too — `Q_β(u, q_0) / Q_A(q_0) = (some cosh combination)`. The c_k are then the Taylor coefficients of that closed form in u.

### 2.b The +1.7% bias is the bridge error, not a methodology defect

PR #1824 item 1 found SDP-extracted c_2 = −1.017 vs proved canonical c_2 = −1 (relative bias +1.71%). Back-of-envelope: with `u ≈ 0.00852` and c_3 ≈ −2, the joint-fit cross-talk Δc_2 ≈ c_3·u ≈ −0.017 — exactly the observed shift. So the bias IS c_3-into-c_2 leakage from finite truncation of the joint fit.

This is precisely what happens when a **single generating function** is approximated by a **finite Taylor truncation**: each rung's fit gets contaminated by the next rung. The bias signature (+1.7% on c_2 specifically tracking c_3·u) **predicts** the generating function exists and is being approximated from below.

### 2.c Connection to existing infrastructure

| Infra | Where it sits | Generating-function role |
|---|---|---|
| **PR #1769** `CKRecursion` Lean scaffold (sorry-free) | Step 11 q-difference equation framework | conditional: "if R(q,ξ) kernel exists, then c_k satisfy linear recurrence". F(q) is the open keystone. |
| **PR #1739** pre-archimedean recursion + bridge | Step 10–11 boundary | scaling map `f: Δtr_M(√u) ↦ Q_β(c_3 at u³)` — concrete instance of the generating-function bridge |
| **PR #1811** fibre vs observable (open) | Step 11 archimedean evaluation | identifies `/25 = [5]_q²|_{q=1}` as the unique fibre point in the c_3 closure |
| **Phase 5b** `cos_q ↔ cosh ↔ Li_2^q` (in cheat sheet) | Step 9 mass identity | three closed-form avatars of the same bar-symmetric kernel |
| **ck-dk registry §3** (PR #1813, merged) | All-step status | "kernel R / element F(q) is the OPEN KEYSTONE" |

So a `F(u, q)` generating function for the c_k is **already declared the open keystone** by the registry. This scoping doc places that keystone within the cheat-sheet chain.

## 3. Three candidate sources for the generating function

### 3.a Candidate A: Chern-Simons perturbative expansion

**Math**: the Witten-Reshetikhin-Turaev (WRT) construction realises `tr_M` as the path integral of Chern-Simons theory at level k (where `q = exp(2πi/(k+h^∨))`). The CS action S = (k/4π)∫_M CS(A) has a perturbative expansion in 1/k whose coefficients are Vassiliev / Kontsevich integrals. These coefficients **generically grow factorially** — exactly the c_k = O(10⁸) at k=10 behavior observed.

**Generating function**: `F_CS(u) = ⟨W(K)⟩_{CS} = Σ_k a_k(K) · ℏ^k` where ℏ = 2πi/k (the CS coupling). For our u = b·ℏ_q² substrate variable, the connection is at the **Archimedean functor** step — CS perturbative ℏ identifies with substrate ℏ_q via q = exp(2πi·ℏ_q / (something)).

**Where it sits in the chain**: Steps 1–2 (categorical R-matrix from CS path integral) + Step 11 (Archimedean evaluation at q_0).

**Signature**: factorial growth of c_k, Borel-resummability, connection to Vassiliev invariants of the knot underlying T_w.

**Probe candidate**: compare c_k / k! to known Vassiliev coefficients of the proton 𝓑₃ braid (or trefoil if that's the closer model).

### 3.b Candidate B: q-difference equation (Dirac-like)

**Math**: F(q) ∈ Habiro ring satisfies a q-difference equation `(R(q, ξ) F)(q) = 0` where ξ is the q-shift operator `(ξF)(q) = F(qζ)` for a primitive root ζ. This is exactly the framework of PR #1769's `CKRecursion` Lean scaffold (sorry-free, conditional).

The q-difference equation acts like a Dirac-style first-order operator. Its solutions form a finite-dimensional space parametrised by initial conditions; the c_k are then Taylor coefficients of the specific solution F(q) pinned by boundary conditions at q=1 (the classical limit) and q=q_0 (the archimedean substrate).

**Generating function**: F(u, q) is the solution of the q-difference equation; its Taylor expansion at u=0 (post Archimedean functor) gives the c_k.

**Where it sits in the chain**: Step 4 (Hecke quadratic = curvature 2-form via Yekutieli) provides the "Dirac-like" operator framework; Step 11 evaluates the specific solution at q_0.

**Signature**: c_k satisfy a finite-depth linear recurrence with q-dependent kernel. PR #1786's depth-d sweep **REFUTED** the constant-kernel case through d=4; a **q-dependent kernel R(q, ξ)** has not been refuted.

**Probe candidate**: re-test the depth-d recurrence with a q-dependent kernel `R(q_0, ξ)` rather than constants. If passing depth-2 with `R(q_0) = α(q_0) + β(q_0)·ξ`, the q-difference framework holds and the recurrence kernel IS the open keystone.

### 3.c Candidate C: cosh-avatar closed form

**Math**: by direct analogy with `P_m(h_0) = cosh((2m+1)η_0) / (2 cosh η_0)`, hypothesise

```
Q_β(u, q_0) / Q_A(q_0) = cosh(A(η_0, u)) · D(η_0, u)
                       =? cosh(α(q_0)·u + β(q_0)·u² + ...) / (rational in η_0, u)
```

where A and D are closed-form functions of η_0 = log q_0 and u. The c_k are then Taylor coefficients of the cosh combination in u.

**Where it sits in the chain**: Step 11 Archimedean functor (the same step where `P_m` lives in Phase 5b). The cosh-avatar is the archimedean closed-form representation of an algebraic Habiro element.

**Signature**: c_k expressed as `(generalised Hermite or Bell polynomial of η_0) / (k! · 2^k)` or similar — alternating signs, k! denominators, structurally bounded.

**Probe candidate**: fit `Q_β(q_0) / Q_A(q_0)` to a cosh-of-polynomial-in-u form; check whether the polynomial coefficients are q_0-stable and classical-limit consistent.

### 3.d Candidate D: Wedderburn-block basis of generating functions

**Author follow-up prompt** (2026-06-04, mid-scoping):
> *"we also have a basis of generating/eigenfunctions... not sure if those useful in this context or not"*

This refines candidates A/B/C: the c_k generating function need not be a SINGLE function — it could be a **sum over a Wedderburn-block basis**. The relevant basis already lives in **Step 5** of the canonical chain:

```
H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(ℚ(q))
tr_M(β) = Σ_λ y_λ(q) · χ^λ(β)             [Wenzl decomposition]
```

The **Hecke characters χ^λ** form a basis of class functions on `H_n(q)`. Each `χ^λ(σ_1^k)` (varying k) is a generating function in q (or in η_0 at substrate), one per partition λ. They are **eigenfunctions** in the sense of being labels of irreducible blocks of the Wedderburn decomposition.

The Wenzl weights `y_λ(q)` are also generating functions in q (per λ).

**Refined hypothesis (combining with A/B/C above)**:

```
Δ(net(T_w))(u, q) = Σ_λ  f_λ(u, q) · y_λ(q) · χ^λ(braid_word(T_w))
                          ↑          ↑         ↑
                    per-block      Wenzl     Hecke
                    generating    weights   character
                    function
```

The c_k are then:

```
c_k = Σ_λ [Taylor coef of u^k in f_λ(u, q_0)] · y_λ(q_0) · χ^λ(T_w)
```

**This explains several observed phenomena**:

| Observation | Wedderburn-basis explanation |
|---|---|
| Factorial c_k growth (c_8 = O(10³), c_10 = O(10⁸)) | Sum of cosh-Taylor terms across partitions with `k!` denominators that don't fully cancel — partial cancellations give intermediate growth |
| `/25 = [5]_q²\|_{q=1}` unique fibre piece (PR #1811) | One specific partition λ contributes a `1/[5]_q²` factor; at q=1 fibre point it becomes 1/25 |
| Cross-anchor c_3 swing 2.88% (PR #1781 falsification) | Different q_0 (proton vs muon anchor) shift the `f_λ(u, q_0)·y_λ(q_0)` evaluations differently per partition, summing to the observed swing |
| `[3]_q/25` SHARED between m_μ V9 and Q_β c_3 (registry) | Same Wedderburn block (likely λ=(3) or λ=(2,1)) contributes the same `[3]_q/25` structure to both observables |

**Where it sits in the chain**: this candidate uses **Step 5** (Wedderburn basis) explicitly + **Step 11** (per-block Archimedean evaluation). It is the **natural multi-block extension** of candidates A/B/C, each of which assumes a SINGLE generating function.

**Signature** (testable):
- `c_k(q_0)` decomposes as `Σ_λ a_k_λ · y_λ(q_0) · χ^λ_evaluated`, where `a_k_λ` are partition-indexed Taylor coefficients of per-block generating functions
- Each `f_λ` per partition may admit a candidate-A/B/C form (CS / q-difference / cosh) at the per-block level
- The cross-anchor swing is then PARTITION-DECOMPOSED: each λ contributes its own swing, summing to the observed total

**Probe candidate (probe 6.d)**: extract c_k(q_0) at proton + muon anchors and **decompose over Wedderburn blocks** using the known `χ^λ` and `y_λ` of the proton braid 𝓑₃ (Step 4). Fit `f_λ(u, q_0)` per λ. If the per-block generating functions are SIMPLER (lower factorial growth, q-stable across anchors) than the aggregate c_k, the Wedderburn-basis framing is correct.

### 3.e Combined picture

| Candidate | Where in chain | Signature | Refutation cost if wrong |
|---|---|---|---|
| **A** CS perturbative | Steps 1–2 + 11 | c_k factorial, Vassiliev pattern | Compare c_k/k! to Vassiliev knot integrals |
| **B** q-difference (Dirac) | Step 4 + 11 | q-dep kernel passes finite-depth recurrence | Re-run depth-d sweep with q-dep kernel |
| **C** cosh avatar | Step 11 | c_k = cosh-Taylor pattern, k!-bounded | Fit cosh closed form to Q_β(q_0)/Q_A(q_0) |
| **D** Wedderburn basis | Step 5 + 11 | c_k decomposes over χ^λ basis with simpler per-block `f_λ` | Decompose c_k(q_0) over χ^λ at proton + muon, check per-block q-stability |

**The candidates are not mutually exclusive.** A might be the underlying physics (CS path integral), B the algebraic substrate (q-difference equation governing the Habiro element F), C the archimedean closed-form at q_0, D the per-block resolution of A/B/C over the Wedderburn basis (each partition λ carries its own A/B/C-style generating function `f_λ`). All four could be consistent and connected: the c_k aggregate is the sum over λ of per-block generating-function Taylor coefficients.

## 4. Lagrangian / Dirac framing the user named explicitly

> *"it might be a change of coordinates. perhaps an ODE or PDE coming from Lagrangian or Dirac"*

**ODE/PDE candidates**:

1. **q-difference equation** (candidate B above) — the Habiro element F(q) satisfies `R(q, ξ) F = 0` where ξ is the q-shift. This is the q-analog of an ODE in q. The Dirac-like first-order structure is plausible.
2. **KZ (Knizhnik-Zamolodchikov) connection** — categorical R-matrix from CS theory satisfies the KZ flat-connection equation. The c_k could be horizontal-section coefficients of a KZ flow from q=1 to q=q_0.
3. **Heat-equation form** — `∂F/∂u = D(q) · ∂²F/∂u²` would give Gaussian-style closed form with c_k = Hermite coefficients. Less natural for the factorial growth observed.

**Lagrangian candidates**:

1. **Chern-Simons** (candidate A above) — `S_CS = (k/4π)∫ Tr(A∧dA + (2/3) A∧A∧A)`. The c_k = perturbative coefficients (Vassiliev integrals of the canonical T_w-defining braid).
2. **Wess-Zumino-Witten** — `S_WZW = (1/16π)∫ Tr(g⁻¹dg)² + WZ-term`. WZW correlators on the q-deformed character variety, evaluated at the substrate q_0.

**Change of coordinates**:

The right "Q_β coordinate" might NOT be `u = b·ℏ_q²`. Candidates:
- `η_0 = log q_0` (the cosh-natural coordinate from `P_m`)
- `h_0 = q_0 − q_0⁻¹` (the Hecke skein coordinate)
- `ℏ_q = (q_0 − 1)/q_0` (the substrate quantum-Planck)

A change `u → η_0` could turn the c_k ladder into a cosh-Taylor expansion with structurally bounded coefficients. The cheat sheet's Phase 5b note that `cosh(n η_0) ≈ cos(n θ)` for small η_0 / θ supports this: at substrate q_0 ≈ 1.11, η_0 ≈ 0.104 is small, and the cosh-avatar is close to its trigonometric cousin.

## 5. Where the +1.7% SDP bias fits

The SDP-extracted c_2 = −1.017 differs from the proved c_2 = −1 by exactly `c_3 · u ≈ −0.017`. This is the **finite-truncation bridge error** when fitting the joint c_2..c_10 ladder.

**This signature is exactly what a generating function F(u) being approximated by a low-order truncation would produce**:

- F(u) has a specific generating-function form whose Taylor coefficients are the c_k
- Truncating at finite order N introduces cross-talk Δc_k ≈ c_{k+1} · u between adjacent rungs
- The cross-talk is proportional to u, which is small but not zero at q_0 ≈ 1.11
- The +1.7% bias is the size of the cross-talk at the c_2-c_3 interface

**Predictions if the generating function exists** (testable on top of PR #1824's item 1 finding):

| Rung | Expected truncation cross-talk Δc_k | Observed extraction bias |
|---|---|---|
| c_2 | c_3 · u ≈ −0.017 | +0.017 (sign matches if joint-fit signed) |
| c_3 | c_4 · u ≈ −0.009 | extraction shows c_3 ≈ −2.010 (close to expected −2) |
| c_4 | c_5 · u ≈ −0.010 | extraction shows c_4 ≈ −1.144 (close to expected −1 ?) |

A clean probe: extract c_k from joint fit at successively higher truncation order N (use c_2..c_N where N grows from 4 to 12), watch each c_k SHIFT toward its asymptotic value. If F(u) exists, the shifts should converge geometrically.

## 6. Probes (IMPLEMENTED on PR #1824)

> **Implementation status.** All four probe sketches below were
> implemented on PR #1824. The original sketches are retained for the
> design rationale; each is followed by its **implementation note** +
> result. A fifth (probe 6.a', higher-order bias correction) and probe
> 6.d' (per-block Hoefsmit extraction) remain future work.

### Probe 6.a — leading-bias correction (IMPLEMENTED)

Sketch: extract c_k at successively higher truncation order N, watch
each c_k shift toward its asymptotic value.

**Implemented** as `qbeta_ck_truncation_bias_correction_probe.py`
(leading-order form): apply `c_k_corr = c_k − c_{k+1}·u` to the
existing SDP-extracted c_k. **Result: c_2_corr = −0.9999932 (7 ppm
from canonical −1), c_3_corr = −1.9999968 (3 ppm from J_Hopf(1) =
−2).** Strong evidence for the generating function. The full
truncation-order sweep (vary N) is the future probe 6.a'.

### Probe 6.b — closed-form candidate fits (IMPLEMENTED)

Sketch: fit a cosh-avatar `Q_β/Q_A = cosh(...)·D(u)` symbolically.

**Implemented** as `qbeta_ck_closed_form_candidate_fits_probe.py`:
compares the bias-corrected c_k_corr against 7 named coefficient
families. **Result: F1 = −(k−1)! matches c_2, c_3 exactly; breaks at
k≥4** (leading correction insufficient there). The pattern −(k−1)! is
the ordinary-coefficient sequence of a divergent factorial series
(asymptotic-perturbative signature). The explicit cosh-avatar
symbolic fit is future work.

### Probe 6.c — q-difference equation kernel test (IMPLEMENTED)

Sketch: allow the recurrence kernel to depend on q_0.

**Implemented** as `qbeta_ck_q_difference_kernel_on_corrected_probe.py`:
depth-2 sliding-window fit on the bias-corrected c_k. **Result:
constant-kernel REFUTED on corrected values too (α/β spread ~600%)** —
so F(u) is not a simple degree-2 rational. PR #1786's constant-kernel
refutation extends to the corrected ladder.

### Probe 6.d — Wedderburn-block decomposition (IMPLEMENTED, scoping form)

**Implemented** as `qbeta_ck_wedderburn_decomposition_scope_probe.py`:
enumerates the 3 partitions of n=3 (𝓑₃ blocks) with correct
dimensions; records the y_λ(q_0) as explicit "pending pyhecke
extraction" placeholders (the full per-block extraction — probe 6.d' —
is future work). dim_q verification anchor recorded for the future
extraction.

## 7. Scope boundaries (what this doc does NOT do)

- Does not propose a specific Lagrangian (CS vs WZW vs other — open)
- Does not propose a specific change of coordinates (η_0 vs h_0 vs ℏ_q — open)
- Does not write any probe — just scopes the candidate sources within the chain
- Does not refute or confirm any of A, B, C — those are probe 6.a/6.b/6.c work
- Does not modify any production wiring

## 8. Cross-references

- Cheat sheet: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — Steps 10–11, Phase 5b cosh avatars
- ck-dk registry: [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) — kernel R / F(q) declared open keystone
- 1ppq ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — Habiro element identification
- PR #1786 c_2 STRUCTURAL: [`q-beta-c-2-eq-neg-one-structural`](../../content/quantum-observable-universe/mass-theory/q-beta-c-2-eq-neg-one-structural.md)
- PR #1786 depth-d sweep: refuted constant-kernel
- PR #1769 CKRecursion: sorry-free conditional scaffold (machinery, NOT values)
- PR #1811 fibre vs observable: /25 = [5]_q²|_{q=1} (the unique fibre piece in c_3 closure)
- PR #1813 ck-dk registry: only c_2 canonical, c_5+ open
- PR #1824 item 1: +1.7% SDP bias = c_3·u truncation cross-talk (this doc's signature evidence)
