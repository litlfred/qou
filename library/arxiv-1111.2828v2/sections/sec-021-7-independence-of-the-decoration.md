---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-021-7-independence-of-the-decoration
section_title: "Independence of the decoration"
section_number: 7
pages: 22-26
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.962
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{decorationsection}

We now show that the extended Bloch group element of a decorated 
representation is independent of the decoration. We first prove that 
we can choose logarithms of the Ptolemy coordinates independently, 
without affecting the extended Bloch group element.

\begin{definition} 
Let $c\colon\dot\Delta^k_n(\Z)\to \C^*$ be a Ptolemy assignment. A \emph{lift} 
of $c$ is an assignment $\widetilde c\colon\dot\Delta^k_n(\Z)\to\C$ such 
that $\exp(\widetilde c)=c$.
\end{definition}

For any lift $\widetilde c$ of a Ptolemy assignment $c$ on $\Delta^3_2$, we have a flattening
\begin{equation}\lbl{cwidetilde}
\lambda(\widetilde c)=(\widetilde c_{03}+\widetilde c_{12}
-\widetilde c_{02}-\widetilde c_{13},\widetilde c_{01}+\widetilde c_{23}
-\widetilde c_{02}-\widetilde c_{13})\in\widehat\C.
\end{equation}

\begin{definition} 
The \emph{log-parameters} of a flattening 
$(e,f)\in\widehat\C$ are defined by
\begin{equation}\lbl{logparameters}
w_{ij}=\begin{cases}e&\text{ if }ij=01\text{ or }ij=23\\
-f&\text{ if }ij=12\text{ or }ij=03\\-e+f&\text{ if }ij=02\text{ or }ij=13.
\end{cases}
\end{equation}
\end{definition}

\begin{lemma}
\lbl{addtwopi} 
Let $\widetilde c\colon\dot\Delta^3_2(\Z)\to\C$ be a lifted Ptolemy assignment, and let 
$w_{ij}$ be the log-parameters of $\lambda(\widetilde c)$. Fix 
$i<j\in\{0,\dots,3\}$ and let $\widetilde c^\prime$ be the lifted Ptolemy 
assignment obtained from  $\widetilde c$ by adding $2\pi\sqrt{-1}$ to 
$\widetilde c_{ij}$. Then
\begin{equation}
\lambda(\widetilde c^\prime)-\lambda(\widetilde c)=\chi(w_{ij}
+2\pi\sqrt{-1}\delta_{ij}),
\end{equation}  
where $\delta_{ij}$ is $1$ if $ij=02$ or $13$ and $0$ otherwise.
\end{lemma}

\begin{proof} 
Denote the flattening $\lambda(\widetilde c)$ by $(e,f)$. If $ij=03$ or 
$12$, it follows from \eqref{cwidetilde} that $\lambda(\widetilde c^\prime)
=(e+2\pi\sqrt{-1},f)$. Similarly, $\lambda(\widetilde c^\prime)
=(e,f+2\pi\sqrt{-1})$ if $ij=01$ or $23$, and $\lambda(\widetilde c^\prime)
=(e-2\pi\sqrt{-1},f-2\pi\sqrt{-1})$ if $ij=02$ or $13$. By 
Lemma~\ref{chipqlemma},
\begin{equation}
\begin{aligned}
(e+2\pi\sqrt{-1},f)-(e,f)=&\chi(-f)\\ (e,f+2\pi\sqrt{-1})-(e,f)=&\chi(e)\\
(e-2\pi\sqrt{-1},f-2\pi\sqrt{-1})=&\chi(-e+f+2\pi\sqrt{-1}).
\end{aligned}
\end{equation} 
This proves the result.
\end{proof}

Let $\widetilde c$ be a lift of a Ptolemy assignment $c$. For each 
$\alpha\in \Delta^3_{n-2}(\Z)$, $\widetilde c$ induces a lift $\widetilde c_\alpha$ 
of $c_\alpha$. Consider the element 
\begin{equation}\lbl{tauinPhat}
\tau=\sum_{\alpha\in \Delta^k_{n-2}(\Z)}\lambda(\widetilde c_\alpha)\in\widehat\Pre(\C).
\end{equation}
Fix a point $t_0\in\dot\Delta^k_n(\Z)$. We wish to understand the effect 
on $\tau$ of adding $2\pi\sqrt{-1}$ to $\widetilde c_{t_0}$. This changes 
$\tau$ into an element $\tau^{\prime}\in\widehat\Pre(\C)$. Let $w_{ij}(\alpha)$ 
denote the log-parameters of $\lambda(\widetilde c_\alpha)$. Note that $t_0$ 
either lies on an edge, on a face, or in the interior of $\Delta^3_n$. 

