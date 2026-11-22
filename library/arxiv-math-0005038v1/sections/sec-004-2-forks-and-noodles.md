---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-004-2-forks-and-noodles
section_title: "Forks and Noodles"
section_number: 2
pages: 3-4
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.957
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
[]{#fn label="fn"}

In this section we define forks and noodles and a pairing between them. The idea of using a fork to represent an element of $H_2(\tilde{C})$ is due to Krammer [@krammer].

A *fork* is an embedded tree $F \subset D$ with four vertices $d_1$, $p_i$, $p_j$ and $z$ such that $F \cap \partial D = \{d_1\}$, $F \cap P = \{p_i,p_j\}$, and all three edges have $z$ as a vertex. The edge containing $d_1$ is called the *handle* of $F$. The union of the other two edges is a single edge, which we call the *tine edge* of $F$ and denote by $T(F)$.

<figure id="doublefork">
<div class="picture">
<p>(120,130)(0,-10)</p>
<p>(60,60)</p>
<p>(50,1)(50,70) (20,60)(30,70)(40,70) (40,70)(80,70) (80,70)(90,70)(100,60) (56,74)<span><span class="math inline"><em>T</em>(<em>F</em>)</span></span> (38,20)<span><span class="math inline"><em>F</em></span></span></p>
<p>(70,1)(70,50) (20,60)(30,50)(40,50) (40,50)(80,50) (80,50)(90,50)(100,60) (56,54)<span><span class="math inline"><em>T</em>(<em>F</em>′)</span></span> (70,20)<span><span class="math inline"><em>F</em>′</span></span></p>
<p>(45,-10)<span><span class="math inline"><em>d</em><sub>1</sub></span></span> (65,-10)<span><span class="math inline"><em>d</em><sub>2</sub></span></span></p>
<p>(20,60) (100,60)</p>
<p>(49,90) (60,90) (71,90) (54.5,100) (65.5,100)</p>
</div>
<figcaption>A fork <span class="math inline"><em>F</em></span> and a parallel copy <span class="math inline"><em>F</em>′</span>.</figcaption>
</figure>

For a given fork $F$ we can define a *parallel copy* of $F$ to be an embedded tree $F'$ as shown in Figure [1](#doublefork){reference-type="ref" reference="doublefork"}. The five punctures at the top of the figure may be replaced by any number, and any orientation-preserving self-homeomorphism may be applied to the entire figure. The tine edge $T(F')$ of $F'$ is defined analogously to that of $F$.

For any fork $F$, we define a surface $\tilde{\Sigma}(F)$ in $\tilde{C}$ as follows. Let $F'$ be a parallel copy of $F$. Let $z$ be the vertex contained in all three edges of $F$, and let $z'$ be the vertex contained in all three edges of $F'$. We define the surface $\Sigma(F)$ to be the set of points in $C$ which can be written in the form $\{x,y\}$, where $x \in T(F) \setminus P$ and $y \in T(F') \setminus P$. Let $\beta_1$ be an arc from $d_1$ to $z$ along the handle of $F$ and let $\beta_2$ be an arc from $d_2$ to $z'$ along the handle of $F'$. Let $\tilde{\beta}$ be the lift of $\{\beta_1,\beta_2\}$ to $\tilde{C}$ which starts at $\tilde{c}_0$. Let $\tilde{\Sigma}(F)$ be the lift of $\Sigma(F)$ to $\tilde{C}$ which contains $\tilde{\beta}(1)$.

A *noodle* is an embedded edge $N \subset D \setminus P$ with endpoints $d_1$ and $d_2$. For a given noodle $N$ we define the surface $\Sigma(N)$ to be the set of points $\{x,y\} \in C$ such that $x$ and $y$ are distinct points in $N$. Let $\tilde{\Sigma}(N)$ be the lift of $\Sigma(N)$ to $\tilde{C}$ which contains $\tilde{c}_0$.

Let $F$ be a fork and let $N$ be a noodle. We define $\langle N,F \rangle \in \Lambda$ as follows. $$\langle N,F \rangle = 
\sum_{a,b \in Z}q^a t^b 
(q^a t^b \tilde{\Sigma}(N), \tilde{\Sigma}(F)).$$ Here $q^a t^b \tilde{\Sigma}(N)$ denotes the image of $\tilde{\Sigma}(N)$ under the covering transformation $q^a t^b$, and $(q^a t^b \tilde{\Sigma}(N), \tilde{\Sigma}(F))$ denotes the algebraic intersection number of the two surfaces in $\tilde{C}$.

::: lem
[]{#blem label="blem"} The pairing between forks and noodles is well-defined. Furthermore, if $[\sigma]$ lies in the kernel of the Lawrence-Krammer representation then $$\langle N,F \rangle = \langle N,\sigma(F) \rangle$$ for every fork $F$ and noodle $N$.
:::
