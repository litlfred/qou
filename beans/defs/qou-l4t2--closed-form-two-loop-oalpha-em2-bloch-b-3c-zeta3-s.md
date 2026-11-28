---
# qou-l4t2
title: Closed-Form Two-Loop O(alpha_EM^2) Bloch-B_3(C) / zeta(3) Schwinger Coefficient c_2 in 1/alpha_EM
status: in-progress
type: task
priority: high
tags:
    - compute-accuracy
created_at: 2026-11-19T06:43:03Z
updated_at: 2026-11-28T00:09:00Z
parent: qou-3l2l
---

## Problem & 80-dps Truncation Level vs Experimental Accuracy Evidence

In `computations/probes/truncation_level_vs_accuracy_sweep_probe.py` (`truncation-level-vs-accuracy-sweep.witness.json`), the gauge fixed-point loop tower (`T2a` vs `T2b`) demonstrates that while the electroweak VEV $v$ and Fermi constant $G_F$ cross strictly inside $1\sigma_{\mathrm{exp}}$ at $L = 3$ and settle at $-0.1142\,\sigma_{\mathrm{exp}}$ ($-29.37\text{ ppb}$) at $L = 4$, the electromagnetic inverse fine-structure constant $1/\alpha_{\mathrm{EM}}$ ($\sigma_{\mathrm{exp}} = 1.532 \times 10^{5}\text{ ppQ} = 0.153\text{ ppb}$) improves across $L = 0 \dots 3$ to $-2.383\,\sigma_{\mathrm{exp}}$ ($-365.2\text{ ppt}$), leaving an exact two-loop $O(\alpha_{\mathrm{EM}}^2)$ deficit at $L = 4$:

```
Level L (1/alpha_EM Fixed-Point Tower) |  1/alpha_EM (pred) |    err (ppQ) | err / sigma_exp | < 1 sigma_exp?
---------------------------------------+--------------------+--------------+-----------------+---------------
L0_bare_tree_q0_9_10                   | 136.8232088536     |  -1.553e+12  |     -1.013e+07  | False
L1_plus_Bring_2_over_3pi               | 137.0354154444     |  -4.260e+09  |     -2.780e+04  | False
L2_1loop_FormA_quadratic               | 137.0359993132     |  +9.937e+05  |     +6.4840     | False
L3_1loop_FormB_Schwinger_cubic         | 137.0359991270     |  -3.652e+05  |     -2.3830     | False
CODATA 2022 target                     | 137.035999177(21)  |       0      |      0.0000     | True
```

At $L = 3$, the Form-B cubic Schwinger fixed-point equation is
$$-H_{\mathrm{hab}} h_0^2 \alpha^3 + H_{\mathrm{hab}} \alpha^2 + T_{\mathrm{EM}} \alpha - 1 = 0, \qquad T_{\mathrm{EM}} = q_0 [9]_{q_0}[10]_{q_0} + \frac{2}{3\pi},\quad H_{\mathrm{hab}} = \frac{[2]_{q_0}}{8\pi}.$$
Adding the $L = 4$ two-loop quartic term $+ c_2 \alpha^4$ in the fixed-point equation (equivalently $\Delta(1/\alpha_{\mathrm{EM}}) = c_2 \alpha_{\mathrm{EM}}^2$) requires:
$$c_{2,\mathrm{req}} = \frac{\alpha_{\mathrm{CODATA}}^{-1} - \alpha_{L=3}^{-1}}{\alpha_{L=3}^2} = +0.000939865 \approx +\frac{3\,\hbar_q}{3\pi}.$$

## Exact Algebraic Starting Point

1. **Level-4 Quartic Schwinger Fixed-Point Equation:**
   $$c_2(q_0) \alpha^4 - H_{\mathrm{hab}}(q_0) h_0^2 \alpha^3 + H_{\mathrm{hab}}(q_0) \alpha^2 + T_{\mathrm{EM}}(q_0) \alpha - 1 = 0.$$