\begin{lemma}
\lbl{edgepoint} 
Suppose $t_0$ is on the edge $ij$ of $\Delta^3_n$. Then 
\begin{equation}\tau^{\prime}-\tau=\chi(w_{ij}(\alpha)+2\pi\sqrt{-1}\delta_{ij}),
\end{equation}
where $\alpha=t-e_i-e_j$, (i.e.~$\alpha$ is such that $t_0$ is an edge point 
of $\Delta^3(\alpha)$).
\end{lemma}

\begin{proof}
This follows immediately from Lemma~\ref{addtwopi}.
\end{proof}

\begin{lemma}
\lbl{facepoint} 
Suppose $t_0$ is on a face opposite vertex $i$. Then 
$\tau^\prime-\tau=(-1)^i\chi(\kappa+2\pi\sqrt{-1})$, where $\kappa$ is given by
\begin{equation}
\kappa=\widetilde c_{\eta_i(0,-1,1)}-\widetilde c_{\eta_i(0,1,-1)}-\big(\widetilde 
c_{\eta_i(-1,0,1)}-\widetilde c_{\eta_i(1,0,-1)}\big)+\widetilde c_{\eta_i(-1,1,0)}
-\widetilde c_{\eta_i(1,-1,0)},
\end{equation}
where $\eta_i$ inserts a zero as the $i$th vertex.
\end{lemma}

\begin{proof}
For simplicity assume $i=0$. The other cases are proved similarly.
There are exactly three $\alpha$'s for which $t_0$ is an edge point of 
$\Delta^3(\alpha)$. These are
\begin{equation}
\lbl{alphais}
\alpha_0=t_0-(0,0,1,1),\quad\alpha_1=t_0-(0,1,0,1),\quad\alpha_2=t_0-(0,1,1,0).
\end{equation}  
Note that $\widetilde c_t=(\widetilde c_{\alpha_0})_{23}
=(\widetilde c_{\alpha_1})_{13}=(\widetilde c_{\alpha_2})_{12}$.
Since adding $2\pi\sqrt{-1}$ to $\widetilde c_{t_0}$ leaves $\widetilde c_\alpha$ unchanged unless $\alpha\in\{\alpha_0,\alpha_1,\alpha_2\}$, Lemma~\ref{addtwopi} implies that
\begin{equation}
\tau^\prime-\tau=\chi(w_{23}(\alpha_0))+\chi(w_{13}(\alpha_1)+2\pi\sqrt{-1})+\chi(w_{12}(\alpha_2)).
\end{equation}
One easily checks that
\begin{equation}
\lbl{firstthree}
\begin{gathered}
w_{23}(\alpha_0)=\widetilde c_{(1,0,-1,0)}+\widetilde c_{(0,1,0,-1)}-\widetilde c_{(1,0,0,-1)}-\widetilde c_{(0,1,-1,0)}\\
w_{13}(\alpha_1)=\widetilde c_{(1,0,0,-1)}+\widetilde c_{(0,-1,1,0)}-\widetilde c_{(1,-1,0,0)}-\widetilde c_{(0,0,1,-1)}\\
w_{12}(\alpha_2)=\widetilde c_{(1,-1,0,0)}+\widetilde c_{(0,0,-1,1)}-\widetilde c_{(1,0,-1,0)}-\widetilde c_{(0,-1,0,1)},
\end{gathered}
\end{equation}
from which the result follows.
\end{proof}

\begin{lemma}
\lbl{interiorpoint} 
If $t_0$ is an interior point, $\tau^\prime=\tau$.
\end{lemma}

