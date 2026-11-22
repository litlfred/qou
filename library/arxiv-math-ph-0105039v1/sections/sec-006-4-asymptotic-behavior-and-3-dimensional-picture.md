---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-006-4-asymptotic-behavior-and-3-dimensional-picture
section_title: "Asymptotic Behavior and 3-dimensional Picture"
section_number: 4
pages: 11-14
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 1.0
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
\label{sec:asymptotic}







































We  shall reveal the 3-dimensional picture  of the knot invariant
$\tau_1(K)$
by studying  an asymptotic behavior in  a limit $\gamma \to 0$.
Using eq.~\eqref{Phi_gamma_0},
we find
that the $S$-operator~\eqref{S_element_2} 
is
represented by
\begin{subequations}
  \label{S_asymptotics}
  \begin{align}
    \langle p_1 , p_2 \ | \ S_{1,2}  \ | \ p_1^\prime , p_2^\prime \rangle
    & \sim
    \delta(p_1 + p_2 - p_1^\prime) \cdot
    \exp
    \left(
      - \frac{1}{2 \, \mathrm{i} \, \gamma}
      \, V(p_2^\prime - p_2 , p_1)
    \right) ,


















  \\[2mm]


  \langle p_1 , p_2 \  | \ S_{1,2}^{-1} \ | \ p_1^\prime , p_2^\prime \rangle
  &
  \sim
  \delta(p_1 - p_1^\prime - p_2^\prime) \cdot
  \exp
  \left(
    \frac{1}{ 2 \, \mathrm{i} \, \gamma} \,
    V(p_2 - p_2^\prime , p_1^\prime)
  \right) ,


















\end{align}
\end{subequations}
where we have defined  the function $V(x,y)$ by
\begin{equation}
  V(x,y)
  =
  \frac{\pi^2}{6} - \Li(\mathrm{e}^x) - x \, y .
\end{equation}
We see that the function $V(x,y)$ is associated with each
$S$-operator, and that
the function $V(x,y)$ has an interesting property for our purpose to
relate with the 3-dimensional hyperbolic geometry;
when we suppose an  analytic continuation  $x,y \in \mathbb{C}$,
we have
\begin{subequations}
  \label{property_V}
  \begin{align}
    V(x,y)
    & =
    L(1- \mathrm{e}^x)
    +
    \frac{1}{2}
    \left(
      x \, \frac{\partial V(x,y)}{\partial x}
      +
      y \, \frac{\partial V(x,y)}{\partial y}
    \right) ,
    \\[2mm]

    \Im \, V(x,y)
    & =
    D(1-\mathrm{e}^x)
    +
    \log | \mathrm{e}^x | \cdot
    \Im \, \biggl( \frac{\partial}{\partial x} V(x,y) \biggr) 
    +
    \log | \mathrm{e}^y | \cdot
    \Im \, \biggl( \frac{\partial}{\partial y} V(x,y) \biggr) .
  \end{align}
\end{subequations}
Here
$L(z)$ is  the Rogers dilogarithm~\eqref{Rogers}, and
the function $D(z)$
is the Bloch--Wigner
function~\eqref{Bloch_Wigner} which gives the hyperbolic volume of
the ideal tetrahedron.
This indicates that  the classical limit of
the $S$-operator
describes

the
ideal tetrahedron at the critical point.
By these observations we can associate the ideal tetrahedron for the
$S$-operators
$\langle p_1, p_2 \ | \ S^{\pm 1} \  | \ p_1^\prime , p_2^\prime \rangle$
as Fig.~\ref{fig:S_operator}.
Due to sign   of the function $V(x,y)$ in eqs.~\eqref{S_asymptotics}
these tetrahedra are mirror images each other.
Therein the modulus of the ideal tetrahedron is
given by $\mathrm{e}^{p_2^\prime - p_2}$ and each face has a momentum;












we regard $p_i$ and $p_i^\prime$ as the outgoing and incoming states
respectively,
\emph{i.e.},
each triangular face
is assigned a transverse orientation.



See that the dihedral angles of opposite edges are equal, and we have
\begin{align*}
  & z_1 \, z_2 \, z_3 = -1 ,
  &
  & 1 - z_1 + z_1 \, z_2 = 0 .
\end{align*}

