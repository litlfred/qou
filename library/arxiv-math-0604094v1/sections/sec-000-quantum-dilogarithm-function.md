---
doc_id: arxiv-math-0604094v1
doc_title: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant"
section_id: sec-000-quantum-dilogarithm-function
section_title: "Quantum Dilogarithm Function"
section_number: null
pages: 3-12
source_pdf: 0604094v1.pdf
source_sha256: f0c4c36ab0acf537
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.956
doc_brief: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant — 9 sections: Front matter; Quantum Dilogarithm Function; Examples"
---
\label{sec:dilog}
We define a function  $\Phi_\gamma(\varphi)$ by an integral form
following Ref.~\citen{LFadd99b}.
We set
$\gamma \in \mathbb{R}$, and for 
$ | \Im \varphi | < \pi$, we define
\begin{equation}
  \label{Faddeev_integral}
  \Phi_\gamma(\varphi)
  =
  \exp
  \left(
    \int\limits_{\mathbb{R}+\I \, 0}
    \frac{\E^{- \I \, \varphi \, x}}
    {
      4 \sinh ( \gamma \, x) \, \sinh(\pi \, x)
      } \,
    \frac{\mathrm{d} x}{x}
  \right) 
\end{equation}
The Faddeev integral~\eqref{Faddeev_integral}, which we call the
quantum dilogarithm function, is also related to the
double sine function~\cite{KharLebeSeme01a,TShinta77a,NKurok91a},
the hyperbolic gamma function~\cite{Ruijse97a,EBarn01a}
and the quantum exponential function~\cite{SLWoron00a}.
We see that 
the integral  $\Phi_\gamma(\varphi)$ has a duality,
\begin{equation}
  \Phi_{\frac{\pi^2}{\gamma}} ( \varphi)
  =
  \Phi_{\gamma} \left(
    \frac{\gamma}{\pi} \, \varphi
  \right) 
\end{equation}
and that it satisfies the inversion relation,
\begin{equation}
  \label{inversion_Phi}
  \Phi_\gamma( \varphi ) \cdot \Phi_\gamma( - \varphi)
  =
  \exp
  \left(
    - \frac{1}{2 \, \I \, \gamma}
    \Bigl(
    \frac{\varphi^2}{2} + \frac{\pi^2 + \gamma^2}{6}
    \Bigr)
  \right) 
\end{equation}
The Faddeev integral satisfies the difference equations;
\begin{subequations}
  \begin{align}
    \frac{\Phi_\gamma(\varphi + \I \, \gamma)}
    {    \Phi_\gamma(\varphi - \I \, \gamma)}
    & =
    \frac{1}{1 + \E^\varphi}         
    \\[2mm]

    \frac{ \Phi_\gamma(\varphi + \I \, \pi)}{
      \Phi_\gamma(\varphi - \I \, \pi)}
    & =
    \frac{1}{1 + \E^{\frac{\pi}{\gamma}\varphi}} 
  \end{align}
\end{subequations}
Due to these relations, the integral $\Phi_\gamma(\varphi)$ defined
in~\eqref{Faddeev_integral}
is
analytically continued to $\varphi \in \mathbb{C}$,
and we see that
  \begin{equation}
    \text{zeros of $\bigl( \Phi_\gamma(\varphi) \bigr)^{\pm 1}$}
    =
    \Bigl\{
    \varphi =
    \mp \I \,
    \bigl(
    (2 \, m +1 ) \, \gamma +
    ( 2 \, n + 1 ) \, \pi
    \bigr)
    \ \big| \
    m, n \in \mathbb{Z}_{\geq 0}
    \Bigr\}


















  \end{equation}



The most important properties of the Faddeev integral is that
it fulfills the pentagon
identity~\cite{FaddKash94,LFadd99b}
\begin{equation}
  \label{pentagon_Phi}
  \Phi_\gamma(\Hat{p}) \, \Phi_\gamma(\Hat{q})
  =
  \Phi_\gamma(\Hat{q}) \, \Phi_\gamma(\Hat{p} + \Hat{q}) \,
  \Phi_\gamma(\Hat{p})  
\end{equation}
where $\Hat{p}$ and $\Hat{q}$ are the canonically conjugate
operators satisfying the Heisenberg commutation relation,
\begin{equation}
  \label{canonical}
  [\Hat{p} ~,~ \Hat{q} ]
  = \Hat{p} \, \Hat{q} - \Hat{q} \, \Hat{p}
  = - 2 \, \I \, \gamma   
\end{equation}
By this commuting relation, we call a limit $\gamma\to 0$  a
classical limit.

We use
$\mathbf{V}$ as the momentum space $|p\rangle$ with
$p\in\mathbb{R}$ which is  an eigenstate of the momentum operator;
\begin{equation}
  \Hat{p} \, | p \rangle
  =
  p \, | p \rangle .
