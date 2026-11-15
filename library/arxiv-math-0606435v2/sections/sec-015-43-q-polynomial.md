---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-015-43-q-polynomial
section_title: "Q polynomial"
section_number: 4.3
pages: 20-26
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.984
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
We extend the scope of the previous results to the
Brandt-Lickorish-Millett-Ho polynomial. The main aim here is to prove

\begin{theo}\label{thQ}
Only finitely many non-trivial 3-braid links have given $Q$
polynomial, and none has trivial (i.e., unlink) polynomial.
\end{theo}

Note that by Kanenobu's work \cite{Kanenobu3}, again
there are finite families of arbitrary large size,
so we claim again a sort of contrary result.

While this result may be considered less relevant
that its analoga for $\Dl$ and $V$, its proof displays
the largest variety of tools necessary to apply, and 
shows how the various approaches to link invariants
(skein relations, state models and representation theory), 
which are often considered in isolation, can usefully 
complement each other. Indeed, $Q$ seems in general 
more difficult to treat than $V$. Apart from Kidwell's 
results \cite{Kidwell} for alternating links, and those
in \cite{pos} for positive \em{knots}, neither the 
non-triviality nor the finiteness property seem to have 
been known previously for any other class of links.

The proof makes use of the full extent of the study of 
Xu's form. Various additional ingredients will be necessary.
One such is J. Murakami's $Q$-$V$ formula, found in
\cite{Murakami} (by representation theory, and proved also
later by Kanenobu \cite{Kanenobu} using skein relations).
It allows to recur in many cases the problem from $Q$ to $V$.
When dealing with $V$, we use beside the previous discussion
the (Kauffman bracket based) formulas of \S\ref{Ssaq}.

In cases Murakami's formula is not helpful, we apply the
Polyak-Viro formula \eqref{pv2} for Casson's knot invariant
$v_2=\myfrac{1}{2}\Dl''(1)$,
and the following formula, (likewise skein theoretic and) due
to Kanenobu \cite{Kanenobu4}, that relates $v_2$ to $Q$.

\begin{theo}(\cite{Kanenobu4})
For a link $L$ with $n$ components $K_i$, $i=1,\dots,n$, we have
\begin{eqn}\label{Kanf}
Q_L'(-2)=3(-2)^n\sum_iv_2(K_i)+3(-2)^{n-2}\sum_{i<j}lk(K_i,K_j)^2
+(n-1)(-2)^{n-3}\,,
\end{eqn}
where $lk$ is the linking number.
\end{theo}

Using this formula, we prove first a special case of theorem
\ref{thQ}.

\begin{prop}\label{pgw}
Only finitely many (non-trivial) strongly quasi-positive 3-braid
links have given $Q$ polynomial, and none has trivial polynomial.
\end{prop}

For the case of knots, we have the following more specific statement,
that has also some independent meaning.

\begin{prop}\label{pgq}
If $K$ is a strongly quasi-positive 3-braid knot, then $v_2(K)\ge
g(K)$.
\end{prop}

Note that in \cite{pos} we proved the same inequality for a
general \em{positive} knot. Since the pretzel knots with
trivial Alexander polynomial are strongly quasi-positive, nothing
like this holds for a general strongly quasi-positive knot, though.

We need some preparations. Let us first fix a convention. We number
braid strands by 1,2,3 from left to right in the bottom of the
braid by and compose words from bottom to top. We propagate strand
number through the crossings. In particular strand( number)s may 
appear permuted in the middle or on top of the braid. To refer to the 
ordering of the strands with regard ot the local position in the braid
diagram, we speak of left, middle and right strand. So, for example, 
if strands 1 and 2 enter below a $\sg_1$ (strand 1 as left strand and
strand 2 as middle strand), then they exit above in the order 2\ 1 
(strand 2 as left strand and strand 1 as middle strand). 

