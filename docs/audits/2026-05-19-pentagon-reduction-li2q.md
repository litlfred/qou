# Pentagon Reduction of Li_2^q at Out-of-Convergence Pair Products

**Author:** Claude, session_01SdmQMzdktVYqqManFF3Dpt
**Trigger:** Repo-owner directive 2026-05-19: "work in Z[q, q⁻¹] as much as possible! do pentagon reduction." Addresses the T3 divergence in `binding_via_interface_knot.py` (PR #801) by algebraic reorganisation rather than archimedean continuation.

## The structural insight: archimedean functor adds the rational denominators

Per [`pre-tau-vs-post-tau.md`](../../content/quantum-observable-universe/braids-and-knots/pre-tau-vs-post-tau.md), every derivation step lives in one of two registers:

| Register | Coefficient ring | Examples |
|---|---|---|
| **Pre-τ** | $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ (or its $z$-Habiro completion) | Hecke spectra, Markov traces, LP/SDP, GS reductions |
| **Post-τ** | $\mathbb{R}$ (or $\mathbb{C}$) via $\tau_{\mathrm{arch}}$ | Hyperbolic volumes, thimble depths, mass eigenvalues |

The user's framing crystallises an important consequence: the $1/(n \cdot [n]_q)$ denominator inside the standard series form of the q-dilogarithm,

$$\mathrm{Li}_2^q(z) \;=\; \sum_{n \ge 1} \frac{z^n}{n \cdot [n]_q},$$

does NOT live pre-τ. The factor $1/[n]_q$ is pre-τ-fine (since $(q-q^{-1})^{-1}$ is in the pre-τ ring, $1/[n]_q$ is a rational function in $q$), but the $1/n$ (division by the integer $n$) requires $\mathbb{Q}$-arithmetic — and inversion of integers is the canonical archimedean operation.

**Pre-τ analog**: $\mathrm{Li}_2^q$ as a Hopf-algebra element (the level-2 primitive of $\mathcal{H}_q$ per [`def:q-dilogarithm`](../../content/quantum-observable-universe/quantum-observable-universes/q-dilogarithm.md)) is uniquely characterised by the **pentagon identity**

$$\mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) \;=\; \mathrm{Li}_2^q(uv) + \mathrm{Li}_2^q\!\!\left(\tfrac{u(1-v)}{1-uv}\right) + \mathrm{Li}_2^q\!\!\left(\tfrac{v(1-u)}{1-uv}\right) \tag{P}$$

— this identity holds in the pre-τ ring $R$ (the rational functions in $u, v, q$). Convergence is a post-τ phenomenon: after $\tau_{\mathrm{arch}}$ specialises to $\mathbb{R}$, $\mathrm{Li}_2^q(z)$ has series radius $|z| < q$ — but the pentagon identity (P) **continues to hold structurally**, as an analytic-continuation-free algebraic rewrite.

**Open**: a self-contained theorem in the paper stating "τ_arch introduces the $1/n!$ / $1/[n]_q!$ rational denominators on grouplikes (exp_q, Li_n^q, etc.) that produce convergence behaviour" would crystallise this. Currently the discipline is documented as register-rules in `pre-tau-vs-post-tau.md` and consumed implicitly by the q-exponential / q-dilogarithm definitions (which are stated as grouplikes / level-k primitives, not as series).

## What this means for the T3 divergence

