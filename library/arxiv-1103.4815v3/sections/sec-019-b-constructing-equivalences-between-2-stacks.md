---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-019-b-constructing-equivalences-between-2-stacks
section_title: "B Constructing Equivalences between 2-Stacks"
section_number: null
pages: 59-62
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.647
latex_coverage_ratio: 0.994
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{app:bicategories}


Let $\mathcal{C}$ be a bicategory  (we assume that associators and unifiers are  \emph{invertible} 2-morphisms). We fix the following terminology: a 1-\emph{iso}morphism $f: X_1 \to X_2$ in $\mathcal{C}$ always includes the data of an inverse 1-morphism $\bar f\maps X_2 \to X_1$ and of 2-isomorphisms $i: \bar f \circ f \Rightarrow \id$ and $j: \id \Rightarrow f \circ \bar f$ satisfying the zigzag identities. Let $\mathcal{D}$ be another bicategory. A 2-functor $F:\mathcal{C} \to \mathcal{D}$ is assumed to have \emph{invertible} compositors and unitors. 

The following lemma is  certainly \quot{well-known}, although we have not been able to find a reference for exactly this statement. 

\begin{lemma}
\label{lem:equivalence}
Let $F: \mathcal{C} \to \mathcal{D}$ be a 2-functor  that is fully faithful on Hom-categories. 
 Suppose one has chosen:
\begin{enumerate}

\item 
for every object $Y \in \mathcal{D}$ an object $G_Y \in \mathcal{C}$ and   a 1-isomorphism $\xi_Y: Y \to F(G_Y)$.

\item
for all objects $X_1,X_2\in \mathcal{C}$ and all 1-morphisms $g:F(X_1) \to F(X_2)$, a 1-morphism $G_g: X_1 \to X_2$ in $\mathcal{C}$ together with a 2-isomorphism $\eta_g: g \Rightarrow F(G_g)$. \footnote{More accurately we should write $G_{X_1,X_2,g}$ and $\eta_{X_1,X_2,g}$, but we will suppress $X_1$ and $X_2$ in the notation.} 
\end{enumerate}
Then, there is a  2-functor $G:\mathcal{D} \to \mathcal{C}$ and pseudonatural equivalences
\begin{equation*}
a: \id_{\mathcal{D}} \Rightarrow F \circ G
\quand
b:G \circ F \Rightarrow \id_{\mathcal{C}}\text{.}
\end{equation*}
In particular, $F$ is an equivalence of bicategories.
\end{lemma}


Proof. 
We recall  our convention concerning 1-isomorphisms: the 1-isomorphisms $\xi_Y$ include choices of inverse 1-morphisms $\bar\xi_Y$  together with 2-isomorphisms $i_Y: \bar \xi_Y \circ \xi_Y \Rightarrow \id$ and $j_Y: \id \Rightarrow \xi_Y \circ \bar \xi_Y$ satisfying the zigzag identities. 

