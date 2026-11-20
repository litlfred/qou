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
joined by the $\bowtie_K$ product.  The splitting
$\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$
is the trace splitting of a rigid category.  Let $V$ be the fundamental
of $U_q(\mathfrak{sl}_3)$ at generic $q$ and $V^*$ its dual, with
coevaluation $c\colon \mathbf{1} \to V \otimes V^*$ and evaluation
$e\colon V \otimes V^* \to \mathbf{1}$ (using the pivotal structure).
The composite $e \circ c$ is multiplication by the quantum dimension
$d = [3]_q = q^2 + 1 + q^{-2}$, which is nonzero for real $q \neq 0$.
Then $p = d^{-1}\, c \circ e$ is an idempotent on $V \otimes V^*$.  Its
image is the singlet, the image of $c$, and the complementary idempotent
$1 - p$ projects onto the kernel of $e$, the octet.  At $q = 1$ this is the
splitting of a $3 \times 3$ matrix into its trace part and its traceless
part.  The Hecke algebra $H_3(q)$ does not enter here: it has no
three-dimensional irreducible and no tensor product of modules, and it
acts on $V^{\otimes 3}$ by Schur--Weyl duality, which is the baryon side.

The idempotent algebra holds in any $k$-linear category: given
$c\colon U \to W$ and $e\colon W \to U$ with $e \circ c = d \cdot 1_U$ and
$d \neq 0$, the maps $p$ and $1 - p$ are complementary idempotents,
$p \circ c = c$, $e \circ p = e$, and $e \circ (1 - p) = 0$.  The octet is not
proved irreducible here, and
$U_q(\mathfrak{sl}_3)$ is not constructed.

**Conditional on $N = 3$.**
This decomposition requires the flavor fundamental to be
three-dimensional ($N = 3$).  As noted in
[the Schur--Weyl proposition](#prop:schur-weyl-eightfold), the $N = 3$ question is
the chapter's central open problem.  The tensor decomposition itself
is a theorem of $\mathrm{SU}(3)$ representation theory; its applicability
to QOU depends on resolving how the three-dimensional flavor space
arises from the multi-fibre groupoid or octonionic stabilization.