Let for a (not necessarily pure, and not closed) braid word the
linking numbers of strand $i$, $j$ numbered as explained above be
the sum of the writhes of all crossings these two strands pass.
(Note that for links this differs by the additional factor 1/2,
which is not relevant, though.)

\begin{lemma}\label{lmlk}
Let $\bt$ be a strongly quasi-positive 3-braid word
(not necessarily pure, and not closed). Then the
linking numbers $l_{ij}$ between pairs $(i,j)$ of 
strands satisfy $l_{13}+l_{23}>0$, unless $\bt$ is split.
\end{lemma}

\proof The sum of writhes of crossings a strand passes
through each of $\sg_{1,2,3}$ is non-negative. So
$l_{13}+l_{23}\ge 0$. If $l_{13}+l_{23}=0$, then
strand 3 passes only from below as left or middle
strand into a $\sg_3=\sg_1^{-1}\sg_2\sg_1$. But since it
starts (at the bottom of the braid) as a rightmost 
strand, this means that is passes no crossing, so $\bt$ is split. 
\qed

We prove proposition \ref{pgq}
by induction on the length of the positive word
in $\sg_{1,2,3}$. Assume $\bt$ is written as such a word.
We can w.l.o.g. cyclically permute the indices. 

\begin{lemma}
If $\hat\bt$ is a strongly quasi-positive 3-braid, then a positive 
word $\bt$ can be chosen so that it contains a non-trivial syllable,
\em{unless} $\bt$ is a power of $[123]$. In particular, it is 
always possible if $\hat\bt$ is a knot, or a fibered link.
\end{lemma}

\proof Choose Xu's form. It is $[12]^k\bt'$, where $k\ge 0$ and $\bt'$ 
has cyclically non-decreasing indices. This word $\bt$ has a non-trivial
syllable up to cyclic permutations of the letters, unless $\bt'$
is a power of $[123]$. In this case, if $k>0$, we apply a YB relation 
at the initial $121$ in $\bt$, and are done. \qed

\proof[of proposition \ref{pgq}] Let $\hat\bt$ be a knot. 
We can w.l.o.g. now assume $\bt$ is written as a word with a 
non-trivial syllable $s$. Now we apply the skein relation
of $\Dl$ at a letter of $s$. Let $K=K,K_-,K_0$ be the skein
triple, and $\bt_{\pm,0}$ the corresponding braids. Also we can 
cyclically permute the indices in $\bt_{\pm,0}$. We choose them so 
that the strand fixed by the permutation of $\bt_0$ is number 3. We 
know from the skein relation of $\Dl$ 
that $v_2(K)-v_2(K_-)=lk(L,M)$ where $L,M$ are the components 
of $K_0$. Now that linking number is positive by lemma \ref{lmlk} 
(unless $\bt_0$ is a split braid, but this is impossible because $s$
is non-trivial). By induction on $g(K)$, the claim of proposition
\ref{pgq} follows. \qed



\proof[of proposition \reference{pgw}] We distinguish three
cases depending on the number of components of $\hat\bt$.

\begin{caselist}
\case 1 component. In this case $Q'(-2)$, by Kanenobu's formula
\eqref{Kanf},
is a multiple of Casson's invariant $v_2$. The claim we wish to 
show then is implied by the estimate in proposition \reference{pgq}.

\case 2 components. In this case Kanenobu's formula 
involves only the square of the linking number of both components 
$K,L$ of the closure link of $\bt$ and $v_2$ of the 2-string subbraid 
component $K$. Looking at Xu's normal form, we see that if $\bt$ is 
a strongly quasi-positive 3-braid, then writing $\bt$ as a word
in $\sg_{1,2,3}$, and then expanding $\sg_3=\sg_1^{-1}\sg_2\sg_1$,
we obtain a word in $\sg_{1,2}$ of some length $c$ with at most 
$c/5$ negative letters. Since thus $\bt$ has at most $c/5$ negative
crossings, it is easy to see that not both $v_2(K)$ and $lk(K,L)$
can be zero, and one grows unboundedly when $c$ grows. So we are done.

