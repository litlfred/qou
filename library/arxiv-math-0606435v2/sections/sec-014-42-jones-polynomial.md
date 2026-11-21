---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-014-42-jones-polynomial
section_title: "Jones polynomial"
section_number: 4.2
pages: 17-20
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.863
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The control of the Jones polynomial on 3-braid links was the
object of main attention in \cite{Birman}. We can accomplish
this with a similar argument to $\Dl$. The result we obtain
can be conveniently described in our setting and is as follows:

\begin{theorem}\label{Hh}
Let $L$ be a non-split 3-braid link, and $L=\hat\bt$ with $\bt\in
B_3$. Then
\begin{eqn}\label{g}
\spn V(L)\,\le\,4-\chi(L)\,.
\end{eqn}
Equality holds if and only if $L$ is strongly quasi-signed (i.e.
-positive or -negative, or equivalently $|[\bt]|=3-\chi(L)$), and
not fibered. More specifically, the following holds:
\def\labelenumi{\theenumi)}
\begin{enumerate}
\item If $L$ is strongly quasi-positive, then 
$\ds\quad
\md V\,=\,\frac{1-\chi}{2}\quad\mbox{and}\quad\mc V\,=\,\pm 1\,.
$\\
Analogously, if $L$ is strongly quasi-negative, then
$\ds\quad
\Md V\,=\,\frac{\chi-1}{2}\quad\mbox{and}\quad\Mc V\,=\,\pm 1$\,.
\item If $L$ is strongly quasi-positive and fibered, then
$\spn V(L)\,\le\,3-\chi(L)$\,.
If $L$ is strongly quasi-positive and not fibered, then \eqref{g}
is an equality and $\Mc V\,=\,\pm 1$. (The properties for strongly
quasi-negative are analogous.)
\item If $L$ is not strongly quasi-signed and $|[\bt]|<1-\chi(L)$,
then 
\[
\mc V(L)\,=\,\pm 1\,, \quad\Mc V(L)\,=\,\pm 1\quad\mbox{and}\quad
\spn V(L)\,=\,3-\chi(L)\,.
\]
\item If $L$ is not strongly quasi-signed and $[\bt]=1-\chi(L)$, then
\[
\Mc V(L)\,=\,\pm 1\quad\mbox{and}\quad
\Md V(L)\,=\,\frac{5}{2}-\frac{3}{2}\chi(L)\,.
\]
Moreover, $\md V\ge \ds\frac{-1-\chi}{2}$, and if equality holds,
then $\mc V=\pm 2$. (The case $[\bt]=\chi(L)-1$ is analogous.)
\end{enumerate}
\end{theorem}

Apart from solving Birman's problem how to determine 3-braids
with given Jones polynomial, theorem \ref{Hh} easily implies that
no non-trivial 3-braid link has trivial (i.e. unlink) polynomial. We
defer the discussion of the non-triviality of the Jones polynomial
to \cite{ntriv}, where we work in the much more general context of
semiadequate links. In that paper we will show that semiadequate
links have non-trivial Jones polynomial. This result in fact motivated
theorem \reference{thq}, which then provides a different conclusion
about the non-triviality of the polynomial. A further application
will be the classification of the 3-braid links with unsharp
Morton-Williams-Franks inequality (mentioned in remark \ref{rqw}).

\begin{corr}\label{fintg}
For a given Jones polynomial $V$ (actually the pair
$(\md V,\Md V)$ is enough), there are at most three
values of $\chi(L)$ of a 3-braid link $L$ with $V(L)=V$.
If $\md V\cdot \Md V\le 0$, then $\chi(L)$ is unique.
\end{corr}

\proof The theorem shows that the value of $\chi$ is determined
by one of $\Md V$, $\md V$ or $\spn V=\Md V-\md V$.
In particular for a pair $(\md V,\Md V)$ there exist at most three
values of $\chi$ of 3-braid links with a Jones polynomial realizing
this pair. If $\md V\cdot \Md V\le 0$, then the options that a 3-braid
$\bt$ with $V(\hat\bt)=V$ is strongly quasi-signed or almost
quasi-signed are excluded (up to a few simple cases that can be
checked directly), so $\chi(L)$ is determined (unambiguously) by
$\spn V$. \qed

In particular, since 3-braid links of given $\chi$
are only finitely many, we have

\begin{corr}\label{finth}
There are only finitely many closed 3-braids with the same
Jones polynomial, actually with the same pair $(\md V,\Md V)$. \qed
\end{corr}

