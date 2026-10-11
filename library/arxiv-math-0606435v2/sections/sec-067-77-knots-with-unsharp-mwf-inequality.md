---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-067-77-knots-with-unsharp-mwf-inequality
section_title: "Knots with unsharp MWF inequality"
section_number: 7.7
pages: 60-64
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.992
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


\section{Postliminaries}
}



\subsection{Fibered Dean knots (Hirasawa-Murasugi)\label{HM}}

Here we present some material due to Hirasawa and Murasugi,
who studied fibering of generalized Dean knots. An overview is given
in \cite{Hirasawa}. As this is work in progress, a longer exposition
may appear subsequently elsewhere.

\begin{defi}
The Dean knot $K(p,q|r,rs)$ is given by the closed $p$-braid
\[
(\sg_{p-1}\sg_{p-2}\cdots \sg_1)^{q}(\sg_1\sg_2\cdots \sg_{r-1})^{rs}\,,
\]
with $p>r>1$ and $q,s$ non-zero integers such that $(q,p)=1$.
\end{defi}

Hirasawa and Murasugi proposed a conjecture on these knots
and obtained so far the following partial results.
 
\begin{conjecture}(Hirasawa-Murasugi)
A Dean's knot $K(p,q|r,rs)$ is a fibred knot if and
only if its Alexander polynomial is monic, that is,
$\Mc\Dl=\pm 1$.
\end{conjecture}

\begin{figure}[th]
\[
\begin{array}{ccc}
\epsfs{6cm}{fig2a} & 
\epsfs{5cm}{fig2b} & 
\epsfs{5cm}{fig2c}\\
 (a) & (b) & (c) \\
\end{array}
\]
\caption{\label{fig2}}
\end{figure}

\begin{prop}(Hirasawa-Murasugi)
This conjecture has been proven for the following cases.
\def\theenumi{\alph{enumi}}
\def\labelenumi{(\theenumi)}
\begin{enumerate}
\item     $q = kp + 1$, and $r$ and $s$ are arbitrary,
\item     $q =kp - 1$, and  $r$ and $s$ are arbitrary,
\item     $r =  p - 1$, and  $q$ and $s$ are arbitrary.
\end{enumerate}
\end{prop}

The last case implies in particular that the conjecture is
true for $p=3$. Below follows a part of the argument in this
case that settles lemma \reference{lki}. (Other parts of their
proof are very similar to some of our previous arguments.
It seems, for example, that Hirasawa and Murasugi were to
some extent aware of Theorem \reference{Thq}.)

\proof [of lemma \reference{lki}] We consider the braids $[(123)^k-2]$,
with $k>0$ fixed. By isotopies and Hopf plumbings, we modify our
surface 
\begin{eqnarray*}



&\rx{-1mm} [(123)^k -2] \to [(1223)^k - 2]=[12(2312)^{k-1}23 - 2] \to
[(2312)^{k-1}23 - 212] = [(2312)^{k-1}2312 -1]=[(2312)^k - 1].
\end{eqnarray*}
Let $F$ be the surface of the band representation $\bt=[(2312)^k-1]$.
We will show that $F$ is a fiber surface.

Consider the subsurface $F_0$ of $F$ that spans $[2 3 1 2]$
in the natural manner.
We deform the $k$ copies of $F_0$ to the (isotopic sub)surfaces
$F'_0$ by a series of diagrams, see figure \reference{fig2}.
(Here strands are numbered from right to left and words composed
downward.)

In figure \reference{fig2}, for the move (a) $\to$ (b), we slide
$B$ and $C$, respectively, along $D$ and $A$, then delete $D$
(by deplumbing a Hopf band), and then slide $C$ back along
$A$. For the move (b) $\to$ (c), we slide $C$ along $B$,
then slide $B$ along $C$. The $k$ bands $A$ can be subsequently
removed by Murasugi desumming a $(2,k)$-torus link fiber surface.
Thus the surface $F$, spanned by $\hat\bt$, turns after
(de)summing Hopf bands into a surface $F'$ consisting of $k$
copies of $F'_0$ and one negative band $N$. See figure \ref{fig3} (a).
 

