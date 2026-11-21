---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-002-11-stratified-spaces
section_title: "Stratified spaces"
section_number: 1.1
pages: 6-14
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.955
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
\label{sec.stratified-spaces}

Before defining \emph{conically smooth} stratified spaces which occupy this work, we first review the baseline topological notions.
We will regard a poset $P$ as a topological space with closed sets $P_{\leq p}$, for each element $p\in P$.
A {\it stratified topological space indexed by a poset $P$} is a paracompact Hausdorff topological space $X$ with a continuous map $X\ra P$.
For many purposes, the indexing poset $P$ can be taken to be the totally ordered set $[n]=\{0<1<\ldots <n\}$, where $n$ is the maximal dimension of a neighborhood of a point in $X$.
A \emph{stratified topological space} $X$ is a stratified topological space indexed by a poset $P$ (typically omitted from the notation).
The {\it stratum} $X_p\subset X$ is the inverse image of the element $p\in P$.
The \emph{depth} of a stratified topological space is the depth of its stratifying poset, by which we mean the maximum among lengths of strictly increasing sequences, should it exist.
A map between stratified topological spaces $X\ra Y$ is a commutative diagram of topological spaces
\[
\xymatrix{
X\ar[r]\ar[d]&Y \ar[d]\\
P\ar[r]& Q}
\]
where $P$ and $Q$ are the indexing posets for $X$ and $Y$. Such maps are closed under composition, so this forms a category.
We say such a map is an \emph{open embedding} if $X\ra Y$ is an open embedding between topological spaces.

\begin{example}
We observe an essential operation for generating new stratified topological spaces from old ones: taking cones. First, for $P$ is a poset, then the left-cone $P^\tl$ on $P$ is the poset defined by adding a new minimum element to $P$.
Note an identification $[n]^\tl = [n+1]$. For $X$ a stratified topological space indexed by $P$, then the open cone on $X$,
\[
\sC(X):=\{0\} \underset{\{0\}\times X}\coprod [0,\infty)\times X \longrightarrow \{0\} \underset{\{0\}\times P}\amalg [1]\times P = P^{\tl}~,
\]
is a stratified topological space indexed by $P^\tl$. 
Note that the cone $\sC(X)$ carries a natural action by multiplication of the nonnegative reals $\RR_{\geq 0}$, by scaling in the cone coordinate.
Note also that the stratifying poset $P^{\tl}$ has strictly greater depth than the poset $P$, provided the latter exists.
\end{example}

The category of {\it $C^0$ stratified space} is the smallest full subcategory of stratified topological spaces characterized by the following properties:

	\begin{enumerate}
	\item The empty set $\emptyset$ is a $C^0$ stratified space indexed by the empty poset.
	\item If $X$ is a $C^0$ stratified space and both $X$ and its indexing poset $P$ are compact, then the open cone $\sC(X)$ is a $C^0$ stratified space.
	\item If $X$ and $Y$ are $C^0$ stratified spaces, then the product stratified space $X\times Y$ is a $C^0$ stratified space. 
	\item  If $X$ is a $C^0$ stratified space and $(U \to P_{|U}) \to (X \to P)$ is an open embedding, then $(U \to P_{|U})$ is a $C^0$ stratified space.
	\item  If $X$ is a stratified topological space admitting an open cover by $C^0$ stratified spaces, then $X$ is a $C^0$ stratified space.
	\end{enumerate}	
Observe these examples of $C^0$ stratified spaces:
\begin{itemize}
\item a singleton, $\ast= (\ast \to \ast)$;
\item a half-open interval, $[0,\infty) = \bigl([0,\infty)\to [1]\bigr)$, with stratification such that the $0$-stratum is precisely $\{0\}$;
\item Euclidean spaces, $\RR^i = (\RR^i\to \ast)$;
\item any $C^0$ manifold.  

\end{itemize}

We now add a {\it conical smoothness} condition to our stratifications. The assumption of conical smoothness will be present throughout this work. This is, unfortunately and perhaps ineluctably, an inductive definition.
The induction is on the \emph{depth} of the stratifying poset.

