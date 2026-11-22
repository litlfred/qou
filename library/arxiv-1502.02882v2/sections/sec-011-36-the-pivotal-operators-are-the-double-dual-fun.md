---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-011-36-the-pivotal-operators-are-the-double-dual-fun
section_title: "The pivotal operators are the double dual functor"
section_number: 3.6
pages: 18-20
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.985
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
\label{pivops}
Our approach to the `double dual functor' on a fusion category $\cat{C}$ been to encode it in a canonical monoidal endofunctor $\mathcal{T} : \cat{C} \rightarrow \cat{C}$, whose underlying functor is simply the identity. The advantage of our approach is that it is canonical, not requiring arbitrary choices of duals for objects. Such fixed initial choices of duals tend to complicate calculations, as the expression for $\omega_{V,W}$ in equation \eqref{defn_omega} below shows.  We now connect our approach to the usual approach, taking more care than is common in the literature. 

We define a {\em system of right duals} on a fusion category $\cat{C}$ as a choice, for every object $V \in \cat{C}$, of a triple
\[
(V^*, \, \eta_V : 1 \rightarrow V^* \otimes V, \, \epsilon_V : V \otimes V^* \rightarrow 1)
\]
which equips $V^*$ as a right dual of $V$. It is then a routine calculation to check that this makes $* : \cat{C} \rightarrow \cat{C}^\text{op}$ into a well-defined functor, which is equipped with canonical isomorphisms $V^* \otimes W^* \rightarrow (W \otimes V)^*$ making it into a monoidal functor. In particular, given such a choice of right duals, we have the associated double dual monoidal endofunctor $**$ of $\cat{C}$, and the following explicit coherence isomorphisms $\omega_{V, W} : V^{**} \otimes W^{**} \rightarrow (V \otimes W)^{**}$, expressed graphically as follows:
\begin{equation} \label{defn_omega}
\omega_{V,W} = \ba \ig{h11.pdf} \ea 
\end{equation}
Given any other system of right duals $*'$ on $\cat{C}$, there is a unique monoidal natural isomorphism $\vartheta : * \Rightarrow *'$ such that $\eta_{V^{*'}} = (\vartheta \otimes \id_V) \circ \eta_{V^*}$. Horizontally composing $\vartheta$ with itself, we get a monoidal natural isomorphism $\theta : ** \Rightarrow *' *'$.

\begin{thm} \begin{enumerate} 
\item Given any system of right duals $*$ on a fusion category $\cat{C}$, there is a canonical monoidal natural isomorphism $\beta: \mathcal{T} \Rightarrow **$.
\item These isomorphisms are natural in the following sense: if $*'$ is another system of right duals on $\cat{C}$, then the diagram
\[
\begin{tikzpicture}[scale=2]
 \node (1) at (0,0) {$V$};
 \node (2) at (0, -1) {$V^{**}$};
 \node (3) at (1, -1) {$V^{*' *'}$};
 \draw[->] (1) -- node[left] {$\beta^{(*)}_V$} (2);
 \draw[->] (1) -- node[above right] {$\beta_V^{(*')}$} (3);
 \draw[->] (2) -- node[below] {$\theta_V$} (3); 
\end{tikzpicture}
\]
commutes for all $V \in \cat{C}$.
\end{enumerate}
\end{thm}
\begin{proof}
(i) We define $\beta_V$ by choosing a basis $e_{i, \alpha} : X_i \rightarrow V$ for the hom-sets $\Hom(X_i, V)$ where $i$ ranges over a representative set of simple objects, with corresponding dual basis $\hat{e}_{i, \alpha}$, and then setting 
\begin{equation} \label{defn_beta}
\beta_V := \sum_{i, \alpha} \ba \ig{h12.pdf} \ea 
\end{equation}
where we have used the partner convention on the $X_i$ strands. It is easy to check that this definition is independent of the basis choice $e_{i, \alpha}$, and that this indeed defines a natural transformation $\beta : \mathcal{T} \Rightarrow **$ of the underlying functors. For $\beta$ to be monoidal, we need to verify that the following coherence diagram commutes:
\begin{equation} \label{comm_check_diagram}
\begin{tikzpicture}[xscale=3, yscale=2]
\node (1) at (0,0) {$V \otimes W$};
\node (2) at (1,0) {$V \otimes W$};
\node (3) at (0, -1) {$(V \otimes W)^{**}$};
\node (4) at (1, -1) {$V^{**} \otimes W^{**}$};
\draw [->] (1) -- node[above] {$T_{V,W}$} (2);
\draw [->] (1) -- node[left] {$\beta_V \otimes \beta_W$} (3);
\draw [->] (3) -- node[below] {$\omega_{V, W}$} (4);
\draw [->] (2) -- node[right] {$\beta_{V \otimes W}$} (4);
\end{tikzpicture}
\end{equation}
Substitute the definition \eqref{defn_omega} of $\omega_{V, W}$ and the definition \eqref{defn_beta} of $\beta_V$ into the equation \eqref{comm_check_diagram}. The left and right hand sides simplify considerably. It is sufficient to check the remaining identity on the representative simple objects $V = X_k$, $W = X_l$, where it is an elementary string diagram verification, best performed in a pivotal basis. The diagram for part (ii) is simpler and can be verified directly.  
\end{proof}
Combining this with Theorem \ref{piv_operator_C}, which says that $\mathcal{T}^2 = \id$, we immediately obtain the following.
\begin{cor}[{cf. \cite[Thm 2.6]{eno02-ofc}}] For any system of right duals $*$ on a fusion category $\cat{C}$, there is a canonical monoidal natural isomorphism $\id \Rightarrow {*}{*}{*}{*}$, which is natural with respect to the choice of system of right duals $*$. \label{explicit_eno_cor}
\end{cor}
