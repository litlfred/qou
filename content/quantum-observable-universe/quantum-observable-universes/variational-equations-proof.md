
Each equation is obtained by computing
$\delta\mathfrak{S}_q = 0$ with respect to the indicated variable, using
the non-degeneracy of $\int_A$.

*Item (1): Vary $\int_A$.*
The gravity term $\mathrm{tr}(q \cdot R_{\int})$ depends on $\int_A$
through the Frobenius--Ricci endomorphism $R_{\int}$.  Varying
$\int_A \mapsto \int_A + \delta\!\int_A$ and requiring
$\delta\mathfrak{S}_q = 0$ for all $\delta\!\int_A$ gives, by
non-degeneracy of the categorical trace,
$R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})\mathrm{id}_A = T_q[\nabla, \psi]$,
where the stress-energy $T_q$ collects the $\int_A$-dependence of the
gauge and matter terms.  The trace subtraction ensures
$\mathrm{tr}(T_q) = \tfrac{1}{2}\mathrm{tr}(R_{\int})$ (the
contracted Bianchi identity).

*Item (2): Vary $\nabla$.*
The gauge term
$\int_A \circ \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$
depends on $\nabla$ through $F_\nabla = \nabla^2$.  A standard
computation using $\delta F_\nabla = \nabla(\delta\nabla)$ and
integration by parts (via non-degeneracy of $\int_A$) yields
$\nabla \star_q F_\nabla + q \cdot [F_\nabla, \star_q F_\nabla] = J_\psi$.
The commutator term $q \cdot [F_\nabla, \star_q F_\nabla]$ arises from
the non-commutativity of the $q$-deformed wedge product; it vanishes
when $q = 1$ (the abelian/classical limit).

*Item (3): Vary $\psi$.*
The matter term $\int_A(\psi^* \cdot D_\nabla\psi)$ is linear
in $\psi$.  Varying $\psi \mapsto \psi + \delta\psi$ and using
$(\delta\psi)^* \cdot D_\nabla\psi = 0$ for
all $\delta\psi$ gives $D_\nabla\psi = 0$ by non-degeneracy
of $\int_A$ and the dagger structure
([positive definite dagger](#prop:positive-definite-dagger)).
