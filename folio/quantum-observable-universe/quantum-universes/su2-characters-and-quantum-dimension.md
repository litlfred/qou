Continuing [$\mathrm{SU}(2)$ as a quantum universe](#ex:quantum-universe-su2), the simple objects are the irreducible representations $V_n$, $n \geq 0$, of dimension $n + 1$; the [Grothendieck group](#def:grothendieck-group-of-a-qou) is $\mathbb{Z}[x]$ with $x = [V_1]$.

**Characters.** Restricted to the maximal torus $\{ \mathrm{diag}(t, t^{-1}) \}$, the weights of $V_n$ are $n, n-2, \dots, -n$, so its character is the Laurent polynomial

$$
  \mathrm{ch}(V_n)(t) \;=\; t^{n} + t^{n-2} + \cdots + t^{-n} \;=\; t^{-n}\bigl(1 + t^{2} + \cdots + t^{2n}\bigr).
$$

Characters are additive on direct sums and multiplicative on tensor products, and a representation of $\mathrm{SU}(2)$ is determined by its character; so $[V] \mapsto \mathrm{ch}(V)$ identifies $K_0(\mathrm{Rep}\,\mathrm{SU}(2))$ with the ring $\mathbb{Z}[t, t^{-1}]^{S_2}$ of Laurent polynomials symmetric under $t \mapsto t^{-1}$ \cite{fulton-harris1991}. This is the [Chern character](#def:chern-character) of the category in the presentation of $HH_0$ by class functions: the class $[\mathrm{id}_{V_n}]$ corresponds to the function $\mathrm{ch}(V_n)$ on the torus.

**Two evaluations.** At $t = 1$ every term is $1$, and $\mathrm{ch}(V_n)(1) = n + 1 = \dim V_n$. At $t = q$, the quantum group $\mathrm{SU}_q(2)$ has the same simple objects and the same characters, but its rigid trace is the *quantum* trace, weighted by the pivotal element; the quantum dimension is the character evaluated there,

$$
  \dim_q(V_n) \;=\; \mathrm{ch}(V_n)(q) \;=\; \frac{q^{n+1} - q^{-(n+1)}}{q - q^{-1}} \;=\; [n+1]_q ,
$$

the symmetric quantum integer \cite{kassel1995}. For the fundamental object, $\dim_q(V_1) = q + q^{-1} = [2]_q$. Three identities follow: $\mathrm{ch}(V_n)(1) = n+1$, $(q - q^{-1})\,\mathrm{ch}(V_n)(q) = q^{n+1} - q^{-(n+1)}$, and $\mathrm{ch}(V_1)(q) = q + q^{-1}$.

**What the example shows.** The character has $n + 1$ terms and does not depend on $q$; the quantum dimension is a single number and does. Their relation is exactly $\dim_q = \mathrm{ev}_q \circ \mathrm{ch}$ of the definition, with $\mathrm{ev}_q$ the evaluation of a class function at the pivotal element. Two consequences follow at once. First, $\dim_q(V_n) > 0$ for every real $q > 0$ and every $n$: a quantum dimension in this category is positive, and a negative number such as $-6$ cannot be one. Second, for the coordinate algebra $A = \mathcal{O}(\mathrm{SU}(2))$ the Peter–Weyl decomposition $[A] = \sum_{n \geq 0} (n+1)[V_n]$ lives in a completion of $K_0$, and its quantum dimension $\sum_{n \geq 0} (n+1)[n+1]_q$ — or $\sum_m [m]_q^{2}$ for $A$ as a bimodule — is a divergent series at every real $q \neq 1$; what one assigns to it is a matter of regularisation, taken up where the base curve is discussed.
