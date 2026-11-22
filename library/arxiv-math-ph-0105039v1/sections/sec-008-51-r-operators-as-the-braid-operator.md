---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-008-51-r-operators-as-the-braid-operator
section_title: "$R$-Operators as the Braid Operator"
section_number: 5.1
pages: 14-18
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.994
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We now give the 3-dimensional picture of the
$R$-operators~\eqref{check_R}, and study  the relationship between the
hyperbolic geometry and our invariant.
The $R$-operator consists from four  $S$ operators, and its
matrix element
$\langle \vec{p} \ | \ \Check{R}_{12,34} \ | \  \vec{p^\prime} \rangle$
is explicitly  given by
\begin{multline}
  \label{R_element_int}
  \langle p_1, p_2, p_3, p_4 \  | \
  \Check{R}_{12,34}  \ | \
  p_1^\prime , p_2^\prime, p_3^\prime, p_4^\prime \rangle
  \\
  =
  \iiiint \mathrm{d} x \ \mathrm{d} y \ \mathrm{d} z \
  \mathrm{d} w \
  \langle p_3, w \ | \  S^{-1}  \ | \  x, p_2 \rangle \,
  \langle y, p_4^\prime \ | \  S \  | \  p_4 , w \rangle \,
  \langle p_2^\prime,  z \ | \  S^{-1} \  | \  y, p_3^\prime \rangle \,
  \langle x, p_1 \  | \  S \  | \  p_1^\prime , z \rangle   .
\end{multline}
This integration can be performed explicitly  as eq.~\eqref{integral_H}, but we
work with this form to see a gluing condition clearly.

As we regard the  $S$-operators as the oriented (ideal) tetrahedron
(Fig.~\ref{fig:S_operator}),
the $\Check{R}$-operator is depicted as the oriented octahedron  in
Fig.~\ref{fig:R_matrix} by gluing faces of tetrahedra  to each other.
{}From the symmetry of the $R$-matrix~\eqref{R_and_R_inv}, the
operator $\Check{R}^{-1}$ is  written as the
octahedron  in Fig.~\ref{fig:R_inverse}.
Assignment of the octahedron to the braiding operator
first appeared  in Ref.~\citen{DThurs99a}, and
it was   later
used to give the  decomposition of the knot complement
directly from  Kashaev's invariant~\cite{YYokot00b}.
Our result in  Fig.~\ref{fig:R_matrix} is essentially same with one in
Ref.~\citen{DThurs99a}, and  this
agreement  suggests  that
our knot invariant $\tau_1(K)$  is indeed  defined as
a non-compact analogue of
Kashaev's invariant (the colored Jones polynomial at a  fixed value),
only replacing the
\emph{finite}-dimensional representation of the quantum dilogarithm
function with the \emph{infinite}-dimensional one.
Consequently  the decomposition of the knot complement which will be presented
below
is same with one
given in Ref.~\citen{YYokot00b}
(see also Ref.~\citen{HMuraka00c}).















\begin{figure}[htbp]
  \begin{center}
    \begin{psfrags}
      \psfrag{A}{$p_3^\prime$}
      \psfrag{B}{\rotatebox{50}{$p_4^\prime$}}
      \psfrag{C}{\rotatebox{-50}{$p_1$}}
      \psfrag{D}{\textcolor{red}{\reflectbox{$p_2$}}}
      \psfrag{E}{\textcolor{red}{\rotatebox{40}{\reflectbox{$p_1^\prime$}}}}
      \psfrag{F}{$p_2^\prime$}
      \psfrag{G}{\textcolor{red}{\reflectbox{$p_3$}}}
      \psfrag{H}{\textcolor{red}{\rotatebox{-45}{\reflectbox{$p_4$}}}}
      \psfig{file=octa.eps,scale=0.7}
    \end{psfrags}
    \caption{The braid operator ($\Check{R}$-matrix)
      $\langle \vec{p}  \ | \  \Check{R}  \ | \ \vec{p^\prime} \rangle$


      is represented by the octahedron.}
    \label{fig:R_matrix}
  \end{center}
