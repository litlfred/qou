---
doc_id: arxiv-2306.13098v2
doc_title: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-003-the-cayley-dickson-construction-and-the-algebra
section_title: "The Cayley-Dickson construction and the algebra of sedenions"
section_number: null
pages: 6-6
source_pdf: 2306.13098v2.pdf
source_sha256: edeb214d587bfca4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.979
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
---
[]{#sedenions label="sedenions"}

The CD process is an iterative construction that generates at each stage an algebra (with involution) of dimension twice that of the previous. Each algebra is constructed as a direct sum of the previous algebra, so that $\mathbb{C}=\mathbb{R}\oplus\mathbb{R}i$ where $i$ is the complex structure introduced in the process. Similarly, $\mathbb{H} = \mathbb{C} \oplus \mathbb{C} J$, where $i$, $J$ and $iJ$ are identified with the quaternion imaginary bases $I, J, K$, and similarly $\mathbb{O} = \mathbb{H}\oplus\mathbb{H}i_4$.

This process does not terminate with $\mathbb{O}$ but continues, generating a series of $2^n$-dimensional (non division) algebras. A generic element of the CD algebra $\mathbb{A}_n$, can then be written as $a+bu$, where $a,b \in \mathbb{A}_{n-1}$, and $u$ is the new imaginary unit introduced by the CD process applied to $\mathbb{A}_{n-1}$. The fifth CD algebra $\mathbb{A}_{4}$ ($\mathbb{A}_{0}=\mathbb{R}$), generated from $\mathbb{O}$, is the 16-dimensional algebra of sedenions $\mathbb{S}$. This algebra is non-commutative, non-associative, and not even alternative ($x(xy) \neq (xx)y$ and $y(xx) \neq (yx)x$ in general). Other properties, like flexibility ($(xy)x = x(yx)$) and power-associativity ($x^n$ associative), still hold (and hold for all CD algebras).

An orthonormal basis for $\mathbb{S}$ comprises 15 mutually anticommuting imaginary units $s_1,...,s_{15}$ together with the unit $1=s_0$. The imaginary units $s_1,..,s_7$ correspond to the original octonion units $i_1,...,i_7$. A general sedenion may then be written as $$\begin{aligned}
    w=w_0s_0+w_1s_1+...+w_{15}s_{15},\quad w_0,...,w_{15}\in\mathbb{R}.
\end{aligned}$$ with the sedenion conjugate $\overline{w}$ defined as $\overline{w}=w_0s_0-w_1s_1-...-w_{15}s_{15}$, and the sedenion norm $\vert w\vert$ defined by $\vert w\vert ^2=w\overline{w}=\overline{w}w$. Whenever $\vert w\vert ^2\neq 0$, the inverse of $w$ is given by $w^{-1}=\overline{w}/\vert w \vert^2$.

The product of two sedenions $w,v$ can be determined using the multiplication table of the orthonormal basis units of $\mathbb{S}$ provided in Appendix A, source [@lohmus1994nonassociative; @cawagas2004structure], together with linearity.

Because $\mathbb{S}$ is not a division algebra, it contains zero divisors. These are elements of the form $$\begin{aligned}
(s_a+s_b)(s_c+s_b)=0,\qquad s_a,s_b,s_c,s_d\in\mathbb{S}.
\end{aligned}$$ There are 84 such zero divisors, and the subspace of zero divisors of unit norm is homeomorphic to $G_2$ [@moreno1997zero].
