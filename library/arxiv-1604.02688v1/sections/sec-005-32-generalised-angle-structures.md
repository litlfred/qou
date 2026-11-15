---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-005-32-generalised-angle-structures
section_title: "Generalised angle structures"
section_number: 3.2
pages: 6-6
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 1.0
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{angle_struct_sect}

Considering the imaginary parts of above gluing equations allows us to 
define an angle structure on the triangulation. If we define $\quads$ 
to be the set of quad types in a triangulation $\T$, then a 
\emph{generalised angle structure} on $\T$ is a function 
$\alpha : \quads \to \R$ which assigns an ``angle'' 
$\alpha(q) \in \R$ to the pair of edges opposite a quad $q$
and satisfies the set of equations:  
\be 
\label{ang_struct1}
\alpha(q_j) + \alpha(q_j')+ \alpha(q_j'') = 
\pi \mbox{ for } j\in\{1,\ldots, n\} \ee
and
\be 
\label{ang_struct2}
\sum_j \left(a_{i,j} \alpha(q_j)+ b_{i,j} \alpha(q_j')
+ c_{i,j} \alpha(q_j'')\right)=2\pi \mbox{ for } i\in\{1,\ldots, n\} 
\ee
where $a_{i,j},b_{i,j},c_{i,j}$ are defined above. A 
\emph{strict angle structure} satisfies the additional condition that 
$\alpha(q)>0$ for all quads $q$ and a \emph{semi angle structure} 
satisfies $\alpha(q)\ge 0$.

A further refinement of generalised angle structures which considers the 
holonomies of peripheral curves will be defined in Appendix 
\ref{gen_angle_euler}.\\

A central theme of this paper is that the entries of the gluing matrix 
can be interpreted in a number of different and interesting ways. 
By exploiting these relationships, we are able to better understand the 
3D-index of a triangulation, which will be defined in the next section.
