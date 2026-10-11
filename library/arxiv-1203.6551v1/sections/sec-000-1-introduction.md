---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-13
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N (v) of orientable hyperbolic 3-manifolds with any given volum e v."
text_source: latex
latex_prose_ratio: 0.673
latex_coverage_ratio: 0.982
---
Thurston and Jørgensen (see [@Th]) showed that the set of volumes of finite volume orientable complete hyperbolic $3$-manifolds is a closed, non-discrete, well ordered subset of $\mathbb{R}_{>0}$ of order type $\omega^\omega$. Further, the number $N(v)$ of complete orientable hyperbolic $3$-manifolds of volume $v$ is finite for all $v\in \mathbb{R}_{>0}$. In this paper we study how $N(v)$ varies with $v$.

There has been much work on determining the lowest volumes in various classes of hyperbolic 3-manifolds. The work of Gabai-Meyerhoff-Milley ([@GMM1; @GMM2; @M]) shows that the Weeks manifold with volume $v_1 = 0.9427 \ldots$ is the unique orientable hyperbolic 3-manifold of lowest volume, so that $N(v_1)=1$. Prior to our work, this was the only known exact value for $N(v)$.

It is also interesting to look at the number of hyperbolic 3-manifolds of a given volume in various special classes. For example, we could study the numbers $N_C (v)$, $N_A(v)$, $N_L(v)$, $N_G(v)$ of orientable hyperbolic 3-manifolds of volume $v$ that are cusped, arithmetic, link complements, or with geodesic boundary, respectively.

