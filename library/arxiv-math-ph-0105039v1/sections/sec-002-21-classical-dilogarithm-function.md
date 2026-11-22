---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-002-21-classical-dilogarithm-function
section_title: "Classical Dilogarithm Function"
section_number: 2.1
pages: 3-5
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.752
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We collect properties concerning the classical dilogarithm function
(see Refs.~\citen{LLewi91Book,Kiril94} for review).
The Euler dilogarithm function $\Li(x)$ is defined by

\begin{align}
  \Li(x)
  =
  \sum_{n=1}^\infty \frac{x^n}{n^2}

  = - \int_0^x
  \frac{\log(1-s)}{s} \, \mathrm{d} s  .
  \label{Euler_integral}
\end{align}

The range $|x| \leq 1$ in an infinite series is extended outside the
unit circle in the second
integral form~\eqref{Euler_integral}.
We later use the Rogers dilogarithm function  defined by
\begin{equation}
  \label{Rogers}
  L(z)
  =
  \Li(z) + \frac{1}{2} \log z \, \log(1-z) .
\end{equation}

Based on the integral form of the dilogarithm function,
we have  the following identities (due to Euler);
\begin{gather}
  \label{Euler_1}
  \Li(z) + \Li(-z) = \frac{1}{2} \, \Li(z^2) ,
  \\[2mm]

  \Li(-z) + \Li(-z^{-1})
  = 2 \, \Li (-1) - \frac{1}{2} \bigl( \log  z  \bigr)^2,
  \label{inverse_Euler}
  \\[2mm]

  \Li(z) + \Li(1-z) = \Li(1) - \log z \, \log(1-z) .
\end{gather}
The first two identities are respectively called the duplication and inversion
relations.
By setting
$z= \mathrm{e}^{\mathrm{i} \, \pi}$ in those identities, we
get
\begin{align}
  \Li(1) &=
  \frac{\pi^2}{6} ,
  &
  \Li(-1) &=
  - \frac{\pi^2}{12} .
\end{align}
Besides above equations, we have a two-variable equation, which we
call  the pentagon identity
 (this form was first written by Schaeffer);
\begin{equation}
  \label{pentagon_Euler}






  \Li(\frac{1-x^{-1}}{1-y^{-1}})
  =
  \Li(x) - \Li(y) + \Li(\frac{y}{x})
  +
  \Li(\frac{1-x}{1-y})
  -\frac{\pi^2}{6}
  + \log x \log (\frac{1-x}{1-y}) ,
\end{equation}
or
\begin{equation}
      L(x) - L(y) + L(\frac{y}{x})
    -L(\frac{1-x^{-1}}{1-y^{-1}})
    +L(\frac{1-x}{1-y}) = \frac{\pi^2}{6} .
\end{equation}

It is known that the variant of the dilogarithm function appears in
the 3-dimensional hyperbolic geometry.
Due to Refs.~\citen{WPThurs80Lecture,JMiln82a}, the  volume of the
ideal tetrahedron in
the 3-dimensional hyperbolic space is given by the Bloch--Wigner
function $D(z)$, which is defined by
\begin{equation}
  \label{Bloch_Wigner}
  D(z)
  = \Im \, \Li(z) + \arg(1-z) \cdot \log |z| .
\end{equation}
Here $z$ is a complex parameter $\Im \, z >0$,
which parameterizes the ideal tetrahedron;
the Euclidean triangle cut out of any vertex of the ideal tetrahedron
is similar to that in Fig.~\ref{fig:triangle}.
{}From eq.~\eqref{Euler_1}--\eqref{pentagon_Euler}  we get
\begin{subequations}
  \label{Bloch_relation}
  \begin{gather}
    D(z)

    =
    -D(z^{-1})
    = - D(1-z)

    ,
    \\[2mm]

    D(x) - D(y) + D(\frac{y}{x})
    - D(\frac{1 - x^{-1}}{1 - y^{-1}})
    + D(\frac{1 - x}{1- y})
    = 0 .





  \end{gather}
\end{subequations}












Using the first identity
we can extend a modulus $z$ to  $z\in\mathbb{C} \setminus \{0,1\}$
by regarding
$D(z)$ as the signed
volume of the oriented tetrahedron.

\begin{figure}[htbp]
  \centering
  \begin{equation*}
    \xy/r1.0pc/:.
    {
      { (0,0) \ar@{-} (10,0) },
      { (0,0) \ar@{-} (6,8) },
      { (10,0) \ar@{-} (6,8) },

      { (-0.5,-0.5)*+{0} },
      { (10.5,-0.5)*+{1} },
      { (6,8.5)*+{z} },

      { (1,0.5)*+{z} },
      { (8.2,1)*+{\frac{1}{1-z}} },
      { (5.7,5.8)*+{{1-\frac{1}{z}}} },
      }
    \endxy
  \end{equation*}
  \caption{}
  \label{fig:triangle}
\end{figure}
