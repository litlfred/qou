---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-6
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.983
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
Giraud introduced gerbes  in order to achieve a geometrical understanding of \emph{non-abelian} cohomology \cite{giraud}. However, already \emph{abelian} gerbes turned out to be interesting: Brylinski introduced the notion of a \emph{connection} on an abelian gerbe, and showed that these represent classes in a certain \emph{differential} cohomology theory, namely Deligne cohomology \cite{brylinski1}. Deligne cohomology in degree two  has before been related to two-dimensional conformal field theory  by Gaw\c edzki \cite{gawedzki3}. This relation is   established by means of the \emph{surface holonomy} of a connection on an abelian gerbe, which provides a term in the action functional of the field theory. 

Surface holonomy of  connections on  abelian gerbes is today well understood; see \cite{waldorf3,fuchs8} for reviews. While definitions of connections on \emph{non-abelian} gerbes have appeared \cite{breen1,aschieri}, it remained unclear what the surface holonomy of these connections is supposed to be,  how it is defined, and how it can be used. 



In the present article we propose a general and systematic approach to connections on non-abelian gerbes, including notions of parallel transport and surface holonomy. Our approach is \emph{general} in the sense that it works for gerbes whose band is an arbitrary Lie 2-groupoid, and whose fibres are modelled by an arbitrary 2-category. Our approach is \emph{systematic} in the sense that it is solely based on axioms for parallel transport along surfaces, formulated in terms of gluing laws and smoothness conditions. The whole theory of connections on non-abelian gerbes is then derived as  a consequence.






  
        



In order to illustrate how this axiomatic formulation works we shall briefly review a corresponding formulation in a more familiar setting, namely the one of connections on fibre bundles; see   \cite{schreiber3}. It shows that for a Lie group $G$ the category of principal $G$-bundles with connection over a smooth manifold $X$ is equivalent to a category consisting of functors
\begin{equation}
\label{eq:functors}
F: \mathcal{P}_1(X) \to G\text{-}\mathrm{Tor}\text{.}
\end{equation}
These functors are defined on the path groupoid $\mathcal{P}_1(X)$ of the manifold $X$; its objects are the points of $X$, and its morphisms are (certain classes of)  paths in $X$. The functors \erf{eq:functors} take values in the category of $G$-torsors, i.e. smooth manifolds with a free and transitive $G$-action. 

The correspondence between principal $G$-bundles with connection and  functors \erf{eq:functors} is established by letting the functor $F$ assign to points the fibres of a given bundle, and to paths the corresponding parallel transport maps. The \emph{gluing laws} of parallel transport are precisely the axioms of a functor. The \emph{smoothness conditions} of parallel transport are more involved; they can be encoded in  the functors \erf{eq:functors} by requiring  \emph{smooth descend data} with respect to an open cover of $X$.
Functors  \erf{eq:functors} with smooth descend data are called \emph{transport functors with $G$-structure} -- they constitute an axiomatic formulation of the parallel transport of connections in $G$-bundles. 


In Sections \ref{sec1} and  \ref{sec6_3} of the present article we generalize this axiomatic formulation to  connections on gerbes. Our formulation does not use any existing concept of a gerbe with connection  --- such concepts are an \emph{output} of our approach. It is based on \emph{2-functors} defined on the \emph{path 2-groupoid} $\mathcal{P}_2(X)$ of $X$, with values in some \quot{target} 2-category $T$,
\begin{equation}
\label{eq:2functors}
F: \mathcal{P}_2(X) \to T\text{.}
\end{equation}
In Section \ref{sec:path2groupoid} we review the path 2-groupoid: it is like the path groupoid but with additional 2-morphisms, which are essentially fixed-end homotopies between paths. 


