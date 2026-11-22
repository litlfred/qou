---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-002-12-resurgence-in-complex-chern-simons-theory
section_title: "Resurgence in complex Chern-Simons theory"
section_number: 1.2
pages: 2-4
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.865
latex_coverage_ratio: 0.972
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
In what follows, we will identify the partition function of complex
Chern-Simons theory with the state integral of Andersen-Kashaev
in~\cite{AK}, following the ideas of Hikami, Dimofte et
al~\cite{Hikami,DGLZ}.  Although this identification has not been
derived from first principles, it turns out to have a number of
startling consequences. We will focus on manifolds of the form
$M= \mathbb{S}^3 \backslash \mathcal{K}$, where $\CK$ is a hyperbolic
knot.

Our goal is to give an explicit description of the resurgent structure
of the formal power series of perturbative Chern-Simons theory in
terms of a fundamental solution of a pair of linear $q$-difference
equation and a matrix of integers. We will describe the general story
first, and illustrate it with concrete examples later.

We will denote by $\calP$ the set of critical points of the complex
Chern-Simons action and by $\s$ a typical critical point.  Given our
identification of Chern-Simons theory with state integrals, it turns
out that the set $\calP$ coincides with the set of critical points of
the integrand of the state integral, an effectively computable set of
algebraic numbers. The critical values of the complex Chern-Simons
function are labeled by $\s$ and an integer $\mu$ (often called
``multicovering''):

\begin{equation}
  \label{actions}
  \text{CS}(\s;\mu) =
  {V(\s) \over 2\pi} - 2\pi {\ri} \mu, \qquad \mu \in \BZ. 
\end{equation}

We conjecture that the corresponding transseries $ \Phi_{\s, \mu}$
satisfy the translation invariance property

\begin{equation}
  \label{Phiqt}
  \Phi_{\s,\mu}(\tau) = \tq^\mu \, \Phi_{\s}(\tau), \qquad
  \tq = {\rm e}^{-2\pi {\rm i}/\tau}, 
\end{equation}

where $\Phi_{\s}(\tau)$ is the conventional asymptotic expansion of
the state integral around the saddle point $\s$. It has the form
 
\begin{equation}
  \label{phi-ex}
  \Phi_{\s}(\tau)=
  \exp\left( { V(\s) \over 2\pi \tau} \right) \varphi_\s (\tau),
  \qquad \varphi_\s (\tau) \in \BC[[\tau]]. 
\end{equation}

As a consequence, all the Stokes automorphisms acting on
$\Phi_{\s,\mu}$ are packaged in two Stokes automorphism matrices
$\ms{S}^{+}(q)$, $\ms{S}^-(q^{-1})$, which are matrices of $q$- and
$q^{-1}$-series respectively, and each of which encodes Stokes
automorphism across a half-plane.  Their detailed definition is given
in Section~\ref{sc:res}.



































An important feature of state integrals is that they depend on
additional parameters and this leads to a system of a pair of linear
$q$-difference equations, one in the upper half-plane and another in
the lower half-plane~\cite{GK:qseries}. In our examples, these linear
$q$-difference equations have explicit sets of fundamental
solutions. We conjecture that

\begin{conjecture}
  \label{conj.1}
  \rm{(a)} $\mathsf{S}^{\pm}(q)$ are bilinear functions of two
  fundamental solutions of the pair of linear $q$-difference
  equations. \newline 
  \rm{(b)} $\mathsf{S}^{\pm}(q)$ satisfy the inversion relation
  \begin{equation}
    \label{Ssym}
    \ms{S}^+(q)^T \ms{S}^-(q) = \md{1} \,.
  \end{equation}
  \rm{(c)} $\mathsf{S}^{\pm}(q)$ are uniquely determined by
  $\mathsf{S}^+(0)$, $\mathsf{S}^-(0)$ and a pair of fundamental
  solutions to the pair of linear $q$-difference equations.
\end{conjecture}

The above matrices $\mathsf{S}^{\pm}$ uniquely determine the collection of
transseries $\Phi_{\s,\mu}(\tau)$ for all $(\s,\mu)$ via an abstract
Riemann-Hilbert correspondence first pointed out in \cite{voros} and
developed recently in \cite{gmn,ims,ks-ar}. Note that this
transcendental correspondence converts the difficult problem of
computing coefficients of $\Phi_{\s,\mu}(\tau)$ (typically, one can
not compute more than a couple of hundred coefficients) into the much
easier problem of computing fundamental solutions of linear
$q$-difference equations, up to a matrix of unknown integers.

