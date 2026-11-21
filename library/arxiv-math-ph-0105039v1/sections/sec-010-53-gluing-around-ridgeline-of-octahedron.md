---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-010-53-gluing-around-ridgeline-of-octahedron
section_title: "Gluing Around Ridgeline of Octahedron"
section_number: 5.3
pages: 20-24
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 1.0
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We shall check  a correspondence between the hyperbolic condition and the
saddle point equation for ridgelines of octahedron.
We consider a case such as Fig.~\ref{fig:Ridge_condition}.
Therein
$n-1$ over-crossings $\text{\rotatebox{45}{$\xybox{0;/r1.4pc/:, {\xoverv}}$}}$
are  sandwiched by two under-crossings
$\text{\rotatebox{45}{$\xybox{0;/r1.4pc/:, {\xunderv}}$}}$.

\begin{figure}[htbp]
  \begin{equation*}
    \xy/r1pc/:.
    {
      {  (2,0) \ar@{-}|@{} (9.5,0) },
      {  (10.5,0) \ar@{-}|@{} (14.5,0) },
      {  (15.5,0) \ar@{-}|@{} (18,0) },
      {  (18,0) \ar@{--}|@{} (22,0) },
      {  (22,0) \ar@{-}|@{} (24.5,0) },
      {  (25.5,0) \ar@{-}|@{} (33,0) },

      {  (5,5) \ar@{-}|@{} (5,0.5) },
      {  (5,-0.5) \ar@{-}|@{} (5,-5) },
      {  (30,5) \ar@{-}|@{} (30,0.5) },
      {  (30,-0.5) \ar@{-}|@{} (30,-5) },

      {  (10,5) \ar@{-}|@{} (10,-5) },
      {  (15,5) \ar@{-}|@{} (15,-5) },
      {  (25,5) \ar@{-}|@{} (25,-5) },

      { (7.5,0.7)*+{p_{1,1}} },
      { (7.5,-0.7)*+{p_{1,2}} },
      { (6,4.5)*+{p_{1,3}} },
      { (6,-4.5)*+{p_{1,4}} },
      { (9,4.5)*+{p_{1,5}} },
      { (9,-4.5)*+{p_{1,6}} },

      { (12.5,0.7)*+{p_{2,1}} },
      { (12.5,-0.7)*+{p_{2,2}} },
      { (11,4.5)*+{p_{2,3}} },
      { (11,-4.5)*+{p_{2,4}} },
      { (14,4.5)*+{p_{2,5}} },
      { (14,-4.5)*+{p_{2,6}} },

      { (27.5,0.7)*+{p_{n,1}} },
      { (27.5,-0.7)*+{p_{n,2}} },
      { (26,4.5)*+{p_{n,3}} },
      { (26,-4.5)*+{p_{n,4}} },
      { (29,4.5)*+{p_{n,5}} },
      { (29,-4.5)*+{p_{n,6}} },

      { (7, 0) \ar@{--}|@{<} (5,3)  },
      { (7, 0) \ar@{--}|@{<} (5,-3)  },
      { (8, 0) \ar@{--}|@{>} (10,3)  },
      { (8, 0) \ar@{--}|@{>} (10,-3)  },

      { (12, 0) \ar@{--}|@{>} (10,3)  },
      { (12, 0) \ar@{--}|@{>} (10,-3)  },
      { (13, 0) \ar@{--}|@{>} (15,3)  },
      { (13, 0) \ar@{--}|@{>} (15,-3)  },

      { (17, 0) \ar@{--}|@{>} (15,3)  },
      { (17, 0) \ar@{--}|@{>} (15,-3)  },

      { (23, 0) \ar@{--}|@{>} (25,3)  },
      { (23, 0) \ar@{--}|@{>} (25,-3)  },

      { (27, 0) \ar@{--}|@{>} (25,3)  },
      { (27, 0) \ar@{--}|@{>} (25,-3)  },
      { (28, 0) \ar@{--}|@{<} (30,3)  },
      { (28, 0) \ar@{--}|@{<} (30,-3)  },

      { (6.4,0.4)*+{\text{\textcolor{red}{$x_1$} }} },
      { (4.5,2)*+{\text{\textcolor{red}{$x_2$} }} },
      { (4.5,-2)*+{\text{\textcolor{red}{$x_3$} }} },

      { (29.1,0.4)*+{\text{\textcolor{red}{$x_4$} }} },
      { (31,2)*+{\text{\textcolor{red}{$x_5$} }} },
      { (31,-2)*+{\text{\textcolor{red}{$x_6$} }} },

      }
    \endxy
  \end{equation*}
  \caption{We parameterize a segment of link $L$.}
  \label{fig:Ridge_condition}
