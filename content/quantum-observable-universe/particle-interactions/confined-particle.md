**Definition.**
*A **confined particle** is a tuple*

$$
  P \;=\; (\mathrm{name},\ \ell,\ [K]_M,\ n_0)
$$

*where:*

1. *$\mathrm{name}$ is a symbol drawn from a fixed registry of particle shortcuts.*
2. *$\ell \in \mathbb{Z}_{\ge 0}$ is the **confinement level** (quark = 0, nucleon = 1, atom = 2, molecule/compound = 3, $\ldots$).*
3. *$[K]_M$ is the **Markov-equivalence class** of a closed braid $K$. It is represented canonically by the Gröbner–Shirshov normal form of its associated Hecke element $T_w \in H_{n_0}(q)$.*
4. *$n_0$ is the **coarse strand count** at level $\ell$: the minimal number of strands needed to express $K$ as a closed braid at its own level.*

*The class $[K]_M$ is not intrinsically confined at any particular $q$. Confinement is a $q$-indexed predicate $\mathrm{confined}(P, q)$ that holds if and only if the matrix Frobenius PSD cone admits a feasible $\Phi^* \succeq 0$. A confined particle is **stable at $q$** if and only if it is additionally Frobenius-non-degenerate there. Unstable species are confined particles for all $q$ in the generic locus even though their decay channels are open.*

**Canonical representative.**
*Among all closed-braid words in $[K]_M$, we choose the one with the shortlex-minimal Gröbner–Shirshov normal form as the canonical representative $\mathrm{GS}(P)$. We compute the witness data $k_{\max}(P, q)$ on this representative. Two particles are equal if and only if their names are equal, which occurs if and only if $\mathrm{GS}(P_1) = \mathrm{GS}(P_2)$.*

**Examples.**

- *`quark`: $\ell = 0$, $n_0 = 1$, $[K]_M = [\sigma_0]$ in $H_1(q)$.*
- *`neutrino`: $\ell = 0$, $n_0 = 1$, $[K]_M = [\mathbf{1}]$ (unknot $0_1$, no crossings). Confined and stable at $q_0$; the Frobenius-PSD cone is satisfied since $\Phi^* = \mathbf{1} \succeq 0$.*
- *`photon`: $\ell = 0$, $n_0 = 4$, $[K]_M = [\mathbf{1}_{B_4}]$ (four-strand identity in $B_4$, no crossings). Confined at $q_0$ via the Reeb-bundle holonomy.*
- *`proton`: $\ell = 1$, $n_0 = 3$, $[K]_M = [B_3(\mathrm{uud})]$ with crossing types $(pp, pn, pn)$.*
- *`neutron`: $\ell = 1$, $n_0 = 3$, $[K]_M = [B_3(\mathrm{udd})]$.*
- *`electron`: $\ell = 1$, $n_0 = 2$, $[K]_M = [\sigma_1^3]$ (trefoil $3_1$).*
- *`\He4`: $\ell = 2$, $n_0 = 4$ nucleons, $[K]_M$ determined by the canonical ILP ground-state configuration for $(Z,N)=(2,2)$.*
- *`\benzene`: $\ell = 3$, $n_0 = 6$ atom-strands.*

**Archimedean specialisation.** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
