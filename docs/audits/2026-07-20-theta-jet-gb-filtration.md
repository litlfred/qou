# The theta-order is CONSTANT across jet order; its leading Gaussian is HALF the Gröbner–Shirshov cumulative q-degree

**Date:** 2026-07-20
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20` (PR #4139)
**Bean:** `qou-mlog` (owner directive: "track theta on jet order and gb filtration")
**Status:** AUDIT — a derived structural bridge between the analytic slope-½
(theta) of the binding q-lift kernel and the categorical GS/Hecke normal-form
grading. Scope-(a)/(b) classification in §4; nothing wired.

## 0. The three objects

- **theta-order** = the Gaussian exponent of the q-difference kernel's growth =
  the Newton-polygon slope. Route B measured the C1 decay leg
  `log_q|b_m| ~ -m²/4` (slope ½), and the gauge-gap synthesis names the slope
  datum `{½,½}` (RSZ Thm 2.2.1/2.2.4). C1 (proved q-lift):
  `[m+2]_q b_{m+2} = b_{m+1} + b_m`.
- **jet order `n` (= `m`)** = the body order indexing `B(K)=Σ_n B_n`,
  `B_n = m_e a_D^{(n)}` (`conj:binding-manybody-eq-jet-filtration`), with
  `a_D^{(n)} = I(n)/n` the involution-number period, **proved Gevrey-½**
  (`QOU.Mass.BindingGevreyHalf`, sorry-free `n! ≤ 4ⁿ I(n)² ≤ 8ⁿ n!`).
- **GS/GB filtration** = the Gröbner–Shirshov normal-form grading of the Hecke
  reducer (`UGB.GrobnerShirshov.JetOrder`): `deg T_w = ℓ(w)` (Coxeter length =
  word length), Poincaré series `Σ_w q^{ℓ(w)} = [m]_q!`, top degree
  `ℓ(w_0) = C(m,2) = m(m−1)/2` (corpus-witnessed:
  `gb-filtration-jet-order.witness.json` — longest `σ₁σ₂σ₁` grade 3 = C(3,2),
  longest H₄ word grade 6 = C(4,2)).

## 1. Q1 — is the theta-order constant across jet order, or graded?

**CONSTANT (intrinsic), not jet-graded.** The clean invariant is the
**curvature** — the second difference of `θ_m := −log_q|b_m|` — which strips the
linear + constant terms and isolates the Gaussian coefficient. The probe
[`theta_jet_gb_grading_probe.py`](../../computations/probes/theta_jet_gb_grading_probe.py)
(mpmath dps 60, C1 to m=200, q₀ muon):

| window | curvature `Δ²θ_m` (→ 2a) |
|---|---|
| m∈[80,110] | 0.499... |
| m∈[140,180] | **0.49998** (sd 0.0017) |
| drift [80,110]→[140,180] | **0.0006** |

⇒ Gaussian coefficient `a = 0.25002 → ¼`, flat. A quadratic fit
`θ_m = a m² + b m + c` on [120,180] gives `a = 0.250019` (→¼). **The slope ½ does
not drift with the jet-order window** — it is one intrinsic number of the binding
module, exactly the proved Gevrey-½ order (effective `2 log I(m)/log m! → 1`,
classical side).

A finite jet-**truncation** is a polynomial (slope 0); the slope ½ is an
asymptotic (n→∞) invariant, not a per-term attribute. What *does* grade with `m`
is the **cumulative** Gaussian `θ_m ~ m²/4` — a consequence of constant curvature
summed over the filtration, not of a drifting slope.

> **Caution against a false discriminant.** `s_m := θ_m/C(m,2)` drifts
> `1.09 → 0.63` and would naïvely suggest jet-grading. It does **not**: the drift
> is a large *linear* term `b·m` (fitted `b = 11.07`) that matches the predicted
> framing `b_pred = ½ log_q(1/(q−1)) = 10.58` — the `[k]_q = (q^k−1)/(q−1)`
> normalization, a **known transient** (Route B's `log_q(1/(q−1)) ~ 62/factor`),
> not the slope. The curvature is the correct invariant and it is flat.

## 2. Q2 — mapping the theta-order onto the GS filtration

C1's denominators are **literally the GS quantum integers `[k]_q`** — the same
`[k]_q` whose product `[m]_q! = Σ_w q^{ℓ(w)}` is the Hecke Poincaré series graded
by GS word length. Because C1 is a **depth-2** recurrence (divide by `[m+2]_q`
every two steps — the shape of the involution recurrence
`I(n)=I(n−1)+(n−1)I(n−2)`), `θ_m` accumulates **half** the `[k]_q` degrees:

$$\theta_m \;=\; -\log_q|b_m| \;\sim\; \tfrac12\sum_{k\le m}\deg_q[k]_q
\;=\; \tfrac12\,\deg_q[m]_q! \;=\; \tfrac12\binom{m}{2}\;=\;\tfrac{m^2}{4}.$$

Equivalently `θ_m ~ deg_q(([m]_q!)^{1/2})`: **the theta factor is the square root
of the Hecke Poincaré series (q-factorial)**, and its q-degree is exactly the
cumulative GS filtration degree ÷ 2. The probe confirms the leading identity:

- leading Gaussian coeff `a = ¼ = (½)·(½)`, where the second `½` is the leading
  coefficient of `deg_q[m]_q! = C(m,2) = m²/2 − m/2`;
- exact arithmetic `C(m,2) = Σ_{k≤m}(k−1)` with **`deg_q[k]_q = k−1`** (the
  per-GS-level q-degree) — verified.

So: **the theta-order's Gaussian is the GS filtration's cumulative q-grading,
scaled by the slope ½** (depth-2 recurrence / Gevrey-½ `√(n!)` ⟺ half the Hecke
Poincaré degree). The subleading linear discrepancy is the `[k]_q`-vs-`q^{k−1}`
framing above, not a defect of the identification.

## 3. The candidate identity

$$\boxed{\;\theta_m \;=\; -\log_q\bigl|b_m\bigr|
\;\sim\; \tfrac12\,\deg_q[m]_q!
\;=\; \deg_q\bigl(([m]_q!)^{1/2}\bigr)\;+\;O(m)\;}$$

— the **theta-order (analytic slope-½ Gaussian) equals half the GS-filtration
cumulative q-degree** of the Hecke normal form, to leading q-order. Read: the
Newton-polygon slope ½ of the binding module *is* the depth-2 half-accumulation
of the GS/Hecke Poincaré grading.

## 4. Derived vs conjectural (scope-(a)/(b) vocabulary)

**DERIVED (exact / proved):**
- `deg_q[k]_q = k−1`; `deg_q[m]_q! = ℓ(w_0) = C(m,2)` (standard, corpus-witnessed).
- Gevrey-½ of the period: `n! ≤ 4ⁿ I(n)² ≤ 8ⁿ n!` (Lean, sorry-free).
- slope ½ = Gevrey order = Newton-polygon slope (RSZ, cited in gauge-gap synthesis).

**MEASURED (scope-(a)):** `θ_m`'s Gaussian coefficient `a = ¼` and its constancy
(curvature flat at 0.49998, drift 6e-4); framing linear term `b ≈ ½ log_q(1/(q−1))`
— numerical growth measurements at q₀, not exclusions.

**CONJECTURAL (the identification):** that `b_m` (C1 kernel) *is* the q-Borel
binding coefficient is the **standing keystone conjecture**
`conj:qdifference-kernel-prolongation-symbol` (narrowed, not proved — §confluent
+ gauge-gap synthesis). Given that, the boxed identity is a **leading-order**
structural bridge; the subleading terms and the exactness (vs asymptotic) of
`θ_m = ½ deg_q[m]_q!` are open.

This is **not** a scope-(b) exclusion and **not** a fit: every quantity is
parameter-free, no AME data, the arithmetic is exact and the growth is measured.

## 5. Candidate Lean brick + consumers

A clean brick, **conditional** on the keystone (state it `_of_` the C1↔binding
identification, per §3b-cond): `theta_order_eq_half_gs_poincare_degree` — for the
depth-2 kernel `[m+2]_q b_{m+2}=b_{m+1}+b_m`, `−log_q|b_m| ~ ½ deg_q[m]_q! = ½·C(m,2)`
(the slope-½ Gaussian is half the Hecke/GS Poincaré top q-degree; the `½` is the
depth-2 accumulation).

Consumers: [`BindingGevreyHalf.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingGevreyHalf.lean)
(the Gevrey-½ = slope-½ side) and
[`JetOrder.lean`](../../content/unital-groebner-bases/lean/UGB/GrobnerShirshov/JetOrder.lean)
(`deg T_w = ℓ(w)`, `bucketize`, degree buckets = the GS grading) — the brick is
the analytic ⟷ categorical bridge between them. Also the keystone module
(`conj:binding-manybody-eq-jet-filtration`) and
[`gb-filtration-jet-order.witness.json`](../../computations/gb-filtration-jet-order.witness.json).

## 6. Discipline

- **Corpus-grep:** the theta ⟷ GS-degree identification is new to this branch;
  `gb_filtration_jet_order_reader.py` + `gb-filtration-jet-order.witness.json`
  carry the GS grading but never relate it to the theta/slope-½; Route B measured
  the theta but did not tie it to `[m]_q!`. No prior closure re-opened.
- **Anti-fit / anti-laundering:** parameter-free; no anchor; the one fitted number
  (quad `b`) is *predicted* by the framing formula, used only to explain finite-m
  pollution, never wired. The identity is leading-order + conjectural on the
  keystone — **not** proved (per "conditional-proved ≠ premise-established").
