## The shared smaller-scope open math, now scaffolded

The α_shift universal derivation chain identified the pole-order origin
of the q-integer indices in several "empirical" fits.  What remained shared across the α_EM, p-n averaging,
and meson m_K/m_π treatments was
the residue/resolvent step: deriving the closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$ from the contour-integral
evaluation on Bring's surface.

This proposition structures that derivation conditionally on the pole non-vanishing hypothesis at order $n$, then specialises to the three concrete pole orders used downstream.

## Structural decomposition

- **Order-$n$ Bring residue hypothesis**: for a field $R$, an integer pole order $n \in \mathbb{N}$, and $q \in R$, the contour-integral / Schwarz-integral condition asserts the pole non-vanishing $1 - h_q \cdot q^n \neq 0$ — the substantive condition any concrete contour route must establish.
- **Resolvent equation**: given $1 - h_q \cdot q^n \neq 0$, the canonical resolvent $F_n(q) = (1 - h_q \cdot q^n)^{-1}$ satisfies $(1 - h_q \cdot q^n) \cdot F_n(q) = 1$.
- **Three specialisations**:
  - $T(3,5)$ at pole order $n = 10$, used by $p$-$n$ averaging
    ([p-n averaging uniqueness](#prop:pn-averaging-uniqueness));
  - $T(2,9)$ at pole order $n = 9$, used by $1/\alpha_{\rm EM}$
    ([fine-structure observation](#rem:fine-structure-observation));
  - the meson pair at pole orders $n = 3$ and $n = 4$, used by
    $m_K^2/m_\pi^2$
    ([meson color-tube uniqueness](#prop:meson-color-tube-uniqueness)).

## Closing the residue hypothesis

Establishing the order-$n$ Bring residue condition from first principles admits two routes:

1. **Analytic route:** complex residue and circle-integral evaluation applied to the
   $\sigma$-action on Hecke representations at the torus-knot
   surface.
2. **Algebraic route:** via the substrate's Bloch–Suslin framework,
   identifying the contour integral with a specific Bloch-group
   class on Bring's surface.

Both routes converge on the same closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$, establishing the
**conditional uniqueness** of the resolvent form.

## Downstream consequence

Each specialisation collapses a separate residue-normalisation gap
into a **single shared pole-order hypothesis**:

| where used | downstream form | resolvent specialisation |
|---|---|---|
| [fine-structure observation](#rem:fine-structure-observation) | $1/\alpha_{\rm EM} = q \cdot [9]_q \cdot [10]_q + 2/(3\pi)$ | orders $n = 9$ and $n = 10$ (genus-4 pair) |
| [p-n averaging uniqueness](#prop:pn-averaging-uniqueness) | $\sigma_{pn}(q)$ Bring color-tube weight $1/(1 - h_q \cdot q^{10})$ | order $n = 10$ |
| [meson color-tube uniqueness](#prop:meson-color-tube-uniqueness) | $m_K^2 / m_\pi^2 = [3]_q \cdot [4]_q$ | orders $n = 3$ and $n = 4$ (meson pair) |

Establishing the residue condition once therefore discharges the residue step
in all three cases.
