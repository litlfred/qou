---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-004-5-a-sequence-of-landen-transformations
section_title: "A sequence of Landen transformations"
section_number: 5
pages: 8-10
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.949
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
\label{sec-landen}
\setcounter{equation}{0}

The transformation theory of elliptic integrals was initiated 
by Landen in 1771. He proved the invariance of the function
\ba
G(a,b) & := & \int_{0}^{\pi/2} \frac{d \, \theta} 
{ \sqrt{ a^{2} \cos^{2} \theta + b^{2} \sin^{2}  \theta } }   \label{gab}
\ea
\no
under the transformation 
\ba
a_{1} = (a+b)/2 &  \qquad &  b_{1} = \sqrt{ab}, \label{transgl}
\ea
\no
i.e. that
\ba
G(a_{1},b_{1}) & = & G(a,b). \label{invargl}
\ea
\no
Gauss \cite{gauss1} rediscovered this invariance 
while numerically calculating the length of 
a lemniscate.  
An elegant proof of (\ref{invargl}) is given by 
Newman in \cite{newman}. Here, the substitution $x = b \tan \theta$ 
converts $2 G(a,b)$ into the integral of $\left[ (a^{2} + x^{2})
(b^{2} + x^{2}) \right]^{-1/2}$ over $\mathbb{R}$; the change of variable 
$t = (x-ab/x)/2$ then completes the proof. 

The Gauss-Landen transformation can be iterated to produce a 
double sequence $(a_{n},b_{n})$ such that $0 \leq a_{n} - b_{n} < 2^{-n}$.
It follows that $a_{n}$ and $b_{n}$ converge to a common limit, the so-called 
{\em arithmetic-geometric mean} of $a$ and $b$, denoted by $AGM(a,b)$. Passing 
to the limit in $G(a,b) = G(a_{n},b_{n})$ produces 
\ba
\frac{\pi}{2 AGM(a,b) } & = &
\int_{0}^{\pi/2} \frac{d \, \theta} 
{ \sqrt{ a^{2} \cos^{2} \theta + b^{2} \sin^{2}  \theta }}.
\ea
\no
The reader is referred to \cite{borbor} and \cite{mckmoll} for details. 


The goal of this section is to produce a map 
${{\mathfrak{T}}}_{2p}: {{\mathfrak{E}}_{2p}} \to 
{{\mathfrak{E}}_{2p}}$
that preserves the integral, i.e.
\ba
\int_{0}^{\infty} R(z) \, dz & = & \int_{0}^{\infty} 
{{{\mathfrak{T}}_{2p}}(R(z))} \, dz.  \label{invar}
\ea
\no
This map is the rational analog of the original Landen transformation 
(\ref{transgl}). 


\begin{Thm}
\label{thmbig}
Let $R(z) = P(z)/Q(z)$ with
\ba
P(z) = \sum_{j=0}^{p-1} b_{j} z^{2(p-1-j)} \text{   and   } \; \;
Q(z) = \sum_{j=0}^{p} a_{j} z^{2(p-j)}. \label{polyb}
\ea
\no
Define $a_{j}=0$ for $j>p$, $b_{j}=0$ for $j>p-1$, 
\ba
d_{p+1-j} & = & 
\sum_{k=0}^{j} a_{p-k} a_{j-k} 
\label{dofj}
\ea
\no
for $0 \leq k \leq p-1$,
\ba
d_{1} & = & 
\frac{1}{2} \sum_{k=0}^{p} a_{p-k}^{2},
\label{dofj1}
\ea
\ba
c_{j} & = & \sum_{k=0}^{2p-1} a_{j}b_{p-1-j+k} 
\label{cofj}
\ea
\no
for $0 \leq j \leq  2p-1$, and also
\ba
\alpha_{p}(i) & = & \begin{cases}
     2^{2i-1} \sum_{k=1}^{p+1-i} \frac{k+i-1}{i} \binom{k+2i-2}{k - 1}
d_{k + i} \text{    if } 1 \leq i \leq p    \\
     1 + \sum_{k=1}^{p} d_{k} \text{ if } i = 0. 
          \end{cases} 
\label{alpha}
\ea
\no
Let
\ba
a_{i}^{+} & = & \frac{\alpha_{p}(i)}{2^{2i} Q(1)^{2(1-i/p)}} 
\label{acoeff}
\ea
\no
for $1 \leq i \leq p-1$, and
\ba
b_{i}^{+} & = & Q(1)^{2i/p+1/p-2}  \times 
\left[ \sum_{k=0}^{p-1-i} (c_{k} + c_{2p-1-k}) \binom{p-1-k+i}{2i} 
\right] \label{bcoeff}  
\ea
\no
for $0 \leq i \leq p-1$. 
\no
Finally, define the polynomials 
\ba
P^{+}(z)  = {\sum_{k=0}^{p-1} b_{i}^{+} z^{2(p-1-i)}} & \text{ and } &
Q^{+}(z) = {\sum_{k=0}^{p} a_{i}^{+} z^{2(p-i)}}. \label{newb}
\ea
\no
Then ${\mathfrak{T}}_{2p}(R(z)) := P^{+}(z)/Q^{+}(z)$ satisfies 
{\rm{(\ref{invar})}}, i.e.
\ba
\int_{0}^{\infty} \frac{P(z)}{Q(z)} \; dz & = & 
\int_{0}^{\infty} \frac{P^{+}(z)}{Q^{+}(z)} \; dz. 
\ea
\end{Thm}

