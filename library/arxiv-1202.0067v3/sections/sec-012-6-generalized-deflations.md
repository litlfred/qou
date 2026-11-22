---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-012-6-generalized-deflations
section_title: "Generalized deflations"
section_number: 6
pages: 22-30
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.953
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
[]{#sec:gendef label="sec:gendef"}

In this section we discuss deflation with respect to an arbitrary irreducible character $\vartheta$ of $S_m$. In the case where $\vartheta$ is labelled by a hook partition, $\vartheta=\chi^{(a,1^b)}$ where $a+b=m$, we give a combinatorial description, generalizing Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}. We also prove some other general results, and show how these, together with the results of §[\[sec:proof\]](#sec:proof){reference-type="ref" reference="sec:proof"}, may be used to calculate the values of an irreducible character of $S_{mn}$ deflated with respect to an arbitrary character of $S_m$.

Firstly we deduce from Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} an analogous result for deflations with respect to the sign character. As is usual, if $\lambda$ is a partition then we denote by $\lambda'$ the conjugate partition to $\lambda$.

::: proposition
[]{#prop:sgn label="prop:sgn"} Let $m$, $n \in \mathbf{N}$ and let $\lambda / \mu$ be a skew-partition of $mn$. If $\gamma$ is a composition of $n$ and $g \in S_n$ has cycle type $\gamma$ then $$(\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n}^{\mathrm{sgn}_{S_m}})(g) = 
\begin{cases} a_{\lambda' / \mu', \gamma} & \text{if $m$ is even} \\
\mathrm{sgn}_{S_n}(g) \, a_{\lambda' / \mu', \gamma} & \text{if $m$ is odd}. 
\end{cases}$$
:::

::: proof
*Proof.* It is easily seen that $$\mathop{\mathrm{Res}}_{S_m \wr S_n} \mathrm{sgn}_{S_{mn}} = \begin{cases}
\widetilde{\mathrm{sgn}_{S_m}^{\times n}} & \text{if $m$ is even} \\[6pt]
\widetilde{\mathrm{sgn}_{S_m}^{\times n}}\, \mathrm{sgn}_{S_n} & \text{if $m$ is odd.}
\end{cases}$$ Hence if $\chi$ is any character of $S_{mn}$ then $$\mathop{\mathrm{Def\hskip-0.3pt res}}^{\mathrm{sgn}_{S_m}}_{S_n} \chi = \eta \mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} (\chi\, \mathrm{sgn}_{S_{mn}})$$ where $\eta = 1_{S_n}$ if $m$ is even and $\eta = \mathrm{sgn}_{S_n}$ if $m$ is odd. It follows from Theorems 7.15.6 and 7.17.5 of [@StanleyII] that if $\lambda / \mu$ is a skew-partition of $mn$ then $\chi^{\lambda / \mu}\, \mathrm{sgn}_{S_{mn}} = \chi^{\lambda' / \mu'}$. Therefore, by Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"}, we have $$\mathop{\mathrm{Def\hskip-0.3pt res}}^{\mathrm{sgn}_{S_m}}_{S_n}(\chi^{\lambda'/\mu'}) = 
\eta(g) a_{\lambda' / \mu',\gamma},$$ as required. ◻
:::

