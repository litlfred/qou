---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-017-51-markings-and-fundamental-bigons
section_title: "Markings and Fundamental Bigons"
section_number: 5.1
pages: 46-49
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.994
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec:holonomy}




Surface holonomy of gerbes has so far only be studied in the abelian case, i.e. for gerbes with structure 2-group $\mathfrak{G}=\mathcal{B}S^1$; see e.g. \cite{murray}. It is understood  that an abelian gerbe with connection over $M$  provides an $S^1$-valued surface holonomy for smooth maps $\phi:S \to M$ defined on \emph{closed oriented surfaces} $S$. Various extensions have been studied for oriented surfaces with boundary \cite{carey2,gawedzki1}, closed unoriented (in particular unorientable) surfaces \cite{schreiber1}, and unoriented surfaces with boundary \cite{gawedzki8}.



Let us try  to explain why the step from  abelian to non-abelian surface holonomy is so difficult, by looking at the analogous but easier situation of ordinary holonomy of a  connection on a principal bundle $P$ over $M$. In the abelian case, say with structure group $S^1$, holonomy is defined for \emph{closed oriented curves} in $M$. Passing to a non-abelian structure group $G$, we have two possibilities. The first is  to choose additional structure on the closed oriented curve, namely a point $x\in M$, in which case the holonomy is a well-defined automorphism of the fibre $P_x$ of the bundle $P$  over the point $x$. The second possibility is to project the value of the holonomy into an appropriate quotient, for example along the map $\mathrm{Aut}(P_x) \to G\red$ into the set $G\red$ of conjugacy classes of $G$. This quotient is designed such that a different choice of $x$ yields the same element in $G\red$, and so $P$ has a well-defined $G\red$-valued holonomy for closed oriented curves. 







Choosing a point in a closed oriented curve means to represent it as a  path (up to thin homotopy). 
The objective of this section is to describe how to represent a closed oriented surface $\phi:S \to M$ as a bigon in $M$. 
It will be convenient to adapt the following standard terminology from the theory of Riemann surfaces to our setting. Suppose $S$ is a closed oriented surface of genus $g$.  A \emph{marking} of $S$ is a point $x\in S$ together with a   set $\EuScript{M}=\left \lbrace \alpha_i,\beta_i \right \rbrace_{i=1}^g$ of paths $\alpha_i:x \to x$ and $\beta_i:x\to x$ such that the homotopy classes $[\alpha_i]$ and $[\beta_i]$ of the paths form a presentation of the fundamental group of $S$ based at $x$ with the relation that $[\tau_{\EuScript{M}}] = 1$, where
\begin{equation*}
\tau_{\EuScript{M}} := \beta_g^{-1}\circ  \alpha_g^{-1} \circ  \beta_g \circ \alpha_g  \circ \hdots  \circ \beta_1^{-1}\circ  \alpha_1^{-1} \circ  \beta_1 \circ \alpha_1\text{.}
\end{equation*}
In other words,
\begin{equation*}
\pi_1(S,x) = \left \langle  [\alpha_i],[\beta_i] \;|\; [\tau_{\EuScript{M}}] = 1  \right \rangle\text{.}
\end{equation*}



Next we formulate --- in the language of bigons ---  the statement that the path $\tau_{\EuScript M}$ can be collapsed to the point $x$ in such a way that the collapsing homotopy parameterizes the surface $S$. The challenge is that such a homotopy cannot simultaneously be a bigon and a good parameterization. We propose the following notion.


\begin{definition}
\label{def:fundamentalbigon}
A \emph{fundamental bigon} with respect to the marking $(x,\EuScript M)$ is a bigon $\Sigma: \tau_{\EuScript{M}} \Rightarrow \id_x$ such that there exist:
\begin{enumerate}[(a)]

\item 
a polygon $\mathcal{P} \subset \R^2$ and a surjective smooth map $\pi: \mathcal{P} \to S$ that is an embedding when restricted to the interior of $\mathcal{P}$ and preserves the orientations. 

\item
a surjective continuous map $k: [0,1]^2 \to \mathcal{P}$ that restricts to a diffeomorphism between the interiors and preserves the orientations, such that there exists a vertex $v_0$ of $\mathcal{P}$ with $v_0=k(s,0)=k(s,1)=k(1,t)$ for all $0 \leq s,t\leq 1$.


