---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-009-52-hyperbolicity-condition-for-surface
section_title: "Hyperbolicity Condition for Surface"
section_number: 5.2
pages: 18-20
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.986
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We first consider a surface $D_a$, which is surrounded by  alternating
crossings as in Fig.~\ref{fig:alternate_knot}.
We assign octahedron  for each crossing following
eq.~\eqref{attach_octa}, and introduce variables as
shown there.
\begin{figure}[t]
  \begin{equation*}
    \xy/r2.0pc/:.
    {
      { (0,0)*+{D_a} },

      { (5, -1.73) \ar@{-}|@{} (4.4, -0.7) },
      { (3.6, 0.7) \ar@{-}|@{} (1, 5.2) },
      { (4, 3.46) \ar@{-}|@{} (2.5, 3.46) },
      { (1.5, 3.46) \ar@{-}|@{} (-4, 3.46) },

      { (-1, 5.2) \ar@{-}|@{} (-1.6, 4.15) },
      { (-2.4, 2.77) \ar@{-}|@{} (-5, -1.73) },
      { (-5, 1.73) \ar@{-}|@{} (-4.4, 0.7) },
      { (-3.6, -0.7) \ar@{-}|@{} (-1, -5.2) },

      { (-4, -3.46) \ar@{-}|@{} (-2.5, -3.46) },
      { (-1.5, -3.46) \ar@{-}|@{} (4, -3.46) },
      { (1, -5.2) \ar@{-}|@{} (1.6, -4.15) },
      { (2.4, -2.77) \ar@{-}|@{} (5, 1.73) },

      { (4,0)*+{\otimes} },
      { (2, 3.46)*+{\otimes} },
      { (-2, 3.46)*+{\otimes} },
      { (-4,0)*+{\otimes} },
      { (2, -3.46)*+{\otimes} },
      { (-2, -3.46)*+{\otimes} },

      { (2.8, 2.08) \ar@{--}|@{<} (3.5, 3.46)  },
      { (2.8, 2.08) \ar@{--}|@{<} (0.5, 3.46)  },
      { (3.5, 3.46)  \ar@{--}|@{>} (1.2, 4.85) },
      { (0.5, 3.46)  \ar@{--}|@{>} (1.2, 4.85) },

      { (3.2, 1.39) \ar@{--}|@{>} (4.8,1.39)  },
      { (3.2, 1.39) \ar@{--}|@{>} (3.2, -1.39)  },
      { (4.8, -1.39) \ar@{--}|@{>} (4.8,1.39)  },
      { (4.8, -1.39) \ar@{--}|@{>} (3.2, -1.39)  },

      { (-3.2, 1.39) \ar@{--}|@{<} (-4.8,1.39)  },
      { (-3.2, 1.39) \ar@{--}|@{<} (-3.2, -1.39)  },
      { (-4.8, -1.39) \ar@{--}|@{<} (-4.8,1.39)  },
      { (-4.8, -1.39) \ar@{--}|@{<} (-3.2, -1.39)  },

      { (-2.8, 2.08) \ar@{--}|@{>} (-3.5, 3.46)  },
      { (-2.8, 2.08) \ar@{--}|@{>} (-0.5, 3.46)  },
      { (-3.5, 3.46)  \ar@{--}|@{<} (-1.2, 4.85) },
      { (-0.5, 3.46)  \ar@{--}|@{<} (-1.2, 4.85) },

      { (-2.8, -2.08) \ar@{--}|@{<} (-3.5, -3.46)  },
      { (-2.8, -2.08) \ar@{--}|@{<} (-0.5, -3.46)  },
      { (-3.5, -3.46)  \ar@{--}|@{>} (-1.2, -4.85) },
      { (-0.5, -3.46)  \ar@{--}|@{>} (-1.2, -4.85) },

      { (2.8, -2.08) \ar@{--}|@{>} (3.5, -3.46)  },
      { (2.8, -2.08) \ar@{--}|@{>} (0.5, -3.46)  },
      { (3.5, -3.46)  \ar@{--}|@{<} (1.2, -4.85) },
      { (0.5, -3.46)  \ar@{--}|@{<} (1.2, -4.85) },


      { (0,4)*+{p_1^\prime} },
      { (0,3)*+{p_1} },
      { (-3.5,2)*+{p_2^\prime} },
      { (-2.5,1.4)*+{p_2} },
      { (-3.5, -2)*+{p_3^\prime} },
      { (-2.5, -1.4)*+{p_3} },
      { (3.5, 2)*+{p_n^\prime} },
      { (2.5, 1.4)*+{p_n} },

      { (1.2, 3.3)*+{\textcolor{red}{x_1}} },
      { (-1.2, 3.7)*+{\textcolor{red}{y_1}} },
      { (-2.1, 2.77)*+{\textcolor{red}{x_2}} },
      { (-3.8, 0.7)*+{\textcolor{red}{y_2}} },
      { (-3.4, -0.7)*+{\textcolor{red}{x_3}} },
      { (-2.6, -2.77)*+{\textcolor{red}{y_3}} },
      { (2.7, 2.77)*+{\textcolor{red}{y_n}} },
      { (3.3, 0.7)*+{\textcolor{red}{x_n}} },

      { (4, 4)*+{\text{\ding{172}}} },
      { (-2, 5)*+{\text{\ding{173}}} },
      { (-5.5, 1)*+{\text{\ding{174}}} },
      }
    \endxy
  \end{equation*}
  \caption{A segment of link $L$ which is surrounded by  
    alternating  crossings is depicted.
    We number each vertex as \ding{172}, \ding{173}, $\ldots$.}
  \label{fig:alternate_knot}
