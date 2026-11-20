**Conjecture ($q$-Collatz, within a QOU).**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ ([torsion avoidance](#rem:substrate-gm-torsion)), and let $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$ be the Skein module of its Reeb bundle $\mathcal{R}_p = (S^3 \to S^2, \xi_q)$ ([Reeb bundle](#def:reeb-bundle)). This is a statement about the $q$-deformed Skein dynamics *of the QOU* — not a claim about the classical Collatz problem, which it recovers only in the archimedean limit $q \to 1$, and only when the substrate admits a well-defined standard part.

We use the combinatorial $q$-integer $[n]_q = (q^n - 1)/(q - 1)$, giving $[2]_q = q + 1$ and $[3]_q = q^2 + q + 1$. The Iwahori--Hecke algebra convention $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ differs by a factor of $q^{(n-1)/2}$. The combinatorial convention ensures the Skein divisibility identity $[3]_q = q[2]_q + 1$ and the contraction gap $[2]_q^2 - [3]_q = q$.

An element $P \in \mathbb{Z}[q^{\pm 1}]$ is $q$-even if $[2]_q \mid P$ and $q$-odd if $[2]_q \mid (P + 1)$. At $q = 1$, we recover integer parity ($[2]_1 = 2$).

Unlike the integers — where every element is even or odd — a Laurent polynomial need be neither: $P$ is $q$-even iff $P(-1) = 0$ and $q$-odd iff $P(-1) = -1$ (evaluating modulo $[2]_q$, i.e. at $q = -1$), so $\mathcal{C}_q$ is a **partial** map, undefined when $P(-1) \notin \{0, -1\}$. Moreover this domain is not forward-invariant: almost every positive element leaves it within a few steps. Accordingly the positive cone below is the **domain-stable** cone — the elements whose entire forward orbit remains $q$-even-or-$q$-odd — a feature with no classical analog.

Define the Skein-Collatz map $\mathcal{C}_q \colon \mathbb{Z}[q^{\pm 1}] \to \mathbb{Z}[q^{\pm 1}]$ by:

$$
\mathcal{C}_q(P) =
\begin{cases}
  P / [2]_q & P \text{ is } q\text{-even},\\[4pt]
  \bigl([3]_q P + 1\bigr) / [2]_q & P \text{ is } q\text{-odd}.
\end{cases}
$$

The odd branch is well-defined by the Skein divisibility identity:

$$
[3]_q = q[2]_q + 1.
$$

Since $P$ is $q$-odd ($[2]_q \mid P + 1$), the numerator is divisible by $[2]_q$. Writing $P + 1 = [2]_q Q$:

$$
\mathcal{C}_q(P) = qP + Q = [3]_q Q - q.
$$

At $q = 1$, $\mathcal{C}_1(n) = n/2$ (even) or $(3n+1)/2$ (odd), recovering the Syracuse map.

Each application of $\mathcal{C}_q$ corresponds to a crossing resolution in the Skein module ([skein generation](#prop:skein-generation)):

- **Even branch** ($P/[2]_q$): Markov destabilization removes one strand from the braid closure, dividing the Jones polynomial by the Markov parameter. This is the $q$-analog of "halving."
- **Odd branch** ($([3]_q P + 1)/[2]_q$): The Hecke relation $T^2 = (q - q^{-1})T + 1$ reduces a quadratic crossing word to linear, followed by destabilization.

The Skein relation $qL_+ - q^{-1}L_- = (q - q^{-1})L_0$ ensures each resolution step is a convex combination:

$$
J(L_+) = q^{-2}J(L_-) + (1 - q^{-2})J(L_0).
$$

For $q > 1$, both coefficients are positive and sum to $1$. The crossing resolution is non-expansive on the Jones polynomial.

The algebraic identity $[2]_q^2 - [3]_q = q$ controls the contraction. Over one Collatz cycle (one odd step followed by enough even steps to exhaust $[2]_q$-divisibility):

- The odd step maps $P \mapsto [3]_q Q - q$. The ratio $|P|/|Q| \approx [2]_q$.
- Subsequent even steps divide by $[2]_q$.

If each tripling is followed by at least two halvings on average, the orbit contracts. Two halvings multiply by $1/[2]_q^2$; one tripling multiplies by $[3]_q/[2]_q$. The net factor per cycle is $[3]_q / [2]_q^3 < 1$, with margin:

$$
[2]_q^2 - [3]_q = q.
$$

Two halvings beat one tripling by a factor $[2]_q^2 / [3]_q = 1 + q/[3]_q \approx 4/3$.

**Conjecture.** Given the QOU above, for all $q > 1$ and all $P \in \mathbb{Z}[q^{\pm 1}]_{>0}$ the orbit $\{\mathcal{C}_q^k(P)\}_{k \geq 0}$ reaches the fundamental $2$-cycle $\{q^{-1},\, 1 + q^{-1}\}$.

At the Skein level the attractor is this $2$-cycle, not the literal unknot polynomial $1$: since $1$ evaluates to $1 \notin \{0, -1\}$ modulo $[2]_q$ (i.e. at $q = -1$), it is neither $q$-even nor $q$-odd, so $\mathcal{C}_q(1)$ is undefined. The cycle $\{q^{-1}, 1 + q^{-1}\}$ is the $q$-lift of the classical $\{1, 2\}$; writing the classical target as "$1$" is the $q \to 1$ shorthand.

The Collatz obstruction $\kappa_C := \mathrm{res}_{C_q}(\kappa_0) \in H^2(\mathcal{S}_{C_q}, \mathbb{G}_m)$ ([classical limit obstruction](#def:classical-limit-obstruction), [QOU obstruction reduction](#thm:qou-obstruction-reduction)) measures the failure of Skein-Collatz orbits to converge. One direction is safe: convergence of every orbit forces $\kappa_C = 0$. The converse — that $\kappa_C = 0$ suffices for convergence — is **not** established and is not claimed: $\kappa_C$ is linked only to the Kummer-removability leg, a divisibility fact about $\chi(A)$.

**Why the converse cannot be cheap (the genericity caveat).** The caveat recorded on the $\mathrm{P}$ versus $\mathrm{NP}$ leg applies here too, and is stated now so it is not rediscovered. Two steps:

1. *Vanishing at a given Kummer level is a divisibility fact, not a dynamical one.* By [QOU obstruction reduction](#thm:qou-obstruction-reduction)(c) the obstruction vanishes at level $n$ exactly when $n \mid \chi(A)$; at $\chi_{\mathrm{eu}}(M_0) = -6$ the even-branch level $n = 2$ therefore vanishes, and this is proved outright without settling any orbit. The set of levels at which it *persists* is cofinite by elementary arithmetic — only $n \in \{1, 2, 3, 6\}$ divide $-6$. (The analogous statement for the substrate *parameter* $q$, that a nonzero polynomial obstruction has cofinite non-vanishing locus, also holds; it is a parallel fact over a different index set, not the same one.) Cheapness of this kind cannot **by itself** discharge an equivalence with a hard uniform statement without collapsing the equivalence — a scope-(a) objection to the route as stated, not a proof that no such equivalence holds.
2. *The content does not live in the ideal.* By Reeb-flow Turing-completeness the halting set is undecidable, hence not cut out by any ideal ([one length filtration, three problems](#rem:skein-filtration-trichotomy)). Note carefully what this does **not** say: it bars an ideal-theoretic description of the halting **set**, and it does *not* bar a scalar equivalent to the single proposition "every orbit converges" — such a scalar exists trivially, since any proposition is equivalent to itself. Conflating the two is a recurring error, and this sentence carried it until 2026-08-15. What the undecidability does establish is that the content cannot be *recovered from* the ideal, so it sits in the filtration. This is structurally analogous to — not an instance of — the algebrization barrier \cite{aaronsonwigderson2009} and the algebraic-natural-proofs barrier \cite{grochow2017}; the shared moral is that a technique insensitive to the hard structure cannot separate, not any formal content of those theorems, which concern proof techniques in Boolean complexity and say nothing about Collatz \cite{razborovrudich1997}.

The conjecture's content therefore sits in the descent measure on the filtration, not in the vanishing of $\kappa_C$. Compare the same caveat on the $\mathrm{P}$ versus $\mathrm{NP}$ leg ([$\mathrm{P} \neq \mathrm{NP}$ at non-torsion $q$](#conj:qou-p-neq-np)) and on the Navier--Stokes leg ([Kummer specialisation](#prop:ns-kummer-specialisation)).

**The shared class transfers nothing between legs.** Because level-$2$ vanishing holds on this leg while the resolution-tree restriction is non-zero at the strictly non-torsion $q_0$ ([$\mathrm{P} \neq \mathrm{NP}$ at non-torsion $q$](#conj:qou-p-neq-np)), the several restrictions of $\kappa_0$ carry *different* verdicts simultaneously. Identifying them would force this conjecture and $\mathrm{P} \neq \mathrm{NP}$ to be incompatible; that identification is refuted by the pair just described. The class is shared; the verdicts are not.

**Shared substrate.** Convergence is the *descent* leg of the shared length-filtration trichotomy on $\mathcal{S}(q)$ ([one length filtration, three problems](#rem:skein-filtration-trichotomy)): $q$-Collatz asks the crossing-number filtration $\ell$ to **descend** to the normal form, while $\mathrm{P}$ vs $\mathrm{NP}$ asks reachability within a polynomial $\ell$-budget and $q$-Navier--Stokes asks $\ell$ to stay **bounded**. The three legs are three predicates on one shared object, the skein observation system on $\mathcal{S}(q)$ (this convergence question is its halting predicate).
