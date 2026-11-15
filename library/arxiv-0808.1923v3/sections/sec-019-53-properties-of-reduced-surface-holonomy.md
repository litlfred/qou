---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-019-53-properties-of-reduced-surface-holonomy
section_title: "Properties of Reduced Surface Holonomy"
section_number: 5.3
pages: 52-56
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.969
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
The reduced surface holonomy has nice properties that we will reveal in the following.
First we treat  the dependence of the reduced surface holonomy on the marking. 

We arrange the  set of markings of $S$ into equivalence classes, as it is common in the theory of Riemann surfaces. 
Two markings $(x,\EuScript{M})$ and $(x',\EuScript{M}')$, with $\EuScript{M}=\left \lbrace \alpha_i,\beta_i \right \rbrace$ and $\EuScript{M}' = \left \lbrace \alpha_i',\beta_i' \right \rbrace$, are called \emph{equivalent}, if there exists a path $\gamma: x \to x'$ and bigons $\Delta_i: \alpha_i \Rightarrow   \gamma \circ \alpha_i' \circ \gamma^{-1}$ and $\Delta_i': \beta_i \Rightarrow   \gamma \circ \beta_i' \circ \gamma^{-1}$. 

\begin{lemma}
\label{lemmarkingindep}
Let $(x,\EuScript M)$ and $(x',\EuScript M')$ be equivalent good markings. Then, 
\begin{equation*}
\mathrm{RHol}_{\mathrm{tra}}(\phi,x,\EuScript M) = \mathrm{RHol}_{\mathrm{tra}}(\phi,x',\EuScript M')\text{.}
\end{equation*}
\end{lemma}

\begin{proof}
Each equivalence between markings splits into a sequence of steps, in which a step is either conjugation of all paths in the marking by a path $\gamma:x \to y$, or changing one of the paths via a bigon. Thus it suffices to prove the invariance of the reduced surface holonomy under each of these steps. Let $\mathrm{tra}\red:\mathcal{P}_2(M) \to \mathcal{B}\mathfrak{G}$ be a reduction of $\mathrm{tra}$, and let $\mathrm{t} := \Red \circ \mathrm{tra}\red$.  


In the first part of the proof we look at a conjugation. Let $\Sigma: \tau_{\EuScript M} \Rightarrow \id_x$ be a fundamental bigon for a marking $(x,\EuScript M)$. Denote by $(x',\EuScript M_{\gamma})$ the marking obtained by conjugating all paths with $\gamma$. We have $\tau_{\EuScript M_{\gamma}} = \gamma \circ \tau_{\EuScript M} \circ \gamma^{-1}$, and  $\Sigma^{\gamma} :=  \id_{\gamma} \circ \Sigma \circ \id_{\gamma^{-1}}$ is a fundamental bigon for $(x',\EuScript M_{\gamma})$. We have the two paths $\mathrm{t}_{\phi,\EuScript M}$ and $\mathrm{t}_{\phi,\EuScript M_{\gamma}}$ and the compositors $c^{\phi,\mathrm{t}}: \mathrm{t}_{\phi,\EuScript M} \Rightarrow \mathrm{t}(\tau_{\EuScript M})$ and $c_{\gamma}^{\phi,\mathrm{t}}: \mathrm{t}_{\phi,\EuScript M_{\gamma}} \Rightarrow \mathrm{t}(\tau_{\EuScript M_{\gamma}})$, so that 
\begin{equation*}
\mathrm{Hol}_{\mathrm{t}}(\phi,x,\EuScript M) = \mathrm{t}(\Sigma) \cdot c^{\phi,t}
\quand
\mathrm{Hol}_{\mathrm{t}}(\phi,x',\EuScript M') = \mathrm{t}(\Sigma^{\gamma}) \cdot c_{\gamma}^{\phi,t}\text{.}
\end{equation*}
Here, and in the following we will suppress writing $\phi_{*}$ when we apply $\mathrm{t}$ to paths or bigons in $S$.

