---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-009-33-some-features-of-transport-2-functors
section_title: "Some Features of Transport 2-Functors"
section_number: 3.3
pages: 18-22
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.98
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec:features}

In this section we provide several features of transport 2-functors.


\subsubsection{Operations on Transport 2-Functors}

\label{operations}

It is straightforward to see that transport 2-functors allow a list of natural operations.
\begin{enumerate}[(i)]
\item 
\emph{Pullbacks}: Let $f:M \to N$ be a smooth map. The pullback $f^{*}\mathrm{tra}$ of any transport 2-functor on $N$ is a transport 2-functor on $M$.

\item
\emph{Tensor products}:
Let $\otimes: T \times T \to T$ be a monoidal structure on a 2-category $T$. For transport 2-functors $\mathrm{tra}_1,\mathrm{tra}_2:\mathcal{P}_2(M) \to T$ with $\mathrm{Gr}$-structure, the pointwise tensor product $\mathrm{tra}_1 \otimes \mathrm{tra}_2: \mathcal{P}_2(M) \to T$ is again a transport 2-functor with $\mathrm{Gr}$-structure, and makes the 2-category $\transport{}{2}{\mathrm{Gr}}{T}$ a monoidal 2-category. 


\item
\emph{Change of the target 2-category}:
Let $T$ and $T'$ be two target 2-categories equipped with 2-functors $i:\mathrm{Gr} \to T$ and $i': \mathrm{Gr} \to T'$,  and let $F:T \to T'$ be a 2-functor together with a \pe
\begin{equation*}
\rho: F \circ i \to i'\text{.}
\end{equation*}
If $\mathrm{tra}:\mathcal{P}_2(M) \to T$ is a transport 2-functor with $\mathrm{Gr}$-structure, $F \circ \mathrm{tra}$ is also a transport 2-functor with $\mathrm{Gr}$-structure. In particular, this is the case for $i':= F \circ i$ and $\rho=\id$.

\item
\emph{Change of the structure 2-groupoid}: Let $\mathrm{tra}:\mathcal{P}_2(M) \to T$ be a transport 2-functor with $\mathrm{Gr}$-structure, for a 2-functor $i:\mathrm{Gr} \to T$ which is a composition
\begin{equation*}
\alxydim{}{\mathrm{Gr} \ar[r]^{F} & \mathrm{Gr}' \ar[r]^{i'} & T}
\end{equation*}
in which $F$ is a smooth 2-functor.
Then, $\mathrm{tra}$ is also a transport 2-functor with $\mathrm{Gr}'$-structure, since for any local $i$-trivialization $(\mathrm{triv},t)$ of $\mathrm{tra}$ we have a local $i'$-trivialization $(F \circ \mathrm{triv},t)$.  

\end{enumerate}


\subsubsection{Structure Lie 2-Groups}

We describe some examples of Lie 2-groupoids and outline the role of the corresponding transport 2-functors. First we recall the following generalization of a Lie group.

\begin{definition}
\label{def4}
A \emph{Lie 2-group} is a strict monoidal Lie category $(\mathfrak{G},\boxtimes,\trivlin)$ together with a smooth functor $inv:\mathfrak{G} \to \mathfrak{G}$ such that \begin{equation*}
X \boxtimes inv(X) = \trivlin = inv(X) \boxtimes X
\quad\text{ and }\quad
f \boxtimes inv(f) = \id_{\trivlin} = inv(f) \boxtimes f
\end{equation*}
for all objects $X$ and all morphisms $f$ in $\mathfrak{G}$.
\end{definition}

The strict monoidal category $(\mathfrak{G},\boxtimes,\trivlin)$ defines a strict 2-category $\mathcal{B}\mathfrak{G}$ with a single object \cite[Example A.2]{schreiber6}. 
The additional functor $inv$ assures that $\mathcal{B}\mathfrak{G}$ is a strict 2-\emph{groupoid}. All our examples in Section \ref{sec4} discuss transport 2-functors with $\mathcal{B}\mathfrak{G}$-structure, for $\mathfrak{G}$ a Lie 2-group.  


Lie 2-groups can be obtained from the following structure.