The work of Cao-Meyerhoff [@CM] shows there are precisely two orientable cusped hyperbolic 3-manifolds of lowest volume $v_\omega \approx 2.029883\ldots$, the figure eight knot complement and its sister (obtained by (-5,1) surgery on the Whitehead link complement). (See Figure [1](#fig8_fig8sister){reference-type="ref" reference="fig8_fig8sister"}.)

<figure id="fig8_fig8sister">
<p><embed src="fig8.eps" /> <embed src="fig8sister_new.eps" /></p>
<figcaption>The figure eight knot and its sister, with complements denoted <span class="math inline"><em>m</em>004</span> and <span class="math inline"><em>m</em>003</span> respectively in SnapPea notation.</figcaption>
</figure>

Gabai-Meyerhoff-Milley [@GMM1] determined the first 10 low volume orientable cusped hyperbolic 3-manifolds. This shows that the next 4 limit volumes are: $$v_{2\omega} = 2.568970\ldots, v_{3\omega}=2.666744\ldots ,
v_{4\omega}= 2.781833\ldots, v_{5\omega} = 2.828122\ldots$$ and that $N_C(v_\omega) = 2 ,  N_C(v_{2\omega})=2,  N_C(v_{3\omega})=2, 
N_C(v_{4\omega})=1, N_C(v_{5\omega})=3.$

The work of Agol [@agol_2cusp] shows that there are exactly two orientable 2-cusped hyperbolic 3-manifolds of lowest volume $v_{\omega^2} = 3.663862\ldots$, namely the Whitehead link complement and the $(-2,3,8)$-pretzel link complement. (See Figure [2](#fig.WL_WS){reference-type="ref" reference="fig.WL_WS"}.)

<figure id="fig.WL_WS">
<p><embed src="Whitehead.eps" /> <embed src="p-238.eps" /></p>
<figcaption>The Whitehead link and the <span class="math inline">(−2,3,8)</span>-pretzel link, with complements <span class="math inline"><em>m</em>129</span> and <span class="math inline"><em>m</em>125</span> in SnapPea notation.</figcaption>
</figure>

Chinburg-Friedman-Jones-Reid [@CFJR] showed that the Weeks manifold and the Meyerhoff manifold are the unique arithmetic hyperbolic 3-manifolds of lowest volume; hence $N_A(0.942707\ldots) = 1$ and $N_A(0.981368\ldots) = 1$.

Kojima and Miyamoto [@KojMiy; @miyamoto] showed the lowest volume for a compact hyperbolic 3-manifold with geodesic boundary is $6.451990\ldots$, and Fujii [@Fu] showed that there are exactly 8 such manifolds with this volume.

The graphs in Figures [3](#closed_cusped_vols){reference-type="ref" reference="closed_cusped_vols"} and [4](#cusped_vols){reference-type="ref" reference="cusped_vols"} below show the frequencies of volumes arising from the manifolds contained in the Callahan-Hildebrand-Weeks census of cusped hyperbolic 3-manifolds (see [@CaHiWe]), and the Hodgson-Weeks census of closed hyperbolic 3-manifolds (see [@HW]). These give *lower bounds* on $N(v)$, but note that infinitely many manifolds are definitely missing in these pictures. Nevertheless, the results suggest that there are often very few manifolds with any given volume.

![Frequencies of volumes of hyperbolic 3-manifolds in the closed and cusped censuses.](vol_cusped_closed_list.eps){#closed_cusped_vols}

![Frequencies of volumes of hyperbolic 3-manifolds in the cusped census.](vol_cusped_list.eps){#cusped_vols}

The first main result of this paper (Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}) shows that there is an infinite sequence of closed hyperbolic 3-manifolds determined by their volumes, obtained by Dehn fillings on the figure eight knot complement. Hence $N(x_i)=1$ for an infinite sequence of volumes $x_i$ converging to $v_\omega$ from below.

The proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"} uses the asymptotic formula of Neumann-Zagier [@NZ] for the change in volume during hyperbolic Dehn filling and a study of the quadratic form giving the squares of lengths of closed geodesics on a horospherical torus cusp cross section, together with some elementary number theory.

Our second major result (Theorem [\[cusped_unique\]](#cusped_unique){reference-type="ref" reference="cusped_unique"}) shows that there is an infinite sequence of 1-cusped hyperbolic 3-manifolds determined by their volumes amongst orientable cusped hyperbolic 3-manifolds. These manifolds are obtained by Dehn fillings on one cusp of the $(-2,3,8)$-pretzel link complement. Hence $N_C(y_i)=1$ for an infinite sequence of volumes $y_i$ converging to $v_{\omega^2}$ from below.

The proof of Theorem [\[cusped_unique\]](#cusped_unique){reference-type="ref" reference="cusped_unique"} is similar to the proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}, but there are some additional complications that require us to study higher order terms in the Neumann-Zagier asymptotic formula.

Another obvious feature of the graphs in Figures [3](#closed_cusped_vols){reference-type="ref" reference="closed_cusped_vols"} and [4](#cusped_vols){reference-type="ref" reference="cusped_vols"} is that there are special values of $v$ for which $N(v)$ is particularly large. So it is natural to ask how fast $N(v)$ can grow with $v$.

If we fix a natural number $n$, then Wielenberg [@Wie] showed that there exists $v$ such that $N(v)>n$, and Zimmerman [@Zim] constructed $n$ distinct closed hyperbolic $3$-manifolds which share the same volume. In both results, the number of manifolds of volume $v$ constructed was at most linear in $v$.

More generally, by considering covering spaces of a fixed non-arithmetic hyperbolic 3-manifold whose fundamental group surjects onto a free group of rank 2, it is possible to find sequences of volumes $x_i \to \infty$ and a constant $c >0$ such that $N(x_i) > x_i^{c \,x_i}$ for all $i$. This argument, known to Thurston and Lubotzky, can be found in [@carlip pp2633-2634] or [@BGLM p1162].

Recent work of Belolipetsky-Gelander-Lubotzky-Shalev [@BGLS] gives very precise upper and lower bounds on the number $N_A(v)$ of *arithmetic* hyperbolic 3-manifolds of volume $v$: there exist constants $a,b>0$ such that for $x >>0$, $$x^{ax} \le \sum_{x_i \le x} N_{A}(x_i) \le  x^{bx}.$$ In particular, this implies that for all sufficiently large $x$, $$x^{ax} \le ~\max_{x_i \le x} N_{A}(x_i)~ \le  x^{bx}.$$

In [@FMP2] (and [@FMP1]), Frigerio, Martelli and Petronio constructed explicit families of hyperbolic $3$-manifolds with totally geodesic boundary giving sequences $x_i \to \infty$ such that the number $N_{G} (x_i)$ of hyperbolic 3-manifolds of volume $x_i$ with geodesic boundary grows at least as fast as $x_i^{c x_i}$ for some $c>0$.

In the last part of this paper, we investigate the number $N_L(v)$ of hyperbolic link complements in $S^3$ with volume $v$. In Theorem [\[thm.expo\]](#thm.expo){reference-type="ref" reference="thm.expo"} we construct sequences of volumes $v_n \to \infty$ such that the number $N_L(v_n)$ of hyperbolic link complements with volume $v_n$ grows at least exponentially fast with $v_n$.

Our main tool is mutation along totally geodesic thrice punctured spheres in fully augmented link complements. It is well known that mutation along certain special surfaces leaves the hyperbolic volume and many other invariants unchanged (see for example [@Ada], [@Rub], [@DGST]). We distinguish the manifolds produced using information about their cusp shapes and maximal horoball cusp neighbourhoods.

Recent independent work of Chesebro-DeBlois [@CD] uses mutations along 4-punctured spheres to show that $N_L(v)$ grows at least exponentially fast with $v$, and that the number of commensurability classes of link complements with a given volume can be arbitrarily large.

Mutation along thrice punctured spheres can be studied by using spatial trivalent graphs. We will say that a spatial trivalent graph is *hyperbolic* if its complement admits a hyperbolic metric with parabolic meridians and geodesic boundaries (see section [\[sec.Vol\]](#sec.Vol){reference-type="ref" reference="sec.Vol"}, [@HHMP] and [@Mas]). In [@Mas], the second author exhibited volume preserving moves on hyperbolic graphs and hyperbolic links, which correspond to cutting and gluing along thrice punctured spheres. By applying these moves, each hyperbolic graph with a planar diagram corresponds to a *fully augmented link*. Such links have been well studied, and we can easily compute the moduli of their cusps (see [@FP] and [@Pur]).

Here is a brief outline of the remainder of the paper. In section 2, we recall the results of Neumann and Zagier relating the decrease in volume during hyperbolic Dehn filling to the length of the surgery curve. We then explain the key ideas that will allow us to obtain manifolds uniquely determined by their volumes. In section 3 (resp. 4), we apply these ideas to the manifolds denoted $m003$ and $m004$ (resp. $m125$ and $m129$) in SnapPea notation, and produce infinitely many manifolds that are determined by their volumes amongst all (resp. all cusped) orientable hyperbolic 3-manifolds. In section 5, we compute some higher order terms in the Neumann-Zagier asymptotic formula for the examples considered in sections 3 and 4; some of those computations are used in section 4. In section [\[sec.Vol\]](#sec.Vol){reference-type="ref" reference="sec.Vol"}, we review some of the volume preserving moves on graphs from [@Mas]. In section [\[pack\]](#pack){reference-type="ref" reference="pack"}, we compute the moduli of the cusps of the manifolds that are obtained from the graph in Figure [\[fig.graphW\]](#fig.graphW){reference-type="ref" reference="fig.graphW"}. Then in section [\[const\]](#const){reference-type="ref" reference="const"}, we construct manifolds corresponding to binary cyclic words of $n$ letters and show that these manifolds are isometric if and only if their cyclic words are related by the natural action of the dihedral group $D_n$. Since the volume of these manifolds is a constant multiple of $n$, this gives a sequence $\mathcal{L}_n$ of families of distinct hyperbolic link complements which share the same volume $v_n$, such that the growth rate of $\#\mathcal{L}_n$ is at least exponential in $v_n$. Finally, in section 9, we collect some open problems related to the work in this paper.

**Acknowledgments:** We thank Sadayoshi Kojima and Danny Calegari for asking questions that led to this paper. We also thank Alan Reid, Rob Meyerhoff, Ze'ev Rudnick and Peter Sarnak for their helpful comments. The work of the first author was partially supported by the Australian Research Council grant DP1095760. The work of the second author was partially supported by the Global COE program "Computationism as a Foundation for the Sciences\". Much of this work was done during the second author's visit to the University of Melbourne; this visit was supported by the above Global COE program.

# Hyperbolic Dehn fillings determined by their volumes {#cusped_hyp}

Let $M$ be a cusped hyperbolic 3-manifold and let $T$ be a horospherical torus cross section of one of the cusps of $M$. Choose an oriented basis for $H_1(T;\mathbb{Z}) \cong \mathbb{Z}^2$, called the "meridian" and "longitude" for $T$, and let $M(a,b)$ be the result of Dehn filling along the simple closed curve with homology class $(a,b) \in H_1(T;\mathbb{Z}) \cong \mathbb{Z}^2$.

Let $A$ denote the area of $T$ and $L(a,b)$ the length of the geodesic on $T$ with homology class $(a,b)$. Then we will study the quadratic form $$\label{eq1}
Q(a,b) = {L(a,b)^2 \over A}.$$ (This gives the square of the length of $(a,b)$ when the torus $T$ is rescaled to have area 1, and is also known as the extremal length of the curve $(a,b)$.)

::: rmk
(Cusp Shape Parameters)[]{#cusp_param label="cusp_param"} *The horospherical torus $T$ is similar to the Euclidean torus $\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$, with *shape parameter* $\tau \in \mathbb{C}$ defined by $$\label{eq2}
\tau = (\text{complex translation of longitude})/
(\text{complex translation of meridian}),$$ where the torus is viewed from the cusp. Note that with the standard orientation convention for a link complement in $S^3$ or for an oriented manifold in SnapPea, this means that $\tau$ will have *negative* imaginary part.[^1] Then we have $$\label{eq3}
Q(a,b) = {  |a + b \tau|^2 \over | \text{Im}( \tau )| }.$$*
:::

The following result shows that the volume of $M(a,b)$ determines $Q(a,b)$ up to a uniformly bounded error. This observation will play a key role in our work.

::: prop
[]{#error_bound label="error_bound"} Let $V_0$ be the volume of the complete hyperbolic structure on $M$. Then there exist constants $C_1=C_1(M), C_2 =C_2(M) >0$ such that

1.  the Dehn filling $M(a,b)$ is hyperbolic whenever $L(a,b) > C_1$, and

2.  for all hyperbolic Dehn fillings $M(a,b)$, $$\label{eq4}
    \left| {\pi^2  \over \Delta V(a,b)}  - {Q(a,b)} \right| < C_2$$ where $\Delta V(a,b) = V_0 - \text{Vol} (M(a,b))$.
:::

::: proof
*Proof.* (a) follows from Thurston's hyperbolic Dehn surgery theorem [@Th].

\(b\) The asymptotic volume formula of Neumann-Zagier [@NZ] shows that the decrease in volume under Dehn filling satisfies $$\label{eq5}
\Delta V(a,b) = {\pi^2 \over Q(a,b)} +O\left({1 \over Q(a,b)^2}\right).$$ This implies the result of (b) when $Q(a,b)$ is sufficiently large. But there are only finitely many additional $(a,b)$ with $M(a,b)$ hyperbolic, so the result follows. ◻
:::

::: rmk
*(a) If $T$ is a maximal embedded horospherical torus, then we can take $C_1=6$ by the "length 6 theorem" of Agol [@agol_dehn] and Lackenby [@lack] and the Geometrization Theorem of Perelman.*

\(b\) The work of Hodgson-Kerckhoff [@HK Theorem 5.12 and Figure 2], and some numerical calculations imply that $$\label{eq6}
-7.05 \le {\pi^2  \over \Delta V(a,b)} - Q(a,b)  \le 5.82$$ whenever $Q(a,b) \ge 57.5041$ and $\Delta V \le 0.155$. Then by volume computations using SnapPy or Snap for the finite number of hyperbolic Dehn fillings with $\Delta V > 0.155$, an explicit value of $C_2$ can be determined for a given manifold $M$.

Numerical calculations using SnapPy suggest that $\left| {\pi^2  \over \Delta V(a,b)} - Q(a,b)\right|$ for hyperbolic Dehn fillings $M(a,b)$ is often considerably lower than these general bounds.
:::

We now study the quadratic form $Q(a,b)$ for a cusped hyperbolic 3-manifold $M$. Let $$\label{eq7}
S_Q= \{ Q(a,b) : a,b \text{ are relatively prime integers} \}.$$

**Key Idea.** Let $(a_0,b_0)$ be a pair of relatively prime integers such that $M(a_0,b_0)$ is hyperbolic and let $q_0 = Q(a_0,b_0)$. Assume that

1.  there is large enough 2-sided gap around $q_0$ in $S_Q$, and

2.  $Q(a,b)=q_0$ has few solutions with $(a,b)$ relatively prime integers.

Then there are few Dehn fillings $M(a,b)$ with the same volume as $M(a_0,b_0)$.

More precisely,

::: prop
[]{#few_mflds_with_vol label="few_mflds_with_vol"} Let $(a_0,b_0)$ be a pair of relatively prime integers such that $M(a_0,b_0)$ is hyperbolic and let $q_0 = Q(a_0,b_0)$. Let $C_2 = C_2(M) >0$ be as in Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}. Assume that

::: center
there exists $g > 2C_2$ such that $s \in S_Q$ and $|s-q_0|< g$ implies $s= q_0$.
:::

Then $\text{Vol} (M(a,b)) =  \text{Vol} (M(a_0,b_0)$ implies $Q(a,b)=Q(a_0,b_0)$. Hence the number of such manifolds $M(a,b)$ is at most $n(q_0)/2$, where $n(q_0)$ is the number of solutions to $Q(a,b)=q_0$ with $a,b$ relatively prime integers.
:::

::: proof
*Proof.* Assume that $M(a,b)$ is hyperbolic with $\text{Vol} (M(a,b)) =  \text{Vol} (M(a_0,b_0))$ and let $\Delta V=  V_0 - \text{Vol} (M(a_0,b_0))$. Then Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"} implies $$\left| {\pi^2  \over \Delta V}  -Q(a,b) \right| < C_2 \text{ and } \left| {\pi^2  \over \Delta V}  -Q(a_0,b_0) \right| < C_2,$$ so $$\left| Q(a,b)   - Q(a_0,b_0) \right| < 2C_2 < g.$$ Hence $Q(a_0,b_0)=Q(a,b)$ by our assumption. But $(a,b)$ and $(-a,-b)$ Dehn fillings on $M$ give the same manifold, so the result follows. ◻
:::

::: rmk
[]{#few_with_symm label="few_with_symm"}

*More generally, there is a version of the previous Proposition which applies when the horospherical torus $T = \mathbb{C}/(\mathbb{Z}+\tau \mathbb{Z})$ has symmetries other than those induced by the maps $(a,b) \mapsto \pm(a,b)$ that extend to symmetries of the cusped manifold $M$.*

Let $G_Q$ be the group of integral automorphisms of the quadratic form $Q$, $$\label{eq8}
 G_Q = \{ A \in GL(2,\mathbb{Z}) :  Q(A X )= Q( X  ) \text{ for all } X=(x,y) \in \mathbb{Z}^2 \}.$$ For each isometry $g$ of $M$ preserving the cusp corresponding to $T$, the induced action on homology gives an automorphism $g_*$ of $H_1(T) \cong \mathbb{Z}^2$. Let $G_M \subset G_Q$ be the subgroup generated by these automorphisms $g_*$ together the automorphism $(x,y) \mapsto (-x,-y)$. Then for each $\sigma \in G_M$, the Dehn fillings of $M$ along $(a,b)$ and $(a',b')=\sigma(a,b)$ give homeomorphic manifolds.

Then the previous argument shows that, with the hypotheses and notation of Proposition [\[few_mflds_with_vol\]](#few_mflds_with_vol){reference-type="ref" reference="few_mflds_with_vol"}, the number of hyperbolic manifolds $M(a,b)$ with $\text{Vol} (M(a,b)) =  \text{Vol} (M(a_0,b_0)$ is at most $n(q_0)/|G_M|$, where $n(q_0)$ is the number of solutions to $Q(a,b)=q_0$ with $a,b$ relatively prime integers.
:::

If the cusp shape parameter $\tau$ belongs to an imaginary quadratic field, then the quadratic form $$Q(x,y) = |x+\tau y|^2= (x + \tau y)(x + \bar\tau y) = x^2 + (\tau+\bar\tau) xy + |\tau|^2 y^2$$ has rational coefficients. Hence, after rescaling, we can assume that the coefficients are relatively prime integers.

If $Q$ is an *integral quadratic form* $$\label{eq9}
Q(x,y)= a x^2 + b xy + c y^2.$$ where $a,b,c \in \mathbb{Z}$, then $D = b^2 - 4ac$ is called the *discriminant* of $Q$. The following elementary result can be found, for example, in [@landau Theorem 201, p180], [@cox pp25--26] or [@buell pp49--50]. Here, and henceforth, we say that a pair of integers $(x,y)$ is *primitive* if $\gcd(x,y)=1$.

::: lem
[]{#discr_quad_res label="discr_quad_res"} Assume that $m$ has a primitive integer representation by an integral quadratic form $Q$, i.e. $Q(x_0,y_0)=m$ where $(x_0,y_0) \in \mathbb{Z}^2$ with $\gcd(x_0,y_0)=1$. Then the discriminant $D$ of $Q$ is a quadratic residue modulo $4m$. In particular, every prime divisor $p$ of $m$ has Kronecker symbol $(D/p)=+1$.
:::

# Dehn filling on the figure eight knot complement and its sister

In this section we study the closed hyperbolic manifolds obtained by Dehn filling on the figure eight knot complement and its sister, denoted $m004$ and $m003$ respectively in SnapPea notation. We will use the ideas described in the previous section to prove the following.

::: thm
[]{#closed_unique label="closed_unique"} There is an infinite sequence of hyperbolic Dehn fillings $M(a_i,b_i)$ on the figure eight knot complement $M=m004$ with $a_i^2+12b_i^2 \to  \infty$ such that if $N$ is any orientable hyperbolic 3-manifold with $\text{Vol} (N)=\text{Vol} (M(a_i,b_i))$ then $N$ is homeomorphic to $M(a_i,b_i)$. So the manifolds $M(a_i,b_i)$ are determined by their volumes, amongst all finite volume orientable hyperbolic 3-manifolds.
:::

For $m003$ and $m004$, the quadratic forms defined in equation ([\[eq1\]](#eq1){reference-type="ref" reference="eq1"}) are closely related to the quadratic form $$\label{eq10}Q_0(a,b) = a^2+ab+b^2 = |a+b \omega|^2$$ where $\omega = {1\over 2}(1-\sqrt{3} i )$ is a cube root of $-1$ satisfying $\omega^2-\omega+1=0$ and $\bar \omega = 1-\omega$. From the symmetries of the lattice $\mathbb{Z}+\mathbb{Z}\omega$, we have $$|a+b \omega| = | \omega^k(a+b \omega)| = | \omega^k(a+ b \bar \omega)| = | \omega^k(a+b-b \omega)|$$ for $k =0, 1, \ldots, 5$. Hence $Q_0$ has symmetry group $G_{Q_0} \cong D_6$ of order 12, and the orbit of $(a,b)$ under $G_{Q_0}$ is $$\label{eq11}\{ \pm(a,b), \pm(-b,a+b), \pm(-a-b,a), \pm (a+b,-b),\pm(b,a), \pm(-a,a+b) \}.$$

Now consider a maximal horospherical cusp torus for $m004$ and $m003$. In each case we choose the geometric basis for the peripheral homology used by SnapPea, consisting of two shortest simple closed geodesics. From Snap or SnapPy (or [@weeks_phd]) we have the following:

For $m004$, this torus has shortest closed geodesic of length 1, cusp shape $\tau = -2 \sqrt{3}i = 4 \omega -2$ and area $2 \sqrt{3}$. Hence, the $(a,b)$ geodesic has length squared $$\label{eq12}Q_1(a,b)= |a + b \tau|^2 = a^2 + 12 b^2 =Q_0(a-2b,4b) .$$ This quadratic form has symmetry group $G_{Q_1} = D_2$, given by $(a,b) \mapsto (\pm a, \pm b)$, and these all extend to symmetries of $m004$, so $G_{m004} = G_{Q_1}$.

For $m003$, the torus has shortest closed geodesic of length 2, cusp shape $\tau = \omega$ and area $2 \sqrt{3}$. Hence, the $(a,b)$ geodesic has length squared $$\label{eq13}Q_2(a,b)= |2a + 2b \omega|^2 = 4(a^2+ab+b^2) = 4Q_0(a,b) .$$ This quadratic form has symmetry group $G_{Q_2}=G_{Q_0} = D_6$ as described above. However, $G_{m003} = D_2$ is the subgroup given by $(a,b) \mapsto \pm(a,b), \pm(a+b,-b)$. (Note that any symmetry of $m003$ must preserve the homologically trivial longitude $(-1,2)$, hence must also preserve the orthogonal $(1,0)$ curve.)

::: prop
[]{#p_with_big_gap label="p_with_big_gap"} Given any integer $g >0$ there exist infinitely many primes $p$ such that

1.  $p$ can be written as $Q_1(a,b)$ where $a,b$ are relatively prime integers, and if $p=Q_1(a,b)=Q_1(a',b')$ then $(a',b') = (\pm a, \pm b)$ (with 4 possible choices of signs),

2.  $p+k$ has no primitive integer representation as $Q_0(a,b)$ for $0<|k|\le g$,

3.  $p$ has no primitive integer representation as $Q_2(a,b)$.
:::

This follows from some elementary number theory.

::: lem
[]{#p=1mod12 label="p=1mod12"} If $p$ is a prime congruent to $1$ modulo $12$, then $p$ can be written uniquely in the form $p= Q_1(a,b) = a^2 + 12 b^2$ where $a,b$ are relatively prime positive integers.
:::

::: proof
*Proof.* Euler showed that each prime $p \equiv 1 \bmod 3$ can be written uniquely in the form $p = x^2 + 3 y^2$ with $x,y$ positive integers (see for example [@cox Chapter 1]). If $p \equiv 1 \bmod 12$, then taking congruences $\bmod 4$ shows that $y$ is even. ◻
:::

::: lem
[]{#p=5mod6 label="p=5mod6"} If $p$ is a prime congruent to $5$ modulo $6$ and $p$ divides $n$, then $n$ has no representation $n = Q_0(a,b)=a^2 + ab + b^2$ with $a,b$ relatively prime integers.
:::

::: proof
*Proof.* Let $p$ be an odd prime dividing $n = a^2 + ab + b^2$ with $a,b$ relatively prime integers. Then by Lemma [\[discr_quad_res\]](#discr_quad_res){reference-type="ref" reference="discr_quad_res"}, $-3$ is a quadratic residue mod $p$. If $p \ne 3$, it follows that $p \equiv 1 \bmod 6$ by Quadratic Reciprocity (see e.g. [@HaWr Thm 96]). ◻
:::

::: proof
*Proof of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}.* We use the previous lemmas together with the Chinese remainder theorem and Dirichlet's theorem on primes in arithmetic progressions.

For $i=0,1,2$ let $$S_i = \{ Q_i(a,b) : a,b \text{ are relatively prime integers} \}.$$

Given any integer $g>0$, let $p_1, p_2, \ldots, p_{2g}$ be distinct primes congruent to $5$ modulo $6$. Consider the integers $n$ satisfying the congruences $$\begin{aligned}
 n-i &\equiv& 0 \bmod p_i   \qquad\text{ for }1 \le i \le g,\\
  n+i &\equiv& 0 \bmod p_{g+i} \quad\text{ for }1 \le i \le g, \text{ and }\\
 n &\equiv& 1 \bmod 12.
 
\end{aligned}$$ By the Chinese Remainder Theorem, these have a general solution of the form $$\label{eq14}
n \equiv n_0 \bmod 12 p_1 \ldots p_{2g}.$$ By Dirichlet's theorem on primes in arithmetic progressions, there are infinitely many solutions to ([\[eq14\]](#eq14){reference-type="ref" reference="eq14"}) such that $n$ is a prime, say $p$. For such $p$ we have $p \equiv 1 \bmod 12$ so $p \in S_1$ by Lemma [\[p=1mod12\]](#p=1mod12){reference-type="ref" reference="p=1mod12"}. Further $p+i$ is divisible by $p_i$ and $p-i$ is divisible by $p_{g+i}$ for $1 \le i \le g$. Hence $p+i \notin S_0, p-i \notin S_0$ for $1\le i \le g$ by Lemma [\[p=5mod6\]](#p=5mod6){reference-type="ref" reference="p=5mod6"}. Finally, $p \notin Q_2$ since $p$ is odd. Hence $p$ satisfies all the conditions (i)--(iii) of the proposition. ◻
:::

We now combine Proposition [\[few_with_symm\]](#few_with_symm){reference-type="ref" reference="few_with_symm"} and Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"} to prove the main theorem of this section.

::: proof
*Proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}.* The quadratic forms $Q_1$ and $Q_2$ for $m004$ and $m003$ considered above give the squares of geodesic lengths on a cusp torus with area $2 \sqrt{3}$. Hence the corresponding normalised quadratic forms, used in Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}, are $$\hat Q_1(a,b) =  {1 \over 2 \sqrt{3}} Q_1(a,b) \text{ and } \hat Q_2(a,b) =  {1 \over 2 \sqrt{3}} Q_2 (a,b).$$

We now apply Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"} with gap size $g = 4 \sqrt{3} C$, where $C$ is the maximum of the constants $C_2$ for $m004$ and $m003$ given by Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}. This gives a sequence of primes $p_i \equiv1 \bmod 12$ with $p_i \to \infty$ and pairs $(a_i,b_i)$ of relatively prime integers with $p_i =a_i^2+12b_i^2$ satisfying the conditions of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}.

Then $\text{Vol} (m004(a,b)) = \text{Vol} (m004(a_i,b_i))$ implies that $Q_1(a,b)=Q_1(a_i,b_i)$ by Proposition [\[few_with_symm\]](#few_with_symm){reference-type="ref" reference="few_with_symm"}, hence $(a,b) = (\pm a_i, \pm b_i)$ by condition (i) of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}. But these solutions differ by symmetries of $Q_1$ that extend to symmetries of $m004$, so $m004(a,b)$ is homeomorphic to $m004(a_i,b_i)$.

Further, $\text{Vol} (m004(a_i,b_i)) = \text{Vol} (m003(a,b))$ implies that $Q_1(a_i,b_i)=Q_2(a,b)$. But this has no solutions by condition (iii) of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}. Hence $m004(a_i,b_i)$ is uniquely determined by its volume amongst Dehn fillings on $m004$ and $m003$.

Cao and Meyerhoff [@CM] showed that the figure eight knot complement $m004$ and its sister $m003$ are the unique orientable cusped hyperbolic 3-manifolds of smallest volume $v_\omega$. The work of Jørgensen and Thurston (see [@Th], [@Gr]) shows that any sequence of closed hyperbolic 3-manifolds with volume approaching $v_\omega$ from below has a subsequence whose geometric limit is a cusped hyperbolic 3-manifold $M_\infty$ with volume $v_\omega$, and that the manifolds in the subsequence are obtained by Dehn filling on $M_\infty$. It follows that there exists $\epsilon >0$ such that if $N$ is any closed orientable hyperbolic 3-manifold with $v_\omega - \epsilon < \text{Vol} (N) <v_\omega$ then $N$ can be obtained by Dehn filling on $m003$ or $m004$. Now the result follows from the previous observations. ◻
:::

# Dehn filling on the Whitehead link complement and its sister

We now study the 1-cusped hyperbolic 3-manifolds obtained by Dehn filling on the Whitehead link complement and its sister, the complement of the $(-2,3,8)$-pretzel link, denoted $m129$ and $m125$ respectively in SnapPea notation. Note that each of these manifolds has a symmetry interchanging the cusps, so it suffices to consider Dehn fillings on cusp 0. See also [@HMW; @NR] and [@AD] for detailed discussions of the geometry and topology of these manifolds and their Dehn fillings.

The main result of this section is the following:

::: thm
[]{#cusped_unique label="cusped_unique"} There is an infinite sequence of hyperbolic Dehn fillings $M(a_i,b_i)$ on one cusp of the $(-2,3,8)$-pretzel link complement $M=m125$ with $a_i^2+b_i^2 \to  \infty$ such that if $N$ is any orientable cusped hyperbolic 3-manifold with $\text{Vol} (N)=\text{Vol} (M(a_i,b_i))$ then $N$ is homeomorphic to $M(a_i,b_i)$. So the manifolds $M(a_i,b_i)$ are determined by their volumes, amongst all orientable cusped hyperbolic 3-manifolds.
:::

The proof is similar to the proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}. However there is an extra difficulty because not every symmetry of the cusp torus extends to a symmetry of the manifold $m125$. To deal with this, we look at the next terms in the Neumann-Zagier asymptotic expansion for volume change during Dehn filling.

The quadratic forms for $m125$ and $m129$ given by ([\[eq1\]](#eq1){reference-type="ref" reference="eq1"}) are closely related to the quadratic form $$\label{eq15}
Q_0(a,b) = a^2+ b^2 = |a+b i|^2 .$$ From the symmetries of the lattice $\mathbb{Z}+\mathbb{Z}i$, we have $$|a+b i | = | i^k(a+b i)| = | i^k(a- b i)|$$ for $k =0, 1, \ldots, 3$, and $Q_0$ has symmetry group $G_{Q_0} \cong D_4$ of order 8, with the orbit of $(a,b)$ under $G_{Q_0}$ given by $$\label{eq16}
\{  \pm(a, b), \pm(-b,a), \pm(a,-b), \pm(b,a) \}.$$

Consider a maximal horospherical cusp torus for $m129$ and $m125$. In each case we choose the geometric basis for peripheral homology used by SnapPea. From SnapPea (or [@HMW; @NR; @AD]) we have the following:

For $m125$, the torus has cusp shape $\tau = i$. If we normalise so that the torus has area $2$ then the $(a,b)$ geodesic has length squared $$\label{eq17}
Q_1(a,b)= 2 |a + b i |^2 = 2(a^2 + b^2) = 2 Q_0(a,b).$$ This quadratic form has symmetry group $G_{Q_1}=G_{Q_0} = D_4$ as described above. The subgroup of symmetries of $Q_1$ extending to symmetries of $m125$ is the subgroup of orientation preserving symmetries $G_{m125} = C_4$, given by $(a,b) \mapsto  \pm(a, b), \pm(-b,a)$.

For $m129$, the torus has cusp shape $\tau = 2 i$. If we normalise so that the torus has area $2$ then the $(a,b)$ geodesic has length squared $$\label{eq18}
Q_2(a,b)={ |a+ 2bi|^2 } = (a^2+ 4b^2) = Q_0(a,2b).$$ This quadratic form has symmetry group $G_{Q_2} = D_2$ consisting of $(a,b) \mapsto (\pm a, \pm b)$, but $G_{m129} = C_2$ is the subgroup $(a,b) \mapsto \pm(a,b)$.

::: prop
[]{#2p_with_big_gap label="2p_with_big_gap"} For each $g >0$ there exist infinitely many integers $m=2p$, with $p$ prime, such that

1.  $m$ can be written as $Q_1(a,b)$ where $a,b$ are relatively prime integers, and if $Q_1(a,b)=Q_1(a',b')$ then $(a',b') = (\pm a, \pm b)$ or $(a',b') = (\pm b, \pm a)$.

2.  $m+k$ has no primitive integer representation as $Q_0(a,b)$ for $0<|k|\le g$,

3.  $m$ has no primitive integer representation as $Q_2(a,b)$.
:::

This again follows from some elementary number theory.

::: lem
[]{#p=1mod4 label="p=1mod4"} If $p$ is a prime congruent to $1$ modulo $4$, then $p$ can be written in the form $p= a^2 + b^2$ where $a,b$ are relatively prime positive integers. Further, if $p=(a')^2+(b')^2$ where $a',b'$ are positive integers then $(a',b')=(a,b)$ or $(b,a)$.
:::

::: proof
*Proof.* This is a result of Euler (see, for example, [@HaWr Chapter 15]). ◻
:::

::: lem
[]{#p=3mod4 label="p=3mod4"} If $p$ is a prime congruent to $3$ modulo $4$ and $p$ divides $n$, then $n$ has no representation $n = Q_0(a,b)=a^2 + b^2$ with $a,b$ relatively prime integers.
:::

::: proof
*Proof.* Let $p$ be an odd prime dividing $n = a^2 + b^2$ with $a,b$ relatively prime integers. Then by Lemma [\[discr_quad_res\]](#discr_quad_res){reference-type="ref" reference="discr_quad_res"}, $-1$ is a quadratic residue mod $p$. It follows that $p \equiv 1 \bmod 4$ (see e.g. [@HaWr Thm 82]). ◻
:::

::: lem
If $n \equiv 2 \mod 4$ then $n = Q_2(a,b) = a^2 + 4 b^2$ has no solution with $a,b$ integers.
:::

::: proof
*Proof.* Reduce modulo $4$. ◻
:::

::: proof
*Proof of Proposition [\[2p_with_big_gap\]](#2p_with_big_gap){reference-type="ref" reference="2p_with_big_gap"}.* This follows from the previous lemmas together with the Chinese remainder theorem and Dirichlet's theorem on primes in arithmetic progressions, as in the proof of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}. ◻
:::

::: proof
*Proof of Theorem [\[cusped_unique\]](#cusped_unique){reference-type="ref" reference="cusped_unique"}.* The quadratic forms $Q_1$ and $Q_2$ for $m125$ and $m129$ considered above give the squares of geodesic lengths on a cusp torus with area $2$. Hence the corresponding normalised quadratic forms are given by $$\hat Q_1(a,b) =  {1 \over 2 } Q_1(a,b) \text{ and } \hat Q_2(a,b) =  {1 \over 2 } Q_2 (a,b).$$ We now apply Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"} with gap size $g = 4 C$, where $C$ is the maximum of the constants $C_2$ for $m125$ and $m129$ given by Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}.

This gives a sequence of primes $p_i \equiv 1 \bmod 4$ with $p_i \to \infty$ and pairs $(a_i,b_i)$ of relatively prime integers with $p_i =a_i^2+b_i^2$ satisfying the conditions of Proposition [\[2p_with_big_gap\]](#2p_with_big_gap){reference-type="ref" reference="2p_with_big_gap"}. Then $\text{Vol} (m125(a,b)) = \text{Vol} (m125(a_i,b_i)$ implies that $Q_1(a,b)=Q_1(a_i,b_i)$, hence $(a,b) = \pm(a_i,b_i), \pm(-b_i,a_i), \pm(a_i,-b_i)  \text{ or} \pm(b_i,a_i)$. For any such $(a,b)=(a_i,b_i)$, $\text{Vol} (m125(a,b)) = \text{Vol} (m125(a',b'))$ implies that $Q_1(a,b)=Q_1(a',b')$ hence $(a',b') = \pm(a, b), \pm(-b,a), \pm(a,-b)  \text{ or} \pm(b,a)$.

Now the surgeries $\pm(a, b), \pm(-b,a)$ give manifolds which are homeomorphic, hence have the same volume. Similarly, the surgeries $\pm(a,-b),   \pm(b,a)$ give homeomorphic manifolds of the same volume. Next, we use the degree 4 terms in the Neumann-Zagier asymptotic formula to show that $\text{Vol} (m125(a,b)) \ne  \text{Vol} (m125(b,a))$ for all sufficiently large $(a,b)$.

In [@AD], Aaber and Dunfield study the Neumann-Zagier asymptotic expansion of volume for Dehn fillings on the Whitehead link sister $m125$. Using their calculations we obtain the following asymptotic formula for decrease in volume for surgeries on cusp 0 of $m125$ (see Example [\[m125_NZ4\]](#m125_NZ4){reference-type="ref" reference="m125_NZ4"} and equation ([\[eq31\]](#eq31){reference-type="ref" reference="eq31"}) below): $$\Delta V_{m125} (a,b)=  
{ \pi^2 \over a^2+b^2} -
\frac{\pi^4(a^4-12 a^3 b-6 a^2 b^2+12 a b^3+b^4)}{ 24\left(a^2+b^2\right)^4}
+ O \left({1 \over (a^2+b^2)^3}\right).$$ Hence, we have $$\label{eq20}\Delta V_{m125} (a,b) - \Delta V_{m125} (b,a)
=  \frac{\pi ^4 a b \left(a^2-b^2\right)}{\left(a^2+b^2\right)^4} +
O \left({1 \over (a^2+b^2)^3}\right).$$

::: lem
[]{#lower_bound label="lower_bound"} If $a$ and $b$ are integers with $a > b > 0$, then $a b (a^2-b^2) \ge  {r^3/4},$ where $r^2 = a^2+b^2$.
:::

::: proof
*Proof.* Consider the function $$f(a,b)=    a b (a^2-b^2) = a b ( a + b ) ( a - b ).$$ Now we have

1.  If $b \le a/2$ then $b(a-b) \ge b (a - a/2)=  b a/2  \ge a/2,$ since $b \ge 1$.

2.  If $b  \ge a/2$ then $b (a-b) \ge  a/2 \cdot (a-b)  \ge  a/2,$ since $a-b  \ge 1$.

Further, $a^2+b^2 = r^2$ and $a > b > 0$ imply that $a^2 \ge r^2/2$ and $a+b \ge r$. Hence $$f(a,b)=  a(a+b) b(a-b) \ge a(a+b) \cdot a/2  = a^2 (a+b)/2 \ge r^3/4,$$ as desired. ◻
:::

Equation ([\[eq20\]](#eq20){reference-type="ref" reference="eq20"}) shows that, whenever $a^2+b^2$ is sufficiently large, $$\Delta V_{m125} (a,b) - \Delta V_{m125} (b,a)
\ge  \frac{\pi ^4 a b \left(a^2-b^2\right) - C(a^2+b^2)}{\left(a^2+b^2\right)^4},$$ where $C$ is a positive constant. Hence, by Lemma [\[lower_bound\]](#lower_bound){reference-type="ref" reference="lower_bound"}, there exists a constant $R>0$ such that if $(a,b)$ are relatively prime integers with $a >b >0$ and $a^2+b^2 \ge R^2$ , then $\Delta V_{m125} (a,b) > \Delta V_{m125} (b,a)$.

This completes the proof that for all sufficiently large $(a_i,b_i)$, the Dehn fillings $m125(a_i,b_i)$ are determined by their volumes amongst Dehn fillings on $m125$.

Further, $\text{Vol} (m125(a_i,b_i)) = \text{Vol} (m129(a,b))$ implies that $Q_1(a_i,b_i)=Q_2(a,b)$, which has no solutions by condition (iii) of Proposition [\[2p_with_big_gap\]](#2p_with_big_gap){reference-type="ref" reference="2p_with_big_gap"}. Hence, for all sufficiently large $(a_i,b_i)$, the manifolds $m125(a_i,b_i)$ are determined by their volumes amongst Dehn fillings on $m129$ and $m125$.

The result now follows as in the proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"} since $m129$ and $m125$ are the unique 2-cusped manifolds of volume $v_{\omega^2}$ by the work of Agol [@agol_2cusp]. So any 1-cusped manifold with volume less than $v_{\omega^2}$ but sufficiently close to $v_{\omega^2}$ comes from Dehn filling on $m129$ or $m125$. ◻
:::

[^1]: Caution: this convention agrees with that used in Snap. However, in SnapPy the 'shape' reported by the function `cusp_info()` is the *complex conjugate* $\bar \tau$.