A \emph{conically smooth stratified space}, or \emph{stratified space} for short, is a $C^0$ stratified space $X$ that is equipped with a \emph{conically smooth atlas}
\[
\Bigl\{\RR^{i_\alpha}\times \sC(Z_\alpha) \hookrightarrow X\Bigr\}_\alpha
\]
by \emph{basics}.
We now explain these terms.
Each $Z_\alpha$ is a compact stratified space of depth strictly less than that of $X$; so we assume that we have already defined what it means for $Z_\alpha$ to be equipped with a conically smooth atlas.
In general, a \emph{basic} is the data of a non-negative integer $i$ and a compact stratified space $Z$; together, these data define the $C^0$ stratified space $\RR^i\times \sC(Z)$, which might also be referred to as a \emph{basic} when the conically smooth atlas on $Z$ is understood.
Note that, for $P$ the stratifying poset of $Z$, the stratifying poset of $\RR^i\times \sC(Z)$ is $P^{\tl}$; the \emph{cone-locus} of this basic is the stratum $\RR^i = \RR^i\times \ast$, which is that indexed by the adjoined minimum.
Continuing toward our definition of a stratified space, a \emph{conically smooth atlas} is a collection of basics openly embedding as $C^0$ stratified spaces into $X$.  This collection satisfies three conditions: 
\begin{enumerate}
\item This collection of open embeddings forms a basis for the topology of $X$, in particular it forms an open cover of $X$.
\item The \emph{transition maps}, by which we mean the inclusions of open embeddings $\RR^i\times \sC(W) \hookrightarrow \RR^j\times \sC(Z)$ over $X$, are \emph{conically smooth}, which we explain momentarily.
\item This collection is maximal with respect to (1) and (2).  
\end{enumerate}
To complete our definition of a stratified space, it remains to explain the condition for an open embedding between basics to be \emph{conically smooth}.
So consider an $C^0$ open embedding $f\colon \RR^i\times \sC(Y) \hookrightarrow \RR^j\times \sC(Z)$ between basics.
This open embedding $f$ is \emph{conically smooth} in the sense of~\S3.3 of~\cite{aft1} if the following conditions are satisfied.
\begin{itemize}
\item {\bf Away from the cone-locus:}
Each element of the atlas $\psi\colon \RR^k\times \sC(W) \hookrightarrow Y$ determines a composite open embedding $\RR^i\times(0,\infty)\times \RR^k \times \sC(W) \hookrightarrow \RR^i\times \sC(Y) \hookrightarrow \RR^j\times \sC(Z)$.
By way of a smooth identification $(0,\infty)\cong \RR$, we recognize the domain of this composition as a basic.  
Using that $f$ is an open embedding between stratified topological spaces, necessarily this is the data of an open embedding $f\psi\colon \RR^{i+1+k}\times \sC(W) \hookrightarrow \RR^j\times \sC(Z)\smallsetminus \RR^j$ to the complement of the cone-locus.  
As so, for each such $\psi$, the condition of \emph{conical smoothness} requires this open embedding $f\psi$ is a member of the atlas of the target, which carries meaning via the induction in the definition of a stratified space.


\item {\bf Along the cone-locus:}
Should the preimage of the cone-locus be empty, then the above point entirely stipulates the conical smoothness condition on $f$.  
So suppose the preimage of the cone-locus is not empty.
Using that $f$ is an open embedding between stratified topological spaces, upon representing the values of $f = \bigl[(f_{\parallel},f_r,f_\theta)\bigr]$ as coordinates, then $f_r(p,0,y) = 0$ for all $(p,y)\in \RR^i\times Y$.  
For $0< k <\infty$, the condition that $f$ is \emph{conically $C^k$ (along the cone-locus)} requires the assignment
\begin{equation}\label{derivative}
(p,v,s,y)~\mapsto~\underset{t\to0^+} {\sf lim} \Bigl[\bigl(\frac{f_{\parallel}(p+tv,ts,y) - f_{\parallel}(p,0,y)}{t}, \frac{f_r(p+tv,ts,y)}{t}, f_\theta(p+tv,ts,y) \bigr)\Bigr] 
\end{equation}
to be defined as a map $D_{\parallel}f\colon T\RR^i\times \sC(Y) \to T\RR^j\times \sC(Z)$, required to be conically $C^{k-1}$ along the cone-locus (which carries meaning via induction on $k$).  
The condition of \emph{conical smoothness} requires that $f$ is conically $C^k$ for all $k\geq 0$.  
\end{itemize}


Outlined above is a definition of a stratified space, in the sense of~\cite{aft1}.  
We now, more briefly, outline the definition of a \emph{conically smooth} map between two; the assumption of conical smoothness on maps between stratified spaces will be present throughout this work, unless otherwise stated.  
Like the definition of a stratified space, a conically smooth map between two stratified spaces is offered by induction on depth.  
For $X$ and $Y$ stratified spaces, a map $f\colon X\to Y$ between their underlying stratified topological spaces is \emph{conically smooth} if, for each pair of basic charts $\phi\colon \RR^i\times \sC(Y) \hookrightarrow X$ and $\psi\colon \RR^j\times \sC(Z)\hookrightarrow Y$ for which there is a containment $f(\phi(\RR^i)) \subset \psi(\RR^j)$ of the images of the cone-loci, the map $\psi^{-1}\circ f \circ \phi\colon \RR^i\times \sC(Y) \to \RR^j\times \sC(Z)$ is \emph{conically smooth}.
This latter use of the term means conically smooth \emph{away from the cone-locus}, which can be ensured to carry meaning via induction on depth, and conically smooth \emph{along the cone-locus} which means $f$ abides by expression~(\ref{derivative}).  



