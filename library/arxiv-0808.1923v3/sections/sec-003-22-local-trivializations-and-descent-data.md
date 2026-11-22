---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-003-22-local-trivializations-and-descent-data
section_title: "Local Trivializations and Descent Data"
section_number: 2.2
pages: 7-10
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.984
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec1_2}
\label{sec:loctriv}

Let $T$ be a 2-category. 
A key feature of a transport 2-functor is that it is locally trivializable. Local trivializations
of a   2-functor $F: \mathcal{P}_2(M)
\to T$ are defined with respect to three attributes:
\begin{enumerate}
\item
A  strict 
2-groupoid $\mathrm{Gr}$, the \emph{structure 2-groupoid}. In Section \ref{sec3} we will require that $\mathrm{Gr}$ is a \emph{Lie} 2-groupoid, and formulate smoothness conditions with respect to its smooth structure. 

\item
A   2-functor $i:\mathrm{Gr} \to T$ that indicates how the structure 2-groupoid is realized in the target 2-category.  

\item 
A surjective
submersion $\pi:Y \to M$, which serves as an \quot{open cover} of the base manifold $M$.
\end{enumerate}
For a surjective submersion $\pi:Y \to M$ the fibre products $Y^{[k]}\nobr := \nobr Y \times_M ... \times_M Y$ are again smooth manifolds in such a way that the  projections
$\pi_{i_1...i_p}\maps Y^{[k]} \to Y^{[p]}$
(to the indexed factors) are smooth maps. An example is an open cover $\mathfrak{U}=\left \lbrace U_\alpha \right \rbrace$ of $M$, for which the disjoint union of all open sets $U_\alpha$ together with the projection to $M$ is a surjective submersion. In this example, the $k$-fold fibre product is the disjoint union of the $k$-fold intersections of the open sets $U_{\alpha}$. 

\begin{definition}
\label{sec2_def5}
A \emph{$\pi$-local $i$-trivialization} of a 2-functor 
$F\maps \mathcal{P}_2(M)
\to T$
is a pair $(\mathrm{triv},t)$ of a strict 2-functor 
\begin{equation*}
\mathrm{triv}: \mathcal{P}_2(Y) \to \mathrm{Gr}
\end{equation*}
and
a \pe
\begin{equation*}
\quadrat{\mathcal{P}_2(Y)}{\mathcal{P}_2(M)}{\mathrm{Gr}}{T\text{.}}{\pi_{*}}{\mathrm{triv}}{F}{i}{t}
\end{equation*}
\end{definition}




For the notion of a pseudonatural equivalence we refer to \cite[Appendix A]{schreiber6}. According to the conventions we fixed there, it \emph{includes} a weak inverse $\bar t$ together with modifications
\begin{equation}
\label{7}
i_t :  \bar t \circ t \Rightarrow \id_{\pi^{*}F}
\quad\text{ and }\quad
j_t :  \id_{\mathrm{triv}_i} \Rightarrow t \circ \bar t
\end{equation}
satisfying the so-called zigzag identities.
 




In the following we use the abbreviation $\mathrm{triv}_i := i \circ \mathrm{triv}$, and we write $\loctrivfunct{i}{\mathrm{Gr}}{2}$ for the 2-category of 2-functors $F: \mathcal{P}_2(M) \to T$ with $\pi$-local $i$-trivializations (together with all pseudonatural transformations and all modifications).
Next we come to the definition of a 2-category $\trans{i}{\pi}{2}$ of \emph{descent data} with respect to a surjective submersion $\pi:Y \to M$ and a structure 2-groupoid $i:\mathrm{Gr} \to T$. 
\begin{definition}
\label{def:descendobject}
A \uline{descent object}  is a  quadruple $(\mathrm{triv},g,\psi,f)$  consisting of a strict  2-functor
\begin{equation*}
\mathrm{triv}\maps\mathcal{P}_2(Y) \to \mathrm{Gr}\text{,}
\end{equation*}
a \pe\
\begin{equation*}
g\maps \pi_1^{*}\mathrm{triv}_i \to \pi_2^{*}\mathrm{triv}_i\text{,}
\end{equation*}
and invertible, coherent modifications 
\begin{equation*}
\psi: \id_{\mathrm{triv}_i} \Rightarrow \Delta^{*}g
\quand 
f\maps \pi_{23}^{*}g \circ \pi_{12}^{*}g \Rightarrow \pi_{13}^{*}g\text{.}
\end{equation*}
\end{definition}
\begin{comment}
In these diagrams, $r$, $l$ and $a$ are the right and left \unifier s and the associator of the 2-category $T$, $\Delta:Y \to Y^{[2]}$ is the diagonal map, and $\Delta_{112},\Delta_{122}:Y^{[2]} \to Y^{[3]}$ are the maps duplicating the first or the second factor, respectively. \end{comment}

The coherence conditions for the modifications $\psi$ and $f$ can be found in \cite[Definition 2.2.1]{schreiber6}.


