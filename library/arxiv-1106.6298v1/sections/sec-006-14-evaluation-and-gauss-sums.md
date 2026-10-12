---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS"
section_id: sec-006-14-evaluation-and-gauss-sums
section_title: "Evaluation and Gauss sums"
section_number: 1.4
pages: 7-9
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariant s."
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.977
---
For each root of unity $\xi$ of odd order $r$,
we define the evaluation map
$\ev_\xi$ by replacing $q$ with $\xi$.








Suppose
  $f(q;n_1,\dots,n_m)$ is a function
of variables $q^{\pm 1}$ and integers $n_1,\dots,n_m$.
In quantum topology, the following sum plays an important role
\[
{\sum_{n_i}}^\xi f := \sum_{\substack{0< n_i< 2r\\ n_i \text{ odd}}}
\ev_\xi  f(q; n_1,\dots, n_m)
\]
where in the sum  all the $n_i$ run over the set of {\em odd} numbers
between $0$ and $2r$.

In particular, the following  variation  of the Gauss sum
\[
\gamma_b(\xi):= {\sum_{n}}^\xi q^{b\frac{n^2-1}{4}}
\]
is well--defined, since for odd $n$, $4\mid n^2-1$.
It is known that, for odd $r$, $|\gamma_b(\xi)|$ is never 0.



\subsection{Definition of the WRT invariants}


 Let
\[


 F_{L}(\xi):= {\sum_{n_i}}^\xi\; \prod_{i=1}^m [n_i]\;
  J_{L}(n_1,\dots,n_m).\]


\begin{Thm} \label{K1M}{\rm [Reshetikhin--Turaev]}
$F_L(\xi)$ is invariant under K1--Move.
\end{Thm}



An important special case is when $L=U^b$, the unknot with framing
$b \neq 0$. In that case $F_{U^{b}}(\xi)$ can be calculated
using the Gauss sum and is nonzero.

 Let $\sigma_+ $ (respectively $\sigma_-$) be the number of
positive (negative) eigenvalues of the linking matrix of $L$.
 Then we define


\begin{equation}
\tau_{M}(\xi) =
\frac{F_{L}(\xi)}{(F_{U^{+1}}(\xi))^{\sigma_+}\,
(F_{U^{-1}}(\xi))^{\sigma_-} }\, .
\label{def_qi}
\end{equation}

It is easy to see that  $\tau_M(\xi)$ is invariant under
K2--Move, and hence, by Theorem \ref{K1M}, it is a topological
invariant of $M$ called the $SO(3)$ WRT invariant.
 Moreover,
 $\tau_{M}(\xi)$ is multiplicative with
respect to the connected sum.

\vskip2mm
\noindent
{\bf Remark.}
If we drop the condition that the colors in the summation are
odd, and sum over all (odd and even) colors, the result will be
the $SU(2)$ WRT invariant  $\tau^{SU(2)}_M (\xi)$.
In this case, the order of $\xi$ could also be even.
\vskip2mm

 The $SO(3)$  WRT invariant  extends naturally to the invariant
