---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-010-35-the-pivotal-operators-as-a-monoidal-functor
section_title: "The pivotal operators as a monoidal functor"
section_number: 3.5
pages: 16-18
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.988
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
\label{piv_monoidal}
We want to precisely relate the pivotal operators with the more traditional notion of the `double dual functor'. We first need to show that the pivotal operators can be viewed as equipping the identity functor with coherence isomorphisms making it into a monoidal functor. 

\begin{lem} \label{extend}Suppose $F,G : \cat{D} \rightarrow \cat{D}'$ are linear functors between semisimple categories. Let $\theta_{i} : F(X_i) \rightarrow G(X_i)$ be a collection of maps, where $X_i$ ranges over the representatives of the simple objects of $\cat{D}$. Then there exists a unique natural transformation $\theta : F \Rightarrow G$ such that $\theta_{X_i} = \theta_i$.
\end{lem}
\begin{proof} Let $A \in \cat{D}$, and for each $i$, choose a basis $\{e_\alpha : X_i \rightarrow A\}$ for $\Hom(X_i, A)$ with corresponding dual basis $\{e^\beta : A \rightarrow X_i\}$. Set  $\theta_A = \sum_{i,\alpha} G(e_\alpha) \circ \theta_i \circ F(e^\alpha)$. The rest of the proof (naturality of $\theta$ and its uniqueness) is the same as \cite[Lemma 3.9]{BBthesis}.
\end{proof}
This allows us to extend the pivotal operators $T^i_{jk}$, initially defined only on the simple objects, to a natural transformation $T \equiv \{T_{A,B} :\ A \otimes B \rightarrow A \otimes B$\} where $A$ and $B$ are arbitrary objects of $\cat{C}$.
\begin{cor} The pivotal operators $T^i_{jk}$ extend uniquely to a natural transformation $T : \otimes \Rightarrow \otimes$ from the tensor functor $\otimes : \cat{C} \boxtimes \cat{C} \rightarrow \cat{C}$ to itself. \label{extend_cor}
\end{cor}
\begin{proof}
The pivotal operators $T^i_{jk} : \Hom(X_i, X_j \otimes X_k) \rightarrow \Hom(X_i, X_j \otimes X_k)$ induce maps
\[
T_{j,k} : X_j \otimes X_k \rightarrow X_j \otimes X_k
\]
for each pair of simple objects $X_j$, $X_k$, defined uniquely by the requirement that for each simple object $X_i$, the map on the hom-sets given by post-composing with $T_{j,k}$,
\begin{align*}
 \text{post}(T_{j,k}) : \Hom(X_i, X_j \otimes X_k) & \rightarrow \Hom(X_i, X_j \otimes X_k)  \\
 f & \mapsto T_{j,k} \circ f
\end{align*}
is equal to $T^i_{jk}$. That is, we require $\text{post}(T_{j,k}) = T^i_{j,k}$ as endomorphisms of the vector space $\Hom(X_i, X_j \otimes X_k)$. By the Yoneda lemma, this indeed gives unique well-defined maps $T_{j,k}$. Now apply Lemma \ref{extend} to the case $\cat{D} =\cat{C} \boxtimes \cat{C}$, $\cat{D}' = \cat{C}$, and $F$($=G$) given by the tensor functor $\otimes : \cat{C} \boxtimes \cat{C} \rightarrow \cat{C}$.  
\end{proof}
Recall that a monoidal functor $(F, T, \phi) : \cat{C} \rightarrow \cat{D}$ \label{monoidal_page}  between monoidal categories $\cat{C}$ and $\cat{D}$ consists of a functor $F :\ \cat{C}\ \rightarrow \cat{D}$ together with natural isomorphisms $\{T_{A,B} : F(A) \otimes F(B) \rightarrow F(A \otimes B), \, A, B \in \cat{C}\}$ and $\phi : 1_{\cat{D}} \rightarrow F(1_{\cat{C}})$ satisfying certain coherence equations.
\begin{prop} The pivotal operators $T^i_{jk}$, when extended to a natural transformation $\{T_{A,B} : A \otimes B \rightarrow A \otimes B\}$, obey the coherence isomorphisms making $T := (\id, T, \id) :\ \cat{C} \rightarrow \cat{C}$ a monoidal functor.
\end{prop}

\begin{proof} By Lemma \ref{extend}, we only need to check the coherence equations on the simple objects. The unit coherence equations are $T^1_{i,1} = T^1_{1,i} = \id$, which is automatically satisfied due to the rigidity equations \eqref{snake_eqns}. The coherence conditions on $T$ are:
\begin{equation} \label{coherence_on_T}
\begin{tikzpicture}[xscale=6, yscale=1.5]
\node (1) at (0,0) {$ (F(X_j) \otimes F(X_k) ) \otimes F(X_l)$};
\node (2) at (0.2,1) {$F(X_j \otimes X_k) \otimes F(X_l)$};
\node (3) at (1.2,1) {$F((X_j \otimes X_k) \otimes X_l)$};
\node (4) at (1.4,0) {$F(X_j \otimes (X_k \otimes X_l))$};
\node (5) at (0.2,-1) {$F(X_j) \otimes (F(X_k) \otimes F(X_l))$};
\node (6) at (1.2,-1) {$F(X_j) \otimes F(X_k \otimes X_l)$};
\draw[->] (1) to node[left] {$T_{X_j, X_k} \otimes \id$} (2); 
\draw[->] (2) to node[above] {$T_{X_j \otimes X_k, X_l}$} (3); 
\draw[->] (3) to node[right] {$F(a_{X_j, X_k, X_l})$} (4); 
\draw[->] (1) to node[left] {$a_{F(X_j), F(X_k), F(X_l)}$} (5); 
\draw[->] (5) to node[below] {$\id \otimes T_{X_k, X_l}$} (6); 
\draw[->] (6) to node[right] {$T_{X_j, X_k \otimes X_l}$} (4); 
\end{tikzpicture} 
\end{equation}
Apply this diagram to the basis vectors \eqref{basis_choice}, working in a pivotal basis to simplify the calculation. It becomes the requirement that
\begin{equation}
\ba \ig{c2.pdf} \ea = \sum_{n, \gamma, \delta} (F^i_{jkl})^{\alpha m \beta}_{\gamma n \delta} \, \ba \ig{c3.pdf} \ea \label{monoidal_pivotal}
\end{equation}
To prove \eqref{monoidal_pivotal}, insert the graphical definition \eqref{defn_piv_operator} of the pivotal operators into \eqref{monoidal_pivotal}, and expand out the left hand side using the associator expansion \eqref{associator_eqn}. As in the proof of Theorem \ref{piv_involution_thm}, we obtain two diagrams which are rigidly isotopic, hence equal.  
\end{proof}
\begin{cor} In a pivotal basis, the pivotal symbols satisfy
\begin{equation} \label{2-cocycle} 
 \epsilon^i_{jk, \alpha} \epsilon^m_{kl, \beta} = \epsilon^i_{nl, \gamma} \epsilon^n_{jk, \delta} \quad \text{whenever } (F^i_{jkl})^{\gamma n \delta}_{\alpha m \beta} \neq 0.
\end{equation}
\end{cor}

\begin{proof}
This is precisely what \eqref{monoidal_pivotal} says, in a pivotal basis.
\end{proof}
\begin{rem} The equation \eqref{2-cocycle} satisfied by the $\epsilon^i_{jk, \alpha}$ is formally similar to the equation satisfied by the 2nd Stiefel-Whitney 2-cocycle $w_2(M) \in H^2(M, \mathbb{Z}/2\mathbb{Z})$ of an oriented manifold $M$ in \v{C}ech cohomology \cite{naber-2011}. It can be thought of as a `$\mathbb{Z}/2$ version' of the 2-cocycle condition in Davydov-Yetter cohomology of the fusion category, see Example \ref{2-cocycle-example}. \label{remark_2_cocycle}
\end{rem}

Let us summarize the results of this section explicitly as follows.

\begin{thm}[{cf. \cite[Thm 2.6]{eno02-ofc}}] Every fusion category $\cat{C}$ over $\mathbb{C}$ comes equipped with a canonical monoidal endofunctor $\mathcal{T} : C \rightarrow C$, the pivotal endofunctor, satisfying:
\begin{itemize}
 \item The underlying functor of $\mathcal{T}$ is the identity functor,
 \item The monoidal coherence isomorphisms $T : A \otimes B \rightarrow A \otimes B$ of $\mathcal{T}$ are specified by the pivotal operators $T^i_{jk}$, extended to a natural transformation using Corollary \ref{extend_cor},
 \item $\mathcal{T}^2 = \id$. 
\end{itemize}
 \label{piv_operator_C}
\end{thm}
