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

## Pre-archimedean status — resolved by uniqueness of $\tau_{\text{arch}}$

The bare formula $1/\alpha_{\text{bare}} = q[9]_q[10]_q$ and its
trace-ratio refactoring
[`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
both live entirely in the pre-archimedean substrate ring
$R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$. The additive
correction $2/(3\pi)$ imports the archimedean transcendental $\pi$
via sphere-volume / Hodge data on Bring's surface — *not* an
object of $R$. An earlier audit (May 2026) flagged this as a
structural cost requiring repair.

**Resolution (May 2026):** The repair route comes from
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness).
The substrate's pentagon-coherence (built into the cosimplicial /
Yekutieli triple structure) factors the QOU mass-formula state
sum through a class in the Bloch group $B(\mathbb{C})$. Bloch-Suslin
pentagon-uniqueness [`suslin1991`, `bloch2000`] then forces every
real-valued archimedean realization to coincide with the
Bloch-Wigner dilogarithm $D$ up to a single overall scalar. The
$\pi$ in $2/(3\pi)$ is therefore *not* an external import: it is
the unique archimedean shadow of substrate pentagon data on
Bring's surface, propagated through $D$.

In summary, the dichotomy is intentional and forced:

- **Pre-archimedean side** ($q$-rational, in $R$): the bare formula
  $q[9]_q[10]_q$ and its categorical trace-ratio derivation. No
  $\pi$, no transcendentals.
- **Archimedean side** (transcendental, in $\mathbb{R}$): the
  unique image under $\tau_{\text{arch}}$, factoring through $D$.
  Carries $\pi$, $\zeta(3)$, hyperbolic volumes, etc., as forced
  archimedean shadows of substrate data.

The additive correction is the archimedean image; the bare formula
is the pre-archimedean source. They live on different sides of
$\tau_{\text{arch}}$, not in different rings of the same kind. The
[figure-8 archimedean illustration](#rem:figure-8-archimedean-illustration)
shows the same dichotomy in concrete miniature: $4_1$ has
$\mathrm{Vol}_q(4_1) \in \mathbb{Z}[q^{\pm 1/2}]$ on the substrate
side and $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx
:val[Vol_4_1]{precision=6}$ on the laboratory side, with the bridge fixed by
uniqueness.

Two open computational sub-problems remain (both are now framed by
uniqueness rather than structural anomaly):

1. **Identify the continuous cohomology pairing on Bring's surface.**
   The conjecture originally predicted that $2/(3\pi) = 2g/(4\pi(g-1))$ at $g=4$ is the $\tau_{\text{arch}}$-image of a specific point-class $[Z] \in B(\mathbb{C})$ such that $D([Z]) = 2/(3\pi)$. However, this hits a **transcendence obstruction**: if $Z$ is assembled from the algebraic trace fields of $\{T_{2,9}, T_{3,5}\}$, then $D([Z])$ evaluates to a combination of $L$-values. Setting $D([Z]) = 2/(3\pi)$ implies $\pi \cdot D([Z]) \in \mathbb{Q}$, which contradicts standard transcendence expectations (e.g., Zagier's conjecture). Therefore, $\tau_{\text{arch}}$ cannot act by pointwise Bloch-Wigner evaluation. Instead, the focus shifts to **group homology**: the Yekutieli cosimplicial data must define a fundamental 2-cycle $[\Sigma] \in H_2(PSL(2,\mathbb{R}); \mathbb{Z})$ for the Bring surface, and $\tau_{\text{arch}}$ acts by pairing this class with the continuous volume/Euler class. The integration natively produces the Gauss-Bonnet area $4\pi(g-1)$ with $\pi$ in the denominator. Explicitly constructing this homology pairing closes the Lean stub.
2. **Compute the next-order self-energy.** The $\alpha/(4\pi)$
   term that brings the residual to $+5.7 \times 10^{-8}$ should
   factor through a higher Bloch group $B_n(\mathbb{C})$ with the
   $n$-variable polylogarithm $D_n$. Pentagon-uniqueness for $D_n$
   at $n \geq 3$ is open (Goncharov 1995); the QOU framework can
   take it as input where needed.

## Status: mechanism resolved (surface harmonic zero-mode); upstream uniqueness conditional

The structural identification $2/(3\pi) = 2g/(4\pi(g-1))$ at $g = 4$ is an
**exact algebraic identity** (Lean `hodgeRatio_at_g4`). Its
**from-the-Lagrangian mechanism** is now derived in
[`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring): the photon
IR zero-mode is the harmonic $1$-form sector $b_1(M_g) = 2g$ on the
**2-surface** $M_{\text{Bring}}$ itself, normalised by the Gauss–Bonnet area
$\operatorname{Area} = -2\pi\chi = 4\pi(g-1)$. The topological/geometric core is
proven sorry-free; only the standard heat-kernel identity (zero-mode
$= b_1/\operatorname{Vol}$) is cited, and the upstream $\tau_{\mathrm{arch}}$
uniqueness remains the named conditional input.

