---
doc_id: arxiv-math-0604094v1
doc_title: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant"
section_id: sec-005-once-punctured-torus-bundles-over-the-circle
section_title: "Once-Punctured Torus Bundles over the Circle"
section_number: null
pages: 19-26
source_pdf: 0604094v1.pdf
source_sha256: f0c4c36ab0acf537
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.918
doc_brief: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant — 9 sections: Front matter; Quantum Dilogarithm Function; Examples"
---
One of benefits of the quantum invariant $Z_\gamma(\mathcal{M})$ is
that we can compute it explicitly
for a once-punctured torus bundle over $S^1$.
A once-punctured torus bundle
over $S^1$, which we denote  $\mathcal{M}(\varphi)$,
 is
described by
$F \times [0,1]/(x,0) \sim (\varphi(x),1)$ where
a monodromy matrix 
$\varphi \in SL(2,\mathbb{Z})$
is a homeomorphism from the punctured torus
$F=\mathbb{T}^2 \setminus \{ 0 \}$ to itself.
Thurston's hyperbolization theorem indicates that
$\mathcal{M}(\varphi)$ admits
a complete hyperbolic metric with a finite volume when $\varphi$ has 2
distinct real eigenvalues.
In this case, the monodromy matrix $\varphi$  can be written up to
conjugation as
\begin{equation}
  \varphi
  =
  L^{s_1} \, R^{t_1} \cdots
  L^{s_{n}}
  R^{t_{n}}
\end{equation}
where
\begin{align*}
  L 
  & =
  \begin{pmatrix}
    1 & 1 \\
    0 & 1
  \end{pmatrix}
  &
  R
  &=
  \begin{pmatrix}
    1 & 0 \\
    1 & 1
  \end{pmatrix}
\end{align*}
with
$n>0$,
and $s_j$ and $t_j$  are positive integers.
Note that 
the complement of the figure-eight knot studied in Sec.~\ref{sec:41}
corresponds to
$\varphi=L \, R =
\begin{pmatrix}
  2 & 1 \\
  1 & 1
\end{pmatrix}
$.

It is known that we can triangulate the manifold $M_\varphi$ with
$\sum_{k=1}^n (s_k+t_k)$ ideal tetrahedra~\cite{FloyHatc82a}, and we have the
quantum invariant as
\begin{multline}
  \label{Z_punctured_torus}
  Z_\gamma\left( \mathcal{M}_u(\varphi) \right)
  =
  \iiiint\limits_{\mathbb{R}}
  \mathrm{d} \boldsymbol{a} \,
  \mathrm{d} \boldsymbol{b} \,
  \mathrm{d} \boldsymbol{c} \,
  \mathrm{d} \boldsymbol{d} \,
  \delta_C(\boldsymbol{a}, \boldsymbol{b} ,
  \boldsymbol{c}, \boldsymbol{d}; u) \,
  \delta_G(\boldsymbol{a}, \boldsymbol{b} ,
  \boldsymbol{c}, \boldsymbol{d})
  \\
  \times
  \prod_{k=1}^n
  \left[
    \prod_{i=0}^{s_{k} -1}
    \left\langle d_{k,i} , c_{k, i+1} \middle| S^{-1} \middle|
      d_{k,i+1}, c_{k,i} \right\rangle \,
    \prod_{j=0}^{t_{k} -1}
    \left\langle b_{k,j} , a_{k,j+1} \middle| S \middle|
      b_{k,j+1}, a_{k,j} \right\rangle \,
  \right]
\end{multline}
where gluing condition $
  \delta_G(\boldsymbol{a}, \boldsymbol{b} ,
  \boldsymbol{c}, \boldsymbol{d})
$ means
\begin{align*}
  &
  \begin{cases}
    b_{k,0} = c_{k+1,0} 
    \\
    a_{k,0} = d_{k+1,0}
  \end{cases}
  \text{for $k=1,2, \dots,n-1$}
  & &
  \begin{cases}
    b_{n,0} = c_{1,0}
    \\
    a_{n,0} = d_{1,0}
  \end{cases}
  \\[2mm]
  & \begin{cases}
    b_{k,t_k} = c_{k, s_k}
    \\
    a_{k,t_k} = d_{k, s_k}
  \end{cases}
  \text{for $k=1,2,\dots, n$}
  & 
\end{align*}
When we set the modulus of each oriented tetrahedra as
\begin{align*}
  z_{k,j}
  & =
  \E^{a_{k,j} - a_{k,j+1}}
  &
  w_{k,j}
  & =
  \E^{c_{k,j} - c_{k,j+1}}
\end{align*}
the developing map is drawn schematically
as Fig.~\ref{fig:developLRgeneral}.
We can then read
a condition
$  \delta_C(\boldsymbol{a}, \boldsymbol{b} ,
  \boldsymbol{c}, \boldsymbol{d}; u)