Let us briefly rephrase the above definition in case that $Y$ is the union of open sets $U_{\alpha}$: first there are  strict 2-functors $\mathrm{triv}_{\alpha}:\mathcal{P}_2(U_{\alpha}) \to \mathrm{Gr}$. To compare the difference between $\mathrm{triv}_{\alpha}$ and $\mathrm{triv}_{\beta}$ on a two-fold intersection $U_{\alpha}\cap U_{\beta}$ there are \pe s $g_{\alpha\beta}: (\mathrm{triv}_{\alpha})_i \to (\mathrm{triv}_{\beta})_i$. If we assume for a moment that $g_{\alpha\beta}$ was the transition function of some fibre bundle, one would demand that $1=g_{\alpha\alpha}$ on every $U_{\alpha}$ and that $g_{\beta\gamma}g_{\alpha\beta}=g_{\alpha\gamma}$ on every three-fold intersection $U_{\alpha}\cap U_{\beta}\cap U_{\gamma}$. In the present situation, however, these equalities have been replaced by modifications: the first one by a modification $\psi_{\alpha}: \id_{(\mathrm{triv}_{\alpha})_i} \Rightarrow g_{\alpha\alpha}$ and the second one by a modification $f_{\alpha\beta\gamma}: g_{\beta\gamma} \circ g_{\alpha\beta} \Rightarrow g_{\alpha\gamma}$.


Next we describe how to extract a descend object from a local trivialization of a 2-functor following \cite[Section 2.3]{schreiber6}. Let $F:\mathcal{P}_2(M) \to
T$ be a  2-functor with a $\pi$-local $i$-trivialization $(\mathrm{triv},t)$.
Using the weak inverse $\bar t: \mathrm{triv}_i
\to \pi^{*}F$ of $t$ we define
\begin{equation*}
g:= \pi_2^{*}t \circ \pi_1^{*}\bar t : \pi_1^{*}\mathrm{triv_i} \to \pi_2^{*}\mathrm{triv}_i\text{.}
\end{equation*}
This composition is well-defined since $\pi_1^{*}\pi^{*}F=\pi_2^{*}\pi^{*}F$. Let $i_t$ and$j_t$ be the modifications \erf{7}. We obtain $\Delta^{*}g= t \circ \bar t$, so that the definition $\psi:= j_t$ yields the invertible modification
$\psi:\id_{\mathrm{triv}_i} \Rightarrow \Delta^{*}g$.
Similarly, one defines with $i_{t}$ the invertible modification $f$.
The quadruple $(\mathrm{triv},g,\psi,f)$ obtained like this is a descend object in the sense of Definition \ref{def:descendobject}; see \cite[Lemma 2.3.1]{schreiber6}.





Next suppose $(\mathrm{triv},g,\psi,f)$ and $(\mathrm{triv}',g',\psi',f')$ are descent objects. A \emph{descent 1-morphism} $(\mathrm{triv},g,\psi ,f) \to (\mathrm{triv}',g',\psi ',f')$
  is a pair $(h,\varepsilon)$  consisting of a 
  \pt
