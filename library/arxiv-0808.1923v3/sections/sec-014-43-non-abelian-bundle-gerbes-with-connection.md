---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-014-43-non-abelian-bundle-gerbes-with-connection
section_title: "Non-Abelian Bundle Gerbes with Connection"
section_number: 4.3
pages: 36-41
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.994
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec3_3}


In this section we generalize the equivalence of the previous section to so-called non-abelian bundle gerbes, as defined in \cite{aschieri}. The difference between abelian and non-abelian bundle gerbes can roughly be summarized as follows:
\begin{enumerate}

\item 
The Lie group $S^1$ is replaced by some connected Lie group $H$.

\item
Principal $S^1$-bundles are replaced by \emph{principal $H$-bibundles}, bundles with commuting left and right principal $H$-action. Morphisms between $H$-bibundles are bi-equivariant bundle morphisms.


\item
Connections on $S^1$-bundles are replaced by so-called \emph{twisted connections} on bibundles. 
\end{enumerate}
Non-abelian $H$-bundle gerbes with connection over $M$ form a 2-category which we denote by $H\text{-}\mathfrak{BGrb}^{\nabla}(M)$; some details are reviewed below. There is a sub-2-category $H\text{-}\mathfrak{BGrb}^{\nabla_{\!f\!f}}(M)$ of fake-flat non-abelian $H$-bundle gerbes, related to Remark \ref{rem2}.


On the side of transport 2-functors, we write $\hbitor$ for the category
  whose objects are smooth manifolds with commuting, free and transitive, smooth left and right
  $H$-actions, and whose morphisms are
  smooth bi-equivariant maps. Using the product over
  $H$ this is naturally a (non-strict) monoidal category, and we   write
  $\mathcal{B}(\hbitor)$ for the corresponding one-object (non-strict)
  2-category. Let $\mathrm{AUT}(H)$ be the Lie 2-group associated to $H$ via Example \ref{ex:2groups} \erf{ex:2groups:aut}. A 2-functor
\begin{equation}
\label{48}
i:\mathcal{B}\mathrm{AUT}(H) \to \mathcal{B}(\hbitor)
\end{equation}
is  defined as follows.
It sends a 1-morphism $\varphi \in \mathrm{Aut}(H)$ to the $H$-bitorsor $_\varphi H$
which is the group $H$ on which an element $h$ acts from the right by multiplication and from the left by multiplication with $\varphi(h)$. The compositors of $i$ are given by the canonical identifications
\begin{equation*}
c_{g_1,g_2}:{}_{g_1} H \;\times_H \;{}_{g_2} H
  \to
  {}_{g_2 g_1} H\text{,}
\end{equation*}
and the unitor is the identity. The 2-functor $i$
further sends a 2-morphism $h:\varphi_1 \Rightarrow \varphi_2$ to the bi-equivariant map
\begin{equation*}
_{\varphi_1}H \to _{\varphi_2}H:x \mapsto hx\text{.}
\end{equation*}
While the bi-equivariance with respect to the right action is obvious, the one with respect to the left action follows from the condition $\varphi_2(x)=h\varphi_1(x)h^{-1}$ we have for the 2-morphisms in $\mathrm{AUT}(H)$ for all $x\in H$. 


The main result of this section is:

\begin{theorem}
\label{th:nagrb}
There is a canonical injective map
\begin{equation*}
\hc 0 (H\text{-}\mathfrak{BGrb}^{\nabla_{\!f\!f}}(M)) \to \hc 0 (\transport{}{2}{\mathcal{B}\mathrm{AUT}(H)}{\mathcal{B}(\hbitor)})
\end{equation*}
from isomorphism classes of fake-flat non-abelian $H$-bundle gerbes to transport 2-functors with values in $\mathcal{B}(H\text{-}\mathrm{BiTor})$ and $\mathcal{B}\AUT(H)$-structure. 
\end{theorem}



That we do not achieve a bijection or an  equivalence of 2-categories is due to the fact that the category of bibundles with twisted connections -- as defined in \cite{aschieri} -- oversees a class of morphisms, which in principle should be allowed
and arise naturally from the theory of transport functors. 