\end{equation}









A reason of the \emph{quantum} dilogarithm function reveals when
we take a \emph{classical} limit $\gamma\to 0$.
In this limit, the Faddeev integral reduces to
\begin{equation}
  \label{Phi_gamma_0}
  \Phi_\gamma(\varphi)

  \sim
  \exp
  \left(
    \frac{1}{2 \,  \I \, \gamma} \,
    \Li(- \E^\varphi)
  \right) 



\end{equation}
where $\Li(x)$ denotes the Euler dilogarithm function defined by
(see, \emph{e.g.}, Refs.~\citen{LLewi81a,Kiril94})
\begin{equation}
  \label{Euler_dilogarithm}
  \Li(x)
  =
  \sum_{n=1}^\infty \frac{x^n}{n^2} 
\end{equation}
where $|x| \leq 1$.
For $x \in \mathbb{C}$, we use the integral form
\begin{equation*}
  \Li(x) =
  -
  \int_0^x  \log(1-s)  \, \frac{\mathrm{d} s}{s} 
\end{equation*}
where the branch of $\log(1-s)$ is on
 $\mathbb{C}\setminus [ 1, \infty)$
for which $\log(1-0)=0$.
See that the inversion relation~\eqref{inversion_Phi} of the quantum
dilogarithm function $\Phi_\gamma(\varphi)$ gives that of the Euler
dilogarithm function as
  \begin{equation*}
    \Li(- \E^x) + \Li(-\E^{-x})
    +
    \frac{x^2}{2} + \frac{\pi^2}{6} = 0 
  \end{equation*}





We note that
the Fourier transformation of the Faddeev integral can be computed as
follows~\cite{SLWoron00a,FaddKashVolk00a,BytskTesch02a,KharLebeSeme01a};
\begin{gather}
  \label{Fourier_transform_1}
  \frac{1}{\sqrt{4 \, \pi \, \gamma}}
  \int\limits_{\mathbb{R}}
  \mathrm{d} y \ \Phi_\gamma(y) \,
  \E^{\frac{1}{2 \, \I \, \gamma} \, x \, y}
  =
  \Phi_\gamma(-x + \I \pi + \I \gamma)
  \,
  \E^{
    \frac{1}{2 \, \I \, \gamma}
    \left(
      \frac{x^2}{2}
      - \frac{1}{2} \pi \gamma
      -
      \frac{\pi^2 + \gamma^2}{6}
    \right)
  } 
  \\[2mm]

  \label{Fourier_transform_2}
  \frac{1}{\sqrt{4 \, \pi \, \gamma}}
  \int\limits_{\mathbb{R}} \mathrm{d} y \
  \frac{1}{\Phi_\gamma(y)} \,
  \E^{
    \frac{1}{2 \, \I \, \gamma} x \, y
  }
  =
  \frac{1}{
    \Phi_\gamma(x - \I\, \pi - \I\, \gamma)
  } \,
  \E^{
    -\frac{1}{2 \, \I \, \gamma}
    \left(
      \frac{x^2}{2}
      - \frac{1}{2} \pi \gamma
      - \frac{\pi^2+\gamma^2}{6}
    \right)
  } 





























\end{gather}






To see a relationship between the integral $\Phi_\gamma(\varphi)$ with
geometry,
we   define the $S$-operator acting  on $\mathbf{V}\otimes\mathbf{V}$ by
\begin{equation}
  \label{define_S_operator}
  S_{1,2}
  =
  \E^{
    \frac{1}{2 \,  \I\, \gamma} \,
    \Hat{q}_1 \, \Hat{p}_2
    } \,
  \Phi_\gamma (\Hat{p}_1 + \Hat{q}_2 - \Hat{p}_2) 
\end{equation}
Here  the Heisenberg operators $\Hat{p}_j$
and $\Hat{q}_j$ act on the $j$-th  vector
space of $\mathbf{V}\otimes\mathbf{V}$,
\emph{i.e.}
$\Hat{p}_1 = \Hat{p} \otimes 1$,
$\Hat{p}_2 = 1 \otimes \Hat{p} $, and so on.
Then the pentagon identity~\eqref{pentagon_Phi} can be
rewritten  in a compact form;
\begin{equation}
  \label{pentagon_S}
  S_{2,3} \, S_{1,2}
  =
  S_{1,2} \, S_{1,3} \, S_{2,3} 
