Continuing [$\mathrm{SU}(2)$ as a quantum universe](#ex:quantum-universe-su2), the simple objects are the irreducible representations $V_n$, $n \geq 0$, of dimension $n + 1$; the [Grothendieck group](#def:grothendieck-group-of-a-qou) is $\mathbb{Z}[x]$ with $x = [V_1]$.

**Characters.** Restricted to the maximal torus $\{ \mathrm{diag}(t, t^{-1}) \}$, the weights of $V_n$ are $n, n-2, \dots, -n$, so its character is the symmetric Laurent polynomial

$$
  \mathrm{ch}(V_n)(t) \;=\; t^{n} + t^{n-2} + \cdots + t^{-n} \;=\; t^{-n}\bigl(1 + t^{2} + \cdots + t^{2n}\bigr).
$$

Characters are additive on direct sums and multiplicative on tensor products, and a representation of $\mathrm{SU}(2)$ is determined by its character; so $[V] \mapsto \mathrm{ch}(V)$ identifies $K_0(\mathrm{Rep}\,\mathrm{SU}(2))$ with the ring $\mathbb{Z}[t, t^{-1}]^{S_2}$ of Laurent polynomials invariant under $t \mapsto t^{-1}$ \cite{fulton-harris1991}. This is the [Chern character](#def:chern-character) of the category in the presentation of $HH_0$ by class functions: the class $[\mathrm{id}_{V_n}]$ corresponds to the character $\mathrm{ch}(V_n)$ on the maximal torus.

**Torus evaluations.** At the identity $t = 1$ every weight term is $1$, and $\mathrm{ch}(V_n)(1) = n + 1 = \dim V_n$. At a general invertible torus parameter $t$, telescoping multiplication by $t - t^{-1}$ gives the three character identities

$$
  \mathrm{ch}(V_n)(1) = n + 1, \qquad
  (t - t^{-1})\,\mathrm{ch}(V_n)(t) = t^{n+1} - t^{-(n+1)}, \qquad
  \mathrm{ch}(V_1)(t) = t + t^{-1}
$$

\cite{kassel1995}. Whenever $t - t^{-1}$ is invertible, the character evaluation takes the closed quotient form $\mathrm{ch}(V_n)(t) = (t^{n+1} - t^{-(n+1)})/(t - t^{-1})$.

**What the example shows.** The formal character $\mathrm{ch}(V_n)(t)$ has $n + 1$ weight terms in $\mathbb{Z}[t, t^{-1}]^{S_2}$, whereas evaluating at a specific torus point $t$ produces a single scalar in the ground ring. Their relation is the factorisation $\mathrm{ev}_t \circ \mathrm{ch}$ of the [Chern character](#def:chern-character), with $\mathrm{ev}_t$ the evaluation of a class function at $t$. Two consequences follow immediately. First, for every real torus parameter $t > 0$ and every $n \geq 0$, each summand $t^{n - 2k}$ is positive, so $\mathrm{ch}(V_n)(t) > 0$: a representation dimension evaluated on the positive real axis is strictly positive, and a negative integer such as $-6$ cannot arise as one. Second, for the coordinate algebra $A = \mathcal{O}(\mathrm{SU}(2))$, the Peter--Weyl decomposition $[A] = \sum_{n \geq 0} (n+1)[V_n]$ is an infinite direct sum living in a completion of $K_0$, and the formal series $\sum_{n \geq 0} (n+1)\,\mathrm{ch}(V_n)(t)$ diverges at every real $t > 0$; assigning a finite scalar invariant to a geometric space requires the homological Euler characteristic of its de Rham or Hochschild complex rather than an unregularised sum of representation dimensions.