\begin{proof}
If $t_0$ is an interior point, there are six $\alpha$'s for which $t_0$ is an edge point of $\Delta^3(\alpha)$.
These are $\alpha_0$, $\alpha_1$ and $\alpha_2$ as defined in \eqref{alphais} as well as 
\begin{equation}
\alpha_3=t_0-(1,1,0,0),\quad \alpha_4=t_0-(1,0,1,0),\quad \alpha_5=t_0-(1,0,0,1).
\end{equation}
Again, by Lemma~\ref{addtwopi}
\begin{multline}\lbl{intpoint}
\tau^\prime-\tau=\chi(w_{23}(\alpha_0))+\chi(w_{13}(\alpha_1)+2\pi\sqrt{-1})+\chi(w_{12}(\alpha_2))+\\\chi(w_{01}(\alpha_3))+\chi(w_{02}(\alpha_4)+2\pi\sqrt{-1})+\chi(w_{03}(\alpha_5)).
\end{multline}
Using \eqref{firstthree} as well as
\begin{equation}
\begin{gathered}
w_{01}(\alpha_3)=\widetilde c_{(0,-1,0,1)}+\widetilde c_{(-1,0,1,0)}-\widetilde c_{(0,-1,1,0)}-\widetilde c_{(-1,0,0,1)}\\
w_{02}(\alpha_4)=\widetilde c_{(0,1,-1,0)}+\widetilde c_{(-1,0,0,1)}-\widetilde c_{(0,0,-1,1)}-\widetilde c_{(-1,1,0,0)}\\
w_{03}(\alpha_5)=\widetilde c_{(0,0,1,-1)}+\widetilde c_{(-1,1,0,0)}-\widetilde c_{(0,1,0,-1)}-\widetilde c_{(-1,0,1,0)}
\end{gathered}
\end{equation}
we see that all terms in~\eqref{intpoint} cancel out. Hence, $\tau^\prime=\tau$.
\end{proof}

\begin{proposition}
\lbl{independenceoflog} 
Let $c$ be a Ptolemy assignment on $K$. For any lift $\widetilde c$ of $c$, the element
\begin{equation}\lbl{cwidetildeelement}
\lambda(\widetilde c)=\sum_i\sum_{\alpha\in \Delta^k_{n-2}(\Z)}\epsilon_i\lambda(\widetilde c^i_\alpha)\in\widehat\Pre(\C)
\end{equation}
is independent of the choice of lift. In particular, if $c$ is the Ptolemy assignment of a decorated representation $\rho$, $\lambda(\widetilde c)$ is the extended Bloch group element of $\rho$.
\end{proposition}

\begin{proof} 
Let $\widetilde c$ and $\widetilde c^\prime$ be lifts of $c$. Let 
$t_0\in\dot\Delta^3_n(\Z)$. We wish to prove that 
$\lambda(\widetilde c)=\lambda(\widetilde c^\prime)$. It is enough to prove 
this when $\widetilde c^\prime$ is obtained from $\widetilde c$ by adding 
$2\pi\sqrt{-1}$ to $\widetilde c_t$. If $t_0$ is an interior point, the 
result follows immediately from Lemma~\ref{interiorpoint}.
If $t_0$ is a face point, $t_0$ lies in exactly two simplices of $K$, and 
it follows from Lemma~\ref{facepoint} that the two contributions to the 
change in $\lambda(\widetilde c)$ appear with opposite signs (by~\eqref{bigdiagram}, 
$2\chi(2\pi\sqrt{-1})=0$). Suppose $t_0$ is an edge point. Let $C$ be the 
$3$-cycle obtained by gluing together all the $\Delta^3(\alpha)$'s having 
$t_0$ as an edge point, using the face pairings induced from $K$. Let $e$ 
be the (interior) $1$-cell of $C$ containing $t_0$. The argument in 
Zickert~\cite[Theorem~6.5]{ZickertDuke} shows that the total log-parameter 
around $e$ is zero. It thus follows from Lemma~\ref{edgepoint} that adding 
$2\pi\sqrt{-1}$ to $\widetilde c_{t_0}$ changes $\lambda(\widetilde c)$ by 
$2$-torsion which is trivial if and only if the number $n$ of simplices in 
$C$ for which $t$ is a $02$ edge or a $13$ edge is even. Consider a curve 
$\lambda$ in $C$ encircling $e$. The vertex ordering induces an orientation 
on each face of each simplex of $C$, such that when $\lambda$ passes through 
two faces of a simplex in $C$, the two orientations agree unless $e$ is a 
$02$ edge or a $13$ edge. Since $M$ is orientable, it follows that $n$ is even.
The second statement follows by letting $\widetilde c=\log c$.
\end{proof}

 
\begin{proposition}
\lbl{independenceofdec} 
The extended Bloch group element of a decorated 
boundary-unipotent representation is independent of the decoration.
\end{proposition}

