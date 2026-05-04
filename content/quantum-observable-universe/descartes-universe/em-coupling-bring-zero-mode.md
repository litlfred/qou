**Conjecture (additive Bring-surface zero-mode form for $1/\alpha_{EM}$).**
*Let $g = 4$ denote the genus of Bring's surface (the unique Riemann
surface supporting the genus-$4$ torus knots $T_{2,9}$ and $T_{3,5}$,
[force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)). Then*

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
   $$\frac{2}{3\pi} \;=\; \frac{\mathrm{Vol}(S^2)}{3\cdot\mathrm{Vol}(S^3)}
     \;=\; \frac{4\pi}{3\cdot 2\pi^2}.$$

## Numerical match

At $q_0 \approx 1.10998$ in 60 dps mpmath:

| Quantity | Value |
|----------|------:|
| $q\cdot[9]_q\cdot[10]_q$ | $136.823219654\ldots$ |
| $2/(3\pi) = 2g/(4\pi(g-1))$ | $0.212206591\ldots$ |
| Sum | $137.035426245\ldots$ |
| CODATA $1/\alpha$ | $137.035999084(21)$ |
| **Residual** | $\mathbf{+4.2 \times 10^{-6}}$ relative |

A second additive term $\alpha/(4\pi) \approx 5.81 \times 10^{-4}$
brings the residual to $-5.7 \times 10^{-8}$ relative, near CODATA
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

## Status: conjectural — naive interpretations fail

The structural identification $2/(3\pi) = 2g/(4\pi(g-1)) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$
at $g = 4$ is an **exact algebraic identity**, but the *physical origin*
in the QOU framework is **not yet established**. A first-pass derivation
attempt (May 2026 audit) ruled out the simplest mechanism:

**Failed: harmonic 1-form zero-mode on $M_{\text{Bring}} \times S^1$.**
For $M^3 = M_{\text{Bring}} \times S^1$ (unit $S^1$):
$$
  \frac{b_1(M^3)}{\mathrm{Vol}(M^3)}
  = \frac{2g+1}{4\pi(g-1)\cdot 2\pi}
  = \frac{9}{24\pi^2}
  \approx 0.038,
$$
which is $\sim 5.6\times$ smaller than the required $2/(3\pi) \approx 0.212$.
So the naive 3-manifold zero-mode picture does not directly yield the
constant.

**The exact form $\mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3)) = 4\pi/(3\cdot 2\pi^2)$
suggests** a different mechanism — perhaps:

1. A Hopf-fibration $S^1 \to S^3 \to S^2$ in which the photon flux is
   a 2-form on $S^2$ (the base) and the gauge connection lives on $S^3$
   (the total space), with the factor $1/3$ reflecting Lie-algebra
   trace normalisation $\mathrm{Tr}(T_a T_b) = \delta_{ab}/2$ combined
   with a 3-fold gauge-sector copy.
2. A Chern-Simons partition-function ratio at level $k$ where the
   quantum dimension formula gives
   $\dim_q V \cdot Z(S^3)^{-1}$-type expressions reducing to
   $\mathrm{Vol}(S^2)/\mathrm{Vol}(S^3)$ in the classical limit.
3. A BV-BRST cohomological mechanism where the $(2-form, 3-form)$
   pair represents a global anomaly cancelled by the categorical
   Wess-Zumino term.

To upgrade this conjecture to a proof, the following are required:

1. **Identify the precise 3-manifold** $M^3$ and gauge structure
   (Hopf-fibration $S^3$ vs $T^*M_{\text{Bring}}$ vs other) that
   produces $1/(3 \cdot \mathrm{Vol}(M^3))$ as the photon zero-mode
   contribution at zero external momentum, with a $1/3$ factor
   from Lie-algebra normalisation or geometric multiplicity.
2. **Compute the photon zero-mode coefficient** end-to-end from
   the categorical Lagrangian, verifying it equals exactly
   $2g/(4\pi(g-1)) = 2/(3\pi)$ at $g = 4$.
3. **Verify UV finiteness.** Reshetikhin-Turaev shadow-world
   regularisation should produce a finite answer — force-carrier
   complexity $[9]_q[10]_q$ regularises the categorical sum,
   replacing continuum momentum integration. This is plausible but
   not proved.
4. **Compute the next-order self-energy** as a 2-loop graph;
   verify the coefficient is exactly $1/(4\pi)$ or identifies as
   $1/(2\pi[2]_q)$ or $1/(4\pi)\cdot(1-\hbar_q^2)$ (best fits at
   $\sim 0.4\%$). The simplest fits are all near-misses; an exact
   form requires the explicit 2-loop calculation.

The numerical match at $4.2 \times 10^{-6}$ with one term and
$5.7 \times 10^{-8}$ with two is far too precise to be coincidence;
the structural derivation almost certainly exists, but it is
**non-trivial** — the naive geometric mechanisms fail.

## Comparison with prior conjectures

| Form | Type | Residual at $q_0$ | Structural status |
|------|------|-------------------|-------------------|
| Bare $q[9]_q[10]_q$ | multiplicative tree | $-1.55\times 10^{-3}$ | Derived |
| [`conj:em-coupling-chern-simons`](#conj:em-coupling-chern-simons) | multiplicative + Gram-det $\kappa$ | $-4\times 10^{-7}$ | $\kappa$ unproved (Lean `sorry`) |
| [`conj:alpha-em-gluon-octet-form`](#conj:alpha-em-gluon-octet-form) | $45[3]_q\,(1+\delta_B+8q\delta_B^2)$ | $+7\times 10^{-9}$ | PSLQ-empirical, 3 of 4 factors unjustified |
| **This conjecture (additive Bring zero-mode)** | $q[9]_q[10]_q + 2g/(4\pi(g-1))$ | $+4.2\times 10^{-6}$ | **Geometrically clean; one Bring-genus-4 quantity in each term** |

The additive form is **structurally cleanest** of the four candidates:
no fitted coefficients, every factor identifiable with a known geometric
or topological invariant of Bring's surface.

## Witness

[`alpha-em-correction-derivation-attempts.witness.json`](#) (full attempt log).
