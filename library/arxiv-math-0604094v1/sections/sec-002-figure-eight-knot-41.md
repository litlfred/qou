---
doc_id: arxiv-math-0604094v1
doc_title: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant"
section_id: sec-002-figure-eight-knot-41
section_title: "Figure-Eight knot 41"
section_number: null
pages: 13-15
source_pdf: 0604094v1.pdf
source_sha256: f0c4c36ab0acf537
toc_source: outline
text_source: latex
latex_prose_ratio: 0.698
latex_coverage_ratio: 0.953
doc_brief: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant — 9 sections: Front matter; Quantum Dilogarithm Function; Examples"
---
\label{sec:41}

We set $\mathcal{K}$ as 
the Figure-Eight knot $4_1$ which is depicted
as
\begin{equation*}
  \includegraphics[scale=.16]{psm_41.eps}    
\end{equation*}
It is well known that the complement of the figure eight knot,
$\mathcal{M}=S^3 \setminus \mathcal{K}$,
is given by two ideal tetrahedra,
and the triangulation induces the quantum invariant as
\begin{equation}
  Z_\gamma(\mathcal{M}_u)
  =
  \int\limits_{\mathbb{R}} \mathrm{d} \boldsymbol{p} \,
  \delta_C(\boldsymbol{p}; u) \,
  \left\langle
    p_1, p_2  \middle| S \middle| p_3, p_4
  \right\rangle \,
  \left\langle
    p_4, p_3 \middle| S^{-1} \middle| p_2, p_1 \right\rangle 
\end{equation}
Modulus of two tetrahedra are given by
$w=\E^{p_4 - p_2}$
and
$z=\E^{p_1 - p_3}$.
The developing map is drawn in Fig.~\ref{fig:develop41},
and
the meridian  is read to be 
\begin{equation*}
  \frac{w}{z} = \E^{-2 u}
\end{equation*}




which shows that the condition $\delta_C(\boldsymbol{p};u)$ is
\begin{equation*}
  p_4 - p_2 - (p_1 - p_3) = -  2\,  u
\end{equation*}
The complete hyperbolic structure is realized when $u=0$.

  \begin{figure}[htbp]
    \centering

    \includegraphics[scale=0.8]{develop41.1.eps}
    \caption{Developing map of the complement of the
      figure-eight knot.
      The gray filled triangle corresponds to top vertex of the
      tetrahedron
      (central vertex of circle in~\eqref{S_tetrahedron})

      with modulus $w$ in projection
      of~\eqref{S_tetrahedron}.
      A curve denotes a meridian of cusp.
  }
    \label{fig:develop41}
  \end{figure}


