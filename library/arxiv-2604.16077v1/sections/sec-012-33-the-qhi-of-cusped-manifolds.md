---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-012-33-the-qhi-of-cusped-manifolds
section_title: "The QHI of cusped manifolds"
section_number: 3.3
pages: 31-33
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.899
latex_coverage_ratio: 0.956
---
\label{sec:QHIcusped} The aim of this section is to introduce some general features of the QHI, provide links to the literature (thus explaining notations), and to explain the splitting formula of the QHI into the symmetry defects and the reduced QHI. We refer to \cite{GT} for the definition of the QHI of cusped manifolds by means of state sums over geometric branched ideal triangulations, and to \cite{AGT} for the general situation of non necessarily branched triangulations. The QHI of cusped manifolds used in this paper are those of \cite[Theorem 1.1]{AGT}, in the case where the bulk weights $h_f,h_c$ are zero, or are determined by the boundary weights $k_f,k_c$ (as for link complements). (By \cite[Corollary 1.8 (1)]{NA}, another choice of bulk weight would at worst modify these QHI by multiplication with a $4N$-th root of unity, which has no consequence on the results of this paper.)

Let $M$ be a cusped manifold. As usual we denote by $\bar{M}$ the compact manifold with interior $M$, $X(M)$ is the variety of {\it $PSL(2,\mc)$-characters of $M$}, and $X_{hyp}(M) \subset X(M)$ is the ``geometric'' irreducible component, containing the character $\rho_{hyp}$ of the complete hyperbolic holonomy (see Section \ref{GhypN}).

The QHI of $M$ are sequences of complex numbers $\Hh_N(M, \rho,k_c,k_f)$ modulo multiplication by $2N$-th roots of unity, indexed by the odd positive integers $N\geq 3$. The arguments of $\Hh_N(M, \rho,k_c,k_f)$ are:
\begin{itemize}
	\item[(i)] a character $\rho\in X_{hyp}(M)$, 
	\item[(ii)] classes $k_c\in H^1(\partial \bar{M},\mz)$ and $k_f\in H^1(\partial \bar{M},\mc)$ satisfying \eqref{fconstraint0}. 
\end{itemize}
The invariant $\Hh_N(M, \rho,k_c,k_f)$ is {\it computed} by the total contractions, denoted $\Hh_{N, (T,b,c)}$ and called {\it QHI state sums},  of certain tensor networks associated to the ideal triangulations $T$ of $M$, similarly as in the Turaev-Viro TQFTs. The QHI state sums are functions of combinatorial data on $T$ encoding $\rho\in X(M)$ and $k_c,k_f$ as in (i)-(ii): $\rho$ is encoded by a point $w_\rho$ of the gluing variety $G(T,b)$ (for some $b$), which is possible for most characters $\rho$ in $X_{hyp}(M)$ (see Remark \ref{mostrho}), and the classes $k_f$ and $k_c$ are a flattening weight and a charge weight, encoded by flattenings $f$ and charges $c$ as in Remark \ref{defflatcharge}-\ref{cfweight}. When $\rho$ is contained in $X_{hyp}(M)$ all the choices of $(T,b,w_\rho,c,f)$ eventually give the QHI state sums the same value, which by definition is $\Hh_N(M, \rho,k_c,k_f)$.

It is shown in \cite{NA} that, up to a possible stronger ambiguity modulo multiplication by $4N$th-roots of unity, which we denote by $=_{\mu_{4N}}$, we have a factorization into refined invariants (recall that $l\kappa := k_f-i\pi k_c$)
\begin{equation}\label{factQHIalphared}
	\Hh_N(M,\rho,k_f,k_c) =_{\mu_{4N}} \alpha_N(M,\rho,k_c;\mathfrak{s})\Hh_N^{red}(M,\rho,l\kappa;\mathfrak{s}),
\end{equation}
called respectively the {\it symmetry defect} and the {\it reduced} QHI. These refined invariants depend on an additional structure $\mathfrak{s}$ on $M$, called a {\it non ambiguous} structure, which is of topological nature ($\mathfrak{s}$ is an equivalence class of ideal triangulations under a restricted set of branched Pachner $2-3$ moves). The argument $l\kappa$ on the right side is the log weight, see \eqref{formulelkappa} and \eqref{deflkappa} (in \cite{NA} it was denoted $\kappa$, and called a fused weight). 

