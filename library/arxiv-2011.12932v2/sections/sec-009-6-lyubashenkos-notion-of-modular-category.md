---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-009-6-lyubashenkos-notion-of-modular-category
section_title: "Lyubashenko's notion of modular category"
section_number: 6
pages: 12-16
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.948
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
\label{S:L-mod_cat}

An \textit{L-modular category} (L for Lyubashenko) can be defined as a finite ribbon category whose Müger center is trivial. Remark that this is not the original definition of Lyubashenko, but it is equivalent to it. This is a consequence of a result of Shimizu \cite{S16}, who compared several notions of non-degeneracy for the braiding of a finite ribbon category, proving the equivalence of four different conditions. Among these, we can find Lyubashenko's original one, as well as the short property used above. This formulation makes it clear that T-modular categories are just semisimple L-modular categories.

In order to review Lyubashenko's definition, let $\calC$ be a finite ribbon category, and let us consider the functor $\calH : \calC^\op \times \calC \to \calC$ determined by $(X,Y) \mapsto X^* \otimes Y$. We recall the classical notion of a \textit{dinatural transformation of source $\calH$}, which is given by an object $Z \in \calC$ equipped with a family $\{ d_X : X^* \otimes X \to Z \}_{X \in \calC}$ of morphisms of $\calC$ satisfying
\[
 d_X \circ (f^* \otimes \id_X) = d_Y \circ (\id_{Y*} \otimes f)
\]
for every morphism $f : X \to Y$ of $\calC$, see \cite[Sec.~IX.4]{M71}. We usually abuse notation, and simply denote dinatural transformations by their underlying objects. The \textit{coend of $\calH$} is the universal dinatural transformation of source $\calH$, which means it is an object $\calL \in \calC$ with a dinatural family of structure morphisms $i_X : X^* \otimes X \to \calL$ satisfying the following condition: for every dinatural transformation $Z$ of source $\calH$ there exists a unique morphism $\ell_Z : \calL \to Z$ such that the diagram
\begin{equation}\label{E:univ_prop_coend}
 \begin{tikzpicture}[descr/.style={fill=white},baseline=(current  bounding  box.center)]
  \node (P0) at (135:{sqrt(2)*2.5}) {$Y^* \otimes X$};
  \node (P1) at (90:2.5) {$X^* \otimes X$};
  \node (P2) at (180:2.5) {$Y^* \otimes Y$};
  \node (P3) at (0:0) {$\calL$};
  \node (P4) at (-45:{2.5/sqrt(2)}) {$Z$};
  \draw
  (P0) edge[->] node[above] {\scriptsize $f^* \otimes \id_X$} (P1)
  (P1) edge[->] node[right] {\scriptsize $i_X$} (P3)
  (P0) edge[->] node[left] {\scriptsize $\id_{Y^*} \otimes f$} (P2)
  (P2) edge[->] node[below] {\scriptsize $i_Y$} (P3)
  (P1) edge[bend left,->] node[right] {\scriptsize $d_X$} (P4)
  (P2) edge[bend right,->] node[below] {\scriptsize $d_Y$} (P4)
  (P3) edge[->] node[descr] {\scriptsize $\ell_Z$} (P4);
 \end{tikzpicture}
\end{equation}
commutes for every morphism $f : X \to Y$ of $\calC$. It has been proved by Majid \cite{M91a} and Lyubashenko \cite{L95,L99} that, since $\calC$ is a finite ribbon category, the coend of $\calH$ always exists, and furthermore it supports the structure of a braided Hopf algebra in $\calC$. This means that it admits:
\begin{enumerate}
 \item a product $\mu : \calL \otimes \calL \to \calL$ and a unit $\eta : \one \to \calL$;
 \item a coproduct $\Delta : \calL \to \calL \otimes \calL$ and a counit $\epsilon : \calL \to \one$;
 \item an antipode $S : \calL \to \calL$.
\end{enumerate}
All these structure morphisms are uniquely determined by the universal property~\eqref{E:univ_prop_coend} of $\calL$. Indeed, they can be defined as the unique morphisms of $\calC$ that satisfy
\begin{gather*}
 \pic{Hopf_algebra_structure_1} \\[5pt]
 \pic{Hopf_algebra_structure_2} \\[5pt]
 \pic{Hopf_algebra_structure_3}
