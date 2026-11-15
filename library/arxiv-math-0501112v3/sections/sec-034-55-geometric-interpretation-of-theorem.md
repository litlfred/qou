---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-034-55-geometric-interpretation-of-theorem
section_title: "Geometric interpretation of Theorem"
section_number: 5.5
pages: 30-32
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.972
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
[]{#subsec:zaklejanie label="subsec:zaklejanie"}

<figure id="fig:przecinajacapartycja">
<embed src="figure03.eps" />
<figcaption>Graphical representation of a partition <span class="math inline">{{1, 3}, {2, 5, 7}, {4}, {6}}</span>.</figcaption>
</figure>

It is very useful to represent partitions graphically by arranging the elements of the set $X=\{1,\dots,n\}$ counterclockwise on a circle and joining elements of the same block by a line, as it can be seen on Figure [1](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"}.

We consider a large sphere with a small circular hole. The boundary of this hole is the circle mentioned above. Let us draw the blocks of the partition $\pi$ with a fat pen; in this way each block becomes a disc glued to the boundary of the hole, cf Figure [2](#fig:firstcollection){reference-type="ref" reference="fig:firstcollection"}.

<figure id="fig:firstcollection">
<embed src="figure12.eps" />
<figcaption>The first collection of discs for partition <span class="math inline"><em>π</em></span> from Figure <a href="#fig:przecinajacapartycja" data-reference-type="ref" data-reference="fig:przecinajacapartycja">1</a>.</figcaption>
</figure>

After gluing the first collection of discs, our sphere becomes a surface with a number of holes. The boundary of each hole is a circle and we shall glue this hole with a disc from the second collection. Thus we obtained an orientable surface without a boundary. We call the genus of this surface the genus of the partition $\pi$ and denote it by $\mathop{\mathrm{genus}}_{\pi}$.

The following result was proved in our previous work [@Sniady2003pushing].

::: proposition
[]{#prop:genusowatosc label="prop:genusowatosc"} For any partition $\pi$ of an $n$--element set $$\label{eq:genusowatosc} \deg \Sigma_{\pi}=n-2 \mathop{\mathrm{genus}}_\pi.$$
:::

## Geometric interpretation of Theorem [\[claim:mnozenie\]](#claim:mnozenie){reference-type="ref" reference="claim:mnozenie"} {#subsec:geometricmultiplication}

We will use the notations of Theorem [\[claim:mnozenie\]](#claim:mnozenie){reference-type="ref" reference="claim:mnozenie"}. On the surface of a large sphere we draw a small circle on which we mark counterclockwise points $i_1+1,i_1+2,\dots,i_{r+1}$.

Inside the circle we cut $r$ holes; for any $1\leq s\leq r$ the corresponding hole has a shape of a disc, the boundary of which passes through the points from the block $\rho_s$. For every $1\leq
s\leq r$ the partition $\pi_s$ connects some points on the boundary of the hole $\rho_s$ and this situation corresponds exactly to the case we considered in Section [\[subsec:zaklejanie\]](#subsec:zaklejanie){reference-type="ref" reference="subsec:zaklejanie"}. We shall glue to the hole $\rho_s$ only the first collection of discs that we considered in Section [\[subsec:zaklejanie\]](#subsec:zaklejanie){reference-type="ref" reference="subsec:zaklejanie"}, i.e. the discs which correspond to the blocks of the partition $\pi_s$. Thus we obtained a number of holes with a collection of glued discs (cf Figure [3](#fig:mnozeniepartycji){reference-type="ref" reference="fig:mnozeniepartycji"}).

![Graphical representation of example [\[eq:przykladmnozenie\]](#eq:przykladmnozenie){reference-type="eqref" reference="eq:przykladmnozenie"}.](figure13.eps){#fig:mnozeniepartycji}

![Figure [3](#fig:mnozeniepartycji){reference-type="ref" reference="fig:mnozeniepartycji"} after inflating small holes.](figure14.eps){#fig:mnozeniepartycji2}

When we inflate the original small holes inside the circle we may think about this picture alternatively: instead of $r$ small holes we have a big one (in the shape of the circle) but some arcs on its boundary are glued by an additional disc (on Figure [4](#fig:mnozeniepartycji2){reference-type="ref" reference="fig:mnozeniepartycji2"} drawn in black) glued to vertices $i_2,i_3,\dots,i_{r+1}$. Furthermore we still have a collection of all discs (on Figure [4](#fig:mnozeniepartycji2){reference-type="ref" reference="fig:mnozeniepartycji2"} drawn in gray) corresponding to partitions $\pi_s$. We merge the additional black disc to a gray disc from this collection if they touch the same vertex. After this merging the collection of discs corresponds to the partition $\pi_1 \bullet \cdots \bullet \pi_r=\big\{
\{i_2,i_3,\dots,i_{r+1} \} \big\} \vee (\pi_1 \cup \cdots \cup
\pi_r)$ which appears in the formula [\[eq:formulanailoczynrozlaczny\]](#eq:formulanailoczynrozlaczny){reference-type="eqref" reference="eq:formulanailoczynrozlaczny"} for the disjoint product.

The last step is to consider all ways of merging of the discs (or equivalently: all partitions $\sigma\geq \pi_1 \bullet \cdots
\bullet \pi_r$) with the property that any two vertices that were lying on the boundary of the same small hole $\rho_s$ if were not connected by a disc from the collection $\pi_s$ then they also cannot be connected after all mergings. In this way we obtain all partitions which contribute to [\[eq:formulanailoczyn\]](#eq:formulanailoczyn){reference-type="eqref" reference="eq:formulanailoczyn"}.

By splitting the holes (we recall that each hole corresponds to some set $\rho_i$) into some new holes we can view the surface associated to the partition $\rho$ as a sphere with a number of new holes glued in pairs by handles and the number of these handles is equal to the genus of the surface. In this way we obtain a graph $G_\sigma$ the vertices of which correspond to the old holes (or, equivalently, sets $\rho_i$) and the edges correspond to the handles between new holes. Of course the above construction can be sometimes performed in many different ways but we do not mind it. Note that multiple connections between vertices are allowed. Also, a vertex can be connected with itself and the number of such loops is equal to the genus of the corresponding partitions $\pi_i$. The genus of $\sigma$ is equal to the total number of edges in $G_{\sigma}$.

In order to obtain all partitions $\sigma$ which contribute to [\[eq:kumulantyklas\]](#eq:kumulantyklas){reference-type="eqref" reference="eq:kumulantyklas"} we should restrict our attention only to $\sigma$ such that the graph $G_{\sigma}$ is connected. A connected graph with $n$ vertices has at least $n-1$ non-loop edges therefore $$\label{eq:nierownosc} \mathop{\mathrm{genus}}_{\sigma}\geq
\mathop{\mathrm{genus}}_{\pi_1}+\cdots+\mathop{\mathrm{genus}}_{\pi_n}+(n-1).$$

::: proof
*Proof of Theorem [\[theo:kumulantykombinatoryczne\]](#theo:kumulantykombinatoryczne){reference-type="ref" reference="theo:kumulantykombinatoryczne"}.* In order to prove [\[eq:kumulantykombinatoryczne\]](#eq:kumulantykombinatoryczne){reference-type="eqref" reference="eq:kumulantykombinatoryczne"} for the special case when $x_i=\Sigma_{\pi_i}$ it is enough to apply Proposition [\[prop:genusowatosc\]](#prop:genusowatosc){reference-type="ref" reference="prop:genusowatosc"} and [\[eq:nierownosc\]](#eq:nierownosc){reference-type="eqref" reference="eq:nierownosc"}.

It remains now to prove [\[eq:a-tak-dokladnie?\]](#eq:a-tak-dokladnie?){reference-type="eqref" reference="eq:a-tak-dokladnie?"} and we shall do it in the following. We use the notations of Theorem [\[claim:mnozenie2\]](#claim:mnozenie2){reference-type="ref" reference="claim:mnozenie2"} if $n=2$ and $\pi_1,\pi_2$ are trivial partitions (every blocks consists of a single element). Let $\sigma$ be a partition which contributes to [\[eq:kumulantyklas\]](#eq:kumulantyklas){reference-type="eqref" reference="eq:kumulantyklas"} with the minimal possible genus, namely $\mathop{\mathrm{genus}}_{\sigma}=1$. It follows that one of the blocks of $\sigma$ is equal to $\{i_2,i_3\}$. Secondly, some of the elements of the set $\{i_1+1,\dots,i_2-1\}$ (but at least one of them) are paired with some of the elements of the set $\{i_2+1,\dots,i_1+i_3-1\}$; this pairing however is not arbitrary. Let us travel counterclockwise along the boundary of the hole corresponding to the block $\pi_1$; in other words we visit the vertices in the order $i_1+1\rightarrow i_1+
2\rightarrow\cdots\rightarrow i_2-1\rightarrow i_1+1$. Some of these vertices are paired by $\sigma$ with some of the elements of $\{i_2+1,\dots,i_3-1\}$ corresponding to the other hole; let us have a look in which order these counterparts appear during our walk. From the very definition of the genus of a partition we know that it is possible to draw the blocks of $\sigma\setminus \big\{
\{i_2,i_3\} \big\}$ on the surface of the handle in such a way that lines do not cross. It follows that these counterparts will be visited in the clockwise order $i_3-1\rightarrow i_3-2\rightarrow
\cdots\rightarrow i_2+1 \rightarrow i_3-1$, cf Figure [5](#fig:cake2){reference-type="ref" reference="fig:cake2"}.

Let $a_1,\dots,a_r$ denote the distances (counted cyclically counterclockwise) between consecutive elements of the pairs in the first hole and let $b_1,\dots,b_r$ denote the distances (counted cyclically counterclockwise) between consecutive elements of the pairs in the second hole. Readers acquainted with the results of Section [\[subsec:explicit\]](#subsec:explicit){reference-type="ref" reference="subsec:explicit"} will see that $$\Sigma_{\sigma}= \Sigma_{a_1+b_1-1,\dots,a_r+b_r-1}.$$ It is easy to see that $a_1+\cdots+a_r=i_2-i_1$ and $b_1+\cdots+b_r=i_3-i_2$. Such sequences $(a_i)$ and $(b_i)$ uniquely determine $\sigma$ once we specify the first element in each cycle (there are $i_2-i_1-1$ choices for the first one and $i_3-i_2-1$ choices for the second one). Partition $\sigma$ can be represented like this in $r$ different ways which correspond to the cyclic rotations of the sequences $(a_i)$ and $(b_i)$. Since $\Sigma_{\pi_1}=\Sigma_{i_2-i_1-1}$ and $\Sigma_{\pi_2}=\Sigma_{i_3-i_2-1}$ this finishes the proof of [\[eq:a-tak-dokladnie?\]](#eq:a-tak-dokladnie?){reference-type="eqref" reference="eq:a-tak-dokladnie?"}.

![Partitions $\sigma$ with genus $1$ which contribute to [\[eq:kumulantyklas\]](#eq:kumulantyklas){reference-type="eqref" reference="eq:kumulantyklas"}.](figure27.eps){#fig:cake2}

 ◻
:::