\end{figure}

A contribution from this segment is given by
\begin{multline}
  \iiint \prod_{i=1}^n \mathrm{d} p_{i,1} \ \mathrm{d} p_{i,2} \cdot
  \mathrm{d} x_1 \   \mathrm{d} x_4 \
  \langle x_1 , p_{1,1} \  | \  S \  | \  p_{1,3} , x_2 \rangle \,
  \langle p_{1,4}, x_3 \ | \  S^{-1} \  | \  x_1, p_{1,2}  \rangle
  \\
  \times
  \prod_{j=1}^{n-1}
  \langle p_{j,5}, p_{j+1,3} , p_{j+1,1}, p_{j+1,2} \  | \
  \Check{R} \ | \
  p_{j,1} , p_{j,2} , p_{j,6} , p_{j+1,4} \rangle \\
  \times
  \langle p_{n,5} , x_5 \  | \  S^{-1} \  | \ x_4 , p_{n,1} \rangle \,
  \langle x_4 , p_{n,2} \ | \ S \  | \  p_{n,6} , x_6 \rangle .
\end{multline}
We substitute eqs.~\eqref{S_asymptotics} and~\eqref{R_asymptotics} into
above equation.
We get
\begin{align*}
  p_{j,1} &= p_{j+1,1} - p_{j+1,3} + p_{j,5},
  &
  p_{j,2} &= p_{j+1,2} - p_{j+1,4} + p_{j,6},
  \\[2mm]

  p_{n,1} & = - x_4 + p_{n,5} ,
  &
  p_{n,2} &= - x_4 + p_{n,6} ,
  \\
  x_1 &= x_4 + \sum_{j=1}^n ( p_{j,3} - p_{j,5} ) ,
\end{align*}
and the integral reduces to that of $x_4$-integration,
whose saddle point equation is given by
\begin{equation*}
  \frac{
    (1 - \mathrm{e}^{x_3 - p_{1,2}} ) \,
    ( 1 - \mathrm{e}^{x_5 - p_{n,1}} )
    }{
    (1 - \mathrm{e}^{x_2 - p_{1,1}} ) \,
    ( 1 - \mathrm{e}^{x_6 - p_{n,2}} )
    }
  \cdot
  \mathrm{e}^{
    + x_2 - x_3 - x_5 + x_6}
  =1 .





\end{equation*}
One sees that this equation coincides with the hyperbolicity equation
around a ridgeline of the octahedron
(bold lines in Fig~\ref{fig:Ridge_octa});
\begin{equation}
  \label{hyperbolic_ridge}
  \frac{1-\mathrm{e}^{p_{1,1} - x_2}}{1-\mathrm{e}^{p_{1,2} - x_3}}
  \cdot
  \prod_{j=1}^{n-1}
  \mathrm{e}^{-p_{j,5} + p_{j,6} + p_{j+1,3} - p_{j+1,4}}
  \cdot
  \frac{
    1-\mathrm{e}^{p_{n,2} - x_6}}{
    1 - \mathrm{e}^{p_{n,1} - x_5}
    } 
  = 1.
\end{equation}


