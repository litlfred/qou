---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-004-3-formalizing-the-ordinary-mathematics
section_title: "Formalizing the ordinary mathematics"
section_number: 3
pages: 7-10
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.985
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
\label{sec:ordinary}

This section describes some of the
work on formalizing Euclidean space and measure theory, and the development of
further proof automation, which should be useful in this endeavor.

The computer code in Flyspeck has so far received the lion's share of the
formal effort. This is entirely reasonable since there are, or at least were,
real questions about the feasibility of reproducing these results in a formal
way. However, the Flyspeck proof includes a large amount of `ordinary'
mathematics, which also needs to be formalized. Here we are on fairly safe
ground in principle, because by now we understand the formalization of
mainstream mathematics quite well~\cite{wiedijk-17}. It is safe to predict that
this formalization can be done, and we can even hope for a reasonably accurate
estimate of the effort involved. Nevertheless, the formalization is certainly
non-trivial and will require considerable work.


\subsection{Formalizing Euclidean space}

Much of our work has been devoted to developing a solid general theory of
Euclidean space $\real^N$ \cite{harrison-euclidean}. For Flyspeck, we
invariably just need the special case $\real^3$. While some concepts, e.g.
vector cross products, are specific to $\real^3$, most of the theory has been
developed for general $\real^N$ so as to be more widely applicable. The theorem
prover HOL Light \cite{harrison-demo} is based on a logic without dependent
types, but we can still encode the index $N$ as a type (roughly, an arbitrary
indexing type of size $N$). This means that theorems about specific sizes like
$3$ really are just type instantiations of theorems for general $N$ stated with
polymorphic type variables. The theory contains the following:

\begin{itemize}

\item Basic properties of vectors in $\real^N$, linear operators and matrices,
dimensions of vector subspaces and other bits of linear algebra. For example,
the following is a formal statement of the theorem that a square matrix $A'$ is
a left inverse to another one $A$ iff it is a right inverse. Note that the
double use of the same type variable $N$ constrains the theorem to square
matrices:

\begin{\sz}
\begin{alltt}
|- \(\forall\)A:real^N^N A':real^N^N. (A ** A' = mat 1) \(\Iff\) (A' ** A = mat 1)
\end{alltt}
\end{\sz}

\item Metric and topological notions like distances, open sets, closure,
compactness and paths. Some of these are very general, others are more specific
to Euclidean space. Some results include the Heine-Borel theorem, the Banach
fixed-point theorem and Brouwer's fixed-point theorem. The following is a
formal statement that continuous functions preserve connectedness.

\begin{\sz}
\begin{alltt}
|-  \(\forall\)f:real^M->real^N s. f continuous_on s \(\And\) connected s 
         \(\Imp\) connected(IMAGE f s)
\end{alltt}
\end{\sz}

\item Properties of convex sets, convex hulls, cones etc. Results include
Helly's theorem, Carath\'eodory's theorem, and various classic results about
separating and supporting hyperplanes. The following states a simpler but not
entirely trivial result that convex hulls preserve compactness.

\begin{\sz}\begin{alltt}
|- \(\forall\)s:real^N->bool. compact s \(\Imp\) compact(convex hull s)
\end{alltt}\end{\sz}

\item Sequences and series of vectors and uniform convergence, Fr\'echet
derivatives and their properties, up to various forms of the inverse function
theorem, as well as specific 1-dimensional theorems like Rolle's theorem and
the Mean Value Theorem. Here is the formal statement of the chain rule for
Fr\'echet derivatives.

\begin{\sz}\begin{alltt}
|- \(\forall\)f:real^M->real^N g:real^N->real^P f' g'.
        (f has_derivative f') (at x) \(\And\)
        (g has_derivative g') (at (f x))
        \(\Imp\) ((g o f) has_derivative (g' o f')) (at x)
\end{alltt}\end{\sz}

\end{itemize}


\subsection{Formalizing measure theory}

Although the basic Euclidean theory is an important foundation, and many of the
concepts like `convex hull' are used extensively in the Flyspeck mathematics,
perhaps the most important thing to formalize is the concept of volume.

We define integrals of general vector-valued functions over subsets of
$\real^N$, using the Kurzweil-Henstock gauge integral definition. We develop
all the usual properties such as additivity and the key monotone and dominated
convergence theorems. We also develop a theory of {\em absolutely} integrable
functions, where both $f$ and $|f|$ are gauge integrable; this is known to
coincide with the Lebesgue integral. Here is a formal statement of the simple
theorem that integration preserves linear scaling:

\begin{\sz}
\begin{alltt}
|- \(\forall\)f:real^M->real^N y s h:real^N->real^P.
        (f has_integral y) s \(\And\) linear h \(\Imp\) ((h o f) has_integral h(y)) s
\end{alltt}
\end{\sz}

Using this integral applied to characteristic functions, we develop a theory of
(Lebesgue) measure, which of course gives volume in the 3-dimensional case. The
specific notion `measure zero' is formalized as {\tt negligible}, and we also
have a general notion of a set having a finite measure, and a function {\tt
measure} to return that measure when it exists. For example, this is the basic
additivity theorem:

\begin{\sz}
\begin{alltt}
|- \(\forall\)s t. measurable s \(\And\) measurable t \(\And\) DISJOINT s t
         \(\Imp\) measure(s UNION t) = measure s + measure t
\end{alltt}
\end{\sz}

We have proved that various `well-behaved' sets such as bounded convex ones and
compact ones, or more generally those with negligible frontier (boundary) are
measurable, e.g.

\begin{\sz}
\begin{alltt}
|- \(\forall\)s:real^N->bool. bounded s \(\And\) negligible(frontier s) \(\Imp\) measurable s
\end{alltt}
\end{\sz}

The main lack at the moment is a set of results for actually computing the
measures of specific sets, as needed for Flyspeck. We can evaluate most basic
1-dimensional integrals by appealing to the Fundamental Theorem of Calculus,
but we need to enhance the theory of integration with stronger Fubini-type
results so that we can evaluate multiple integrals by iterated one-dimensional
integrals. This work is in progress at the time of writing.


\subsection{Enhanced automation}

Using coordinates, many non-trivial geometric statements in $\real^3$, or other
Euclidean spaces of specific finite dimension, can be reduced purely to the
elementary theory of reals. This is known to be decidable using quantifier
elimination \cite{tarski-decision,collins,hormander-pdo2}. However, in practice
this is often problematic because quantifier elimination for nonlinear formulas
is inefficient. The problem is particularly severe if we want to have any kind
of {\em formal} proof, as we do in Flyspeck, since producing such a proof
induces further slowdowns \cite{mahboubi-hormander}, \cite{mclaughlin-harrison}. With
this in mind, we have explored a different approach to the case of purely
universally quantified formulas \cite{harrison-sos}, based on ideas of Parrilo
\cite{parrilo-semidefinite}. This involves reducing the initial problem to
semidefinite programming, solving the SDP problem using an external tool and
reconstructing a `sum-of-squares' (SOS) certificate that can easily be formally
checked.

For example, suppose we wish to verify that if a quadratic equation $a x^2 + b
x + c = 0$ has a real root, then $b^2 \geq 4 a c$. Using the SDP solver we find
an algebraic certificate $b^2 - 4 a c = (2 a x + b)^2 - 4 a (a x^2 + b x + c)$,
from which the required fact follows easily: $(2 a x + b)^2 \geq 0$ because it
is a square, and $4 a (a x^2 + b x + c) = 0$ because $x$ is a root, and so we
deduce $b^2 - 4 a c \geq 0$. This method seems very useful for automating
routine nonlinear reasoning in a way that is easy and quick to formally verify,
so that we don't have to rely on the correctness of a complicated program. It
is even capable of solving the coordinate forms of some of the simpler Flyspeck
inequalities directly, though it seems unlikely to be competitive with
customized nonlinear optimization methods as described in Section~\ref{sec:zumkeller}. For
example, one simple Flyspeck inequality is the following, which after being
reduced to a real problem with 9 variables (three coordinates for each point)
is solved by SOS in a second:
$$ \|u - v\| \geq 2 \,\And\, \|u - w\| \geq 2 \,\And\, \|v - w\| \geq 2 \,\And\,
   \|u - v\| < \sqrt{8}
   \Imp \|w - (u + v)/2\| > \|u - v\|/2.
$$

A quite different approach to geometric theorem proving is to work in the
setting of a general real vector space or normed real vector space. In this
case, other decision methods are available \cite{solovay-jointpaper}. In
particular, one of these decision procedures that we have implemented in HOL
Light can sometimes handle simple forms of spatial reasoning in a purely
`linear' way, and so be much more efficient than the direct reduction to
coordinates, even if we do in fact have a specific dimension in mind. One
real example from formalizing complex analysis is the following in $\real^2$:
$$ |\|w - z\| - r| = d \And \|u - w\| < d/2 \And \|x - z\| = r
   \Imp d/2 \leq \|x - u\|.
$$