First we explicitly construct the 2-functor $G$. 
On objects, we put $G(Y) := G_Y$.  We use the notation $\tilde g := (\xi_{Y_2} \circ g) \circ \bar\xi_{Y_1}$ for all 1-morphisms $g: Y_1 \to Y_2$ in $\mathcal{D}$, and define $G(g) = G_{\tilde g}$.   If $g,g': Y_1 \to Y_2$ are 1-morphisms, and $\psi:g \Rightarrow g'$ is a 2-morphism, we consider the 2-morphism $\tilde \psi$ defined by
\begin{equation*}
\alxydim{@C=1.5cm}{F(G_{\tilde g}) \ar@{=>}[r]^-{\eta_{\tilde g}^{-1}} & (\xi_{Y_2} \circ g) \circ \bar\xi_{Y_1} \ar@{=>}[r]^-{(\id \circ \psi) \circ \id} & (\xi_{Y_2} \circ g') \circ \bar\xi_{Y_1} \ar@{=>}[r]^-{\eta_{\tilde g'}} & F(G_{\tilde g'})\text{.} }
\end{equation*}
Since $F$ is fully faithful on 2-morphisms, we may choose the unique 2-morphism $G(\psi): G(g) \Rightarrow G(g')$ such that $F(G(\psi))=\tilde \psi$. In order to define the compositor of $G$ we look at 1-morphisms $g_{12}:Y_1 \to Y_2$ and $g_{23}: Y_2 \to Y_3$. We consider the 2-morphism
\begin{equation*}
\alxydim{@C=1.2cm@R=0.6cm}{F(G(g_{23}) \circ G(g_{12})) \ar@{=>}[r]^-{c^{-1}_{G(g_{12}),G(g_{23})}} & F(G_{\tilde g_{23}}) \circ F(G_{\tilde g_{12}}) \ar@{=>}[d]^{\eta_{\tilde g_{23}}^{-1} \circ \eta_{\tilde g_{12}}^{-1}} \\ & ((\xi_{Y_3} \circ g_{23}) \circ \bar\xi_{Y_2}) \circ ((\xi_{Y_2} \circ g_{12}) \circ \bar\xi_{Y_1}) \ar@{=>}[d]^{a,i_{Y_2}} \\ & (\xi_{Y_3} \circ (g_{23} \circ g_{12})) \circ \bar\xi_{Y_1} \ar@{=>}[r]_-{\eta_{\widetilde {g_{23} \circ g_{12}}}} &  F(G(g_{23} \circ g_{12}))\text{;}}
\end{equation*}
its unique preimage under the 2-functor $F$ is the compositor 
\begin{equation*}
c_{g_{12},g_{23}}:G(g_{23}) \circ G(g_{12}) \Rightarrow G(g_{23} \circ g_{12})\text{.}
\end{equation*}
In order to define the unitor of $G$ we consider an object $Y \in \mathcal{D}$ and look at the 2-morphism
\begin{equation*}
\alxydim{@C=1.6cm}{F(G(\id_Y))  \ar@{=>}[r]^-{\eta^{-1}_{\widetilde{\id_Y}}} & (\xi_{Y} \circ \id_Y) \circ \bar\xi_{Y} \ar@{=>}[r]^-{l_{\xi_{Y}},j_Y^{-1}} &   \id_{F(G(Y))} \ar@{=>}[r]^-{u_{G(Y)}^{-1}} &  F(\id_{G(Y)})\text{.}}
\end{equation*}
Its unique preimage under the 2-functor $F$ is the unitor
$u_Y: G(\id_Y) \Rightarrow \id_{G(Y)}$.
The second step is to verify the axioms of a 2-functor. This is simple but extremely tedious and can only be left as an exercise. 
\begin{comment}
There are four of them: (F1) to (F4) in the notation of Appendix A of \cite{schreiber2}. Axiom (F1) is the compatibility with the vertical composition. We check for 2-morphisms $\varphi: g \Rightarrow h$ and $\psi: h \Rightarrow k$ in the image of $F$:
\begin{eqnarray*}
F(G(\psi \bullet \psi)) &=& \eta_{\tilde k} \bullet  ((\id \circ (\psi \bullet \varphi)) \circ \id) \bullet \eta_{\tilde g}^{-1}\\ &=& \eta_{\tilde k} \bullet  ((\id \circ \psi ) \circ \id)  \bullet  ((\id \circ \varphi) \circ \id) \bullet \eta_{\tilde g}^{-1} \\&=& F(G(\psi)) \bullet F(G(\varphi)) \\&=& F(G(\psi) \bullet G(\varphi))\text{,}
\end{eqnarray*}
and further
\begin{equation*}
F(G(\id_g)) =\eta_{\tilde g} \bullet  ((\id \circ \id) \circ \id) \bullet \eta_{\tilde g}^{-1} = \id_{G(g)} \text{.}
\end{equation*}

Axiom (F2) describes the compatibility between the compositors and the horizontal composition. Its image under $F$ is the commutativity of the outer shape of the following diagram composed of commutative subdiagrams.
\begin{equation*}
\footnotesize
\alxydim{@C=0.7cm@R=1.4cm}{F(G(g) \circ G(f)) \ar@{=>}[dr]_-{c^{-1}_{G(f),G(g)}} \ar@{=>}[dddd]_{F(c_{f,g})}  \ar@{=>}[rrr]^-{F(G(\psi) \circ G(\varphi))}="1" &&& F(G(g') \circ G(f')) \ar@{=>}[dl]^{c^{-1}_{G(f'),G(g')}} \ar@{=>}[dddd]^{F(c_{f',g'})} \\ & F(G(g)) \circ F(G(f)) \ar@{}[dddl]|*+{\text{Def. of $c$}} \ar@{=>}[r]^-{F(G(\psi)) \circ F(G(\varphi))}="2" \ar@{}"1";"2"|*+{\text{(F2) for $F$}} \ar@{=>}[d]_{\eta^{-1}_{\tilde g} \circ \eta^{-1}_{\tilde f}} &  F(G(g')) \circ F(G(f')) \ar@{}[dddr]|*+{\text{Def. of $c$}} \ar@{}[dl]|*+{\text{Def. of $G$ on 2-morph.}}\ar@{=>}[d]^{\eta^{-1}_{\tilde g'} \circ \eta^{-1}_{\tilde f'}} & \\ & \hspace{-1cm}((\xi_{Y_3} \circ g) \circ \bar\xi_{Y_2}) \circ ((\xi_{Y_2} \circ f) \circ \bar\xi_{Y_1}) \ar@{=>}[r] \ar@{=>}[d]_{a,i_{Y_2}}  &((\xi_{Y_3} \circ g') \circ \bar\xi_{Y_2}) \circ ((\xi_{Y_2} \circ f') \circ \bar\xi_{Y_1}) \ar@{}[dl]|*+{\text{Naturality of $a$}} \hspace{-1cm}\ar@{=>}[d]^{a,i_{Y_2}} & \\ & ((\xi_{Y_3} \circ (g \circ f)) \circ \bar\xi_{Y_2}) \ar@{=>}[dl]_-{\eta_{\widetilde{g \circ f}}} \ar@{=>}[r]_-{(\id \circ (\psi \circ \varphi)) \circ \id}="3" &((\xi_{Y_3} \circ (g' \circ f')) \circ \bar\xi_{Y_2}) \ar@{=>}[dr]^{\eta_{\widetilde{g' \circ f'}}}& \\ F(G(g \circ f)) \ar@{=>}[rrr]_-{F(G(\psi \circ \varphi))}="4" \ar@{}"3";"4"|*+{\text{Def. of $G$ on 2-morphisms}} &&& F(G(g' \circ f'))}
\end{equation*}
Axiom (F3) describes the compatibility of the compositors with the associators of the bicategories $\mathcal{C}$ and $\mathcal{D}$, the diagram is moved to Figure \ref{figf}.

\begin{sidewaysfigure}
\tiny
\begin{equation*}
\alxydim{@C=-0.9cm@R=1.15cm}{F((G(h) \circ G(g)) \circ G(f)) \ar@{=>}[dr]_{c^{-1}} \ar@{=>}[dddd]_{F(c_{g,h} \circ \id)} \ar@{=>}[rrrrrr]^{F(a_{G(f),G(g),G(h)})}="3" &&&&&& F(G(h) \circ (G(g) \circ G(f))) \ar@{=>}[dl]^{c^{-1}} \ar@{=>}[dddd]^{F(\id \circ c_{f,g})} \\ & F(G(h) \circ G(g)) \circ F(G(f)) \ar@{}[ldddd]|{\text{(F2)}} \ar@{=>}[dddd]|<<<<<<<<<<<<<<<<<{F(c_{g,h}) \circ F(\id)}  \ar@{=>}[dr]^{c^{-1}} &&&& F(G(h)) \circ F(G(g) \circ G(f)) \ar@{}[rdddd]|{\text{(F2)}} \ar@{=>}[dddd]|<<<<<<<<<<<<<<<<<<{F(\id) \circ F(c_{f,g})}\ar@{=>}[dl]_{c-1} & \\ && (F(G(h)) \circ F(G(g))) \circ F(G(f)) \ar@{}[lddd]|{\text{Def. of c}}\ar@{=>}[rr]^{a_{F(G(f)),F(G(g)),F(G(h))}}="4" \ar@{}"3";"4"|*+{\text{(F3) for $F$}}\ar@{=>}[d]^{(\eta_{\tilde h}^{-1} \circ \eta_{\tilde g}^{-1}) \circ \id_{F(G(f))}}  && F(G(h)) \circ (F(G(g)) \circ F(G(f))) \ar@{}[rddd]|{\text{Def. of c}} \ar@{=>}[d]_{\id_{F(G(h))} \circ (\eta^{-1}_{\tilde g} \circ \eta^{-1}_{\tilde f})} && \\ && (((\xi \circ h) \circ \bar \xi) \circ ((\xi \circ g) \circ \bar \xi)) \circ F(G(f))\ar@{=>}[d]^{a,i_{Y_3}} &\hspace{4cm}& F(G(h)) \circ (((\xi \circ g) \circ \bar \xi) \circ ((\xi \circ f) \circ \bar \xi))\ar@{=>}[d]_{a,i_{Y_2}}  & \\ F(G(h\circ g) \circ G(f)) \ar@{}[drddd]|*+{\text{Def. of $c$}} \ar@{=>}[dr]^{c^{-1}} \ar@{=>}[dddd]_{F(c_{f,h \circ g})} && ((\xi \circ (h \circ g)) \circ \bar\xi) \circ F(G(f)) \ar@{=>}[dd]^{\id \circ \eta^{-1}_{\tilde f}}\ar@{=>}[dl]^{\eta_{\widetilde{h \circ g}} \circ \id} && F(G(h)) \circ((\xi \circ (g \circ f)) \circ \bar\xi)\ar@{=>}[dd]_{\eta^{-1}_{\tilde h} \circ \id}\ar@{=>}[dr]_<<<<<<<<{\id \circ \eta_{\widetilde{g \circ f}}}  && F(G(h) \circ G(g \circ f)) \ar@{}[dddld]|*+{\text{Def. of $c$}} \ar@{=>}[dddd]^{F(c_{g\circ f},h)} \\  & F(G(h \circ g)) \circ F(G(f))\ar@{=>}[dr]_<<<<<{\eta^{-1}_{\widetilde{h \circ g}} \circ \eta^{-1}_{\tilde f}} &&&& F(G(h)) \circ F(G(g \circ f)) \ar@{=>}[ru]^{c}\ar@{=>}[dl]^<<<<<{\eta^{-1}_{\tilde h} \circ \eta^{-1}_{\widetilde{g \circ f}}}  &  \\ && (( \xi \circ (h \circ g)) \circ \bar\xi ) \circ (( \xi \circ f) \circ \bar \xi )\ar@{=>}[d]^{a,i_{Y_2}} && (( \xi \circ h) \circ \bar\xi ) \circ (( \xi \circ (g \circ f)) \circ \bar \xi )\ar@{=>}[d]_{a,i_{Y_3}} & \\ && (\xi \circ ((h \circ g) \circ f)) \circ \bar\xi \ar@{=>}[rr]_{(\id \circ a_{f,g,h}) \circ \id}="1" \ar@{=>}[dll]_{\eta_{\widetilde{(h \circ g) \circ f}}} && (\xi \circ (h \circ (g \circ f))) \circ \bar\xi \ar@{=>}[drr]^{\eta_{\widetilde{h \circ (g \circ f)}}} & \\ F(G((h\circ g) \circ f)) \ar@{=>}[rrrrrr]_{F(G(a_{f,g,h}))}="2" \ar@{}"1";"2"|*+{\text{Def. of $G$ on 2-morphisms}} &&&&&& F(G(h \circ (g \circ f)))}
\end{equation*}
\caption{Proof of the axiom (F3). The commutativity of the big subdiagram in the middle follows from the exchange law, the naturality of the associator, and its associahedron. }
\label{figf}
\end{sidewaysfigure}

Axiom (F4) describes the compatibility of the compositors with the unitors and is proved in Figure \ref{figff}.
\begin{sidewayscommentfigure}
\begin{equation*}
\tiny
\alxydim{@C=0.7cm@R=1.5cm}{F(G(g) \circ G(\id_Y)) \ar@{}[drrrr]|{\text{Def. of $c$}} \ar@{=>}[rrrrr]^{F(c_{\id_Y,G(g)})} \ar@{=>}[dr]^{c^{-1}_{G(\id_Y),G(g)}} \ar@{=>}[ddddd]_{F(\id_{G(g)} \circ u_Y)} &&&&& F(G(g \circ \id_Y)) \ar@{=>}[ddddd]^{F(G(l_g))} \\ & F(G(g)) \ar@{}[ldddd]|{\text{(F2) for $F$}} \circ F(G(\id_Y)) \ar@{=>}[r]^{\eta^{-1}_{\tilde g} \circ \eta^{-1}_{\widetilde{\id_Y}}} \ar@{=>}[ddd]|{F(G(g)) \circ F(\id_{G(Y)})} & ((\xi \circ g) \circ \bar\xi) \circ ((\xi \circ \id_Y) \circ \bar\xi) \ar@{}[dr]|{=} \ar@{}[dldd]|{\text{Def. of $u$}} \ar@{=>}[rr]^{a,i_Y,l} \ar@{=>}[d]_{\id \circ (l_{\xi} \circ \bar\xi)} && ((\xi \circ (g \circ \id_Y)) \circ \bar\xi) \ar@{}[rdddd]|{\txt{Def. of $G$\\on 2-morph.}} \ar@{=>}[ur]^{\eta_{\widetilde{g \circ \id_Y}}} \ar@{=>}[dd]|{(\id \circ l_g) \circ \id}="1" \ar@{=>}[dl]_{a} \\ && ((\xi \circ g) \circ \bar\xi) \circ (\xi \circ \bar\xi) \ar@{}[drr]|{\text{Zigzag identity}} \ar@{=>}[r]^{a,i_Y} \ar@{=>}[d]_{\id\circ j^{-1}} & (\xi \circ g) \circ (\id \circ \bar\xi) \ar@{}"1"|{\text{(C2)}} \ar@{=>}[dr]_{\id\circ r_{\bar\xi}} \\ &&((\xi \circ g) \circ \bar\xi) \circ \id_{F(G(Y))} \ar@{=>}[dl]_{\eta_{\tilde g} \circ u_{G(Y)^{-1}}} \ar@{=>}[dr]^{\eta_{\tilde g} \circ \id} \ar@{=>}[rr]_{l} && (\xi \circ g) \circ \bar\xi \ar@{}[dl]|{\text{Nat. of $l$}} \ar@{=>}[ddr]_{\eta_{\tilde g}} \\ & F(G(g)) \circ F(\id_{G(Y)}) \ar@{=>}[dl]_{c_{\id_{G(Y)},G(g)}} \ar@{=>}[rr]_{\id_{F(G(g))} \circ u_{G(Y)}} && F(G(g)) \circ \id_{F(G(Y))} \ar@{}[dll]|{\text{(F4) for $F$}} \ar@{=>}[drr]_{l_{F(G(g))}} \\ F(G(g) \circ \id_{G(Y)}) \ar@{=>}[rrrrr]_{F(l_{G(g)})} &&&&& F(G(g))}
\end{equation*}
\caption{The diagram shows one part of the proof of the axiom (F4). The other part is the analogous diagram with the identity morphism on the left, and goes analogously. }
\label{figff}
\end{sidewayscommentfigure}
\end{comment}
The third step is to  construct the pseudonatural transformation \begin{equation*}
a: \id_{\mathcal{D}} \Rightarrow F \circ G\text{.}
\end{equation*}
Its component at an object $Y$ in $\mathcal{D}$ is the 1-morphism $a(Y) := \xi_Y: Y \to F(G(Y))$. Its component at a 1-morphism $g:Y_1 \to Y_2$ is the 2-morphism $a(g)$ defined by
\begin{equation*}
\alxydim{@R=0.6cm}{a(Y_2) \circ g \ar@{=}[r] & \xi_{Y_2} \circ g \ar@{=>}[d]^{\id \circ l^{-1}_{\xi_{Y_2} \circ g}} \\ & (\xi_{Y_2} \circ g) \circ \id  \ar@{=>}[d]^{a,i^{-1}_{Y_2}}  \\ & ((\xi_{Y_2} \circ g) \circ \bar\xi_{Y_1}) \circ \xi_{Y_1} \ar@{=>}[d]^{\eta_{\tilde g} \circ \id} \\ & F(G_{\tilde g}) \circ \xi_{Y_1} \ar@{=}[r] & F(G(g)) \circ a(Y_1)\text{.}}
\end{equation*}
There are two axioms a pseudonatural transformation has to satisfy, and their proofs are again left as an exercise.
\begin{comment}
Note that in the comments we work with the inverse transformation $a: F \circ G \Rightarrow \id_{\mathcal{D}}$.
 Axiom (T1) is proved in Figure \ref{fig:ateins}. 
\begin{sidewayscommentfigure}
\begin{equation*}
\tiny
\alxydim{@R=2.5cm@C=0.5cm}{(a(Y_3) \circ F(G(h))) \circ F(G(g)) \ar@{}[dd]^{\text{Def. of $a$}} \ar@{=>}[dd]_{a(h) \circ \id} \ar@{=>}[ddr]^{(\id \circ \eta^{-1}_{\tilde h}) \circ \id} \ar@{=>}[rrrr]^{a} &&&& a(Y_3) \circ (F(G(h)) \circ F(G(g))) \ar@{}[ddll]|{\text{Def. of $c$}}\ar@{=>}[dd]^{\id \circ c} \\    &    & \bar\xi_{Y_3} \circ (((\xi_{Y_3} \circ h) \circ \bar\xi_{Y_2}) \circ ((\xi_{Y_2} \circ g) \circ \bar\xi_{Y_1})) \ar@{=>}[urr]_-{\id \circ (\eta_{\tilde h} \circ \eta_{\tilde g})} \ar@{=>}[rd]^-{a,i_{Y_2}} \ar@{=>}[dd]_{i_{Y_3},a,r}   \\ (h \circ a(Y_2)) \circ F(G(g)) \ar@{=>}[d]_{a} \ar@{=>}[r]^-{a,i_{Y_{3}},r} &\xi_{Y_3} \circ (((\xi_{Y_3} \circ h) \circ \bar\xi_{Y_2}) \circ F(G(g)))\hspace{-2cm} \ar@{=>}[ru]^-{\id \circ \eta^{-1}_{\tilde g}} && \bar\xi_{Y_3} \circ ((\xi_{Y_3} \circ (h \circ g)) \circ \bar\xi_{Y_1}) \ar@{=>}[r]^-{\id \circ \eta^{-1}_{\widetilde{h \circ g}}} \ar@{=>}[rdd]_{a,i_{Y_3},r} & a(Y_3) \circ F(G(h \circ g)) \ar@{}[dd]_{\text{Def. of $a$}} \ar@{=>}[dd]^{a(h \circ g)} \\ h \circ (a(Y_2) \circ F(G(g))) \ar@{}[d]^{\text{Def. of $a$}} \ar@{=>}[d]_{\id \circ a(g)} \ar@{=>}[rr]^{\id \circ (\id \circ \eta^{-1}_{\tilde g})} && h \circ (\bar\xi_{Y_2} \circ ((\xi_{Y_2} \circ g)\circ \bar\xi_{Y_1})) \ar@{=>}[dll]^{r,a,i_{Y_2}} \ar@{=>}[drr]_{a,i_{Y_2},r} \\ A \ar@{=>}[rrrr]_{a^{-1}} &&&& (h \circ g) \circ a(Y_1) }
\end{equation*}
\caption{Proof of axiom (T1) for the pseudonatural transformation $a$. The unlabeled subdiagrams commute due to the exchange law. }
\label{fig:ateins}
\end{sidewayscommentfigure}
Axiom (T2) is the commutativity of the diagram
\begin{equation*}
\alxydim{}{a(Y_2) \circ F(G(g)) \ar@{}[drr]^>>>>>>>>>>>>>{\text{Def. of $a(g)$}} \ar@{}[ddd]^{\txt{\footnotesize Def. of $G$\\\footnotesize on 2-morph.}} \ar@{=>}[rrr]^{a(g)} \ar@{=>}[dr]^{\id \circ \eta^{-1}_{\tilde g}} \ar@{=>}[ddd]_{\id \circ F(G(\psi))} &&& g \circ a(Y_1) \ar@{}[ddd]_{\txt{\footnotesize Naturality\\\footnotesize of $r$}} \ar@{=>}[ddd]^{\psi \circ \id} \\ & \bar\xi_{Y_2} \circ (( \xi_{Y_2} \circ g) \circ \bar\xi_{Y_1}) \ar@{}[dr]|{\text{Exchange law}} \ar@{=>}[r]_-{i_{Y_2}} \ar@{=>}[d]_{\id \circ ((\id\circ \psi)\circ \id)} & \id \circ (g \circ \bar\xi_{Y_1}) \ar@{=>}[d]^{\id \circ (\psi \circ \id)} \ar@{=>}[ur]_{r_{g \circ \bar\xi_{Y_1}}} & \\ & \bar\xi_{Y_2} \circ ((\xi_{Y_2} \circ h) \circ \bar\xi_{Y_1}) \ar@{=>}[dl]_{\id \circ \eta_{\tilde h}} \ar@{=>}[r]_-{a,i_{Y_2}} & \id \circ (h \circ \bar\xi_{Y_1}) \ar@{=>}[dr]^{r_{h \circ \bar\xi_{Y_1}}} \\ a(Y_2) \circ F(G(h)) \ar@{}[urr]_>>>>>>>>>>>>>{\text{Def of $a(h)$}} \ar@{=>}[rrr]_{a(h)} &&& h \circ a(Y_2)}
\end{equation*}
for all 2-morphisms $\psi:g \Rightarrow h$. 
\end{comment}
It is easy to see that $a$ is a pseudonatural \emph{equivalence}, with an inverse transformation given by $\bar a(Y) := \bar\xi_Y$.
The fourth and last step is to construct the pseudonatural transformation 
\begin{equation*}
b: G \circ F \Rightarrow \id_{\mathcal{C}}\text{.}
\end{equation*}
Its component at an object $X$ is $b(X) := G_{\bar\xi_{F(X)}}: G(F(X)) \to X$. Its component at a 1-morphism $f\maps X_2 \to X_2$ is the  2-morphism 
\begin{equation*}
b(f): b(X_2) \circ G(F(f)) \Rightarrow f \circ b(X_1)
\end{equation*}
given as the unique preimage under $F$ of the 2-morphism
\begin{equation*}
\alxydim{@R=0.6cm}{F(b(X_2) \circ G(F(f))) \ar@{=>}[r]^-{c^{-1}} & F(b(X_2)) \circ F(G(F(f))) \ar@{=>}[d]_{\eta^{-1}_{\bar\xi_{F(X_2)}} \circ \eta^{-1}_{F(f)}} \\ & \bar\xi_{F(X_2)} \circ ((\xi_{F(X_2)} \circ F(f)) \circ \xi_{F(X_1)}) \ar@{=>}[d]_{a,i_{F(X_2)},r}  \\ & F(f) \circ \bar\xi_{F(X_1)} \ar@{=>}[d]_{\id_{F(f)} \circ \eta_{\bar\xi_{F(X_1)}}} \\ & F(f) \circ F(b(X_1)) \ar@{=>}[r]_-{c} & F(f \circ b(X_1))\text{.}}
\end{equation*}
The proofs of the axioms are again left for the reader, and again it is easy to see that $b$ is a pseudonatural \emph{equivalence} with an inverse transformation given by $\bar b(X) := G_{\xi_{F(X)}}$.
\begin{comment}
Axiom (T1) is shown in Figures \ref{figtoneba} and \ref{figtonebb}.
\begin{sidewayscommentfigure}
\tiny
\begin{equation*}
\alxydim{@C=-0cm@R=1.3cm}{F((b(X_3) \circ G(F(g)))\circ G(F(f))) \ar@{}[rrdr]|{\text{(F3)}} \ar@{=>}[dd]_{F(b(g) \circ \id)} \ar@{=>}[rd]^{c_F} \ar@{=>}[rrrr]^{F(a)} &&&& F(b(X_3) \circ (G(F(g)) \circ G(F(f))))\ar@{=>}[dd]^{F(\id \circ c_{G \circ F})} \\ & F(b(X_3) \circ G(F(g))) \circ F(G(f)) \ar@{}[dl]|{\text{(F2)}} \ar@{=>}[d]^{F(b(g)) \circ F(\id)} \ar@{=>}[rr]^-{c_F} &\hspace{1cm}& (F(b(X_3)) \circ F(G(F(g)))) \circ F(G(F(f))) \ar@{}[ddll]|{\txt{Def.\\of\\$b$}} \ar@{=>}[d]_{(\eta^{-1} \circ \eta^{-1}_{F(g)}) \circ \id} \ar@{=>}[ru]^{a,c_F} \\ F((g \circ b(X_2)) \circ G(F(f))) \ar@{}[dddr]_{\text{(F3)}}  \ar@{=>}[r]^-{c_F} \ar@{=>}[ddd]_{F(a)} & F(g \circ b(X_2)) \circ F(G(F(f)))\ar@{=>}[d]^{c_F} && (\bar\xi \circ ((\xi \circ F(g))\circ \bar\xi)) \circ F(G(F(f)))\ar@{=>}[d]_{a,i,r} & F(b(X_3) \circ G(F(g \circ f)))\ar@{=>}[ddddd]^{F(b(g \circ f))} \\ & (F(g) \circ F(b(X_2))) \circ F(G(F(f))) \ar@{}[drr]|{=}\ar@{=>}[d]^{a}\ar@{=>}[rr]^-{(\id \circ \eta^{-1} \circ \id)} && (F(g) \circ \bar\xi) \circ F(G(F(f)))\ar@{=>}[d]_{a,\eta_{F(f)}^{-1}} \\ & F(g) \circ (F(b(X_2)) \circ F(G(F(f)))\ar@{=>}[d]^{c_F}\ar@{=>}[rr]_-{\id \circ (\eta^{-1} \circ \eta_{F(f)}^{-1})} && F(g) \circ (\bar\xi \circ ((\xi \circ F(f)) \circ \bar\xi)) \ar@{}[ddll]|{\txt{Def. of $b$}} \ar@{=>}[d]_{a,i,r}  \\ F(g \circ (b(X_2) \circ G(F(f))))  \ar@{=>}[r]^{i} \ar@{=>}[dd]_{F(\id \circ b(f))} & F(g) \circ F(b(X_2) \circ G(F(f))) \ar@{}[dld]|{\text{(F2)}} \ar@{=>}[d]^{F(\id) \circ F(b(f))} && F(g) \circ (F(f) \circ \bar\xi)\ar@{=>}[d]_{\id \circ (\id \circ \eta)} \\ & F(g) \circ F(f \circ b(X_1)) \ar@{}[drr]_{\text{(F3)}}  \ar@{=>}[rr]^{c_F} && F(g) \circ (F(f) \circ F(b(X_1)))\ar@{=>}[rd]^{a,c_F} \\ F(g \circ (f \circ b(X_1)))\ar@{=>}[ru]^{c_F} \ar@{=>}[rrrr]_{F(a)} &&&& F((g \circ f) \circ b(X_1)) }
\end{equation*}
\caption{The first part of the proof of axiom (T1) for the pseudonatural transformation $b$. The commutativity of the subdiagram on the right is addressed in Figure \ref{figtonebb}.}
\label{figtoneba}
\end{sidewayscommentfigure}
\begin{sidewayscommentfigure}
\begin{equation*}
\tiny
\alxydim{@C=0.4cm@R=1.7cm}{(F(b(X_3)) \circ F(G(F(g)))) \circ F(G(F(f)))\ar@{=>}[r]^-{a}\ar@{=>}[d]_{(\eta^{-1} \circ \eta^{-1}_{F(g)}) \circ \id} & F(b(X_3)) \circ (F(G(F(g))) \circ F(G(F(f))))\ar@{=>}[d]_{\eta \circ (\eta^{-1}_{F(g)} \circ \eta^{-1}_{F(f)})}\ar@{=>}[r]^-{c_F} & F(b(X_3)) \circ F(G(F(g)) \circ G(F(f))) \ar@{}[ddr]|>>>>>>>>>>>>>>>{\txt{(F2)}} \ar@{}[dl]|{\text{Def. of $c_G$}}\ar@{=>}[d]^{\id \circ F(c_G)}\ar@{=>}[r]^-{c_F} &  F(b(X_3) \circ (G(F(g)) \circ G(F(f))))\ar@{=>}[dd]^{F(\id \circ c_{G \circ F})} \\ (\bar\xi \circ ((\xi \circ F(g))\circ \bar\xi)) \circ F(G(F(f)))\ar@{=>}[r]_-{\id \circ \eta^{-1}_{F(f)}}\ar@{=>}[d]_{a,i,r} & \bar\xi \circ (((\xi \circ F(g)) \circ \bar \xi) \circ ((\xi \circ F(f)) \circ \bar\xi))\ar@{=>}[dd]_{i,a,r} & F(b(X_3)) \circ F(G(F(g) \circ F(G(f)))) \ar@{=>}[ddl]_{\eta \circ \eta^{-1}_{F(g) \circ F(f)}}\ar@{=>}[d]^{\id \circ F(G(c_F))} \\ (F(g) \circ \bar\xi) \circ F(G(F(f)))  \ar@{=>}[d]_{a,\eta_{F(f)}^{-1}} && F(b(X_3)) \circ F(G(F(g \circ f))) \ar@{}[dddr]|{\text{Def. of $b$}} \ar@{}[dl]|{\txt{Def. of $G$\\on 2-morphisms}}\ar@{=>}[d]^{\eta^{-1} \circ \eta^{-1}_{F(g \circ f)}}\ar@{=>}[r]^{c_F} & F(b(X_3) \circ G(F(g \circ f)))\ar@{=>}[ddd]^{F(b(g \circ f))} \\ F(g) \circ (\bar\xi \circ ((\xi \circ F(f)) \circ \bar\xi))\ar@{=>}[r]^{i,i^{-1},r}\ar@{=>}[d]_{a,i,r} & \bar\xi \circ ((\xi \circ (F(g) \circ F(f)))\circ \bar\xi)\ar@{=>}[dd]_{i,\eta}\ar@{=>}[r]^{c_F} & \bar\xi \circ ((\xi \circ F(g \circ f)) \circ \bar\xi) \ar@{=>}[d]_{a,i,r} \\ F(g) \circ (F(f) \circ \bar\xi) \ar@{=>}[d]_{\id \circ (\id \circ \eta)} && F(g \circ f) \circ \bar\xi\ar@{=>}[d]_{\id \circ \eta}  \\ F(g) \circ (F(f) \circ F(b(X_1)))\ar@{=>}[r]_{a} &(F(g) \circ F(f)) \circ F(b(X_1))\ar@{=>}[r]_{c_F}&F(g \circ f) \circ F(b(X_1))\ar@{=>}[r]_-{c_F}&F((g \circ f) \circ b(X_1))}
\end{equation*}
\caption{The second part of the proof of axiom (T1) for the pseudonatural transformation $b$. The unlabelled subdiagrams commute due to the exchange law.}
\label{figtonebb}
\end{sidewayscommentfigure}
Axiom (T2) is the commutativity of the following diagram:
\begin{equation*}
\tiny
\alxydim{@C=-0.8cm}{F(b(X_2) \circ G(F(f))) \ar@{=>}[ddddd]_{F(\id \circ G(F(\varphi)))} \ar@{=>}[rd]^{c^{-1}} \ar@{=>}[rrrrrr]^{b(f)} &&&\hspace{3cm}&&& F(f \circ b(X_1)) \ar@{=>}[dl]_{c^{-1}} \ar@{=>}[ddddd]^{F(\varphi \circ \id)} \\ & F(b(X_2)) \circ F(G(F(f))) \ar@{}[rrrr]|{\text{Def. of $b$}} \ar@{}[rddd]|{\text{Def. of $G$}} \ar@{}[ddl]|{\text{(F2)}}  \ar@{=>}[ddd]|{\id \circ F(G(F(\varphi)))} \ar@{=>}[dr]^{\eta^{-1} \circ \eta^{-1}} &&&& F(f) \circ F(b(X_1)) \ar@{}[ddr]|{\text{(F2)}} \ar@{=>}[dl]_{\id \circ \eta^{-1}} \ar@{=>}[ddd]|{F(\varphi) \circ \id} &\\&& \bar\xi_{F(X_2)} \circ (( \xi_{F(X_2)} \circ F(f)) \circ \bar\xi_{F(X_1)}) \ar@{=>}[d]^{\id \circ ((\id \circ F(\varphi)) \circ \id)} \ar@{=>}[rr]^-{a,i,r}&& F(f) \circ \bar\xi_{F(X_1)} \ar@{=>}[d]_{F(\varphi) \circ \id}&& \\&& \bar\xi_{F(X_2)} \circ (( \xi_{F(X_2)} \circ F(g)) \circ \bar\xi_{F(X_1)}) \ar@{=>}[rr]_-{a,i,r} \ar@{=>}[dl]^{\eta \circ \eta}&& F(g) \circ \bar\xi_{F(X_1)} \ar@{=>}[dr]_{\eta}&&\\ &F(b(X_2)) \circ F(G(F(g))) \ar@{}[rrrr]|{\text{Def. of $b$}} \ar@{=>}[dl]^{c}&&&&F(g) \circ F(b(X_1)) \ar@{=>}[dr]_{c}& \\ F(b(X_2) \circ G(F(g))) \ar@{=>}[rrrrrr]_{b(g)} &&&&&& F(g \circ b(X_1))}
\end{equation*}
in which the diagram in the middle commutes due to the naturality of $a$ and $r$.
\end{comment}
\strut\hfill$\square$

As a consequence of Lemma \ref{lem:equivalence} we obtain the certainly well-known result:

\begin{corollary}
Let $F: \mathcal{C} \to \mathcal{D}$ be essentially surjective, and an equivalence on all Hom-categories. Then, $F$ is an equivalence of bicategories.  
\end{corollary}

Since we work with 2-stacks over manifolds, we need the following \quot{stacky} extension of Lemma \ref{lem:equivalence}.
For a pre-2-stack $\mathcal{C}$, we denote by $\mathcal{C}_M$ the 2-category it associates to a smooth manifold $M$, and by $\psi^{*}: \mathcal{C}_N \to \mathcal{C}_M$ the 2-functor it associates to a smooth map $\psi: M \to N$. The pseudonatural equivalences $\psi^{*} \circ \varphi^{*} \cong (\varphi\circ \psi)^{*}$ will be suppressed from the notation in the following.
If $\mathcal{C}$ and $\mathcal{D}$ are pre-2-stacks, a \emph{ 1-morphism} $F: \mathcal{C} \to \mathcal{D}$ associates 2-functors $F_M: \mathcal{C}_M \to \mathcal{D}_M$ to a smooth manifold $M$,  pseudonatural equivalences
\begin{comment}
\footnote{Since these are 1-isomorphisms in a bicategory of 2-functors, our convention from the beginning of this section applies. Thus, they are supposed to come with chosen inverse 1-morphisms and invertible modifications satisfying the zigzag identities. }
\end{comment}
\begin{equation*}
F_{\psi}: \psi^{*} \circ F_N \to F_M \circ \psi^{*}
\end{equation*}
to smooth maps $\psi:M \to N$,
\begin{comment}
As such, it assign to objects $X \in \mathcal{C}_N$ 1-isomorphisms
\begin{equation*}
F_{\psi}(X): \psi^{*}F_N(X) \to F_M(\psi^{*}X)
\end{equation*}
and to 1-morphisms $f:X_1 \to X_2$ in $\mathcal{C}_N$ 2-isomorphisms
\begin{equation*}
F_{\psi}(f): F_{\psi}(X_2) \circ \psi^{*}F_N(f) \Rightarrow F_M(\psi^{*}f) \circ F_{\psi}(X_1)\text{.}
\end{equation*}
\end{comment}
and certain modifications $F_{\psi,\varphi}$ that control the relation between $F_{\psi}$ and $F_{\varphi}$ for composable maps $\psi$ and $\varphi$. 
\begin{comment}
These are modifications
\begin{equation*}
F_{\psi,\varphi}: (F_{\psi} \circ \id_{\varphi^{*}}) \circledcirc (\id_{\psi^{*}}  \circ F_{\varphi}) \Rightarrow F_{\varphi \circ \psi}
\end{equation*}
associated to pairs of composable smooth maps $\psi:M \to N$ and $\varphi: N \to O$. Here we have denoted by $\circ$ and $\circledcirc$ horizontal and vertical composition of pseudonatural equivalences, respectively.
So, the modification $F_{\psi,\varphi}$ has for every object $X \in \mathcal{C}_O$ a 2-isomorphism
\begin{equation*}
F_{\psi,\varphi}(X) : F_{\psi}(\varphi^{*}X) \circ \psi^{*}F_{\varphi}(X) \Rightarrow F_{\varphi \circ \psi}(X)\text{.}
\end{equation*}
For a further smooth map $\chi: O \to P$, these modifications
have to fit into the commutative diagram
\begin{equation}
\label{eq:compthree}
\footnotesize
\alxydim{@C=2cm}{(F_{\psi} \circ \id_{\varphi^{*}\chi^{*}} ) \circledcirc (\id_{\psi^{*}} \circ F_{\varphi} \circ \id_{\chi^{*}}) \circledcirc (\id_{\psi^{*}\varphi^{*}} \circ F_{\chi}) \ar@{=>}[d]_{(F_{\psi,\varphi} \circ \id)\circledcirc \id} \ar@{=>}[r]^-{\id\circledcirc (\id \circ F_{\varphi,\chi})} & (F_{\psi} \circ \id_{\varphi^{*}\chi^{*}})\circledcirc (\id_{\psi^{*}} \circ  F_{\chi \circ \varphi}) \ar@{=>}[d]^{F_{\psi,\chi \circ \varphi}} \\ (F_{\varphi \circ \psi} \circ \id_{\chi^{*}}) \circledcirc (\id_{\psi^{*}\varphi^{*}} \circ F_{\chi}) \ar@{=>}[r]_-{F_{\varphi \circ \psi,\chi}}  & F_{\chi\circ \varphi \circ \psi} }
\end{equation}
Evaluated on an object $X\in \mathcal{C}_O$, this is the diagram
\begin{equation*}
\alxydim{@C=2.5cm}{F_{\psi}(\varphi^{*}\chi^{*}X) \circledcirc \psi^{*}F_{\varphi}(\chi^{*}X) \circledcirc \psi^{*}\varphi^{*}F_{\chi}(X) \ar@{=>}[r]^-{\id\circledcirc \psi^{*}F_{\varphi,\chi}(X)} \ar@{=>}[d]_{F_{\psi,\varphi}(\chi^{*}X)\circledcirc \id} & F_{\psi}(\varphi^{*}\chi^{*}X) \circledcirc \psi^{*}F_{\chi \circ \varphi}(X) \ar@{=>}[d]^{F_{\psi,\chi \circ \varphi}(X)} \\ F_{\varphi\circ \psi}(\chi^{*}X) \circledcirc \psi^{*}\varphi^{*}F_{\chi}(X) \ar@{=>}[r]_-{F_{\varphi\circ \psi,\chi}(X)} & F_{\chi\circ \varphi \circ \psi}(X)}
\end{equation*}
\end{comment}

  
\begin{lemma}
\label{lem:stackequivalence}
Suppose $\mathcal{C}$ and $\mathcal{D}$ are pre-2-stacks over smooth manifolds, and $F: \mathcal{C} \to \mathcal{D}$ is a  1-morphism. Suppose
that for every smooth manifold $M$
\begin{enumerate}
\item 
the assumptions of Lemma \ref{lem:equivalence} for the 2-functor $F_{M}$ are satisfied and 

\item
the  data $(G_Y,\xi_Y)$ and $(G_g,\eta_g)$ is chosen for all objects $Y$ and 1-morphisms $g$  in $\mathcal{D}_M$. 
\end{enumerate}
Then, there is a  1-morphism 
$G:\mathcal{D} \to \mathcal{C}$
of pre-2-stacks together with 2-isomorphisms
\begin{equation*}
a:F \circ G \Rightarrow \id_{\mathcal{D}}
\quand
b:G \circ F \Rightarrow \id_{\mathcal{C}}
\end{equation*}
such that
for every smooth manifold $M$ the 2-functor $G_M$ and the pseudonatural transformations $a_M$ and $b_M$ are the ones of Lemma  \ref{lem:equivalence}. In particular, $F$ is an equivalence of  pre-2-stacks. 
\end{lemma}


For the proof one constructs the required pseudonatural equivalences $G_{\psi}$ and the modifications $G_{\psi,\varphi}$ from the given ones, $F_{\psi}$ and $F_{\psi,\varphi}$, respectively, in a similar way as explained in the proof of Lemma \ref{lem:equivalence}. Since these constructions are straightforward to do but would consume many pages,  and the statement of the lemma is not too surprising and certainly  well-known to many people, we   leave these constructions for the interested reader. 


\begin{comment}
\begin{proof}
It is in fact easier to provide the inverse of the structure listed for the 1-morphism $F$ above, but we don't mention that. 
First we have to provide a pseudonatural equivalence
\begin{equation*}
G_{\psi}: G_M \circ \psi^{*} \to \psi^{*} \circ G_N
\end{equation*}
associated to a smooth map $\psi:M \to N$. 
For simplicity, we shall suppress occurrences of associators, unifiers, compositors and unitors in the following.
For an object $Y \in \mathcal{D}_N$, we denote by $h_{\psi,Y}$ the 1-morphism
\begin{equation*}
\alxydim{@C=1.8cm}{F_M (G_{\psi^{*}Y}) \ar[r]^{\bar \xi_{\psi^{*}Y}} & \psi^{*}Y \ar[r]^-{\psi^{*}\xi_{Y}} &  \psi^{*}F_N(G_{Y}) \ar[r]^-{F_{\psi}(G_{Y})} & F_M(\psi^{*}G_{Y})\text{,} }
\end{equation*}
and define $G_{\psi}(Y) := G_{h_{\psi,Y}}$. For a 1-morphism $g:Y_1 \to Y_2$ in $\mathcal{D}_N$ we look at the 2-morphism
\begin{equation*}
\small
\alxydim{@C=0cm@R=0.7cm}{F_{M}(G_{\psi}(Y_2) \circ G_M(\psi^{*}g)) \ar@{=>}[r]^-{c^{-1}} & F_{M}(G_{h_{\psi,Y_2}}) \circ F_{M}(G_{\widetilde{\psi^{*}g}}) \ar@{=>}[d]^{\eta_{h_{\psi,Y_2}}^{-1} \circ \eta^{-1}_{\widetilde{\psi^{*}g}}} \\ & F_{\psi}(G_{Y_2}) \circ \psi^{*}\xi_{Y_1} \circ \bar\xi_{\psi^{*}Y_2} \circ \xi_{\psi^{*}Y_2} \circ \psi^{*}g \circ \bar\xi_{\psi^{*}Y_1} \ar@{=>}[d]^{\id \circ \id \circ i_{\psi^{*}Y_2} \circ \id \circ \psi^{*}i_{Y_1}^{-1} \circ \id}   \\ & F_{\psi}(G_{Y_2}) \circ \psi^{*}\xi_{Y_1} \circ \psi^{*}g \circ \psi^{*}\bar\xi_{Y_1} \circ \psi^{*}\xi_{Y_1} \circ \bar\xi_{\psi^{*}Y_1} \ar@{=>}[d]^{\id \circ \eta_{\tilde g} \circ \id \circ \id}  \\& F_{\psi}(G_{Y_2}) \circ \psi^{*}F_N(G_N(g))\circ \psi^{*}\xi_{Y_1} \circ \bar\xi_{\psi^{*}Y_1}  \ar@{=>}[d]^{F_{\psi}(G_N(g)) \circ \id \circ \id} \\ & F_M(\psi^{*}G_N(g)) \circ F_{\psi}(G_{Y_1}) \circ \psi^{*}\xi_{Y_1} \circ \bar\xi_{\psi^{*}Y_1}  \ar@{=>}[d]^{\id \circ \eta_{h_{\psi,Y_1}}} \\ &  F_M(\psi^{*}G_N(g)) \circ F_M(G_{h_{\psi,Y_1}}) \ar@{=>}[r]_-{c} & F_M(\psi^{*}G_N(g) \circ G_{\psi}(Y_1)) }
\end{equation*} 
Its unique preimage under $F$ is the component $G_{\psi}(g)$ of $G_{\psi}$ at $g$. One can check that the axioms for a pseudonatural transformation are satisfied. Now it remains to define the modification
\begin{equation*}
G_{\psi,\varphi}: (\id_{\psi^{*}} \circ G_{\varphi}) \circledcirc (G_{\psi} \circ \id_{\varphi^{*}}) \Rightarrow G_{\varphi \circ \psi} \text{.}
\end{equation*} 
For  $Y \in \mathcal{D}_O$ we look at the 2-morphism
\begin{equation*}
\small
\alxydim{@C=-1.3cm@R=0.7cm}{F_{M}(\psi^{*}G_{\varphi}(Y) \circ G_{\psi}(\varphi^{*}Y)) \ar@{=>}[r]^-{c} & F_{M}(\psi^{*}G_{\varphi}(Y)) \circ F_M(G_{h_{\psi,\varphi^{*}Y}}) \ar@{=>}[d]^{\id \circ \eta^{-1}_{h_{\psi,\varphi^{*}Y}}} \\ &  F_{M}(\psi^{*}G_{\varphi}(Y)) \circ F_{\psi}(G_{\varphi^{*}Y}) \circ \psi^{*}\xi_{\varphi^{*}Y} \circ \bar \xi_{\psi^{*}\varphi^{*}Y} \ar@{=>}[d]^{F_{\psi}(G_{\varphi}(Y))^{-1} \circ \id \circ \id} \\ & F_{\psi}(\varphi^{*}G_Y) \circ \psi^{*}F_N(G_{h_{\varphi,Y}})\circ \psi^{*}\xi_{\varphi^{*}Y} \circ \bar \xi_{\psi^{*}\varphi^{*}Y}  \ar@{=>}[d]^{\id \circ \psi^{*}\eta^{-1}_{h_{\varphi,Y}} \circ \id \circ \id } \\ &   F_{\psi}(\varphi^{*}G_{Y}) \circ \psi^{*}F_{\varphi}(G_Y) \circ  \psi^{*}\varphi^{*}\xi_{Y}\circ \psi^{*}\bar \xi_{\varphi^{*}Y}\circ \psi^{*}\xi_{\varphi^{*}Y}\circ \bar\xi_{\psi^{*}\varphi^{*}Y}  \ar@{=>}[d]^{F_{\psi,\varphi}(G_Y) \circ \id \circ \psi^{*}i_{\varphi^{*}Y} \circ \id} \\ &  F_{\varphi \circ \psi}(G_{Y}) \circ  \psi^{*}\varphi^{*}\xi_{Y}\circ \bar\xi_{\psi^{*}\varphi^{*}Y}  \ar@{=>}[d]^{\eta_{h_{\varphi \circ \psi,Y}}} \\ & F_M(G_{h_{\varphi\circ \psi,Y}}) \ar@{=}[r]_{} & F_M(G_{\varphi \circ \psi} (Y))\text{.}}
\end{equation*}
Its unique preimage under $F_M$ is the component $G_{\psi,\varphi}(Y)$. One can show that the axiom for a modification is satisfied. The compatibility condition \erf{eq:compthree} for the modification $G_{\psi,\varphi}$ follows from the one for the modification $F_{\psi,\varphi}$. 


Next we prove that the pseudonatural transformation $a_M:\id_{\mathcal{D}_M} \Rightarrow F_M \circ G_M $ is natural in $M$. 
Generally, if $a_M: F_M \to G'_M$ is a pseudonatural transformation, one needs a modification
\begin{equation*}
a_{\psi}: (a_M \circ \id_{\psi^{*}}) \circledcirc F_{\psi} \Rightarrow F'_{\psi} \circledcirc (\id_{\psi^{*}} \circ a_N)
\end{equation*}
that satisfies
\begin{equation*}
\def\corr{3.8cm}
\alxydim{@C=-7cm@R1.8cm}{&& (a_M \circ \id_{\psi^{*}} \circ \id_{\varphi^{*}}) \circledcirc (F_{\psi} \circ \id_{\varphi^{*}}) \circledcirc (\id_{\psi^{*}} \circ F_{\varphi}) \ar@{=>}[drr]^{\id \circ F_{\psi,\varphi}} \ar@{=>}[dll]_{a_{\psi} \circ \id} \\ (F'_{\psi} \circ \id_{\varphi^{*}}) \circledcirc (\id_{\psi^{*}} \circ a_N \circ \id_{\varphi^{*}}) \circledcirc (\id_{\psi^{*}} \circ F_{\varphi})\hspace{1cm} \ar@{=>}[dr]_{\id \circ a_{\varphi}} &&\hspace{15cm}&& \hspace{\corr}(a_M \circ \id_{\psi^{*}} \circ \id_{\varphi^{*}}) \circledcirc F_{\varphi\circ\psi}\hspace{\corr} \ar@{=>}[dl]^{a_{\varphi\circ\psi}}  & \\ & (F'_{\psi} \circ \id_{\varphi^{*}}) \circledcirc (\id_{\psi^{*}} \circ F'_{\varphi}) \circledcirc (\id_{\psi^{*}} \circ \id_{\varphi^{*}}  \circ a_O) \ar@{=>}[rr]_-{F'_{\psi,\varphi} \circ \id} && F'_{\varphi \circ \psi}\circ (\id_{\psi^{*}} \circ \id_{\varphi^{*}} \circ a_O)\text{.} }
\end{equation*}
For this purpose, we have to provide a modification
\begin{equation*}
a_{\psi}: (\id_{F_M} \circ G_{\psi}) \circledcirc (a_M \circ \id_{\psi^{*}}) \Rightarrow   (F_{\psi} \circ \id_{G_N}) \circledcirc (\id_{\psi^{*}} \circ a_N)
\end{equation*}
that is compatible with the composition of smooth maps in the sense that the diagram
\begin{equation*}
\footnotesize
\alxydim{@C=0.8cm@R=1cm}{(\id_{F_M} \circ \id_{\psi^{*}} \circ G_{\varphi}) \circledcirc (\id_{F_M} \circ G_{\psi} \circ \id_{\varphi^{*}}) \circledcirc (a_M \circ \id_{\psi^{*}} \circ \id_{\varphi^{*}}) \ar@{=>}[dr]^{\qquad(\id \circ G_{\psi,\varphi}) \circledcirc \id} \ar@{=>}[dd]_{\id \circledcirc (a_{\psi} \circ \id)} &  \\ & (\id_{F_M} \circ G_{\varphi \circ \psi}) \circledcirc (a_M \circ \id_{(\varphi \circ \psi)^{*}} ) \ar@{=>}[dddd]^{a_{\varphi \circ \psi}}  \\(\id_{F_M} \circ \id_{\psi^{*}} \circ G_{\varphi}) \circledcirc (F_{\psi} \circ \id_{G_N} \circ \id_{\varphi^{*}}) \circledcirc (\id_{\psi^{*}} \circ a_N \circ \id_{\varphi^{*}}) \ar@{=}[d]\\ (F_{\psi} \circ \id_{\varphi^{*}} \circ \id_{G_O})  \circledcirc(\id_{\psi^{*}} \circ \id_{F_M} \circ G_{\varphi}) \circledcirc (\id_{\psi^{*}} \circ a_N \circ \id_{\varphi^{*}}) \ar@{=>}[d]_-{\id \circledcirc(\id \circ a_{\varphi}) } &\\  (F_{\psi} \circ \id_{\varphi^{*}} \circ \id_{G_O})\circledcirc  (\id_{\psi^{*}} \circ F_{\varphi} \circ\id_{G_O}) \circledcirc (\id_{\psi^{*}} \circ \id_{\varphi^{*}} \circ a_O) \ar@{=>}[dr]_{(F_{\psi,\varphi} \circ \id) \circledcirc \id\qquad} & \\ &  (F_{\varphi \circ \psi}  \circ \id_{G_O}) \circledcirc (\id_{(\varphi \circ \psi)^{*}} \circ a_O)}
\end{equation*}
is commutative.
The component $a_{\psi}(Y)$ of the modification $a_{\psi}$ at an object $Y$ in $\mathcal{D}_N$ is the 2-isomorphism
\begin{equation*}
\alxydim{@C=0.6cm}{F_M(G_{\psi}(Y)) \circ a_M(\psi^{*}Y) \ar@{=}[r] &F_M(G_{h_{\psi,Y}}) \circ \xi_{\psi^{*}Y} \ar@{=>}[d]^-{\eta^{-1}_{h_{\psi,Y}} \circ \id} \\ & F_{\psi}(G_{Y}) \circ \psi^{*}\xi_{Y}  \circ \bar \xi_{\psi^{*}Y} \circ \xi_{\psi^{*}Y} \ar@{=>}[d]^-{\id \circ \id \circ i_{\psi^{*}Y}} & \\ & F_{\psi}(G_Y) \circ \psi^{*}\xi_Y \ar@{=}[r] & F_{\psi}(G_N(Y)) \circ \psi^{*}a_N(Y)\text{.}}
\end{equation*}
It is straightforward to check the axiom for a modification, and also toi verify the commutativity of the above diagram. The proof that the pseudonatural transformation $b$ is natural in $M$ works similarly and is left out for brevity.
Finally, we show that the pseudonatural transformation $b_M:G_M \circ F_M \Rightarrow \id_{\mathcal{C}_M}$ is natural in $M$. For this purpose, we have to provide a modification
\begin{equation*}
b_{\psi}:(b_M \circ \id_{\psi^{*}}) \circledcirc (\id_{G_M} \circ F_{\psi}) \Rightarrow (\id_{\psi^{*}} \circ b_N) \circledcirc (G_{\psi} \circ \id_{F_N})
\end{equation*}
that is compatible with the composition of smooth maps in the sense that the diagram 
\begin{equation*}
\footnotesize
\alxydim{@C=0.8cm@R=1cm}{(b_M \circ \id_{\psi^{*}} \circ \id_{\varphi^{*}}) \circledcirc (\id_{G_M} \circ F_{\psi} \circ \id_{\varphi^{*}}) \circledcirc (\id_{G_M}\circ \id_{\psi^{*}} \circ F_{\varphi}) \ar@{=>}[dr]^{\qquad\id \circledcirc ( \id \circ F_{\psi,\varphi})} \ar@{=>}[dd]_{(b_{\psi} \circ \id) \circledcirc \id} &  \\ & (b_M \circ \id_{(\varphi \circ \psi)^{*}} ) \circledcirc  (\id_{G_{M}} \circ F_{\varphi \circ \psi}) \ar@{=>}[dddd]^{b_{\varphi \circ \psi}}  \\(\id_{\psi^{*}} \circ b_N\circ \id_{\varphi^{*}}) \circledcirc (G_{\psi} \circ \id_{F_N}\circ \id_{\varphi^{*}})  \circledcirc (\id_{G_M}\circ \id_{\psi^{*}} \circ F_{\varphi}) \ar@{=}[d]\\ (\id_{\psi^{*}} \circ b_N\circ \id_{\varphi^{*}}) \circledcirc(\id_{G_M}\circ \id_{\psi^{*}} \circ F_{\varphi})\circledcirc (G_{\psi} \circ \id_{\varphi^{*}} \circ \id_{F_O}) \ar@{=>}[d]_-{(\id \circ b_{\varphi}) \circledcirc \id } &\\  (\id_{\psi^{*}} \circ \id_{\varphi^{*}} \circ b_O) \circledcirc(\id_{\psi^{*}} \circ G_{\varphi} \circ \id_{F_O}) \circledcirc (G_{\psi} \circ \id_{\varphi^{*}} \circ \id_{F_O}) \ar@{=>}[dr]_{\id \circledcirc (G_{\psi,\varphi} \circ \id) \qquad} & \\ &  (\id_{(\varphi \circ \psi)^{*}} \circ b_O) \circledcirc (G_{\varphi \circ \psi} \circ \id_{F_O})}
\end{equation*}
is commutative. The component $b_{\psi}(X)$ of the modification $b_{\psi}$ at an object $X \in \mathcal{C}_N$ is the unique preimage under $F_M$ of the 2-isomorphism
\begin{equation*}
\footnotesize
\alxydim{@C=-0.7cm}{F_M(b_M(\psi^{*}X) \circ G_M(F_{\psi}(X))) \ar@{=>}[r]^-{c^{-1}}&  F_M(G_{\bar\xi_{F_M(\psi^{*}X)}})  \circ  F_M(G_{\widetilde{F_{\psi}(X)}}) \ar@{=>}[d]^{\eta^{-1}_{\bar\xi_{F_N(\psi^{*}X)}} \circ \eta^{-1}_{\widetilde{F_{\psi}(X)}}} \\  &  \bar\xi_{F_M(\psi^{*}X)} \circ \xi_{F_M(\psi^{*}X)} \circ F_{\psi}(X) \circ \bar\xi_{\psi^{*}F_N(X)}  \ar@{=>}[d]^{i_{F_M(\psi^{*}X)} \circ \id \circ \psi^{*}i^{-1}_{F_N(X)} \circ \id}  \\ & F_{\psi}(X) \circ\psi^{*}\bar\xi_{F_N(X) } \circ \psi^{*}\xi_{F_N(X)}\circ \bar\xi_{\psi^{*}F_N(X)}  \ar@{=>}[d]^{\id \circ \psi^{*}\eta_{\bar\xi_{F_N(X)}}} \\ &   F_{\psi}(X) \circ \psi^{*}F_N(G_{\bar\xi_{F_N(X)}})\circ \psi^{*}\xi_{F_N(X)} \circ \bar\xi_{\psi^{*}F_N(X)} \ar@{=>}[d]^{F_{\psi}(G_{\bar\xi_{F_N(X)}})} \\ & F_M(\psi^{*}G_{\bar\xi_{F_N(X)}}) \circ F_{\psi}(G_{F_N(X)}) \circ \psi^{*}\xi_{F_N(X)} \circ \bar\xi_{\psi^{*}F_N(X)}    \ar@{=>}[d]^{\id\ \circ \eta_{h_{\psi,F_N(X)}}} \\  & F_M(\psi^{*}G_{\bar\xi_{F_N(X)}}) \circ F_M(G_{h_{\psi,F_N(X)}})  \ar@{=>}[r]_-{c} &  F_M(\psi^{*}b_N(X) \circ G_{\psi}(F_N(X)))\text{.}} 
\end{equation*}
\end{proof}
\end{comment}


\end{appendix}



\kobib{.}
