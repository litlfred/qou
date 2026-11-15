---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-006-5-proving-nonlinear-inequalities-with-bernstein
section_title: "Proving nonlinear inequalities with Bernstein bases"
section_number: 5
pages: 12-16
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.98
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
\label{sec:zumkeller}


The hardest computational part of the original proof of the Kepler conjecture is the verification of a list of about a thousand nonlinear inequalities. This section presents a technique aimed at proving
them, based on polynomial approximation and Bernstein bases. We feel that
this approach better fits the requirements of formal proof, as outlined in
Section~\ref{sec:sean}.  We hope to refine the method to cover all Flyspeck
inequalities.

We exhibit the method on a single inequality~\calc{586468779}.
The original proof contains the following definitions \cite{sp1}:
\begin{align*}
  \pt &\coloneq - \frac \pi 3 + 4 \arctan \frac{\sqrt 2}5 \\
\doct &\coloneq \frac {\pi - 4 \arctan \frac{\sqrt 2}5}{2 \sqrt 2}\\
\Delta(y) &\coloneq \frac 1 2
  \left|
  \begin{array}{ccccc}
0 & 1 & 1 & 1 & 1 \\
   1 & 0 & y_3^2 & y_2^2 & y_1^2 \\
   1 & y_3^2 & 0 & y_4^2 & y_5^2 \\
   1 & y_2^2 & y_4^2 & 0 & y_6^2 \\
   1 & y_1^2 & y_5^2 & y_6^2 & 0
  \end{array}
  \right|\\
\asolid_0(y) &\coloneq y_1 y_2 y_3 + \sfrac 1 2 (
y_1^2 y_2 + y_1 y_2^2 + y_1^2 y_3 + y_2^2 y_3 + y_1 y_3^2 \\
&\qquad\qquad\qquad {} + y_2 y_3^2 - y_1 y_4^2 - y_2 y_5^2 - y_3 y_6^2)\\
\asolid_1(y) &\coloneq \asolid_0 (y_1, y_5, y_6, y_4, y_2, y_3)\\
\asolid_2(y) &\coloneq \asolid_0 (y_2, y_4, y_6, y_5, y_1, y_3)\\
\asolid_3(y) &\coloneq \asolid_0 (y_4, y_5, y_3, y_1, y_2, y_6)\\
\gamma(y) &\coloneq 
- \frac \doct 6 \sqrt {\Delta(y)} + \frac 2 3 \sum_{i=0}^3 \arctan \frac
{\sqrt{\Delta(y)}} {\asolid_i(y)}.
\end{align*}

The statement of the inequality is:
\begin{equation}
\forall y \in [2,2.51]^6.\; \gamma(y) \le \pt. \label{gamma-pt}
\end{equation}
Define the difference of two intervals by $[a_1,b_1]-[a_2,b_2] = [a_1-b_2,b_1-a_2]$.
Interval arithmetic is used to prove the inequalities in the original proof.
It
suffers from the \emph{dependency problem}: the minimum and maximum of the
formula $x-x$ are overestimated because $[a,b] - [a,b] = [a-b,b-a]$, although
$x-x$ is clearly $0$. Subdividing $[a,b]$ into $[a,\sfrac{a+b}2]$ and
$[\sfrac{a+b}2,b]$, and then re-evaluating the formula yields an improved
result. However, depending on the problem, the number of required subdivisions
can be very large. This is why checking some inequalities takes a very long
time.


\subsection{From geometrical functions to polynomials}
Fortunately, better methods than interval arithmetic are available, if the
function under consideration is polynomial. A quick look at $\gamma$ tells us
that \eqref{gamma-pt} is not polynomial, since it has occurrences of
$\sqrt\cdot$, $1/\cdot$, and $\arctan$. Can it nevertheless be reduced
to a polynomial problem? Two strategies come to mind:

First, algebraic laws such as $\sqrt a \le b \Leftrightarrow a \le b^2$ (if $b
\ge 0$) and $\frac a b \le c \Leftrightarrow a \le bc$ (if $b>0$) can often be
used to eliminate occurrences of $\sqrt\cdot$ and $1/\cdot$. The list of
trigonometric identities is endless. For our example, Vega's rule $\arctan a +
\arctan b = \arctan \frac {a + b} {1 - ab}$ seems useful. Unfortunately, this
technique quite often yields huge expressions that are difficult to deal with by
virtue of their sheer size. Also, an algebraic transformation to a polynomial problem may
simply be impossible (we suspect that this is the case for \eqref{gamma-pt}).

A second technique is based on replacing $\gamma$ with a polynomial $g$ that
dominates it, but is still smaller than $\pt$. Clearly, if there exists a $g$
such that
\begin{equation}
\forall y \in [2,2.51]^6.\; \gamma(y) \le g(y) \label{gamma-g}
\end{equation}
and
\begin{equation}
\forall y \in [2,2.51]^6.\; g(y) \le \pt, \label{g-pt}
\end{equation}
then by transitivity \eqref{gamma-pt} holds.

Such a polynomial $g$ can be obtained by replacing $\sqrt{\cdot}$, $1/\cdot$ and
$\arctan$ with polynomial approximations. We only need to ensure that we use
upper approximations for positive occurrences and lower approximations for
negative ones. Only occurrences whose arguments contain variables need to be
replaced, since e.g. $\sqrt 2$ is a (constant) polynomial itself.

