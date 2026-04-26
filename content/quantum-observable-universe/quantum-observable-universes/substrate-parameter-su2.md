Continuing the [quantum universe for $\mathrm{SU}(2)$](#ex:quantum-universe-su2),
we specify the [substrate parameter](#def:substrate-parameter) that
controls the deformation from classical $\mathrm{SU}(2)$ to quantum
$\mathrm{SU}_q(2)$.

**The specialisation map.** The categorical substrate parameter
$q \in \mathrm{End}(\mathbf{1})$ is realised via a ring
homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{C}$
determined by its value on the generator:
$\iota(q) = q_0 \in \mathbb{C}^\times$. All algebraic structures
(multiplication, comultiplication, antipode, $R$-matrix) are defined
over $\mathbb{Z}[q, q^{-1}]$ and specialise to concrete $\mathbb{C}$-algebras
via $\iota$.

**Classical case.** Setting $q_0 = 1$ recovers the undeformed coordinate
ring $\mathcal{O}(\mathrm{SU}(2))$ with its commutative multiplication:

$$
  \iota_{q_0 = 1} \colon
  \mathcal{O}_q(\mathrm{SU}(2))
   \longrightarrow 
  \mathcal{O}(\mathrm{SU}(2)),
  \qquad
  \begin{pmatrix} a & b \\ c & d \end{pmatrix}
  \mapsto
  \begin{pmatrix} a & b \\ c & d \end{pmatrix},
$$

where $ab = ba$, $ac = ca$, etc. This is the setting of the classical
[brane tower](#ex:recursive-brane-tower-su2).

**Quantum case.** For $q_0 = e^{\pi i / \kappa}$ with $\kappa \in \mathbb{Z}_{\geq 2}$ the Chern--Simons level, the specialisation
produces $\mathcal{O}_{q_0}(\mathrm{SU}(2))$ with non-commutative
relations:

$$
  ab = q_0 ba, \quad ac = q_0 ca, \quad
  bc = cb, \quad ad - da = (q_0 - q_0^{-1}) bc.
$$

The representation category
$\mathrm{Rep}(\mathrm{SU}_{q_0}(2))$ is a modular tensor category
with finitely many simple objects $V_0, V_{1/2}, \ldots, V_{(\kappa - 2)/2}$
when $q_0$ is a root of unity.

**Root-of-unity truncation.** At $q_0 = e^{\pi i / \kappa}$, the
spin-$j$ representations with $2j \geq \kappa - 1$ become reducible
or zero, leaving a finite semisimple category. The quantum dimension
of $V_j$ is

$$
  \dim_q(V_j) = \frac{q_0^{2j+1} - q_0^{-(2j+1)}}{q_0 - q_0^{-1}}
  = [2j + 1]_{q_0},
$$

the quantum integer. For $q_0 = 1$ this reduces to the classical
dimension $2j + 1$.

**Physical interpretation.** The substrate parameter $q_0$ interpolates
between the classical gauge theory ($q_0 = 1$, infinite-dimensional
representation category) and the topological quantum field theory
($q_0$ a root of unity, finite modular category). The Chern--Simons
level $\kappa$ controls the "granularity" of the quantum geometry.
