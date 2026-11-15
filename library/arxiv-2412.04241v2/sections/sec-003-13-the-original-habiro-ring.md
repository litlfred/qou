---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-003-13-the-original-habiro-ring
section_title: "The original Habiro ring"
section_number: 1.3
pages: 4-6
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.976
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.habZ}
The Habiro ring, given by the remarkably short definition~\cite{Habiro:completion}
\be
\label{habdefZ}
\calH \;:=\; \varprojlim_n \;\BZ[q]/(q;q)_n\BZ[q]
\ee
(where $(q;q)_n=(1-q) \dots (1-q^n)$ is the $q$-Pochhammer symbol),
originated in Quantum Topology as a natural home for quantum invariants of knots
and 3-manifolds such as the Kashaev invariant of a knot~\cite{HuL} or the
Witten-Reshetikhin-Turaev
invariant of an integer homology 3-sphere~\cite{Habiro:WRT}. A detailed discussion
of this ring is given in the recent work~\cite{GL:skein}. 

Let us recall some basic properties of $\calH$ whose proofs can be found
in Habiro~\cite{Habiro:completion}. From its very definition, it follows that
it consists of elements of the form
\be
\label{eq:elts.hab}
f(q)\=\sum_{n=0}^\infty P_{n+1}(q) (q;q)_{n}, \qquad P_{n}(q) \inn \BZ[q]\,.
\ee
(The shift of index by $1$ will be very convenient in Section~\ref{sec.hab} and
reflect multiplicative properties of $n$.)
This makes it easy to construct elements of $\calH$. In fact, those quantum
invariants of knots and three-manifolds often arise as expressions of this form.
An example coming from the Kashaev invariant of the trefoil ($3_1$) knot is given by
~\cite[Eqn.(4.7)]{K94}
\be
\label{eq:KZ}
f_{3_1}(q) \= \sum_{n=0}^{\infty}(q;q)_{n}\inn\calH\,.
\ee
This particular element of $\calH$ was studied years later by Kontsevich and Zagier
(cf.~\cite{Za:strange}), without knowing its topological provenance, from the point
of view of its modularity properties (with respect to $\tau$, where $q=e^{2\pi i\tau}$).

