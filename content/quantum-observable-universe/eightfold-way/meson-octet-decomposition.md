*The tensor product of the fundamental triplet and its conjugate
decomposes as $\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8}
\oplus \mathbf{1}$, yielding the meson octet and the flavor singlet.*

A meson is a quark--antiquark bound state.  In the flavor
$\mathrm{SU}(3)_{\mathrm{f}}$ classification, a quark transforms in the fundamental
$\mathbf{3}$ and an antiquark in the conjugate $\bar{\mathbf{3}}$.
The tensor product decomposes into the adjoint (octet) and the trivial
(singlet) representations:
$$
  \mathbf{3} \otimes \bar{\mathbf{3}}
  = \mathbf{8} \oplus \mathbf{1}.
  \qquad (9 = 8 + 1)
$$

The $\mathbf{8}$ (adjoint representation) has weights forming a
regular hexagon with double multiplicity at the origin, sitting in the
$(I_3, Y)$ plane.  Weights are recorded in the quark-count coordinates
$(\lambda_1, \lambda_2) = (n_u - n_s,\; n_d - n_s)$ used for the
$\mathbf{3}$ in [the $A_2$ proposition](#prop:a2-from-three-strands), so
that the charge formulas
$I_3 = \tfrac{1}{2}(\lambda_1 - \lambda_2)$ and
$Y = \tfrac{1}{3}(\lambda_1 + \lambda_2)$
of that proposition apply verbatim to every row below:

| Weight | $I_3$ | $Y$ | Meson identification |
|---|---|---|---|
| $(1, -1)$ | $+1$ | $0$ | $\pi^+\ (u\bar{d})$ |
| $(-1, 1)$ | $-1$ | $0$ | $\pi^-\ (d\bar{u})$ |
| $(2, 1)$ | $+\tfrac{1}{2}$ | $+1$ | $K^+\ (u\bar{s})$ |
| $(1, 2)$ | $-\tfrac{1}{2}$ | $+1$ | $K^0\ (d\bar{s})$ |
| $(-2, -1)$ | $-\tfrac{1}{2}$ | $-1$ | $K^-\ (s\bar{u})$ |
| $(-1, -2)$ | $+\tfrac{1}{2}$ | $-1$ | $\bar{K}^0\ (s\bar{d})$ |
| $(0, 0)_a$ | $0$ | $0$ | $\pi^0\ (u\bar{u} - d\bar{d})/\sqrt{2}$ |
| $(0, 0)_b$ | $0$ | $0$ | $\eta\ (u\bar{u} + d\bar{d} - 2s\bar{s})/\sqrt{6}$ |

The $\mathbf{1}$ (singlet) is the $\eta'$:
$$
  \eta' = \frac{1}{\sqrt{3}}(u\bar{u} + d\bar{d} + s\bar{s}).
$$

**QOU realization.**
In the knot-particle dictionary, each meson is a quark--antiquark pair
joined by the $\bowtie_K$ product.  The tensor decomposition
$\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$
is realized by the Clebsch--Gordan decomposition of the Hecke algebra
$H_3(q)$ acting on the tensor product of the fundamental and conjugate
Specht modules.  The octet channel corresponds to the traceless
component $V \otimes V^* / \langle \mathrm{tr} \rangle$, and the
singlet to the trace $\mathrm{tr}(V \otimes V^*) \cong \mathbb{C}$.

**Conditional on $N = 3$.**
This decomposition requires the flavor fundamental to be
three-dimensional ($N = 3$).  As noted in
[the Schur--Weyl proposition](#prop:schur-weyl-eightfold), the $N = 3$ question is
the chapter's central open problem.  The tensor decomposition itself
is a theorem of $\mathrm{SU}(3)$ representation theory; its applicability
to QOU depends on resolving how the three-dimensional flavor space
arises from the multi-fibre groupoid or octonionic stabilization.
