Let $\mathcal{S}_q$ be the categorical action
([Definition](#def:categorical-action)).  The three variational
equations are:

1. *Gravity (vary $\lambda$)*:
   $\delta\mathcal{S}_q / \delta\lambda = 0$ yields the
   *categorical Einstein equation*:

   $$
     R_\lambda - \tfrac{1}{2}\,\mathrm{tr}(R_\lambda)\,\mathrm{id}_A
     \;=\; T_q[\nabla, \psi],
   $$

   where $T_q$ is the stress-energy endomorphism constructed from the
   gauge and matter terms.

2. *Gauge (vary $\nabla$)*:
   $\delta\mathcal{S}_q / \delta\nabla = 0$ yields the
   *categorical Yang--Mills equation*:

   $$
     \nabla \star_q F_\nabla + q \cdot [F_\nabla,\, \star_q F_\nabla]
     \;=\; J_\psi,
   $$

   where $J_\psi = \psi^* \otimes D_\nabla\psi - D_\nabla\psi^* \otimes \psi$
   is the matter current.

3. *Matter (vary $\psi$)*:
   $\delta\mathcal{S}_q / \delta\psi = 0$ yields the
   *categorical transport equation*:

   $$
     D_\nabla\,\psi \;=\; 0.
   $$

---

Each equation is obtained by computing
$\delta\mathcal{S}_q = 0$ with respect to the indicated variable, using
the non-degeneracy of $\lambda$.

*Item (1): Vary $\lambda$.*
The gravity term $\mathrm{tr}(q \cdot R_\lambda)$ depends on $\lambda$
through the Frobenius--Ricci endomorphism $R_\lambda$.  Varying
$\lambda \mapsto \lambda + \delta\lambda$ and requiring
$\delta\mathcal{S}_q = 0$ for all $\delta\lambda$ gives, by
non-degeneracy of the categorical trace,
$R_\lambda - \tfrac{1}{2}\,\mathrm{tr}(R_\lambda)\,\mathrm{id}_A
= T_q[\nabla, \psi]$,
where the stress-energy $T_q$ collects the $\lambda$-dependence of the
gauge and matter terms.  The trace subtraction ensures
$\mathrm{tr}(T_q) = \tfrac{1}{2}\,\mathrm{tr}(R_\lambda)$ (the
contracted Bianchi identity).

*Item (2): Vary $\nabla$.*
The gauge term
$\lambda \circ \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$
depends on $\nabla$ through $F_\nabla = \nabla^2$.  A standard
computation using $\delta F_\nabla = \nabla(\delta\nabla)$ and
integration by parts (via non-degeneracy of $\lambda$) yields
$\nabla \star_q F_\nabla + q \cdot [F_\nabla,\, \star_q F_\nabla]
= J_\psi$.
The commutator term $q \cdot [F_\nabla, \star_q F_\nabla]$ arises from
the non-commutativity of the $q$-deformed wedge product; it vanishes
when $q = 1$ (the abelian/classical limit).

*Item (3): Vary $\psi$.*
The matter term $\lambda(\psi^* \cdot D_\nabla\,\psi)$ is linear
in $\psi$.  Varying $\psi \mapsto \psi + \delta\psi$ and using
$(\delta\psi)^* \cdot D_\nabla\,\psi = 0$ for
all $\delta\psi$ gives $D_\nabla\,\psi = 0$ by non-degeneracy
of $\lambda$ and the dagger structure
([Definition](#def:positive-definite-dagger)).