A different property of the Habiro ring will play the central role in this paper.
Observe that if $q=\z_m$
is a primitive $m$-th root of unity, then $(q;q)_n=0$ for all $m >n$; thus an
element $f(q) \in \calH$ can be evaluated at $q=\z_m$ and the result is an element
of $\BZ[\z_m]$. More generally, when $q=\z_m+x$, we have
$(q;q)_n \in x^{\lfloor{n/m\rfloor}}\BZ[\z_m][x]$.
This implies that if $f(q)$ is an element of the Habiro ring, then
$f(\z_m+x) \in \BZ[\z_m][\![x]\!]$, giving rise to a ring homomorphism 
$\iota_m: \calH \to \BZ[\z_m][\![x]\!]$. Putting these homomorphisms together,
we obtain a map 
\be
\label{iota}
\iota: \calH \to \prod_{m\geq1}\BZ[\z_m][\![x]\!]\,,
\quad\text{such that}\quad
\iota(f) \= (f_m(x))_{m \geq 1}\,,
\qquad f_m(x)\;:=\;f(\z_m+x) \,,
\ee
where $\z_m$ for each $m$ is a fixed primitive $m$-th root of unity. We will
always suppose that the collection $(\z_m)$ is a compatible collection of roots
of unity of order $m$, that is a collection satisfying
\be
\label{zmdef}
\z_{mm'} \=\z_m\z_{m'}, \qquad (m,m')\=1, \qquad
(\z_{p^r})^p \=\z_{p^{r-1}}
\ee
for all positive integers $m$ and $m'$, primes $p$ and positive integers $r$.
For example, one can think of $\z_m=\exp(2\pi i\sum_{p\text{ prime}}p^{-v_{p}(m)})$,
with $v_p(m)$ being the $p$-adic valuation of $m$. 
We note that our choice of compatible collection differs from the traditional
choice $\omega_m=e^{2\pi i/m}$, which does not satisfy~\eqref{zmdef}, but instead
satisfies $\omega_{mm'}^m=\omega_{m'}$. However, our choice satisfies the important
property that $v_p(\z_{pm}-\z_m)>0$ for all positive integers $m$ and all
primes~$p$, and this will be more convenient for us.

For a ring $R$, the map $\iota$ motivates the notion of Galois invariant
$R$-valued ``functions near roots of unity''. By this, we mean elements of the ring 
\be
\label{PR}
\calP_{R}
\=
\Big(\prod_{\z\in\mu_{\infty}} R[\z]
\llbracket x\rrbracket\Big)^{\mathrm{Gal}(\BQ^{\mathrm{ab}}/\BQ)}
\;\cong\; \prod_{m\geq 1} R[\z_m]\llbracket x\rrbracket\,.
\ee
(Here the $f_m$ suffice to expand $F(q)$
around any root of unity, and not just around our distinguished collection of
roots of unity, using Galois invariance.)
We will denote a typical element of $\calP_R$ by $f(q)=(f_m(x))$, where $q=\z_m+x$,
rather than the more cumbersome $(f_m(x))_{m \geq 1}$.
We see that equation~\eqref{iota} now
gives a map $\iota:\calH\to\calP_\BZ$. Note that $f_m(x)$ are formal series with
no convergence properties assumed. In fact, in examples where $R\subseteq\BC$
coming from perturbative knot invariants, the associated series
will be factorially divergent series over the complex numbers, whereas at the same
time they are always $p$-adically convergent on a disc of radius $p^{-p/((p-1)(p-2))}$,
as follows from~\cite[Thm.9.1, Thm.9.2]{GZ:kashaev}.
The series $f_m(x)$ are related to ``functions near $\BQ$'' defined in the
previous work~\cite{GZ:kashaev} and more specifically the series $\Phi_{\alpha}(h)$,
where $\z_m+x=e^{2\pi i\alpha-h/m}$ and $\alpha \in \BQ$.

In~\cite{Habiro:completion} Habiro proved that the map~\eqref{iota} (and in fact,
each of its factors $\iota_m:\calH_\BZ\rightarrow\BZ[\z_m][\![x]\!]$)
is injective and that its image consists of the collection of power series
$f_m(x)=(\iota_m f)(x)$ that arithmetically ``glue'', generalising earlier
work of Ohtsuki~\cite{Ohtsuki:poly}. Let us explain how gluing works. 
The map~\eqref{iota} satisfies the formal substitution property
\be
\label{glue0}
f_m(x + \z_{pm} - \z_m) \= f_{pm}(x) 
\ee
for all positive integers $m$ and all prime numbers $p$. The only issue is that this
equation requires one to re-expand the left hand side, which is a power series in $x$,
after shifting $x$ to $x + \z_{pm} -\z_m$. This is possible using the binomial
theorem on $x$ and $\z_{pm}-\z_m$ if the shift
$\z_{pm} -\z_m$ is \emph{small}, and indeed it is in the completion
$\BZ[\z_{pm}]^\wedge_p$ of $\BZ[\z_{pm}]$, since $\z_{pm} -\z_m$ has positive
$p$-valuation. 
Here $R^{\wedge}_p=\varprojlim_n R/(p^n)$, which is isomorphic to $R\otimes \BZ_p$ and
will often be denoted simply by $R_p$, denotes the $p$-completion
of a ring $R$. Then, equation~\eqref{glue0} holds as an identity in the ring
$\BZ[\z_{pm}]^\wedge_p[\![x]\!]$, and this compatibility property is what we meant
by ``gluing''.

Summarising, an element $f(q)$ of the Habiro ring can be identified with a
collection of power series $(f_m(x))_{m \geq 1} \in \prod_{m \geq 1} \BZ[\z_m][\![x]\!]$
that satisfy the gluing property~\eqref{glue0} for all primes~$p$.

The gluing property implies
that the entire collection $(f_m(x))_{m \geq 1}$ is uniquely determined by any one
of its coordinate functions $f_m(x)$, indeed in many different ways, which of
course are consistent with each other. For instance $f_6(x)$ can be determined from
$f_1(x)$ via the chain $f_1(x) \to f_3(x)=f_1(x+\z_3-1) \to f_6(x)=f_3(x+\z_6-\z_3)$ 
or via the chain $f_1(x) \to f_2(x)=f_1(x+\z_2-1) \to f_6(x)=f_2(x+\z_6-\z_2)$:
\be
\begin{tiny}
\begin{aligned}
\begin{tikzpicture}
\draw (0,1) node (p1) {$f_1(x)$};
\draw (-3,0) node (p2) {$f_3(x) = f_1(x+\z_3-1)$};
\draw (3,0) node (p3) {$f_1(x+\z_2-1) = f_2(x)$};
\draw (0,-1) node (p4) {$f_3(x+\z_6-\z_3) = f_6(x) = f_2(x+\z_6-\z_2)$};
\draw[->] (p1) -- (p2);
\draw[->] (p1) -- (p3);
\draw[->] (p2) -- (p4);
\draw[->] (p3) -- (p4);
\end{tikzpicture}
\end{aligned}\,.
\end{tiny}
\ee










Notice, however, that the equalities here hold in different completions.
We can phrase this gluing using the

language of
$p$-adic power series and their corresponding functions.  
Namely, an element of the Habiro ring consists of a collection of series
$f_m(x) \in \BZ[\z_m][\![x]\!]$ that satisfy the following property. For every
prime $p$, $f_m(x)$ is convergent on the open disc $|x|_p < 1$ that contains
$\z_{pm} -\z_m$, and its re-expansion $f_m(x+\z_{pm} -\z_{m})$, which is therefore
defined but a~priori has potentially transcendental coefficients in $\BZ_p[\z_{pm}]$,
has algebraic coefficients (in fact, in $\BZ[\z_{pm}]$) and agrees with $f_{pm}(x)$.
In other words, for each fixed prime $p$, the
collection of functions $(f_m(x))$ can be used to define a single $p$-adic
analytic function on the \emph{disconnected} domain 
$\{q\in\BC_p\;|\;|q|_p=1\}$, which is the union of the (not all distinct) open unit
discs centred at roots of unity.
(Of course this set is totally disconnected anyway in the $p$-adic topology,
but here we mean that no two of the discs in question are $p$-adically close, so that
the analytic functions on them cannot
be continued
from one to the other.)
The remarkable fact is that, given these series come from
something global, this ``disconnectedness'' disappears once
we start varying the prime $p$, in the sense that the small
neighbourhoods of any two roots of unity can be connected by neighbourhoods
overlapping with respect to varying $p$-adic metrics.
It is this property that makes the Habiro ring work.
