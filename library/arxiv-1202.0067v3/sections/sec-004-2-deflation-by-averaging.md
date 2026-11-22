---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE"
section_id: sec-004-2-deflation-by-averaging
section_title: "Deflation by averaging"
section_number: 2
pages: 7-9
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.891
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE — Given natural numbers m and n, we deﬁne a deﬂation map from the characters of the symmetric group Smn to the characters of"
---
\label{sec:averaging}


Let $m$, $n \in \N$. 
We shall think
of $S_m \wr S_n$ as the group of permutations of
\[ \{1,\ldots, m\} \times \{1,\ldots, n\} \]
that leaves invariant the set of blocks of the form $\Delta_j = \{(1,j), \ldots, (m,j)\}$, 
$1 \le j \le n$.					
Given $h_1, \ldots, h_n \in S_m$ and $g \in S_n$, we
write $(h_1,\ldots,h_n;g)$
for the permutation which sends $(i,j)$ 
to $(h_{gj} i,gj)$. 
This left action is equivalent to the action
defined in \hbox{\cite[4.1.18]{JK}}. 
Let $B = S_m \times \cdots \times S_m$ denote
the base group in the wreath product. As shorthand,
if $k = (h_1,\ldots,h_n) \in B$ 
then we shall write $(k\,;g)$ for $(h_1,\ldots,h_n;g)$.


\begin{lemma}\label{lemma:sum}
Let $m$, $n \in \mathbf{N}$, let $\theta$ be an irreducible character of $S_m$, 
and let $\xi$ be an irreducible character of $S_m \wr S_n$. 
 If $\xi = \widetilde{\theta^{\times n}} \Inf_{S_n}^{S_m \wr S_n}\!\chi^\nu$ for some partition $\nu$ of $n$ then 
 \[ \frac{1}{|B|} \sum_{k \in B} \xi (k\, ;g) 
 \widetilde{\theta^{\times n}} (k\, ;g) = \chi^\nu(g), \]
and if $\xi\in \Irr(S_m \wr S_n)$ is not of this form then the left-hand side is zero.
\end{lemma}

\begin{proof}
Suppose that the left-hand side is non-zero. The character
$\widetilde{\theta^{\times n}}$ of $S_m \wr S_n$ restricts to
the irreducible character $\theta \times \cdots \times \theta$ of $B$.
Hence,
by  \cite[Lemma 8.14(b)]{IsaacsChars}, applied with $G = S_m \wr S_n$
and $N = B$, we have
$\left<\Res_B \xi, \Res_B \widetilde{\theta^{\times n}}\right> \not=0$.
It follows by Frobenius Reciprocity that $\xi$ is a constituent of
\[ \Ind_{B}^{S_m \wr S_n} (\theta \times \cdots \times \theta) = 
\sum_{\nu} \chi^\nu(1) \widetilde{\theta^{\times n}} \Inf_{S_n}^{S_m \wr S_n}\!\chi^\nu ,\]
where the sum is over all partitions $\nu$ of $n$.
Since $\xi$ is irreducible 
we must have $\xi =  \widetilde{\theta^{\times n}}\Inf_{S_n}^{S_m \wr S_n}\!\chi^\nu$ for some 
$\nu$. Therefore the left-hand side in the lemma is  
\[ \frac{\chi^\nu(g)}{|B|} \sum_{k \in B}
\bigl( \widetilde{\theta^{\times n}}(k\, ;g) \bigr)^2 \]
which is equal to $\chi^\nu(g)$ by \cite[Lemma 8.14(c)]{IsaacsChars}.
\end{proof}



By Definition~\ref{def:def}, 
we have $\Defres^\theta_{S_n}
(\widetilde{\theta^{\times n}} \Inf_{S_n}^{S_m \wr S_n}\!\chi^\nu)(g) = 
\chi^\nu(g)$ for all $g\in S_n$. The next proposition therefore
follows immediately from Lemma~\ref{lemma:sum}. 

\begin{proposition}\label{prop:deflation}
Let $m$, $n \in \N$, let $\theta$ be an irreducible
character of $S_m$, and let $\psi$ be a character of $S_m \wr S_n$.
If $g \in S_n$ then
\begin{flalign*}
    &&(\Def^\theta_{S_n} \psi)(g) = 
\frac{1}{|B|} \sum_{k \in B} 
\psi (k\, ;g) \widetilde{\theta^{\times n}} (k\,;g). && \qed  
\end{flalign*}
\end{proposition}



\begin{corollary}\label{cor:deflation}
Let $m$, $n \in \N$, let $\theta$ be an irreducible
character of $S_m$, and let $\psi$ be a character of $S_{m} \wr S_n$.
If  $g \in S_n$ is an $n$-cycle then
\[ (\Def^\theta_{S_n} \psi)(g) =
\frac{1}{m!} \sum_{h \in S_m} \psi (h,1,\ldots,1;g)\theta(h).\]
\end{corollary}

