---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-017-44-the-partial-symmetrization-procedure
section_title: "The Partial Symmetrization Procedure"
section_number: 4.4
pages: 29-31
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.963
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{n-s5}

Recall Remark~\ref{r-complex}, the partial 
symmetrization
of (complex) measures on $2^{[n]}$ defined in \eqref{t-theta}, and
Definition~\ref{d-rs-pol}. The main 
result of this section is the following theorem. 

\begin{theorem}\label{asym}
Let $\mu$ be a complex measure on $2^{[n]}$ with 
(complex) stable generating polynomial. Then for any  
transposition $\tau\in\fS_n$ and $\theta\in[0,1]$ the generating polynomial of
the partial symmetrization 
$\mu^{\tau,\theta}=\theta\mu+(1-\theta)\tau(\mu)$ is (complex) stable.
\end{theorem}


In particular, Theorem~\ref{asym} implies that the class of strongly
Rayleigh measures on $2^{[n]}$ is invariant under the partial symmetrization
procedure. Clearly, the latter result is real stable in nature. However, in 
order
to establish it we have to consider the (wider) complex stable context 
(cf.~Definition~\ref{d-rs-pol}), as in the above theorem. 

For the proof of Theorem~\ref{asym}
we need a multivariate generalization of the classical 
Obreschkoff theorem that was obtained in \cite{BBS2}. 

\begin{theorem}[Multivariate Obreschkoff theorem]
Let $f,g \in \RR[z_1, \ldots z_n]$. Then all non-zero polynomials in the space 
$
\{\alpha f + \beta g: \alpha, \beta \in \RR\}
$
are stable if and only if either $f +ig$ or $f-ig$ is stable or $f=g\equiv 0$. 
\end{theorem}

\begin{remark}
There are now elementary proofs of Theorem \ref{asym} that avoid the 
multivariate Obresckoff theorem, see \cite{BB,L3}. Also, the referee 
sketched an elementary proof similar to those given in \cite{BB,L3}.
\end{remark}














\begin{proof}[Proof of Theorem \ref{asym}] 
Let $f \in \CC[z_1,\ldots,z_n]$ be the generating polynomial of $\mu$. 
Hence $f$ is  stable and multi-affine. 
Assuming, as we may, that $i=1$ and $j=2$, we need to prove that 
$$
\theta f(\xi_1, \xi_2, \ldots, \xi_n)+(1-\theta) 
f(\xi_2, \xi_1,\ldots, \xi_n) \neq 0
$$
whenever $\xi_1, \ldots, \xi_n \in \{z :\Im(z)> 0\}$ 
(cf.~Definition~\ref{d-rs-pol}). By fixing 
$\xi_3,\ldots,\xi_n$ arbitrarily in the open upper half-plane and considering 
the multi-affine polynomial in variables $z_1,z_2$ given by
$$(z_1,z_2)\mapsto g(z_1,z_2):= f(z_1,z_2,\xi_3, \ldots, \xi_n)$$ 
we see that the problem reduces to proving that the linear operator 
$T_\theta$ on multi-affine polynomials in two variables defined by  
$$
T_\theta(h)(z_1,z_2)=\theta h(z_1,z_2)+(1-\theta)h(z_2, z_{1}) 
$$
preserves stability. Let us first show that $T_\theta$ preserves real 
stability. For this let  
$$f(z_1,z_2) = a_{00} + a_{01}z_2 + a_{10}z_1 + a_{11}z_1z_2 \in 
\RR[z_1,z_2]\setminus \{0\}$$ 
be real stable and set $D_f=a_{00}a_{11}-a_{01}a_{10}$. By 
Theorem~\ref{stable-Rayleigh} we know that 
$f$ is real stable if and only if $D_f \leq 0$. Since 
$$
D_{T_\theta(f)} = D_f - \theta(1-\theta)(a_{01}-a_{10})^2\le D_f
$$
it follows that $T_\theta(f)$ is also real stable, as required.
To deal with the (non-real) stable case let first
$h = g +if \in \CC[z_1,z_2]$ be {\em strictly stable} and multi-affine.  
This means that 
$h(z_1,z_2)\neq 0$ whenever $\Im(z_1) \geq 0$ and $\Im(z_2) \geq 0$.  By the 
multivariate Obreschkoff theorem we have that $\alpha g + \beta f$ is real  
stable or zero for all $\alpha, \beta \in \RR$. Hence, by the above, we also 
have that $\alpha T_\theta(f) + \beta T_\theta (g)$ is real stable or zero  
for all $\alpha, \beta \in \RR$. By the  multivariate Obreschkoff theorem 
again this gives that $T_\theta(g+ if)$ or 
$T_\theta(g- if)$ is stable. However, one has 
$$T_\theta(h)(z,z)=h(z,z)=g(z,z)+if(z,z),$$ 
which is strictly stable by assumption. If $T_\theta(g - if)$ is stable then $g(z,z)-if(z,z)$ is stable and 
$g(z,z)+if(z,z)$ is strictly stable which is impossible since it would imply that all zeros of (the strictly stable polynomial)  $g(z,z)+if(z,z)$ were real. Hence   
$T_\theta(g + if)$ is stable. 

Now if $\epsilon>0$ and $p\in\CC[z_1,z_2]$ is stable then clearly 
$p(z_1+i\epsilon,z_2+i\epsilon)$ is strictly stable (in the sense defined 
above) and thus any stable polynomial is the uniform limit on compact sets 
of strictly stable polynomials. By the multivariate version of 
Hurwitz' classical theorem on the ``continuity of zeros'' 
(see, e.g., \cite[Theorem 2.3]{BBS1} and \cite[Footnote 3, p.~96]{COSW}) 
this proves that $T_\theta$ preserves stability. 
\end{proof}

\begin{remark}\label{rem-sym}
From Theorem~\ref{asym} it follows that the symmetrization $\mu_s$ of a 
strongly Rayleigh measure $\mu$ is also strongly Rayleigh. A different 
proof is as follows. If $\mu$ is a strongly Rayleigh measure on $2^{[n]}$ 
then~\eqref{sym} implies that the diagonal
specialization $\De(g_{\mu_s})(t)=\De(g_{\mu})(t)$ (cf.~Definition~\ref{d-ulc})
is a real-rooted univariate polynomial and by the 
Grace-Walsh-Szeg\"o theorem we conclude that the symmetrization
$\mu_s$ of $\mu$ is also strongly Rayleigh.
\end{remark}
