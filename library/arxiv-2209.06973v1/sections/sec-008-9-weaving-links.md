---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-008-9-weaving-links
section_title: "Weaving links"
section_number: 9
pages: 51-58
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.991
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
Recall our notation for $a$ a positive integer, $\underline{a}:=\{0,1,\ldots ,a-1\}$.

In this section we consider only braids with zero writhe and three strands. In this case the framed and unframed colored Jones polynomial coincide. The colored Jones polynomial will take values in $\mathbb{Z}[t^{\pm 1/2}]$, in fact in $\mathbb{Z}[t^{\pm 1}]$ in the case of knots or $n$ even. For $\mathfrak{s}=3$ we have: $$\delta (\mathcal{K},n)=\delta '(\mathcal{K},n)=n.$$ and vertex contributions for states as in equation [\[eq=vertex contribution\]](#eq=vertex contribution){reference-type="eqref" reference="eq=vertex contribution"}.

We will consider those *weaving links*, which are defined by the following alternating $3$-braid closures: $$\left((\sigma_1^{-1}\sigma_2)^m\right)^{\wedge}=\overline{W(3,m)}.$$ For $m\equiv 1\ \textrm{mod}\ 3$ and $m\equiv 2\ \textrm{mod} \ 3$ the closure of the braid is a knot, for $m\equiv 0 \ \textrm{mod} \ 3$ the closure is a $3$-component link. Note that all links $K=W(3,m)$ are amphichiral and therefore $J_n(K)=J_n(\overline{K})$. Note that for $m=3\ell +1$ the induced cycle permutation is $(132)$ respectively for $m=3\ell +2$ it is $(123)$. In the case of weaving links the cyclic order of overcrossing arcs by $k\in \underline{2m-1}$ will be such that $\varepsilon (k)=(-1)^{k+1}$.

