**Proposition (Interface-knot contribution to canonical-atom Markov trace).**

*Let $\mathcal{B}_K \in H_{3A}(q)$ be the canonical atomic braid for atom
$K = (Z, N)$ with $A = Z + N$, decomposed as*
$$
  \mathcal{B}_K \;=\; \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K
$$
*where $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)}$
is the disjoint Hecke product on disjoint 3-strand blocks (constituent
vacuum, `def:ew-interface-knot`) and
$\bowtie_K$ is the interface knot — a product of single-generator
crossings at the strand-block boundaries
$g \in \{3, 6, \ldots, 3(Z+N-1)\}$, each one either $\sigma_g$
(positive) or $\sigma_g^{-1}$ (negative).*

*Then the Markov trace ratio satisfies the **Markov-axiom interface
identity***
$$
  \boxed{\;
    \frac{\tau_M(\mathcal{B}_K)}{\tau_M(\mathcal{B}_K^{\mathrm{vac}})}
    \;=\; z(q)^{p_+(K)} \cdot \bigl(z(q) - h(q)\bigr)^{p_-(K)}
  \;}
  \tag{$\star$}
$$
*exactly, where $z(q) = 1/(q^{1/2}+q^{-1/2})$ is the Markov parameter,
$h(q) = q - q^{-1}$ is the Hecke skein parameter, and $p_+(K)$ /
$p_-(K)$ are the counts of positive / negative interface generators
in $\bowtie_K$.*