\end{gather*}
for all $X,Y \in \calC$. Remark that the product $\mu$ is actually determined by a universal property satisfied by the so-called \textit{double coend} $\calL \otimes \calL$, and it requires a Fubini theorem for coends \cite[Prop.~IX.8]{M71} whose name comes from the standard notation
\[
 \calL = \int^{X \in \calC} X^* \otimes X,
\]
see also \cite[Prop.~5.1.2]{KL01}. We should point out that, dually, every finite ribbon category $\calC$ also admits an \textit{end}
\[
 \calE = \int_{X \in \calC} X \otimes X^*,
\]
which is similarly defined as a universal dinatural transformation, see Appendix \ref{A:end} for details. Equivalent constructions can be carried out exploiting the properties of $\calE$, which are completely analogous to those of $\calL$, and it is for historical reasons that we focus on $\calL$ instead of $\calE$, following Lyubashenko.

From a topological point of view, what we said so far hints at the fact that the universal property \eqref{E:univ_prop_coend} of the coend $\calL$ provides an alternative to the Reshetikhin--Turaev functor for extracting morphisms of $\calC$ from diagrams of certain framed oriented tangles. For instance, a Hopf pairing $\omega : \calL \otimes \calL \to \one$ is uniquely determined by the equality
\[
 \pic{Hopf_pairing}
\]
for all $X,Y \in \calC$. Then, following Lyubashenko's original definition, an L-modular category is a finite ribbon category for which the Hopf pairing $\omega$ is non-degenerate, meaning that it induces an isomorphism between $\calL$ and $\calL^*$. Remark how similar the defining diagram for $\omega$ is with respect to the one defining the S-matrix of Turaev. In fact, when $\calC$ is semisimple, then Prop.~\ref{P:end_fusion} and \cite[Lem.~2]{K96a} give
\[
 \calE \cong \bigoplus_{i \in I} V_i \otimes V_i^*, \qquad 
 \calL \cong \bigoplus_{i \in I} V_i^* \otimes V_i,
\]
and $\omega$ is non-degenerate if and only if the S-matrix is invertible \cite[Prop.~7.4.3]{KL01}. 


An alternative condition for the modularity of $\calC$ is that a certain morphism $D : \calL \to \calE$ called the \textit{Drinfeld map} is an isomorphism, see \cite[Prop.~4.11]{FGR17}. When $\calC$ is the category $\mods{H}$ of finite-dimensional representations of a finite-dimensional ribbon Hopf algebra $H$, then let us denote with $\ad$ the \textit{adjoint representation} of $H$, which is given by the vector space $H$ equipped with the adjoint left $H$-action defined by
\[
 \ad_x(y) = x_{(1)}yS(x_{(2)})
\]
for all $x,y \in H$, where we are using Sweedler's notation $\Delta(x) = x_{(1)} \otimes x_{(2)}$ for the coproduct. Similarly, let us denote with $\coad$ the \textit{coadjoint representation} of $H$, which is given by the vector space $H^*$ equipped with the coadjoint left $H$-action defined by
\[
 \coad_x(\phi)(y) = \phi(S(x_{(1)})yx_{(2)})
\]
for all $x,y \in H$ and $\phi \in H^*$. Then Prop.~\ref{P:end_H-mod} and \cite[Lem.~3]{K96a} give
\[
 \calE \cong \ad, \qquad \calL \cong \coad.
\]
In this setting, the Drinfeld map $D : \coad \to \ad$ was first defined in \cite[Prop.~3.3]{D90} as the $H$-module morphism determined by $D(\phi) := (\phi \otimes \id_H)(R_{21}R_{12})$, where $R_{12} = R \in H \otimes H$ is the R-matrix of $H$, and $R_{21} \in H \otimes H$ is obtained from $R$ by reversing the order of its components. The element $M = R_{21}R_{12} \in H \otimes H$ is sometimes called the \textit{M-matrix}, or \textit{monodromy matrix}, of $H$. By definition, $H$ is \textit{factorizable} if $D$ is an isomorphism.

