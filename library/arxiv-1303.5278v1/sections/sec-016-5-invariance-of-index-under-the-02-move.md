---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-016-5-invariance-of-index-under-the-02-move
section_title: "Invariance of index under the 0–2 move"
section_number: 5
pages: 29-32
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.933
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sec.02move label="sec.02move"}

Let $M$ be a cusped 3-manifold and consider the 0--2 move on a pair $\mathcal{T}$ and $\widetilde\mathcal{T}$ of ideal triangulations of $M$ with $N$ and $N+2$ tetrahedra, as shown in Figure [1](#0-2move_labelled){reference-type="ref" reference="0-2move_labelled"}.

<figure id="0-2move_labelled">
<p><span class="math inline"><em>e</em></span> at 32 95 <span class="math inline"><em>e</em></span> at 32 95 <span class="math inline"><em>e</em><sub>2</sub></span> at 8 129 <span class="math inline"><em>e</em><sub>4</sub></span> at 55 127 <span class="math inline"><em>e</em><sub>1</sub></span> at 8 55 <span class="math inline"><em>e</em><sub>3</sub></span> at 55 54</p>
<p><span class="math inline"><em>e</em><sub>2</sub></span> at 165 124 <span class="math inline"><em>e</em><sub>4</sub></span> at 215 123 <span class="math inline"><em>e</em><sub>1</sub></span> at 165.5 55 <span class="math inline"><em>e</em><sub>3</sub></span> at 216 55 <span class="math inline"><em>e</em>′</span> at 175 79.5 <span class="math inline"><em>e</em>″</span> at 207 97.5 <span class="math inline"><em>ẽ</em></span> at 186 110.5</p>
<p><span class="math inline"><em>ā</em><sub>2</sub></span> at 113 58 <span class="math inline"><em>ā</em><sub>1</sub></span> at 138 58 <span class="math inline"><em>c̄</em><sub>2</sub></span> at 121 71 <span class="math inline"><em>b̄</em><sub>2</sub></span> at 121 45 <span class="math inline"><em>b̄</em><sub>1</sub></span> at 130 71 <span class="math inline"><em>c̄</em><sub>1</sub></span> at 130 45</p>
<p><span class="math inline"><em>ā</em><sub>1</sub></span> at 238 70 <span class="math inline"><em>ā</em><sub>2</sub></span> at 263 70 <span class="math inline"><em>c̄</em><sub>1</sub></span> at 246 83 <span class="math inline"><em>b̄</em><sub>1</sub></span> at 246 57 <span class="math inline"><em>b̄</em><sub>2</sub></span> at 255 83 <span class="math inline"><em>c̄</em><sub>2</sub></span> at 255 57</p>
<p><span class="math inline"><em>ā</em><sub>1</sub></span> at 172 20 <span class="math inline"><em>c̄</em><sub>1</sub></span> at 159 20 <span class="math inline"><em>b̄</em><sub>1</sub></span> at 185 20 <span class="math inline"><em>ā</em><sub>2</sub></span> at 172 9.4 <span class="math inline"><em>b̄</em><sub>2</sub></span> at 159 9.4 <span class="math inline"><em>c̄</em><sub>2</sub></span> at 185 9.4</p>
<p><span class="math inline"><em>ā</em><sub>2</sub></span> at 216 162 <span class="math inline"><em>c̄</em><sub>2</sub></span> at 203 162 <span class="math inline"><em>b̄</em><sub>2</sub></span> at 229 162 <span class="math inline"><em>ā</em><sub>1</sub></span> at 216 151.4 <span class="math inline"><em>b̄</em><sub>1</sub></span> at 203 151.4 <span class="math inline"><em>c̄</em><sub>1</sub></span> at 229 151.4</p>
<img src="draws_eps/0-2move_labelled2" />
<figcaption>The 0–2 move shown with truncated tetrahedra. The four triangulated ends of the new pair of tetrahedra are shown. All of the “zoomed in” pictures are as seen from viewpoints outside of the pair of tetrahedra. The labels at the corners of the triangles in the “zoomed in” pictures are explained in Section <a href="#sub.peripheral" data-reference-type="ref" data-reference="sub.peripheral">[sub.peripheral]</a>. </figcaption>
</figure>

::: thm
[]{#thm.20move.index label="thm.20move.index"} Suppose that $\mathcal{T}$ and $\widetilde\mathcal{T}$ are ideal triangulations related by a 0--2 move and both admit an index structure. Then, for any $[\varpi] \in H_1(\partial M;\mathbb{Z})$, $I_{\mathcal{T}}([\varpi])=I_{\widetilde\mathcal{T}}([\varpi])$.
:::

::: proof
*Proof.* Our assumptions imply that both $I_{\mathcal{T}}$ and $I_{\widetilde\mathcal{T}}$ exist. We now compare these indices using the alternative definition [\[JD_index_eq\]](#JD_index_eq){reference-type="eqref" reference="JD_index_eq"} and quadratic identity [\[eq.JD_quad_id\]](#eq.JD_quad_id){reference-type="eqref" reference="eq.JD_quad_id"}.

We use the labelling of the two bigons and triangles on $\widetilde\mathcal{T}$ shown in Figure [1](#0-2move_labelled){reference-type="ref" reference="0-2move_labelled"}. Let $T_i$ for $i=3,\dots,N+2$ denote the tetrahedra in $\mathcal{T}$, and let $T_1, T_2$ be the additional tetrahedra added in $\widetilde\mathcal{T}$. Note that the edge $e$ in $\mathcal{T}$ splits into two edges $e',e''$ in $\widetilde\mathcal{T}$, and there is another new edge $\widetilde e$ in $\widetilde\mathcal{T}$. We abuse notation by identifying the symbols for the corresponding remaining edges in $\mathcal{T}$ and $\widetilde\mathcal{T}$. We denote these as $e_1, \ldots, e_{N-1}$.

Let $\widetilde\boldsymbol{k}\in \mathbb{Z}^{N+2}$ be a weight function on the edges of $\widetilde\mathcal{T}$ and write $\widetilde\boldsymbol{k}= (k',k'',\widetilde k, k_1, \ldots, k_{N-1})$ where $k',k'',\widetilde k, k_i$ are the values of $\widetilde\boldsymbol{k}$ on $e',e'', \widetilde e$ and $e_i$ respectively. Similarly, let $\boldsymbol{k}= (k, k_1, \ldots, k_{N-1})\in\mathbb{Z}^N$ be a corresponding weight function on $\mathcal{T}$. We choose label $\bar a_j$ on the edge $\widetilde e$ on tetrahedron $T_j$ for $j=1,2$; then the location of labels $\bar b_j,\bar c_j$ are determined using the orientation on $M$.

Let $\varpi$ be an oriented multi-curve which is normal with respect to the triangulation $\mathcal{T}_\partial$ of $\partial M$ induced by $\mathcal{T}$, and let $\widetilde\varpi$ an oriented multi-curve which is normal with respect to $\widetilde\mathcal{T}_\partial$ and represents the same homology class $[\varpi]\in H_1(\partial M;\mathbb{Z})$. Let $J(T_j,\boldsymbol{k},\varpi) = J_{\Delta}(\bar a_j(\boldsymbol{k},\varpi), \bar b_j(\boldsymbol{k},\varpi), \bar c_j(\boldsymbol{k},\varpi))$ denote the contribution of tetrahedron $T_j$ to the index with weight function $\boldsymbol{k}$ on its edges and peripheral curve $\varpi$ on its truncated ends, and similarly let $J(T_j, \widetilde\boldsymbol{k},\widetilde\varpi)$ be contribution with weight function $\widetilde\boldsymbol{k}$ and peripheral curve $\widetilde\varpi$.

To compute $I_{\mathcal{T}}$ we use Theorem [\[pick_edges\]](#pick_edges){reference-type="ref" reference="pick_edges"} to choose an excluded set $\mathcal X$ of $r$ edges in a maximal tree with 1- or 3-cycle in $\mathcal{T}$ to be omitted from the summation in [\[JD_index_eq\]](#JD_index_eq){reference-type="eqref" reference="JD_index_eq"}.

Case 1: If $e \notin \mathcal X$ we can order the edges of $\mathcal{T}$ so that $\mathcal X = \{ e_{N-r}, \ldots, e_{N-2}, e_{N-1} \}$. Then we can compute $I_{\widetilde\mathcal{T}}$ by omitting the same edge set $\widetilde{\mathcal X} = \mathcal X$.

Case 2: If $e \in \mathcal X$ we can order the edges so $\mathcal X = \{ e, e_{N-r+1}, \ldots, e_{N-2}, e_{N-1} \}$. Then we can compute $I_{\widetilde\mathcal{T}}$ by omitting the edge set $\widetilde{\mathcal X} =  \{ e'', e_{N-r+1}, \ldots, e_{N-2}, e_{N-1} \}$.

Then $$\label{eq.JD_index_sum1}
I_{\widetilde\mathcal{T}} (\widetilde\varpi)= \sum_{\widetilde\boldsymbol{k}\in \widetilde S} \ 
q^{k' + k'' + \widetilde k + \sum_{i=1}^{N-1} k_i } \,
J(T_1,\widetilde\boldsymbol{k},\widetilde\varpi) J(T_2,\widetilde\boldsymbol{k},\widetilde\varpi) \prod_{j=3}^{N+2} J(T_j, \widetilde\boldsymbol{k},\widetilde\varpi),$$ where $$\widetilde S = \left\{ \widetilde\boldsymbol{k}= (k',k'',\widetilde k, k_1, \ldots, k_{N-1}) \in \mathbb{Z}^{N+2} : k_{N-i}=0 \text { for } i=1, \ldots, r  \right\} \text{  in case 1}$$ and $$\widetilde S = \left\{ \widetilde\boldsymbol{k}= (k',k'',\widetilde k, k_1, \ldots, k_{N-1})\in \mathbb{Z}^{N+2} : k''=0, k_{N-i}=0 \text { for } i=1, \ldots, r-1 \right\} \text{  in case 2}.$$ Note that in both cases, the new edge $\tilde e$ is *included* in the set of basic edges so $\tilde k$ varies over $\mathbb{Z}$ in the sum.

Now we look at the contribution to $I_{\widetilde\mathcal{T}}$ coming from the tetrahedra $T_1,T_2$ and summed over the weight $\widetilde k$ on $\tilde e$, namely $$\label{tilde_k_sum}
\sum_{\widetilde k \in \mathbb{Z}}
q^{\widetilde k}
J( T_1; \widetilde\boldsymbol{k},\widetilde\varpi)  J( T_2; \widetilde\boldsymbol{k},\widetilde\varpi)$$ where $$J( T_1; \widetilde\boldsymbol{k},\widetilde\varpi)=J_{\Delta}(k' + \widetilde k+\bar a_{\widetilde\varpi,1}, k_2+k_3+\bar b_{\widetilde\varpi,1},k_1+k_4+\bar c_{\widetilde\varpi,1})$$ and $$J( T_2; \widetilde\boldsymbol{k},\widetilde\varpi)=J_{\Delta}(k'' + \widetilde k +\bar a_{\widetilde\varpi,2},  k_1+k_4+\bar b_{\widetilde\varpi,2},k_2+k_3+\bar c_{\widetilde\varpi,2}).$$

Recall that $\varpi$ be an oriented multi-curve which is normal with respect to the triangulation $\mathcal{T}_\partial$ of $\partial M$ induced by $\mathcal{T}$. Since the index only depends on the homology class of a peripheral curve, we can calculate $I_{\widetilde\mathcal{T}}([\varpi])$ by using for $\widetilde\varpi$ a corresponding curve on $\partial M$ which is normal with respect to $\widetilde\mathcal{T}_\partial$ and goes "straight through" each pair of added triangles on $\partial M$. See Figure [2](#0-2_bdry_curve_changes){reference-type="ref" reference="0-2_bdry_curve_changes"}.

<figure id="0-2_bdry_curve_changes">
<p><span class="math inline"><em>ā</em><sub>2</sub></span> at 93 29 <span class="math inline"><em>ā</em><sub>1</sub></span> at 118 29 <span class="math inline"><em>c̄</em><sub>2</sub></span> at 101 42 <span class="math inline"><em>b̄</em><sub>2</sub></span> at 101 16 <span class="math inline"><em>b̄</em><sub>1</sub></span> at 110 42 <span class="math inline"><em>c̄</em><sub>1</sub></span> at 110 16</p>
<p><span class="math inline"><em>ā</em><sub>2</sub></span> at 105.5 88 <span class="math inline"><em>c̄</em><sub>2</sub></span> at 92.5 88 <span class="math inline"><em>b̄</em><sub>2</sub></span> at 118.5 88 <span class="math inline"><em>ā</em><sub>1</sub></span> at 105.5 77.4 <span class="math inline"><em>b̄</em><sub>1</sub></span> at 92.5 77.4 <span class="math inline"><em>c̄</em><sub>1</sub></span> at 118.5 77.4 <img src="draws_eps/0-2_bdry_curve_changes" style="width:10cm" alt="image" /></p>
<figcaption>Changes in peripheral curve from <span class="math inline">ϖ</span> in <span class="math inline">𝒯<sub>∂</sub></span> to <span class="math inline">$\widetilde\varpi$</span> in <span class="math inline">$\widetilde\mathcal{T}_\partial$</span>. Note that the curve in the top diagram could go either way around the new vertex. </figcaption>
</figure>

Then we have $$\bar a_{\widetilde\varpi,1}=\bar a_{\widetilde\varpi,2}=0,\quad
\bar b_{\widetilde\varpi,1} = \bar c_{\widetilde\varpi,2} = x,\quad \bar b_{\widetilde\varpi,2} = \bar c_{\widetilde\varpi,1} = y,$$ for some $x,y \in \mathbb{Z}$, and $$\bar a_{\widetilde\varpi,j}=\bar a_{\varpi,j},~~ \bar b_{\widetilde\varpi,j}=\bar b_{\varpi,j},~~\bar c_{\widetilde\varpi,j}=\bar c_{\varpi,j} \text{ for } j = 3, \ldots, N+2.$$

Using the invariance of $J_{\Delta}$ under all permutations of its arguments and the quadratic identity [\[eq.JD_quad_id\]](#eq.JD_quad_id){reference-type="eqref" reference="eq.JD_quad_id"}, the sum [\[tilde_k_sum\]](#tilde_k_sum){reference-type="eqref" reference="tilde_k_sum"} becomes $$\sum_{\widetilde k \in \mathbb{Z}}  q^{\widetilde k}
J_{\Delta}(k' + \widetilde k, k_2+k_3+x,k_1+k_4+y)
J_{\Delta}(k'' + \widetilde k ,  k_1+k_4+y,k_2+k_3+x)
= q^{-k'} \,\delta_{k',k''}.$$ This means that in the sum [\[eq.JD_index_sum1\]](#eq.JD_index_sum1){reference-type="eqref" reference="eq.JD_index_sum1"} we can remove the summation over $\widetilde\boldsymbol{k}$ and put $k' = k'' =k$. Hence $J(T_j, \widetilde\boldsymbol{k},\widetilde\varpi) = J(T_j, \boldsymbol{k},\varpi)$ for $j=3, \ldots, N+2$, and $$I_{\widetilde\mathcal{T}} (\widetilde\varpi)= \sum_{\boldsymbol{k}\in S} \ 
q^{k + \sum_{i=1}^{N-1} k_i } \,
 \prod_{j=3}^{N+2} J(T_j, \boldsymbol{k},\varpi)= I_{\mathcal{T}} (\varpi),$$ where $$S = \left\{ \boldsymbol{k}=(k, k_1, \ldots, k_{N-1})  \in \mathbb{Z}^{N} : k_{N-i}=0 \text { for } i=1, \ldots, r \right\} \text{  in case 1}$$ and $$S = \left\{ \boldsymbol{k}= (k, k_1, \ldots, k_{N-1}) \in \mathbb{Z}^{N} : k=0, k_{N-i}=0 \text { for } i=1, \ldots, r-1 \right\} \text{  in case 2}.$$ This completes the proof of invariance of the index under the 0--2 move. ◻
:::