\end{figure}

\begin{figure}[htbp]
  \begin{center}
    \begin{psfrags}
      \psfrag{A}{$p_4$}
      \psfrag{B}{\rotatebox{50}{$p_3$}}
      \psfrag{C}{\rotatebox{-50}{$p_2^\prime$}}
      \psfrag{D}{\textcolor{red}{\reflectbox{$p_1^\prime$}}}
      \psfrag{E}{\textcolor{red}{\rotatebox{40}{\reflectbox{$p_3^\prime$}}}}
      \psfrag{F}{$p_4^\prime$}
      \psfrag{G}{\textcolor{red}{\reflectbox{$p_1$}}}
      \psfrag{H}{\textcolor{red}{\rotatebox{-45}{\reflectbox{$p_2$}}}}
      \psfig{file=octa.eps,scale=0.7}
    \end{psfrags}
    \caption{The inverse of the  $\Check{R}$-matrix,
      $\langle \vec{p} \  | \  \Check{R}^{-1} \ | \  \vec{p^\prime} \rangle$,


      is represented by the same  octahedron with the $\Check{R}$
      operator, though the content is different.}
    \label{fig:R_inverse}
  \end{center}
\end{figure}

The braiding property can be seen from
the realization of the $R$-operators as in
Figs.~\ref{fig:R_matrix}--\ref{fig:R_inverse}.
When we suppose that the gray bold lines in those figures
denote the link $L$ and we
look down each octahedron from the top,
we find that the braiding is indeed  realized as follows;
\begin{subequations}
  \label{realize_R}
  \begin{align}
    \langle \vec{p} \ | \ \Check{R} \ | \ \vec{p^\prime} \rangle
    & = \quad
    \xygraph{!{0;/r4pc/:/u4pc/::}="A"
      "A"  [d(0.5)]!{\xunderv}
         !{(-0.09,.4)*+{p_1}}
         !{(0.09,.6)*+{p_2}}
         !{(0.91,.6)*+{p_3}}
         !{(1.1,.38)*+{p_4}}
         !{(-0.09,-0.4)*+{p_1^\prime}}
         !{(0.09,-0.6)*+{p_2^\prime}}
         !{(0.91,-0.6)*+{p_3^\prime}}
         !{(1.1,-0.38)*+{p_4^\prime}}
         }

\\[2mm]

    \langle \vec{p} \ | \  \Check{R}^{-1}  \ | \ \vec{p^\prime} \rangle
    & = \quad
    \xygraph{!{0;/r4pc/:/u4pc/::}="A"
      "A"  [d(0.5)]!{\xoverv}
         !{(-0.09,.4)*+{p_1}}
         !{(0.09,.6)*+{p_2}}
         !{(0.91,.6)*+{p_3}}
         !{(1.1,.38)*+{p_4}}
         !{(-0.09,-0.4)*+{p_1^\prime}}
         !{(0.09,-0.6)*+{p_2^\prime}}
         !{(0.91,-0.6)*+{p_3^\prime}}
         !{(1.1,-0.38)*+{p_4^\prime}}
         }
     \end{align}
   \end{subequations}
We should stress  that  every 0-simplex  of the octahedron is on the
link $L$, and that the octahedron is in the complement of the link $L$.