When $\calC$ is modular, an \textit{integral} of the coend $\calL$ is a morphism\footnote{The source of $\Lambda$ might be a different invertible object in general, called the \textit{object of integrals}, but here we are supposing $\calC$ is modular.} $\Lambda : \one \to \calL$ satisfying
\[
 \mu \circ (\Lambda \otimes \id_\calL) = \Lambda \circ \epsilon = \mu \circ (\id_\calL \otimes \Lambda).
\]
In analogy with Sweedler's result for Hopf algebras in the category of finite-di\-men\-sion\-al vector spaces, the coend $\calL$ admits an integral, which is unique up to scalar \cite[Thm.~6.1]{L95}. When $\calC$ is semisimple, then, up to scalar, we have
\[
 \Lambda = \left( \dim_\calC(V_i) \cdot \rcoev_{V_i} \right)_{i \in I},
\]
which means that we can think of an integral $\Lambda$ of the coend $\calL$ as extending the Kirby color to the non-semisimple case. When $\calC$ is the category $\mods{H}$ of finite-dimensional representations of a finite-dimensional factorizable ribbon Hopf algebra $H$, then, up to scalar, we have
\[
 \Lambda(1) = \lambda \in H^*,
\]
where $\lambda \in H^*$ is a classical right integral on the Hopf algebra $H$. See \cite[Sec.~2.5]{K96a} for both claims.

The algebraic setup discussed up to here is sufficient to perform Lyubashenko's construction, but in order to obtain TQFTs, we also need the theory of modified traces. Let us present the key definitions by focusing on a relevant special case. We denote by $\Proj(\calC)$ the full subcategory of projective objects of $\calC$, which forms a \textit{tensor ideal} in $\calC$, in the sense that it is closed under retracts and absorbent under tensor products, see \cite[Def.~3.1.1]{GKP10}. A \textit{trace} on $\Proj(\calC)$ is a family of linear maps
\[
 \rmt := \{ \rmt_P : \End_\calC(P) \to \Bbbk \}_{P \in \Proj(\calC)}
\]
satisfying:
\begin{enumerate}
 \item \textit{Cyclicity}: $\rmt_P \left( \pic{m-trace_cyclicity_1} \right) = \rmt_Q \left( \pic{m-trace_cyclicity_2} \right)$ \par \bigskip
  for all $P,Q \in \Proj(\calC)$, $f \in \calC(P,Q)$, and $g \in \calC(Q,P)$; 
  \bigskip
 \item \textit{Partial trace}: $\rmt_{P \otimes X} \left( \pic{m-trace_partial_trace_1} \right) = \rmt_P \left( \pic{m-trace_partial_trace_2} \right)$ \par \bigskip
  for all $P \in \Proj(\calC)$, $X \in \calC$, and $f \in \End_{\calC}(P \otimes X)$.
\end{enumerate}
We say a trace $\rmt$ on $\Proj(\calC)$ is \textit{non-degenerate} if, for all $P \in \Proj(\calC)$ and $X \in \calC$, the bilinear pairing $\rmt_P(\_ \circ \_) : \calC(X,P) \times \calC(P,X) \to \Bbbk$ determined by $(g,f) \mapsto \rmt_P(g \circ f)$ is non-degenerate. Thanks to \cite[Cor.~5.6]{GKP18}, for a modular\footnote{The statement is a particular case of a much more general existence and uniqueness result, see \cite[Thm.~5.5]{GKP18}.} category $\calC$ there exists a trace $\rmt$ on $\Proj(\calC)$, which is unique up to scalar and furthermore non-degenerate. When $\calC$ is semisimple, then $\Proj(\calC) = \calC$, and the standard categorical trace $\tr_\calC$ is the unique trace on $\calC$ up to scalar. When $\calC$ is the category $\mods{H}$ of finite-dimensional representations of a finite-dimensional factorizable\footnote{Again, hypotheses for this result can be considerably relaxed, but we prefer to avoid introducing more terminology.} ribbon Hopf algebra $H$, there is a natural correspondence between the space of traces on $\Proj(\calC)$ and the spaces of so-called \textit{symmetrized} integrals on $H$, see \cite[Thm.~1]{BBG18}.