\begin{figure}[htbp]
  \begin{center}
    \parbox{5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{20}{$p_{1,1}$}}
        \psfrag{B}{\rotatebox{0}{$p_{1,2}$}}
        \psfig{file=glue_ryosen.eps,scale=0.4} 
      \end{psfrags}
      }

    \parbox{5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-10}{\rotatebox{10}{$p_{j,2}$}}}
        \psfrag{B}{\textcolor{red}{\reflectbox{\rotatebox{-20}{$p_{j,1}$}}}}
        \psfrag{C}{\rotatebox{20}{$p_{j+1,2}$}}
        \psfrag{D}{\textcolor{red}{\reflectbox{\rotatebox{30}{$p_{j+1,1}$}}}}
        \psfrag{E}{$p_{j,6}$}
        \psfrag{F}{\textcolor{red}{\reflectbox{\rotatebox{-10}{$p_{j,5}$}}}}
        \psfrag{G}{\rotatebox{20}{$p_{j+1,4}$}}
        \psfrag{H}{\textcolor{red}{\reflectbox{\rotatebox{10}{$p_{j+1,3}$}}}}
        \psfig{file=octa_glue.eps,scale=0.35}
      \end{psfrags}
      }

    \parbox{4cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-20}{$p_{n,1}$}}
        \psfrag{B}{\rotatebox{10}{$p_{n,2}$}}
        \psfig{file=glue_ryosen_2.eps,scale=0.4}
      \end{psfrags}
      }

    \caption{
      The 3-dimensional picture of
      Fig.~\ref{fig:Ridge_condition} is given.
      Eq.~\eqref{hyperbolic_ridge} coincides with the hyperbolicity
      condition around  ridgelines (bold line)
      of the octahedra.
      }
    \label{fig:Ridge_octa}
  \end{center}
\end{figure}

In the same manner, we can see a correspondence between the    saddle
point equation and the hyperbolicity condition in a case
that
$n-1$ under-crossings $\text{\rotatebox{45}{$\xybox{0;/r1.4pc/:, {\xunderv}}$}}$
are  sandwiched by two over-crossings
$\text{\rotatebox{45}{$\xybox{0;/r1.4pc/:, {\xoverv}}$}}$.
(Fig.~\ref{fig:Ridge_2}).

\begin{figure}[htbp]
  \begin{equation*}
    \xy/r1pc/:.
    {
      { (-3,0)\ar@{-} (-0.5,0)},
      { (0.5,0)\ar@{-} (12,0)},
      { (12,0)\ar@{--} (17,0)},
      { (17,0)\ar@{-} (24.5,0)},
      { (25.5,0)\ar@{-} (28,0)},
                                
      { (0,5)\ar@{-} (0,-5)},
      { (25,5)\ar@{-} (25,-5)},
                                
      { (5,5)\ar@{-} (5,0.5)},
      { (5,-0.5)\ar@{-} (5,-5)},

      { (10,5)\ar@{-} (10,0.5)},
      { (10,-0.5)\ar@{-} (10,-5)},

      { (20,5)\ar@{-} (20,0.5)},
      { (20,-0.5)\ar@{-} (20,-5)},

      { (2.5,0.7)*+{p_{1,1}} },
      { (2.5,-0.7)*+{p_{1,2}} },
      { (1,4.5)*+{p_{1,3}} },
      { (1,-4.5)*+{p_{1,4}} },
      { (4,4.5)*+{p_{1,5}} },
      { (4,-4.5)*+{p_{1,6}} },

      { (7.5,0.7)*+{p_{2,1}} },
      { (7.5,-0.7)*+{p_{2,2}} },
      { (6,4.5)*+{p_{2,3}} },
      { (6,-4.5)*+{p_{2,4}} },
      { (9,4.5)*+{p_{2,5}} },
      { (9,-4.5)*+{p_{2,6}} },

      { (22.5,0.7)*+{p_{n,1}} },
      { (22.5,-0.7)*+{p_{n,2}} },
      { (21,4.5)*+{p_{n,3}} },
      { (21,-4.5)*+{p_{n,4}} },
      { (24,4.5)*+{p_{n,5}} },
      { (24,-4.5)*+{p_{n,6}} },

      { (2, 0) \ar@{--}|@{>} (0,3)  },
      { (2, 0) \ar@{--}|@{>} (0,-3)  },
      { (3, 0) \ar@{--}|@{<} (5,3)  },
      { (3, 0) \ar@{--}|@{<} (5,-3)  },

      { (7, 0) \ar@{--}|@{<} (5,3)  },
      { (7, 0) \ar@{--}|@{<} (5,-3)  },
      { (8, 0) \ar@{--}|@{<} (10,3)  },
      { (8, 0) \ar@{--}|@{<} (10,-3)  },

      { (12, 0) \ar@{--}|@{<} (10,3)  },
      { (12, 0) \ar@{--}|@{<} (10,-3)  },

      { (18, 0) \ar@{--}|@{<} (20,3)  },
      { (18, 0) \ar@{--}|@{<} (20,-3)  },
      { (22, 0) \ar@{--}|@{<} (20,3)  },
      { (22, 0) \ar@{--}|@{<} (20,-3)  },

      { (23, 0) \ar@{--}|@{>} (25,3)  },
      { (23, 0) \ar@{--}|@{>} (25,-3)  },

      { (1.4,0.4)*+{\text{\textcolor{red}{$x_1$} }} },
      { (-0.5,2)*+{\text{\textcolor{red}{$x_2$} }} },
      { (-0.5,-2)*+{\text{\textcolor{red}{$x_3$} }} },

      { (24.1,0.4)*+{\text{\textcolor{red}{$x_4$} }} },
      { (26,2)*+{\text{\textcolor{red}{$x_5$} }} },
      { (26,-2)*+{\text{\textcolor{red}{$x_6$} }} },
      }
    \endxy
  \end{equation*}
  \caption{A segment of link $L$.}
  \label{fig:Ridge_2}
