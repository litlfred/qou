---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-013-61-definition-of-principal-2-bundles
section_title: "Definition of Principal 2-Bundles"
section_number: 6.1
pages: 33-36
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.854
latex_coverage_ratio: 0.974
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{sec:definitionzwoabundle}

As an important prerequisite for principal 2-bundles we have to discuss actions of Lie 2-groups on Lie groupoids, and equivariant anafunctors.

\begin{definition}
\label{def:rightaction}
Let $\mathcal{P}$ be a Lie groupoid, and let $\Gamma$ be a Lie 2-group. A \emph{smooth right action of $\Gamma$ on $\mathcal{P}$} is a smooth functor
$R: \mathcal{P} \times \Gamma \to \mathcal{P}$
such that $R(p,1)=p$ and $R(\rho,\id_1)=\rho$ for all $p\in \mathcal{P}_0$ and $\rho\in \mathcal{P}_1$,  and such that the diagram
\begin{equation*}
\alxydim{@=1.3cm}{\mathcal{P} \times \Gamma \times \Gamma \ar[r]^-{\id \times m} \ar[d]_{R \times \id} & \mathcal{P} \times \Gamma  \ar[d]^{R} \\ \mathcal{P} \times \Gamma \ar[r]_{m} & \mathcal{P}}
\end{equation*}
of smooth functors is commutative (strictly, on the nose).
\end{definition}


For example, every Lie 2-group acts on itself via multiplication. Note that due to strict commutativity, one has $R(R(p,g),g^{-1})=p$ and $R(R(\rho,\gamma),i(\gamma))=\rho$ for all $g\in \Gamma_0$, $p\in \mathcal{P}_0$, $\gamma\in \Gamma_1$ and $\rho\in \mathcal{P}_1$. 

\begin{remark}
This definition could be weakened  in two steps. First, one could allow a natural transformation in the above diagram instead of commutativity. Secondly, one could allow $R$ to be an anafunctor instead of an ordinary functor.  It turns out that for our purposes the above definition is sufficient. 
\end{remark}

\begin{definition}
\label{def:equivanafunctor}
Let $\mathcal{X}$ and $\mathcal{Y}$ be Lie groupoids with smooth actions $(R_1,\rho_1)$, $(R_2,\rho_2)$ of a Lie 2-group $\Gamma$. An \emph{equivariant structure} on an anafunctor $F: \mathcal{X} \to \mathcal{Y}$ is a transformation
\begin{equation*}
\alxydim{@=1.3cm}{\mathcal{X} \times \Gamma \ar[d]_{F \times\id} \ar[r]^-{R_1} & \mathcal{X} \ar@{=>}[dl]|*+{\lambda} \ar[d]^{F} \\ \mathcal{Y} \times \Gamma \ar[r]_-{R_2} & \mathcal{Y}}
\end{equation*}
satisfying the following condition:
\begin{equation*}
\alxydim{@R=0.6cm@C=0.2cm}{\mathcal{X} \times \Gamma \times \Gamma \ar[rr]^{\id \times m} \ar[dr]|{R_1 \times \id} \ar[dd]_{F \times \id\times\id} && \mathcal{X} \times \Gamma  \ar[dr]^{R_1} & \\ & \mathcal{X} \times \Gamma \ar@{=>}[dl]|{\lambda \times \id} \ar[rr]|{R_1} \ar[dd]|{F \times \id} && \mathcal{X} \ar@{=>}[ddll]|*+{\lambda} \ar[dd]^{F} \\ \mathcal{Y} \times \Gamma \times \Gamma \ar[dr]_{R_2 \times \id} &&& \\ & \mathcal{Y} \times \Gamma  \ar[rr]_{R_2} && \mathcal{Y}}
\qquad=\qquad
\alxydim{@R=0.6cm@C=0.2cm}{\mathcal{X} \times \Gamma \times \Gamma \ar[rr]^{\id \times m} \ar[dd]_{F \times \id \times \id} && \mathcal{X} \times \Gamma  \ar[dd]|{F \times \id} \ar[dr]^{R_1} \\ &&&\mathcal{X}\ar@{=>}[dl]|{\lambda} \ar[dd]^{F} \\ \mathcal{Y} \times \Gamma \times \Gamma \ar[dr]_{R_2 \times \id} \ar[rr]|{\id \times m} && \mathcal{Y} \times \Gamma \ar[dr]|{R_2} & \\ & \mathcal{Y} \times \Gamma \ar[rr]_{R_2} && \mathcal{Y}}
\end{equation*}
An anafunctor together with a $\Gamma$-equivariant structure is called \emph{$\Gamma$-equivariant anafunctor}. 
\end{definition}

