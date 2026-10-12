---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.972
---
[]{#sec:intro label="sec:intro"}

Tableaux combinatorics is a pivotal theme in the representation theory of the symmetric groups. Fundamental results in this area include the Murnaghan--Nakayama rule for the values taken by irreducible characters of symmetric groups and the Littlewood--Richardson rule (as well as its special case, Young's rule), which determines the restrictions of irreducible characters to Young subgroups of symmetric groups.

The two main results of this paper are Theorems [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"}, which give a combinatorial description of the restrictions of characters of symmetric groups to their maximal imprimitive subgroups. Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} is a simultaneous generalization of the Murnaghan--Nakayama rule and Young's rule. Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"} gives a further generalization, in which Young's rule is replaced by a family of special cases of the Littlewood--Richardson rule.

As a corollary of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}, we obtain in Proposition [\[prop:Foulkes\]](#prop:Foulkes){reference-type="ref" reference="prop:Foulkes"} a new recursive formula for the character multiplicities that are the subject of Foulkes' Conjecture, a long-standing problem which spans representation theory, invariant theory and algebraic combinatorics. We use this formula to verify Foulkes' Conjecture in some new cases, extending the results in [@MN]. Figures [\[fig:FoulkesGraph\]](#fig:FoulkesGraph){reference-type="ref" reference="fig:FoulkesGraph"} and [\[fig:FoulkesGraphsComp\]](#fig:FoulkesGraphsComp){reference-type="ref" reference="fig:FoulkesGraphsComp"} in §5 show some of the data computed using this formula.

## Character deflations

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

## Some special cases

It is clear than if $m=1$ then $\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi=
\chi$ for any character $\chi$ of $S_n$, and so the special case $m=1$ of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} asserts that $\chi^{\lambda / \mu} (g) = a_{\lambda/ \mu , \gamma}$ for any skew-partition $\lambda / \mu$ of $n$ and any element $g \in S_n$ of cycle type $\gamma$. Equivalently, $$\chi^{\lambda / \mu} (g) = \sum_{T} \mathrm{sgn}(T)$$ where the sum is over all border-strip tableaux of shape $\lambda / \mu$ and type $\gamma$. This is the Murnaghan--Nakayama rule, as stated in [@StanleyII Equation (7.75)]. It should be noted that we require the Murnaghan--Nakayama rule in §[\[subsec:omega_proof\]](#subsec:omega_proof){reference-type="ref" reference="subsec:omega_proof"} below, and so our work does not provide a new proof of this result. In practice the Murnaghan--Nakayama rule is most frequently used as a recursive formula for the values of characters or skew characters. Equation [\[eq:defres_decomp_sgn\]](#eq:defres_decomp_sgn){reference-type="eqref" reference="eq:defres_decomp_sgn"} at the end of §[\[sec:proof\]](#sec:proof){reference-type="ref" reference="sec:proof"} formulates Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} in this way.

As Stanley observes in [@StanleyII page 348], it is far from obvious that the character values given by the Murnaghan--Nakayama rule applied to a skew-partition $\lambda / \mu$ and a composition $\gamma$ are independent of the order of the parts of $\gamma$. This remark applies even more strongly to Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}. For example, the reader may check that if $\lambda / \mu = (6,5,3,2) / (3,1)$, as in Example [\[example:border_strip\]](#example:border_strip){reference-type="ref" reference="example:border_strip"}, and $\gamma' = (2,1,3)$, then there is a unique $2$-border-strip tableau of shape $(6,5,3,2) / (3,1)$ and type $\gamma'$. Thus $a_{\lambda/\mu,\gamma'} = 1$, but the sums defining $a_{\lambda/ \mu,\gamma}$ and $a_{\lambda / \mu, \gamma'}$ are different.

Another special case of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} worth noting occurs when $g$ is the identity element of $S_n$. If $\xi$ is an irreducible character of $S_m \wr S_n$ then either the base group $B = S_m \times \cdots \times S_m$ is contained in the kernel of $\xi$ and $\left<\mathop{\mathrm{Res}}_B \xi, 1_B\right>
= \xi(1)$, or $\left<\mathop{\mathrm{Res}}_B \xi, 1_B\right> = 0$. Hence, by linearity, we have $$\label{eq:deflation_special} 
(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi)(1) = \left<\mathop{\mathrm{Res}}_B \chi ,1_B\right>$$ for any character $\chi$ of $S_{mn}$. It now follows from Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and Frobenius reciprocity that $$a_{\lambda / \mu, (1^n)} =
\left< \chi^{\lambda / \mu},
 \mathop{\mathrm{Ind}}_{S_m \times \cdots \times S_m}^{S_{mn}}
1_{S_m} \times \cdots \times 1_{S_m} \right>$$ for any skew-partition $\lambda / \mu$ of $mn$. It is clear from Definition [\[def:a\]](#def:a){reference-type="ref" reference="def:a"} that $a_{\lambda / \mu, (1^n)}$ is the number of semi-standard tableaux of shape $\lambda / \mu$ and type $(m^n)$. Therefore, by setting $\mu = \varnothing$ in the previous equation, we obtain a special case of Young's rule (see [@JK 2.8.5] or [@StanleyII Proposition 7.18.7]).

## Outline of the paper

The remainder of the paper proceeds as follows. Throughout, we shall adopt the convention that if $\alpha$ is a partition of $r \in \mathbf{N}$, then $g_\alpha \in S_r$ is an element of cycle type $\alpha$, and $z_\alpha$ is the size of the centralizer of $g_\alpha$ in $S_r$. (The choice of $g_\alpha$ within the conjugacy class is irrelevant.) If $\alpha = (\alpha_1,\ldots,\alpha_k)$, we write $n\alpha = (n\alpha_1,\ldots,n\alpha_k)$.

In §[\[sec:averaging\]](#sec:averaging){reference-type="ref" reference="sec:averaging"} we prove Proposition [\[prop:deflation\]](#prop:deflation){reference-type="ref" reference="prop:deflation"}, which implies that if $\chi$ is a character of $S_{mn}$ and $g\in S_n$, then $(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi)(g)$ is the average value of $\chi$ on the coset of the base group $S_m \times \cdots \times S_m$ in $S_m \wr S_n$ corresponding to $g$. Equation [\[eq:deflation_special\]](#eq:deflation_special){reference-type="eqref" reference="eq:deflation_special"} above is a special case of this result. In the case when $g \in S_n$ is an $n$-cycle, we obtain Proposition [\[prop:omega\]](#prop:omega){reference-type="ref" reference="prop:omega"}(ii), which implies that if $\lambda / \mu$ is a skew-partition of $mn$, then $$\label{eq:cycle_deflation}
 \mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\lambda / \mu}(g) = 
\sum_{\alpha}\frac{\chi^{\lambda / \mu}(g_{n\alpha})}{z_\alpha}$$ where the sum is over all partitions $\alpha$ of $m$, and $n\alpha$ denotes the partition obtained from $\alpha$ by multiplying each of its parts by $n$.

In §[\[sec:skew\]](#sec:skew){reference-type="ref" reference="sec:skew"} we state a theorem of Farahat (see [@Farahat1954 Section 4]), which gives a formula for the character values $\chi^{\lambda/\mu}(g_{n\alpha})$ appearing on the right-hand side of [\[eq:cycle_deflation\]](#eq:cycle_deflation){reference-type="eqref" reference="eq:cycle_deflation"}. We then give a character-theoretic proof of this theorem.

In §[\[sec:proof\]](#sec:proof){reference-type="ref" reference="sec:proof"} we combine the results of §3 and §4 to show that Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} holds when $g \in S_n$ is an $n$-cycle (Proposition [\[prop:basecase\]](#prop:basecase){reference-type="ref" reference="prop:basecase"}) and then to deduce it in general.

In §[\[sec:Foulkes\]](#sec:Foulkes){reference-type="ref" reference="sec:Foulkes"} we apply our results on deflations to Foulkes' Conjecture on permutation characters the symmetric group. In particular, we prove a new recursive formula for the character multiplicities that appear in this conjecture. Using this formula we check Foulkes' Conjecture in some new cases, extending the results in [@MN].

In §[\[sec:gendef\]](#sec:gendef){reference-type="ref" reference="sec:gendef"}, we consider the more general deflation maps $\mathop{\mathrm{Def}}^\vartheta_{S_n}$. When $\vartheta=\chi^{(a,1^b)}$ is labelled by a hook partition, Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"} gives a combinatorial description of the value of $\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_n} \chi^{\lambda/ \mu}$ on an $n$-cycle. This result generalizes the case $\gamma=(n)$ of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and may be viewed as a simultaneous generalization of the Murnaghan--Nakayama rule and a special case of the Littlewood--Richardson rule. We also give an illustrative example showing how our methods can be used to compute values of deflated characters in the non-hook case.

Finally, in §[\[sec:concl\]](#sec:concl){reference-type="ref" reference="sec:concl"}, we discuss the aforementioned connections between Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and results in [@DLT; @Macdonald1995] stated in terms of symmetric functions.