For example, if $T$ is the 2-category of algebras (over some fixed field), bimodules, and intertwiners, a 2-functor \erf{eq:2functors} provides for each point $x\in X$ an algebra $F(x)$, which is supposed to be the fibre of the gerbe at the point $x$. Further, it provides for each path $\gamma$ from $x$ to $y$ a $F(x)$-$F(y)$-bimodule $F(\gamma)$, which is supposed to be the parallel transport of the connection on that gerbe along the curve parameterized by  $\gamma$. Finally, it provides for each homotopy  $\Sigma$  between paths $\gamma$ and $\gamma'$ an intertwiner 
\begin{equation*}
F(\Sigma): F(\gamma) \to  F(\gamma')\text{,}
\end{equation*}
which is supposed to be the parallel transport of the connection on that gerbe along the surface parameterized by $\Sigma$. 
The axioms of the 2-functor \erf{eq:2functors}  describe how these parallel transport structures are compatible with the composition of paths and gluing of homotopies.
These axioms and all other 2-categorical structure we use can be looked up in \cite[Appendix A]{schreiber6}.


Apart from the evident generalization from functors to 2-functors, more work has to be  invested into the generalization of the smoothness conditions. Imposing smoothness conditions relies on a notion of \emph{local triviality}
for 2-functors defined on path 2-groupoids. A 2-functor
\begin{equation*}
F: \mathcal{P}_2(X) \to T
\end{equation*}
is considered to be trivializable, if it factors through a prescribed 2-functor $i: \mathrm{Gr} \to T$, with $\mathrm{Gr}$ a strict Lie 2-groupoid. The  Lie 2-groupoid $\mathrm{Gr}$ plays the role of the \quot{typical fibre}, and the 2-functor $i$ indicates how the typical fibre is realized in the target 2-category $T$. A local trivialization of the 2-functor $F$
is a cover of $X$ by open sets $U_{\alpha}$,  a collection of locally defined \quot{trivial} 2-functors $\mathrm{triv}_{\alpha}: \mathcal{P}_2(U_{\alpha}) \to \mathrm{Gr}$ and of equivalences
\begin{equation*}
\alxydim{}{t_{\alpha}: F|_{U_{\alpha}} \ar[r]^-{\cong} & i \circ \mathrm{triv}_{\alpha}}
\end{equation*}
between 2-functors defined on $U_{\alpha}$. Local trivializations lead to \emph{descend data}, generalizing the transition functions of a bundle.
The descent data of a 2-functor with a local trivialization consists of the 2-functors $\mathrm{triv}_{\alpha}$, of transformations
\begin{equation*}
g_{\alpha\beta}: i \circ \mathrm{triv}_{\alpha} \to i \circ \mathrm{triv}_{\beta}
\end{equation*}
between 2-functors over $U_{\alpha} \cap U_{\beta}$,
and of higher coherence data that we shall ignore for the purposes of this introduction.  The theory of local trivializations and descent data for 2-functors is developed in our paper \cite{schreiber6} and reviewed in Section \ref{sec:loctriv}.


The smoothness conditions we want to formulate are imposed with respect to descent data;  they are the content of Section \ref{sec6_3}.  First of all, we require that the 2-functors $\mathrm{triv}_{\alpha}$ are smooth. This makes sense since they take values in the \emph{Lie} 2-groupoid $\mathrm{Gr}$. For certain Lie 2-groupoids, a theory developed in our paper \cite{schreiber5} identifies the smooth functors $\mathrm{triv}_{\alpha}$ with certain 2-forms $B_{\alpha}$ on $U_{\alpha}$ --- the curving of the gerbe connection. In order to treat the transformations $g_{\alpha\beta}$, we apply an observation in abstract 2-category theory: the transformations $g_{\alpha\beta}$ can be regarded as a collection of functors 
\begin{equation*}
\holo(g_{\alpha\beta}): \mathcal{P}_1(U_{\alpha} \cap U_{\beta}) \to \Lambda T\text{,}
\end{equation*}
for $\Lambda T$ a certain category of diagrams in $T$.
The smoothness condition that we impose for the transformation $g_{\alpha\beta}$ is that the functors $\holo(g_{\alpha\beta})$ are transport functors. According to the before-mentioned correspondence between transport functors and fibre bundles with connection, we thus obtain a smooth fibre bundle $\holo(g_{\alpha\beta})$ with connection over two-fold overlaps $U_{\alpha} \cap U_{\beta}$ --- a significant feature of a gerbe.


Summarizing this overview, our axiomatic formulation of connections on gerbes consists of transport 2-functors: 2-functors $F: \mathcal{P}_2(X) \to T$ that are locally trivializable with respect to a typical fibre $i: \mathrm{Gr} \to T$, and have smooth descent data. 


In Section \ref{sec4} of this article we test our axiomatic formulation by choosing examples of target 2-categories $T$ and 2-functors $i: \mathrm{Gr} \to T$. In these examples the Lie 2-groupoids are \quot{deloopings} of strict Lie 2-groups, $\mathrm{Gr}=\mathcal{B}\mathfrak{G}$; these Lie 2-groups $\mathfrak{G}$ play the same role for gerbes as Lie groups  for principal bundles. We find the following results:
\begin{enumerate}[(i)]
\item 
For a general Lie 2-group $\mathfrak{G}$ and the identity 2-functor 
\begin{equation*}
i = \id_{\mathcal{B}\mathfrak{G}}: \mathcal{B}\mathfrak{G} \to \mathcal{B}\mathfrak{G}
\end{equation*}
we prove (Theorem \ref{th:class}) that there is a bijection
\begin{equation*}
\hc 0 \mathrm{Trans}_{\mathcal{B}\mathfrak{G}}(X, \mathcal{B}\mathfrak{G})  \cong \hat H^2(X,\mathfrak{G}) 
\end{equation*}
between isomorphism classes of transport 2-functors  and the degree two differential non-abelian cohomology of  $X$ with coefficients in  $\mathfrak{G}$. These cohomology groups have been explored in \cite{breen1} and \cite{baez2}; they are an extension of Giraud's non-abelian cohomology by differential form data. Upon setting $\mathfrak{G}=\mathcal{B}S^1$ it reduces to  Deligne cohomology. 


  

\item
The Lie 2-group $\mathcal{B}S^1$ has a monoidal functor $\mathcal{B}S^1 \to S^1\text{-}\mathrm{Tor}$ to the monoidal category of $S^1$-torsors, by sending the single objects of $\mathcal{B}S^1$ to $S^1$ considered as a torsor over itself. Delooping  yields a 2-functor 
\begin{equation*}
i: \mathcal{BB}S^1 \to \mathcal{B}(S^1\text{-}\mathrm{Tor})\text{.}
\end{equation*}
We prove (Theorem \ref{th:bgrb})  that there is an  equivalence of 2-categories
\begin{equation*}
\mathrm{Trans}_{\mathcal{BB}S^1}(X, \mathcal{B}(S^1\text{-}\mathrm{Tor})) \cong \bigset{10em}{$S^1$-bundle gerbes with connection over $X$}\text{.}
\end{equation*}
Bundle gerbes have been introduced by Murray \cite{murray}.
The equivalence arises  by realizing that the transport functor $\holo(g_{\alpha\beta})$ in the descent data  corresponds in the present situation to an $S^1$-bundle with connection.

 

\item
Let $H$ be a Lie group and let $\mathrm{AUT}(H)$ be the automorphism 2-group of $H$. It has a monoidal functor $\AUT(H) \to \hbitor$ to the monoidal category of $H$-bitorsors. Delooping yields a 2-functor
\begin{equation*}
i: \mathcal{B}\AUT(H) \to \mathcal{B}(\hbitor)\text{.}
\end{equation*}  
We prove (Theorem \ref{th:nagrb}) that there is an  equivalence of 2-categories
\begin{equation*}
\mathrm{Trans}_{\mathcal{B}\mathrm{AUT}(H)}(X,\mathcal{B}(H\text{-}\mathrm{BiTor})) \cong \bigset{13em}{Non-abelian $H$-bundle gerbes with connection over $X$}\text{.}
\end{equation*}
Non-abelian bundle gerbes are a generalization of $S^1$-bundle gerbes introduced in \cite{aschieri}, and the above equivalence arises by proving that the transport functor $\holo(g_{\alpha\beta})$ corresponds in the present situation to a \quot{principal $H$-bibundle with twisted connection}.

\end{enumerate}
The relations (i) to (iii) show that all these existing concepts of gerbes with connection fit into our axiomatic formulation. 


Apart from these relations to existing gerbes with connection, transport 2-functors are able to  determine systematically new  concepts  in cases when only the target 2-category $T$ and the 2-group $\mathfrak{G}$ are given. We demonstrate this in Section \ref{sec4_4} with the examples of connections on  vector 2-bundles, string 2-bundles, and  principal 2-bundles. 



Finally,  we  discuss in Section \ref{sec5} the notion of parallel transport along surfaces,  which is manifestly included in the concept of a transport 2-functor. We  introduce a notion of surface holonomy for transport 2-functors, defined for closed oriented surfaces with a marking, i.e. a certain presentation of its fundamental group. It is obtained by evaluating the transport 2-functor on a homotopy that realizes the single relation in this presentation. 


The existing notion of surface holonomy for \emph{abelian} gerbes  takes values in  $S^1$ \cite{gawedzki3,murray}, while our notion of surface holonomy takes values in the 2-morphisms of the target 2-category $T$. In order to compare the two notions, we propose a \quot{reduction} procedure which can be applied in the case that typical fibre of the transport 2-functor is of the form $i: \mathcal{B}\mathfrak{G} \to T$, where $\mathfrak{G}$ is a Lie 2-group. The first part of this procedure is the definition of an abelian group $\mathfrak{G}\red$ which can be formed for any Lie 2-group $\mathfrak{G}$ (Definition \ref{def:redgroup}). Heuristically, it generalizes the abelianization of an ordinary Lie group. As the second part of the reduction procedure, we show (Proposition \ref{prop:reduction}) that the surface holonomy of every transport 2-functor with $\mathcal{B}\mathfrak{G}$-structure can consistently be reduced to a function with values in $\mathfrak{G}\red$.  






Our main results in Section \ref{sec5} concern this reduced  surface holonomy of transport 2-functors with $\mathcal{B}\mathfrak{G}$-structure. We prove in Theorem \ref{th:rhol} a  rigidity result for reduced surface holonomy, namely that it  depends only on the isomorphism class of the transport 2-functor, and only on the equivalence class of the marking. The isomorphism invariance allows us to transfer the reduced surface holonomy from transport 2-functors through the equivalences (i), (ii), and (iii) described above. In particular, we equip non-abelian $\mathfrak{G}$-gerbes with a well-defined notion of a $\mathfrak{G}\red$-valued surface holonomy; such a concept was not known before.


Finally, we show that our new concept of reduced surface holonomy is compatible with the existing notion of $S^1$-valued surface holonomy of abelian gerbes. Namely, in the case  $\mathfrak{G}=\mathcal{B}S^1$ we  find  for the reduction  $(\mathcal{B}S^1)\red = S^1$, so that both concepts take values in the same set. We prove then
in Proposition \ref{propabsf} that the two concepts indeed coincide.  Thus, our new notion of (reduced) surface holonomy consistently extends the existing notion from abelian to non-abelian gerbes.


\paragraph{Acknowledgements.} 
The project described here has some of
its roots in ideas of John Baez and in his joint work with  US, and we are grateful for all discussions and suggestions.
We are also  grateful for opportunities to give talks about this project at an unfinished state, namely at the Fields Institute, at the VBAC 2007 meeting in Bad Honnef, at the MedILS in Split and at the NTNU in Trondheim. In addition, we thank the Hausdorff Research Institute for Mathematics in Bonn for kind hospitality and support during several visits.




\setsecnumdepth{2}