\case 3 components. In this case Kanenobu's formula \eqref{Kanf} 
reduces to the square sum of the linking number of pairs components.
Let $l_{12},l_{13},l_{23}$ be these linking numbers. Again it is 
clear that not all of $l_{12},l_{13},l_{23}=0$, and that when 
$l_{12}+l_{13}+l_{23}\ge 2c/5$ grows unboundedly, then so will
$l_{12}^2+l_{13}^2+l_{23}^2$, so again we are done.
\end{caselist}
\qed

Now we move on to settle the remaining cases in theorem \ref{thQ}.
Here the tools differ considerably. Beside the study of Xu's form,
we need the help of the following theorem, proved in \cite{ntriv}.

\begin{theorem}\label{thq}
Any $3$-braid is up to conjugacy $A$-adequate or $B$-adequate.
\end{theorem}

We proved also the following

\begin{theorem}
A $3$-braid word is $B$-adequate if and only if it is (a) a
negative word, or (b) it contains no $[121]$ as subword, and negative
entries in the Schreier vector appear isolated. (That is, in
cyclic order they are preceded and followed by a positive entry.)
\end{theorem}

Using this criterion we prove now

\begin{lemma}\label{oia}
Assume $\bt$ is strongly $\le 2$-almost positive and of exponent 
sum $e\ge 0$. Then $\bt$ is $B$-adequate.
\end{lemma}

\proof
If $\bt$ is strongly quasi-positive or almost strongly
quasi-positive, then it is of Xu's form $L^{-1}R$
where $L$ is a single letter. By direct observation
we can verify that when permuting indices cyclicly
properly and writing out $\sg_3$ in $\sg_{1,2}$, then
the resulting word has no $[121]$ subword, and negative
entries in the Schreier vector appear isolated. (In case
of $[(312)^k31-2]$, we must cancel 2 crossings first.)

If $\bt$ is 2-almost strongly quasi-positive, then then
it is of Xu's form $L^{-1}R$ where $L$ has 2 letters.
We can assume that $L=[12]$ or $L=[1^2]$, then we write down
the subword of $L^{-1}R$ consisting of the first and last
letters of $R$ and $L$ (herein $k\ge 1$):
\[
\begin{array}{ll}
[[23] \dots 33-2-1] & [[23] \dots 22-1-1] \\{}
[[23] \dots 23-2-1] & [[23] \dots 31^k2-1-1] \\{}
[[23] \dots 31^k-2-1] & [[23] \dots 33-1-1] \\{}
& [[23] \dots 23-1-1]
\end{array}
\]
(Here `[23]' means as in \S\ref{brs} that the word is to begin with
`2' or `3'.) The reductions and $B$-adequacy test are done
case-by-case. \qed

Using the formulas in \S\reference{Ssaq}, we prove

\begin{lemma}\label{yu}
If $L=\hat\bt$ is a link, which is the closure of an $A$-semiadequate 
$3$-braid $\bt$, and $V_0V_1=-1$, then $V_0V_2=1$ or $2$.
\end{lemma}