\begin{definition}
\label{def:crossedmodule}
A \emph{smooth crossed module} is a quadruple $(G,H,t,\alpha)$ of Lie groups $G$ and $H$,  of a Lie group homomorphism  $t: H \to G$, and of a smooth left action $\alpha: G \times H \to H$ by Lie group homomorphisms such that
\begin{itemize}
\item[a)]
$t(\alpha(g,h))=gt(h)g^{-1}$ for all $g\in G$ and $h\in H$.
\item[b)] 
$\alpha(t(h),x) = hxh^{-1}$ for all $h,x\in H$.
\end{itemize}
\end{definition}

The construction of a Lie 2-group $\mathfrak{G}=\mathfrak{G}(G,H,t,\alpha)$ from a given smooth crossed module $(G,H,t,\alpha)$ can be found in the Appendix of \cite{schreiber5}. We shall explicitly  describe the corresponding  Lie 2-groupoid $\mathcal{B}\mathfrak{G}$. It has one object denoted  $\ast$ . A 1-morphism is a group element $g\in G$, the identity 1-morphism is the neutral element, and the composition of 1-morphisms is the multiplication, $g_2 \circ g_1 := g_2g_1$.  
The 2-morphisms are pairs $(g,h)\in G \times H$, considered as 2-morphisms
\begin{equation*}
\bigon{\ast}{\ast}{g}{g'}{h}
\end{equation*}
with $g':=t(h)g$.
The vertical composition is
\begin{equation*}
\alxydim{@C=2cm}{\ast \ar[r]|{g'}="2" \ar@/^2.5pc/[r]^{g}="1" \ar@/_2.5pc/[r]_{g''}="3" \ar@{=>}"1";"2"|{h}\ar@{=>}"2";"3"|{h'} & \ast}
 = \bigon{\ast}{\ast}{g}{g''}{h'h}
\end{equation*}
with $g'=t(h)g$ and $g''=t(h')g'=t(h'h)g$, and the horizontal composition is
\begin{equation*}
\alxydim{@C=1.2cm}{\ast \ar@/^1.5pc/[r]^{g_{1}}="1" \ar@/_1.5pc/[r]_{g'_{1}}="2" \ar@{=>}"1";"2"|*+{h_{1}} & \ast \ar@/^1.5pc/[r]^{g_2}="3" \ar@/_1.5pc/[r]_{g'_2}="4" \ar@{=>}"3";"4"|*+{h_2} & \ast} = \alxydim{@C=3cm}{\ast \ar@/^2.5pc/[r]^{g_2g_1}="1" \ar@/_2.5pc/[r]_{g_2'g_1'}="2" \ar@{=>}"1";"2"|*+{h_2\alpha(g_2,h_1)} & \ast\text{.}}
\end{equation*}
Summarizing, one can go from smooth crossed modules to Lie 2-groups, and then to Lie 2-groupoids. 

\begin{example}\
\label{ex:2groups}
\begin{enumerate}[(i)]
\item
Let $A$ be an abelian Lie group. A smooth crossed module is defined by  $G=\lbrace 1 \rbrace$  and $H:= A$. This fixes the maps to $t(a):=1$ and $\alpha(1,a):=a$. Notice that axiom b) is  satisfied because $A$ is abelian. The associated Lie 2-group is denoted by $\mathcal{B} A$. Transport 2-functors with $\mathcal{BB}A$-structure play the role of \emph{abelian gerbes with connection}; see Section \ref{sec3_2}. 

\item
Let $G$ be a Lie group. A smooth crossed module is defined by  $H := G$, $t=\id$ and $\alpha(g,h)\df ghg^{-1}$. The associated Lie 2-group is  denoted by  $\mathcal{E}G$. This notation is devoted to the fact that the geometric realization of the nerve of the category $\mathcal{E}G$ yields the universal $G$-bundle $EG$. Transport 2-functors with $\mathcal{BE}G$-structure arise as the \emph{curvature} of transport functors; see Section \ref{sec5_1}.

\item
\label{ex:2groups:aut}
Let $H$ be a connected Lie group, so that the group of Lie group automorphisms of $H$ is again a Lie group $G:=\mathrm{Aut}(H)$. The definitions  $t(h)(x):=hxh^{-1}$ and $\alpha(\varphi,h):= \varphi(h)$ yield a smooth crossed module whose associated Lie 2-group is denoted by $\mathrm{AUT}(H)$, it is called the  \emph{automorphism 2-group} of $H$. Transport 2-functors with $\mathcal{B}\mathrm{AUT}(H)$-structure play the role \emph{non-abelian gerbes with connection}; see Section \ref{sec3_3}. 