{

\def\@captype{figure}
\long\def\@makecaption#1#2{
   
   \vskip 10pt
   {\let\label\@gobble
   \let\ignorespaces\@empty
   \xdef\@tempt{#2}
   
   }
   \ea\@ifempty\ea{\@tempt}{
   \setbox\@tempboxa\hbox{
      \fignr#1#2}
      }{
   \setbox\@tempboxa\hbox{
      {\fignr#1:}\capt\ #2}
      }
   \ifdim \wd\@tempboxa >\captionwidth {
      \rightskip=\@captionmargin\leftskip=\@captionmargin
      \unhbox\@tempboxa\par}
   \else
      \hbox to\captionwidth{\hfil\box\@tempboxa\hfil}
   \fi}








\
\captionwidth0.3\textwidth\relax
\[
\begin{array}{cc@{\qquad}c}
\epsfs{5cm}{fig3a} & \epsfs{5cm}{fig3b} & \epsfs{5cm}{surf} \\
(a) & (b) \\[-2mm]
\multicolumn{2}{c}{ \vbox{\caption{\label{fig3}}} } &
\raisebox{1em}{\vbox{\caption{\label{fig4}}}}
\end{array}
\]

}

In figure \reference{fig3}, we perform the move (a) $\to$ (b), sliding
$B$ along $N$. The last surface $F'$, in figure \reference{fig3} (b),
is Murasugi sum of a fibre surface spanning the $(2,2,-2)$-pretzel
link and $\tl F$, where $\tl F$ consists 
of $k - 1$ copies of $F'_0$ and the band $N$. By induction on
$k$, we see that $F'$ is a fibre surface, and hence $\hat\bt$
is a fibred link. \qed
 

\subsection{$A$-decomposition (joint with Hirasawa-Ishiwata)\label{HI}}

For the proof of theorem \reference{thuq} we introduce the
$A$-decomposition due to T.~Kobayashi \cite{Kobayashi}.

A \em{sutured manifold} in the sense of Gabai \cite{Gabai3} can be
understood as a pair $(L,H)$ consisting of a closed 3-dimensional
submanifold $H$ of $\bR^3$ with boundary $S=\prt H$ a connected
surface, and a set of oriented loops $L\subset H$. We require that
one can orient the connected components of $S\sm L$ so that the
induced orientations on $L$ coincide from both sides of $L$ (in
particular a connected component of $S\sm L$ never bounds to itself
along a loop of $L$), and are given by the orientation of $L$.

Let $F$ be a connected Seifert surface of a(n oriented) link $L=\prt
F$. We embed $F$ as $F\times\{0.5\}$ into the \em{bicolar} $H=
F\times I$ (with $I=[0,1]$). Then $(L,H)$ becomes a sutured
manifold. We call it \em{canonical sutured manifold} $C(F)$ of $F$.

We describe some basic operations on sutured manifolds $(L,H)$.

A \em{decomposition disk} $D$ is a disk with $P=\prt D\subset \prt
H$, properly embedded in the complement of $H$ (i.e. $D\cap H=P$).
We require that $D$ is not parallel to $S=\prt H$, and
satisfies $P\cap F\ne\vn$. We assume also that the intersection of
$P$ and $F$ is transversal, so that it is a collection of points.

Since $L=\prt F$ is separating on $S$, the intersection $D\cap L= P
\cap F$ is an even number of points, and the orientation of $L$ at
the intersection points is alternating (with respect to the
orientation of the loop $P$). See figure \reference{fig5} (a).

\begin{figure}[th]
\[
\begin{array}{c@{\kern1.4cm}c}
\diag{1cm}{3}{3}{
  \piccircle{1.5 d}{0.6}{$D$}
  \pictranslate{1.5 1.5}{
    { \piclinedash{0.05 0.05}{0.02}
      \picmultigraphics[rt]{4}{90}{
        \picline{0.0 0.6}{-0.3 1.4}
      }
    }
    \picputtext{0.4 0.9}{$L$}
    \picmultigraphics[rt]{2}{180}{
      \picvecline{0.3 1.4}{0.0 0.6 0.3 1.4 0.5 conv}
      \picline{0.0 0.6}{0.0 0.6 0.3 1.4 0.5 conv}
      \picrotate{90}{
        \picvecline{0.0 0.6}{0.0 0.6 0.3 1.4 0.5 conv}
        \picline{0.3 1.4}{0.0 0.6 0.3 1.4 0.5 conv}
      }
    }
  }
}
&
\diag{1cm}{2.5}{2.0}{
  \picline{1 0}{1 2}
  \picline{0 0.5}{1 0.5}
  \picvecline{2 0.5}{1 0.5}
  \picvecline{0 1.5}{2 1.5}
  \picputtext{1 2.3}{$D$}
  \picputtext{2.3 0.5}{$L$}
  \picputtext{2.3 1.5}{$L$}
  \picputtext{0.8 1.0}{$a$}
}\quad\lra\quad
\diag{1cm}{2}{2.0}{
  \picline{1 0}{1 2}
  \picputtext{1 2.3}{$D$}
  \pictranslate{1 1}{
    \picmultigraphics[rt]{2}{180}{
      \picline{1 -0.5}{0.2 -0.5}
      \piclineto{0.2 0.5}
      \picveclineto{1 0.5}
    }
  }
}   
\\
\ry{1.7em}(a) & \raisebox{0.8em}{$(b)$} \\
\end{array}
\]
\caption{\label{fig5}}
\end{figure}

Then $L\cap P$ separates $P$ into a collection of intervals or
\em{arcs}. Let $a$ be such an arc. An \em{$A$-operation} on $D$ along
$a$ is a transformation of $(L,H)$ into a sutured manifold $(L',H)$,
where $L'$ is obtained by splicing $L$ along $a$. See figure
\ref{fig5} (b).

A \em{product decomposition} along $D$ is a similar operation, due
to Gabai \cite{Gabai3}, and can be described as an $A$-operation
if $|L\cap D|=2$ (in which case which of the two arcs is chosen
is irrelevant), followed by a subsequent gluing of a $D^2\times I$ into
$H$ along a neighborhood $N(P)\simeq S^1\times I$ of $P$ on $S$.

\begin{defi}
We define a sutured manifold $(L,H)$ to be \em{$A$-decomposable} as
follows:
\def\theenumi{\arabic{enumi}}
\def\labelenumi{\theenumi)}
\begin{enumerate}
\item Assume $H$ is a standardly embedded handlebody (i.e. so that
$\ol{S^3\sm H}$ is also one). If $L$ is a collection of trivial loops
on $\prt H$, and all loops bound \em{disjoint} disks in $\prt H$,
then $(L,H)$ is $A$-decomposable.

\item If $(L',H')$ is obtained from $(L,H)$ by a product decomposition
(along some decomposition disk $D$),
and $(L',H')$ is $A$-decomposable, then so is $(L,H)$.

\item Let $D$ be a decomposition disk of $H$ with $|L\cap D|=2n$ and
choose among the $2n$ arcs on $P=\prt D$ a collection of $n$ cyclically
consecutive arcs $a_1,\dots,a_n$. (Consecutive is to mean that, taken
with their boundary in $L\cap P$, their union is a single interval
in $P$, and not several such intervals.) Let $(L_i,H)$ be obtained
from $(L,H)$ by $A$-decomposition on $D$ along $a_i$ for $i=1,\dots,n$.
Then if all $(L_i,H)$ are $A$-decomposable, so is $(L,H)$.
\end{enumerate}
\end{defi}

\begin{theorem}(T.~Kobayashi \cite{Kobayashi}, O.~Kakimizu
\cite{Kakimizu}) 
\def\theenumi{\arabic{enumi}}
\def\labelenumi{\theenumi)}
\begin{enumerate}
\item A fiber surface is a unique incompressible surface.
\item The property a surface to be a unique incompressible surface 
  is invariant under Hopf (de)plumbing.
\item If $C(F)$ is $A$-decomposable, then $F$ is a
  unique incompressible surface for $L=\prt F$.
\end{enumerate}
\end{theorem}

\begin{figure}
\[
\epsfsv{4.5cm}{dec1} \stackrel{a_1}{\lra} \epsfsv{4.7cm}{dec2}
\]
\[
\epsfsv{4.5cm}{dec3} \qquad \epsfsv{4.5cm}{dec4} 
\]
\[
\epsfsv{4.5cm}{dec5} \qquad \epsfsv{4.5cm}{dec6}
\]
\[
\epsfsv{4.2cm}{dec7} \qquad \epsfsv{4.2cm}{dec8}
\]
\[
\epsfsv{3.5cm}{dec9} \qquad \epsfsv{3.7cm}{dec10}
\]
\[
\epsfsv{3.5cm}{dec11} \qquad \epsfsv{3.2cm}{dec12}
\]
\caption{\label{fig6} This sequence of diagrams describes the
$A$-decomposition along arc $a_1$ of the canonical sutured
manifold corresponding to the surface in figure \reference{fig4}.
The $A$-operation is the change between the first and the second
diagram. The following diagrams (left to right in each row)
display isotopies and product decompositions, leading finally to
a trivial curve on a torus. The $A$-operation along $a_2$
must be performed too, but the decomposition is similar.}
\end{figure}

Now we complete the proof of theorem \reference{thuq}.

\proof[of theorem \reference{thuq}] 
Let $L$ be a 3-braid link. If $L$ is split, the splitting sphere
also splits any incompressible surface for $L$. Since
$L$ is a split union of a 2-braid link and an unknot
(incl.~2 and 3-component unlinks), the claim is easy.
Excluding split links, corollary \reference{cbd} shows we
need to consider only connected Seifert surfaces. It also
suffices to deal with the non-fibered links only. These are
equivalent under Hopf (de)plumbing to some of $(123)^k$ ($k\ne
0$). For such links, we can modify the transformation of
Hirasawa and Murasugi from \S\reference{HM}. Then we can turn
by Hopf (de)plumbing the surfaces into those like in figure
\reference{fig3} (a), consisting of $k$ copies of $F_0'$, but
now \em{without} the lower band $N$. (Figure \reference{fig4}
shows the case $k=4$.) Then we use $A$-decomposition, as
shown in figure \reference{fig6}. One applies $A$-operations
along the arcs $a_{1,2}$. We show only the result for $a_1$,
the case of $a_2$ and other $k$ is analogous. \qed

\end{appendix}




{\small
