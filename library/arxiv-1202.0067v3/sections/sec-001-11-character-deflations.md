---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-001-11-character-deflations
section_title: "Character deflations"
section_number: 1.1
pages: 2-5
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.949
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
We now introduce the ideas needed to state Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}. By a construction originally due to Frobenius, the irreducible characters of the symmetric group $S_r$ are canonically labelled by the partitions of $r$. As is usual, we write $\chi^\lambda$ for the irreducible character labelled by the partition $\lambda$, and $\chi^{\lambda / \mu}$ for the character labelled by the skew-partition $\lambda / \mu$. We refer the reader to [@JK Chapter 2] or [@StanleyII §7.18] for a construction of these characters and to [@StanleyII page 309] for background on skew-partitions.

For each $r \in \mathbf{N}$, it is well known (see, for example, [@DixonMortimer Exercise 5.2.8]) that the maximal imprimitive subgroups of $S_r$ are precisely the imprimitive wreath products $S_m \wr S_n \le S_{r}$ for $m$, $n \in \mathbf{N}$ such that $mn = r$. Let $\vartheta$ be a character of $S_m$, and let $V$ be a representation of $S_m$ affording $\vartheta$. Then $V^{\otimes n}$ is a representation of the base group $S_m\times \cdots \times S_m$. The complement $S_n$ of this base group acts on $V^{\otimes n}$ by permuting the factors: $$g(v_1\otimes \cdots \otimes v_n) = v_{g^{-1} (1)} \otimes \cdots \otimes v_{g^{-1} (n)}$$ for $g \in S_n$ and $v_1, \ldots, v_n \in V$. These two actions combine to give a representation of $S_m\wr S_n$ on $V^{\otimes n}$ (see [@JK 4.3.6]). We shall denote by $\widetilde{\vartheta^{\times n}}$ the character of $S_m\wr S_n$ afforded by this representation. We also need the characters of $S_m \wr S_n$ whose kernel contains $S_m \times \cdots \times S_m$. These characters are precisely the inflations of the characters of $S_n$ to $S_m \wr S_n$ along the canonical surjection $S_m \wr S_n \twoheadrightarrow S_n$. If $\nu$ is a partition of $n$, we denote by $\mathop{\mathrm{Inf}}_{S_n}^{S_m \wr S_n} \!\chi^\nu$ the irreducible character of $S_m \wr S_n$ constructed in this way. It is easily seen that the characters $\widetilde{\vartheta^{\times n}} \mathop{\mathrm{Inf}}_{S_n}^{S_m \wr S_n}\!\chi^\nu$ obtained by multiplying characters of these two types are irreducible. (By [@JK Theorem 4.3.33], any irreducible character of $S_m \wr S_n$ is induced from a suitable product of characters of this form.)

Given a finite group $G$, we let $\mathcal{C}(G)$ denote the abelian group of virtual characters of $G$.

::: definition
[]{#def:def label="def:def"} Let $m$, $n \in \mathbf{N}$ and let $\vartheta$ be an irreducible character of $S_m$. Let $\xi$ be an irreducible character of $S_m \wr S_n$. We define $$\mathop{\mathrm{Def}}^\vartheta_{S_n} \xi = \begin{cases}
\chi^\nu & \text{if $\xi = \widetilde{\vartheta^{\times n}} \mathop{\mathrm{Inf}}_{S_n}^{S_m
\wr S_n}\!\chi^\nu$
where $\nu$ is a partition of $n$} \\
0 & \text{otherwise}. \end{cases}$$ Let $\mathop{\mathrm{Def}}_{S_n}^\vartheta: \mathcal{C}(S_m \wr S_n) \rightarrow \mathcal{C}(S_n)$ be the group homomorphism defined by linear extension of this definition. Given $\psi \in \mathcal{C}(S_m \wr S_n)$, we say that $\mathop{\mathrm{Def}}_{S_n}^\vartheta\psi$ is the *deflation of $\psi$ with respect to $\vartheta$*. Let $\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n}^\vartheta: \mathcal{C}(S_{mn}) \rightarrow
\mathcal{C}(S_n)$ be the group homomorphism defined by $$\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n} \chi = \mathop{\mathrm{Def}}^\vartheta_{S_n} 
\mathop{\mathrm{Res}}^{S_{mn}}_{S_m \wr S_n} \chi$$ for $\chi \in \mathcal{C}(S_{mn})$.
:::

