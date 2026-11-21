---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-037-77-knots-with-unsharp-mwf-inequality
section_title: "Knots with unsharp MWF inequality"
section_number: 7.7
pages: 60-61
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
This brief part was motivated by the paper of Kawamuro
\cite{Kawamuro}, which I came across during the continuous work
on my paper. Kawamuro was interested in finding infinitely many
knots for which the MWF inequality is strict, in particular such
satisfying Jones' conjecture in \S\ref{SJS}. The point to make
is that we have at least two ways allowing us to obtain her, and
further such knots much more easily. (In particular it is not
necessary to appeal to the heavy geometric machinery of
Neumann-Rudolph-Giroux.)

We already saw an infinite family of examples with unsharp MWF
(and satisfying Jones' conjecture) in the proof of theorem
\ref{thJC}. This family is, of course, little insightful,
since it is settled already by Birman-Menasco's 3-braid
work. The 4-braid examples they proposed, but could not
decide about, deserve more attention. As given in figure 4
of \cite{Kawamuro}, consider for $(x,y,z,w)\in\bZ^4$ the
4-braids $\bt_{x,y,z,w}=[212^213^x2^y-12^z3^w]$, and let
$K_{x,y,z,w}=\hat\bt_{x,y,z,w}$. Birman-Menasco observe that
$MWF(K_{x,y,z,w})\le 3$ (see lemma 2.9 in \cite{Kawamuro}),
but suspect that many of the $K_{x,y,z,w}$ have braid index 4.
One can exhibit an infinite family of $K_{x,y,z,w}$ of $b=4$,
and thus recover theorem 2.8 of \cite{Kawamuro}, like this.

\begin{prop}
There is a natural number $N$ and 6 tuples $(\ap_1,\dots,
\ap_4)\in \bZ^4$ of different mod-2-reductions in $(\bZ/2)
^4$, such that if $K_\gm:=K_{\gm_1,\dots,\gm_4}$ is a knot,
then $b(K_\gm)=4$ whenever $(\ap_i)\equiv (\gm_i)\bmod
2$ and $\gcd\Bigl(\ffrac{\gm_i-\ap_i}{2}\Bigr)\ge N$.
\end{prop}

\proof Since (complex) roots of unity are dense on the complex
unit circle, choose a root of unity $t$, for which the 3-braid
test in corollary \ref{pp1} applies for $9_{42}$ or $9_{49}$ (see
example \ref{4249}). Then, using the formula for $\Dl$ in lemma 3.1
of \cite{SSW}, we see that for each such $t$ there is an $n\in2\bZ
\sm\{0\}$, such that $\Dl_{\hat\bt}(t)$ is preserved when $\bt$
is replaced by $\sg_i^n\bt$.

Moreover, it is easy to check that for all 6 of the 16 possible
vectors of parities of $(x,y,z,w)$, for which $K_{x,y,z,w}$ is a
knot, there is a representation of (at least one of) $9_{42}$ or
$9_{49}$ of that parity combination. (The representations given
after definition 2.7 of \cite{Kawamuro} show 3 of the parity
types.) Now, take such a representation $\bt_{\ap_1,\dots,\ap_4}$
and vary the parameters $\ap_i$ by multiples of $n$. Then, since
we can choose (for proper $t$) $n$ to be any sufficiently
large even natural number, we obtain in the claim. \qed

Of course, this elementary argument could be further concretified
and strengthened. Presumably, one can do much better using
J.~Murakami's test theorem \reference{TMF} (since it is an equality).
Note that our proof does not confirm Jones' conjecture on any
$K_{x,y,z,w}$, so it may trigger the question: would it help
to find a counterexample? This seems very optimistic, though,
as we will soon see from an alternative approach to Kawamuro's
theorem, using the work in \S\ref{SJS}. First we can settle
(also with regard to Jones' conjecture) the concrete examples
$K_{-1,-2,m,2}$ for $m\ge 2$ even, obtained in her proof.

\begin{prop}\label{pZ}
We have $b(K_{-1,-2,m,2})=4$ for $m\ne -1,0$.
\end{prop}

\proof We give just a brief explanation. We try to calculate the
skein polynomial of the 2-cable $\bt^{[2]}_{-1,-2,m,2}$ of $\bt_
{-1,-2,m,2}$, obtained by replacing $\sg_i$ by $\sg_{2i}\sg_{2i+1}
\sg_{2i-1}\sg_{2i}$, and we may consider just the coefficient
of $v^{4[\bt_{-1,-2,m,2}]+7}$. Again $\pi_Y([2312])$ has at
most 7 different eigenvalues $\dl_i$, for all $Y\vdash 8$ taken
together. But now we have no full twist, and so do not need to
deal with the various $Y$ (and their weights $W_Y$ etc.) one by
one. We can sum $W_Y\cdot c(i,Y)$ over $Y\vdash 8$, and are left
with 7 different $q$-rational expressions $c_i$ to determine. 
Again this can be done from 7 explicit polynomials, which can be
obtained using Morton's program. (If we focus on one parity of $m$
only, we can again reduce the unknowns $c_i$ and test polynomials 
to 5, but need to calculate polynomials from slightly more
complicated braids.)

We calculated in fact 11 polynomials, for $|m|\le 5$, and
used those 9 for $|m|\le 4$ in the determination of $c_i$
to have extra safety. The resulting linear
equation system for $c_i$ (with matrix $\{\dl_i^m\}$) is now
not a serious problem to MATHEMATICA, which gives the solution
(for generic $q$) in just a few seconds. Clearing denominators,
and looking already at the extremal $q$-degrees, we see that for
$|m|\ge 6$ among the 7 terms $c_i\dl_i^m$ the one for $i=2$ has
the lowest minimal or highest maximal degree (as a unique term,
except for $m=6$, where we must use also that the leading
coefficient of $c_6\dl_6^m$ has the same sign). With an
explicit check for the other $m$, we conclude the claim. \qed

This method of proof has also the advantage of easily leading
to a qualitative improvement of Kawamuro's theorem, which is
closer to what one should expect.

\begin{prop}
The tuples $(x,y,z,w)$ for which $K_{x,y,z,w}$ has braid index 4 (and
satisfies Jones' conjecture) are generic in $\bZ^4$, in the sense that
\begin{eqn}\label{bla}
\lim_{n\to\infty}\es
  \frac{
   \big|\,
    \{\,(x,y,z,w)\in \bZ^4\,:\,b(K_{x,y,z,w})=4\,\}\,\cap\, {[-n,n]^4} 
   \,\big|
  \rule[-0.6em]{\z@}{1.3em}}
  {\big|\,[-n,n]^4\,\big|\rule[0.1em]{\z@}{1.0em}}
\es=\,1\,.
\end{eqn}
\end{prop}

\proof Extending the argument for proposition \ref{pZ}, we see that 
\[
\tl P(x,y,z,w):=
  [P(\hat\bt^{[2]}_{x,y,z,w})]_{v^{4[\bt_{x,y,z,w}]+7}}(
  \sqrt{q}-1/\sqrt{q})\cdot \sqrt{q}^{\,4[\bt_{x,y,z,w}]+7}
  \,=\,\sum_{i_x,i_y,i_z,i_w=1}^7\,c_{i_x,i_y,i_z,i_w}\dl_{i_x}^x
  \dl_{i_y}^y\dl_{i_z}^z\dl_{i_w}^w\,,
\]
where $c_{i_x,i_y,i_z,i_w}$ are again some rational expressions
in $q$. They are obviously not all zero, and the polynomials $\tl
P(x,y,z,w)$ have the following property: if one fixes three of the
parameters (say $x,y,z$), and $\tl P(x,y,z,w)=0$ for 7 different
values of the remaining parameter (here $w$), then it vanishes
for all values of that parameter (at the given fixed 3 others).
It is then not hard to deduce \eqref{bla} from this (see e.g.
the proof of lemma 11.1 of \cite{gen2}). \qed



\noindent{\bf Acknowledgement.} I would like to thank to M. Hirasawa,
M. Ishiwata and K.~Murasugi for their contribution, and S.~Kamada,
K.~Kawamuro, T.~Nakamura and D.~Silver for some helpful remarks.
The calculations were performed largely using the programs of
\cite{MorSho2} and \cite{KnotScape}, and MATHEMATI\-CA\TM{}
\cite{Wolfram}. I also wish to thank to my JSPS host Prof. T.~Kohno
at University of Tokyo for his support.




\begin{appendix}

\renewcommand{\thesection}{\Alph{section}}
{\def\@seccntformat#1{Appendix \csname the#1\endcsname . \quad}
