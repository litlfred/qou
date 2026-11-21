---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-005-6-proving-the-garoufalidis-loebl-state-sum
section_title: "Proving the Garoufalidis-Loebl state-sum"
section_number: 6
pages: 23-38
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.995
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
We will now rewrite the usual state-sum contributions as described in [@G] into the Garoufalidis Loebl state-sum contributions using the above identities and the flow Lemma. There two important steps: The first will be to transform the formulas in the last section into formulas for the $(+)$-model (increasing colors on overcrossing arcs at overcrossings). The second is to rewrite the two functions $f_{\pm }$ into a single vertex contribution formula, depending on the crossing sign.

Our convention at crossings will be:

::: center
![image](Figure10.pdf){width="80%"}
:::

*Figure 10*

Note that in order to apply the formulas from section 5 we change the orientation of the projection. It is known that a change of orientation does not change the colored Jones polynomial. There will be though a change in rotation numbers, which will show up in defining $\textrm{rot}(f)$ for a state on $G\mathcal{K}$ in this section, and it will appear in the definition of $\delta '(\mathcal{K},n)$, which is a global power of $t$ for the state-sum contributions. We also point out that there are different conventions with respect whether right or left oriented extrema introduce the terms $b_{\ell }(s)$ in equation [\[eq=Fterm\]](#eq=Fterm){reference-type="eqref" reference="eq=Fterm"}.