Given a hyperbolic knot $\CK$ there is a distinguished critical point
$\s_1$ (the geometric representation, corresponding to the complete
hyperbolic structure), and in that case we conjecture a precise
relation between the entry $\mathsf{S}^+_{\s_1,\s_1}(q)$ of the matrix
$\ms{S}^+(q)$ and the (rotated) 3D-index of
Dimofte-Gaiotto-Gukov~\cite{DGG1,DGG2}.

\begin{conjecture}
  \label{conj.2}
  We have:
  \begin{equation}
    \label{Sind}
    \mathsf{S}^+_{\s_1\s_1}(q) =  \,\Ind_\CK^\rot(q)\,.
  \end{equation}
\end{conjecture}

We recall that the 3D-index $\CI_\CK (m,e)(q)$ associated to a knot
$\CK$ is labeled by two integers $(m,e)$. It counts BPS states in a
three-dimensional, $\mathcal{N}=2$ supersymmetric theory $T_M$ which
can be associated to the manifold $M=\mathbb{S}^3\backslash \CK$
\cite{DGG1}.  The rotated index is then given by

\begin{equation}
  \Ind_\CK^\rot(q)=\sum_{e \in \IZ} \CI_\CK (0,e)(q). 
\end{equation}

The relation in \eqref{Sind} between the resurgent structure of
complex Chern--Simons theory and a counting of BPS states in the
corresponding supersymmetric theory was anticipated in
\cite{mm-s2019,ggm}.

We emphasize that although the state integrals and their perturbation
theory are well-defined, the above picture is largely conjectural.
However, it fits well with the work of Kontsevich-Soibelman~\cite{KS},
as well as with a lecture of Kontsevich on June 30, 2020
\cite{kontsevich-talk}, and it paves the way for a deeper
understanding of the topological/physical meaning of the integers
appearing in $\mathsf{S}^{\pm}$.





We should point out that the above theory in fact has little to do
with knots and 3-manifolds and complex Chern-Simons theory, and little
to do with the Bloch group, but appears to be part of a larger
combinatorial structure. This is apparent in the data needed to define
the formal power series of~\cite{DG,DG2} as well as the data needed to
define $q$-hypergeometric Nahm sums (and thus their asymptotic
expansion at roots of unity~\cite{GZ:asymptotics}) and the data needed
to define state integrals~\cite{GK:qseries}. This combinatorial
structure is sometimes called a $K_2$-Lagrangian, or an extended
symplectic group.

We will illustrate the above conjectures concretely for the invariants
of the two simplest hyperbolic knots, the $4_1$ and the $5_2$
knots. Some aspects of the resurgent structure of complex
Chern--Simons theory for the $4_1$ knot were studied in
\cite{gmp,gh-res}, but they focused on the ``classical" transseries
$\Phi_{\s}(\tau)$ (i.e. they didn't address the resurgent structure of
the tower of singularities). The resurgent problem in the case of
compact $\SU(2)$ Chern--Simons theory was addressed in \cite{CG, gmp},
where complete towers of Stokes constants were explicitly computed for
some Seifert three-manifolds.

This paper is, in a sense, a sequel to~\cite{GZ:kashaev}
and~\cite{GZ:qseries} which the reader can consult for further
information, motivation, historical presentation, as well as for the
connection with the asymptotics of the Kashaev invariant and with the
quantum modularity conjecture.

Note that our notation $\varphi_\s(\tau)$ from Equation~\eqref{phi-ex}
corresponds to the notation $\Phi^{(\s)}_0(2\pi \ri x)$
of~\cite{GZ:kashaev}.  In particular, the coefficient of $\tau^n$ in
$\varphi_\s(\tau)$ is (up to multiplication by an eighth root of unity
and the square root of an nonzero element of $F_\s$) in
$(2\pi \ri)^n F_\s$, where $F_\s$ is the trace field of $\s$.





\section{The equation $(1-x)(1-x^{-1})=1$ and the $4_1$ knot}
\label{sec.41}