In the following we will focus on an explicit description of the jump maps $\tau$, rotation and excess, because these are the main ingredients to apply [\[thm:GL2\]](#thm:GL2){reference-type="ref" reference="thm:GL2"}. The braid projections are alternating and thus $\tau$ is a bijection. For small $\ell$ we can explicitly describe the recursion to determine $\mathbf{i}$ from $\mathbf{j}$, and the inequalities for the sets of contributing states. But in general, it seems better to just refer to the general formula [\[eq=contributing\]](#eq=contributing){reference-type="eqref" reference="eq=contributing"}.

**(a)** Let $\ell \geq 1$ and $$K=\left((\sigma_1^{-1}\sigma_2)^{3\ell +1}\right)^{\wedge}=\overline{W(3,3\ell +1)}$$ with corresponding long component projection $\mathcal{K}$ with $6\ell +2$ crossings. For $\ell =0$ we have $\sigma_1^{-1}\sigma_2$, which is braid representation of the unknot. It is a nice exercise to check that the formula gives the polynomial $1$ in this case.

We can work with the reduced arc graph and thus describe a contributing state (in our case $\tau^{-1}(0)=2\ell$). $$\mathbf{j}=(j_1,j_2,\ldots ,j_{6\ell +1}), j_{2\ell }=0$$ and $$\mathbf{i}=(i_1,i_2,\ldots ,i_{6\ell })$$ We have for $k\in \underline{6\ell +1}$: $$\tau (k)=k+4\ell +2\ \textrm{mod}\ (6\ell +2),$$ the modulus is defined in $\underline{6\ell +1}$, or $\tau^{-1}(k)=k+2\ell \ \textrm{mod} (6\ell +2)$. Recall that we set $i_0=j_0=0$. The contributing states are described by a vector of length $6\ell$ with entries in $\underline{n}$ subject to $6\ell -1$ [double inequalities]{.roman} for contributing states [\[eq=contributing\]](#eq=contributing){reference-type="eqref" reference="eq=contributing"}. But there is only one inequality for vertex $2\ell$, $i_{2\ell -1}+j_{4\ell }\leq n$.

![image](Figure23-1.pdf){width="50%"} ![image](Figure23-2.pdf){width="50%"}

*Figure 23*

We have $\textrm{rot}(f)=(i_{2\ell }+j_{4\ell +1})+i_{4\ell +1}$ and $$\textrm{exc}(f)=-\sum_{k=1}^{6\ell +1}(-1)^{k+1}i_ki_{\tau (k)-1}.$$ See Figure 21 for the rotation and see the arc graph for the braid projection of $W(3,4)$ below in Figure 22. Thus $\delta (\mathbf{j})=-(i_{2\ell }+j_{4\ell +1}+i_{4\ell +1})+\sum_{k=1}^{6\ell +1}(-1)^ki_ki_{\tau (k)-1}$.

::: wrapfigure
l7.5cm ![image](Figure24.pdf){width="7.5cm" height="11cm"}

*Figure 24*
:::

For $\ell =1$ we are calculating the colored Jones polynomial of the weaving knot $W(3,4)$, which is the knot $8_{18}$. The figure shows the long braid representation of this knot and coloring according to [@G].

Figure 21 shows the corresponding arc graph-graph according to [@GL] with colorings. Note that it is our specific choice of braid (starting with a negative braid generator and ending with a positive braid generator), which allows to discard the first overcrossing arc (which we label $0$). The system of equations restricting the values of the vector $\mathbf{j}$ by the non-negativity of the vector $\mathbf{i}$ and $n$ are now obvious from the figure. We would like to point out that working out the restriction to contributing states seems the most challenging piece of the computation. In the case of weaving links this can be reduced to periodicity according to the value of $\ell$. In general we will get a linear system of inequalities restricting the values to an intersection of half-spaces. For $\ell =1$ the system of inequalities can be reduced in the following way for the coefficients of the vector (see [\[eq=contributing\]](#eq=contributing){reference-type="eqref" reference="eq=contributing"}): $$\mathbf{j}'=(j_1,j_3,j_4,j_5,j_6,j_7)\in (\underline{n+1})^6$$ $$\begin{aligned}
j_1&\leq \textrm{min} \{j_3,j_4+j_5.j_5+j_6\}\\
\textrm{max} \{j_3+j_4,j_4+j_5,j_5+j_6\}&\leq n
\end{aligned}$$ The main question seems to be to get a direct geometric understanding of those inequalities in terms of the geometry of the links.

::: center
![image](Figure25.pdf){width="100%"}
:::

*Figure 25*

**(b)** Let $\ell \geq 0$ and consider the knots $$K=\left((\sigma_1^{-1}\sigma_2)^{3\ell +2}\right)^{\wedge}=\overline{W(3,3\ell +2)}$$ with corresponding braid projection $\mathcal{K}$. For $\ell =0$ we have $(\sigma_1^{-1}\sigma_2)^2$, which is the figure eight knot. The next knot in this series is $W(3,5)$, which is the knot $10_{123}$. The description of the set of contributing states is very similar to (a): $$\mathbf{j}=(j_1,\ldots ,j_{6\ell +3}) \ \textrm{with}\  j_{4\ell +2}=0$$ with $\mathbf{i}=(i_1,\ldots ,i_{6\ell +2})\in (\underline{n+1})^{6\ell +2}$ is determined by [\[eq=cycle i\]](#eq=cycle i){reference-type="eqref" reference="eq=cycle i"} with $$\tau (k)=k+2\ell +2\ \textrm{mod}\ (6\ell +4)$$ and the inequalities determining the contributing states are given by [\[eq=contributing\]](#eq=contributing){reference-type="eqref" reference="eq=contributing"}. Note that the braid word contains $6\ell +4$ braid generators. Taking into account $j_{4\ell +2 }=0$ we describe states by vectors with values in $\underline{n+1}$ of length $6\ell +2$. We have $$\textrm{rot}(f)=(i_{4\ell +2}+j_{2\ell +1})+i_{2\ell +1}$$ and $$\textrm{exc}(f)=\sum_{k=1}^{6\ell +2}(-1)^ki_ki_{\tau (k)-1},$$ and thus $\delta (\mathbf{j})=-(i_{4\ell +2}+j_{2\ell +1}+i_{2\ell +1})+\sum_{k=1}^{6\ell +2}(-1)^ki_ki_{\tau (k)-1}$.

**(c)** Now for $m=3\ell$ and $\ell \geq 1$ we consider the weaving links $W(3,3\ell )$ with $3$ components. The corresponding braid word includes $6\ell$ braid generators. The resulting links are Brunnian, in fact $W(3,3)$ is the Borromean classical rings link.

The non-negativity requirement for contributing states and basing of $0$ on the long strand immediately implies $j_0=j_{6\ell -2}=0$. The following two cycle relations have to hold for each coloring (note that the relation for the first component follows from the other two as we know):

$$\begin{aligned}
j_1+j_2+\cdots +j_{2\ell -1}=j_{2\ell}+j_{2\ell +1}+\cdots +j_{4\ell -2}+j_{4\ell -1}\\
j_{2\ell}+j_{2\ell +1}+\cdots +j_{4\ell -2}+j_{4\ell -1}=j_{4\ell }+j_{4\ell +1}+\cdots +j_{6\ell -1}
\end{aligned}$$

We use the equations to eliminate $j_{2\ell }$ and $j_{4\ell }$ but will use them in subsequent inequalities: $$j_{2\ell }=j_1+\cdots j_{2\ell -1}-(j_{2\ell +1}+\cdots +j_{4\ell -1})$$ respectively $$\begin{aligned}
j_{4\ell }&=j_{2\ell }+\cdots j_{4\ell -1}-(j_{4\ell +1}+\cdots j_{6\ell -1})\\
&=j_1+\cdots j_{2\ell -1}-(j_{4l+1}+\cdots +j_{6\ell -3}, j_{6\ell -1})
\end{aligned}$$

::: wrapfigure
l7.5cm ![image](Figure26.pdf){width="7.5cm" height="13cm"}

*Figure 26*
:::

Just like in the knot cases we can determine the set of contributing states $\mathcal{F}_n^*(G\mathcal{K})$. Each contributing state is determined by a vector $$\mathbf{j}=(\mathbf{j}(1),\mathbf{j}(2),\mathbf{j}(3),\beta_1,\beta_2)$$ with components in $\underline{n+1}$. We $\mathfrak{c}(1)=\mathfrak{c}(2)=\mathfrak{c}(3)=2\ell$. The vector $\mathbf{i}$ determined from the system of equations [\[eq=cycle i\]](#eq=cycle i){reference-type="eqref" reference="eq=cycle i"}.

Using the base value on the first component and the two cycle relations above we can omit the first components in the vectors $\mathfrak{j}(\ell )$, and so have $$\begin{aligned}
\mathbf{j}(1)&=(j_1,\ldots ,j_{2\ell -1})\\
\mathbf{j}(2)&=(j_{2\ell +1},\ldots ,j_{4\ell -1})\\
\mathbf{j}(3)&=(j_{4\ell +1},\ldots ,j_{6\ell -3},j_{6\ell -1})
\end{aligned}$$ We have $j_{6\ell -}=j_{\tau^{-1}(0)}=0$.

These vectors satisfy a system of inqualities see [\[eq=contributing\]](#eq=contributing){reference-type="eqref" reference="eq=contributing"} determining the contributing states, in fact one system for each cycle.

Figure 27 shows the corresponding arc-graph.

     

::: center
![image](Figure27.pdf){width="100%"}
:::

*Figure 27*

The jump map is given by: $$\tau (k)=\begin{cases}
k+2\ell \ \textrm{mod}\ 6\ell & \textrm{if} \ k=1,\ldots, 4\ell -1\\
k+2\ell +2\ \textrm{mod}\ 6\ell & \ \textrm{if} \ k=4\ell ,\ldots , 6\ell -1
\end{cases}$$

::: rem
The classical Jones polynomials $J(W(3,m))$ have also been recently computed by Mishra and Staffeldt in [@MS] using recursion in the Hecke algebra.
:::