Anyway, Theorem \ref{th:nagrb} provides non-trivial examples of transport 2-functors. The injective map of Theorem \ref{th:nagrb} is constructed as 
\begin{equation*}
H\text{-}\mathfrak{BGrb}^{\nabla_{\!f\!f}}(M) \to \transsmoothpi{i}{2}{\mathrm{Gr}}{}_M\cong \transport{}{2}{\mathcal{B}\mathrm{AUT}(H)}{\mathcal{B}(\hbitor)}\text{,}
\end{equation*}
where the first 2-functor is constructed in Proposition \ref{prop:locequivnagrb} and the equivalence is the one of Theorem \ref{th4}. 
We first review necessary material.



\subsubsection{Twisted Connections on Bibundles}

\label{bitorsors}


Let $P$ be a principal $H$-bibundle over $X$.
We  denote the left and right actions by an element $h\in H$ on  $P$ by $l_h$ and $r_h$, respectively. Measuring the difference between the left and the right action in the sense of  $l_h(p) = r_{g(h)}(p)$ furnishes a smooth map
\begin{equation}
\label{47}
g: P \to \mathrm{Aut}(H)\text{.}
\end{equation}
In the following we denote by $\mathfrak{aut}(H)$ the Lie algebra of $\mathrm{Aut}(H)$. Further, we denote by $t: H \to \mathrm{Aut}(H)$ the assignment of inner automorphisms and by $\alpha: \mathrm{Aut}(H) \times H \to H$ the evaluation. 

\begin{definition}[\cite{aschieri}]
Let $p : P \to X$ be a principal $H$-bibundle, and let 
  $A \in \Omega^1(X,\mathfrak{aut}(H))$ be a 1-form on the base space. An \emph{$A$-twisted connection on $P$} is
  a  1-form $\phi \in \Omega^1(P,\mathfrak{h})$ satisfying
\begin{equation}
\label{53}
    \phi_{\rho h}\left(
      \frac{\mathrm{d}}{\mathrm{d}t}(\rho h)
    \right)
    =
    \mathrm{Ad}_h^{-1}
    \left(
      \phi_\rho\left(\frac{\mathrm{d} \rho}{\mathrm{d} t}\right)
    \right)
    -
    (r_h \circ \alpha_h)_{*}\circ (p^*A)
    +
    \theta_h\left(
      \frac{\mathrm{d} h}{\mathrm{d}t}
    \right)
\end{equation}
for all smooth curves $\rho : [0,1] \to P$ and $h : [0,1] \to H$. A morphism $f: P \to P'$ respects $A$-twisted connections $\phi$ on $P$ and $\phi'$ on $P'$ if $f^{*}\phi'=\phi$.  
\end{definition}

We write $\mathfrak{Bibun}_H^{\nabla}(X,A)$ for the category of principal $H$-bibundles with $A$-twisted connection over $X$, and $\mathfrak{Bibun}_{H}^{\nabla}(X)$ for the union of these categories over all 1-forms $A$.

\begin{remark}
For $A = 0$ an $A$-twisted connection on $P$ is the same as an ordinary
connection on $P$ regarded  as a right principal
bundle. 
\begin{comment}
One can give an analogous definition of a twisted left connection. Then, a twisted right connection
gives rise to a twisted left connection, for a different
twist, and vice versa. This is discussed in detail in
\cite{aschieri}, but will be a manifest consequence of
the reformulation which we give later.
\end{comment}
\end{remark}

\begin{lemma}[{{\cite{aschieri}}}]
Let $A\in \Omega^1(X,\mathfrak{aut}(H))$ be a 1-form and let
 $p : P \to X$ be a principal $H$-bibundle. For any $A$-twisted connection
$\phi$ on $P$ there exists a unique 1-form $A_{\phi} \in \Omega^1(X,\mathfrak{aut}(H))$ satisfying
\begin{equation*}
    p^* A_{\phi} =
    \mathrm{Ad}_{g} (p^* A )
    - g^* \bar\theta
    -
    t_{*} \circ \phi
    \text{,}
\end{equation*}
where $g$ is the map from \erf{47}.
\end{lemma}