For example, one
easily sees that no 3-braid knot has the polynomial of $9_{42}$.
Similarly, no other 3-braid knot has the polynomial of the figure-8-knot
(there is, however, a 4-braid knot with such polynomial, $11_{386}$).

That there are only finitely many closed 3-braids with the same
skein polynomial was known from \cite{3br}. For the Jones polynomial
one should note that infinite families were constructed
by Traczyk \cite{Traczyk} if one allows polynomials up to units.
Traczyk's examples show that for fibered
(strongly quasi-)positive links $\spn V$ may remain the same
while $\chi\to-\infty$, so one cannot expect a full (lower) 
control on $\spn V$ from $\chi$. From these links, one obtains
by connected sum infinite families with the same
polynomial for 5-braids. (The status of 4-braids remains unclear.)
Also Kanenobu \cite{Kanenobu2} constructed finite families of 3-braids
of any arbitrary size, so that our result is the maximal possible.

A question that surfaces naturally with these remarks in mind is 

\begin{question}
Does for 3-braid links the Jones polynomial (or Alexander polynomial)
determine the skein polynomial? In other words, do any two
3-braid links with the same $V$ (or $\Dl$) have also equal $P$?
\end{question}

We have at least the following partial result, whose proof we
postpone after the proof of theorem \reference{Hh}.

\begin{corr}\label{CVP}
A given Jones polynomial $V=V(L)$ is realized for 3-braid links
$L$ by at most three different skein polynomials $P(L)$. If
$\md V\cdot \Md V\le 0$, then $V(L)$ determines $P(L)$.
\end{corr}

In the general case one cannot expect a positive answer to the
above question. At least for links there is now the method
of \cite{EKT} available, which should yield large families of
links with the same Jones but different skein (or Alexander)
polynomial. For constructing families with the same Alexander
(but different Jones or skein) polynomial, further techniques
are available, applicable also for knots, like the non-faithfulness
of the Burau representation (see \cite{Bigelow}) or tangle surgeries
(see \cite{Bleiler}).