2. **Candidate Geometric Origins of $c_2(q_0)$ on Bring's Surface $\Sigma_4$ / Bloch Group $B_3(\mathbb{C})$:**
   - **Bring $H^1(\Sigma_4)$ zero-mode dressing of the 1-loop Habiro coefficient:**
     Notice that the tree level $T_{\mathrm{EM}} = q_0[9]_{q_0}[10]_{q_0} + \frac{2}{3\pi}$ carries the Bring zero-mode shift $\frac{2}{3\pi} = \frac{4}{-\chi(\Sigma_4)\pi}$, while the $L=3$ cubic coefficient is $-H_{\mathrm{hab}} h_0^2 = -\frac{[2]_{q_0}}{8\pi} h_0^2$. At two loops ($L=4$), the next $q$-skew / Bloch-$B_3(\mathbb{C})$ self-energy coefficient in the $(h_0, \hbar_q, 1/\pi)$ basis is constrained by bar-parity ($q \leftrightarrow q^{-1}$) and the trilogarithmic regulator $\mathrm{Li}_3(q_0^{-2}) / \pi^2$.
3. **Deliverables:**
   - Derive $c_2(q_0)$ from the two-loop $U(1)$ Schwinger–Dyson self-energy on Bring's curve $\Sigma_4$ without fitting to $\alpha_{\mathrm{CODATA}}^{-1}$.
   - Formalize the $L=4$ quartic fixed-point contraction and existence/uniqueness theorem in Lean (`folio/quantum-observable-universe/lean/QOU/`), extending `ElectroweakBringSchwingerBridge.lean`.



## Progress Update (2026-11-19)
Wave-6A proved Dyson resummation Form-B uniqueness (`+0.433 ppt` tail) and `q_0 <-> q_2t` sensitivity `dC/dq = +843.64` in `QOU/StandardModel/PhotonDysonHabiroAndTwoLoopStructure.lean` + `alpha_em_dyson_uniqueness_and_twoloop_delta2_probe.py` (`scriptHash = e459d13ec01b`, Red-Team PASS). Pre-registered `-Li_3(q^{-2})(alpha/pi)^2` (`c_2 = -0.9263`) cuts the `q_2t` offset from `+75.97 ppb` to `+39.50 ppb`; remaining `~ -1.00 (alpha/pi)^2` 2-loop Habiro-Chern-Simons coefficient remains genuinely open without fitting.

## Resolution (2026-11-19)

Completed (`0 sorry, 0 axiom`, Red-Team UNCONDITIONAL PASS): `QOU/StandardModel/PhotonDysonHabiroAndTwoLoopStructure.lean` (768 lines) + 80-dps `alpha_em_dyson_uniqueness_and_twoloop_delta2_probe.py` proving Dyson-Schwinger geometric series uniqueness (`Delta alpha^{-1} = -Pi(0)`), cyclotomic Habiro `Phi_1 Phi_2 Phi_3 = q^4 + q^3 - q - 1`, and 2-loop Schwinger/zeta(3) diagnostic.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-22 — applicability review (wave-2, owner instruction to review older beans against current rulings)

**Blocked by current rulings; not workable as written.** The bean presumes one fixed-point loop tower for 1/α_EM and asks for its two-loop coefficient c_2 in closed form, with an accuracy table against experiment. Since 2026-11-21 the owner has ruled that the canonical α_em form stays open (`qou-aemx`; "no form is chosen by its residual") and that the dashboard carries the CS tower and the additive (A, B) forms as labelled arms. Until a form is chosen, "the" two-loop coefficient is not one object. The accuracy table is an empirical comparison and cannot enter a proof (owner: no empirical predictions in formal proofs). The resolution recorded 2026-11-19 was reopened 2026-11-20 because its files exist nowhere. A pure-math core that survives: for each labelled arm separately, decide whether its second-order coefficient lies in the Q-span of {ζ(3), π²·log 2, π², 1} (a period / Bloch-B₃ question), as a conditional statement per arm. That belongs to the α_em thread, which owns the chain. Status left as is.

## 2026-11-22 — applicability verdict (STRICT review, wave-2 brief)

**NEEDS-OWNER.** canonical α_em form open (qou-aemx, 2026-11-21); “the” two-loop coefficient is undefined until a form is chosen; α_em chain owned elsewhere.

## 2026-11-27 — skein part derived (PR #9841)

Answers the surviving pure-math core for the Form B arm. Lean `QOU/MassTheory/EmVertexPairScalarChain.lean` (no sorry): in convention D the skein `σ − σ⁻¹ = h` is scalar in any algebra, so every chirality-summed vertex pair, at any positions, is `−h²`, and `k` pairs give `(−h²)^k` under every moment. Two-loop coefficient of the skein chain = `−N₁h²H`; `N₁ = 1` is Form B's own term. Nothing from the vertex algebra lies outside `ℤ[q,q⁻¹]·[2]_q/(8π)`: no ζ(3)/Li₃. A Bloch-B₃ term would need a two-loop measure (undefined in the corpus). C1 stays a labelled arm. Open: N₁ (placement count), §3b-cond normalization, two-loop measure. Audit `docs/audits/2026-11-27-alpha-em-two-loop-skein-scalar.md`.

