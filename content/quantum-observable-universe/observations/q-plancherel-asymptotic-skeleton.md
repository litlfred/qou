*Let $w_\lambda^{(n)}(q) := \dim_q^2(\lambda) / [n]_q!$ be the q-deformed Wedderburn weight ([Wedderburn weight canonical form](#prop:wedderburn-weight-canonical)). We define a topological space $\mathcal{K}_q$ (the $q$-deformed Kerov limit-shape space) and pushforward maps*

$$
  \iota_n \colon \{\lambda \vdash n\}
    \;\longrightarrow\; \mathcal{K}_q,
  \qquad
  n \in \mathbb{N},
$$

*such that $\mu_n^{(q)} := (\iota_n)_*\,w_\lambda^{(n)}(q)$ satisfy:*

1. *(Existence at $q = 1$.) The sequence $\{\mu_n^{(1)}\}$ converges weakly to $\mu_\infty^{(1)}$* [`vershik-kerov1977`, `biane1998`].
2. *(Variance bound at generic $q$.) Character fluctuations have variance $O(1/\sqrt{n - 3})$* [`feray2010`].
3. *(Limit identification, conjectural.) For $q \neq 1$, $\{\mu_n^{(q)}\}$ converges weakly to $\mu_\infty^{(q)}$. We identify $\mu_\infty^{(q)}$ with a measure on $\pi_{\mathrm{GNS}}(H_\infty(q))$.*

**Established results.** Part (1) holds.

**Part (2) is NOT established for this weight — corrected 2026-09-05.** It
previously read "Parts (1) and (2) hold". The cited result is proved for a
*different measure*. Féray–Méliot's theorems are stated "under the
$q$-Plancherel measure $M_{n,q}$", whose Definition 1 is

$$
M_{n,q}(\lambda) \;=\; \frac{D_\lambda(q)\,\dim\lambda}{\{n!\}_q}
  \;=\; \frac{q^{b(\lambda)}\, f^\lambda}{\prod_{\square\in\lambda}\{h(\square)\}_q},
$$

which is **not** the $w_\lambda^{(n)}(q) = \dim_q^2(\lambda)/[n]_q!$ this block
pushes forward. Measured at the substrate $q_0$, `mp.dps = 50`:
$\sum_\lambda M_{n,q} = 1$ **exactly** at $n = 3,4,5,6,9,12$, while
$\sum_\lambda w_\lambda^{(n)}$ runs $0.9874 / 0.9822 / 0.9822 / 0.9911 /
1.1109 / 1.5171$; and the two disagree **per partition** by a relative
$0.158 / 0.320 / 0.575 / 0.951 / 3.53 / 12.6$ at those same $n$. They are not
one normalisation apart — at $n = 12$ they differ by more than an order of
magnitude on some $\lambda$. They coincide only at $q = 1$, which is exactly
why part (1) is unaffected and part (2) — stated "at generic $q$" — is not.

Note the $q>1$ hypothesis is *not* the obstruction: Féray–Méliot state their
theorems for $q<1$ but record that "in the case $q > 1$, our result gives the
asymptotic behavior of the columns", so the substrate's $q_0 \approx 1.11$
costs an orientation (rows $\leftrightarrow$ columns), not the theorem.

The honest status of part (2) is therefore: **holds for $M_{n,q}$; its transfer
to $w_\lambda^{(n)}(q)$ is unestablished.** Closing it means either proving the
transfer, restating this skeleton over $M_{n,q}$, or checking whether
Theorem 1.1's hypothesis class is broad enough to cover $w_\lambda^{(n)}$ —
none of which has been done. Bean `qou-hu7j`.

**Conjectural results.** Part (3) isolates two open problems: q-deformed Kerov–Vershik convergence and operator-algebra realisation.
