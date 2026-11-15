---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-002-skew-characters
section_title: "Skew characters"
section_number: 3
pages: 9-18
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
text_source: latex
latex_prose_ratio: 0.799
latex_coverage_ratio: 0.954
---
[]{#sec:skew label="sec:skew"}

In this section we state and prove a result on the values of skew characters on elements of the form $g_{n\alpha}$ (Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}). First, we give the necessary combinatorial definitions. In several arguments we shall refer to James' abacus notation for partitions, as described in [@JK page 78].

## Quotients of skew-partitions {#subsec:quotients}

We shall define $n$-quotients and $n$-signs for the following class of skew-partitions.

::: definition
[]{#def:n_dec label="def:n_dec"} Let $m$, $n \in \mathbf{N}$. We say that a skew-partition $\lambda /\mu$ of $mn$ is *$n$-decomposable* if there exists a border-strip tableau of shape $\lambda / \mu$ and type $(n^m)$.
:::

::: definition
[]{#def:n_quo label="def:n_quo"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be an $n$-decomposable skew-partition of $mn$. Let $\Gamma(\lambda)$ be an abacus display for $\lambda$ on an $n$-runner abacus using $tn$ beads for some $t \in \mathbf{N}$. Let $\Gamma(\mu)$ be the abacus display for $\mu$ obtained by performing an appropriate sequence of $m$ upward bead moves on $\Gamma(\lambda)$.

(This is possible since $\lambda / \mu$ is $n$-decomposable.)

Let $(\lambda^{(0)}, \ldots, \lambda^{(n-1)})$ and $(\mu^{(0)}, \ldots, \mu^{(n-1)})$ be the $n$-quotients of $\lambda$ and $\mu$ corresponding to $\Gamma(\lambda)$ and $\Gamma(\mu)$, respectively. The *$n$-quotient* of $\lambda / \mu$ is defined to be $$(\lambda^{(0)} / \mu^{(0)}, \ldots, \lambda^{(n-1)} / \mu^{(n-1)}).$$ We define the $n$-*sign* of $\lambda / \mu$, denoted $\varepsilon_n(\lambda/\mu)$ to be the sign of any border-strip tableau of shape $\lambda / \mu$ and type $(n^m)$.
:::

To avoid cumbersome restatements, we adopt the convention that $\lambda^{(i)} / \mu^{(i)}$ always has the meaning of Definition [\[def:n_quo\]](#def:n_quo){reference-type="ref" reference="def:n_quo"} above. It is clear from the abacus that $\mu^{(i)}$ is a subpartition of $\lambda^{(i)}$ for each $i \in \{0,\ldots,n-1\}$, and so the $n$-quotient is well-defined. It follows from Proposition 3.13 in [@OlssonCombinatorics], or our Proposition [\[prop:nbij\]](#prop:nbij){reference-type="ref" reference="prop:nbij"} below, that the $n$-sign of a skew-partition is well defined. See §[0.4](#subsec:example){reference-type="ref" reference="subsec:example"} below for an example of these definitions and all the results in this section.

We remark that it appears to be impossible to define the $n$-core of an arbitrary skew-partition. The example $\lambda / \mu = (2,2) / (1)$ and $n=2$ illustrates the obstacles that arise. Representing $\lambda$ on a $2$-runner abacus as $$\begin{matrix} \circ& \circ\\ \bullet& \bullet\end{matrix}$$ we see that either bead may be moved up, giving two different skew-partitions from which no border strip of length $2$ can be removed, namely $(2) /(1)$ and $(1,1) / (1)$. The $2$-quotients corresponding to these bead moves, namely $((1),\varnothing)$ and $(\varnothing,(1))$, are also different.

::: theorem
[]{#thm:ind label="thm:ind"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. Let $\alpha$ be a partition of $m$. If $\lambda / \mu$ is not $n$-decomposable then $\chi^{\lambda / \mu}(g_{n \alpha}) = 0$. If $\lambda / \mu$ is $n$-decomposable and $(\lambda^{(0)} / \mu^{(0)}, \ldots, \lambda^{(n-1)} / \mu^{(n-1)})$ is its $n$-quotient, then $$\chi^{\lambda / \mu}(g_{n\alpha}) = \varepsilon_n(\lambda / \mu)
\mathop{\mathrm{Ind}}^{S_m}_{S_{\ell_0} \times \cdots \times S_{\ell_{n-1}}}
\bigl(
\chi^{\lambda^{(0)} / \mu^{(0)}} \times \cdots \times 
\chi^{\lambda^{(n-1)}/ \mu^{(n-1)}} \bigr)
(g_\alpha)$$ where $|\lambda^{(i)} / \mu^{(i)}| = \ell_i$.
:::

This result, stated in the alternative language of star diagrams, was first proved in [@Farahat1954 Section 4]. The special case where $\mu$ is the $n$-core of $\lambda$ also follows from the correction by Thrall and Robinson [@ThrallRobinson1951] to Section 7 of Robinson [@Robinson1947] or, alternatively, from Littlewood's result in [@Littlewood1951 Section 2]. Farahat's proof depends on an algebraic argument using Schur functions. A character-theoretic proof is given by Kerber, Sänger, and Wagner: see [@KSW Equation 3.6]. In the remainder of this section, we give a shorter character-theoretic proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}, expressing each side of the theorem as a sum, and then constructing a bijection between the summands. An example to illustrate this bijection is given in §[0.4](#subsec:example){reference-type="ref" reference="subsec:example"}. (Our bijection is similar to that defined using *Brettspiele* in [@KSW].)

## A model for induction from a Young subgroup {#subsec:model}

The following general result on the values of a character induced from a Young subgroup will be used in the proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}. (The notation is chosen to be consistent with this later use.)

::: lemma
[]{#lemma:model label="lemma:model"} Let $(\ell_0,\ldots,\ell_{n-1})$ be a composition of $m \in \mathbf{N}$. For each $i \in \{0,\ldots,n-1\}$, let $\vartheta_i$ be a character of $S_{\ell_i}$. If $g\in S_m$ then $$\mathop{\mathrm{Ind}}^{S_m}_{S_{\ell_0} \times \cdots \times S_{\ell_{n-1}}} 
(\vartheta_0 \times \cdots \times \vartheta_{n-1})(g)
=
\sum_{\mathbf{t}} \vartheta_0(g_{\alpha_0(\mathbf{t})}) \ldots
\vartheta_{n-1}(g_{\alpha_{n-1}(\mathbf{t})})$$ where the sum is over all $(\ell_0,\ldots,\ell_{n-1})$-tabloids $\mathbf{t}$ such that $g \mathbf{t} = \mathbf{t}$, and $\alpha_i(\mathbf{t})$ is the cycle type of the permutation induced by $g$ on the entries of row $i+1$ of $\mathbf{t}$.
:::

::: proof
*Proof.* Let $\mathbf{t}_1$, ..., $\mathbf{t}_N$ be the $(\ell_0,\ldots,\ell_{n-1})$-tabloids. Let $\mathbf{s}$ be a $(\ell_0,\ldots,\ell_{n-1})$-tabloid fixed by the Young subgroup $S_{\ell_0} \times \cdots \times S_{\ell_{n-1}}$. For each $j$ such that $1 \le j \le N$, choose $x_j \in S_m$ such that $\mathbf{t}_j =  x_j \mathbf{s}$. Let $\vartheta= \vartheta_0 \times \cdots \times \vartheta_{n-1}$. For each $g\in S_m$ we have $$\bigl( 
\mathop{\mathrm{Ind}}^{S_m}_{S_{\ell_0} \times \cdots \times 
S_{\ell_{n-1}}} \vartheta\bigr)
(g)
= 
\sum_j \vartheta(x_j^{-1}gx_j)$$ where the sum is over all $j$ such that $$x_j^{-1}gx_j \in S_{\ell_0} \times \cdots \times S_{\ell_{n-1}},$$ or, equivalently, over all $j$ such that $g \mathbf{t}_j  = \mathbf{t}_j$. If

$\Delta_1, \ldots, \Delta_q$ are the orbits of $g$ on row $i+1$ of $\mathbf{t}_j$, then

$x_j^{-1}\Delta_1, \ldots, x_j^{-1}\Delta_q$ are the orbits of $x_j^{-1}gx_j$ on row $i+1$ of $\mathbf{s}$. Hence $x_j^{-1}gx_j$ acts with cycle type $\alpha_i(\mathbf{t}_j)$ on row $i+1$ of $\mathbf{s}$ and so $$\vartheta(x_j^{-1}gx_j) = \vartheta_0(g_{\alpha_0(\mathbf{t_j})})
\ldots \vartheta_{n-1}(g_{\alpha_{n-1}(\mathbf{t_j})}).$$ The lemma follows. ◻
:::

## Proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"} {#subsec:cfs}

[]{#subsec:omega_proof label="subsec:omega_proof"}

Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. Let $\alpha$ be a partition of $m$. If there is a border-strip tableau of shape $\lambda /\mu$ and type $n\alpha$ then it is clear from the abacus that $\lambda / \mu$ is $n$-decomposable. Hence if $\lambda / \mu$ is not $n$-decomposable then, by the Murnaghan--Nakayama rule, $\chi^{\lambda/\mu}(g_{n \alpha}) = 0$.

We may therefore assume that $\lambda / \mu$ is $n$-decomposable. Let $\ell_i = |\lambda^{(i)} / \mu^{(i)}|$ for each $i \in \{0,\ldots,n-1\}$ and let $H = {S_{\ell_0} \times \cdots \times S_{\ell_{n-1}}}$. To show that $$\label{eq:charmain}
 \chi^{\lambda / \mu}(g_{n\alpha}) = \varepsilon_n(\lambda / \mu)
\mathop{\mathrm{Ind}}^{S_m}_H
\bigl(
\chi^{\lambda^{(0)} / \mu^{(0)}} \times \cdots 
\times \chi^{\lambda^{(n-1)} / \mu^{(n-1)}} \bigr)
(g_\alpha),$$ we shall use the following generalization of border-strip tableaux.

::: definition
[]{#def:n_bs label="def:n_bs"} Let $m$, $n \in \mathbf{N}$. Let $\lambda / \mu$ be an $n$-decomposable skew-partition and let $\alpha = (\alpha_1,\ldots,\alpha_k)$ be a composition of $m$. A *$n$-quotient border-strip tableau* of *shape $\lambda / \mu$* and *type* $\alpha$ is an $n$-tuple $(T_0, \ldots, T_{n-1})$ of border-strip tableaux such that

\(a\) for each $i \in \{0, \ldots, n-1\}$, the shape of $T_i$ is $\lambda^{(i)} 
/ \mu^{(i)}$, *and*

\(b\) for each $j \in \{1,\ldots,k\}$, the boxes in the $T_i$ labelled $j$ lie in a single tableau, where they form a border strip of length $\alpha_j$.
:::

By the Murnaghan--Nakayama rule we have $$\chi^{\lambda / \mu}(g_{n\alpha}) = \sum \mathrm{sgn}(T)$$ where the sum is over all border-strip tableaux of shape $\lambda / \mu$ and type $n\alpha$. The bijection in the following proposition implies that $$\label{eq:midpoint} \chi^{\lambda / \mu}(g_{n\alpha}) =
\varepsilon_n(\lambda / \mu) \sum \mathrm{sgn}(T_0) \ldots \mathrm{sgn}(T_{n-1})$$ where the sum is over all $n$-quotient border-strip tableaux $(T_0,\ldots,T_{n-1})$ of shape $\lambda / \mu$ and type $\alpha$. An illustrative example of the bijection is given in Figure [1](#fig:bijection){reference-type="ref" reference="fig:bijection"} in §[0.4](#subsec:example){reference-type="ref" reference="subsec:example"} below.

::: proposition
[]{#prop:nbij label="prop:nbij"} Let $\lambda / \mu$ be an $n$-decomposable skew-partition of $mn$ and let $\alpha = (\alpha_1,\ldots,\alpha_k)$ be a partition of $m$. There is a canonical bijection between border-strip tableaux of shape $\lambda / \mu$ and type $n\alpha$ and $n$-quotient border-strip tableaux of shape $\lambda / \mu$ and type $\alpha$. Under this bijection, if $T$ is mapped to $(T_0, \ldots, T_{n-1})$, then $$\mathrm{sgn}(T) = \varepsilon_n(\lambda / \mu)\, \mathrm{sgn}(T_0) \ldots \mathrm{sgn}(T_{n-1}).$$
:::

::: proof
*Proof.* Let $T$ be a border-strip tableau of shape $\lambda / \mu$ and type $\alpha$. The abacus gives a canonical bijection between border strips in $\lambda / \mu$ of length $n \ell$ and border strips of length $\ell$ in the skew-partitions $\lambda^{(i)} / \mu^{(i)}$ for $i \in \{0,\ldots,n-1\}$. If the border strip of length $n\alpha_k$ in $T$ corresponds to a border strip of length $\alpha_k$ in $\lambda^{(i_k)} / \mu^{(i_k)}$, then we label the corresponding boxes in the Young diagram of $\lambda^{(i_k)} / \mu^{(i_k)}$ by $k$. Removing these border strips from the tableaux concerned and iterating the process with the border strip of length $n\alpha_{k-1}$, and so on, we obtain a canonical bijection between border-strip tableaux of shape $\lambda / \mu$ and type $n\alpha$ and $n$-quotient border-strip tableaux of shape $\lambda / \mu$ and type $\alpha$.

It only remains to prove the assertion about signs. Since $\varepsilon_n(\lambda / \mu)$ is the common sign of any $\lambda/\mu$-tableau of shape $\lambda/\mu$ and type $(n^m)$, it suffices to show that if $T$ is a $\lambda/\mu$-tableau of type $n\alpha$ and $U$ is a $\lambda/\mu$-tableau of type $n\beta$ then $$\mathrm{sgn}(T) \mathrm{sgn}(U) = \mathrm{sgn}(T_0) \ldots \mathrm{sgn}(T_{n-1}) \mathrm{sgn}(U_0) \ldots \mathrm{sgn}(U_{n-1}).$$ Starting from $\Gamma(\lambda)$ with the beads numbered in order of their positions, perform the sequence of bead moves corresponding to $T$, then perform the inverse of the sequence of bead moves corresponding to $U$. Let $\sigma$ be the resulting permutation of the beads. Each time a border-strip of height $\ell$ is removed or added, the permutation required to restore the order of numbers is an $\ell+1$-cycle. Therefore $\mathop{\mathrm{sgn}}\sigma = \mathrm{sgn}(T) \mathrm{sgn}(U)$. On the other hand, $\sigma$ permutes the beads on each runner amongst themselves, and a similar argument shows that $\mathrm{sgn}(\sigma) =  \mathrm{sgn}(T_0) \ldots \mathrm{sgn}(T_{n-1}) \mathrm{sgn}(U_0) \ldots \mathrm{sgn}(U_{n-1})$. ◻
:::

Comparing Equations [\[eq:charmain\]](#eq:charmain){reference-type="eqref" reference="eq:charmain"} and [\[eq:midpoint\]](#eq:midpoint){reference-type="eqref" reference="eq:midpoint"} we see that to complete the proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}, it suffices to show that $$\label{eq:final} 
\sum \mathrm{sgn}(T_0) \ldots \mathrm{sgn}(T_{n-1}) =
\mathop{\mathrm{Ind}}^{S_m}_H 
\bigl(
\chi^{\lambda^{(0)} / \mu^{(0)}} \times \cdots 
\times \chi^{\lambda^{(n-1)} / \mu^{(n-1)}} \bigr) (g_\alpha)$$ where the sum is over all $n$-quotient border-strip tableaux $(T_0,\ldots,T_{n-1})$ of shape $\lambda / \mu$ and type $\alpha$. In fact Equation [\[eq:final\]](#eq:final){reference-type="eqref" reference="eq:final"} follows from Lemma [\[lemma:model\]](#lemma:model){reference-type="ref" reference="lemma:model"} and the Murnaghan--Nakayama rule, by some manipulations that are essentially formal. By Lemma [\[lemma:model\]](#lemma:model){reference-type="ref" reference="lemma:model"} we have $$\label{eq:formal1} 
\begin{split} \mathop{\mathrm{Ind}}^{S_m}_H 
\bigl( 
\chi^{\lambda^{(0)} /  \mu^{(0)}} {}&{}\times \cdots 
\times \chi^{\lambda^{(n-1)} / \mu^{(n-1)}} \bigr)
(g_\alpha)  \\ &= \sum_{\mathbf{t}} \chi^{\lambda^{(0)} / \mu^{(0)}} (g_{\alpha_0(\mathbf{t})})
\ldots \chi^{\lambda^{(n-1)} / \mu^{(n-1)}} (g_{\alpha_{n-1}(\mathbf{t})} )
\end{split}$$ where the sum is over all $(\ell_0,\ldots,\ell_{n-1})$-tabloids $\mathbf{t}$ such that $g_\alpha \mathbf{t} = \mathbf{t}$ and $\alpha_i(\mathbf{t})$ is the cycle type of the permutation of row $i+1$ of $\mathbf{t}$ induced by $g_\alpha$.

For such a tabloid $\mathbf{t}$, let

$$f(\mathbf{t}) = \sum \mathrm{sgn}(T_0) \ldots \mathrm{sgn}(T_{n-1})$$ where the sum is over all $n$-quotient border-strip tableaux $(T_0,\ldots, T_{n-1})$ of shape $\lambda / \mu$ and type $\alpha$, such that $T_i$ has a border strip labelled $j$ (of length $\alpha_j)$ if and only if the elements of the orbit of $g_\alpha$ corresponding to the part $\alpha_j$ lie in row $i+1$ of $\mathbf{t}$. The Murnaghan--Nakayama rule implies that if $g_\alpha \mathbf{t} = \mathbf{t}$ then $$\chi^{\lambda^{(0)} / \mu^{(0)}} (g_{\alpha_0(\mathbf{t})})
\ldots \chi^{\lambda^{(n-1)} / \mu^{(n-1)}} (g_{\alpha_{n-1}(\mathbf{t})} ) =  f(\mathbf{t}),$$ and so, by Equation [\[eq:formal1\]](#eq:formal1){reference-type="eqref" reference="eq:formal1"}, $$\label{eq:formal2} 
\mathop{\mathrm{Ind}}^{S_m}_H 
\bigl( 
\chi^{\lambda^{(0)} /  \mu^{(0)}} \times \cdots 
\times \chi^{\lambda^{(n-1)} / \mu^{(n-1)}} \bigr)
(g_\alpha) = \sum f(\mathbf{t})$$ where the sum is over all $(\ell_0, \ldots, \ell_{n-1})$-tabloids $\mathbf{t}$ such that $g_\alpha \mathbf{t} = \mathbf{t}$. Every $n$-quotient border-strip tableau of shape $\lambda /\mu$ and type $\alpha$ corresponds to some tabloid $\mathbf{t}$ such that $g_\alpha \mathbf{t} = \mathbf{t}$. Thus $$\label{eq:sums}
 \sum \mathrm{sgn}(T_0) \ldots \mathrm{sgn}(T_{n-1}) = \sum f(\mathbf{t})$$ where the left-hand sum is over all $n$-quotient border-strip tableaux of shape $\lambda / \mu$ and type $\alpha$, and the right-hand sum is over all $(\ell_0, \ldots, \ell_{n-1})$-tabloids $\mathbf{t}$ such that $g_\alpha \mathbf{t} = \mathbf{t}$. Equation [\[eq:final\]](#eq:final){reference-type="eqref" reference="eq:final"} now follows on comparing the two preceding equations.

## Example {#subsec:example}

We give an example of the correspondences used in the proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}. Let $\lambda / \mu = (8,5,3,2,2,2) / (2,2,1,1,1)$. Any border-strip tableau of shape $\lambda/\mu$ and type $(3^5)$ has either two or four $3$-border-strips of height $1$, with the rest of height $0$, so $\varepsilon_3(\lambda /\mu) = 1$. Let $\alpha = (2,1,1,1)$. By the Murnaghan--Nakayama rule, $\chi^{\lambda / \mu}(g_{3 \alpha})$

is the sum of the signs of the four border-strip tableaux of type $\lambda / \mu$ and type $3 \alpha =(6,3,3,3)$

shown in Figure [1](#fig:bijection){reference-type="ref" reference="fig:bijection"} above. Their signs are $+1$, $-1$, $-1$, $-1$, respectively, so $\chi^{\lambda / \mu}(g_{3 \alpha}) = -2$. These tableaux are in bijection with the four $3$-quotient border-strip tableaux of shape $\lambda / \mu$ and type $\alpha=(2,1,1,1)$ shown in Figure [1](#fig:bijection){reference-type="ref" reference="fig:bijection"}; since $\mathrm{sgn}_3(\lambda / \mu) = 1$, the bijection is sign preserving.

<figure id="fig:bijection">

<figcaption> The bijection in Proposition <a href="#prop:nbij" data-reference-type="ref" data-reference="prop:nbij">[prop:nbij]</a> between border-strip tableaux of shape <span class="math inline">(8,5,3,2,2,2)/(2,2,1,1,1)</span> and type <span class="math inline">(6,3,3,3)</span> and <span class="math inline">3</span>-quotient border-strip tableaux of the same shape and type <span class="math inline">(2,1,1,1)</span>. The shapes of the border-strip tableaux forming each <span class="math inline">3</span>-quotient border-strip tableau are given by the <span class="math inline">3</span>-quotient of <span class="math inline">(8,5,3,2,2,2)/(2,2,1,1,1)</span>, namely <span class="math inline">((1,1,1), (3,1)/(1,1), ⌀)</span>. To make clear the skew-shape, the tableaux of shape <span class="math inline">(3,1)/(1,1)</span> are drawn as <span class="math inline">(3,1)</span>-tableaux with two empty boxes. </figcaption>
</figure>

The $3$-quotient of $\lambda / \mu$ is $\bigl( (1,1,1), (3,1) / (1,1), \varnothing\bigr)$, so the characters of $S_3$ and $S_2$ we must consider are the sign character and the trivial character, respectively. Taking $g_{(2,1,1,1)} = (12) \in S_5$, and following the end of the proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}, we see that there are four $(3,2)$-tabloids fixed by $(12)$, namely $$\youngtabloid(345,12)\, , \quad \youngtabloid(123,45)\, , \quad \youngtabloid(124,35)\, , \quad \youngtabloid(125,34),$$ in the order corresponding to the tableaux shown in Figure [1](#fig:bijection){reference-type="ref" reference="fig:bijection"}. The corresponding values of the function $f$ used in the proof of Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"} are $+1$, $-1$, $-1$, $-1$ respectively. It should be noted that in general there will be several tableaux corresponding to each product of character values $$\chi^{\lambda^{(0)} / \mu^{(0)}} (g_{\alpha_{0}(\mathbf{t})})\ldots
\chi^{\lambda^{(n-1)} / \mu^{(n-1)}} (g_{\alpha_{n-1}(\mathbf{t})});$$ it is a special feature of this example that each $f(\mathbf{t})$ has a single summand, and so the bijection extends all the way to tabloids.

# Proof of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} {#sec:proof}

We shall prove Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} by induction on the number of parts of $\gamma$. Most of the work occurs in proving the base case when $\gamma$ has a single part. In the first step we combine the results of §3 and §4. For later use in §[\[sec:gendef\]](#sec:gendef){reference-type="ref" reference="sec:gendef"}, we state the following proposition for a general deflation map.

::: proposition
[]{#prop:gen_basecase label="prop:gen_basecase"} Let $m$, $n \in \mathbf{N}$, let $\vartheta$ be an irreducible character of $S_m$, and let $\lambda / \mu$ be a skew-partition of $mn$. Let $g\in S_n$ be an $n$-cycle. If $\lambda / \mu$ is not $n$-decomposable, then $\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n}(g) = 0$. If $\lambda / \mu$ is $n$-decomposable, then $$\begin{split}
(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n} 
\chi^{\lambda / \mu} )(g) 
= \varepsilon_n(\lambda / \mu)
\left< \mathop{\mathrm{Ind}}^{S_m}_H 
 \bigl(
\chi^{\lambda^{(0)} / \mu^{(0)}} \times \cdots \times 
\chi^{\lambda^{(n-1)}/ \mu^{(n-1)}} \bigr), \vartheta\right>,
\end{split}$$ where $H = S_{|\lambda^{(0)} / \mu^{(0)}|} \times \cdots
\times S_{|\lambda^{(n-1)} / \mu^{(n-1)}|}$.
:::

::: proof
*Proof.* If $\lambda / \mu$ is not $n$-decomposable then, by Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"}, $\chi^{\lambda / \mu}(g_{n\alpha}) = 0$ for all partitions $\alpha$ of $m$. Hence, by Proposition [\[prop:omega\]](#prop:omega){reference-type="ref" reference="prop:omega"}(ii), $(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n}\chi^{\lambda/\mu})(g) = 0$. If $\lambda / \mu$ is $n$-decomposable then, using Proposition [\[prop:omega\]](#prop:omega){reference-type="ref" reference="prop:omega"}(i), we may restate Theorem [\[thm:ind\]](#thm:ind){reference-type="ref" reference="thm:ind"} as $$\label{eq:omegares}
\omega(\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^{\lambda / \mu}) = \varepsilon_n(\lambda / \mu)
\mathop{\mathrm{Ind}}^{S_m}_H \bigl(
\chi^{\lambda^{(0)} / \mu^{(0)}} \times \cdots \times 
\chi^{\lambda^{(n-1)}/ \mu^{(n-1)}} \bigr).$$ The result now follows from Proposition [\[prop:omega\]](#prop:omega){reference-type="ref" reference="prop:omega"}(ii). ◻
:::

It is clear from the condition on row numbers in Equation [\[eq:row_numbers\]](#eq:row_numbers){reference-type="eqref" reference="eq:row_numbers"} in Definition [\[def:a\]](#def:a){reference-type="ref" reference="def:a"} that if $\lambda / \mu$ is a skew-partition of $mn$ then there is at most one $m$-border-strip tableau of shape $\lambda / \mu$ and type $(n)$. The following lemma gives a more precise condition. Recall that a skew-partition $\sigma / \tau$ is said to be a *horizontal strip* if the Young diagram of $\sigma / \tau$ has no two boxes in the same column.

::: lemma
[]{#lemma:horiz label="lemma:horiz"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. If $\lambda / \mu$ is $n$-decomposable, and each $\lambda^{(i)} / \mu^{(i)}$ is a horizontal strip, then there is a unique $m$-border-strip tableau of shape $\lambda / \mu$ and type $(n)$; this tableau has sign $\varepsilon_n(\lambda / \mu)$. Otherwise there are no such tableaux.
:::

::: proof
*Proof.* Suppose that $T$ is an $m$-border-strip tableau of type $(n)$ and shape $\lambda / \mu$. Then by Definition [\[def:n_dec\]](#def:n_dec){reference-type="ref" reference="def:n_dec"}, $\lambda / \mu$ is $n$-decomposable. Let $\Gamma(\lambda)$ be an $n$-runner abacus display for $\lambda$ using $tn$ beads for some $t \in \mathbf{N}$. Let $\Gamma(\mu)$ be the abacus display for $\mu$ obtained from $\Gamma(\lambda)$ by an appropriate sequence of $m$ single bead moves, so that in each move a bead is slid upwards into a gap immediately above it. We label the positions on the abacus from top to bottom so that the positions in row $r$ of an abacus display are numbered $(r-1)n, \ldots, rn-1$ (as usual).

Observe that the row number of a border strip of length $n$ in $T$ corresponding to a bead in position $p$ of $\Gamma(\lambda)$ is the number of beads in positions $p+1$, $p+2$, ... of $\Gamma(\lambda)$. Therefore if $p < p'$ and the beads in positions $p$ and $p'$ of $\Gamma(\lambda)$ both correspond to border strips in $T$, then in the sequence of bead moves corresponding to $T$, the bead in position $p'$ is moved upwards before the bead in position $p$.

Let $i \in \{0,\ldots,n-1\}$. Suppose that $\Gamma(\lambda)$ has beads in positions $nq + i$ and $nq' + i$ where $q < q'$, and that $\Gamma(\mu)$ has no beads in positions $n(q+1) + i$, ..., $nq' + i$. The bead in position $nq+i$ of $\Gamma(\lambda)$ prevents the bead initially in position $nq'+i$ from reaching its final position in $\Gamma(\mu)$. Therefore the bead in position $nq+i$ must be moved before the bead in position $nq'+i$ reaches its final position. This contradicts the previous paragraph. Hence there exist $x_j \in \mathbf{N}_0$ and $y_j \in \mathbf{N}_0$ such that the beads on runner $i$ of $\Gamma(\lambda)$ are in positions $\{i + nx_j : 1\le j \le s \}$, the beads on runner $i$ of $\Gamma(\mu)$ are in positions $\{ i + ny_j : 1 \le j \le s \}$ and $$\label{eq:beads}
 y_1 \le x_1 < y_2 \le x_2 < \cdots < y_s \le x_s.$$ It easily follows that $\lambda^{(i)} / \mu^{(i)}$ is a horizontal strip. Then, by Proposition [\[prop:nbij\]](#prop:nbij){reference-type="ref" reference="prop:nbij"}, $\mathrm{sgn}(T) = \varepsilon_n(\lambda / \mu)$.

Conversely, suppose that $\lambda / \mu$ is $n$-decomposable and each $\lambda^{(i)} / \mu^{(i)}$ is a horizontal strip. Then the inequality [\[eq:beads\]](#eq:beads){reference-type="eqref" reference="eq:beads"} on the bead positions in each runner holds. We now describe a sequence of $m$ single upward bead moves that transforms $\Gamma(\lambda)$ into $\Gamma(\mu)$, and thus corresponds to a border-strip tableau $T$ of shape $\lambda / \mu$ and type $(n)^{\star m}$. At each step, locate the bead with maximal position $p$ such that there is no bead in position $p$ of $\Gamma(\mu)$. Slide that bead up into position $p-n$. This is possible by inequality [\[eq:beads\]](#eq:beads){reference-type="eqref" reference="eq:beads"}. The row numbers of the border strips of length $n$ corresponding to this sequence of moves are increasing, so $T$ is a $m$-border-strip tableau of shape $\lambda / \mu$ and type $(n)$. Uniqueness is clear since there is always at most one $m$-border strip tableau of shape $\lambda / \mu$ and type $(n)$. ◻
:::

We can now complete the proof of the base case.

::: proposition
[]{#prop:basecase label="prop:basecase"} Let $m$, $n \in \mathbf{N}$ and let $g\in S_n$ be an $n$-cycle. If $\lambda / \mu$ is a skew-partition of $mn$ then $$(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda / \mu})(g) 
= a_{\lambda / \mu, (n)} .$$
:::

::: proof
*Proof.* If $\lambda / \mu$ is not $n$-decomposable then $a_{\lambda / \mu,(n)} = 0$ by Lemma [\[lemma:horiz\]](#lemma:horiz){reference-type="ref" reference="lemma:horiz"}. Proposition [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"} implies that the result holds in this case.

Now suppose that $\lambda / \mu$ is $n$-decomposable. Let $\ell_i = |\lambda^{(i)} / \mu^{(i)}|$ for each $i \in \{0,\ldots,n-1\}$. By Proposition [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"} and Frobenius reciprocity, we have $$(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda/\mu})(g)=
\varepsilon_n(\lambda/\mu)
\left< \chi^{\lambda^{(0)} / \mu^{(0)}}, 1_{S_{\ell_0}} \right> 
\ldots \left< \chi^{\lambda^{(n-1)} / \mu^{(n-1)}}, 1_{S_{\ell_{n-1}}} \right>.$$

It follows from [@JK Theorem 2.3.13(ii)] that if $\sigma / \tau$ is a skew-partition of $\ell$ then $$\left< \chi^{\sigma / \tau}, 1_{S_\ell} \right> =  \begin{cases}
1 & \text{if $\sigma / \tau$ is a horizontal strip} \\
0 & \text{otherwise}.\end{cases}$$ Therefore $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n}\chi^{\lambda/\mu})(g) = \varepsilon_n(\lambda / \mu)$ if each $\lambda^{(i)} / \mu^{(i)}$ is a horizontal strip, and otherwise $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n}\chi^{\lambda/\mu})(g) = 0$. The proposition now follows from Lemma [\[lemma:horiz\]](#lemma:horiz){reference-type="ref" reference="lemma:horiz"}. ◻
:::

For the inductive step we need the following lemma and proposition. The former is well-known and can be deduced from [@JK 2.3.12]. We write $\mu\subseteq \lambda$ if $\mu$ is a subpartition of $\lambda$ (i.e. the Young diagram of $\mu$ is contained in that of $\lambda$).

::: lemma
[]{#lemma:skewres label="lemma:skewres"} Let $\lambda / \mu$ be a skew-partition of $r$. If $1 \le c < r$ then $$\mathop{\mathrm{Res}}_{S_{c} \times S_{r-c}} \chi^{\lambda / \mu} =
\sum_\tau \chi^{\tau / \mu} \times \chi^{\lambda / \tau}$$ where the sum is over all partitions $\tau$ such that $\mu \subseteq \tau \subseteq \lambda$ and $|\tau / \mu| = c$.
:::

For later use we state and prove the following proposition for a general deflation map.

::: proposition
[]{#prop:defres_decomp label="prop:defres_decomp"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. Let $\vartheta$ be an irreducible character of $S_m$. Let $g\in S_n$. If $g = kh$ where $k \in S_{\ell}$ and $h \in S_{n-\ell}$, then $$(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n} \chi^{\lambda/\mu})(g) = \sum_{\tau} 
(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_\ell} \chi^{\tau / \mu})(k)
(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_{n-\ell}} \chi^{\lambda / \tau})(h)$$ where the sum is over all partitions $\tau$ such that $\mu \subseteq \tau \subseteq \lambda$ and $|\tau / \mu|  = m\ell$.
:::

::: proof
*Proof.* Let $B$ be the base group of the wreath product $S_m \wr S_n \le S_{mn}$. Choose a subgroup $S_{m\ell} \times S_{m(n-\ell)} \le S_{mn}$ containing $B$. If $\psi$ is a character of $S_{m} \wr S_n$ then it is easily checked that $$\mathop{\mathrm{Res}}_{S_\ell \times S_{n-\ell}} (\mathop{\mathrm{Def}}_{S_n}^{\vartheta} 
\psi) = (\mathop{\mathrm{Def}}_{S_\ell}^{\vartheta} \times 
\mathop{\mathrm{Def}}_{S_{n-\ell}}^{\vartheta})   
(\mathop{\mathrm{Res}}^{S_m \wr S_n}_{S_m \wr S_\ell \times S_m \wr S_{n-\ell}} \psi).$$ Hence $$\mathop{\mathrm{Res}}_{S_\ell \times S_{n-\ell}} 
(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_{n}} \chi) = 
(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_\ell} 
\times \mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_{n-\ell}}
)  
(\mathrm{Res}^{S_{mn}}_{S_{m\ell} \times S_{m(n-\ell)}} \chi)$$ for any character $\chi$ of $S_{mn}$. The proposition now follows from the expression for $\mathop{\mathrm{Res}}_{S_{m\ell} \times S_{m(n-\ell)}} \chi^{\lambda / \mu}$ given in Lemma [\[lemma:skewres\]](#lemma:skewres){reference-type="ref" reference="lemma:skewres"}. ◻
:::

We are now ready to prove Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}. Let $m$, $n\in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. Let $\gamma = (\gamma_1,\ldots,
\gamma_d)$ be a composition of $n$. Let $g \in S_n$ have cycle type $\gamma$ and let $h \in S_{n-\gamma_1}$ have cycle type $(\gamma_2,\ldots,\gamma_d)$. Note that, by Lemma [\[lemma:horiz\]](#lemma:horiz){reference-type="ref" reference="lemma:horiz"}, if $\tau / \mu$ is a skew-partition of $m \gamma_1$ then there is at most one $m$-border-strip tableau of shape $\tau / \mu$ and type $(\gamma_1)$. We shall denote this tableau by $T_{\tau / \mu}$ when it exists. By Definition [\[def:a\]](#def:a){reference-type="ref" reference="def:a"}, $a_{\tau / \mu, (\gamma_1)} = \mathrm{sgn}(T_{\tau / \mu})$ (or is zero if no such tableau exists). Therefore Proposition [\[prop:basecase\]](#prop:basecase){reference-type="ref" reference="prop:basecase"} may be restated as $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_{\gamma_1}} \chi^{\tau/\mu})(k)=
\mathrm{sgn}(T_{\tau / \mu})$, where $k \in S_{\gamma_1}$ is a $\gamma_1$-cycle and $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_{\gamma_1}} \chi^{\tau/\mu})(k)=0$ if no tableau $T_{\tau / \mu}$ exists. It therefore follows from Proposition [\[prop:defres_decomp\]](#prop:defres_decomp){reference-type="ref" reference="prop:defres_decomp"} that $$\label{eq:defres_decomp_sgn}
 (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda / \mu})(g) = \sum_\tau \mathrm{sgn}(T_{\tau/ \mu}) 
 (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_{n-\gamma_1}} \chi^{\lambda / \tau})(h)$$ where the sum is over all partitions $\tau$ such that $\mu \subseteq \tau \subseteq \lambda$, $|\tau / \mu| = m\gamma_1$ and there is an $m$-border-strip tableau of shape $\tau / \mu$. By induction on the number of parts of $\gamma$ we have $$(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda / \mu})(g) = \sum_\tau \mathrm{sgn}(T_{\tau/ \mu}) 
 a_{\lambda / \tau, (\gamma_2,\ldots,\gamma_d)}$$ with the same conditions on the sum. It is clear that if $T$ is an $m$-border-strip tableau of shape $\lambda / \mu$ and type $\gamma$ then the border strips in $T$ corresponding to the $m$ parts of length $\gamma_1$ in $\gamma^{\star m}$ form an $m$-border-strip tableau of shape $\tau / \mu$ for some $\tau$. Therefore the right-hand side of the previous equation is $a_{\lambda / \mu, \gamma}$. This completes the proof of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}.
