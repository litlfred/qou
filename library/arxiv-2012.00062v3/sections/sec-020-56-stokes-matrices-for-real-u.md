---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-020-56-stokes-matrices-for-real-u
section_title: "Stokes matrices for real u"
section_number: 5.6
pages: 41-43
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.957
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.41stokesp}

In Section~\ref{sub.41stokes} we only considered the resurgent
structure for $x$ near $1$, or equivalently, $u=\log x $ near $0$.
When $x$ is arbitrary, the resurgent structure of the vector $\Phi_\s(x;\tau)$
could be very different.  According to the Picard--Lefschetz theory
(for review, see for instance \cite{Witten:2010cx}), when a set of
asymptotic series originates from a (path) integral, the Borel sum of
each asymptotic series is the evaluation of the integral along a
Lefschetz thimble anchored to a critical point.  In the $x$-plane,
there are walls of marginal stability which start
from the roots to the discriminant \eqref{disc41y} and which end at
infinity.  When we cross such a Stokes line, Lefschetz thimbles jump
leading to linear transformations of the Borel summed asymptotic
series.  In this section we extend slightly the discussion of
Section~\ref{sub.41stokes} by considering the resurgent structure of
$\Phi_\s(x;\tau)$ for generic positive $x$ (see \cite{Beem} for a
similar discussion in complex Chern-Simons theory).  The positive real
axis is divided by the two real solutions to~\eqref{disc41y} 

\begin{equation}
  \label{z35}
  x_{\pm} = \frac{1}{2}(3\pm \sqrt{5})
\end{equation}
to three intervals
\begin{equation}
  (0,x_{-}),\;(x_-,x_+),\;(x_+,\infty).
\end{equation}
The middle interval is covered by Section~\ref{sub.41stokes}, while
the first (labeled by $<$) and third (labeled by $>$) intervals are
discussed below.

\begin{figure}[htpb!]
\leavevmode
\begin{center}
\includegraphics[height=7cm]{fig8_borelplane_s1l}\hspace{4ex}
\includegraphics[height=7cm]{fig8_borelplane_s2l}
\end{center}
\caption{The singularities in the Borel plane for the series
  $\varphi_{\sigma_{j}} (u;\tau)$ with $j=1,2$ of knot $\knot{4}_1$
  for $x=\re^{2\pi\bb u}$ in the first or the third interval of the
  positive axis.}
\label{fig:sings-l-41}
\end{figure}

\begin{figure}[htpb!]
\leavevmode
\begin{center}
\includegraphics[height=7cm]{fig8_regions_l}
\end{center}
\caption{Four different sectors in the $\tau$-plane for $\Phi(u;\tau)$
  of knot $\knot{4}_1$ with $x=\re^{2\pi\bb u}$ in the first or the
  third interval of the positive axis.}
\label{fig:secs-l-41}
\end{figure} 

First of all, we notice that the first and third intervals are related
by the reflection $x\mapsto x^{-1}$.  In fact, due to the property
\eqref{eq:-xphi} of the asymptotic series, the Borel plane
singularities for $\Phi_\s(x;\tau)$ and $\Phi_\s(x^{-1};\tau)$ are
identical, and we illustrate them uniformly in
Figure~\ref{fig:sings-l-41}. The positions of singularities are still
described by \eqref{iota}.  However, the difference of action
$(V(\s_1)-V(\s_2))/(2\pi\ri)$ is now imaginary and it describes the
vertical spacing between neighoring singularities.  The shortest
horizontal spacing is $\log x$. Finally all singularities are repeated
vertically by the spacing $2\pi\ri$.  Similar to the discussion in
Section~\ref{sub.41stokes}, we label in the $\tau$-plane by
$I,II,III,IV$ the four sectors which separate the 12 singularities
close to the real axis and other singularities along the imaginary
axis or away from the real axis, as in Figure~\ref{fig:secs-l-41}.  In
each of the four sectors, the Borel summed vector
$s_R^{\gtrless}(\Phi)(x;\tau)$ is a linear transformation of the Borel
summed vector $s_R(\Phi)(x;\tau)$ in the middle interval, as per the
Picard-Lefschetz theory
\begin{equation}
  s_R^{\gtrless}(\Phi)(x;\tau) = T_R^{\gtrless}(\tx)\cdot s_R(\Phi)(x;\tau).
