---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-016-43-stochastic-domination-and-truncations
section_title: "Stochastic Domination and Truncations"
section_number: 4.3
pages: 25-29
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.979
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{ss-trunc}

Recall the notion of stochastic domination from Definition~\ref{d-stoc} in 
\S \ref{s24}. 
It turns out that for strongly Rayleigh measures, stochastic domination is 
intimately connected with central notions in the theory of stable and 
real-rooted polynomials, namely the notions of interlacing zeros and 
proper position \cite{BBS,BBS1,BBS2,PB,Le,RS}. In particular, this connection
allows us to extend one of Lyons' main results \cite{Lyons} and to answer
Pemantle's questions on stochastic domination for truncations of ``negatively
dependent'' measures \cite{P} (cf.~\S \ref{s24}).


\subsubsection{Partial Orders for Strongly Rayleigh Measures and 
Polynomials}\label{sss-stoc}

Let $\alpha_1 \leq \alpha_2 \leq \cdots \leq \alpha_n$ and 
$\beta_1 \leq \beta_2 \leq \cdots \leq \beta_m$ be the zeros of two 
real-rooted polynomials $p,q \in \RR[z]$. These zeros are  
{\em interlacing} if they can 
be ordered so that either   $\alpha_1 \leq \beta_1 \leq \alpha_2 \leq 
\beta_2 \leq 
\cdots$ or $\beta_1 \leq \alpha_1 \leq \beta_2 \leq \alpha_2 \leq 
\cdots$. If 
the zeros of $p,q$ interlace then 
the {\em Wronskian} 
$W[p,q]:=p'q-pq'$ is either non-negative or non-positive on the whole
 real axis 
$\RR$, see, e.g., \cite{Le,RS}. 
We say that $p$ and $q$ 
are  in  
{\em proper position}, denoted $p \ll q$, if the zeros of $p$ and $q$ 
interlace and 
 $W[p,q] \leq 0$. For technical reasons, we also say that the zeros of the 
polynomial $0$ 
interlace the zeros of any (non-zero) real-rooted polynomial and write 
$0 \ll p$ and $p \ll 0$. 

The following theorem proved in \cite{BBS2} 
provides a notion of proper position for  multivariate polynomials. 

\begin{theorem}\label{addz}
Let $f, g \in \RR[z_1,\ldots,z_n]$. The following are equivalent: 
\begin{enumerate}
\item The polynomial $g+if \in \CC[z_1,\ldots,z_n]$ is stable; 
\item The polynomial $g+z_{n+1}f \in \RR[z_1,\ldots,z_n,z_{n+1}]$ is 
real stable; 
\item For all $\lambda \in \RR_+^n$ and $\mu \in \RR^n$ we have 
$$
f(\lambda t + \mu) \ll g(\lambda t + \mu),  
$$
where $f(\lambda t + \mu)
=f(\lambda_1 t+\mu_1, \ldots, \lambda_n t+\mu_n)$, $t\in\CC$.
\end{enumerate}
\end{theorem}

We say that the polynomials $f, g \in \RR[z_1,\ldots,z_n]$ are in 
{\em proper position}, written $f \ll g$, if any of the equivalent 
conditions in Theorem \ref{addz} are satisfied. 

\begin{remark}\label{dada}
The typical proper position is between a real stable polynomial and any of its 
partial derivatives: 
if $f \in \RR[z_1,\ldots,z_n]$ is real stable then 
$\partial_j f \ll f$ for all $j\in [n]$. 
If $f \ll g$ and $\alpha$ is a real number then either 
$f(\alpha,z_2,\ldots,z_n) \ll g(\alpha,z_2,\ldots,z_n)$ or  
$f(\alpha,z_2,\ldots,z_n)= g(\alpha,z_2,\ldots,z_n)\equiv 0$, see \cite{BBS2}.
Note also that by Theorem~\ref{addz} (3) one has $f\ll g\Leftrightarrow 
\alpha f\ll \beta g$ for any $\alpha,\beta\in \RR_+$.
\end{remark} 

We define a partial order $\unlhd$ on the set of strongly Rayleigh 
probability measures on $2^{[n]}$ as follows. 
 
\begin{definition}\label{d-order}
 Let $\SR_n$ be the set of  strongly Rayleigh probability measures on 