\begin{proof}
The first step is to convert the polynomial $Q(z)$ to its symmetric form: 
\ba
I := \int_{0}^{\infty} \frac{P(z)}{Q(z)} dz  = 
\int_{0}^{\infty} \frac{C(z)}{D(z)} dz \nn
\ea
\no
with 
\ba
C(z) & = & P(z) \times z^{2p} Q(1/z) := \sum_{k=0}^{2p-1} c_{k}z^{2k} \nn 
\\
D(z) & = & Q(z) \times z^{2p} Q(1/z) := \sum_{k=0}^{p} d_{p+1-k}
(z^{2k} + z^{2(2p-k)} ). \nn
\ea
\no
Then
\ba
I  & =  & \sum_{k=0}^{2p-1} c_{k} \int_{0}^{\infty} \frac{z^{2k} \; dz}
{Q^{s}(z)}. \nn
\ea
\no
Now employ the reduction formula in Section \ref{sec-reduc} to evaluate 
\ba
L_{k} & := & \int_{0}^{\infty} \frac{z^{2k} \; dz }{Q^{s}(z)}. \nn
\ea
\no
Observe that one needs to evaluate $L_{k}$ only for $0 \leq k \leq p-1$. 
Indeed, the usual symmetry rule yields 
$L_{k} = L_{2p-1-k}$.  The reduction formula now gives
\ba
L_{k} & = & 
\sum_{j=0}^{p-1-k} 2^{2j} \binom{p-1-k+j}{2j}  
\int_{0}^{\infty} \frac{z^{2(p-1-j)} \; dz}{ \sum_{i=0}^{p}
\alpha_{p}(i) z^{2(p-i)} } \nn \\
& = & \frac{1}{\alpha_{p}(p)} \sum_{j=1}^{p-k} 
2^{2(j-1)} \binom{p-k+j-2}{2j-2} \lambda^{2p-2j+1}  
\int_{0}^{\infty} \frac{z^{2(p-j)} \; dz}{\sum_{i=0}^{p} b_{i}^{+} z^{2(p-i)} }
\nn
\ea
\no
with $\alpha_{p}(i)$ as in (\ref{alpha}) and
$\lambda = \left[ \alpha_{p}(p)/\alpha_{p}(0) \right]^{1/2p}$. 
\end{proof}

\no
{\bf Note}. The extension of this transformation to the case  of 
\ba
\ift \frac{P(z)}{Q^{m+1}(z)} \, dz \nn
\ea
\no
requires explicit formulae for the coefficients of $P(z) \times 
\left( \, z^{2p} Q(1/z) \right)^{m+1}$ and 
$ Q^{m+1}(z) \times \left( \, z^{2p} Q(1/z) \right)^{m+1}$.
\vskip 10pt

\no
{\bf An algorithm for integration}.  Let ${\mathbf{x}} = 
( {\mathbf{a}}, {\mathbf{b}})$ with ${\mathbf{a}} = (a_{1}, \cdots, a_{p-1})$,
${\mathbf{b}} = (b_{0}, \cdots, b_{p-1})$, and let ${\mathfrak{O}}_{2p}^{+} = 
{\mathbb{R}_{+}}^{p-1} \times {\mathbb{R}_{+}}^{p}$. We then have a 
map 
\ba
\Phi_{2p}: {\mathfrak{O}}_{2p}^{+} & \to & {\mathfrak{O}}_{2p}^{+}   \nn \\
     {\mathbf{x}}:= ( {\mathbf{a}}, {\mathbf{b}} ) & \to & 
     {\mathbf{x}}^{+}:= ( {\mathbf{a}}^{+}, {\mathbf{b}}^{+} )  \nn
\ea
\no
where $a_{i}^{+}$ and $b_{i}^{+}$ are given in (\ref{acoeff},
\ref{bcoeff}).  
Iteration of this map, starting at ${\mathbf{x}}_{0}$, produces a sequence  
${\mathbf{x}}_{n+1} := \Phi_{2p}({\mathbf{x}}_{n})$ of points in 
${\mathfrak{O}}_{2p}^{+}$. The rational functions formed with these parameters
have integrals that remain constant along this orbit. Numerical studies
suggest the existence of a number $L = L({\mathbf{x}}_{0}) 
\in {\mathbb{R}}_{+}$ such that
\ba
{\mathbf{x}}_{n} & \to &  \left( 
\binom{p}{1}, \binom{p}{2}, \cdots, \binom{p}{p-1};
\binom{p-1}{0} \, L, \binom{p-1}{1} \, L, \cdots, 
\binom{p-1}{p-1} \, L \right).
\nn 
\ea
\no
Thus the integral of the original rational function is
$\tfrac{\pi}{2} \times L$. \\