## 2026-11-28 — placement count N₁ = 1 (PR #9856)

`[3]_q = 3 + h² = 3 − V` (`EmThetaGraphSkeinSplit.lean`, sorry-free). The corpus
θ-graph two-loop term is a classical 3 plus exactly one vertex pair, so N₁ = 1, and
Form B agrees. No integer multiple of h² equals [3]_q. What remains open: the
classical constant 3 (absent from Form B) and the per-loop measure ((α/8π)² vs
[2]_q α²/(8π)). Measure is in a separate thread. Audit:
docs/audits/2026-11-28-alpha-em-two-loop-placement-count.md.


## 2026-11-28T00:09Z
Two-loop measure on Bring: PR #9860 (EmTwoLoopMeasureConnected, FlatSunsetConnectedPeriod).

## 2026-11-28 — the θ-graph's classical 3 (PR #9896)

`(σ+σ⁻¹)² = 4 + h² = [2]_q²` at one convention-D generator, so `[3]_q = (unsigned
four-history pair) − 1` (Clebsch–Gordan `[2]² = [3] + [1]`; `EmThetaClassicalThree.lean`,
sorry-free). The 3 is the four chiral histories counted with weight 1, minus the
singlet. Form B's signed `−ε₁ε₂` weights cancel it. Open choice (qou-aemx): signed vs
unsigned-spin-1 weights on the two-vertex photon insertion. Measure: thread "Define
the two-loop measure on Bring", PR #9860.

## 2026-11-28 — photon form vs pair weights (PR #9899)

Mixed histories M = 2, same-chirality S = 2 + h² at one generator; weights (a,b) give
(2a+2b) + b h², classical part zero iff a = −b. The ruled photon term σ₀σ₁⁻¹ carries
(1,0), value 2: neither Form B (1,−1) nor θ-graph (1,1). Scope (a): the photon form
does not decide the pair weights; that needs a propagator rule (a definition, owner
call). Both readings stay as fallbacks. `EmPhotonPairWeights.lean`, sorry-free.

## 2026-11-28 — joining rules compared (PR #9909, Carl chose "Compare candidate rules")

Four rules for joining two photon vertices: plain v w, bar-Hermitian v̄ w, bar-even
(v+v̄)(w+w̄), signed bar-odd −(v−v̄)(w−w̄). Only bar-odd (Form B) is the scalar −h² at
any two positions. Bar-even gives [2]² at one position (θ-graph after the singlet) and
the non-scalar 4στ − 2h(σ+τ) + h² at two. None adopted; adopting one is Carl's call.

## 2026-11-28 — ruling: bar-odd join (PR #9911)

Carl tapped "Bar-odd (Form B), θ as fallback" (01:09Z). Two-loop vertex pair = −h², N₁ = 1;
θ-graph [3]_q kept as fallback. Remaining open item for this bean: the per-loop measure
(thread "Define the two-loop measure on Bring").

## 2026-11-28 — two-loop coefficient in closed form, conditional on μ₁

With the bar-odd join (ruling, #9911) and the one-factor measure (Carl's tap 01:11Z,
PR #9915, EmFormBLoopMeasure.lean), the two-loop slot is −h²[2]_q α²·μ₁, i.e.
−h²[2]_q α²/(8π) at μ₁ = 1/(8π). No ζ(3) / Bloch-B₃ term arises from the vertex
algebra or this measure. Still open, so the bean stays open: μ₁ = 1/(8π) is
underived (phase-4 per-loop measure). Fallbacks: θ-graph [3]_q, squared measure,
R1 flat sunset ζ(3).

## 2026-11-28 — μ₁ stated as a conditional (PR #9932)

Lean now states μ₁ = 1/(8π) as an implication from two hypotheses with no instances: `GermPeriodShare` (Φ / R2, generic) and `HeatKernelLeadingCoeff` (Clause A, under Transcendental/). The generic class supplies only the factor 1/2 (`perLoop_share_satisfiable`). μ₁ is still **not derived**. The next step is the owner-gated 08a2 Gauss–Manin keystone, which discharges Φ. This bean stays open.
