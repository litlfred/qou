---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-002-3-the-quartic-case
section_title: "The quartic case"
section_number: 3
pages: 5-7
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.86
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
\label{sec-quartic}
\setcounter{equation}{0}


In this section we describe the computability of rational functions 
$R \in {\E}_{4}^{m}$. These are functions of the form 
\ba
R(z) & = &  \frac{P(z)}{(z^{4} + 2az^{2} + 1)^{m+1} } \nn
\ea
\no
where $P(z)$ is an even polynomial of degree $4m+2$. Observe that
the normalization $a_{0}=a_{2} = 1$ makes the denominator of $R$ 
automatically symmetric.  It suffices to evaluate
\ba
N_{n,4}(d_{1};m) & := &  \int_{0}^{\infty} \frac{z^{2n} \; dz}{(z^{4} + 2d_{1}z^{2} 
+1)^{m+1} } \label{n04}
\ea
\no
where $0 \leq n \leq 2m+1$ is required for convergence. From (\ref{symrule}) 
we have
$N_{n,4}(d_{1};m)  =  N_{2m-1-n,4}(d_{1};m)$, so we
may assume $0 \leq n \leq m$. 
We now employ Theorem \ref{main} to obtain a closed form expression 
for $N_{n,4}(d_{1};m)$.  

\begin{Thm}
\label{mainthm}
Let $m \in \mathbb{N}$ and assume $0 \leq n \leq m$. Then 
\ba
N_{n,4}(d_{1};m) := \int_{0}^{\infty} \frac{z^{2n} \; dz}
{ \left( z^{4} + 2d_{1}z^{2} + 1 \right)^{m+1} } \; \; =  \label{quartic1}
\ea
\ba
\frac{\pi}{ 2^{3m+3/2} (1+a)^{m+1/2} } \times 
\sum_{j=0}^{m-n} 2^{j}(1+d_{1})^{j} \times
\binom{2m-2j-1}{m-j}  \binom{m-n+j}{2j} \binom{2j}{j}
\binom{m}{j}^{-1} . \nn
\ea
\no
For $m+1 \leq n \leq 2m+1$ we have
\ba
\int_{0}^{\infty} \frac{z^{2n} \; dz}
{ \left( z^{4} + 2d_{1}z^{2} + 1 \right)^{m+1} } \; \; =  \label{quartic2}
\ea
\ba
\frac{\pi}{ 2^{3m+3/2} (1+d_{1})^{m+1/2} } \times 
\sum_{j=0}^{n-m-1} 2^{j}(1+d_{1})^{j} \times
\binom{2m-2j-1}{m-j}  \binom{m-n+j}{2j} \binom{2j}{j}
\binom{m}{j}^{-1} . \nn
\ea
\end{Thm}

\begin{proof}
We apply the result of the Theorem \ref{main} with 
$D_{1}(d_{1};z)  =  z^{4} + 2d_{1}z^{2} + 1 $ and
$E_{1}(d_{1};z) = (1 + d_{1})z^{2} + 2$, so that 
\ba
\int_{0}^{\infty} \frac{z^{2n} \, dz }{(z^{4} + 2d_{1}z^{2} + 1)^{m+1} } & = &
2^{-m} \sum_{j=0}^{m-n} 4^{j} \binom{m-n+j}{2j} 
\int_{0}^{\infty} \frac{z^{2(m-j)} \, dz}{ ( (1+d_{1})z^{2} + 2 )^{m+1} }. \nn
\ea
\no
The change of variable $u = (1+d_{1})z^{2}/2$ then yields
\ba
\int_{0}^{\infty} \frac{z^{2(m-j)} \, dz}{ ( \; (1+d_{1})z^{2} + 2 \; )^{m+1} } 
& = &  2^{-(j+3/2)} (1+d_{1})^{-m+j-1/2} 
\int_{0}^{\infty} \frac{u^{m-j-1/2} \; du }{(1+u)^{m+1} }
\nn \\
 &  = & \pi \binom{2m-2j}{m-j} \binom{2j}{j} \binom{m}{j}^{-1} 2^{-(2m+j+3/2)}
(1+d_{1})^{-(m-j+1/2)}, \nn
\ea
\no
where we have used
\ba
\ift \frac{u^{r- 1/2}}{(1+u)^{s}} \, du & = & 
\frac{\pi}{2^{2(s-1)}} \binom{2r}{r} \binom{2(s-r-1)}{s-r-1} 
\binom{s-1}{r}^{-1}. \nn
\ea
\end{proof}

\no
The algorithm also requires a scaled version of $N_{0,4}(d_{1};m)$. 

\no
\begin{Cor}
\label{cor62}
Let $b>0, \, c>0,\; a > - \sqrt{bc}, \, m \in \mathbb{N}$, 
and $0 \leq n \leq m$. Define
\ba
N_{n,4}(a,b,c;m) & := &  \ift \frac{z^{2n} \; dz}{ \left( bz^{4} + 2az^{2} + c 
\right)^{m+1}}. \nn
\ea
\no
Then for $0 \leq n \leq m$, 
\ba
N_{n,4}(a,b,c;m) & = & 
 \pi \left( c (c/b)^{m-n} \left\{ 8(a + \sqrt{bc}) \right\}^{2m+1} 
\right)^{-1/2} \times  \nn \\
 & & \times
\sum_{k=0}^{m-n} 2^{k} \binom{2m-2k}{m-k} \binom{m-n+k}{2k} 
\binom{2k}{k} \binom{m}{k}^{-1} \left( \frac{a}{\sqrt{bc}} +1 
\right)^{k}, \nn \\
 &  & \label{sum1}
\ea
and for $m+1 \leq n \leq 2m+1$, 
\ba
N_{n,4}(a,b,c;m) & = & 
 \pi \left( c (c/b)^{m-n} \left\{ 8(a + \sqrt{bc}) \right\}^{2m+1} 
\right)^{-1/2} \times  \nn \\
 & & \times
 \sum_{k=0}^{n-m-1} 2^{k} 
\binom{2m-2k}{m-k} \binom{m-n+k}{2k} 
\binom{2k}{k} \binom{m}{k}^{-1} \left( \frac{a}{\sqrt{bc}} + 1 \right)^{k}.
\nn \\
 &  & \label{sum2}
\ea
\end{Cor}

\begin{proof}
Let $0 \leq n \leq m$. The substitution $u = z (b/c)^{1/4}$ yields
\ba
N_{n,4}(a,b,c;m) & = & 
\frac{1}{c^{m-n/2 + 3/4} b^{n/2 + 1/4} } N_{n,4} 
\left( \frac{a}{\sqrt{bc}} ; m \right), \label{scaled}
\ea
\no
so (\ref{sum1}) then follows from Theorem \ref{mainthm}.
From (\ref{symrule}) we have
$N_{n,4}(a,b,c;m)  =  
N_{2m+1-n,4}(c,b,a;m)$ for $m+1 \leq n \leq 2m+1$, giving (\ref{sum2}).
\end{proof}