\item
Let 
\begin{equation*}
\alxydim{}{1 \ar[r] & N \ar[r]^-{t} & H \ar[r]^{p} & G \ar[r] & 1}
\end{equation*}
be an  exact sequence of Lie groups, not necessarily central. There is a canonical action $\alpha$ of $H$ on $N$ defined by requiring
\begin{equation*}
t(\alpha(h,n)) = ht(n)h^{-1}\text{.}
\end{equation*}
This defines a smooth crossed module, whose associated Lie 2-group we  denote by $\mathfrak{N}$.  Transport 2-functors with $\mathcal{B}\mathfrak{N}$-structure correspond to (non-abelian) \emph{lifting gerbes}. They generalize the abelian lifting gerbes \cite{brylinski1,murray} for central extensions to arbitrary short exact sequences of Lie groups.  
\end{enumerate}
\end{example}






\subsubsection{Transgression to Loop Spaces}

Transport 2-functors on a smooth manifold $M$ induce interesting structure on the loop space $LM$. This comes from the fact that there is a canonical smooth functor
\begin{equation*}
\ell: \mathcal{P}_1(LM) \to \Lambda \mathcal{P}_2(M)
\end{equation*}
expressing  that a point in $LM$ is just a particular path in $M$, and that a path in $LM$ is just a particular bigon in $M$ \cite[Section 4.2]{schreiber5}. If $\mathrm{tra}: \mathcal{P}_2(M) \to T$ is a transport 2-functor, then the composition of $\ell$ with 
\begin{equation*}
\Lambda\mathrm{tra}: \Lambda \mathcal{P}_2(M) \to \Lambda_{\mathrm{tra}}T
\end{equation*}
yields a functor
\begin{equation*}
\mathscr{T}_{\mathrm{tra}} := \Lambda\mathrm{tra} \circ \ell: \mathcal{P}_1(LM) \to \Lambda_{\mathrm{tra}}T
\end{equation*}
that we call the \emph{transgression of $\mathrm{tra}$ to the loop space}. In order abbreviate the discussion of the functor $\mathscr{T}_{\mathrm{tra}}$ we make three simplifying assumptions:
\begin{enumerate}[(i)]

\item
We restrict our attention to the based loop  space $\Omega M$ (for some fixed base point) and identify $\mathscr{T}_{\mathrm{tra}}$ with its pullback along the embedding $\iota: \Omega M \to LM$.
 

\item 
We assume that there exists a surjective submersion $\pi:Y \to M$ for which $\mathrm{tra}$ admits smooth local trivializations  and for which $\Omega\pi:\Omega Y \to \Omega M$ is also a surjective submersion. 

\item
We assume that the target 2-category $T$ is strict, so that $\Lambda T$ is the target category of the functor $\mathscr{T}_{\mathrm{tra}}$.

\end{enumerate}

\begin{proposition}
\label{prop:trans}
Let $\mathrm{tra}: \mathcal{P}_2(M) \to T$ be a transport 2-functor with $\mathrm{Gr}$-structure  satisfying (ii) and (iii).
Then,
\begin{equation*}
\mathscr{T}_{\mathrm{tra}}: \mathcal{P}_1(\Omega M) \to \Lambda T
\end{equation*}
is a transport functor with $\Lambda\mathrm{Gr}$-structure.
\end{proposition}