$2^{[n]}$. First, define a (preliminary) partial order $\unlhd'$ on $\SR_n$ 
by setting $\mu \unlhd' \nu$ if there exists a sequence of  strongly 
Rayleigh probability measures $\mu=\mu_0, \mu_1, \ldots, 
 \mu_\ell=\nu$ such that 
 $g_{\mu_0} \ll g_{\mu_1} \ll \cdots \ll g_{\mu_\ell}$. Then 
 define the partial order $\unlhd$ on $\SR_n$ as the closure of 
$\unlhd'$, i.e., set $\mu \unlhd \nu$ if there are two sequences 
 $\{\mu_j\}_{j=0}^{\infty}, \{\nu_j\}_{j=0}^{\infty} \subset \SR_n$ such that 
 $$
 \lim_{j \rightarrow \infty} \mu_j =\mu,\, 
 \lim_{j \rightarrow \infty} \nu_j =\nu, \mbox{ and } 
\mu_j \unlhd' \nu_j \text{ for all } j \in \NN 
 $$
(as the measures are defined 
on $2^{[n]}$ it does not matter what notion of limit we use). 
We will also consider $\unlhd$  to be a partial order on 
 the set of generating polynomials of strongly Rayleigh measures and write 
$g_{\mu} \unlhd g_{\nu}$ whenever $\mu \unlhd \nu$.   
\end{definition}

\begin{remark}
It seems likely that the partial orders $\unlhd'$ and $\unlhd$ on $\SR_n$ 
defined above are actually the same. However, since it is 
irrelevant for the present purposes we do not further pursue this 
issue here.
\end{remark}

As we noted in \S \ref{s24}, the stochastic domination relation $\pc$ defines
a partial order on $\fP_n$ (cf.~\cite{MO}). 
The anti-symmetry of $\unlhd$ follows from our next result. 

\begin{proposition}\label{stdom}
Let $\mu$ and $\nu$ be strongly Rayleigh probability measures on $2^{[n]}$. 
Then 
$\mu \unlhd \nu \Longrightarrow \mu \pc \nu$.
\end{proposition}

\begin{proof}
Clearly, we may assume that $g_\mu \ll g_\nu$, 
so that by Theorem~\ref{addz} the
polynomial in $n+1$ variables 
$G=(g_\nu +z_{n+1}g_\mu)/2$ is stable. Let $\gamma\in\fP_{n+1}$ be the 
measure with generating polynomial $G$. By 
Theorem \ref{stab-NA}, $\gamma$ is NA. Let $\AS$ be an 
increasing event not depending on the last coordinate  and 
set $\BS=\{ S  \in 2^{[n+1]} : n+1 \in S \}$. Then 
$$
\frac{1}{2} \mu(\AS) = \gamma(\AS \cap \BS) \leq \gamma(\AS) 
\gamma(\BS)
= \left(\frac{1}{2} \mu(\AS) + \frac{1}{2} \nu(\AS)\right)\frac{1}{2}, 
$$
which gives $\mu(\AS) \leq \nu(\AS)$. 
\end{proof}

Recall that the standard partial order on the set of all Hermitian $n\times n$
matrices -- often referred to as the {\em Loewner order} \cite{MO} -- is
induced by the cone of all positive semi-definite $n\times n$ matrices: 
$A\le B$ 
(respectively, $A<B$) means that $B-A$ is positive semi-definite (respectively,
positive definite). Using our discussion so far and the arguments further 
below, we can prove the following extension of one of the main results in 
\cite{Lyons}: 

\begin{theorem}\label{th-lyo}
Let $A$ and $B$ be positive contractions such that $A \leq B$ and let 
$\mu$ and $\nu$ be their corresponding determinantal measures. Then 
$\mu \unlhd \nu$ and thus $\mu\pc \nu$. 
\end{theorem}

In \cite[Theorem 8.1]{Lyons} Lyons 
proved the last statement ($\mu\pc \nu$) in Theorem~\ref{th-lyo} under 
the additional hypothesis $[A,B]=0$. 







We will need the following elementary lemma. 

\begin{lemma}\label{l-dado}
If $A,B$ are positive semi-definite $n \times n$ matrices such that 
$A\le B<I$ then $A(I-A)^{-1} \leq B(I-B)^{-1}$.
\end{lemma}