\end{figure}

In this case a contribution to the invariant is given by the integral,
\begin{multline}
  \iiint \prod_{j=1}^n \mathrm{d} p_{j,1} \ \mathrm{d} p_{j,2} \cdot
  \mathrm{d} x_1 \ \mathrm{d} x_4 \
  \langle p_{1,1} , x_1 \  | \  S^{-1} \  | \ x_2 , p_{1,3} \rangle \,
  \langle x_3 , p_{1,4} \ | \  S \  | \ p_{1,2} , x_1 \rangle
  \\
  \times
  \prod_{j=1}^{n-1}
  \langle p_{j,2} , p_{j,1} , p_{j,5}, p_{j+1,3} \  | \
  \Check{R}  \ | \
  p_{j,6} , p_{j+1,4}, p_{j+1,2} , p_{j+1,1} \rangle
  \\
  \times
  \langle x_5 , p_{n,5} \  | \  S \ | \  p_{n,1} , x_4 \rangle \,
  \langle p_{n,2} , x_4 \ | \ S^{-1} \  | \  x_6 , p_{n,6} \rangle .
\end{multline}
By substituting eqs.~\eqref{S_asymptotics} and~\eqref{R_asymptotics}, 
we obtain
\begin{align*}
  p_{j,2} & = p_{j,1} - p_{j,5} + p_{j,6} ,
  &
  p_{1,1} & = p_{1,3} + x_2 ,
  \\[2mm]

  p_{n,1} & = x_5 + p_{n,5},
  &
  p_{n,2} &= x_6 + p_{n,6} ,
\end{align*}
and the integral reduces to an integration over
$x_1$, $x_4$, and $p_{j,1}$ for
$j=2, 3, \dots, n-1$.
The saddle point equations for $x_1$ and $x_4$ are respectively
written as
\begin{align*}
  \frac{1 - \mathrm{e}^{x_1 - p_{1,3}}}
  {1 - \mathrm{e}^{x_1 -  p_{1,4}}}
  \cdot
  \mathrm{e}^{-x_2 + x_3}
  & = 1 ,

  &

  \frac{1 - \mathrm{e}^{x_4 - p_{n,6}}}
  {1 - \mathrm{e}^{x_4 - p_{n,5}}}
  \cdot
  \mathrm{e}^{- x_6 + x_5}
  &  = 1 .