\begin{figure}[htbp]
  \begin{center}
    \parbox{2cm}
    {$\langle p_1, p_2 \  | \ S \  | \ p_1^\prime , p_2^\prime \rangle ~:~$}

    \begin{psfrags}
      \psfrag{A}{\textcolor{red}{\reflectbox{$p_1$}}}
      \psfrag{B}{\rotatebox{40}{$p_2$}}
      \psfrag{C}{\rotatebox{-10}{$p_1^\prime$}}
      \psfrag{D}{\textcolor{red}{\reflectbox{$p_2^\prime$}}}

      \psfrag{a}{$z_1$}
      \psfrag{b}{$z_2$}
      \psfrag{c}{$z_3$}
      \psfig{file=tetra.eps,scale=0.4}
    \end{psfrags}

    \hspace{20mm}

    \parbox{2cm}
    {$\langle p_1, p_2 \  | \ S^{-1} \  | \  p_1^\prime , p_2^\prime \rangle ~:~$}

    \begin{psfrags}
      \psfrag{A}{\textcolor{red}{\reflectbox{$p_1$}}}
      \psfrag{B}{\textcolor{red}{\reflectbox{$p_2$}}}
      \psfrag{C}{\rotatebox{-10}{$p_1^\prime$}}
      \psfrag{D}{\rotatebox{40}{$p_2^\prime$}}

      \psfrag{a}{$z_1$}
      \psfrag{b}{$z_2$}
      \psfrag{c}{$z_3$}

      \psfig{file=tetraDual.eps,scale=0.4}
    \end{psfrags}

    \caption{Both operators
      $\langle p_1, p_2 \  | \ S \  | \  p_1^\prime , p_2^\prime \rangle$
      and
      $\langle p_1, p_2 \  | \  S^{-1} \  | \  p_1^\prime , p_2^\prime \rangle$
      are represented by the oriented tetrahedra,
      which become the ideal tetrahedra in the classical limit
      $\gamma  \to 0$.
      In this limit they  have  the modulus
      $\mathrm{e}^{p_2^\prime - p_2}$, and
      each edge is associated  by
      $z_1=\mathrm{e}^{p_2^\prime -p_2}$,
      $z_2=1-z_1^{~-1}$, and
      $z_3=(1-z_1)^{-1}$.
      These modulus denote the dihedral angle.
      }
    \label{fig:S_operator}
  \end{center}
\end{figure}

Our  identification
of the modulus and dihedral angles
can be justified  from the 3-dimensional picture of the
pentagon identity as follows.


The pentagon identity~\eqref{pentagon_S}  is depicted as
the 2-3 Pachner move
(Fig.~\ref{fig:pentagon})
once we represent the $S$-operators by the oriented tetrahedra as in
Fig.~\ref{fig:S_operator}.

The matrix element of the right hand side of eq.~\eqref{pentagon_S}
is written as
\begin{equation}
  \label{pentagon_rhs}
  \iiint \mathrm{d} y \ \mathrm{d} z \
  \mathrm{d} w \
  \langle p_1, p_2 \ | \  S \  | \ y,z \rangle \,
  \langle y, p_3 \ | \  S \  | \  p_1^\prime ,w \rangle \,
  \langle z, w \ | \ S \  | \  p_2^\prime , p_3^\prime \rangle   .
\end{equation}
After  substituting  the asymptotic form~\eqref{S_asymptotics} into this
integral,
we get immediately
\begin{align*}
  y &= p_1 + p_2 ,
  &
  w &= p_2^\prime -z ,
\end{align*}
and the integral reduces to
\begin{multline*}
  \delta(p_1 + p_2 + p_3 - p_1^\prime) \cdot
  \int \mathrm{d} z \
  \exp \frac{1}{2 \, \mathrm{i} \, \gamma}
  \Bigl(
  -\frac{\pi^2}{2}
  + \Li(\mathrm{e}^{z-p_2})
  + \Li(\mathrm{e}^{p_2^\prime - p_3 - z})
  + \Li(\mathrm{e}^{p_3^\prime - p_2^\prime + z})
  \\
  + z \, (-p_2 + p_3^\prime - p_2^\prime + z)
  - p_1 \, p_2 + ( p_2^\prime - p_3) \, ( p_1 + p_2)
  \Bigr).
\end{multline*}
As we study a limit $\gamma\to 0$, the integral is evaluated by the
saddle point method, whose
saddle point condition  is given by
\begin{equation}
  \label{pentagon_condition}
  ( 1 - \mathrm{e}^{w-p_3} )^{-1} \cdot
  ( 1 - \mathrm{e}^{p_2-z}) \cdot
  ( 1 - \mathrm{e}^{w-p_3^\prime}) = 1 .
\end{equation}
This condition  exactly coincides with the hyperbolicity equation
around an axis which penetrates 2 adjacent 
tetrahedra in the right hand side of
Fig.~\ref{fig:pentagon},
once we regard the $S$-operator as the ideal tetrahedron
whose dihedral angles are written in Fig.~\ref{fig:S_operator}.
See that by substituting  a  solution of
eq.~\eqref{pentagon_condition}
into eq.~\eqref{pentagon_rhs} we  recover the left hand side of
eq.~\eqref{pentagon_S} after  using  Schaeffer's pentagon
identity~\eqref{pentagon_Euler}.

\begin{figure}[htbp]
  \begin{center}
    \psfig{file=pentagon.eps,scale=0.5}
    \caption{Pachner move $2 \leftrightarrow 3$.}
    \label{fig:pentagon}
  \end{center}
\end{figure}

This coincidence between the   saddle point equation and the
hyperbolicity consistency condition can be seen for other pentagon identities,
such as
$S_{2,3} \, S_{1,2} \, S_{2,3}^{~-1} = S_{1,2} \, S_{1,3}$,
$S_{1,2}^{~-1} \, S_{2,3} = S_{1,3} \, S_{2,3} \, S_{1,2}^{~-1}$,
and the trivial identities
$S_{1,2} \, S_{1,2}^{~-1} = 1$.

This fact supports a validity
that at the critical point the classical limit of the  $S$-operator
represents the (oriented) ideal tetrahedron
whose dihedral angles are fixed as in Fig.~\ref{fig:S_operator}.
