---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-011-52-exclusion-measures
section_title: "Exclusion measures"
section_number: 5.2
pages: 16-17
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.984
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#ss:exclusion label="ss:exclusion"}

The symmetric group ${\cal S}_n$ acts on ${\mathcal B}_n$ by permuting the coordinates. Suppose a nonnegative rate $r(\tau)$ is given for each transposition $\tau \in {\cal S}_n$. Define a random evolution on ${\mathcal B}_n$ by letting each pair of coordinates $(i,j)$ transpose independently at rate $r(\tau_{ij})$. In other words, we have a continuous time chain on ${\mathcal B}_n$ which jumps from $x$ to $\tau (x)$ at rate $r(\tau)$ for each transposition $\tau$. This process is known as the symmetric exclusion process.

Borcea, Branden and Liggett [@borcea-branden-liggett Proposition 5.1] prove that the strong Rayleigh property is preserved under this evolution. In particular, because the point mass at a single state is always strong Rayleigh, it follows that the time $t$ distribution of a symmetric exclusion process started from a deterministic state is strong Rayleigh. The stochastic covering property follows, as do PHR and negative association. Interestingly, before the publication of [@borcea-branden-liggett], all that was known about this model was negative cylinder dependence [@liggett77 Lemma 2.3.4]).

Recently, it was shown by [@wagner-BAMS] that one can add birth and death to the exclusion dynamics and still preserve the strong Rayleigh property. More specifically, let $\{ \alpha_i ,
\beta_i : 1 \leq i \leq n \}$ be positive real numbers and let $\omega_i$ change to one at rate $\alpha_i$ and to zero at rate $\beta_i$, along with the exclusion dynamics. Then the evolution preserves the strong Rayleigh property and in particular, if the starting state is deterministic, all time $t$ marginals are strong Rayleigh.

::: cor
[]{#cor:exclusion label="cor:exclusion"} Let ${\mathbb P}$ be the law on ${\mathcal B}_n$ resulting from running an exclusion process for a fixed time, starting from a deterministic state with $k$ sites occupied. Then $${\mathbb P}(f - {\mathbb E}f \geq a) \leq e^{- a^2 / (8 k)} \, .$$
:::

::: example
[]{#eg:exclusion label="eg:exclusion"} Let $n > 0$ be even and populate a $n \times n$ square of the integer lattice in $\mathbb{Z}^2$ (with torus boundary conditions) by filling all sites in the left half and leaving empty all sites in the right half. Run the symmetric exclusion process for time $t$ with rate 1 on each edge. Let $f_t (\omega)$ denote the number of edges at time $t$ with exactly one endpoint occupied. The mean of $f_t$ starts at $n$ at time 0 and approaches its limiting value of $n^2 - O(1)$ as $t \to \infty$. Once $t = \Theta (n^2)$, the variance of $f_t$ becomes $\Theta (n^2)$ and the concentration inequality $${\mathbb P}(f - {\mathbb E}f \geq a) \leq e^{- a^2 / (4 n^2 )} \, ,$$ which holds for all $t$, becomes a meaningful Gaussian tail bound (here $k = n^2 / 2$).
:::
