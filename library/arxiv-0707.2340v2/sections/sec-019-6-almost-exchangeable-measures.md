---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-019-6-almost-exchangeable-measures
section_title: "Almost Exchangeable Measures"
section_number: 6
pages: 33-41
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.813
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{Almost}

By Pemantle's result (Theorem~\ref{pro-w} in \S \ref{ss-ex-case}), for 
symmetric measures in $\fP_n$ all five conditions NLC, h-NLC, 
Rayleigh/h-NLC+, CNA, CNA+ are equivalent to the ULC condition for the rank 
sequence. Therefore, the relations between 
all these negative dependence properties are completely understood in the 
exchangeable case. In this section we study the almost exchangeable
case, that is, measures whose generating polynomials are 
symmetric in all but possibly one variable (Definition~\ref{d-exc}). We prove 
that for such measures one has both 
h-NLC $\Leftrightarrow$ CNA and 
Rayleigh/h-NLC+ $\Leftrightarrow$ CNA+, which confirms 
Pemantle's Conjecture \ref{con-cna-R} in this case. In the next section we 
will use this result to show that the counterexamples in 20 or more 
variables  that we 
construct there satisfy 
all negative dependence properties other than strongly Rayleigh.

Let $C$ be an $m \times n$ matrix (where $m,n$ are allowed to be infinite), 
and let $\mathbf{i}$ and $\mathbf{j}$ be 
finite equi-numerous subsets of $[m]$ and $[n]$, respectively. Denote by 
$C(\mathbf{i}, \mathbf{j})$ the minor of $C$ with rows indexed by 
$\mathbf{i}$ and columns indexed by $\mathbf{j}$. The Cauchy-Binet theorem, 
see, e.g., \cite{Kar}, asserts that 
$$
(AB)(\mathbf{i}, \mathbf{j})
= \sum_{\mathbf{k},\,|\mathbf{k}|=|\mathbf{i}|=|\mathbf{j}|} A(\mathbf{i}, 
\mathbf{k})B(\mathbf{k}, \mathbf{j})
$$
for any $m\times n$ matrix $A$ and $n\times q$ matrix $B$, where
$1\le m,n,q\le \infty$, provided that the sum in the right-hand side converges
absolutely. 

Recall the notion of (non-negative) $\LC$ sequence from 
Definition \ref{d-ulc}. For convenience, we first prove a technical result 
that will be frequently used later on.

\begin{lemma}\label{l-tech}
Let $\{a_j\}_{j=0}^n$ and $\{b_j\}_{j=0}^n$ be two LC 
sequences that satisfy
\begin{itemize} 
\item[(i)] $\{a_j +  b_j\}_{j=0}^n$ is LC, and 
\item[(ii)] $a_jb_{j+1} \geq a_{j+1}b_j$ for all $0 \leq j \leq n-1$. 
\end{itemize}
If $\ell<k$ and $b_\ell a_k>0$, then $b_ra_r>0$ for all $\ell\leq r\leq k$.
\end{lemma}

\begin{proof}
Suppose that $a_r=0$ for
some $\ell \leq r< k$ and let $s$ the largest such index. Assumption (ii) 
for $j=s$ gives $b_s=0$, hence $a_s+b_s=0$. This contradicts the 
``no internal zeros" part of assumption (i) (cf.~Definition~\ref{d-ulc}). 
Therefore $a_r>0$, and a similar argument shows that $b_r>0$ as well. 








\end{proof}

The following proposition shows that for almost exchangeable measures the 
Rayleigh property is the same as the negative lattice condition (NLC) 
closed under conditioning and external fields on the last variable. 
Indeed, condition (ii) follows directly from 
NLC while (i) follows from NLC after having imposed an external field on the 
last coordinate and then projected onto the first $n$ coordinates. 