\begin{proof}
Let $t: \pi^{*}\mathrm{tra} \to \mathrm{triv}_i$ be a $\pi$-local $i$-trivialization of $\mathrm{tra}$ for $\pi$ a surjective submersion satisfying (ii). A local trivialization $\tilde t$ of $\mathscr{T}_{\mathrm{tra}}$ is given by 
\begin{equation*}
\alxydim{}{\mathcal{P}_1(\Omega Y) \ar[d]_{\ell} \ar[r]^{(\Omega \pi)_{*}} & \mathcal{P}_1(\Omega M) \ar[d]^{\ell} \\ \Lambda \mathcal{P}_2(Y) \ar[d]_{\Lambda\mathrm{triv}} \ar[r]|{\pi_{*}} & \Lambda \mathcal{P}_2(M) \ar@{=>}[dl]|{\Lambda t} \ar[d]^{\Lambda\mathrm{tra}} \\ \Lambda \mathrm{Gr} \ar[r]_{\Lambda i} & \Lambda T}
\end{equation*}
in which the upper subdiagram is commutative on the nose. If $g: \pi_1^{*}\mathrm{triv}_i \to \pi_2^{*}\mathrm{triv}_i$ is the \pt\ in the smooth descent object $\ex{\pi}(\mathrm{tra},t,\mathrm{triv})$, and $\tilde g$ is the natural transformation in the descent object $\ex{\pi}(\mathscr{T}_{\mathrm{tra}}, \tilde t, \ell^{*}\Lambda \mathrm{triv})$ associated to the above trivialization, we find $\tilde g = \ell^{*}\Lambda g$. 
Since $\holo(g)$ is a transport 2-functor with $\Lambda\mathrm{Gr}$-structure, it has smooth Wilson lines \cite{schreiber3}: for a fixed point $\alpha\in Y^{[2]}$ there exists a smooth natural transformation $g': \pi_1^{*}\ell^{*}\Lambda\mathrm{triv} \to \pi_2^{*}\ell^{*}\Lambda\mathrm{triv}$ with $g=i(g')$. This shows that $\tilde g$ factors through a smooth natural transformation $\ell^{*}\Lambda g'$, so that $\mathscr{T}_{\mathrm{tra}}$ is a transport functor.
\end{proof}


Having in mind that transport functors correspond to fibre bundles with connection, Proposition \ref{prop:trans} shows that transport 2-functors on a manifold $M$ naturally induce fibre bundles with connection on the loop space $\Omega M$. In general, these are so-called groupoid bundles \cite{moerdijk, schreiber3}, whose structure groupoid is $\Lambda\mathrm{Gr}$. However, in the abelian case, i.e. $\mathrm{Gr}=\mathcal{BB}A$ for an abelian Lie group $A$, we have $\Lambda\mathrm{Gr} \cong \mathcal{B}A$ (see Lemma \ref{lem6} below), so that the transgression $\mathscr{T}_{\mathrm{tra}}$ is -- via Theorem \ref{th3} -- a principal $A$-bundle with connection over $\Omega M$. This fits well into Brylinski's picture of transgression \cite{brylinski1}.



\subsubsection{Curving and Curvature}

Suppose $\mathrm{tra}:\mathcal{P}_2(M) \to T$ is a transport 2-functor with $\mathcal{B}\mathfrak{G}$-structure, for $\mathfrak{G}$ some Lie 2-group coming from a smooth crossed module $(G,H,t,\alpha)$. Since such 2-functors are supposed to describe (non-abelian) gerbes with connection, we want to identify a \emph{3-form curvature}. Just as for (non-abelian) principal bundles, this curvature is only locally defined. 


First we need the following fact: if $\mathfrak{g}$ and $\mathfrak{h}$ denote the Lie algebras of the Lie groups $G$ and $H$, respectively, there is a bijection
\begin{equation}
\label{bij}
\bigset{3.2cm}{Smooth 2-functors\\$F: \mathcal{P}_2(X) \rightarrow \mathcal{B}\mathfrak{G}$} \cong 
\bigset{5.8cm}{Pairs $(A,B) \in \Omega^1(X,\mathfrak{g}) \times \Omega^2(X,\mathfrak{h})$ satisfying $t_{*}(B) = \mathrm{d}A + [A \wedge A]$}\text{,}
\end{equation}
where $t_{*}: \mathfrak{h} \to \mathfrak{g}$ is the differential of $t$.
This bijection is the lowest level of an equivalence of 2-categories that we will review in more detail in Section \ref{sec4_1}; see Theorem \ref{th1}. 


\begin{definition}
\label{def:curv}
Let $\mathrm{tra}: \mathcal{P}_2(M) \to T$ be a transport functor with $\mathcal{B}\mathfrak{G}$-structure over $M$, let $\pi\maps Y \to M$ be a surjective submersion, and let $(t,\mathrm{triv})$ be a $\pi$-local trivialization with smooth descent data.
\begin{enumerate}[(i)]