The state integral of the $4_1$ knot is given by
Equation~\eqref{eq.statelm} below with $(A,B)=(1,2)$ and
$\mu=\lambda=0$. The critical points of the integrand are solutions of
the algebraic equation
\begin{equation}
  \label{41xi}
  (1-x)(1-x^{-1})=1.
\end{equation}
The latter has two solutions $\xi_1= {\rm e}^{2 \pi \ri/6}$ and
$\xi_2= \re^{-2 \pi \ri/6}$ which lie in the number field
$\BQ(\sqrt{-3})$, the trace field of the $4_1$ knot. The corresponding
series $\Phi_{\s_j}(\tau)$ satisfy the relation
$\Phi_{\s_2}(\tau) = {\rm i} \Phi_{\s_1}(-\tau)$ and the first few
terms of
$\varphi_{\s_1}(\tau/(2\pi \ri)) \in 3^{-1/4} \BQ(\sqrt{-3})[[\tau]]$
are given by
\begin{equation}
  \label{varphi41}
  \varphi_{\s_1}\left(\frac{\tau}{2\pi \ri}\right) =
  \frac{1}{\sqrt[4]3}\, 
  \Bigl(1 \+ \frac{11\tau}{72\sqrt{-3}}
  \+ \frac{697\tau^2}{2\,(72\sqrt{-3})^2}
  \+ \frac{724351\tau^3}{30\,(72\sqrt{-3})^3} \+\cdots\Bigr)\,. 
\end{equation}

The exponent in \eqref{phi-ex} involves the hyperbolic volume of the
$4_1$ knot complement

\begin{equation}
  \label{volume-41}
  V(\s_1)= V=2 {\rm Im}\, {\rm Li}_2(\re^{\ri \pi/3})= 2.029883\dots \,.
\end{equation}

The two series $\Phi_{\s_{j}}(\tau)$ for $j=1,2$ form a vector

\begin{equation}
  \label{phivec}
  \Phi(\tau)=
  \begin{pmatrix} \Phi_{\s_1}(\tau)\\ \Phi_{\s_2}(\tau) \end{pmatrix}
\end{equation}

that also appears in the refined quantum modularity
conjecture~\cite{GZ:kashaev}. $\Phi(\tau)$ is the vector of series
whose description in Borel plane we wish to give.

Consider the linear $q$-difference equation

\begin{equation}
  \label{41qdiff}
  y_{m+1}(q) -(2-q^m) y_m(q) + y_{m-1}(q)=0 \qquad (m \in \BZ) \,.
\end{equation}
It has a fundamental solution set given by the columns of the
following matrix
\begin{equation}
  \label{Gfund}
  W_m(q) =
  \begin{pmatrix} G^0_m(q) & G^1_m(q) \\ G^0_{m+1}(q) & G^1_{m+1}(q)
  \end{pmatrix},
\end{equation}  
where $G^0_m(q)$ and $G^1_m(q)$ are defined by
\begin{subequations}
  \begin{align}
\label{gm}
    G^0_m(q)
    &=\sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2+m n}}{(q;q)_n^2}
    \\
\label{Gm}
    G^1_m(q)
    &=\sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2+m n}}{(q;q)_n^2}
      \left(2m+ E_1(q) + 2 \sum_{j=1}^n \frac{1+q^j}{1-q^j} \right) \,,
\end{align}
\end{subequations}

and $E_1(q)=1-4\sum_{n=1}^\infty q^n/(1-q^n)$ is the Eisenstein series. 

It is easy to see that $G^0_m$ satisfies~\eqref{41qdiff}. Indeed,
$G^0_m(q)=\sum_{n=0}^\infty a_{n,-m}(q)^{-1}$ where $a_{n,m}(q)$ is
given in~\eqref{anm41} below. Equations~\eqref{ap1}-\eqref{ap3},
applied to $a_{n,-m}(q)^{-1}$ conclude the result. A similar proof
applies for $G^1_m$. Another way to do so is to use the state
integral~\eqref{eq.statelm} (with $(A,B)=(1,2)$) and show that the
latter satisfies the linear $q$-difference equation~\eqref{41qdiff} in
two ways, one with respect to the variable $\lambda$ and another with
respect to the variable $\mu$.

