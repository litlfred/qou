---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-023-71-generic-example
section_title: "Generic Example"
section_number: 7.1
pages: 44-45
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.963
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
The next example was treated along the paper. At the end we proved that the reconstructed Hopf algebra from the forgetful functor $F:{^H}\vc\to \vc$ coincides with $H.$

\begin{exa}
Let $H$ be a Hopf algebra in a braided finite tensor category $\vc$ and consider the tensor category $\Bc={^H}\vc$. Then the forgetful functor admits an exact faithful monoidal functor $F:{^H}\vc\to \vc$ and  the counit $\varepsilon_H$ gives rise to a monoidal section ${^H}\vc\leftarrow \vc$ that turns ${^H}\vc$ into a $\vc$-module category. 
\end{exa}

\begin{exa}
Let $H\subset L$ be Hopf algebras in $\vect_\ku$ with $\iota:H\to L$ the inclusion and assume there is a left-inverse Hopf algebra map $\pi:H\rightarrow L$, called projection. Then we have the restriction functor $\iota^*\,:\Rep(H)\leftarrow \Rep(L)$ and in addition $\Bc=\Rep(L)$ becomes a modules category over $\vc=Rep(H)$ via $\pi^*:\,\Rep(H)\leftarrow \Rep(L)$. Assume that $H$ is quasitriangular. Hence our result shows that there exists a Hopf algebra $C\in \Rep(H)$ such that there is an equivalence of monoidal modular categories
$$\Rep(L)\cong {^C}\Rep(H).$$ 
We now discuss how this is related to the classical Radford Projection Theorem \cite{Rad85}. This result states that the existence of a Hopf algebra projection $\pi$ implies that $L$ is isomorphic to a Radford biproduct $$L\cong R\# H$$
where $R$ is a Hopf algebra in ${^H_H}\YD(\Vect_\ku)$. In our case we have assumed that $H$ is quasitriangular  and $\iota^*$ lifts to a braided functor to the center of $\Bc$. This gives rise to a choice of a functor $\Rep(H)\to {^H_H}\YD(\Vect_\ku)$ and shows $R$ to be in the image - more explicitly the $R$-matrix of $H$ determines the $H$-coaction from the $H$-action. Then this $R$ is precisely the dual of our Hopf algebra $C$.
\end{exa}
