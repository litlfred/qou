---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-001-motivations
section_title: "Motivations"
section_number: null
pages: 1-3
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.989
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
The idea of the \emph{formal deformation quantization} program \cite{BFFLS}, initiated by Bayen, Flato, Fronsdal, Lichnerowicz and Sternheimer, is to generalize the Weyl product to an arbitrary symplectic (or Poisson) manifold. In this context, the framework of quantum mechanics is the same as classical mechanics, observables are the same, and quantization arises as a \emph{deformation} of the algebra of functions on the manifold, from a commutative to a non-commutative one.

\noindent A {\sl formal star product} (or {\sl deformation quantization}) of a symplectic manifold $(M,\omega)$
is an associative $\C[[\hbar]]$-bilinear product:
\begin{equation}
\star:C^\infty(M)[[\hbar]]\times C^\infty(M)[[\hbar]]\longrightarrow C^\infty(M)[[\hbar]]:(u,v)\mapsto u\star v
\end{equation}
such that, for $u,v\in C^\infty(M)$, the formal series
\begin{equation}\label{DefStar}
u\star v\;=\;\sum_{k=0}^\infty\,\hbar^k\,C_k(u,v)
\end{equation}
involves bi-differential operators $C_k:C^\infty(M)\times C^\infty(M)\to C^\infty(M)$
satisfying the following properties:
\begin{enumerate}
\item[(i)] $C_0(\,u\,,\,v\,)\;=\;u\,v$
\item[(ii)] $C_1(u,v)-C_1(v,u)\;=\;2i\{\,u\,,\,v\,\}$ where $\{\,,\,\}$ denotes the Poisson
bracket on $C^\infty(M)$ associated to $\omega$.
\end{enumerate}
Two such star products $\star^i\quad (i=1,2)$ on the same symplectic manifold $M$ are called {\sl equivalent} if there exists a formal series of the form 
\begin{equation}
T\;=\;I\,+\,\sum_{k=1}^\infty\hbar^k\,T_k
\end{equation}
where the $T_k$'s are differential operators on $C^\infty(M)$ such that for all $u,v\in C^\infty(M)$, one has
\begin{equation}
u\star^2v\;=\;T\,(\,T^{-1}u\star^1T^{-1}v\,)\;;
\end{equation}
the latter expression will be shortened by $\star^2=T(\star^1)$.

\noindent The first existence proofs were given in the 80's independently by Dewilde-Lecomte, Fedosov and 
Omori-Maeda-Yoshioka \cite{DW, Fe, OMY}. 
Equivalence classes of star products on a symplectic manifold are in 1-1 correspondence with the space
of formal series with coefficients in the second de Rham cohomology space of $M$ \cite{BCG, NT}.

\noindent The most important example of star product is the so-called Moyal star product $\star^0_\hbar $ on the plane $\R^2$
endowed with its standard symplectic structure $\Omega$:
\begin{eqnarray}\label{asympt}
 u \star^0_\hbar v &:=& u.v + i\frac \hbar 2\{ u,v \} +
 \underset{k=2}{\overset{\infty}\sum}\frac{(i\,\hbar/2)^k}{k!} \Omega^{i_1
 j_1}\cdots \Omega^{i_k j_k} \partial_{i_1\cdots i_k}u \partial_{j_1\cdots
 j_k}v \quad,\\
 \label{MoyalAsympt}
& = &\sum_{k=0}^{\infty} \, \frac{(i\,\hbar/2)^k}{k!}
\sum_{p=0}^{k}(-1)^{p} \,
\frac{k!}{p!(k-p)!}\, \partial_a^{k-p} \partial_\ell^p u \,
\partial_a^{p} \partial_\ell^{k-p} v  \quad ,
\end{eqnarray}
where \begin{equation}\label{PoissonBrackAN}
 \Omega_{ik}\Omega^{kj}=-\delta_i^k\qquad,\qquad \{ u,v \}=\Omega^{ij}\partial_iu\partial_jv: = \partial_a u \partial_\ell v - \partial_\ell u \partial_a
  v \quad.
  \end{equation}
\noindent In the context of formal deformation quantization, one does not worry about the convergence of the series (\ref{DefStar}). In particular, a formal star product does not, in general, underlie any operator algebraic or spectral theory. However, situations exist where star products occur as asymptotic expansions of operator calculi. The most known example is provided by the Weyl product which has the following integral representation:
\begin{equation}\label{IntMoy}
 (u \star^W v)(x) = (\pi\,\hbar)^{-2n} \int_{\R^{2n}\times \R^{2n}} \, u(y) v(z) \, e^{  i\frac{2}{\hbar} S^0(x,y,z)} dy dz,  
\end{equation}
where
\begin{equation}\label{Wphase}
  S^0(x,y,z)  =  \Omega (x,y) + \Omega (y,z) + \Omega (z,x), 
\end{equation}
$\Omega$ denoting the standard symplectic two-form on $\R^{2n}$. The product represented by \re{IntMoy} enjoys an important property: it is internal on the Schwartz space, the space of rapidly decreasing functions, on $\R^{2n}$\cite{Hansen}. Thus, the product of two (Schwartz) functions is again a (Schwartz) function ---rather than a formal power series as in the formal context. Such a situation will be referred to as {\sl non-formal deformation quantization}. Note that Moyal's star product (\ref{asympt}) can be defined as  a formal asymptotic expansion
of Weyl's product.