For the proof of theorem \ref{Hh} we use the previous work in
\cite{3br} (that in
particular answered Birman's question) on the skein polynomial. We
apply again the result in \cite{3br} that $\Md_zP=1-\chi$ for closed
3-braids. As in that paper, we distinguish the cases of band-
positive, band-negative 3-braids, and such of Xu's form $L^{-1}R$. 

By the Morton-Williams-Franks inequalities \eqref{mq},
a 3-braid $\bt$ of exponent sum (writhe) $[\bt]$ has $v$-degrees of
$P$ in $[\bt]-2$ we call \em{left degree}, $[\bt]$ we call \em{middle
degree} and $[\bt]+2$ we call \em{right degree}. The terms of
$[P]_{z^k}$ for some $k$ in these degrees will be called left,
middle and right terms\footnote{Note that here the brackets for
polynomials and for braids have a completely different meaning.}. 

\begin{lemma}\label{lemg}\mbox{}\\
(a) If $\bt$ is band-positive, then $\Mc_zP$ has $v$-terms in the left
degree and possibly in the middle degree. If $\bt$ is band-negative,
$\Mc_zP$ has $v$-terms in the right degree and possibly in the
middle degree. In either situation a term in the middle degree occurs
if and only if $\hat\bt$ is not fibered.\\
(b) If $\bt$ is $L^{-1}R$
then $\Mc_zP$ has $v$-terms in the middle degree only.\\
In both cases all non-zero occurring coefficients are $\pm 1$.
\end{lemma}

\proof In (a) we prove only the first claim (the second
claim is analogous). Let $\chi=\chi(\hat\bt)$. Since
$\md_lP\le \Md_zP=1-\chi$ and $1-\chi=[\bt]-2\ge 
\md_lP$ by MWF, we have $\md_lP=\Md_zP$, and then \eqref{p21}
implies that $\Mc_zP$ has a $v$-term in the left
degree, with coefficient $\pm 1$. From \cite[Theorem 3]{3br} we
have then that it has no right-degree term, and that if it has
a middle-degree term, the coefficient is $\pm 1$. Now the
previous work and the substitution $v=1$, $z=t^{1/2}-t^{-1/2}$
for $\Dl$ in \eqref{DP} easily show that the middle term
occurs if and only if $\hat\bt$ is not fibered.

Now consider (b). If $\Mc_zP$ has a left-degree term, then using
the substitution \eqref{p21}, we saw that $\bt$ is band-positive.
Otherwise, $[\bt]<3-\chi$, so the contribution of the coefficient
of $z^{1-\chi}v^{[\bt]-2}$ in \eqref{p21}, which is not cancelled,
is not in degree $0$. Analogously one argues if $\Mc_zP$ has a
right-degree term. \qed

Note that keeping track of $[\bt]$ and distinguishing between
left and middle term is important here. By remark \ref{rqw},
we have links with equal polynomials such that the left
term of the one is the middle term of the other.

\begin{lemma}\label{lemldg}
(a) If $\bt$ is $L^{-1}R$ and $L$ has exponent sum $[L]>1$, then
$[P]_{z^{-1-\chi}}$ has a left-degree term, and the coefficient
is $\pm 1$. \\
(b) If $[L]=1$ and
$[P]_{z^{-1-\chi}}$ has a left-degree term, then the coefficient
is $\pm 2$. \\
The two analogous statements hold replacing $L$ by $R$
and left-degree term by right-degree term.
\end{lemma}

\proof We proved already that $\Mc_zP$ has only a middle-degree term.
So it must remain under the substitution of \eqref{p21} if and only
if $[\bt]=1-\chi$. The cases (a) and (b) occur when this term must
be cancelled, and complemented to $1$, respectively. \qed

\proof[of theorem \reference{Hh}]
The statements follow mainly by putting together the last two
lemmas and looking in which degrees the
non-cancelling contributions of the coefficients of $P$
occur under the substitution \eqref{VPsub}.

If part (a) of lemma \reference{lemg} applies, we established already
(in theorem \reference{thqp})
that the positive band form of $\bt$ is equivalent to the strong
quasi-positivity of $\hat\bt$. In this case $\md V$ comes from
the left-degree term in $\Md_zP$. If $\hat\bt$ is not
fibered, then $[P]_{z^{-1-\chi}}$ must have a right-degree
term (with coefficient $\pm 1$) to cancel the middle-degree
term of $\Md_zP$ under \eqref{p21}.

If part (b) of lemma \reference{lemg} applies, we use the
further information of lemma \ref{lemldg}.
In case (a) of lemma \ref{lemldg}, the left and right
terms in $[P]_{z^{-1-\chi}}$ determine the degrees
and edge coefficients of $V$.

In case (b) of lemma \ref{lemldg},
the maximal term in $V$ comes from the right-degree term in
$[P]_{z^{-1-\chi}}$. A coefficient in $t^{(-1-\chi)/2}$
may come only from a left-degree term in $[P]_{z^{-1-\chi}}$,
which, if occurring, is with coefficient $\pm 2$. \qed

This proof underscores the significance of \eqref{VPsub}
as a tool for studying the Jones polynomial. So far it
seems to have been useful just for calculating specific
Jones polynomials from $P$. In \S\reference{Sfg} we will
see further results that come out of considering this
substitution.

We note the following equalities that follow from the proof of
theorem \ref{Hh}. These will be needed in the study of the Q
polynomial, and are also helpful for corollary \reference{CVP}.

\begin{lemma}\label{lemma_}
If $\bt$ is a not strongly quasi-signed 3-braid of exponent sum $e$
and $V$, $\chi$ the Jones polynomial resp. Euler characteristic
of its closure, then
\begin{eqnarray}
\label{one_}\Md V-e & = & \frac{1-\chi}{2}+1 \\
\label{two_}\md V-e & = & -\frac{1-\chi}{2}-1 
\end{eqnarray}
\em{Exceptions} are \eqref{two_} if $\bt$ is strongly
almost quasi-positive, and \eqref{one_} if $\bt$ is strongly
almost quasi-negative. \qed
\end{lemma}

\proof[of corollary \reference{CVP}]
Depending on whether a 3-braid representation $\bt$ is strongly
quasi-signed, almost quasi-signed, or none of both, $V$ determines
$e=[\bt]$ via $\chi(\hat\bt)$ and/or \eqref{one_} or \eqref{two_}.
With $V$ and $e$, one can recover the trace of the Burau matrix
$\psi_2(\bt)$, and from that also $P(\hat\bt)$ (see \cite{Birman} or
\eqref{V_3} below). Again, if $\md V\cdot \Md V\le 0$, then the
options that $\bt$ is strongly quasi-signed or almost quasi-signed
are ruled out easily. \qed
