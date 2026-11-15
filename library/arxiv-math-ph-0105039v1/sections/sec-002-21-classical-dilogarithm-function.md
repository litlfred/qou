---
doc_id: arxiv-math-ph-0105039v1
doc_title: "arXiv:math-ph/0105039v1 28 May 2001"
section_id: sec-002-21-classical-dilogarithm-function
section_title: "Classical Dilogarithm Function"
section_number: 2.1
pages: 3-8
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.888
latex_coverage_ratio: 0.899
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





\subsection{Quantum Dilogarithm Function and the $R$ Operator}

We define a function  $\Phi_\gamma(\varphi)$ by an integral form
following Ref.~\citen{LFadd96a}:
\begin{equation}
  \label{Faddeev_integral}
  \Phi_\gamma(\varphi)
  =
  \exp
  \left(
    \int_{\mathbb{R}+\mathrm{i} \, 0}
    \frac{\mathrm{e}^{- \mathrm{i} \, \varphi \, x}}
    {
      4 \sh ( \gamma \, x) \, \sh(\pi \, x)
      } \,
    \frac{\mathrm{d} x}{x}
  \right) ,
\end{equation}
where we take $\gamma \in \mathbb{R}$.
We note that in Ref.~\citen{Ruijse97a} an essentially same integral
was introduced
in a context of the hyperbolic gamma function, and that
in Ref.~\citen{SLWoron00a} another integral was studied  as the
quantum exponential function which solves the same functional
equations
below.
Also the integral~\eqref{Faddeev_integral} was used to compute the
asymptotic form of Kashaev's invariant~\cite{Kasha96b}.
The function $\Phi_\gamma(\varphi)$
is known as a quantization of the dilogarithm function, and
we have in a limit $\gamma \to 0$
\begin{equation}
  \label{Phi_gamma_0}
  \Phi_\gamma(\varphi)

  \sim
  \exp
  \left(
    \frac{1}{2 \,  \mathrm{i} \, \gamma} \,
    \Li(- \mathrm{e}^\varphi)
  \right) .



\end{equation}

We list below several interesting properties of the integral
$\Phi_\gamma(\varphi)$.
\begin{itemize}
\item Duality,
  \begin{equation}
    \Phi_{\frac{\pi^2}{\gamma}} ( \varphi)
    =
    \Phi_{\gamma}(\frac{\gamma}{\pi} \, \varphi) .
  \end{equation}

\item Zero points,
  \begin{equation}
    \text{zeros of $\bigl( \Phi_\gamma(x) \bigr)^{\pm 1}$}
    =
    \Bigl\{
    \mp \mathrm{i} \,
    \bigl(
    (2 \, m +1 ) \, \gamma +
    ( 2 \, n + 1 ) \, \pi
    \bigr)
    \ \big| \
    m, n \in \mathbb{Z}_{\geq 0}
    \Bigr\}


















  \end{equation}

\item  Inversion relation,
  \begin{equation}
    \label{inversion_Phi}
    \Phi_\gamma(x) \cdot \Phi_\gamma( -x)
    =
    \exp
    \left(
      - \frac{1}{2 \, \mathrm{i} \, \gamma}
      \Bigl(
      \frac{x^2}{2} + \frac{\pi^2 + \gamma^2}{6}
      \Bigr)
    \right) .
  \end{equation}
  By taking a limit $\gamma \to 0$ and using eq.~\eqref{Phi_gamma_0},
  we obtain
  \begin{equation*}
    \Li(- \mathrm{e}^x) + \Li(-\mathrm{e}^{-x})
    +
    \frac{x^2}{2} + \frac{\pi^2}{6} = 0 ,
  \end{equation*}
  which is nothing but
  the inversion identity~\eqref{inverse_Euler}  for the Euler
  dilogarithm function.


\item Difference equations,
  \begin{subequations}
    \begin{align}
      \frac{\Phi_\gamma(\varphi + \mathrm{i} \, \gamma)}
      {    \Phi_\gamma(\varphi - \mathrm{i} \, \gamma)}
      & =
      \frac{1}{1 + \mathrm{e}^\varphi}         ,
      \\[2mm]

      \frac{ \Phi_\gamma(\varphi + \mathrm{i} \, \pi)}{
        \Phi_\gamma(\varphi - \mathrm{i} \, \pi)}
      & =
      \frac{1}{1 + \mathrm{e}^{\frac{\pi}{\gamma}\varphi}} .
    \end{align}


    
  \end{subequations}