We then obtain
  \begin{equation}
    Z_\gamma\left( \mathcal{M}_u \right)
    =
    \frac{1}{ 4 \, \pi \, \gamma}
    \int \mathrm{d} x \,
    \frac{
      \Phi_\gamma(x+ \I \, \pi + \I \, \gamma)
    }{
      \Phi_\gamma(-x-  2 \, u - \I \, \pi - \I \, \gamma)
    } \,
    \E^{\frac{-1}{2 \I \gamma} 4 u(u +x)}
  \end{equation}
  In a limit $\gamma \to 0$, we have
  \begin{align}
    Z_\gamma(\mathcal{M}_u)
    & \sim
    \int \mathrm{d} x \, 
    \exp
    \left(
      \frac{1}{2 \, \I \, \gamma} \,
      \left(
        \Li(\E^x) - \Li(\E^{-x- 2 u}) -  4 \, u \, (u+ x)
      \right)
    \right)
    \nonumber \\
    & =
    \int \mathrm{d}x \,
    \exp \left( \frac{1}{2 \, \I \, \gamma} \,
      V_{\mathcal{M}}( \E^x ; \E^u) \right)
    \label{Z_V_classical_41}
  \end{align}
  where the potential function is set to be
  \begin{equation}
    \label{41_potential}
    V_{\mathcal{M}}(x; m)
    =
    \Li(x) - \Li \left(\frac{1}{x \, m^2 }\right)
    -4   \log m \,   \log (x \, m)
  \end{equation}
  
  To evaluate the integral~\eqref{Z_V_classical_41}, we may apply the
  saddle point method, and a condition~\eqref{hyperbolic_consistency}
  reduces to
  \begin{gather}
    \label{41_saddle}
    - \frac{x}{m^2 \, (1-x) \, (1-m^2 \, x)} = 1
  \end{gather}
  From~\eqref{differential_longitude} the longitude is given by
  \begin{gather}
    \label{41_long}
    \frac{1}{m^2 \, x \, (m^2 \, x - 1)}
    =
    \ell
  \end{gather}

  Completeness condition $m=1$ gives
  $x=\frac{1 \pm \sqrt{3} \, \I}{2}$ from~\eqref{41_saddle}.
  Substituting this solution for the potential
  function~\eqref{41_potential},
  the imaginary part coincides with
  the hyperbolic volume of the figure-eight knot
  $\Vol(S^3 \setminus 4_1)
  = 2.02988 \cdots$.

  For a deformed manifold $\mathcal{M}_u$,
  we get an algebraic equation of $\ell$ and $m$ by eliminating $x$
  from~\eqref{41_saddle} and~\eqref{41_long} as
  \begin{equation}
    A(\ell , m) = 0
  \end{equation}
  Here  $A(\ell, m)$ is the A-polynomial for the figure-eight knot;
  \begin{equation}
    A(\ell,m)
    =
    - m^4 + \ell \, (1 - m^2 - 2 \, m^4 - m^6 + m^8 )
    -
    \ell^2 \, m^4
  \end{equation}
  which can be  expressed as in the Newton polygon as follows;
  \begin{equation*}

    \begin{pmatrix}
      0 & 1 & 0 \\
      0 & -1 & 0 \\
      -1 &-2 & -1 \\
      0 & -1 & 0 \\
      0 & 1 & 0
    \end{pmatrix}

  \end{equation*}


  We note that a set of equations~\eqref{41_saddle}
  and~\eqref{41_long} gives
  \begin{equation*}
    2 \, v
    =
    -2 \, \pi \, \I + 4\, \sqrt{3} \,  \I \, u
    + \frac{16 \, \I}{\sqrt{3}} \, u^3
    +
    \frac{368 \, \I}{15 \sqrt{3}} \, u^5
    +
    \frac{2848 \, \I}{45 \sqrt{3}} \, u^7
    + \cdots
  \end{equation*}
  which coincides with a result in Ref.~\citen{NeumZagi85a}
  under~\eqref{uv_NZ}.


















\subsection{
  $5_2$}
We set $\mathcal{K}$ as the knot $5_2$ depicted as
\begin{equation*}
  \includegraphics[scale=.16]{psm_52.eps}  
\end{equation*}
The knot complement $\mathcal{M}=S^3 \setminus \mathcal{K}$
is constructed from three tetrahedra (see, \emph{e.g.},
Ref.~\citen{MoTaka85a})
and we obtain the invariant as
\begin{equation}
  Z_\gamma\left( \mathcal{M}_u \right)
  =
  \int\limits_\mathbb{R} \mathrm{d}\boldsymbol{p} \,
  \delta_C(\boldsymbol{p}; u ) \,
  \left\langle
    p_1 , p_5 \middle| S^{-1} \middle| p_4 , p_3
  \right\rangle \,
  \left\langle
    p_2 , p_4 \middle| S^{-1} \middle| p_6 , p_5
  \right\rangle \,
  \left\langle
    p_3 , p_6 \middle| S^{-1} \middle| p_1 , p_2
  \right\rangle 
\end{equation}
Modulus of three tetrahedra are respectively
$z_1 =\E^{p_3 - p_5}$,
$z_2 =\E^{p_5 - p_4}$, and
$z_3 =\E^{p_2 - p_6}$.
The developing map is depicted in Fig.~\ref{fig:develop52}.
The meridian is read to be  $\frac{z_3}{z_2}$, and the condition
$\delta_C(\boldsymbol{p}; u)$ is
\begin{equation*}
  p_5 - p_4 + p_6 - p_2
  =  2\, u
\end{equation*}
We then have
\begin{multline}
  Z_\gamma\left( \mathcal{M}_u \right)
  =
  \frac{1}{
    \left( 4 \, \pi \, \gamma \right)^{3/2}
  } \,
  \iint \mathrm{d} x \, \mathrm{d} y 
  \,
  \E^{\frac{1}{2 \I \gamma}
    \left(
      \frac{\pi^2+\gamma^2}{2}
      +
      \frac{3}{2} \pi \gamma 
      +
      ( 2 u-y) (y-x)
    \right)
  }
  \\
  \times
  \frac{1}{
    \Phi_\gamma(-x+y- 2 \,  u-\I \, \pi - \I \, \gamma) \,
    \Phi_\gamma(-y- 2 \, u-\I \, \pi - \I \, \gamma) \,
    \Phi_\gamma(-y- 2 \, u-\I \, \pi - \I \, \gamma)
  }
