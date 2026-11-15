---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-001-2-the-reduction-formula
section_title: "The reduction formula"
section_number: 2
pages: 4-5
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.972
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
\label{sec-reduc}
\setcounter{equation}{0}

In this section we present a map ${\mathfrak{F}}_{p}: 
{\mathfrak{E}}_{2p}^{m,s} \to {\mathfrak{E}}_{p}^{m}$ that is the basis of the 
integration algorithm described in Section \ref{sec-landen}. The proof 
is elementary and the
binomial sums discussed in the Appendix are employed.  

Let $D_{p}(z)$ be the general symmetric polynomial of degree $4p$. We express
the integral of $z^{2n}/D_{p}^{m+1}$ as a linear combination of integrals of 
$z^{2j}/E_{p}^{m+1}$ where $E_{p}$ is a polynomial of degree $2p$ whose 
coefficients are determined by those of $D_{p}$. 
 

\begin{Thm}
\label{main}
Let $m,n,p \in \mathbb{N}$. Define 
\ba
D_{p}(d_{1},d_{2}, \cdots, d_{p};z) & = & \sum_{k=0}^{p} d_{p+1-k} 
(z^{2k} + z^{4p-2k})  \label{dp}
\ea
\no
and 
\ba
 E_{p}(d_{1},d_{2}, \cdots, d_{p}; z) & = & 
 \left( \sum_{j=1}^{p+1} d_{j} \right) z^{2p} + \nn \\
 & + & \sum_{i=1}^{p} 2^{2i-1} z^{2(p-i)} \sum_{j=1}^{p-i+1} 
   \frac{j+i-1}{i} \binom{j+2i-2}{j-1} d_{j+i}, \nn \\ 
 & & \label{ep}
\ea
\no
for $d_{i} \in {\mathbb{R}}_{+}$. Then 
for $ \; 0 \leq n \leq (m+1)p-1,$ 
\ba
\int_{0}^{\infty} \frac{ z^{2n} \; dz }{ \left( D_{p}(d_{1}, \cdots,d_{p};z) 
\right)^{m+1}  }   =   \nn
\ea
\ba
2^{-m} 
\sum_{j=0}^{(m+1)p-n-1} 4^{j} \binom{(m+1)p-n-1+j}{2j} 
\int_{0}^{\infty} \frac{ 
z^{2((m+1)p-1-j)}} 
{ \left( \, E_{p}(d_{1},\cdots, d_{p};z) \, \right)^{m+1} } \; dz,  \nn \\
& & \label{newmain}
\ea
\no
and for $(m+1)p - 1 < n < 2p(m+1)-1$ we employ the symmetry rule 
\ba
N_{n,p} & = & N_{2p(m+1)-1-n,p}.  \label{symrule}
\ea
\end{Thm}