\item
a smooth map $h: [0,1] \times \mathcal{P} \to S$ with $h_0 = \pi$ and $h_1 \circ k  = \Sigma$, such that for each edge $e$ of $\mathcal{P}$ the restriction $h|_{[0,1] \times e}$ has rank one, and $h(-,v)=x$ for each vertex $v$. 

\end{enumerate}
\end{definition}

In this definition the polygon $\mathcal{P}$ serves as the standard parameter domain of the surface, and the map $\pi: \mathcal{P} \to S$ is such a parameterization. The map $k: [0,1]^2 \to \mathcal{P}$ is responsible for the transition between  the standard parameter domain $\mathcal{P}$ and the parameter domain $[0,1]^2$ for bigons. 
The map $h$ ensures that the fundamental bigon $\Sigma$ is homotopic to the \quot{bigonized} standard parameterization, $\pi \circ k$. The various conditions on $k$ and $h$ ensure that the homotopy $h \circ k$ is constantly equal to $x$ over the boundary parts of $[0,1]^2$ that are parameterized by $(s,0)$, $(s,1)$, and $(1,t)$, and ensure that it restricts to a thin homotopy between the path $(\pi \circ k)(0,-)$ and $\tau_{\EuScript M}$ over the remaining boundary part $(0,t)$. 



\begin{comment}
such that there exist
\begin{enumerate}[(a)]

\item 
a smooth surjective map $\pi: \mathcal{P}_{4g} \to S$ whose restriction to the interior is an embedding. 



\item
a smooth map $h: [0,1] \times \C \to S$ such that $h_0|_{\mathcal{P}_{4g}} = \pi$ and $h_1|_{[0,1]^2} = \Sigma$.

\end{enumerate}



that there exists  a regular deformation of $\Sigma$: a map $f:[0,1]^2 \to S$ with the following properties:
\begin{enumerate}[(i)]

\item 
It is a fixed-ends-homotopy between the path $\tau_f(t) := f(0,t)$ and $\id_x$.  That is, it satisfies  $f(s,0)=f(s,1)=f(1,t)=x$ for all $s,t$. 

\item
It is a regular parameterization of $S$. That is, $f$ is continuous and surjective and a smooth embedding when restricted to the interior $(0,1)^2$. 

\item
It represents the bigon $\Sigma$ up to homotopy. That is, there exists a smooth map $h:[0,1] \times [0,1]^2 \to S$ such that $h(\sigma,s,0)=h(\sigma,s,1)=h(\sigma,1,t)=x$, such that $h(0,s,t)=f(s,t)$ and $h(1,s,t)=\Sigma(s,t)$, and such that the homotopy $h(-,0,-)$ between $\tau_f$ and $\tau_{\EuScript M}$ is thin.  

\end{enumerate}
\end{comment}

A marking will be called \emph{good}, if it admits a fundamental bigon. The following three lemmata elaborate some properties of good markings and fundamental bigons. 

\begin{lemma}
Every closed oriented surface $S$ has a good marking.
\end{lemma}

