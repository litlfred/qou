*A **confined particle** is a tuple*

$$
  P \;=\; (\mathrm{name},\ \ell,\ [K]_M,\ n_0)
$$

*where:*

1. *$\mathrm{name}$ is a symbol drawn from a fixed registry of particle shortcuts.*
2. *$\ell \in \mathbb{Z}_{\ge 0}$ is the **confinement level** (quark = 0, nucleon = 1, atom = 2, molecule/compound = 3, $\ldots$).*
3. *$[K]_M$ is the **Markov-equivalence class** of a closed braid $K$. It is represented canonically by the Gröbner–Shirshov normal form of its associated Hecke element $T_w \in H_{n_0}(q)$.*
4. *$n_0$ is the **coarse strand count** at level $\ell$: the minimal number of strands needed to express $K$ as a closed braid at its own level.*

*Confinement is a $q$-indexed predicate $\mathrm{confined}(P, q)$ that holds if and only if the matrix Frobenius PSD cone admits a feasible $\Phi^* \succeq 0$. A confined particle is **stable at $q$** if and only if it is additionally Frobenius-non-degenerate there.*

**Canonical representative.**
*Among all closed-braid words in $[K]_M$, we choose the one with the shortlex-minimal Gröbner–Shirshov normal form as the canonical representative $\mathrm{GS}(P)$.*

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