\begin{example}
Note that smooth manifolds are precisely those stratified spaces that have no strata of positive codimension.
If $g:M\ra N$ is a smooth map between compact smooth manifolds, then the map of cones $\sC(g):\sC(M)\ra \sC(N)$ is conically smooth. If additionally $h:\RR^i \ra \RR^j$ is a smooth map between Euclidean spaces, then the product map $h\times \sC(g): \RR^i \times \sC(M)\ra \RR^j\times \sC(N)$ is again conically smooth.
\end{example}
Let $f\colon X\to Y$ be a map between stratified spaces.
We single out three important classes of conically smooth maps:
\begin{itemize}
\item Say $f$ is an \emph{embedding} if it is an isomorphism onto its image, and that it is an \emph{open embedding} if it is an embedding and it is an open map.  
\item Say $f$ is a \emph{refinement} if it is a homeomorphism of underlying topological spaces, and its restriction to each stratum of $X$ is an embedding.  
\item Say $f$ is a \emph{constructible bundle} if the following is true:
\begin{itemize}
\item[~]
Let $Y \to Q$ be the stratification of $Y$.
Then for each $q\in Q$, the restriction to the $q$-stratum $f_|\colon X_{|f^{-1}Y_q} \to Y_q$ is a fiber bundle of stratified spaces. 
\end{itemize}
\end{itemize}
\noindent
Unlike in the preceding definitions, for this next notion of {\it weak} constructibility the map $f$ does not preserve the stratification (i.e., it does not lie over a map of posets).

\begin{itemize}
\item Say a continuous map $f\colon X \to Y$ between the underlying topological spaces of stratified spaces is a \emph{weakly constructible bundle} if there is a diagram among stratified spaces $X\xla{r} \w{X} \xra{\ov{f}} Y$, with $r$ a refinement and $\ov{f}$ a constructible bundle, for which there is an equality between maps of underlying topological spaces: $\ov{f} = f\circ r$.  
\end{itemize}
Conically smooth maps compose, as do those that are open embeddings, thereby yielding the pair of categories
\[
\stratd~\supset~\snglrd~.
\]
The category $\stratd$ admits finite products, and so we regard it as enriched over the Cartesian category $\Fun(\stratd^{\op},\Set)$ of set-valued presheaves on itself through the expression 
\[
\Map_{\stratd}(X,Y) \colon Z\mapsto \stratd_{/Z}(X\times Z, Y\times Z)
\]
where the subscript ${}_{/Z}$ indicates those maps that commute with projecting to $Z$.  
Restricting along the standard cosimplicial object $\Delta^\bullet_e\colon \bDelta \longrightarrow \stratd$ given by $[p]\mapsto \{[p]\xra{t}\RR\mid \sum_{i\in [p]} t_i = 1\}$, gives a natural enrichment of $\stratd$, and thereafter of $\snglrd$, over simplicial sets.
In~\cite{aft1} we show that these enrichments factors as a $\Kan$-enrichments.
In a standard manner, we obtain $\infty$-categories
\[
\snglr\qquad\text{ and }\qquad \Strat
\]
of stratified spaces and \emph{spaces} of open embeddings among them, and respectively of conically smooth maps among them.   
Manifestly, there are natural functors $\snglrd \to \snglr$ and $\stratd \to \Strat$.
There is a full subcategory and an $\infty$-subcategory,
\[
\iota \colon \bscd~\subset~\snglrd\qquad\text{ and }\qquad \iota \colon \bsc~\subset~\snglr
\]
consisting of the \emph{basics}.  
A key result is that the functor $[-]\colon \bsc\to [\bsc]$ to the poset of isomorphism classes is \emph{conservative} (i.e., it does not create isomorphisms), which has immense consequences that are specific to the set-up herein. (See Theorem 4.3.1 of~\cite{aft1}.)

The \emph{tangent classifier} is the restricted Yoneda functor
\[
\snglr\xra{~j~} \Psh(\snglr)\xra{~\iota^\ast~} \Psh(\bsc)~,\qquad X\mapsto \bigl({\sf Entr}(X)\xra{\tau_X} \bsc\bigr)
\]
where, here, we have taken the model for presheaves on $\infty$-categories as \emph{right fibrations}.  
Specifically, each stratified space $X$ determines an $\infty$-category ${\sf Entr}(X):= \bsc_{/X}$ over $\bsc$.
(A key result in~\cite{aft1} is that ${\sf Entr}(X)$ is identified as the \emph{enter-path category} of the stratified space $X$, though we do not explain this result here for we do not use it.)
Imitating the notion of a tangential structure in differential topology, we define a \emph{category of basics} as a right fibration
\[
\cB ~=~(\cB \to \bsc)
\]
and declare a $\cB$-manifold to be a stratified space $X$ together with a lift of its tangent classifier:
\[
\xymatrix{
&&
\cB \ar[d]
\\
{\sf Entr}(X) \ar[rr]^-{\tau_X}  \ar[urr]^-g
&&
\bsc.
}
\]
A $\cB$-manifold $(X,g)$ will typically be denoted simply as $X$.  
More precisely, we define the pullback $\infty$-categories
\[
\xymatrix{
\mfldd(\cB)  \ar[r]  \ar[d]
&
\mfld(\cB)  \ar[r]  \ar[d]
&
\Psh(\bsc)_{/\cB}  \ar[d]
\\
\snglrd  \ar[r]
&
\snglr \ar[r]^-{\tau}
&
\Psh(\bsc)
}
\]
and refer to the upper middle as that of $\cB$-manifolds.