\begin{proposition}\label{RAS}
Let $\mu\in\fP_{n+1}$ be such that its generating polynomial $g=g_\mu$ is 
symmetric in its first $n$ variables, so that
$$
g(z_1,\ldots,z_{n+1})= z_{n+1}\sum_{k=0}^{n}a_ke_k(z_1,\ldots, z_n)+
\sum_{k=0}^{n}b_ke_k(z_1,\ldots, z_n).
$$
Then $\mu$ is Rayleigh if and only if 
\begin{itemize} 
\item[(i)] $\{\theta a_k + (1-\theta) b_k\}_{k=0}^n$ is LC 
for all $0 \leq \theta \leq 1$, and 
\item[(ii)] $a_kb_{k+1} \geq a_{k+1}b_k$ for all $0 \leq k \leq n-1$. 
\end{itemize}
\end{proposition}
\begin{proof}
Suppose first that $\mu$ is Rayleigh. By Proposition~\ref{p-proper} we get 
that if
$0 \leq \theta < 1$ then
$g(z_1, \ldots, z_n,\theta/(1-\theta))$ is a Rayleigh polynomial that is 
symmetric in all its $n$ variables. Condition (i) now follows from the 
exchangeable case (Theorem~\ref{pro-w}).  
Let $S \subseteq [n-1]$ be of cardinality $i$.
The NLC condition gives 
$$
a_ib_{i+1} = \mu(S \cup \{n+1\})\mu(S \cup \{n\}) \geq 
\mu(S \cup \{n,n+1\})\mu(S)= a_{i+1}b_i, 
$$
which verifies (ii). 

Assume now that $\{a_k\}_{k=0}^{n}$ and $\{b_k\}_{k=0}^n$ satisfy (i) and 
(ii). The inequality 
$$
\frac {\partial g} {\partial z_i}(x) \frac {\partial g} {\partial z_j}(x) 
\geq \frac {\partial^2 g} {\partial z_i \partial z_j}(x) g(x), 
\quad x\in \RR_+^{n+1}, \,i,j \in [n],
$$
follows from the exchangeable case and (i). What is left to prove is the 
inequality 
$$
\frac {\partial g} {\partial z_i}(x) \frac {\partial g} {\partial z_{n+1}}(x) 
\geq \frac {\partial^2 g} {\partial z_i \partial z_{n+1}}(x) g(x), 
\quad x\in \RR_+^{n+1},\, i\in [n], 
$$
and by symmetry (in the first $n$ variables) we only need to check it for
e.g.~$i=n$. We may write $g$ as 
\begin{multline*}
g(z_1,\ldots,z_{n+1})= \sum_{k=0}^{n} b_k e_k(z_1, \ldots, z_{n-1})+
z_n\sum_{k=0}^{n} b_{k+1} e_k(z_1, \ldots, z_{n-1}) \\
+ z_{n+1}\sum_{k=0}^n a_k e_k(z_1, \ldots, z_{n-1})+ z_nz_{n+1} 
\sum_{k=0}^n a_{k+1} e_k(z_1, \ldots, z_{n-1}),
\end{multline*}
so the desired inequality is equivalent to 
\begin{equation}\label{eqq}
\left(\sum_j a_je_j\right)\!\left(\sum_j b_{j+1}e_j\right)
-\left(\sum_j a_{j+1}e_j\right)\!\left(\sum_j b_je_j\right)\geq 0
\end{equation}
for all $x \in \RR_+^{n-1}$, where $e_j=e_j(x_1,\ldots, x_{n-1})$. Let now
 $$C=\left( \begin{array}{ccccc}
  a_0 & a_1 & a_2 & \ldots & a_n \\
  b_0 & b_1 & b_2 & \ldots  & b_n
\end{array} \right)$$
and recall the definition of a $\TP_p$ matrix from \S \ref{ss-ex-case}.
We claim that $C$ is $\TP_2$. Let $1 \leq i<j \leq n$. We need to 
prove that 
$a_ib_j \geq b_ia_j$. Clearly, we may assume that $b_ia_j \neq 0$ and that 
$j-i \geq 2$. By Lemma~\ref{l-tech} we have $b_ra_r>0$ for $i\le r\le j$ and
thus 
$$
\frac {a_i} {b_i} \geq \frac {a_{i+1}} {b_{i+1}} \geq \cdots 
\geq \frac {a_j} {b_j}
$$
by (ii), which shows that $C$ is indeed $\TP_2$. 






















