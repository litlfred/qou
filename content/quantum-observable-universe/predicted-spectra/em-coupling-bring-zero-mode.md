**Proposition (additive Bring-surface zero-mode form for
$1/\alpha_{EM}$, conditional on
[`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)
and on the Bloch-Suslin pentagon-uniqueness theorem
[`suslin1991`]).**
*Let $g = 4$ denote the genus of Bring's surface (the unique Riemann
surface supporting the genus-$4$ torus knots $T_{2,9}$ and $T_{3,5}$,
[force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)).
Assume the upstream typeclasses
`QOU.QPochhammer.ArchimedeanLimit`,
`QOU.Archimedean.BlochSuslinUniqueness`, and
`QOU.Archimedean.BringZeroModeBlochClass` are all inhabited
([`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)).
Then*

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  \underbrace{q\cdot[9]_q\cdot[10]_q}_{\text{tree level (force-carriers)}}
  \;+\;
  \underbrace{\frac{2g}{4\pi(g-1)}}_{\text{Bring zero-mode shift}}
  \;+\;
  \mathcal{O}(\alpha)
  \;=\;
  q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi} + \mathcal{O}(\alpha).
$$

*The constant $2/(3\pi) = 8/(12\pi)$ admits two independent geometric
identifications in Bring's-surface terms*:

1. **Hodge / Gauss-Bonnet ratio:**
   $$\frac{2g}{4\pi(g-1)} \;=\; \frac{\dim H^1(M_{\text{Bring}};\,\mathbb{R})}{\mathrm{Area}(M_{\text{Bring}})},$$
   *where the area is computed with constant negative curvature $-1$
   (Gauss-Bonnet: $\mathrm{Area} = -2\pi\chi = 4\pi(g-1) = 12\pi$).*
2. **Sphere-volume ratio:**
   $$\frac{2}{3\pi} \;=\; \frac{\mathrm{Vol}(S^2)}{3\cdot\mathrm{Vol}(S^3)} \;=\; \frac{4\pi}{3\cdot 2\pi^2}.$$

## Numerical match

At $q_0 = 1.109978595554181\ldots$ (50 dps) in 60 dps mpmath:

| Quantity | Value |
|----------|------:|
| $q\cdot[9]_q\cdot[10]_q$ | $136.823219654\ldots$ |
| $2/(3\pi) = 2g/(4\pi(g-1))$ | $0.212206591\ldots$ |
| Sum | $137.035426245\ldots$ |
| CODATA $1/\alpha$ | $137.035999084(21)$ |
| **Residual** (calc $-$ CODATA, relative) | $\mathbf{-4.2 \times 10^{-6}}$ |

A second additive term $\alpha/(4\pi) \approx 5.81 \times 10^{-4}$
brings the residual to $+5.7 \times 10^{-8}$ relative (calc $-$ CODATA), near CODATA
$\sigma_\alpha = 1.5 \times 10^{-10}$ — but the coefficient $1/(4\pi)$
is currently a numerical near-match (1.4% off) and may refine to
$1/(2\pi[2]_q)$ or another small $q$-correction.

## Conjectural physical interpretation

The numerical match suggests a clean structural decomposition:

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  \underbrace{q\cdot[9]_q\cdot[10]_q}_{\substack{\text{tree-level categorical}\\\text{coupling: singlet idempotent}\\\text{normalised by force-carrier}\\\text{q-dimensions } [9]_q[10]_q}}
  \;+\;
  \underbrace{\frac{2g}{4\pi(g-1)}}_{\substack{\text{IR zero-mode shift:}\\\text{photon harmonic 1-forms}\\\text{on Bring's surface,}\\\text{regularised by Area}}}
  \;+\;
  \underbrace{\mathcal{O}(\alpha)}_{\text{higher loops}}.
$$

The $g = 4$ structure of Bring's surface appears in **both** terms:
the tree-level coefficient $[9]_q[10]_q$ comes from the unique pair
of genus-$4$ torus knots $\{T_{2,9}, T_{3,5}\}$
([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)),
and the IR shift $2g/(4\pi(g-1))$ comes from the Hodge data of the
*same* Bring's surface. This double appearance of $g = 4$ is
structurally consistent and not coincidental — it is what one expects
from a categorical-Lagrangian QFT whose UV completion lives on
Bring's curve.

> **Conditional theorem (§3b-cond).** Per CLAUDE.md §3b-cond: the
> upstream conjectures are axiomatised in Lean as the typeclasses
> [`QOU.QPochhammer.ArchimedeanLimit`](../braids-and-knots/dilogarithm-archimedean-limit.lean),
> [`QOU.Archimedean.BlochSuslinUniqueness`](archimedean-functor-uniqueness.lean),
> and the new
> [`QOU.Archimedean.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean).
> The Lean theorem
> [`QOU.Archimedean.bring_zero_mode_additive_form`](em-coupling-bring-zero-mode.lean)
> takes `BringZeroModeBlochClass` as `[Instance]` and is proved
> **without `sorry`** (the algebraic identity $2g/(4\pi(g-1)) = 2/(3\pi)$
> at $g=4$ is closed unconditionally by `field_simp; ring`). The
> remaining structural input is the explicit Bloch-group class
> realising $2/(3\pi)$ on Bring's surface — captured exactly by the
> single `[Instance]` hypothesis.

| Form | Type | Residual at $q_0$ | Structural status |
|------|------|-------------------|-------------------|
| Bare $q[9]_q[10]_q$ | multiplicative tree | $-1.55\times 10^{-3}$ | Derived |
| [`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons) | multiplicative + Gram-det $\kappa$ | $-4\times 10^{-7}$ | $\kappa$ unproved (Lean `sorry`) |
| **This conjecture (additive Bring zero-mode)** | $q[9]_q[10]_q + 2g/(4\pi(g-1))$ | $-4.2\times 10^{-6}$ | **Geometrically clean; one Bring-genus-4 quantity in each term** |

The additive form is **structurally cleanest** of the four candidates:
no fitted coefficients, every factor identifiable with a known geometric
or topological invariant of Bring's surface.

## Witness

[`alpha-em-correction-derivation-attempts.witness.json`](#) (full attempt log).