$ for meridian  as
\begin{equation}
  u=
  \frac{1}{2} 
  \sum_{k=1}^n
  \left(
    c_{k,0} - c_{k,s_{k}} - a_{k,0} + a_{k,t_{k}}
  \right)
\end{equation}
With these conditions, we have the quantum invariant
$Z_\gamma \left( \mathcal{M}_u(\varphi) \right)$, and the
Neumann--Zagier potential function
can be given by taking a classical limit $\gamma\to 0$.
As far as we know,
the A-polynomial-type invariant for the once-punctured torus bundle over
$S^1$ is not studied, but we can  obtain
such polynomials from the
Neumann--Zagier function.

Below we give a few examples for concreteness.

\begin{figure}[htbp]
  \centering
  \includegraphics[scale=0.88]{developLRgeneral.1.eps}  
  \caption{Schematic developing map for $\mathcal{M}(\varphi)$.
    Top vertex of tetrahedron with modulus $z_{1,0}$ is filled gray.
    Gray straight line denotes meridian.
  }
  \label{fig:developLRgeneral}
\end{figure}



\subsubsection{$L^2  \, R$}

We set $\varphi = L^2 \, R=
\begin{pmatrix}
  3 & 2 \\
  1 & 1
\end{pmatrix}
$.
The hyperbolic Dehn surgery of this manifold is studied in
Ref.~\citen{BetlPrzyZuko86a}.
The invariant~\eqref{Z_punctured_torus} is rewritten as
\begin{multline}
  Z_\gamma
  \left( \mathcal{M}_u(L^2 \, R)
  \right)
  \\
  =
  \int\limits_\mathbb{R} \mathrm{d} \boldsymbol{p} \,
  \delta_C(\boldsymbol{p}; u) \,
  \left\langle
    p_1 , p_5 \middle| S^{-1} \middle| p_6 , p_3
  \right\rangle \,
  \left\langle
    p_6 , p_4 \middle| S^{-1} \middle| p_2 , p_5
  \right\rangle \,
  \left\langle
    p_3 , p_2 \middle| S \middle| p_4 , p_1
  \right\rangle   
\end{multline}
When we set the modulus of tetrahedra as
$w_0=\E^{p_3 - p_5}$,
$w_1 = \E^{p_5 - p_4}$, and
$z_0 = \E^{p_1 - p_2}$,
the developing map $\mathcal{M}(L^2 \, R)$
can be depicted as Fig.~\ref{fig:developL2R}.
Then  the meridian  is read as
\begin{equation}
  p_3 - p_4 - p_1 + p_2 = 2 \, u
\end{equation}

\begin{figure}[htbp]
  \centering
    \includegraphics[scale=1.0]{developL2R.1.eps}
  \caption{Developing map of $\mathcal{M}(L^2 \, R)$.
    Gray filled triangle is top vertex of the tetrahedron with modulus
    $z_0$.
    Gray curve is meridian.
  }
  \label{fig:developL2R}
\end{figure}

In the classical limit, we have
\begin{equation}
  Z_\gamma \left( \mathcal{M}_u(L^2 \, R) \right)
  \sim
  \iint \mathrm{d} x \, \mathrm{d} y \,
  \exp \left(
    \frac{1}{2 \, \I \, \gamma} \,
    V_{\mathcal{M}(L^2 R)}(\E^x, \E^y; \E^u)
  \right)
\end{equation}
where  the potential function is computed as
\begin{multline}
  V_{\mathcal{M}(L^2 R)}(x,y;m)
  =
  \Li \left( \frac{1}{m^2 \, x} \right)
  - \Li \left( \frac{1}{ m^2 \, x \, y^2} \right)
  - \Li \left( m^2 \, x^2 \, y^2 \right)
  \\
  - \log \left( m^2 \right)
  \log \left( m^2 \, x^2 \, y^4 \right) 
  -
  2 \left(
    \log \left( x \, y \right)
  \right)^2 + \frac{\pi^2}{6}
\end{multline}



The saddle point conditions~\eqref{hyperbolic_consistency},
which correspond to the hyperbolic consistency condition,
reduce to
\begin{equation}
  \label{consistent_L2R}
  \begin{gathered}
    \frac{
      \left( -1 + m^2 \, x \right) \,
      \left( -1 + m^2 \, x^2 \, y^2 \right)^2
    }{
      m^4 \, x^4 \, y^2 \,
      \left( -1 + m^2 \, x \, y^2 \right)
    } = 1 \\[2mm]

    \frac{
      \left(-1 + m^2 \, x^2 \,y^2 \right)
    }{
      m^2 \, x \,  \left( -1 + m^2 \, x \, y^2  \right)
    }
    =1
  \end{gathered}