`binding_via_interface_knot.py` (PR #801) defers T3 because pair products $|V_i V_j| \approx 1.15$ exceed $q_0 \approx 1.110$, taking $\mathrm{Li}_2^q(-|V_i V_j|)$ outside its post-τ series radius. The script's docstring listed three regularization options:

> (a) re-deriving V̂ under a Wedderburn-weight scheme that bounds |V̂| < q^{1/2}
> (b) analytic continuation of Li_2^q via reflection formula at |z| ≥ q
> (c) restriction to non-divergent pairs with a structural justification

Per the user's directive, (b) is the WRONG framing — "analytic continuation" is archimedean language for a phenomenon that doesn't exist pre-τ. The right framing is **algebraic pentagon reduction**: $\mathrm{Li}_2^q(uv)$ rewrites as a sum of $\mathrm{Li}_2^q$ at SIMPLER arguments via (P), and the rewrite is valid in the pre-τ ring $R$ where convergence is not a concept.

For our concrete case $z = -|V_i V_j|$ with $|z| > q_0$:

- Factor $z = u \cdot v$ with $u = i \cdot \sqrt{|z|}$, $v = i \cdot \sqrt{|z|}$ (both pure imaginary, $u v = i^2 |z| = -|z| = z$).
- $|u| = |v| = \sqrt{|z|}$; for $|z| \approx 1.15$ this gives $|u|, |v| \approx 1.07 < q_0$.
- $\alpha = u(1-v)/(1-uv) = i\sqrt{|z|} \cdot (1 - i\sqrt{|z|}) / (1 + |z|)$, modulus $\sqrt{|z|}/\sqrt{1+|z|} \approx 0.73 < q_0$.
- $\beta = $ same modulus by symmetry $u = v$.

All four sub-arguments fall inside the post-τ convergence disk; their series evaluations are well-defined. Pentagon (P) reorganises the divergent target into convergent pieces:

$$\mathrm{Li}_2^q(-|V_i V_j|) = 2 \,\mathrm{Li}_2^q(i\sqrt{|V_i V_j|}) \;-\; 2\,\mathrm{Li}_2^q\!\!\left(\tfrac{i\sqrt{|V_i V_j|}}{1 + i\sqrt{|V_i V_j|}}\right) \tag{P'}$$

(the duplication-form of pentagon since $u = v$).

## Implementation

[`pentagon_reduction_li2q.py`](../../folio-assistant/computations/pentagon_reduction_li2q.py) implements (P) recursively: convergent arguments evaluate via the existing `li_2_q` series; out-of-radius arguments factor via the duplication form (P') and recurse. For atomic-braid pair products $|V_i V_j| \in [1.148, 1.185]$, a single pentagon iteration suffices.

[`pentagon-reduction-li2q.witness.json`](../../folio-assistant/computations/pentagon-reduction-li2q.witness.json) records per-atom T3 contributions and the resulting binding-energy estimates.

## First-pass numerical results

Including T3 (pentagon-reduced) on top of PR #801's T1+T2:

| Atom | T1+T2 (PR #801) | T3 (pentagon, this) | T1+T2+T3 | B_pred (MeV) | B_AME (MeV) | ratio |
|---|---:|---:|---:|---:|---:|---:|
| D | 5.381 | +1.016 | 6.397 | 1.382 | 2.225 | 0.621 |
| T | 8.215 | +2.710 | 10.925 | 2.795 | 8.482 | 0.330 |
| ³He | 8.143 | +2.791 | 10.934 | 2.835 | 7.718 | 0.367 |

Comparison vs PR #801 (T1+T2 only):

| Atom | PR #801 ratio | This (with pentagon T3) | Movement |
|---|---:|---:|---|
| D | 0.704 | 0.621 | **worse by 12%** |
| T | 0.304 | 0.330 | better by 8% |
| ³He | 0.339 | 0.367 | better by 8% |

## Caveats

1. **Imaginary residue ≠ 0**. The pentagon-reduced T3 values have small but nonzero imaginary parts (0.16 for D, 0.48 for T, 0.47 for ³He) after taking 2·Re[Li_2^q(i√|z|)] - 2·Re[Li_2^q(α)]. Per (P) the imaginary parts should cancel exactly. The non-zero residue indicates either:
   - **Missing log-correction term** — classical Rogers' pentagon for Li_2 carries a $(1/2)\log^2(\cdot)$ correction that vanishes only at specific arguments. The paper's q-pentagon (per `q-dilogarithm.md`) is stated WITHOUT explicit log correction, but this needs verification: if the q-deformation truly cancels the log-squared, the imaginary residue should be zero up to numerical precision. The non-zero residue suggests we might be missing a "$+ \frac{1}{2} (\log_q u + \log_q v - \log_q uv)^2$" piece or similar.
   - **Series truncation precision loss** at the boundary $|z| \to q_0^-$.

2. **D got worse with T3 added**. T1+T2 gave 0.704; T3 adding pentagon-reduced contribution pushed ratio down to 0.621 for D. T and ³He improved marginally. This suggests T3 has the **wrong sign on D**, OR the pentagon reduction at $u = v$ degenerate factorisation has a sign issue. A non-degenerate factorisation $u = a$, $v = z/a$ for general $a \ne \sqrt{z}$ might give a cleaner result.

3. **Pure-imaginary u, v are a deliberate choice**. For real negative $z$, factoring $z = u \cdot v$ with real $u, v$ would require one negative and one positive, giving $|u| \cdot |v| = |z|$ — both sub-arguments would be real, but at least one of them must satisfy $|u| \ge \sqrt{|z|}$ which can still exceed $q_0$. Pure-imaginary $u = v = i\sqrt{|z|}$ symmetrically keeps both sub-moduli at $\sqrt{|z|}$, which IS below $q_0$ in our cases.

## Next steps

| # | Task |
|---|---|
| 1 | **Verify** the log-correction status of the paper's q-pentagon identity numerically: pick small convergent $x, y$, check $\sum$ matches both sides of (P) at 50 dps without the imaginary residue. |
| 2 | If (1) shows a missing term: **derive** the q-analog of Rogers' $\log^2$ correction; add to (P) in the implementation. |
| 3 | **Try alternative factorisations** of $z = u v$: e.g. $u = \sqrt{|z|} \cdot e^{i\theta}$, $v = \sqrt{|z|} \cdot e^{-i\theta}$ (a Bloch-Wigner-style choice that keeps $u, v$ complex-conjugate). |
| 4 | Once T3 is reliable, **add T4 (triple-products)** if structurally needed — the framework's m_first_order may itself be a truncation. |
| 5 | **Test on ⁴He** (n=12, deferred for compute time) once the formula is sign-consistent. |

## Cross-references

- [`pre-tau-vs-post-tau.md`](../../content/quantum-observable-universe/braids-and-knots/pre-tau-vs-post-tau.md) — the substrate-archimedean wall discipline.
- [`q-dilogarithm.md`](../../content/quantum-observable-universe/quantum-observable-universes/q-dilogarithm.md) — Li_2^q definition + pentagon identity.
- [`q-dilogarithm-unique.md`](../../content/quantum-observable-universe/quantum-observable-universes/q-dilogarithm-unique.md) — uniqueness of Li_2^q.
- [`binding_via_interface_knot.py`](../../folio-assistant/computations/binding_via_interface_knot.py) — PR #801 host script, T3 deferred.
- [`pentagon_reduction_li2q.py`](../../folio-assistant/computations/pentagon_reduction_li2q.py) — first-pass implementation.
- [`2026-05-19-weight-factor-audit.md`](2026-05-19-weight-factor-audit.md) — weight-family catalogue + KLR-positivity diagnostic.

## Open paper-side question

**Is the τ_arch-introduces-rational-denominators picture proved?**

The discipline is stated in `pre-tau-vs-post-tau.md` and the q-exp / Li_n^q chapters define their objects as Hopf grouplikes / level-k primitives (not series). But an explicit theorem of the form

> τ_arch ( ∑_n x^[n] ) = ∑_n x^n / n!

(where $x^{[n]}$ are divided powers and τ_arch maps them to rational-coefficient series in $\mathbb{R}$) does not appear as a stand-alone proven statement. The closest is the implicit usage in the q-exp definition (grouplike whose τ_arch image is the analytic exponential series) and the algebraic-quantum-volume → hyperbolic-volume bridge in [`kashaev-as-archimedean-realization.md`](../../content/quantum-observable-universe/braids-and-knots/kashaev-as-archimedean-realization.ts).

A unified statement — perhaps `prop:archimedean-divided-power-rationalisation` — would make this part of the framework explicit. Filing as a paper TODO.
