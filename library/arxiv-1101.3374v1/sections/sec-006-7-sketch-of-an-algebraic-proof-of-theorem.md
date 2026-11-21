---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-006-7-sketch-of-an-algebraic-proof-of-theorem
section_title: "Sketch of an algebraic proof of Theorem ??"
section_number: 7
pages: 43-45
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.944
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:A' label="sec:A'"}

In this section we sketch an entirely different proof of the theorem using string links and maps of the $2$-torus to the $2$-sphere. The reader is referred to our paper [@DGKMSV] for more details.

The proof is organized around the following key diagram, in which the left half, devoid of algebraic structure, represents the topological problem we are trying to solve, while the right half represents the algebraic structures that we impose on the left half via the two horizontal maps in order to solve the problem.

$$\label{eqn:keydiagram}
\begin{diagram}[size=3em]
\fbox{\parbox{0.24\linewidth}{\begin{center} \small Three-component \\ links in $S^3$ \\ up to link homotopy\end{center}}}  
&&& 
\lTo^{\text{closing up}} 
&&& 
\fbox{\parbox{0.24\linewidth}{\begin{center} \small Three-component \\ string links \\ up to link homotopy\end{center}}}    
\\ \\
\dTo^{\text{characteristic}\atop\text{maps}}_{\ g} 
&&&&&& 
\dTo_{\text{makes diagram}\atop\text{commutative}}  
\\ \\
\fbox{\parbox{0.24\linewidth}{\begin{center} 
\small Maps of $T^3$ to $S^2$ \\ up to homotopy\end{center}}}  
&&& 
\lTo_{\text{natural map}} 
&&& 
\fbox{\parbox{0.24\linewidth}{\begin{center} 
\small Fundamental groups \\ of spaces of maps \\ of $T^2$ to $S^2$\end{center}}}  \\ 
\end{diagram}$$

 

In the upper left corner of the diagram we have the set of link homotopy classes of three-component links in the $3$-sphere $S^3$, and in the lower left corner the set of homotopy classes of maps of the $3$-torus $T^3$ to the $2$-sphere $S^2$. The vertical map $g$ between them assigns to the link homotopy class of $L$ the homotopy class of its characteristic map $g_L$. Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} describes $g$ and asserts that it is one-to-one.

A $k$-component ***string link*** consists of $k$ disjoint, oriented, properly embedded arcs in a cube, with their tails on the bottom face and their tips on the top face directly above their tails. The product of two such string links with endpoints in a common position is given by stacking the second one on top of the first. When a string link moves by a link homotopy, each strand is allowed to cross itself, while different strands must remain disjoint, just as for links. Then the above product induces a group structure on the set of link homotopy classes of $k$-component string links.

In the upper right corner of the diagram we have the group of link homotopy classes of three-component string links. Following Habegger and Lin [@HabeggerLin], an explicit presentation for this group can be given in which the pairwise linking numbers and the Milnor $\mu\text{-invariant}$ figure prominently.

The upper horizontal map denotes the operation of closing up a string link to a link. It is easily shown that this map is onto, and that point inverse images are conjugacy classes of string links, a special circumstance for links with three components which fails for four or more components.

We see in the figure below that the string link on the right closes up to the Borromean rings on the left.

<figure id="fig:br">
<p><embed src="FigBR.pdf" style="height:1.52778in" /> (-136,58)<span>closes up</span></p>
<figcaption>Borromean rings as the closure of a string link</figcaption>
</figure>

Thus the Borromean rings, a "primitive example\" in the world of links, is the closure of a string link which is itself a commutator of simpler string links.

In the lower right corner of the diagram we have the union of the fundamental groups of the components of the space of continuous maps of the $2$-torus $T^2$ to the $2$-sphere $S^2$, one for each possible degree. The work of Fox [@Fox] on torus homotopy groups (the case $p = 0$) and its generalization by Larmore and Thomas [@LarmoreThomas] provide explicit presentations for these groups in which the degrees on subtori and the Pontryagin $\nu$-invariant figure prominently.

The lower horizontal map takes the homotopy class of a based loop in the space of maps of $T^2$ to $S^2$, ignores base points, and interprets this as a homotopy class of maps of $T^3$ to $S^2$ in the usual way. The resulting map is onto, and point inverse images are conjugacy classes in the various fundamental groups.

Finally, the vertical map on the right side is defined to make the diagram commute. We have a group in the upper right corner, but demote it to a union of groups to match what is below it, so that the vertical map can be regarded as a union of group homomorphisms. Using the explicit presentations of domain and range, one can determine the effects of this map on generators, and then use the commutativity of the diagram to show that the vertical map $g$ on the left is precisely as described in Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.
