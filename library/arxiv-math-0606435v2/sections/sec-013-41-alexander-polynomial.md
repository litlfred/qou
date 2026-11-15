---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-013-41-alexander-polynomial
section_title: "Alexander polynomial"
section_number: 4.1
pages: 15-17
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.86
latex_coverage_ratio: 0.974
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
In \cite{Birman}, Birman proposed (but considered as very difficult)
the problem to classify 3-braid
links with given polynomials. In \cite{3br} we dealt with the skein
polynomial. Now we can extend our results to the Alexander polynomial
(with the convention in the beginning of \S\reference{ppp}).
The following discussion gives a fairly exact description how to
find the 3-braid links, if such exist, for any possible admissible
(as specified in \S\reference{brD}) polynomial.

A solution for the Jones polynomial is presented afterwards.


\begin{lemma}
If $\bt$ is strongly quasi-positive and fibered, then $\Mc\Dl=+1$.
\end{lemma}

(Here it is essential to work with the leading, not trailing
coefficient of $\Dl$ and with strongly quasi-positive links and
not their mirror images.)

\proof We know $\md_vP=\Md_zP=1-\chi$. So $[P]_{z^{1-\chi}}$ has
a term in degree $v^{1-\chi}$. The coefficient must be $+1$
because of \eqref{p21} and because it is the only coefficient that
contributes to the absolute term in $P(v,v^{-1}-v)$. Now from
the classification of leading $z$-terms of $P$ in \cite{3br}
it follows that $[P]_{z^{1-\chi}}$ can have at most one further term,
with coefficient $\pm 1$. If such term exists, the substitution
\eqref{DP} would either cancel the terms
in degree $t^{(1-\chi)/2}$ in $\Dl(t)$, or give coefficient $\pm 2$,
so our link cannot be fibered. Thus a second term does not exist,
and the claim follows from \eqref{DP}. \qed

\begin{lemma}\label{ty}
Let $\bt'=[(123)^k]$ be an even power $k$ of $[123]$.
Assume $\bt$ has Xu normal form $R$, and after syllable
reduction becomes $\bt'$, but $\bt\ne\bt'$ itself (i.e. some
syllable in $\bt$ is non-trivial). Then $\hat\bt$ satisfies
$\Md\Dl=-1-\chi$; moreover $\Mc\Dl>0$ and is equal to the 
number of non-trivial syllables in $\bt$.
\end{lemma}

\proof We use for fixed $k$ induction on the exponent sum.
If exactly one syllable is non-trivial with exponent $2$,
then applying the skein relation at the exponent-2
syllable shows that $\bt=\bt_+$ inherits the Alexander
polynomial of $\bt_-$ with positive sign (since $\bt_0=\bt'$,
whose closure has zero polynomial). 
Now $\bt_-$ is positive and has an index array with a subsequence
of the form $xyx$, and so is fibered by theorem \reference{Thq}.
Then by lemma \reference{ty}, $\Mc\Dl=+1$ and
$\Md\Dl=1-\chi(\hat\bt_-)=-1-\chi(\hat\bt)$.

If $[\bt]-[(123)^k]>1$, then applying the skein relation
at any non-trivial exponent $2$ syllable gives (with positive
sign) the Alexander polynomials of two closed braids
$\bt_0$ and $\bt_-$, former of which is fibered and
latter of which has the requested property by induction.
Then the maximal terms in degree $1-\chi(\hat\bt_-)=
-\chi(\hat\bt_0)$ are positive and do not cancel.
The one of $\bt_-$ is $+1$, while the one of $\bt_0$
by induction one less than the number of non-trivial 
syllables in $\bt$ (since in $\bt_0$ one more syllable
becomes trivial).

If some syllable in $\bt$ has exponent $>2$ then $\bt_-$ is
not minimal, and the degree and leading coefficient of $\Dl$
are inherited (with positive sign) from $\bt_0$. \qed