\begin{proof}
It is well-known that every surface $S$ of positive genus $g>0$ has a \quot{fundamental polygon} $\mathcal{P}\subset \C$ with $4g$ edges, together with a map $\pi: \mathcal{P} \to S$ that has all  required properties. It can be arranged such that all vertices go to a single point $x\in S$, and ---
if the $4g$ edges are parameterized by $A_1,B_1,A_1',B_1',A_2,...: [0,1] \to \mathcal{P}$ in counter-clockwise order starting at a vertex $v_0$ --- then \begin{equation}
\label{pathrel}
\pi(A_i(1-t)) = \pi(A_i'(t))
\quand
\pi(B_i(1-t)) = \pi(B_i'(t))\text{.}
\end{equation} 
Let $D \subset \C$ denote the disc centered at $-1\in \C$. It is obvious that $\mathcal{P}$ and $D$ are homeomorphic. The homeomorphism can be arranged such that
(i) it preserves orientations, (ii) 
it is a smooth embedding when restricted to the complement of the vertices of $\mathcal{P}$, and (iii)
the vertices map to points equidistantly distributed over the boundary of $D$, with $v_0$ at $0\in \C$.
We define
\begin{equation*}
k': [0,1]^2 \to D: (s,t) \mapsto (1-s)(e^{2\pi\mathrm{i}t}-1)\text{.}
\end{equation*}
Under the homeomorphism between $\mathcal{P}$ and $D$, this gives the map $k$ with all required properties.  


The map $h: [0,1] \times \mathcal{P} \to S$ is chosen such that $h_1: \mathcal{P} \to S$ is  constantly equal to $x$ in neighborhoods of all vertices, and such that \erf{pathrel} remains true with $h_1$ instead of $\pi$. Then we define
\begin{equation*}
\Sigma := h_1 \circ k
\end{equation*}
This is smooth because $h_1$ is locally constant at all points where $k$ is not smooth. We consider for $0 \leq k \leq 4g-1$ the map $p_{k}: [0,1] \to [0,1]: t \mapsto \frac{k+t}{4g}$ that squeezes the interval into the $k$-th of $4g$ many pieces. Then, we define for $i=1,..,g$
\begin{equation*}
\alpha_i := \pi\circ \Sigma(0,-) \circ p_{4i-4}
\quand
\beta_i := \pi \circ \Sigma(0,-) \circ p_{4i-3}\text{,} \end{equation*}
which give smooth maps with sitting instants, each going from  $x$ to $x$, Thus, $(x,\EuScript M)$ with $\EuScript M := \left \lbrace \alpha_i,\beta_i \right \rbrace$ is a marking, and \erf{pathrel} imply that $\Sigma$ is a bigon $\Sigma: \tau_{\EuScript M} \Rightarrow \id_x$. 


The case of genus $g=0$ can be treated in a similar way using the disc $D_1$ with one marked point; this is left as an  exercise.
\end{proof}

 
 






The main idea behind the definition of a fundamental bigon is that the integral of a 2-form  $\omega\in \Omega^2(S)$ over $S$ can be computed over a fundamental bigon.

\begin{lemma}
\label{fundamentalbigonintegral}
Suppose $S$ is a closed oriented surface with a good marking $(x,\EuScript M)$. Let $\Sigma$ be a fundamental bigon with respect to $(x,\EuScript M)$. Then,
\begin{equation*}
\int_S \omega = \int_{[0,1]^2}\Sigma^{*}\omega
\end{equation*}
for all 2-forms $\omega \in \Omega^2(S)$.
\end{lemma}

\begin{proof}
We choose the structure  $(\mathcal{P},k,\pi,h)$ of  Definition \ref{def:fundamentalbigon}. Then, 
\begin{equation*}
\int_{S} \omega = \int_{\mathcal{P}} \pi^{*}\omega = \int_{\mathcal{P}} h_1^{*}\omega = \int_{\mathrm{int}(\mathcal{P})} h_1^{*}\omega = \int_{(0,1)^2} \Sigma^{*}\omega = \int_{[0,1]^2} \Sigma^{*}\omega \text{.}
\end{equation*}
The second equality holds because the homotopy $h$ between $h_0=\pi$ and $h_1$ has rank one on the boundary. The other equalities hold immediately due to the assumptions on all the involved maps. 
\end{proof} 

Finally, we show that the choice of a fundamental bigon is essentially unique. 

\begin{lemma}
\label{lem:choicefundamentalbigon}
Let $S$ be a closed oriented surface and  $(x,\EuScript{M})$ be a marking. Suppose $\Sigma \maps \tau_{\EuScript{M}} \Rightarrow \id_x$ and $\Sigma': \tau_{\EuScript{M}} \Rightarrow \id_x$ are two fundamental bigons with respect to the marking $(x,\EuScript{M})$. Then, $\Sigma$ and $\Sigma'$ are thin homotopy equivalent in the sense of Section \ref{sec:path2groupoid}. 
\end{lemma}

\begin{proof}
We choose for both fundamental bigons the structures $(\mathcal{P},k,\pi,h)$ and $(\mathcal{P}',k',\pi',h')$ of Definition \ref{def:fundamentalbigon}. We can assume that $\mathcal{P}=\mathcal{P}'$, since any two polygons are diffeomorphic, and such diffeomorphism can be absorbed into $\pi'$ and $k'$. We can assume that $\mathcal{P}$ is convex; in that case it is easy to see that $k$ and $k'$ are homotopic, with the homotopy  fixing the three boundary components that map to $v_0$, and restricting to a homotopy with values in $\partial P$ over the forth boundary component. 
\begin{comment}
The homotopy is given by
\begin{equation*}
H(\sigma,s,t) := \sigma k(s,t) + (1-\sigma)k(s,t)
\end{equation*}
\end{comment}
The homotopies $h$ and $h'$ restrict on the boundary to thin homotopies $\pi|_{\partial P} \simeq \tau_{\EuScript M}$ and $\pi'|_{\partial P} \simeq \tau_{\EuScript M}$. 
By a version of Alexander's trick, we obtain a smooth homotopy $\pi \simeq \pi'$ that fixes all vertices and has rank one over the edges. 
\begin{comment}
One first changes $\pi$ into a homotopic map $\tilde \pi$ that coincides with $\pi'$ over the boundary. One can still invert $\pi'$ to give a smooth map
\begin{equation*}
\alxydim{}{\mathrm{int}(\mathcal{P}) \ar[r]^-{\tilde\pi} & S\setminus \mathrm{im}(\pi'|_{\mathrm{int}(\mathcal{P})}) \ar[r]^-{\pi'^{-1}} & \mathrm{int}(\mathcal{P})}
\end{equation*}
and then extends that by the identity to a smooth map $\mathcal{P} \to \mathcal{P}$. By Alexander's trick, this map is homotopic to the identity. Composing with $\pi'$ gives a  homotopy between $\tilde\pi$ and $\pi'$ that fixes the boundary. Replacing $\tilde\pi$ by $\pi$ gives the claimed homotopy.
\end{comment}
Then we have chains of homotopies
\begin{equation*}
\Sigma \simeq h_1 \circ k \simeq h_0 \circ k \simeq \pi \circ k\simeq \pi \circ k' \simeq \pi' \circ k' \simeq h_0' \circ k' \simeq h_1' \circ k' \simeq \Sigma' 
\end{equation*}
which are all smooth and have rank one restricted over the boundary. By dimensional reasons, this homotopy can at most have rank two everywhere. This means that it is a thin homotopy between $\Sigma$ and $\Sigma'$.
\end{proof}




Next we come to the definition of surface holonomy. Since the generic transport 2-functor is not strict, we have to deal with the difference between the 1-morphism $\mathrm{tra}(\phi_{*}\tau_{\EuScript M})$ and the 1-morphism
\begin{equation*}
\mathrm{tra}_{\phi,\EuScript M} := \prod_{i=1}^g  \mathrm{tra}(\alpha_i) \circ \mathrm{tra}(\beta_i) \circ \mathrm{tra}(\alpha_i^{-1}) \circ \mathrm{tra}(\beta_i^{-1})\text{,}
\end{equation*}
for which we may agree for an arbitrary convention how to put parentheses in case $T$ has a non-trivial associator. The relation between these two 1-morphisms is given by a 2-morphism
\begin{equation*}
c^{\phi,\mathrm{tra}}: \mathrm{tra}_{\phi,\EuScript M} \Rightarrow \mathrm{tra}(\phi_{*}\tau_{\EuScript M}) 
\end{equation*}
made up from the compositors of $\mathrm{tra}$ in a unique way, due to the coherence axiom for compositors (this is axiom (F3) in \cite[Appendix A]{schreiber6}).


\begin{definition}
\label{def:surfaceholonomy}
Let  $\mathrm{tra}:\mathcal{P}_2(M) \to T$ be a transport 2-functor. Suppose
 $S$ is a closed oriented surface equipped with a good marking $(x,\EuScript{M})$ and a smooth map  $\phi:S \to M$. Let $\Sigma$ be a fundamental bigon for $(x,\EuScript{M})$. The 2-morphism
\begin{equation*}
\mathrm{Hol}_{\mathrm{tra}}(\phi,x,\EuScript{M}) := \mathrm{tra}(\phi_{*}\Sigma) \bullet c^{\phi,\mathrm{tra}}: \mathrm{tra}_{\phi,\EuScript M} \Rightarrow \mathrm{tra}(\id_{\phi(x)}) 
\end{equation*}
in $T$ is called the \emph{surface holonomy} of $\mathrm{tra}$. 
\end{definition}

Note that the surface holonomy  is independent of the choice of the fundamental bigon due to Lemma \ref{lem:choicefundamentalbigon}.
On the other hand, the  surface holonomy does depend on the choice of the  marking $(x,\EuScript{M})$. Even worse, it is not invariant under isomorphisms between transport 2-functors. It is the purpose of the following discussion to improve these dependence issues.
