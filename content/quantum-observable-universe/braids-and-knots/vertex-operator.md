Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU, let
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor
at a brane point $p$
([exceptional divisor](#def:exceptional-divisor)), and let
$\mathcal{R}_p$ be the Reeb bundle over $\mathcal{S}_p$
([Reeb bundle](#def:reeb-bundle)).

**The formal variable.**
In the standard VOA formalism, the formal variable $z$ is an
indeterminate in the ring of formal Laurent series.  In the QOU it
has a geometric realisation: $z$ is the affine coordinate
$z = v_1/v_2$ on the projective line
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$
([projective line](#ex:projective-line-su2)), which coincides with
the contact affine coordinate $Z = \alpha_H / \iota_\xi\alpha$
([contact affine chart](#def:contact-affine-chart)) restricted to
the fibre $\mathcal{S}_p$.  Algebraically, on the standard affine
chart $v_2 \neq 0$, $z$ generates the coordinate ring
$\mathbb{C}[z]$.

The **vertex operator algebra** of the QOU at $p$ is the triple
$(V, Y, |0\rangle)$ defined as follows.

**Graded state space.**  The $\mathbb{Z}_{\geq 0}$-graded vector
space is the brane tower:

$$
  V =  \bigoplus_{n \geq 0} V_n,
  \qquad V_n =  A_n =  J^n(A_0),
$$

where $A_0 = \mathcal{O}(\mathrm{SU}_q(2))$ is the coordinate ring
and $J^n$ denotes the $n$-th jet prolongation
([jet prolongation](#prop:jet-prolongation)).  The grading $n$ is the
**conformal weight**: the eigenvalue of the Reeb charge operator
$L_0 = \xi_q^{(0)}$ (the zero-mode of the $q$-Reeb vector field).

**State-operator correspondence.**  The map

$$
  Y \colon V  \longrightarrow  (\mathrm{End}V)[\![z, z^{-1}]\!]
$$

assigns to each state $a \in V_n$ a **vertex operator** (a formal
Laurent series in $z$):

$$
  Y(a, z) =  \sum_{m \in \mathbb{Z}} a_m z^{-m-1},
$$

where the **modes** $a_m \in \mathrm{End}V$ are defined by the
$R$-matrix insertion:

$$
  a_m
  = 
  \oint_{|z| = 1} Y(a, z) z^m \frac{dz}{2\pi i}
  = 
  \mathrm{tr}_M\!\bigl(
    \check{R}_{(a)} z^m
  \bigr),
$$

with $\check{R}_{(a)} = P \circ \mathcal{R}$ the braid operator
([R-matrix braiding](#rem:r-matrix-braiding)) applied to the state
$a$, and $\mathrm{tr}_M$ the Markov trace
([Jones--Markov trace](#thm:jones-markov-trace)).  The contour
integral is taken around the equator of $\mathcal{S}_p \cong S^2$, i.e.\
along a fibre of the Reeb bundle $\mathcal{R}_p$.

**Vacuum and translation.**

$$
  |0\rangle = 1 \in A_0, \qquad
  T = L_{-1} = j \colon A_n \to A_{n+1},
$$

where $j$ is the jet prolongation map.  The vacuum is the unknot
(identity element of $A_0$), and the translation operator
advances one level in the brane tower.

**OPE as Skein resolution.**  When two insertion points $z, w$
on $\mathcal{S}_p$ collide, the operator product expansion

$$
  Y(a, z) Y(b, w)
   \sim 
  \sum_{n \geq 0}
  \frac{Y(c_n, w)}{(z - w)^{n+1}}
$$

has its **leading singularity** governed by the Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$, which is the Skein relation

$$
  L_+ - L_- =  (q - q^{-1}) L_0.
$$

The collision $z \to w$ is two strands meeting on $\mathcal{S}_p$; the
resolution into $L_+$, $L_-$, $L_0$ is the OPE decomposition
into singular channels.  The two eigenvalues $q$ and $-q^{-1}$
of $\sigma_i$ correspond to the symmetric (bosonic) and antisymmetric
(fermionic) OPE channels respectively.
