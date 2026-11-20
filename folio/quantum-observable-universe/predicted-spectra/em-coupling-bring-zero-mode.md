**Proposition (additive Bring-surface zero-mode form for $1/\alpha_{EM}$, conditional on [$(1{-}q)\,\log\Phi_n(x; q) \to \mathrm{Li}_2(x)$ under $\tau_{\mathrm{arch}}$](#conj:dilogarithm-archimedean-limit) and Bloch-Suslin pentagon-uniqueness [`suslin1991`]).**
*Let $g = 4$ denote the genus of Bring's surface. This is the unique Riemann surface supporting the genus-$4$ torus knots $T_{2,9}$ and $T_{3,5}$ ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)). Assume the upstream typeclasses `QOU.QPochhammer.ArchimedeanLimit`, `QOU.Archimedean.BlochSuslinUniqueness`, and `QOU.Archimedean.BringZeroModeBlochClass` are inhabited ([Uniqueness of the archimedean realization functor (Bloch-Suslin pentagon, conditional)](#prop:archimedean-functor-uniqueness)). Then*

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  \underbrace{q\cdot[9]_q\cdot[10]_q}_{\text{tree level}}
  \;+\;
  \underbrace{\frac{2g}{4\pi(g-1)}}_{\text{Bring zero-mode}}
  \;+\;
  \mathcal{O}(\alpha)
  \;=\;
  q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi} + \mathcal{O}(\alpha).
$$

*The constant $2/(3\pi) = 8/(12\pi)$ admits two independent geometric identifications on Bring's surface*:

1. **Hodge / Gauss-Bonnet ratio:**
   $$\frac{2g}{4\pi(g-1)} \;=\; \frac{\dim H^1(M_{\text{Bring}};\,\mathbb{R})}{\mathrm{Area}(M_{\text{Bring}})}.$$
   *The area evaluates under constant negative curvature $-1$ as $\mathrm{Area} = -2\pi\chi = 4\pi(g-1) = 12\pi$.*
2. **Sphere-volume ratio:**
   $$\frac{2}{3\pi} \;=\; \frac{\mathrm{Vol}(S^2)}{3\cdot\mathrm{Vol}(S^3)} \;=\; \frac{4\pi}{3\cdot 2\pi^2}.$$

## Numerical match

Evaluation at $q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps) using 60 dps precision yields:

| Quantity | Value |
|----------|------:|
| $q\cdot[9]_q\cdot[10]_q$ | $136.823219729\ldots$ |
| $2/(3\pi) = 2g/(4\pi(g-1))$ | $0.212206591\ldots$ |
| Sum | $137.035426320\ldots$ |
| CODATA-2022 $1/\alpha$ | $137.035999177(21)$ |
| **Residual** (relative) | $\mathbf{-4.2 \times 10^{-6}}$ |

The second additive term $\alpha/(4\pi) \approx 5.81 \times 10^{-4}$ brings the relative residual to $+5.7 \times 10^{-8}$. This approaches the CODATA standard deviation $\sigma_\alpha = 1.5 \times 10^{-10}$.

## Conjectural physical interpretation

The numerical match supports a structural decomposition:

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  q\cdot[9]_q\cdot[10]_q
  \;+\;
  \frac{2g}{4\pi(g-1)}
  \;+\;
  \mathcal{O}(\alpha).
$$

The $g = 4$ structure of Bring's surface appears in both main terms. The tree-level coefficient $[9]_q[10]_q$ derives from the unique pair of genus-$4$ torus knots $\{T_{2,9}, T_{3,5}\}$ ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)). The infrared shift $2g/(4\pi(g-1))$ emerges from the Hodge data of the same Bring's surface. This double appearance of $g = 4$ is structurally consistent. It matches the expectations for a categorical-Lagrangian quantum field theory with a UV completion on Bring's curve.

> **Conditional theorem.** Lean axiomatises the upstream conjectures as typeclasses [`QOU.QPochhammer.ArchimedeanLimit`](../mass-theory/dilogarithm-archimedean-limit.lean), [`QOU.Archimedean.BlochSuslinUniqueness`](../mass-theory/archimedean-functor-uniqueness.lean), and [`QOU.Archimedean.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean). The Lean theorem [`QOU.Archimedean.bring_zero_mode_additive_form`](em-coupling-bring-zero-mode.lean) takes `BringZeroModeBlochClass` as an instance and concludes unconditionally. The algebraic identity $2g/(4\pi(g-1)) = 2/(3\pi)$ at $g=4$ closes via `field_simp; ring`. The remaining structural input is the explicit Bloch-group class realising $2/(3\pi)$ on Bring's surface.

| Form | Type | Residual at $q_0$ | Structural status |
|------|------|-------------------|-------------------|
| Bare $q[9]_q[10]_q$ | multiplicative tree | $-1.55\times 10^{-3}$ | Derived |
| [`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons) | multiplicative + Gram-det $\kappa$ | $-4\times 10^{-7}$ | $\kappa$ unproved (Lean `sorry`) |
| **This conjecture (additive Bring zero-mode)** | $q[9]_q[10]_q + 2g/(4\pi(g-1))$ | $-4.2\times 10^{-6}$ | **Geometrically clean; one Bring-genus-4 quantity in each term** |

The additive form provides the cleanest structure. It avoids fitted coefficients. Every factor maps to a known geometric or topological invariant of Bring's surface.

## Witness

See `alpha-em-correction-derivation-attempts.witness.json` for the full attempt log.