\begin{proof}
By performing a barycentric subdivision if necessary, we may assume that any 
decoration is generic.
Fix a lift $\widetilde\Delta_i$ of each simplex $\Delta_i$ of $K$. A 
decoration $D$ assigns a coset $g_j^iN$ to each vertex $j$ of 
$\widetilde\Delta_i$. Suppose we have another decoration $D^\prime$ of $\rho$ 
with cosets $h_j^iN$. Since equivalent decorations have the same fundamental 
class, we may assume that $h_j^i=g_j^id_j^i$, where the $d_j^i$'s are diagonal 
matrices (see Remark~\ref{normalizerremark}). Let $c$ and $c^\prime$ denote the 
Ptolemy assignments on $K$ induced by $D$ and $D^\prime$. Suppose 
$d^i_j=\diag(d^i_{j0},\dots,d^i_{j,n-1})$. By \eqref{ctformula} we have 
\begin{equation}
c^{i\prime}_t=c^i_t\prod_{k=0}^{t_0}d^i_{0k}\prod_{k=0}^{t_1}d^i_{1k}
\prod_{k=0}^{t_2}d^i_{2k}\prod_{k=0}^{t_3}d^i_{3k}.
\end{equation}
Fix a lift $\widetilde c$ of $c$. Letting $\log$ denote a logarithm, 
define a lift $\widetilde c^\prime$ of $c^\prime$ by
\begin{equation}
\widetilde c^{\prime i}_t=\widetilde c^i_t+\sum_{k=0}^{t_0}\log(d^i_{0k})
+\sum_{k=0}^{t_1}\log(d^i_{1k})+\sum_{k=0}^{t_2}\log(d^i_{2k})+\sum_{k=0}^{t_3}\log(d^i_{3k}).
\end{equation}
Using this, one easily checks that $\lambda(c^i_\alpha)
=\lambda(c^{\prime i}_\alpha)$ for each $i$ and each $\alpha\in \Delta^3_{n-2}(\Z)$.



The result now follows from Proposition~\ref{independenceoflog}.
\end{proof}



\subsection{$p\SL(n,\C)$-decorations}
\lbl{sub.pSLdecorations}

Let $n$ be even. All results in this section have 
natural analogs for $p\SL(n,\C)$. The proofs of these are obtained by replacing 
$2\pi\sqrt{-1}$ by $\pi\sqrt{-1}$, and logarithms by lifts of 
$\C\xrightarrow{\exp}\C^*\big/\langle\pm 1\rangle$. In particular, we have

\begin{proposition} 
\lbl{pSLindependence}
The fundamental class $[\rho]\in\widehat\B(\C)_{\PSL}$ of a decorated boundary-unipotent representation $\rho\colon\pi_1(M)\to p\SL(n,\C)$ is independent 
of the decoration.\qed
\end{proposition} 



\section{A cocycle formula for $\widehat c$}
\lbl{sec.computationofchat}

Let $i_*\colon H_3(\SL(n,\C))\to H_3(\SL(n,\C),N)$ denote the natural map.
We wish to prove that the composition
\begin{equation}
\xymatrix{{H_3(\SL(n,\C))}\ar[r]^-{i_*}&{H_3(\SL(n,\C),N)}\ar[r]^-{\lambda}&
{\widehat\B(\C)}\ar[r]^-R&{\C/4\pi^2\Z}}
\end{equation}
equals the Cheeger-Chern-Simons class $\widehat c$. Note that $i_*$ is induced by the map $(g_0,\dots,g_3)\mapsto (g_0N,\dots,g_3N)$.

We shall make use of the canonical isomorphisms
\begin{equation}\label{canonicalisomorphisms}
H_3(\SL(n,\C))\cong H_3(\SL(3,\C))\cong H_3(\SL(2,\C))\oplus K_3^M(\C).
\end{equation}
The first isomorphism is induced by stabilization (see Suslin~\cite{Suslin1046}) and the second isomorphism 
is the $\pm$-eigenspace decomposition with respect to the transpose-inverse 
involution on $\SL(3,\C)$ (see Sah~\cite{Sah}).