\begin{proof}
By a standard density argument it is enough to prove the lemma for
positive definite matrices. Note first that if $C$ is a positive definite
$n\times n$ matrix such that $C\le I$ then $C^{-1}\ge I$. Moreover, if $D$ is
a positive definite $n\times n$ matrix such that $C\le D$ then 
$M^* CM\le M^* DM$ for any $n\times n$ matrix $M$ since
$$\langle M^* CMu, u\rangle =\langle CMu,Mu\rangle\le \langle DMu,Mu\rangle=
\langle M^* DMu, u\rangle$$
for any $u\in\CC^n$. The latter property with $M=D^{-1/2}$ yields 
$D^{-1/2}CD^{-1/2}\le I$, then by taking inverses and using the first 
property we get $D^{1/2}C^{-1}D^{1/2}\ge I$, and finally by using again the
second property with $M=D^{-1/2}$ we obtain $C^{-1}\ge D^{-1}$. Therefore, 
if $A,B$ are
positive definite matrices as in the lemma it follows
that $I-A^{-1}\le I-B^{-1}$, hence
$$A(I-A)^{-1}=-\left(I-A^{-1}\right)^{-1}\le -\left(I-B^{-1}\right)^{-1}=
B(I-B)^{-1},
$$
which is the desired conclusion.
\end{proof}

\begin{proposition}\label{dado}
Let $A$ and $B$ be positive semi-definite $n \times n$ matrices such that 
$A \leq B$ and set $Z=\diag(z_1,\ldots,z_n)$. Then 
$$
\frac {\det(I+AZ)}{\det(I+A)} \unlhd \frac{\det(I+BZ)}{\det(I+B)} 
\quad \mbox{ and } \quad 
\frac {\det(B+Z)}{\det(B+I)} \unlhd \frac{\det(A+Z)}{\det(A+I)}. 
$$
Moreover, if $A$ and $B$ are positive contractions, then 
$$
\det(I-A+AZ) \unlhd \det(I-B+BZ).
$$
\end{proposition}

\begin{proof}
We just prove the first inequality. The second inequality then follows upon 
considering the operation 
$$\det(I+MZ):=f_M(z_1, \ldots, z_n) \mapsto 
z_1\cdots z_nf_M(z_1^{-1},\ldots, z_n^{-1})$$  
with $M=A$ and $M=B$, respectively, which preserves the set of stable 
polynomials with non-negative coefficients 
(Proposition~\ref{pro-rs}) and obviously reverses the partial order $\unlhd$
(Theorem~\ref{addz}).
Similarly, for the third inequality note that if $A \leq B$ and $A,B$ are 
positive contractions then 













by continuity we may assume that $B<I$. But then  
$A'=A(I-A)^{-1} \leq B(I-B)^{-1}=B'$ by Lemma \ref{l-dado}, hence
$$
\det(I-A+AZ)= \frac {\det(I+A'Z)}{\det(I+A')} \unlhd 
\frac{\det(I+B'Z)}{\det(I+B')}=\det(I-B+BZ). 
$$

