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

*with $f^\lambda$ the number of standard Young tableaux and $h(\square)$ the hook lengths. Here $n(\lambda)$ is Macdonald's partition statistic, not a function of the size $n$ — the two are distinct objects sharing a glyph, and the size is always the bare $n$. We write $\lambda'$ for the conjugate (transposed) partition and $c(\square) = j - i$ for the content of the box in row $i$, column $j$. The blackboard-bold $\mathbb{M}$ follows the $\mathbb{V}$ precedent in the notation register: it is the source literature's own symbol, raised out of plain $M$ and $\mathcal{M}$, both of which are claimed here (the latter by the mass endomorphism). We define a topological space $\mathcal{K}_q$ (the $q$-deformed Kerov limit-shape space) and pushforward maps*

$$
  \iota_n \colon \{\lambda \vdash n\}
    \;\longrightarrow\; \mathcal{K}_q,
  \qquad
  n \in \mathbb{N},
$$

*such that $\mu_n^{(q)} := (\iota_n)_*\,\mathbb{M}_{n,q}$ satisfy:*

1. *(Existence at $q = 1$.) The sequence $\{\mu_n^{(1)}\}$ converges weakly to $\mu_\infty^{(1)}$* [`vershik-kerov1977`, `biane1998`].
2. *(Asymptotics at generic $q$.) The row lengths obey a law of large numbers, $\lambda_i/n \to (1-q)q^{i-1}$ in probability, and their fluctuations are asymptotically Gaussian at scale $\sqrt{n}$* [`feray-meliot2012`].
3. *(Limit identification, conjectural.) For $q \neq 1$, $\{\mu_n^{(q)}\}$ converges weakly to $\mu_\infty^{(q)}$. We identify $\mu_\infty^{(q)}$ with a measure on $\pi_{\mathrm{GNS}}(H_\infty(q))$.*

## Which weight this is, and why it changed

**Identification of $\mathbb{M}_{n,q}$ with the Molien fake-degree measure.** Note that the Plancherel measure $\mathbb{M}_{n,q}$ governing clause 2 is distinct from the squared-quantum-dimension weight $w_\lambda^{(n)}(q) = \dim_q^2(\lambda)/[n]_q!$; rather, $\mathbb{M}_{n,q}$ coincides with the Molien fake-degree weight, which satisfies

$$
  \frac{f^\lambda \, q^{-\kappa_\lambda} \, \dim_q(\lambda)}{[n]_q!}
  \;=\; \mathbb{M}_{n,\,q^2}(\lambda),
  \qquad
  \kappa_\lambda \;=\; \sum_{\square \in \lambda} c(\square),
$$

verified in exact rational arithmetic for every partition of $n = 1,\dots,9$. So this proposition is not being restated over a *new* object; it is being restated over one the corpus has had all along, with the substitution $Q = q^2$ making the identification.

**The exponent $\kappa_\lambda$ is forced, not chosen.** Substituting $Q = q^2$ into the display above leaves $q^{2n(\lambda) - \sum_\square h(\square) + n}$, which collapses to $q^{-\kappa_\lambda}$ by two identities — $\sum_\square h(\square) = n(\lambda) + n(\lambda') + n$ and $\kappa_\lambda = n(\lambda') - n(\lambda)$ — each verified independently over all partitions of $n \leq 10$ in the same probe. Without them the identity would be an agreement at $96$ sample points; with them it is a derivation.

This also explains a coincidence the corpus carried without comment: the proved identity $\sum_\lambda f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda) = [n]_q!$ holds for every $n$, and $\mathbb{M}_{n,q}$ is a probability measure by construction. Those are the same theorem.

## The substrate sits at $q > 1$, and that costs an orientation, not the theorem

[`feray-meliot2012`] states its asymptotics for $q < 1$, while the substrate gives $Q = q_0^2 \approx 1.2321$. The paper's own duality $\mathbb{M}_{n,q^{-1}}(\lambda') = \mathbb{M}_{n,q}(\lambda)$ closes the gap: it is an *exact* identity, verified here over all partitions of $n \leq 9$ in exact arithmetic, so the $Q > 1$ results are the $Q^{-1} < 1$ results read on conjugate diagrams. Clause 2 at the substrate therefore describes the **columns** of $\lambda$ where the cited statement describes rows. Nothing is lost and nothing is approximated; the reader has to transpose.

## What is still open

**The transfer to $w_\lambda^{(n)}(q) = \dim_q^2/[n]_q!$ is unestablished, and that family is still in production.** Restating *this* block does not migrate [`plancherel-term-7-formulation`](../mass-theory/plancherel-term-7-formulation.md), whose $\Phi_k$ functional is defined against a $\dim_q^2$ family. The canonical numerator for $\Phi_k$ is the Molien weight $f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda)/[n]_q!$, with the self-normalised $\dim_q^2/\sum_\mu \dim_q^2$ kept as a labelled comparison arm; what remains is to migrate the functional onto it. The choice is not cosmetic: the same harness ranks three different distinguished knots at $k = 3$ under three of the candidate families.

**Clause 3 remains conjectural**, isolating two open problems: $q$-deformed Kerov–Vershik convergence, and the operator-algebra realisation of the limit.
