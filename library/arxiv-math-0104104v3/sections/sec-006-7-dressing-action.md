---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds"
section_id: sec-006-7-dressing-action
section_title: "Dressing action"
section_number: 7
pages: 10-11
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.952
doc_brief: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-vector ﬁelds on quaternionic ﬂag manifolds, which geometrically determine"
---
The Iwasawa  decomposition of $\GL{\H}=\RR\UU \Sp = \Sp \RR \UU $ 
allows us to define:
\begin{definition} 
	The \emph{dressing action} of $\RR\UU$ on $\Sp$ is the map
	$\RR\UU\times \Sp \rightarrow \Sp $ given by
	$(G,K)\mapsto K'$ where $G \cdot K = K' \cdot R \cdot  U$ for the unique 
	$R\in\RR$ and $U\in\UU$.
\end{definition}

Our goal of this section is to relate the orbits of
the dressing action with the tetraplectic leaves of the group $\Sp$.
Notice that we have restricted the usual dressing action to $\RR\UU$ since 
we will be only concerned with $\RR\UU$ orbits of the dressing
action in the remainder.
Finally, we can state the main result of this section. 
 
\begin{Th}
	The tetraplectic leaves  of  $\sham$ on $\Sp$ are the orbits of the 
	dressing action of $\RR\UU$ on $\Sp$.
\end{Th} 
\proof 
	We already know that the leaves are parametrized by $S_n$ and $\Sph$. More
	precisely, we define the center of any leaf as the element $P_w\sigma$, where $w$ as
	usual is the permutation matrix  corresponding to $w\in S_n$, and
	$\sigma\in\Sph$. The dressing action
	can be rewritten as $(G,K)\mapsto GKG'\in \Sp$, for $G,G'\in\RR\UU$, which leaves
	us in the same (open) submanifold of the Bruhat decomposition. 

	Taking $K=\sigma P_w$, we see
	that the orbit of a dressing action on a cell remains in that cell as
	there are no permutations appearing in $G$ or $G'$.  Further, the fact that the
	orbit is contained within a single leaf follows from $G$ and $G'$  being
	upper triangular with real diagonal, and thus the dressing action does not introduce
	any non-trivial elements of $\Sph$.

	For the opposite inclusion, suppose we are given two  points, $K_1,K_2$,
	of a tetraplectic leaf. As the $K_i$ are in the
	same leaf, this implies that the $K_i$'s have the same permutation 
	type, $w$,  in the Bruhat decomposition, so we write $K_i=B_i P_w V_i$ for
	some $B_i \in \BB$ and some $V_i \in\VV_w$.  Then we have
	$B_2 B_1^{-1} K_1 = K_2 V_2 V_1^{-1}$ with  $V_2 V_1^{-1} \in \VV_w$. 
	Now, as $B_i \in \BB$, we may write:
	\begin{displaymath}
		B_i = \diag{d_1^i,\dots, d_n^i}\diag{r_1^i,\dots,r_n^i}, \ \ \ r_j^i\in\R_+,
	 	\ \ d_j^i\in \Sp[1].
	\end{displaymath}
	But as the orbits are parametrized by $\Sph$, we know that $d_j^1$  
	corresponds to $d_j^2$, which
	implies that $B_2 B_1^{-1}$ must be in $\RR$ from which it follows that 
	the $K_i$'s lie in the same orbit. 
\qed

\

Another possible proof of the above result can be obtained using the
infinitesimal computations near the centers of each leaf \cite{LW},
\cite{STS}. Once we know that the tetraplectic leaves go along the orbits 
of the dressing action infinitesimally, the analyticity of the manifolds in 
question will provide a global coincidence. 

We have established that the orbits of the dressing action of $\RR\UU$ on $\Sp$ 
coincide with the tetraplectic leaves induced by the 4-vector field
$\sham$, and these are permuted by the action of $\Sph$. Therefore 
we have obtained a geometric orbit picture for any tetraplectic leaf or a 
Bruhat cell, in $F_n$.
