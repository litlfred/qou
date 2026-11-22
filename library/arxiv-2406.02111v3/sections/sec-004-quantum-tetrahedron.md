---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-004-quantum-tetrahedron
section_title: "Quantum tetrahedron"
section_number: null
pages: 3-4
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.814
doc_brief: "Categorical Quantum Volume Operator — 17 sections: Categorical Quantum Volume Operato; Introduction; The Volume Operator in Loop Quantu"
---
\label{subsec:quantumtetrahedron}
\begin{figure}
	\centering
	\includegraphics{Fig_1_Tetrahedron.pdf}
	\caption{Schematic illustration of a quantum tetrahedron as the dual of a graph state. The node $\kappa$ is located in the center of the tetrahedron and carries a four-valent intertwiner $\ket{\iota_\kappa}$. A link $\ell$ in the graph state connected to this vertex pierces one of the tetrahedron's faces. It carries a half-integer spin $j_\ell\in\mathbb{N}\frac{1}{2}$ representing the area of the polyhedron face it pierces. More precisely, the quantum numbers $j_\ell$ are associated with the normal vectors $\vec{L}_\ell$ of the tetrahedron faces via the eigenvalue relation $\vec{L}_\ell^2\ket{j_\ell}=j_\ell(j_\ell+1)\ket{j_\ell}$.}
	\label{fig:Tetrahedron} 
\end{figure}

In addition, intertwiners satisfy the closure constraint $\sum\limits_{\ell=1}^4 \vec{L}_\ell \ket{\iota_\kappa} = 0$, i.e.\ the sum of the normals $\vec{L}_\ell$ to the faces of a tetrahedron normalized to their area vanishes~\cite{Rovelli2014}:
\begin{equation}
	\vec{L}_1 + \vec{L}_2 + \vec{L}_3 + \vec{L}_4 = 0.
	\label{eq:closure_constraint}
\end{equation}
Thus any oriented triplet of edges gives the same result for the computation of the volume and it suffices to limit our considerations to the study of triplets of edges. Note also that for $\varv \geqslant 3$ a $\varv$-valent intertwiner possesses precisely $N_{\text{dof}} = \varv-3$ internal degrees of freedom, i.e.\ trivalent intertwiners are uniquely specified through their edges.
