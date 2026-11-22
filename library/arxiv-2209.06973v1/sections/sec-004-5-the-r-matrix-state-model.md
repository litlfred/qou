---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-004-5-the-r-matrix-state-model
section_title: "The R-matrix state model"
section_number: 5
pages: 17-23
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.996
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
We review and reformulate the state model for the framed colored Jones polynomial $J_n$ as defined in [@G]. Recall that $n$ labels the $(n+1)$-dimensional standard irreducible representation of $\textrm{sl}(2,\mathbb{C})$, or the corresponding type **1** $U_q(\textrm{sl}(2,\mathbb{C})$-module, see [@J], 5.2. Our normalization will coincide with [@GL] so that $n=1$ corresponds to the trivial $2$-dimensional representation and the classical Jones polynomial. Link components will all be colored by the same representation. We will use the word *coloring* for the edge-colorings of the projection graphs only. Throughout $\varepsilon (v)$ will denote the sign of the crossing $v$ (vertex of the part arc-graph $P\mathcal{K})$. Moreover, in [@G] a variable $v$ is used for $J_n$ while we will use the variable $v^2=t$ in this paper, which corresponds up to a change from $t$ to $t^{-1}$ to the variable $t$ in [@GL]. So our variable $t$ corresponds to $q$ in [@G] and $t^{-1}$ in [@GL]. While describing the state-sum formula of [@G] we will already rewrite all formulas to variable $t$. This includes rewriting quantum symbols in corresponding crossing-sign dependent functions, which are used in [@GL].

Let $a,b\in \mathbb{Z}$. Then $$\{a\}:=v^a-v^{-a}=v^{-a}(v^{2a}-1)=( t^{a/2}-t^{-a/2}=t^{-a/2}(t^a-1).$$ and $$[a]=\frac{\{a\}}{\{1\}}=\frac{v^a-v^{-a}}{v-v^{-1}}=v^{a-1}(1+v^{-2}+\cdots +v^{-2(a-1)})$$ This corresponds to $$[a]=t^{\frac{a-1}{2}}(1+t^{-1}+\cdots +t^{-(a-1}).$$ This is mostly important for normalization. The $n$-th colored Jones polynomial of the unknot will be $[n+1]$. In fact if a framed link $L$ contains $k$ trivially framed unknotted and unlinked components then $J_L=[n+1]^kJ_{L'}$, where $L'$ is the link defined from $L$ by omitting the unknotted and unlinked components, see [@G].

For $b\geq 0$ we define the *Pochhammer symbol* $$\begin{aligned}
\begin{split}
\{a\}_b&=\{a\}\{a-1\}\cdots \{a-b+1\}\\
&=t^{-ab/2+b(b-1)/4}(t^a-1)(t^{a-1}-1)\cdots (t^{a-b+1}-1) \\
&=(-1)^bt^{-ab/2+b(b-1)/4}(1-t^a)(1-t^{a-1})\cdots (1-t^{a-b+1}) \\
&=t^{ab/2-b(b-1)/4}(1-t^{-a})(1-t^{-(a-1)})\cdots (1-t^{-(a-b+1)})
\end{split}
\end{aligned}$$ and for $b<0$, $\{a\}_b:=0$. We will relate the above definition to the *sign-dependent* Pochhammer symbol (not used by [@GL] but we will use in rewriting their formula) defined by $$\{a\}_{b,t}:=\prod_{s=0}^{b-1}(1-t^{a-s})$$ with $\varepsilon \in \{\pm 1\}$. $$\label{eq=Pochhammer}
\{a\}_b=(-1)^{(1+\varepsilon )\frac{b}{2}}t^{-\varepsilon (\frac{ab}{2}-\frac{b(b-1}{4})}\{a\}_{b,t^{\varepsilon }}$$

It follows for $b\geq 0$ from the definitions in [@G]: $${a \choose b}:=\frac{\{a\}_b}{\{b\}_b}=t^{b(b-a)/2}\frac{(t^a-1)\cdots (t^{a-b+1}-1)}{(t^b-1)\cdots (t-1)}$$ Note that the expression on the right hand side is not defined for $b=0$, and is defined to be $1$ in this case. As above these quantum binomials are related to the sign-dependent versions in [@GL] as follows: $(a)_t:=\frac{t^a-1}{t-1}$ and $(a)_t!:=(1)_t(2)_t\cdots (a)_t$ and $${{a}\choose {b}}_t:=\frac{(a)_t!}{(b)_t!(a-b )_t!}=\frac{(t^a-1)\cdots (t^{a-b+1}-1)}{(t^b-1)\cdots (t-1)}$$ and thus $$\label{eq=binomial}
{a \choose b}=t^{\varepsilon b(b-a)/2}{{a}\choose {b}}_{t^{\varepsilon }}$$ This follows because $$\begin{aligned}
{{a}\choose {b}}_{t^{-1}}&=\frac{(t^{-a}-1)\cdots (t^{-(a-b+1)}-1)}{(t^{-b}-1)\cdots (t^{-1}-1)} \\
&=\frac{t^{-(a+(a-1)+\cdots (a-b+1))}}{t^{-(b+(b-1)+\cdots +1)}}{a\choose b}_t\\
&=t^{b(b-a)}{a\choose b}_t
\end{aligned}$$

We will use the following well-known lemma for the *symmetry* of quantum binomials:

::: lem
[]{#lem=binomial symmetry label="lem=binomial symmetry"} For $c,d$ nonnegative integers we have $${c+d \choose c}={c+d \choose d}$$
:::

::: proof
*Proof of lemma.* We have the formula: $${c+d\choose c}=t^{-cd/2}\frac{(t^{c+d}-1)\cdots (t^{d+1}-1)}{(t^c-1)\cdots (t-1)}$$ If $c\leq d$, multiplying both numerator and denominator on the right hand side by $$(t^d-1)\cdots (t^{c+1}-1)$$ and noting that $d(d-(c+d))=c(c-(c+d))$ the result follows. If $d<c$ both numerator and denominator contain the product $$(t^c-1)\cdots (t^{d+1}-1),$$ so after cancellation the result follows in this case too. ◻
:::

Note that by formula [\[eq=binomial\]](#eq=binomial){reference-type="eqref" reference="eq=binomial"}, $${c+d\choose c}=t^{-\varepsilon cd/2}{c+d\choose c}_{t^{\varepsilon }}$$ and $${c+d\choose d}=t^{-\varepsilon dc/2}{c+d\choose d}_{t^{\varepsilon }}$$ so that symmetry of quantum binomials also holds for the sign-dependent versions.

The formula in Proposition 3.7 of [@G] generalizes to link projections, as described in [@G], Remark 3.5, in the following way: Let $\mathcal{F}_{-,*}^n$ be the set of all colorings $(-)$ of the part arc-graph $P\mathcal{K}$ of a link projection $\mathcal{K}$ as defined in section 2. We we assume that the first strand of the braid projection is colored $0$ at the bottom, which is indicated by $*$. Let $J'_n(K)$ be the framed colored Jones-polynomial [@G], we will discuss more details in section 6. Let $\mathfrak{s}$ be the number of braid strings and let $\{c_1,\ldots c_{\mathfrak{c}}\}$ be the set of crossings in the braid projection. Then $$J'_n(K)=\sum_{s\in \mathcal{F}_{-,*}^n}F(n,s)$$ where $F(n,s)$ is the product $$\label{eq=Fterm}
F(n,s):=\prod_{\ell=2}^{\mathfrak{s}}v^{-n+2b_{\ell }(s)}\prod_{k=1}^{\mathfrak{c}}f_{\varepsilon (c_k)}(n,i(k,s),j(k,s),r).$$ Here $i(s),j(s)$ are the colors at the crossing $c_k$ determined by the state $s$ and the following convention (colors are decreasing on overcrossings):

::: center
![image](Figure8.pdf){width="80%"}
:::

*Figure 8*

with the functions $f_{\pm }$ are defined by (see [@GL], 3.1, [@Ja], Chapter 3, and [@KiM], 2.32 and 2.34) $$\label{eq=positive crossing}
f_+(n,i,j,r):=(-1)^rv^{-((n-2i)(n-2j)+r(r-1))/2}{j+r \choose r}\{n+r-i\}_r$$ while the contribution at a negative crossing will be $$\label{eq=negative crossing}
f_-(n,i,j,r):=v^{((n-2i-2r)(n-2j+2r)+r(r-1))/2}{i+r \choose r}\{n+r-j\}_r.$$

::: rem
\(a\) What is called state $s$ in [@G] in the long knot case we call a potential inducing the state on the part arc-graph with part arc colorings $(i(s),j(s))$ on part arcs labeled by the crossings. In order to be able to include overcrossing circles without crossings in the link case restrict the values of $r,\beta_j$ to $\underline{n}$ so that the colorings at extrema are in $\underline{n}$.

\(b\) Some care has to be taken when considering the above formula for the state-sum with Proposition 3.7 in [@GL] for the long knot case. Garoufalidis and Loebl sum over all possible nonnegative jumps at vertices, noticing that the quantum algebra definitions will set state-sum contributions to $0$ if colorings of part arcs are $>n$. This will not be true in the link case because of the $b_i(s)$ in the formula because there can be overcrossing circles such that the maximim is not connected to a crossing at which the label $b_i(s)$ appears. We have to restrict the state space so that all part arc colors are $\leq n$, or only consider projections without overcrossing circles. Note that the set of contributing states is usually much more restricted by the requirement that all induced part arc colors $c$ (defined from a given potential) satisfy $c\in \underline{n}$.
:::

The following examples will show the dependence of state-sums on the framing. We will also be able to state the skein relation of the classical Jones polynomial in the framed case, which is of course related to a modification of the Kauffman bracket.

::: exmp
If we represent the unknot by the empty braid then there is a unique state with color $0$ on the single strand, and the state-sum gives $J'_n(U)=1$ for all $n$. The corresponding vertex product is empty because there is no crossing. It is known that the colored Jones polynomial is changed by a power of $v$ if we change the framing in the first component of a link (see [@L], (1.7)). If we use the closure of the braid $\sigma_1$ to represent the unknot $U(1)$ with framing $+1$ the decreasing condition at the single vertex implies that the only state is the all-$0$ state and $J'_n(U(1))=v^{-n^2/2-n}$. On the other hand if we use $\sigma_1^{-1}$ to represent $U(-1)$, the $-1$-framed unknot, then we get states labeled by $0\leq r\leq n$ for a single crossing.

::: center
![image](Figure9.pdf){width="30%"}
:::

*Figure 9*

Using ${r \choose r}=1$ the following state-sum results for $U(-1)$:

$$\begin{aligned}
J_n'(U(-1))&=\sum_{0\leq r\leq n}v^{-n+2r}v^{\left(n(n-2r)+r(r-1)\right)/2}\{n\}_r\\
&=v^{n^2/2-n}\sum_{0\leq r\leq n}v^{r(2-n)+\frac{r(r-1)}{2}}\{n\}_r,
\end{aligned}$$

and thus the following identity for the well-known $q$-Pochhammer symbol:

$$\sum_{0\leq r\leq n}v^{r(2-n)+\frac{r(r-1)}{2}}\{n\}_r=v^{2n},$$

which is easily proved by induction using $\{n+1\}_{r+1}=(v^{n+1}-v^{-(n+1)})\{n\}_r$. For $n=1$ and $\{1\}_0=1$ (empty product) and $\{1\}_1=v-v^{-1}$ the right hand side is $$1+v(v-v^{-1})=v^2$$ The induction step gives: $$\begin{aligned}
\ &1+\sum_{1\leq r\leq n+1}v^{r(2-(n+1))+\frac{r(r-1)}{2}}\{n+1\}_{r}\\
=&1+\sum_{0\leq r\leq n}v^{(r+1)[2-(n+1)]+\frac{r(r+1)}{2}}(v^{n+1}-v^{-(n+1)})\{n\}_r\\
=&1+v^2\cdot v^{2n}-v^{-2n}\cdot v^{2n}\\
=&v^{2(n+1)}
\end{aligned}$$
:::

::: exmp
We consider the case $n=1$. The framed Jones polynomial $J'=J_1'$ defined by the state-sum [@G] above satisfies the skein relation $$v^{-1/2}J'(K_+)-v^{1/2}J'(K_-)=(v^{-1}-v)J'(K_0)$$ and $J'(U)=1$ for $U$ the trivially framed unknot (represented by the $1$-braid closure of a single strand), $J'(K\sqcup U)=(v^{-1}+v)J'(K)$ for each non-empty framed link $K$, and $$J'(K(1))=v^{-3/2}J'(K).$$ It is a good exercise to check the skein relation follows directly from the formula above: For $n=1$ only $r=0$ and $r=1$ are possible values at a crossing. For a given $\mathcal{K}$ and crossing we can divide the set of states at a crossing into $\mathcal{F}_{(\pm ,r)}$ with $r\in \{0,1\}$. For $r=0$ there are all colors $0$ or $1$ states possible for both the positive and negative crossing. For $r=1$ the sign of the crossing determines the possible part arc colorings at the crossing. For the Conway smoothing $K_0$ at the crossing the states are naturally divided into subsets by the two part arcs colored as $(\textrm{left},\textrm{right})$: $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$. Now the all $0$, respectively all $1$-states, in $\mathcal{F}_{(\pm ,0)}$ correspond to $(0,0)$ and $(1,1)$-states of the smoothing. The vertex contribution of the crossing at the positive crossing is $v^{-1}$ while the contribution at the negative crossing is $v$, corresponding to the states on $K_0$ multiplied by $v^{-1}-v$. Recall that $\{1\}_1=v-v^{-1}$. For $r=1$ admissibility reduces the colorings at the positive crossing to $i=1$ and $j=0$ and the formula for $f_+$ shows vertex contribution $(-1)^1v^{-(1-2)/2}\{1\}_1$, which multiplied by $v^{-1/2}$ contributes the factor $-(v-v^{-1}=v^{-1}-v$ for each corresponding $(1,0)$-state of the smoothing, while the formula for $f_-$ shows vertex contribution $v^{(1-2)/2}\{1\}_1$, which multiplied by $-v^{1/2}$ also contributes $v^{-1}-v$ as a factor but this time to the $(0,1)$ states on $K_0$. If we use the usual writhe normalization we have the definition of the unframed Jones polynomial $$J(K)=v^{\frac{3}{2}\omega (\mathcal{K})}J'(\mathcal{K})$$ Substituting in the skein relation for framed links above and using $]\omega (K_{\pm})=\omega (K_0)\pm 1$ where we use the notation for the link instead of the projection, we get $$v^{-2}J(K_+)-v^2J(K_-)=(v^{-1}-v)J(K_0)$$
:::

::: rem
We note that in the formula for $F$ in [@G], Proposition 3.7 the variable $v$ has to be replaced by $q$ and thus we have a factor $2$ additionally. This for example can easily be seen from the calculations of $J_n'$ for the examples above.
:::