We claim that the polynomial  $f \in \RR[z_1,\ldots, z_n,y]$ defined by 
$$f(z,y)=\det(y(I+AZ)+I+BZ):=y^nP_0(z)+ y^{n-1}P_1(z)+\cdots + P_n(z),$$ 
where $z=(z_1,\ldots,z_n)$, is real stable with non-negative coefficients. 
Assuming this claim we see that 
since $P_k(z)= (n-k)!^{-1}\partial^{n-k}f/\partial y^{n-k}\big|_{y=0}$,  
by Remark \ref{dada} we have that 
$$
\det(I+AZ)=P_0 \ll P_1 \ll \cdots \ll P_n=\det(I+BZ), 
$$ 
which then settles the lemma (note that $P_k(0)=\binom n k$, so none of the 
$P_k$'s is identically zero). To prove the remaining claim, note that the 
polynomial 
$
G(z,y)= \det(A+y(B-A)+Z)
$
is stable with non-negative coefficients by Proposition \ref{det-pen}. 
Hence, so are the polynomials 
$$
F(z,y)= z_1\cdots z_ny^nG(z_1^{-1},\ldots, z_n^{-1},y^{-1})
=\det(y(I+AZ)+(B-A)Z) 
$$
and $F(z,y+1)=\det(y(I+AZ)+I+BZ)=f(z,y)$. 
\end{proof}









































































































\begin{proof}[Proof of Theorem~\ref{th-lyo}]
The generating polynomials of $\mu$ and $\nu$ are $\det(I-A+AZ)$ and 
$\det(I-B+BZ)$,  respectively. Combine Propositions~\ref{stdom} and~\ref{dado}.
\end{proof}

We end this section with an open question, namely whether the following
converse to Proposition~\ref{dado} holds. 

\begin{question}\label{q-pos-d}
Let $A$ and $B$ be positive semi-definite $n \times n$ matrices such that 
$$
\frac {\det(I+AZ)}{\det(I+A)} \unlhd \frac{\det(I+BZ)}{\det(I+B)},  
\quad \mbox{ or equivalently, } \quad 
\frac {\det(B+Z)}{\det(B+I)} \unlhd \frac{\det(A+Z)}{\det(A+I)},
$$
where $Z=\diag(z_1,\ldots,z_n)$. Is it true that $A\le B$?
\end{question}

Note that an affirmative answer to Question \ref{q-pos-d} would give a 
characterization of the Loewner order
on the cone of all positive semi-definite $n\times n$ matrices in terms
of determinantal stable polynomials.

\begin{remark}\label{r-spec}
Stochastic domination is closely related to the
notion of majorization (or spectral order) for real vectors 
that was axiomatized by Hardy-Littlewood-P\'olya 
and Schur \cite{HLP,MO}. The latter also induces a partial order (though not 
the same as the proper position) on univariate real-rooted polynomials, 
see, e.g., \cite{Bor}. 
\end{remark}


\subsubsection{Truncations of Strongly Rayleigh Measures and 
Polynomials}\label{sss-trunc}

We will now discuss certain truncations of stable polynomials and strongly 
Rayleigh measures.

\begin{lemma}\label{lum}
Suppose that  $f(z)= \sum_{\alpha\in\NN^n} a(\alpha) z^\alpha \in 
\RR[z_1,\ldots, z_n]$ is stable of total degree at most $d$ and has 
non-negative 
coefficients. For $0\le k\le d$ let 
$$
E_k(z)= \sum_{\mid \alpha \mid = k}a(\alpha)z^\alpha. 
$$
If $0\leq p \leq q \leq d$, then 
\begin{equation}\label{Eqp}
\sum_{k=p}^q \binom {q-p}{k-p} \frac {E_k(z)}{\binom {d}{k}}y^{q-k}
\end{equation}
 is a stable polynomial in the variables  $z_1, \ldots, z_n,y$.
\end{lemma}

\begin{proof}
Define a sequence of polynomials in $\RR[z_1, \ldots, z_n, y]$ as follows: 
\begin{eqnarray*} 
f_1(z,y) &=&  \sum a(\alpha) z^\alpha y^{d-|\alpha|} 
= \sum_{k=0}^d E_k(z)y^{d-k}, \\ 
f_2(z,y) &=& {\partial^ {d-q}f_1}/{\partial y^{d-q}}, \\
f_3(z,y) &=& y^{q}z_1^d\cdots z_n^d 
f_2(z_1^{-1}, \ldots, z_n^{-1}, y^{-1}), \\
f_4(z,y) &=&   {\partial^ {p}f_3}/{\partial y^{p}}, \\ 
f_5(z,y) &=& y^{q-p}z_1^d\cdots z_n^d 
f_4(z_1^{-1}, \ldots, z_n^{-1}, y^{-1}).
\end{eqnarray*}
By Theorem \ref{homhom},  $f_1$ is a stable polynomial, and by the 
closure properties of stable polynomials (Proposition~\ref{pro-rs}) 
we also have that $f_2, \ldots, f_5$ are stable. The polynomial $f_5$ is a 
constant multiple of \eqref{Eqp}. 
\end{proof}

The above lemma gives the following generalization of Newton's inequalities,
which correspond to the special case when $f(z)=(1+z_1)\cdots (1+z_n)$. 

\begin{corollary}\label{Newton-in}
Let $f(z)$ and $E_k(z)$, $k=0,\ldots,d$, be as in the statement of 
Lemma~\ref{lum}. Then 
\begin{equation}\label{N-IE}
\frac {E_k^2(z)}{{\binom {d}{k}}^2} \geq 
\frac {E_{k-1}(z)}{\binom {d}{k-1}}\frac {E_{k+1}(z)}{\binom {d}{k+1}}, 
\quad z \in \RR^n, 1 \leq k \leq d-1.
\end{equation}
\end{corollary}

\begin{proof}
By Lemma~\ref{lum}, the polynomial 
\begin{equation}\label{ert}
 (z,y)\mapsto \frac {E_{k-1}(z)}{\binom {d}{k-1}}y^2+ 
2\frac {E_k(z)}{\binom {d}{k}}y + \frac {E_{k+1}(z)}{\binom {d}{k+1}}
 \end{equation}
 is stable. Hence, for any fixed $z \in \RR^n$ the resulting
(univariate) polynomial in $y$ is real-rooted. The corollary 
 follows upon taking the discriminant in \eqref{ert}. 
 \end{proof}

Recall from Definition~\ref{d-trunc} the truncation $\mu_{p,q}$ 
of a measure $\mu$ to $[p,q]$. It has been discussed whether truncations of 
measures preserve negative dependence properties, cf.~\cite{J-DP,P} and 
references therein. As we show in Corollary \ref{cor-trunc} below, this is 
the case for strongly Rayleigh measures and truncations of length 
$q-p \leq 1$. 
Truncations of length 
$q-p \geq 2$ do not preserve the strong Rayleigh property. However, the 
weighted truncation suggested by \eqref{Eqp} obviously does. 

\begin{corollary}\label{cor-trunc}
Suppose that $\mu$ is a strongly Rayleigh probability measure 
on $2^{[n]}$ and that $0 \leq p \leq q \leq n$ with $q-p \leq 1$. 
Then $\mu_{p,q}$ is strongly Rayleigh. 
\end{corollary}

\begin{proof}
We prove the corollary for $q-p=1$. Let $f$ be the generating polynomial of 
$\mu$ and let $E_k$ be as in the statement of Lemma~\ref{lum}. Then the 
polynomial 
\begin{equation}\label{pq}
 g(z,y)=\frac {E_p(z)}{\binom {n}{p}}y + \frac {E_q(z)}{\binom {n}{q}} 
\end{equation}
is stable. Clearly, the generating polynomial of $\mu_{p,q}$ is a (positive)
constant multiple of $g(z,q/(n-p))$. The corollary follows since stable 
polynomials are closed under setting variables equal to real numbers, 
see Proposition~\ref{pro-rs}. 
\end{proof}

In \S \ref{s-countex} we show that Pemantle's Conjecture~\ref{st} (see 
\S \ref{s24}) fails in its full generality. However, it is true for strongly 
Rayleigh measures: 

