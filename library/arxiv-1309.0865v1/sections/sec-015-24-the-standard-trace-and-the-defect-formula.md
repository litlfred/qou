---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-015-24-the-standard-trace-and-the-defect-formula
section_title: "The standard trace and the defect formula"
section_number: 2.4
pages: 16-18
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.937
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-defectformula}


A \emph{trace} on $\HB$ is a $\Zvv$-linear map $\e \co \HB \to \Zvv$ satisfying $\e(hh') = \e(h'h)$ for all $h,h' \in \HB$. A straightforward calculation shows that the map $\e(\sum c_w
H_w) = c_e$ is a trace, called the \emph{standard trace}. There is a nice combinatorial formula for the standard trace of a product $\un{H}_{\un{w}}$, known
as the \emph{defect formula}, which we now discuss.

A \emph{subsequence} of $\un{w} = s_1s_2\dots s_m$ is a sequence $\pi_1 \pi_2 \dots \pi_m$ such that $\pi_i \in \{ e, s_i \}$ for all $1 \le i \le m$. Instead of working with subsequences,
we work with the equivalent datum of a sequence $\eb = \eb_1 \eb_2 \dots \eb_m$ of 1's and 0's giving the indicator function of a subsequence, which we refer to as a \emph{01-sequence}.

We can also think of $\eb$ as a roadmap for a gentle stroll through the Bruhat graph (with much pausing to admire the scenery). This \emph{Bruhat stroll} is the sequence $x_0=e, x_1,
\dots, x_m$ defined by \[ x_i \define s_1^{\eb_1} s_2^{\eb_2} \dots s_i^{\eb_i} \] for $0 \le i \le m$. We call $x_m$ the \emph{end-point} of the Bruhat stroll, and denote it by $\un{w}^{\eb}$. Alternatively, we will say that a subsequence $\eb$ of $\un{w}$ \emph{expresses} the end-point $\un{w}^{\eb}$.
The Bruhat stroll allows us to decorate each index of $\eb$ with an additional token, either U(p) or D(own). If $\eb_i=1$ so that $x_i = x_{i-1}s_i$, then we assign U to $i$ if $x_i >
x_{i-1}$ (so that we moved up in the Bruhat order at time $i$) or D if $x_i < x_{i-1}$ (so that we moved down at time $i$). If $\eb_i=0$ so that $x_i = x_{i-1}$, we glance longingly in the
direction of $x_{i-1}s_i$ but remain unmoved: we assign U or D to the index $i$ according to whether $x_{i-1}s_i > x_{i-1}$ or $x_{i-1}s_i < x_{i-1}$. The \emph{defect} of a 01-sequence
$\eb$, denoted $d(\eb)$, is defined to be the number of U0's minus the number of D0's. It measures the defect between where we longed to go and where we actually went.

\begin{ex} \label{ex:defects}
Here are some examples of subexpressions, end-points and defects:
  \begin{itemize}
  \item Suppose that $\un{w}=sss$. There are four subsequences with end-point $e$: $(U1,D1,U0)$ and $(U0,U1,D1)$ with defect $1$, $(U1,D0,D1)$ with defect $-1$, and $(U0,U0,U0)$
with defect $3$. There are four subsequences with end-point $s$: $(U1,D1,U1)$ and $(U0,U1,D0)$ with defect $1$, $(U1,D0,D0)$ with defect $-2$, and $(U0,U0,U1)$ with defect $2$.
  \item Suppose that $\un{w} = sts$ and that $m_{st}  = 3$. There are unique subexpressions with endpoints $sts, ts, st$ and $t$ with defects $0$, $1$, $1$ and $2$ respectively. There are two subexpressions $(U1, U0, D0)$ and $(U0, U0, U1)$ with end-point $s$ of defects $0$ and $2$ respectively, and two subexpressions $(U1, U0, D1)$ and $(U0, U0, U0)$ with end-point $e$ with defects $1$ and $3$ respectively.
  \end{itemize}
\end{ex}

The defect is useful because of the following lemma of Deodhar \cite{DD}:

\begin{lem} \label{lem:defects}
For any expression $\un{w}$ we have
\[
\un{H}_{\un{w}} = \sum v^{d(\eb)}H_{\un{w}^{\eb}}
\]
where the sum runs over all 01-sequences of length $\ell(\un{w})$.
\end{lem}

\begin{proof}(Sketch) It is an straightforward consequence of \eqref{rank1heckestd'} that in $\HB$ we have the relation
\[
H_x\un{H}_s = \begin{cases} H_{xs} + vH_{x} & \text{if $xs > x$,} \\
H_{xs} + v^{-1}H_x & \text{if $xs < x$.} \end{cases}
\]
We conclude that if the lemma is true for $\un{w} = \un{x}$ it is also true for $\un{w} = \un{x}s$. The result now follows by induction.
\end{proof}

We now come to the defect formula for the trace:

\begin{cor}\label{cor:defects}
For any expression $\un{w}$ we have
\[ \e(\un{H}_{\un{w}}) = \sum v^{d(\eb)} \]
where the sum is over all 01-sequences expressing the identity element.\end{cor}

\begin{ex} We continue Example \ref{ex:defects} and check Lemma \ref{lem:defects}:
  \begin{itemize}
  \item Using relation \eqref{rank1hecke} we see that
\[
\un{H}_s^3=(v+v^{-1})^2\un{H}_s = (v^{-2} + 2 + v^2)H_s + (v^{-1}+2v+v^3)H_e.
\]
  \item Using direct calculation, or smoothness and \eqref{rank2hecke}, or Lemma \ref{lem:defects} we obtain
\[
\un{H}_s\un{H}_t\un{H}_s = H_{sts} + vH_{ts} + vH_{st} + v^2H_t + (1+v^2)H_s + (v+v^3)H_e.
\]
  \end{itemize}
\end{ex}

It will be important later that the set of subsequences $\eb$ of a fixed expression $\un{w}$ is equipped with a partial order, the \emph{path dominance order}. Let $\eb$ and $\fb$ be two 01-sequences and let their corresponding Bruhat strolls be $x_0, x_1, \dots, x_m$ and $y_0, y_1, \dots, y_m$. We say that $\eb \ge \fb$ if $x_i \ge y_i$ for all $0 \le i \le m$. Clearly if $\eb \ge \fb$ then the end-point of $\eb$ is greater than the end-point of $\fb$. The path dominance order restricts to a partial order on the set of subsequences with fixed end-point.

Let $\w$ be the $\Z$-linear antiinvolution for which $\w(\un{H}_s)=\un{H}_s$ and $\w(v)=v^{-1}$. The standard trace gives rise to the \emph{standard pairing} $\HC \times \HC \to \Zvv$,
defined by $(a,b) = \e(b\w(a))$. This pairing is \emph{semilinear} over $\Zvv$; that is $(v^{-1}a,b)=(a,vb)=v(a,b)$ for all $a, b \in \HB$. Under this pairing, $b_s$ is self-biadjoint, i.e. \[(b_s x,y) = (x,b_s y),\qquad \qquad (x b_s,y) = (x,y b_s). \]

\begin{remark} \label{rmk:traces pairings} The formula $(a,b) = \e(b\w(a))$ can be used both ways, to define a pairing from a trace or vice versa. One can see that the $\Zvv$-module of all
semilinear pairings with self-biadjoint $b_s$ is isomorphic to the module of all $\Zvv$-linear traces. Any such pairing is determined by the values $\e(b_\xb)=(1,b_\xb)$ over all sequences
$\xb$. \end{remark}






\section{Soergel Bimodules}
\label{sec-sbim}
