**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation
$\mathfrak{Q}_\beta(q) = Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot \prod_{k \ge 2}(1 + c_k u^k)$
with $u = b(q) \cdot \hbar_q^2$, any candidate Habiro element $F(q)$
generating the ladder coefficients $c_k$ must satisfy the classical-limit
shadows*

$$
\lim_{q \to 1} c_2(q) \;=\; -1 \qquad \text{and} \qquad
\lim_{q \to 1} c_3(q) \;=\; J_{\text{Hopf}}(q = 1) \;=\; -2.
$$

*A candidate failing either shadow is structurally REFUTED.*

## Role as the $\S 4(c)$ formalize-first gate

The refuted-class map (`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`)
$\S 4$ lists four structural invariants any candidate $F(q)$ must satisfy:

| # | invariant | formalised in |
|---|---|---|
| (a) | **Anchor-stable** (cross-anchor swing < 1 ppm) | [`prop:q-beta-radius-of-convergence-gate`](q-beta-radius-of-convergence-gate.md) |
| (b) | **Bar-even** under $q \mapsto q^{-1}$ | [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) |
| (c) | **q = 1 classical-limit shadow** | **this proposition** |
| (d) | **Direction sanity** | [`prop:q-beta-direction-sanity-gate`](q-beta-direction-sanity-gate.md) |

The q = 1 shadow invariant has **two canonical anchors** at the registry level:

- **$c_2 = -1$** is Taylor-exact ([`prop:q-beta-c-2-eq-neg-one-structural`](q-beta-c-2-eq-neg-one-structural.md)) — the structural seed of the entire ladder. Any candidate must reproduce this without fitting.
- **$c_3 \to J_{\text{Hopf}}(q = 1) = -2$** is the canonical Hopf-Jones limit (registry §3, [`canonical-derivation-chain.md`](../../../docs/canonical-derivation-cheat-sheet.md)) — the categorical anchor for the inter-block N=3 correction.

A candidate $F(q)$ whose Taylor expansion at $q = 1$ disagrees with either anchor fails the $\S 4(c)$ invariant, regardless of how cleanly it passes (a), (b), or (d). The two are independent: candidates can satisfy (a) + (b) (anchor-stable + bar-even) while still failing (c) if their classical-limit expansion gives the wrong integers.
## Use in the formalize-first checklist

This is **Step 5** of the 7-step Δ_λ pre-flight checklist (`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md` $\S 3$). Concretely, for any candidate $F(q)$:

1. Compute $F(q)$'s Taylor expansion at $q = 1$ (or take the limit if there's a removable singularity).
2. Read off the $c_2(q = 1)$ and $c_3(q = 1)$ coefficients in the ladder normalization.
3. If $c_2(q = 1) \neq -1$ or $c_3(q = 1) \neq -2$, REJECT — add a new row to refuted-class map $\S 2$.
4. If both shadows match, proceed to Step 6 (direction sanity) of the checklist.

## Composition with the prior three gates

A candidate $F(q)$ must clear (in order):

```
1. Bar-even check (§4b)        PASS (q ↔ q⁻¹ Taylor-even-in-t)
2. Radius-of-convergence (§4a) PASS (simple pole at u_substrate)
3. q = 1 shadow (§4c)          PASS (c_2 → −1, c_3 → −2)
4. Direction sanity (§4d)      PASS (|F(q_0)| in target's magnitude)
5. CFinite recurrence          PASS (generates c_k from kernel)
```

With all four §4 invariants formalized, the formalize-first gate chain is complete; any future $F(q)$ candidate is evaluable as a Lean class-instance attempt rather than as a canonical fit.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
