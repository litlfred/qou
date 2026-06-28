**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation
$\mathfrak{Q}_\beta(q) = Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot \prod_{k \ge 2}(1 + c_k u^k)$
with $u = b(q) \cdot \hbar_q^2$, the log-correction generating function*

$$
g(u) \;:=\; \sum_{k \ge 2} c_k \cdot u^k
$$

*has a simple pole at $u = u_{\text{substrate}} \approx 0.00852$, and the
ratio test for the radius of convergence yields*

$$
\lim_{k \to \infty} \frac{|c_{k+1}|}{|c_k|} \;=\; \frac{1}{u_{\text{substrate}}}.
$$

*Consequently, any candidate Habiro element $F(q)$ whose log-correction
generating function has its nearest singularity elsewhere than
$u_{\text{substrate}}$ is structurally REFUTED as a valid $\mathfrak{Q}_\beta$
precision-ladder kernel.*

## Role as the $\S 4(a)$ formalize-first gate

The refuted-class map (`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`)
$\S 4$ lists four structural invariants any candidate $F(q)$ must satisfy:

| # | invariant | formalised in |
|---|---|---|
| (a) | **Anchor-stable** (cross-anchor $u_{\text{substrate}}$ swing < 1 ppm = $10^{-6}$ relative; 210 ppb observed) | **this proposition** |
| (b) | **Bar-even** under $q \mapsto q^{-1}$ | [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) |
| (c) | **q = 1 shadow** reproduces known integer (e.g. $c_3 \to J_{\text{Hopf}}(1) = -2$) | *not yet formalised* |
| (d) | **Direction sanity** — $|F(q_0)|$ scales appropriately | *not yet formalised* |

The radius-of-convergence gate is the **sharpest concrete form** of $\S 4(a)$:
The cross-anchor analysis established that $u_{\text{substrate}}$ at $q_{\text{muon}}$ vs
$q_{\text{proton}}$ differs by only **210 ppb** (well within the 1 ppm
fibre-level tolerance), so the simple-pole location IS anchor-stable; a
candidate $F(q)$ violating this is automatically anchor-incompatible.
## Use in the formalize-first checklist

This is **Step 4** of the 7-step Δ_λ pre-flight checklist
(`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md` $\S 3$).
Concretely, for any candidate $F(q)$:

1. Express $F(q)$ as a rational function $P(u) / Q(u)$ in $u = b \cdot \hbar_q^2$
   (or a power series with explicit recursion via `CFinite`).
2. Locate the nearest pole $u_0$ in the $u$-plane.
3. Compute $|u_0 - u_{\text{substrate}}| / u_{\text{substrate}}$.
4. If the ratio $> 10^{-6}$, REJECT — add a new row to refuted-class map $\S 2$.
5. If the ratio $\le 10^{-6}$, proceed to Step 5 (q=1 shadow) of the checklist.

## Composition with the bar-even gate and the `CFinite` engine

A candidate $F(q)$ must clear (in order):

```
1. Bar-even check        →  bar-even gate (q ↦ q⁻¹ Taylor-even-in-t)
2. Radius-of-convergence →  this proposition (simple pole at u_substrate)
3. CFinite recurrence    →  CFinite engine (generates c_k from kernel + seed)
4. q=1 shadow            →  not yet formalised (c_2 = −1, c_3 = J_Hopf(1) = −2 anchors)
5. Direction sanity      →  not yet formalised (|F(q_0)| in target's magnitude range)
```

Steps 1–3 are formalised in Lean (sorry-free); steps 4–5 are not yet formalised.
