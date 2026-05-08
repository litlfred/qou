Continuing the [Reeb derivation for $\mathrm{SU}(2)$](#ex:reeb-su2) and the
[Bring coordinate ring](#def:brings-coordinate-ring), we construct
the [categorical Reeb derivation](#def:categorical-reeb)
$(\xi, \varTheta_A)$ on Bring's surface explicitly.

**Step 1: identify the generator $\xi$.** The maximal torus of
$\mathrm{SU}_q(2)$ is $T = \mathrm{U}(1)$, embedded as diagonal
matrices. Its Lie algebra generator in $\mathfrak{su}(2)$ is

$$
  \xi = e_3
  = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

On the quantum coordinate ring
$A = \mathcal{O}_q(\mathrm{SU}(2))$, $\xi$ acts as the infinitesimal
adjoint coaction. In terms of the standard generators
$\alpha, \beta, \bar\alpha, \bar\beta$
($\alpha\bar\alpha + q^{-2}\beta\bar\beta = 1$), the action is:

$$
  \xi \cdot \alpha = \tfrac{1}{2}\alpha, \quad
  \xi \cdot \beta  = -\tfrac{1}{2}\beta, \quad
  \xi \cdot \bar\alpha = -\tfrac{1}{2}\bar\alpha, \quad
  \xi \cdot \bar\beta  = \tfrac{1}{2}\bar\beta.
$$

This is a *derivation*: $\xi \cdot (fg) = (\xi \cdot f)g + f(\xi \cdot g)$.

**Step 2: construct the dual $1$-form $\varTheta_A$.** The Woronowicz
$3$-dimensional calculus on $\mathcal{O}_q(\mathrm{SU}(2))$ has basis
$\{\omega_+, \omega_-, \omega_3\}$ of left-invariant $1$-forms. The
form dual to $\xi = e_3$ is

$$
  \varTheta_A = \omega_3
$$

where $\omega_3$ is defined by $\omega_3(e_3) = 1$ and
$\omega_3(e_\pm) = 0$, that is, $\omega_3$ is the left-invariant
basis element dual to $e_3$ in the Woronowicz $3$-dimensional
calculus \cite{woronowicz1989}.

**Step 3: verify the axioms.** The two defining properties of the
categorical Reeb derivation are now checkable by direct computation:

1. *Normalisation*: $\varTheta_A(\xi) = \omega_3(e_3) = 1 = \mathrm{id}_{\mathbf{1}}$. $\checkmark$

2. *Reeb/contact identity*: the directly verified condition is
   $\iota_\xi\,d\varTheta_A = 0$ for $\varTheta_A = \omega_3$.
   The exterior derivative $d\omega_3$ is computed from the
   Woronowicz structure equations
   $d\omega_3 = -q^{-1}\omega_+ \wedge \omega_-$, and
   $\iota_{e_3}(d\omega_3) = -q^{-1}(\omega_+(e_3)\omega_-
   - \omega_-(e_3)\omega_+) = 0$, confirming that $\omega_3$ is a
   contact form with Reeb field $\xi$. The vertical projection
   $\pi_V$ is the independent projection onto non-zero-weight
   components under the $\xi$-action, as constructed in
   [weight decomposition](#ex:weight-decomposition-su2). Combined
   with $\iota_\xi\,d\varTheta_A = 0$, the vertical generator axiom
   $\pi_V \circ d = \iota_\xi\,d\varTheta_A$ restricts to horizontal
   forms (annihilated by $\iota_\xi$) and recovers the Reeb
   decomposition $\pi_H + \pi_V = \mathrm{id}$. $\checkmark$

**Bring's surface specialisation.** On the
[Bring coordinate ring](#def:brings-coordinate-ring)
$\mathcal{O}_q(\mathcal{B})$, the $\xi$-action extends to the
five coordinates $x_1, \ldots, x_5$ via the $S_5$-equivariant
embedding. The $8 = 2g$ independent cycles of the genus-$4$ curve
decompose into $\xi$-eigenspaces (by Hodge decomposition,
$H^1(\Sigma_4, \mathbb{C}) = H^{1,0} \oplus H^{0,1}$ with
$\dim H^{1,0} = g = 4$):

- $4$ cycles of weight $+1$ (holomorphic differentials $H^{1,0}$),
- $4$ cycles of weight $-1$ (anti-holomorphic differentials $H^{0,1}$).

The Reeb spectrum is $\mathrm{Spec}(\xi) = \{-1, +1\}$ with
multiplicity $4$ each, matching the $8$ fundamental modes of
Bring's curve. The contact form $\varTheta_A$ restricts to the
canonical $1$-form on $\Sigma_4$ whose kernel defines the horizontal
distribution.