of the pair $(M,L')$, where
the manifold $M$ contains a link $L'$ inside. In this case we have
to replace the surgery link $L$ of $M$ by $L\cup L'$ in all definitions,
fix colors on $L'$ and sum over all colorings of
$L$ only. We omit here the precise definition and refer to \cite{BBL}
for more details.


For example, the $SO(3)$ invariant of the lens space $L(b,1)$,
obtained by surgery along $U^b$,  is
\begin{equation} \tau_{L(b,1)} (\xi)= \frac{ F_{U^b}(\xi)}{F_{U^{\sn(b)}}(\xi) },
\label{2005}
\end{equation}
were $\sn(b)$ is the sign of the integer $b$.






Suppose
$M$ is a rational homology
3--sphere.

Then there is a unique decomposition
 $ H_1(M,\Z)=\bigoplus_{i}
\Z/{b_{i}\Z}$, where each $b_i$ is a prime power.
We renormalize the $SO(3)$  WRT invariant  as follows:
\begin{equation}
\tau'_{M}(\xi)=\frac{\tau_{M}(\xi)}
{\prod\limits_{i}\;\,
\tau_{L(b_{i},1)}(\xi)}\; ,




\label{0910}
\end{equation}
where $L(b,a)$ denotes the $(b,a)$ lens space. Note that
$\tau_{L(b,1)}(\xi)$ is always nonzero.



Let us focus on the special case when the linking matrix of
$L$ is diagonal.

Assume each $L_{ii}=b_i$ is a power of a prime or 1, up to sign.
Then $H_1(M,\Z) = \oplus_{i=1}^m \Z/|b_i|$, and
$$\sigma_+ = {\rm card}\, \{ i\mid b_i >0\}, \quad \sigma_- =
{\rm card}\, \{ i \mid b_i < 0\}.$$
Thus from the definitions \eqref{def_qi}, \eqref{2005} and \eqref{0910} we have
\begin{equation}
 \tau'_{M}(\xi) = \left( \prod_{i=1}^m  \tau'_{L(b_i,1)}(\xi)
 \right)\,
\frac{F_{L}(\xi)}
{\prod_{i=1}^m F_{U^{b_i}}(\xi) }
\,  ,
\label{0077}
\end{equation}
with
$$\tau'_{L(b_i,1)}(\xi)= \frac{\tau_{L(b_i,1)}(\xi)}{\tau_{L(|b_i|,1)}(\xi)}\, .$$

The collection of $SO(3)$ WRT invariants is difficult to study, since
their definition heavily depends on the order of $\xi$.
The following cyclotomic expansion will play an important role
for the unification of the WRT invariants.



\subsection{Habiro's cyclotomic expansion of the colored Jones
polynomial}


For non--negative integers $n,k$ we define
$$ A(n,k) := \frac{\prod^{k}_{i=0}
\left(q^{n}+q^{-n}-q^i -q^{-i}\right)}{(1-q) \, (q^{k+1};q)_{k+1}}.$$
For $\bk=(k_1,\dots,k_m)$ let
$$ A(\bn,\bk):= \prod_{j=1}^m \; A(n_j,k_j).$$
Note that $A(\bn,\bk)=0$ if $k_j \ge n_j$ for some index $j$. Also
$ A(n,0)= q^{-1} J_U(n)^2.$


The colored Jones polynomial $J_{L}
(\n)$  can be repackaged into the invariant $C_{L}
(\bk)$ as stated in the following theorem.
\begin{Thm} {\rm [Habiro]}\label{GeneralizedHabiro}
 Suppose $L$ is a link in $S^3$ having zero linking matrix.


Then  there are invariants
\begin{equation}\label{Jones2}
C_{L}(\bk) \in \frac{(q^{k+1};q)_{k+1}}{(1-q)}
\,\,\BZ[q^{\pm 1}] ,\quad \text{where  $k=\max\{k_1,\dots, k_m\}$}
\end{equation}
such that for every $\bn =(n_1,\dots, n_m)$
\begin{equation}\label{Jones}
 J_{L}
(\n)  \,  \prod^m_{i=1}\; [n_i] = \sum_{0\le k_i \le n_i-1}
C_{L}(\bk)\;
  A(\bn, \bk).
\end{equation}
\end{Thm}




 Note that the existence of $C_{L}(\bk)$ as
rational functions in $q$ satisfying \eqref{Jones} is
 easy to establish. They correspond to the Jones polynomial
colored by different elements of the Grothendieck ring
of $U_q(\frak {sl}_2)$, i.e. by linear combinations of representations.
The difficulty here is to show the integrality
of \eqref{Jones2}.

 Since $A(\bn, \bk) =0$ unless $ \bk < \bn$, in the sum on the right
hand side of \eqref{Jones} one can assume that $\bk$ runs over the set
 of all $m$--tuples $\bk$ with non--negative integer components. We will use
this fact later.
