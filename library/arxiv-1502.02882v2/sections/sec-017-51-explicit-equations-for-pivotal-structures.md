---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-017-51-explicit-equations-for-pivotal-structures
section_title: "Explicit equations for pivotal structures"
section_number: 5.1
pages: 26-27
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.978
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
\label{Explicit_equations} 

In Section \ref{piv_monoidal} we showed that, by using the pairing convention, every fusion category over $\mathbb{C}$ comes equipped with a canonical monoidal endofunctor $T : \cat{C} \rightarrow \cat{C}$, the pivotal endofunctor, whose underlying functor is simply the identity, with the pivotal operators $T^i_{jk}$ supplying the coherence isomorphisms.

On the other hand, a {\em pivotal structure} on a fusion category is usually defined (see eg. \cite{eno02-ofc, bw99-sc}) by making choices of right duals $(V^*, \eta_V, \epsilon_V)$ for every object $V$ as in Section \ref{pivops}, giving rise to a monoidal double dual functor $** : \cat{C} \rightarrow \cat{C}$, and then declaring that a pivotal structure is a monoidal natural isomorphism $\gamma : \id \Rightarrow **$.  In Section \ref{pivops} we showed that there is a canonical monoidal natural isomorphism $\mathcal{T} \cong **$. Thus, to avoid fixing choices of duals, in this paper we adopt the following cleaner definition. 

\begin{defn} A pivotal structure on a fusion category over $\mathbb{C}$ is a monoidal natural isomorphism $\gamma: \id \Rightarrow \mathcal{T}$, where $\mathcal{T}$ is the canonical pivotal endofunctor of the category.
\end{defn}
For an alternative formulation in terms of {\em even-handed structures}, see \cite{BBthesis}. Under this definition, quantum dimensions are defined as follows. 
\begin{defn} Let $\gamma$ be a pivotal structure on a fusion category. The {\em quantum dimension} of an object $V$ with respect to $\gamma$ is defined as
\[
 \dim_\gamma (V) = \ig{d107.pdf}
\]
where the pairing convention has been used. The pivotal structure $\gamma$ is {\em spherical} when $\dim_\gamma (V) = \dim_\gamma (V^*)$ for all objects $V$.
\end{defn}
The following is clear.
\begin{lem} The quantum dimension of a simple object $X_i$ with respect to a pivotal structure $\gamma$ computes as $\dim_\gamma(X_i) = \gamma_i d_i$ where $d_i$ is the fusion dimension of $X_i$. \label{dimension_simple}
\end{lem}

Under these conventions, we have the following.

\begin{thm} A pivotal structure on fusion category $\cat{C}$ with representative simple objects $X_i$, $i \in I$ corresponds to a collection of numbers $\gamma_i \in U(1)$, $i \in I$ satisfying
\begin{equation} \label{piveqn2}
 \gamma_j \gamma_k \id = \gamma_i T^i_{jk} \quad \text{whenever $X_i$ is a summand of $X_j \otimes X_k$} 
\end{equation}
where the $T^i_{jk}$ are the pivotal operators of the fusion category. Moreover, the pivotal structure is spherical precisely when $\gamma_i = \pm 1$ for all $i \in I$. \label{piv_structure_thm}
\end{thm}
\begin{proof}
By Lemma \ref{extend}, $\gamma$ is uniquely determined by its components $\gamma_i = \gamma_{X_i}$ on the representative simple objects $X_i$. The coherence equation for being a monoidal natural isomorphism reduces to the scalars $\gamma_i \in \mathbb{C}^\times$ obeying \eqref{piveqn2}. Given a solution to \eqref{piveqn2}, the collection $\{ \pm \gamma_i\}$ forms a finite subgroup of $\mathbb{C}^\times$ and hence $\gamma_i \in U(1)$.  Since $T^1_{11} = \id$ from Lemma \ref{triv_pivs}, we have $\gamma_1 = 1$, and similarly since $T^1_{ii^*} = \id$, we have $\gamma_i = \overline{\gamma_{i^*}}$ for all $i \in I$. From Lemma \ref{dimension_simple}, if $\gamma$ is spherical, then $\gamma_i d_{i^*} = \gamma_{i^*} d_{i^*}$ whence $\gamma_i = \gamma_{i^*}$ since $d_{i^*} = d_i$. Hence $\gamma_i = \pm 1$.  
\end{proof}
\begin{cor}[{cf. \cite[Prop 8.23]{eno02-ofc}}] A pseudo-unitary fusion category admits a canonical spherical structure. \label{pseudo_cor}
\end{cor}
\begin{proof}
Follows from Corollary \ref{pseudo_unitary}.
\end{proof}

\begin{defn} We say that a fusion category $\cat{C}$ over $\mathbb{C}$ is {\em orientable} if the pivotal symbols $\epsilon^i_{jk, \alpha}$ do not depend on $\alpha$, that is, $T^i_{jk} = \epsilon^i_{jk} \id$ for some signs $\epsilon^i_{jk} = \pm 1$.
\end{defn}
Clearly we have the following.
\begin{lem} If a fusion category is not orientable, then it does not admit a pivotal structure. 
\end{lem}
Recall from Theorem \ref{formula_piv} that the pivotal operators can be expressed in terms of the apex associator monodromy operators.
\begin{prop} If the apex associator monodromy $A_{ijk} = \id$ for all $i,j,k \in I$, then the fusion category admits a canonical spherical structure.
\end{prop}
\begin{proof} If $A_{ijk} = \id$, then from Theorem \ref{formula_piv}, 
\[
T^i_{jk} = p_i p_j p_k \id
\]
where the $p_i = \pm 1$ are the pivotal indicators. Hence setting $\gamma_i = p_i$ will solve \eqref{piveqn2}.
\end{proof}
