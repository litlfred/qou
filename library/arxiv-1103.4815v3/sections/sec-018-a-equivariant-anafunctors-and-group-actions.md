---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-018-a-equivariant-anafunctors-and-group-actions
section_title: "A Equivariant Anafunctors and Group Actions"
section_number: null
pages: 57-59
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 1.0
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{sec:equivariantanafunctorsandgroupactions}

In this section we are concerned with a Lie 2-group $\Gamma$ and Lie groupoids   $\mathcal{X}$ and $\mathcal{Y}$  with actions $R_1: \mathcal{X} \times \Gamma \to \mathcal{X}$ and $R_2: \mathcal{Y} \times \Gamma \to \mathcal{Y}$.

\begin{definition}
\label{def:actionanafunctor}
An \emph{action} of the 2-group $\Gamma$ on an anafunctor $F:\mathcal{X} \to \mathcal{Y}$ is an ordinary smooth action
$\rho: F \times \Gamma_1 \to F$
of the group $\Gamma_1$ on the total space $F$ that
\begin{enumerate}[(i)]

\item
preserves the anchors in the sense that the diagrams
\begin{equation*}
\alxydim{@R=1.3cm}{F \times \Gamma_1 \ar[d]_{\alpha_l \times t} \ar[r]^-{\rho} & F \ar[d]^{\alpha_l} \\ \mathcal{X}_0 \times \Gamma_0 \ar[r]_-{R_1} & \mathcal{X}_0}
\quand
\alxydim{@R=1.3cm}{F \times \Gamma_1 \ar[r]^-{\rho} \ar[d]_{\alpha_r \times s} & F \ar[d]^{\alpha_r} \\ \mathcal{Y}_0 \times \Gamma_0 \ar[r]_-{R_2} & \mathcal{Y}_0}
\end{equation*}
are commutative.

\item
is compatible with the $\Gamma$-actions in the sense that the identity
\begin{equation*}
\rho(\chi \circ f \circ \eta,\gamma_l \circ \gamma \circ \gamma_r) =R_1(\chi,\gamma_l) \circ  \rho(f,\gamma) \circ R_2(\eta,\gamma_r)
\end{equation*}
holds for all appropriately composable $\chi\in \mathcal{X}_1$, $\eta\in \mathcal{Y}_1$, $f\in F$, and $\gamma_l,\gamma,\gamma_r\in \Gamma_1$.
\end{enumerate} 
If $F_1,F_2:\mathcal{X} \to \mathcal{Y}$ are anafunctors with $\Gamma$-action, a transformation $\eta: F_1 \Rightarrow F_2$ is called $\Gamma$-equivariant if the map $\eta:F_1 \to F_2$ between total spaces is $\Gamma_1$-equivariant in the ordinary sense. 
\end{definition}



Anafunctors $\mathcal{X} \to \mathcal{Y}$ with $\Gamma$-actions together with $\Gamma$-equivariant transformations form a groupoid $\af_{\Gamma}(\mathcal{X},\mathcal{Y})$. On the other hand, there is another groupoid $\Gamma\text{-}\af(\mathcal{X},\mathcal{Y})$ consisting of  $\Gamma$-equivariant anafunctors (Definition \ref{def:equivanafunctor}) and $\Gamma$-equivariant transformations (Definition \ref{def:equivtransformation}). 
\begin{lemma}
\label{lem:equivarianceidentification}
The categories $\af_{\Gamma}(\mathcal{X},\mathcal{Y})$ and $\Gamma\text{-}\af(\mathcal{X},\mathcal{Y})$ are canonically isomorphic.
\end{lemma}