\begin{remark}\label{g-sheaf}
Via the straightening/unstraightening construction (see Section 2.2 of~\cite{HTT} -- this is the $\infty$-categorical analogue of the Grothendieck construction), a right fibration $\cB\to \bsc$ is the same data as a presheaf of spaces: $\bsc^{\op} \to \spaces$.  
Precomposing this presheaf with the tangent classifier for $X$ determines another presheaf of spaces: ${\sf Entr}(X)^{\op}\xra{\tau_X} \bsc^{\op} \xra{\cB} \spaces$.  
Via Theorem~A.9.3 of~\cite{HA}, such a presheaf is the data of a sheaf of spaces on $X$ that happens to be constructible with respect to the given stratification of $X$.  
As so, a $\cB$-manifold is a stratified space $X$ together with a section $g$ the sheaf named just above.  

\end{remark}



Definitionally, there is a fully faithful inclusion 
\[
\iota \colon \cB \hookrightarrow \mfld(\cB)~.
\]
A main result of~\cite{aft1} is that $\mfld(\cB)$ is generated by $\cB$ through the formations of \emph{collar-gluings} and \emph{sequential unions}:
\begin{itemize}
\item A \emph{collar-gluing} is a weakly constructible bundle $X\xra{f} [-1,1]$.  
We typically denote such a collar-gluing as $X\cong X_-\underset{\RR\times X_0} \bigcup X_+$ where $X_- := f^{-1}[-1,1)$ and $X_0 := f^{-1}(0)$ and $X_+ := f^{-1}(-1,1]$; we regard $X$ as the collar-gluing of $X_-$ and $X_+$ along $X_0$.  

\item A \emph{sequential union} is a sequence of open subspaces $X_0\subset X_1\subset \dots \subset X$ of a stratified space for which $\underset{i\geq 0} \bigcup X_i = X$. 

\end{itemize}

It is also useful to single out this notion of a finitely-presented $\cB$-manifolds, namely one which is generated from $\cB$ only by collar-gluings.
We say that an $\oo$-subcategory $\cM$ of $\mfld(\cB)$ is {\it closed under the formation of collar-gluings} if $X$ belongs to $\cM$ whenever $X_0$, $X_-$, and $X_+$ belong to $\cM$, where $X\ra [-1,1]$ is a weakly constructible bundle with those inverse images.
The $\oo$-category $\mfld(\cB)^{\sf fin}$ of {\it finitary} $\cB$-manifolds is the smallest full $\oo$-subcategory of $\mfld(\cB)$ which contains $\cB$ and is closed under collar-gluings.

\begin{example}\label{union-collar-gluing}
Disjoint unions are instances of collar-gluings.
That is, if $\cB$ is a category of basics, and $X:= X_- \sqcup X_+$ is a disjoint union of $\cB$-manifolds, then the map $f:X\ra [-1,1]$, given by $f_{|X_\pm} \equiv \pm 1$, is a collar-gluing.  
\end{example}

We conclude this subsection with a remark on our use of weakly constructible bundles.

\begin{remark}
Wherever we use weakly constructible bundles in this work, we will only work with a single map at a time. That is, we will not consider any sort of category or $\oo$-category of stratified spaces whose morphisms are weakly constructible bundles. This is due to a technical issue: it is unclear how to directly topologize the set of weakly constructible bundles (and then how to ensure a well-defined composition on these spaces of maps). This issue is dealt with in a successor work, \cite{striation}, by the construction of the $\oo$-category ${\sf c}\cB{\sf un}$. This is an $\oo$-category of compact stratified spaces whose morphisms are proper contructible bundles over the asymmetrically stratified interval $\{0\}\subset [0,1]$. A main result of that paper implies that such a proper constructible bundle $X\ra [0,1]$ is equivalent to a weakly constructible bundle map $X_1 \ra X_0$ from the generic fiber to the special fiber. Consequently, one could {\it define} the $\oo$-category of compact stratified spaces and weakly constructible bundles among them to be ${\sf c}\cB{\sf un}^{\op}$, but we have chosen not to incorporate this later work into the present paper.
\end{remark}







\subsection{Symmetric monoidal $\oo$-categories}
We review some aspects of symmetric monoidal $\infty$-categories, as well as $\infty$-operads, that we will make use of later on.
The content of this section is essentially extracted from \S2 of~\cite{HA}.  