There is a unique compositor 2-morphism $c: \mathrm{t}_{\phi,\EuScript M_{\gamma}} \Rightarrow \mathrm{t}(\gamma) \circ \mathrm{t}_{\phi,\EuScript M} \circ \mathrm{t(\gamma)}^{-1}$, and another unique compositor 2-morphism $c': \mathrm{t}(\tau_{\EuScript M_{\gamma}}) \Rightarrow t(\gamma) \circ \mathrm{t}(\tau_{\EuScript M}) \circ t(\gamma)^{-1}$.  
We claim that the diagram
\begin{equation*}
\alxydim{@C=1.8cm}{\mathrm{t}_{\phi,\EuScript M_{\gamma}} \ar@{=>}[d]_{c} \ar@{=>}[r]^{c^{\phi,\mathrm{t}}_{\gamma}} & \mathrm{t}(\tau_{\EuScript M_{\gamma}}) \ar@{=>}[d]^{c'} \ar@{=>}[r]^-{\mathrm{t}(\Sigma^{\gamma})} & \id_{t(\phi(x))} \ar@{=>}[d]^{\id} \\ t(\gamma) \circ \mathrm{t}_{\phi,\EuScript M} \circ t(\gamma)^{-1} \ar@{=>}[r]_-{\id \circ c^{\phi,\mathrm{t}} \circ \id}  & t(\gamma) \circ \mathrm{t}(\tau_{\EuScript M}) \circ t(\gamma)^{-1} \ar@{=>}[r]_{\id \circ \mathrm{t}(\Sigma) \circ \id} &  t(\gamma) \circ \id \circ t(\gamma)^{-1} }
\end{equation*} 
is commutative. The subdiagram on the left commutes because of the coherence of compositors enforced by axiom (F3). In order to see that the subdiagram on the right commutes we note that $c' \eq c_{\tau_{\EuScript M_{\gamma}} \circ \gamma^{-1}, \gamma} \cdot c_{\gamma^{-1},\tau_{\EuScript M_{\gamma}}}$. Axiom (F2) applied to the 2-morphisms $\id$, $\Sigma^{\gamma}$ and $\id$ gives the commutativity with $c_{\gamma^{-1},\gamma} \cdot c_{\gamma^{-1},\id}$ on the right hand side of the diagram. But the latter expression is equal to $1$ for the normalized 2-functor $\mathrm{t}$. 



 Next we compute $c$. We note the compositor between $\mathrm{t}(\gamma \circ \alpha \circ \gamma^{-1})$ and $\mathrm{t}(\gamma) \circ \mathrm{t}(\alpha) \circ \mathrm{t}(\gamma^{-1})$ is $c_{\alpha \circ \gamma^{-1},\gamma}\cdot c_{\gamma^{-1},\alpha}$,  while the one between  $\mathrm{t}(\gamma \circ \alpha^{-1} \circ \gamma^{-1})$ and $\mathrm{t}(\gamma) \circ \mathrm{t}(\alpha^{-1}) \circ \mathrm{t}(\gamma^{-1})$ is
$c_{\alpha^{-1} \circ \gamma^{-1},\gamma}\cdot c_{\gamma^{-1},\alpha^{-1}}$. These two compositors are actually inverse to each other; this follows from axiom (F3) for compositors and the fact that $\mathrm{t}$ is normalized. Also note that $\mathrm{t}(\gamma) \circ \mathrm{t}(\gamma^{-1})=\id$; again since $\mathrm{t}$ is normalized. Thus, we see that $c=1$. 
All together, we see that $\mathrm{Hol}_{\mathrm{t}}(\phi,x,\EuScript M)=\mathrm{Hol}_{\mathrm{t}}(\phi,x',\EuScript M')$. 



In the second part of the proof we look at a change of one of the paths via a bigon. If $\EuScript M = \left \lbrace \alpha_i,\beta_i \right \rbrace_{i=1}^{g}$ is a marking, we look at another marking $\EuScript M'$ consisting of the same paths except for an index $i_0$ where a different path $\alpha_{i_0}'$ is present, related to $\alpha_{i_0}$ by a bigon $\Delta: \alpha'_{i_0} \Rightarrow \alpha_{i_0}$. Let  $\Delta^{\#}: \alpha_{i_0}'^{-1} \Rightarrow \alpha_{i_0}^{-1}$ be the \quot{horizontally inverted} bigon given by $\Delta^{\#}(s,t) := \Delta(s,1-t)$. 
We consider the 2-morphism
\begin{equation*}
\tilde \Delta := \id \circ (\Delta \circ \id_{\beta_{i_0}} \circ \Delta^{\#} \circ \id_{\beta_{i_0}^{-1}}) \circ \id : \tau_{\EuScript M'} \Rightarrow \tau_{\EuScript M}\text{,}
\end{equation*}
with the outer identities meant for all factors with indices not equal to $i_0$. We also consider the 2-morphism
\begin{equation*}
\mathrm{t}_{\Delta} := \id \circ (\mathrm{t}(\Delta) \circ \id \circ \mathrm{t}(\Delta^{\#}) \circ \id) \circ \id: \mathrm{t}_{\phi,\EuScript M'}\Rightarrow \mathrm{t}_{\phi,\EuScript M}\text{.}
\end{equation*}
If $\Sigma: \tau_{\EuScript M} \Rightarrow \id_x$ is a fundamental bigon for $\EuScript M$, then $\Sigma' := \Sigma \bullet \tilde\Delta$ is a fundamental bigon for $\EuScript M'$. We claim that the diagram
\begin{equation*}
\alxydim{@R=0.6cm@C=1.5cm}{\mathrm{t}_{\phi,\EuScript M'} \ar@{=>}[r]^-{c^{\prime\;\phi,\mathrm{t}}} \ar@{=>}[dd]_{t_{\Delta}} & \mathrm{t}(\tau_{\EuScript M'}) \ar@{=>}[dr]^{\mathrm{t}(\Sigma')} \ar@{=>}[dd]^{\mathrm{t}(\tilde\Delta)} \\ && \id\\ \mathrm{t}_{\phi,\EuScript M} \ar@{=>}[r]_-{c^{\phi,\mathrm{t}}} & \mathrm{t}(\tau_{\EuScript M}) \ar@{=>}[ur]_{\Sigma} }
\end{equation*}
is commutative. Indeed, the rectangular part commutes due to axiom (F2) for the 2-functor $\mathrm{t}$, and the triangular part commutes by definition of $\Sigma'$. It remains to notice that $t_{\Delta} = 1 \in \mathfrak{G}\red$, since the contributions of $\Delta$ and $\Delta^{\#}$ cancel. Then, the diagram implies the coincidence of the surface holonomies.
\end{proof}



We  summarize our results about the surface holonomy of non-abelian gerbes in the following theorem, which constitutes the main result of this section.

\begin{theorem}
\label{th:rhol}
Let $\mathfrak{G}$ be a Lie 2-group,  $T$ be a 2-category, and $i: \mathcal{B}\mathfrak{G} \to T$ be an equivalence of 2-categories. Let $\mathrm{tra}: \mathcal{P}_2(M) \to T$ be a transport 2-functor with $\mathcal{B}\mathfrak{G}$-structure. Let $S$ be a closed oriented surface with a good marking $(x,\EuScript M)$, and let $\phi:S \to M$ be a smooth map. Then, the reduced surface holonomy 
\begin{equation*}
\mathrm{RHol}_{\mathrm{tra}}(\phi,x,\EuScript M) \in \mathfrak{G}\red
\end{equation*}
depends only on the equivalence class of the marking, and only on the isomorphism class of $\mathrm{tra}$.
\end{theorem}


\begin{proof}
After Lemma \ref{lemmarkingindep} it only remains to prove that the reduced surface holonomy only depends on the isomorphism class of $\mathrm{tra}$. Indeed, if $\mathrm{tra}\cong\mathrm{tra}'$ is an isomorphism we can choose the \emph{same} reduction for both.  
\end{proof}


In Section \ref{sec4} we have collected  various equivalences between transport 2-functors and  concrete models of gerbes with connections. These equivalences were mostly established by  zigzags of canonically defined 2-functors. On the level of isomorphism classes, such zigzags give a well-defined bijection. Since the reduced surface holonomy is invariant under isomorphisms, these bijections convey the concept of reduced surface holonomy to a well-defined, isomorphism-invariant concept for each of these concrete models:
\begin{enumerate}[(i)]

\item
The bijection
\begin{equation*}
\hat H^2(M,\mathfrak{G})  \cong \hc 0 \transport{}{2}{\mathrm{Gr}}{T}
\end{equation*}
of Theorem \ref{th:class} between the non-abelian differential cohomology and transport 2-functors equips non-abelian cohomology with a well-defined, isomorphism-invariant  concept of surface holonomy. In particular, it equips degree two Deligne cocycles and (fake-flat) Breen-Messing  cocycles with a well-defined, isomorphism-invariant  concept of surface holonomy. We show below in Proposition \ref{propabsf} in the case of Deligne cocycles it reproduces  the existing concept of surface holonomy. In the case  of Breen-Messing cocycles such a concept was previously unknown; its is one of the main results of this article.   

\item 
The equivalence of Theorem \ref{th:bgrb} induces a canonical bijection
\begin{equation*}
\hc 0 \mathfrak{BGrb}^{\nabla}(M) 
\cong 
\hc 0 \mathrm{Trans}_{\mathcal{BB}S^1}(M,\mathcal{B}(S^1\text{-}\mathrm{Tor}))
\end{equation*}
of  between isomorphism classes of bundle gerbes with connections and isomorphism classes of transport 2-functors, and so equips bundle gerbes with connection with a well-defined, isomorphism-invariant  concept of surface holonomy. We show below in Proposition \ref{propabsf} that it reproduces  the existing concept of surface holonomy for abelian gerbes.

\item
The injective map 
\begin{equation*}
\hc 0 (H\text{-}\mathfrak{BGrb}^{\nabla_{\!f\!f}}(M)) \to \hc 0 (\transport{}{2}{\mathcal{B}\mathrm{AUT}(H)}{\mathcal{B}(\hbitor)})
\end{equation*}
of Theorem \ref{th:nagrb}
between isomorphism classes of fake-flat non-abelian $H$-bundle gerbes with connection and transport 2-functors, equips fake-flat non-abelian $H$-bundle gerbes with connection with a well-defined, isomorphism-invariant  concept of surface holonomy. Such a concept was previously unknown; it is one of the main results of this article.


\end{enumerate}


Now we prove that the reduced surface holonomy of Theorem \ref{th:rhol} reduces in the case $\mathfrak{G} =\mathcal{B}S^1$ to the established notion of surface holonomy for connections on $\mathcal{B}S^1$-gerbes. Let us first recall that established notion. 

It can be given for an element  $\xi\in \hat H^2(M,\mathcal{B}S^1)$ of the (abelian) differential cohomology group which classifies  $\mathcal{B}S^1$-gerbes. It is solely based on the fact that  differential cohomology   sits in an exact sequence
\begin{equation*}
\alxydim{}{1 \ar[r]& \Omega^2_{\mathrm{cl},\Z}(M) \ar[r]& \Omega^2(M) \ar[r]^-{\mathcal{I}}& \hat H^2(M,\mathcal{B}S^1) \ar[r]& H^3(M,\Z) \ar[r]& 0}\text{,}
\end{equation*}
in which $\Omega^2_{\mathrm{cl},\Z}(M)$ denotes the closed 2-forms with integral periods \cite{brylinski1}. If $\phi:S \to M$ is a smooth map from a closed oriented surface $S$ to $M$, then $\phi^{*}\xi \in \hat H^2(S,\mathcal{B}S^1)$ projects to zero in  $0\in H^3(S,\Z)$ for dimensional reasons, and so is the image of a 2-form $B \in \Omega^2(S)$ under the  map $\mathcal{I}$ in the sequence. The abelian surface holonomy of $\xi$ around $\phi$ is then defined as
\begin{equation*}
\mathrm{AbHol}_{\xi}(\phi) := \exp \left (- \int_S B \right ) \in S^1\text{.}
\end{equation*}
Since the difference between two choices of 2-forms is a closed 2-form with integral periods, this integral is independent of the choice of $B$. 

 
\begin{proposition}
\label{propabsf}
Let $\mathrm{tra}: \mathcal{P}_2(M) \to T$ be a transport 2-functor with $\mathcal{BB}S^1$-structure. Let $\xi \in \hat H^2(M,\mathcal{B}S^1)$ be the associated class under the bijection of Theorem \ref{th:class}. Then,
\begin{equation*}
\mathrm{RHol}_{\mathrm{tra}}(\phi,x,\EuScript{M}) = \mathrm{AbHol}_{\xi}(\phi)\text{,}
\end{equation*}
i.e. the reduces surface holonomy of $\mathrm{tra}$ coincides with the established notion of surface holonomy for abelian gerbes. In particular, it is independent of the marking. 
\end{proposition}
 

 

\begin{proof}
For any smooth manifold $X$, we have an equality between $\Omega^2(X)$ and the objects of the 2-category $\diffco{\mathcal{B}S^1}{2}{X}$. The latter is isomorphic to the 2-category $\mathrm{Funct}^{\infty}(\mathcal{P}_2(X),\mathcal{B}S^1)$ of smooth 2-functors via Theorem \ref{th1}, and we have computed in Lemma \ref{sfdfbsone}  that
\begin{equation}
\label{sfholco1}
F(\Sigma) = \exp \left (- \int_{\Sigma} B \right ) 
\end{equation}
for any bigon $\Sigma \in BX$. 
By construction we have a commutative diagram
\begin{equation*}
\alxydim{}{\Omega^2(X) \ar[r]^-{\mathcal{I}} \ar[d] & \hat H^2(X,\mathcal{B}S^1) \ar[d]  \\  \mathrm{Funct}^{\infty}(\mathcal{P}_2(X),\mathcal{B}S^1) \ar[r] & \hc 0 \mathrm{Trans}^2_{\mathcal{BB}S^1}(X,\mathcal{BB}S^1)\text{,}}
\end{equation*}
in which the map on the bottom is the inclusion of smooth 2-functors in transport 2-functors. 


Note that $\mathfrak{G}\red=S^1$ with Example \ref{ex4} (a) and $\Red = \id_{\mathcal{BB}S^1}$. Let $\mathrm{tra}\red$ be a reduction of the given transport 2-functor, corresponding to the class $\xi$ under the vertical map on the right hand side of the diagram. After pullback along $\phi:S \to M$ we obtain the 2-form $B \in \Omega^2(S)$ such that $\mathcal{I}(B) = \xi$. Let $F: \mathcal{P}_2(S) \to \mathcal{B}S^1$ be the smooth 2-functor that corresponds to  $B$. By commutativity of the diagram, we find an isomorphism 
\begin{equation}
\label{sfholco2}
F \cong \phi^{*}\mathrm{tra}\red
\end{equation}
between transport 2-functors. 

If now $\Sigma$ is a fundamental bigon for the marking $(x,\EuScript M)$, then we have
on one side
\begin{equation*}
\mathrm{AbHol}_{\xi} (\phi) := \exp \left(- \int_S B  \right ) \stackrel{\text{Lemma \ref{fundamentalbigonintegral}}}{=} \exp \left(- \int_\Sigma B  \right ) \stackerf{sfholco1}{=} F(\Sigma) = \mathrm{Hol}_F(\id,x,\EuScript M)\text{,}
\end{equation*}
where the last equality is Definition \ref{def:surfaceholonomy} combined with the fact that $F$ is a strict 2-functor (with trivial compositors). Lemma \ref{independenceofreduction} applied to the equivalence \erf{sfholco2} shows that \begin{equation*}
\mathrm{Hol}_F(\id,x,\EuScript M) = \mathrm{Hol}_{\phi^{*}\mathrm{tra}\red}(\id,x,\EuScript M)\text{.}
\end{equation*}
We have on the other side
\begin{equation*}
\mathrm{Hol}_{\phi^{*}\mathrm{tra}\red}(\id,x,\EuScript M)=\mathrm{Hol}_{\mathrm{tra}\red}(\phi,x,\EuScript M)=\mathrm{RHol}_{\mathrm{tra}}(\phi,x,\EuScript M)\text{,}
\end{equation*}
this shows the claimed coincidence.
\end{proof} 


Finally, let us comment on the dependence of the reduced surface holonomy on the equivalence class of a marking.  Let $S$ be a closed oriented surface, and let $(x,\EuScript M)$ and $(x',\EuScript M')$ two markings. A standard result from the theory of Riemann surfaces is:
\begin{enumerate}[(i)]

\item 
There exists an orientation-preserving diffeomorphism $f:S \to S$ such that $(x',\EuScript M') = f(x,\EuScript M)$, 


\item
The diffeomorphism $f$ is homotopic to the identity map $\id_S$ if and only if $(x,\EuScript M)$ and $(x',\EuScript M')$ are equivalent.

\begin{comment}
By assumption there exists a smooth homotopy $h: [0,1] \times S \to S$ between $\id_S$ and  $f$. Define the paths $\gamma_s(t) := h(st,x)$, so that $\gamma := \gamma_1: x \to f(x)$. Define further the paths $\alpha_i^s(t) := h(s,\alpha_i(t))$. Then define
\begin{equation*}
\Delta_i(s,t) := (\gamma_s^{-1} \circ \alpha_i^s \circ \gamma_s)(t)\text{,}
\end{equation*}
which is a bigon from $\alpha_i$ to $\gamma^{-1} \circ \alpha'_i \circ \gamma$. Similarly, we get bigons $\Delta_i'$ from $\beta_i$ to $\gamma^{-1} \circ \beta_i' \circ \gamma$.   
\end{comment} 

\end{enumerate}
The quotient of the group of orientation-preserving diffeomorphisms modulo those homotopic to the identity is the mapping class group of $S$, denoted $\mathcal{M}(S)$. Thus, $\mathcal{M}(S)$ acts on the reduced surface holonomies of a surface $\phi:S\to M$. Currently we do not know what this action is; in particular, we do not know if it is trivial or not. 

        



\kobib{../../bibliothek/tex}
