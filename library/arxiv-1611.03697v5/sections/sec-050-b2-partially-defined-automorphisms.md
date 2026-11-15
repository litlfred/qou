---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-050-b2-partially-defined-automorphisms
section_title: "B.2. Partially defined automorphisms"
section_number: null
pages: 44-45
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.631
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{tird}
Let $(\Gamma,Z,\Omega)$ be a  BPS structure, and fix a  convex sector $\Delta\subset \bC^*$. As above, we also fix  a norm $\|\cdot \|$ on the vector space $\Gamma\tensor_\bZ \bR$.

In the next subsection we will be interested in controlling Hamiltonian flows of functions on the twisted torus $\bT$  of the form $\DT(\gamma)\cdot x_\gamma$, for those classes $\gamma\in \Gamma$ satisfying $Z(\gamma)\in \Delta$. Thus it makes sense to define,  
for each real number $R>0$, a subset 
\[V_\Delta(R)=\big\{\xi\in \bT: \gamma\in \Gamma \text{ active with }  Z(\gamma)\in \Delta\implies |x_\gamma(\xi)|<\exp(-R \|\gamma\|)\big\}.\]
It is not clear that the subset $V_\Delta(R)\subset \bT$ is open in general, so we define $U_\Delta(R)$ to be its interior.
We note the obvious implications
\[R_2\geq R_1 \implies U_{\Delta}(R_2)\subseteq U_{\Delta}(R_1), \quad \Delta_2\supseteq \Delta_1 \implies U_{\Delta_2}(R)\subseteq U_{\Delta_1}(R).\]
We think of the open subsets $U_\Delta(R)\subset \bT$ as forming a system of neighbourhoods of   the boundary in some fictitious partial compactification of $\bT$.


\begin{lemma}
\label{dyl}
The open subset $U_\Delta(R)=\interior V_\Delta(R)\subset \bT$ is non-empty.
\end{lemma}

\begin{proof}
Take an element $z\in \Delta$.  Since $\Delta$ is acute we can find a constant $k>0$ such that
\[Z(\gamma)\in \Delta \implies \Re \big(Z(\gamma)/z\big) > k\cdot |Z(\gamma)|.\]
Take a point $\xi\in \bT$. Using the support property, we conclude that for any active class $\gamma\in \Gamma$ with $Z(\gamma)\in \Delta$, and all real numbers $S>0$, there are inequalities
\[|e^{-SZ(\gamma)/z}\cdot \xi(\gamma)| =e^{-S\Re (Z(\gamma)/z)}\cdot |\xi(\gamma)|<e^{-kS|Z(\gamma)|}\cdot |\xi(\gamma)|<e^{-cS\|\gamma\|}\cdot |\xi(\gamma)|,\]
for some universal constant $c>0$. Since the numbers $\|\gamma\|$ are bounded below, it follows that the element $e^{-SZ/z}\cdot \xi\in \bT$ lies in the subset $V_\Delta(R)$ for sufficiently large $S>0$. The  argument applies uniformly to all elements $\xi$ lying in a compact subset of $\bT$, so we conclude that $V_\Delta(R)$ has non-empty interior.
\end{proof}

Let us define a $\Delta$-map germ to be an equivalence class of holomorphic maps of the form $f\colon U_\Delta(R)\to \bT$, where two such maps $f_i\colon U_\Delta(R_i)\to \bT$  are considered to be equivalent if they agree on the intersection $U_\Delta(\max(R_1,R_2))$ of their domains. Thus a $\Delta$-map germ gives a partially-defined holomorphic map  $f\colon \bT\dashrightarrow \bT$ which is well-defined on  the open subset $U_\Delta(R)\subset \bT$ for all sufficiently large $R> 0$. A $\Delta$-map germ $f$ will be called bounded if for any $\epsilon>0$ one has
\begin{equation}\label{finger}f(U_\Delta(R+\epsilon))\subset U_\Delta(R)\end{equation}
for all sufficiently large $R>0$. 

It is clear  from \eqref{finger} that composition of such maps is well-defined and hence gives the set of  bounded $\Delta$-map germs the structure of a monoid. 
 We write  $\Aut_\Delta(\bT)$ for the group of invertible elements in this monoid, and call the elements of this group invertible bounded $\Delta$-map germs.  Elements of  $\Aut_\Delta(\bT)$ give  partially-defined holomorphic maps $f\colon \bT\dashrightarrow \bT$  with partially-defined inverses, 
 and hence give a precise meaning to the idea of a partially-defined automorphism of $\bT$.



\subsection{BPS automorphisms}

Let $(\Gamma,Z,\Omega)$ be a convergent BPS structure and fix  a  convex sector $\Delta\subset \bC^*$. Recall the definition of the formal series $\DT(\ell)$ associated to a ray  $\ell\subset \bC^*$ from Section \ref{raydiagram}. In this section we show that this series is absolutely convergent on suitable open subsets of $\bT$ and that the Hamiltonian flow of the resulting holomorphic function gives a partially-defined automorphism of $\bT$ in the precise sense described in the last subsection. 


