---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-017-512-maximal-subwords
section_title: "Maximal subwords"
section_number: 5.1.2
pages: 27-29
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.755
latex_coverage_ratio: 0.99
---
Here we start the technical considerations needed to prove 
theorem \reference{thmwf}. We consider the form \eqref{wd},
now with all $l_i>0$.

\begin{defi}
We define \em{summit syllables} in \eqref{wd}:
\def\theenumi{\alph{enumi}}
\def\labelenumi{\theenumi)}
\begin{enumerate}
\item All $\sg_{n-1}^{l_i}$ are summit syllables, and
\item if $\ap=\sg_k^{l_i}$ and $\ap'=\sg_k^{l_j}$ are summit
syllables, with no $\sg_{k'}^{l'}$ for $k'\ge k$ occurring between
$\ap$ and $\ap'$, then all $\sg_{k-1}^{l'}$ occurring between $\ap$
and $\ap'$ are summit syllables.
\end{enumerate}
\end{defi}

Note that, according to definition \reference{dfext}, we
consider syllables in cyclic order. The relation ``between'' in
the above definition should also be understood in that sense:
a syllable occurring after the last index $i$ syllable
$\ap$ and/or before the first index $i$ syllable $\ap'$ is
considered to be between $\ap$ and $\ap'$.

For the following considerations it is (not necessary but) helpful
to visualize $\bt$ by the braid scheme explained in \cite{bind}.

Separate $\bt$ in
\eqref{wd} into subwords $\ap_1\dots \ap_n$, such that $\ap_i$
contains only syllables of odd or even index, and this parity
changes between $\ap_i$ and $\ap_{i+1}$. Then for a syllable
$\sg_k^l$ occurring in $\ap_i$, put the integer $l$ at the point
$(k,i)\in \bN\times \bN\subset \bR^2$ in the plane. Here $(k,i)$
is the point in the $i$-th row and $k$-th column, with rows
numbered (as in Cartesian coordinates) from bottom to top and
columns from left to right.

One obtains a certain checkerboard pattern of integers we call
\em{braid scheme} of $\bt$. (If we do not put any integer on
a point $(k,i)$, we assume its ``content'' is zero, or it is
``empty''. So for all non-empty points $(k,i)$ in the scheme,
$i+k$ is always even or always odd.)

One can \em{reduce} the
scheme by moving an integer $l$ at $(k,i)$ to $(k,i-2)$ if $i>2$
and the points $(k\pm 1,i-1)$ are empty. We call the scheme
reduced if it does not admit any such move. Then in a reduced
scheme, summit syllables of $\bt$ are those, whose entries in
the scheme are ``on top'' when viewing the scheme from the left.
{}From this viewangle the following ``geographic'' choice of
terminology becomes more plausible.