\proof By \cite{ntriv} a A-semiadequate $3$ braid is either
positive, in which case $V_1=0$, or has no $[-1-2-1]$ and
positive entries are isolated in the Schreier vector.
In \cite{ntriv} we described the words  for latter
type which have $V_1=0$. They are (up to braid relations
and cyclic letter permutations) of the form
\footnote{Note that these are exactly the 3-braids which are
reducible in the terminology of dynamic properties;
this reducibility has nothing to do, though, with the
reducibility in Markov's theorem.}
\[
[1^{-2}2^{-2}1^{-2}\dots 1^{-2}2^{-1}1^p2^{-1}]\,.
\]

Analogously to that study, we can see that if $V_0V_1=-1$,
then $\bt$ has a word which is obtained from the above type
by replacing some $1^{-2}$ by $1^{-k}$ 
for $k\ge 3$. The intertwining graph of
the $A$-state is a path (all vertices have valence 2, except two
of valence 1), so $\chi(IG)=1$. We have $\bigtriangleup
=1$ if $k=3$, and otherwise $\bigtriangleup=0$. So by
theorem \reference{T02}, we have $V_0V_2=1$ for
$k=3$, and $V_0V_2=2$ otherwise. \qed

To explain what such a property has to do with $Q$, 
now we must introduce J. Murakami's formula \cite{Murakami}.
(See also Kanenobu \cite[Theorem 2]{Kanenobu}.)

Let $i=\sqrt{-1}$, $u=\sqrt{-t}$ and $x=u+u^{-1}$. Let further
\footnote{Note that $V$ is here what is written as $J$, and not $V$, 
in \cite{Kanenobu}.} for a braid $\bt$ of exponent sum $e$,
\begin{eqn}\label{chi}
\chi(\bt,t)=i^eu^{-2e}V_{\hat\bt}(t)+u^{-e}(x^2-2)\,.
\end{eqn}

Then Murakami's formula is

\begin{theo}(J. Murakami)\label{TMF}
If $L$ is a closure of a 3-braid $\bt$ of exponent sum $e$,
then
\begin{eqn}\label{sonjo}
Q(L,x)\,=\,\chi(\bt,\sqrt{t})^2-1\,+\,\frac{2(x^2+x-1)}{x^2(x^2-3)}
(u^e+e^{-e})+\frac{-x^4-2x^3+3x^2+4x-4}{x^2(x^2-3)}\chi(\bt,t)\,.
\end{eqn}
\end{theo}

\proof[of theorem \ref{thQ}] We can w.l.o.g. (taking the mirror image)
assume that $e\ge 0$, and (excluding trivial to check special cases)
that $\chi\le 0$. Clearing denominators and absolute terms in
\eqref{sonjo}, we find
\begin{eqnarray}
\label{Q1} Q_1(L,x):=x^2(x^2-3)(Q(L,x)+1) & = &
\bigl[ i^e(-t)^{-e}V(t)+(-t)^{-e/2}(-t-\frac{1}{t}) \bigr]
\cdot (-x^4-2x^3+3x^2+4x-4) \\
\nonumber & &  + \bigl[ i^e(-t)^{-e/2}V(-\sqrt{-t})+(-t)^{-e/4}x \bigr]^2
\cdot x^2(x^2-3) \\
\nonumber & & +2(x^2+x-1)(\sqrt{-t}^e+\sqrt{-t}^{-e})\,.
\end{eqnarray}

Rearranging, we need to show that the sum of the following 5
expressions,
regarded as a polynomial in $t^{\pm 1/2}$, has either arbitrarily
small minimal degree or arbitrarily large maximal degree.
(Note that by \eqref{sonjo} this sum must be self-conjugate in 
$t$ up to coefficient signs, which is not at all evident directly.)

\begin{eqnarray*}
T'_1 & = & i^e(-t)^{-e}V(t)\cdot (-x^4-2x^3+3x^2+4x-4) \\
T'_2 & = & t^{-e}\bigl[V(-\sqrt{-t})\bigr]^2\cdot x^2(x^2-3) \\
T'_3 & = & 2i^e(-t)^{-3e/4}V(-\sqrt{-t})x^3(x^2-3) \\
T'_4 & = & (-t)^{-e/2}\bigl[(x^2-2)(-x^4-2x^3+3x^2+4x-4)+x^4(x^2-3)+2(x^2+x-1)
 \bigr] \\
T'_5 & = & (-t)^{e/2}\bigl[2(x^2+x-1) \bigr] 
\end{eqnarray*}