\begin{lemma}\label{tz}
Assume $\bt$ has Xu normal form $R$, which after syllable
reduction becomes an odd power $k$ of $[123]$.
Then $\Md\Dl=1-\chi$, and $\Mc\Dl=+2$.
\end{lemma}

\proof First we prove the claim if $\bt=[(123)^k]$.
We know that $\Md\Dl=1-\chi$ and $\Mc\Dl=\pm 2$,
so we must exclude $\Mc\Dl=-2$. Applying the skein relation gives
the polynomials of $\bt_0$ and $\bt_-$ with positive sign.
$\bt_0$ is positive and fibered as before, so $\Mc\Dl=+1$.
Then clearly $\bt_-$ (which is of the form $L^{-1}R$ and also
fibered) cannot have $\Mc\Dl=-3$. 

If $\bt\ne [(123)^k]$, then it has a non-trivial syllable.
Applying the skein relation at a letter in that syllable
we find that $\bt_-$ reduces. So the leading term comes
from $\bt_0$, and with positive sign. \qed



\begin{theorem}\label{THA}
Fix some admissible Alexander polynomial $\Dl$. Then
\def\labelenumi{\theenumi)}
\begin{enumerate}
\item If $\Dl=0$, then the 3-braid links with such polynomial
are the split links and the closures of (incl.\ negative)
even powers of $[123]$.
\item If $\Dl\ne 0$, there are only finitely many 3-braid links
with this $\Dl$. They all have $1-\chi=2\Md\Dl$ or $-1-\chi=2\Md\Dl$.
In latter case they are up to mirroring strongly quasi-positive.
\item If $\Mc\Dl\le -2$, then no 3-braid knot or 3-component
link has such Alexander polynomial, and any 2-component link
is strongly quasi-negative.
\item If $\Mc\Dl\ge +2$, any 3-braid knot or 3-component link
with such Alexander polynomial is strongly quasi-positive or a
mirror image of it. Any 2-component link is strongly quasi-positive.
\item If $|\Mc\Dl|>2$, then any 3-braid link 
with such Alexander polynomial has $2\Md\Dl=-1-\chi$.
\end{enumerate}
\end{theorem}

\begin{defi}\label{DEFB}
Let for $\bt\in B_3$ with $6\mid [\bt]$, the \em{Birman dual}
$\bt^*$ be defined by $\bt^{-1}\dl^{2[\bt]/3}$, where
$\dl=[121]$ and $\dl^2$ generates the center of $B_3$.
\end{defi}

Birman \cite{Birman} shows that $\hat\bt$ and $\hat\bt^*$
have the same skein polynomial. This observation relates to
our explanation at a couple of places, for example, in remark
\reference{rqw}, and also in the below arguments.

\proof[of theorem \reference{THA}]
Let us exclude \em{a priori} trivial and split links.  The claims
follow from the discussion of $2\Md\Dl$ and $\Mc\Dl$ in cases.

We know by theorem \reference{xLR} (or by \cite{3br,ntriv}, as noted
before) that if $\bt\in B_3$ is not (up to mirroring) strongly
quasi-positive, then $2\Md\Dl=1-\chi$ and $\Mc\Dl=\pm 1$.

It remains to deal with the Xu form $R$. The form $L$ is just the
mirror image, and mirroring preserves the Alexander polynomial for
knots and 3-component links and alters the sign for 2-component
links.

If making trivial all syllables in $\bt$, the new word
$\bt'$ is not a power of $[123]$, then we proved that $\hat\bt$
is fibered, so again $2\Md\Dl=1-\chi$ and $\Mc\Dl=\pm 1$.