\begin{proof}
We construct a functor
\begin{equation}
\mathcal{E}: \af_{\Gamma}(\mathcal{X},\mathcal{Y}) \to \Gamma\text{-}\af(\mathcal{X},\mathcal{Y})\text{.}
\end{equation}
Let $F:\mathcal{X} \to \mathcal{Y}$ be an anafunctor with $\Gamma$-action $\rho$. We shall define a transformation
\begin{equation*}
\lambda_{\rho}: F \circ R_1 \Rightarrow R_2 \circ (F \times \id)\text{.}
\end{equation*}
First of all, the composite
\begin{equation*}
\alxydim{}{\mathcal{X} \times \Gamma \ar[r]^-{R_1} & \mathcal{X} \ar[r]^{F} & \mathcal{Y}}
\end{equation*}
is given by the total space $(\mathcal{X}_0 \times \Gamma_0) \lli{R_1} \times_{\alpha_l} F$, left and right anchors send an element $(x,g,f)$ to $(x,g)$ and $\alpha_r(f)$, respectively, and the actions are
\begin{equation*}
(\chi,\gamma) \circ (x,g,f) = (t(\chi),t(\gamma),R_1(\chi,\gamma) \circ f)
\quand
(x,g,f) \circ \eta = (x,g,f\circ \eta)\text{.}
\end{equation*}
On the other hand, the composite
\begin{equation*}
\alxydim{}{\mathcal{X} \times \Gamma \ar[r]^{F \times \id} & \mathcal{Y} \times \Gamma \ar[r]^-{R_2} & \mathcal{Y}} 
\end{equation*}
is given by the total space $((F \times \Gamma_1) \lli{R_2 \circ (\alpha_r \times s)} \times_{t} \mathcal{Y}_1) / \sim$ with the equivalence relation
\begin{equation*}
(f \circ \eta',\gamma \circ \gamma',\eta) \sim (f,\gamma,R_2(\eta',\gamma') \circ \eta)\text{.}
\end{equation*}
The left and right anchors send an element $(f,\gamma,\eta)$ to $(\alpha_l(f),t(\gamma))$ and $s(\eta)$, respectively, and the actions are
\begin{equation*}
(\chi,\gamma') \circ (f,\gamma,\eta) = (\chi \circ f,\gamma'\circ \gamma,\eta)
\quand
(f,\gamma,\eta) \circ \eta' = (f,\gamma,\eta \circ \eta')\text{.}
\end{equation*}
The inverse of the following map will define the transformation $\lambda$:
\begin{equation*}
 (F \times \Gamma_1) \lli{R_2 \circ (\alpha_r \times s)} \times_{t} \mathcal{Y}_1 \to (\mathcal{X}_0 \times \Gamma_0) \lli{R_1} \times_{\alpha_l} F: (f,\gamma,\eta) \mapsto (\alpha_l(f),t(\gamma),\rho(f,\gamma)\circ \eta)\text{.} \end{equation*}
Condition (i) ensures that this map ends in the correct fibre product, and condition (ii) assures that it is well-defined under the equivalence relation $\sim$. The left anchors are automatically respected, and the right anchors require condition (i). Similarly, the left action is respected automatically, and the right actions due to condition (ii). The axiom for a transformation is satisfied because $\rho$ is a group action. This defines the functor $\mathcal{E}$ on objects. On morphisms, it is straightforward to check that the conditions on both hand sides coincide; in particular, $\mathcal{E}$ is full and faithful. 


In order to prove that the functor $\mathcal{E}$ is an isomorphism, we start with a given $\Gamma$-equivariant structure $\lambda$ on the anafunctor $F$. Then, an action $\rho: F \times \Gamma_1 \to F$ is defined by
\begin{equation*}
(f,\gamma) \mapsto \mathrm{pr}_3(\lambda^{-1}(f,\gamma,\id_{R_2(\alpha_r(f),s(\gamma))})) \end{equation*}
with $\mathrm{pr}_3: (\mathcal{X}_0 \times \Gamma_0) \lli{R_1} \times_{\alpha_l} F \to F$ the projection. The axiom for an action is satisfied due to the identity $\lambda$ obeys. 
It is straightforward to verify conditions (i) and (ii) of Definition \ref{def:actionanafunctor}.
\begin{comment}
Indeed, 
\begin{eqnarray*}
\alpha_l(\rho(f,\gamma))
&=& \alpha_l(\mathrm{pr}_3(\lambda^{-1}(f,\gamma,\id_{R_2(\alpha_r(f),s(\gamma))})))
\\&=& R_1(\alpha_l(\lambda^{-1}(f,\gamma,\id_{R_2(\alpha_r(f),s(\gamma))})))
\\&=& R_1(\alpha_l(f),t(\gamma))
\end{eqnarray*}
using that $\lambda$ preserves the left anchors, and
\begin{eqnarray*}
\alpha_r(\rho(f,\gamma)) &=& \alpha_r(\mathrm{pr}_3(\lambda^{-1}(f,\gamma,\id_{R_2(\alpha_r(f),s(\gamma))})))
\\&=& \alpha_r(f,\gamma,\id_{R_2(\alpha_r(f),s(\gamma))})
\\&=& s(\id_{R_2(\alpha_r(f),s(\gamma))})
\\&=& R_2(\alpha_r(f),s(\gamma))
\end{eqnarray*}
using that $\lambda$ preserves the right anchors. For the compatibility with the actions,
\begin{eqnarray*}
\rho(\chi \circ f \circ \eta,\gamma_l \circ \gamma \circ \gamma_r) &=& \mathrm{pr}_3(\lambda^{-1}(\chi \circ f \circ \eta,\gamma_l \circ \gamma \circ \gamma_r,\id_{R_2(s(\eta),s(\gamma_r))})) \\&=& \mathrm{pr}_3((\chi,\gamma_l) \circ \lambda^{-1}( f \circ \eta, \gamma \circ \gamma_r,\id_{R_2(s(\eta),s(\gamma_r))}))
\\&=& R_1(\chi,\gamma_l) \circ  \mathrm{pr}_3(\lambda^{-1}( f, \gamma,R_2(\eta,\gamma_r)))
\\&=& R_1(\chi,\gamma_l) \circ  \mathrm{pr}_3( \lambda^{-1}( f, \gamma,\id) \circ R_2(\eta,\gamma_r))
\\&=& R_1(\chi,\gamma_l) \circ  \mathrm{pr}_3( \lambda^{-1}( f, \gamma,\id) )\circ R_2(\eta,\gamma_r)\text{.}
\end{eqnarray*}
\end{comment}
To close the proof it suffices to notice that the two procedures we have defined are (strictly) inverse to each other.
\end{proof}