Switching $-t\to t$ to simplify the expressions, and regrouping terms, 
we have
\begin{eqnarray*}
T_1 & = & i^et^{-e}V(-t)\cdot (-1\ -2\ -1\ -2\ [-4]\ -2\ -1\ -2\ -1) \\
T_2 & = & (-t)^{-e}\bigl[V(-\sqrt{t})\bigr]^2\cdot (1\ 0\ 1\ 0\ [0]\ 0\ 1\ 0\ 1) \\
T_3 & = & 2i^et^{-3e/4}V(-\sqrt{t})\cdot (1\ 0\ 2\ 0\ 1\ [0]\ 1\ 0\ 2\ 0\ 1) \\
T_4 & = & t^{-e/2}\bigl[-2(x-1)(x^2-3)(x^2-1) \bigr] \\
T_5 & = & t^{e/2}\bigl[2(x^2+x-1) \bigr] 
\end{eqnarray*}
Now $u=t^{1/2}$ and $x=t^{1/2}+t^{-1/2}$. The last factors for $T_
{1,2,3}$ are given as a list of coefficients, with the absolute term
put in brackets. Note that these are polynomials in $\sqrt{t}$, so for
example, the first two polynomials have degree $2$ in $t$.

Since we are concerned with cancellations of the leading and trailing
coefficients of $T_k$, let us compile their minimal $m_k=\md_tT_k$ and
maximal degrees $M_k=\Md_tT_k$ (note that by taking degrees w.r.t.
$t$, and not $\sqrt{t}$, the $m_k$, $M_k$ are only half-integers).
\[
\begin{array}{c|c|c}
\raisebox{-1em}{\ry{2.3em}} k & m_k & M_k \\
\hline
\raisebox{-1em}{\ry{2.5em}}1 & \md V-e-2 & \Md V-e+2 \\[2mm]
2 & \md V-e-2 & \Md V-e+2 \\[2mm]
3 & -\ffrac{3e}{4}+\ffrac{\md V}{2}-\ffrac{5}{2} & -\ffrac{3e}{4}+
    \ffrac{\Md V}{2}+\ffrac{5}{2}\\[2mm]
4 & -\frac{e}{2}-\frac{5}{2} & -\frac{e}{2}+\frac{5}{2} \\[2mm]
5 & \frac{e}{2}-1 & \frac{e}{2}+1\raisebox{-1em}{\ry{1.7em}}
\end{array}
\]
(Here again $\md V=\md_t V(t)$ is a half-integer, and similarly
$\Md V$.)

Our aim will be to determine what of the $M_k$ is the largest, and 
to show that the coefficients of the contributing $T_k$ do not cancel.
An important case where we exclude (problematic) cancellation is

\begin{lemma}\label{lmcan}
Assume that 
\begin{eqnarray}
\label{GG} M_1=M_2 & \ge & M_k+3/2\quad\mbox{ and } \\
\label{gg} m_1=m_2 & \le & m_k-3/2
\end{eqnarray}
for $k=3,4,5$.
Then $\Md_t Q_1(L,x)\ge M_1-1$. (Here $Q_1(L,x)$ refers to \eqref{Q1}.)
If $L$ the closure of a 3-braid which is $A$-adequate resp. $B$-adequate
then assuming \eqref{gg} resp.\ \eqref{GG} alone is sufficient.
\end{lemma}

\proof By theorem \ref{thq}, $L$ is the closure of a 3-braid $\bt$ which 
is either $A$-adequate or $B$-adequate. We consider the $B$-adequate case 
and show that $M_1=M_2\ge M_k+3/2$ implies $\Md_t Q_1(L,x)\ge M_1-1$.
If $\bt$ is $A$-adequate, we obtain similarly $\md_t Q_1(L,x)\le 
m_1+1$, and the result follows by the (anti)symmetry of $Q_1$.

Now if $M_1=M_2\ge M_k+3/2$, the last three coefficients of $M_{1,2}$
are not cancelled from other $M_k$ (remember these are polynomials
in $\sqrt{t}$, and coefficients are meant for such polynomials), 
so it is enough to show that they do not (completely) cancel 
among each other. Now a look at the formulas for $T_{1,2}$ shows
that if these three coefficients are all to cancel, then (apart from
proper sign coincidences) we must have $\bar V_1\bar V_0=-1$ and 
$\bar V_2=0$. (Take also into account the switch $-t\to t$.)
However, this situation was ruled out by lemma \ref{yu}. \qed