\begin{equation*}
h: \mathrm{triv}_i \to \mathrm{triv}_i'
\end{equation*}
and  an invertible    modification
\begin{equation*}
\epsilon: \pi_2^{*}h \circ g \Rightarrow g' \circ \pi_1^{*}h
\end{equation*}
satisfying two natural coherence conditions; see \cite[Definition 2.2.2]{schreiber6}.
\begin{comment}
These are the commutativity of the diagrams
\begin{equation}
\label{5}
\alxydim{@C=2cm}{\pi_{23}^{*}g' \circ (\pi_{2}^{*}h \circ \pi_{12}^{*}g) \ar@{=>}[r]^{a} \ar@{=>}[d]_{\id \circ \pi_{12}^{*}\epsilon} & (\pi_{23}^{*}g' \circ \pi_{2}^{*}h) \circ \pi_{12}^{*}g \ar@{=>}[d]^{\pi_{23}^{*}\epsilon^{-1} \circ \id}   \ar@{=>}[d]\\\pi_{23}^{*}g' \circ (\pi_{12}^{*}g' \circ \pi_1^{*}h)  \ar@{=>}[d]_{a^{-1}} & (\pi_{3}^{*}h \circ \pi_{23}^{*}g) \circ \pi_{12}^{*}g \ar@{=>}[d]^{a}   \ar@{=>}[d] \\(\pi_{23}^{*}g' \circ \pi_{12}^{*}g') \circ \pi_1^{*}h\ar@{=>}[d]_{f' \circ \id} &\pi_{3}^{*}h \circ (\pi_{23}^{*}g \circ \pi_{12}^{*}g)\ar@{=>}[d]^{\id\circ f} \\ \pi_{13}^{*}g'\circ \pi_1^{*}h \ar@{=>}[r]_{\pi_{13}^{*}\epsilon} & \pi_{3}^{*}h \circ \pi_{13}^{*}g\text{.}}
\end{equation}
and
\begin{equation}
\label{4}
\alxydim{}{\id_{\mathrm{triv}'_i} \circ h \ar@{=>}[r]^-{l_{h}} \ar@{=>}[d]_{\psi' \circ \id_h} & h \ar@{=>}[r]^-{r_{h}^{-1}} & h \circ \id_{\mathrm{triv}_i} \ar@{=>}[d]^{\id_h \circ \psi} \\ \Delta^{*}g' \circ h \ar@{=>}[rr]_{\Delta^{*}\epsilon} && h \circ \Delta^{*}g\text{.}}
\end{equation}
\end{comment}
Finally, we suppose that $(h_1,\varepsilon_1)$ and $(h_2,\varepsilon_2)$ are descent 1-morphisms from a descent object $(\mathrm{triv},g,\psi,f)$ to another descent object $(\mathrm{triv}',g',\psi',f')$. A \emph{descent 2-morphism} $(h_1,\varepsilon_1) \Rightarrow (h_2,\varepsilon_2)$ is a modification 
\begin{equation*}
E: h_1 \Rightarrow h_2
\end{equation*}
satisfying another coherence condition; see \cite[Definition 2.2.3]{schreiber6}.
\begin{comment}
Namely, the diagram
\begin{equation}
\label{6}
\alxydim{@=1.2cm}{g' \circ \pi_1^{*}h_1 \ar@{=>}[d]_{\id \circ \pi_1^{*}E}  \ar@{=>}[r]^{\varepsilon_{1}} & \pi_2^{*}h_1 \circ g \ar@{=>}[d]^{\pi_2^{*}E \circ \id } \\ g' \circ \pi_1^{*}h_2 \ar@{=>}[r]_{\varepsilon_2} & \pi_2^{*}h_2 \circ g\text{.}}
\end{equation}
\end{comment}


Descent objects, 1-morphisms and 2-morphisms form a  2-category $\trans{i}{\pi}{2}$, called the \emph{descent 2-category}. In concrete examples of the target 2-category $T$ these structures have natural interpretations in terms of smooth maps and differential forms,  as we show in Section \ref{sec4}. The extraction of a descent object from a local trivialization  outlined above extends to a 2-functor
\begin{equation}
\label{eq:expi}
\ex{\pi}:\loctrivfunct{i}{\mathrm{Gr}}{2} \to \trans{i}{\mathrm{Gr}}{2}\text{,}
\end{equation}
which we have described in \cite[Section 2.3]{schreiber6}.
 






\label{sec:locglob}







In order to avoid the dependence to the fixed surjective submersion $\pi:Y \to M$, we have shown in \cite[Section 4.2]{schreiber6} that the two 2-categories $\loctrivfunct{i}{\mathrm{Gr}}{2}$ and $\trans{i}{\mathrm{Gr}}{2}$ form a direct system for refinements of surjective submersions over $M$. The corresponding direct limits are 2-categories
\begin{equation*}
\mathrm{Triv}^2(i)_{M} := \lim_{\overrightarrow{\pi}} \mathrm{Triv}^2_{\pi}(i)
\quand
\mathfrak{Des}^2(i)_{M} := \lim_{\overrightarrow{\pi}} \mathfrak{Des}^2_{\pi}(i)\text{.}
\end{equation*}
For instance, an object in the direct limit is a pair of a surjective submersion $\pi$ and an object in the corresponding  2-category $\mathrm{Triv}^2_{\pi}(i)$ or $\mathfrak{Des}^2_{\pi}(i)$. 1-morphisms and 2-morphisms are defined over common refinements.
The 2-functor $\ex{\pi}$ from \erf{eq:expi} induces an equivalence
\begin{equation*}
\mathrm{Triv}^2(i)_{M} \cong \mathfrak{Des}^2(i)_{M}
\end{equation*}
between these two direct limit 2-categories \cite[Proposition 4.2.1]{schreiber6}.


Finally, we want to get rid of the chosen trivializations that are attached to the objects of $\mathrm{Triv}^2(i)_{M}$. We denote by $\mathrm{Funct}_i(\mathcal{P}_2(M),T)$ the 2-category of locally $i$-trivializable 2-functors, i.e. 2-functors which \emph{admit} a $\pi$-local $i$-trivialization, for \emph{some} surjective submersion $\pi$. We have shown \cite[Theorem 4.3.1]{schreiber6}:
\begin{theorem}
\label{th:locglobequiv}
There is an equivalence
\begin{equation*}
\mathrm{Funct}_i(\mathcal{P}_2(M),T) \cong \mathfrak{Des}^2(i)_{M} 
\end{equation*}
between 2-categories of locally $i$-trivializable 2-functors and their descend data.
\end{theorem}

In Section \ref{sec6_3} we  select a sub-2-category of $\mathfrak{Des}^2(i)_{M}$ consisting of \emph{smooth descend data}. The corresponding sub-2-category of $\mathrm{Funct}_i(\mathcal{P}_2(M),T)$ is the one we are aiming at -- the 2-category of transport 2-functors.