\item Pentagon relation~\cite{FaddKash94,ChekFock99a,LFadd99b},
    \begin{equation}
      \label{pentagon_Phi}
      \Phi_\gamma(\Hat{p}) \, \Phi_\gamma(\Hat{q})
      =
      \Phi_\gamma(\Hat{q}) \, \Phi_\gamma(\Hat{p} + \Hat{q}) \,
      \Phi_\gamma(\Hat{p})  ,
    \end{equation}
    where $\Hat{p}$ and $\Hat{q}$ are the canonically conjugate
    operators satisfying the Heisenberg commutation relation,
    \begin{equation}
      \label{canonical}
      [\Hat{p} ~,~ \Hat{q} ] = - 2 \, \mathrm{i} \, \gamma .  
    \end{equation}
    In this sense, the parameter $\gamma$ in the
    integral~\eqref{Faddeev_integral}  is the Planck constant.

  \item
    The Fourier transformation~\cite{FaddKashVolk00a,PonsoTesch00a},
    \begin{subequations}
      \label{Fourier_transform}
      \begin{gather}
        \frac{1}{\sqrt{4 \, \pi \, \gamma}}
        \int \mathrm{d} y \ \Phi_\gamma(y) \,
        \mathrm{e}^{\frac{1}{2 \, \mathrm{i} \, \gamma} \, x \, y}
        =
        \Phi_\gamma(-x + \mathrm{i} \pi + \mathrm{i} \gamma)
        \,
        \mathrm{e}^{
          \frac{1}{2 \, \mathrm{i} \, \gamma}
          \left(
            \frac{x^2}{2}
            - \frac{1}{2} \pi \gamma
            -
            \frac{\pi^2 + \gamma^2}{6}
          \right)
          } ,
        \\[2mm]

        \frac{1}{\sqrt{4 \, \pi \, \gamma}}
        \int \mathrm{d} y \
        \frac{1}{\Phi_\gamma(y)} \,
        \mathrm{e}^{
          \frac{1}{2 \, \mathrm{i} \, \gamma} x \, y
          }
        =
        \frac{1}{
          \Phi_\gamma(x - \mathrm{i}\, \pi - \mathrm{i}\, \gamma)
          } \,
        \mathrm{e}^{
          -\frac{1}{2 \, \mathrm{i} \, \gamma}
          \left(
            \frac{x^2}{2}
            - \frac{1}{2} \pi \gamma
            - \frac{\pi^2+\gamma^2}{6}
          \right)
          } ,
        \\[2mm]

        \begin{split}
          & \frac{1}{\sqrt{4 \, \pi \, \gamma}}
          \int \mathrm{d} y \
          \frac{\Phi_\gamma(y+u)}{\Phi_\gamma(y+v)} \,
          \mathrm{e}^{
            -\frac{1}{2 \mathrm{i} \gamma} \, x \, y
            }
          \\
          & \qquad =
          \frac{
            \Phi_\gamma(v-u-x+\mathrm{i}\pi + \mathrm{i}\gamma)
            }{
            \Phi_\gamma(v-u+\mathrm{i}\pi + \mathrm{i}\gamma) \,
            \Phi_\gamma(-x-\mathrm{i}\pi - \mathrm{i}\gamma)
            } \,
          \mathrm{e}^{
            \frac{1}{2 \mathrm{i} \gamma}
            \left(
              x ( u- \mathrm{i} \pi - \mathrm{i} \gamma)
              +
              \frac{1}{2} \pi \gamma
              +
              \frac{\pi^2+\gamma^2}{6}
            \right)
            } .
        \end{split}
      \end{gather}
    \end{subequations}
\end{itemize}

For our later convention, we rewrite the pentagon
identity~\eqref{pentagon_Phi}
into a
simple form.
We   define the $S$-operator  on $\mathbf{V}\otimes\mathbf{V}$ by
\begin{equation}
  \label{define_S_operator}
  S_{1,2}
  =
  \mathrm{e}^{
    \frac{1}{2 \,  \mathrm{i}\, \gamma} \,
    \Hat{q}_1 \, \Hat{p}_2
    } \,
  \Phi_\gamma (\Hat{p}_1 + \Hat{q}_2 - \Hat{p}_2) ,
\end{equation}
where the Heisenberg operators $\Hat{p}_a$
and $\Hat{q}_a$ act on the $a$-th  vector
space $\mathbf{V}$.
Then the pentagon identity~\eqref{pentagon_Phi} can be
rewritten as
\begin{equation}
  \label{pentagon_S}
  S_{2,3} \, S_{1,2}
  =
  S_{1,2} \, S_{1,3} \, S_{2,3} ,
