---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-007-4-semisimple-quantum-invariants-and-tqfts
section_title: "Semisimple quantum invariants and TQFTs"
section_number: 4
pages: 7-9
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.977
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
\label{S:TQFT_sem-sim}

The diagrammatic interpretation for morphisms of ribbon categories which was discussed earlier highlights the fundamental interplay between algebra and topology arising in this context. In fact, it is a result of Turaev that certain topological gadgets called \textit{ribbon graphs} provide the relevant topological structure underlying Penrose graphical notation \cite[Thm.~I.2.5]{T94}. Indeed, isotopy classes of ribbon graphs can be organised as morphisms of a category $\calR_\calC$, and the graphical calculus introduced above can be implemented by a functor
\[
 F_\calC : \calR_\calC \to \calC
\]
called the \textit{Reshetikhin--Turaev functor}. This technology plays a fundamental role in every construction discussed in this survey.

Starting from a T-modular category $\calC$, Turaev showed how to construct a topological invariant $\RT_\calC$ of closed oriented 3-manifolds decorated with closed\footnote{A ribbon graph is \textit{closed} if it has no boundary vertices, and thus represents an endomorphism of the tensor unit $\one$ of $\calC$ under the Reshetikhin--Turaev functor $F_\calC$.} ribbon graphs. By their very definition, ribbon graphs have a rather hybrid nature, between topology and algebra. This of course can be seen as a strenght of the theory, which allows for great flexibility. However, for the benefit of those who are looking for a purely topological point of view, the construction can be understood as producing, in particular, a family $\{ \RT_V \}_{V \in \calC}$ of topological invariants of framed oriented links inside 3-manifolds, where each invariant $\RT_V$ is obtained by choosing the object $V \in \calC$ as a label for every component of the link. The definition of these topological invariants is based on surgery presentations, which allow us to interpret framed links in $S^3$ as closed oriented 3-manifolds. The main idea consists in choosing orientations and labels for a surgery presentation, and then using the Reshetikhin--Turaev functor $F_\calC$ in order to extract a scalar. The choice needs to be made in such a way that the resulting scalar is invariant under orientation reversals and Kirby moves. Turaev came up with such a label, which is given by a formal linear combination of objects of $\calC$ called the \textit{Kirby color}, and given by
\[
 \Omega := \sum_{i \in I} \dim_\calC(V_i) \cdot V_i,
\]
where again $\Gamma(\calC) = \left\{ V_i \mid i \in I \right\}$ is a set of representatives of isomorphism classes of simple objects of $\calC$, and where
\[
 \dim_\calC(X) = \tr_\calC(\id_X) = \rev_X \circ \lcoev_X
\]
is the \textit{categorical dimension} of an object $X \in \calC$, which coincides with the \textit{categorical trace} of its identity endomorphism. Labeling components of a framed oriented link using the Kirby color is a shortcut that has to be understood through multilinear expansions. More precisely, if $L$ is a framed oriented link featuring a component $K$ labeled by $\Omega$, and if $L_i$ is obtained from $L$ by replacing the label of $K$ with $V_i \in \Gamma(\calC)$, then we set
\[
 F_\calC(L) := \sum_{i \in I} \dim_\calC(V_i) F_\calC(L_i).
\]
This oriented framed link invariant is already preserved under Kirby II moves, as the terminology might suggest. In order to obtain invariance under Kirby I moves, we need a normalization coefficient. This is defined in terms of the so-called \textit{stabilization coefficients}
\[
 \Delta_+ := F_\calC \left( \pic{stabilization_coeff_+_black} \right) \in \Bbbk, \qquad
 \Delta_- := F_\calC \left( \pic{stabilization_coeff_-_black} \right) \in \Bbbk.
\]
As a consequence of T-modularity, their product $\Delta_+ \Delta_-$ is invertible, and so we can choose two parameters $\calD,\delta \in \Bbbk^\times$ satisfying
\[
 \calD^2 = \Delta_+ \Delta_-, \qquad 
 \delta = \frac{\Delta_+}{\calD} = \frac{\calD}{\Delta_-}.
\]
The definition of the topological invariant $\RT_\calC$ depends on the choice of $\calD$, which uniquely determines $\delta$. If $M$ is a closed oriented 3-manifold, if $T \subset M$ is a closed ribbon graph, and if $L \subset S^3$ is a surgery presentation of $M$, which we assume having $\ell$ components and signature $\sigma$, and which we equip with an arbitrary orientation and the label $\Omega$ on every component, then
\[
 \RT_\calC(M,T) := \calD^{-1-\ell} \delta^{-\sigma} F_\calC(L \cup T)
\]
is a topological invariant of the pair $(M,T)$.

The universal construction of \cite{BHMV95} extends the invariant $\RT_\calC$ to a dual pair of TQFTs given by a covariant functor $\rmV_\calC$ and a contravariant one $\rmV'_\calC$. This means that, for a closed oriented surface $\Sigma$, we obtain dual vector spaces $\rmV_\calC(\Sigma)$ and $\rmV'_\calC(\Sigma)$ supporting respectively left and right actions of decorated cobordisms. If $\bar{\Sigma}$ is obtained from $\Sigma$ by reversing its orientation, we have a natural isomorphism $\rmV'_\calC(\Sigma) \cong \rmV_\calC(\bar{\Sigma})$. This means we can simply focus on the covariant TQFT $\rmV_\calC$. If $\Sigma_g$ is a closed oriented surface of genus $g$, then
\begin{equation}\label{E:st_sp_sem-sim}
 \rmV_\calC(\Sigma_g) \cong \bigoplus_{i_1,\ldots,i_g \in I} \calC \left( \one,\bigotimes_{j=1}^g V_{i_j} \otimes V_{i_j}^* \right).
\end{equation}
Since $\calC$ is semisimple, this vector space can be rewritten, using fusion rules, in terms of labelings of trivalent graphs, with different graphs determining different decompositions. If $\calG$ is an oriented trivalent graph, whose sets of vertices and egdes are denoted $\calV$ and $\calE$ respectively, then, for every vertex $v \in \calV$, we denote with $v_-$ the set of incoming germs of edges with target $v$, and we denote with $v_+$ the set of outgoing germs of edges with source $v$. A fundamental labeling of $\calE$ is a function $i : \calE \rightarrow I$, and for every $v \in \calV$ the morphism space
\[
 \calC(i,v) := \calC \left( \bigotimes_{e \in v_-} V_{i(e)},\bigotimes_{e \in v_+} V_{i(e)} \right)
\]
is called the \textit{multiplicity module} of $i$ in $v$. Then, let us consider the embedded oriented trivalent graph
\begin{equation}\label{E:triv_graph}
 \calG_g := \pic{trivalent_graph} \subset \R^3, 
\end{equation}
and let us denote with $\calV_g$ and $\calE_g$ its sets of vertices and edges respectively. We should think of $\Sigma_g$ as being identified with the boundary of a regular neighborhood of $\calG_g$. Then, the state space $\rmV_\calC(\Sigma_g)$ decomposes as a direct sum of tensor products of multiplicity modules
\begin{equation}\label{E:E:st_sp_sem-sim_dec}
 \rmV_\calC(\Sigma_g) \cong \bigoplus_{i : \calE_g \to I} \bigotimes_{v \in \calV_g} \calC(i,v).
\end{equation}
