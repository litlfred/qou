---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-014-51-non-alternating-montesinos-knots-up-to-nine-c
section_title: "Non-alternating Montesinos knots up to nine crossings"
section_number: 5.1
pages: 23-25
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 1.0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
Table 2 summarizes the relevant information 
about these knots.
The Jones slopes and  the sets of cluster points 
$\{2b_K(n)\}', \{2b_K^{*}(n)\}'$ were obtained from Garoufalidis' paper \cite{Ga-slope}.
The corresponding
boundary slopes together with the values $\chi(S)$ and $\abs{\partial S}$ were obtained using Dunfield's program for calculating boundary slopes of Montesinos knots \cite{ndunfield}.
In all cases,  Conjectures \ref{conj} and \ref{slopeaug} are easily verified for the knots and their mirror images.
Note that, for example, for $9_{44}$
we have $a/b=14/3 \in js_K$, $\{2b_K(n)\}'=\{-2, -8/3\}$, and $\frac{\chi(S)}{{\abs{\partial S} b}} =\frac{-6}{3}=-2$ as predicted
by  Conjecture \ref{slopeaug}. However, this assertion alone  doesn't guarantee that $b_K(n)\le 0$. Thus,
in general,   Conjecture \ref{slopeaug} does not imply Conjecture \ref{conj}.

\begin{table}[]
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
$K$& $js_K$ & $jx_{K}$ & $\chi(S)$ & $|\partial{S}|$ & $js^*_K$ & $jx_K^*(n)$ & $\chi(S^*)$ & $|\partial{S^*}|$\\
\hline
$8_{19}$ & $\{12\}$ &   $\{0\}$ & $0$ & $2$ & $\{0\}$ & $\{5\}$ & $-5$ & $1$ \\
\hline
$8_{20}$ &$\{ 8/3\}$  &$\{-1, -5/3\}$  & $-3$ & $1$ & $\{-10\}$& $\{4\}$ &$-4$ &$1$\\
\hline
$8_{21}$ & $\{1\}$ &  $\{-2\}$ & $-4$ & $2$ & $\{-12\}$ & $\{3\}$ &$-3$ &$1$\\
\hline
$9_{42}$  & $\{6\}$ &  $\{-1\}$ & $-2$ & $2$ & $\{-8\}$ & $\{5\}$ &$-5$ &$1$\\
\hline
$9_{43}$  & $\{ 32/3\}$ &  $\{-1, -5/3\}$ & $-3$& $1$ & $\{-4\}$& $\{5\}$ &$-5$ &$1$\\
\hline
$9_{44}$ & $\{ 14/3\}$ & $\{-2, -8/3\}$  &$-6$ &$1$ & $\{-10\}$ & $\{4\}$ &$-4$ &$1$\\
\hline
$9_{45}$  & $\{ 1\}$ &  $\{-2\}$ &$-4$ &$2$ & $\{-14\}$& $\{4\}$ &$-4$&$1$\\
\hline
$9_{46}$  & $\{ 2\}$ &  $\{-1\}$ &$-2$ &$2$& $\{-12\}$ & $\{5\}$ &$-5$&$1$\\
\hline
$9_{48}$ & $\{11\}$ &  $\{-3\}$ &$-6$ & $2$ &$\{-4\}$& $\{3\}$ &$-3$&$1$\\
\hline
 \end{tabular}
\vskip 0.3in 
\caption{Non-alternating Montesinos knots up to nine crossings.}
\end{center}
\end{table}

\begin{corollary}\label{conjcables} Suppose that $K\in \{ 8_{19},  8_{21}, 9_{42}, 9_{45}, 9_{46},
9_{48}, 9_{49} \}$ and let $K'$ be an iterated cable of $K$. Then, Conjectures \ref{conj} and  \ref{slopeaug}
hold true for $K'$.
\end{corollary}
\begin{proof}
We first note that $
d_+[J_{K}(n)]=an^2+bn+d(n)
$
is a quadratic quasi-polynomial of period $\le 2$, with $4a \in \BZ, 2b \in \BZ$ and $b \le 0$. Suppose
${K_{p,q}}$ is cable of $K$.
Theorem \ref{thm-quasi} and the proof of Proposition \ref{quasi} then imply that 
$$
d_+[J_{K_{p,q}}(n)]=An^2+Bn+D(n)
$$
is a quadratic quasi-polynomial of period $\le 2$, with $4A \in \BZ, 2B \in \BZ$ and $B \le 0$.
Moreover, the proof of Proposition \ref{quasi} shows that one of the following is true:
\begin{enumerate}
\item We have $4A=pq$ and $B=0$.
\item We have $4A=4q^2a$ and $2B=2 \abs{q} b+ (1- \abs{q}) \abs{4aq-p}$.

\end{enumerate}
 In case (1), a surface $S$ with boundary slope $pq$ is the cabling annulus; thus $\chi(S)=0=2B$
and Conjectures \ref{conj} and  \ref{slopeaug} are satisfied.
In case (2),  let $S$ be a surface that satisfies Conjecture \ref{slopeaug}
for $K$. We view $\M$ as the union of $M_K$ and a cable space $\C$.
An essential  surface $S'$ realizing the boundary slope $4A=4q^2a$ for $\K$ 
is obtained by Theorem \ref{main:bs}. This surface is constructed as in the proof of Lemma \ref{glue}.
By  Corollary \ref{integers} we see that $\abs{\partial S'}=\abs{\partial S}$,
$\abs {S'\cap T_{+}}=\abs{q} \, \abs{\partial S}$ and
$$\chi(S')=\chi(M_K\cap S')+\chi(\C \cap S')=\abs{q}  \chi(S)+\abs{\partial S} \, \abs{4aq-p} (1- \abs{q} ).$$
By assumption, $\chi(S)=\abs{\partial S} (2b)$.
Combining the last  two equations with the formula in (2) above, we have
$$\chi(S')=\abs{\partial S} \left( 2 \abs{q} b+ (1-\abs{q}) \abs{4aq-p}\right)=\abs{\partial S'}(2B),$$
which shows that $S'$ satisfies Conjecture \ref{slopeaug}.

Applying the above argument repeatedly we obtain the result for iterated cables.
\end{proof}