\end{multline}

\begin{figure}[htbp]
  \centering

  \includegraphics[scale=1.28]{develop52.1.eps}
  \caption{Developing map of the complement of $5_2$.
    Gray filled triangle denotes top vertex of the tetrahedron with
    modulus $z_1$.
    Meridian is denoted by a gray curve.
  }
  \label{fig:develop52}
\end{figure}


In a classical limit $\gamma\to 0$, we obtain
\begin{equation}
  Z_\gamma\left( \mathcal{M}_u \right)
  \sim
  \iint \mathrm{d} x \, \mathrm{d} y \,
  \exp 
  \left(
    \frac{1}{2 \, \I \, \gamma} \,
    V_{\mathcal{M}}(\E^x, \E^y ; \E^u)
  \right)
\end{equation}
where the Neumann--Zagier potential function is
  \begin{equation}
    V_{\mathcal{M}}(x,y; m)
    =
    \frac{\pi^2}{2}
    - \Li\left(\frac{y}{x \, m^2}\right)
    - \Li \left( \frac{1}{ y \, m^2}\right)
    - \Li \left(\frac{1}{y}\right)
    + \log \left( y/x \right) \, \log \left(m^2/y \right)
  \end{equation}
The integral is evaluated by the saddle point method, and  saddle
point conditions~\eqref{hyperbolic_consistency} which denote 
hyperbolic consistency conditions
reduce to
\begin{equation}
  \label{consistency_52}
  \begin{gathered}
    m^2 \, x - y = x \, y
    \\[2mm]
    (m^2 \, y -1) \, (y -1) = m^2 \, (m^2 \, x - y)
  \end{gathered}
\end{equation}
and
the identity for the longitude~\eqref{differential_longitude} 
is given as
\begin{equation}
  \label{longitude_52}
  m^4 \, y^2 =
  (m^2 \, x - y) \, (m^2 \, y - 1) \, \ell
\end{equation}

In the case of complete structure $\mathcal{M}$, \emph{i.e.}, $u=0$,
there exists a solution of~\eqref{consistency_52},
$(x,y)=
(-0.877439 + 0.744862 \, \I ,
0.78492 + 1.30714 \, \I)$,
 such that the
imaginary part of the potential function
\begin{equation*}
  \Im V_\mathcal{M}(x,y;1)
  =
  -D \left( \frac{y}{x} \right)
  - 2 \,D\left( \frac{1}{y} \right)
\end{equation*}
gives the hyperbolic volume of $\mathcal{M}$;
$\Vol(\mathcal{M})
=
2.82812 \cdots$.
.

To get the A-polynomial, we
eliminate variables $x$ and $y$ from a set of
equations~\eqref{consistency_52} and~\eqref{longitude_52}.
After some algebra we obtain
$A_\mathcal{K}(\ell,m)=0$, where the function
$A_\mathcal{K}(\ell,m)$ coincides with the
A-polynomial for $5_2$
given by the following Newton polygon;
  \begin{equation*}
    \begin{pmatrix}
      -1 & 1 &  &  \\
       & -2 &  &  \\
       & -2 & -1 &  \\
        &  & 1 &  \\
        & 1 &  &  \\
        & -1 & -2 &  \\
        &  & -2 &  \\
        &  & 1 & -1 \\
    \end{pmatrix}
  \end{equation*}



\subsection{
  Pretzel knot $(-2,3,7)$}

Let $\mathcal{K}$ be the $(-2,3,7)$ Pretzel knot depicted as
\begin{equation*}
  \includegraphics[scale=.16]{psm_k31.eps}
\end{equation*}
and we set $\mathcal{M}$ as the complement of $\mathcal{K}$.
The Pretzel knot $(-2,3,7)$ has the same hyperbolic volume with $5_2$,
$\Vol(\mathcal{M})
=
2.82812 \cdots$,
but the triangulations  of the complement give the following partition
function;
\begin{multline}
  Z_\gamma\left( \mathcal{M}_u \right)
  = \int\limits_{\mathbb{R}}
  \mathrm{d} \boldsymbol{p} \,
  \delta_C(\boldsymbol{p}; u) \,
  \langle p_4 , p_7 | S | p_6 , p_1 \rangle \,
  \langle p_5 , p_8 | S | p_7 , p_5 \rangle
  \\
  \times
  \langle p_1 , p_6 | S | p_8 , p_2 \rangle \,
  \langle p_3 , p_2 | S | p_4 , p_3 \rangle 
