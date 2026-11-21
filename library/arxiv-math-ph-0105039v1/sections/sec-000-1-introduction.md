---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.719
latex_coverage_ratio: 0.993
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
Since
the discovery of  the Jones polynomial~\cite{Jones85},
many knot invariants are proposed.
In  construction of these  quantum invariants, the quantum group
plays a crucial role,
and a representation of the
braid generator is derived  from  the
universal $R$-matrix ~\cite{Turae88}.
Contrary to
that the Alexander polynomial was known to be related with the
homology of the universal abelian covering,
the quantum invariants  still lack
the geometrical interpretation.


In Ref.~\citen{Kasha95}, Kashaev introduced 
the knot invariant   by
use of the finite dimensional representation of  the quantum
dilogarithm function.
He further  conjectured~\cite{Kasha96b} that the asymptotic behavior of
this invariant for a hyperbolic   knot $K$ gives  the hyperbolic volume of
the knot complement $S^3 \setminus K$.
As it is well known that the hyperbolic volume of the ideal
tetrahedron is given by the Lobachevsky function~\cite{WPThurs80Lecture,JMiln82a} which
is closely related with the dilogarithm function,
his  conjecture
may sound  natural.
Later in Ref.~\citen{MuraMura99a}
Kashaev's  knot invariant was shown to be equivalent with the colored Jones
polynomial at  a specific value, and his
conjecture is rewritten as the ``volume conjecture'';
\begin{equation}
  \label{volume_conjecture}
  \| K \|
  =
  \frac{1}{v_3}
  \lim_{N\to \infty}
  \frac{2 \, \pi}{N} \log | J_N(K) | ,
\end{equation}
where  $\| K \|$ is the Gromov norm of $S^3 \setminus K$, and
$v_3$ is the hyperbolic volume of the regular ideal tetrahedron.
The knot invariant  $J_N(K)$ is defined from the colored Jones
polynomial
$V_N(K;t)$
($N$-dimensional representation of $s\ell_2$)
by
\begin{equation*}
  J_N(K) 
  =
  V_N(K ; \mathrm{e}^{\frac{2 \, \pi \, \mathrm{i}}{N}}) .
\end{equation*}
Thus to clarify  a geometrical property of the quantum knot invariants
such as the Jones polynomial,
it is very fascinating to  reveal the 3-dimensional picture of this
invariant.
Recently some geometrical aspects for the
conjecture~\eqref{volume_conjecture}
have been proposed  in
Refs.~\citen{YYokot00b}
(see also Ref.~\cite{HMuraka00c}) based on the 3-dimensional picture
of Ref.~\citen{DThurs99a}.

In this paper we define the knot invariant
as a ``non-compact'' analogue of Kashaev's invariant, or the colored
Jones invariant.
This is based on an infinite dimensional representation of the quantum
dilogarithm function, and
both the $R$-matrix and  the invariant  are  defined in an integral form.






In our construction a    parameter $\gamma$ which corresponds to
$\pi/N$ in eq.~\eqref{volume_conjecture} is regarded as
the Planck constant $\hbar/2$, and a limit in
eq.~\eqref{volume_conjecture} is realized by the classical limit
$\gamma \to 0$.
We shall  demonstrate how the hyperbolic structure
appears in the classical limit of the non-compact Jones invariant.


This paper is organized as follows.
In \S~\ref{sec:dilog} we review the properties of the classical and
quantum dilogarithm functions.
A key is that both functions satisfy the so-called pentagon identity.
Using these properties
we   construct a solution of the Yang--Baxter equation in terms
of the quantum dilogarithm function.
With this  $R$-operator, we introduce  the knot invariant in
\S~\ref{sec:invariant}.
This invariant is given  in the integral form from the beginning.
We recall that the integral form of the quantum dilogarithm function
was used in Ref.~\citen{Kasha96b} to elucidate the asymptotic
behavior of the colored Jones polynomial.
In \S~\ref{sec:asymptotic} we show that the hyperbolic structure
naturally appears in the classical limit of  our knot invariant.
We find that
in  $\gamma\to 0$ limit
the oriented ideal tetrahedron with transverse oriented faces is
associated to  the matrix elements of the quantum dilogarithm
function.
Correspondingly the $R$-operator is identified with the oriented
octahedron, whose vertices belong to the link $L$.
This explains how the octahedron was introduced for each braiding  in
Ref.~\citen{DThurs99a}.
We can apply the saddle point method to evaluate the asymptotic
behavior of the classical limit of the knot invariant, and
we further demonstrate that the   saddle point equation for  integrals
of the knot invariant exactly coincides with the hyperbolicity
consistency condition in gluing faces.
Combining the fact that the imaginary part of the classical
dilogarithm function gives the hyperbolic volume of the ideal
tetrahedron at the critical point,
we can  conclude that the  invariant is related with the hyperbolic
volume of the knot complement


at the critical point.
In \S~\ref{sec:eight}
we show how to triangulate the knot complement in a case of the
figure-eight knot.
This method can be easily applied to other knots and links.
The last section is devoted to discussions and concluding remarks.