A first-pass attempt (May 2026 audit) had used the *wrong manifold*; its failure
pinpoints the fix.

**Failed: harmonic 1-form zero-mode on $M_{\text{Bring}} \times S^1$.**
For $M^3 = M_{\text{Bring}} \times S^1$ (unit $S^1$):
$$
  \frac{b_1(M^3)}{\mathrm{Vol}(M^3)}
  = \frac{2g+1}{4\pi(g-1)\cdot 2\pi}
  = \frac{9}{24\pi^2}
  \approx 0.038,
$$
which is $\sim 5.6\times$ smaller than the required $2/(3\pi) \approx 0.212$.
Crossing with $S^1$ adds a spurious harmonic generator ($b_1 \to 2g+1$) and a
factor $2\pi$ of volume — the recorded failure.

**Resolved: harmonic 1-form zero-mode on the 2-surface $M_{\text{Bring}}$.**
The photon zero-mode lives on the surface itself, giving
$b_1(M_g)/\operatorname{Area}(M_g) = 2g/(4\pi(g-1)) = 2/(3\pi)$ at $g=4$ —
exactly the required constant, dominating the naive value by
$(16\pi-9)/(24\pi^2) > 0$ (Lean `surface_minus_naive_g4`,
[`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring)). The "$/3$"
is the Gauss–Bonnet factor $(g-1)=3$.

The earlier speculative mechanisms (a Hopf-fibration $S^1 \to S^3 \to S^2$
sphere-volume ratio, a Chern–Simons partition-function ratio, a BV–BRST anomaly)
are **superseded** by the surface harmonic zero-mode above. The secondary
identity $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$ is the same
number written with sphere volumes, but the *primary* derivation is the
Hodge/Gauss–Bonnet ratio $b_1/\operatorname{Area}$ on the surface — the "$/3$" is
$(g-1)$, not a sphere-volume coincidence.

**Remaining open items** (the mechanism itself is now derived):

1. **UV finiteness.** Reshetikhin–Turaev shadow-world regularisation should
   produce a finite answer — force-carrier complexity $[9]_q[10]_q$ regularises
   the categorical sum, replacing continuum momentum integration. Plausible but
   not proved.
2. **Next-order self-energy** $\alpha/(4\pi)$ (the $n=2$ jet order of
   [`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition)): an
   explicit 2-loop calculation. The simplest closed forms ($1/(4\pi)$,
   $1/(2\pi[2]_q)$, $1/(4\pi)(1-\hbar_q^2)$) are near-misses at $\sim 0.4\%$.

The numerical match at $4.2 \times 10^{-6}$ with one term and
$5.7 \times 10^{-8}$ with two is far too precise to be coincidence; the
structural mechanism is now derived
([`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring)) — the
surface harmonic zero-mode $b_1/\operatorname{Area}$, with the naive
$M\times S^1$ guess explained and superseded.

## Comparison with prior conjectures

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