If $\bt'$ is an even power of $[123]$, then by Birman duality we
conclude that $\Dl(\hat\bt')=0$. If $\bt\ne \bt'$, then one uses
lemma \reference{ty}.






Thus $2\Md\Dl=-1-\chi$.


If $\bt'$ is an odd power of $[123]$, then use the observation in
lemma \reference{tz}  (or make one syllable to exponent $4$ and
use Birman duality) to conclude that $2\Md\Dl=1-\chi$ and
$\Mc\Dl=+2$. \qed

\begin{exam}
In certain situations this theorem gives the most rapid test to
exclude closed 3-braids. For example, the knot $13_{6149}$ has
$MWF=3$, but seeing that $\Dl$ has $\Mc\Dl=-2$ we immediately
conclude that it cannot be a closed 3-braid.
\end{exam}

\begin{corr}
There are only finitely many 3-braid links with given $\Md\Dl$
(provided $\Dl\ne 0$). \qed
\end{corr}

It is actually true (as we will prove below) that for links with
\em{any} bounded braid index there are only finitely many different
Alexander polynomials of given degree admitted. However, such
Alexander polynomials may be admitted by infinitely many different
links (of that braid index). See \S\reference{s4.2} for some remarks.










\begin{corr}\label{cbd}
Non-split 3-braid links bound no disconnected Seifert surfaces (with
no closed components). In particular there are no non-trivial 3-braid
boundary links.
\end{corr}

\proof For such links the Alexander polynomial is zero. The only
non-split 3-braid links $L$ of zero polynomial are closures of
$[(123)^k]$ for even $k$. These cases are easily ruled out by linking
numbers. Any pair of components of $L$ has non-zero linking number.
So a connected component of any Seifert surface $S$ of $L$ must have
at least two boundary components of $L$, and if $S$ is disconnected,
$L$ has at least 4 components, which is clearly not the case. \qed

The examples that falsify this claim for 4-braids are again
easy: consider the (closure links of) words in $[1\pm 2-1]$ and
$[2\pm 3-2]$.

\begin{corr}
If $\Dl$ is the Alexander polynomial of a 3-braid link, then
$|\Mc\Dl|\le \Md\Dl+2$. For a knot $|\Mc\Dl|\le\Md\Dl+1$.
\end{corr}

\proof If $|\Mc\Dl|\le 2$ then we are easily done. 
($\Dl=\pm 2$ cannot occur for a knot.) Otherwise we have
up to mirroring a strongly quasi-positive word $\bt$ reducing to
an even power of $[123]$. Now $|\Mc\Dl|$ counts non-trivial syllables,
so $[\bt]=3-\chi\ge 2|\Mc\Dl|$, and $-1-\chi=2\Md\Dl$. For a knot
the number of syllables with exponent $\ne 2$ is at least $2$,
so $[\bt]-2\ge 2|\Mc\Dl|$. \qed

Note in particular that the proof shows that $|\Mc\Dl|$
can be any given natural number, and how to find the link
that realizes this number. We emphasize this here, because
later we will prove a contrary statement in the case of
\em{alternating} links for \em{every} arbitrary braid index
(see corollary \reference{cSG}).

\begin{corr}
A 3-braid \em{knot} is fibered if and only if $\Mc\Dl=\pm 1$.
\end{corr}

\proof It remains to explain why no 3-braid knot has $\Mc\Dl=\pm 1$
but $\Md\Dl<1-\chi$. Latter condition would imply that we have
up to mirroring a strongly quasi-positive word $\bt$ reducing to
an even power of $[123]$, and former condition that $\bt$ has only one
non-trivial syllable. But $[(123)^{2k}]$ has 3-component closure,
and making one syllable non-trivial cannot give a knot. \qed

In particular, it is worth noting

\begin{corr}
No non-trivial 3-braid knot has trivial Alexander polynomial. \qed
\end{corr}

Again, the two 11 crossing knots immediately show that this is
not true for 4-braids.

\begin{exam}\label{x29}
We can also easily determine the 3-braid links for some small degree
Alexander polynomials. For example, we see that no other 3-braid
knot has the polynomial of $3_1$, $4_1$ or $5_2$. Similarly we can
check that no 3-braid knot has the polynomial of $9_{42}$ and
$9_{49}$ (which shows that these knots have braid index 4), a
fact we will derive in the last section using entirely different
representation theory arguments. 
\end{exam}