In Appendix \ref{sec:equivariantanafunctorsandgroupactions} we translate this abstract (but evidently correct) definition of equivariance into more concrete terms involving a $\Gamma_1$-action on the total space of the anafunctor.  


\begin{definition}
\label{def:equivtransformation}
If $(F,\lambda):\mathcal{X} \to \mathcal{Y}$ and $(G,\gamma): \mathcal{X} \to \mathcal{Y}$ are $\Gamma$-equivariant anafunctors, a transformation $\eta: F \Rightarrow G$ is called \emph{$\Gamma$-equivariant}, if the following equality of transformation holds:
\begin{equation*}
\alxydim{@R=1.3cm@C=2cm}{\mathcal{X} \ar@/_1.5pc/[d]_<<<<<<{G \times \id}="1" \times \Gamma \ar@/^1.5pc/[d]^<<<<<<{F \times\id}="2" \ar@{=>}"2";"1"|{\eta \times \id} \ar[r]^-{R_1} & \mathcal{X} \ar@{=>}[dl]|>>>>>>>>>>*+{\lambda} \ar[d]^{F} \\ \mathcal{Y} \times \Gamma \ar[r]_-{R_2} & \mathcal{Y}}
\quad=\quad 
\alxydim{@R=1.5cm@C=2cm}{\mathcal{X} \times \Gamma \ar[d]_{G \times\id} \ar[r]^-{R_1} & \mathcal{X} \ar@{=>}[dl]|*+{\gamma} \ar@/_1.5pc/[d]_{G}="1" \ar@/^1.5pc/[d]^{F}="2" \ar@{=>}"2";"1"|*+{\eta} \\ \mathcal{Y} \times \Gamma \ar[r]_-{R_2} & \mathcal{Y}}
\end{equation*}
\end{definition}

It follows from abstract nonsense in the bicategory of Lie groupoids, anafunctors and transformations that we have another bicategory with
\begin{itemize}
\item 
objects: Lie groupoids with smooth right $\Gamma$-actions.

\item
1-morphisms: $\Gamma$-equivariant anafunctors.

\item
2-morphisms: $\Gamma$-equivariant transformations.
\end{itemize}


We need three further notions for the definition of a principal 2-bundle. Let $M$ be a smooth manifold, and let
 $\mathcal{P}$ be a Lie groupoid. We say that a smooth functor $\pi: \mathcal{P} \to \idmorph M$ is a \emph{surjective submersion functor}, if $\pi: \mathcal{P}_0 \to M$ is a surjective submersion. 
Let $\pi:\mathcal{P} \to \idmorph M$ be a surjective submersion functor, and let $\mathcal{Q}$ be a Lie groupoid with some smooth functor $\chi:\mathcal{Q} \to \idmorph M$. Then, the fibre product $\mathcal{P} \times_M \mathcal{Q}$ is defined to be the full subcategory of $\mathcal{P} \times \mathcal{Q}$ over the submanifold $\mathcal{P}_0 \times_M \mathcal{Q}_0 \subset \mathcal{P}_0 \times \mathcal{Q}_0$. 


\begin{definition}
\label{def:zwoabun}
Let $M$ be a smooth manifold and let $\Gamma$ be a Lie 2-group.
\begin{enumerate}[(a)]

\item 
A \emph{principal $\Gamma$-2-bundle over $M$} is a Lie groupoid $\mathcal{P}$, a surjective submersion  functor $\pi: \mathcal{P} \to \idmorph M$,  and a smooth right action $R$ of $\Gamma$ on $\mathcal{P}$ that preserves  $\pi$,
such that the smooth functor
\begin{equation*}
\tau :=(\mathrm{pr}_1, R) : \mathcal{P} \times \Gamma \to \mathcal{P} \times_M \mathcal{P} \end{equation*}
is a weak equivalence.