ln the following we consider now $a,b,r,\varepsilon$ as functions on the set of crossings and often omit the argument in formulas. Then the vertex state-sum contribution at $c$ is given by [\[eq=positive crossing\]](#eq=positive crossing){reference-type="eqref" reference="eq=positive crossing"} and [\[eq=negative crossing\]](#eq=negative crossing){reference-type="eqref" reference="eq=negative crossing"}, with the variable $v$ replaced by the variable $t=v^2$. We also use here the symmetry of the quantum binomials. The following expression is immediate by substituting formulas [\[eq=binomial\]](#eq=binomial){reference-type="eqref" reference="eq=binomial"} and [\[eq=Pochhammer\]](#eq=Pochhammer){reference-type="eqref" reference="eq=Pochhammer"} and using Lemma [\[lem=binomial symmetry\]](#lem=binomial symmetry){reference-type="ref" reference="lem=binomial symmetry"}. It gives a single expression to be evaluated at each crossing with the sign of the crossing contained in the definitions of the $q$-algebra symbols.

$$\begin{aligned}
&(-1)^{(1+\varepsilon)\frac{r}{2}}t^{-\varepsilon /2\left((n-2b-(1-\varepsilon )r)(\frac{n}{2}-a+\frac{1}{2}(1-\varepsilon )r \right)+\frac{r(r-1)}{2}})\\
&\cdot  t^{\varepsilon /2 \cdot br}{{b+r}\choose {r}}_{t^{-\varepsilon}}\cdot (-1)^{(1+\varepsilon )\frac{r}{2}}t^{-\varepsilon (\frac{(n+r-a)r}{2}-\frac{r(r-1)}{4})}  \{n+r-a\}_{r,t^{\varepsilon }}
\end{aligned}$$

Using that $1+\varepsilon \in \{0,2\}$ to eliminate the sign dependence, and cancelling the $r(r-1)/4$-terms, we see that the vertex contribution function is given by $$\label{eq=vertex contribution}
t^{\varepsilon /2\cdot (-n^2/2+ n\rho +\sigma)-\frac{1}{2}\tau}\cdot {{b+r}\choose {r}}_{t^{-\varepsilon}}\cdot \{n+r-a\}_{r,t^{\varepsilon }}$$ with the two functions, defined for each crossing: $$\begin{aligned}
\rho &=b+a-r \\
\sigma& =-2ab+(b-a)r+br-(r-a)r+r^2 \\
\tau&=r(b-a+r)
\end{aligned}$$ Here we also used $\frac{1}{2}(1-\varepsilon )^2=(1-\varepsilon )$. If we let $a=r+R$ then $$\sigma =-2ar-2aR+(b-a)r+br-r^2+ar+r^2=2b(r-a)=-2bR$$

The crucial geometric statements leading to the Garoufalidis-Loebl formula are contained in the following two propositions. As noted above we usually omit the arguments of the functions defined on the set of crossings.

::: prop
For each $\mathbb{Z}$-coloring of a chord graph, respectively the corresponding coloring of a part arc-graph inducing this coloring, $$\sum_cr(a-b-r)=0$$
:::

::: proof
*Proof.* The formula is equivalent to:

$$\sum_cr(a-b)=\sum r^2$$

We will first show the equation for chords only between distinct components. As a first step we consider the abstract chord graph with exactly one chord for each $1\leq j<k\leq \ell$ directed from the $k$-th to the $j-th$ component with chord color $r_{j,k}$. In this case the sum $\sum_cr(a-b)$ is easily computed as follows. The contribution of $r_{jk}$ in the sum is $$r_{jk}(-\sum_{1\leq i\leq j-1}r_{ij}+\sum_{j<i\leq k}r_{ji}+\sum_{1\leq i\leq j}r_{ik})$$

::: center
![image](Figure11.pdf){width="80%"}
:::

*Figure 11*

By using the cycle relation for the $j$-th component, the first two sums can be replaced by $-\sum_{k<i\leq \mu }r_{ji}$ and so the contribution from $r_{jk}$ is (those be read from the incoming chords of the $j$-th component and the corresponding values on the $k$-th component): $$r_{jk}(r_{jk}+\sum_{1\leq i<j}r_{ik}-\sum_{k<i\leq \mu }r_{ji})=r_{jk}^2+r_{jk}(\sum_{1\leq i<j}r_{ik}-\sum_{k<i\leq \mu }r_{ji})$$

::: center
![image](Figure12.pdf){width="80%"}
:::

*Figure 12*

Thus it suffices to prove the claim: $$\sum_{1\leq j<k\leq \mu}r_{jk}(\sum_{1\leq i<j}r_{ik}-\sum_{k<i\leq \mu }r_{ji})=0$$ Now we can define a skew-symmetric matrix $\mu \times \mu$-matrix $(r_{jk})$ with the coefficients $r_{jk}$ for $j<k$ given by chord colors of the chord graph. The $\mu$ cycle relations then exactly say that the sum of columns of this matrix is the zero-vector. In this case, the claim follows from the lemma below. The chord graphs resulting from actual link projections differ from the standard graph considered above by doubling of chords and switching the order of attachment to the circles. We will show that the relation of the proposition remains true in this case. Also note since the relation holds for chord colorings by arbitrary integers and changing chord orientation and color by multiplication by $-1$ we finally prove the result for arbitrary chord graphs and thus arbitrary part arc-graphs.

We calculate the sums $\sum r(a-b)$ for chord graphs differing locally only by the following chord respectively two chords as in the picture

::: center
![image](Figure13.pdf){width="95%"}
:::

*Figure 13*

Then the contribution to the sum from the chord in the left picture is $$(r+r')(a-(b-(r+r'))=(r+r')^2+(r+r')(a-b)$$ while the contribution from the two chords on the right is $$r(a-(b-r))+r'(a-r-(b-r-r'))=r^2+r'^2+(r+r')(a-b)$$ Note that the contributions from all other chords are unchanged. In going from formula (1) to formula (3) above we eliminate copies of $r^2$ and both sides and then justify that the remaining sum on the left of the equation is $0$. But this means that in the specific situation above we subtract $(r+r')^2$ for the above sum and specific chord and $r^2+r'^2$ for the doubled chord. The result is the same in each case as our computation shows. Because for the chord colored $r+r'$ we know from before that the sum is $0$ it will also follow for the doubled chord.

Next, adding chords attached to single circles, so corresponding to self-crossings in the part arc-graph, we first attach a chord just in the special way:

::: center
![image](Figure14.pdf){width="35%"}
:::

*Figure 14*

Note that this will change $\sum r(a-b)$ by a contribution $r(c-(c-r))=r^2$ so the result is true in this case. It suffices at this point to show that the relation remains true under arbitrary switches in the way the chords are attached to the circles. It will suffice to consider the following case of two consecutive chords. There will other chords attached to the circles not shown.

::: center
![image](Figure15.pdf){width="45%"}
:::

*Figure 15*

The contribution to $\sum r(a-b)$ for the above picture is $$r(a+b-r)+r'(a+r+r'-b')$$ and after switching the endpoints of chords: $$r'(a+r'-b')+r(a+r+r'-b),$$ which in each case is $r^2+r'^2+rr'+r(a-b)+r'(a-b')$, so the sum is not changing. But any possible constellation of chords joining distinct components of the chord graph can be reached by sequences of those switches. ◻
:::

::: lem
Let $A=(a_{jk})$ be an $\mu \times \mu$ skew-symmetric matrix (over $\mathbb{Z}$ (the argument works in fact over any commutative ring with $1$) such that for $A=(a^1,\ldots ,a^{\mu})$ we have the sum of column vectors $\sum_{j=1}^{\mu }a^j$ is the zero-vector. Define for each $j<k$, $$s_{jk}=\sum_{1\leq i<j}a_{ik}-\sum_{k<i\leq \mu}a_{ji}.$$ Then $$(*) \qquad \qquad \sum_{1\leq j<k\leq \mu}a_{jk}s_{jk}=0$$
:::

::: proof
*Proof.* The set $\mathcal{A}_{\mu }$ of skew symmetric $\mu \times \mu$ matrices with zero column sum is a submodule of the module of all skew symmetric matrices. Note that the skew symmetry implies the zero row sum condition. It is easily proved by induction that the following set of elementary matrices $E_{jk}$ defined for $1\leq j<\mu$ and $j<k\leq \mu$ is a generating set of $\mathcal{A}_{\mu}$. Let $(j,k)$ be the position of the upper left entry of the $2\times 2$-matrix $$\begin{pmatrix} 1 &  -1 \\ -1 & 1\end{pmatrix}\ \textrm{for} \ k>j+1$$ in a skew symmetric matrix with only the entries for $(j,k), (j,k+1), (j+1,k), (j+1,k+1)$ above the diagonal are non-zero and given by the $2\times 2$ matrix, and the entries below the diagonal are such that the matrix is skew-symmetric. Similarly, we position the $2\times 2$-matrix $$\begin{pmatrix} 1 & -1 \\ 0 & 1\end{pmatrix} \ \textrm{for}\ k=j+1$$ above the diagonal with the $0$ on the diagonal, and define the entries below the diagonal to get a skew-symmetric matrix. For example, when $\ell =3$ there is only the matrix $$E_{23}=\begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix},$$ corresponding to $\dim \mathcal{A}_{\mu }=1$. Note that for $\mu =0,1$, $\mathcal{A}_{\mu }=\{0\}$. For $\mu >3$ we can proceed inductively to prove that the matrices $E_{jk}$ generate: $$A=a_{12}E_{12}+(a_{12}+a_{13})E_{13}+\cdots +(a_{12}+\cdots +a_{1,\mu -1})E_{1,\mu -1}+A',$$ with $A'\in \mathcal{A}_{\mu }$ a matrix with first row and column $0$ because $\sum_{i=2}^{\mu } a_{1i}=0$. To prove the lemma it thus suffices to show that for each $A\in \mathcal{A}_{\mu }$ satisfying $(*)$, als $B=A+E_{jk}$ satisfies $(*)$. It suffices to consider $A+E_{jk}$, the result for $A-E_{jk}$ is obvious because if $A$ satisfies $(*)$ also $-A$ satisfies $(*)$. For $k>j+1$ this is easily checked. Note that the coefficients of $B$ are only changed in the $2\times 2$-submatrix with upper left position at $(j,k)$, and there it will be $$\begin{pmatrix} a_{jk}+1 & a_{j,k+1}-1 \\ a_{j+1,k}-1 & a_{j+1,k+1}+1\end{pmatrix}$$ Contributions in $(*)$ for $B$ from $a_{i\ell }$ with $\ell <k$ and $i=j,j+1$, or $i>j+1$ and $\ell =k,k+1$ will not change because $\pm 1$ cancel out in $s_{i \ell}$. So it suffices to consider how $(*)$ is changing considering the products of $b_{i\ell }$ with the corresponding $s_{i\ell }$ and $i\in \{j,j+1\}, \ell \in \{k,k+1\}$. Finally, new contributions in the products $(a_{j,k}+1)(-(a_{j,k+1}-1))$, $(a_{j+1,k}-1)(-(a_{j+1,k+1}+1))$, $(a_{j+1,k}-1)(a_{jk}+1)$ and $(a_{j+1,k+1}+1)(a_{j,k+1}-1)$ will cancel as is easily checked. The case $k=j+1$ is similar but involves both the zero column sum and skew symmetry. In order to avoid too many index consideration we will discuss the case $\mu =5$ and $E_{23}$ because it shows all necessary considerations. In this case the upper diagonal part of the matrix $B$ is given by $$\begin{pmatrix} 0 & a_{12} & a_{13} & a_{14} & a_{15} \\  \ & 0 & a_{23}+1 & a_{24}-1 & a_{25} \\ \ & \ & 0 & a_{34}+1 & a_{35} \\ \ & \ & \ & 0 & a_{45} \\ \ & \ & \ & \ & \ 0 \end{pmatrix}$$ In this case multiplying out just terms in $a_{jk}$ and $s_{jk}$ within the changed $2\times 2$-submatrix gives $$(a_{23}+1)(-(a_{24}-1))=-a_{23}a_{24}+a_{23}-a_{24}+1$$ $$(a_{34}+1)(a_{24}-1)=a_{34}a_{24}-a_{34}+a_{24}-1$$ Note that the $\pm a_{24}$ and $\pm 1$ cancel out, the $-a_{23}a_{24}$ and $a_{34}a_{24}$ are in the $(*)$-summation for $A$, so there is a contribution of $a_{23}-a_{34}$. But the $+1$ in the upper left contributes an additional $a_{13}$, the $+1$ in the lower right an additional $-a_{35}$. So the change in $(*)$ is given by $$a_{13}+a_{23}-(a_{34}+a_{35})=0,$$ which follows by considering the zero row sum relation in column $3$. The general argument is completely analogous with $a_{13}$ and $a_{35}$ contributions replaced by corresponding sums. ◻
:::

::: prop
[]{#prop=2 label="prop=2"} For each $\mathbb{Z}$-coloring of a signed chord graph, respectively the corresponding coloring of a part arc-graph inducing this chord graph coloring, $$\frac{1}{2}\sum_c\varepsilon (b+a-r)=\sum_c\varepsilon b,$$ or equivalently $$\sum_c\varepsilon (a-b)=\sum_c\varepsilon r.$$
:::

::: proof
*Proof.* We will consider the equivalent statement for states on signed chord graphs. The argument will proceed as follows: First the claim is proved for part arc-graphs without chords joining distinct circles, but allowing distinct components. This corresponds to considering the horizontal multiplication of braids. Then we will argue that for general chord graphs we can assume for components $j>i$ that at all crossings of $j$ and $i$ the component $j$ will overcross component $i$. This corresponds to a change of the sign of the crossing. Finally we will argue that the equation to be proved remains valid under braid moves corresponding to specific Reidemeister II and III moves. This will extend the claim to the general link case. We will work in the free abelian group generated by variables $r$ representing the chord colors. Then we can define an element in the free abelian group for each circle segment representing a part-arc. The following figure shows a component with a self-chord colored $r$ and sign $\varepsilon$. We chose a specific orientation of the chord but the computation is similar if the orientation is reversed.

::: center
![image](Figure16.pdf){width="70%"}
:::

*Figure 16*

The contribution in the left sum for the chord labeled $r$ is $d-(c-r)=r+(d-c)$, with $c,d$ not containing any $r$, so the contribution of $r$ in $\sum \varepsilon (a-b)$ is $r$. Now the variable $r$ is carried along the segments following the orientation of the circle in the chord graph. But note that each incoming positive/outgoing negative chord will both contribute $+r$ and move the horizontal position to the right. In the same way each outgoing positive/incoming negative chord will contribute $-r$ while moving to the left. Because we start and end at $k+\varepsilon$ these contributions of $r$ will cancel. This proves the result in the knot case or more generally in the case of arbitrary braid closures where different components have no crossings. Please check some of the arguments given in the example tbelow to see e. g. that the choice of $\beta$ in the potential does not change the equation. In order to discuss the non-trivial link case note that we can always change crossings and assume that component $j$ always overcrosses component $i$ for $j>i$ (see the argument in section 4). It will suffice to show that the equation is preserved under special Reidemeister II braid moves involving distinct components, and arbitrary Reidemeister III braid moves. Consider the following Reidemeister II move of distinct components.

::: center
![image](Figure17.pdf){width="90%"}
:::

*Figure 17*

If one of the strands is not included at any further mixed crossings then the corresponding cycle relation is $r+s=0$. In the figure we have a bottom negative crossing and the top crossing is positive. If we calculate $\sum \varepsilon r$ the contribution will be $-r+s=2s=-2r$. The contribution in $\varepsilon (a-b)$ is $$-[(d+r)-(c-r)]+(d-c)=-2r.$$ If both components of the Reidemeister II move are included in crossings with distinct components then we can change $r_1,r_2$ to $r_1',r_2'$ such that the equation will hold for the new diagram. We ignore the consideration of any self-crossings here. Note that the signs at the crossing slabeled $r_1, r_2$ does not matter. Again it can be checked that the equation will hold for the right diagram if and only if it holds for the left diagram. The discussion of Reidemeister III moves is in fact easier because all what has to be made sure is that the positions of $r_1,r_2,r_3$ in a diagram before a move and after the move are chosen correctly so that the contributions coincide. The remaining details are left to the reader. ◻
:::

::: exmp
Figure 18 shows the projection of the long component $2$-component link closure for $\beta =\sigma_1\sigma_2^{-2}\sigma_1^{-1}\sigma_2$.

::: center
![image](Figure18.pdf){width="60%"}
:::

*Figure 18*

The cycle relation is $r_1-r_2+r_3+r_4=0$. There are four crossings of the two components and one self-crossing of the second component. The base value of the part-arc at the base $*_2$ of the second component is set to $0$. It is easy to see that changing this value to $c\neq 0$ will not change the computation in the two sums considered in Proposition 6.2. Note that the signs at the five crossings from bottom to top are $(+,-,-,-,+)$. There will be a contribution of $c$ in $\sum \varepsilon (a-b)$ at each mixed crossing at which the second component crosses from the right and a $-c$ if it crosses from the left. In fact, the sign of $\pm c$ does not depend on the sign of the crossing. If we change the sign of a crossing then the roles of $a$ and $b$ in the computation change. At the self-crossing $c$ appears in both $a$ and $b$. So the reason is just that we *always* can set $c=0$ is that the crossing number of the second component with the first component is even. We calculate $$\begin{aligned}
\sum_c\varepsilon (a-b)=&+[r_1-(-r_1)] \\
&-[-r_1+r_2-r_4+r)-(r_1-r_2)]\\
&-[(r_1-r_2+r_3)-r]\\
&-[0-(-r_1-r_4)]\\
&+[(-r_1-r_4+r-0]\\
=&\ r_1-r_2-r_3+r_4+r\\
=&\ \sum_c \varepsilon r
\end{aligned}$$ We were lucky in that we did not have to use the cycle relation again to get the correct result. Of course we already used it at the third crossing to simplify. Note that $r$ appears three times but the contributions from $a-b$ calculated at crossings different from the one colored $r$ cancel out.
:::

The statements in the proposition above are non-trivial. They apply to each state-sum contribution individually. Thus we get the following strengthened result of Garoufalidis and Loebl including the statement that the understanding that the two state-sums are equivalent in the sense of Definition [\[defn: equivalency\]](#defn: equivalency){reference-type="ref" reference="defn: equivalency"}. Now consider the arc-graph corresponding to $\mathcal{K}$ and the coloring $f$ from the set of edges into $\mathbb{N}_0$ corresponding to [\[lem: flow lemma\]](#lem: flow lemma){reference-type="ref" reference="lem: flow lemma"}. The contributing states are given by restricting values to $f(v)\in \underline{n}$ for each vertex $v$ of $G\mathcal{K}$ (see [\[defn:edge coloring\]](#defn:edge coloring){reference-type="ref" reference="defn:edge coloring"}).

The quantity $-\frac{\varepsilon }{2}\sigma =bR$ is the *local excess*, and the sum over all vertices is the *excess* of the state.

The flow lemma identifies the coloring $b$ in Figure 10 with $f(e_v^b)$, and $f(e_v^r)$ is the jump $r$ in colors at a crossing $c$. Recall that overcrossing arcs are identified with vertices at their endpoints, so $$\sum_c \varepsilon b=\sum_v \varepsilon (v) f(e_v^b).$$ Identifying $R=\sum_{e<e_v^r}f(e)$ we define $$\textrm{exc}(f):=\sum_v\varepsilon (v)f(e_v^b)\sum_{e<e_v^r}f(e),$$ where we identity $R=\sum_{e<e_v^r}f(e)$ at each vertex. We use here that $R=a-r$. Finally following the definition of rotation of a state $f$ in [@GL], Definition B.6, we define $$\textrm{rot}(f):=\sum_{i=2}^{\mathfrak{s}} \beta_i(s)=\sum_{e'\in T(e)}f(e').$$ Here $T(e)\neq \emptyset$ only for $e_v^b,e_v^r$ for vertices corresponding to braid generators at the top of the braid. For $e_v^b$ we have $T(e)=\{e_v^b\}$ while for $e_v^r$ we have $\{e: e<e_v^r\}\cup \{e_v^r\}$. In each case this determines the color of the part arc, which is a closure arc of the braid diagram. Recall that the $\beta_i$ are the colors on the part-arcs at the top (or bottom) of the braid-closure diagram. See also the comments about rotation following the statement of Theorem 6.2.

Finally note that $\sum_v\varepsilon (v)=\omega (\mathcal{K})$ is the writhe of the projection. Let $\delta (f):=-(\textrm{exc}(f)+\textrm{rot}(f))$. It follows now from equation [\[eq=vertex contribution\]](#eq=vertex contribution){reference-type="eqref" reference="eq=vertex contribution"} and [\[eq=Fterm\]](#eq=Fterm){reference-type="eqref" reference="eq=Fterm"} that each state has an addition *total* multiplicative contribution of $$\delta '(\mathcal{K},n):=-\frac{n^2}{4}\omega (\mathcal{K})+\frac{n}{2}(\mathfrak{s}-1)$$ Next recall that $f(v)=f(e_v^b)+f(e_v^r)$

For each braid projection $\mathcal{K}$ of a framed link $K$ and $\delta (\mathcal{K}), \delta (f)$ as above we let $\mathcal{F}_{n}^*(G\mathcal{K})\subset \mathcal{F}_{n}(G\mathcal{K})$ be the set of $n$-flows, which will induce $0$ for the part arc framing of that part arc, which is the closure arc of the first braid string. This implies $f(e_w^b)=f(e)=0$ for $w$ the overcrossing arc preceding the overcrossing arc $v$ containing the bottom part arc of the first string. Here $e$ runs through all red edges preceding the $+$-marker on the fat vertex $v$ corresponding to $v$. If the closure part arc is on an overcrossing circle then the base value of this circle and all incoming red edge colorings are $0$. Now the following theorem has been proved:

::: thm
(see [@GL] for $0$-framed long knot projections) []{#thm:main label="thm:main"} The framed colored Jones polynomial can be calculated from a braid projection $\mathcal{K}$ by the following state-sum: $$\begin{aligned}
\label{eq=main formula}
\begin{split}
J_n'(K)&=t^{\delta '(\mathcal{K},n)}\sum_{f\in \mathcal{F}_{n}^*(G\mathcal{K})}t^{\delta (f)}
\prod_{v}t^{n\varepsilon (v)f(e_v^b)}{f(v) \choose f(e_v^b)}_{t^{-\varepsilon (v)}}\cdot \\ &
\cdot \{n-\sum_{e<e_v^r}f(e)\}_{f(e_v^r),t^{\varepsilon (v)}}
\in \mathbb{Z}[t^{\pm 1/4}]
\end{split}
\end{aligned}$$

Moreover, each state-sum contributions for this state-sum corresponds to the state-sum contribution for the state-sum defined for $\mathcal{P}\mathcal{K}$ defined in [@G] under the bijection of states defined in the flow lemma [\[lem: flow lemma\]](#lem: flow lemma){reference-type="ref" reference="lem: flow lemma"}. Thus the $R$-matrix state model [@GL] is equivalent to the state models on arc graphs [@GL] as defined in [\[defn: equivalency\]](#defn: equivalency){reference-type="ref" reference="defn: equivalency"}.
:::

For simplicity we have given the proof of the Garoufalidis-Loebl formula [@GL] for braid projections. The proof immediately generalizes to all Morse projections of links. The main difficulty is the extension of rotation numbers to Morse projections following [@T], see also [@GL], Definition B.6. Each Morse projection defines a *Gauss map* on $\mathcal{K}$ by the unit tangent vectors of the immersions along the components of $\mathcal{K}$. We know that the value $1\in S^1$ is a regular value with preimages the local maxima and minima. The Gauss map restricts to maps on part arcs and defines the *rotation numbers* in $\{0,\pm 1\}$ for each part arc with $\pm 1$ according to right oriented maxima respectively minima [@W]. If the rotation number of a part arc is $\neq 0$ then we will indicate this by $\pm$ in the boundary of the fat vertex corresponding to the overcrossing arc containing that part arc. Note that there can be several part arcs with nontrivial rotation number on a given overcrossing arc. The inclusion of only right oriented extrema comes from the more general ribbon functor definition of $\textrm{sl}(2,\mathbb{C})$ because those correspond to the *insertion* of right oriented evaluation and coevaluation maps. For each state on $G\mathcal{K}$, or $P\mathcal{K}$, the part arcs carrying nonzero rotation numbers will contribute factors of $t$ exponentiated by the part arc color for this state. In order to prove the formula [\[eq=main formula\]](#eq=main formula){reference-type="eqref" reference="eq=main formula"} we first consider special Morse projections for which at crossings all strings are directed upwards. Special Morse projections have additional properties with respect to extrema, e. g. a right going maximum is immediately followed by a right or left directed minimum on the same part arc. Which situation occurs is given by the rotation number of that part arc. So the rotation data controls left-right position on a grid, which is necessary to generalize the proof of Proposition [\[prop=2\]](#prop=2){reference-type="ref" reference="prop=2"} beyond the case of braid projections. Finally we use that every Morse projection easily can be isotoped by planar isotopy into a special Morse projection using local rotations at crossings. It is easy to see that the state-sum contributions will not change under those rotations.

::: rem
\(a\) For $0$-framed links $K$, $J_n'(K)\in \mathbb{Z}[t^{\pm 1/2}]$. This follows easily by the change of variables in Examples 1 and 2 above. Recall that for each framed link $K$ and $r\in \mathbb{Z}$ we let $K(r)$ denote the link with framing changed by $r$ twists. Then we have $$J_n'(K(r))=t^{-r(\frac{n^2}{4}+\frac{n}{2})}J_n'(K)$$ For a framed link $K$ with projection and corresponding writhe $\omega (\mathcal{K})$ the writhe is the total framing, and $$J_n'(K(-\omega (\mathcal{K}))=t^{\omega (\mathcal{K})(\frac{n^2}{4}+\frac{n}{2})}J_n'(K).$$ The unframed (or better framing corrected) version of the colored Jones polynomial thus is computed from an arbitrary projection by the relation $$J_n(K):=t^{\omega (\mathcal{K})(\frac{n^2}{4}+\frac{n}{2})}J_n'(K).$$ If we define $$\begin{aligned}
\delta (\mathcal{K},n)&:=\delta '(\mathcal{K},n)+\omega (\mathcal{K} )(\frac{n^2}{4}+\frac{n}{2})\\
&=\frac{n}{2}(\omega (\mathcal{K})+\mathfrak{s}-1))
\end{aligned}$$ and replace $\delta '(\mathcal{K},n)$ by $\delta (\mathcal{K},n)$ we get the state-sum formula for the unframed colored Jones polynomial from the theorem. It follows that $J_n(K)\in \mathbb{Z}[t^{\pm 1/2}]$.

For $n=1$ we have the skein relations for framed links: $$t^{-1/4}J'(K_+)-t^{1/4}J(K_-)=(t^{-1/2}-t^{1/2})J(K_0)$$ and the corresponding writhe normalized for the unframed version: $$t^{-1}J(K_+)-tJ(K_-)=(t^{-1/2}-t^{1/2})J(K_0).$$

This is not the standard relation for the Jones polynomial derived from the Kauffman bracket but differs by a relative sign of the two sides. It corresponds to the relation in [@GL], Appendix B, and [@RT], Theorem 4.2.1. Because the number of components of $K_{\pm}$ and $K_0$ differs by v$1$ modulo $2$ for each skein triple it follows that the corresponding invariants only differ by sign.

In fact, for the standard skein relation the Jones polynomials of even number component links carry an additional $-$ sign if the normalization on the unknot is kept. Since the colored Jones polynomial can be calculated from $n$-parallels the sign correction will only occur for $n$ odd (like in the classical case).

In fact, the mod $2$ number of components is nicely related to $\delta (\mathcal{K},n)$ as follows: Let $K=\hat{\beta }$ and $|K|$ the number of components of $K$. We assume that $\beta$ is a $\mathfrak{s}$-braid. Note that the mod $2$ number of transpositions in the permutation carried by $\beta$ is equal to $\omega (\mathcal{K})$, while the number of cycles in the disjoint cycle decomposition is $K$. Let $\ell_i$ be the length of the $i$-th cycle and recall that each cycle of length $\ell_i$ can be written with $\ell-i-1$ transpositions. Thus we have the equations: $$\sum_{i=1}^{|K|}(\ell_i-1)\equiv \omega (K), \quad \sum_{i=1}^{|K|}\ell_i=\mathfrak{s}$$ It follows that if $n$ is even, or $|K|+1\equiv \omega (\mathcal{K})+\mathfrak{s}-1\equiv 0\ \textrm{mod}\ 2$, or the number of components of $K$ is odd, then $\delta (\mathcal{K},n)\in \mathbb{Z}$ and it follows that $J_n(K)\in \mathbb{Z}[t^{\pm 1}]$. On the other hand, if $n$ and $|K|$ are odd then $J_n(K)\in t^{1/2}\mathbb{Z}[t^{\pm 1}]$. This coincides with the skein relation deduced of $J=J_1$ above.

b\) For $sl(N+1)$ in the fundamental representations the quantum invariants determine the HOMFLY polynomial. In this case the [st]{.roman}-condition translates to flows on $G\mathcal{K}$ satisfying the condition: If $f(e_v^r)\neq 0$ then $f(e_v^b)=\sum_{e<e_v^r}f(e)$ for $N$-flows.

\(c\) Let $\overline{K}$ be the reflected link and $\overline{\mathcal{K}}$ be correspondingly the reflected projection. Then $G_+\overline{\mathcal{K}}=\overline{(G_-\mathcal{K})}$, where the bar over the graph denotes switching the signs of the vertices.

Using this and $J_n(\overline{K})(t)=J_n(K)(t^{-1})$, it is easy to derive a formula calculating $J_n(K)$ from $G_-\mathcal{K}$. It should be noted that the graphs $G\mathcal{K}$ and $G(\overline{\mathcal{K}})$ are usually very different as oriented graphs and thus give rise to very different state-sums calculating the same link polynomial, up to $t\mapsto t^{-1}$. A trivial component contributes $t^{1/2}+t^{-1/2}$ for our skein relation but $-(t^{1/2}+t^{-1/2})$ in the standard case.

\(d\) It should have become clear by now that the arc graph is just an equivalent representation of exactly the data necessary to be taken from the part arc-graph necessary to define either of the two state-sums. In fact, after labeling the overcrossing arcs in cyclic way all what is needed are the jumps at the crossings for $f(e_v^r)$ and the part-arc colors of outgoing undercrossing part arcs for $f(e_v^b)$. The real assertion of formula 6.2, or its generalization to Morse projection, is contained in Propositions 6.1 and 6.2, which are generalizations of Lemma B.5 in [@GL] or Lemma 2.1-2.4 in [@Li]. The main arguments for $n=1$ here are already contained in [@T], sections 5 and 6. It seems that the *integration* of certain state-sum contributions simplifies the computation using formula 6.2 over the usual $R$-matrix formula. The remaining steps are just rewriting of quantum algebra expressions.
:::
