---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.943
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
\label{sec-intro} 
\setcounter{equation}{0}
 
We consider the space of
even rational functions of degree $2p$
\ba
{\E}_{2p} & := & \left\{ R(z) = \frac{P(z)}{Q(z)} \; {\Big{|}} \; 
P(z) := \sum_{k=0}^{p-1} b_{k} z^{2(p-1-k)} \text{ and }
Q(z) := \sum_{k=0}^{p} a_{k} z^{2(p-k)} \right\} \nn
\ea
\no
with positive real coefficients $a_{k}, \, b_{k} \in \rplus$ 
normalized by the condition $a_{0} = a_{p} = 1$,  the space
\ba
{\E}_{\infty}  & := & \bigcup_{p=1}^{\infty} {\E}_{2p} \nn
\ea
\no
of normalized even rational functions, and the set 
of $2p-1$ parameters 
$${\mathfrak{P}}_{2p} := \{ a_{1}, \cdots, a_{p-1}; b_{0}, \cdots, 
b_{p-1} \}.$$ 
\no
We describe an algorithm to determine, as a 
function of the parameter set 
${\mathfrak{P}}_{2p}$,  a {\em closed-form} expression of the 
integral 
\ba
I & := & \ift R(z) \, dz \label{integral1}
\ea
\no
for a large class of functions $R \in {\E}_{\infty}$. The function $R$ is 
called {\em symmetric} if its denominator $Q$ satisfies $Q(1/z) = z^{-2p}Q(z)$.
This is equivalent to its coefficients being palindromic, i.e.
$a_{j} = a_{p-j}$ for $1 \leq j \leq p$.  

The class of symmetric functions plays a crucial role in this 
algorithm.  Define
\ba
{\E}_{2p}^{s} & := & \{ R \in {\E}_{2p} \; {\Big{|}} \;  
den(R) \text{ is symmetric} \}
\nn
\ea 
\no
(where $den(R)$ denotes the denominator of $R$), 
the class of rational functions with symmetric denominators of degree $2p$, and
\ba
{\E}_{\infty}^{s}  & := & \bigcup_{p=1}^{\infty} {\E}_{2p}^{s}. \nn
\ea
\no
For $m \in \mathbb{N}$  define
\ba
{\E}_{2p}^{m} & := & \{ R \in {\E}_{\infty} \; {\Big{|}} \;  (den(R))^{1/(m+1)} 
\text{ is even, symmetric of degree } 2p \}
\nn
\ea 
\no
and ${\E}_{2p}^{m,s} := {\E}_{2p}^{m} \cap {\E}_{2p}^{s}$, so a function
$R \in {\E}_{2p}^{m,s}$ can be written in the form 
\ba
R(z) & = &  \frac{P(z)}{Q^{m+1}(z) }, \nn
\ea
\no
where $P(z)$ is an even polynomial and $Q(z)$ is an even 
symmetric polynomial of degree  $2p$. 


The method of partial fractions gives (in principle) the 
value of $I$ in terms of the roots of $Q$. Symbolic computations yield
either a closed-form answer, an expression in terms of the 
roots of an associated polynomial, or the integral returned unevaluated.

The algorithm described here allows only algebraic 
operations on elementary functions and changes of variables of the same type.
In particular, we exclude the solution of algebraic equations of degree higher 
than $2$.
We say that a rational function 
$R \in {\E}_{\infty}$ is {\em computable}  if its integral can be evaluated by 
our algorithm. 

The first step in the algorithm is to consider 
symmetric rational functions.  In Section \ref{sec-reduc}
we prove a reduction formula, i.e. a map 
${\mathfrak{F}}_{p} : {\E}_{2p}^{s} \to {\rat}_{p}$ that 
reduces the computability of the integral of the symmetric function 
$R$ to that of one
of degree $\tfrac{1}{2} deg(R)$. Here ${\rat}_{p}$ is the space of rational 
functions with denominator of degree $p$. These new
functions are not necessarily symmetric, and this is the main limitation 
of our algorithm. The details of 
${\mathfrak{F}}_{p}$ require the evaluation of some binomial sums which are 
presented in Appendix \ref{sec-binom}.  The classical Wallis' formula 
\ba
\ift \frac{dz}{(z^{2} + 1)^{m+1} } & = & \frac{\pi}{2^{2m+1}} \binom{2m}{m}
\nn
\ea
\no
shows that
every $R \in {\E}_{2}^{m}$ is computable. The reduction formula now 
implies that every $R \in {\E}_{4}^{m}$ is computable. This is 
described in Section
\ref{sec-quartic}.  The computability of $R \in {\E}_{4}$ is also a 
consequence of the 
classical theory of hypergeometric functions; the details are given
in \cite{hyp}. In Section \ref{sec-degree8} we compute the 
integral of every function in ${\E}_{8}^{m,s}$, where the reduction method 
expresses these integrals in terms of functions in ${\E}_{4}^{m}$.  The
algorithm does not, in general, provide a value for the integral of a 
nonsymmetric function of degree $8$. 

The final 
piece of the algorithm is described in Section \ref{sec-landen}: for 
$R \in {\E}_{2p}$, the 
symmetrization of its denominator produces a (symmetric) rational 
function in ${\E}_{4p}$ with the same integral as $R$. The
reduction formula now yields a new function in
${\E}_{2p}$ with the same integral as $R$. We thus obtain a map 
$ {\mathfrak{T}}_{2p}: {\E}_{2p} \to {\E}_{2p}$
such that 
\ba
\int_{0}^{\infty} R(z) \, dz & = & \int_{0}^{\infty} 
{{{\mathfrak{T}}_{2p}}(R(z))} \, dz.  \label{1invar}
\ea