\begin{theorem}\label{stst}
Let $\mu$ be a strongly Rayleigh probability measure on $2^{[n]}$, 
and let $1\leq k \leq n$. If 
$\mu(\{S : |S|=k-1\})\mu(\{S:|S|=k\}) \neq 0$, then 
$\mu_{k-1} \pc \mu_k$.  
\end{theorem}

\begin{proof}
Let $f$ be the generating polynomial of $\mu$ and let $E_k$ be as in the 
statement of Lemma~\ref{lum}. By assumption one has 
$E_{k-1}(\ben)E_k(\ben)\neq 0$, where $\ben\in\RR_+^n$ 
is as before the ``all ones 
vector''. From Lemma~\ref{lum} and the last part of Remark~\ref{dada} 
we deduce that the polynomial 
$$
F(z_1,\ldots,z_{n+1})=z_{n+1}
\frac{E_{k-1}(z_1,\ldots, z_n)}{E_{k-1}(\ben)} + 
\frac {E_{k}(z_1,\ldots, z_n)}{E_{k}(\ben)} 
$$
is stable. Since the above quotients are the generating polynomials
of $\mu_{k-1}$ and $\mu_k$, respectively, we have $\mu_{k-1} \unlhd \mu_k$ 
by Theorem \ref{addz} and Definition \ref{d-order}. The desired 
conclusion follows from Proposition \ref{stdom}. 
\end{proof}
