---
doc_id: arxiv-2306.13098v2
doc_title: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-001-normed-division-algebras
section_title: "Normed division algebras"
section_number: null
pages: 3-5
source_pdf: 2306.13098v2.pdf
source_sha256: edeb214d587bfca4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.891
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
---
[]{#sec:normeddivisionalgebras label="sec:normeddivisionalgebras"}

A division algebra is an algebra over a field where division is always well-defined, except by zero. A normed division algebra has the additional property that it is also normed vector spaces, with the norm defined in terms of a conjugate. A well-known result by Hurwitz [@hurwitz1898ueber] is that there exist only four normed division algebras (over the field of real numbers): $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, of dimensions one, two, four and eight respectively. In going to higher-dimensional algebras, successive algebraic properties are lost: $\mathbb{R}$ is self-conjugate, commutative and associative, $\mathbb{C}$ is commutative and associative (but no longer self-conjugate), $\mathbb{H}$ is associative but no longer commutative, and finally $\mathbb{O}$ is neither commutative nor associative (but alternative).

The quaternions $\mathbb{H}$ are a generalization of the complex numbers $\mathbb{C}$ with three mutually anticommuting imaginary units $I,J,K$, satisfying $I^2=J^2=K^2=IJK=-1$, which implies $IJ=K=-JI$, $JK=I=-KJ$, and $KI=J=-IK$. A general quaternion $q$ may then be written as $$\begin{aligned}
    q=q_01+q_1I+q_2J+q_3K,\qquad q_0,q_1,q_2,q_3\in\mathbb{R},
\end{aligned}$$ With the quaternion conjugate $\overline{q}$ defined as $\overline{q}=q_0-q_1I-q_2J-q_3K$. The norm of a quaternion $\vert q\vert$ is subsequently defines by $\vert q\vert^2=q\overline{q}=\overline{q}q$, and the inverse $q^{-1}=\overline{q}/\vert q\vert^2$.

The automorphism group of $\mathbb{H}$ is $SU(2)$. Indeed, there is an isomorphism between the quaternions $\mathbb{H}$ and the real Clifford algebra $C\ell(0,2)$, while the complexified quaternions $\mathbb{C}\otimes\mathbb{H}$ (isomorphic to the Pauli algebra) are isomorphic to the complex Clifford algebra $\mathbb{C}\ell(2)$. Note, however, that $\mathbb{C}\otimes\mathbb{H}$ is not a division algebra (but remains associative), and manifestly contains projectors, for example: $(1+iK)(1-iK)=0$.

The octonions $\mathbb{O}$ are the largest division algebra, of dimension eight. Its orthonormal basis comprises seven imaginary units: $i_1,...i_7$, along with the unit $1=i_0$. A general octonion $x$ may then be written as $$\begin{aligned}
    x=x_0i_0+x_1i_i+...+x_7i_7,\qquad x_0,...,x_7\in\mathbb{R},
\end{aligned}$$ with the octonion conjugate $\overline{x}$ defined as $\overline{x}=x_0i_0-x_1i_1-...-x_7i_7$. The norm of an octonion $\vert x\vert$ is subsequently defines by $\vert x\vert^2=x\overline{x}=\overline{x}x$, and the inverse $x^{-1}=\overline{x}/\vert x\vert^2$.

The multiplication of octonions[^1] is captured in terms of the Fano plane Fig. [1](#fanoplane){reference-type="ref" reference="fanoplane"}. Each projective line in the Fano plane corresponds (together with the identity $i_0$) to an $\mathbb{H}$ subalgebra; there are seven such subalgebras. Like with $\mathbb{H}$, all the imaginary units anticommute under multiplication. Unlike with $\mathbb{H}$, the multiplication of elements not belonging to the same $\mathbb{H}$ subalgebra is non-associative. For example $i_4(i_7i_6) = -i_5 \neq i_5 = (i_4i_7)i_6$. Octonion multiplication however is alternative $x(xy) = (xx)y$ and $y(xx) = (yx)x$, $\forall x,y\in\mathbb{O}$. The complexified octonions $\mathbb{C}\otimes \mathbb{O}$ are again not a division algebra (but remains alternative).

![The Fano plane, encoding the multiplicative structure of our octonions, where $a\equiv i_a,\; a=1,...,7$. Note that each line is cyclic, representing a quaternionic triple.](fanoupdated){#fanoplane}

As vector spaces $\mathbb{O}=\mathbb{C}^4$. The splitting of $\mathbb{O}$ as $\mathbb{C}\oplus\mathbb{C}^3$ relies on choosing a preferred octonion unit $i_a$ (and hence a preferred $\mathbb{C}$ subalgebra in $\mathbb{O}$). For our purpose we choose $i_4$. The map [@manogue1999dimensional] $$\begin{aligned}
\pi(x)=\frac{1}{2}(x+i_4x\Bar{i_4}),\quad x\in\mathbb{O},
\end{aligned}$$ where $\Bar{i_4}$ indicates the octonion conjugation, then projects $\mathbb{O}$ down to this preferred $\mathbb{C}\subset \mathbb{O}$, and we can write the octonion $x=x_0i_0+...+x_7i_7$ as: $$\begin{aligned}
x=(x_0+x_4i_4)i_0+(x_1-x_5i_4)i_1+(x_2-x_6i_4)i_2+(x_3-x_7i_4)i_3.
\end{aligned}$$ Note that the product $i_4x\Bar{i_4}$ is defined unambiguously since $\mathbb{O}$ is alternative.

The automorphism group of $\mathbb{O}$ is the $14$-dimensional exceptional Lie group $G_2$. This exceptional group contains $SU(3)$ as one of its maximal subgroups, corresponding to the stabilizer subgroup of one of the octonion imaginary units, or equivalently, the subgroup of $Aut(\mathbb{O})$ that preserves the representation of $\mathbb{O}$ as the complex space $\mathbb{C}\oplus \mathbb{C}^3$. This splitting is associated with the quark-lepton symmetry [@manogue1999dimensional]. The space of internal states of a quark is then the three complex dimensional space $\mathbb{C}^3$ whereas the internal space of a lepton is $\mathbb{C}$.

Since $\mathbb{O}$ and $\mathbb{C}\otimes\mathbb{O}$ are nonassociative, they are not representable as matrix algebras (with the standard matrix product). The algebra generated from the composition of left and right actions of $\mathbb{O}$ (and $\mathbb{C}\otimes\mathbb{O}$) however is associative, since each such left (right) action corresponds to a linear operator (endomorphism).

Let $L_a$ ($R_a$) denote the linear operator of left (right) multiplication by $a\in\mathbb{C}\otimes\mathbb{O}$: $$\begin{aligned}
    L_a[x]=ax,\quad R_a[x]=xa,\quad \forall a,x\in  \mathbb{C}\otimes\mathbb{O}.
\end{aligned}$$ Then $$\begin{aligned}
    L_aL_b[x]&=&a(bx) \quad \neq \quad L_{ab}[x]=(ab)x,\\
    R_aR_b[x]&=&(xb)a \quad \neq \quad R_{ab}[x]=x(ab).
\end{aligned}$$ The mappings $a\rightarrow L_a$ and $a\rightarrow R_a$ do not correspond to algebra homomorphisms as they each generate an associative algebra called the *associative multiplication algebra*[^2]. They do however preserve the quadratic relations $\langle x,y\rangle=\frac{1}{2}(x\overline{y}+y\overline{x})$ where $x,y\in \mathbb{C}\otimes\mathbb{O}$ $$\begin{aligned}
    L_xL_{\overline{y}}1+L_yL_{\overline{x}}1=2\langle x,y \rangle 1=R_xR_{\overline{y}}1+R_yR_{\overline{x}}1.
\end{aligned}$$

Since $L_a$ ($R_a$) correspond to linear operators, they can be represented as $8\times 8$ complex matrices (acting on the vector space $\mathbb{C}\otimes\mathbb{O}$ written as a column vector).

For $\mathbb{C}\otimes\mathbb{O}$, one finds the following identities [@dixon2013division; @furey2016standard]: $$\begin{aligned}
    L_{i_1}L_{i_2}L_{i_3}L_{i_4}L_{i_5}L_{i_6}x&=&L_{i_7}x,\\
    ...L_{i_b}L_{i_a}L_{i_a}L_{i_c}....x&=&-...L_{i_b}L_{i_c}....x,\\
    ...L_{i_a}L_{i_b}...x&=&-...L_{i_b}L_{i_a}...,
\end{aligned}$$ where $a,b,c=1,...,7$.

Due to the nonassociativity of $\mathbb{O}$, the left (right) associative multiplication algebra of $\mathbb{C}\otimes\mathbb{O}$ contains genuinely new maps which are not captured by $\mathbb{C}\otimes\mathbb{O}$. For example, $i_3(i_4(i_6+i_2))\neq y(i_6+i_2)$ for any $y\in\mathbb{C}\otimes\mathbb{O}$. There are a total of 64 distinct left-acting complex-linear maps from $\mathbb{C}\otimes\mathbb{O}$ to itself, and these (due to the given identities above) provide a faithful representation of $\mathbb{C}\ell(6)$.

Denoting the 64-dimensional left (right) associative multiplication algebra generated from left (right) actions of $\mathbb{C}\otimes\mathbb{O}$ on itself by $(\mathbb{C}\otimes\mathbb{O})_L$ ($(\mathbb{C}\otimes\mathbb{O})_R$), one finds that any left (right) action can always be rewritten as a right (left) action [@dixon2013division]. That is: $$\begin{aligned}
(\mathbb{C}\otimes\mathbb{O})_L\cong (\mathbb{C}\otimes\mathbb{O})_R\cong \mathbb{C}\ell(6).
\end{aligned}$$ This is in contrast to a similar construction for $\mathbb{C}\otimes\mathbb{H}$, where one finds that the left and right actions are genuinely distinct, each generating a copy of $\mathbb{C}\ell(2)$. The left and right adjoint actions in this case commute, and only by considering both does one obtain a basis for $Mat(4,\mathbb{C})\cong\mathbb{C}\ell(4)$.

[^1]: There are different multiplication rules for $\mathbb{O}$ used by different authors in the literature. Here we follow the multiplication table used in [@lohmus1994nonassociative]

[^2]: We will henceforth refer to this algebra simply as the left action algebra or left multiplication algebra