Let $E=(e_{i-j})_{i,j=0}^{n}$. By Theorem~\ref{ESC} we have that $E$ is 
$\TP_2$ and by the Cauchy-Binet formula so is $CE$.  Now 
 $$CE=\left( \begin{array}{ccc}
  \sum a_je_j  & \sum a_{j+1}e_j\ & \ldots  \\
  \sum b_je_j & \sum b_{j+1}e_j & \ldots 
\end{array} \right),$$
from which \eqref{eqq} follows. 
\end{proof}

The next result is the analog of Proposition~\ref{RAS} for the h-NLC property.

\begin{proposition}\label{pro-h-NLC}
Let $\mu\in \fP_{n+1}$ be such that its  generating polynomial $g=g_{\mu}$
is symmetric in its first $n$ variables, so that
$$g(z_1,\ldots,z_{n+1})
=z_{n+1}\sum_{k=0}^n a_ke_k(z_1,\ldots,z_n)+
\sum_{k=0}^n b_ke_k(z_1,\ldots,z_n).$$
Then $\mu$ is $h$-NLC if and only if
\begin{itemize}
\item[(i)] $\{a_k\}_{k=0}^n$, $\{b_k\}_{k=0}^n$, and 
$\{a_k+b_k\}_{k=0}^n$ are LC, and
\item[(ii)] $a_kb_{k+1}\geq a_{k+1}b_k$ for all $0\leq k\leq n-1$. 
\end{itemize}
\end{proposition}

\begin{proof}
Let $S,T\subset [n]$. The NLC condition applied to each of the three pairs
$(S,T)$, $(S,T\cup\{n+1\})$, and $(S\cup\{n+1\},T\cup\{n+1\})$ gives  
respectively
$$b_{|S|}b_{|T|}\geq b_{|S\cup T|}b_{|S\cap T|},\quad b_{|S|}a_{|T|} 
\geq a_{|S\cup T|}b_{|S\cap T|},
\quad a_{|S|}a_{|T|}\geq a_{|S\cup T|}a_{|S\cap T|}.$$
Therefore, setting $\ell=|S|$, $k=|T|$, $m=|S\cap T|$, we see that 
NLC is  equivalent to
\begin{equation}\label{tech1}
b_\ell b_k\geq b_{k+\ell-m}b_m,\quad b_\ell a_k\geq a_{k+\ell-m}b_m,\quad 
a_\ell a_k \geq a_{k+\ell-m}a_m
\end{equation}
for $m\leq k,\ell\leq n$ and $k+\ell\leq n+m$.

If $S\subseteq [n]$ has cardinality $n-j$, the measure obtained by  
projecting $\mu$ onto $2^{S\cup\{n+1\}}$
is of the same form as $\mu$ with  coefficients
$$a_k(j)=\sum_{i=0}^j\binom jia_{k+i}\quad\text{and}\quad 
b_k(j)=\sum_ {i=0}^j\binom jib_{k+i},
\quad 0\leq k\leq n-j,$$
while the one obtained by projecting $\mu$ onto $2^S$ is exchangeable with  
coefficients $a_k(j)+b_k(j)$, $0\leq k\leq n-j$.
Therefore, h-NLC is equivalent to the statement that for each 
$0 \leq j\leq n$ one has 
\begin{equation}\label{tech2}
\begin{split}
&b_\ell(j)b_k(j)\geq b_{k+\ell-m}(j)b_m(j),\\  
&b_\ell(j)a_k(j)\geq  a_{k+\ell-m}(j)b_m(j),\,\,
a_\ell(j)a_k(j)\geq a_{k+\ell-m}(j)a_m(j),\\
&(a_\ell(j)+b_\ell(j))(a_k(j)+b_k(j))\geq 
(a_{k+\ell-m}(j)+b_{k+\ell-m}(j))(a_m(j) +b_m(j))
\end{split}
\end{equation}
for $m\leq k,\ell\leq n-j$ and $k+\ell\leq n-j+m$.

It follows from this that the h-NLC property implies that the sequences in 
(i) have no internal zeros.
For example, if $k\leq \ell$, $b_{k-1}>0, b_k=\cdots=b_\ell=0$, 
$b_{\ell+1}>0$  contradicts $b_kb_\ell\geq
b_{k-1}b_{\ell+1}$. Given this, the fact that the three sequences are LC  
and satisfy (ii) is
a consequence of the first and last inequalities in \eqref{tech1} with 
$\ell=k$, $m=k-1$, the middle
inequality in \eqref{tech1} with $\ell=k+1$, $m=k$, and the last inequality 
in \eqref{tech2} with $j=0$, $\ell=k$, $m=k-1.$

