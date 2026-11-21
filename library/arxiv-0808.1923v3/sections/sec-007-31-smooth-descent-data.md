---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-007-31-smooth-descent-data
section_title: "Smooth Descent Data"
section_number: 3.1
pages: 12-15
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.655
latex_coverage_ratio: 0.987
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec:smoothdescent}

In this section we select a sub-2-category $\transsmooth{i}{2}{\mathrm{Gr}}$ of \emph{smooth descent data} in the 2-category $\trans{i}{\mathrm{Gr}}{2}$ of descent data described in Section \ref{sec:loctriv}.  If $(\mathrm{triv},g,\psi,f)$ is a descent object, we demand that the strict 2-functor $\mathrm{triv}: \mathcal{P}_2(Y) \to \mathrm{Gr}$ has to be smooth in the sense of Section \ref{sec3_1}, i.e. internal to diffeological spaces. Imposing smoothness conditions for the \pt\ $g$ and the modifications $\psi$ and $f$ is more subtle since they do not take  values  in the Lie 2-category $\mathrm{Gr}$ but in the 2-category $T$ which is not assumed to be a Lie 2-category.


Briefly, we proceed in the following two steps. We explain first how the  \pt
\begin{equation*}
g: \pi_1^{*}\mathrm{triv}_i \to \pi_2^{*}\mathrm{triv}_i
\end{equation*}
can be viewed as a certain functor $\holo(g)$ defined on $\mathcal{P}_1(Y^{[2]})$. Secondly,  we impose the  condition that $\mathscr{F}(g)$ is a transport functor. A little motivation might be the observation that $\holo(g)$  corresponds then (at least in some cases, by Theorem \ref{th3}) to a principal bundle with connection  over $Y^{[2]}$ -- one of the well-known ingredients of a (bundle) gerbe, see Sections \ref{sec3_2} and \ref{sec3_3}. 



Let us first explain in general how a \pt\ between two 2-functors can be viewed as a functor. We consider  2-functors $F$ and $G$  between 2-categories $S$ and $T$.
Since a \pt\ $\rho:F\to G$ assigns 1-morphisms in $T$ to objects in $S$ and 2-morphisms in $T$ to 1-morphisms in $S$, the general idea is to construct a category $S_{0,1}$ consisting of objects and 1-morphisms of $S$ and a category $\Lambda T$ consisting of 1-morphisms and 2-morphisms of $T$ such that $\rho$ yields a functor
\begin{equation*}
\holo(\rho): S_{0,1} \to \Lambda T\text{.}
\end{equation*}
We assume that $S$ is strict, so that forgetting its 2-morphisms produces a well-defined category $S_{0,1}$. The construction of  the category $\Lambda T$ is more involved. 

If $T$ is strict, the objects of $\Lambda T$ are the 1-morphisms of $T$. A morphism between objects $f\maps X_f \to Y_f$ and $g:X_g \to Y_g$ is a pair of 1-morphisms $x:X_f \to X_g$ and $y:Y_f \to Y_g$ and a 2-morphism
\begin{equation}
\label{36}
\alxydim{}{X_f \ar[r]^{x} \ar[d]_{f} & X_g \ar@{=>}[dl]|{\varphi} \ar[d]^{g} \\ Y_f \ar[r]_{y} & Y_g\text{.}}
\end{equation}
This gives indeed a category $\Lambda T$, whose composition is defined by putting the diagrams \erf{36} next to each other. Clearly, any strict 2-functor $f:T' \to T$ induces a functor $\Lambda f\maps\Lambda T' \to \Lambda T$. For a more detailed discussion of these constructions we refer the reader to Section 4.2 of \cite{schreiber5}.

 
Now let $\rho:F \to G$ be a \pt\ between two strict 2-functors from $S$ to $T$. Sending an object $X$ in $S$ to the 1-morphism $\rho(X)$ and sending a 1-morphism $f$ in $S$ to the 2-morphism $\rho(X)$ now yields a functor \begin{equation*}
\holo(\rho): S_{0,1} \to \Lambda T\text{.}
\end{equation*}
It respects the composition due to axiom (T1) for $\rho$ and the identities due to \cite[Lemma A.7]{schreiber6}. Moreover, a modification $\mathcal{A}:\rho_1\Rightarrow \rho_2$ defines a natural transformation $\holo(\mathcal{A})\maps \holo(\rho_1) \Rightarrow \holo(\rho_2)$, so that the result is a functor
\begin{equation}
\label{8}
\holo: \mathrm{Hom}(F, G) \to \mathrm{Funct}(S_{0,1},\Lambda T)
\end{equation} 
between the category of \pt s between $F$ and $G$ and the category of functors from $S_{0,1}$ to $\Lambda T$,
for $S$ and $T$ strict 2-categories and $F$ and $G$ strict 2-functors.