In the definition of $\gamma$ the function $\arctan{}$ occurs positively, so it
is replaced by an upper approximation $\overline{\arctan}$. The term
$\frac{\sqrt{\Delta(y)}} {\asolid_i(y)}$ is first unfolded to $
{\sqrt{\Delta(y)}}~\cdot~\frac1{\asolid_i(y)}$. Both the square root and
reciprocal occur positively again here, so they can be replaced by upper
approximations $\overline\sqroot$ and $\overline\rcp$, respectively. This yields
$\overline{\arctan} (\overline\sqroot(\Delta(y)) \cdot
\overline\rcp(\asolid_i(y)))$ in all four summands. There remains only 
$\sqrt\cdot$ occurring negatively after $-\frac \doct 6$, which is to be
replaced by a lower approximation $\underline\sqroot$.

We choose the following approximations:
\begin{align*}
\overline{\arctan}(t) &\coloneq \arctan \frac{\sqrt 2}5 + \frac {25} {27}\left(t - \frac{\sqrt 2}5\right)\\
\overline\rcp(t) &\coloneq \frac 1 4 - \frac {37 t} {1600} + \frac {t^2} {1000}- \frac{13 t^3} {640000} + \frac {t^4} {6400000}\\
\underline\sqroot(t) &\coloneq 8 \sqrt 2 + \frac 3 {64 (\pi - 4 \arctan \frac{\sqrt 2}5)} (t - 128)\\
\overline\sqroot(t) &\coloneq 8 \sqrt 2 + \frac 1 {16 \sqrt 2}(t -128).
\end{align*}

These approximations are valid on the domain~\eqref{gamma-pt}. For example,
$$\forall t \in\Delta ([2,2.51]^6).\; \sqrt{t} \le \overline\sqroot(t).$$ This
can be established by elementary means, knowing that $\Delta ([2,2.51]^6)
\subseteq [128;501]$. The latter can be shown automatically by the method
outlined in the next subsection.

In summary, we arrive at the following definition of $g$:
\begin{align*}
g(y) &\coloneq 
- \frac \doct 6 \underline\sqroot (\Delta(y)) + \frac 2 3 \sum_{i=0}^3 
\overline{\arctan} (\overline\sqroot(\Delta(y)) \cdot
\overline\rcp(\asolid_i(y))).
\end{align*}
In form, it is almost identical to the definition of $\gamma$.
Our construction of $g$ therefore ensures \eqref{gamma-g}. Moreover, the
approximations were chosen (using polynomial interpolation) in a way such that
\begin{equation}
\gamma (2,2,2,2,2,2) = g (2,2,2,2,2,2) = \pt. \label{eq-gamma-g-pt}
\end{equation}
This is important, because otherwise~\eqref{g-pt} cannot hold.




\subsection{Bounding polynomials}
\label{bernstein}
In order to prove~\eqref{gamma-pt}, it remains to be shown that $g(y) \le \pt$.
This can be done with the help of Bernstein polynomials. We briefly outline the
case of a single variable $x$ here.

The $i$th Bernstein basis polynomial of order $k$ is defined as
$$\bstein^k_i(x) \coloneq {\binom{k}{i} }

x^i(1-x)^{k-i}.$$
For a polynomial $p$ and a vector $b \in \mathbb R^k$, if
$$p(x) = \sum_{i=0}^k b_i \cdot \bstein^k_i(x),$$
then $b$ is called the \emph{Bernstein representation} of $p$. In this case
$$\forall x \in [0;1].\; p(x) \le \max_i b_i.$$

This property is tremendously useful: it gives us an upper bound on $p$, namely
the largest coefficient of $p$'s Bernstein representation. By a change of
variable we can reduce any interval to $[0,1]$. The generalization to the
multivariate case is straightforward~\cite{garloff}, \cite{roland-thesis}.

In order to bound a polynomial it thus suffices to convert it into Bernstein
representation. This can be done by a matrix multiplication (the Bernstein basis
of order $k$ forms a basis of the vector space of all polynomials of degree up
to $k$). For practical purposes it is however crucial to use a more efficient
algorithm (cf. \cite{garloff}, \cite{roland-thesis}).

Note that $g$ contains irrational coefficients. This is a consequence of
requirement~\eqref{eq-gamma-g-pt} and cannot be avoided. However, we were able
to choose the approximation polynomials in a way such that the transcendental
parts can be factored out (hence the occurrence of $\pi - 4 \arctan \frac{\sqrt
  2}5$ in the definition of $\underline\sqroot$). As can be easily checked with
symbolic algebra software, the polynomial $p(y) \coloneq \sqrt 2 (g(y) - \pt)$
has rational coefficients! It can thus be converted to a Bernstein
representation without rounding, using the algorithm presented in
\cite{roland-thesis}. With this method the only divisions are by powers of 2,
which can be efficiently represented using dyadic numbers.

The polynomial $p$ consists of 12945 monomials and has total degree
18. A prototype implementation in Haskell returns $0$ as the maximum
for $p$ in about half a minute. Thus $\sqrt 2 (g(y) - \pt) \le 0$ and
$g(y) \le \pt$.