\begin{lemma}
[Suslin~\cite{Suslin1046}]
\lbl{Milnorgenerator}
Let $D\subset\SL(3,\C)$ be the subgroup of diagonal matrices. The $K_3^M(\C)$ 
summand of $H_3(\SL(3,\C))$ is generated by the elements $B\rho_*([T])$, where 
$T=S^1\times S^1\times S^1$ is the $3$-torus, and $\rho\colon \pi_1(T)\to D$ is 
a representation.\qed
\end{lemma}

\begin{lemma}
\lbl{zeroonMilnor} 
Let $T=S^1\times S^1\times S^1$ and let $\rho\colon\pi_1(T)\to D$ 
be a representation.
The extended Bloch group element $[\rho]\in\widehat\B(\C)$ of $\rho$ is trivial.
\end{lemma}

\begin{proof}
We regard $T$ as a cube $C$ with opposite faces identified, and triangulate 
$C$ as the cone on the triangulation on $\partial C$ indicated in 
Figure~\ref{cubefigure} with cone point in the center. We order the vertices 
of each simplex by codimension, i.e.~the $0$-vertex is the cone point, the 
$1$-vertex is a face point etc. Let $\rho\colon\pi_1(T)\to D$ be a 
representation, and pick a decoration of $\rho$ by cosets in general 
position (the triangulation is such that this is always possible). 
Note that for every $3$-simplex $\Delta$ of $T$, there is a unique opposite 
$3$-simplex $\Delta^{\text{opp}}$, such that the faces opposite the cone point 
are identified. We may assume that the cone point is decorated by the coset 
$N$. If a simplex $\Delta$ is decorated by the cosets $(N,g_0N,g_1N,g_2N)$, 
the simplex $\Delta^{\text{opp}}$ must be decorated by the cosets 
$(N,dg_0N,dg_1N,dg_2N)$, where $d$ is the image of the generator of 
$\pi_1(T)$ pairing the faces of $\Delta$ and $\Delta^{\text{opp}}$. It thus 
follows from \eqref{cosetrep} that the fundamental class is represented by 
a sum of terms of the form
\begin{equation}
\lbl{terms}
(N,dg_0N,dg_1N,dg_2N)-(N,g_0N,g_1N,g_2N)\in C_3^{\gen}(\SL(n,\C)/N).
\end{equation}
Let $c$ and $c^\prime$ be the Ptolemy assignments associated to the tuples 
$(N\comma g_0N\comma g_1N\comma g_2N)$ and $(N\comma dg_0N\comma dg_1N\comma dg_2N)$. Letting 
$d=\diag(d_1,\dots,d_n)$, we have $c_t^\prime=c_t\prod_{i=t_0}^n d_i$. Fix a lift 
$\widetilde c$ of $c$, and consider the lift  
\begin{equation}
\widetilde c^\prime_t=\widetilde c_t+\sum_{i=t_0}^n\log(d_i)
\end{equation}
of $c^\prime$. One now checks that $\lambda(\widetilde c_\alpha^\prime)
=\lambda(\widetilde c_\alpha)$ for all $\alpha\in\dot\Delta^k_n(\Z)$, so 
$\lambda(\widetilde c)-\lambda(\widetilde c^\prime)=0$. This proves the result.
\end{proof}

\begin{theorem}
\lbl{formulaforchat} 
The composition $R\circ\lambda\circ i_*$ equals $\widehat c$.
\end{theorem}

\begin{proof}
Since $\lambda$ commutes with stabilization, it follows from Goette-Zickert~\cite{GoetteZickert} that $R\circ\lambda\circ i_*=\widehat c$ 
on $H_3(\SL(2,\C))$. Since $\widehat c$ is zero on $K_3^M(\C)$ (this follows 
from Lemma~\ref{Milnorgenerator} and 
\cite[Theorem~8.22]{CheegerSimons}), the result follows from~\eqref{canonicalisomorphisms} and
Lemma~\ref{zeroonMilnor}.
\end{proof}

\begin{figure}[htpb]
$$
\psdraw{SLrepFigures.6}{1.2in}
$$
\caption{Triangulation of $\partial C$.}\lbl{cubefigure}
\end{figure}

\begin{remark}\label{extensionremark}By defining $\widehat c=R\circ\lambda\colon H_3(\SL(n,\C),N)\to\C/4\pi^2\Z$, we have a natural extension of the 
Cheeger-Chern-Simons class to bundles with boundary-unipotent holonomy, and we can define the complex volume as in Definition~\ref{complexvolumedefn}.
\end{remark}