For the converse, assume that (i) and (ii) hold. Note that for  
each $j$, $\{a_k(j)\}_{k=0}^{n-j}$
is a convolution of two LC sequences, and hence is LC by 
\cite[Theorem 1.2 on p.~394]{Kar},
and the same holds for the sequences $b_k(j)$ and $a_k(j)+b_k(j)$.  
This gives three of the
four inequalities in \eqref{tech2}. For the other one, note that since  
evaluating the elementary symmetric
polynomials at the ``all ones vector'' produces binomial coefficients, 
it follows 
from \eqref{eqq} that
\begin{equation}\label{tech3}
a_k(j)b_{k+1}(j)\geq a_{k+1}(j)b_k(j).
\end{equation}
We need to check that 
$$a_k(j)b_\ell(j)\geq a_{k+\ell-m}(j)b_m(j)$$
for $m\leq k,\ell$, and in doing so, can assume that the right-hand side is  
not zero. By Lemma~\ref{l-tech},
it follows that $a_i(j)b_i(j)>0$ for $m\leq i\leq k+\ell-m$. To conclude  
the proof, write
$$\frac{a_k(j)}{a_{k+\ell-m}(j)}\geq 
\frac{a_m(j)}{a_\ell(j)}\geq\frac{b_m (j)}{b_\ell(j)}.$$
The first inequality comes from the already proved part of 
\eqref{tech2}, while  the second
is obtained by repeated application of \eqref{tech3}. 
\end{proof}

\begin{theorem}\label{th-a-ex}
Let $\mu\in\fP_{n+1}$ be such that its generating polynomial $g=g_\mu$ 
is symmetric in its first $n$ variables, so that
$$
g(z_1,\ldots,z_n)= z_{n+1}\sum_{k=0}^{n}a_ke_k(z_1,\ldots, z_n)+
\sum_{k=0}^{n}b_ke_k(z_1,\ldots, z_n).
$$
Suppose that $\{a_k\}_{k=0}^n$ and $\{b_k\}_{k=0}^n$ are LC 
sequences that satisfy
\begin{itemize} 
\item[(i)] $\{a_k +  b_k\}_{k=0}^n$ is LC, and 
\item[(ii)] $a_kb_{k+1} \geq a_{k+1}b_k$ for all $0 \leq k \leq n-1$. 
\end{itemize}
Then $\mu$ is $\CNA$. 
\end{theorem}

