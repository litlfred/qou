---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-007-8-working-with-cyclic-ordering
section_title: "Working with cyclic ordering"
section_number: 8
pages: 47-51
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.989
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
In the following we assume that our projection $\mathcal{K}$ is based and we consider the cyclic ordering with respect to the basing. This defines a bijection $V\leftrightarrow \underline{\mathfrak{c}-1}$ with $\mathfrak{c}$ denoting the number of crossings. The base vertex on the first component is labelled $0$ by the order because it is deleted in reduced graphs. We will usually identify vertices with their order labeling. The parametrization of the set of states is now given by integer valued vectors $\mathbf{j}=(j_0,\ldots ,j_{\mathfrak{c}-1})$, possibly with components removed, or just set equal to $0$, in the reduced case. The vector $\mathbf{i}=(i_0,\ldots ,i_{\mathfrak{c}-1})$ is similarly defined.

With respect to this ordering the undercrossing map has a simple description $\sigma$ is now given by $$\sigma (k)=k+1\ \textrm{mod}\ (\mathfrak{c}-1),$$ where we will as usual think of $a \textrm{mod}\ b$ for integers $a,b$ and $b>0$ as an element in $\underline{b}=\{0,1,\ldots ,b-1\}$. Theorem [\[thm:GL2\]](#thm:GL2){reference-type="ref" reference="thm:GL2"} can be rewritten, now writing $i_k, j_k,\varepsilon (k)$ etc. for $i_v, j_v,\varepsilon (v)$ if $v$ is the vertex $k$. The jump map $\tau$ now becomes a map $$\tau : \underline{\mathfrak{c}}\rightarrow \underline{\mathfrak{c}}.$$ Recall that this a bijection if and only if $\mathcal{K}$ is an alternating projection.

In the case of a link of $\mu >1$ components some more notation will be necessary. Suppose that the number of overcrossing arcs on the $\ell$-th component is $\mathfrak{c}(\ell )$. Then define $$\mathfrak{d}(\ell ):=\mathfrak{c}(1)+\cdots +\mathfrak{c}(\ell )$$ for $\ell =1,\ldots ,\mu$, and let $\mathfrak{c}(0):=0$. Then we enumerate the overcrossing arcs on the $\ell$-th components in the following way $$\mathfrak{d}(\ell -1),\mathfrak{d}(\ell -1) +1,\ldots ,\mathfrak{d}(\ell )-1$$

In the reduced case we have $i_0=0$ and $i_{\mathfrak{c}(\ell -1)}=\beta_{\ell }$ is determined by the potential for $\ell =2,\ldots ,\mu$. As explained in section 7 we can determine the colors $i_k$ from the vector $$\mathbf{j}=(j_1,\ldots ,j_{\mathfrak{c}-1})$$ Note that he vector is partitioned by components into $\mathbf{j}=(\mathbf{j}(1),\ldots ,\mathbf{j}(\mu ))$ with $$\mathbf{j}(1)=(j_1,\ldots ,j_{\mathfrak{d}(1)-1})$$ and for $\ell \geq 2$, $$\label{eq=comp}
\mathbf{j}(\ell )=(j_{\mathfrak{d}(\ell -1)},\ldots ,j_{\mathfrak{d}(\ell )-1})$$

We always have to take into account the $\mu -1$ cycle relations. In order to determine these we have to first find for each $1\leq \ell \leq \mu$ those numbers $k$ for which the corresponding overcrossing arc ends at a crossing of distinct components, say for a fixed $\ell$ these are $k_1,\ldots ,k_{\rho }$. Finally we have to determine for which overcrossing arcs $k$, $\tau^{-1}(k)$ is an overcrossing arc of a component distinct from the $\ell$-th, say those are $m_1,\ldots ,m_{\rho'}$. Then the cycle relation for the $\ell$-th component is $$\sum_{r=1}^{\rho '}j_{\tau^{-1}(m_r)}-\sum_{r=1}^{\rho }j_{k_r}=0$$ Note that $\rho +\rho '$ is always an even number. The system of equations to find $\mathbf{i}$ from $\mathbf{j}$, given $i_{\mathfrak{c}(k-1)}$ for $k=2,\ldots ,\mu$ is given by the flow equations, equalities to determine the contributing states then are found as explained in section 7.

We will now briefly show how to find the set of contributing states for a $2$-component alternating braid projection $\mathcal{K}=\hat{\beta }$. We assume that the first appearance of the braid generator $\sigma _1$ will be corresponding to vertex $0$ and comes as $\sigma_1^{-1}$. This will allow us to work with the reduced graph. Let $\tau^{-1}(0)=:\kappa$.

We have crossings $0,1,\ldots ,\mathfrak{c}(1)-1$ along the first component, and\
$\mathfrak{c}(1),\ldots ,\mathfrak{c}-1$ with $\mathfrak{c}=\mathfrak{c}(1)+\mathfrak{c}(2)$ along the second component, the number of crossings of $\mathcal{K}$. The potential is given by $(\mathbf{j},\beta_2)$ and we assume that $\beta_2=i_{\mathfrak{c}(1)}$. Fiigure 21 shows the arc-graph for a $2$-component alternating link.

![image](Figure21.pdf){width="90%"}

*Figure 21*

We have $i_0=i_{\mathfrak{c}(1)-1}=j_0=j_{\kappa }=0$ by the choice of braid. Furthermore we have flow equations [\[eq=local 1\]](#eq=local 1){reference-type="eqref" reference="eq=local 1"} for $k=0,\ldots \mathfrak{c}(1)-1$, and as before from the vertices of the first component, see equation ([\[eq=cyclic\]](#eq=cyclic){reference-type="eqref" reference="eq=cyclic"}): $$\sum_{k=1}^{\mathfrak{c}(1)-1}j_{\tau^{-1}(k-1)}-j_k=0.$$

In the alternating $2$-component case this is not obvious, even though $\tau$ is a bijection of $\underline{\mathfrak{c}}$. This is because when the first component overcrosses the second component at vertex $k$ then $\tau^{-1}(k)\in \mathfrak{c}(1)+\underline{\mathfrak{c}(2)}=\{\mathfrak{c}(1),\ldots ,\mathfrak{c}-1\}$, while at an undercrossing of the second component $\tau (k) \in \mathfrak{c}(1)+\underline{\mathfrak{c}(2)}$. But the above relation holds anyway because of the cycle condition. Thus $i_0=0$ still implies $$\label{eq=cycle i}
i_k=\sum_{\ell =1}^kj_{\tau^{-1}(\ell )}-j_{\ell }$$ for $k=1,\ldots \mathfrak{c}(1)-2$, and $i_{\mathfrak{c}(1)-1}=0$. Finally the flow equations and base value at the vertices corresponding to the second component will give $i_{\mathfrak{c}(1)}=\beta_2$ and $$i_k=i_{\mathfrak{c}(1)}+\sum_{\ell =\mathfrak{c}(1)+1}^kj_{\tau^{-1}(\ell )}-j_{\ell }$$ for $k=\mathfrak{c}(1)+1,\ldots ,\mathfrak{c}-1$. Again, the cycle equation is necessary to show that the solution of the system of flow equations is consistent. Note that flow equation at the first vertex of the second component holds $$\beta_2=i_{\mathfrak{c}(1)}=i_{\mathfrak{c}-1}+j_{\tau^{-1}(\mathfrak{c}(0)}-j_{\mathfrak{c}(0)}$$ because of the cycle relation, compare the arguments following Definition [\[defn=potential\]](#defn=potential){reference-type="ref" reference="defn=potential"}, where we explain how a state is defined from the potential. Note that with $j_0=j_{\kappa }=0$ we reduce the red colors at arc-graph vertices corresponding to the first component to $\mathfrak{c}(1)-2$. Now we have a choice of $\beta_2$ and a cycle relation for the red colors at arc-graph vertices of the second component. Usually this will allow to eliminate of those red colors from the cycle relation and end up with a total of $\mathfrak{c}-2$ colorings determining a contributing state, of course with restrictions given by $\mathbf{0}\leq \mathbf{i}+\mathbf{j}\leq \mathbf{n}$ as before. But if the two components split and have no crossings this is not the case, in this case we need $\mathfrak{c}-1$ colors. Also if one of the components is completely crossing over the other component the red colors for those crossings all have to be $0$. In this case we only need $\mathfrak{c}'-1=\mathfrak{c}'(1)
+\mathfrak{c}'(2)-1$ colors to determine a contributing state, where $\mathfrak{c}'(\ell )$ is the number of self-crossings of the $\ell$-th component for $\ell =1,2$. Note that the requirement $\mathbf{0}\leq \mathbf{j}\leq \mathbf{n}$ in combination with cycle conditions will often reduce the *dimension* of the space of red colors giving contributing states. But e. g. the case of the Hopf link $\sigma_1^{-2}$ shows that the answer in general can be $\mathfrak{c}-1$.

::: exmp
Let $\beta =\sigma_1^{-6}$ and $\mathfrak{s}=2$. Then $\mathcal{K}=\beta ^{\wedge }$ is a $2$-component link projection for a link with linking number $-3$. Note that $\omega (\mathcal{K})=-6$. The set of contributing states then can be described as the set of $(j_1,j_3,j_5,\beta )$ such that $0\leq j_3,\beta \leq n$ and $$\textrm{max}(0,j_3-\beta)\leq j_1\leq j_5\leq \textrm{min}(n+j_1-j_3,n-\beta )$$ It is interesting to count the contributing states for fixed $\beta =0,1,\ldots ,n$. For example when $\beta =n$ it follows that $j_1=j_5=0$ but $j_3$ can take any values $0,1,\ldots n$, so we have $n+1$ states. On the other hand when $\beta =0$ then the inequalities reduce to $0\leq j_3\leq j_1\leq j_5\leq n$. So there are $\frac{1}{6}(n+1)(n+2)(n+3)$ states for $\beta =0$. (Here we use the usual way to enumerate the overcrossing arcs).

::: center
![image](Figure22.pdf){width="100%"}
:::

*Figure 22*
:::