We use the notation $\Fin_\ast$ for the category of based finite sets.
We let $\Fin$ denote the category of (possibly empty) finite sets, and $\Fin^{\sf inj}$ the subcategory of only injective morphisms.
There is a functor $(\Fin^{\sf inj})^{\op} \xra{\sf inert} \Fin_\ast$ given on objects as $I\mapsto I_+$ (i.e., attaching a disjoint basepoint) and on morphisms as $(f\colon I\hookrightarrow J)\mapsto (f^+:J_+\to I_+)$ where $f^+$ is specified by requiring both that the diagram of finite sets
\[
\xymatrix{
I_+  \ar[r]^-=  \ar[d]_-{f_+}
&
I_+  
\\
J_+  \ar[r]_-=  
&
J_+  \ar[u]_-{f^+}
}
\] 
commutes and that $f$ sends $J\smallsetminus f(I)$, the complement of the image of $f$, to the basepoint $+$.  
We denote the essential image of ${\sf inert}$ as $\Fin_\ast^{\sf inrt}\subset \Fin_\ast$ and refer to its morphisms as \emph{inert} maps -- these are the maps for which the inverse image of a point (which is not the basepoint) consists of at most a single element. The category $\Fin^{\sf inj}\simeq (\Fin_\ast^{\sf inrt})^{\op}$ carries the standard Grothendieck topology in which the covers are surjective maps.

\begin{defn}[After Definition 2.1.1.10 of~\cite{HA}]\label{def.operad}
An $\infty$-operad is a functor $\cO \to \Fin_\ast$ that satisfies the following points:
\begin{itemize}
\item For each inert map $I_+\xra{f} J_+$, and for each lift $O\in \cO_{|I_+}$, there is a coCartesian morphism $O \xra{\w{f}} O'$ lifting $f$. 
In particular, the restriction $\cO_{|\Fin^{\sf inrt}_\ast} \to \Fin_\ast^{\sf inrt}$ is a coCartesian fibration.

\item  The coCartesian fibration $\cO_{|\Fin^{\sf inrt}_\ast} \to \Fin^{\sf inrt}_\ast \cong (\Fin^{\sf inj})^{\op}$ is a $\Cat$-valued sheaf whose value on $+$ is terminal.