\no
In particular, the class of computable rational functions of degree $2p$ is 
invariant under forward and backward iteration of ${\mathfrak{T}}_{2p}$. 
This map is the rational analog of the original Landen transformation 
for elliptic integrals described in \cite{borbor,mckmoll}.  The  map 
${\mathfrak{T}}_{2p}$ can also be interpreted as a map on the coefficients 
$\Phi_{2p} : {\mathfrak{O}}_{2p}^{+} \to 
{\mathfrak{O}}_{2p}^{+}$ where 
${\mathfrak{O}}_{2p}^{+} = 
{\mathbb{R}_{+}}^{p-1} \times {\mathbb{R}_{+}}^{p}$. 

The case of $\Phi_{6}$ is described in detail in  
Section \ref{sec-degree6} and
is given explicitly by 
\ba
a_{1} & \to & \frac{9 + 5a_{1} + 5a_{2} + a_{1}a_{2}}
{( a_{1} + a_{2} + 2)^{4/3} } \label{scheme6a}  \\
a_{2} & \to & \frac{a_{1} + a_{2}+6}{( a_{1} + a_{2} + 2)^{2/3} } \nn \\
b_{0} & \to & \frac{b_{0} + b_{1} + b_{2}}{(a_{1}+a_{2}+2)^{2/3} } \nn \\ 
b_{1} & \to & \frac{b_{0}(a_{2} + 2) + 2b_{1} + b_{2}(a_{1} + 3)}{ a_{1} + a_{2} + 2} \nn \\
b_{2} & \to & \frac{b_{0} + b_{2}}{( a_{1} + a_{2} + 2)^{1/3} }. \nn 
\ea

\no
Let ${\mathbf{x}}_{0}:= (a_{1},a_{2};b_{0},b_{1},b_{2})$. Then
$\Phi_{6}: {\mathfrak{O}^{+}_{6}} \to {\mathfrak{O}^{+}_{6}}$ is 
iterated to produce a sequence ${\mathbf{x}}_{n+1} := 
\Phi_{6}({\mathbf{x}}_{n})$
of points in ${\mathfrak{O}^{+}_{6}}$ that yield a sequence of
rational functions with constant integral. We have proved 
in \cite{landen} the existence of 
$L \in {\mathbb{R}^{+}}$, depending upon the initial 
point ${\mathbf{x}}_{0} = (a_{1},a_{2};b_{0},b_{1},b_{2}),$  such that  
${\mathbf{x}}_{n} \to 
(3,3;L,2L,L)$. Thus
\ba
\ift \frac{b_{0}z^{4} + b_{1}z^{2} + 
b_{2}}{z^{6} + a_{1}z^{4} + 
a_{2}z^{2} + 1} \; dz & = &  
L({\mathbf{x}}_{0}) \times \frac{\pi}{2}.  \label{int1}
\ea
\no
This establishes a numerical method to compute the integral in (\ref{int1}). 

Numerical studies on integrals of even degree $2p$ 
suggest the existence of a limiting value 
$L = L( {\mathbf{x}}_{0})$ such that the sequence 
${\mathbf{x}}_{n} := \Phi_{2p}( 
{\mathbf{x}}_{n} )$  satisfies 
\ba
{\mathbf{x}}_{n} & \to &  \left( 
\binom{p}{1}, \binom{p}{2}, \cdots, \binom{p}{p-1};
\binom{p-1}{0} \, L, \binom{p-1}{1} \, L, \cdots, 
\binom{p-1}{p-1} \, L \right).
\nn 
\ea
\no
The integral of the original rational function is thus
$\tfrac{\pi}{2} \times L({\mathbf{x}}_{0})$. The proof of convergence remains 
open for $p \geq 4$.  Examples are given in Section \ref{sec-examples}. 


The most important
issues left unresolved in this paper are the convergence of the iteration 
of the map $\Phi_{2p}$ discussed above and the geometric interpretation of 
the Landen transformation ${\mathfrak{T}}_{2p}$. Finally, the question of
integration of odd functions has not been addressed at all.

\vskip 20pt

\no
{\bf Some history}. The problem of 
integration of rational functions $R(z)=P(z)/Q(z)$ was 
considered by 
J. Bernoulli in the $18^{th}$ century.  He completed the original 
attempt by Leibniz
of a general partial fraction decomposition of $R(z)$. 
The main difficulty associated with this procedure is to obtain a 
complete factorization of $Q(z)$ over $\R$. Once this is known
the partial fraction decomposition of $R(z)$ can be  computed. The 
fact is that the primitive of a rational function is always 
elementary: it consists of a new rational function (its {\em rational 
part}) and the logarithm of a second rational function (its {\em 
transcendental part}). In his classic monograph \cite{hardy} G. H. Hardy states:
{\em The solution of the problem (of definite integration) in the case of 
rational functions may therefore be said to be complete; for the difficulty 
with regard to the explicit solution of algebraical equations is one not of 
inadequate knowledge but of proved impossibility}. He goes on to add: 
{\em It appears from the preceding paragraphs that we can always find the
rational part of the integral, and can find the complete integral if we 
can find the roots of} $Q(z) = 0 $. 

In the middle of the last century Hermite \cite{herm} and Ostrogradsky
\cite{ostro} developed algorithms to compute the rational part of the primitive
of $R(z)$ {\em without} factoring $Q(z)$. More recently Horowitz \cite{horo}
rediscovered this method and discussed its complexity.  The problem of 
computing the transcendental part of the primitive was finally solved by 
Lazard and Rioboo \cite{lazrio}, Rothstein \cite{roth} and 
Trager \cite{trag}.  For detailed descriptions and proofs of these algorithms 
the reader is referred to \cite{bron} and \cite{geddes}. 



\no
