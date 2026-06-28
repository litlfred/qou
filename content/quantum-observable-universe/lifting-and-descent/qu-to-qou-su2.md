Continuing
[Yekutieli lifting for SU(2)](#ex:yekutieli-lifting-su2), we verify all
five structural properties of the
[main theorem](#thm:qu-to-qou) for $G = \mathrm{SU}(2)$.

**Hypotheses.** From the [SU(2) QOU](#ex:qou-su2), the quantum universe
is $(\mathrm{Rep}(\mathrm{SU}(2)), \mathcal{O}(\mathrm{SU}(2)), \tau)$ with substrate parameter $q$.  Observability holds:
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ because
$\mathrm{Ad}(\mathrm{SU}(2)) \cong \mathfrak{su}(2)$ has no trivial
sub-representation (the adjoint representation is irreducible,
isomorphic to $V_1$).

**(1) :refterm[Descent]{#descent} terminates.**
The center of the endomorphism algebra is
$Z(\mathrm{End}_{\mathbf{C}}(A)) \cong \mathcal{O}(\mathrm{SU}(2))^{\mathrm{SU}(2)}$,
the $\mathrm{SU}(2)$-invariant functions, which form a ring of Krull
dimension $\mathrm{rank}(\mathrm{SU}(2)) = 1$.  The geometric :refterm[descent]{#descent}
tower is

$$
  \mathbb{CP}^1  \longrightarrow  \mathrm{pt},
$$

which terminates in $1$ step (since
$\mathrm{Krulldim} Z(\mathrm{End}(A)) = 1$).  At each step, the
$G_q$-action is faithful (observability ensures strict dimension
reduction).

**(2) First obstruction equals the Euler class.**
The Yekutieli obstruction $\kappa_0 \in H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$ equals the Euler class of the Reeb bundle, which for
the Hopf fibration is $c_1(\text{Hopf}) = 1$.  Under the trace map,

$$
  \kappa_0  \longmapsto  \chi(A)
  =  \mathrm{tr}(\mathrm{id}_A)
  =  \chi(\mathbb{CP}^1) =  2.
$$

**(3) Perpetual obstruction.**
From the
[quantum characteristic classes](#ex:quantum-characteristic-classes-su2),
$\kappa_0 = 1 \in \mathbb{Z}$ is non-torsion (since $\mathbb{Z}$ is
torsion-free).  By the
[Yekutieli lifting analysis](#ex:yekutieli-lifting-su2), the jet
corrections at level $n$ are non-negative, so $\kappa_n \geq 1 > 0$ for
all $n \geq 0$.  The gerbe tower is perpetually obstructed.

**(4) Branch point formula.**
The projective line object is $\mathbb{P}(V) = \mathbb{CP}^1$
([projective line for SU(2)](#ex:projective-line-su2)).  The :refterm[descent]{#descent} map
$\mathbb{CP}^1 \to \mathbb{CP}^1$ has degree $d = 1$ (the identity
covering).  The Riemann--Hurwitz formula gives

$$
  R_{\mathrm{tot}} =  2d + |\chi(A)|
  =  2 \cdot 1 + |2| =  4,
$$

with $B = 2$ branch points (the north and south poles of $\mathbb{CP}^1 \cong S^2$), each with ramification index $e = 2$.

**(5) Terminal fiber data.**
At each branch point $p \in \{0, \infty\} \subset \mathbb{CP}^1$, the
QOU reduces to fiber data
$(\mathcal{O}(\mathrm{SU}(2)), \tau, q(p))$ with the involution

$$
  \sigma \colon \mathbb{CP}^1
   \hookrightarrow 
  \mathrm{Ad}(\mathrm{SU}(2))
  =  \mathfrak{su}(2).
$$

This embedding realizes $\mathbb{CP}^1 \cong S^2$ as the unit sphere in
$\mathfrak{su}(2) \cong \mathbb{R}^3$.  At the north pole $p = 0$, the
involution acts as $\sigma(v) = e_3 v e_3^{-1}$ (conjugation by the
Cartan generator), which is the identity on $\mathrm{U}(1)$-invariant
sections and negation on the off-diagonal components.  The fiber data at
$p = \infty$ is conjugate via the Weyl group element
$w \colon e_3 \mapsto -e_3$.

**Conclusion.** All five properties of the
[main theorem](#thm:qu-to-qou) are verified for $\mathrm{SU}(2)$.  The
quantum universe $(\mathrm{Rep}(\mathrm{SU}(2)), \mathcal{O}(\mathrm{SU}(2)), \tau)$ with observability and the
Yekutieli lifting condition is a quantum observable universe, with
:refterm[descent]{#descent} terminating in $1$ step, perpetually obstructed brane tower,
$2$ branch points on $\mathbb{CP}^1$, and fiber data governed by the
adjoint embedding $S^2 \hookrightarrow \mathfrak{su}(2)$.