\end{equation}
and,
as~\eqref{differential_longitude},
the longitude is defined by
\begin{equation}
  \label{longitude_L2R}
  \ell =
  - \frac{
    ( -1 + m^2 \, x) \,
    ( -1 + m^2 \, x^2 \, y^2 )
  }{
    m^4 \, x^2 \, y^2 \, ( -1 + m^2 \, x \, y^2)
  }
\end{equation}

In the case of complete case $m=1$, we 
find that
$
(x,y^2)=
\left(
  \frac{1 \pm \sqrt{7} \, \I}{4},
  \frac{-1 \pm \sqrt{7} \, \I}{2}
\right)
$ solves the consistency condition~\eqref{consistent_L2R}.
Among these, we can check numerically that
the largest value
of the imaginary part of the potential function at the saddle points
\begin{equation*}
  \Im V_{\mathcal{M}(L^2 R)}(x,y;m=1)
  =
  D \left( \frac{1}{ x} \right)
  - D \left( \frac{1}{  x \, y^2} \right)
  - D \left(  x^2 \, y^2 \right)
\end{equation*}
 coincides
with the hyperbolic volume  
$\Vol \left(\mathcal{M}(L^2 \, R) \right)
= 2.66674 \cdots$.

The A-polynomial is now given by eliminating $x$ and $y$ from the  set of
equations,~\eqref{consistent_L2R} and~\eqref{longitude_L2R},
and we obtain the algebraic curve
$A_{\mathcal{M}(L^2 R)}(\ell,m)=0$ whose  Newton polygon is given by
\begin{equation*}
  \begin{pmatrix}
    0 & -1 & 0
    \\
    0 & 2 & 1
    \\
    1 & 2 & 0
    \\
    0 & -1 & 0
  \end{pmatrix}
\end{equation*}



\subsubsection{$L \, R^3$}

We take another example $\varphi= L\, R^3
=
\begin{pmatrix}
  4 & 1 \\
  3 & 1
\end{pmatrix}
$.
In this case, the invariant~\eqref{Z_punctured_torus} becomes
\begin{multline}
  Z_\gamma(\mathcal{M}_u(L \, R^3))
  =
  \int\limits_{\mathbb{R}} \mathrm{d} \boldsymbol{p} \,
  \delta_C(\boldsymbol{p};u) \,
  \left\langle p_1, p_4 \middle|  S \middle| p_3, p_2 \right\rangle \,
  \left\langle p_3, p_6 \middle|  S \middle| p_5, p_4 \right\rangle
  \\
  \times
  \left\langle p_5, p_8 \middle|  S \middle| p_7, p_6 \right\rangle \,
  \left\langle p_2, p_7 \middle|  S^{-1} \middle| p_8, p_1 \right\rangle 
\end{multline}
We set the modulus of each tetrahedron as
\begin{align*}
  z_0 & = \E^{p_2 - p_4}
  &
  z_1 & = \E^{p_4 - p_6}
  \\
  z_2 & = \E^{p_6 - p_8}
  &
  w_0 & = \E^{p_1 - p_7}
\end{align*}
The developing map is depicted in Fig.~\ref{fig:developLR3}, and
the meridian is read as $\frac{w_0}{z_0 \, z_1 \, z_2}$.
We thus have
a condition of $\delta_C(\boldsymbol{p} ; u)$ as
\begin{equation}
  p_1 - p_7 - p_2 + p_8 =  2 \, u
\end{equation}

\begin{figure}[htbp]
  \centering
  \includegraphics[scale=0.88]{developLR3.1.eps}
  \caption{Developing map of $\mathcal{M}(L \, R^3)$.}
  \label{fig:developLR3}
\end{figure}


In the classical limit, we obtain
\begin{equation}
  Z_\gamma(\mathcal{M}_u(L \, R^3))
  \sim
  \iiint \mathrm{d} x \, \mathrm{d} y \, \mathrm{d} z \,
  \exp
  \left(
    \frac{1}{2 \, \I \, \gamma} \,
    V_{\mathcal{M}(L R^3)}(\E^x , \E^y , \E^z ; \E^u)
  \right)
\end{equation}
where the potential function is computed as
\begin{multline}
  V_{\mathcal{M}(L R^3)}(x , y , z; m)
  =
  - \Li\left(\frac{1}{m^4 \, y}\right)
  +  \Li\left(\frac{1}{m^2 \, x  \, y \, z^2}\right)
  + \Li\left( m^2 \, x^2 \, z \right)
  \\
  + \Li \left( \frac{m^2 \, y^2 \, z}{x} \right)
  -\left( \log \left( m^2 \right) \right)^2
  + 2 \log\left(\frac{x}{m^2}\right) \log\left(\frac{x}{y}\right)
  \\
  + 2 \log y \log ( y \, z) + 2 \log z \log(x \, z \, m^2)
  -\frac{\pi^2}{3}
