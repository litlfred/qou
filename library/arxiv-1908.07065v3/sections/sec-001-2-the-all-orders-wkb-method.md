---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-001-2-the-all-orders-wkb-method
section_title: "The all-orders WKB method"
section_number: 2
pages: 4-8
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.989
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{wkb}


Our first approach to the quantum SW curve will be based on the
so-called exact WKB method, see for example
\cite{voros,voros-quartic,ddpham,in-exactwkb}.  We will now summarize
the basic ingredients of the theory.


The Schr\"odinger equation for a non-relativistic particle in a
potential $V(x)$ and with energy $E$ reads as follows:

\be
\label{schrodinger}
-\hbar^2 \psi''(x) + (V(x)-E) \psi(x)=0. 
\ee

The standard WKB method produces asymptotic expansions in $\hbar$ for
the solutions to this equation.  Let us consider the following ansatz
for the wavefunction,

\begin{equation}\label{eq:psi-WKB}
  \psi(x) = \exp\(\frac{\ri}{\hbar}\int^x Y(x',E;\hbar) \rd x'\) \ .
\end{equation}

The function $Y(x,E;\hbar)$ satisfies the Riccati equation

\begin{equation}\label{riccati}
  Y^2 - \ri \hbar \frac{\rd Y}{\rd x} = E - V(x)
  \ .
\end{equation}

It has the formal power series expansion in powers of $\hbar$





\begin{equation}\label{ricwkb}
  Y(x,E;\hbar) = \sum_{n=0}^\infty p_n(x,E) \hbar^n \ ,
\end{equation}

where in particular $p_0(x, E)$ is the classical momentum as a
function of $x$ and the conserved energy. If one splits $Y$ into the even component and the odd component,

\be
Y = p_{\text{even}}+p_{\text{odd}}, 
\ee

 with
 
\begin{equation}
\label{p-series}
  p_{\text{even}}(x,E;\hbar) = \sum_{n=0}^\infty p_{2n}(x,E)\hbar^{2n}
  \ ,\quad
  p_{\text{odd}}(x,E;\hbar) = \sum_{n=0}^\infty
  p_{2n+1}(x,E)\hbar^{2n+1} \ ,
\end{equation}

one finds that the odd component is in fact a total derivative

\begin{equation}
  p_{\text{odd}}(x,E;\hbar) = \frac{\ri\hbar}{2}\frac{\rd}{\rd x} \log
  p_{\text{even}}(x,E;\hbar).
\end{equation}

By substituting \eqref{eq:psi-WKB} into the Schr\"{o}dinger equation,
one finds (see for instance \cite{bpv})

\begin{gather}
  p_{2n} = (-1)^n v_{2n} \ , \quad n \geq 0 \\
  v_{n} = \frac{1}{2p_0}\(\pd_xv_{n-1} - \sum_{k=1}^{n-1}v_k v_{n-k}\) \ ,
\end{gather}

from which the components $p_{2n}(x,E)$ can be solved recursively,
starting from the known expression of $p_0$.

Geometrically, we can regard $p_{\rm even}(x, E;\hbar) \rd x$ as a
meromorphic differential on the curve defined by

\be
\label{wkb-curve} 
y^2 = 2(E- V(x)). 
\ee

We will call it the {\it WKB curve}, and we will denote it as
$\Sigma_{\rm WKB}$.  This curve depends on a set of moduli which
include the energy $E$ and the parameters of the potential $V(x)$. The
basic objects in the exact WKB method are the periods of
$p_{\rm even} (x, E;\hbar) \rd x$ along one-cycles of
$\Sigma_{\rm WKB}$, which we will call {\it WKB periods} or {\it
  quantum periods}. We will denote them as

\be
\Pi_\gamma(\hbar)= \oint_\gamma p_{\rm even} (x,E;\hbar) \rd x, \qquad \gamma \in H_1(\Sigma_{\rm WKB}), 
\ee

and they are formal power series in even powers of $\hbar$, just like
$p_{\rm even}(x)$,

\be
\label{pi-wkb-expansion}
\Pi_\gamma(\hbar)=\sum_{n \ge 0} \Pi^{(n)}_\gamma \hbar^{2n}, \qquad
\Pi^{(n)}_\gamma = \oint_\gamma p_n(x, E) \rd x.  
\ee

Note that the coefficients $ \Pi^{(n)}_\gamma$ depend on the moduli of
the WKB curve. We will call $\Pi^{(0)}_\gamma$ the {\it classical
  periods}. The calculation of these coefficients at high order can be
quite involved, even for simple quantum systems.

In this paper we are interested in the modified Mathieu Hamiltonian,
with the conventions

\begin{equation}
  H(p,x) =p^2+V(x), \qquad  V(x)= 2\Lambda^2 \cosh x.
\label{eq:su2curve}
\end{equation}

Upon quantization, we obtain the operator 

\be
\label{eq:schrodinger}
\mH= \mm^2+ 2 \Lambda^2 \cosh(\mx), \qquad [\mx, \mm]= \ri \hbar. 
\ee

We will refer to this as the modified Mathieu operator. It is
well-known that the WKB curve of the modified Mathieu Hamiltonian
happens to coincide with the SW curve of ${\cal N}=2$, $SU(2)$
Yang--Mills theory, in the conventions appropriate for the relation to
integrable systems (see e.g. \cite{lerche-rev} for a review of SW
theory and \cite{swbook} for its connection to integrable
systems). In order to do this, we identify $E$ with the Coulomb
modulus $u$ by

\begin{equation}
  E = 2u \ .
\end{equation}


Let us first consider the classical periods of the modified Mathieu
equation. Since the WKB curve is a torus, there will be two periods,
corresponding to the two cycles of the torus.  The $B$ period
corresponds to the classical volume of phase space

\begin{equation}\label{eq:PiB0}
  \Pi_B^{(0)}(E)=4\,\ri\int_0^{x_+} \rd x \, \sqrt{E-2\Lambda^2 \cosh
    x},\ee 
    
  where 
  
  \be x_+=\cosh^{-1} \frac{E}{2\Lambda^2}
\end{equation}

is the turning point. This classical period can be evaluated
explicitly as

\begin{equation}\label{PB0}
  \Pi_B^{(0)}(E)=8\,\ri\sqrt{E+2\Lambda^2} \left[ {\bf K}\left(
      \frac{E-2\Lambda^2}{E+2\Lambda^2} \right) 
    -{\bf E} \left( \frac{E-2\Lambda^2}{E+2\Lambda^2} \right) \right].
\end{equation}

(We denote the elliptic integrals with boldface letters ${\bf K}$,
${\bf E}$, and their argument is the squared modulus $m=k^2$).  There
is in addition an $A$ period which corresponds to motion along the
imaginary axis. Classically, it is given by,

\begin{equation}\label{eq:PiA0}
  \Pi_A^{(0)}(E)
  = 
  -2\,\ri
  \int_{-\pi \ri }^{\pi \ri } \rd x \,
  \left(  \sqrt{E-2\Lambda^2 \cosh x}  \right) 
  
  
  
  =8 {\sqrt{E+2\Lambda^2}}  {\bf E} \left( {4
      \Lambda^2 \over 2 \Lambda^2+E} \right).  
\end{equation}

In the simplest case when $E=0$ and $\Lambda=1$, we have







\begin{equation}
  \Pi_A^{(0)}(0) = (1+\ri) \frac{16\pi^{3/2}}{\Gamma(1/4)^2},\quad
  \Pi_B^{(0)}(0) = -\ri \frac{16\pi^{3/2}}{\Gamma(1/4)^2} .
  
  
  
  
\end{equation}

We note that these classical periods are, up to normalization, the
famous $a$ and $a_D=\partial_a F$ periods of SW theory \cite{sw},
namely

\be
\label{abcpe}  
\Pi^{(0)}_A(E)=2 \pi a(u), \qquad \Pi_B^{(0)}(E) ={ 2 \ri }a_D(u). 
\ee

We will denote the all-orders WKB quantum periods as

\begin{equation}
  \label{QP}  \Pi_{A, B} (E,\hbar) =\sum_{n=0}^\infty \hbar^{2n} \Pi_{A, B}^{(n)} (E). 
\end{equation}


In the case of the modified Mathieu equation, the most efficient way
to calculate the quantum corrections is the so-called quantum operator
approach (see e.g. \cite{huangNS}). It turns out that, for each
function $p_{2n}(x, E)$ appearing in (\ref{p-series}), one can find a
first order differential operator $\mc O_n(E)$ such that

\begin{equation}
  \mc O_n(E)\circ p_0(x,E) = p_{2n}(x,E)
\end{equation}

up to a total derivative.
Since $\mc O_n(E)$ commutes with integration, one immediately has

\begin{equation}
  \Pi_{A,B}^{(n)}(E) = \mc O_n(E)\circ \Pi_{A,B}^{(0)}(E) \ .
\end{equation}

In this way, we have computed quantum corrections up to order 193.  As
a simple example, with $\Lambda=1$ we have \cite{huangNS}

\begin{equation}
  \mc O_1 (E) = \frac{E}{48(4-E^2)} + \frac{\pd}{24\pd E} \ .
\end{equation}

Therefore, 

\begin{equation}
  \Pi_A^{(1)}(E=0) = -\frac{1-\ri}{6\sqrt{2}}\md K(-1)\ ,\quad
  \Pi_B^{(1)}(E=0) = -\frac{\ri}{6\sqrt{2}}\md K(-1) \ .
\end{equation}

We recall that the quantum periods satisfy the so-called quantum
Matone relation
\cite{matone,francisco,basar-dunne,bdu-quantum,gorsky,coms}. One of
the consequences of this relation is that

\begin{equation}\label{eq:qMatone}
  \Pi^{(0)}_A(E) \Pi^{(1)}_B(E) - \Pi^{(0)}_B(E) \Pi^{(1)}_A(E) =
  \text{const.} \ , 
\end{equation}
which we can then evaluate at $E=0$ to be
$-2 \pi \ri /3$. 















It is well-known that the formal power series appearing in the quantum
periods diverge generically as \cite{bpv,cm-ha}

\begin{equation}
  \Pi_\gamma^{(n)}\approx (2n)!, \quad n \gg 1.
\end{equation}

Therefore the expressions \eqref{pi-wkb-expansion} are just formal
power series and need to be properly resummed. A natural way of doing
so is to perform the Borel resummation. In general, given an
asymptotic series of the form

\begin{equation}
  F = \sum_{n=0}^\infty f_n \hbar^{2n} \ ,\quad\hbar\in\IC \ ,
\end{equation}

with

\begin{equation}
  f_n \sim (2n)!\ , \quad n\gg 1
\end{equation}

we split $\hbar = \re^{\ri\phi}|\hbar|$, and define the Borel
resummation to be

\begin{equation}\label{eq:sF}
  s(F)(\hbar) =
  \frac{1}{|\hbar|} \int_0^\infty \widehat F(\re^{\ri\phi}\zeta)
  \re^{-\zeta/|\hbar|} \rd \zeta\ ,
\end{equation}

where $\widehat  F (\zeta)$ is the Borel transform

\begin{equation}
  \widehat F (\zeta) = \sum_{n=0}^\infty \frac{f_n}{(2n)!} \zeta^{2n} \ .
\end{equation}

The analytic properties of $\widehat F(\zeta)$ in the $\zeta$-plane,
also called the Borel plane, are crucial. If the Borel transform has
singularities along the ray $\arg(\zeta) = \phi$, the series
$F(\hbar)$ is not Borel summable, as the integral in the Laplace
transformation \eqref{eq:sF} is obstructed. We can however deform
slightly the integration contour below or above the positive real
axis, obtaining in this way the so-called \emph{lateral Borel
  resummations} of the formal power series $F(\hbar)$:

\begin{equation}
  s_{\pm}(F)(\hbar) =
  \frac{1}{|\hbar|}
  \int_{0}^{\re^{ \ri 0^{\pm}} \infty } \widehat F (\re^{\ri\phi}\zeta)
  \re^{-\zeta/|\hbar|} \rd \zeta .
\end{equation}

These lateral resummations are in general
different, and their difference is defined as the {\it Stokes
  discontinuity} of $F$:

\be
\label{stokes-disc}
{\rm disc}(F)(\hbar) = s_+(F)(\hbar)- s_-(F)(\hbar). 
\ee

Stokes discontinuities play a crucial r\^ole in the theory of
resurgence, see e.g. \cite{abs}.

\begin{figure}
  \centering
  \subfloat[$\Pi_A$]{\includegraphics[width=0.4\linewidth,valign=c]
    {qPiau0}} 
  \hspace{4ex}
  \subfloat[$\Pi_B$]{\includegraphics[width=0.4\linewidth,valign=c]
    {qPiaDu0}}
  \caption{Poles of the Borel--Pad\'e transforms, which would accumulate to branch
    cuts for the Borel transform of the quantum periods $\Pi_A(E,\hbar)$ (a) and
    $\Pi_B(E,\hbar)$ (b) at $u=0$ and $\Lambda=1$. The red points are
    the central charges of the BPS states which contribute to the
    branch points, and their electromagnetic charges are labelled
    nearby. See discussion in section~\ref{sc:SW-TBA}.}\label{fg:u0-bc}
\end{figure}

Let us look at some examples of the Borel plane of the quantum periods
for the modified Mathieu equation. In practice, to calculate the Borel transform, we use standard Borel--Pad\'e techniques, i.e.\ we use a finite number of terms in the 
formal power series (in this case we have used $193$ terms), and in order to extend analytically the resulting function, 
we use a Pad\'e transform of the Borel transform. In this method, branch cuts of the Borel transform 
are indicated by a dense accumulation of poles of the Borel--Pad\'e transform along a segment. The first example is when
$u=E=0$. We plot the poles of the Borel--Pad\'e transforms of
$\Pi_A(0,\hbar), \Pi_B(0,\hbar)$ in the Borel plane in
Figures~\ref{fg:u0-bc}. They indicate the existence of four branch cuts
in the case of the $A$ period, and two branch cuts in the case of
$B$ period. Since in both cases there are branch cuts along the positive
real axis, neither of the two quantum periods are Borel summable.

\begin{figure}
  \centering
  \subfloat[$\Pi_A$]{\includegraphics[width=0.4\linewidth,valign=c]
    {qPiau4}}
  \hspace{4ex}
  \subfloat[$\Pi_B$]{\includegraphics[width=0.4\linewidth,valign=c]
    {qPiaDu4}} 
  \caption{Poles of the Borel--Pad\'e transforms, which would accumulate to branch
    cuts for the Borel transforms of the quantum periods $\Pi_A(u,\hbar)$ (a) and
    $\Pi_B(u,\hbar)$ (b) at $u=4$ and $\Lambda=1$. The red points are
    the central charges of the BPS states which contribute to the
    branch points, and their electromagnetic charges are labelled
    nearby. See discussion in section~\ref{sc:SW-TBA}.}\label{fg:u4-bc}
\end{figure}

Next, we consider $u=E/2=4$. Again we plot the poles of the
Borel--Pad\'e transforms of $\Pi_A(4,\hbar), \Pi_B(4,\hbar)$ in the
Borel plane in Figures~\ref{fg:u4-bc}. In both cases we observe six
branch cuts, and they are in different locations as compared to what
we found at $u=0$. In this case, the quantum $A$ period is Borel
summable, but the quantum $B$ period is not.

As we can see, in general, the quantum periods are not Borel summable,
and their Borel transforms and resummations have a rich
structure. Fortunately the connection with SW theory gives very
powerful information on this structure, which we will explore in
detail in the next section.
