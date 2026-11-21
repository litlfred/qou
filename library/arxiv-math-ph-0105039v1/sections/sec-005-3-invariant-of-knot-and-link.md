---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-005-3-invariant-of-knot-and-link
section_title: "Invariant of Knot and Link"
section_number: 3
pages: 10-11
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.99
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
\label{sec:invariant}

With the ${R}$-matrix
$\Check{R}: \mathbf{W}^{\otimes 2} \to \mathbf{W}^{\otimes 2}$
satisfying the braid
relation~\eqref{YBE_compact},
we can define the invariant of  the  knot $K$.










We assume that we
have the  enhanced Yang--Baxter operators
($\Check{R}, \mu , \alpha, \beta$)
satisfying~\cite{Turae88}
\begin{subequations}
  \label{other_enhanced}
  \begin{gather}
    \bigl( \mu \otimes \mu \bigr) \, \Check{R}
    =
    \Check{R} \, \bigl( \mu \otimes \mu \bigr) ,
    \\[2mm]
                                
    \Tr_2 \Bigl(
    \Check{R}^{\pm 1} \, 
    \bigl( 1 \otimes \mu \bigr)
    \Bigr)
    =
    \alpha^{\pm 1} \, \beta  .
  \end{gather}
\end{subequations}
Here the operator $\mu$ acts on a space $\mathbf{W}$.
When the knot $K$ is given as the closure of
a braid $\xi$ which is represented  in terms of
the Artin $n$ string braid group,
\begin{equation}
  \left\langle
    \sigma_1, \dots, \sigma_{n-1}
    \ \Big| \
    \begin{array}{ll}
      \sigma_i \, \sigma_j = \sigma_j \, \sigma_i,
      &
      \text{for $|i-j| \geq 2$}
      \\[2mm]
      \sigma_i \, \sigma_{i+1} \, \sigma_i
      =
      \sigma_{i+1} \, \sigma_i \, \sigma_{i+1} ,
      &
      \text{for $i=1,\dots,n-1$}
    \end{array}
  \right\rangle ,
\end{equation}
we get the knot invariant $\tau(K)$;
\begin{equation}
  \tau(K)
  =
  \alpha^{- w(\xi)} \, \beta^{-n} \,
  \Tr_{1,\dots, n}
  \Bigl(
  b_R(\xi) \, \mu^{\otimes n}
  \Bigr)  ,
\end{equation}
where $w(\xi)$ is a writhe, \emph{i.e.},  a sum of the exponents, and
$b_R(\xi)$ means   to replace the braid operators $\sigma^{\pm 1}$
by $\Check{R}^{\pm 1}$.
Later we   use another knot  invariant,
\begin{equation}
  \label{tau_1_invariant}
  \tau_1(K)
  =
  \alpha^{- w(\xi)} \,
  \beta^{-n} \,
  \Tr_{2,\dots,n}
  \Bigl(
  b_R(\xi) \, \mu^{\otimes (n-1)}
  \Bigr) ,
\end{equation}
which is associated for ($1,1$)-tangle.

When we use the $\Check{R}$-matrix defined
in eq.~\eqref{R_element},
we find that the $\mu$ operator defined by~\footnote{
The author  thanks
Rinat Kashaev for pointing out an error of
previous manuscript.}
\begin{equation}
  \label{mu_operator}
  \mu =
  \mathrm{e}^{\frac{\pi + \gamma}{\gamma} \, \Hat{p}}
  \otimes
  \mathrm{e}^{ - \frac{\pi + \gamma}{\gamma} \, \Hat{p}^{\mathrm{t}}}
\end{equation}
fulfills eqs.~\eqref{other_enhanced}
with parameters
\begin{align}
  \label{alpha_beta}
  \alpha
  & =
  \mathrm{e}^{- \mathrm{i} \, \frac{\pi^2+\gamma^2}{\gamma}}
  ,
  &
  \beta
  & =
  \frac{
    \gamma \,
    \mathrm{e}^{\mathrm{i} \frac{\pi^2+\gamma^2}{\gamma}}
    }{
    ( 1 - \mathrm{e}^{2 \gamma \mathrm{i}} ) \,
    ( 1 - \mathrm{e}^{2 \frac{\pi^2}{\gamma} \mathrm{i}})
    } .
\end{align}
In this computation  $\Tr$ means integration, and we have used
$
  \delta(x)
  =
  \lim_{\Delta \to 0} \frac{\Delta}{x^2+ \Delta^2} 
$.
As a consequence we have obtained the knot invariant $\tau_1(K)$ from
a set of the
Yang--Baxter operators defined with  eq.~\eqref{R_compact} and
eqs.~\eqref{mu_operator}~--~\eqref{alpha_beta}.
We should stress
that our invariant $\tau_1(K)$
can be viewed as a  non-compact analogue
of Kashaev's invariant which coincides with the colored Jones
polynomial at a specific value as was proved in Ref.~\citen{MuraMura99a}.
In fact
Kashaev's $R$-matrix~\cite{Kasha95} was originally defined based on 
a reduction of
the quantum $S$-operator
when the deformation parameter $\mathrm{e}^{\mathrm{i} \gamma}$
approaches a root of unity.
In  that case the pentagon identity~\eqref{pentagon_S} is
replaced by
\begin{equation*}
    S_{1,2}(p,q,r) \, S_{1,3}(p, q \, r , s) \, S_{2,3}(q,r,s)
  =
  S_{2,3}(p \, q , r , s) \, S_{1,2}(p,q,r \, s)  ,
\end{equation*}
where $p , \dots, s$ are parameters, and a solution $S$  is given in a
finite-dimensional  matrix.





In the following,
we have interests in the asymptotic behavior of the invariant
$\tau_1(K)$, and we define
\begin{equation}
  \label{limit_invariant}
  \Tilde{\tau}_1(K)
  =
  \lim_{\gamma \to 0}
  \Bigl(
  2 \, \mathrm{i} \, \gamma
  \log \tau_1(K)
  \Bigr) .
\end{equation}
As our construction of the invariant is essentially  same with
Kashaev's invariant,
we expect that
the conjecture~\eqref{volume_conjecture} will be applicable to the
invariant~\eqref{limit_invariant}.
