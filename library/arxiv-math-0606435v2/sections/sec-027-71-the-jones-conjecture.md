---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-027-71-the-jones-conjecture
section_title: "The Jones conjecture"
section_number: 7.1
pages: 42-48
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.996
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
There is a conjecture, often attributed to Jones (who speculated
on it at least for knots and in it its weaker form, as given below;
see 357 l.-6 of his paper), stating that a minimal
string braid representation has a unique exponent sum.

\begin{conj}(Jones's conjecture)\label{jcc}
\def\labelenumi{\theenumi)}
\begin{enumerate}
\item (weaker version)\label{weV}
If $\bt,\bt'\in B_n$ satisfy $\hat\bt=\hat\bt'=L$ and $n=b(L)$,
then $[\bt]=[\bt']=:w_{\min}(L)$.
\item (stronger version) Part \reference{weV} holds, and if
$\bt''\in B_n'$ for $n'>n$ has $\hat\bt''=L$, then 
\begin{eqn}\label{stz}
\big|[\bt'']-w_{\min}(L)\big|\le n'-n\,.
\end{eqn}
\end{enumerate}
\end{conj}

It was observed in \cite{posex_bcr} that counterexamples
to the conjecture would make MWF and \em{all} of its cabled
versions unsharp. (In \cite{posex_bcr} the weaker version was
focussed on, but the same arguments address the stronger version
too.) Thus, for example, corollary \reference{cft} can also
be regarded as a partial solution to Jones's conjecture.
Similarly, the work in \S\reference{S2.2} shows:

\begin{corr}
If a link $L$ is the closure of a positive braid, and $b(L)\le 4$,
then the strong Jones conjecture is true for $L$. 
\end{corr}

\proof We use theorem \reference{thmwf}, with the remark that
the exceptional braid words therein were shown to have braid
index 4 using the 2-cabled MWF. \qed

For 3-braids the weaker version was known to be true again
from Birman-Menasco's classification result. We will show now
the stronger version, as a consequence of the description in
\cite{3br} of 3-braid links with unsharp MWF inequality (and thus
with a much simpler proof than appealing to Birman-Menasco). See
also remark \reference{rJC}.

\begin{theorem}\label{thJC}
The stronger version of Jones's conjecture holds for 3-braid links.
\end{theorem}

\noindent{\bf Convention.}
The letter $\Dl$, with an integer subscript $n$, is used in
\S\ref{SJS},
in deviation from other sections, exclusively for the half-twist
braid on $n$ strings, and \em{not} for the Alexander polynomial.
(The Alexander polynomial will not appear in \S\reference{SJS}.)

\proof[of theorem \reference{thJC}]
As explained, it suffices to deal only with the 3-braid links
of unsharp MWF inequality. In \cite{3br} these links were
described fully. If $\mu=\sg_1^{6a\pm 1}\sg_2^{\mp 1}$,
then for the Birman dual $\bt=\mu^*$ of $\mu$ (see definition
\ref{DEFB}) we have $\hat\mu^*\ne \hat\mu$ when $6a\pm 1>6$, but
$K=\hat\bt$ has the skein polynomial of the $(2,6a\pm 1)$-torus
knot $\hat \mu$. In \cite{3br} is was proved that these knots $K$
form the full list of 3-braid links with unsharp MWF inequality.
 
Consider first 
the knots $K=\hat\bt$ with $\bt=\mu^*$ for
$\mu=\sg_1^{6a+1}\sg_2^{-1}$ and $a>0$. It is easy
to bring $\bt$ into Xu's normal form, and to observe
that it has exactly one negative band. This exhibits
a Seifert ribbon (see \cite{Rudolph}) of smaller genus
than $g(K)$, i.e. $g_s(K)<g(K)$ (see also the proof of
theorem \reference{thqp}). Now from Xu's form one sees $w_{\min}
(K)=[\bt]=2g(K)$. Take this for a moment as a definition of
$w_{\min}(K)$; this writing will be justified when we
show that the writhe is unique. (One could also quote
Birman-Menasco here, but the complexity of their argument
is unnecessary.) So 
\begin{eqn}\label{iopa}
1-\chi_s(L)<w_{\min}(L)\,.
\end{eqn}
Using \eqref{mq},
we see that if \eqref{stz} is violated for some $\bt''\in B_{n'}$,
then $[\bt'']=w_{\min}(L)+2+(n'-3)$. However, by the Rudolph-
Bennequin inequality \cite{Rudolph2} (see also \cite{pos}),
we would have then 
\[
1-\chi_s(L)\ge [\bt'']-n'+1=w_{\min}(L)\,,
\]
in contradiction to \eqref{iopa}.

The effort focusses on the other braids $\bt=\mu^*$
for $\mu=\sg_1^{6a-1}\sg_2$.
In this case we consider $!K$, whose Xu form has only negative
bands. The inequalities \eqref{mq} show that we must rule out a
braid representation $\bt''\in B_{n'}$ of $!K$ with $[\bt'']=w_{\min}
(!K)+2+(n'-3)$, where (we set in the same \em{a posteriori} to
be justified manner) $w_{\min}(!K)=-2g(K)-2$.

We prohibit $\bt''$ by evaluating the 2-cable skein polynomial
$P(\hat\gm_a)$ of $!K$ for
\begin{eqn}\label{gma}
\gm_a\,=\,[4354]\cdot [2132]^{6a-1}\,(\Dl_6^2)^{-2a}\,\in\,B_6,
\end{eqn}
with $a>1$ and $\Dl_6^2=[12345]^6$ generating the center of $B_6$,
and showing that the polynomial has non-zero terms in $v$-degree
$[\gm_a]-5$ or $[\gm_a]-3$. This may appear a banality, but in
fact requires a substantial use of Jones' work in \cite{Jones}.

Consider the more general 6-braids
\[
\bt_{k,l}\,:=\,[4354]\cdot [2132]^k\,\Dl_6^{2l}\,.
\]
(We are of course only interested in the special case $k=6a-1$,
$l=-2a$ and $a>1$, but it is useful to treat the 2-parameter family
first.)

The skein polynomial of $\hat\bt_{k,l}$ can be evaluated using
the representation theory in \cite{Jones}. We adopt the convention
that \em{all references} to lemmas, page and paragraph numbers,
equations of the form ($x.y$), etc. for the rest of this proof
are understood to be \em{to Jones's paper}, unless noted otherwise.

Jones's 

version of the skein polynomial, 
\[
X(q,\lm)=P(v,z)\mbox{\quad with $v=\sqrt{\lm q}$\ \ and
\ $z=\sqrt{q}-1/\sqrt{q}$\,},
\]
can be evaluated on a closed
$n$-braid $\bt$ by a weighted sum, with weights $W_Y$ in $\lm$ and
$q$, of traces (in $q$) of irreducible representations (irreps) $\pi_Y$
of $B_n$, indexed by Young diagrams (or tableaux\footnote{Here
consistently `tableau' is used as a synonym for (Young) diagram,
i.e. with no additional information attached to it.}) $Y$, or
equivalently by partitions of $n$. (A partition of $n$ is a
tuple $(n_1,\dots,n_k)$ with $n_k>0$, $n_i\ge n_{i+1}$ and
$\sum n_i=n$.) We may identify the Young diagram with its
partition, counting partitions in horizontal rows. For
example the partition $(4)=\Young{4}$ means one row (trivial
representation), while $(1111)=\Young{1,1,1,1}$ means one column
(parity representation); thus $\pi_{3,1}=\pi_{\Young[1.5mm]
{3,1}}$. Since the calculation of $W_Y$ was given in
\cite{Jones}, we will not repeat it in detail. We will
also deal (mostly) with $Y$ where the calculation of
$\pi_Y$ is explained in \cite{Jones}.

Using Definition 6.1 (of \cite{Jones}), (5.5) and the formula
for $W_Y(q,\lm)$ from p. 347 top, one has for a 6-braid $\bt$
of exponent sum $e=[\bt]$,
\begin{eqn}\label{STR}
X_{\hat\bt}(q,\lm)\,=\,-\sqrt{\lm}^{e-5}\,\sum_{Y\vdash 6}
\wt W_Y(q,\lm)\,\tr \pi_Y(\bt)\,.
\end{eqn}
Here $\wt W_Y$ denote the slightly rescaled weights
\[
\wt W_Y(q,\lm)\,=\,\frac{R_{Y}(q,\lm)}{Q_Y(q)}\,\cdot\,
\frac{1-q}{1-\lm q}\,,
\]
with $R_Y$ being specified on p.\ 347 after Figure 5.6, and
$Q_Y(q)$ being the hook length product term from p. 346 middle.
The symbol `$\mathord{\vdash}$' is taken from partition theorists
and is used to mean here that $Y$ is a Young tableau of $6$ boxes
(or equivalently a partition of $6$).
In order to avoid denominators it is useful to multiply
\eqref{STR} by $(1-q^2)\cdot\dots\cdot(1-q^6)$, so
\begin{eqn}\label{STR2}
-(1-q^2)\cdot\dots\cdot(1-q^6)X_{\hat\bt}\,=\,
\sqrt{\lm}^{e-5}\,\sum_{Y\vdash 6}
\wh W_Y(q,\lm)\,\tr \pi_Y(\bt)\,,
\end{eqn}
with 
\[
\wh W_Y(q,\lm)\,=\,\frac{R_Y(q,\lm)}{1-\lm q}\,\cdot\,
\frac{(1-q)(1-q^2)\cdot\dots\cdot(1-q^6)}{Q_Y(q)}\,
\]
becoming a Laurent polynomial in $\lm$ and $q$\,.

Note that $\pi_Y$ are representations that involve only the
variable $q$, not $\lm$. The obvious question is how to
evaluate their traces.

Consider first 
\[
\bt_k=\bt_{k,0}\,=\,[4354]\,[2312]^k\,.
\]

There are 11 Young diagrams $Y$ of 6 boxes. Now $\bt_k\in B_4\subset
B_6$, and according to p. 340 top, the restriction of $\pi_Y$ to $B_4$
splits into a direct sum of representations $\pi_{Y'}$ indexed by
4-box Young diagrams $Y'$, which we name for shorthand
\begin{eqn}\label{shh}
A=\Young{1,1,1,1}\quad
B=\Young{2,1,1}\quad
C=\Young{2,2}\quad
D=\Young{3,1}\quad
E=\Young{4}\,.
\end{eqn}

The representations $\pi_{Y'}$ are clarified completely in \S 8
(see also \S\reference{SUn} in \em{this} paper below). Denote by
$\psi_{n-1}$ the (reduced) $(n-1)$-dimensional representation
of $B_n$; see \S 2. Let us also write $-1$ for the parity
representation $(-1)^{[\,.\,]}$, and $-\rho=-1\otimes \rho$ for the
direct (tensor, or Kronecker) product of a representation $\rho$ with
the parity. Then $\pi_A=-1$, $\pi_E$ is given by $q^{[\,.\,]}$,
$\pi_B=-\psi_3$ (Note 5.7; the sign disappears here, though,
because for us always $e=[\bt]$ is even), $\pi_D=-\bigwedge^2\psi_3$
and $\pi_E=\pi_{\Young[1.5mm]{2,1}}\circ\ol{\ry{0.6em}\es}$,
with $\ol{\es\ry{0.6em}}$ being the homomorphism $B_4\to B_3$
given by $\ol{\sg_{1,2,3}\ry{0.6em}}=\sg_{1,2,1}$ (p. 355).
Also $\pi_{\Young[1.5mm]{2,1}}=-\psi_2$.

Let us write below $\ol{Y}$ for the \em{transposed} (or \em{dual})
Young diagram to $Y$, given by exchanging rows and columns.
For example, for $Y=\Young{3,1}$, we have $\ol{Y}=\Young{2,1,1}$.
The relation between $\pi_Y$ and $\pi_{\ol{Y}}$ is given in Note
4.6.

Now $\psi_3(\ap)$ and $\psi_2(\bar\ap)$ for 
\[
\ap=[2132]
\]
are easy to
calculate (see \S 2). We find former's eigenvalues to be $\pm t$ and
$-t^2$, and latter's $t$ and $t^3$. In particular, both matrices are
diagonalizable (because the eigenvalues are distinct for generic $t$).
Setting $t=q$ as in Note 5.7, then we
have the following table of eigenvalues of the $\pi_{Y'}(\ap)$
\[
\begin{array}{|c|c|c|c|c|}
\hline
\ry{1.3em}A & B & C & D & E \\[1mm]
\hline
\ry{1.5em}1& -q   & q^3 & -q^3 & q^4 \\
	 &  q   & q   &  q^3 &     \\
	 & -q^2 &     & -q^2 &     \\[2mm]
\hline
\end{array}
\kern2cm
\begin{array}{c|*{7}{|c}}
\ry{1.2em}i & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\[1.5mm]
\hline  
\ry{1.2em}\dl_i & 1 & q^4 & q & -q & -q^2 & q^3 & -q^3\\[1mm]
\end{array}
\]
Let us number the 7 possible eigenvalues of $\pi_Y'(\ap)$ by
$\dl_i$ as shown on the right. 

Thus $\pi_Y(\ap)$ are all diagonalizable, with eigenvalues $\dl_i$.
The multiplicities of $\pi_{Y'}$ in $\pi_Y$ are also easy to
calculate. They are the number of descending paths from $Y'$ to
$Y$ in the Figure 3.3 (continued one more row to the bottom).
Table \reference{tab1} shows the multiplicities of $\pi_{Y'}$
(in the shorthand of \eqref{shh}) in $\pi_Y$ and the resulting ones,
which we write $M(i,Y)$, of the eigenvalues $\dl_i$ in $\pi_Y(\ap)$.

\begin{table}[ptb]
\captionwidth\vsize\relax
\newpage
\vbox to \textheight{\vfil
\rottab{ 
\hbox to \vsize{
\hss


$\displaystyle
\begin{array}{|c||*{11}{c|}}
\hline\ry{1.0cm}
Y & \Young{1,1,1,1,1,1} & 
\Young{2,1,1,1,1} &       
\Young{2,2,1,1} &         
\Young{2,2,2} &           
\Young{3,1,1,1} &         
\Young{3,2,1} &           
\Young{3,3} &             
\Young{4,1,1} &           
\Young{4,2} &             
\Young{5,1} &             
\Young{6} \\[6mm]         
\hline\ry{1.6em}
Y' & A & 2A+B & A+2B+C & B+C & A+2B+D & 2B+2C+2D & C+D & B+2D+E & C+2D+E
& D+2E & E \\[2mm]
\hline\ry{1.6em}


1    & 1 & 2 & 1 &   & 1 &   &   &   &   &   &   \\
q^4  &   &   &   &   &   &   &   & 1 & 1 & 2 & 1 \\
q    &   & 1 & 3 & 2 & 2 & 4 & 1 & 1 & 1 &   &   \\
-q   &   & 1 & 2 & 1 & 2 & 2 &   & 1 &   &   &   \\
-q^2 &   & 1 & 2 & 1 & 3 & 4 & 1 & 3 & 2 & 1 &   \\
q^3  &   &   & 1 & 1 & 1 & 4 & 2 & 2 & 3 & 1 &   \\
-q^3 &   &   &   &   & 1 & 2 & 1 & 2 & 2 & 1 &   \\[2mm]
\hline\ry{1.6em}
d    & 1 & 5 & 9 & 5 & 10& 16& 5 &10 & 9 & 5 & 1 \\
r    & 0 & 1 & 3 & 2 & 4 & 8 & 3 & 6 & 6 & 4 & 1 \\
30r/d& 0 & 6 &10 &12 & 12& 15& 18& 18& 20& 24& 30\\[2mm]
\hline
\end{array}
$





\hss}
}{This table displays the Young tableaux $Y$ of 6 boxes, the
decomposition into $\pi_{Y'}$ for 4-box Young tableaux $Y'$ of the
sub-representation of $B_4$ in $\pi_Y$ (writing $Y'$ for $\pi_{Y'}$),
the multiplicities $M(i,Y)$
of the 7 possible eigenvalues $\dl_i$ of $\pi_Y(\ap)$, and the
quantities $d$ ($=\dim \pi_Y$) and $r$ (rank of the idempotent
$e_i$) occurring in Jones's lemma 9.3.\label{tab1}}{table}
\vss}
\newpage
\end{table}

Since with $\pi_{Y'}(\ap)$ also all $\pi_Y(\ap)$ are
diagonalizable, we have
\begin{eqn}\label{XX}
\tr \pi_Y(\bt_k)\,=\,\tr \pi_Y(\ap^k\cdot [4354])\,=\,
\sum_{i=1}^7\,c(i,Y)\,\dl_i^k\,,
\end{eqn}
with $c(i,Y)$ given as follows. Consider $\pi_Y([4354])$ in
the basis of $\pi_Y$ that diagonalizes $\pi_Y(\ap)$. Then to
obtain $c(i,Y)$, sum the $(j,j)$-entries of the matrix
of $\pi_Y([4354])$ over rows/columns $j$, for which the
$(j,j)$-entry of $\pi_Y(\ap)$ is $\dl_i$.

So the problem to evaluate $\tr \pi_Y(\bt_k)$ transforms into
the one to determine $c(i,Y)$. There are \em{a priori} 77
of those, given by combining $7$ eigenvalues $\dl_i$ with
11 Young diagrams $Y$. However, one immediately notes that
clearly $c(i,Y)=0$ when $M(i,Y)=0$. This leaves 45 of the 77 values.

If we can calculate $\tr \pi_Y$ for general 6-braids, then we
can use \eqref{XX} as a linear equation for $c(i,Y)$.
If $\pi_Y(\ap)$ has $l_Y$ different eigenvalues, we can
determine $c(i,Y)$ for that $Y$ by calculating the l.h.s. of
\eqref{XX} for $l_Y$ different values of $k$ and solving for $c(i,Y)$.
(Always $l_Y\le 6$, as evident from table \reference{tab1}.)

In case $Y$ is one of the one-hook diagrams like $\Young{4,1,1}$,
then $\pi_Y$ is by p. 354 bottom (a tensor product of a parity,
which disappears at even exponent sum, with) an exterior power
of $\psi_5$. Thus, as in \S 7 (of Jones's paper), one can evaluate
$\tr \pi_Y(\bt_k)$ from the characteristic polynomial of the Burau
matrix $\psi_5(\bt_k)$. We determined this way the corresponding
$c(i,Y)$, and 
verified them with a few extra values of $k$ in \eqref{XX}. While
it is clear that all $c(i,Y)$ should be rational expressions in $q$,
we expected them to be in fact Laurent polynomials. So we were a bit
startled by the denominators $1+q^2$. However, according to p. 343
top, the Hecke algebra may degenerate at roots of unity $q$, which
justifies at least cyclotomic polynomials as denominators.

\begin{table}[ptb]
\captionwidth\vsize\relax
\newpage
\vbox to \textheight{\vfil
\rottab{ 
\hbox to \vsize{
\hss


$\displaystyle
\begin{array}{|c||*{11}{c|}}
\hline\ry{1.0cm}
Y & \Young{1,1,1,1,1,1} & 
\Young{2,1,1,1,1} &       
\Young{2,2,1,1} &         
\Young{2,2,2} &           
\Young{3,1,1,1} &         
\Young{3,2,1} &           
\Young{3,3} &             
\Young{4,1,1} &           
\Young{4,2} &             
\Young{5,1} &             
\Young{6} \\[6mm]         
\hline\ry{1.6em}


1 & 1 & -\left( \frac{q^4}{1 + q^2} \right)  & \frac{q^7}
   {\left( 1 + q^2 \right) \,\left( 1 + q + q^2 \right) } & 0 & 0 & 0 & 0 & \
0 & 0 & 0 & 0 \\

q^4  & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{q}
   {\left( 1 + q^2 \right) \,\left( 1 + q + q^2 \right) } & -\left( \frac{q^2}{1 + q^2} \right)  & q^4 \\

q    & 0 & \frac{1}{2} & \frac{-\left( 
       \left( -1 + q \right) \,q \right) }{2} & q + \frac{q^3}{2} & \frac{q^2 + 2\,q^4}{-2 - 2\,q^2} & \frac{q\,\left( 1 - 4\,q + q^2 \right) }
    {2} - c(6,\Young[1.5mm]{ 3,2,1} ) & 0 & \frac{q^6}{2 + 2\,q^2} & \frac{q^6}
   {1 + q + q^2} & 0 & 0 \\[2mm]

-q &   0 & \frac{1}{2} & \frac{-\left( 
       \left( -1 + q \right) \,q \right) }{2} & \frac{q^3}{2} & \frac{q^2 + 
     2\,q^4}{-2 - 2\,q^2} & \frac{{\left( 1 - q \right) }^2\,q}{2} - 
   \frac{q^2}{1 + q} - c(6,\Young[1.5mm]{ 3,2,1} ) & 0 & \frac{q^6}
   {2 + 2\,q^2} & 0 & 0 & 0 \\

-q^2 &   0 & \frac{1}{1 + q^2} & \frac{q\,
     \left( 1 + \left( -1 + q \right) \,q \right) }{1 + q^2} & -q^2 & 
-q^2 & q\,\left( 1 + \left( -1 + q \right) \,q \right)  & -q^2 & -q^2 & \frac{q^3\,\left( 1 - q + q^2 \right) }{1 + q^2} & \frac{q^6}
   {1 + q^2} & 0 \\[2mm]
   
q^3 &   0 & 0 & \frac{1}{1 + q + q^2} & 0 & \frac{1}
   {2 + 2\,q^2} & c(6,\Young[1.5mm]{ 3,2,1} ) & \frac{q}{2} + q^3 & \frac{-\left( q^2\,
       \left( 2 + q^2 \right)  \right) }{2\,\left( 1 + q^2 \right) } & \frac{\left( -1 + q \right) \,q^2}{2} & \frac{q^4}
   {2} & 0 \\[3mm]
-q^3 &   0 & 0 & 0 & 0 & \frac{1}{2 + 2\,q^2} & \frac{q^2}{1 + q} + 
   c(6,\Young[1.5mm]{ 3,2,1} ) & \frac{q}{2} & \frac{-\left( q^2\,
       \left( 2 + q^2 \right)  \right) }{2\,\left( 1 + q^2 \right) } & \frac{\left( -1 + q \right) \,q^2}{2} & \frac{q^4}{2} & 0 \\[2mm]
\hline
\end{array}
$





\hss}
}{This table shows the values $c(i,Y)$ of \eqref{XX} for Young tableaux
$Y$ of 6 boxes and the 7 possible eigenvalues $\dl_i$ of $\pi_Y(\ap)$.
\label{tab2}}{table}
\vss}
\newpage
\end{table}

For $Y=\Young{2,2,2}$, $\pi_Y$ was written down directly on p. 362,
and for its transposed (dual) Young diagram $\Young{3,3}$, one
uses Note 4.6. 

There remain 3 representations, for $Y=\Young{3,2,1}$,
$\Young{4,2}$, and its dual $\Young{2,2,1,1}$, with a total of
15 unknown $c(i,Y)$. These were more complicated to find, since
we knew of no way to evaluate $\tr \pi_Y$ directly. To help
ourselves, first observe that we have, for fixed $Y$, the trace
identities
\begin{eqn}\label{tri}
\sum_{i=1}^7\,c(i,Y)\,=\,\tr \pi_Y([4354])\,=\,
\tr \pi_Y([2132])\,=\,\sum_{i=1}^7 M(i,Y)\dl_i\,,
\end{eqn}
which again give a linear condition on the $c(i,Y)$. To find
further identities, we used \eqref{STR2} in a ``backward'' manner.
We calculated for small\footnote{In the parametrization $P(v,z)$,
used by Morton-Short, unlike for $X$, the coefficients of
$P(\hat\bt_{k,l})$ become quickly large and produce machine
size integer overflows. In particular, we could not calculate
correctly polynomials for $|l|>2$.} $k,l$ ($k$ odd, $|k|\le 5$,
$|l|\le 1$) the polynomial on the left using Morton-Short's
program \cite{MorSho2}. We substituted the known $c(i,Y)$ on
the right of \eqref{STR2}, obtaining thus linear conditions
for the yet unknown $c(i,Y)$. To determine the coefficients,
it remains to understand the effect on $\tr\pi_Y$ of multiplying
with the full twist $\Dl_6^2$. This was, however, done also by
Jones in \S 9, lemma 9.3:
\begin{eqn}\label{l93}
\pi_Y(\Dl_n^2)\,=\,q^{rn(n-1)/d}\,Id_{\pi_Y}\,.
\end{eqn}
For given $Y$, the number $r=r_Y$ is calculated as in lemma 9.1
from figure 3.3, and $d=d_Y=\dim \pi_Y$ more easily by the hook
length formula on p. 341. Call $e_Y=n(n-1)r/d$ (with $n=6$) the
exponent\footnote{This is not to be confused with the variable
$e$, which we use for exponent sum of a braid, or with the
idempotent $e_i$ from Jones's lemma 9.1.} of $q$ on the right
hand-side of \eqref{l93}. These values are given in table
\ref{tab1}. Two simple checks are $\sum\limits_{Y\vdash n}d_Y^2=
n!$ (because the multiplicity of each irrep in the Hecke algebra
equals its dimension), and that $e_Y$ are integers (Remark on p. 358
bottom) and satisfy $e_{Y}+e_{\ol{Y}}=n(n-1)$ for all $Y$
(because of Note 4.6). So \eqref{STR2} gets
\begin{eqn}\label{STR3}
-
(1-q)\cdot\dots\cdot(1-q^6)\,X(\hat\bt_{k,l})(q,\lm)\,=\,
\sqrt{\lm}^{e-5}\,\sum_{Y\vdash 6}\,\wh W_Y(q,\lm)\,
q^{l\cdot e_Y}\,\sum_{i=1}^7\,c(i,Y)\,\dl_i^k\,,
\end{eqn}
with $e=[\bt_{k,l}]=4+4k+30l$.

Actually, each polynomial
$X(\hat\bt_{k,l})$ gives 6 equations for $c(i,Y)$, because
there are 6 relevant $\lm$-coefficients on both hand-sides
of \eqref{STR2} (in degrees $\ffrac{e-5}{2}$, $\ffrac{e-3}{2}$,
\dots, $\ffrac{e+5}{2}$\,; it is helpful to multiply again by
$(1+q^2)$ to get disposed of the denominators of the known
$c(i,Y)$). We have with 18 polynomials 111 equations (6 equations per
polynomial plus the three relevant trace equations \eqref{tri}).
Still the resulting system was too hard to solve by computer, using 
MATHEMATI\-CA\TM{} \cite{Wolfram}, since its coefficients are
(Laurent) polynomials in $q$, with dozens of terms each.

However, substituting some (rational) values of $q$, the system
can be solved immediately. We used this to check first the rank of
the matrix (i.e. which equations are linearly redundant). Again we
were surprised that for 15 variables $c(i,Y)$ the rank was only
$14$. This, however, can be explained from our restraint to odd
$k$ (which we chose for some, purely technical,
component number concerns in the calculation
with Morton-Short's program). Whenever two opposite eigenvalues
$\dl_i$ and $\dl_{i'}=-\dl_i$ occur in $\pi_Y(\ap)$, the equations
\eqref{STR2} for odd $k$ can detect only $c(i,Y)-c(i',Y)$. The
trace equations \eqref{tri}, which involve $c(i,Y)$ and $c(i',Y)$
with the same sign, remedy the shortcoming for $\Young{4,2}$ and
its transposed diagram, but for $\Young{3,2,1}$ we have two pairs
$(i,i')$ of opposite eigenvalues, so we still lose one dimension.
This is, however, not really a problem, because in the
braids $\gm_a=\bt_{6a-1,-2a}$ of \eqref{gma} we
need for our proof, $k=6a-1$ is always odd, so we need only
$c(i,Y)-c(i',Y)$ to evaluate the polynomial in \eqref{STR2}.

We used the special evaluations to select equations that give
the full matrix rank, and to guess the formula for general $q$
for some of the $c(i,Y)$. (The ones we already found suggest that
these formulas should not be so complicated.) Substituting these
(yet potential) solutions too, gives an even simpler linear system
for the still unknown $c(i,Y)$, which then could be solved in $q$.

Since we know that our matrix has rank 14, it is enough to check
our solution (up to the 1-dimentional ambiguity, which will
disappear in \eqref{STR2}) with the 111 equations we have. The
result was confirmed, and is shown in table \ref{tab2}.

With all $c(i,Y)$ determined, the main work is done.
So far we can evaluate $X(\hat\bt_{k,l})$ for odd $k$.
Multiplying \eqref{STR3} by $Z=(1+q)(1+q^2)(1+q+q^2)$ to clear
all denominators in the $c(i,Y)$, normalizing and taking
coefficients in $\lm^m$ for $m=0,\dots,5$, we have
(with $e_Y$ being the exponents of $q$ in \eqref{l93} and
$e=[\bt_{k,l}]$)
\begin{eqn}\label{OPI}
\left[-\frac{1}{\sqrt{\lm}^{e-5}}\,\cdot\,Z\,\cdot\,
(1-q)\cdot\dots\cdot(1-q^6)\,
X_{\hat\bt_{k,l}}(q,\lm)\,\right]_{\lm^m}\,=\,
\sum_{Y\vdash 6}\,\sum_{i=1}^7\,
(Z\cdot c(i,Y))\,\dl_i^k\,
q^{l\cdot e_Y}\,\bigl[\wh W_Y(q,\lm)\,\bigr]_{\lm^m}\,.
\end{eqn}

Recall that for our proof it is enough to show that this term
becomes non-zero for $m=0$ or $m=1$, when $k=6a-1$ and $l=-2a$
for an integer $a>1$ (and $\bt_{k,l}=\gm_a$ in \eqref{gma}).
Now, for odd $k$ (and fixed $Y$), we can group
the sum over $7$ terms $Z\cdot c(i,Y)$ into 5 terms $\tl c(i,Y)$
accounting for $\dl_3=-\dl_4$ and $\dl_6=-\dl_7$, and thus
excluding $i=4,7$. So the above sum in \eqref{OPI} becomes
\begin{eqn}\label{yy}
\sum_{Y\vdash 6}\,\sum_{\scbox{\shortstack{$i=1$\\$i\ne 4$}}}^6
\tl c(i,Y)\dl_i^k\,q^{l\cdot e_Y}\,\bigl[\wh W_Y(q,\lm)\,\bigr]
_{\lm^m}\,.
\end{eqn}
(Now in the $\tl c(i,Y)$, the 1-degree ambiguity of $c(i,Y)$ for
$Y=\Young{3,2,1}$, as explained above, cancels out.)

Among the 55 possible $(i,Y)$ (with $i\ne 4,7$), only 21
of the $\tl c(i,Y)$ are non-zero. It turns out that for $m=0$,
when $k=6a-1$, $l=-2a$ and $a>1$, there is a unique term among
the 21 summands in \eqref{yy} whose minimal degree in $q$ is the
smallest (it is $14-36a$). Thus $[P(\hat\bt_{k,l})]_{v^{e-5}}\ne 0$.
We calculated the polynomial with Morton-Short's program for $a=2$
(where the calculation was still feasible), and it confirmed that
all 6 $v$-terms appear. We also calulated that for $m=0$ and
$a=0,1$ there are two terms of smallest minimal degree. This
better ought to be so, because in that case $\hat\gm_{a}$ are just
a 2-cable of the unknot and $!5_1$, resp., and the coefficients
for $m=0,1$ in \eqref{yy} must be $0$, which we checked once
more separately. (Also we found that for $m=1$ there are two
terms of smallest minimal degree in \eqref{yy} for all $a\ge 0$.)
With this the proof of theorem \reference{thJC} is complete.

Let us finally say that the computer part of the calculation owed
a lot to the use of MATHEMATI\-CA. While, if done properly, it could
be carried out in a few minutes, it required a week of work to
find the way of skillfully programming MATHEMATI\-CA
to do all the separate steps in an efficient way. \qed

\begin{rem}
Note that one could handle the cases $\mu=\sg_1^{6a+1}\sg_2^{-1}$
from the beginning of the proof also using the representation
theoretic argument, by looking at $m=4,5$ for $a<0$. We waived on
this investigation, though, since the proof for $a>0$ was laborious
enough.
\end{rem}
