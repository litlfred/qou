---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-006-7-evaluation-of-the-garoufalidis-loebl-state-sum
section_title: "Evaluation of the Garoufalidis-Loebl state-sum"
section_number: 7
pages: 38-47
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.992
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
Note that the arc-graphs are *abstract* enhanced graphs representing the data necessary to calculate the state-sum [\[eq=main formula\]](#eq=main formula){reference-type="eqref" reference="eq=main formula"}. For explicit computations it will be helpful to present the data in non-geometritc way so that it can easily be implemented as an algorithm.

Suppose that $G\mathcal{K}$ is defined from a Morse projection $\mathcal{K}$ without overcrossing circles. The case including overcrossing circles can easily be described but requires to consider vertices corresponding to the circles separately. For the moment we will work with non-reduced graphs.

The enhanced arc-graph $G\mathcal{K}$ can be encoded by a *graph sextuple* $G'\mathcal{K}:=(V,\varepsilon ,\sigma ,\tau ,\mathfrak{o}, \mathfrak{r})$. Here $V$ is the set of vertices of $G\mathcal{K}$ and $\varepsilon$ is the function assigning the crossing sign to each vertex (i. e. overcrossing arc) of $G\mathcal{K}$. At each vertex of $G\mathcal{K}$ we have a unique outgoing blue edge $e_v^b$ and red edge $e_v^r$. Let $\sigma (v)$ respectively $\tau (v)$ be the endpoints of those directed edges in $G\mathcal{K}$. This defines maps $\sigma ,\tau : V\rightarrow V$, with $\sigma$ a bijection. We call $\sigma$ the *undercrossing map* and $\tau$ the *jump map*.

::: rem
$\tau$ is a bijection if and only of $\mathcal{K}$ is an alternating projection, in particular $\tau ^{-1}(v)\neq \emptyset$ for each vertex $v$ in this case, and the inverse map is defined.
:::

Next, $\mathfrak{o}=(\mathfrak{o}_v)_{v\in V}$ is a total ordering $\mathfrak{o}_v$ on each of the sets $\tau^{-1}(v)$ for each $v\in V$. Note that the order $\mathfrak{o}_v$ also defines a total ordering on the set of all incoming edges of the fat vertex $v$ of $G\mathcal{K}$ with the convention that $e_{\sigma ^{-1}(v)}^b$ precedes $e_w^r$ for each $w\in \tau^{-1}(v)$. Also note that $V=\sqcup_v \tau^{-1}(v)$ is a disjoint union. This is the ordering, which is used in the Pochhammer symbol in [\[eq=main formula\]](#eq=main formula){reference-type="eqref" reference="eq=main formula"}. If $\tau^{-1}(v)=\emptyset$ then the overcrossing arc corresponding to $v$ is a part arc. But if $\tau^{-1}(v)\neq \emptyset$ then a choice of element $w\in \tau^{-1}(v)$ determines the unique part arc on the boundary of the *fat* vertex $v$ following the edge $e_w^r$, and thus a unique part arc of $P\mathcal{K}$.

Finally, $\mathfrak{r}$ is given by two functions $\mathfrak{r}_{\sigma },\mathfrak{r}_{\tau }: V\rightarrow \{-1,0,1\}$. These are the sums of the rotation numbers of all part-arcs following the transitions $\sigma ,\tau$ from the vertex $v$. So for $\sigma$ this is the rotation number of the overcrossing arc $\sigma (v)$, for $\tau$ this is the sum of the rotation numbers of all part arcs following $v\in \tau^{-1}(\tau (v))$ in the order of $\tau^{-1}(\tau (v))$. Consider the left part in Figure 19 below, with $v$ replaced by $\tau (v)$. A non-decorated part arc will have rotation number $0$. See [\[defn:arc-graph\]](#defn:arc-graph){reference-type="ref" reference="defn:arc-graph"}.

::: rem
\(a\) Each part arc-graph or arc-graph determines a quintuple as above. But not each such quintuple will determine an arc-graph induced from a part arc-graph.

\(b\) The unique cycle decomposition of $\sigma$ will determine the number of components of $\mathcal{K}$. Let $\mu$ be the number of cycles in this decomposition.

\(c\) We let $e_{\tau^{-1}(v)}:=\{e_w^r:\tau (w)=v\}$, and this will be $\emptyset$ if $\tau^{-1}(v)=\emptyset$.

\(d\) Note that at this point we will **not** work with any particular order on the vertex set $V$.
:::

Suppose that the cycle length of the $i$-th cycle is $\mathfrak{c}(i)$ for $i=1,\ldots ,\mu$. Note that $\mathfrak{c}=\sum_{i=1}^{\mu }\mathfrak{c}(i)$ is the number of elements in $V$, and we let $V=\sqcup_{\ell =1}^{\mu }V_{\ell }$ be with $V_{\ell }$ be the set of vertices corresponding to the overcrossing arcs of the $\ell$-th component. In order to state the cycle equations from $G'\mathcal{K}$ we need to identify the overcrossings and undercrossings of the $\ell$-th component with all other components. In fact $$\bigcup_{k\neq \ell }\bigcup_{v\in V_{\ell }} \tau^{-1}(v)\cap V_k$$ will be the set of vertices corresponding to overcrossings of some overcrossing arc in $V_{\ell }$ with distinct components. Note that these are not vertices in $V_{\ell }$. Similarly $$\{v\in V_{\ell }: \tau (v)\notin V_{\ell }\}$$ corresponds to the set of all crossings at which the component $\ell$ undercrosses a distinct component.

We will next describe how to use the data $G'\mathcal{K}$ to construct the set of contributing states on $G\mathcal{K}$, which we know in natural one-to-one correspondence with the contributing states on $P\mathcal{K}$ by the flow lemma [\[lem: flow lemma\]](#lem: flow lemma){reference-type="ref" reference="lem: flow lemma"}. Next recall that a potential will be an ordering of the components and a choice of vertex $v^i$ for $i=1,\ldots \mu$ on each cycle of the cycle decomposition of $\sigma$, a function $\mathbf{j}: V\rightarrow \underline{n+1}$, and values $\beta_i\in \underline{n+1}$ for $i=1,2,\ldots ,\mu$. We assume that the function $\mathbf{j}$ satisfies the cycle equations. For a state $f$ of $G\mathcal{K}$ we use the notation $j_v:=f(e_v^r)$, $i_v:=f(e_v^b)$, $j_{\tau^{-1}(v)}:=\sum_{w,\tau (w)=v}f(e_w^r)$. Then Figure 19 []{#fig=19 label="fig=19"} shows the local picture at each vertex:

::: center
![image](Figure19.pdf){width="100%"}
:::

*Figure 19*

The flow equation using the above notation now is $$\label{eq=local 1}
i_v+j_v=i_{\sigma ^{-1}(v)}+j_{\tau ^{-1}(v)}$$

This is a recursion to calculate the state colorings from the potential, for each cycle of $\sigma$ at a time. We show how to use the recursion to find the function $\mathbf{i}: V\rightarrow \mathbb{N}_0$ in the cycle case. Below we will show for a $2$-component example how to find the function $\mathbf{i}$ from the function $\mathbf{j}$ with base values $(0,\beta )$ for the two components.

Now suppose $\mu =1$ and let $\mathfrak{c}=|V|$ be the number of crossings of $\mathcal{K}$. Then for each $v\in V$ let $k_v\in \underline{\mathfrak{c}}$ be the unique number such that $\sigma ^{-k_v}(v)=v^1$. Suppose that $i_{v^1}=\beta_1$ is given. Then $$\label{eq=solved recursion}
i_v=i_{v^1}+\sum_{k=0}^{k_v-1}j_{\tau^{-1}\sigma^{-k}(v)}-j_{\sigma^{-k}(v)}$$ The recursion will start with equation [\[eq=local 1\]](#eq=local 1){reference-type="eqref" reference="eq=local 1"}: $$i_v=i_{\sigma^{-1}(v)}+j_{\tau^{-1}(v)}-j_v$$ and then substitute the recursion with $v$ replaced by $\sigma ^{-1}(v)$ to substitute for $i_{\sigma ^{-1}(v)}$: $$i_v=i_{\sigma^{-2}(v)}+(j_{\tau^{-1}\sigma^{-1}(v)}-j_{\sigma^{-1}(v)})+(j_{\tau^{-1}(v)}-j_v)$$ After $k_v$ steps we have the solution for $v$. This solution is in fact compatible because if we apply to $v^1$ the recursion step $\mathfrak{c}$ times, recall that $\sigma^{-\mathfrak{c}}(v)=v$ since $\sigma^{\mathfrak{c}}=\textrm{id}$, then we get $$i_{\sigma^{-\mathfrak{c}}(v^1)}=i_{v^1}+\sum_{k=0}^{\mathfrak{c}-1}j_{\tau^{-1}\sigma^{-k}(v^1)}-j_{\sigma^{-k}(v^1)}=i_{v^1}$$ This follows from $$\label{eq=cyclic}
\sum_{k=0}^{\mathfrak{c}-1}j_{\tau^{-1}\sigma^{-k}(v)}=\sum_{k=0}^{\mathfrak{c}-1}j_{\sigma^{-k}(v)}$$ because $\{\sigma^{-k}(v):k=0,\ldots ,\mathfrak{c}-1\}=V$ and $V=\sqcup \tau^{-1}(v)$ as we observed above. Note that formula [\[eq=solved recursion\]](#eq=solved recursion){reference-type="eqref" reference="eq=solved recursion"} just formally states how to calculate the part arc colors from a potential, just following along a component. In the link case, the above discussion has to be done for each cycle of $\sigma$ separately, noting that the final argument uses the cycle conditions. In fact, in the process of computing the part arc color by following a component, overcrossings of distinct components are in the left sum while undercrossing a distinct component is in the right hand sum, and those contributions cancel for each component. Thus for each $v\in V$ such that $\sigma ^{-k_v}v=v^{\ell }$ with $\ell \in \{1,\ldots ,\mu\}$ we have $$\label{eq=solved recursion link}
i_v=\beta_{\ell }+\sum_{k=0}^{k_v-1}j_{\tau^{-1}\sigma^{-k}(v)}-j_{\sigma^{-k}(v)}$$ The contributing states are determined by the $n$-flow conditions [\[defn:edge coloring\]](#defn:edge coloring){reference-type="ref" reference="defn:edge coloring"} for colorings of $G\mathcal{K}$, and are $$i_v,j_v\geq 0\ \textrm{and} \ i_v+j_v\leq n$$ for all $v\in V$. These conditions are equivalent, see the proof of [\[lem: flow lemma\]](#lem: flow lemma){reference-type="ref" reference="lem: flow lemma"} to the flows on $P\mathcal{K}$ being $n$-bounded, i. e. all part arc colors take values in $\{0,\ldots ,n\}$, see [\[defn:edge coloring\]](#defn:edge coloring){reference-type="ref" reference="defn:edge coloring"}. Obviously the equations are satisfied if for all $v\in V$: $$j_v\geq 0, i_{\sigma ^{-1}(v)}\geq 0 \ \textrm{and}\ i_{\sigma^{-1}(v)}+j_{\tau^{-1}(v)}\leq n,$$ because the part arc colors along the overcrossing arc $v$ are increasing from $i_{\sigma^{-1}(v)}$ to $i_{\sigma^{-1}(v)}+j_{\tau^{-1}(v)}$, then jump down to $i_v$. The last inequalities are equivalent to $$j_v, i_v\geq 0 \ \textrm{and}  \ i_v\leq n-j_v$$ So, using the recursion [\[eq=solved recursion link\]](#eq=solved recursion link){reference-type="eqref" reference="eq=solved recursion link"} we get the system of inequalities for each $v\in V$ in terms of the potential, for all $v^{\ell }\neq v\in V$, $\ell \in \{1,\ldots ,\mu\}$ depending on $v$,

$$\label{eq=contributing}
\begin{aligned}
0&\leq j_v\leq \beta_{\ell }+j_{\tau^{-1}(v)}+\sum_{k=1}^{k_v-1}j_{\tau^{-1}\sigma^{-k}(v)}-j_{\sigma^{-k}(v)}\leq n \\
0&\leq j_{v^{\ell }},\beta_{\ell } \ \textrm{and}\ \beta_{\ell }+j_{v^{\ell }}\leq n \ \textrm{for the starting vertex}\ v^{\ell }
\end{aligned}$$

Note that the part arc coloring preceding the base vertex on the $\ell$-th component is $i_{\sigma^{-1}(v^{\ell })}+j_{\tau^{-1}(v^{\ell })}\leq n$ because $i_{\sigma^{-1}(v^{\ell })}+j_{\tau^{-1}(v^{\ell })}-j_{v^{\ell }}=\beta _{\ell }$ and the part arc color following the crossing $v^{\ell }$ is just $\beta_{\ell }$.

::: defn
A *return loop* at the self-crossing $v\in V_{\ell }$ is a loop in $P\mathcal{K}$ starting at vertex $v$ on the overcrossing arc in the direction of the orientation, following the link until it returns to $v$. The number of overcrossing arcs except the one at which the loop starts is the number $k$ (modulo $\mathfrak{c}(\ell )$) in $\sigma^k\tau (v)=v \Longleftrightarrow v=\tau^{-1}\sigma^{-k}(v)$. For $k=0$ the return loop follows an overcrossing arc until its return to $v$. This is a circle in $P\mathcal{K}$, which could be eliminated by isotopy,
:::

Figure 20 shows three return loops.

::: center
![image](Figure20.pdf){width="100%"}
:::

*Figure 20*

Note that for $k=0$ the inequality $$j_v\leq a_v+j_1+\ldots +j_s\leq n$$ holds. For $k>0$ such an equation is $$j_v\leq a_v+j_1+\ldots j_s-(j_1'+\ldots j'_{k}\leq n$$ Of $j_s=j'_t$ can occur (like $j_2=j_1'$ in the right figure of Figure 20). Then there will be a shorter return loop contained in the original loop. A *minimal return loop* is a loop, which does not contain shorter return loops. The system of inequalities for contributing states seems to contain geometric information about return loops in the part arc graph. The study of the geometry of return loops reminds of the purely inductive arguments in [@LiMi] proving the existence of the Homflypt polynomial.

In order to determine $\mathcal{F}_n^*G\mathcal{K}$ in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} for a long component projection, note that the part arc color $0$ on the part arc corresponding to the long half arcs in general does not imply $\beta_1=0$ if we take for the base vertex on the first component, which we choose to be the long one, but in fact it will imply that the vertex preceding this bottom vertex has color $0$. This follows because overcrossing can only increase the colors. So depending on the projection this will imply that the jumps are zero up this part-arc. To simplify, and actual be able to work with the reduced graph we assume that the first crossing of the bottom long arc is an undercrossing and is the base vertex of the first cycle. This will imply $\beta_1=0$ because at the base crossing the value can only decrease. This implies $j_{v^1}=0$ and by the flow condition of course also that $i_{\sigma^{-1}(v^1)}=j_{\tau^{-1}(v^1)}=0$. Note that $j_{\tau^{-1}(v)}=0 \Longleftrightarrow j_w=0$ for all $w\in \tau^{-1}(v)$. But note that $i_w\neq 0$ is possible for $w\in \tau^{-1}(v)$ in this case (and thus also $i_{\sigma ^{-1}(w)}$ and $j_{\tau^{-1}(w)}$ can be nonzero for $w\in \tau^{-1}(v)$ in this case), so these vertices cannot be discarded. If we delete the base vertex on the long component including all edges of $G\mathcal{K}$ incident to that vertex we will not change state contributions because $0$-colorings factor in as multiplication by $1$. While computationally comfortable, some of the symmetry is lost because $\tau$ is no longer defined for the vertices in $\tau^{-1}(v^1)$. Also $\sigma$ will no longer be defined on $\sigma ^{-1}(v^1)$ if we delete the base vertex $v^1$. In all recursively defined formulas we will still include the base vertex $v^1$ so that the maps $\sigma ,\tau$ are always defined.

Let $V^*:=V\setminus (\{v^1\}\cup \tau^{-1}(v^1))$ and $V':=V\setminus \{v^1\}$. Then we can parametrize the set of contributing states as follows: $$\label{eq=contributing states}
\mathcal{F}_n^*G\mathcal{K}\leftrightarrow \{\mathbf{j}:=(j_v,\beta_{\ell }): v\in V^*,\ell =2,\ldots \mu, \eqref{eq=contributing}, \textrm{cycle relations} \ \ref{defn=potential} \}$$ In order to write formula [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} for the data $G'\mathcal{K}$ from a long component projection we need to determine the contributions from right oriented extrema. For this let $v\in V^*$ define $$\label{eq=rot}
\textrm{rot}(v,\mathbf{j})=\mathfrak{r}_{\tau }(v)j_v+\mathfrak{r}_{\sigma }(v)i_v$$ and $$\textrm{rot}(\mathbf{j}):=\sum_{v\in V^*}\textrm{rot}(v,\mathbf{j})$$

::: rem
In order to see that $\textrm{rot}(\mathbf{j})$ for a state determined by $\mathbf{j}$ and Definition [\[eq=rot\]](#eq=rot){reference-type="eqref" reference="eq=rot"} determines the contributions resulting from right oriented extrema, consider first a right oriented extremum on an overcrossing arc $\sigma (v)$, and assume that this is the only right oriented extremum on the overcrossing arc. The part arc color of the part arc containing the maximum is given by $i_v+\sum j_w$, where the sum runs through those $w\in \tau^{-1}(\sigma (v))$ preceding the maximum. Recall from above that a choice of element in $\tau^{-1}(v)$ determines a unique part arc if $\tau^{-1}(v)\neq \emptyset$, and otherwise there is only one part-arc on the given overcrossing arc. The contribution $i_v=\mathfrak{r}_{\sigma }(v)i_v$, while the $j_w$ are contributions $\mathfrak{r}_{\tau }(w)j_w$ for the $w$ along the overcrossing arc $\sigma (v)$ preceding the maximum. It is not hard to see that the result for the rotation of a state persists, even though contributions for individual extrema will show up differently in the formula for $\textrm{rot}(\mathbf{j})$ given above. For example, if right oriented maximum is followed by an right oriented minimum, then the part arc color before the maximum will count with factor $+1$ while the part arc color before the minimum will contribute with factor $-1$ in the definition by ribbon functor [@L]. In the formula for $\textrm{rot}(\mathbf{j})$ given above this will be counted correctly because in this case, if no further right oriented extrema follow on the part arc considered, the rotation numbers of part arcs preceding the maximum will be $0$. In the braid projection case this cannot occur but it is possible to have overcrossing arcs rotating through several maxima, in which case the above analysis similarly proceeds.
:::

Finally the last item to be considered is the excess of a state in terms of the potential. We will use the following definition for $v\in V$: $$\label{eq=tilde}
\tilde{j}_v:=\sum_{\substack{w\in \tau^{-1}(\tau (v))\\ w<v}}j_w+i_{\sigma^{-1}(\tau(v))}$$ Then $$\label{eq=excess}
\textrm{exc}(\mathbf{j}):=\sum_{v\in V^*}\varepsilon (v)i_v\tilde{j}_v$$

Let $$\delta (\mathbf{j}):=-(\textrm{exc}(\mathbf{j})+\textrm{rot}(\mathbf{j}).$$

We can now restate Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} using the graph sextuple $G'\mathcal{K}$. Note that this description does not use any ordering of the vertex set $V$. For a long component projection $\textrm{rot}(\mathcal{K})$ let the *rotation number* of $\mathcal{K}$ be the sum of the rotation numbers of all components. This is a sum over the rotation numbers of all part arcs and thus is also the sum of the rotation numbers of all circle components resulting from smoothing all crossings. Let $$\label{eq=delta'}
\delta '(\mathcal{K},n):=-\frac{n^2}{4}\omega (\mathcal{K})+\frac{n}{2}\textrm{rot}(\mathcal{K}).$$ Note that our rotation numbers are positive in clockwise direction.

::: thm
[]{#thm:GL2 label="thm:GL2"} Let $\mathcal{K}$ be a long component projection of an oriented link $K$ with data quintuple $G'\mathcal{K}$ and $\delta '(\mathcal{K},n)$ defined in equation [\[eq=delta\'\]](#eq=delta'){reference-type="eqref" reference="eq=delta'"}. Let $$\beta_n(\mathbf{j})=\prod_{v\in V'}\beta_n(\mathbf{j},v)$$ for $\mathbf{j}\in \mathcal{F}_n^*G\mathcal{K}$ as defined in [\[eq=contributing states\]](#eq=contributing states){reference-type="eqref" reference="eq=contributing states"}, and for each $v\in V^*$ $$\label{eq=vertex contribution}
\beta_n(\mathbf{j},v)=t^{n\varepsilon (v)i_v}{i_v+j_v \choose i_v}_{t^{-\varepsilon (v)}} \{n-\tilde{j}_v\}_{j_v,t^{\varepsilon (v)}}$$ with $\tilde{j}_v$ defined in [\[eq=tilde\]](#eq=tilde){reference-type="eqref" reference="eq=tilde"}. Then $$\label{eqn=GL2}
J_n'(K)=t^{\delta '(\mathcal{K},n)}\sum_{\mathbf{j}\in \mathcal{F}_n^*G\mathcal{K}}t^{\delta (\mathbf{j})}\beta_n(\mathbf{j})$$
:::

::: rem
\(a\) The appearence of $\frac{n}{2}\textrm{rot}(K)$ is a consequence of evaluation maps at extrema, see e. g. the definition of the endomorphism $K$ in [@G], p. 1264 or Theorem 5.3.2 in [@CP].

\(b\) Note that the representation of the colored Jones polynomial in [\[thm:GL2\]](#thm:GL2){reference-type="ref" reference="thm:GL2"} references only the vertex set of $G\mathcal{K}$, which is identified with the crossings of $\mathcal{K}$ and defined by overcrossing arcs of $P\mathcal{K}$. We did reduce the reference to edge colorings to the computation of blue edge colors from the potential.

\(c\) Note that the Potts model on a graph is defined from colorings of vertices. Even though the

\(d\) We have purposefully not introduced any ordering of vertices in this section. Given an ordering and basing of the components of a projection there is a natural *cyclic ordering* by running along components starting from the basepoint. Also, if the projection is a closed braid projection in the plane starting from a given braid word then the crossings are naturally ordered by each braid generator corresponding to a crossing. If $\mathcal{O}$ is any ordering of $V$ then there is a natural $\mathcal{K}$-*twisting* of this order given by the orderings $\mathfrak{o}_v$ for each $v\in V$. If $\mathcal{O}$ orders the vertices as $\{v_1,\ldots ,v_{\mathfrak{c}}\}$ then the ordering is given by the elements in $\tau^{-1}(v_i)$ ordered by $\mathfrak{o}_{v_i}$ as above preceding the elements in $\tau^{-1}(v_{i+1})$ ordered by $\mathfrak{o}_{v_{i+1}}$. This could be related to Definition 5.1 in [@GL].

\(e\) If $\mathcal{K}$ is an alternating link projection then, in the non-reduced description, $\tau^{-1}(v)$ consists of a single element and the orderings $\mathfrak{o}_i$ are trivial. In particular in the alternating case the $\tilde{j}_v$ reduces to $\tilde{j}_v=i_{\sigma^{-1}(\tau (v))}$ so that the Pochhammer symbol and also the excess are easier to calculate.
:::
