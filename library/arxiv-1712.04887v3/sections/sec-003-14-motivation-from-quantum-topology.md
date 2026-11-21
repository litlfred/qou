---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-003-14-motivation-from-quantum-topology
section_title: "Motivation from quantum topology"
section_number: 1.4
pages: 6-8
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.975
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
\label{sec.motivation}

In this subsection --- which will not be used anywhere else in this paper --- we

discuss the empirical discoveries that led us to conjecture the results presented here.
A much more detailed discussion of these ideas and of the experimental results
can be found in~\cite{GZ:quantum} (Introduction, Sections~1, 5 and~9, and~Appendix).

The story has its origin in Quantum Topology and one of its most prized problems, the 
Volume Conjecture of Kashaev, which relates the Jones polynomial of a hyperbolic knot 
with hyperbolic geometry. More precisely, the Volume Conjecture~\cite{Volume} asserts 
that the Kashaev invariant $\la K \ra_N$ of a hyperbolic knot (which is equal to the
value of the $N$-th colored Jones polynomial at $e^{2 \pi i/N}$~\cite{MM}) grows
exponentially at a rate proportional to the hyperbolic volume $\Vol(K)$ of the knot:
\be
\lim_N \frac{1}{N} \log |\la K \ra| = \frac{\Vol(K)}{2\pi} \,. 
\ee
A refinement of the Volume Conjecture asserts the existence of an asymptotic expansion
\be 
\label{ArithConj2}
\la K\ra_N\;\sim\; N^{3/2}\,\Phih^K (2 \pi i/N),
\qquad \Phih^K(h)= e^{\tV(K)/h} \Phi^K(h)
\ee
to all orders in $1/N$ as $N\to\infty$, where
$\tV(K)=i \Vol(K) + \CS(K) \in \BC/4\pi^2\BZ$
is the complexified volume of $K$  
and $\Phi^K(h)$ is a power series which satisfies $\mu\delta(K)^{1/2} \Phi^K(h)
\in F_K[[h]]$ where $F_K$ is the trace field of the hyperbolic knot, $\mu$ is some 
eighth root of unity, and $\delta(K)$ is a non-zero number in $F_K$ related to the 
Ray-Singer torsion of~$K$. For instance, for the simplest hyperbolic (figure-eight) 
knot, whose trace field is $F_{4_1}=\Q(\sqrt{-3})$, the first few terms of the series 
$\Phi^{4_1}(h)$ are given by
$$ \Phi^{4_1}(h) \= \frac1{\root4\of3}\,\Bigl(1 \+ \frac{11}{72\sqrt {-3}} h  
\m \frac{697}{31104}h^2\m\frac{724351}{33592320\sqrt{-3}}h^3 
\+\cdots\Bigr) \,.
$$
In~\cite{Za:QMF}, the third author observed that if we extend the Kashaev invariant
to a function $\J^{(K)}:\Q/\Z\to\Qbar$ by Galois equivariance (i.e., by setting 
$\J^{(K)}(a/N):=\s_{-a}\bigl(\la K\ra_N\bigr)$ for $N>0$ and $(a,N)=1$), 
then~\eqref{ArithConj2} can be improved to 
\be
\label{ModConj2}
\J^K(-1/X) \;\sim\;  X^{3/2}\, \J^K(X) \, \Phih^K (2 \pi i/X)\,,
\ee
to all orders in $1/X$ as $X\to\infty$ in~$\Q$ with bounded denominator (note that 
$\J^K(X)=1$ if $X=N\in\N$), and more generally that for any $\sm abcd\in\SL(2,\Z)$ 
we have
\be
\label{ModConj3}
\J^K\Bigl(\frac{aX+b}{cX+d}\Bigr) \;\sim\;
(cX+d)^{3/2}\, \J^K(X) \,
e^{\tV(K)(X+d/c)}\,\Phi^K_{a/c}\Bigl(\frac{2\pi i}{cX+d}\Bigr)
\ee
to all orders in $1/X$ as $X\to\infty$ in~$\Q$ with bounded denominator, where 
$\Phi^K_\a(h) \in\Qbar[[h]]$ ($\a\in\Q$) is a power series depending only on $\a\in\Q/\Z$.
This conjectural modular property led to the concept 
of a \emph{quantum modular form}~\cite{Za:QMF}, and its more recent development, that 
of a \emph{holomorphic quantum modular form}~\cite{GZ:quantum, Za:HQMF}. 
Experiments for various knots and various values of~$\a$ suggested that the power
series $\Phi^K_\a$ is the product of a number $\kappa_\a\in\Qbar$ with a power series
having coefficients in
the cyclotomic extension $F_K(e^{2\pi i\a})$ of the trace field of the knot.  
The story that led to the present paper was then the striking empirical discovery that 
the quotient of~$\kappa_\a$ by~$\kappa_0$ was always the product of a root 
of unity 

and the $c$-th root of an
$S$-unit $\eps_\a^K$ in $F_K(e^{2\pi i\a})$ with $S$ independent
of $\a$, where $c$ is the denominator of $\a$, and 


 furthermore that 
this unit, which is well-defined only up to $c$th powers, transforms according to
Equation~\eqref{eq.2actions}. For example, numerical computations given
in~\cite{Za:QMF} for the $4_1$ knot and~$c=5$ suggested that $\ve_\a^K$ in this case
equals $(\z^4+1)/\z(\z-1)^2$ with
$\z=e^{2\pi i(\a-1/3)}\in F_{4_1}(e^{2\pi i\a})=\Q(e^{2\pi i/15})$.

On the other hand, it is well known that a hyperbolic knot (and more generally,
a complete, finite-volume hyperbolic 3-manifold) gives an element $\xi_K$
in the Bloch group $B(F_K)$, or equivalently of the third $K$-group $K_3(F)$,
which determines (via the regulator map) the complexified volume of~$K$,
and this led to the guess that the units appearing in the quantum modularity
conjecture might depend only on~$\xi_K$.  Moving away from hyperbolic manifolds
and of quantum topology, these observations prompted the third author to ask
the first author during an Oberwolfach meeting (in July 2011) whether he could
suggest a construction of a map $c_\z$ as in Theorem~\ref{thm.c}.
The answer was positive, but of course with no proof that the units coming from
the Kashaev invariant and the units given by $c_\z$ were connected, leading to
an initial two-author version of the current paper with an abstract saying that
we conjectured that a number that could not be defined was equal to a number
that could not be computed!  In the following years, the number of authors
increased by one and it was discovered that the asymptotic expansions of 
Nahm sums at roots of unity also involved a unit with very similar properties,
which together with Nahm's
construction of an element of the Bloch group associated canonically to any
Nahm sum suggested the existence of a map $R_\z$ as in Theorem~\ref{thm.R} as
well as of the map~$c_\z$ in algebraic $K$-theory.
The map $R_\z$ has the fortunate property of
being well-defined and computable.
Eventually we found complete constructions of both
maps, as explained in the current paper.   But the basic disclaimer of the 
old abstract remains true: the quantum modular conjecture is still open, so
that we cannot rigorously prove even the existence of the units~$\ve_\a^K$.
There is, however, a conjectural description of the power series $\Phi_\a^K$
occurring in~\eqref{ModConj3}, as given by Tudor Dimofte and the second
author~\cite{DG,DG2}, and these {\it can} be related to the map~$R_\z$, as
discussed in Section~7 of~\cite{GZ:quantum}, so in conjunction with the
extensive numerical computations of the putative units coming from the
quantum modular conjecture described in the appendix of that paper we can
conjecture with a fair degree of conviction that these numbers do indeed
always coincide.}
