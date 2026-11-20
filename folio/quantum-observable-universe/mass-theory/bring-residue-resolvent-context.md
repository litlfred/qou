## The shared smaller-scope open math, now scaffolded

The α_shift universal derivation chain identified the pole-order origin
of the q-integer indices in several "empirical" fits.  What remained shared across the α_EM, p-n averaging,
and meson m_K/m_π treatments was
the residue/resolvent step: deriving the closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$ from the contour-integral
evaluation on Bring's surface.

This proposition reduces that derivation to a single hypothesis
together with a theorem, then specialises to the three concrete pole
orders used downstream.

## Structure of the reduction

- **Hypothesis (pole non-vanishing at order $n$).** Over a field, the
  contour-integral / Schwarz-integral input is axiomatised by the single
  condition $1 - h_q \cdot q^n \neq 0$ — the **pole non-vanishing**, the
  substantive output any concrete contour route must establish.
- **Resolvent equation.** Given the hypothesis, the canonical resolvent
  $F_n(q) = (1 - h_q \cdot q^n)^{-1}$ satisfies
  $(1 - h_q \cdot q^n) \cdot F_n(q) = 1$.
- Three specialisations:
  - pole order 10, used by p-n averaging
    ([p-n averaging uniqueness](#prop:pn-averaging-uniqueness));
  - pole order 9, used by 1/α_EM
    ([fine-structure observation](#rem:fine-structure-observation));
  - pole orders 3 and 4, used by
    $m_K^2/m_\pi^2$
    ([meson color-tube uniqueness](#prop:meson-color-tube-uniqueness)).

## Establishing the hypothesis

Establishing the pole non-vanishing hypothesis at order $n$ requires either:

1. **Analytic route:** residue calculus (removable singularities and
   circle integrals) applied to the
   $\sigma$-action on Hecke representations at the torus-knot
   surface.
2. **Algebraic route:** via the substrate's Bloch-Suslin framework
   of the [Bring zero mode](#prop:em-coupling-bring-zero-mode),
   identifying the contour integral with a specific Bloch-group
   class on Bring's surface (the open computational sub-problem
   already scoped there).

Both routes converge on the same closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$.  Until the hypothesis is
established, the statement is the
**conditional uniqueness** of the resolvent form.

## Downstream consequence

Each specialisation collapses a separate residue-normalisation gap
into a **single shared open hypothesis**:

| where used | downstream form | pole order $n$ |
|---|---|---|
| [fine-structure observation](#rem:fine-structure-observation) | $1/\alpha_{\rm EM} = q \cdot [9]_q \cdot [10]_q + 2/(3\pi)$ | $9$ and $10$ (genus-4 pair) |
| [p-n averaging uniqueness](#prop:pn-averaging-uniqueness) | $\sigma_{pn}(q)$ Bring color-tube weight $1/(1 - h_q \cdot q^{10})$ | $10$ |
| [meson color-tube uniqueness](#prop:meson-color-tube-uniqueness) | $m_K^2 / m_\pi^2 = [3]_q \cdot [4]_q$ | $3$ and $4$ (meson pair) |

Establishing the hypothesis once therefore discharges the residue open
math in all three cases.

## Status

This proposition is **proved conditional on the pole non-vanishing
hypothesis at the relevant pole orders**. The specialisations above are
conditional on the same hypothesis, which remains open.