The fundamental solution $W_m(q)$ satisfies
\begin{equation}
  \label{det41}
  \det(W_m(q))=2
\end{equation}
and the symmetry
\begin{equation}
  \label{W41inv}
  W_m(q^{-1}) = W_{-m}(q)
  \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \,,
\end{equation}
and the orthogonality
\begin{equation}
  \label{WWT41b}
  \frac{1}{2} W_m(q)
  \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
  W_{m}(q)^T =
  \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \,.
\end{equation}
for all integers $m$, as well as
\begin{equation}
  \label{WWT41}
  \frac{1}{2} W_m(q)
  \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
  W_{\ell}(q)^T \in \SL(2,\BZ[q,1/q]) 
\end{equation}
for all integers $m, \ell$. The $\mathsf{S}$ matrix is given by 
\begin{subequations}
  \begin{align}
    \label{S41p}
    \mathsf{S}^+(q)
    &={1\over 2}
      \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}
       W_{-1}(q) \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}W_{-1}(q)^T
  \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix},\\
  
  
  
  
  \label{S41m}
  \mathsf{S}^-(q) &= {1\over 2}
  \begin{pmatrix} -1 & -1 \\ 0 & 1 \end{pmatrix} W_{-1}(q)
  \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}W_{-1}(q)^T
  \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \,.
\end{align}
\end{subequations}
The above matrix $\ms{S}$ satisfies Equation~\eqref{Ssym}.





\section{The equation $x^{-2}(1-x)^3=1$ and the $5_2$ knot}
\label{sec.52}

The state integral of the $5_2$ knot is given by
Equation~\eqref{eq.statelm} below with $(A,B)=(2,3)$ and
$\mu=\lambda=0$. The critical points of the integrand are solutions of
the algebraic equation

\begin{equation}
  \label{52xi}
  x^{-2}(1-x)^3=1 \,.
\end{equation}

The above equation (which defines a cubic field of discriminant $-23$,
the trace field of the $5_2$ knot) has three solutions
$\xi_1=0.78492+1.30714\dots \ri$, $\xi_2=0.78492-1.30714\dots \ri$ and
$\xi_3=0.43016\dots $, corresponding to the geometric representation,
its conjugate and the real representation.  The corresponding series
$\Phi_{\s_j}(\tau)$ satisfy
$\Phi_{\sigma_2}(\tau) = -\ri \overline{\Phi}_{\sigma_1}(-\tau)$ and
the first few terms of $\phi_{\s_j}(\tau/(2\pi \ri))$ are given by
\begin{align}
  \notag
  \varphi_{\s_j}\left(\frac{\tau}{2\pi \ri}\right)
  &=
    \left(\frac{-3\xi_j^2+3\xi_j-2}{23}\right)^{1/4}
    \left(1+\frac{33\xi_j^2+242\xi_j-245}{2^2\cdot 23^2}\tau
    +\frac{100250\xi_j^2-12643\xi_j+2732}{2^5\cdot 23^3}\tau^2\right.
  \\
  \notag
  &+\frac{-50198891\xi_j^2+35443870\xi_j-79016748}
    {2^7\cdot 3\cdot 5\cdot 23^5}\tau^3
  \\
    \label{varphi52}
  &\left.+\frac{-3809943572\xi_j^2+1861268771\xi_j+1015686665}
    {2^{11}\cdot 3\cdot 5 \cdot 23^6}\tau^4+\dots
    \right) \,.
\end{align}
The exponent in \eqref{phi-ex} involves 
\begin{equation}
  V(\sigma_1) = 2.821\ldots+ 1.379\ldots \ri,\;
  V(\sigma_2) = -2.821\ldots+ 1.379\ldots \ri,\;
  V(\sigma_3) = -2.758\ldots 
  \label{eq:V_52}
\end{equation}






where $\Re\,V(\sigma_1)$ is the hyperbolic volume of the $5_2$ knot
complement, and $\Im\,V(\sigma_1) = \Im\,V(\sigma_2)$ the Chern-Simons
action. The three series $\Phi_{\sigma_j}(\tau)$ for $j=1,2,3$ form a
vector
\begin{equation}
  \Phi(\tau) = \left(
    \begin{array}{c}
      \Phi_{\sigma_1}(\tau)\\
      \Phi_{\sigma_2}(\tau)\\
      \Phi_{\sigma_3}(\tau)
    \end{array}
  \right).
  \label{eq:phivec_52}
