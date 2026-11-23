The normal-form basis of $H_3(q)$ admits two Gram matrices, and they do not have the
same signature. Which one is meant has to be said.

## The bilinear pairing

Dropping the star and pairing $G_{ij} = \mathrm{tr}_M(b_i b_j)$ gives, block by block,
the *bilinear* trace form $\mathrm{tr}(AB)$ on each matrix algebra. Parametrise
$A \in M_2$ by its symmetric part $(\alpha,\delta,\beta)$ and its antisymmetric part
$\gamma$, so that

$$
  A \;=\; \begin{pmatrix} \alpha & \beta+\gamma \\ \beta-\gamma & \delta \end{pmatrix}.
$$

Then

$$
  \mathrm{tr}(A^{2}) \;=\; \alpha^{2} \;+\; 2\beta^{2} \;-\; 2\gamma^{2} \;+\; \delta^{2}.
$$

Three squares enter with a plus sign and one with a minus, and the symmetric and
antisymmetric parts are orthogonal, so $\mathrm{tr}(AB)$ on $M_d$ has signature
$\bigl(\tfrac{d(d+1)}{2},\, \tfrac{d(d-1)}{2}\bigr)$. Summing over the blocks with
$y_\lambda > 0$ reproduces the whole signature of $G$: convention C gives $(5,1,0)$
and convention D gives $(4,1,1)$.

The negative direction is identified rather than measured. It is the antisymmetric
element $E_{12} - E_{21}$ of the $M_2$ sitting in the $(2,1)$ block --- the rotation
generator of $\mathfrak{sl}_2$. Any algebra with a two-dimensional irrep contributes
one such direction, so $G$ is indefinite for every $q$ and for every convention with
$y_{(2,1)} > 0$. The indefiniteness is a property of the *pairing*, not of the
substrate.

## The star pairing versus the bilinear trace form

An earlier reading took the single negative eigenvalue of $G$ as a physical
signature: the trace pairing was said to be a spacetime form, and the framework's
natural object a causal structure rather than a metric space. That causal-signature interpretation does not apply: a metric is built from the $*$-structure, and the Hecke $*$-structure is
$T_w^{*} = T_{w^{-1}}$. Pairing against it replaces the bilinear $\mathrm{tr}(AB)$ by
the sesquilinear $\mathrm{tr}(AB^{*})$, which on $M_d$ is a sum of $d^{2}$ squares:
signature $(d^{2},0)$, no negative direction anywhere. The eigenvalue magnitudes are
unchanged --- the star flips exactly the sign of the antisymmetric direction, which is
what a $*$-structure is for --- and the sign flip is what
[the star form's positivity](#prop:markov-gram-star-positive) records.

The bilinear analysis is retained because it is the same block decomposition that
explains both answers. It is the interpretation that was wrong, not the arithmetic.

**Archimedean specialisation.** What follows sits on the archimedean side of the
substrate wall: it invokes real- or complex-analytic constructs --- real-valued
physical observables, real-analytic bounds, transcendental constants, or numerical
evaluation at the substrate parameter $q_0$. Any generic categorical or
$q$-deformation identities it draws on remain valid over an abstract coefficient ring;
only their archimedean realisation is specialised here. Under the bilinear pairing at
$q_0$ the eigenvalues are $-0.855067,\, 0.101797,\, 0.855067^{\times 3},\, 3.476950$
for convention C and $-0.752702,\, 0,\, 0.752702^{\times 3},\, 4.230339$ for
convention D, where $\det G = 2.89 \times 10^{-51}$, i.e. zero at $50$ decimal places.
Under the star pairing every one of those magnitudes recurs with a positive sign.