\noindent  In this paper, we will be interested in {\sl invariant} deformation quantizations. When a group $\LL$ acts on $M$ by symplectomorphisms, a star product is saaid to be $\LL$- {\sl invariant}
if for all $g\in\LL$, $u,v\in C^\infty(M)$:
\begin{equation}
g^\star(u\star v)\;=\;g^\star u\star g^\star v\;.
\end{equation}
When $\LL$ preserves a symplectic connection $\nabla$ on $M$:
\begin{equation}
\LL\subset\mbox{\rm Aff}(\nabla)\cap\mbox{\rm Symp}(\omega)\;,
\end{equation}
then, Fedosov's construction yields an $\LL$-invariant star product. The notion of equivalence
of $\LL$-invariant star products is the same as above except that each differential operator $T_k$
is required to commute with the action of $\LL$. The set of $\LL$-equivariant equivalence classes
of $\LL$-invariant star products is in this case parametrized by the space $H^2_{\mbox{\rm dR}}(M)^\LL[[\hbar]]$
of series with coefficients in the classes of $\LL$-invariant 2-forms on $M$ \cite{BBG}.

\vspace{2mm}

\noindent Although the study of deformation quantization admitting  a given symmetry is natural, one may 
mention important specific situations where the symmetric situation is relevant. 
Firstly, the observable algebra of a conformal field theory defines an algebra of vertex operators. Thus any finite dimensional limit of such a theory must contains some remanent of this structure. In particular if the limit procedure is equivariant the remanent will also be symmetric. For instance, in the seminal work of Seiberg and Witten [\cite{SeibWitt}] it is shown that , in the limit of a large B-field on a flat brane, the limit of the vertex operator algebra is an associative invariant product on the space of functions on the brane that has the symmetry of the initial brane and fields configuration. Accordingly it becomes natural to inquire about all the associative composition law of functions compatible with a given symmetry group (especially for non-compact symmetries). Actually, let us emphasize that our considerations go beyond string theory, but concern any Kac-Moody invariant theory.

\noindent Moreover, it is known since the seminal works \cite{ConnesDouglas,SeibWitt} that noncommutative geometry (and deformation theory) has intricate links with string theory. A manifestation of this statement stems from the fact that, in flat space-time, the worldvolume of a D-brane, on which open strings end, is deformed into a noncommutative manifold in the presence of a $B$-field. In particular, in the limit in which the massive open string modes decouple, the operator product expansion of open string tachyon vertex operators is governed by the Moyal-Weyl product\cite{SeibWitt, SchomDefQ}. This can be schematically written as
$ {\rm e}^{i P.X}(\tau)  {\rm e}^{i Q.X}(\tau') \sim ({\rm e}^{i P.X} \overset{M}{\star} {\rm e}^{i Q.X})(\tau')$, where $X$ represents the string coordinates on the brane, $P$ and $Q$ the momenta of the corresponding string states, $\tau$ and $\tau'$ parameterize the worldsheet boundary, and where the classical limit $f \overset{M}{\star} g \ra f.g$ is recovered for $B \ra 0$. It is not clear how this generalizes to an arbitrary curved string background supporting D-brane configurations. Nevertherless, some particular examples have been tackled in the litterature. The SU(2) WZW model for instance supports symmetric D-branes wrapping $S^2$ spheres in the $SU(2)$ group manifold. It has been shown that in an appropriate limit the worldvolume of these branes are deformed into fuzzy spheres \cite{AleksReckSchom2, AleksReckSchom1, AleksReckSchom3, Schomerus:2002dc}. The latter fuzzy spheres can be related to the Berezin/geometric quantization
of $S^2$ hence to star product theory (see \cite{PierreJan} and references therein). The appearance of noncommutative structures was also pointed out in relation with other backgrounds, like the Melvin Universe \cite{Hashimoto:2005hy,Hashimoto:2002nr,Halliday:2006qc,Behr:2003qc,Cai:2002sv,Cai:2006td,Cai:1999aw} or the Nappi-Witten plane wave \cite{Halliday:2006qc,Halliday:2005zt}, see e.g. \cite{Szabo:2006wx} for a recent review. Another model that has attracted much attention in recent years is the $\SL$ WZW model, describing string propagation on $AdS_3$ (and its euclidian counterpart, the $H_3^+$ model), see e.g. \cite{MO} and \cite{Teschner1}. This model has played, and still plays an important role in the understanding of string theory in non-compact and curved space-times. It appears as ubiquitous when dealing with black holes in string theory and is also particularly important in connection with the AdS/CFT correspondence. In this perspective, much effort has been devoted in studying the D-brane configurations this model can support (see e.g. \cite{Bachas:2000fr}). The most simple and symmetric D-branes in $AdS_3$ turn out to wrap $AdS_2$ and $H_2$ spaces in the $\SL$ group manifold. The question 
one could then ask is: what is the low energy effective dynamics of open string modes ending on such branes? By analogy with the flat case, it seems not unreasonable to expect a field theory defined on a noncommutative deformation of the D-branes' worldvolume. This deformation would have to enjoy some properties, namely to respect the symmetries of the model, just like the Moyal product and the fuzzy sphere construction do in their respective cases. 

\noindent In the present paper, we will be concerned with the specific situation of formal and non-formal deformation quantizations of  the hyperbolic plane. In this particular case, a third motivation relies on the relevance of the hyperbolic plane in the study of Riemann surfaces through the uniformization theorem (establishing the hyperbolic plane $\DD$  as the metric universal covering space of every constant curvature hyperbolic surface). Therefore, invariant deformations of the Poincar\'e disk could constitute a step towards a spectral theory of non-commutative Riemann surfaces.
