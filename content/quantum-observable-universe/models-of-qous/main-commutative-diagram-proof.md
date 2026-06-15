
We verify commutativity by tracing both paths around the diagram.

**Top-right path** (variational $\to$ coupling). The Euler--Lagrange
operator $\mathfrak{E}[\mathfrak{S}_q]$ applied to a jet $j^1_p \sigma$ yields the
variational equation
$\mathrm{Ric}_{g_\varTheta} = T^{(q)}$
([GR substrate geometry](#rem:gr-substrate-geometry)). Solving for
$L_\varTheta$ determines the Webster metric, which in turn fixes the
substrate field via the coupling
$q(p) = 1 + \lvert\langle L_\varTheta, F_A^+\rangle\rvert$.
This determines $\hbar_q = 1 - q^{-1}$, the $q$-Reeb field $\xi_q$,
and the $q$-Hamiltonian $\hat{H}_q = -\tfrac{1}{2}\hbar_q\Delta_q + V_q$ appearing in the transport equation.

**Left-bottom path** (evaluation $\to$ transport). The jet evaluation map
$j^1_p \sigma \mapsto \sigma(p)$ produces a section
$\psi \in \Gamma(\mathcal{S}_{\mathrm{lin}})$ by linearising the fibre
$\mathbb{P}^1(\mathbb{C})$ at the chosen base-point. Parallel transport
along $A$ then imposes
$J\hbar_q\iota_{\xi_q} D_A\psi = \hat{H}_q\psi$
([Schrödinger equation](#rem:schrodinger-jet-coaction)).

**Commutativity.** Both paths share the same input ($j^1_p \sigma$)
and the same output (a section $\psi$ satisfying the transport
equation at substrate parameter $q$). The key identity is that the
chain rule for the composite $\mathfrak{S}_q[\nabla, L_\varTheta, \psi]$ factorises
the variation into two coupled equations:

1. $\delta \mathfrak{S}_q / \delta L_\varTheta = 0$ determines $L_\varTheta$ (hence
   $q$ and $\hat{H}_q$) — this is the top row;
2. $\delta \mathfrak{S}_q / \delta \psi = 0$ gives $D_\nabla\psi = 0$
   ([variational equations](#prop:variational-equations), Item 3) —
   this is the bottom row.

The coupling $q = 1 + \lvert\langle L_\varTheta, F_A^+\rangle\rvert$
ensures that the $q$ appearing in the top-right path equals the $q$
in the left-bottom path. Non-degeneracy of $\int_A$
([Frobenius pairing](#def:frobenius-pairing)) guarantees that the
solution sets agree: solving for $L_\varTheta$ first and then
substituting into the transport equation yields the same $\psi$ as
evaluating the jet and transporting along $A$.
