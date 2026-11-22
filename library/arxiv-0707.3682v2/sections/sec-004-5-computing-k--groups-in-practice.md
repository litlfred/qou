---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-004-5-computing-k--groups-in-practice
section_title: "Computing K -groups in practice"
section_number: 5
pages: 23-30
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.959
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
[]{#practical label="practical"}

Let $n \ge 2$. It follows from Theorem [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"} that Zagier's approach as described in Section [\[ksection\]](#ksection){reference-type="ref" reference="ksection"} can be used to obtain at least some part of $\Kn k$. Using the notation introduced in Section [\[ksection\]](#ksection){reference-type="ref" reference="ksection"}, in order to carry this approach out in practice one starts with two sets $S \subseteq S'$ of primes of $\O$ and considers only $[x]_n^\sim$ where $x$ is an $S$-unit and $1-x$ is an $S'$-unit. When we consider several hundred of such $[x]_n^\sim$'s (and avoid using both $[x]_n^\sim$ and $[1/x]_n^\sim$ since $[x]_n + (-1)^n [1/x]_n = 0$ as mentioned in Section [\[ksection\]](#ksection){reference-type="ref" reference="ksection"}) this method is well suited to computer calculations. The only point in Zagier's approach that cannot be carried out algebraically is to determine which elements in $\Ker(\tilde\dd_n)$ are actually in $\Ker(\tilde\dd_n) \cap \Ker(\widetilde P_n)$. This is done using standard methods for finding linear relations between the $\widetilde P_n(\a_j)$'s for a basis $\{\a_j\}$ of $\Ker(\tilde\dd_n)$ with small integral coefficients. Typically, we used about the first 50 decimals after the decimal point of all the polylogarithms of all elements of $k$ involved in the $\a_j$ embedded into $\C$ in all possible ways. The relations that were found this way were then verified to hold up to at least 30 additional decimal places. As a final check, when $\Ker(\dd_n)$ had the same rank as $K_{2n-1}(k)$ the number $q$ in [\[borelq\]](#borelq){reference-type="eqref" reference="borelq"} (but now using the regulator $\widetilde V_n(k)$ for the subgroup of $\Kn k$ we obtained rather than $V_n(k)$; cf. Remark [\[basisremark\]](#basisremark){reference-type="ref" reference="basisremark"}) was computed with a working precision of up to 120 decimals. It turned out that its reciprocal looked rational rather convincingly.

For example, for the cubic field $k = \Q[x]/(x^3 - x^2 - 3 x + 1)$ with discriminant 148, one of the fields used in Example [\[S3computation\]](#S3computation){reference-type="ref" reference="S3computation"}, we find for $\z_k(n) |D_k|^{1/2} / \widetilde V_n(k)$ the values $$\begin{aligned}
{1}
& -1.7531044558071585098612125639152666179693206722 \times 10^{-2}      \qquad (n=3)
\cr
&  -4.1170685884062518549452525064367732455835167754 \times 10^{-9}     \qquad (n=5)
\end{aligned}$$ with reciprocals $$\begin{aligned}
{1}
& -57.041666666666666666666666666666666666666666662            \qquad (n=3)
\cr
& -242891265.59999999999999999999999999999999999998            \qquad (n=5)
\,.
\end{aligned}$$

As the calculation of a basis of $\Kn k$, using the method outlined above, tends to take (substantially) longer when $[k:\Q]$, the absolute value of the discriminant of $k$, or $n$ increase, we describe two straightforward methods to reduce this. They, and most of our arguments below, will rely on Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"}.

::: method
[]{#firstmethod label="firstmethod"} If $k$ is an Abelian extension of $\Q$, hence is contained in a cyclotomic field $k'$, then we can find $\Kn k$ by computing $\Kn k'$ as in Example [\[cyclo\]](#cyclo){reference-type="ref" reference="cyclo"} and applying Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"} $($using Remark [\[equivariance\]](#equivariance){reference-type="ref" reference="equivariance"}$)$.
:::

Since parts (1), (2) and (3) of Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} are known for all idempotents of $E[G]$ to which it applies if $G$ is Abelian by Remark [\[consequencesremark\]](#consequencesremark){reference-type="ref" reference="consequencesremark"} and Proposition [\[abelprop\]](#abelprop){reference-type="ref" reference="abelprop"}, this will not be used for verifying Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}. Instead, in the cases that we shall consider we rely on the following method in order to find the $K$-groups.

::: method
[]{#subfields label="subfields"} Let $k/\Q$ be Galois with Galois group $G$, $E/\Q$ any extension, and $M$ an irreducible $E[G]$-module in $\KnE k$. If $H$ is a subgroup of $G$ with $M^H \ne 0$ then $M \subseteq E[G] \cdot \Kn k^H$. If for every irreducible $M$ we can take $H \ne \{e\}$, then we reduce to finding $\Kn l$ together with the action of $G$ on it inside $\Kn k$ for proper subfields $l$ of $k$.
:::

We now discuss in Examples [\[S3example\]](#S3example){reference-type="ref" reference="S3example"}, [\[D8example\]](#D8example){reference-type="ref" reference="D8example"} and [\[sexticexample\]](#sexticexample){reference-type="ref" reference="sexticexample"} how to use Method [\[subfields\]](#subfields){reference-type="ref" reference="subfields"} for certain Galois extensions $k/\Q$. In the decomposition of $\KnE k$ according to central idempotents $\pi_i$ of $E[G]$ as in Section [\[motivicsection\]](#motivicsection){reference-type="ref" reference="motivicsection"} we concentrate on those primitive central $\pi_i$ for which the action on $E[G]\pi_i$ is not Abelian and describe corresponding primitive idempotents $\pi$ (as in Definition [\[mindef\]](#mindef){reference-type="ref" reference="mindef"}(2)) for later use. Due to restrictions on when we can calculate the numerically (see Section [1](#pLsection){reference-type="ref" reference="pLsection"}) we only consider $k$ that are Abelian over a quadratic subfield. Of course Proposition [\[whenconj\]](#whenconj){reference-type="ref" reference="whenconj"} describes when Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} applies to $\pi$, but we work out the structure of the $K$-groups and the Galois action in more detail.

::: example
[]{#S3example label="S3example"} Let $k/\Q$ be an $S_3$-extension with quadratic subextension $q$. With $E=\Q$ and $\s$ in $G$ of order three, $\pi_1 = (e+\s+\s^2)/3$ and $\pi_2 = 1-\pi_1$ are orthogonal central idempotents with $\pi_2$ primitive (as in Definition [\[mindef\]](#mindef){reference-type="ref" reference="mindef"}(2)). In $\Q[G] = \Q[G] \pi_1  \oplus  \Q[G] \pi_2$ the first summand consists of Abelian representations of $G$ and the last of two copies of the irreducible 2-dimensional representation $V$ of $G$. A corresponding primitive idempotent for $\pi_2$ is $\pi = \pi_2 \pi_H$ for any subgroup $H = \langle \t \rangle$ of $G$ of order 2 where $\pi_H = (e+\t)/2$.

By Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"} we have $\pi_1 \Kn k = \Kn q$ so that $$\label{S3iso}
\Kn k = \Kn q \oplus \pi_2 \Kn k
\,.$$ The last summand is a $\Q[G]$-module isomorphic to $V^{t_n}$ for some $t_n \geq 0$. As $V = \pi V \oplus \t'\pi V$ for any $\t'\ne\t$ of order 2, we find, if $c = k^H$, $$\pi_2 \Kn k = \pi_2 \Kn c \oplus \t' \pi_2 \Kn c$$ again by Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"}. So we reduce to the calculation of $\Kn q$ and $\Kn c$ together with the action of $G$ on the latter.

A dimension count in [\[S3iso\]](#S3iso){reference-type="eqref" reference="S3iso"} using Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} determines $t_n$. We distinguish two cases.

*Case 1.* If $q$ is real then $t_n = 0$ for $n$ even and 2 for $n$ odd.

*Case 2.* If $q$ is imaginary then $t_n = 1$.

Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} applies to $\pi$ when $t_n=2$.
:::

::: example
[]{#D8example label="D8example"} Let $k/\Q$ be a $D_8$-extension where $D_8 = \langle \s,\t | \s^4=\t^2=(\s\t)^2 = e \rangle$. We fix an isomorphism $G = \Gal(k/\Q) \iso D_8$ and use notation as in Figure [1](#D8figure){reference-type="ref" reference="D8figure"}.

<figure id="D8figure">
<p> @!=10pt <span> &amp;&amp;{e}[lld][ld][d][rd][rrd]&amp;&amp; ͡&amp; ^2͡&amp; ^2&amp; ͡&amp; ^3͡ &amp; ,͡^2[lu] [u] [ru] &amp; [u] &amp; ,͡^2[lu] [u] [ru] &amp; &amp;&amp; D_8 [lu][u][ru] &amp;&amp; </span> @!=10pt <span> &amp;&amp; k [lld][ld][d][rd][rrd]&amp;&amp; k_1&amp; k_2 &amp; k_3 &amp; k_4 &amp; k_5 &amp; q_1 [lu] [u] [ru] &amp; q_2 [u] &amp; q_3 [lu] [u] [ru] &amp; &amp;&amp; [lu][u][ru] &amp;&amp; </span> </p>
<figcaption>The subgroups of <span class="math inline"><em>G</em> = <em>D</em><sub>8</sub></span> and their fixed fields in <span class="math inline">$k/\Q$</span>.</figcaption>
</figure>

Then $\Q[G] = \Q[G] \pi_1 \oplus  \Q[G] \pi_2$ where $\pi_1 = (1+\s^2)/2$ and $\pi_2 = 1-\pi_1$ are orthogonal central idempotents. The first term is an Abelian representation of $G$ and the second as a $\Q[G]$-module is isomorphic to $V^2$ for $V$ the irreducible 2-dimensional representation of $G$ over $\Q$. Then $\pi_2$ is a primitive central idempotent and $\pi = \pi_2 \pi_H$ a corresponding primitive idempotent if we let $H = \langle\t \rangle$ and $\pi_H = (1+\t)/2$.

Since $\pi_1 \Kn k = \Kn k_3$ by Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"}, for $\Kn k$ we find $$\label{D8iso}
\Kn k =  \Kn k_3 \oplus \pi_2 \Kn k$$ with the second term a $\Q[G]$-module isomorphic with $V^{t_n}$ for some $t_n \geq 0$. If $\t'$ in $G$ has order two and does not commute with $\t$ then $V = \pi V \oplus \t'\pi V$, so by Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"} we obtain $$\Kn k =  \Kn k_3 \oplus  \pi_2 \Kn k_1 \oplus \t' \pi_2 \Kn k_1$$ and we reduce to the calculation of $\Kn k_3$ and $\Kn k_1$ together with the action of $G$ on the latter.

We can find $t_n$ by counting dimensions in [\[D8iso\]](#D8iso){reference-type="eqref" reference="D8iso"}, and distinguish three cases.

*Case 1.* For $k_3$ and $k$ totally real $t_n =0$ for $n$ even and $t_n=2$ for $n$ odd.

*Case 2.* For $k_3$ totally real but $k$ not $t_n=2$ for $n$ even and $t_n=0$ for $n$ odd.

*Case 3.* For $k_3$ not totally real $t_n=1$.

Again Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} applies to $\pi$ when $t_n = 2$.
:::

::: example
[]{#sexticexample label="sexticexample"} Let $k/\Q$ be an $S_3 \times \Z/3\Z$-extension, identify $G = \Gal(k/\Q)$ and $S_3 \times \Z/3\Z$ via a fixed isomorphism, and choose a generator $\s$ of $A_3 \subset S_3$. Let $q$ be the quadratic subfield of $k$, $s'$ the fixed field of $A_3 \times \{0\}$, $s''$ the fixed field of $\{e\} \times \Z/3\Z$ and $s_i$ for $i=1$, 2 the fixed field of $H_i = \langle (\s,i) \rangle$.

If $E$ is an extension of $\Q$ that contains a primitive third root of unity $\z_3$ then $$\label{sexticEGdecomp}
\begin{aligned}
   E[G] & = E[G] \pi_1 \oplus E[G] \pi_2 \oplus E[G] \pi_3 \oplus E[G] \pi_4
\cr
        & \iso E[\Z/6\Z] \oplus W_1^2 \oplus W_{\z_3}^2 \oplus W_{\z_3^2}^2 
\end{aligned}$$ where $$\begin{aligned}
\pi_1 & = ((e,0) + (\s,0) + (\s^2,0))/3 
\cr
\pi_2 & = (1-\pi_1)((e,0)+(e,1)+(e,2))/3
\cr
\pi_3 & = (1-\pi_1)((e,0)+\z_3^2(e,1)+\z_3(e,2))/3
\cr
\pi_4 & = (1-\pi_1)((e,0)+\z_3(e,1)+\z_3^2(e,2))/3 
\end{aligned}$$ are orthogonal central idempotents of $E[G]$ satisfying $\pi_1 + \pi_2 + \pi_3 + \pi_4 = (e,0)$, and $W_a$ is the irreducible representation of $G$ given by $(\r,m)(v) = a^m \r(v)$ for $v$ in the irreducible 2-dimensional representation of $S_3$. With $\pi_{H_i} = \frac13 \sum_{h \in H_i} h$, a primitive idempotent corresponding to the primitive central idempotent $\pi_j$ ($j=3$, 4) is $\pi = \pi_j \pi_{H_i}$.

Using Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"} for $A_3 \times \{0\}$ and $\{e\} \times \Z/3\Z$ we see that $$\begin{aligned}
\KnE k & = \pi_1 \KnE k \oplus \pi_2 \KnE k \oplus \pi_3 \KnE k \oplus \pi_4 \KnE k 
\cr
      & = \KnE s' \oplus (1-\pi_1) \KnE s'' \oplus \pi_3 \KnE k \oplus \pi_4 \KnE k 
\,.
\end{aligned}$$ Because $W_a = W_a^{H_1} \oplus W_a^{H_2}$ when $a \ne 1$ we have $$\pi_j \KnE k = \pi_j \KnE s_1 \oplus \pi_j \KnE s_2 
\qquad (j=3, 4)$$ so that we reduce to the calculation of $\Kn s$ for the sextic subfields $s$ of $k$, together with the action of $G$ when $s = s''$, $s_1$ or $s_2$.

We have $\pi_3 \KnE k \iso W_{\z_3}^{t_n}$ and $\pi_4 \KnE k \iso W_{\z_3^2}^{t_n}$ for the same $t_n$ as one sees by taking $E = \Q(\z_3)$ and considering the obvious action of $\Gal(E/\Q)$ on $E[G]$. Since the dimension of $(1-\pi_1) \KnE s''$ was obtained in Example [\[S3example\]](#S3example){reference-type="ref" reference="S3example"} we get the following results for $t_n$.

*Case 1.* For $q$ real $t_n = 0$ when $n$ is even and $t_n=2$ when $n$ is odd.

*Case 2.* For $q$ imaginary $t_n = 1$.

Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} applies to $\pi$ corresponding to $\pi_j$ ($j=3,$ 4) when $t_n=2$.
:::

We finish this section with a result that was promised in Remark [\[newrem\]](#newrem){reference-type="ref" reference="newrem"}(1). Note that the assumption $\dim_E(E[G]\pi) = \dim_E(\pi \KnE k )$ is not needed here: we consider the regulator map with values in $\pi(\oplus_{\t:k\to\C} E\tensor \R(n-1))^+$ obtained from [\[Bregulator\]](#Bregulator){reference-type="eqref" reference="Bregulator"}, and use Beilinson's regulator $R_\Bei$ comparing $E$-structures as in Remark [\[BBmotiverem\]](#BBmotiverem){reference-type="ref" reference="BBmotiverem"}. Beilinson's conjecture [@bei85 Conjecture 3.4] states that the order of vanishing at $s=1-n$ of $\L s {\chi_\pi^\vee\tensor\id} {\Q}$ should be $\dim_E(\pi \KnE k )$ and that the first non-vanishing coefficient at $s=1-n$ equals $$\Lsharp {1-n} {\chi_\pi^\vee\tensor\id} {\Q} = e R_\Bei$$ for some $e$ in $E^*$.

::: proposition
[]{#grossprop label="grossprop"} Let $k$ be a $G=S_3$-extension $($resp. $G= D_8$-extension$)$ of $\Q$, and let $n \ge 2$. Then this conjecture holds for any primitive idempotent $\pi$ corresponding to $\pi_2$ in Example [\[S3example\]](#S3example){reference-type="ref" reference="S3example"} $($resp. Example [\[D8example\]](#D8example){reference-type="ref" reference="D8example"}$)$.
:::

::: proof
*Proof.* Clearly it suffices to prove this when $E=\Q$. If $G=S_3$ then by Remark [\[consequencesremark\]](#consequencesremark){reference-type="ref" reference="consequencesremark"}(3) we may assume $\pi_H = \pi_1 \pi_H + \pi$ with $\pi_1 \pi_H$ and $\pi = \pi_2 \pi_H$ orthogonal idempotents, where we use notation as in Example [\[S3example\]](#S3example){reference-type="ref" reference="S3example"}. The conjecture for $\pi_H$ follows from Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} for $c = k^H$ by the arguments of Remark [\[sameconj\]](#sameconj){reference-type="ref" reference="sameconj"} and the functional equation [\[oldfuneq\]](#oldfuneq){reference-type="eqref" reference="oldfuneq"} of $\z_c(s)$. Similarly, it holds for $\pi_1 \pi_H = \frac16 \sum_{g \in G} g$, where it corresponds to that theorem for $k^G = \Q$, and it follows that it must hold for $\pi$ as well. If $G=D_8$ the argument is identical, using Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} for $k_1$ and $q_1$. ◻
:::

# Computing  {#pLsection}

We briefly sketch the method used to compute values of $L$-functions of 1-dimensional Artin characters. Values of of characters of higher dimension can then be deduced using [\[artinLp\]](#artinLp){reference-type="eqref" reference="artinLp"}. The method we employ is somewhat similar to, but more technical than the construction in [@Colm88], and generalizes the one used in [@Sol-Rob] to compute values of $p$-adic $L$-functions of real quadratic fields at $s = 1$. Note that several modifications are necessary compared to [@Colm88] since the construction there is for partial $\z$-functions of the ray class modulo $p$ whereas we need to work with partial $\z$-functions of arbitrary class groups. Also, we need to replace $p = 2$ in a certain number of results by $q = 4$. We leave it to the careful reader to check that these changes are indeed possible, or refer to the forthcoming article [@Rob06] where the details of the actual method used will be given.

Let $k$ be a totally real number field and let $d=[k:\Q]$. Let $\chi$ be a $\Qpbar$-valued 1-dimensional Artin character of $\Gal(\kbar/k)$. As in Section [\[conjecturesection\]](#conjecturesection){reference-type="ref" reference="conjecturesection"}, we let $q = p$ if $p$ is odd, and $q = 4$ if $p = 2$.

By class field theory, $\chi$ can be viewed as a character of a suitable ray class group of $k$. We denote by $\mathfrak{f}$ the conductor of $\chi$, which is an integral ideal of $k$, and we let $\mathfrak{g}$ be the modulus with infinite part $\mathfrak{g}_\infty$ consisting of all infinite places of $k$, and finite part $\mathfrak{g}_0$ equal to the least common multiple of $\mathfrak{f}$ and $q$. Let $\mathfrak{a}_1, \dots, \mathfrak{a}_h$ be representatives of the classes of the ray class group of $k$ modulo $\mathfrak{g}$, and let $\zeta_{\mathfrak{a}_i}(s)$, $i = 1, \dots,h$, be the corresponding partial $\z$-functions. According to [@Neu99 Chapter VII, p.526] we have, for any isomorphism $\sigma:\Qpbar \to \C$, $$\sum_{i=1}^h \s\circ\chi(\mathfrak{a}_i) \zeta_{\mathfrak{a}_i}(s) 
=
\Eul_p(s,\s\circ\chi,k) \L s {\s\circ\chi} k 
\,.$$ Since all $\zeta_{\mathfrak{a}_i}(m)$ are rational for integers $m \leq 0$ by loc. cit. Chapter VII, Corollary 9.9, we may identify them with $\sigma^{-1}(\zeta_{\mathfrak{a}_i}(m))$ in $\Qp$. Thus for such $m$ we have $$\label{partialzeta}
\sum_{i=1}^h  \chi(\mathfrak{a}_i) \zeta_{\mathfrak{a}_i}(m) 
= 
\Eul^\ast_p(m, \chi, k) L^\ast(m, \chi, k)$$ where $L^\ast(m, \chi, k)$ and $\Eul^\ast_p(m, \chi, k)$ are as in [\[sigmaindependence\]](#sigmaindependence){reference-type="eqref" reference="sigmaindependence"} and [\[sigmaeuler\]](#sigmaeuler){reference-type="eqref" reference="sigmaeuler"}.

Now let $\beta\ne1$ in $\mathcal{O}_k$ be such that

1.  $\beta \equiv 1 \pmod{\mathfrak{g}_0}$ and $v(\beta) > 0$ for every infinite place $v$ of $k$;

2.  $\O/(\beta) \simeq \Z/b\Z$, where $b = \mathcal{N}(\beta)$ is the norm of the principal ideal $(\beta)$.

Scaling the measures obtained in [@Colm88 Lemme 4.4] for the $\mathfrak{a}_i$ we obtain $\Qp$-valued measures $\widetilde\lambda_i$ ($i=1,\dots,d$) on $\Zp^d$, depending on $\beta$ and $\mathfrak{a}_i$, such that for all integers $m\le0$, $$(b^{m-1}-1) \zeta_{\mathfrak{a}_i}(m) = (-1)^{dm}
\mathcal{N}(\mathfrak{a}_i)^{-m} \int (x_1\cdots x_d)^{-m} \, d\widetilde\lambda_i
\,.$$ The proof of Lemma 4.3 of loc. cit. shows, contrary to the statement of that lemma, that the measures $\widetilde\lambda_i$ are supported on $(-1+q\Zp)^d$. Therefore pulling back over multiplication by $-1$ on $\Zp^d$ we obtain measures $\lambda_i$ on $\Zp^d$, supported on $(1+q\Zp)^d$, such that, for the same $m$, $$\label{mnonpositive}
(b^{m-1}-1) \zeta_{\mathfrak{a}_i}(m) = 
\mathcal{N}(\mathfrak{a}_i)^{-m} \int (x_1\cdots x_d)^{-m} \, d\lambda_i
\,.$$

For a fixed $x$ in $1 + q\Zp$ the function $s \mapsto x^s$ is defined and analytic on $\Zp$. Since, in general, $\mathcal{N}(\mathfrak{a}_i)$ will not be congruent to $1$ modulo $q$, we do the following. For any integer $l$ and any integral ideal $\mathfrak{a}$ of $k$ that is coprime to $p$, the function $s \mapsto \omega_p(\mathfrak{a})^l \langle
\mathcal{N}\mathfrak{a} \rangle^{-s}$ is an analytic $\Zp$-valued function on $\Zp$, whose value equals $\mathcal{N}(\mathfrak{a})^{-m}$ at any integer $m$ with $m + l \equiv 0 \pmod{\varphi(q)}$. We define the $p$-adic partial $\zeta$-function of the class of $\mathfrak{a}_i$ by mapping $s$ in $\Zp \setminus \{1\}$ to $$\zeta_{p, \mathfrak{a}_i}(s) = 
  \left(b^{s-1} - 1\right)^{-1}
  \langle \mathcal{N}(\mathfrak{a}_i) \rangle^{-s} 
  \pint (x_1 \cdots x_d)^{-s} \, d\lambda_i \,,$$ where $'$ indicates that we restricted the domain of integration to $(1+q\Zp)^d$.

Let $\Psi_i$ be the function defined by the above integral, that is, for $s$ in $\Zp$, $$\Psi_i(s) = \pint (x_1 \cdots x_d)^{-s} \, d\lambda_i\,.$$ For $a$ in $\Zp$ with $|a - 1|_p \leq q^{-1}$, and $s$ in $\Zp$, one can write $a^{-s} =
\exp_p(-s \log_p(a))$, where $\exp_p$ and $\log_p$ are the exponential and logarithm functions respectively; and thus the function $s
\mapsto a^{-s}$ can be expressed as a power series with coefficients in $\Zp$, where the coefficient of $s^m$ has absolute value at most $q^{-m}p^{m/(p-1)}$. Developing $(x_1\cdots x_d)^{-s}$ in this way as a power series of $s$ and using the fact that the measures $\lambda_i$ have bounded norm by [@Colm88 Lemme 4.2 bis], we see that $\Psi_i(s)$ can also be expressed as a power series in $\Qp[[s]]$ where the absolute value of the coefficient of $s^m$ is at most $C_i q^{-m}p^{m/(p-1)}$ for some $C_i>0$. In the same way, the function $s \mapsto \langle \mathcal{N}(\mathfrak{a}_i) \rangle^{-s}$ can be expressed as a power series in $\Zp[[s]]$ whose coefficients satisfy the same bounds. Similarly, since the only solution for $s$ of $b^{s-1} = 1$ with $|s| < q p^{-1/(p-1)}$ is $s = 1$, it follows from the Weierstrass preparation theorem that the function $s \mapsto b^{s-1}-1$ can be expressed as the product of a power of $p$, the polynomial $s-1$, and an invertible power series in $\Zp[[s]]$ with the absolute value of the coefficient of $s^m$ bounded by $q^{-m} p^{m/(p-1)}$. Therefore $\zeta_{p,\mathfrak{a}_i}(s)$ can be expressed as the quotient of a power series in $\Qp[[s]]$ with the absolute value of the coefficient of $s^m$ bounded by $C_i' q^{-m} p^{m/(p-1)}$ with $C_i'>0$, and $s-1$.

If we define $p$-adic functions of $s$, $$\label{merpL}
 L_p^{(l)}(s, \chi, k) =
\sum_{i=1}^h   \omega_p(\mathfrak{a}_i)^l \chi(\mathfrak{a}_i) \zeta_{p, \mathfrak{a}_i}(s) \,
\qquad (l \text{ modulo } \phi(q))
\,,$$ then it follows from [\[partialzeta\]](#partialzeta){reference-type="eqref" reference="partialzeta"}, [\[mnonpositive\]](#mnonpositive){reference-type="eqref" reference="mnonpositive"}, and the equality $\zeta_{p,\mathfrak{a}_i}(m) = \omega_p(\mathfrak{a}_i)^m \zeta_{\mathfrak{a}_i}(m)$ for any integer $m 
\le 0$, that $$\label{interpol1}
 L_p^{(l)}(m, \chi, k) = \Eul^\ast_p(m, \chi, k) L^\ast(m, \chi, k)$$ for all non-positive $m$ such that $l + m \equiv 0$ modulo $\varphi(q)$. In particular, the $p$-adic $L$-function of $\chi$ is given by $\Lp p s {\chi} k = L_p^{(-1)}(s, \chi, k)$. Moreover, its residue at $s=1$ is zero if $\chi$ is non-trivial because the functions $\omega_p(\mathfrak{a}_i)^{-1}\z_{p,\mathfrak{a}_i}(s)$ all have the same residue there by [@Colm88 Corollaire on page 388].

The estimates on the coefficients of the power series expansions above imply the claims in Theorem [\[padicLfunction\]](#padicLfunction){reference-type="ref" reference="padicLfunction"}(1). Through the Weierstrass preparation theorem they also imply that the function in [\[artinLp\]](#artinLp){reference-type="eqref" reference="artinLp"} can be written as the quotient of a power series in $\Qp(\chi)[[s]]$ that converges for $s$ in $\Cp$ with $|s| < q p^{-1/(p-1)}$, and a polynomial in $\Qp(\chi)[s]$.

We note in passing that if $l$ is any integer then $$\Lp p s {\chi\omega_p^l} k 
=
 \sum_{i=1}^h \omega_p(\mathfrak{a}_i)^{l-1} \chi(\mathfrak{a}_i)  \zeta_{p, \mathfrak{a}_i}(s)
=
L_p^{(l-1)}(s, \chi, k)
\,,$$ so that we obtain from [\[interpol1\]](#interpol1){reference-type="eqref" reference="interpol1"} that $$\Lp p m {\chi\omega_p^l} k = \Eul^\ast_p(m, \chi, k) L^\ast(m, \chi, k)$$ for all $m\le0$ with $l + m \equiv 1$ modulo $\varphi(q)$, as stated in Remark [\[interpolrem\]](#interpolrem){reference-type="ref" reference="interpolrem"}.

In order to compute $L(s, \chi, k)$ for a fixed $s$ in $\Zp$, it suffices to compute $\zeta_{p, \mathfrak{a}_i}(s)$, for which one mainly has to compute the $\Psi_i(s)$. The measures $\lambda_i$ can be represented as power series in $d$ variables, $$F_i(w_1, \dots, w_d) = \sum_{n_1, \dots, n_d \geq 0} a_{i, n_1, \dots, n_d} w_1^{n_1} \cdots w_d^{n_d} \,,$$ with (bounded) coefficients $$a_{i, n_1, \dots, n_d} = \int {x_1 \choose n_1} \cdots {x_d \choose n_d} d \lambda_i$$ that can be computed using Shintani's method [@Shin76], which is practical for calculations if the base field $k$ is $\Q$ or real quadratic. On the other hand, the function $h$ on $\Zp$ defined by $$x \mapsto
\begin{cases}
  x^{-s} & \text{ if } x \text{ is in } 1+q\Zp, 
\\
  0 & \text{otherwise},
\end{cases}$$ is continuous and thus admits a Mahler expansion $\sum_{n \geq 0} c_{s, n} \binom{x}{n}$, where the coefficients satisfy $c_{s, n} \to 0$ when $n \to \infty$ and can be easily computed recursively. Then we have $$\Psi_i(s)
=
\int  h(x_1) \cdots h(x_d) \, d\lambda_i 
=
\sum_{n_1, \dots, n_d \geq 0} a_{i, n_1, \dots, n_d} c_{s,
  n_1} \cdots c_{s, n_d} \,.$$ Thus, by computing enough terms in the above sum, we can get a good approximation of the integral, and therefore, putting everything together, of the $p$-adic $L$-function.

In order to apply this we make [\[brauerinduction\]](#brauerinduction){reference-type="eqref" reference="brauerinduction"} explicit in the cases we are interested in, writing of representations for the of the corresponding characters. In particular, we write the classical of the irreducible 2-dimensional representations of $S_3$ and $D_8$ in Examples [\[S3example\]](#S3example){reference-type="ref" reference="S3example"} and [\[D8example\]](#D8example){reference-type="ref" reference="D8example"}, and the irreducible 2-dimensional representations $W_a$ with $a \ne 1$ of $S_3 \times \Z/3\Z$ in Example [\[sexticexample\]](#sexticexample){reference-type="ref" reference="sexticexample"}, as the of Abelian characters over quadratic fields. For later use we also note how to write some of them in terms of $\z$-functions of certain fields.

We take the field of coefficients $E$ to be $\C$ in the remainder of this section, and denote the trivial 1-dimensional representation of any group $G$ by $1_G$.

::: example
[]{#S3L label="S3L"} Let $\Alt_{S_3}$ be the 1-dimensional representation of $S_3$ through the sign character, and $V$ the irreducible 2-dimensional representation. Since $$\Ind A_3 S_3 \circ \Ind \{e\} A_3 (1_{\{e\}})  \iso \Ind \{e\} S_3 (1_{\{e\}}) \iso 1_{S_3} \oplus \Alt_{S_3} \oplus V^2$$ and $\Ind A_3 S_3 (1_{A_3}) \iso 1_{S_3} \oplus \Alt_{S_3}$ it follows that $\Ind A_3 S_3 (V') \iso V$ for either non-trivial 1-dimensional representation $V'$ of $A_3$. Applying this to the situation of Example [\[S3example\]](#S3example){reference-type="ref" reference="S3example"} we see that $\L s  V {\Q} = \L s V' q$. Similarly, if $H$ is any subgroup of $S_3$ of order 2, then $\Ind H S_3 (1_H) \iso 1_{S_3} \oplus V$. In the situation of Example [\[S3example\]](#S3example){reference-type="ref" reference="S3example"} this means that $\z_{c}(s) = \z_{\Q}(s) \L s V {\Q}$.
:::

::: example
[]{#D8L label="D8L"} If $D_8$ is as in Example [\[D8example\]](#D8example){reference-type="ref" reference="D8example"}, $\V a b$ for $a,b=\pm1$ the 1-dimensional representation of $D_8$ where $\s$ acts as multiplication by $a$ and $\t$ by $b$, and $V$ the irreducible 2-dimensional representation, then for any subgroup $H$ $$\Ind H D_8 \circ \Ind {\{e\}} H (1_{\{e\}}) \iso (\oplus_{a,b=\pm1} \V a b ) \oplus V^2
\,.$$ If we take $H = \langle \t, \s^2 \rangle$ then $\Ind {\{e\}} H (1_{\{e\}}) \iso \oplus_{a,b=\pm1} \W a b$ with $\W a b$ the 1-dimensional representation of $H$ where $\s^2$ acts as multiplication by $a$ and $\t$ by $b$. Because $\Ind H D_8 (\W 1 b ) \iso \oplus_{a=\pm1} \V a b$ we have $\Ind H D_8 (\W -1 1 ) \iso \Ind H D_8 (\W -1 -1 ) \iso V$, so with notation as in Figure [1](#D8figure){reference-type="ref" reference="D8figure"} we get $\L s V {\Q}  = \L s {\W -1 1 } q_1 = \L s {\W -1 -1 } q_1$.

Similarly, $\Ind {\langle\t\rangle} D_8 (1_{\langle\t\rangle}) \iso ( \oplus_{a=\pm1} V_{a,1} ) \oplus V$ so that $\z_{k_1}(s) = \z_{q_1}(s) \L s V {\Q}$ as well.
:::

::: remark
If $H=\langle\s\rangle$ in Example [\[D8L\]](#D8L){reference-type="ref" reference="D8L"} then $\Ind \{e\} H (1_{\{e\}}) \iso \oplus_{m=1}^4 U_{i^m}$ with $U_a$ the 1-dimensional representation of $\langle\s\rangle$ where $\s$ acts as multiplication by $a$. Now $\Ind H D_8 (U_a) \iso \V a 1 \oplus \V a -1$ when $a = \pm 1$ so that $\Ind H D_8 (U_a) \iso V$ when $a \ne \pm 1$, and in Example [\[D8example\]](#D8example){reference-type="ref" reference="D8example"} we also have $\L s V {\Q}  = \L s U_i q_2 = \L s U_{-i} q_2$.
:::

::: example
[]{#sexticL label="sexticL"} If $G = S_3 \times \Z/3\Z$ and $H = A_3 \times \Z/3\Z$ then $$\Ind H G \circ \Ind {\{(e,0)\}} H (1_{\{(e,0)\}})
\iso W \oplus W_1^2 \oplus W_{\z_3}^2 \oplus W_{\z_3^2}^2$$ with $W$ the direct sum of the 1-dimensional representations of $G$ and the $W_a$ as in Example [\[sexticexample\]](#sexticexample){reference-type="ref" reference="sexticexample"}. Write $\Ind {\{(e,0)\}} H (1_{\{(e,0)\}}) \iso \oplus_{a,b} V_{a,b}$ where, for $a$ and $b$ cubic roots of unity, $V_{a,b}$ is the 1-dimensional representation of $H$ on which $(\s^m,n)$ acts as multiplication by $a^m b^n$. Since $\Ind H G (\oplus_b V_{1,b}) \iso W$ we find by considering the action of $(e,1)$ that $\Ind H G (V_{a,b}) \iso W_b$ when $a \ne 1$. In particular, in the notation of Example [\[sexticexample\]](#sexticexample){reference-type="ref" reference="sexticexample"}, we have $\L s W_b {\Q} = \L s V_{a,b} q$ since $q = k^H$.

It is easy to see that the coefficients of $p^{-s}$ in the Euler factors of $\L s W_{\z_3} {\Q}$ and $\L s W_{\z_3^2} {\Q}$ are conjugate, but since not all of them can be real it is not possible to express those functions in terms of $\z$-functions of subfields of $k$.
:::