\item Let $(O_i)_{i\in I} \in \cO_{\ast_+}^{\times I} \simeq \underset{i\in I} \prod \cO_{\{i\}_+} \xla{\simeq} \cO_{|I_+}$ be an object, and likewise let $(O'_j)_{j\in J} \in \cO_{|J_+}$ be an object.
The canonical map of spaces 
\[
\Map_{\cO}\bigl((O_i)_{i\in I}, (O'_j)_{j\in J}\bigr) \xra{~\simeq~}\underset{I_+\xra{f}J_+}\coprod\underset{j\in J}\prod \Map_{\cO}\bigl((O_i)_{f(i)=j}, O_j\bigr)
\]
is an equivalence.  

\end{itemize}
Let $\cO$ be an $\infty$-operad.
We say $\cO$ is \emph{unital} if $\cO$ has an initial object.
The \emph{active $\infty$-subcategory}
\[
\cO_{\sf act} ~:=~ \cO_{|\Fin}
\]
is the restriction of $\cO$ along the functor $\Fin\xra{(-)_+}\Fin_\ast$ that adjoins a disjoint base point.  
An active morphism in $\cO$ whose target lies over $\ast_+\in \Fin_\ast$ is called a \emph{multi-morphism}.
\end{defn}



\begin{remark}
Definition~\ref{def.operad} of an $\infty$-operad is an $\infty$-categorical version of a \emph{colored operad}, also known as a \emph{multi-category}.
In that terminology, each object of the fiber $\cO_{|\ast_+}$ is a \emph{color}.  

\end{remark}


\begin{notation}\label{sym-cat-same}
Let $\cO \to \Fin_\ast$ be an $\infty$-operad. We will typically only carry the notation $\cO$ for such an $\infty$-operad.  We will refer to its restriction to $\ast_+$ as the \emph{underlying $\infty$-category}, and again denote it as $\cO$. Context should prevent confusion.
\end{notation}

\begin{remark}
Recall that giving a coCartesian fibration $\cO \to \fin_\ast^{\sf inrt}$ is equivalent to giving a functor $\fin_\ast^{\sf inrt} \to \Cat$ by the straightening/unstraightening construction (see Section 2.2 of~\cite{HTT} -- this is the $\infty$-categorical analogue of the Grothendieck construction). Further, the sheaf condition guarantees that the fiber over the based finite set $I_+$ is an $\infty$-category equivalent to an $I$-fold product of the fiber over $+$.
\end{remark}

\begin{defn}[Definition 2.1.2.7 of~\cite{HA}]
For $\cO$ and $\cP$ $\infty$-operads, the $\infty$-category of \emph{$\cO$-algebras in $\cP$} is the full $\infty$-subcategory
\[
\Alg_\cO(\cP)~\subset~\Fun_{\Fin_\ast}(\cO,\cP)
\]
consisting of those functors over based finite sets that preserve inert-coCartesian morphisms. 
There is an $\infty$-category ${\sf Operad}_\infty$ whose objects are $\infty$-operads and whose space of morphisms from $\cO$ to $\cP$ is the underlying $\infty$-groupoid of $\Alg_\cO(\cP)$. (See Definition 2.1.4.1 of~\cite{HA}.)
\end{defn}

\begin{defn}[Definition~2.0.0.7 of~\cite{HA}; see also Remark~2.1.2.19 of~\cite{HA}.]\label{def.sym-mon}
A \emph{symmetric monoidal $\infty$-category} is a coCartesian fibration $\cV \to \Fin_\ast$ whose restriction $\cV_{|\Fin^{\sf inrt}_\ast} \to \Fin^{\sf inrt}_\ast$ is a $\Cat$-valued sheaf whose value on $+$ is terminal.
(In particular, a symmetric monoidal $\infty$-category is an $\infty$-operad.)
Let $\cV$ be a symmetric monoidal $\infty$-category.
A \emph{symmetric monoidal unit} $\uno_\cV$ for $\cV$ is a target of a morphism in $\cV$ over $+\to \ast_+$.  
For $\cD$ another symmetric monoidal $\infty$-category, the $\infty$-category of \emph{symmetric monoidal functors (from $\cV$ to $\cD$)} is the full $\infty$-subcategory
\[
\Fun^\ot(\cV,\cD)~\subset~\Fun_{\Fin_\ast}(\cV,\cD)
\]
consisting of those functors over based finite sets that preserve coCartesian morphisms.  
There is an $\infty$-category ${\sf Cat}^\ot_\infty$ whose objects are symmetric monoidal $\infty$-categories and whose space of morphisms from $\cV$ to $\cD$ is the underlying $\infty$-groupoid of $\Fun^\ot(\cO,\cV)$. (See Variant 2.1.4.13 of~\cite{HA}.)
\end{defn}

\begin{lemma}\label{creates-limits} 
The forgetful functor 
\[
{\sf Operad}_\infty \longrightarrow \Cat_{/\Fin_\ast}
\]
creates limits.
The underlying $\infty$-category functor
\[
{\sf Cat}^\ot_\infty \longrightarrow \Cat
\]
is conservative and creates limits.  
\end{lemma}

\begin{proof}
The first statement can be verified directly.
Consider a small diagram $\cK\to {\sf Operad}_\infty$, denoted $k\mapsto \cO_k$, and a limit cone $\cK^\tl \to \Cat_{/\Fin_\ast}$.  Denote the value of the cone-point as $\cO$.
Let $I_+\xra{f} J_+$ be an inert map, and let $O \in (\cO)_{|I_+}$ be an object over $I_+$.  
Consider the composite functor 
\[
\cK \to {\sf Operad}_\infty \to \Cat_{/\Fin_\ast} \xra{\{O\}\underset{(-)_{|I_+}}\times \Fun^{\sf coCart}\bigl([1],(-)\bigr)_{|f}} \Cat
\]
given by assigning to an object $k$ the category of coCartesian lifts of $O_k\xra{\w{f}_k} O_k'$ in $\cO_k$ from the image of $O$.
This functor takes values in terminal $\infty$-categories, and so the limit too is terminal and it is equipped with a functor to 
\[
\underset{k\in \cK} \lim\Bigl( \{O\}\underset{(\cO_k)_{|I_+}} \times \Fun\bigl([1],\cO_k\bigr)_{|f} \Bigr)\xla{\simeq} \{O\}\underset{\cO_{|I_+}} \times \Fun\bigl([1],\cO\bigr)_{|f}~.
\]
By design, a morphism $O\xra{\w{f}} O'$ in the essential image of this functor is coCartesian.  

Now consider a functor $\cO_{|I_+} \to \underset{i\in I}\prod \cO_{\{i\}_+}$ induced by the diagram of inert morphisms $(I_+ \xra{a_i} \{i\}_+)_{i\in I}$.  
That this functor is an equivalence follows because limits commute with finite products.
Likewise, for each pair of objects $(O_i)_{i\in I}\in  \cO_{|I_+}$ and $(O'_j)_{j\in J} \in \cO_{|J_+}$, consider the map of spaces
\[
\Map_\cO\bigl((O_i)_{i\in I}, (O'_j)_{j\in J}\bigr) \longrightarrow \underset{j \in J} \prod \Map_{\cO}\bigl( (O_i)_{\{f(i)=j\}}, O_j\bigr)~. 
\]
That this map is an equivalence follows again because limits commute with finite products.  

The second statement is easier to find the literature.  
By Lemma~3.2.2.6 of~\cite{HA}, a forgetful map from a category of algebras over an operad is both conservative and limit-creating. Symmetric monoidal $\infty$-categories are commutative algebra objects in the symmetric monoidal category $\Cat$, hence Lemma~3.2.2.6 of~\cite{HA} applies.
\end{proof}

\begin{remark}
Let $F: \cO \to \cV$ be a symmetric monoidal functor. Since $F$ preserves coCartesian morphisms, it induces a map between the sheaves on $\Fin^{\sf inj}$ associated to $\cO$ and $\cV$. Hence for every $f: I_+ \to J_+$, we obtain a diagram $[1]\times [1] \to \Cat$ as follows:
 \[
 \xymatrix{
 \cO^I  \ar[d]_-{f_\ast}  \ar[rr]^-{F^I}
 &&
 \cV^I  \ar[d]^-{f_\ast}
 \\
 \cO^J  \ar[rr]^-{F^J}
 &&
 \cV^J.
 }
\]
For $J=\ast$, one can interpret the diagram as specifying an equivalence $\bigotimes_\cV^I F(O_i) \simeq F(\bigotimes_\cO^I O_i)$.
\end{remark}

\begin{remark}
Let $\cV$ and $\cD$ be symmetric monoidal $\infty$-categories.
There is an evident full inclusion $\Fun^\ot(\cV,\cD) \subset \Alg_{\cV}(\cD)$ -- it is typically not essentially surjective. The latter corresponds to lax monoidal functors.
\end{remark}

For each finite set $I$, there is then a canonical diagram of $\infty$-categories
\[
\ot \colon \cV^I \xla{~\simeq~}\cV_{I_+}  \xra{\cV_{(I_+ \to \ast)}} \cV~.
\]


\begin{defn}\label{def-siftedcocplt}

For $\cK$ a small $\infty$-category, the symmetric monoidal structure of $\cV$ {\it distributes over $\cK$-shaped colimits} if for each $c\in \cV$, the composite functor \[c\ot -\colon \cV \simeq \ast \times \cV \xra{ c\times {\sf id}_\cV} \cV\times \cV \xra{\ot} \cV\] commutes with colimits of $\cK$-shaped diagrams.  
We say $\cV$ is \emph{$\ot$-sifted cocomplete} if its underlying $\infty$-category admits sifted colimits and its symmetric monoidal structure distributes over sifted colimits, where an $\oo$-category $\cK$ is {\it sifted} if it is nonempty and the diagonal $\cK\ra \cK\times \cK$ is a final functor.

\end{defn}

\begin{lemma}[Section~2.2.4 of~\cite{HA}]\label{sym-env}
The forgetful functor admits a left adjoint
\[
{\sf Env}\colon {\sf Operad}_\infty ~\rightleftarrows~ {\sf Cat}^\ot_\infty~,
\]
referred to as the \emph{symmetric monoidal envelope} functor.  
\end{lemma}

\begin{observation}\label{extending-endos}
There is a canonical filler in the diagram among $\infty$-categories:
\[
\xymatrix{
{\sf Cat}_\infty^\ot\ar@{-->}[rr]^-{(-)^{\op}}  \ar[d]
&&
{\sf Cat}_\infty^\ot  \ar[d]
\\
\Cat  \ar[rr]^-{(-)^{\op}}
&&
\Cat.
}
\]
In other words, the opposite of the underlying $\infty$-category of a symmetric monoidal $\infty$-category is canonically endowed with a symmetric monoidal structure.  
\end{observation}


\begin{example}
Here are some examples of symmetric monoidal $\infty$-categories that are $\ot$-sifted cocomplete.  
\begin{itemize}
\item $({\sf Ch}_\Bbbk,\oplus)$ and $({\sf Ch}_\Bbbk,\ot)$: chain complexes over a ring $\Bbbk$ with equivalences given by quasi-isomorphisms, equipped with direct sum, or with tensor product.  
\item $({\sf Spectra}, \vee)$ and $({\sf Spectra}, \wedge)$: spectra with equivalences generated by stable homotopy equivalences, equipped with wedge sum, or with smash product.  
\item $(\cX,\times)$: any cocomplete Cartesian closed $\infty$-category (for instance $\spaces$ or $\Cat$) with finite product.  
\item Let $\cV$ be any symmetric monoidal $\infty$-category whose underlying $\infty$-category admits small colimits and whose symmetric monoidal structure distributes over small colimits.
Then, for $\cO$ any $\infty$-operad, the $\infty$-category of algebras $\Alg_{\cO}(\cV)$ inherits a standard symmetric monoidal structure which is given pointwise, and this symmetric monoidal $\infty$-category is $\ot$-sifted cocomplete.  
\end{itemize}
An example of a symmetric monoidal $\infty$-category that is \emph{not} $\ot$-sifted cocomplete is $({\sf Ch}_\QQ^{\op}, \ot)$, for $\ot$ does not distribute over totalizations.  

\end{example}

We are about to define an $\infty$-operad $\cV_{/c}$ for $\cV$ a unital symmetric monoidal $\infty$-category and $c\in \cV$ an object in its underlying $\infty$-category.  
Recall the construction from \S2.4.3 of \cite{HA} of an $\infty$-operad $\cD^\amalg$ from an $\infty$-category $\cD$.  Quickly, a functor $\cK \to \cD^\amalg$ is the datum of a functor $\cK\underset{\Fin_\ast}\times \Fin_{\ast, \ast'} \to \cD$ where the second factor in the fiber product is the category of finite sets equipped with an inclusion from the two-element set $\{\ast,\ast'\}$ and maps among such that preserve such inclusions.  
Should $\cD$ be an ordinary category, then the $\cD^{\amalg}$ is an ordinary colored operad with one color for each object of $\cD$, while a multi-morphism from $(d_1,\dots,d_n)$ to $d$ is simply a collection of morphisms $d_i\to d$ for each $1\leq i \leq n$.   

\begin{lemma}\label{unit-initial-cocart}
For $\cO =(\cO\to \Fin_\ast)$ a unital $\infty$-operad,
there is a preferred map of $\infty$-operads
\[
\cO \longrightarrow (\cO_{|\ast_+})^\amalg~.
\]

\end{lemma}

\begin{proof}
We will use the notation $\Fin^{\sf inj}\subset\Fin \xra{(-)_+} \Fin_\ast$ for the category of finite sets and injections among them.  
Consider the category $\Fun_{\sf inj}\bigl([1], \Fin_\ast\bigr)$ consisting of those functors from the two-object totally ordered set $[1]=\{0<1\}$ which classify \emph{injective} maps among based finite sets, and natural transformations among them.   
Evaluation at $0$ gives a functor $\Fun_{\sf inj}\bigl([1], \Fin_\ast\bigr)\xra{{\sf ev}_0} \Fin_\ast$.  
Notice the evident functor $\Fin_{\ast,\ast'}\to \Fun_{\sf inj}\bigl([1], \Fin_\ast\bigr)$, and notice that it factors as an equivalence $\Fin_{\ast,\ast'} \xra{\simeq} {\sf ev}_0^{-1}(\ast_+)$.  

The $\infty$-operad $\cO$ being unital grants that the underlying $\infty$-category $\cO_{|\ast_+}$ has an initial object.  
It follows that the restricted projection $\cO_{|\Fin^{\sf inj}} \to \Fin^{\sf inj}$ is a Cartesian fibration.  
In particular, there is a canonical filler in the diagram of $\infty$-categories
\[
\xymatrix{
\cO \underset{\Fin_\ast} \times \Fun_{\sf inj}\bigl([1], \Fin_\ast\bigr)     \ar@{-->}[rr]  \ar[dr]^{{\sf ev}_0}
&&
\cO  \ar[dl]
\\
&
\Fin_\ast
&
}
\]
in which the implicit functor $\Fun_{\sf inj}\bigl([1], \Fin_\ast\bigr) \xra{{\sf ev}_1} \Fin_\ast$ is evaluation at $1$.
Restricting the second factor in the above fiber product to $\Fin_{\ast,\ast'}$ gives the functor $\cO \to (\cO_{|\ast_+})^\amalg$.  
It is direct to verify that this functor sends inert-coCartesian morphisms to inert-coCartesian morphisms.  

\end{proof}

\begin{cor}\label{slice-operads}
Let $\cO$ be a unital $\infty$-operad.
Let $\cE_{|\ast_+} \to \cO_{|\ast_+}$ be a right fibration over the underlying $\infty$-category.
We denote the pullback $\infty$-category
\[
\xymatrix{
\cE  \ar[r]  \ar[d]
&
(\cE_{|\ast_+})^\amalg  \ar[d]
\\
\cO  \ar[r]
&
(\cO_{|\ast_+})^\amalg ~.
}
\]
After Lemma~\ref{creates-limits}, the composite functor $\cE \to \cO \to \Fin_\ast$ makes $\cE$ into an $\infty$-operad, and the functor $\cE \to \cO$ is a map of $\infty$-operads.  

\end{cor}

\begin{notation}\label{slice-convention}
Let $\cD \to \cM$ be a symmetric monoidal functor between symmetric monoidal $\infty$-categories, each for which the symmetric monoidal unit is initial.  
Let $X\in \cM$ be an object of the underlying $\infty$-category.
We use the notation
\[
\cD_{/X}
\]
for the output of Corollary~\ref{slice-operads} applied to the right fibration $\cD_{/X}\to \cD$.  
By construction, this $\infty$-operad is equipped with an $\oo$-operad map to $\cD$ for which the functor on underlying $\infty$-categories is the standard projection from the slice.  
Say a morphism of $\cD_{/X}$ is \emph{pre-coCartesian} if its image in $\cD$ is coCartesian over $\Fin_\ast$.  
We adopt the following notational convention: for $\cV$ a symmetric monoidal $\infty$-category, the $\infty$-category of $\cD_{/X}$-algebras in $\cV$ is the full $\infty$-subcategory
\[
\Alg_{\cD_{/X}}(\cV)~\subset~ \Fun_{\Fin_\ast}\bigl(\cD_{/X}, \cV\bigr)
\]
consisting of those functors that send pre-coCartesian morphisms to coCartesian morphisms.  

\end{notation}