\begin{remark}\label{NAdefectmars25} {\rm When $M$ fibers over $S^1$, {\it any} fibration $\psi\colon M\ra S^1$ (with oriented fibers) defines a canonical non ambiguous structure $\mathfrak{s}_\psi$ on $M$, carried by the ideal triangulations of $M$ which are layered triangulations for the fibration (\cite[Prop. 6.3(1)]{NA}). Such triangulations are taut, which allows to associate to them a canonical charge, as in Remark \ref{defflatcharge}, whence a canonical charge weight $k_\psi$, as in Remark \ref{cfweight}, to the fibration (\cite[Prop. 4.3(2) and 4.8(2)]{NA}).  From the definition of the symmetry defect (\cite[page 808]{NA}), it is quite immediate to check that $\alpha_N(M,\rho,k_\psi;\mathfrak{s}_\psi)=_{4N} 1$ for every $\rho$, whence $\Hh_N(M,\rho,k_f,k_\psi) =_{\mu_{4N}} \Hh_N^{red}(M,\rho,k_f-i\pi k_\psi;\mathfrak{s}_\psi)$. Note, however, that the classes $k_\psi$ are very peculiar, and a layered triangulation can carry several (possibly taut) non ambiguous structures, that the symmetry defect $\alpha_N(M,\rho,k_c;\mathfrak{s})$ can distinguish (see the examples in \cite[Section 9]{NA}).} 
\end{remark}

Recall the relations \eqref{lkconstraint0}-\eqref{h2class}. By setting 
\begin{equation}\label{dconstraintclass} h_\rho(\gamma) := l\kappa(\gamma)-\Log(\delta_{w_\rho}(\gamma)) \in i\pi\mz
\end{equation}
and using that $l\kappa = k_f-i\pi k_c$ (see \eqref{deflkappa}), we can explain the notations of Theorem \ref{asyinvteo}:
\begin{equation}\label{HNdefh}
	\Hh_{N}(M,\rho,h_\rho,k_c) := \Hh_N(M,\rho,k_f,k_c).
\end{equation}

Now, for every class $a \in H^1(\partial \bar M; \pi i N \mz)$ we have $\Hh_N^{red}(M,\rho,l\kappa + a;\mathfrak{s}) = \Hh_N^{red}(M,\rho,l\kappa;\mathfrak{s})$ (see \cite[Theorem 1.6 (3)]{NA}). From this and \eqref{h2class} it follows that $\Hh_N^{red}(M,\rho,l\kappa;\mathfrak{s})$, regarded as a function of $l\kappa$, eventually depends only the boundary weight $\kappa\in H^1(\partial \bar M; \mc^*)$, defined in \eqref{kappaborddef}. We shall therefore denote
\begin{equation}\label{HNredkappamars25}
\Hh_N^{red}(M,\rho,\kappa;\mathfrak{s}):=\Hh_N^{red}(M,\rho,l\kappa;\mathfrak{s}).
\end{equation}
Recall that, since $\kappa$ is given by its values on a basis of $H_1(\partial \bar{M};\mz)$, the relations \eqref{lkconstraint0}-\eqref{h2class} show that $\kappa$ is a choice of $N$-th roots of the values of $\delta_{w_\rho}$ on these basis elements. Combining \eqref{factQHIalphared}, \eqref{HNdefh} and \eqref{HNredkappamars25} we can write
\begin{equation}\label{splitHNteo1.1}
\Hh_{N}(M,\rho,h_\rho,k_c) =_{\mu_{4N}} \alpha_N(M,\rho,k_c;\mathfrak{s})\Hh_N^{red}(M,\rho,\kappa;\mathfrak{s}).
\end{equation}
The invariant $\Hh_N(M,\rho,h_\rho,k_c)$ or $\Hh_N^{red}(M,\rho,\kappa;\mathfrak{s})$, for fixed $k_c$ and varying couple $(\rho,k_f)$, or fixed $\mathfrak{s}$ and varying couple $(\rho,\kappa)$ respectively, defines a rational function on the variety ${}_NX_{hyp}(M)$ of Section \ref{GhypN}  (\cite[Theorem 1.1]{AGT}, \cite[Corollary 1.8]{NA}). This function is obtained from the QHI state sums $\Hh_{N,(T,b,c)}$: these are rational functions on the space $G_{hyp,N}(T,b)$ defined in \eqref{GhypNdef}, and factor through the map $\widetilde{hol}$ in \eqref{grostildeholmars25}. 


\subsubsection{The case of $M=S^3\setminus 4_1$}\label{caseMsplitmars25} It follows immediately from definitions (see \cite[Section 8]{NA}) that $\alpha_N(M,\rho,k_c;\mathfrak{s})$ is in $PM(N)$, as defined in Section \ref{sec:sketchproof}, for every fixed $\rho\in X_{hyp}(M)$, $k_c\in H^1(\partial \bar M;\mz)$ and $\mathfrak{s}$. Because of the splitting \eqref{splitHNteo1.1}, the proof of Theorem \ref{asyinvteo} is therefore reduced to the asymptotic analysis of $\Hh_N^{red}(M,\rho,\kappa;\mathfrak{s})$ as $N\ra +\infty$.