We shall check the hyperbolicity consistency  condition in constructing
the  $R$-operator from
the ideal tetrahedra in a case of $\gamma \to 0$.
Substituting the asymptotic form~\eqref{S_asymptotics}
into
eq.~\eqref{R_element_int},
we get
\begin{multline}
  \langle \vec{p} \ | \  \Check{R}_{12,34} \  | \ \vec{p^\prime} \rangle
  \sim
  \delta(p_1 - p_2 + p_3 - p_1^\prime) \,
  \delta(p_2^\prime -p_3^\prime + p_4^\prime - p_4) \\
  \times
  \iint \mathrm{d} z \ \mathrm{d} w \
  \exp
  \frac{1}{ 2 \, \mathrm{i} \, \gamma}
  \biggl(
  - \Li(\mathrm{e}^{w-p_2}) + \Li(\mathrm{e}^{w-p_4^\prime})
  - \Li(\mathrm{e}^{z-p_3^\prime})
  + \Li(\mathrm{e}^{z-p_1})
  \\
  + (-p_1 + p_1^\prime) \, (-w+p_2 + z - p_1)
  + (p_4 - p_4^\prime) \, ( w - p_4^\prime - z + p_3^\prime)
  \biggr) .
\end{multline}
Here we have used  trivial  constraints;
\begin{align}
  \label{constraint_x_y}
  x & = -p_1 + p_1^\prime  ,
  &
  y &=  p_4 - p_4^\prime .
\end{align}
Above  integral is  evaluated by the saddle point,
in which
we have constraints
  \begin{align*}
    & \frac{1- \mathrm{e}^{w-p_2}}{1-\mathrm{e}^{w-p_4^\prime}}
    \,
    \mathrm{e}^{p_1 - p_1^\prime + p_4 - p_4^\prime}
    = 1 ,
    &

    &
    \frac{1- \mathrm{e}^{z-p_3^\prime}}{1-\mathrm{e}^{z-p_1}}
    \,
    \mathrm{e}^{-p_1 + p_1^\prime - p_4 + p_4^\prime}
    = 1  .
  \end{align*}
This set of equations solves
\begin{align}
  \label{obtain_w_z}
  \mathrm{e}^w
  &=
  \frac{1- \mathrm{e}^{p_1 - p_1^\prime + p_4 - p_4^\prime}}
  {
    \mathrm{e}^{-p_4^\prime}
    -
    \mathrm{e}^{p_1 - p_1^\prime + p_4 - p_4^\prime - p_2}
    } ,
  &

  \mathrm{e}^z
  &=
  \frac{1- \mathrm{e}^{p_1 - p_1^\prime + p_4 - p_4^\prime}}
  {
    \mathrm{e}^{-p_3^\prime}
    -
    \mathrm{e}^{p_1 - p_1^\prime + p_4 - p_4^\prime - p_1}
    } ,
\end{align}
and we easily find a constraint,
\begin{equation}
  \label{constraint_w_z}
  \frac{1- \mathrm{e}^{w-p_2}}{1-\mathrm{e}^{w-p_4^\prime}} \cdot
  \frac{1- \mathrm{e}^{z-p_3^\prime}}{1-\mathrm{e}^{z-p_1}}
  = 1 ,
\end{equation}
which
coincides with  the hyperbolicity condition around vertical axis
(crossing point in eq~\eqref{realize_R}).

Due to the symmetry of the $R$-operator~\eqref{symmetry_R},
we can conclude that
for each crossing in a link  $L$
we can attach the oriented
octahedron, which has a following projection;
