It would also have been possible to prove Proposition [\[prop:sgn\]](#prop:sgn){reference-type="ref" reference="prop:sgn"} directly from Proposition [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"}, by reasoning along the same lines as the proof of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} in §5.

We now turn our attention to the case where $\vartheta=\chi^{(a,1^b)}$ for a hook partition $(a,1^b)$. For convenience, we use the language of skew shapes (see, for example, [@Zelevinsky1981]). A *skew shape* is a finite subset $\kappa$ of $\mathbb{N}\times\mathbb{N}$ that is convex with respect to the partial order $\le_p$ defined by $(i,j) \le_p (i',j')$ if and only if $i\le i'$ and $j\le j'$. We identify the skew-partition $\lambda / \mu$ in which $\lambda$ has $t$ parts with the skew shape $\{ (i,j) : 1 \le j \le t, \mu_i+1 \le j \le \lambda_i\}$. We define $\chi^\kappa = \chi^{\lambda / \mu}$ and $\varepsilon_n(\kappa) = \varepsilon_n(\lambda / \mu)$.

Suppose $\kappa$ is a skew shape. Then we define the *initial box* of $\kappa$ to be $(i_\kappa, j_\kappa)$ where $(i_\kappa, j_\kappa) \in \kappa$ and, for any $i \le i_\kappa$ and $j \ge j_\kappa$, if $(i,j) \in \kappa$ then $i = i_\kappa$ and $j = j_\kappa$. Similarly, we define the *terminal box* of $\kappa$ to be $(k_\kappa, \ell_\kappa)$ where $(k_\kappa, \ell_\kappa) \in \kappa$ and, for any $k \ge k_\kappa$ and $\ell \le \ell_\kappa$, if $(k,\ell) \in \kappa$ then $k = k_\kappa$ and $\ell = \ell_\kappa$. The initial and terminal boxes exist due to the convexity of $\kappa$. For all $(i,j) \in \kappa$, $i_\kappa \le i \le k_\kappa$ and $\ell_\kappa \le j \le j_\kappa$.

We use the term *border strip* in this context to mean a connected skew shape which contains no $2 \times 2$ square. We say that $D$ is a *border-strip $n$-diagram* if $D$ is a finite set of disjoint border strips, each of length $n$, such that $\bigcup D$ is a skew shape. We say that $D$ is a *horizontal border-strip $n$-diagram* if whenever $(i_\rho,j_\rho)$ is the initial box of some border strip $\rho \in D$, we have $(i,j_\rho) \notin \bigcup D$ for all $i<i_\rho$. Similarly, $D$ is a *vertical border-strip $n$-diagram* if whenever $(k_\rho,\ell_\rho)$ is the terminal box of some border strip $\rho \in D$, we have $(k_\rho, \ell) \notin \bigcup D$ for all $\ell<\ell_\rho$.

We define a relation $\mathcal{R}$ on the set of border strips of length $n$ by $(\rho_1, \rho_2) \in \mathcal{R}$ if $\rho_1$ and $\rho_2$ are disjoint border strips of length $n$ and there exist $z \in \rho_1$ and $w \in \rho_2$ such that $z<_p w$. Observe that when $n\ge 3$ the relation $\mathcal{R}$ is not transitive. We can now state the following combinatorial definition, which is illustrated in Figure [1](#fig:skewDiag){reference-type="ref" reference="fig:skewDiag"} overleaf.

::: definition
[]{#def:hook-like label="def:hook-like"} Let $\kappa$ be a skew shape of size $mn$, $a,b$ be positive integers such that $a+b=m$, and $D$ and $E$ be two border-strip $n$-diagrams such that $\kappa=\bigcup (D\cup E)$. We say that $(D,E)$ is an *$(a,1^b)$-like border-strip $n$-diagram of shape $\kappa$* if the following conditions are satisfied:

1.  $|D| = a$ and $|E| = b+1$;

2.  $D\cap E = \{ \sigma \}$ where $\sigma$ is border strip of length $n$ which contains the initial box of $\kappa$;

3.  $D$ is a horizontal border-strip $n$-diagram, and $E$ is a vertical border-strip $n$-diagram;

4.  there do not exist $\rho_D\in D$ and $\rho_E \in E$ such that $(\rho_E, \rho_D) \in \mathcal{R}$.

We denote the set of $(a,1^b)$-like border-strip $n$-diagrams of shape $\kappa$ by $\mathcal{B}_{a,b}^\kappa$.
:::

![A $(4,1^4)$-like border-strip $3$-diagram of shape $(9,8,7,7,6,2,1) /     
(5,5,3,3)$. Ribbons in the horizontal border-strip $3$-diagram are shown in light grey and white, with their initial boxes labelled $I$; ribbons in the vertical border-strip $3$-diagram are shown in light grey and dark grey with their terminal boxes labelled $T$.](SkewDiagram.pdf){#fig:skewDiag}

We note that, by a simple counting argument, whenever $(D,E)\in \mathcal{B}_{a,b}^{\kappa}$, the elements of $D$ are pairwise disjoint, as well as those of $E$, and we have $(\bigcup D) \cap (\bigcup E) = \sigma$. Definition [\[def:hook-like\]](#def:hook-like){reference-type="ref" reference="def:hook-like"} is inspired by the Littlewood--Richardson Rule (see [@JK 2.8.13] or [@StanleyII A1.3.3]) in the case of a hook partition $(a,1^b)$. In this case the rule states that the multiplicity of $\chi^{(a,1^b)}$ in $\chi^\kappa$ is the number of ways to represent $\kappa$ as a union of two skew shapes $\alpha$ and $\beta$ satisfying the following:

\(1\) the size of $\alpha$ is $a$ and the size of $\beta$ is $b+1$; (2) $\alpha\cap \beta= \{ x \}$ where $x$ is the initial box of $\kappa$; (3) $\alpha$ is a horizontal strip and $\beta$ is a vertical strip; (4) there do not exist $y\in \alpha$ and $z\in \beta$ such that $z<_{p} y$. Thus $$(\mathop{\mathrm{Def}}_{S_1}^{\chi^{(a,1^b)}}\!\chi^\kappa)(1_{S_1}) = | \mathcal{B}^\kappa_{a,b}|.$$ This is the case $n=1$ of the following theorem.

::: theorem
[]{#thm:hookdefl label="thm:hookdefl"} Let $\kappa$ be a skew shape of size $mn$. Let $a,b$ be positive integers such that $a+b=m$. Let $g\in S_n$ be an $n$-cycle. Then $$(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{(a,1^b)}}_{S_n} \!\chi^{\kappa})(g) = \varepsilon_n(\kappa) |\mathcal{B}_{a,b}^\kappa|.$$
:::

We observe that an $(m)$-like border-strip $n$-diagram of shape $\kappa$ may be viewed as an $m$-border-strip tableau of shape $\kappa$ and type $(n)$ by labelling the border strips in the unique way so that the condition on row numbers in Definition [\[def:a\]](#def:a){reference-type="ref" reference="def:a"} holds. Thus Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"} is a generalization of Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} in the case of an $n$-cycle.

::: example
[]{#example:hook label="example:hook"} We compute $(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{(3,1)}}_{S_3} \chi^{(4,4,4)})(g)$ where $g$ is a 3-cycle. There are two $(3,1)$-like border-strip $3$-diagrams of shape $(4,4,4,4)$, namely $( \{\rho_1, \rho_2, \rho_3\}, \{\rho_3, \rho_4\})$ and $( \{\rho_5, \rho_6, \rho_7\}, \{\rho_7, \rho_8\})$, where $\rho_i$ denotes the border strip consisting of those boxes labelled by $i$ in the tableaux below. $$\young(1223,1233,1444)\ ,  \quad \young(5677,5678,5688)\ .$$ Since $\varepsilon_3(4,4,4)=1$, Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"} implies that $(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{(3,1)}}_{S_3} \chi^{(4,4,4)})(g)=2$.
:::

The proof of Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"} requires the following definition, in which we assume that $a+b=m$.

::: definition
[]{#def:D_a,b label="def:D_a,b"} Let $\kappa$ be a skew shape of size $mn$. Define $\mathcal{D}^\kappa_{a,b}$ to be the set of pairs $(D,E)$ where $D$ and $E$ are border-strip $n$-diagrams such that $\kappa=\bigcup (D\cup E)$ and the following conditions are satisfied:

1.  $|D| = a$ and $|E| = b$;

2.  $D$ is a horizontal border-strip $n$-diagram, and $E$ is a vertical border-strip $n$-diagram;

3.  there do not exist $\rho_D\in D$ and $\rho_E \in E$ such that $(\rho_E, \rho_D) \in \mathcal{R}$.
:::

Note that since $|\kappa| = mn$, the border-strips in $D$ and $E$ are necessarily disjoint. We need the following two lemmas on $\mathcal{D}^\kappa_{a,b}$; their proofs are given after the proof of Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"}.

::: lemma
[]{#lemma:D_a,b label="lemma:D_a,b"} Let $\kappa$ be a skew shape of size $mn$, and let $a,b$ be positive integers such that $a+b=m$. Then $$\langle\omega(\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^\kappa), \ \mathop{\mathrm{Ind}}_{S_a \times S_b}^{S_m} (\chi^{(a)} \times \chi^{(1^b)}) \rangle= \varepsilon_n(\kappa) | \mathcal{D}^\kappa_{a,b}|,$$
:::

::: lemma
[]{#lemma:DandB label="lemma:DandB"} Let $\kappa$ be a skew shape of size $mn$. Let $0\le a <m$ and $b=m-a$. Then $$|\mathcal{D}^{\kappa}_{a,b}| = |\mathcal{B}^{\kappa}_{a,b}| + |\mathcal{B}^{\kappa}_{a+1,b-1}|.$$
:::

::: proof
*Proof of Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"}.* The proof is by induction on $b$. Recall that $g$ denotes an $n$-cycle. In the case $b=0$ we have $$(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{(m)}}_{S_n} \chi^{\kappa})(g)= a_{\kappa, (n)}= \varepsilon_n(\kappa) | \mathcal{D}^\kappa_{m,0}|=\varepsilon_n(\kappa) | \mathcal{B}^\kappa_{m,0}|,$$ where the first equality follows from Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and the second by Lemma [\[lemma:horiz\]](#lemma:horiz){reference-type="ref" reference="lemma:horiz"}.

For $b>0$, we combine Proposition [\[prop:omega\]](#prop:omega){reference-type="ref" reference="prop:omega"} with Lemmas [\[lemma:D_a,b\]](#lemma:D_a,b){reference-type="ref" reference="lemma:D_a,b"} and [\[lemma:DandB\]](#lemma:DandB){reference-type="ref" reference="lemma:DandB"}, Young's Rule and the inductive hypothesis to get $$\begin{aligned}
(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{(a ,1^{b})}}_{S_n} \chi^{\kappa}) (g) &=
 \langle\omega (\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^{\kappa}), \chi^{(a,1^b)} \rangle\\
 & =    \langle\omega (\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^{\kappa}), \mathop{\mathrm{Ind}}_{S_a \times S_b}^{S_m} (\chi^{(a)} \times \chi^{(1^b)}) - \chi^{(a+1,1^{b-1})} \rangle\\
& =  \varepsilon_n(\kappa) |\mathcal{D}^\kappa_{a,b}|- (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\chi^{(a+1 ,1^{b-1})}}_{S_n} \chi^{\vartheta}) (g)\\
& =  \varepsilon_n(\kappa) |\mathcal{D}^\kappa_{a,b}| -  \varepsilon_{n} (\kappa) |\mathcal{B}^{\kappa}_{a+1,b-1}|\\
 & =   \varepsilon_{n} (\kappa) |\mathcal{B}^{\kappa}_{a ,b}|.
\end{aligned}$$ as required. ◻
:::

It remains to demonstrate the truth of the two lemmas.

::: proof
*Proof of Lemma [\[lemma:D_a,b\]](#lemma:D_a,b){reference-type="ref" reference="lemma:D_a,b"}.* Let $g$ denote an $n$-cycle. In the case $b=0$, $$\langle\omega(\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^\kappa), \ \chi^{(m)} \rangle= (\mathop{\mathrm{Def\hskip-0.3pt res}}_{S_n} \chi^{\kappa}) (g)=a_{\kappa, (n)}=\varepsilon_n(\kappa)|\mathcal{D}^{\kappa}_{m ,0}|$$ by Proposition [\[prop:omega\]](#prop:omega){reference-type="ref" reference="prop:omega"}, Theorem [\[thm:cd\]](#thm:cd){reference-type="ref" reference="thm:cd"} and Lemma [\[lemma:horiz\]](#lemma:horiz){reference-type="ref" reference="lemma:horiz"}. Similarly, the case $a=0$ follows using Proposition [\[prop:sgn\]](#prop:sgn){reference-type="ref" reference="prop:sgn"}: $$\langle\omega(\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^\kappa), \ \chi^{(1^m)} \rangle= (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\mathrm{sgn}_{S_m}} _{S_n} \chi^{\kappa}) (g) =\varepsilon_n(\kappa)|\mathcal{D}^{\kappa}_{0 ,m}|.$$

In the general case, let $\kappa=\lambda / \mu$. By Frobenius reciprocity and Lemma [\[lemma:skewres\]](#lemma:skewres){reference-type="ref" reference="lemma:skewres"}, $$\begin{split}
\langle\omega(\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^\kappa), \ \mathop{\mathrm{Ind}}_{S_a \times S_b}^{S_m} (\chi^{(a)} \times \chi^{(1^b)}) \rangle
= \hskip2in \\ 
\hskip1in \langle\sum_\tau \omega(\mathop{\mathrm{Res}}_{S_a \wr S_n} \chi^{\tau / \mu}) \times \omega(\mathop{\mathrm{Res}}_{S_b \wr S_n} \chi^{\lambda / \tau}), \chi^{(a)} \times \chi^{(1^b)} \rangle, 
\end{split}$$ where the sum is over all partitions $\tau$ such that $\mu \subseteq \tau \subseteq \lambda$ and $|\tau / \mu| = an$. Using the two extreme cases, it follows that $$\begin{aligned}
\langle\omega(\mathop{\mathrm{Res}}_{S_m \wr S_n} \chi^\kappa), \ \mathop{\mathrm{Ind}}_{S_a \times S_b}^{S_m} (\chi^{(a)} \times \chi^{(1^b)}) \rangle&=   \sum_\tau \varepsilon_n(\tau / \mu) |\mathcal D^{\tau / \mu}_{a,0}| \varepsilon_n(\lambda / \tau) |\mathcal D^{\lambda / \tau}_{0,b}|\\
 & = \varepsilon_n(\lambda / \mu) \sum_\tau |\mathcal D^{\tau / \mu}_{a,0} | \, |\mathcal D^{\lambda / \tau}_{0,b}|\\
&=   \varepsilon_n(\lambda / \mu) |\mathcal D^{\lambda/ \mu}_{a,b}|
\end{aligned}$$ as required. ◻
:::

The proof of Lemma [\[lemma:DandB\]](#lemma:DandB){reference-type="ref" reference="lemma:DandB"} relies upon the following simple result.

::: lemma
[]{#lemma:compar label="lemma:compar"} Let $\rho_1$ and $\rho_2$ be disjoint border strips, each of length $n$, such that $(\rho_1, \rho_2) \in \mathcal{R}$. For $t\in \{1,2\}$, let $(i_t,j_t)$ and $(k_t,\ell_t)$ be the initial and terminal boxes respectively of $\rho_t$. Then

1.  There exists $(r,s)\in \rho_2$ such that either $r \ge i_1$ and $s> j_1$, or $r> k_1$ and $s\ge \ell_1$.

2.  There exists $(t,q)\in \rho_1$ such that either $t< i_2$ and $q\le j_2$, or $t \le k_2$ and $q<\ell_2$.
:::

::: proof
*Proof.* We prove the first statement only; the second is entirely analogous. Suppose that $(\rho_1, \rho_2) \in \mathcal{R}$ but there exists no $(r,s)\in \rho_2$ satisfying the stated conditions. Since $(\rho_1, \rho_2)\in  \mathcal{R}$, there exist $(a,b ) \in \rho_1$ and $(e,f)\in \rho_2$ such that $(a,b) <_p (e,f)$. In particular, $i_1 \le e$ and $\ell_1\le f$, and our assumption implies that $f\le j_1$ and $e\le k_1$. Thus $(e,f)$ belongs to the rectangle $[i_1,k_1]\times [\ell_1,j_1]$. The ribbon $\rho_1$ divides its complement in $[i_1,k_1]\times [\ell_1,j_1]$ into two connected components, with $(e,f)$ lying to the south east of $\rho_1$ (as $(a,b) \in \rho_1$ satisfies $(a,b)  <_p (e,f)$).

Let $\tau = \{ (c, j_1+1) : i_1\le c\le k_1+1\} \cup \{ (k_1+1, d) : \ell_1\le d\le j_1+1 \}$, and observe that our assumption ensures that $\tau \cap \rho_2=\varnothing$. The set $\rho_1 \cup \tau$ is the boundary of a certain region $\Delta$. Since $(e,f)\in \Delta$ and $\rho_2$ does not intersect the boundary, the whole border strip $\rho_2$ must be contained in $\Delta$ and, in particular, $\rho_2 \subset [i_1,k_1]\times [\ell_1,j_1]$. However, as $\rho_1$ is a border strip of the same length with initial and terminal boxes $(i_1,k_1)$ and $(\ell_1,j_1)$ respectively, $\rho_2$ must contain the corners $(i_1,k_1)$ and $(\ell_1,j_1)$ and hence intersect $\rho_1$, contrary to our hypotheses. ◻
:::

This lemma can be used to verify that if $D$ is a horizontal border-strip $n$-diagram with initial box $(i_\sigma, j_\sigma)\in \sigma \in D$ then $(\sigma, \rho) \notin \mathcal{R}$ for all $\rho \in D$. Indeed, if $(\sigma, \rho) \in \mathcal{R}$ then by Lemma [\[lemma:compar\]](#lemma:compar){reference-type="ref" reference="lemma:compar"}(1) there exists $(r,s) \in \rho$ such that either $r \ge i_\sigma$ and $s > j_\sigma$, or $r>k_\sigma$ and $s \ge \ell_\sigma$. The 'either' case is impossible because $(i_\rho, j_\rho)$ is the initial box of $D$.

Hence $(i_\rho, j_\rho)$ must lie in $[i_\sigma,r]\times [s,j_\sigma]$, to the south of $\sigma$, and so a box of $\sigma$ lies above $(i_\rho, j_\rho)$, contradicting the horizontality of $D$. Similarly, if $E$ is a vertical border-strip $n$-diagram with initial box $(i_{\sigma}, j_{\sigma}) \in \sigma \in E$ then $(\rho,\sigma) \notin \mathcal{R}$ for all $\rho \in E$: indeed if $(\rho,\sigma) \in \mathcal{R}$ then by Lemma [\[lemma:compar\]](#lemma:compar){reference-type="ref" reference="lemma:compar"}(2) there exists $(t,q) \in \rho$ such that either $t < i_\sigma$ and $q \le j_\sigma$, or $t\le k_\sigma$ and $q < \ell_\sigma$. The 'either' case is again ruled out because $(i_{\sigma}, j_{\sigma})$ is the initial box of $E$. Hence $$(t,q) <_p (k_\sigma,q) \le_p (k_\sigma, \ell_\sigma),$$ and so $(k_{\sigma}, q)$ is a box of $E$ because $\bigcup E$ is convex. But this box lies to the left of the terminal box of $\sigma$, a contradiction. We shall use these observations in the proof of Lemma [\[lemma:DandB\]](#lemma:DandB){reference-type="ref" reference="lemma:DandB"}.

::: proof
*Proof of Lemma [\[lemma:DandB\]](#lemma:DandB){reference-type="ref" reference="lemma:DandB"}.* We construct a bijection $$f \colon \mathcal{B}^{\kappa}_{a,b} \sqcup \mathcal{B}^{\kappa}_{a+1,b-1}  
\to \mathcal{D}^{\kappa}_{a,b}.$$ Given $(D,E) \in \mathcal{B}^{\kappa}_{a,b} \sqcup \mathcal{B}^{\kappa}_{a+1,b-1}$, let $\sigma$ denote the unique element of $D\cap E$. For $(D,E) \in \mathcal{B}^{\kappa}_{a,b}$, we set $f(D,E)=(D,E \setminus \{\sigma\})$, and for $(D,E) \in \mathcal{B}^{\kappa}_{a+1,b-1}$ we set $f(D,E)=(D\setminus \{\sigma\}, E)$.

Firstly, we verify that $f(D,E) \in \mathcal{D}^{\kappa}_{a,b}$. Suppose that $(D,E) \in \mathcal{B}^{\kappa}_{a,b}$ (as the second case is exactly analogous). The conditions ($1'$), (3), (4) on $(D,E \setminus \{\sigma\})$ follow immediately provided that $\bigcup\, (E \setminus \{\sigma\})$ is a skew shape. Take $x<_p y<_p z$ with $x,z \in \bigcup\, (E \setminus \{\sigma\})$. We know $y$ lies in the skew shape $\bigcup E$, so suppose that $y \in \sigma$. Then if $z \in \rho_E \in E \setminus \{\sigma \}$ we have $(\sigma, \rho_E) \in \mathcal{R}$, contrary to condition (4) of Definition [\[def:hook-like\]](#def:hook-like){reference-type="ref" reference="def:hook-like"}.

To see that $f$ is the bijection we require, we define its inverse map $$h \colon   \mathcal{D}^{\kappa}_{a,b} \to  \mathcal{B}^{\kappa}_{a,b} \sqcup \mathcal{B}^{\kappa}_{a+1,b-1}.$$ For $(D,E) \in \mathcal{D}^{\kappa}_{a,b}$, let $\sigma$ denote the border strip of $D \cup E$ containing the initial box of $\kappa$. Then if $\sigma \in D$ we set $h(D,E)=(D, E \cup \{\sigma\})$ and if $\sigma \in E$ we set $h(D,E)=(D \cup \{\sigma\}, E)$.

We verify that $h(D,E) \in  \mathcal{B}^{\kappa}_{a,b} \sqcup \mathcal{B}^{\kappa}_{a+1,b-1}$. Suppose $\sigma \in D$. To see that $\bigcup\,(E \cup \{\sigma\})$ is a skew shape, take $x <_p y<_p z$ with $x ,z \in\bigcup\,( E \cup \{\sigma\})$. If $x,z$ lie in the skew shape $\bigcup E$ then so does $y$, and similarly if $x,z \in \sigma$ then $y \in \sigma$. Two cases remain. Firstly, if $x \in \rho \in E$ and $z \in \sigma \in D$ then $(\rho, \sigma) \in \mathcal{R}$, contrary to the definition of $\mathcal{D}^{\kappa}_{a,b}$. Secondly, suppose that $x \in \sigma \in D$ and $z   \in \bigcup E$, and, for a contradiction, that $y \in \rho \in D \setminus\{ \sigma\}$. Then $(\sigma, \rho) \in \mathcal{R}$, which is impossible by the first observation following Lemma [\[lemma:compar\]](#lemma:compar){reference-type="ref" reference="lemma:compar"}. (The proof that $D \cup \{\sigma\}$ is a skew shape in the case $\sigma \in E$ is entirely analogous.)

Next we verify that if $\sigma \in D$ then $E \cup \{\sigma \}$ is a vertical $n$-border strip diagram. Let $(i_\sigma, j_\sigma)$ be the initial box of $\sigma$ and let $(k_\sigma, \ell_\sigma) \in \sigma$ be the terminal box of $\sigma$. Since $E$ is a vertical $n$-border strip diagram, it suffices to check firstly that there is no box $(k_\sigma, \ell) \in \rho_E \in E$ for $\ell <\ell_\sigma$, and secondly that, if $\rho \in E$ has terminal box $(k_\rho, \ell_\rho)$, then $(k_\rho, j) \notin \sigma$ for any $j<\ell_\rho$. The first statement is a consequence of the definition of $\mathcal{D}^{\kappa}_{a,b}$ since the existence of such a box implies $(\rho_E,\sigma) \in \mathcal{R}$. If the second statement fails with $(k_\rho, j) \in \sigma$, then $(\sigma, \rho) \in \mathcal{R}$ and Lemma [\[lemma:compar\]](#lemma:compar){reference-type="ref" reference="lemma:compar"}(1) implies that there is a box $(r,s) \in \rho$ with either $r \ge i_\sigma$ and $s > j_\sigma$, or $r>k_\sigma$ and $s \ge \ell_\sigma$. The 'either' case is ruled out because $(i_\sigma, j_\sigma)$ is the initial box of $\sigma$. In the 'or' case, since $(k_\rho, j) \in \sigma$, we have $k_\sigma\ge k_\rho$, and therefore $r> k_\sigma\ge k_\rho$, contradicting that $(r,s) \in \rho$. (The proof that if $\sigma \in E$ then $D \cup \{\sigma \}$ is a horizontal $n$-border strip diagram is simpler, using the definition of $\mathcal{D}^{\kappa}_{a,b}$ and the fact that $(i_\sigma, j_\sigma)$ is the initial box of $\vartheta$.)

Finally, we must check that if $\sigma \in D$ then there do not exist $\rho \in D$ and $\rho' \in E \cup \{\sigma \}$ with $(\rho', \rho) \in \mathcal{R}$. This is true because $(D,E) \in \mathcal{D}^{\kappa}_{a,b}$, and, by the observation following Lemma [\[lemma:compar\]](#lemma:compar){reference-type="ref" reference="lemma:compar"}, for all $\rho \in D$, $(\sigma, \rho) \notin \mathcal{R}$. (Again, the case $\sigma \in E$ is similar).

We have demonstrated that $f$ and $h$ are well-defined, and by their construction the maps are mutually inverse. ◻
:::

This completes the proof of Theorem [\[thm:hookdefl\]](#thm:hookdefl){reference-type="ref" reference="thm:hookdefl"} on deflation with respect to hook characters. We now give some results on $\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n} \chi^{\lambda}$ for an arbitrary irreducible character $\vartheta$.

Proposition [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"} combined with the Littlewood--Richardson rule yields the following corollary, which gives a useful sufficient condition for the deflation of an irreducible character of $S_{mn}$ to vanish on an $n$-cycle.

::: corollary
[]{#cor:nv label="cor:nv"} Let $m$, $n \in \mathbf{N}$, let $\lambda$ be a partition of $mn$. Let $\beta$ be a partition of $m$ and let $\vartheta= \chi^\beta$. Let $g \in S_n$ be an $n$-cycle. If $(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n} \chi^{\lambda})(g) \not= 0$ then $\lambda$ has empty $n$-core and moreover, $\lambda^{(i)} \subseteq \beta$ for each $i \in \{0,\ldots,n-1\}$, where $(\lambda^{(0)}, \ldots, \lambda^{(n-1)})$ is the $n$-quotient of $\lambda$. In this case $$(\mathop{\mathrm{Def\hskip-0.3pt res}}^\vartheta_{S_n} \chi^{\lambda})(g) = \varepsilon_n(\lambda / \varnothing) c^\beta_{\lambda^{(0)}\ldots\lambda^{(n-1)}}$$ where $c^\beta_{\lambda^{(0)}\ldots\lambda^{(n-1)}}$ denotes a generalized Littlewood--Richardson coefficient.
:::

A related result is Proposition [\[prop:gen_deg\]](#prop:gen_deg){reference-type="ref" reference="prop:gen_deg"} below, which gives the degrees of the deflations of the irreducible characters of $S_{mn}$ to $S_n$. It may be proved in the same way as Equation [\[eq:deflation_special\]](#eq:deflation_special){reference-type="eqref" reference="eq:deflation_special"} in §1. Note that the right-hand side equals the generalized Littlewood--Richardson coefficient $c^\lambda_{\beta\ldots\beta}$.

::: proposition
[]{#prop:gen_deg label="prop:gen_deg"} Let $m$, $n \in \mathbf{N}$. Let $\beta$ be a partition of $m$ and let $\vartheta= \chi^\beta$. Then $$\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_n}(\chi^\lambda)(1_{S_n}) = 
\left<
\mathop{\mathrm{Ind}}^{S_{mn}}_{S_m \times \cdots \times S_m} \chi^{\beta} \times \cdots \times \chi^\beta, 
 \chi^\lambda
\right>$$ for any partition $\lambda$ of $mn$.$\qed$
:::

We end with an example showing how Propositions [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"}, [\[prop:defres_decomp\]](#prop:defres_decomp){reference-type="ref" reference="prop:defres_decomp"}, and  [\[prop:gen_deg\]](#prop:gen_deg){reference-type="ref" reference="prop:gen_deg"} and Corollary [\[cor:nv\]](#cor:nv){reference-type="ref" reference="cor:nv"} may be used to calculate the values of an irreducible character of $S_{mn}$ deflated with respect to an arbitrary character of $S_m$.

::: example
Let $\vartheta= \chi^{(2,2)}$. We shall find $(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4}  \chi^{(6,4,4,2)})(g)$ in the cases where $g\in S_4$ is a transposition or a double transposition.

Firstly take $g$ to be a transposition. By Proposition [\[prop:defres_decomp\]](#prop:defres_decomp){reference-type="ref" reference="prop:defres_decomp"} we have $$(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4} \!\chi^{(6,4,4,2)})(g) = \sum_{\tau} (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_2} \chi^{\tau})(1_{S_2})  (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_2} \chi^{(6,4,4,2) / \tau})(k)$$ where $k = (12) \in S_2$ and the sum is over all partitions $\tau$ of $8$. Using Proposition [\[prop:gen_deg\]](#prop:gen_deg){reference-type="ref" reference="prop:gen_deg"} on the first term we obtain $$(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4} \!\chi^{(6,4,4,2)})(g) = \sum_{\tau} c^{\tau}_{(2,2)(2,2)} (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_2} \chi^{(6,4,4,2) / \tau})(k)$$ with the same conditions on the sum. By Proposition [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"}, we need only consider those partitions $\tau$ such that $(6,4,4,2) / \tau$ is 2-decomposable. The $2$-quotient of $(6,4,4,2)$ is $\bigl((2,1), (3,2)\bigr)$, so the $\tau$ we must consider are the partitions $(6,1^2)$, $(4,3,1)$, $(6,2)$, $(4,2^2)$, $(4^2)$, $(3^2,2)$, $(4,2,1^2)$, $(2^4)$, $(3^2,1^2)$. Calculation shows that $c^{\tau}_{(2,2)(2,2)} = 1$ when $\tau \in P$ where $$P=\{
(4,3,1),(4,2^2), (4^2), (2^4), (3^2,1^2) \}$$ and that $c^{\tau}_{(2,2)(2,2)}$ is zero in the other four cases. Hence by Proposition [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"} we have $$\begin{split}
 (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4} \chi^{(6,4,4,2)})(g) = \hskip3in \\ \hskip1in \sum_{\tau \in P} \varepsilon_2\bigl((6,4,4,2) / \tau\bigr) \left< \mathop{\mathrm{Ind}}^{S_4}_H   \chi^{(2,1) / \tau^{(0)}} \times \chi^{(3,2) / \tau^{(1)}}, \chi^{(2,2)} \right> \end{split}$$ where $H=S_{|(2,1) / \tau^{(0)}|} \times S_{|(3,2) / \tau^{(1)}|}$. The contributions to the sum from the elements of $P$, in the order given above, are $-1$, $+2$, $+1$, $+1$ and $+1$ respectively. For example, the $2$-quotient of $(6,4,4,2) / (4,2,2)$ is $$\bigl((2,1) / (1), (3,2) / (2,1)\bigr)$$ and $\varepsilon_2\bigl( (6,4,4,2) / (4,2,2) ) = 1$, so the contribution from $(4,2,2)$ is $$\left< \mathop{\mathrm{Ind}}^{S_4}_{S_2 \times S_2} \chi^{(2,1) / (1)} \times \chi^{(3,2) / (2,1)}, \chi^{(2,2)} \right> = 
\left< \mathop{\mathrm{Ind}}_{1}^{S_4} 1, \chi^{(2,2)} \right> = 2.$$ Therefore $(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4} \chi^{(6,4,4,2)})(g) = 4$.

Similar arguments can be used in the case where $g$ is a double transposition. By Proposition [\[prop:defres_decomp\]](#prop:defres_decomp){reference-type="ref" reference="prop:defres_decomp"} we have $$(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4} \!\chi^{(6,4,4,2)})(g) = \sum_{\tau} (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_2} \chi^{\tau})(k)  (\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_2} \chi^{(6,4,4,2) / \tau})(h)$$ where $k$ and $h$ are transpositions, and the sum is over all partitions $\tau$ of $8$. Proposition [\[prop:gen_basecase\]](#prop:gen_basecase){reference-type="ref" reference="prop:gen_basecase"} and Corollary [\[cor:nv\]](#cor:nv){reference-type="ref" reference="cor:nv"} restrict the possible partitions $\tau$ to be considered and show that $(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4} \chi^{(6,4,4,2)})(g)$ equals $$\sum_{\tau \in P} \varepsilon_2\bigl(\tau / \varnothing\bigr) c^{(2,2)}_{\tau^{(0)} \tau^{(1)}} \varepsilon_2\bigl((6,4,4,2) / \tau\bigr)
 \left< \mathop{\mathrm{Ind}}^{S_4}_H   \chi^{(2,1) / \tau^{(0)}} \times \chi^{(3,2) / \tau^{(1)}}, \chi^{(2,2)} \right>$$ where $$P = \{ (4,3,1), (4,2^2), (4^2), (2^4), (3^2,1^2) \}$$ and $H=S_{|(2,1) / \tau^{(0)}|} \times S_{|(3,2) / \tau^{(1)}|}$. The contributions to the sum from the elements of $P$, in the order given above, are $+1$, $+2$, $+1$, $+1$ and $+1$ respectively. Hence $(\mathop{\mathrm{Def\hskip-0.3pt res}}^{\vartheta}_{S_4} \!\chi^{(6,4,4,2)})(g) = 6$.
:::