\begin{proof}
Suppose that $g$ is the $n$-cycle $(x_1 \, x_2 \, \ldots \, x_n)$. 
By~\cite[4.2.8]{JK}, the permutations $(h_1,\ldots,h_n;g)$ and
$(h_1',\ldots,h_n';g) \in S_m \wr S_n$ are conjugate
in $S_m \wr S_n$ if and only if 
the elements $h_{x_n} h_{x_{n-1}}\ldots h_{x_1}$ and   $h'_{x_n} h'_{x_{n-1}}\ldots h'_{x_1}$ are conjugate in $S_m$.
In particular, each conjugacy class of $S_m \wr S_n$ 
which meets $\{(k\,; g) : k \in B\}$ has 
a representative of the form $(h,1,\ldots,1;g)$. Moreover,
the number of elements $(h_1,h_2,\ldots,h_n;g)$ conjugate
to $(h,1,\ldots,1;g)$ is
$m!^{n-1} |h^{S_m}|$,
since $h_2, \ldots, h_n$ may be chosen arbitrarily, 
and then 
$h_1$ must be chosen so that 
$h_{x_n} h_{x_{n-1}}\cdots h_{x_1} \in h^{S_m}$.
It follows that
\begin{align*}
\sum_{k \in B} \psi(k\, ;g) \widetilde{\theta^{\times n}}(k\, ;g)  &= 
m!^{n-1} \sum_{h \in S_m}
 \psi (h,1,\ldots,1;g) \widetilde{\theta^{\times n}}(h,1,\ldots
,1;g) \\
&= m!^{n-1} \sum_{h \in S_m} \psi (h,1,\ldots,1;g) \theta(h)
\end{align*}
where the second equality uses~\cite[Lemma 4.3.9]{JK}. 
Now apply Proposition~\ref{prop:deflation} to the left-hand side.
\end{proof}

The following definition and lemma allow for a more convenient
statement of Corollary~\ref{cor:deflation}.

\begin{definition}\label{def:omega}
Let $m$, $n \in \N$, let $g \in S_n$ be
an $n$-cycle, and
let $\psi$ be a character of $S_m \wr S_n$. We define
$\omega(\psi)$ to be the 
 class function on $S_m$ such that
\[ \omega(\psi) (h) = \psi(h,1,\ldots,1;g)  \]
for all $h \in S_m$.
\end{definition}

\begin{lemma}\label{lemma:cycles}
Let $m$, $n \in \N$. If $g\in S_n$ is an $n$-cycle
and $h \in S_m$ has cycle
type $\alpha$ 
then $(h,1,\ldots,1;g) \in S_m \wr S_n$ has cycle
type $n\alpha$.
\end{lemma}

\begin{proof}
It suffices to show that if $\mathcal{O}$ is an orbit
of $h$ on $\{1,2,\ldots,m\}$ then $\mathcal{O} \times \{1,\ldots,n\}$
is an orbit of $(h,1,\ldots,1;g)$ in its action on 
$\{1,\ldots,m\} \times \{1,\ldots,n\}$.
We leave this to the reader as an easy exercise. 
\end{proof}


The next proposition follows easily from
 Lemma~\ref{lemma:cycles} and
Corollary~\ref{cor:deflation}.

\vbox{
\begin{proposition}\label{prop:omega}
Let $m$, $n \in \N$, and let $\chi$ be a character of $S_{mn}$. 

\begin{thmlist}
\item
If
$\alpha$ is a partition of $m$ then
\[ \omega(\Res_{S_m \wr S_n} \chi) (g_\alpha) = \chi(g_{n\alpha}).\]
\item If $\theta$ is an irreducible
character of $S_m$ and $g \in S_n$ is an $n$-cycle then
\begin{align*} (\Defres^\theta_{S_n} \chi)(g) &= 
\left< \omega(\Res_{S_m \wr S_n} \chi), \theta  \right> \\
&= \sum_{\alpha} 
\frac{\chi(g_{n\alpha})}{z_\alpha} \theta(g_\alpha) \end{align*}
where the sum is over all partitions $\alpha$ of $m$.\hfill$\qed$
\end{thmlist}
\end{proposition}}

The character
value $\chi(g_{n\alpha})$ in part (i) is the subject of
Theorem~\ref{thm:ind}; we shall see that
combining this theorem with part (ii) gives
Equation~\eqref{eq:omegares} in \S\ref{sec:proof} below. 
Note also that part~(ii) of the proposition
implies Equation~\eqref{eq:cycle_deflation} in~\S 2.