We assumed $e\ge 0$; we also excluded the case $e=3-\chi$ of
strongly quasi-positive braids. To apply the lemma, we need to
establish \eqref{gg} and/or \eqref{GG}. For this we use now
lemma \reference{lemma_}.

Clearly, a strongly almost quasi-negative braid should not 
be considered for $e\ge 0$; the almost quasi-positive braid
require a small extra argument, which is given below. Now
\begin{eqn}\label{hj}
\Md V-e\,=\,\frac{1-\chi}{2}+1\,\ge\,\frac{e}{2}+1\,,
\end{eqn}
so $M_3\ge M_4$, and we can discard $M_4$. Also from \eqref{hj}
we obtain
\[
M_1-M_5-1=\Md V-\frac{3e}{2}\ge 1\,,
\]
so $M_1>M_5+1$, and can neglect $M_5$. Similarly, if
$\bt$ is not almost strongly quasi-positive, we have with 
\eqref{two_} and $\md V<e/2$ that
\begin{eqn}\label{mmm}
m_3< m_4<m_5\,,
\end{eqn}
so $m_{4,5}$ are also irrelevant.

So we need to deal only with $m_k,M_k$ for $k\le 3$. Moreover, we 
see from \eqref{one_} that $M_1\ge (1-\chi)/2+3$. So whenever we can 
apply lemma \ref{lmcan}, we have for $\chi\le 0$ that $\Md Q_1\ge 
M_1-1>2$, so $\Md_z Q>0$, and $Q$ is not an unlink 
polynomial. Moreover, we have for a sequence of links
from $\chi\to -\infty$ also $\Md M_1\to \infty$, so
$\Md Q\to \infty$, and a given (even just degree of a)
$Q$ polynomial occurs only finitely many times, as desired.
A similar argument applies if we use \eqref{two_}.

To apply lemma \ref{lmcan}, we need to check $M_3<M_1-1$ and $m_3>m_1+
1$. Note that if $\bt$ is almost strongly quasi-positive, then \eqref
{two_} may not hold. So may not be able to apply lemma \ref{lmcan}
directly. However, we remedied this by showing in lemma \ref{oia}
that $\bt$ is $B$-adequate. Then \eqref{one_} holds, and it is enough
to use $M_3<M_1-1$ (the condition \eqref{mmm} becomes also irrelevant).

Now using \eqref{one_} and \eqref{two_}
\begin{eqnarray}
\nonumber
m_1-m_3+1 & = & \md V -e -2 +\frac{3e}{4}-\frac{\md V}{2}+\frac{5}{2}+1
\,=\,\frac{\md V}{2}-\frac{e}{4}+\frac{3}{2} \\
\nonumber
& = & \frac{e}{2}-\frac{1-\chi}{4}-\frac{1}{2}-\frac{e}{4}+\frac{3}{2}\,=\,
\frac{e}{4}-\frac{1-\chi}{4}+1\,, \\
\label{iua}
M_1-M_3-1 & = & \frac{\Md V}{2}-\frac{e}{4}-\frac{3}{2} \\
\nonumber
& = & \frac{e}{2}+\frac{1-\chi}{4}+\frac{1}{2}-\frac{e}{4}-\frac{3}{2}\,=\,
      \frac{1-\chi}{4}+\frac{e}{4}-1\,.
\end{eqnarray}

Then \eqref{GG} becomes equivalent to
\[
\frac{1-\chi}{4}+\frac{e}{4}>1\,.
\]
So, assuming $\chi\le 0$ and $e\le 1-\chi$, for \eqref{GG} 
we are left to consider only $(e,\chi)=(0,-1)$, $(0,-3)$,
$(1,0)$, $(1,-2)$, or $(2,-1)$, which are trivial cases to check. 

