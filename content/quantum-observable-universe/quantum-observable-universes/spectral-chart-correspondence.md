*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)).  The
Hecke spectral decomposition

$$
  V \otimes V  =  S^2 V \oplus \Lambda^2 V,
  \qquad
  c_{V,V}|_{S^2 V} = \lambda_+ = q,
  \quad
  c_{V,V}|_{\Lambda^2 V} = \lambda_- = -q^{-1},
$$

of ([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
realises geometrically as the chart-glue datum of the quantum projective
line ([projective line object](#def:projective-line-object)).  On the two
affine charts $U_0, U_1$ of
([contact affine chart](#def:contact-affine-chart)) the chart-transition
coefficient $\kappa$ in $z\,w = \kappa$ is fixed by the spectral data:

$$
  \kappa  =  \lambda_+^{-1}  =  -\lambda_-  =  q^{-1}.
$$

Two readings of the same equality:

1. *Glue from the antisymmetric line.*  The Hecke determinant constraint
   $\lambda_+ \lambda_- = -1$ from
   ([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
   is an eigenvalue identity on $\Lambda^2 V \cong \mathbf{1}$.  Because
   $\Lambda^2 V$ is the unit summand, that scalar identity is precisely
   the chart-glue datum on $\mathbb{P}_q(V)$ — no extra freedom remains.

2. *Classical degeneration.*  At $q = 1$ the eigenvalues collapse to
   $(+1, -1)$, the chart transition becomes the classical inversion
   $z\,w = 1$, and the projective line is the symmetric-monoidal
   $\mathbb{P}(V)$ of ([commutative QOU](#def:commutative-qou)).

The spectral and the geometric extractions of $q$ are therefore the same
datum read twice: eigenvalues of $c_{V,V}$ on $V \otimes V$, and
chart-transition data on $\mathbb{P}_q(V)$.  The explicit
$z\,w = q^{-1}$ presentation in coordinates $z = y x^{-1}$, $w = x y^{-1}$
on the quantum plane is worked out in
([affine-chart origin of $i$ and $q$](#rem:affine-chart-origin-of-i-and-q)).