In case that the 2-category $T$ is not strict, the construction of $\Lambda T$ suffers from the fact that the composition is not longer associative.  The situation becomes treatable if one requires the objects $X_{f},Y_f$ and $X_g,Y_g$ and the 1-morphisms $x$ and $y$ in \erf{36} to be contained the image of a strict 2-category $T^{\mathrm{str}}$ under some 2-functor $i:T^{\mathrm{str}} \to T$. \begin{figure}[h]
\begin{equation*}
\alxydim{}{i(X) \ar[d]^{f} \\ i(Y)}
\quad\text{, }\quad
\alxydim{}{i(X_f) \ar[r]^{i(x)} \ar[d]_{f} & i(X_g) \ar@{=>}[dl]|{\varphi} \ar[d]^{g} \\ i(Y_f) \ar[r]_{i(y)} & i(Y_g)}
\quad\text{ and }\quad
\alxydim{}{i(X_f) \ar@/^3.2pc/[rr]^{i(x' \circ x)}="1" \ar@{=>}"1";[r]|-{c_{x,x'}^{-1}} \ar[r]^{i(x)} \ar[d]_{f} & i(X_g) \ar@{=>}[dl]|{\varphi} \ar[d]^{g} \ar[r]^{i(x')} & i(X_h) \ar[d]^{h} \ar@{=>}[dl]|{\varphi'} \\ i(Y_f) \ar@/_3.2pc/[rr]_{i(y'\circ y)}="2" \ar@{=>}[r];"2"|{c_{y,y'}} \ar[r]_{i(y)} & i(Y_g) \ar[r]_{i(y')} & i(Y_h)\text{.}}
\end{equation*}
\caption{Objects, morphisms and the composition of the category $\Lambda_iT$ (the diagram on the right hand side ignores the associators and the bracketing of 1-morphisms). Here, $c$ is the compositor of the 2-functor $i$.}
\label{fig1}
\end{figure} The result is a category $\Lambda_iT$, in which the associativity of the composition is restored by axiom (F3) on the compositor of the 2-functor $i$. We omit a more formal definition and refer the reader to Figure \ref{fig1} for an illustration. 
For any 2-functor $f: T \to T'$, a functor
\begin{equation*}
\Lambda F: \Lambda_i T \to \Lambda_{F \circ i} T'
\end{equation*}
is induced by applying $f$ to all involved objects, 1-morphisms, and 2-morphisms.

We may now consider strict 2-functors $F$ and $G$ from $S$ to $T^{\mathrm{str}}$. Then, the functor \erf{8} generalizes straightforwardly to a functor
\begin{equation*}
\holo: \mathrm{Hom}(i \circ F, i \circ G) \to \mathrm{Funct}(S_{0,1},\Lambda_i T)
\end{equation*}
between the category of \pt s\ between $i\circ F$ and $i\circ G$ and the category of functors from $S_{0,1}$ to $\Lambda_i T$. The following lemma follows directly from the definitions. 



\begin{lemma}
\label{lem:F}
The functor $\mathscr{F}$ has the following properties:
\begin{enumerate}[(i)]
\item 
\label{lem:F9}
It is natural with respect to strict 2-functors $f:S' \to S$ in the sense that the diagram
\begin{equation*}
\alxydim{@C=1.5cm}{\mathrm{Hom}(i \circ F,i\circ G) \ar[d]_{f^{*}} \ar[r]^-{\holo} &  \mathrm{Funct}(S_{0,1},\Lambda_i T) \ar[d]^{f^{*}} \\ \mathrm{Hom}(i \circ F \circ f,i\circ G \circ f) \ar[r]_-{\holo} & \mathrm{Funct}(S'_{0,1},\Lambda_i T)}
\end{equation*}
is strictly commutative.

\item
\label{lem:F50}
It preserves the composition of pseudonatural transformations in the sense that if $F,G,H\maps S \to T^{\mathrm{str}}$ are three strict 2-functors, the diagram
\begin{equation*}
\alxydim{@C=1.1cm}{\mathrm{Hom}(i\! \circ\! G,i\!\circ\! H)\! \times \!\mathrm{Hom}(i \!\circ \!F,i\!\circ\! G) \ar[d]_{\circ} \ar[r]^-{\holo \times \holo} & \mathrm{Funct}(S_{0,1},\Lambda_i T) \!\times\! \mathrm{Funct}(S_{0,1},\Lambda_i T) \ar[d]^{\otimes} \\ \mathrm{Hom}(i \circ H,i \circ F) \ar[r]_-{\holo} & \mathrm{Funct}(S_{0,1},\Lambda_i T)}
\end{equation*}
is commutative. 


\end{enumerate}
\end{lemma}

In Lemma \ref{lem:F} \erf{lem:F50}
the symbol $\otimes$ has the following meaning. The composition of morphisms in $\Lambda_iT$ was defined by putting the diagrams \erf{36} next to each other as shown in Figure \ref{fig1}. But one can also put the diagrams of appropriate morphisms on top of each other, provided that the arrow on the bottom of the upper one coincides with the arrow on the top of the lower one. This is indeed the case for the morphisms in the image of composable \pt s under $\holo \times \holo$, so that the diagram in (ii) makes sense. In a more formal context, the tensor product $\otimes$ can be discussed in the formalism of \emph{weak double categories}, but we will not stress this point. 


In the following discussion the strict 2-category $S$ is the path  2-groupoid of some smooth manifold, $S=\mathcal{P}_2(X)$. Notice that  $S_{0,1}=\mathcal{P}_1(X)$ is then the path groupoid of $X$. The 2-category $T$ is the target 2-category, and the strict 2-category $T^{\mathrm{str}}$ is the Lie 2-groupoid $\mathrm{Gr}$.  

Let $(\mathrm{triv},g,\psi,f)$ be a descent object in the  descent 2-category $\trans{i}{\mathrm{Gr}}{2}$.  The \pt\ $g:\pi_1^{*}\mathrm{triv}_i \to \pi_2^{*}\mathrm{triv}_i$ induces a functor
\begin{equation*}
\holo(g): \mathcal{P}_1(Y^{[2]}) \to \Lambda_i T\text{.}
\end{equation*}
In order to impose the condition that $\mathscr{F}(g)$ is a transport functor, we will use the functor
\begin{equation*}
\Lambda i: \Lambda \mathrm{Gr} \to \Lambda_i T
\end{equation*}
as its structure Lie groupoid. 
Further, the modification $\psi:\id_{\mathrm{triv}_i} \to \Delta^{*}g$ induces via Lemma \ref{lem:F} \erf{lem:F9} a natural transformation
\begin{equation*}
\holo(\psi):\holo(\id_{\mathrm{triv}_i}) \Rightarrow \Delta^{*}\holo(g)\text{.}
\end{equation*}
Finally, the modification $f$ induces via Lemma \ref{lem:F} \erf{lem:F9} and  \erf{lem:F50} a natural transformation
\begin{equation*}
\holo(f): \pi_{23}^{*}\holo(g) \otimes \pi_{12}^{*}\holo(g) \Rightarrow \pi_{13}^{*}\holo(g)\text{.}
\end{equation*}


\begin{definition}
A descent object $(\mathrm{triv},g,\psi,f)$ is called \emph{smooth} if the following  conditions are satisfied:
\begin{enumerate}[(i)]
\item
the 2-functor $\mathrm{triv}\maps\mathcal{P}_2(Y) \to \mathrm{Gr}$ is smooth.

\item
the functor $\holo(g)$ is a transport functor with $\Lambda \mathrm{Gr}$-structure.

\item
the natural transformations $\mathscr{F}(\psi)$ and $\mathscr{F}(f)$ are morphisms between transport functors. 
\end{enumerate}

\end{definition}

In the same way we qualify smooth descent 1-morphisms and descent 2-morphisms. A descent 1-morphism 
\begin{equation*}
(h,\varepsilon):(\mathrm{triv},g,\psi,f) \to (\mathrm{triv}',g',\psi',f')
\end{equation*}
is converted into a functor
\begin{equation*}
\holo(h): \mathcal{P}_1(Y) \to \Lambda_iT
\end{equation*}
and a natural transformation
\begin{equation*}
\holo(\varepsilon): \pi_2^{*}\holo(h) \otimes \holo(g) \Rightarrow \holo(g') \otimes \pi_1^{*}\holo(h)\text{.}
\end{equation*}
We say that $(h,\epsilon)$ is \emph{smooth}, if  $\holo(h)$ is a  transport functor
with $\Lambda\mathrm{Gr}$-structure and   $\holo(\epsilon)$
is a 1-morphism between transport functors.
A descent 2-morphism $E: (h,\varepsilon) \Rightarrow (h',\varepsilon')$ is converted into a natural transformation
\begin{equation*}
\holo(E): \holo(h) \Rightarrow \holo(h')\text{,}
\end{equation*}
and we say that $E$ is \emph{smooth}, if  $\holo(E)$
is a 1-morphism between transport functors. 
We claim two obvious properties of smooth descent data:
\begin{enumerate}[(i)]

\item 
Compositions of smooth descent 1-morphisms and smooth descent 2-morphisms are again smooth, so that smooth descent data forms a sub-2-category of $\trans{i}{\mathrm{Gr}}{2}$, which we denote by $\transsmooth{i}{2}{\mathrm{Gr}}$. 


\item
Pullbacks of smooth descend objects, 1-morphisms and 2-morphisms along refinements of surjective submersions are again smooth, so that the direct limit
\begin{equation*}
\transsmoothpi{i}{2}{\mathrm{Gr}}{}_M := \lim_{\overrightarrow{\pi}} \transsmooth{i}{2}{\mathrm{Gr}}
\end{equation*}
is a well-defined sub-2-category of $\mathfrak{Des}^2(i)_M$.

\end{enumerate}
In Section \ref{sec4} we show that the 2-category $\transsmoothpi{i}{2}{\mathrm{Gr}}{}_M$ of smooth descent data becomes nice and familiar upon choosing concrete examples for the structure 2-groupoid $i:\mathrm{Gr} \to T$.







\subsection{Transport 2-Functors}

\label{sec:def}

Now we come to the central definition of this paper.

\begin{definition}
Let $M$ be a smooth manifold, $\mathrm{Gr}$  be a strict Lie 2-groupoid,  $T$  be a 2-category and  $i:\mathrm{Gr} \to T$  be a 2-functor. 
A \emph{transport 2-functor on $M$ with values in $T$ and with $\mathrm{Gr}$-structure} is a 2-functor
\begin{equation*}
\mathrm{tra}:\mathcal{P}_2(M) \to T
\end{equation*}
such that there exists a surjective submersion $\pi:Y \to M$ and a $\pi$-local $i$-trivialization $(\mathrm{triv},t)$ whose  descent object $\ex{\pi}(\mathrm{tra},\mathrm{triv},t)$ is smooth. 
\end{definition}


A 1-morphism between transport 2-functors $\mathrm{tra}$ and $\mathrm{tra}'$ is a \pt\ 
 $A\maps \mathrm{tra} \to \mathrm{tra}'$
such that there exists a surjective submersion $\pi$ together with $\pi$-local $i$-trivializations of $\mathrm{tra}$ and $\mathrm{tra}'$ for which the descent 1-morphism $\ex{\pi}(A)$ is smooth. 2-morphisms are defined in the same way. 
Transport 2-functors $\mathrm{tra}:\mathcal{P}_2(M) \to T$ with $\mathrm{Gr}$-structure, 1-morphisms, and 2-morphisms form a sub-2-category of the 2-category of locally $i$-trivializable 2-functor $\mathrm{Funct}_i(\mathcal{P}_2(M),T)$, and we  denote this sub-2-category by $\transport{}{2}{\mathrm{Gr}}{T}$. We emphasize that being a transport 2-functor is a property, not additional structure. In particular, no surjective submersion or open cover  is contained in the structure of a transport 2-functor: they are manifestly \emph{globally defined} objects. 

We want to establish an equivalence between transport 2-functors and their smooth descent data. In order to achieve this equivalence we have to make a slight assumption on the 2-functor $i$. We call a 2-functor $i:\mathrm{Gr} \to T$ \emph{full and faithful}, if it induces an equivalence on Hom-categories. In particular, $i$ is full and faithful if it is an equivalence of 2-categories, which is in fact true in all examples we are going to discuss.


\begin{theorem}
\label{th:locglobeqsmooth}
\label{th4}
Let $M$ be a smooth manifold, and let $i \maps \mathrm{Gr} \to T$ be a full and faithful 2-functor. Then, the equivalence of Theorem \ref{th:locglobequiv} restricts to an equivalence
\begin{equation*}
\transport{}{2}{\mathrm{Gr}}{T} \cong \mathfrak{Des}^2(i)_M^{\infty}
\end{equation*}
between transport 2-functors and their smooth descent data.
\end{theorem}

Theorem \ref{th:locglobeqsmooth} is proved by the following two lemmata. As an intermediate step we introduce -- for a surjective submersion $\pi$ -- the sub-2-category $\loctrivfunctsmooth{i}{}{\pi}{2}$ of $\loctrivfunct{i}{}{2}$ as the preimage of $\transsmooth{i}{2}{}$ under the 2-functor $\ex{\pi}$. 

\begin{lemma}
\label{lem9}
The 2-functor $\ex{\pi}$ restricts to an equivalence of 2-categories
\begin{equation*}
\loctrivfunctsmooth{i}{}{\pi}{2} \cong \mathfrak{Des}^2_{\pi}(i)^{\infty}\text{.}
\end{equation*}
\end{lemma}

\begin{proof}
It is clear that $\ex\pi$ restricts properly. Recall from \cite[Section 3]{schreiber6}  that inverse to $\ex\pi$ is a \quot{reconstruction} 2-functor $\mathrm{Rec}_{\pi}$. In order to prove that the image of the restriction of $\mathrm{Rec}_{\pi}$ is contained in $\loctrivfunctsmooth{i}{}{\pi}{2}$ we have to check that $\ex{\pi} \circ \mathrm{Rec}_{\pi}$ restricts to an endo-2-functor of $\transsmooth{i}{2}{}$. In the proof of \cite[Lemma 4.1.2]{schreiber6} we have explicitly computed this 2-functor, and by inspection of the corresponding expressions one recognizes its image as smooth descent data.


The second part of the proof is to show that the components of two pseudonatural equivalences  $\rho:\ex{\pi} \circ \mathrm{Rec}_{\pi} \to \id$ and $\eta: \id \to \mathrm{Rec}_{\pi} \circ \ex{\pi}$ that establish the equivalence of \cite[Proposition 4.1.1]{schreiber6} are in $\mathfrak{Des}^2_{\pi}(i)^{\infty}$ and $\loctrivfunctsmooth{i}{}{\pi}{2}$, respectively. For the transformation $\rho$, this is again by inspection of the formulae in the proof of  \cite[Lemma 4.1.2]{schreiber6}. For the transformation $\eta$, we suppose $F$ is a 2-functor with a $\pi$-local $i$-trivialization $(t,\mathrm{triv})$ with smooth descent data $(\mathrm{triv},g,\psi,f)$. We have to prove that the descent 1-morphism $\ex\pi(\eta(F,t,\mathrm{triv}))$ is smooth. Indeed, according to the definition of $\eta$ given in the proof of \cite[Lemma 4.1.3]{schreiber6} it is given by the \pt\ $g$  and a modification composed from the modifications $f$ and $\psi$. The descent object is by assumption smooth, and so is $\eta(F)$. The same argument shows that the component $\eta(A)$ of a \pt\ $A:F \to F'$ with smooth descent data is smooth. 
\end{proof}

Next we go to the direct limit
\begin{equation*}
\loctrivfunctsmooth{i}{}{}{2}_M := \lim_{\overrightarrow{\pi}} \loctrivfunctsmooth{i}{}{\pi}{2}\text{.}
\end{equation*}
The equivalence of Lemma \ref{lem9} induces an equivalence
\begin{equation*}
\mathrm{Ex} : \loctrivfunctsmooth{i}{}{}{2}_M \to \mathfrak{Des}^2_{\pi}(i)^{\infty}
\end{equation*}
in the direct limit. Next we show that the 2-categories $\loctrivfunctsmooth{i}{}{}{2}_M$ and $\transport{}{2}{\mathrm{Gr}}{T}$  are equivalent. We have an evident 2-functor
\begin{equation*}
v^{\infty}:\loctrivfunctsmooth{i}{}{}{2}_M \to \transportX{}{2}{\mathrm{Gr}}{T}
\end{equation*}
induced by forgetting the chosen trivialization. 

\begin{lemma}
Under the assumption that the 2-functor $i$ is full and faithful,
the 2-functor $v^{\infty}$
is an equivalence of 2-categories. 
\end{lemma} 

\begin{proof}
It is clear that an inverse functor $w^{\infty}$ takes a given transport 2-functor and picks some smooth local trivialization for some surjective submersion $\pi:Y\to M$. It follows immediately that $v^{\infty} \circ w^{\infty}=\id$. It remains to construct a pseudonatural equivalence $\id\cong w^{\infty} \circ v^{\infty}$, i.e. a 1-isomorphism 
\begin{equation*}
A: (\mathrm{tra},\pi,\mathrm{triv},t) \to (\mathrm{tra},\pi',\mathrm{triv}',t')
\end{equation*}
in $\loctrivfunctsmooth{i}{}{}{2}_M$, where the original $\pi$-local trivialization $(\mathrm{triv},t)$ has been forgotten and replaced by a new $\pi'$-local trivialization $(\mathrm{triv}',t')$. But since the 1-morphisms in $\loctrivfunctsmooth{i}{}{}{2}_M$ are just \pt\ between the 2-functors ignoring the trivializations,  we only have to prove that the identity \pt
\begin{equation*}
A:=\id_{\mathrm{tra}}: \mathrm{tra} \to \mathrm{tra}
\end{equation*}
of a transport 2-functor $\mathrm{tra}$ has smooth descent data $(h,\varepsilon)$ with respect to \textit{any} two  trivializations $(\pi,\mathrm{triv},t)$ and $(\pi',\mathrm{triv}',t')$. 

The first step is to choose a refinement $\zeta: Z \to Y \times_M Y'$ of the common refinement of the to surjective submersions. One can choose $Z$ such that is has contractible connected components. If $c: Z \times[0,1] \to Z$ is such a contraction, it defines for each point $z\in Z$ a path $c_z: z \to z_k$ that moves $z$ to the distinguished point $z_k$ to which the component of $Z$ that contains $z$ is contracted. It further defines for each path $\gamma:z_1 \to z_2$ a bigon $c_{\gamma}:\gamma \Rightarrow c_{z_2}^{-1} \circ c_{z_1}$. Axiom (T2) for the pseudonatural transformation 
\begin{equation*}
h:=t' \circ \bar t: \mathrm{triv}_i \to \mathrm{triv}_i'
\end{equation*}
applied to the bigon $c_{\gamma}$ yields the commutative diagram
\begin{equation*}
\alxydim{@C=2.4cm@R=1.3cm}{h(z_2) \circ \mathrm{triv}_i(\gamma) \ar@{=>}[r]^-{h(\gamma)} \ar@{=>}[d]_{\id\circ \mathrm{triv}_i(c_{\gamma})} & \mathrm{triv}_i'(\gamma) \circ h(z_1) \ar@{=>}[d]^{\mathrm{triv}_i'(c_{\gamma}) \circ \id} \\ h(z_2) \circ \mathrm{triv}_i(c_{z_2}^{-1} \circ c_{z_1}) \ar@{=>}[r]_-{h(c_{z_2}^{-1}\circ c_{z_1})} & \mathrm{triv}_i'(c_{z_2}^{-1}\circ c_{z_1}) \circ h(z_1)\text{.}}
\end{equation*}
Notice that the 1-morphisms $h(z_j): \mathrm{triv}_i(z_j) \to \mathrm{triv}_i'(z_j)$ have by assumption preimages $\kappa_j: \mathrm{triv}(z_j) \to \mathrm{triv}'(z_j)$ under $i$ in $\mathrm{Gr}$, and that the 2-morphism $h(c_{z_2}^{-1}\circ c_{z_1})$ also has a preimage $\Gamma$ in $\mathrm{Gr}$. Thus,
\begin{equation*}
h(\gamma) = i \left ( (\mathrm{triv}'(c_{\gamma}) \circ \id)^{-1} \bullet \Gamma \bullet (\id \circ \mathrm{triv}(c_{\gamma})) \right )\text{.}
\end{equation*}
This is nothing but the Wilson line $\mathcal{W}^{\holo(h),\Lambda i}_{z_1,z_2}$ of the functor $\holo(h)$ and it is smooth since $\mathrm{triv}$ and $\mathrm{triv}'$ are smooth 2-functors. Hence, by Theorem 3.12 in \cite{schreiber3}, $\holo(h)$ is a transport functor with $\Lambda \mathrm{Gr}$-structure. 

It remains to prove that the modification  $\varepsilon: \pi_2^{*}h \circ g \Rightarrow g' \circ \pi_1^{*}h$
induces a morphism $\holo(\varepsilon)$ of transport functors. This simply follows from the general fact that under the assumption that the functor $i: \mathrm{Gr} \to T$ is full, every natural transformation $\eta$ between transport functors with $\mathrm{Gr}$-structure is a morphism of transport functors. We have not stated that explicitly in \cite{schreiber3} but it can easily be deduced from the naturality conditions on trivializations $t$ and $t'$ and on $\eta$, evaluated for paths with a fixed starting point. \end{proof}

With Theorem \ref{th4} we have established an equivalence between globally defined transport 2-functors and locally defined smooth descent data. In Section \ref{sec4} we will identify smooth descent data with various models of gerbes with connections. Under this identifications, Theorem \ref{th4} describes the relation between these gerbes with connections and their parallel transport.