\end{align*}
These two equations give
\begin{equation}
  \label{condition_ridge_2_octa}
  \frac{
    1 - \mathrm{e}^{p_{1,4} - x_1}
    }{
    1 - \mathrm{e}^{p_{1,3} - x_1}
    } \cdot
  \prod_{j=1}^{n-1}
  \mathrm{e}^{-p_{j,2} + p_{j+1,2} - p_{j+1,1} + p_{j,1}}
  \cdot
  \frac{
    1 - \mathrm{e}^{p_{n,5} - x_4}
    }{
    1 - \mathrm{e}^{p_{n,6} - x_4}
    }
  = 1 ,
\end{equation}
which denotes the hyperbolicity equation around  ridgelines of the
octahedron
(Fig.~\ref{fig:Ridge_2_octa}).

\begin{figure}[htbp]
  \begin{center}
    \parbox{5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{20}{$p_{1,1}$}}
        \psfrag{B}{\rotatebox{0}{$p_{1,2}$}}
        \psfig{file=glue2_ryosen.eps,scale=0.4} 
      \end{psfrags}
      }

    \parbox{5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-10}{$p_{j,6}$}}
        \psfrag{B}{\textcolor{red}{\reflectbox{\rotatebox{-20}{$p_{j,5}$}}}}
        \psfrag{C}{\rotatebox{20}{$p_{j+1,4}$}}
        \psfrag{D}{\textcolor{red}{\reflectbox{\rotatebox{30}{$p_{j+1,3}$}}}}
        \psfrag{E}{$p_{j,2}$}
        \psfrag{F}{\textcolor{red}{\reflectbox{\rotatebox{-10}{$p_{j,1}$}}}}
        \psfrag{G}{\rotatebox{20}{$p_{j+1,2}$}}
        \psfrag{H}{\textcolor{red}{\reflectbox{\rotatebox{10}{$p_{j+1,1}$}}}}
        \psfig{file=octa2_glue.eps,scale=0.35}
      \end{psfrags}
      }

    \parbox{4cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-20}{$p_{n,1}$}}
        \psfrag{B}{\rotatebox{10}{$p_{n,2}$}}
        \psfig{file=glue2_ryosen_2.eps,scale=0.4}
      \end{psfrags}
      }

  \end{center}
  \caption{
    Depicted are  polyhedra
    which  come  from Fig.~\ref{fig:Ridge_2}.
    The hyperbolicity condition around bold edges is given in
    eq.~\eqref{condition_ridge_2_octa}.}
  \label{fig:Ridge_2_octa}
\end{figure}




As a result,
we have seen that
the 3-dimensional hyperbolic structure naturally appears in
the invariant $\Tilde{\tau}_1(K)$, \emph{i.e.},
a classical limit of
the knot invariant $\tau_1(K)$  which is defined
by the integral form based on the quantum dilogarithm function.
The saddle point equation  exactly coincides
with the hyperbolicity consistency  condition in  gluing the octahedra which is
assigned to each crossing.
To be precise,
in order to see that
a finite collection of ideal tetrahedra results in  a 3-manifold,
we need to  prove  the completeness condition
by showing that
the  developing map near the ideal vertex yields Euclidean structure.
We have  checked this condition for several knots,
but  we do not
have proof at this moment.
There is still another problem to be solved.
Generally a set of the saddle point equations (hyperbolicity
consistency conditions)  has several algebraic solutions, and
we are not sure which solutions
among   them
we should choose  as 
dominant  in a definition of the invariant $\Tilde{\tau}_1(K)$.
When we assume that  
geometrically preferable   solutions $z_i$ of the saddle point
conditions
are
dominant
in  the  classical limit,
we may  conclude that
\begin{align}
  \label{result_tau}
  \Tilde{\tau}_1(K)
  & =
  \sum_{\text{ideal tetrahedra}:  i}
  L(1-z_i) ,







\end{align}
as each tetrahedron has a function $V(x,y)$
which reduces to the Rogers dilogarithm
function   at the critical point~\eqref{property_V}.