\begin{equation}
  \label{attach_octa}
  \xy/r1.2pc/:.
  {
    { (0,0)*+{\text{\LARGE$\bigotimes$}} },
    { (0,0) \ar@{-}|@{>} (4,-4)},
    { (0,0) \ar@{-}|@{>} (-4,4)},
    { (1.5,1.5) \ar@{-}|@{<} (4,4)},
    { (-1.5,-1.5) \ar@{-}|@{<} (-4,-4)},
    { (4,4) \ar@{--}|@{>} (4,-4)},
    { (4,4) \ar@{--}|@{>} (-4,4)},
    { (-4,-4) \ar@{--}|@{>} (4,-4)},
    { (-4,-4) \ar@{--}|@{>} (-4,4)},
    { (4,4) \ar@{-}|@{} (6,6)},
    { (4,-4) \ar@{-}|@{} (6,-6)},
    { (-4,4) \ar@{-}|@{} (-6,6)},
    { (-4,-4) \ar@{-}|@{} (-6,-6)},

    { (-6,5)*+{p_1} },
    { (-5,6)*+{p_2} },
    { (5,6)*+{p_3} },
    { (6,5)*+{p_4} },
    { (-6,-5)*+{p_1^\prime} },
    { (-5,-6)*+{p_2^\prime} },
    { (5,-6)*+{p_3^\prime} },
    { (6,-5)*+{p_4^\prime} },

    { (0,5)*+{\langle p_3, w \ | \  S^{-1}  \ | \  x, p_2 \rangle} },
    { (0,-5)*+{\langle p_2^\prime, z \ | \  S^{-1} \  | \  y, p_3^\prime \rangle} },
    { (-5,0)*+{
        \text{
          \rotatebox{-90}{
            $\langle x, p_1 \ | \  S  \ | \  p_1^\prime, z \rangle$}
        }}
      },
    { (5,0)*+{
        \text{
          \rotatebox{90}{
            $\langle y, p_4^\prime \ | \  S \  | \  p_4, w \rangle$}
        }}
      },









    { (2,2.5)*+{
        \text{
          \rotatebox{45}{
            \textcolor{red}{$w$}
            } }} },
    { (-2,-2.5)*+{
        \text{
          \rotatebox{45}{
            \textcolor{red}{$z$}
            } }} },
    { (-2,1.5)*+{
        \text{
          \rotatebox{-45}{

            \textcolor{red}{$x$}
            } }} },
    { (2,-1.5)*+{
        \text{
          \rotatebox{-45}{
            \textcolor{red}{$y$}

            } }} },
        { (0,1.1)*+{
        \text{
          $a_4$
              } }},
        { (1.1,0)*+{
        \text{
          \rotatebox{90}{
            $a_3$
            } }} },
    { (-1.1,0)*+{
        \text{
          \rotatebox{-90}{
            $a_1$
          }} }},
    { (0,-1.1)*+{
        \text{
          $a_2$
          }} },
    }
  \endxy
\end{equation}
Here $x$ and $y$ are auxiliary momenta
given by eq.~\eqref{constraint_x_y}, and $w$ and $z$
are fixed by eq.~\eqref{obtain_w_z}.
We further have
\begin{align}




  p_3
  & = - p_1 + p_2 + p_1^\prime ,
  &
  p_2^\prime
  & = p_4 + p_3^\prime - p_4^\prime  .
\end{align}
and the dihedral angles $a_i$ satisfying
$a_1 \, a_2 \, a_3 \, a_4 = 1$ are given by
\begin{align*}
  a_1
  &=
  (1- \mathrm{e}^{z-p_1})^{-1}
  =
  \frac{
    \mathrm{e}^{p_1 - p_1^\prime + p_4 - p_4^\prime}
    - \mathrm{e}^{p_1 - p_3^\prime}}
  {1 - \mathrm{e}^{p_1 - p_3^\prime}} ,
  \\

  a_2
  &=
  1- \mathrm{e}^{z-p_3^\prime}
  =
  \frac{1 - \mathrm{e}^{p_1 - p_3^\prime}}
  {
    1
    - \mathrm{e}^{-p_1 + p_1^\prime - p_4 + p_4^\prime}
    \mathrm{e}^{p_1 - p_3^\prime}
    } ,
  \\

  a_3
  &=
  (1 - \mathrm{e}^{w-p_4^\prime})^{-1}
  =
  \frac{
    1 
    - \mathrm{e}^{-p_1 + p_1^\prime - p_4 + p_4^\prime}
    \mathrm{e}^{p_2 - p_4^\prime}
    } 
  {1 - \mathrm{e}^{p_2 - p_4^\prime}} ,
  \\

  a_4
  &=
  1 - \mathrm{e}^{w-p_2}
  =
  \frac{1 - \mathrm{e}^{p_2 - p_4^\prime}}
  {
    \mathrm{e}^{p_1 - p_1^\prime + p_4 - p_4^\prime}
    -
    \mathrm{e}^{p_2 - p_4^\prime}
    } .