\begin{proof}
As in \S \ref{s21}, we denote by $X_i$, $i\in [n+1]$, the $i$-th coordinate
function/random (binary) variable on $2^{[n+1]}$. First, observe that it is 
enough to prove that $\mu$ is  NA. To see this, note
that if $\mu$ is conditioned on 
$X_i=1$ for $k$ values of $i\leq n$, on $X_i=0$ for
$l$ values of $i\leq n$, and possibly on the value of $X_{n+1}$, the  
resulting measure is
of the same form with a new value $n'$ of $n$ and new $a_i$'s and $b_i$'s  
that again satisfy the assumptions of the
theorem. Using primes to denote the new values, we have $n'=n-k-l$ and if the  
value of $X_{n+1}$ is not conditioned on,
then, except for a constant factor, $a_i'=a_{i+k}$ and $b_i'=b_{i+k}$. If
the value of $X_{n+1}$ is conditioned on, then $a_i'=b_i'=a_{i+k}$ if  
the conditioning is on
$X_{n+1}=1$ and $a_i'=b_i'=b_{i+k}$ if the conditioning is on $X_{n+1} =0$.
Now take two increasing functions $F$ and $G$ on $2^{[n+1]}$ that  depend on 
disjoint sets of coordinates (cf.~Definition~\ref{d-inc-ev}). Without loss of 
generality, we may assume that there  is an $m$ satisfying
$1\leq m\leq n$ such that $F$ depends on the coordinates $\{X_1\ldots,X_m \}$, 
and $G$ depends on the
coordinates $\{X_{m+1},\ldots,X_{n+1}\}$. We need to prove
\begin{equation}\label{cna1}
\int FGd\mu\leq\int Fd\mu\int G d\mu.
\end{equation}
Since $\mu$ is symmetric in the first $n$ coordinates, these three  
integrals are not
changed if $F$ and $G$ are replaced by the functions obtained by  
symmetrizing them with
respect to the coordinates $\{X_1,\ldots,X_m\}$ and $\{X_{m+1},...,X_n\}$, 
respectively. These symmetrized
functions are also increasing. Therefore, we may assume that $F$ and  $G$ are 
of the following form:
\begin{equation*}
\begin{split}
&F(X_1,\ldots,X_m)=f_k\text{ if }\sum_{i=1}^mX_i =k,\\
&G(X_{m+1},\ldots,X_n,X_{n+1}=0)=g_k\text{ if }\sum_{i=m+1}^nX_i =k,
\text{ and}\\
&G(X_{m+1},\ldots,X_n,X_{n+1}=1)=h_k\text{ if }\sum_{i=m+1}^nX_i =k,
\end{split}
\end{equation*}
where $f_k,g_k$ and $h_k$ are increasing, and $g_k\leq h_k$ for each  $k$.
Using the fact that the covariance of $F$ and $G$ with respect to the  
measure $\mu$
can be written as
$$\frac 12\sum_{S,T\in 2^{[n+1]}}[F(S)-F(T)][G(S)-G(T)]\mu(S)\mu(T),$$
\eqref{cna1} becomes
\begin{multline*}
\sum_{i,j,k,\ell}\binom mi\binom mj\binom {n-m}k\binom {n-m}\ell 
(f_j-f_i)\bigg[(h_k-h_\ell)a_{k+i}a_{\ell+j}\\+
(g_k-g_\ell)b_{k+i}b_{\ell+j}+(h_k-g_\ell)a_{k+i}b_{\ell+j}
+(g_k-h_\ell)a_{\ell+j}b_{k +i}\bigg]\geq 0.
\end{multline*}
Note that we are using the usual convention that $\binom nm=0$ unless  
$0\leq m\leq n$.
Since the summand above is not changed if the roles of $i$ and $j$  
are interchanged and the roles
of $k$ and $\ell$ are interchanged, this can be written as
\begin{multline}\label{cna2}
\sum_{i<j}\sum_{k,\ell}\binom mi\binom mj\binom {n-m}k\binom
{n-m}\ell(f_j-f_i)\bigg[(h_k-h_\ell)a_{k+i}a_{\ell+j}\\
+ (g_k-g_\ell)b_{k+i}b_{\ell +j}+(h_k-g_\ell)a_{k+i}b_{\ell+j}
+(g_k-h_\ell)a_{\ell+j}b_{k+i}\bigg]\geq 0.
\end{multline}
So, it is enough to show that for fixed $i<j$, and fixed $p$,
\begin{multline*}
\sum_{k+\ell=p}\binom {n-m}k\binom {n-m}\ell
\bigg[(h_k-h_\ell)a_{k+i} a_{\ell+j}\\
+ (g_k-g_\ell)b_{k+i}b_{\ell+j}+(h_k-g_\ell)a_{k+i}b_{\ell+j}
+(g_k-h_\ell)a_{\ell+j}b_{k +i}\bigg]\geq 0.
\end{multline*}
Furthermore, it is enough to prove this in case when the $g_k$'s and $h_k $'s 
take only the values 0 and 1,
since any increasing function on a partially ordered set (in this  case, 
$\{0,\ldots,n\}\times \{0,1\}$)
can be written as a positive linear combination of increasing  
functions that take only the values 0 and 1.

