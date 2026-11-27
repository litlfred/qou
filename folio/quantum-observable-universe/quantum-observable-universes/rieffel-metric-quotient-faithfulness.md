The [categorical Dirac operator](#def:categorical-dirac-operator) $\mathcal{D}_\nabla = q^{-1}\nabla + (1 - q^{-1})\iota_\xi\nabla$ combines horizontal covariant differentiation and Reeb contact transport with weights $q^{-1}$ and $1 - q^{-1}$ summing to $1$; for $1 < q$ both weights are strictly positive, making the induced transport cost anisotropic across horizontal and contact directions rather than a pure Reeb step count. On any unital $K$-algebra $A$ over a strictly ordered field $K$, a first-order differential operator of this form induces a Lipschitz seminorm $L \colon A \to K$ satisfying $L(1_A) = 0$, $L(c a) = |c|\,L(a)$ for $c \in K$, and $L(a + b) \le L(a) + L(b)$ \cite{connes1989,connes1994,rieffel1999}.

Dualising $L$ across unital $K$-linear states $\varphi, \psi \colon A \to K$ defines the Connes--Rieffel transport supremum

$$
  d_L(\varphi, \psi)
  \;=\;
  \sup\{\,|\varphi(a) - \psi(a)| : a \in A,\; L(a) \le 1\,\},
$$

which coincides on finite state graphs with the Kantorovich--Rubinstein optimal transport distance \cite{kantorovich1942,rubinstein1957,rieffel2004}. Two structural properties link metric separation to algebraic indiscernibility in a [quantum observable universe](#def:quantum-observable-universe):

1. **Metric Identity of Indiscernibles.** Zero dual bound $d_L(\varphi, \psi) = 0$ holds if and only if $\varphi = \psi$ on all of $A$: elements with $L(a) = 0$ lie directly in the unit Lipschitz ball, while elements with $L(a) > 0$ enter after normalisation to $L(a)^{-1} a$.
2. **Trace-radical descent and scalar-kernel faithfulness.** If $L$ vanishes on a non-scalar element $r \in A$ and two states satisfy $\varphi(r) \neq \psi(r)$, arbitrary scalar multiples $t r$ remain inside $\{L \le 1\}$ while driving $|\varphi(t r) - \psi(t r)|$ past every bound \cite{rieffel1999}. In particular, whenever $L$ vanishes on the null radical $\mathrm{rad}\,\tau = \{r \in A : \tau(r b) = 0 \text{ for all } b \in A\}$ of a trace functional $\tau$, every pair of states at finite distance agrees identically on $\mathrm{rad}\,\tau$. Passing to the Gelfand--Naimark--Segal quotient $A / \mathrm{rad}\,\tau$ \cite{gelfand-naimark1943,segal1947} eliminates trace-indiscernible combinations, collapses $\ker L$ to the scalar subalgebra $K \cdot 1$, and converts a degenerate seminorm into a faithful Kantorovich--Rubinstein metric on the quotient state space.