A twisted connection in a principal bibundle $P$ gives rise to parallel transport maps
\begin{equation*}
\tau_{\gamma}: P_x \to P_y
\end{equation*}
between the fibres of $P$
over points $x,y$ associated to any path $\gamma:x \to y$. It is obtained in the same way as in an ordinary principal bundle but using equation \erf{53} instead of the usual one. As a result of the twist, the maps $\tau_{\gamma}$ are not bi-equivariant; they satisfy
\begin{equation}
\label{54}
\tau_{\gamma}(l_{F_{\phi}(\gamma)(h)}(p)) = l_{h^{-1}}(\tau_{\gamma}(p))
\quad\text{ and }\quad
\tau_{\gamma}(r_h(p)) = r_{F(\gamma)^{-1}(h^{-1})}\tau_{\gamma}(p)
\end{equation}
where $F,F_{\phi}: PX \to \mathrm{Aut}(H)$ are the parallel transport maps associated to the 1-forms $A$ and $A_{\phi}$; see \cite[Proposition 4.7]{schreiber3}. These complicated relations have a very easy interpretation, as we will see in the next section.

Finally, an $A$-twisted connection $\phi$ on a principal $H$-bundle $P$ has a curvature: this is the 2-form
\begin{equation*}
\mathrm{curv}(\phi) := \mathrm{d}\phi + [\phi \wedge \phi] + \alpha_{*}(A \wedge \phi) \in \Omega^2(P,\mathfrak{h})\text{.}
\end{equation*}



For two principal $H$-bibundles $P$ and $P'$ over $X$ one can fibrewise take the tensor product of $P$ and $P'$ yielding a new principal $H$-bibundle $P \times_H P$ over $X$. If the two bibundles are equipped with twisted connections, the bibundle $P \times_H P'$ inherits a twisted connection only  if the two twists
satisfy an appropriate matching condition. Suppose the principal $H$-bibundle $P$ is equipped with an $A$-twisted connection $\phi$, and $P'$ is equipped with an $A'$-twisted connection $\phi'$, and suppose that the matching condition
\begin{equation}
\label{49}
A'_{\phi'} = A
\end{equation}
is satisfied. Then, the tensor product bibundle $P \times_H P'$ carries an $A'$-twisted connection $\phi_{\mathrm{tot}}\in\Omega^1(P \times_H P,\mathfrak{h})$
characterized uniquely by the condition that
\begin{equation*}
    \mathrm{pr}^{*} \phi_{\mathrm{tot}}
    =
    (g \circ p')_* \circ p^*\phi
    +
    p'^* \phi'\text{,}
\end{equation*}
where $\mathrm{pr}: P \times_X P' \to P \times_H P'$ is the projection to the tensor product and $p$ and $p'$ are the projections to the two factors.
This tensor product,  defined only between appropriate pairs of bibundles with twisted connections, turns $\mathfrak{Bibun}_{H}^{\nabla}(X)$
into a \quot{monoidoidal} category. 

A better point of view is to see it as a 2-category: the objects are 
the twists, i.e.  1-forms $A \in \Omega^1(X,\mathfrak{aut}(H))$,
  a 1-morphism $A \to A'$ is a principal $H$-bibundle $P$ with $A'$-twisted connection $\phi$ such that $A'_{\phi'}=A$,  and a 2-morphism $(P,\phi) \Rightarrow (P',\phi')$ is just a morphism of principal $H$-bibundles that respects the $A'$-twisted connections.


\subsubsection{Transport Functors for Bibundles with Twisted Connections}

\label{sec4_3_2}

We are now going to relate the category $\mathfrak{Bibun}_H^{\nabla}(X)$ of principal $H$-bibundles with twisted connections over $X$ to a category of transport functors. Using the terminology of Section \ref{sec:smoothdescent}, we have:


\begin{proposition}
\label{prop4}
There is a surjective and faithful functor
\begin{equation*}
\mathfrak{Bibun}_H^{\nabla}(X) \to \transportX{}{1}{\Lambda\mathcal{B}\mathrm{AUT}(H)}{\Lambda_i\mathcal{B}(\hbitor)}\text{.}
\end{equation*}
\end{proposition}