We will in fact prove that for such $g_k$'s and $h_k$'s,
\begin{multline*}
S_q=\sum_{k+\ell=p,\,|k-\ell|\leq 2q}
\binom{n-m}k\binom{n-m}\ell\bigg[(h_k-h_\ell)a_{k+i}a_{\ell+j}\\
+ (g_k-g_\ell)b_{k+i}b_{\ell+j}+(h_k-g_\ell)a_{k+i}b_{\ell+j}
+(g_k-h_\ell)a_{\ell+j}b_ {k+i}\bigg]\geq 0
\end{multline*}
by induction on $q$.  For the
basis step, note that $S_0=0$ if $p$ is odd, while if $p=2r$ is even,  
then
$$S_0=\binom{n-m}{r}^2(h_r-g_r)(a_{r+i}b_{r+j}-a_{r+j}b_{r+i}),$$
which is non-negative by (ii), since $i<j$.

We will prove now that $S_q\geq 0$, assuming that $S_{q-1}\geq 0$.  
The difference $S_q-S_{q-1}$ consists
of two summands, which when combined, become
\begin{multline}\label{cna3}
\binom {n-m}k\binom {n-m}\ell\bigg[(h_k-h_\ell)(a_{k+i}a_{\ell+j}
-a_ {\ell+i}a_{k+j})+
(g_k-g_\ell)(b_{k+i}b_{\ell+j}-b_{\ell+i}b_{k+j})\\
+(h_k-g_\ell)(a_{k+i}b_{\ell+j}
-a_ {k+j}b_{\ell+i})+
(g_k-h_\ell)(a_{\ell+j}b_{k+i}-a_{\ell+i}b_{k+j})\bigg],
\end{multline}
where $k+\ell=p$ while $k-\ell=2q$ if $p$ is even and 
$k-\ell=2q-1$ if $p$ is odd.
Now we consider the possible values of $g_\ell,h_k$ for this pair $k,\ell$.  
Recall that
$g_\ell\leq h_\ell,g_k\leq h_k$. If $g_\ell=h_k$, then $g_t=h_t=$ this common  
value for all $\ell\leq t\leq k$,
so that \eqref{cna3} is zero. So, we may assume that $g_\ell=0,h_k=1$. 
Now there  are four
possible values for the pair $(h_\ell,g_k)$ (note that the use of the 
fractions that appear below is justified by Lemma~\ref{l-tech}):

\medskip

(a) $\quad h_\ell=g_k=1$. In this case, \eqref{cna3} becomes
$$\binom {n-m}k\binom
{n-m}\ell\bigg[(b_{k+i}b_{\ell+j}-b_{\ell+i}b_{k+j})
+(a_{k+i}b_{\ell+j}-a_{k+j}b_ {\ell+i})\bigg].$$
This is non-negative by the log-concavity of the $b$'s and (ii):
$$\frac{a_{k+i}}{a_{k+j}}\geq\frac{b_{k+i}}{b_{k+j}}\geq
\frac{b_{\ell+i}} {b_{\ell+j}}.$$

\medskip

(b) $\quad h_\ell=0,g_k=1$. Now \eqref{cna3} is
$$\binom {n-m}k\binom {n-m}\ell\bigg[(a_{k+i}+b_{k+i})(a_{\ell+j}+b_{\ell+j})
- (a_{\ell+i}+b_{\ell+i})(a_{k+j}+b_{k+j})
\bigg],$$
which is non-negative by (i).

\medskip

(c) $\quad h_\ell=g_k=0$. This time \eqref{cna3} is
$$\binom {n-m}k\binom {n-m}\ell\bigg[(a_{k+i}a_{\ell+j}-a_{\ell+i}a_{k+j})+
(a_{k+i}b_{\ell+j}-a_{k+j}b_{\ell+i})\bigg],$$
which is non-negative by the log-concavity of the $a$'s and (ii).

In these three cases, \eqref{cna3} is non-negative, and therefore 
$S_q \geq 0$ by the induction
hypothesis. The fourth case is different, since \eqref{cna3} need not be  
non-negative:

\medskip