We are also concerned with  the composition of anafunctors with $\Gamma$-action. Suppose that $\mathcal{Z}$ is a third Lie groupoid with a $\Gamma$-action $R_3$, and $F:\mathcal{X} \to \mathcal{Y}$ and $G:\mathcal{Y} \to \mathcal{Z}$ are anafunctors with $\Gamma$-actions  $\rho:F \times \Gamma_1 \to F$ and $\tau: G \times \Gamma_1 \to G$. Then, the composition $G \circ F$ is equipped with the $\Gamma$-action defined by
\begin{equation}
\label{eq:companafunctorsaction}
(F \times_{\mathcal{Y}_0} G) \times  \Gamma_1 \to (F \times_{\mathcal{Y}_0} G): ((f,g),\gamma) \mapsto (\rho(f,\gamma),\tau(g,\id_{s(\gamma)}))\text{.}
\end{equation}
We leave it to the reader to check

\begin{lemma}
\label{lem:actioncomposition}
\label{lemactionequivariantidentity}
Let $\mathcal{X}$, $\mathcal{Y}$ and $\mathcal{Z}$ be Lie groupoids with $\Gamma$-actions $R_1$, $R_2$ and $R_3$.
\begin{enumerate}[(a)]
\item 
Let $F: \mathcal{X} \to \mathcal{Y}$ and $G: \mathcal{Y} \to \mathcal{Z}$ be $\Gamma$-equivariant anafunctors. If $\Gamma$-equivariant structures on $F$ and $G$ correspond to $\Gamma_1$-actions under the isomorphism of Lemma \ref{lem:equivarianceidentification}, then the $\Gamma$-equivariant structure on the composite $F \circ G$ corresponds to the $\Gamma_1$-action defined above. 

\item
The isomorphism of Lemma \ref{lem:equivarianceidentification} identifies the trivial $\Gamma$-equivariant structure on the identity anafunctor $\id: \mathcal{X} \to \mathcal{X}$ with the $\Gamma_1$-action $R_1: \mathcal{X}_1 \times \Gamma_1 \to \mathcal{X}_1$ on its total space $\mathcal{X}$.
\end{enumerate}
\end{lemma}

\begin{comment}
For (a), one calculates that the following diagram is commutative:
The $\Gamma$-equivariant structure on the composition $G \circ F$ is by definition the following composition:
\begin{equation*}
\tiny
\alxydim{@C=0cm}{
T \circ ((G \circ F) \times \id) \ar[d] &=&
[(F \lli{\alpha_r} \times_{\alpha_l} G) \times \Gamma_1] \lli{T \circ (\alpha_r \times s)} \times_{t} \mathcal{Z}_1]/\sim & \ni & (f,g,\gamma,\zeta) \ar@{|->}[d]
\\
(T \circ (G \times \id)) \circ (F \times \id) \ar[d] &=& [(F \times \Gamma_1) \lli{\alpha_r \times s} \times_{\alpha_l \times t}(G \times \Gamma_1) \lli{T \circ (\alpha_r \times s)} \times_{t} \mathcal{Z}_1] / \sim &\ni& (f,\gamma,g,\id_{s(\gamma)},\zeta) \ar@{|->}[d]
\\
(G \circ S) \circ (F \times \id) \ar[d] &=& [(F \times \Gamma_1) \lli{S \circ (\alpha_r \times s)} \times _{\alpha_l} G] / \sim &\ni& (f,\gamma,\tau(g,\id_{s(\gamma)})\circ \zeta)\ar@{|->}[d]
\\
G \circ (S \circ (F \times \id)) \ar[d] &=& [(F \times \Gamma_1) \lli{S \circ (\alpha_r \times s)} \times_t \mathcal{Y}_1 \lli{s}\times_{\alpha_l} G] / \sim &\ni& (f,\gamma,\id_{S(\alpha_r(f),s(\gamma))},\tau(g,\id_{s(\gamma)})\circ \zeta)\ar@{|->}[d]
\\
(G \circ F) \circ R &=&
[(\mathcal{X}_0 \times \Gamma_0) \lli{R} \times_{\alpha_l} (F \lli{\alpha_r} \times_{\alpha_l} G)] / \sim & \ni &  (\alpha_l(f),t(\gamma),\rho(f,\gamma),\tau(g,\id_{s(\gamma)})\circ \zeta)
}
\end{equation*}
The assignment on the right hand side is the equivariant structure induced from the stated action. 
\end{comment}



\setsecnumdepth{1}