\end{equation}
where $S_{j,k}$ acts on the $j$- and $k$-th spaces of
$\mathbf{V}\otimes \mathbf{V} \otimes \mathbf{V}$.
Matrix elements can be computed by use of~\eqref{Fourier_transform_1}
and~\eqref{Fourier_transform_2};
\begin{subequations}
  \label{S_element_2}
  \begin{gather}
    \begin{split}
      & \langle p_1, p_2  \ | \ S_{1, 2}  \ | \ p_1^\prime , p_2^\prime \rangle
      \\
      &  \qquad =
      \frac{1}{\sqrt{4 \, \pi \, \gamma}} \,
      \delta(p_1 + p_2 - p_1^\prime) \cdot
      \Phi_\gamma(p_2^\prime - p_2
      + \I \, \pi + \I \, \gamma) \,
      \E^{\frac{1}{2 \, \I \, \gamma}
        \left(
          - \frac{\pi^2 + \gamma^2}{6} - \frac{\gamma \, \pi}{2}
          + p_1 \, (p_2^\prime - p_2)
        \right)
        } 
    \end{split}
    \\[4mm]

    \begin{split}
      & \langle p_1, p_2 \ | \ S_{1, 2}^{~-1} \ | \ p_1^\prime , p_2^\prime
      \rangle
      \\
      &  \qquad =
      \frac{1}{\sqrt{4 \, \pi \, \gamma}} \,
      \delta(p_1 - p_1^\prime - p_2^\prime) \,
      \frac{1}{
        \Phi_\gamma(p_2 - p_2^\prime - \I \, \pi
        - \I \, \gamma)
        } \,
      \E^{
        \frac{1}{2 \I \gamma}
        \left(
        \frac{\pi^2 + \gamma^2}{6}
        + \frac{\gamma \, \pi}{2}
        - p_1^\prime ( p_2 - p_2^\prime)
        \right)
        } 
    \end{split}
  \end{gather}
\end{subequations}

In the classical limit $\gamma \to 0$, we find 
by use of \eqref{Phi_gamma_0}
that the $S$-operators~\eqref{S_element_2} 
reduce to
\begin{subequations}
  \label{S_asymptotics}
  \begin{align}
    \langle p_1 , p_2 \ | \ S_{1,2}  \ | \ p_1^\prime , p_2^\prime \rangle
    & \sim
    \delta(p_1 + p_2 - p_1^\prime) \cdot
    \exp
    \left(
      - \frac{1}{2 \, \I \, \gamma}
      \, V(p_2^\prime - p_2 , p_1)
    \right) 


















  \\[2mm]


  \langle p_1 , p_2 \  | \ S_{1,2}^{-1} \ | \ p_1^\prime , p_2^\prime \rangle
  &
  \sim
  \delta(p_1 - p_1^\prime - p_2^\prime) \cdot
  \exp
  \left(
    \frac{1}{ 2 \, \I \, \gamma} \,
    V(p_2 - p_2^\prime , p_1^\prime)
  \right) 


















\end{align}
\end{subequations}
where we have defined  the function $V(x,y)$ by
\begin{equation}
  V(x,y)
  =
  \frac{\pi^2}{6} - \Li(\E^x) - x \, y .
\end{equation}
We see that the function $V(x,y)$ satisfies partial differential
equations;
\begin{gather}
  \label{V_partial}
  V(x,y)
  =
  L(1- \E^x)
    +
    \frac{1}{2}
    \left(
      x \, \frac{\partial V(x,y)}{\partial x}
      +
      y \, \frac{\partial V(x,y)}{\partial y}
    \right) 
    \\[3mm]

    \label{imaginary_V_saddle}
    \Im \, V(x,y)
    =
    D(1-\E^x)
    +
    \log | \E^x | \cdot
    \Im \, \biggl( \frac{\partial}{\partial x} V(x,y) \biggr) 
    +
    \log | \E^y | \cdot
    \Im \, \biggl( \frac{\partial}{\partial y} V(x,y) \biggr) 
  \end{gather}
Here
the Rogers dilogarithm $L(z)$ and the
Bloch--Wigner  function $D(z)$
are respectively defined  in terms of the Euler dilogarithm
function~\eqref{Euler_dilogarithm} by
\begin{align}
  L(z)
  & =
  \Li(z) + \frac{1}{2} \log z \, \log(1-z) 
  \\[3mm]

  \label{Bloch_Wigner}
  D(z)
  & =
  \Im \, \Li(z) + \arg(1-z) \cdot \log |z| 
\end{align}
both of which fulfill the pentagon identity
(see, \emph{e.g.}, Ref.~\citen{LLewi81a});
\begin{gather}
  \label{Rogers_pentagon}





  L(z) - L(w)
  +
  L \left(\frac{w}{z} \right)
  - L\left( \frac{1-z^{-1}}{1- w^{-1}} \right)
  + L\left( \frac{1-z}{1-w} \right)
  =
  \frac{\pi^2}{6}
  \\[2mm]





  \label{Bloch-Wigner_pentagon}
   D(z) - D(w)
   +
   D \left(\frac{w}{z} \right)
   - D\left( \frac{1-z^{-1}}{1- w^{-1}} \right)
   + D\left( \frac{1-z}{1-w} \right)
   =0