(d) $\quad h_\ell=1, g_k=0$. In this case, $g_t\equiv 0$ and $h_t\equiv 1$ 
for  
$\ell\leq t\leq k$, so
$$S_q=\sum_{r+s=p,\,|r-s|\leq 2q}\binom {n-m}r\binom  {n-m}s(
a_{r+i}b_{s+j}-a_{s+j}b_{r+i}).$$
Now use summation by parts, together with the fact that
$$u(r)=\binom{n-m}r\binom{n-m}{p-r}$$
is decreasing in $r$ for $r\geq p/2$, to argue that it suffices to  show that
\begin{equation}\label{cna4}
T_q=\sum_{r+s=p,\,r,s\geq 0,\,|r-s|\leq 2q}(
a_{r+i}b_{s+j}-a_{s+j}b_{r+i})\geq 0
\end{equation}
for each $q$. Here is the argument: noting that
$$S_q-S_{q-1}=(T_q-T_{q-1})u\big(q+[p/2]\big)$$
and summing, we have
\begin{equation*}
\begin{split}
S_q=&\,\,\sum_{r\leq q}(S_r-S_{r-1})=\sum_{r\leq q}(T_r-T_{r-1})u 
\big(r+[p/2]\big)\\
=&\,\,T_qu\big(q+[p/2]\big)+\sum_{r<q}T_r\big[u\big(r+[p/2]\big)
-\big[u\big(r+1+[p/2]\big)\big].
\end{split}
\end{equation*}
Now to check \eqref{cna4}, we rearrange the sum as follows, 
noting  that there
may be some cancellation of terms, leading to the truncation of the  
upper limit
of the sum:
$$\sum_{r=\ell+i}^{(k+i)\wedge(\ell+j-1)}(a_rb_{p-r+i+j}-a_{p-r+i+j}b_r).$$
Here again $k+\ell=p,$ and $k-\ell=2q$ if $p$ is even and $k-\ell=2q-1$ if 
$p$  is odd. The summands in this sum are
non-negative by (ii) since for all $r$ appearing in the sum, $r\leq p-r +i+j$.
To check this, write $2r=r+r\leq (k+i)+(\ell+j)=p+i+j$.
\end{proof}

\begin{corollary}\label{cor-cna+}
Suppose $\{a_k\}_{k=0}^n$ and $\{b_k\}_{k=0}^n$ are LC sequences
that satisfy
\begin{itemize}
\item[(i)] $\{\lambda a_k+b_k\}_{k=0}^n$ is LC for all $\lambda>0$, and
\item[(ii)] $a_kb_{k+1}\geq a_{k+1}b_k$ for $0\leq k<n.$
\end{itemize}
Then $\mu$ is CNA+.
\end{corollary}

\begin{proof}
Let $\{w_i>0\}_{i=1}^{n+1}$ be the external field that is  applied to $\mu$, 
and
$\mu'$ be the resulting measure:
$$\mu'(S)=\text{ constant }\times\prod_{i=1}^{n+1}w_i^{X_i(S)}\mu(S), \quad 
S\subseteq [n+1].$$
We need to show that \eqref{cna1} holds with $\mu$ replaced by $\mu'$. 
First,  note that the effect
of $w_{n+1}$ is to replace $a_k$ by a constant multiple of $a_k$, so  
since we have introduced a general
positive $\lambda$ in assumption (i), we may assume that $w_{n+1}=1.$  
The analog of \eqref{cna2} that we must check is
\begin{multline}\label{cna5}
\sum_{i<j}\sum_{k,\ell}(f_j-f_i)c_ic_jd_kd_\ell
\bigg[(h_k-h_\ell)a_ {k+i}a_{\ell+j}\\+
(g_k-g_\ell)b_{k+i}b_{\ell+j}+(h_k-g_\ell)a_{k+i}b_{\ell+j} 
+(g_k-h_\ell)a_{\ell+j}b_{k +i}\bigg]\geq 0,
\end{multline}
where now the $f_k$'s, $g_k$'s and $h_k$'s are obtained by  symmetrizing $F$ 
and $G$ with respect to the
field on the set of coordinates $\{X_1,\ldots,X_m\}$ in the case of $F$  
and $\{X_{m+1},\ldots,X_n\}$
in the case of $G$. For example,
$$f_k=c_k^{-1}\cdot\sum F(S)\prod_{i=1}^mw_i^{X_i(S)},$$
where 
$$c_k=\sum \prod_{i=1}^mw_i^{X_i(S)}$$
and the above sums are taken over all $S\subseteq [m]$ such that 
$\sum_{i=1} ^mX_i(S)=k$. The formulas for $g_k$ and $h_k$ are exactly 
analogous and the corresponding normalization factor (instead of $c_k$) is
$$d_k=\sum \prod_{i=m+1}^{n}w_{i}^{X_i(S)},$$
the sum being taken over all $S\subseteq \{m+1,\ldots,n\}$ such that 
$\sum_{i=m+1}^{n}X_i(S)=k$. 
Note that if $w_i\equiv 1$, then $c_k=\binom mk$ and $d_k=\binom{n-m} {k}$, 
so that $f_k$ reduces to the symmetrization used in the proof of 
Theorem~\ref{th-a-ex}, and \eqref{cna5} reduces
to \eqref{cna2}.

In order to deduce \eqref{cna5} from the arguments used to prove \eqref{cna2},
we then  need to check the following statements:

\medskip

(a) $\quad f_k\le f_{k+1}$, $g_k\le g_{k+1}$, $h_k\le h_{k+1}$ and
$g_k\leq h_k$ for all $k$, and

(b) $\quad \{d_k\}_{k=0}^{n-m}$ is an LC sequence.

\medskip

\noindent The latter is needed to check that
$d_rd_{p-r}$
is decreasing in $r$ for $r\geq p/2$, which is then used in the analog  
of the treatment of case (d) in the proof of Theorem~\ref{th-a-ex}. Note that 
statement (b) follows from e.g.~Theorem~\ref{ESC}, since $d_k$ is just the
$k$-th elementary symmetric function on $\{w_{m+1},\ldots,w_n\}$.
 
Now the fact that $g_k\leq h_k$ is immediate from the monotonicity of $G$  
in its last argument. The
verification of the first three statements in (a) is the  same 
for all of them, so
we check (a) only for $f_k$. Letting as usual $|S|$ denote the cardinality
of a set $S$, write
$$c_kc_{k+1}(f_{k+1}-f_k)= 
\sum_{|S|=k,\,|T|=k+1} [F(T)-F(S)] \prod_{i=1}^mw_i^{X_i(S)+X_i(T)}.$$
Consider the sum of the terms corresponding to $S$'s and $T$'s that  
satisfy $X_i(S)+X_i(T)=z_i$
for all $i$ and an arbitrarily fixed $z\in\{0,1,2\}^m$. If $A,B,C$ are the  
index sets corresponding to those coordinates $X_i$ for which
$z_i=0,1,2$, respectively, we see that we need to check
\begin{equation}\label{cna6}
\sum_{|T|=k+1,\,X_i(T)=0,\,i\in A,\atop X_i(T)=1,\,i\in C} F(T)\geq
\sum_{|S|=k,\,X_i(S)=0,i\in A,\atop X_i(S)=1,i\in C} F(S).
\end{equation}
Noting that the sums above have the same number of summands, namely
$$\binom{2k-2|C|+1}{k-|C|+1}\quad\text{and}\quad\binom{2k-2|C|+1}{k-| C|},$$
respectively, we see that \eqref{cna6} is a consequence of the monotonicity  
of $F$.


\end{proof}

Recall from Remark~\ref{r-cn-hn} that CNA+ $\Rightarrow$ Rayleigh/h-NLC+ and 
CNA $\Rightarrow$ h-NLC. By combining Proposition~\ref{RAS} and 
Corollary~\ref{cor-cna+} on the one hand, and Proposition~\ref{pro-h-NLC} and 
Theorem~\ref{th-a-ex} on the other hand, we deduce the following result.

\begin{corollary}\label{RandC}
If $\mu$ is an almost symmetric measure (i.e., its
generating polynomial is symmetric in all but possibly one variable,
cf.~Definition~\ref{d-exc}), then 
\begin{enumerate}
\item $\mu$ is Rayleigh/h-NLC+ $\Longleftrightarrow$ $\mu$ is CNA+;
\item $\mu$ is h-NLC $\Longleftrightarrow$ $\mu$ is CNA.
\end{enumerate}
\end{corollary} 

This shows that Pemantle's Conjecture~\ref{con-cna-R} 
is true for almost 
symmetric measures (recall that by the results in \S \ref{s-sna}, 
Conjecture~\ref{con-cna-R} also holds for strongly Rayleigh measures and
PHR measures).