\end{equation}
It is most convenient to compute the transformation matrix
$T_R^{\gtrless}$ by comparing the left hand side with the holomorphic
lifts of $s_R(\Phi)(x;\tau)$ summarized in
Corollary~\ref{cor.41borel}.  By doing so, we find in the first
interval
\begin{align}
  T^{<}_{I}(\tx) &=
    \begin{pmatrix}
      \tx&0\\-\tx&1
    \end{pmatrix}, &
         T^{<}_{II}(\tx) &=
           \begin{pmatrix}
             0&1\\-\tx&1
           \end{pmatrix}\\
  T^{<}_{III}(\tx) &=
    \begin{pmatrix}
      \tx&1\\-\tx&0
    \end{pmatrix}, &
         T^{<}_{IV}(\tx) &=
           \begin{pmatrix}
             \tx&1\\0&1
           \end{pmatrix},
\end{align}
while in the third interval
\begin{align}
  T^{>}_{I}(\tx) &=
    \begin{pmatrix}
      \tx^{-1}&0\\
      -\tx^{-1}&1
    \end{pmatrix},  &
              T^{>}_{II}(\tx) &=
                \begin{pmatrix}
                  0&1\\-\tx^{-1}&1
                \end{pmatrix}\\
  T^{>}_{III}(\tx) &=
    \begin{pmatrix}
      \tx^{-1}&1\\
      -\tx^{-1}&0
    \end{pmatrix}, &
              T^{>}_{IV}(\tx) &=
                \begin{pmatrix}
                  \tx^{-1}&1\\0&1
                \end{pmatrix}.
\end{align}
They are indeed related by
\begin{equation}
  T^{<}_R(\tx) = T^{>}_R(\tx^{-1}).
  \label{eq:Tgtrless}
\end{equation}

Once the linear combinations are known, the Stokes matrices can be
computed using the Stokes matrices in the middle interval given in
Section~\ref{sub.41stokes}
\begin{equation}
  \mfS^{\gtrless}_{R\rightarrow R'}(x;q) =
  T_{R'}^{\gtrless}(x)\cdot
  \mfS_{R\rightarrow R'}(x;q)\cdot \left(T_{R}^{\gtrless}(x)\right)^{-1}.
\end{equation}
We find
\begin{align}
  \mfS^>_{I\rightarrow II}(x;q) =
    &\begin{pmatrix}
      0&1\\
      -x^{-1}&1
    \end{pmatrix}\cdot
               \mfS_{I\rightarrow II}(x;q)\cdot
               \begin{pmatrix}
                 x&0\\1&1
               \end{pmatrix}\\
  \mfS^>_{II\rightarrow III}(x) =
    &\begin{pmatrix}
      1-x-x^2 && x+x^2\\-x-x^2 && 1+x+x^2
    \end{pmatrix}\\
  \mfS^>_{III\rightarrow IV}(x;q) =
    &\begin{pmatrix}
      x^{-1}&1\\-x^{-1}&0
    \end{pmatrix}\cdot \mfS_{III\rightarrow IV}(x;q)\cdot
    \begin{pmatrix}
      x&-x\\0&1
    \end{pmatrix}\\
  \mfS^>_{IV\rightarrow I}(x)=
    &\begin{pmatrix}
      1+x^{-1}+x^{-2} && x^{-1}+x^{-2}\\-x^{-1}-x^{-2} &&
      1-x^{-1}-x^{-2}
    \end{pmatrix},
\end{align}
and thanks to \eqref{eq:Tgtrless}, 
\begin{equation}
  \mfS^{<}_{R\rightarrow R'}(x;q) =
  \mfS^{>}_{R\rightarrow R'}(x^{-1};q).
\end{equation}

Note that $\mfS^>_{III\rightarrow I}(x)$ and
$\mfS^>_{II\rightarrow IV}(x)$ encode all the 12 singularities near the
real axis illustrated in Figure~\ref{fig:secs-l-41}, as well as the
Stokes constants associated to them.  Furthermore, the Stokes matrices
also have the property
\begin{equation}
  \mfS^>_{IV\rightarrow III}(x^{-1};q)^{-1} = \mfS^>_{I\rightarrow II}(x;q)^T,
\end{equation}
in accord with Conjecture~\ref{conj.ann}.