\item
The differential forms $A \in \Omega^1(Y,\mathfrak{g})$ and $B \in \Omega^2(Y,\mathfrak{h})$ that correspond to the smooth 2-functor $\mathrm{triv}$ under the above bijection, are called the \emph{1-curving} and the \emph{2-curving} of $\mathrm{tra}$. 
\item
The 3-form
\begin{equation*}
\mathrm{curv}(\mathrm{tra}) = \mathrm{d}B + \alpha_{*}(A \wedge B)\in\Omega^3(Y,\mathfrak{h})\text{,}
\end{equation*}
where $\alpha_{*}: \mathfrak{g} \times \mathfrak{h} \to \mathfrak{h}$ is the differential of the action $\alpha: G \times H \to H$ of the crossed module, is called the \emph{curvature} of $\mathrm{tra}$.


\end{enumerate}

\end{definition}

We recall that we  called a 2-functor $\mathrm{tra}:\mathcal{P}_2(M) \to T$ \emph{flat} if it factors through the projection $\mathcal{P}_2(M) \to \Pi_2(M)$ of thin homotopy classes of bigons to homotopy classes. The next proposition shows that this notion of flatness is equivalent to the vanishing of the curvature. 

\begin{proposition}
\label{prop3}
Suppose that the 2-functor $i:\mathcal{B}\mathfrak{G} \to T$ is injective on 2-morphisms.
A transport 2-functor $\mathrm{tra}:\mathcal{P}_2(M) \to T$ with $\mathcal{B}\mathfrak{G}$-structure is flat if and only if its local curvature 3-form $\mathrm{curv}(\mathrm{tra})\in\Omega^3(Y,\mathfrak{h})$ with respect to any smooth local trivialization vanishes.
\end{proposition}

\begin{proof}
We proceed in two parts. (a): $\mathrm{curv}(\mathrm{tra})$ vanishes if and only if $\mathrm{triv}$ is a flat 2-functor, and (b): $\mathrm{tra}$ is flat if and only if $\mathrm{triv}$ is flat. The claim (a) follows from Lemma A.11 in \cite{schreiber5}. To see (b) consider two bigons $\Sigma_1: \gamma \Rightarrow \gamma'$  and $\Sigma_2: \gamma \Rightarrow \gamma'$ in $Y$ which are smoothly homotopic so that they define the same element in $\Pi_2(Y)$. Suppose $\mathrm{tra}$ is flat and let $\Sigma := \Sigma_2^{-1} \bullet \Sigma_1$. Axiom (T2) for the trivialization $t$ is then
\begin{equation*}
\alxydim{@C=1.8cm@R=1.6cm}{t(y) \circ \pi^{*}\mathrm{tra}(\gamma) \ar@{=>}[r]^-{t(\gamma)} \ar@{=>}[d]_{\id_{t(y)}\circ \pi^{*}\mathrm{tra}(\Sigma)} & \mathrm{triv}_i(\gamma) \circ t(x) \ar@{=>}[d]^{\mathrm{triv}_i(\Sigma) \circ \id_{t(x)}} \\ t(y) \circ \pi^{*}\mathrm{tra}(\gamma) \ar@{=>}[r]_-{t(\gamma)} & \mathrm{triv}_i(\gamma) \circ t(x)}
\end{equation*}
and since $\pi^{*}\mathrm{tra}(\Sigma)=\id$ by assumption it follows that $\mathrm{triv}_i(\Sigma)=\id$, i.e. $\mathrm{triv}$ is flat. Conversely, assume that $\mathrm{triv}$ is flat. The latter diagram shows that  $\mathrm{tra}$ is then flat on all bigons in the image of $\pi_{*}$. This is actually enough: let $h: [0,1]^3 \to M$  be a smooth homotopy between two bigons $\Sigma_1$ and $\Sigma_2$ which are not in the image of $\pi_{*}$. Like explained in Appendix A.3 of \cite{schreiber5} the cube $[0,1]^3$ can be decomposed into small cubes such that $h$ restricts to smooth homotopies between small bigons that bound these cubes. The decomposition can be chosen so small that each of these bigons is contained in the image of $\pi_{*}$, so that $\mathrm{tra}$ assigns the same value to the source and the target bigon of each small cube. By 2-functorality of $\mathrm{tra}$, this infers $\mathrm{tra}(\Sigma_1) = \mathrm{tra}(\Sigma_2)$.
\end{proof}
