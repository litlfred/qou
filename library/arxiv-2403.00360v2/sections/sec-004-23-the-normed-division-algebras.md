---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-004-23-the-normed-division-algebras
section_title: "The Normed Division Algebras"
section_number: 2.3
pages: 6-7
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.974
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
A division algebra is an algebra over a field where division is always well-defined, except by zero. A normed division algebra has the additional property that it is also a normed vector space, with the norm defined in terms of a conjugate. A well-known result by Hurwitz [@hurwitz1898ueber] states that there exist only four normed division algebras (over the field of real numbers): $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, being of dimensions one, two, four and eight, respectively. In going to higher-dimensional algebras, successive algebraic properties are lost: $\mathbb{R}$ is self-conjugate, commutative and associative, $\mathbb{C}$ is commutative and associative (but no longer self-conjugate), $\mathbb{H}$ is associative but no longer commutative, and finally $\mathbb{O}$ is neither commutative nor associative (but alternative).

The octonions $\mathbb{O}$ are the largest division algebra, of dimension eight. Its orthonormal basis is comprised of the seven imaginary units $e_1,...,e_7$ along with the unit $1=e_0$. A general octonion $x$ may then be written as $$x=x_0\, e_0+x_1\, e_1+...+x_7\, e_7 \qquad \text{with} \qquad x_0,...,x_7\in\mathbb{R} \:.$$ The octonionic *conjugate* $\overline{x}$ is defined as $\overline{x}=x_0e_0-x_1e_1-...-x_7e_7$. The *norm* of an octonion $x$ is subsequently defined by $\vert\vert x\vert\vert^2=x\overline{x}=\overline{x}x$, and the *inverse* of $x$ is given by $x^{-1}=\overline{x}/\vert\vert x\vert\vert^2$.

There are many different multiplication tables for octonions, with different authors using different multiplication rules. Here we will follow the multiplication table used in [@lohmus1994nonassociative], which is the multiplication table most naturally obtained via the Cayley-Dickson process. That is the multiplication of $e_0,e_1,e_2,e_3$ generates $\mathbb{H}$ and the multiplication of $e_0,e_1$ generates $\mathbb{C}$ (and of course $e_0$ generates $\mathbb{R}$ trivially). One way to represent octonion multiplication is in terms of the *Fano plane*; see Figure [1](#fanoplane){reference-type="ref" reference="fanoplane"}.

![The Fano plane, encoding the multiplicative structure of our octonions, where $a\equiv e_a,\; a=1,...,7$. Note that each line is cyclic, representing a quaternionic triple.](fanoupdated){#fanoplane}

The Fano plane representing the multiplication of octonion basis elements can be summarized as: $$e_ie_j= \left\{ \begin{array}{cl}
        e_j&\textrm{if}\;i=0\\
        e_i&\textrm{if}\;j=0\\
        -\delta_{ij}+\epsilon_{ijk}e_k&\textrm{otherwise}\:,
    \end{array} \right.$$ where $\epsilon_{ijk}$ is the completely antisymmetric tensor with value 1 when $ijk = 123$, $145$, $176$, $246$, $257$, $347$ or $365$.

Each projective line in the Fano plane corresponds (together with the identity $e_0$) to a quaternion ($\mathbb{H}$) subalgebra; there are seven such subalgebras. All the imaginary octonion units anti-commute under multiplication. Unlike for the smaller division algebras, the multiplication of elements not belonging to the same $\mathbb{H}$ subalgebra is *non-associative*. For example, $$e_4(e_7e_6) = -e_5 \neq e_5 = (e_4e_7)e_6 \:.$$ Octonion multiplication however is *alternative*, meaning that $$x(xy) = (xx)y \quad\text{and} \quad y(xx) = (yx)x \qquad \text{for all~$x,y\in\mathbb{O}$}\:.$$

By singling out one imaginary octonion basis element, an octonion can be written as $$\begin{aligned}
 \label{2.4}
x=(x_0+x_4e_4)e_0+(x_1-x_5e_4)e_1+(x_2-x_6e_4)e_2+(x_3-x_7e_4)e_3 \:.
\end{aligned}$$ This singling out of one of the imaginary basis elements of the octonions is equivalent to choosing a privileged subalgebra of $\mathbb{C}\otimes \mathbb{O}$, and induces a splitting of $\mathbb{O}$ as $\mathbb{C}\oplus\mathbb{C}^3$. Therefore, as vector spaces, the octonions $\mathbb{O}$ are therefore isomorphic to $\mathbb{C}^4$. this splitting of $\mathbb{O}$ as $\mathbb{C}\oplus\mathbb{C}^3$ has been associated with the lepton-quark splitting [@manogue1999dimensional]. The space of internal states of a quark then corresponds to the three complex dimensional space $\mathbb{C}^3$, whereas the internal space of a lepton is $\mathbb{C}$.

The automorphism group of $\mathbb{O}$ is the $14$-dimensional exceptional Lie group $G_2$. This exceptional group contains ${\rm{SU}}(3)$ as one of its maximal subgroups, corresponding to the stabilizer subgroup of one of the octonion imaginary units or, equivalently, the subgroup of $\text{Aut}(\mathbb{O})$ that preserves the representation of $\mathbb{O}$ as the complex space $\mathbb{C}\oplus \mathbb{C}^3$.

On account of being a division algebra, the octonions do not contain any projectors. One way to include projectors it to instead consider the complex octonions $\mathbb{C}\otimes \mathbb{O}$[^1], and this is one reason why in octonionic models it is inevitably the complex octonion algebra $\mathbb{C}\otimes\mathbb{O}$ that is considered, and not just $\mathbb{O}$. The algebra $\mathbb{C}\otimes\mathbb{O}$ is no longer a division algebra (even though the separate factors are), but $\mathbb{C}\otimes \mathbb{O}$ remains alternative. Two specific projectors can be introduced in $\mathbb{C}\otimes \mathbb{O}$ by singling out one of the octonion basis elements, say $e_4$. The the two mutually annihilating projectors are $$\rho_{\pm}=\frac{1}{2}(1 \pm ie_4) \:,$$ satisfying the relations $$\rho_-+\rho_+=1,\quad \rho_-^2=\rho_-,\quad \rho_+^2=\rho_+,\quad \rho_-\rho_+=\rho_+\rho_-=0 \:.$$

[^1]: Another option is to consider the split octonions algebra, which is not a normed division algebra, and does contain projectors. The split octonions differ from the octonions in that its quadratic form has a split signature $(4,4)$ whereas the octonions quadratic form has a positive-definite signature $(8,0)$.