\end{equation}
where $S_{a,b}$ acts on the $a$- and $b$-th spaces of
$\mathbf{V}\otimes \mathbf{V} \otimes \mathbf{V}$.
See that
the  operator,
$
  T_{1,2}
  =
  \mathrm{e}^{\frac{1}{2 \, \mathrm{i} \, \gamma } \, \Hat{q}_1 \,
    \Hat{p}_2}  
$,
which is a prefactor of the $S$-operator~\eqref{define_S_operator},
is a simple solution of  eq.~\eqref{pentagon_S}.
We remark  that
the pentagon identity~\eqref{pentagon_S} is a natural consequence  of
the Heisenberg double~\cite{Kasha95b,Kasha96a}, in which the $S$-operator is
given by
\begin{equation*}
  S = \sum_\alpha e_\alpha \otimes e^\alpha .
\end{equation*}
Here $\{ e_\alpha , e^\alpha \}$ is a set of generators satisfying
\begin{gather*}
  e_\alpha \, e_\beta = \sum_\gamma m^\gamma_{\alpha ~ \beta} \, e_\gamma ,
  \\
  e^\alpha \, e^\beta
  = \sum_\gamma  \mu_\gamma^{\alpha ~ \beta} \, e^\gamma ,
  \\
  e_\alpha \, e^\beta =
  \sum_{\gamma, \rho, \sigma}
  m^\beta_{\rho ~ \gamma} \, \mu_\alpha^{\gamma ~ \sigma} \,
  e^\rho \, e_\sigma .
\end{gather*}

For our purpose to define the knot invariant, we  introduce the
$R$-operator by use of the $S$-operators as~\cite{LFadd99b,Kasha95b,Hikam00a}
\begin{equation}
  \label{R_compact}
  R_{1 2, 3 4}
  =
  \Bigl( S_{1,4}^{\mathrm{t}_4} \Bigr)^{-1} \,
  S_{1,3} \,
  S_{2,4}^{\mathrm{t}_2  \mathrm{t}_4} \,
  \Bigl( S_{2,3}^{\mathrm{t}_2} \Bigr)^{-1} ,
\end{equation}
and we set
\begin{equation}
  \label{check_R}
  \Check{R}_{1 2, 3 4}
  = P_{1,3} \, P_{2,4} \, R_{1 2 , 3 4} .
\end{equation}
Here $\mathrm{t}_a$ means a transposition on the $a$-th space, and $P$
is the permutation operator.
The $R$-operator  acts on a vector space $\mathbf{V}^{\otimes 4}$.
Based on the pentagon identity~\eqref{pentagon_S}, we find that the
$\Check{R}$-operator~\eqref{check_R}
satisfies the Yang--Baxter relation,
\begin{equation}
  \label{YBE_compact}
  \Check{R}_{1 1^\prime, 2 2^\prime} \,
  \Check{R}_{2 2^\prime, 3 3^\prime} \,
  \Check{R}_{1 1^\prime, 2 2^\prime}
  =
  \Check{R}_{2 2^\prime, 3 3^\prime} \,
  \Check{R}_{1 1^\prime, 2 2^\prime} \,
  \Check{R}_{2 2^\prime, 3 3^\prime} .








\end{equation}
By regarding the $R$-operator as an operator on
$\mathbf{W} \otimes \mathbf{W}$ with
$\mathbf{W} = \mathbf{V}^{\otimes 2}$,
this Yang--Baxter relation can be seen as a braid relation as usual,
which can be depicted 
as a projection onto 2-dimensional space in Fig.~\ref{fig:YBE}.

\begin{figure}[htbp]
  \centering
  \begin{equation*}
    \xygraph{!{0;/r2pc/:/u3pc/::}="A"
      "A"  [u(.5)]!{\xunderv}
      [urr]!{\xcapv}
      "A"     [d(.5)]!{\xcapv[-1]}
      [ur]!{\xunderv}
      "A"  [d(1.5)] !{\xunderv}
      [urr]!{\xcapv}
      }
    =
    \xygraph{!{0;/r2pc/:/u3pc/::}="A"
      "A"  [u(.5)]!{\xcapv[-1]}
      [ur]!{\xunderv}
      "A"      [d(.5)]!{\xunderv}
      [urr]!{\xcapv}
      "A"     [d(1.5)]!{\xcapv[-1]}
      [ur] !{\xunderv}
      }
    \label{fig:braid_relation}
  \end{equation*}
  \caption{Braid relation, or the constant Yang--Baxter equation.}
  \label{fig:YBE}
\end{figure}
