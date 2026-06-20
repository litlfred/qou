*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Definition.**
*The **Hecke normal form** of an element $h \in H_n(R, q)$ is the
unique representative in the Gröbner--Shirshov canonical basis
obtained by iterated application of three rewriting rules:*

1. *Hecke relation: $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.*
2. *Far commutativity: $\sigma_i \sigma_j \to \sigma_j \sigma_i$
   for $|i - j| \geq 2$.*
3. *Yang--Baxter: $\sigma_i \sigma_{i+1} \sigma_i \to
   \sigma_{i+1} \sigma_i \sigma_{i+1}$ (in the direction
   decreasing shortlex order).*

*The reduction is confluent (Diamond Lemma), so the normal form
is independent of the order in which rules are applied.  The
resulting basis elements are in bijection with the symmetric
group $S_n$: each $w \in S_n$ gives a basis element
$T_w = T_{s_{i_1}} \cdots T_{s_{i_k}}$ for any reduced
expression $w = s_{i_1} \cdots s_{i_k}$.*

**Computational shortcut.**
*Under the Brundan–Kleshchev isomorphism the irreducible $T_w$
are equivalently the highest-weight vertices of a finite component
of the Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$; the
engine may compute $T_w$ by directed crystal traversal rather than
by S-polynomial overlap analysis.  See
[crystal-graph realisation](#conj:crystal-graph-realization).*
