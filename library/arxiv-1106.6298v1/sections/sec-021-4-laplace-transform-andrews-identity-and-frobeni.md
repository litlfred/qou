---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-021-4-laplace-transform-andrews-identity-and-frobeni
section_title: "Laplace transform, Andrews identity and Frobenius maps"
section_number: 4
pages: 15-16
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.932
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
\label{map-frob}
The aim of this section is to define the Laplace transform
 and to study its image.




\subsection{Laplace transform}
To define the unified invariant we have to compute
$${\sum_n}^\xi q^{b\frac{n^2-1}{4}} A(n,k)$$
where  terms depending on $n$ in $A(n,k)$ look as follows
$$\prod^k_{i=0} (q^n+q^{-n}-q^i-q^{-i})\,=(-1)^{k+1}\;(q^n;q)_{k+1}\;
(q^{-n};q)_{k+1}\, .$$
Formally, the last expression can be considered as a Laurent polynomial
in $q$ and $q^{n}$. Hence we only have to compute
$${\sum_n}^\xi q^{b\frac{n^2-1}{4}} q^{na}\; ,$$
which can be easily done by the square completing argument.
Let us state the result.

Suppose $r$ is an odd number,  $b$ is positive integer and
$$ c:= (r,b), \quad b_1:= b/c, \quad r_1:=r/c.$$
\newcommand{\Tor}{{\rm Tor}}
\begin{lemma}{\rm [Beliakova--Le]}
\label{33}
One has
\begin{equation}
 \gamma_b(\xi) = c \,\gamma_{b_1}(\xi^c). \label{02}
 \end{equation}
\begin{equation}{\sum_{n}}^\xi q^{b \frac{n^2-1}{4}}\, q^{an} = \begin{cases}
0
&\text{if $c\, \nmid \, a$;}\\
 (\xi^c)^{-a_1^2 b_1^*}\; \gamma_b(\xi)  & \text{if $a=ca_1$},
 \end{cases}
 \end{equation}
where $b_1^\ast$ is an integer satisfying $b_1 b_1^* \equiv 1 \pmod{r_1}$.
\end{lemma}


This computation inspired us to introduce the following operator,
called the Laplace transform. Remember that $\int e^{ax^k} f(x)\, dx$
is called the Laplace transform
of $f$ of order $k$.

Let $\cL_{b,c;n}: \BZ[q^{\pm n},q^{\pm 1}] \to \BZ[q^{\pm  c/b}]$ be
the $\BZ[q^{\pm 1}]$--linear operator, called the (discrete)
Laplace transform (of the second order),
defined by
\be\label{four}
\cL_{b,c;n}(q^{na}) := \begin{cases}
0
&\text{if $c\, \nmid\,  a$;}\\
q^{-a^2/b}   & \text{if $a=ca_1$},
 \end{cases}
\ee
\begin{lemma} {\rm [Beliakova--Le]}
Suppose  $f \in \BZ[q^{\pm n},q^{\pm 1}]$. Then
$$ {\sum_{n}}^\xi q^{b\frac{n^2-1}{4}}  f = \gamma_b(\xi) \,
\ev_\xi(\cL_{b,c;n}(f)).
$$
\label{1000}
\end{lemma}




The point is that $\cL_{b,c;n}(f)$, unlike the left hand side
${\sum_{n}^\xi}  q^{b\frac{n^2-1}{4}} f$, does not depend on $\xi$.
To prove Theorem \ref{0078} we need  to show that
$\cL_{b,c;n} ((q^{n};q)_{k+1}\; (q^{-n};q)_{k+1})$ is divisible by
$(q^{k+1};q)_{k+1}$.
 For  this we use the remarkable identity
discovered by Andrews.