\end{align*}








































































To close this section,
we give an explicit form of an asymptotic form of the
$\Check{R}$-operators.
As
the integral~\eqref{integral_H} has an asymptotic
form,
\begin{multline}
  H(a,b,c,d) \\

  \sim
  \exp \frac{1}{2 \, \mathrm{i} \, \gamma}
  \biggl(
  \Li(\mathrm{e}^{a-b}) + \Li(\mathrm{e}^{d-a})
  - \Li(\mathrm{e}^{c-b}) - \Li(\mathrm{e}^{d-c})

  + c\, ( -a + b - c + d)
  \biggr) ,
\end{multline}
the $\Check{R}^{\pm 1}$ operators  in a limit
$\gamma \to 0$
are
respectively given by
\begin{subequations}
\label{R_asymptotics}
\begin{multline}

  \langle \vec{p} \ | \
  \Check{R}_{1 2, 3 4} \
  | \ \vec{p^\prime} \rangle


  \sim
  \delta(p_1 + p_3 - p_2 - p_1^\prime ) \cdot
  \delta(p_2^\prime - p_3^\prime + p_4^\prime - p_4)
  \\
  \times
  \exp
  \frac{1}{2 \, \mathrm{i} \, \gamma}
  \biggl(
  \Li( \mathrm{e}^{p_4  - p_3} )
  +  \Li( \mathrm{e}^{p_3^\prime - p_1} )
  -  \Li( \mathrm{e}^{p_4^\prime - p_2} )
  -  \Li( \mathrm{e}^{p_2^\prime - p_1^\prime} )
  \\
  + ( p_1^\prime - p_1) \,
  (-p_4 + p_3 - p_1^\prime + p_2^\prime)
  \biggr) ,





















\end{multline}
\begin{multline}

  \langle \vec{p} \ |  \
  ( \Check{R}_{1 2, 3 4} )^{-1} \ | \
  \vec{p^\prime} \rangle


  \sim
  \delta(p_4^\prime  -p_2+p_3- p_4) \,
  \delta(p_1 - p_1^\prime - p_3^\prime  + p_2^\prime) 
  \\
  \times
  \exp \frac{1}{2 \, \mathrm{i} \, \gamma}
  \biggl(
    \Li(\mathrm{e}^{p_2 - p_1}) 
    + \Li(\mathrm{e}^{p_4 - p_2^\prime})
    - \Li(\mathrm{e}^{p_3 - p_1^\prime})
    - \Li(\mathrm{e}^{p_4^\prime - p_3^\prime})
    \\
    + (p_1 - p_1^\prime) \, (p_1 - p_2 - p_3^\prime + p_4^\prime)
  \biggr) .


















\end{multline}
\end{subequations}


























































































































































































































































































































In constructing the knot invariant $\tau_1(K)$, we need another
operator $\mu$~\eqref{mu_operator}.
The  matrix element of the  $\mu$-operator
can be computed simply,
and  in the classical  limit $\gamma \to 0$ reduces to
\begin{equation}
  \langle p_1 , p_2 \ | \ \mu \ | \ p_1^\prime , p_2^\prime \rangle
  \sim
  \delta(p_1 - p_1^\prime) \, \delta(p_2 - p_2^\prime) \cdot
  \exp \frac{\pi}{\gamma} \bigl( p_1 - p_2 \bigr) .
\end{equation}
Thus
the saddle point condition coming  from the $\mu$-operator is always
$2 \, \pi \, \mathrm{i}$, and
we can ignore
a  contribution  from the $\mu$-operator
to the saddle point condition.





In the rest of this   section, we 
study how to glue these octahedra in the invariant $\tau_1(K)$.
We   show that for every gluing
there exists  a  correspondence between the
saddle point equations and the hyperbolicity consistency conditions
around edge.