\end{multline}
In the case of complete case $m=1$, we can check numerically
that among algebraic solutions of~\eqref{hyperbolic_consistency}
the maximum of the imaginary part of
$V_{\mathcal{M}(L R^3)}(x,y,z;m=1)$,
\begin{equation*}
  \Im V_{\mathcal{M}(L R^3)}(x , y , z; 1)
  =
  - D \left(\frac{1}{ y}\right)
  +  D \left(\frac{1}{ x  \, y \, z^2}\right)
  + D\left(  x^2 \, z \right)
  + D \left( \frac{ y^2 \, z}{x} \right)
\end{equation*}
coincides with the hyperbolic volume
$\Vol(\mathcal{M}(L \, R^3))= 2.98912 \cdots$.
See Ref.~\citen{Franca04a} where algebraic solutions of consistency
equations are investigated in detail.

Correspondingly we obtain the A-polynomial for  $\mathcal{M}(L \, R^3)$
by eliminating $x$, $y$, and $z$ from a set of equations.
Explicitly the polynomial $A_{\mathcal{M}(L R^3)}(\ell,m)$ is given in
the form of Newton
polygon as follows;
\begin{equation*}
  \begin{pmatrix}
    0 & 0 & 0 & 1 & 0 & 0
    \\
    0 & 0 & 0 & -3 & 0 & 0
    \\
    -1 & -2 & -3 & -1 & -2 & 0
    \\
    0 & -3 & -2 & 2 & 3 & 0
    \\
    0 & 2 & 1 & 3 & 2 & 1
    \\
    0 & 0 & 3 & 0 & 0 & 0
    \\
    0 & 0  & -1 & 0 & 0 & 0
  \end{pmatrix}
\end{equation*}






\section{Conclusion and Discussion}


We have constructed  quantum invariant
$Z_\gamma(\mathcal{M})$
for cusped hyperbolic
3-manifolds $\mathcal{M}$
by assigning the Faddeev quantum dilogarithm function to oriented
ideal tetrahedra.
Once the triangulation of cusped 3-manifold $\mathcal{M}$ is given, it
is rather
straightforward to define the invariant $Z_\gamma(\mathcal{M})$ in an
integral form.
In the classical limit, the Faddeev integral reduces to the
dilogarithm function, which denotes the hyperbolic volume of ideal
tetrahedron.
Remarkable is that
the saddle point conditions coincide with the hyperbolic
consistency conditions around edges~\cite{Hikam00d}.
We have discussed as a variant of the volume conjecture
that the invariant
$Z_\gamma(\mathcal{M})$, which can be regarded as a generalization of
the Kashaev invariant (specific value of the colored Jones polynomial),
is dominated by the hyperbolic volume  in the classical limit
$\gamma\to 0$.


We have shown  that the invariant
can be defined for a one-parameter  deformation 
of  manifold $\mathcal{M}_u$ (not complete),
and that the Neumann--Zagier potential function can be given by taking
a classical limit $\gamma\to 0$.
Correspondingly the A-polynomial can be computed from the potential
function~\eqref{v_differential_limit}.
This  supports  the generalized volume conjecture.
We have demonstrated by taking examples
that our method recovers
previously known A-polynomial when $\mathcal{M}$ is a complement of
hyperbolic knots.
We have further  applied our method  in the case of the once-punctured torus bundle over
the circle.
It seems that the A-polynomial-type invariant is not known for this
3-manifold,
and  it will be interesting to study a relationship with the boundary slope.
To conclude,
our results indicate that the $S$-operator~\eqref{define_S_operator}
denotes the quantum Bloch
invariant for oriented ideal tetrahedron.

The A-polynomial may give an interesting insight for mathematical
physics.
For example, the Mahler measure of the A-polynomial is expected to
coincide with
the hyperbolic volume of knot.
On the other hand, the Mahler measure of the determinant of the
Kasteleyn matrix has appeared as the free energy
of the dimer problem.
From the viewpoint of our combinatorial
construction of the quantum invariant,
the quantum invariants based on
oriented ideal triangulation may be interpreted  as a matching of
in-states and out-states, and it might be interesting to investigate a
Kasteleyn matrix interpretation of the A-polynomial.



\section{Acknowledgments}

We have used computer programs,
SnapPea~\cite{SnapPea99}, Knotscape~\cite{Knotscape99}, and
Snap~\cite{CouGooHodNeu00a}, in studying triangulation of manifolds.
We have also used \texttt{Mathematica} and Pari/GP.
Pictures of knots in this paper are drawn using KnotPlot~\cite{KnotPlot}.
This work is supported in part  by Grant-in-Aid for Young Scientists
from the Ministry of Education, Culture, Sports, Science and
Technology of Japan.