\begin{prop}
\label{prop}
For all sufficiently large $R>0$ the following statements hold.
For each ray $\ell\subset \Delta$, the power series $\DT(\ell)$ is absolutely convergent on $U_\Delta(R)$, and hence defines a holomorphic function \[\DT(\ell)\colon U_\Delta(R)\to \bC.\]
Moreover the time 1 Hamiltonian flow of this function gives a holomorphic map
\[\bS(\ell)\colon U_\Delta(R)\to \bT\]
which defines an invertible, bounded  $\Delta$-map  germ.

\end{prop}

\begin{proof}
Take assumptions as in the statement and choose $\epsilon>0$. For convenience we choose the norm $\|\cdot \|$ on $\Gamma_\bZ \tensor \bR$ so that for all $\beta,\gamma\in \Gamma$ there is an inequality
\begin{equation}
\label{blbly}|\<\beta,\gamma\>|< \|\beta\|\cdot \|\gamma\|.\end{equation}
Take $R>0$  satisfying the conclusion of Lemma \ref{sven}.  Thus for each ray $\ell\subset \Delta$ we can choose  $M(\ell)>0$ such that
\begin{equation}
\label{thatwas}\sum_{Z(\gamma)\in \ell} \|\gamma\|^p \cdot |\DT(\gamma)|\cdot e^{-R \|\gamma\|}<M(\ell),\end{equation}
for each $p\in \{0,1,2\}$, and such that
\begin{equation}
\label{flfl}\sum_{\ell\subset \Delta} M(\ell)<\epsilon.\end{equation}

Since the $\|\gamma\|$ are bounded below,  the $p=0$ case of \eqref{thatwas} immediately implies that for each point $\xi\in U_\Delta(R)$
\begin{equation}
\label{again}\sum_{Z(\gamma)\in \ell}| \DT(\gamma)|\cdot  |x_\gamma(\xi)|< \sum_{Z(\gamma)\in \ell}| \DT(\gamma)|\cdot  e^{-R\|\gamma\|}<\infty,\end{equation}
 which proves that $\DT(\ell)$ is absolutely convergent.
 
 The Hamiltonian flow of $\DT(\ell)$ is defined by the differential equation
\begin{equation}
\label{ca}\frac{dx_\beta}{dt} =\{\DT(\ell),x_\beta\}=x_\beta \cdot \sum_{Z(\gamma)\in \ell}\DT(\gamma)\cdot \<\gamma,\beta\>\cdot x_\gamma.\end{equation}
Using \eqref{blbly} it follows
that  providing the flow stays in $U_\Delta(R)$ it satisfies
\begin{equation}
\label{co2}\Big|\frac{d}{dt}\log x_\beta\Big|\leq  \sum_{Z(\gamma)\in \ell} |\DT(\gamma) |\cdot \|\beta\|\cdot  \|\gamma\| \cdot e^{-R \|\gamma\|} <M(\ell)\cdot  \|\beta\|.\end{equation}

Let us consider an integral curve $\phi(t)$ for this flow which starts at some point $\phi(0)\in U_\Delta(R+\epsilon)$. We claim that this curve extends to all times $t\in [0,1]$ and remains in $U_\Delta(R)$. It follows from this that the time 1 Hamiltonian flow $\bS(\ell)$ exists, and defines a holomorphic map
\[\bS(\ell)\colon U_\Delta(R+\epsilon)\to U_\Delta(R).\]
Since we can make $\epsilon>0$ arbitrarily small by increasing $R>0$, the resulting $\Delta$-map germ is  bounded. 
 Considering the opposite flow then shows that the map is invertible, which completes the proof of Proposition \ref{prop}.
 
 To prove the claim, let us define $t_0\in [0,1]$ to be the supremum of $s\in [0,1]$ such that the integral curve $\phi(t)$ can be extended to a map $\phi\colon [0,s]\to U_\Delta(R)$. We obtain an integral curve $\phi\colon [0,t_0)\to U_\Delta(R)$. Equation \eqref{co2} implies that\begin{equation}
\label{curry}e^{-M(\ell) \cdot \|\beta\|}\cdot  |x_\beta(\phi(0))|\leq |x_\beta(\phi(t))|\leq e^{M(\ell) \cdot \|\beta\|}\cdot  |x_\beta(\phi(0))|\end{equation}
for  $0\leq t<t_0$. Thus the flow stays in the compact subset of $\bT$ defined by these inequalities, and hence extends to a flow $\phi\colon [0,t_0]\to \bT$. Applying \eqref{curry} 
to the  active classes $\beta\in \Gamma$ then shows that  $\phi(t_0)\in U_\Delta(R)$. But now local existence of solutions to \eqref{ca} shows that we can extend the flow a little further, which contradicts  the definition of $t_0$ unless $t_0=1$. This proves the claim.\end{proof}