\begin{proof}
Given a principal $H$-bibundle $P$ with $A$-twisted connection, we define the associated transport functor by
\begin{equation*}
\mathrm{tra}_P\quad:\quad\alxydim{}{x \ar[r]^{\gamma} & y}\quad\mapsto\quad\alxydim{@C=1.5cm@R=1.3cm}{i(*) \ar[d]_{P_x} \ar[r]^{i(F(\gamma))} & i(*) \ar@{=>}[dl]|{\tau_{\gamma}^{-1}} \ar[d]^{P_y} \\ i(*) \ar[r]_{i(F_{\phi}(\gamma))} & i(*)\text{.}}
\end{equation*}
Here $F,F_{\phi}:PX \to \mathrm{Aut}(H)$ are the maps defined by $A$ and $A_{\phi}$ that we have already used in the previous section. The definition contains the claim that the parallel transport map $\tau_{\gamma}$ gives a bi-equivariant map
\begin{equation*}
\tau_{\gamma}^{-1}: P_y \;\times_H \;_{F(\gamma)}H \to \;_{F_{\phi}(\gamma)}H \;\times_H\; P_x\text{;}
\end{equation*}
it is indeed easy to check that this is precisely the meaning of equations \erf{54}. A morphism $f:P \to P'$ between bibundles with $A$-twisted connections induces a natural transformation $\eta_f: \mathrm{tra}_P \to \mathrm{tra}_{P'}$ between the associated  functors, whose component at a point $x$ is the bi-equivariant map $f_x:P_x \Rightarrow P_x'$. This is a particular morphism in $\Lambda_i\mathcal{B}(\hbitor)$ for which the horizontal 1-morphisms are identities. Here it becomes clear that the assignments
\begin{equation*}
(P,\phi) \mapsto \mathrm{tra}_P\quad\text{ and }\quad f\mapsto \eta_f
\end{equation*}
define a functor which is faithful but not full. 

It remains to check that the functor $\mathrm{tra}_P$ is a transport 2-functor. We leave it as an exercise for the reader to construct a local trivialization $(t,\mathrm{triv})$ of $\mathrm{tra}_P$ with smooth descent data.
Hint: use an ordinary local trivialization of the bibundle $P$ and follow the proof of Proposition 5.2 in \cite{schreiber3}.
\end{proof}


Both categories in Proposition \ref{prop4} have the feature that they have tensor products between appropriate objects. Concerning the bibundles with twisted connections, we have described this in terms of the matching condition \erf{49} on the twists. Concerning the category of transport functors, this tensor product is inherited from the one on $\Lambda_i\mathcal{B}(\hbitor)$, which has been discussed in Section \ref{sec:smoothdescent}.

\begin{lemma}
\label{lem7}
The matching condition \erf{49} corresponds to the required condition for tensor products in $\Lambda_i\mathcal{B}(\hbitor)$ under the functor of Proposition \ref{prop4}. Moreover, the functor respects tensor products whenever they are well-defined.
\end{lemma}

\begin{proof}
Suppose that the matching condition $A'_{\phi'}=A$ holds, so that principal $H$-bibundles $P$ and $P'$ with connections $\phi$ and $\phi$ have a tensor product. It follows that the map $F_{\phi'}$  which labels the horizontal 1-morphisms at the bottom of the images of $\mathrm{tra}_{P'}$ is equal to the map  $F$ which labels the ones at the top of the images of $\mathrm{tra}_{P}$; this is the required condition for the existence of the tensor product $\mathrm{tra}_{P'} \otimes \mathrm{tra}_{P}$. That the tensor products are respected follows from the definition of the twisted connection $\phi_{\mathrm{tot}}$ on the tensor product bibundle.
\end{proof}

An alternative formulation of Lemma \ref{lem7} would be that the functor of Proposition \ref{prop4} respects the \quot{monoidoidal structures}, or, that it is a double functor between (weak) double categories.


\subsubsection{Non-Abelian Bundle Gerbes as Transport 2-Functors}

Let $\pi:Y \to M$ be a surjective submersion. We recall:

\begin{definition}[{{\cite{aschieri}}}]
\label{def:nagrb}
A \emph{non-abelian $H$-bundle gerbe with connection} with respect to $\pi$ is a 2-form $B\in\Omega^2(Y,\mathfrak{h})$, a 1-form $A \in \Omega^1(Y,\mathfrak{aut}(H))$, a principal $H$-bibundle $p\maps P \to Y^{[2]}$ with $A$-twisted connection $\phi$ such that
\begin{equation}
\label{56}
\mathrm{curv}(\phi) = (\pi_1 \circ p)^{*}B - (\alpha_{g})_{*} \circ (\pi_2 \circ p)^{*}B\text{,}
\end{equation}
and an associative morphism 
\begin{equation*}
\mu: \pi_{23}^{*}P \;\times_H \; \pi_{12}^{*}P \to \pi_{13}^{*}P
\end{equation*}
of bibundles over $Y^{[3]}$ that respects the twisted connections.
\end{definition}


In \erf{56}, $g$ is the smooth map \erf{47} and $\alpha: \mathrm{Aut}(H) \times H \to H$ is the evaluation.   The definitions of  1-morphisms and  2-morphisms generalize in a straightforward way the definitions from the abelian case.  This defines the 2-category $H\text{-}\mathfrak{BGrb}^{\nabla}(\pi)$.  The 2-category $H\text{-}\mathfrak{BGrb}^{\nabla}(M)$ of non-abelian $H$-bundle gerbes over $M$ is defined as the direct limit,
\begin{equation*}
H\text{-}\mathfrak{BGrb}^{\nabla}(M) := \lim_{\overrightarrow{\pi}} H\text{-}\mathfrak{BGrb}^{\nabla}(\pi)\text{.}
\end{equation*}
We remark:
\begin{enumerate}[(i)]
\item
A non-abelian $S^1$-bundle gerbe is \textit{not} the same as an abelian $S^1$-bundle gerbe: for the non-abelian bundle gerbes also the automorphisms are important, and $\mathrm{Aut}(S^1)\cong \Z_2$. For transport 2-functors this is even more obvious: the Lie 2-groups $\mathcal{B}S^1$ and $\mathrm{AUT}(S^1)$ are not equivalent.

\item
The non-abelian bundle gerbes of Definition \ref{def:nagrb} are a priori not \quot{fake-flat}, i.e. the relation
\begin{equation*}
t_{*}(B) = \mathrm{d}A + [A \wedge A]
\end{equation*}
may not be satisfied, see Remark \ref{rem2}. We denote the sub-2-categories of fake-flat non-abelian $H$-bundle gerbes by $H\text{-}\mathfrak{BGrb}^{\nabla_{\!f\!f}}(-)$.
\end{enumerate}
 

 
 
\begin{proposition}
\label{prop:locequivnagrb}
For every surjective submersion $\pi:Y \to M$, there is a 2-functor
\begin{equation*}
H\text{-}\mathfrak{BGrb}^{\nabla_{\!f\!f}}(\pi) \to \transsmooth{i}{2}{}\text{.}
\end{equation*}
which is surjective and faithful on Hom-categories. In particular, it induces an injective map on isomorphism classes of objects.
\end{proposition}
 

\begin{proof}
All relations concerning the bimodules are analogous to those in the abelian case, upon generalizing Lemma \ref{lem6} to Proposition \ref{prop4} and Lemma \ref{lem7}. Relation \erf{56} for the 2-form $B$ can be proved in the same way as  Lemma \ref{lem8}, but now using the full version of equation \erf{55}.
The comments concerning the descent datum $\psi$ also remain valid. 
\end{proof}


In the direct limit, the 2-functors of Proposition \ref{prop:locequivnagrb} induce a 2-functor
\begin{equation}
\label{dirlimfun}
H\text{-}\mathfrak{BGrb}^{\nabla_{\!f\!f}}(M) \to \transsmoothpi{i}{2}{\mathrm{Gr}}{}_M\text{.}
\end{equation}
Since the direct limit respects the operation of forming isomorphism classes of objects, and on the level of sets a direct limit of injective maps is injective, the 2-functor \erf{dirlimfun} induces an injective map on isomorphism classes of objects. This completes the proof of Theorem \ref{th:nagrb}.