\end{multline}
Note that this triangulation differs from the canonical triangulation
in Ref.~\citen{SnapPea99}.
The developing map is given in Fig.~\ref{fig:developPretzel}.
Here we set the modulus of four ideal tetrahedra as
\begin{align*}
  z_1 & = \E^{p_1 - p_7}
  &
  z_2 &= \E^{p_5-p_8}
  \\
  z_3 & = \E^{p_2 - p_6}
  &
  z_4 & = \E^{p_3 - p_2}
\end{align*}
Then the
meridian is read as
\begin{equation*}
   p_2 - p_6 - p_1 + p_7
   = -  2 \, u
\end{equation*}

\begin{figure}[htbp]
  \centering

  \includegraphics[scale=1.04]{developPretzel.1.eps}
  \caption{Developing map of  complement of the Pretzel knot
    $(-2,3,7)$.
    Horosphere of the top vertex of the tetrahedron with modulus $z_1$
    is depicted by gray triangle.
    Gray curve denotes a meridian.
  }
  \label{fig:developPretzel}
\end{figure}

In the classical limit of the quantum invariant $Z_\gamma(\mathcal{M}_u)$
we obtain the potential function after some change of variables as
\begin{multline}
  V_{\mathcal{M}}(x,y,z ; m)
  =    -\frac{2 \, \pi^2}{3}+
  \Li\left(\frac{1}{z}\right)
  + \Li\left(\frac{1}{x \, y \, z \, m^4}\right)
  + \Li\left(\frac{1}{z \, m^2}\right)
  + \Li\left(\frac{m^2}{x}\right)
  \\
  + 3 \left( \log \left( m^2 \right) \right)^2 +
  \log \left(\frac{y^5}{x^2} \right) \log \left( m^2 \right)
  + \left( \log x \right)^2 +
  \left( \log y \right)^2
\end{multline}


The hyperbolic consistency
conditions~\eqref{hyperbolic_consistency} give
\begin{equation}
  \label{consistency_pretzel}
  \begin{gathered}
    \left( x \, y \, z \, m^4 - 1 \right) \, \left( x- m^2 \right)
    = y \, z \, m^8
    \\[2mm]
    y \, m^6 \, \left( x \, y \, z \, m^4 - 1 \right)
    = x \, z
    \\[2mm]
    (z-1) \, \left(
      x \, y \, z \, m^4 - 1 \right) \, \left( m^2 \, z -1 \right)
    =
    x \, y \, z^3 \, m^6
  \end{gathered}
\end{equation}
and the longitude~\eqref{differential_longitude} is defined by
\begin{equation}
  \label{long_pretzel}
  \ell
  =
  \frac{
    \left( x \, y \, z \, m^4 -1 \right)^2 \,
    \left( m^2 \, z - 1 \right)^2 \, m^2 \, y^3
  }{
    \left( x - m^2 \right) \, x^3 \, z^3}
\end{equation}
In the complete hyperbolic structure $m=1$,
we have a solution of~\eqref{consistency_pretzel},
\begin{equation*}
  \begin{pmatrix}
    x \\ y \\ z
  \end{pmatrix}
  =
  \begin{pmatrix}
    0.337641 - 0.56228 \, \I \\
    0.122561 + 0.744862 \, \I \\
    0.618504 - 0.410401 \, \I
  \end{pmatrix}
\end{equation*}
s.t.
we recover the hyperbolic volume of $\mathcal{K}$;
\begin{equation*}
  \Im V_\mathcal{M}(x,y,z; m=1)
  =
  2 \, D(1/z) + D\left(\frac{1}{x \, y \, z}\right)
  + D(1/x)
  =
  2.82812 \cdots
\end{equation*}

The A-polynomial is computed by eliminating
$(x,y,z)$ from~\eqref{consistency_pretzel} and~\eqref{long_pretzel},
and we obtain 
$A_\mathcal{K}(\ell, m)=0$, where the A-polynomial for the $(-2,3,7)$
Pretzel knot is
\begin{multline}
  A_{\mathcal{K}}(\ell, m)
  =
  -1 +  \left(
    m^{16} - 2 \, m^{18} + m^{20}
  \right) \, \ell
  +
  \left( 2 \, m^{36} + m^{38} \right) \, \ell^2
  \\
  - \ell^4 \, \left(
    m^{72} + 2 \, m^{74}
  \right)
  -\ell^5 \, \left(
    m^{90} - 2 \, m^{92} + m^{94}
  \right)
  + m^{110} \, \ell^6
\end{multline}