\end{gather}



\section{Quantum Invariant and Potential Function}
\label{sec:invariant}


The result that the $S$-operator satisfies the pentagon
identity~\eqref{pentagon_S} indicates that we can assign 
(oriented) tetrahedron to each $S$-operator.
See Refs.~\citen{ChekFock99a,RKasha01a}
(also Ref.~\citen{ChekPenn03a})
for another interpretation as a
quantization of the Teichm{\"u}ller theory.
In the classical limit $\gamma\to 0$,
imaginary part of
the $S$-operator gives the Bloch--Wigner function
$D(z)$ which
denotes  the
hyperbolic volume of the ideal tetrahedron
$\Delta(z)$
with totally geodesic faces
which has a modulus $z$
(see, \emph{e.g.}, Refs.~\citen{BenedPetro92a,JMiln82a,WPThurs80Lecture}).
Extra terms in~\eqref{imaginary_V_saddle}
including partial differentials of $V(x,y)$
can be neglected when we assume a
saddle point condition as will be discussed later,
and 
we can assign the oriented hyperbolic ideal
tetrahedra to these $S$-operators as follows~\cite{Hikam00d};
\begin{align}

  \left\langle
    a, b \  \middle| \ S \  \middle| \  c , d 
  \right\rangle
  & =
  \mbox{
    \raisebox{-1.6cm}{





      \includegraphics[scale=1.6]{tetrahedronProj.1.eps}
    }
  }
  =
  \mbox{
    \raisebox{-1.6cm}{

      \includegraphics[scale=1.0]{tetrahedron.1.eps}
    }
  }
  \label{S_tetrahedron}

  \\[4.8mm]


  \left\langle
    a, b \  \middle| \ S^{-1} \  \middle| \  c, d
  \right\rangle
  & =
  \mbox{
    \raisebox{-1.6cm}{

      \includegraphics[scale=1.6]{tetrahedronDualProj.1.eps}
    }
  }
  =
  \mbox{
    \raisebox{-1.6cm}{

      \includegraphics[scale=1.0]{tetrahedronDual.1.eps}
    }
  }
  \label{S_tetrahedronDual}
\end{align}
Namely in the momentum space  representation 
we assign four
momentum parameters $\{ a , b, c , d\}$ to faces of tetrahedron.
This differs from the (quantum) $6j$ symbol as a solution of the pentagon
identity~\cite{PonzaTRegg68a,KirilReshe89}, which was used to define
the topological (quantum) gravity.

Here both ideal tetrahedra have the modulus $z = \E^{d-b}$,
and we mean that the dihedral angles are given by
\begin{align*}

  z[1] & = z=  \E^{d-b} 
  \\[2mm]
  z[2] & = 1- \frac{1}{z} 
  \\[2mm]
  z[3] & = \frac{1}{1-z} 
\end{align*}































The cross sections by the horosphere


is similar to the triangle
in $\mathbb{C}$ with vertices $0$, $1$, and $z$ (see
Fig.~\ref{fig:triangle}),
and we have
$z[1] \, z[2] \, z[3] = -1$.
See that the opposite edges of tetrahedra have the same dihedral angles.
Then  the hyperbolic volume of the ideal tetrahedron
$\Delta(z)$ with modulus $z$ is
given by~\cite{WPThurs80Lecture}
\begin{align}
  \Vol \left( \Delta(z) \right)
  & =
  D(z)
  \nonumber
  \\
  & =
  \Lob \left(\arg(z[1]) \right)
  + \Lob \left(\arg(z[2]) \right)
  + \Lob \left( \arg(z[3]) \right)
\end{align}
where $\Lob(\theta)$  is the Lobachevsky function defined by
\begin{equation}
  \Lob(\theta)
  =
  \frac{1}{2} \sum_{n=1}^\infty \frac{\sin(2 \, n \, \theta)}{n^2}
\end{equation}

\begin{figure}
  \centering

  \includegraphics[scale=1.2]{triangle.1.eps}
  \caption{Triangle with vertices $0$, $1$, and $z$ in
    $\mathbb{C}$. Here we set
    $ z[1] = z$, $z[2] = 1 - \frac{1}{z}$, and $z[3] = \frac{1}{1-z}$.
  }
  \label{fig:triangle}
\end{figure}


Any hyperbolic cusped $3$-manifold $\mathcal{M}$
(for simplicity we assume that the manifold $\mathcal{M}$ has one cusp
in this paper)
can be ideally
triangulated, and
it is  constructed from finite
number of the oriented ideal tetrahedra in~\eqref{S_tetrahedron}
and~\eqref{S_tetrahedronDual}.
Other types of oriented ideal tetrahedra,
such as one that has a face with loop,
are prohibited.
So   our triangulation sometimes differ from
the canonical triangulation used in computer programs, such as
SnapPea~\cite{SnapPea99}, Knotscape~\cite{Knotscape99}, and
Snap~\cite{CouGooHodNeu00a}.

To construct
3-manifolds from these ideal  tetrahedra, we glue each face to
match orientations of edges.
Every faces have no loops, so there is no ambiguity in gluing faces
together once two faces to be glued are fixed.
Furthermore,
one finds that in-state $|p \rangle$ can glue only with
out-states
$\langle p|$,
and that we cannot glue two in-states or out-states together.
As suggested by the momentum representation of the pentagon identity,
gluing  two faces, which have same label $p$,
can be formulated by an
integration with respect to $p$,
$\int\limits_\mathbb{R} \mathrm{d} p \, | p \rangle \, \langle p |$.




By these identifications of the $S$-operators as the oriented ideal
tetrahedra, the pentagon identity~\eqref{pentagon_S} is identified with
the Pachner move as is depicted in
Fig.~\ref{fig:pentagon_S};
oriented polytope with 5 vertices can be decomposed into
2 tetrahedra with a face in common, or into 3 tetrahedra with an edge
in common.
In case of decomposing into 3 tetrahedra, we need a hyperbolic
consistency condition around the common edge.
This condition coincides with a saddle point condition of the right
hand side of~\eqref{pentagon_S} after substituting~\eqref{S_element_2}
and taking a classical limit $\gamma \to 0$.







One can see a coincidence  for any other type of gluings
such as other choices of orientations in the Pachner move
between the hyperbolic consistency condition
and the saddle point equations~\cite{Hikam00d}.


\begin{figure}
  \centering
  \includegraphics[scale=0.48]{pentagon.1.eps}
  \caption{Pentagon identity~\eqref{pentagon_S} is interpreted as the
    Pachner move.}
  \label{fig:pentagon_S}
\end{figure}






Once triangulation is given and we know how to glue faces together,
we can naturally define the quantum invariant for hyperbolic
cusped $3$-manifold $\mathcal{M}$
based on the
$S$-operator by
\begin{equation}
  \label{define_Z}
  Z_\gamma(\mathcal{M})
  =
  \int\limits_\mathbb{R}
  \mathrm{d} \boldsymbol{p} \,
  \delta_C(\boldsymbol{p}) \,
  \delta_G(\boldsymbol{p}) \,
  \prod_{i=1}^M 
  \left\langle
    p_{2i-1}^{(-)}, p_{2 i}^{(-)}
    ~ \middle| ~ S^{\varepsilon_i}
    ~ \middle| ~ 
    p_{2i-1}^{(+)}, p_{2 i}^{(+)}
  \right\rangle 
















\end{equation}
where $\boldsymbol{p}$ denotes a set of variables
$(p_1^{(\pm)}, p_2^{(\pm)}, \dots , p_{2M}^{(\pm)})$,
and
$\varepsilon_i = \pm 1$ depending on an orientation of
tetrahedron.
We set
$M$ as  the number of ideal tetrahedra.
The condition 
$  \delta_G(\boldsymbol{p})$




determines how to glue faces together
(``G'' stands for ``gluing'').
Every faces with same momentum  mean to be glued together, and the
fact that in-states can be glued only with out-states indicates that 
the gluing condition
$  \delta_G(\boldsymbol{p})$




is  a product of
$\delta\left(p_{j}^{(-)} - p_{k}^{(+)}\right)$








We need another geometrical condition
$ \delta_C(\boldsymbol{p})$






to define invariant
besides a way how to glue faces
(``C'' stands for ``completeness'')~\cite{KHikami01e}.
We can draw a developing map from an ideal triangulation of
3-manifold,
and we need to read off  a hyperbolic complete condition.
This condition
can be written as a constraint for $\boldsymbol{p}$ by
identifications~\eqref{S_tetrahedron} and~\eqref{S_tetrahedronDual}.
By construction, the partition function
$Z_\gamma(\mathcal{M})$
is invariant under the Pachner move (Fig.~\ref{fig:pentagon_S}),
and it is essentially the invariant constructed in
Ref.~\citen{Hikam00d}.





As was studied by Thurston~\cite{WPThurs86a},
\emph{deformation}   of the hyperbolic structure on the manifold
$\mathcal{M}$ can be holomorphically parametrized by a parameter $u$
in a neighborhood of completeness condition $u=0$.
The parameter $u$
is the logarithm of the
eigenvalue of the meridian by the holonomy representation, and
we set
\begin{equation}
  \label{meridian_m_u}
  m= e^u
\end{equation}
Correspondingly  we call such  manifold $\mathcal{M}_u$ which is no
more complete,
and define the invariant by
\begin{equation}
  \label{define_deform_Z}
  Z_\gamma(\mathcal{M}_u)
  =
  \int\limits_\mathbb{R}
  \mathrm{d} \boldsymbol{p} \,
  \delta_C(\boldsymbol{p}; u) \,
  \delta_G(\boldsymbol{p}) \,
  \prod_{i=1}^M 
  \left\langle
    p_{2i-1}^{(-)}, p_{2 i}^{(-)}
    ~ \middle| ~ S^{\varepsilon_i}
    ~ \middle| ~ 
    p_{2i-1}^{(+)}, p_{2 i}^{(+)}
  \right\rangle 


















\end{equation}
Here the condition
$\delta_C(\boldsymbol{p} ; u)$






follows from that the meridian has a holonomy~\eqref{meridian_m_u}.
The invariant~\eqref{define_Z} for $\mathcal{M}$ with complete
hyperbolic structure follows
from~\eqref{define_deform_Z} by assuming a completeness 
$u=0$ of the
hyperbolic structure of $\mathcal{M}_u$;
\begin{equation}
  Z_\gamma(\mathcal{M})
  =
  Z_\gamma \left( \mathcal{M}_{u=0} \right)
\end{equation}
because
\begin{equation}
  \delta_C(\boldsymbol{p})
  =
  \delta_C(\boldsymbol{p} ; u=0)









\end{equation}
























We now study a classical limit of our quantum invariant
$Z_\gamma(\mathcal{M}_u)$.
When we take a  limit $\gamma \to 0$
by use of~\eqref{S_asymptotics},
the quantum invariant defined by~\eqref{define_deform_Z} becomes
\begin{align}
  Z_\gamma \left( \mathcal{M}_u \right)
  &\sim
  \int\limits_{\mathbb{R}} \mathrm{d} \boldsymbol{p} \,
  \delta_C(\boldsymbol{p}; u) \,
  \delta_G(\boldsymbol{p}) \,
  \left[
    \prod_{i=1}^M
    \delta \left(
      p_{2i-1}^{( \varepsilon_i)} - p_{2i-1}^{( - \varepsilon_i)}
      -p_{2i}^{( - \varepsilon_i)}
    \right)
  \right]
  \nonumber \\
  & \qquad \qquad 
  \times
  \exp
  \left(
    \frac{\I}{2 \, \gamma} 
    \sum_{i=1}^M
    \varepsilon_i \,
    V \left(
      p_{2i}^{(\varepsilon_i)} - p_{2i}^{( - \varepsilon_i)} ,
      p_{2i-1}^{( - \varepsilon_i)}
    \right)
  \right)
  \nonumber
  \\
  & =
  \int\limits_{\mathbb{R}} \mathrm{d} \boldsymbol{x}  \,
  \exp
  \left(
    \frac{1}{2 \, \I \, \gamma} \,
    \Phi_{\mathcal{M}}(\boldsymbol{x}; u )
  \right)
  \label{classical_partition_function}
\end{align}
Here in the last equality for our convention
we have re-parametrized variables

$\boldsymbol{p}$
with
$\boldsymbol{x}
=
\left(
  x_1, x_2, \dots, x_{M-1}
\right)$  after incorporating constraints written in
terms of delta functions.





The integral~\eqref{classical_partition_function} could be evaluated
by the saddle point method as we have taken a 
classical
limit $\gamma\to 0$.
The saddle point condition for
variables $\boldsymbol{x}$ is
\begin{equation}
  \label{hyperbolic_consistency}
  \frac{\partial }{\partial x_i}
  \Phi_\mathcal{M} (\boldsymbol{x}   ; u) = 0 
\end{equation}
As was extensively studied in Ref.~\citen{Hikam00d},
these conditions coincide with 
hyperbolic consistency conditions around 
edges when we glue oriented tetrahedra together.
By construction
the variable $u$ denotes the meridian of cusp in
this classical limit,
and the complete hyperbolic structure is  realized by setting $u=0$.
To conclude, the function $\Phi_{\mathcal{M}}(\boldsymbol{x} ; u)$
defined 
by a classical limit~\eqref{classical_partition_function} of the
quantum invariant $Z_\gamma(\mathcal{M}_u)$
is nothing but
the
Neumann--Zagier
potential function~\cite{NeumZagi85a,TYoshi85a}.



As a result, differential of the potential function with respect to
the
deformation parameter $u$ gives
\begin{equation}
  \label{differential_longitude}


  \frac{\partial}{\partial  u}  \,
  \Phi_{\mathcal{M}}(\boldsymbol{x} ; u)
  =

  2 \, v
\end{equation}
where $v$ is related to the
eigenvalue of the longitude by the holonomy representation
\begin{equation}
  \ell = \E^{v}
\end{equation}
Variables  $x_i$ can be solved from the hyperbolic consistency
equation~\eqref{hyperbolic_consistency} as a function of $u$,
and we can regard the potential function
$\Phi_\mathcal{M}(\boldsymbol{x};u)$ as a function of $u$;
$\Phi_\mathcal{M}(u) =
\left.
  \Phi_{\mathcal{M}}( \boldsymbol{x} ; u)
\right|_{\eqref{hyperbolic_consistency}}$.
Then we can rewrite~\eqref{differential_longitude} by
\begin{equation}
  \label{v_differential_limit}
  \frac{\mathrm{d}}{\mathrm{d} u}
  \lim_{\gamma \to 0 }
  \I \, \gamma \,
  \log Z_\gamma\left( \mathcal{M}_u \right)
  =  v
\end{equation}
We note that our variables $(u,v)$ differs from those in
Ref.~\citen{NeumZagi85a};
when we denote their variables $(u_{\text{NZ}}, v_{\text{NZ}})$, we
have
\begin{equation}
  \label{uv_NZ}
  (u, v) =
  \left(
    \frac{u_{\text{NZ}}}{2} ,
    \frac{v_{\text{NZ}}}{2} + \pi \, \I
  \right)
\end{equation}
Hereafter we  also use  the function
$V_{\mathcal{M}}(\boldsymbol{x}; m)$ defined by
\begin{equation}
  V_{\mathcal{M}}(x_1, x_2, \dots ; m)
  =
  \Phi_{\mathcal{M}}(\log x_1, \log x_2, \dots ;  u=\log m)
\end{equation}

As seen from~\eqref{V_partial} and~\eqref{imaginary_V_saddle}, the
potential function $\Phi_{\mathcal{M}}(\boldsymbol{x};u)$
under  saddle point conditions~\eqref{hyperbolic_consistency} becomes
a sum of the Rogers
dilogarithm functions.
We recall here the Bloch invariant 
studied in 
Refs.~\citen{NeumYang99a,NeumYang95b}.
The Bloch invariant $\beta(\mathcal{M})$ is defined for
finite volume
hyperbolic 3-manifold $\mathcal{M}$ as
\begin{equation}
  \beta(\mathcal{M}) = \sum_{i=1}^M \left[ z_i \right]
\end{equation}
where $\left[ z \right]$ satisfies  the Bloch group
\begin{equation}
  \left[ z \right] -  \left[w \right]
  +
  \left[\frac{w}{z} \right]
  - \left[ \frac{1-z^{-1}}{1- w^{-1}} \right]
  + \left[ \frac{1-z}{1-w} \right]
  =
  0
\end{equation}
The Bloch regulator map $\rho$ gives~\cite{NeumYang99a}
\begin{equation}
  \rho\left( \beta(\mathcal{M}) \right)
  =
  \Vol(\mathcal{M})
  + \I \, \CS(\mathcal{M})
\end{equation}
where $\CS$ denotes the Chern--Simons invariant
(see Ref.~\citen{RMeyer86b} for definition of the Chern--Simons invariant for a
case of cusped manifolds).
As identities~\eqref{V_partial}--~\eqref{imaginary_V_saddle} show that
the $S$-operator reduces to the Rogers dilogarithm function
(or the Bloch--Wigner function) in the saddle
point, and that they satisfy the pentagon
identities~\eqref{Rogers_pentagon} and~\eqref{Bloch-Wigner_pentagon},
we can interpret our invariant $Z_\gamma(\mathcal{M})$ as a
quantization of the Bloch invariant.


Generally we have many saddle points as algebraic solutions of a set of
equations~\eqref{hyperbolic_consistency}.
Among them, a solution which has the  largest absolute value
dominates an asymptotics of the quantum invariant $Z_\gamma(\mathcal{M})$.
Combining this with a fact that
our quantum invariant $Z_\gamma(\mathcal{M})$ may be regarded as a
quantization of the Bloch invariant,
we should have
\begin{equation}
  \lim_{\gamma \to 0}
  2 \, \gamma\,
  \log \left(
    Z_\gamma(\mathcal{M})
  \right)
  =
  \Vol(\mathcal{M})
  + \I \,
  \CS(\mathcal{M})
\end{equation}
as a variant of the volume conjecture~\cite{Hikam00d}.
Although, there still remains an ambiguity of branch in complex plane
in an actual computation.


The Neumann--Zagier
potential function $\Phi_\mathcal{M}(\boldsymbol{x};u)$ has much 
information on geometry of manifold.
One of the properties
is  a relationship with the A-polynomial  defined in
Ref.~\citen{CCGLS94a}.
When the manifold $\mathcal{M}$ is a complement of knot
$S^3 \setminus \mathcal{K}$,
the A-polynomial 
$A_\mathcal{K}(\ell, m)$ of $\mathcal{K}$
as an algebraic equation of $\ell$ and $m$
can be given by using
the Gr\"obner
base or resultant theory to eliminate $x_i$ from a set of
equations,~\eqref{hyperbolic_consistency}
and~\eqref{differential_longitude}.
So the pair $(\ell,m)=(\E^v, \E^u)$ defined
from~\eqref{v_differential_limit}
is a zero locus of the A-polynomial $A_\mathcal{K}(\ell,m)$.
This result should be comparable with a
conjecture~\eqref{Gukov_conjecture}, and the invariant
$Z_\gamma(\mathcal{M}_u)$ is a \emph{non-compact} generalization of the
Jones--Witten invariant.


The A-polynomial has following
properties~\cite{CCGLS94a,CoopLong98a};
\begin{itemize}

\item Polynomial $A_\mathcal{K}(\ell,m)$ is an integer polynomial, and
  it  contains only even powers of $m$.


\item Up to powers of $\ell$ and $m$, we have
  \begin{equation}
    A_\mathcal{K}(\ell, m) =
    A_\mathcal{K}(1/\ell, 1/m)
  \end{equation}

\item If $\mathcal{K}$ and $\mathcal{K}^\prime$ are mirror images,
  then
  \begin{equation}
    A_\mathcal{K}(\ell, m)=
    A_{\mathcal{K}^\prime}(1/\ell, m) 
  \end{equation}

\item With additional property that every closed incompressible
  surface embedded in $S^3 \setminus \mathcal{K}$ is parallel to the
  boundary torus, we have
  \begin{equation}
    A_\mathcal{K}(\ell, \pm 1 )
    =
    n \, \left( \ell+1 \right)^{\alpha_+}
    \,
    \left( \ell - 1 \right)^{\alpha_-} \,
    \ell^\beta
  \end{equation}
  with non-zero integer $n$.


  \item Slopes of edges of the Newton polygon of
    $A_\mathcal{K}(\ell,m)$ are boundary slopes of $\mathcal{K}$.


  \item Coefficients of terms in the corners of the Newton polygons of
    $A_\mathcal{K}(\ell,m)$ are $\pm 1$.

\end{itemize}




Another property of
the Neumann--Zagier potential function $\Phi_{\mathcal{M}}(u)$ associated to
cusped manifold $\mathcal{M}$ is
the volume of the Dehn surgered
manifold.
The $(p,q)$-hyperbolic Dehn surgery of $\mathcal{M}$,
where $(p,q)$ is a pair of coprime integers, is performed by
gluing back a
solid torus with cusp of $\mathcal{M}$, where the surgery data
satisfy~\cite{WPThurs80Lecture}
\begin{equation}
  p \, u+ q \, v =  \pi \, \I
\end{equation}
Then for the core $c$ of solid torus, we have
\begin{equation}
  \length(c) + \I \, \torsion(c)
  =
  - 2\, \left(
    r \, u + s\, v
  \right)
  \mod 2 \, \pi \, \I
\end{equation}
where
$
\begin{pmatrix}
  p & r \\
  q & s
\end{pmatrix}
\in SL(2,\mathbb{Z})$.
We have
\begin{equation}
  \Im \left( u \, \bar{v} \right)
  =
  -\frac{ \pi}{2} \, \length(c)
\end{equation}
According to Refs.~\citen{TYoshi85a,NeumZagi85a}, 
we have for
the hyperbolic $(p,q)$-Dehn surgered manifold $\mathcal{M}_{(p,q)}$
as
\begin{multline}
  \left( \Vol\left(\mathcal{M}_{(p,q)}\right)
    + \I \, \CS \left(\mathcal{M}_{(p,q)} \right) \right)
  -
  \left( \Vol(\mathcal{M}) + \I \, \CS(\mathcal{M}) \right)
  \\
  =
  - \frac{\I}{4} \, \left(
    \Phi_{\mathcal{M}}(u) - 4 \, u \, v
  \right) -
  \frac{\pi}{2} \,
  \left(
    \length(c)
    + \I \, 
    \torsion(c)
  \right)
\end{multline}
which follows from 
\begin{equation}
  Z_\gamma \left( \mathcal{M}_{(p,q)} \right)
  \sim
  \int \mathrm{d} u \,
  \E^{
    \frac{1}{2 \I \gamma}
    \left(
      \frac{p}{q} u^2 +
      \frac{2 ( \pi + \gamma)  \I}{q} u
    \right)
  } \,
  Z_\gamma(\mathcal{M}_u)
\end{equation}
