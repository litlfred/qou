---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-009-34-complex-structures
section_title: "Complex structures"
section_number: 3.4
pages: 12-14
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
text_source: latex
latex_prose_ratio: 0.759
latex_coverage_ratio: 1.0
---
We now enter into a less familiar part of the discussion. It is clear that any of the 3 Clifford generators $\tilde{E}^{5,6,7}$ (or any unit vector constructed as their linear combination) can serve as a complex structure on $\tilde{{\mathbb O}}$. This complex structure identifies $\tilde{{\mathbb O}}={\mathbb C}^4$. What commutes with it in ${\mathfrak so}(4,3)$ is the subalgebra ${\mathfrak so}(4,2)$. But this is not the complex structure that is of interest to us in relation to physics.

Any of the generators $\tilde{E}^{1,2,3,4}$ squares to plus the identity, and so is not a complex structure. But we also have the object $$\begin{aligned}
\tau = \tilde{E}^5 \tilde{E}^6 \tilde{E}^7.
\end{aligned}$$ This is an operator that reverses the signs of the positive-definite directions $\tilde{{\mathbb I}}, \tilde{e}^{5,6,7}$ of the split quadratic form ([\[Q-split\]](#Q-split){reference-type="ref" reference="Q-split"}), and leaves the negative-definite directions $\tilde{e}^{1,2,3,4}$ intact. As a matrix, this is the already encountered matrix of the quadratic form ([\[norm-split\]](#norm-split){reference-type="ref" reference="norm-split"}). This operator squares to plus the identity $\tau^2={\mathbb I}$, but **anti-commutes** with any of the Clifford generators $\tilde{E}^{1,2,3,4}$ (and commutes with all the $\tilde{E}^{5,6,7}$ generators). Thus, the product of $\tau$ with any one of $\tilde{E}^{1,2,3,4}$ (or with a unit linear combination constructed from them) is a complex structure. We choose $\tilde{u}=\tilde{e}^4$ and define $$\begin{aligned}
\tilde{J} := \tilde{E}^4 \tau.
\end{aligned}$$ Note the strong analogy with ([\[J-right\]](#J-right){reference-type="ref" reference="J-right"}). This is the complex structure that is of our main interest. Indeed, being given by the product of 4 Clifford generators, its commutant in ${\mathfrak so}(4,3)$ is the algebra ${\mathfrak so}(3)\times{\mathfrak so}(1,3)$. Both groups are very interesting, because the first factor reminds us of the ${\rm SU}(2)$ acting on isospin of particles, while the second factor is the Lorentz group. The first factor is the one describing rotations in the $\tilde{e}^{1,2,3}$ plane, while the second one mixes the directions $\tilde{e}^{4,5,6,7}$. The direction $\tilde{e}^4$ is a timelike direction with respect to the split octonion quadratic form ([\[Q-split\]](#Q-split){reference-type="ref" reference="Q-split"}), and we will refer to it as such in what follows. For later purposes we note that we can rewrite the complex structure $\tilde{J}$ as $$\begin{aligned}
\label{J-split-123}
\tilde{J} := -\tilde{E}^1 \tilde{E}^2\tilde{E}^3,
\end{aligned}$$ i.e., as the product of the timelike Clifford generators that are distinct from the chosen $\tilde{E}^4$.

## Decomposition of $\tilde{{\mathbb O}}$ under ${\mathfrak so}(3)\times{\mathfrak so}(1,3)$

The split octonions $\tilde{{\mathbb O}}$ form the spinor representation of ${\rm Spin}(4,3)$. When we restrict to ${\rm Spin}(3)\times{\rm Spin}(1,3)$, we expect the spinor to transform as spinor with respect to both of the factors. It is nevertheless very interesting to see how this happens explicitly.

The $(1,0)$ coordinates on $\tilde{{\mathbb O}}$ for the complex structure $\tilde{J}$ are given by $$\begin{aligned}
w_0:= \frac{1}{2}(y_0 + {\rm i\,}y_4), \quad w_i:= \frac{1}{2}(y_i +{\rm i\,}y_{i+4}), 
\end{aligned}$$ where the index $i=1,2,3$ and we introduced the factors of $1/2$ for future convenience. The transformations from ${\mathfrak so}(3)\times{\mathfrak so}(1,3)$ commute with $\tilde{J}$ and thus preserve the $(1,0)$ subspace. Therefore, they can be described as $4\times 4$ complex matrices acting on the 4-columns $(w_0, w_1, w_2, w_3)$. Explicitly, we have $$\begin{aligned}
X_{{\mathfrak so}(3)} = \left( \begin{array}{cccc} 0 & {\rm i\,}x & {\rm i\,}y & {\rm i\,}z \\
{\rm i\,}x & 0 &  z&  -y  \\
{\rm i\,}y &  - z & 0 & x \\
{\rm i\,}z & y & - x & 0 \end{array}\right), 
\end{aligned}$$ where $$\begin{aligned}
x= \tilde{\omega}_{23}, \quad y =  -\tilde{\omega}_{13}, \quad z= \tilde{\omega}_{12}
\end{aligned}$$ are 3 real parameters. We also have $$\begin{aligned}
X_{{\mathfrak so}(1,3)} = \left( \begin{array}{cccc} 0 & a & b& c \\
a& 0 &  {\rm i\,}c &  -{\rm i\,}b  \\
b &  - {\rm i\,}c & 0 & {\rm i\,}a \\
c& {\rm i\,}b & - {\rm i\,}a & 0 \end{array}\right),
\end{aligned}$$ where $$\begin{aligned}
a= -\tilde{\omega}_{45} + {\rm i\,}\tilde{\omega}_{67}, \quad b= -\tilde{\omega}_{46} - {\rm i\,}\tilde{\omega}_{57}, \quad c=-\tilde{\omega}_{47} + {\rm i\,}\tilde{\omega}_{56}
\end{aligned}$$ are complex parameters. It can be verified that the matrices $X_{{\mathfrak so}(3)}$ and $X_{{\mathfrak so}(1,3)}$ commute.

It is then easy to check that the 2-component columns $$\begin{aligned}
\label{ud}
u = \left(\begin{array}{c} u_1 \\ u_2 \end{array}\right):= \left( \begin{array}{c} w_0 + w_3 \\ w_1-{\rm i\,}w_2 \end{array}\right), \qquad
d= \left(\begin{array}{c} d_1 \\ d_2 \end{array}\right):= \left( \begin{array}{c} w_1+{\rm i\,}w_2 \\ w_0 - w_3 \end{array}\right)
\end{aligned}$$ transform under $X_{{\mathfrak so}(1,3)}$ transformations as 2-component spinors of the same Lorentz chirality, that is $$\begin{aligned}
u\to A u, \qquad d\to Ad, \qquad 
A=\left( \begin{array}{cc} c & a+{\rm i\,}b \\ a-{\rm i\,}b & -c \end{array}\right).
\end{aligned}$$ On the other hand, the 2-component column with $u, d$ as entries transforms under $X_{{\mathfrak so}(3)}$ as $$\begin{aligned}
\left(\begin{array}{c} u \\ d \end{array}\right) \to \left(\begin{array}{cc} {\rm i\,}z & y +{\rm i\,}x \\ - y+{\rm i\,}x & -{\rm i\,}z\end{array}\right) \left(\begin{array}{c} u \\ d \end{array}\right).
\end{aligned}$$ Summarising, by introducing the complex structure $\tilde{J}$, the space of split octonions $\tilde{{\mathbb O}}={\mathbb R}^8$ splits into its $(1,0)$ and $(0,1)$ eigenspaces. The $(1,0)$ eigenspace ${\mathbb C}^4$ transforms as the spinor representation of ${\rm Spin}(3)$, as well as the 2-component spinor representation of the Lorentz group ${\rm Spin}(1,3)$ $$\begin{aligned}
{\mathbb C}^4_{(1,0)} = ( {\bf 2}, {\bf 2}, {\bf 1}).
\end{aligned}$$ The complex conjugate $(0,1)$ eingespace transforms as the spinor of ${\rm Spin}(3)$, as well as the complex conjugate 2-component spinor representation of Lorentz $$\begin{aligned}
{\mathbb C}^4_{(0,1)} = ( {\bf 2}, {\bf 1}, {\bf 2}).
\end{aligned}$$ Thus, a single copy of $\tilde{{\mathbb O}}$ gives us a 2-component Lorentz spinor that is at the same time a spinor of what can be identified as \"weak\" ${\rm SU}(2)$.[^1] Thus, the \"weak\" ${\rm SU}(2)$ and the Lorentz group are very naturally unified within ${\rm Spin}(4,3)$.

## Parametrisation

It will help if we develop the notation a bit further. We have seen that a ${\rm Spin}(4,3)$ spinor $y\in\tilde{{\mathbb O}}$ splits into its $(1,0), (0,1)$ components $$\begin{aligned}
y = \tilde{P}_+ y + \tilde{P}_- y := y^+ + y^-,
\end{aligned}$$ where $$\begin{aligned}
\tilde{P}_\pm = \frac{1}{2} ( {\mathbb I}\pm {\rm i\,}\tilde{J})
\end{aligned}$$ are the projectors. The split octonion $y^+$ transforms as a 2-component Lorentz and ${\rm SU}(2)$ spinors, and $y^-$ transforms as a 2-component Lorentz spinor of the opposite chirality, and again as a ${\rm SU}(2)$ spinor. Note that the two complex octonions $y^\pm$ are related by the complex conjugation $y^-= (y^+)^*$.

It will be helpful to write down the explicit parametrisation of the octonions $y_\pm$ by the components of the Lorentz and ${\rm SU}(2)$ spinors. Using ([\[ud\]](#ud){reference-type="ref" reference="ud"}) we have $$\begin{aligned}
w_0 = \frac{1}{2}( u_1+d_2), \quad w_3=\frac{1}{2}( u_1-d_2), \quad
w_1=\frac{1}{2}( u_2+d_1), \quad w_2=\frac{{\rm i\,}}{2}( u_2-d_1).
\end{aligned}$$ We also have for the real coordinates on $\tilde{{\mathbb O}}$ $$\begin{aligned}
y_0 =  (w_0 + w_0^*), \quad y_4=-{\rm i\,}(w_0-w_0^*), \quad
y_i = ( w_i + w_i^*), \quad y_{i+4} = -{\rm i\,}( w_i - w_i^*),
\end{aligned}$$ with $i=1,2,3$, and where the star denotes the complex conjugation. This means that we have $$\begin{aligned}
y^+ = \frac{1}{2} \left( \begin{array}{c} u_1+d_2 \\ u_2 + d_1 \\ {\rm i\,}(u_2-d_1) \\ u_1-d_2 \\ 
-{\rm i\,}(u_1+d_2) \\ -{\rm i\,}(u_2+d_1) \\ (u_2-d_1) \\ -{\rm i\,}(u_1-d_2) \end{array}\right).
\end{aligned}$$

If we introduce an octonion $y$ parametrised in this way, a computation gives the expected Lorentz and ${\rm SU}(2)$ invariant pairing $$\begin{aligned}
\langle y, y \rangle =  \langle y^+, y^+ \rangle +  \langle y^-, y^- \rangle= \left( \begin{array}{cc} u & d \end{array}\right) 
\left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right)  \left( \begin{array}{c} u \\ d \end{array}\right) + {\rm c.c.},
\end{aligned}$$ where c.c. stands for \"complex conjugate\", and we have used the index-free 2-component spinor notation for the pairing of 2-component spinors $$\begin{aligned}
ud = -du :=u^T \epsilon d, \qquad u= \left( \begin{array}{c} u_1 \\ u_2 \end{array}\right) , d=\left( \begin{array}{c} d_1 \\ d_2 \end{array}\right), \quad  \epsilon:= \left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right).
\end{aligned}$$ From now on, we will never spell out the Lorentz pairing of 2-component spinors in terms of matrices, always using the index-free (and matrix-free) notation. But in order to avoid confusion, it will be useful to explicitly write the ${\rm SU}(2)$ invariant pairing in matrix terms. Also, from now on \"complex conjugate\" will always refer to the operation that maps between the $(1,0), (0,1)$ eigenspaces of the complex structure $\tilde{J}$. When we consider ${\rm Spin}(11,3)$, there will be another complex structure floating around, but in order to avoid confusion we will always spell out the complex conjugate with respect to this other complex structure explicitly.

We can also write a more general formula for the pairing of two different ${\rm Spin}(4,3)$ spinors. We have $$\begin{aligned}
\label{y12}
\langle y_1, y_2\rangle = \langle y_1^+, y_2^+ \rangle + \langle y_1^-, y_2^- \rangle =
\left( \begin{array}{cc} u & d \end{array}\right)_1 
\left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right)  \left( \begin{array}{c} u \\ d \end{array}\right)_2 + {\rm c.c.}
\end{aligned}$$ The first term is a Lorentz and ${\rm SU}(2)$ invariant pairing of two different 2-component Lorentz and ${\rm SU}(2)$ spinors.

[^1]: Below we will see that this ${\rm SU}(2)$ corresponds to the diagonal subgroup in ${\rm SU}(2)_L\times{\rm SU}(2)_R$.
