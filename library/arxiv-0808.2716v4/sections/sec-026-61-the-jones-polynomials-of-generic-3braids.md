---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-026-61-the-jones-polynomials-of-generic-3braids
section_title: "The Jones polynomials of generic 3–braids"
section_number: 6.1
pages: 34-40
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.987
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#subsec:generic-jones label="subsec:generic-jones"}

In the case that $K$ is the closure of a 3--braid, we need to relate the Jones polynomial to the Schreier normal form of the braid. (See Theorem [\[thm:schreier-normal\]](#thm:schreier-normal){reference-type="ref" reference="thm:schreier-normal"}.) Here, we will concern ourselves with 3--braids whose Schreier normal forms are *generic*. That is, we will consider braids $b\in B_3$ written in the form $$b= C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}
\sigma_2^{-q_s},$$

where $p_i, q_i, k \in {\mathbb{Z}}$, with $p_i, q_i>0$, and $C:=(\sigma_1
\sigma_2 \sigma_1 )^2$. We set $${\bf p}:=\sum_{i=1}^s p_i, \ \ {\rm and} \ \ {\bf q}:=\sum_{i=1}^s
q_i.$$

The *exponent* $e_b$ of a braid $b$ is the signed sum of its powers. Thus for an alternating braid $a$, $e_a = {\bf p} - {\bf q}$, and if $b=C^k a$, then $e_b = 6k + {\bf p} - {\bf q} = 6k + e_a$. The exponent $e_b$ is closely related to the *writhe* of a diagram, namely the algebraic sum of oriented crossings. Because both of the generators $\sigma_1$ and $\sigma_2$ depicted in Figure [\[fig:3braid-generators\]](#fig:3braid-generators){reference-type="ref" reference="fig:3braid-generators"} are negative crossings, the writhe of the standard diagram of a closed 3--braid is $w(D_b) = - e_b$.

For a braid $b\in B_3$, let $\hat {b}$ denote the closure of $b$. Let $K$ denote the link type represented by ${\hat b}$ and let $J_{K}(t)$ denote the Jones polynomial of $K$. We write $$J_{K}(t)= \alpha_K t^{M(K)}+ \beta_K t^{M(K)-1}+ \ldots + \beta'_K
t^{m(K)+1}+ \alpha'_K t^{m(K)},
\label{eqn:jp}$$ so that $M(K)$ is the highest power of $t$ in $J_K(t)$ and $m(K)$ is the lowest power of $t$ in $J_K(t)$. Now the second and next-to-last coefficients of $J_{K}(t)$ are $\beta_K$ and $\beta'_K$, respectively.

We will also need the following definitions. Associated to a link diagram $D$ and a crossing of $D$ are two link diagrams, each with one fewer crossing than $D$, called the *$A$--resolution* and *$B$--resolution* of the crossing. See Figure [1](#fig:splicing){reference-type="ref" reference="fig:splicing"}.

<figure id="fig:splicing">

<figcaption>Resolutions of a crossing</figcaption>
</figure>

Starting with any $D$, let $s_A(D)$ (resp. $s_B(D)$) denote the crossing--free diagram obtained by applying the $A$--resolution (resp. $B$--resolution) to all the crossings of $D$. We obtain graphs ${\mathbb{G}_A}(D)$, ${\mathbb{G}_B}(D)$ as follows: The vertices of ${\mathbb{G}_A}(D)$ are in one-to-one correspondence with the components of $s_A(D)$. For every crossing of $D$, we add an edge between the vertices of ${\mathbb{G}_A}(D)$ that correspond to the components of $s_A(D)$ at that crossing. In a similar manner, construct the $B$--graph ${\mathbb{G}_B}$ by considering components of $s_B(D)$. A link diagram $D$ is called *adequate* if the graphs ${\mathbb{G}_A}(D)$, ${\mathbb{G}_B}(D)$ contain no 1--edge loops, i.e. if there are no edges with both ends at the same vertex.

Let $v_A(D)$, $e_A(D)$ (resp. $v_B(D)$, $e_B(D)$) denote the number of vertices and edges of ${\mathbb{G}_A}(D)$ (resp. ${\mathbb{G}_B}(D)$). The reduced graph ${\mathbb{G}'_A}(D)$ is obtained from ${\mathbb{G}_A}(D)$ by removing multiple edges connected to the same pair of vertices; similarly one has the reduced graph ${\mathbb{G}'_B}(D)$. Let $e'_A(D)$ (resp. $e'_B(D)$) denote the number edges of ${\mathbb{G}'_A}(D)$ (resp. ${\mathbb{G}'_B}(D)$).

The following results about Jones polynomials of adequate knots are well known.

::: lemma
[]{#lemma:adequate-jones label="lemma:adequate-jones"} Let $D$ be an adequate diagram of a link $K$, whose Jones polynomial is written as in equation ([\[eqn:jp\]](#eqn:jp){reference-type="ref" reference="eqn:jp"}). Then the top and bottom coefficients of $J_K(t)$ satisfy $$\alpha_K = (-1)^{v_B(D) + w(D) -1}, \qquad
  \beta_{K} = (-1)^{v_B(D) + w(D)} (e'_B(D) - v_B(D) + 1),$$ $$\alpha'_K = (-1)^{v_A(D) + w(D) -1} , \qquad
    \beta'_{K} = (-1)^{v_A(D) + w(D)} (e'_A(D) - v_A(D) + 1).$$
:::

::: proof
*Proof.* Let ${\mathbb{Z}}[A,\ A^{-1}]$ denote the ring of Laurent polynomials in a variable $A$, with integer coefficients. Recall that the Kauffman bracket of the diagram $D$, denoted by $\left < D\right >$, is an element in ${\mathbb{Z}}[A, \ A^{-1}]$ such that $$J_{K_a}(t)= (-A)^{-3 w(D)} \left< D\right>
  \left|_{\displaystyle{A=t^{-1/4}}}\right., 
  \label{eqn:Jones-Kauffman}$$ where $w(D)$ is the writhe of $D$, or the algebraic sum of crossings. Now, Kauffman showed that the first and last coefficients of $\left< D
\right>$ are $(-1)^{v_A(D)-1}$ and $(-1)^{v_B(D)-1}$, respectively. (See [@{dasbach-futer2...} Theorem 6.1] for a proof.) Meanwhile, Stoimenow showed [@stoimenow:amphichiral] that the second coefficient is given by $(-1)^{v_A(D)}(e'_A(D) - v_A(D) + 1)$, and similarly the next--to--last coefficient is given by $(-1)^{v_B(D)}(e'_B(D) - v_B(D)
+ 1)$. See [@{dasbach-futer2...} Corollary 6.3] for an alternate proof.

Next, we multiply $\left< D \right>$ by $(-A)^{-3w(D)}$. As a result, all the coefficients are multiplied by $(-1)^{-3w(D)} =
(-1)^{w(D)}$. Finally, to recover the Jones polynomial, we substitute $A = t^{-1/4}$. As a result, the highest powers of $A$ will correspond to the lowest powers of $t$, and vice versa. Thus the top and bottom coefficients of $J_K(t)$ are as claimed. ◻
:::

Given a condition $R$, let $\delta_R$ be the characteristic function of $R$: its value is $1$ when $R$ is true, and $0$ when $R$ is false. The characteristic functions $\varepsilon_{{\bf p}}: = \delta_{{\bf p}\leq 2}$ and $\varepsilon_{{\bf q}}: = \delta_{{\bf q}\leq 2}$ will be particularly useful for expressing the Jones polynomials of $3$--braids.

::: lemma
[]{#lemma:alternating label="lemma:alternating"} Suppose that a link $K_a$ is the closure of an alternating 3-braid $$a= \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}
\sigma_2^{-q_s},$$

with $p_i, q_i>0$. Suppose as well that ${\bf p}> 1$ and ${\bf q}> 1$. Then the following hold:

1.  The highest and lowest powers of $t$ in $J_{K_a}(t)$ are $$M(K_a)=\frac{3{\bf q}-{\bf p}}{2} \quad \mbox{and} \quad
            m(K_a)= \frac{{\bf q}-3{\bf p}}{2}.$$

2.  The first two and last two coefficients in $J_{K_a}(t)$ are $$\alpha_{K_a} = (-1)^{{\bf p}}, \quad \beta_{K_a} = (-1)^{{\bf p}+1} (s - \varepsilon_{{\bf q}}), \quad 
    \beta'_{K_a} = (-1)^{{\bf q}+1}  (s - \varepsilon_{{\bf p}}), \quad \alpha'_{K_a} =(-1)^{{\bf q}},$$ where $\varepsilon_{{\bf p}}$ equals $1$ if ${\bf p}= 2$ and $0$ if ${\bf p}> 2$, and similarly for $\varepsilon_{{\bf q}}$.

3.  The third and third-to-last coefficients in $J_{K_a}(t)$ satisfy $$1 \leq (-1)^{{\bf p}} \gamma_{K_a} \leq \frac{s(s+3)}{2} \quad \mbox{and} \quad
    1 \leq (-1)^{{\bf q}} \gamma'_{K_a} \leq \frac{s(s+3)}{2}.$$

    These upper bounds are attained when $s>1$ and $p_i, q_i > 1$ for all $i$. See Equation ([\[eq:gamma-exact\]](#eq:gamma-exact){reference-type="ref" reference="eq:gamma-exact"}) for a precise formula for $\gamma_{K_a}$.
:::

::: proof
*Proof.* Consider the link diagram $D:={\hat a}$ obtained as the closure of $a$. Note that the diagram $D$ is alternating and reduced, i.e. it contains no nugatory crossings (here, we are using the hypothesis that if $s=1$, then $p_1 = {\bf p}>1$ and $q_1 = {\bf q}>1$). This implies that $D$ is an adequate diagram (compare [@lickbook Proposition 5.3]). Thus we may use Kauffman's work to find the highest and lowest powers of $A$, and Lemma [\[lemma:adequate-jones\]](#lemma:adequate-jones){reference-type="ref" reference="lemma:adequate-jones"} to find the coefficients.

Kauffman showed that the highest and lowest powers of $A$ in the bracket polynomial $\left< D\right>$ are $c(D)+2v_A(D) -2$ and $-c(D)-2v_B(D)+2$, respectively. (See [@lickbook] for an exposition. A proof from the graph theoretic viewpoint can be found in [@{dasbach-futer...} Proposition 7.1].) In our setting, the crossing number is $c(D)={\bf p}+{\bf q}$, $v_A(D)={\bf p}+1$, and $v_B(D)={\bf q}+1$. Thus the highest and lowest powers of $A$ in $\left< D \right>$ are $3{\bf p}+{\bf q}$ and $-3{\bf q}-{\bf p}$, respectively.

By equation ([\[eqn:Jones-Kauffman\]](#eqn:Jones-Kauffman){reference-type="ref" reference="eqn:Jones-Kauffman"}) we multiply $\left< D \right>$ by $(-A)^{-3w(D)} = (-A)^{-3{\bf q}+3{\bf p}}$. (Recall that for a closed 3--braid, $w(D)
= -e_a={\bf q}-{\bf p}$.) Thus the highest power of $A$ becomes $6{\bf p}-2{\bf q}$, and the lowest becomes $2{\bf p}-6{\bf q}$. Then to obtain $J_{K_a}(t)$, replace $A$ by $t^{-1/4}$. Thus the highest power of $t$ in $J_{K_a}(t)$ corresponds to $-1/4$ times the lowest power of $A$, and vice versa: $$M(K_a) = \frac{-(2{\bf p}-6{\bf q})}{4} = \frac{3{\bf q}-{\bf p}}{2}
\quad \mbox{and} \quad
m(K_a) = \frac{{\bf q}-3{\bf p}}{2}.$$

Next, we turn our attention to the top and bottom coefficients of $J_{K_a}$. In the following calculation, we focus on the first three coefficients $\alpha_{K_a}$ $\beta_{K_a}$, and $\gamma_{K_a}$. By Lemma [\[lemma:adequate-jones\]](#lemma:adequate-jones){reference-type="ref" reference="lemma:adequate-jones"} and [@dasbach-lin:head-tail; @stoimenow:amphichiral], these top coefficients only depend on the $B$--resolution of $D$. To find the last three coefficients, one merely needs to interchange ${\bf p}$ with ${\bf q}$ in all the formulas.

From the $B$--resolution of the diagram $D$, one can readily compute that $v_B(D)={\bf q}+1$. Thus, by Lemma [\[lemma:adequate-jones\]](#lemma:adequate-jones){reference-type="ref" reference="lemma:adequate-jones"}, $\alpha_{K_a} = (-1)^{2{\bf q}-{\bf p}}=(-1)^{{\bf p}}$. The total number of edges of ${\mathbb{G}_B}$ is $e_B(D) = {\bf p}+ {\bf q}$, the number of crossings in $D$. Out of this total number, the ${\bf p}$ edges corresponding to the powers of $\sigma_1$ will become identified to $s$ classes of edges in $e'_B$ (with one edge for each $\sigma_1$--twist region. The ${\bf q}$ edges corresponding to the powers of $\sigma_2$ all survive in $e'_B$, except in the special case when ${\bf q}=2$, when a loop of two edges running all the way around the braid counts for only a single reduced edge in $e'_B$. Putting it together, the number of reduced edges will be $e'_B(D)= {\bf q}- \varepsilon_{{\bf q}}+ s$, hence $$\label{eq:beta}
\beta_{K_a} =(-1)^{2{\bf q}- {\bf p}+1} (e'_B - v_B + 1) = (-1)^{{\bf p}+1} (s - \varepsilon_{{\bf q}}).$$

To find $\gamma_{K_a}$, we must calculate the third-to-last coefficient of the Kauffman bracket $\langle D \rangle$, and then multiply by $(-1)^{w(D)} = (-1)^{{\bf q}-{\bf p}}$. Thus $\gamma_{K_a}$ is the third-to-last coefficient of $\langle D \rangle$, which was computed in closed form by Dasbach and Lin [@dasbach-lin:head-tail Theorem 4.1] and ozawa:adequate [@stoimenow:amphichiral Proposition 3.3]. According to their formula, $$\label{eq:gamma}
\gamma_{K_a}\:=\:(-1)^{{\bf p}} \left( \frac{ {\left\vert  \beta_{K_a} \right\vert} ({\left\vert \beta_{K_a} \right\vert}+1)}{2}-\theta+\mu-\tau \right) \!,$$ where $\theta$, $\mu$, and $\tau$ are defined as follows. The quantity $\theta$ is always zero for reduced alternating diagrams; this is because the circles $s_B$ do not nest on the projection plane. The quantity $\mu$ is the number of edges in the reduced graph ${\mathbb{G}'_B}$ whose multiplicity in ${\mathbb{G}_B}$ is greater than one. By the argument preceding equation ([\[eq:beta\]](#eq:beta){reference-type="ref" reference="eq:beta"}), $$\label{eq:mu}
\mu \: = \: \#\{i : p_i > 1 \} + \varepsilon_{{\bf q}}\: = \: s -   \#\{i : p_i = 1 \} + \varepsilon_{{\bf q}}.$$

Finally, the quantity $\tau$ is defined to be number of loops in ${\mathbb{G}'_B}$ that consist of exactly $3$ edges. In our context, one of these loops (surrounding a region of the diagram $D$) typically arises for any $i$ where $q_i= 1$. However, in the special case when $s={\bf q}=2$, two of these regions involve the same triple of vertices in ${\mathbb{G}_B}$, and account for the same loop in ${\mathbb{G}'_B}$. Furthermore, a loop of length $3$ goes all the way around the braid when ${\bf q}= 3$. All together, $$\label{eq:tau}
\tau =  \#\{i : q_i = 1 \} - \delta_{s={\bf q}=2} + \delta_{{\bf q}= 3}.$$

Thus, plugging equations ([\[eq:beta\]](#eq:beta){reference-type="ref" reference="eq:beta"}), ([\[eq:mu\]](#eq:mu){reference-type="ref" reference="eq:mu"}), ([\[eq:tau\]](#eq:tau){reference-type="ref" reference="eq:tau"}) into equation ([\[eq:gamma\]](#eq:gamma){reference-type="ref" reference="eq:gamma"}) gives $$\begin{aligned}
(-1)^{{\bf p}} \gamma_{K_a} &=&
\frac{ (s-\varepsilon_{{\bf q}}) (s-\varepsilon_{{\bf q}}+1)}{2}  +\mu - \tau \notag \\
 &=&
\frac{s^2 + s - 2s \varepsilon_{{\bf q}}}{2}  + s  -     \#\{i : p_i = 1 \}   -    \#\{i : q_i = 1 \}   +    \varepsilon_{{\bf q}}+   \delta_{s={\bf q}=2}   -   \delta_{{\bf q}= 3} \notag \\
 &=&
\frac{s^2 + 3s}{2}   - (s-1)\varepsilon_{{\bf q}}+   \delta_{s={\bf q}=2} -  \#\{i : p_i = 1 \}   -    \#\{i : q_i = 1 \}         -   \delta_{{\bf q}= 3} \notag \\
 &=&
\frac{s^2 + 3s}{2}     -  \#\{i : p_i = 1 \}   -    \#\{i : q_i = 1 \}       -   \delta_{{\bf q}= 3}.
\label{eq:gamma-exact}
\end{aligned}$$ The last equality holds because both $(s-1)\varepsilon_{{\bf q}}$ and $\delta_{s={\bf q}=2}$ must be $0$ for $s \neq 2$, while on the other hand $\delta_{s={\bf q}=2} = \varepsilon_{{\bf q}}$ for $s = 2$. Thus, since all terms of ([\[eq:gamma-exact\]](#eq:gamma-exact){reference-type="ref" reference="eq:gamma-exact"}) after $(s^2+3s)/2$ are non-positive, $(-1)^{{\bf p}} \gamma_{K_a}$ is always bounded above by $(s^2+3s)/2$. This upper bound will be attained whenever $s>1$ and $p_i, q_i >1$ for all $i$, for then all correction terms must be $0$.

For the lower bound on $(-1)^{{\bf p}} \gamma_{K_a}$, observe that each of $\#\{i : p_i = 1 \}$ and $\#\{i : q_i = 1 \}$ is at most $s$. In fact, each of these quantities is $0$ when $s=1$ (by hypothesis). Furthermore, $\#\{i : q_i = 1 \}   +   \delta_{{\bf q}= 3} \leq s$ when $s=2$. Thus $${\setlength{\jot}{1.3ex}
\begin{array}{r c c c c c l}
(-1)^{{\bf p}} \gamma_{K_a}  &\geq &  \dfrac{s^2 + 3s}{2}    -1 &\geq &  1 & \qquad \mbox{when} & s = 1, \\
(-1)^{{\bf p}} \gamma_{K_a}  &\geq &  \dfrac{s^2 + 3s}{2}   - 2s &\geq &  1 & \qquad \mbox{when} & s = 2,\\
(-1)^{{\bf p}} \gamma_{K_a}  &\geq &  \dfrac{s^2 + 3s}{2}   - 2s -1 &\geq &  2 & \qquad \mbox{when} & s \geq 3.
\end{array}}$$ ◻
:::

Let ${\mathbb{Z}}[t, \ t^{-1}]$ denote the ring of Laurent polynomials with integer coefficients and $G(2, t)$ the group of $2\times 2$ matrices with entries in ${\mathbb{Z}}[t, t^{-1}]$. The Burau representation $\psi\colon\thinspace
B_3 \to G(2,t)$ is defined by $$\psi(\sigma_1^{-1}) = \left[\begin{array}{cc}
            -t&1\\0&1\end{array}\right], \quad 
\psi(\sigma_2^{-1}) = \left[\begin{array}{cc}
        1&0\\t&-t\end{array}\right]. 
\label{eqn:burau}$$ See [@birman:book; @jones] for more details.[^1]

For a braid $b\in B_3$, let $\hat {b}$ denote the closure of $b$ and let $e_b$ denote the exponent of $b$. As calculated in [@jones] (the formula is also given and used in the papers [@birman:3braid-jones] and [@kanenobu] where properties of the Jones polynomial of 3--braids are discussed), the Jones polynomial of ${\hat b}$ is given by $$J_{{\hat b}}(t)= (-\sqrt t)^{-e_b}\cdot (t+t^{-1}+ {\rm trace}(\psi
  (b))).
\label{eqn:jones-burau}$$

::: lemma
Suppose that a link $K_b$ is the closure of a generic 3--braid $$b= C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}
\sigma_2^{-q_s},$$

with $p_i, q_i>0$. Let $K_a$ denote the alternating link represented by the closure of the alternating braid $a:=\sigma_1^{p_1}
\sigma_2^{-q_1} \cdots \sigma_1^{p_s} \sigma_2^{-q_s}$. If $J_{K_a}(t)$ and $J_{K_b}(t)$ denote the Jones polynomials of $K_a$ and $K_b$ respectively, then $$J_{{K_b}}(t)= t^{-6k}\, J_{{K_a}}(t)+ (-\sqrt t)^{-e_a}\,
\left(t+t^{-1}\right) \, \left(t^{-3k}-t^{-6k}\right),$$ where $e_a$ is the braid exponent of $a$. []{#lemma:generic label="lemma:generic"}
:::

::: proof
*Proof.* An easy calculation, using equation ([\[eqn:burau\]](#eqn:burau){reference-type="ref" reference="eqn:burau"}), will show that $$\psi(C)=\psi((\sigma_1 \sigma_2 \sigma_1)^{2})=
\left[\begin{array}{cc} t^{-3}&0\\0&t^{-3}\end{array}\right],$$

and thus $${\rm trace}(\psi (b))=t^{-3k}\,  {\rm trace}(\psi (a)).
\label{eqn:trace}$$

The braid exponents $e_b$ and $e_a$ satisfy $e_b=6k + e_a$.

Thus, by equations ([\[eqn:jones-burau\]](#eqn:jones-burau){reference-type="ref" reference="eqn:jones-burau"}) and ([\[eqn:trace\]](#eqn:trace){reference-type="ref" reference="eqn:trace"}), $$J_{{K_b}}(t)= t^{-3k}(-\sqrt t)^{-e_a}\, \left(t+t^{-1}+ t^{-3k}\,
  {\rm trace}(\psi (a))\right),
\label{eqn:jones-Kb}$$ and $$J_{{K_a}}(t)= (-\sqrt t)^{-e_a}\, \left(t+t^{-1}+ {\rm trace}(\psi
  (a))\right). 
\label{eqn:jones-Ka}$$

By eliminating ${\rm trace}(\psi (a))$ from equations ([\[eqn:jones-Kb\]](#eqn:jones-Kb){reference-type="ref" reference="eqn:jones-Kb"}) and ([\[eqn:jones-Ka\]](#eqn:jones-Ka){reference-type="ref" reference="eqn:jones-Ka"}) we obtain $$J_{{K_b}}(t)= t^{-6k}\, J_{{K_a}}(t)+ (-\sqrt t)^{-e_a}\,
\left(t+t^{-1}\right) \, \left(t^{-3k}-t^{-6k}\right),
\label{eqn:lemma-generic}$$ as desired. ◻
:::

We are now ready to estimate certain outer coefficients of the Jones polynomial for any generic closed 3--braid.

::: define
[]{#def:zeta label="def:zeta"} Let $K$ be a link in $S^3$. From the Jones polynomial $J_K(t)$, we define the following quantities. Let $$\zeta_K = \left\{ \begin{array}{r l}
\beta_K, & \mbox{if } {\left\vert \alpha_K \right\vert} = 1 \\
0, & \mbox{otherwise}
\end{array} \right.
\qquad \mbox{and} \qquad
\zeta'_K = \left\{ \begin{array}{r l}
\beta'_K, & \mbox{if } {\left\vert \alpha'_K \right\vert} = 1 \\
0, & \mbox{otherwise.}
\end{array} \right.$$

Note that by Lemma [\[lemma:adequate-jones\]](#lemma:adequate-jones){reference-type="ref" reference="lemma:adequate-jones"}, adequate links will satisfy $\zeta_K = \beta_K$ and $\zeta'_K = \beta'_K$. This definition gives a way to generalize approximately the same quantity.
:::

::: prop
[]{#prop:3-braids label="prop:3-braids"} Let $K_b$ be the closure of a generic 3--braid $b= C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}
\sigma_2^{-q_s},$

with $p_i, q_i>0$. Define $\zeta_{K_b}$ and $\zeta'_{K_b}$ as in Definition [\[def:zeta\]](#def:zeta){reference-type="ref" reference="def:zeta"}. Then $$s-1 \leq  \max \left\{ {\left\vert \zeta_{K_b} \right\vert}, {\left\vert \zeta'_{K_b} \right\vert} \right\} \leq s+1.$$
:::

::: proof
*Proof.* For the majority of this argument, we will work under the hypothesis that ${\bf p}>1$ and ${\bf q}>1$. At the end of the proof, we will consider the (simpler) case when ${\bf p}= 1$ or ${\bf q}= 1$.

So: assume that ${\bf p}>1$ and ${\bf q}>1$, and let $a = \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}$ be the alternating part of $b$. Consider $J_{K_b}(t)$, as expressed as a sum of two terms in equation ([\[eqn:lemma-generic\]](#eqn:lemma-generic){reference-type="ref" reference="eqn:lemma-generic"}). By Lemma [\[lemma:alternating\]](#lemma:alternating){reference-type="ref" reference="lemma:alternating"}, the first term, $t^{-6k}\,J_{K_a}(t)$, is $$\begin{aligned}
  t^{-6k} \, J_{{K_a}}(t) & = 
   (-1)^{{\bf p}} \ t^{(3{\bf q}-{\bf p})/2-6k} +
   (-1)^{{\bf p}+1}(s- \varepsilon_{{\bf q}}) \, t^{(3{\bf q}-{\bf p})/2-6k-1} + \cdots
        \label{eqn:jones-1st} 
 \\
  &  + (-1)^{{\bf q}+1}(s - \varepsilon_{{\bf p}}) \, t^{({\bf q}-3{\bf p})/2-6k+1} +
   (-1)^{{\bf q}} \ t^{({\bf q}-3{\bf p})/2-6k}. \notag
\end{aligned}$$

Meanwhile, the second term on the right hand side of equation ([\[eqn:lemma-generic\]](#eqn:lemma-generic){reference-type="ref" reference="eqn:lemma-generic"}) expands out to $$(-1)^{e_a} \left( t^{-e_a/2-3k +1} +
t^{-e_a/2-3k-1}- t^{-e_a/2-6k+1}-
t^{-e_a/2-6k-1}\right).
\label{eqn:jones-2nd}$$

If $k=0$, then the expression in ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) vanishes, and the link $K_b$ is alternating. Thus $\zeta_{K_b} = \beta_{K_b}$ and $\zeta'_{K_b} = \beta'_{K_b}$, and the desired result is true by Lemma [\[lemma:alternating\]](#lemma:alternating){reference-type="ref" reference="lemma:alternating"}.

Next, suppose that $k \neq 0$. We claim that no generality is lost by assuming that $k > 0$. Otherwise, if $k < 0$, the mirror image $K_d$ of the link $K_b$ can be represented by the braid word $d = C^{-k} \sigma_1^{q_s} \sigma_2^{-p_1} \sigma_1^{q_1} \cdots \sigma_2^{-p_s} ,$ so the power of $C$ will now be positive. The Jones polynomial $J_{K_d}$ can be obtained from $J_{K_b}$ by interchanging $t$ and $t^{-1}$, so $\zeta_{K_b} = \zeta'_{K_d}$ and $\zeta'_{K_b} = \zeta_{K_d}$, with the maximum of the two values unaffected. Thus we may assume $k > 0$.

If $k > 0$, the monomials of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) are listed in order of decreasing powers of $t$, and each monomial has a coefficient of $\pm 1$. Furthermore, we claim that the degree of any term in ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) is strictly higher than the degree of the lowest term in ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}). This is because the last monomial of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) has degree $-e_a/2-6k-1 = ({\bf q}-{\bf p})/2 - 6k -1$, and $$\label{eq:powers}
{\bf p}\geq 2 \qquad \mbox{is equivalent to} \qquad   \frac{{\bf q}-{\bf p}}{2} - 6k -1 \: \geq \: \frac{{\bf q}-3{\bf p}}{2} - 6k +1.$$ Thus the lowest--degree term of $J_{K_b}(t)$ is $(-1)^{{\bf q}} \ t^{({\bf q}-3{\bf p})/2-6k}$, and $\alpha'_{K_b} = (-1)^{{\bf q}}$.

From equation ([\[eq:powers\]](#eq:powers){reference-type="ref" reference="eq:powers"}), we can also conclude that the last monomial of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) only affects the next-to-last monomial of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) if ${\bf p}=2$. When ${\bf p}$ is even, the signs of these two monomials are $(-1)^{{\bf q}+1}$ and $(-1)^{e_a + 1} = (-1)^{{\bf p}- {\bf q}+ 1} = (-1)^{{\bf q}+ 1}$: they have the same sign. Thus when ${\bf p}= 2$, the last monomial of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) will contribute $1$ to $|\beta'_{K_b}|$; when ${\bf p}> 2$, no monomial of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) affects $|\beta'_{K_b}|$ at all. We conclude that when $k >0$, $$\zeta'_{K_b} \: = \: \beta'_{K_a} + (-1)^{{\bf q}+ 1}\varepsilon_{{\bf p}}\: = \: (-1)^{{\bf q}+ 1} (s - \varepsilon_{{\bf p}}+ \varepsilon_{{\bf p}}) \: = \: (-1)^{{\bf q}+ 1} s.$$

Next, consider how the top two terms of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) might interact with the monomials of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}). If the top degree of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) is lower than the top degree of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}), we will have $\alpha_{K_b} = (-1)^{{\bf p}}$ and $\zeta_{K_b} = \beta_{K_b}$ will be off by at most $1$ from $\beta_{K_a}$. In particular, $s-2 \leq {\left\vert \zeta_{K_b} \right\vert} \leq s+1$. If the top degree of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) is higher than the top degree of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) by $2$ or more, we will have $\alpha_{K_b} = (-1)^{e_a}$ and $\zeta_{K_b} = \beta_{K_b} = 0$. If the top degree of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) is higher by exactly $1$, then we will have $\alpha_{K_b} = (-1)^{e_a}$ and $\zeta_{K_b} = \beta_{K_b} = (-1)^{\bf p}$. If the top degree of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) is exactly equal to the top degree of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}), then the two monomials either add or cancel. If the top monomials add, $\alpha_{K_b} = (-1)^{\bf p}\cdot 2$ and $\zeta_{K_b} = 0$ by Definiton [\[def:zeta\]](#def:zeta){reference-type="ref" reference="def:zeta"}. Thus, in all cases when the top monomials of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) and ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) do not cancel, we have $0 \leq {\left\vert \zeta_{K_b} \right\vert} \leq s+1$.

If the top monomials of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) and ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) cancel (which can occur: see Proposition [\[prop:cancelation\]](#prop:cancelation){reference-type="ref" reference="prop:cancelation"}), we have $$\frac{3{\bf q}-{\bf p}}{2}-6k = \frac{-e_a}{2}-3k +1, \quad \mbox{which simplifies to} \quad
{\bf q}= 3k + 1,$$ since $e_a = {\bf p}- {\bf q}$. In particular, it follows that ${\bf q}\geq 4$. Then $\alpha_{K_b} = \beta_{K_a} = (-1)^{{\bf p}+ 1}s$. So, if $s \geq 2$, we have ${\left\vert \alpha_{K_b} \right\vert} \geq 2$, and again $\zeta_{K_b} = 0$ by Definiton [\[def:zeta\]](#def:zeta){reference-type="ref" reference="def:zeta"}. Thus when $s \geq 2$, we get $0 \leq {\left\vert \zeta_{K_b} \right\vert} \leq s+1$ in all cases. Since $|\zeta'_{K_b}|$ is always equal to $s$ if $k>0$, we conclude that $$s-1 \leq  \max \left\{ {\left\vert \zeta_{K_b} \right\vert}, {\left\vert \zeta'_{K_b} \right\vert} \right\} \leq s+1
\qquad \mbox{whenever} \qquad s \geq 2.$$ Note that the lower bound of $s-1$ is only achieved when $k = 0$ and $s = {\bf p}= {\bf q}= 2$, i.e., when $K_b$ is the figure--$8$ knot.

If $s = 1$ and the top monomials of ([\[eqn:jones-1st\]](#eqn:jones-1st){reference-type="ref" reference="eqn:jones-1st"}) and ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}) cancel, then $\alpha_{K_b} = \beta_{K_a} = (-1)^{{\bf p}+ 1}$ and $\zeta_{K_b} = \beta_{K_b} = \gamma_{K_a} + (-1)^{{\bf p}+1}$, where $\gamma_{K_a}$ is the third coefficient of $J_{K_a}(t)$ and $(-1)^{{\bf p}+1}$ comes from the second monomial of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}). By Lemma [\[lemma:alternating\]](#lemma:alternating){reference-type="ref" reference="lemma:alternating"}(c), $${\left\vert \zeta_{K_b} \right\vert} \: = \: {\left\vert \gamma_{K_a} \right\vert} - 1 \: \leq \: \frac{s(s+3)}{2} - 1\: = \: 1.$$ Since we get $0 \leq {\left\vert \zeta_{K_b} \right\vert} \leq s+1$ whenever the top monomials do not cancel, and since $|\zeta'_{K_b}|$ is always equal to $s$ if $k>0$, we conclude that $$s-1 \leq  \max \left\{ {\left\vert \zeta_{K_b} \right\vert}, {\left\vert \zeta'_{K_b} \right\vert} \right\} \leq s+1
\qquad \mbox{whenever} \qquad s = 1 \quad \mbox{and} \quad {\bf p}, {\bf q}\geq 2.$$

To complete the proof, we need to consider the case when ${\bf p}= 1$ or ${\bf q}= 1$, hence $s=1$. Without loss of generality, we may assume that ${\bf p}\geq {\bf q}= 1$ (otherwise, take the mirror image of $K_b$, as above). Then $K_a$ is the $(2,{\bf p})$ torus link. By direct computation (for example, using [@lickbook Theorem 14.13] or [@ck:cyclotomic Proposition 2.1 and Example 3]), it follows that $$J_{K_a}(t) = (-1)^{{\bf p}+1} \left( t^{-({\bf p}-1)/2} + t^{-({\bf p}+3)/2} - t^{-({\bf p}+5)/2}  +  t^{-({\bf p}+7)/2} - \ldots + (-1)^{\bf p}t^{-(3{\bf p}-1)/2} \right).$$ In particular, the second coefficient of $J_{K_a}(t)$ is $0$ and every other coefficient is $\pm 1$. If $k \neq 0$, we may still use Lemma [\[lemma:generic\]](#lemma:generic){reference-type="ref" reference="lemma:generic"} to compute the Jones polynomial $J_{K_b}(t)$. Thus, after multiplying $J_{K_a}(t)$ by $t^{-6k}$ and adding in the four monomials of ([\[eqn:jones-2nd\]](#eqn:jones-2nd){reference-type="ref" reference="eqn:jones-2nd"}), it will follow that every coefficient of $J_{K_b}(t)$ is $0$, $\pm 1$, or $\pm 2$. Thus $$0 \leq  \max \left\{ {\left\vert \zeta_{K_b} \right\vert}, {\left\vert \zeta'_{K_b} \right\vert} \right\} \leq 2
\qquad \mbox{whenever} \qquad  {\bf p}= 1 \quad \mbox{or} \quad {\bf q}= 1,$$ which is exactly what the proposition requires for $s=1$. ◻
:::

[^1]: Our definition of the braid generator $\sigma_i$, depicted in Figure [\[fig:3braid-generators\]](#fig:3braid-generators){reference-type="ref" reference="fig:3braid-generators"}, corresponds to Jones' definition of $\sigma_i^{-1}$ [@jones]. The literature contains many examples of both conventions: compare [@birman:3braid-jones; @burde-zieschang:knots] to [@kanenobu; @murasugi]. Replacing $\sigma_i$ with $\sigma_i^{-1}$ produces the mirror image of a link, and affects the Jones polynomial by replacing $t$ with $t^{-1}$.