For \eqref{gg} we must deal with $A$-adequate but not $B$-adequate
braids with $e\ge -3-\chi$, i.e. $\le 3$-almost strongly
quasi-positive braids. For $\le 2$-almost strongly
quasi-positive braids we can use lemma \reference{oia}.
While one may extend the argument there to $3$-almost strongly
quasi-positive braids, it would require a longer
case-by-case analysis. We provide instead a different argument.

We try to modify the argument for proposition \reference{pgw}.
In case $\hat\bt$ is a link of 2 or 3 components, we can argue again
as there, and are left with the cases $e=0,1$ of $6$ and $7$ bands,
which are easy to deal with.

So assume $\hat\bt$ is a knot.
Now from \eqref{iua}, we have $m_3=m_1+1$, so if still some of the
first two coefficients of $T_1$, $T_2$ do not cancel, we have
$\md_t Q_1\le m_1+\myfrac{1}{2}$, and are done.
Otherwise again $V_1V_0=-1$. So by the proof of lemma \reference{yu},
\[
\bt=[1^{-k}2^{-2}1^{-2}\dots 1^{-2}2^{-1}1^l2^{-1}]\,,
\]
with $k\ge 3$ and $l\ge 1$. Since $\hat\bt$ is a knot, $k$ and $l$
are easily observed to be odd. Now a $\le 3$-almost positive
word in Xu's form can be chosen, when written out as a word in
$\sg_{1,2}$ of $c$ letters, to have $c_-\le c/5+3$ negative
letters/crossings. If we reduce the word by cancelling
crossings, this inequality remains true.

We estimate the Casson invariant $v_2$ of $\hat\bt$ using the Gau\ss{}
diagram formula of Polyak-Viro \eqref{pv2}. Let us put the
basepoint right after the group of $l$ positive crossings (which
of either strands is immaterial). 

Now $l$ is odd and the $l$ positive crossings are pairwise linked,
so their contribution to the Gau\ss{} diagram sum \eqref{pv2} is,
independently on the location of the basepoint, equal to $v_2(T_{2,l})
=\ffrac{l^2-1}{8}$, where $T_{2,l}$ is the $(2,l)$-torus knot. The
analogous claim is true for the group of $k$ negative crossings.

If some of the positive crossings is linked with a negative crossing,
it must be a negative crossing of a $\sg_2^{-1}$. Now by our choice
of basepoint, in
each syllable $\sg_2^{-2}$ only one of the two crossings gives a pair
that contributes to \eqref{pv2}, and the contribution is always
$-1/2$. Putting this together, we have
\begin{eqn}\label{oiz}
v_2\,\ge\,\frac{l^2-1}{8}+\frac{k^2-1}{8}-\frac{c_--k+2}{4}\cdot l
\cdot \frac{1}{2}\,.
\end{eqn}
Assuming $c\ge 10$ (the other cases are checked directly), we have
\[
l\,\ge\frac{4c}{5}-3\,\ge\,\frac{c}{5}+3\,\ge\,c_-=c-l\,.
\]
So the r.h.s. in \eqref{oiz} is minimized for $l\,\ge\ffrac{4c}{5}-3$
when putting $l=\ffrac{4c}{5}-3$. Then we have, with $k\ge 3$ and
$c_-=c-l$, the estimate
\[
v_2\,\ge\,\frac{3c^2}{50}-\frac{29c}{40}+\frac{11}{4}\,,
\]
which is positive for $c\ge 10$, and grows when $c\to \infty$. 

With this theorem \ref{thQ} is proved. \qed

\begin{rem}
It is interesting whether $\Md Q\to\infty$ also for the strongly 
quasi-positive braids, but in Murakami's formula massive cancellations 
become possible and $Q_1$ cannot be easily controlled.
At least one can prove using theorem \ref{thq} and
some results of Thistlethwaite in \cite{Thistle} that
there are only finitely many 3-braid links with given
$\Md_zF$, where $F$ is the Kauffman polynomial.
\end{rem}
