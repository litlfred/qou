*Let $\mathbb{M}_{n,q}$ denote the $q$-Plancherel measure on partitions of $n$,*

$$
  \mathbb{M}_{n,q}(\lambda)
  \;=\; \frac{q^{n(\lambda)}\, f^\lambda}
             {\prod_{\square \in \lambda} \{h(\square)\}_q},
  \qquad
  \{k\}_q \;=\; \frac{q^k - 1}{q - 1},
  \quad
  n(\lambda) \;=\; \sum_i (i-1)\lambda_i ,
$$

*with $f^\lambda$ the number of standard Young tableaux and $h(\square)$ the hook lengths. Here $n(\lambda)$ is Macdonald's partition statistic, not a function of the size $n$ — the two are distinct objects sharing a glyph, and the size is always the bare $n$. Here $\lambda'$ denotes the conjugate (transposed) partition and $c(\square) = j - i$ denotes the content of the box in row $i$, column $j$. The blackboard-bold $\mathbb{M}$ keeps the Plancherel measure distinct from plain $M$ and from the mass endomorphism $\mathcal{M}$. Let $\mathcal{K}_q$ denote a topological space (the $q$-deformed Kerov limit-shape space) equipped with pushforward maps*

$$
  \iota_n \colon \{\lambda \vdash n\}
    \;\longrightarrow\; \mathcal{K}_q,
  \qquad
  n \in \mathbb{N},
$$

*such that $\mu_n^{(q)} := (\iota_n)_*\,\mathbb{M}_{n,q}$ satisfy:*

1. *(Existence at $q = 1$.) The sequence $\{\mu_n^{(1)}\}$ converges weakly to $\mu_\infty^{(1)}$* [`vershik-kerov1977`, `biane1998`].
2. *(Asymptotics at generic $q$.) The row lengths obey a law of large numbers, $\lambda_i/n \to (1-q)q^{i-1}$ in probability, and their fluctuations are asymptotically Gaussian at scale $\sqrt{n}$* [`feray-meliot2012`].
3. *(Limit identification, conjectural.) For $q \neq 1$, $\{\mu_n^{(q)}\}$ converges weakly to $\mu_\infty^{(q)}$, where $\mu_\infty^{(q)}$ corresponds to a measure on $\pi_{\mathrm{GNS}}(H_\infty(q))$.*

## Relation to the Molien fake-degree measure

**Identification of $\mathbb{M}_{n,q}$ with the Molien fake-degree measure.** The Plancherel measure $\mathbb{M}_{n,q}$ governing clause 2 is distinct from the squared-quantum-dimension weight $w_\lambda^{(n)}(q) = \dim_q^2(\lambda)/[n]_q!$; rather, $\mathbb{M}_{n,q}$ coincides with the Molien fake-degree weight satisfying

$$
  \frac{f^\lambda \, q^{-\kappa_\lambda} \, \dim_q(\lambda)}{[n]_q!}
  \;=\; \mathbb{M}_{n,\,q^2}(\lambda),
  \qquad
  \kappa_\lambda \;=\; \sum_{\square \in \lambda} c(\square),
$$

verified in exact rational arithmetic for every partition of $n = 1,\dots,9$, with the substitution $Q = q^2$ making the identification.

**The exponent $\kappa_\lambda$ is algebraically forced.** Substituting $Q = q^2$ into the display above leaves $q^{2n(\lambda) - \sum_\square h(\square) + n}$, which collapses to $q^{-\kappa_\lambda}$ by two identities — $\sum_\square h(\square) = n(\lambda) + n(\lambda') + n$ and $\kappa_\lambda = n(\lambda') - n(\lambda)$ — each verified independently over all partitions of $n \leq 10$ in exact arithmetic. Without them the identity would be an agreement at $96$ sample points; with them it is a derivation.

Consequently, the Molien sum identity $\sum_\lambda f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda) = [n]_q!$ and the normalization of $\mathbb{M}_{n,q}$ as a probability measure express the same algebraic theorem.

## The aether sits at $q > 1$, and that costs an orientation, not the theorem

[`feray-meliot2012`] states its asymptotics for $q < 1$, while the aether gives $Q = q_0^2 \approx 1.2321$. The paper's own duality $\mathbb{M}_{n,q^{-1}}(\lambda') = \mathbb{M}_{n,q}(\lambda)$ closes the gap: it is an *exact* identity, verified over all partitions of $n \leq 9$ in exact arithmetic, so the $Q > 1$ results are the $Q^{-1} < 1$ results read on conjugate diagrams. Clause 2 at the aether therefore describes the **columns** of $\lambda$ where the cited statement describes rows. Nothing is lost and nothing is approximated; passing to $Q > 1$ simply transposes diagrams.

## Unresolved asymptotic questions

**Transfer to $w_\lambda^{(n)}(q) = \dim_q^2/[n]_q!$ remains unestablished.** The functional $\Phi_k$ in [the Plancherel mass-functional formulation](../mass-theory/plancherel-term-7-formulation.md) is defined against a $\dim_q^2$ weight family, whereas the canonical Molien numerator is $f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda)/[n]_q!$, with the self-normalised $\dim_q^2/\sum_\mu \dim_q^2$ retained as a comparison family; reconciling the two weight families is unresolved. The distinction is substantive: at $k = 3$, three candidate weight families rank three different distinguished knots first.

**Clause 3 is conjectural**, isolating two unproved analytic steps: $q$-deformed Kerov–Vershik convergence and the operator-algebra realisation of the limit.
