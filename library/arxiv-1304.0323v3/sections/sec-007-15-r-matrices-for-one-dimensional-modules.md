---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-007-15-r-matrices-for-one-dimensional-modules
section_title: "R-matrices for one-dimensional modules"
section_number: 1.5
pages: 19-21
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 0.81
---
\label{subsec:R1}
Let $\mu=(\mu_1,\ldots, \mu_n)$ be a sequence of elements in $I$.
Let $L(\mu)$ be a free $\cor$-module $\cor u(\mu)$ with the
generator $u(\mu)$ of degree $0$. The following lemma can be easily
verified. \Lemma By defining \eqn &&x_k u(\mu)=0,\quad
\tau_ku(\mu)=0, \quad e(\nu) u(\mu) = \delta_{\nu,\mu} u(\mu),
\eneqn $L(\mu)$ becomes an  $R(\al_{\mu_1}+\cdots+\al_{\mu_n})$
-module if and only if \eq &&\parbox{70ex}{ \bna\item
$(\al_{\mu_k},\al_{\mu_{k+1}})<0$ for $1\le k<n$,
\item if  $\mu_{k}=\mu_{k+2}$ $(1\le k\le n-2)$,
then
$\lan h_{\mu_k}, \al_{\mu_{k+1}}\ran\not=-1$.
\ee
\label{cond:oned}}
\eneq
\enlemma

Now we assume \eqref{cond:sym}; i.e., $R$ is a symmetric \KLR.
The following lemma immediately follows from the definition.
\Lemma \label{lem:expliciteR_easiest cases}
Let $\mu=(\mu_1,\ldots,\mu_m)$
and $\nu=(\nu_1,\ldots,\nu_n)$
be a pair of sequences satisfying \eqref{cond:oned}. If $\mu_i\not=\nu_j$
for any $1\le i\le m$ and $1\le j\le n$,
then
$$R_{L(\mu)_z,L(\nu)_{z'}}\bl u(\mu)_z\tens u(\nu)_{z'}\br
=\tau_{n,m}\bl u(\nu)_{z'}\tens u(\mu)_z\br.$$
\enlemma

We shall use the following lemma later in the type $A$ case.
\Lemma \label{lem:expliciteR}
 Let $i \in I$  and  let  $\mu=(\mu_1,\ldots,\mu_n)$ be a sequence satisfying \eqref{cond:oned}.
Set $\beta=\sum_{k=1}^n\al_{\mu_k}$ and $p=\inp{\beta,\al_i}$.
Then we have
\eqn
&&
\ba{l}
R_{L(\mu)_z, L(i)_{z'}}(u(\mu)_z\tens u(i)_{z'})\\[1ex]
\hs{5ex}=\bl (z'-z)^p\tau_n\cdots\tau_1+\delta_{\mu_n,i}(z'-z)^{p-1}
\tau_{n-1}\cdots \tau_1\br
\bl u(i)_{z'}\tens u(\mu)_z\br,\\[2ex]
R_{L(i)_{z}, L(\mu)_{z'}}(u(i)_{z}\tens u(\mu)_{z'})\\[1ex]
\hs{5ex}=
\bl (z'-z)^p\tau_1\cdots\tau_n+\delta_{\mu_1,i}(z'-z)^{p-1}
\tau_{2}\cdots \tau_n\br
\bl u(\mu)_{z'}\tens u(i)_{z}\br.
\ea
\eneqn
\enlemma
\Proof
We shall prove only the second formula.
We prove it by induction on $n$.
 Since $n=1$ case is obvious, assume that $n>1$.
Set $\mu'=(\mu_2,\ldots,\mu_n)$ and $j=\mu_1$.

\smallskip
First assume that $i\not=j$.
Then we have
\eqn
&&R_{L(i)_{z}, L(j)_{z'}\circ L(\mu')_{z'}}(u(i)_{z}\tens u(j)_{z'}
\tens u(\mu')_{z'})\\
&&\hs{0.3ex}=
\bl L(j)_{z'}\circ R_{L(i)_{z}, L(\mu')_{z'}}\br\cdot
\Bigl(\bl R_{L(i)_{z}, L(j)_{z'}}(u(i)_{z}\tens u(j)_{z'})\br\tens u(\mu')_{z'}
\Bigr)\\
&&\hs{0.3ex}=
\bl L(j)_{z'}\circ R_{L(i)_{z},   L(\mu')_{z'} }\br
\Bigl(\tau_1(u(j)_{z'}\tens u(i)_{z})\tens u(\mu')_{z'}\Bigr)\\
&&\hs{0.3ex}=
\tau_1\bl L(j)_{z'}\circ R_{L(i)_{z},L(\mu')_{z'} }\br
\Bigl(u(j)_{z'}\tens u(i)_{z}\tens u(\mu')_{z'}\Bigr)  \\
&&\hs{0.3ex}=
\tau_1\Bigl( u(j)_{z'}\tens
 R_{L(i)_{z}, L(\mu')_{z'}}(u(i)_{z}\tens u(\mu')_{z'})\Bigr)\\
&&\hs{0.3ex}=
\tau_1\biggl( u(j)_{z'}\tens\Bigl(\bl
(z'-z)^p\tau_1\cdots \tau_{n-1}
+\delta_{i,\mu_2}(z'-z)^{p-1}\tau_2\cdots\tau_{n-1}\br
(u(\mu')_{z'}\tens u(i)_{z})\Bigr)\biggr).
\eneqn
Hence we obtain
\eqn
&&R_{L(i)_{z}, L(\mu)_{z'}}(u(i)_{z}\tens u(\mu)_{z'})\\
&&\hs{4ex}=
\bl
(z'-z)^p\tau_1(\tau_2\cdots \tau_n)
+\delta_{i,\mu_2}(z'-z)^{p-1}\tau_1(\tau_3\cdots\tau_{n})\br
(u(\mu)_{z'}\tens u(i)_z).
\eneqn
Then the last term vanishes since
$\tau_1u(\mu)_{z'}=0$.

Now assume that $i=\mu_1$. Then $\mu_2\not=i$.
Since we have
\eqn
R_{L(i)_z, L(i)_{z'}}(u(i)_z\tens u(i)_{z'})
&=&(\tau_1(x_1-x_2)+1)(u(i)_{z'}\tens u(i)_{z})\\
&=&((z'-z)\tau_1+1)(u(i)_z\tens u(i)_{z'}), \eneqn which gives \eqn
&&R_{L(i)_{z}, L(j)_{z'}\circ L(\mu')_{z'}}(u(i)_{z}\tens u(j)_{z'}
\tens u(\mu')_{z'})\\
&&\hs{3ex}=
\bl L(j)_{z'}\circ R_{L(i)_{z},\circ L(\mu')_{z'}}\br
\Bigl(\bl(z'-z)\tau_1+1\br u(i)_{z'}\tens u(i)_{z}\tens u(\mu')_{z'}\Bigr)\\
&&\hs{5ex}=
((z'-z)\tau_1+1)
(z'-z)^{p-1}\tau_2\cdots \tau_n
(u(i)_{z'}\tens  u(\mu')_{z'}\tens u(i)_{z}).
\eneqn
Hence we obtain the desired result.
\QED