\item
A \emph{1-morphism} between principal $\Gamma$-2-bundles is a  $\Gamma$-equivariant anafunctor 
\begin{equation*}
F: \mathcal{P}_1 \to \mathcal{P}_2
\end{equation*}
that respects the surjective submersion functors to $M$.
 
\item 
A \emph{2-morphism} between 1-morphisms is a $\Gamma$-equivariant transformation between these.
\end{enumerate}
\end{definition}

\begin{remark}
\label{rem:preserving}
\begin{enumerate}[(a)]
\item 
\label{rem:preserving:a}
The condition in (a) that the action $R$ preserves
the surjective submersion functor $\pi$ means that the diagram of functors
\begin{equation*}
\alxydim{@R=1.3cm}{\mathcal{P} \times \Gamma \ar[r]^{R} \ar[d]_{\mathrm{pr}_1} & \mathcal{P} \ar[d]^{\pi} \\ \mathcal{P} \ar[r]_-{\pi} &\idmorph M&}
\end{equation*} 
is commutative. 

\item
\label{rem:preserving:b}
The condition in (b) that the anafunctor $F$ respects the surjective submersion functors means in the first place
that there exists a transformation
\begin{equation*}
\alxydim{@R=1.3cm}{\mathcal{P}_1 \ar[rr]^{F} \ar[dr]_{\pi_1}="1" && \mathcal{P}_2 \ar@{=>}"1"\ar[dl]^{\pi_2} \\ &\idmorph M\text{.}&}
\end{equation*} 
However, since the target of the anafunctors $\pi_1$ and $\pi_2 \circ F$ is the \emph{discrete} groupoid $\idmorph{M}$, the equivalence of Example \ref{anafunctors:c} applies, and implies that if such a transformation exists, it is unique. Indeed, it is easy to see that an  anafunctor $F: \mathcal{P} \to \mathcal{Q}$ with anchors  $\alpha_l: F \to \mathcal{P}_0$ and $\alpha_r: F \to \mathcal{Q}_0$ 
respects smooth functors $\pi: \mathcal{P} \to \idmorph{M}$ and $\chi: \mathcal{Q} \to \idmorph{M}$ if and only if
$\pi \circ \alpha_l = \chi \circ \alpha_r$.
\begin{comment}
The composite $\chi \circ F$ is an anafunctor with total space a quotient $F'$ of $F$, and with anchors $\alpha_l: F' \to \mathcal{P}_0$ and $\chi \circ \alpha_r: F' \to M$. As discussed in Examples \ref{ex:idmorphbundle} and \ref{anafunctors:c}, the right anchor $\chi \circ \alpha_r$ descends along $\alpha_l$ to a smooth map $f: \mathcal{P}_0 \to M$ and the criterion for the claimed transformation is that $f = \pi$.   
\end{comment}
\end{enumerate}
\end{remark}




\begin{example}
\label{ex:trivzwoabun}
The \emph{trivial  $\Gamma$-2-bundle} over $M$ is defined by
\begin{equation*}
\mathcal{P} := \idmorph M \times \Gamma
\quomma
\pi:= \mathrm{pr}_1 
\quomma 
R := \id_M \times  m
\text{.}
\end{equation*}
Here, the smooth functor $\tau$  even has a smooth inverse \emph{functor}. In the following we denote the trivial $\Gamma$-2-bundle by $\mathcal{I}$.
\end{example}


\begin{comment}
\begin{remark}
Bartels has shown \cite{bartels} that principal 2-bundles with weaker versions of \emph{Lie 2-groups} actions can be \quot{semi-strictified}. 
\end{remark}
\end{comment}


\begin{remark}
\label{rem:ginot}
The principal $\Gamma$-2-bundles of Definition \ref{def:zwoabun} are very similar to those of Bartels \cite{bartels} and Wockel \cite{wockel1}, in the sense that their fibres are groupoids with a $\Gamma$-action. They only differ in the strictness assumptions for the action, and in the formulation of principality. Opposed to that, the \emph{principal 2-group bundles} introduced in \cite{ginot1} are quite different: their fibres are Lie 2-groupoids equipped with a certain Lie 2-groupoid morphism to $B\Gamma$. 
\end{remark}