Let us give the details of this argument for $M=S^3\setminus 4_1$. The invariant $\Hh_N^{red}(M,\rho,\kappa;\mathfrak{s})$ has a simple state sum $\Hh_{N}^{red}(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N})$ on the branched triangulation $(T,b)$ of Figure \ref{Teight}, given in \eqref{form1} below. In the notations of Section \ref{4_1} the couple $(\rho,\kappa)$ is encoded by the parameters 
$$\bu_{k,N} = \exp\left(\frac{1}{N}\left(\Log(u_k)+ \pi i (N+1)a_k\right)\right)\ ,\ \bv_{k,N} = \exp\left(\frac{1}{N}\left(\Log(v_k) + \pi i (N+1)b_k\right)\right)$$
for $k\in \{0,1\}$, where $u_k,v_k\in \mc_*$ are fixed shape parameters of the tetrahedra of $T$. The non ambiguous structure $\mathfrak{s}$ is defined by the branching $b$ of $T$, and was studied in \cite[Section 9.2]{NA} (where it was denoted $[(T,\omega_1)]$). The symmetry defect $\alpha_N(M,\rho,k_c;\mathfrak{s})$ is computed on $(T,b)$ by the monomial $(\bu_{0,N}^{-1}\bv_{0,N}^{-1})^{\frac{N-1}{2}}$ for a certain charge $c$.

From \eqref{splitHNteo1.1} and this discussion it follows that the state sum expression of $\Hh_{N}(M,\rho,h_\rho,k_c)$ on $(T,b)$ is \begin{equation}\label{ssumrednonred}
	\Hh_{N,(T,b,c)}(\bu_N,\bv_N) := (\bu_{0,N}^{-1}\bv_{0,N}^{-1})^{\frac{N-1}{2}}\Hh_{N}^{red}(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N}).
\end{equation}

\begin{lem}\label{lem:lim:sym:defect} We have:
$$\lim_{N\ra +\infty} \dfrac{2\pi}{N}\Log \left \vert (\bu_{0,N}^{-1}\bv_{0,N}^{-1})^{\frac{N-1}{2}} \right \vert =0.$$
\end{lem}

\begin{proof} Indeed
\begin{align*}
	\dfrac{2\pi}{N}\Log \left \vert (\bu_{0,N}^{-1}\bv_{0,N}^{-1})^{\frac{N-1}{2}} \right \vert 
	&= \dfrac{2\pi}{N} \frac{N-1}{2}\Log \left \vert (\bu_{0,N}^{-1}\bv_{0,N}^{-1}) \right \vert 
	\\
	&= -\pi \frac{N-1}{N^2}\mathfrak{R}(\Log (u_{0})+\Log (v_{0}))
\end{align*}
using the above expressions of $\bu_{k,N}$, $\bv_{k,N}$ in the last equality. The result follows.\end{proof}


\subsection{The QHI state sum of $M=S^3\setminus 4_1$}\label{sec:statesum} In this section we describe the formula of $\Hh_{N}^{red}(M,\rho,\kappa; \mathfrak{s})$ in the case of the figure-eight knot complement $M$, using the branched ideal triangulation $(T,b)$ of Figure \ref{Teight}.

Recall the lifted holonomy map $\widetilde{hol}$ in \eqref{grostildeholmars25}; by \eqref{Ghypcas41mars25} we have $G_{hyp,N}(T,b)=G_N(T,b)$. For any $\rho \in hol(G(T,b))\subset X_{hyp}(M)$ and compatible boundary weight $\kappa$, let $(\bu_0,\bu_1,\bv_0,\bv_1)\in G_N(T,b)$ (as in Section \ref{4_1}) be such that $\widetilde{hol}(\bu_0,\bu_1,\bv_0,\bv_1)=(\rho,\kappa)$.  Denote by $\mathfrak{s}$ the non ambiguous structure carried by $(T,b)$. 

By \cite[Section 6.4, page 912]{AGT0} and the formula \eqref{splitHNteo1.1}, the reduced QHI of $(M,\rho,\kappa;\mathfrak{s})$ can be expressed by the state sum 
\begin{align}
\Hh_{N}^{red}(M,\rho,\kappa; \mathfrak{s}) & =  \Hh_{N}^{red}(\bu_0,\bu_1,\bv_0,\bv_1)\notag \\
& =  \frac{g_N(\bu_0)g_N(\bv_0^*)^*}{|g(1)|^2}\sum_{\alpha,\beta=0}^{N-1}
  \zeta^{\beta^2-\alpha^2} \omega_N(\bu_0,\bu_1^{-1}\vert \beta)\
  \omega_N(\bv_0^*,\bv_1^*{}^{-1}\vert \alpha)^*\nonumber \\
& = \frac{g_N(\bu_0)g_N(\bv_0^*)^*}{|g(1)|^2}\ \Sigma_N(\bu_0,\bu_1)\ \Sigma_N(\bv_0^*,\bv_1^*)^*  \label{form1} .
\end{align}
where $^*$ denotes the complex conjugation, the functions $\omega_N$ and $g_N$ were defined in \eqref{functomegadef} and \eqref{gfunctiondef}, and we put
\begin{equation}\label{sumS}
\Sigma_N(\bu_0,\bu_1) = \sum_{\beta=0}^{N-1} \zeta^{\beta^2}
\omega_N(\bu_0,\bu_1^{-1}\vert \beta).
\end{equation}
