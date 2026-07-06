**Setup.**
Let $\beta$ be a braid on $n$ strands with $c$ crossings. Let $L = \hat{\beta}$ be its closure, and let $\mathcal{R}(L)$ be the Skein resolution tree ([Skein Turing machine](#rem:skein-turing-machine)). We fix a polynomial bound $p(c) = c^d$. Let $\mathcal{R}^{\circ}(L, q)$ denote the polynomial observable subcategory ([polynomial observable subcategory](#def:polynomial-observable-subcategory)), and let $\mathcal{H}_c(L, q)$ denote the computational boundary ([computational boundary](#def:computational-boundary)).

**Conjecture ($\mathrm{P}$ versus $\mathrm{NP}$ as boundary emptiness).**

$$
  \boxed{
    \mathrm{P} = \mathrm{NP} \Longleftrightarrow \mathcal{H}_c(L, q) = \varnothing \text{ for every NP link } L
  }
$$

*$\mathrm{P} \neq \mathrm{NP}$ if and only if there exists an NP-complete link $L$ for which the computational horizon is non-empty:*

$$
  \mathrm{P} \neq \mathrm{NP} \Longleftrightarrow \exists L \text{ (NP-complete)} \text{ with } \mathcal{H}_c(L, q) \neq \varnothing.
$$

**The formal conjecture.**
*For the QOU at substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$ (non-torsion, [substrate $\mathbb{G}_m$-torsion](#rem:substrate-gm-torsion)):*

*There exists a family of braids $\{L_N = \hat{\beta}_N\}_{N \geq 1}$ with $c_N = 3N$ crossings encoding an NP-complete problem \cite{cook1971} such that:*

$$
  \mathcal{H}_c(L_N, q_0) \neq \varnothing \qquad \text{for all } N \geq N_0.
$$

*The computational boundary is non-empty. A genuine event horizon exists in the resolution tree, meaning $\mathrm{P} \neq \mathrm{NP}$ over $\mathbb{R}$ at $q = q_0$ \cite{freedman2003}.*
