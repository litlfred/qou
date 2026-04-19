Let $H_n(q)$ be the Iwahori--Hecke algebra with generators
$T_1, \ldots, T_{n-1}$ and the three defining relations

$$
\begin{aligned}
  \text{(H1)}\quad &T_i^2 = (q - q^{-1})\,T_i + 1 \\
  \text{(H2)}\quad &T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1} \\
  \text{(H3)}\quad &T_i T_j = T_j T_i \qquad (|i - j| \geq 2),
\end{aligned}
$$

and let $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Z}[q, q^{-1}]$
denote the Jones--Markov trace
([Markov trace](#thm:jones-markov-trace)).

**Proposition.** For every braid word
$\beta = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_\ell}^{\varepsilon_\ell}
  \in B_n$ with image $\rho(\beta) \in H_n(q)$ and unique
Gröbner--Shirshov normal form $\mathrm{NF}(\rho(\beta))$ under the
rewriting system
([Buchberger's theorem](#thm:ugb-buchberger)) oriented by (H1)/(H2)/(H3):

1. **(Skein identification.)** The (H1) rule is the Jones skein
   relation. Oriented as $T_i^2 \to (q - q^{-1})\,T_i + 1$, the
   two coefficients $(q - q^{-1}, \,1)$ are precisely the skein
   weights in
   $
     L_+ - L_- \;=\; (q - q^{-1})\,L_0.
   $
   The (H2) and (H3) rules are cost-preserving --- they permute
   monomials without changing the multiset of leading coefficients.

2. **(Cost equals Jones polynomial.)** Write
   $
     \mathrm{NF}(\rho(\beta)) \;=\; \sum_{w \in \text{NF-basis}} c_w(q)\;w,
     \qquad c_w(q) \in \mathbb{Z}[q, q^{-1}].
   $
   Then the Jones polynomial of the closure $\widehat{\beta}$ is
   $
     J_{\widehat\beta}(q) \;=\; \mathrm{tr}_M\!\bigl(\mathrm{NF}(\rho(\beta))\bigr)
     \;=\; \sum_{w} c_w(q)\,\mathrm{tr}_M(w),
   $
   where $\mathrm{tr}_M(w)$ depends only on the cycle structure of
   the underlying permutation of $w \in S_n$.

3. **(Cost well-definedness.)** The cost function
   $
     \mathrm{cost}(f) \;:=\; \sum_{m \in \mathrm{supp}(f)} |c_m(q)|
   $
   (the $\mathrm{heckeCost}$ of
   [Hecke--GS](#def:jet-stratified-reduction)) is independent of the
   reduction order by the threading-cost uniqueness theorem (a
   consequence of [Buchberger's theorem](#thm:ugb-buchberger)
   applied to $H_n(q)$).

*Proof sketch.* (1) is the definitional content of the (H1) rule
--- expanding $\mathrm{heckeRelation}$ gives
$([T_i, T_i], 1),\; ([T_i], -(q - q^{-1})),\; ([\,], -1)$,
matching the skein trio $(L_+, L_0, 1)$ up to sign.

(2) follows from Jones 1987, Theorem 5.1: the Markov trace on
$H_n(q)$ is the unique linear functional satisfying the two Markov
properties, and its value on a braid image is the writhe-normalised
Jones polynomial of the closure. Gröbner--Shirshov confluence
([S-polynomial decomposition](#prop:ugb-s-poly-decomposition))
guarantees that any reduction order produces the same NF, hence
the same trace value.

(3) is a direct corollary of
[Buchberger's theorem](#thm:ugb-buchberger): all S-polynomials of
(H1)/(H2)/(H3) reduce to zero (Bokut--Shiao 2001, Theorem 3.5),
so the Hecke rewriting system is a Gröbner--Shirshov basis and
normal forms are unique. $\square$

**Operational reading.** The reduction cost
$\mathrm{cost}(\mathrm{NF}(\rho(\beta)))$ counts the skein-weighted
work needed to evaluate $J_{\widehat\beta}(q)$ --- one factor of
$|q - q^{-1}|$ per (H1) application and one factor of $1$ per
trivial branch. (H2) and (H3) reshape monomials but do not add
skein weight. Thus GS reduction *is* the Jones recursion: a
confluent, order-independent algorithm for computing the Jones
polynomial of a closed braid, with the cost function serving as
its arithmetic complexity measure.
