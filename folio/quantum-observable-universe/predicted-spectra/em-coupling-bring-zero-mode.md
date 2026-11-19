**Proposition (additive Bring-surface zero-mode form for $1/\alpha_{EM}$, conditional on [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit) and Bloch-Suslin pentagon-uniqueness [`suslin1991`]).**
*Let $g = 4$ denote the genus of Bring's surface. This is the unique Riemann surface supporting the genus-$4$ torus knots $T_{2,9}$ and $T_{3,5}$ ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)). Assume the upstream typeclasses `QOU.QPochhammer.ArchimedeanLimit`, `QOU.Archimedean.BlochSuslinUniqueness`, and `QOU.Archimedean.BringZeroModeBlochClass` are inhabited ([`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)). Then*

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

Evaluation at the canonical proton pin $q_0 = {{ qou.computations.alpha-em-form-ladder.data.ladder.proton.q0 | precision: 16 }}\ldots$ using 60-dps precision yields:

| Quantity | Value |
|----------|------:|
| $q\cdot[9]_q\cdot[10]_q$ (tree level) | ${{ qou.computations.alpha-em-form-ladder.data.ladder.proton.tree | precision: 12 }}\ldots$ |
| $2/(3\pi) = 2g/(4\pi(g-1))$ (Bring zero-mode) | ${{ qou.computations.alpha-em-form-ladder.data.ladder.proton.zero_mode | precision: 9 }}\ldots$ |
| Tree $+$ Bring zero-mode sum | ${{ qou.computations.alpha-em-form-ladder.data.ladder.proton.additive | precision: 12 }}\ldots$ |
| Form A quadratic fixed point ($+\alpha H$, $H = [2]_q/(8\pi)$) | ${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_alpha_inv | precision: 13 }}$ |
| Form B cubic Schwinger fixed point ($+\alpha H(1 - h^2\alpha)$) | ${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_alpha_inv | precision: 13 }}$ |
| CODATA-2022 $1/\alpha$ | ${{ qou.computations.alpha-em-schwinger-ladder.data.codata_reference.alpha_inv | precision: 12 }}(21)$ |
| **Tree $+$ zero-mode residual** | $\mathbf{{{ qou.computations.alpha-em-form-ladder.data.ladder.proton.additive_resid_ppb | precision: 4 }}\;\mathrm{ppb}}$ ($\mathbf{-4.26 \times 10^{-6}}$) |
| **Form A quadratic residual** | $\mathbf{+{{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_no_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}}$ (${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_sigma | precision: 3 }}\,\sigma_\alpha$) |
| **Form B cubic Schwinger residual** | $\mathbf{{{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}}$ (${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_sigma | precision: 3 }}\,\sigma_\alpha$) |

The self-consistent one-loop term $\alpha H$ with $H = [2]_q/(8\pi) \approx 5.839 \times 10^{-4}$ reduces the relative residual from ${{ qou.computations.alpha-em-form-ladder.data.ladder.proton.additive_resid_ppb | precision: 4 }}\;\mathrm{ppb}$ to $+{{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_no_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}$, and retaining the Hecke–Schwinger factor $(1 - h^2\alpha)$ ($h = q - q^{-1}$) brings the residual to ${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}$ (${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_sigma | precision: 3 }}\,\sigma_\alpha$ against the CODATA-2022 standard uncertainty $\sigma_\alpha = {{ qou.computations.alpha-em-schwinger-ladder.data.codata_reference.sigma_ppb | precision: 4 }}\;\mathrm{ppb}$). At the ideal muon pin $q_0 = {{ qou.computations.alpha-em-form-ladder.data.ladder.muon.q0 | precision: 16 }}\ldots$, the tree level is ${{ qou.computations.alpha-em-form-ladder.data.ladder.muon.tree | precision: 12 }}$, the tree-plus-zero-mode sum is ${{ qou.computations.alpha-em-form-ladder.data.ladder.muon.additive | precision: 12 }}$ (${{ qou.computations.alpha-em-form-ladder.data.ladder.muon.additive_resid_ppb | precision: 4 }}\;\mathrm{ppb}$), and the Form-A quadratic fixed point has residual $+{{ qou.computations.alpha-em-form-ladder.data.ladder.muon.fixed_point_resid_ppb | precision: 4 }}\;\mathrm{ppb}$.

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

| Form | Type | Residual at proton $q_0$ | Structural status |
|------|------|--------------------------|-------------------|
| Bare $q[9]_q[10]_q$ | multiplicative tree | $-1.553\times 10^{-3}$ | Derived |
| [`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons) | multiplicative + Gram-det $\kappa$ | $-4.68\times 10^{-7}$ ($-468\;\mathrm{ppb}$) | $\kappa$ unproved |
| **Additive Bring zero-mode** | $q[9]_q[10]_q + 2g/(4\pi(g-1))$ | $-4.26\times 10^{-6}$ (${{ qou.computations.alpha-em-form-ladder.data.ladder.proton.additive_resid_ppb | precision: 4 }}\;\mathrm{ppb}$) | **Geometrically clean; one Bring-genus-4 quantity in each term** |
| **Form A (Bring + 1-loop $\alpha H$)** | quadratic fixed point, $H = [2]_q/(8\pi)$ | $+{{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_no_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}$ (${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_sigma | precision: 3 }}\,\sigma_\alpha$) | Conditional fixed-point closure |
| **Form B (Bring + Schwinger $\alpha H(1 - h^2\alpha)$)** | cubic fixed point, $h = q - q^{-1}$ | ${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}$ (${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_sigma | precision: 3 }}\,\sigma_\alpha$) | Conditional fixed-point + Hecke–Schwinger cubic |

The additive form provides the cleanest structure. It avoids fitted coefficients. Every factor maps to a known geometric or topological invariant of Bring's surface.

## Witness

See [`alpha-em-form-ladder.witness.json`](../../../computations/alpha-em-form-ladder.witness.json) and [`alpha-em-schwinger-ladder.witness.json`](../../../computations/alpha-em-schwinger-ladder.witness.json) for the 60-dps proton- and muon-pinned ladder evaluations.