\end{figure}
A contribution to the  invariant $\tau_1(L)$
from above segment of link
$L$
is thus
given by
\begin{equation}
  \iiint \mathrm{d} p_1 \cdots \mathrm{d} p_n \

  \prod_{i=0}^{n-1}
  \langle p_{i+1} , x_{i+1} \  | \  S^{-1} \ | \  y_i, p_i \rangle

  ,
\end{equation}
where we use $y_0=y_n$ and $p_0=p_n$.
By substituting an asymptotic form~\eqref{S_asymptotics},
we get
$p_{i+1}= p_1 + \sum_{j=1}^{i} y_j$ for $i>0$, and the integral reduces to
\begin{equation*}
  \delta(y_1 + \dots + y_n) \cdot
  \int \mathrm{d} p_1 \
  \exp \frac{1}{2 \, \mathrm{i} \, \gamma}
  \biggl(
  \sum_{i=0}^{n-1}
  \Bigl( \frac{\pi^2}{6} - \Li(\mathrm{e}^{x_{i+1} - p_i})
  - x_{i+1} \, y_i \Bigr)

  +\sum_{1 \leq i< j \leq n} y_i \, y_j
  \biggr) .
\end{equation*}
We evaluate this integral at the saddle point, whose condition is
\begin{equation}
  \prod_{i=0}^{n-1}
  \bigl(
  1 - \mathrm{e}^{x_{i+1} - p_i}
  \bigr)
  = 1  .
\end{equation}
This equation coincides with
the hyperbolicity condition for gluing $n$
tetrahedra in surface $D_a$ along an axis parallel to  axes
$\otimes$ in Fig.~\ref{fig:alternate_knot}
(see also Fig.~\ref{fig:41_glue_1} and Fig.~\ref{fig:41_glue_sp}
for  $n=3$ and $n=2$ cases).

We can see that the same
correspondence occurs for non-alternating case.
We suppose a surface $D_a$ is surrounded like
Fig.~\ref{fig:alternate_knot} whereas  each  vertex  $i$ is
either
over-crossing $\xybox{0;/r1.4pc/:, {\xoverv<|||>{~D_a}} }$ or
under-crossing  $\xybox{0;/r1.4pc/:, {\xunderv<|||>{D_a}} }$,
which  we  denote $i \in \mathcal{O}$ and $i \in \mathcal{U}$
respectively.
In this case  a  contribution to the invariant is given by
\begin{equation}
  \iiint \mathrm{d} p_1 \cdots \mathrm{d}p_n \
  \prod_{i \in \mathcal{O}}
  \langle p_{i+1}, x_{i+1} \ | \  S^{-1} \  | \ y_i , p_i \rangle \cdot
  \prod_{i \in \mathcal{U}}
  \langle x_{i+1} , p_{i+1} \  | \  S \  | \  p_i , y_i \rangle .
\end{equation}
By substituting an expression~\eqref{S_asymptotics} 
we obtain
\begin{align*}
  p_{k+1}
  & =
  p_1 + \sum_{
    \substack{1\leq i \leq k\\
      i\in \mathcal{O}}} y_i
  - \sum_{
    \substack{1 \leq i \leq k\\
      i \in \mathcal{U}}}
  x_{i+1} ,

  &

  & \sum_{i \in \mathcal{O}} y_i = \sum_{i \in \mathcal{U}} x_{i+1} ,
\end{align*}
and the integral becomes
\begin{multline*}
  \delta(\sum_{i \in \mathcal{O}} y_i - \sum_{i \in \mathcal{U}} x_{i+1} )
  \int \mathrm{d} p_1 \
  \exp \frac{1}{2 \, \mathrm{i} \, \gamma}
  \biggl(
  \sum_{i\in \mathcal{O}}
  \Bigl(
  \frac{\pi^2}{6} - \Li(\mathrm{e}^{x_{i+1} - p_i}) - x_{i+1} \, y_i
  \Bigr)
  \\
  +
  \sum_{i \in \mathcal{U}}
  \Bigl(
  -\frac{\pi^2}{6} + \Li(\mathrm{e}^{y_i - p_{i+1}}) + x_{i+1} \, y_i
  \Bigr)
  +
  \sum_{\substack{i,j \in \mathcal{O}\\
    i<j}} y_i \, y_j
  -
  \sum_{\substack{i \in \mathcal{U} \\
      j \in \mathcal{O}}} x_{i+1} \, y_j
  +
  \sum_{\substack{i,j \in \mathcal{U}\\
      i \leq j}}
  x_{i+1} \, x_{j+1}
  \biggr).
\end{multline*}
The saddle point equation is given as
\begin{equation}
  \prod_{i \in \mathcal{O}}
  \Bigl(
  1- \mathrm{e}^{x_{i+1} - p_i}
  \Bigr)
  \cdot
  \prod_{i \in \mathcal{U}}
  \Bigl(
  1- \mathrm{e}^{y_i - p_{i+1}}
  \Bigr)^{-1}
  =1 ,
\end{equation}
which coincides with  the hyperbolicity equation around an axis in
$D_a$   parallel to axes $\otimes$.
