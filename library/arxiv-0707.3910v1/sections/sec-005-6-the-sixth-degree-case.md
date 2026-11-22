---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-005-6-the-sixth-degree-case
section_title: "The sixth degree case"
section_number: 6
pages: 10-11
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.991
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
\label{sec-degree6}
\setcounter{equation}{0}

We discuss the map 
${\mathfrak{T}}_{2p}: {{\mathfrak{E}}_{2p}} \to 
{{\mathfrak{E}}_{2p}}$
for the case $p=3$. The effect of ${\mathfrak{T}}_{6}$ on the 
coefficients 
${\mathfrak{P}}_{6} =  \{ b_{0},b_{1},b_{2},a_{1},a_{2} \}$
is denoted by $\Phi_{6} : {{\mathfrak{O}}}_{6}^{+} \to 
{{\mathfrak{O}}}_{6}^{+}$ and is given explicitly by 

\ba
a_{1} & \to & \frac{9 + 5a_{1} + 5a_{2} + a_{1}a_{2}}
{( a_{1} + a_{2} + 2)^{4/3} } \label{scheme6} \\
a_{2} & \to & \frac{a_{1} + a_{2}+6}{( a_{1} + a_{2} + 2)^{2/3} } \nn \\
b_{0} & \to & \frac{b_{0} + b_{1} + b_{2}}{(a_{1}+a_{2}+2)^{2/3} }  \nn \\
b_{1} & \to & \frac{b_{0}(a_{2} + 2) + 2b_{1} + b_{2}(a_{1} + 3)}{ a_{1} + a_{2} + 2} \nn \\
b_{2} & \to & \frac{b_{0} + b_{2}}{( a_{1} + a_{2} + 2)^{1/3} } \nn
\ea
\no
using Theorem \ref{thmbig}. The 
map $\Phi_{6}$  preserves the integral 
\ba
U_{6}(a_{1},a_{2},b_{0};b_{1},b_{2}) & := & 
\ift \frac{b_{0}z^{4} + b_{1}z^{2} + b_{2}}{z^{6} + a_{1}z^{4} + 
a_{2}x^{2} + 1} \; dz
\ea
\no
and the convergence of its iterations has been proved in \cite{landen}, the
main result of which is the following theorem. 

\begin{Thm}
Let ${\mathbf{x}}_{0}:= (a_{1}^{0},a_{2}^{0};b_{0}^{0},b_{1}^{0},b_{2}^{0})
\in {\mathbb{R}_{+}}^{5}$. Define
${\mathbf{x}}_{n+1} := \Phi_{6}({\mathbf{x}}_{n})$.  Then 
$U_{6}$ is invariant under $\Phi_{6}$.  Moreover, the 
sequence $\{ (a_{1}^{n},a_{2}^{n}) \}$ converges to $(3,3)$ and
$\{ (b_{0}^{n}, b_{1}^{n},b_{2}^{n}) \}$ converges 
to $(L, 2L,L)$, where the limit 
$L$ is a function of the initial data ${\mathbf{x}}_{0}$. 
Therefore
\ba
\ift \frac{b_{0}z^{4} + b_{1}z^{2} + 
b_{2}}{z^{6} + a_{1}z^{4} + 
a_{2}z^{2} + 1} \; dz & = &  
L({\mathbf{x}}_{0}) \times \frac{\pi}{2}.  \nn
\ea
\end{Thm} 

\no
This iteration is similar to Landen's transformation for elliptic integrals
that has been employed in \cite{borbor} in the efficient calculation of $\pi$. 
Numerical data indicate
that the convergence of ${{\mathbf{x}}}_{n}$ is 
quadratic. The proof of convergence is based  on the fact that $\Phi_{6}$
cuts the distance from $(a_{1},a_{2})$ to $(3,3)$ by at least half.  \\

\no
{\bf A sequence of algebraic curves}. The complete characterization of 
parameters $(a_{1},a_{2})$ in the first quadrant  that yield computable 
rational functions 
\ba
R(z) & := & 
\frac{b_{0}z^{4} + b_{1}z^{2} + 
b_{2}}{z^{6} + a_{1}z^{4} + 
a_{2}z^{2} + 1}. \nn
\ea
\no
of degree $6$ remains open. The  polynomial 
$z^{6} + a_{1}z^{4} + a_{2}z^{2} + 1$ factors when 
$a_{1} = a_{2}$ so the diagonal
$\Delta  :=  \{ (a_{1},a_{2}) \in  {\R}_{+} \times {\R}_{+}: a_{1} = a_{2} \} $
produces computable functions. 
In view of the invariance of the class of computable functions 
under iterations by $\Phi_{6}$, the  curves 
${\mathbb{X}}_{n} := \Phi_{6}^{(-n)}(\Delta)$, with $n \in {\mathbb{Z}}$, are 
also computable.

The curve  ${\mathbb{X}}_{1}$ has equation 
\ba
(9 + 5a_{1} + 5a_{2} + a_{1}a_{2})^{3} & = & (a_{1} + a_{2} + 2)^{2} 
(a_{1} + a_{2} + 6)^{3}  \nn
\ea
\no
and consists of two branches meeting at the cusp $(3,3)$. In terms 
of the coordinates $x = a_{1} - 3$ and $y = a_{2} - 3$ the leading order 
term is $T_{1}(x,y) = 1728(x-y)^2$. This curve 
is rational and can be parametrized by 
\ba
a_{1}(t) & = & t^{-2}( t^{5} -t^{4} + 2t^{3} -t^{2} + t + 1) \label{param1} \\
a_{2}(t) & = & t^{-3}( t^{5} +t^{4} - t^{3} + 2t^{2} - t + 1). \nn
\ea

The rationality of ${\mathbb{X}}_{n}$ for $n \neq 1$ and its significance 
for the integration algorithm remains open. The  complexity 
of these curves increases with $n$. For example, the curve 
${\mathbb{X}}_{2} := \Phi_{3}^{(-2)}(\Delta)$ is of total degree $90$ in 
$x = a_{1} -3$ and $y=a_{2}-3$ with leading term
\ba
T_{2}(x,y) & := & 2^{121} 3^{35} (x-y)^{18} \left[ -163(x^{4} + y^{4}) +
668xy(x^{2} + y^{2}) -1074x^{2}y^{2} \right]. \nn
\ea
\no
The diagonal $\Delta$ can be replaced by a $2$-parameter family of 
computable curves ${\mathbb{X}}(c,d)$ that are produced from the factorization 
of the sextic with $a_{1} = c+d$ and $a_{2} = cd + 1/d$.  All the images 
$\Phi_{6}^{(-n)}{\mathbb{X}}(c,d)$ with $n \in {\mathbb{Z}}$ are computable
curves.  The question of whether these are {\em all }
the computable parameters remains open.