\end{equation}

Consider the linear $q$-difference equation 
\begin{equation}
  \label{52qdiff}
  y_m(q)-3y_{m+1}(q)+(3-q^{2+m})y_{m+2}(q) - y_{m+3}(q) = 0.
\end{equation}











The above equation has a fundamental solution set given by the
columns of the following matrix
\begin{equation}
  \label{52fund}
  W_m(q) =
  \begin{cases}
    W_m^+(q),\quad &|q|<1,\\
    \begin{pmatrix}
      0&0&1\\
      0&1&0\\
      1&0&0
    \end{pmatrix}
    W_{-m-2}^-(q^{-1})
    \begin{pmatrix}
      1&0&0\\
      0&-1&0\\
      0&0&1
    \end{pmatrix},\quad &|q|>1.
  \end{cases}
\end{equation}
where the matrices $W_m^\ve(q)$ with $\ve=\pm$ are respectively
\begin{equation}
  \label{52fund1}
  W^\ve_m(q) =
    \begin{pmatrix}
      H^{\ve}_{0,m}(q) & H^{\ve}_{1,m}(q) & H^{\ve}_{2,m}(q)       \\
      H^{\ve}_{0,m+1}(q) & H^{\ve}_{1,m+1}(q) & H^{\ve}_{2,m+1}(q) \\
      H^{\ve}_{0,m+2}(q) & H^{\ve}_{1,m+2}(q) & H^{\ve}_{2,m+2}(q)
    \end{pmatrix} 
\end{equation}

and $H^\ve_{j,m}(q)$ are given in Appendix~\ref{sec.A52} for $j=0,1,2$
and $m \in \BZ$.



The fundamental solutions satisfy
\begin{equation}
  \label{det52}
  \det(W_m(q))=2,
\end{equation}
for all integers $m$ as well as
\begin{equation}
  \label{WWT52}
  \frac{1}{2} W_m(q)
  \begin{pmatrix} 0&0&1 \\ 0&2&0 \\ 1&0&0 \end{pmatrix}
  W_{\ell}(q^{-1})^T \in \SL(3,\BZ[q,1/q]) 
\end{equation}
for all integers $m, \ell$. In particular, we have:
\begin{equation}
  \label{WWT52b}
  \frac{1}{2} W_{m-1}(q)
  \begin{pmatrix} 0&0&1 \\ 0&2&0 \\ 1&0&0 \end{pmatrix}
  W_{-m-1}(q^{-1})^T =
  \begin{pmatrix} 1&0&0 \\ 0&0&1 \\ 0&1&3-q^{m} \end{pmatrix} \,.
\end{equation}
The $\mathsf{S}$ matrix is given by 
\begin{subequations}
\begin{align}
  \label{S52p}
  \mathsf{S}^+(q) &= \frac{1}{2}
      \begin{pmatrix}
        0&1&0\\
        0&1&1\\
        -1&0&0
      \end{pmatrix} W_{-1}(q^{-1})
               \begin{pmatrix}
                 0&0&1\\
                 0&-2&0\\
                 1&0&0
               \end{pmatrix} W_{-1}(q)^T
               \begin{pmatrix}
                 0&0&-1\\
                 1&1&0\\
                 0&1&0
               \end{pmatrix},\\
  
  
  
  
  \label{S52m}
  \mathsf{S}^-(q) &= \frac{1}{2}
      \begin{pmatrix}
        0&3&-1\\
        0&-1&0\\
        1&0&0
      \end{pmatrix}
              W_{-1}(q)
              \begin{pmatrix}
                 0&0&1\\
                 0&-2&0\\
                 1&0&0
               \end{pmatrix} W_{-1}(q^{-1})^T
              \begin{pmatrix}
                0&0&1\\
                3&-1&0\\
                -1&0&0
              \end{pmatrix}\,.
\end{align}
\end{subequations}
The above matrix $\ms{S}$ satisfies Equation~\eqref{Ssym}. A proof is
given in Appendix~\ref{sub.qsym}.
