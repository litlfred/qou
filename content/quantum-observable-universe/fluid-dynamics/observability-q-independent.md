Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def\:quantum-observable-universe) and let
$\mathcal{Q}_M = M \times \mathbb{G}_m$ be the
[substrate line bundle](#def\:substrate-line-bundle).  Let
$q_1, q_2 \colon M \to \mathbb{G}_m$ be any two substrate
sections.

Then:

$$
  \mathrm{Hom}_{\mathbf{C}_{q_1}}\!
  \bigl(\mathbf{1}, \mathrm{Ad}(A)\bigr)
  = 
  \mathrm{Hom}_{\mathbf{C}_{q_2}}\!
  \bigl(\mathbf{1}, \mathrm{Ad}(A)\bigr).
$$

In particular, if $(\mathbf{C}, A, \tau)$ satisfies the
observability axiom for any substrate section $q > 1$, then
it satisfies it for **every** substrate section, including
$q = 1$.

*Proof.*
The space $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A))$
is computed in the category $\mathbf{C}$, which is defined
independently of $q$.  The substrate parameter $q$ determines
only the differential $d_q$ on $\Omega^\bullet(A)$; it does
not modify the objects, morphisms, tensor product, or braiding
of $\mathbf{C}$.  The adjoint object $\mathrm{Ad}(A)$ is
defined via the conjugation action
$a \mapsto S(a_{(1)})xa_{(2)}$, which involves only the
Hopf structure $(\mu, \Delta, S)$ — none of which depends on
$q$.

The subscript $\mathbf{C}_q$ in the notation
$\mathrm{Hom}_{\mathbf{C}_q}$ refers to the category equipped
with the differential $d_q$.  But
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ involves no
differential — it is a morphism space in the underlying
:refterm[monoidal category]{#monoidal-category}, which is the same for all $q$.

**Corollary.**  The QOU axioms (observability, measurability,
volume constraint) are properties of the
[substrate line bundle](#def\:substrate-line-bundle) base
$(\mathbf{C}, A, \tau)$, not of any particular fibre
$q \in \mathbb{G}_m$.  They hold uniformly over
$\mathbb{G}_m$, including at the torsion point $q = 1$ and
at all roots of unity.