\no
\begin{proof}
First observe that (\ref{symrule}) follows from the change of variable
$z \to 1/z$. Now consider
\ba
N_{n,p}(d_{1}, \cdots, d_{p};m) & := & 
 \int_{0}^{\infty} \frac{ z^{2n} \; dz }
{ \left( \; \sum_{k=0}^{p} d_{p+1-k} (z^{4p-2k} + z^{2k} ) \; \right)^{m+1}}
\label{nnp}
\ea
\no
for $0 \leq n \leq (m+1)p-1$. The 
substitution $z = \tan \, \theta$ yields 
\ba
N_{n,p} & = & 
   \int_{0}^{\pi/2}  \frac{ (1 - C^{2})^{n} C^{4(m+1)p-2n-2} \; d \theta }
{ \left( \; \sum_{k=0}^{p} d_{p+1-k} \left\{ (1-C^{2})^{2p-k} C^{2k} + 
(1-C^{2})^{k} C^{4p-2k} 
\right\} \; \right)^{m+1} },  \nn 
\ea
\no
where $C = \cos \theta$. Letting 
$\psi = 2 \, \theta$ and
$D = \cos \psi = 2C^{2} -1$ then gives 
\ba
N_{n,p} & = & \int_{0}^{\pi} 
\frac{ (1 - D^{2})^{n} (1+D)^{2(m+1)p-2n-1} \; d \psi }
{ \left( \; \sum_{k=0}^{p} d_{p+1-k} (1-D^{2})^{k} \left\{(1-D)^{2p-2k} + 
(1+D)^{2p-2k}  \right\}  \; \right)^{m+1} }. \nn
\ea
\no
Now observe that the integrals of the odd powers of cosine vanish when we 
expand $(1+D)^{2(m+1)p-2n-1}$, producing
\ba
N_{n,p} & = & 2^{-m} \int_{0}^{\pi/2}
\frac{(1-D^{2})^{n} \sum_{j=0}^{(m+1)p-n-1} \binom{2(m+1)p-2n-1}{2j} 
D^{2j} \, d \theta}
{ \left\{ \sum_{k=0}^{p} d_{p+1-k} (1-D^{2})^{k} \sum_{j=0}^{p-k} 
\binom{2p-2k}{2j} D^{2j} \right\}^{m+1} }.  \nn 
\ea
\no
A second double angle substitution $\varphi = 2 \psi$  gives 
\ba
N_{n,p} & = & 2^{-m} \int_{0}^{\pi}
\frac{(1-E)^{n} \sum_{j=0}^{(m+1)p-n-1} \binom{2(m+1)p-2n-1}{2j} 
2^{p(m+1)-n-j-1} (1+E)^{j} \, d \varphi}
{ \left\{ \sum_{k=0}^{p} d_{p+1-k} (1-E)^{k} \sum_{j=0}^{p-k} 
\binom{2p-2k}{2j} 2^{p-k-j} (1+E)^{j} \right\}^{m+1} },  \nn
\ea
\no
where $E  = \cos \varphi = 2D^{2} - 1$. The 
change of variable $z = \tan(\varphi/2)$ then yields 
\ba 
N_{n,p} & = & 2^{-m} \int_{0}^{\infty} 
\frac{ z^{2n}  \sum_{j=0}^{(m+1)p-n-1} \binom{2(m+1)p-2n-1}{2j} 
(1+z^{2})^{(m+1)p-n-j-1}
\, dz } 
{ \left\{ \sum_{k=0}^{p} d_{p+1-k} z^{2k} \left( \sum_{j=0}^{p-k} 
\binom{2p-2k}{2j} (1+z^{2})^{p-k-j} \right) \right\}^{m+1} }. \nn  \\
 & & \label{mess10}
\ea
\no
Finally, we modify (\ref{mess10}) using 
Lemma \ref{lem32} and Lemma \ref{lem34} with 
$N = (m+1)p-n-1$ to produce  (\ref{newmain}).
\end{proof}


Note that the previous theorem associates to each rational function 
of symmetric denominator
\ba
R_{1}(z) & = & \frac{b_{s}z^{2s} + b_{s-1}z^{2(s-1)} + \cdots + b_{0} }
{ \left( \, z^{4p} + d_{p} z^{4p-2} + \cdots + 2d_{1}z^{2p} + \cdots 
+ 1 \, \right)^{m+1} }  \nn
\ea
\no
a new rational function
\ba
R_{2}(z) & = & 2^{-m} \sum_{n=0}^{(m+1)p-1}  
b_{n} \sum_{j=0}^{(m+1)p-n-1} 4^{j} \binom{(m+1)p-n-1+j}{2j} 
\frac{z^{2((m+1)p-1-j)}} 
{ \left( E_{p}(d_{1},\cdots, d_{p};z) \right)^{m+1} } \; \nn
\ea
\no
such that 
\ba
\ift R_{1}(z) \, dz & = & \ift R_{2}(z) \, dz. \nn
\ea

\vskip 5pt

\no
