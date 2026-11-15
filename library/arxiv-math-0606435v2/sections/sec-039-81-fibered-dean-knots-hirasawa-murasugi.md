---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-039-81-fibered-dean-knots-hirasawa-murasugi
section_title: "Fibered Dean knots (Hirasawa-Murasugi)"
section_number: 8.1
pages: 61-63
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.882
latex_coverage_ratio: 0.961
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
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
