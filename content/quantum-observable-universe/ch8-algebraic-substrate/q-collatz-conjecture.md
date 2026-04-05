**Conjecture ($q$-Collatz).**
Let $(\mathbf{C}, A, \tau)$ be a quantum universe with
Frobenius--Hopf substrate $A$
([substrate](#def:frobenius-hopf-substrate)),
categorical Reeb derivation $\xi_q \colon A \to A$
([Reeb derivation](#def:categorical-reeb-derivation)),
and substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$
([torsion avoidance](#rem:substrate-gm-torsion)).

Over the multiplicative group scheme
$\mathbb{G}_m = \mathrm{Spec}\,\mathbb{Z}[q, q^{-1}]$,
define the **Hecke--Collatz endomorphism**
$C_q \in \mathrm{End}_{\mathbf{C}}(A)[q^{\pm 1}]$ by:

$$
  C_q \;=\;
  e_+(\xi_q)\,\circ\,\mu^{-1}_{[2]_q}
  \;+\;
  e_-(\xi_q)\,\circ\,\bigl(\mu_{[3]_q} + \eta\bigr),
$$

where $\mu_{[k]_q} \colon A \to A$ is scalar multiplication
by $[k]_q = (q^k - 1)/(q - 1)$ in the Frobenius algebra,
$\eta \colon \mathbf{1} \to A$ is the unit, and the
**Hecke--Reeb idempotents** are

$$
  e_+(\xi_q) = \frac{\xi_q + q^{-1}\,\mathrm{id}_A}{[2]_q},
  \qquad
  e_-(\xi_q) = \frac{q\,\mathrm{id}_A - \xi_q}{[2]_q},
$$

obtained by evaluating the Hecke algebra $H_1(q)$
idempotents $e_\pm = (T + q^{-1})/(q + q^{-1})$,
$(q - T)/(q + q^{-1})$ at $T = \xi_q$
([skein generation](#prop:skein-generation)).
These project onto the symmetric (weight-$0$, horizontal)
and antisymmetric (weight-$1$, vertical) eigenspaces of
the Reeb action.

Each application of $C_q$ is clocked by one period of
the Reeb flow
([categorical $q$-Reeb flow](#def:categorical-q-reeb-flow)),
consuming $n_R(q) = q/(q-1)$ discrete substrate iterations
([operations per Planck](#prop:reeb-operations-per-planck)).

**The obstruction.**
The Collatz obstruction is the restriction of the Euler
class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$
([classical limit obstruction](#def:classical-limit-obstruction))
to the sub-bundle $\mathcal{S}_{C_q} \subset \mathcal{S}$
traced by $C_q$-orbits:

$$
  \kappa_C
  \;:=\;
  \mathrm{res}_{C_q}\!\bigl(\kappa_0\bigr)
  \;\in\;
  H^2(\mathcal{S}_{C_q},\, \mathbb{G}_m).
$$

In a general QU, $\dim HH^2(\mathrm{Ad}) \geq 1$ and
$\kappa_C$ can be non-trivial.  In a QOU, observability
forces $HH^2(\mathrm{Ad}) \cong k$
([QOU obstruction reduction](#thm:qou-obstruction-reduction)),
so $\kappa_C = c_C \cdot \chi(A)$ for some $c_C \in k$.

**The conjecture.** $c_C = 0$:

$$
  \boxed{\kappa_C = 0
  \quad\text{in}\quad
  H^2(\mathcal{S}_{C_q},\, \mathbb{G}_m).}
$$

Equivalently: for every $q > 1$ and every
$a \in A$ in the positive cone, the Reeb-clocked orbit
$\{C_q^k(a)\}_{k \geq 0}$ converges to $\eta(\mathbf{1})$.

**Classical limit.**
At $q = 1$: $[2]_1 = 2$, $[3]_1 = 3$, $\xi_1 = \mathrm{id}$,
and $e_\pm((-1)^n) = (1 \pm (-1)^n)/2$.
The endomorphism $C_1$ recovers the classical Collatz map:

$$
  C_1(n)
  = \begin{cases}
      n/2 & n \text{ even},\\
      3n + 1 & n \text{ odd}.
    \end{cases}
$$

Since $q = 1 \in \mu_1$ is a torsion point, the mass gap
closes ($\Delta_1 = 0$), the QOU axioms fail, and the
classical Collatz conjecture is the $q \to 1$ boundary case.