In the case when $\vartheta$ is the trivial character of $S_m$, we shall omit $\vartheta$ and simply write $\mathop{\mathrm{Def}}_{S_n}$ and $\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n}$. If $V$ is a complex representation of $S_m \wr S_n$ with character $\chi$, then $\mathop{\mathrm{Def}}_{S_n}\chi$ is the character of the maximal subrepresentation of $V$ on which the base group $S_m \times \cdots \times S_m$ acts trivially.

Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} gives a combinatorial rule for the values of $\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda / \mu}$ where $\lambda / \mu$ is a skew-partition of $mn$. In order to state this rule, we review and extend the definition of a border-strip tableaux (see [@StanleyII §7.17]).

Recall that a skew-partition $\sigma / \tau$ is said to be a *border strip* (or rim hook) if the Young diagram of $\sigma / \tau$ is connected and contains no $2 \times 2$ square. The $\emph{length}$ of the border strip $\sigma / \tau$ is $|\sigma / \tau|$ and its *height* is defined to be one less than its number of non-empty rows. If $\lambda / \mu$ is a skew-partition, then we define a *border-strip tableau* of shape $\lambda / \mu$ to be an assignment of the elements of a set $J \subseteq \mathbf{N}$ to the boxes of the Young diagram of $\lambda / \mu$ so that the rows and columns are non-decreasing, and for each $j \in J$, the boxes labelled $j$ form a border strip; if $J = \{1,\ldots,k\}$, and for each $j \in J$ the border strip formed by the boxes labelled $j$ has length $\alpha_j$, then we say that the tableau has *type* $(\alpha_1,\ldots,\alpha_k)$. We need the following three further definitions, which are illustrated in Figure [1](#fig:border_strip){reference-type="ref" reference="fig:border_strip"} and Example [\[example:border_strip\]](#example:border_strip){reference-type="ref" reference="example:border_strip"} below.

::: definition
[]{#def:sgn label="def:sgn"} Let $T$ be a border-strip tableau. The *sign* of $T$ is defined by $\mathrm{sgn}(T) = (-1)^h$, where $h$ is the sum of the heights of the border strips forming $T$.
:::

<figure id="fig:border_strip">
<p><span class="math display">$$\young(::112444,::122,:11,:1,:3,33)$$</span></p>
<figcaption>A border-strip tableau of shape <span class="math inline">(8,5,3,2,2,2)/(2,2,1,1,1)</span> and type <span class="math inline">(6,3,3,3)</span>. The heights of the border strips labelled <span class="math inline">1, 2, 3, 4</span> are <span class="math inline">3, 1, 1, 0</span> respectively, and the sign of this border-strip tableau is thus <span class="math inline"> − 1</span>. </figcaption>
</figure>

::: definition
[]{#def:row_number label="def:row_number"} Let $\lambda / \tau$ be a border strip in a partition $\lambda$. If the lowest-numbered row of $\lambda$ met by $\lambda / \tau$ is row $k$ then we define the *row number* of $\lambda / \tau$ to be $k$, and write $N(\lambda/ \tau) = k$.
:::

Note that if $T$ is a border-strip tableau of shape $\lambda / \mu$ and type $(\alpha_1, \ldots, \alpha_k)$ then there are partitions $$\mu = 
\lambda^0 \subset \lambda^1 \subset \cdots \subset \lambda^{k-1}
\subset \lambda^{k} = \lambda$$ such that for each $j \in \{1,\ldots,k\}$, the border strip in $T$ labelled $j$ is $\lambda^j /\lambda^{j-1}$.

::: definition
[]{#def:a label="def:a"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. Given a composition $\gamma = (\gamma_1, \ldots, \gamma_d)$ of $n$, let $\gamma^{\star m} = (\gamma_1, \ldots, \gamma_1,
\ldots, \gamma_d, \ldots, \gamma_d)$ denote the composition of $mn$ obtained from $\gamma$ by repeating each part $m$ times. An *$m$-border-strip tableau* of *shape $\lambda / \mu$* and *type $\gamma$* is a border-strip tableau of shape $\lambda / \mu$ and type $\gamma^{\star m}$ such that for each $j \in \{1,2,\ldots,d\}$, the row numbers of the border strips $$\lambda^{(j-1)m+1} / \lambda^{(j-1)m},  
\ldots ,
\lambda^{jm} / \lambda^{jm-1}$$

corresponding to the $m$ parts in $\gamma^{\star m}$ of length $\gamma_j$ satisfy $$\label{eq:row_numbers} 
N(\lambda^{(j-1)m+1} / \lambda^{jm}) 
\ge \cdots \ge N(\lambda^{jm} / \lambda^{jm-1}).$$ Let $$a_{\lambda/ \mu, \gamma} = \sum_{T} \mathrm{sgn}(T)$$ where the sum is over all $m$-border-strip tableaux $T$ of shape $\lambda / \mu$ and type $\gamma$.
:::

::: theorem
[]{#thm:cd label="thm:cd"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. If $\gamma$ is a composition of $n$ and $g \in S_n$ has cycle type $\gamma$ then $$(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda / \mu})(g) = a_{\lambda/\mu,\gamma}.$$
:::

::: example
[]{#example:border_strip label="example:border_strip"} Let $\lambda = (6,5,3,2)$ and let $\mu = (3,1)$. The three different $2$-border-strip tableaux of shape $\lambda / \mu$ and type $\gamma = (1,2,3)$ are shown below. $$\rule[-27pt]{0pt}{29pt}\young(:::266,:1556,345,34) 
\qquad
\young(:::466,:1246,355,35) 
\qquad
\young(:::266,:1446,355,35)$$ As required by Definition [\[def:a\]](#def:a){reference-type="ref" reference="def:a"}, for each $j \in \{1,2,3\}$, the row number of the border strip labelled $2j-1$ in each tableau is at least the row number of the border strip labelled $2j$. Thus the first border strip corresponding to each part of $\gamma$ is added no higher up in each partition diagram than the second. The sums of the heights of the border strips forming these tableaux are $4$, $4$ and $3$ and so their signs are $+1$, $+1$ and $-1$, respectively. By Definition [\[def:a\]](#def:a){reference-type="ref" reference="def:a"} we have $a_{\lambda / \mu,\gamma} = 1$. Hence Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} implies that $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_6}\chi^{(6,5,3,2) / (3,1)}) (g) = 1$ if $g \in S_6$ has cycle type $(1,2,3)$.
:::

Deflation is closely related to plethysm of Schur functions (see [@Macdonald1995 §I.8]). In fact, using the standard correspondence between characters of symmetric groups and symmetric functions, one can show that the special case $\gamma=(n)$ of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} is equivalent to a result proved in [@DLT Section 9]. Also, in the special case $\mu=\varnothing$, the combinatorial description of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} can be shown (using our Lemma [\[lemma:horiz\]](#lemma:horiz){reference-type="ref" reference="lemma:horiz"} below) to be equivalent to the one given for plethysm by Macdonald [@Macdonald1995 §I.8, Example 8]. These connections are discussed in more detail in §[\[sec:concl\]](#sec:concl){reference-type="ref" reference="sec:concl"}.

We prove Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} in §§[\[sec:averaging\]](#sec:averaging){reference-type="ref" reference="sec:averaging"}--[\[sec:proof\]](#sec:proof){reference-type="ref" reference="sec:proof"}. The only prerequisites, apart from some basic character theory, are the Murnaghan--Nakayama rule and the combinatorics of the abacus. In addition to being self-contained, our proof is highly combinatorial in the sense that the key steps, given in §3, can all be stated in terms of explicit bijections between certain classes of tableaux.