\begin{defi}
Summit syllables still have a cyclic order from \eqref{wd}. We call
the subword $\bt'$ of $\bt$ in \eqref{wd} made of summit syllables
the \em{maximal subword}. The subword made of non-summit syllables
(i.e. the subword obtained by deleting in $\bt$ all syllables in
$\bt'$) is called \em{non-maximal subword}. 

Note that neighbored summit syllables have indices $k_i$ differing
by $\pm 1$. We say that a summit syllable is \em{minimal} resp.
\em{maximal} if its both neighbors have higher resp.\ lower index.

We call $\bt$ \em{summit reduced} if all its minimal summit syllables
are non-trivial.  We call $\bt$ \em{index reduced} if it is
non-singular and its index sum $\sum_{i=1}^n k_i\cdot l_i$ cannot be
reduced by a Yang-Baxter relation, i.e. $\bt$ contains no
$\sg_{i+1}\sg_i\sg_{i+1}$ as subword.
\end{defi}

\begin{lemma}
Index reduced $\So$ summit reduced. In particular a summit reduced
form always exists.\qed
\end{lemma}

Recall that a positive resolution tree is a rooted tree with directed 
edges,
whose vertices (nodes) contain positive braid words, the root labelled
by $\bt$. Every vertex has exactly one incoming edge, except the
root that has none, and zero or two outoutgoing edges. In former
case it is labelled by an unlink (terminal node).
In latter case it is labelled by
a word of the form $\ap\sg_i^2\ap'$, with $\ap,\ap'$ positive
words, and the two vertices connected by the outgoing edges 
are labelled by $\ap\sg_i\ap'$ and $\ap\ap'$, or positive words
obtained therefrom by Markov equivalence (isotopy of the closure link).

In \cite{Nakamura} the following fact was observed, and used
decisively, and we shall do the same here.

\begin{theorem}(Nakamura \cite{Nakamura})
$MWF(\bt)$ is the maximal number of components of a (link in a) node
in a positive resolution tree for $\bt$.
\end{theorem}

In particular, $MWF$ is monotonous (does not decrease) under word
extension, and does not depend on the exponent of non-trivial
syllables.

\begin{lemma}\label{lemh}
If $\bt$ is \em{summit reduced}, and $\bt'$ is obtained from $\bt$
by removing all summit syllables, then there is a positive resolution
tree for $\bt$ that contains $\bt'$ as a node.
\end{lemma}

\proof Since minimal syllables are non-trivial, one can delete them
in the resolution tree. The two neighbors in the maximal subword
join to a non-trivial new minimal syllable, and so one iterates the
procedure. \qed

Since all $\sg_{n-1}^{l'}$, $\sg_{n-2}^{l'}$ in \eqref{wd} occur as
summit syllables, $\bt'$ has split last two strands, and so we have
a quick proof of Nakamura's main result.

\begin{corr}(Nakamura \cite{Nakamura})
Any summit reduced positive word on $n\ge 3$ strands has $MWF\ge 3$.
\qed
\end{corr}

In particular any positive braid representation of a $(2,n)$-torus
link can be reduced to the standard one by index-decreasing YB
relations and removals of nugatory crossings.  


\subsubsection{The proof of Theorem \reference{thmwf}:
Initial simplifications\label{4.0}}

The following fact is well-known:

\begin{theorem}\label{th4.1}
$MWF(\bt)=1$ if an only if $[\bt]_i=1$ for $i=1,\dots,n-1$.
\end{theorem}

Now for $MWF=3$ it suffices to ensure that (either we can reduce the
braids) or can find words, whose non-maximal subwords do not
give an unknot. \em{For the rest of the section we assume that
$\bt'$ gives the unknot.}

We will work by induction on the number of strands, and for
fixed number of strands on the index sum. So we consider a
positive braid word $\bt$, and assume w.l.o.g. it has the
smallest index sum among positive braid representatives of
its closure link for the same number of strands. For such
$\bt$, we will either reduce it (by at least one strand or
crossing), or show $MWF\ge 4$.

Most braids $\bt$ will be easily dealt with, but there remain certain
families of words that require a case-by-case study. We decided not
to omit too many of the (tedious) details of this part, in order
to keep the proof followable, even if it may not contribute to
its (esthetic) appearance.

Note that in order to prove $MWF(\bt)\ge 4$, it suffices to
go over to a (link in a) suitably chosen node in a positive
resolution tree for $\bt$ and show $MWF\ge 4$ for this node. In
particular, we can remove from $\bt$ all syllables of index $\le
k$ and the $k$ resulting left isolated strands.

The case of reductions is more delicate. In some situations
we can describe them directly, but this is not always the case.
Then we proceeded as follows. First we took generic examples, in
making all syllables non-trivial whose triviality we have not argued
about. We adjust parities so that the closure is a knot, and checked
using KnotScape \cite{KnotScape} that the braid reduces (by at least one
strand/crossing).

Later we wrote a computer program that seeks reductions by keeping
given crossings rigid. Such reductions would commute with replacing
rigid crossings by any tangle, in particular by any non-trivial
braid word syllable. (Non-trivial syllables behave
similarly to  rigid vertices, and suggest that the reduction
is likely to work in general.) This way we can find reductions for
infinite families of braids on a given number of strands. By turning
all summit index-1 syllables into rigid crossings, one can also
handle the braids that occur for an increasing number of strands.

The technical details of the application of this program are,
however, tedious and little insightful. Instead we content
ourselves with giving the examples we processed with KnotScape.





\begin{defi}
A \em{valley} resp. \em{mountain} is a subword of the maximal word
that starts with same index syllables and contains only one minimal
resp. maximal syllable. This syllable is called the \em{bottom} of
the valley resp.\ \em{summit} or \em{top} of the mountain.
The index of the bottom/top is the \em{depth} resp.\ \em{height}.
\end{defi}

We assume there are at least two mountains of maximal height (i.e.
$n-1$). Otherwise we have a split component or a $(2,n)$-torus
connected component, or a reducible braid and can work by induction
on the number of strands. Similarly at least one valley has
depth $1$, otherwise $\sg_1$ in $\bt'$ remains reducible in $\bt$.

The following operation will be somewhat important, and we will
call it ``filling the valley''.

\begin{lemma}(``filling the valley'')
Any valley can be removed from the maximal subword in the positive
resolution tree.
\end{lemma}

\proof Same as for lemma \reference{lemh}. \qed

\begin{lemma}
If a mountain $M$ is not of maximal height
(i.e. $n-1$), then $MWF(\bt)\ge 4$.
\end{lemma}

\proof Let $k<n-1$ be the height of $M$.
We assumed there are at least two mountains of maximal height. So
now w.l.o.g. assume some, say
the left, of the neighbored mountains of $M$ has height $k'>k$.
Fill the two valleys around $M$ starting with $\sg_{k-1}$.
Then the maximal subword has a syllable index sequence
$k+1,k,k-1,k,k-1,k$. Make the second and third syllable trivial
(if not already), and apply YB relations, moving the fourth
syllable to the left: $k+1,\ul{k-1},k,k-1(,k-1),k$. The result is a
summit reduced word, in which a new syllable of index $k-1$
(the underlined one) was removed and it became non-maximal. Hence the
non-maximal subword has exponent sum $[\bt']_{k-1}>1$, and so
$MWF\ge 4$. \qed

\begin{lemma}\label{lem2val}
If $\bt$ has $>2$ valleys of depth at most $n-3$, then $MWF(\bt)\ge 4$.
\end{lemma}

\proof 
It suffices to check for 3 mountains (as one can fill
separate valleys) and 4-braids (as one can fill valleys by
levels as in the proof of lemma \reference{lemh} and the remark
after theorem \reference{th4.1}). This is just
the word [1232112321121321], which is easily checked (to
have $MWF=4$). \qed


\subsubsection{Two mountains\label{S4.1}}

We assume in \S\reference{S4.1} and \S\reference{S4.2} that $n\ge 5$.
The case of $4$-braids is considered later in \S\reference{S4.3}.
We refer to \S\reference{brs} for the use of notation we will employ.

We assume first $\bt$ has two mountains. By the previous remarks they
are both of height $n-1$.

So now consider words with syllable index sequence
\begin{eqnarray}\nonumber
& 1,2,\dots,n-2,n-1,\quad
p_1@,\dots,p_k@,\quad
n-2,n-3,\dots,g+1,g!,\quad \\
\label{xx} &
g+1,\dots,n-2,n-1,\quad
q_1@,\dots,q_l@,\quad
n-2,n-3,\dots,2,1
\end{eqnarray}
such that $l+k=n-3$ and
$\{p_1,\dots,p_k,q_1,\dots,q_l\}=\{1,\dots,n-3\}$.
We will distinguish only between non-trivial and trivial syllables
(in former case exponent is immaterial). For non-trivial syllables
we write an exclamation mark
after the index, for trivial ones an `at' (@) sign.
If none of $!$ and @ is specified, we do not exclude explicitly any of
either types. We write $\bt_1,\dots,\bt_6$ for the subwords separated by
space in \eqref{xx}.

Assume w.l.o.g. (up to reversing the braid's orientation) that
some $p_i$ is $1$, and let up to commutativity the $p_1,\dots,p_k$
subword be written as $h,h-1,\dots,1,p_1',\dots,p_{k-h}'$ (the 
$p_i'$ contain the indices above $h$ occurring as $p_i$).

Assume the maximal syllable of $\sg_{h+1}$ in $\bt_1$ is non-trivial.
Then one can write $\bt$ as word with a subword of index sequence 
\begin{eqn}\label{siks}
1,\dots,h+1!,h@,\dots,1@\,. 
\end{eqn}
If now $h<n-3$, we can make in \eqref{siks} all syllables
trivial except $h+1$, which we make of exponent $2$, then
split a loop (component of a link in a node of a positive
resolution tree) by removing all the syllables in \eqref{siks}
together with the terminating `$1$' in \eqref{xx}. We obtain
\begin{eqnarray*}
& h+2,\dots,n-2,n-1,\quad
p_1'@,\dots,p_{k-h}'@,\quad
n-2,n-3,\dots,g+1,g!,\quad \\
& g+1,\dots,n-2,n-1,\quad
q_1@,\dots,q_l@,\quad
n-2,n-3,\dots,2.
\end{eqnarray*}
(Here no syllables of index 1 occur, and the split loop is the
isolated leftmost strand.) Then we fill the valley starting with the
index-$n-1$-summits, splitting another loop (the rightmost strand),
\[
h+2,\dots,n-3,n-2,\quad p_1'@,\dots,p_{k-h}'@,\quad q_1@,\dots,q_l@,
\quad n-2,n-3,\dots,2,
\]
and are left with a
word that has at least two $\sg_{n-2}$. So $MWF\ge 4$. 

\begin{caselist}
\case Assume the smaller valley has depth $g>1$.
The $\bt$ has two index-1 syllables, a trivial (non-summit)
and a non-trivial (summit) one. By a flype one can exchange
them, and so have a non-summit reduced word. Then one
can change $\bt$ to a word of smaller index sum, and so
we are done by induction.








































































\case Now $g=1$. We write $\bt_1,\dots, \bt_6$ for the
6 subwords separated by spacing in \eqref{xx}.
By a similar argument as after \eqref{siks} we can argue that
if one can reorder the syllables in $\bt_{2,5}$ so that
$\bt$ has a subword with an index sequence 
\begin{eqn}\label{(eight)}
k,k+1,\dots,h-1,h!,h-1,\dots,k\,,
\end{eqn}
with the first or last
$h-k$ syllables belonging to $\bt_{2,5}$ and the others
to $\bt_{1,3,4,6}$, and $h<n-2$, then $MWF\ge 4$.

W.l.o.g. assume $1\in \bt_5$ (which is meant to abbreviate that
$\bt_5$ contains an index-$1$ syllable).

\begin{caselist}
\case
Now if $2\not\in\bt_5$ (so $2\in\bt_2$) then the
$2$-index syllables in $\bt_{4,6}$ are trivial
(because we have otherwise \eqref{(eight)} with $k=1$, $h=2$).

We distinguish several cases by the subwords of
(non-summit) syllables of index $1,2$ and $3$ in $\bt_{2,5}$.
We separate the subwords between $\bt_{2}$ and $\bt_5$
by a vertical line `$|$'. (We assume here that $n\ge 6$.
The case $n=5$ must be handled by a separate, but
simplified, argument.) Note that by symmetries we can
exchange the words of $1,2$ and $3$ left and right from `$|$'
and also (simultaneously) reverse both, and can also use the
commutativity of $1$ and $3$. Then we are left with
the following cases.

\begin{caselist}
\case
$2|31$. If $3\in \bt_5$, then both $3$ in $\bt_{1,3}$ are trivial.
(Otherwise, we would have \eqref{(eight)} for $k=2$ and $h=3$.)

Below we give pairs of words, the first obtained by extending all
admissible syllables to be non-trivial, and the second one by
extending the first word to one with knot closure, which was then
checked to reduce (by at least one strand, not necessarily to a
3 braid).
\\
$[1122344  2 55665544322111   2334455 3441 66554433211]$, \\
$[11222344 2 5556655444322111 2334455 3441 666554433211]$ reduces. \\

\case
If $3\in \bt_2$, then one of both $3$-index syllables in
$\bt_{1,3}$ must be trivial. (It is the syllable in $\bt_3$ if `$3$'
occurs before `$2$' in $\bt_2$, or the syllable in $\bt_1$
otherwise.)

\begin{caselist}
\case
$ 23|1$.

\\
$[1122344 23 556655443322111    2334455 441 66554433211]$, \\
$[1122344 23 556665554443322111 2334455 441 66554433211]$ reduces. \\

\case $ 32|1$

\\
$[11223344  32 55665544322111   2334455 441 66554433211]$, \\
$[112233444 32 5556665544322111 2334455 441 66554433211]$ reduces.  \\

\end{caselist}
\end{caselist}

\case
Now assume $2\in\bt_5$. Since $1\in\bt_5$, now the exclusion
of \eqref{(eight)} shows that only one of the $2$-index syllables
in $\bt_{4,6}$ is trivial, but we will show that also one in
$\bt_{1,3}$ is. Namely, by making the proper index-$1$ (summit)
syllable to exponent 2, and one of the $2$-index syllables of $\bt_
{1,3}$ trivial, one can slide by braid relations the $1$-index
syllable $\sg_1=X$ from $\bt_5$ to $\bt_2$.
By applying the previous argument, both
$2$-index syllables in (the now modified) $\bt_{1,3}$ are trivial.
One of them was previously made trivial to slide $X$ in, but the
condition on the other one persists for the original braid.


In all situations,
make all the other syllables in $\bt_{1,3,4,6}$ non-trivial and
check using KnotScape that the braid reduces. 



\begin{caselist}
\case $ 3| 12$. In this case the above argument shows that the
syllable $2\in\bt_1$ is trivial.

\\
$[11233445566  344 55443322111 234455   12 66554432211]$, \\
$[112334455666 344 55443322111 23444555 12 665544322111]$ reduces. \\

\case $ 3| 21$. Here $2\in\bt_3$ is trivial.

\\
$[112233445566 344 5544332111 2234455 21 6655443211]$, \\
$[112233445566 344 5544332111 2234455 21 66655544432111]$ reduces. \\

\case $| 123$. As before $2\in\bt_1$ is trivial.

\\
$[11233445566 55443322111 234455 123 665544332211]$, \\
$[11233445566 55443322111 234455 123 666555444332211]$ reduces. \\

\case $| 132$.

\\
$[11233445566 55443322111 2334455 132 66554432211]$, \\
$[11233445566 55443322111 2334455 132 66655544432211]$ reduces. \\

\end{caselist}
\end{caselist}

\end{caselist}
