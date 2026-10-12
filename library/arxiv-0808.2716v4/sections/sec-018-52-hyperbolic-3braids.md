---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-018-52-hyperbolic-3braids
section_title: "Hyperbolic 3–braids"
section_number: 5.2
pages: 28-34
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.969
---
Our goal in this subsection is to show that the $3$--braids whose closure is a hyperbolic link can be easily identified from their Schreier normal form.

Because a closed braid presentation of a link $K$ comes with a natural orientation, we need to consider all possible orientations on components of $K$ that are consistent with $K$ being a 3--braid.

In the lemmas that lead up to Theorem [\[thm:hyperbolic-3braid\]](#thm:hyperbolic-3braid){reference-type="ref" reference="thm:hyperbolic-3braid"}, we rely on two classical invariants that are insensitive to orientation changes on a component of $K$: the (absolute value of) the linking number between components of $K$, and the determinant $\det(K)$. Recall that that $\det(K)$ is the absolute value of the Alexander polynomial of $K$, evaluated at $t=-1$, or equivalently the absolute value of the Jones polynomial of $K$, also evaluated at $t=-1$. It is well--known that reversing the orientation on a component of $K$ leaves the determinant unchanged: from the point of view of the Jones polynomial, this follows because changing the orientation of some component of $K$ changes the Jones polynomial $J_K(t)$ by a power of $t$.

::: lemma
[]{#lemma:determinant label="lemma:determinant"} Let $K = \hat{w}$ be the closure of a generic $3$--braid $$w =  C^k
\sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s} \sigma_2^{-q_s},$$ where $p_i$, $q_i$ are all positive. Suppose that $K$ has two or three components and $\det(K) \leq 4$. Then one of two possibilities holds:

-   $\det(K) =2$, and $w = C^k a$, where $k$ is even and $a \in \left\{  \sigma_1^2 \sigma_2^{-1} , \,  \sigma_1
    \sigma_2^{-2} \right\}$, or

-   $\det(K) =4$, and $w = C^k a$, where $k$ is even and $a \in \left\{ \sigma_1^2 \sigma_2^{-2}, \,  \sigma_1^4
    \sigma_2^{-1}, \,  \sigma_1 \sigma_2^{-4} \right\}$.
:::

::: proof
*Proof.* The proof uses a result of Murasugi [@murasugi:3braids Proposition 5.1]. There, Murasugi shows that a generic $3$--braid must have strictly positive determinant. (In his notation, the class of generic $3$--braids is denoted $\Omega_6$.) The same proposition states that, if $\hat{a}$ denotes the closure of $a=\sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s} \sigma_2^{-q_s}$, then $$\det(K) = \left\{ 
\begin{array}{r l}
\det(\hat{a}), & \mbox{if $k$ is even,} \\
\det(\hat{a})+4, &  \mbox{if $k$ is odd.}
\end{array} \right.$$

If $w$ is generic, then $a$ is also generic, hence $\det(\hat{a})>0$. Thus, if $\det(K) \leq 4$, we must have $k$ even and $\det(K) = \det{\hat{a}}$.

Since $\hat{a}$ is an alternating link, the minimum crossing number is bounded above by the determinant (see, for example, Burde and Zieschang [@burde-zieschang:knots]). Thus the crossing number of $\hat{a}$ is at most 4, and we may list the possibilities for $a$.

Recall that the crossing number of an alternating link is realized by any alternating diagram without nugatory crossings, and the only way an alternating 3--braid can have nugatory crossings is if the braid word is $\sigma_1^r \sigma_2^{-1}$ or $\sigma_1
\sigma_2^{-r}$. Thus alternating closed 3--braids with crossing number at most $4$ consist of words of the form $\sigma_1^p$ for appropriate $p$, $\sigma_1^{p} \sigma_2^{-q}$, for appropriate $p$, $q$, and $\sigma_1\sigma_2^{-1}\sigma_1 \sigma_2^{-1}$. All others will have higher crossing numbers.

Since $\sigma_1^p$ is not generic, we need not consider these. Since the closed braid corresponding to $C^k \sigma_1 \sigma_2^{-1}
\sigma_1 \sigma_2^{-1}$ has just one component, and we are assuming $K$ has at least two components, we need not consider these words either. Finally, the braids $\sigma_1^p \sigma_2^{-q}$ have the appropriate number of crossings for $(p,q) =
(1,1)$, $(1,2)$, $(1,3)$, $(1, 4)$, $(2, 1)$, $(2,2)$, $(3, 1)$, and $(4, 1)$. Of these, $(1,1)$, $(1,3)$, and $(3,1)$ have only one link component. The remaining possibilities are $$a \,  \in \,  \{  \sigma_1^2 \sigma_2^{-1} , \,  \sigma_1
\sigma_2^{-2},  \, \sigma_1^2 \sigma_2^{-2}, \,  \sigma_1^4
\sigma_2^{-1}, \,  \sigma_1 \sigma_2^{-4} \}.$$ If $a = \sigma_1^2 \sigma_2^{-1}$ or $a=  \sigma_1
\sigma_2^{-2}$, one easily computes that $\det(K) = \det(\hat{a})=2$, and conclusion (a) holds. If $a$ is one of $\sigma_1^2 \sigma_2^{-2}$, $\sigma_1^4
\sigma_2^{-1}$, or $\sigma_1 \sigma_2^{-4}$, then $\det(K) = \det(\hat{a})=4$, and conclusion (b) holds. ◻
:::

We can now restrict the $3$--braids that correspond to Seifert fibered links.

::: lemma
[]{#lemma:seifert-braids label="lemma:seifert-braids"} Let $K = \hat{w}$ be the closure of a 3--braid $w$, and suppose that $S^3 {\smallsetminus}K$ is Seifert fibered. Then $w$ is either non-generic, or else conjugate to $\sigma_1^p \sigma_2^{\pm 1}$, $\sigma_1^{\pm 1}
\sigma_2^{q}$, or $\sigma_1^{2} \sigma_2^{-2}$.
:::

::: proof
*Proof.* A theorem of Burde and Murasugi [@burde-murasugi] states that if $S^3 {\smallsetminus}K$ is Seifert fibered, then $K$ consists of finitely many fibers in a (possibly singular) Seifert fibration of $S^3$. In case the Seifert fibration of $S^3$ is not singular, the fibration extends to $S^3$. The Seifert fibrations of $S^3$ were classified by Seifert [@seifert:fibering] (see also Orlik [@orlik:seifert-manifolds]). As a consequence, $K$ must be a *generalized torus link*: a link that is embedded on an unknotted torus $T$ (this is called an $(m,n)$ torus link) plus possibly one or both cores of the solid tori in the complement of $T$.

The singular fibration does not extend to $S^3$: it is the product fibration on a solid torus, in which each fiber is a meridian of the complementary unknot. However, note that in this case the result is again a generalized torus link, with the unknot making up the core of the $(m, 0)$ torus link.

The question of which closed 3-braids represent generalized torus links has been studied by Murasugi in [@murasugi:3braids].

In an $(m,n)$ torus link, we may assume without loss of generality that $m>0$, and that either $n=0$ or ${\left\vert n \right\vert} \geq m$. With this normalization, a theorem of Schubert [@schubert:braids] implies that the bridge number of the $(m,n)$ torus link is $m$. Since the braid index is greater than or equal to the bridge number, any choice of orientation on the components of an $(m,n)$ torus link must yield a braid index of at least $m$.

Thus, if we add $c$ cores of solid tori and obtain a $3$--braid, $1
\leq m \leq 3-c$. There are three cases, conditioned on the value of $c$.

[Case 0: $c=0$.]{.underline} Then $K$ is an $(m, n)$ torus link, where $1 \leq m \leq 3$.

Murasugi classifies the torus links that can be written as closed 3--braids in [@murasugi:3braids Section 12]. However, a careful reading of his proofs indicates that he is assuming multiple components of torus links are always oriented consistently. For our purposes, we will also need to consider the torus links in which the orientation of some component is reversed. In fact, the machinery developed by Murasugi in this monograph is sufficient to handle all choices of orientation. For ease of reading, we will include the arguments for all the cases not immediately apparent from [@murasugi:3braids].

If $m=1$, then $K$ is the unknot, and Theorem 12.1 in Murasugi's monograph shows $w \sim \sigma_1^{\pm 1} \sigma_2^{\pm 1}$. If $m=2$, then $K$ is a $(2,n)$ torus link. If the (one or two) components of $K$ are oriented consistently, then it is an *elementary* torus link in Murasugi's terminology. Then, Theorem 12.3 of his monograph implies $w \sim \sigma_1^p \sigma_2^{\pm 1}$ or $w\sim
\sigma_1^{\pm 1} \sigma_2^{q}$.

Now, suppose that $n=2\ell$, and $K$ is a $(2, 2\ell)$ torus link whose components have opposite orientations. Then $K$ is the oriented boundary of a Seifert surface that is an annulus. Using this annulus, we calculate that the Alexander polynomial of $K$ is $\Delta_K(t)=
\ell(1-t)$; thus $\deg{\Delta_K(t)}=1$. By Proposition 8.1 of [@murasugi:3braids], $K$ can be the closure of a 3--braid only if ${\left\vert \ell \right\vert} \leq \frac{1}{2}{\deg \Delta_K(t)}+2=\frac{5}{2}$. Since the determinant of the $(2, 2\ell)$ torus link is ${\left\vert 2\ell \right\vert}$, and this fact remains true under orientation reversal of components, $\det(K) =
{\left\vert 2\ell \right\vert} \leq 4$. Thus, if $w$ is a generic $3$--braid that represents $K$ with this orientation, Lemma [\[lemma:determinant\]](#lemma:determinant){reference-type="ref" reference="lemma:determinant"} applies.

If $\det(K)= 2$, Lemma [\[lemma:determinant\]](#lemma:determinant){reference-type="ref" reference="lemma:determinant"} says the generic braid $w$ representing $K$ must be conjugate to $C^k \sigma_1^2
\sigma_2^{-1}$ or $w \sim C^k \sigma_1 \sigma_2^{-2}$, where $k$ is even. Without loss of generality, say $w \sim C^k \sigma_1^2 \sigma_2^{-1}$. Then the two components of $\hat{w}$ have linking number equal to ${\left\vert 2k+1 \right\vert}$. But since $K$ is the $(2, \pm2)$ torus link, the linking number of the two components is $1$. Thus $k=0$, and $w \sim \sigma_1^2
\sigma_2^{-1}$, as desired.

If $\det(K)= 4$, Lemma [\[lemma:determinant\]](#lemma:determinant){reference-type="ref" reference="lemma:determinant"} says the only generic braids representing $K$ must be conjugate to $C^k \sigma_1^2
\sigma_2^{-2}$, $C^k \sigma_1^4 \sigma_2^{-1}$, or $C^k \sigma_1
\sigma_2^{-4}$. The closure of $C^k \sigma_1^2 \sigma_2^{-2}$ has three components, so we don't need to consider this case. If $w \sim
C^k \sigma_1^{4} \sigma_2^{-1}$, then the two components of $\hat{w}$ have linking number ${\left\vert 2+2k \right\vert}$, which is equal to $2$ by hypothesis. Thus $k$ is $-2$ or $0$. But if $k = -2$, the closure of $C^{-2}
\sigma_1^4 \sigma_2^{-1}$ is a hyperbolic link, a contradiction. Thus $k=0$, and $w \sim \sigma_1^4 \sigma_2^{-1}$, as desired. The argument when $w \sim C^k \sigma_1 \sigma_2^{-4}$ is identical.

Finally, suppose that $m=3$, and $K$ is a $(3,n)$ torus link. Then $K$ has either one or three components. If $K$ is a knot, Proposition 12.3 of [@murasugi:3braids] shows that $K$ cannot be represented by a generic $3$--braid. In fact, Murasugi's argument also works for links, with all orientations, but for completenss we include the argument here.

If $K$ is a 3--component torus link $(3, 3\ell)$, the linking number of any two components of $K$ has absolute value ${\left\vert \ell \right\vert}$. Proposition 3.3 of [@murasugi:3braids] implies that $\det(K)$ is either $0$ or $4$. By Lemma [\[lemma:determinant\]](#lemma:determinant){reference-type="ref" reference="lemma:determinant"}, any generic braid $w\sim C^k a$ representing $K$, must be conjugate to $C^k
\sigma_1^2 \sigma_2^{-2}$, as all the other possibilities in the lemma have two components. Now, consider the pairwise linking numbers between components in the closure of $w\sim C^k \sigma_1^2 \sigma_2^{-2}$. These pairwise linking numbers are equal in absolute value to ${\left\vert k \right\vert}$, ${\left\vert k+1 \right\vert}$, and ${\left\vert k-1 \right\vert}$. But all these numbers must be equal to ${\left\vert \ell \right\vert}$, a contradiction.

[Case 1: $c=1$.]{.underline} Then $K = L_t \cup L_a$, where $L_t$ is a $(m,n)$ torus link with $m=1$ or $m=2$, and $L_a$ is the core of one of the two solid tori. If $m=1$, then (depending on the choice of solid torus) $K$ is either a $(2, 2n)$ torus link and we reduce to case 0, or $K$ is the Hopf link, which is the $(2,2)$ torus link, and we again reduce to case 0. Thus we may suppose that $L_t$ is a $(2,n)$ torus link. Then, as an unoriented link, $K$ admits a diagram in one of two possible forms, shown in Figure [1](#fig:augmented-torus){reference-type="ref" reference="fig:augmented-torus"}, depending on which solid torus $L_a$ came from.

<figure id="fig:augmented-torus">
<div class="center">
<embed src="figures/Fig_augmented-torus.eps" />
</div>
<figcaption>Case 1 of Lemma <a href="#lemma:seifert-braids" data-reference-type="ref" data-reference="lemma:seifert-braids">[lemma:seifert-braids]</a>: two ways to add the core of a solid torus to a <span class="math inline">(2,<em>n</em>)</span> torus link.</figcaption>
</figure>

[Subcase 1a:]{.underline} Suppose that the link $K$ is depicted in the left panel of Figure 10. Then we can characterize the linking number $lk(L_t, L_a)$ as follows. If $n$ is odd and $L_t$ is a knot, then its linking number with $L_a$ is $\pm 2$; if $n$ is even and $L_t$ has two components, then each component of $L_t$ has linking number $\pm 1$ with $L_a$. Note that the absolute value of the linking number is insensitive to changes of orientation.

If all the strands in Figure [1](#fig:augmented-torus){reference-type="ref" reference="fig:augmented-torus"} are oriented counterclockwise, the link $K$ in the left panel of the figure can be represented by the braid word $v = \sigma_1^n \sigma_2 \sigma_1^2
\sigma_2$. Of course, *a priori* there may be other braid representatives, possibly corresponding to other choices of orientation on one or more components of $K$. Nonetheless, knowing that $K$ can be obtained as the closure $\hat{v}$ of the braid represented by $v$ allows us to compute link invariants. Because the normal form of $v$ is $C \,
\sigma_1^{n-2}$, Murasugi's Proposition 3.6 gives that $\det(K)=4$. Suppose that, with some choice of orientation, $K$ is represented by the generic braid $w$. Since $\det(K)=4$, Lemma [\[lemma:determinant\]](#lemma:determinant){reference-type="ref" reference="lemma:determinant"} implies the normal form of $w$ must be one of $C^k \sigma_1^2 \sigma_2^{-2}$, $C^k \sigma_1^4
\sigma_2^{-1}$, or $C^k \sigma_1 \sigma_2^{-4}$.

If $w \sim C^k \sigma_1^2 \sigma_2^{-2}$, then $K = \hat{w}$ is a 3--component link. The $2$--component links contained in $K$ have pairwise linking numbers equal in absolute value to ${\left\vert k \right\vert}$, ${\left\vert k+1 \right\vert}$, and ${\left\vert k-1 \right\vert}$. By hypothesis, two of these linking numbers must be equal to 1. It follows that the only possibility is $k = 0$, hence $w \sim \sigma_1^2 \sigma_2^{-2}$, as desired.

If $w \sim C^k \sigma_1^{4} \sigma_2^{-1}$, then $K = \hat{w} = L_t
\cup L_a$ is a 2--component link. In this case, we compute that ${\left\vert lk(L_t, L_a) \right\vert} = {\left\vert 2+2k \right\vert}$, which is equal to $2$ by hypothesis. Thus $k$ is $-2$ or $0$. But if $k = -2$, the closure of $C^{-2} \sigma_1^4 \sigma_2^{-1}$ is a hyperbolic link, a contradiction. Thus $k=0$, and $w \sim \sigma_1^4 \sigma_2^{-1}$, as desired. The case when $w \sim C^k \sigma_1 \sigma_2^{-4}$ is identical.

[Subcase 1b:]{.underline} Suppose that the unoriented link $K$ is depicted in the right panel of Figure 10. It follows that $\, lk(L_t, L_a) = \pm n,$ depending on choices of orientations of the components. If all the strands of $K$ are oriented counterclockwise, $K$ can be represented by the braid word $v = (\sigma_1 \sigma_2 \sigma_1)^n$. (Just as in Subcase 1a, there may be other braid representatives, but knowing one braid representative $v$ allows us to compute invariants that are insensitive to orientation.) Using the braid relation $\sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1
\sigma_2$, we can rewrite $v$ as $$v = \left\{ \begin{array}{l l} C^{n/2}, & \mbox{if $n$ is even,} \\
C^{(n-1)/2} \sigma_1 \sigma_2 \sigma_1, & \mbox{if $n$ is odd.}
\end{array} 
\right.$$ If $n$ is even, then $\hat v$ is a torus link. Thus the unoriented link $K$ is a torus link, and we reduce to Case 0. If $n$ is odd, then Murasugi's Proposition 3.5 gives $\det(K)=2$. Thus, by Lemma [\[lemma:determinant\]](#lemma:determinant){reference-type="ref" reference="lemma:determinant"}, any generic braid $w$ that also represents $K$ must have normal form $C^k \sigma_1^{2} \sigma_2^{-1}$ or $C^k \sigma_1 \sigma_2^{-2}$.

If $w \sim C^k \sigma_1^{2} \sigma_2^{-1}$, then $K = \hat{w} = L_t
\cup L_a$ is a 2--component link. We may immediately compute that one component $L_t$ is the $(2, 2k-1)$ torus knot, the other component $L_a$ is the unknot, and ${\left\vert lk(L_t, L_a) \right\vert} = {\left\vert 2k+1 \right\vert}$. Because by assumption, $L_t$ is the $(2, n)$ torus link, this implies ${\left\vert n \right\vert}={\left\vert 2k-1 \right\vert}$. Additionally, since by assumption $lk(L_t,
L_a)=\pm n$, we may conclude that ${\left\vert n \right\vert}={\left\vert 2k+1 \right\vert}$. This is possible only if $k=0$. So $w \sim \sigma_1^2 \sigma_2^{-1}$, as desired. The case when $w \sim C^k \sigma_1 \sigma_2^{-2}$ is identical.

[Case 2: $c=2$.]{.underline} Then $K = L_t \cup L_a \cup L_b$, where $L_t$ is an unknot on $T$, and $L_a$ and $L_b$ are cores of the two solid tori. Since $L_t$ is a $(1,n)$ curve on the torus $T$, one of the cores $L_a$ or $L_b$ (say, $L_b$) can be isotoped to lie on $T$, disjointly from $L_t$. Thus, as an unoriented link, $L_t \cup L_b$ is a torus link on $T$, and this case reduces to Case 1. ◻
:::

The next theorem characterizes the 3-braids whose closures represent hyperbolic links.

::: theorem
[]{#thm:hyperbolic-3braid label="thm:hyperbolic-3braid"} Let $w \in B_3$ be a word in the braid group, and let $K \subset S^3$ be the link obtained as the closure of $w$. Then $S^3 {\smallsetminus}K$ is hyperbolic if and only if $w$ is generic and not conjugate to $\sigma_1^p \sigma_2^q$ for arbitrary integers $p, q$.
:::

::: proof
*Proof.* First, we check the "only if" direction. If $w$ is non-generic, then by Theorem [\[thm:hyperbolic-bundle\]](#thm:hyperbolic-bundle){reference-type="ref" reference="thm:hyperbolic-bundle"}, $M_w = S^3 {\smallsetminus}(K
\cup A)$ is a graph manifold with Gromov norm 0. Since the Gromov norm of a manifold cannot increase under Dehn filling [@thurston:notes Proposition 6.5.2], $S^3 {\smallsetminus}K$ also has Gromov norm 0, and is not hyperbolic. If $w$ is generic and conjugate to $\sigma_1^p \sigma_2^{\pm 1}$, then $K$ is a $(2,p)$ torus link (similarly for $\sigma_1^{\pm 1} \sigma_2^{q}$). Finally, if $w$ is conjugate to $\sigma_1^p \sigma_2^q$, where $|p|, |q| \geq 2$, then $K$ is the connected sum of $(2,p)$ and $(2,q)$ torus links, hence cannot be hyperbolic.

For the "if" direction, suppose that $S^3 {\smallsetminus}K$ is not hyperbolic. Then, by Thurston's hyperbolization theorem [@thurston:survey], it is reducible, toroidal, or Seifert fibered. If $S^3{\smallsetminus}K$ is Seifert fibered, then Lemma [\[lemma:seifert-braids\]](#lemma:seifert-braids){reference-type="ref" reference="lemma:seifert-braids"} implies $w$ is non-generic or conjugate to $\sigma_1^p \sigma_2^{q}$. Meanwhile, if $S^3 {\smallsetminus}K$ is reducible, then $K$ is a split link. By a theorem of Murasugi [@murasugi:3braids Theorem 5.1], this can only happen if $w \sim \sigma_1^p$: hence, $w$ is not generic.

Finally, suppose that $S^3 {\smallsetminus}K$ contains an essential torus $T$. If $w$ is not generic, then we are done. If $w$ is generic, a theorem of Lozano and Przytycki [@lozano-przytycki Corollary 3.3] says that $T$ always has meridional compression disks, i.e. there is some disk $D \subset S^3$ such that $D\cap T = \partial D$ and $D\cap
K$ is a point.[^1] After meridionally compressing $T$, i.e. after replacing a neighborhood of $\partial D$ on $T$ with two parallel copies of the annulus $D{\smallsetminus}K$, we obtain an essential, meridional annulus that splits $K$ into connected summands. But by a theorem of Morton [@morton:composite-braids], a braid $w \in B_3$ represents a composite link if and only if $w \sim \sigma_1^p \sigma_2^q$, where $|p|, |q| \geq 2$. See Birman and Menasco [@birman-menasco:toroidal Corollary 1] for another way to identify the toroidal $3$--braids. ◻
:::

## Volume estimates

For sufficiently long generic $3$--braids, the methods of the previous sections estimate hyperbolic volume.

::: theorem
[]{#thm:3braid-volume label="thm:3braid-volume"} Let $K= \hat{w}$ be the closure of a generic 3--braid $w \sim C^k
\sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s} \sigma_2^{-q_s}$, where $p_i$, $q_i$ are all positive and $w \nsim
\sigma_1^p\sigma_2^{-q}$. Then $K$ is hyperbolic, and $$\label{eq:3braid-volume}
4v_3 \, s - 276.6 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \: 4v_8 \, s.$$ Furthermore, the multiplicative constants in both the upper and lower bounds are sharp.
:::

::: proof
*Proof.* Let $A$ be the braid axis of $K$. Then $M_w = S^3 {\smallsetminus}(K \cup
A)$ is a 4--punctured sphere bundle with monodromy $$\Omega = L^{p_1} R^{q_1} \cdots L^{p_s} R^{q_s}.$$

Futer and Guéritaud showed [@gf:two-bridge Corollary B.2] that the length of $\Omega$ coarsely determines the volume of $M$: $$\label{eq:bundle-volume}
4 v_3 \, s \: \leq \: {\rm vol}(M_w) \: < \: 4v_8 \, s,$$ where both the upper and lower bounds are sharp. That is: there exist $4$--punctured sphere bundles that realize the lower bound, and other bundles that are $\varepsilon$--close to the upper bound. Since $S^3
{\smallsetminus}K$ is obtained by Dehn filling on $M_w$, the same upper bound applies to the volume of $S^3 {\smallsetminus}K$. Furthermore, by choosing an extremely long filling slope (which will happen when ${\left\vert k \right\vert} \to \infty$), one can arrange for ${\rm vol}(S^3 {\smallsetminus}K)$ to be arbitrarily close to $4 v_8 \, s$.

For the lower bound on volume, we rely on Theorem [\[thm:4ps-area\]](#thm:4ps-area){reference-type="ref" reference="thm:4ps-area"}. That theorem states that the meridian of $A$ (which will be transverse to the fibers) has length at least $8\sqrt{3} \, s/147$. In particular, when $s \geq 67$, the meridian will be longer than $2\pi$. Thus we may apply Theorem 1.1 of [@fkp-07], which estimates the change in volume under Dehn filling along slopes longer than $2\pi$. For all $s \geq 67$, we obtain $$\begin{array}{l l l l l}
{\rm vol}(S^3 {\smallsetminus}K) 
&\geq&  \left(1-\left(\dfrac{2\pi}{8\sqrt{3} \, s/147}\right)^2\right)^{3/2} {\rm vol}(M_w), 
& \mbox{by \cite[Thm 1.1]{fkp-07} and Thm \ref{thm:4ps-area} }\\
&\geq&  \left(1-\dfrac{7203  \, \pi^2 }{16 \, s^2} \right)^{3/2} 4 v_3 \, s,
& \mbox{by inequality (\ref{eq:bundle-volume})}
\end{array}$$ Note that by calculus, $$\left(1-\dfrac{7203 \, \pi^2}{16\,s^2}\right)^{3/2} 4 v_3 \, s -
4v_3\,s$$ has a minimum of $-276.52\cdots$ for $s\geq 67$. Thus ${\rm vol}(S^3
{\smallsetminus}K) > 4v_3\,s - 276.6$.

On the other hand, if $s \leq 67$, then $4v_3 \, s - 276.6 < 0$, hence the volume estimate is trivially true. Thus the lower bound on volume holds for all hyperbolic $3$--braids.

Finally, to show sharpness of the multiplicative constant in the lower bound, consider $3$--braids of the form $w=(\sigma_1
\sigma_2^{-1})^s$. In the proof of Theorem B.1 of [@gf:two-bridge], it was shown that for the closures of these braids, ${\rm vol}(M_w) = 4v_3s$. Since ${\rm vol}(S^3{\smallsetminus}K) < {\rm vol}(M_w)
= 4v_3s$ for this sequence of knots, the multiplicative constant $4v_3$ must be sharp. ◻
:::

We close this section with an interesting side comment. Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} compares in an intriguing way to prior results that estimate the volume of a link complement in terms of the twist number of a diagram. (See Section [\[sec:diagram-intro\]](#sec:diagram-intro){reference-type="ref" reference="sec:diagram-intro"} and the introduction of [@fkp:coils] for definitions and background.) In the braid word $w$, each term $\sigma_1^{p_i}$ or $\sigma_2^{-q_i}$ corresponds to a twist region involving a pair of strands of $K$. Meanwhile, when $k \neq 0$, the term $C^k$ defines a single *generalized twist region*, in which we perform $k$ full twists on all three strands of the braid. Altogether, the braid word $w$ defines a diagram with either $2s$ or $2s+1$ generalized twist regions -- including $2s$ ordinary twist regions twisting on two strands of $K$. As a result, Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} can be reformulated in the following way.

::: corollary
[]{#cor:3braid-twists label="cor:3braid-twists"} Let $K$ be a hyperbolic closed 3--braid, and let $D(K)$ be the braid diagram corresponding to the Schreier normal form for $K$. If ${t_{\mathrm{gen}}(D)}$ denotes the number of generalized twist regions in the diagram $D$, then $$2v_3 \, {t_{\mathrm{gen}}(D)}- 279 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \: 2v_8 \,
{t_{\mathrm{gen}}(D)}.$$
:::

::: proof
*Proof.* By Theorem [\[thm:hyperbolic-3braid\]](#thm:hyperbolic-3braid){reference-type="ref" reference="thm:hyperbolic-3braid"}, $K$ must be represented by a generic word $w = C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots
\sigma_1^{p_s} \sigma_2^{-q_s}$. Substituting $2s \leq {t_{\mathrm{gen}}(D)}\leq 2s+1$ into Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} gives the desired volume estimate. ◻
:::

::: remark
In [@fkp:coils Corollary 3.2], we show that the twist number alone, as opposed to the generalized twist number, is not a good measure of the volume of 3--braids. Thus the single generalized twist region from the term $C^k$ is important in the corollary above.
:::

[^1]: Lozano and Przytycki's result is stated for "hyperbolic" 3--braids. However, their definition of *hyperbolic* is the same as our definition of *generic*.
