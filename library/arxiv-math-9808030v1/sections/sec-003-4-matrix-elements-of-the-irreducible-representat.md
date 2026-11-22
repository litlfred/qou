---
doc_id: arxiv-math-9808030v1
doc_title: "Planscherel Measure on Eq(2)"
section_id: sec-003-4-matrix-elements-of-the-irreducible-representat
section_title: "Matrix Elements of the Irreducible Representations of $E_q(2)$ from $SU_q(2)$ by Contraction"
section_number: 4
pages: 8-10
source_pdf: 9808030v1.pdf
source_sha256: 7889d6481b876b12
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 1.0
doc_brief: "Planscherel Measure on Eq(2) — Following the construction of the invariant integral and the scalar product for the quantum Euclidean group Eq(2), we obtained the full matrix elements of its unitary"
---
Unitary representations of $E_q(2)$ are previously studied [@5]. We now show that the matrix elements of the unitary irreducible representations of $E_q(2)$ can be obtained from the ones of $SU_q(2)$ by contraction. This example shows that there exists q--analog of contraction procedure of classical groups representations which was investigated in [@6].

In Appendix C we review the derivation of the matrix elements of the unitary irreducible representations of $E(2)$ from $SU(2)$ by the following contraction procedure $$t_{ij}^p (\phi , \rho , \zeta )= \lim _{l\rightarrow \infty }t_{ij}^l(\phi
,p\rho /l,\zeta-\phi ),$$ where one puts $\theta =p\rho /l$ in the decomposition (C.5) of $SU(2)$. The quantum analog of the above procedure is $$\label{eq: c4}t_{ij}^p=\lim _{l\rightarrow \infty } t_{ij}^l(x_0, y_0, \frac{
pv_0}{[l]}, \frac{pu_0}{[l]}),$$ where $[m]=\frac{q^m-q^{-m}}{q-q^{-1}}$ and $t^l_{ij}(x,y,v,u)$ are the matrix elements of the unitary irreducible representation of $SU_q(2)$ (see [@vil] and references therein ) : $$t^l_{ij} =\lambda^l_{ij}x^{-i-j}v^{i-j}  _2\phi_1(q^{-2(l+j)},q^{2(j+l+1)};
q^{2(l+i-j)}\mid q^2, - q^2uv),$$ with $i+j\leq 0$, $j\leq i$ and $$\lambda^l_{ij} =q^{(l+i)(l-j)} \sqrt{\left[ 
\begin{array}{c}
l+j \\ 
j-i 
\end{array}
\right ]_{q^2} \left[ 
\begin{array}{c}
l-j \\ 
j -i 
\end{array}
\right ]_{q^2}}.$$ Here $_2\phi_1$ and $[\cdot]_q$ are the q--hypergeometric function and the q--binomial coefficients respectively. We first calculate $$\lim _{l\rightarrow \infty } \lambda_{i,j}^lx_0^{-i-j} (\frac{(pv)}{[l]}
))^{i-j} = \frac{q^{\frac{m^2-n^2}{2}+ \frac{j-i}{2}}}{[i-j]!}
p^{i-j}x_0^{-i-j}v_0^{i-j}$$ and $$\begin{aligned}
\lim_{l\rightarrow\infty }
(\phi_{21}(q^{-2(l+j)},q^{2(l+1+j)};q^{2(1+i-j)}\mid q^2,
q^2 \frac{ (p^2v_0v_0^*) }{[l]})  ) = 
\nonumber \\
=[i-j]! \sum_{k=0}^\infty\frac{(-1)^k}{[k]![k+i-j]!}
(q^{-i-j}p^2zz^* )^k.
\end{aligned}$$ We then combine them to arrive at $$\label{irep12}t^p_{ij}(g)=(iq^{-1/2})^{i-j}\delta ^{-j/2}(pz^*)^{i-j}{\cal J}
_{i-j}(p^2zz^*)\delta ^{-j/2}, \ \ \ i\geq j.$$ For $i\leq j$ on the other hand one obtains $$\label{irep13}t^p_{ij}(g)=(-iq^{1/2})^{i-j}\delta ^{-j/2}{\cal J}
_{j-i}(p^2zz^*)(pz)^{j-i}\delta ^{-j/2}.$$ In the above formulae ${\cal J}_j$ are the q--Bessel functions given by $${\cal J}_j(x)=\sum_{k=0}^\infty \frac{(-1)^k} {[k]![k+j]!} (q^{-j}x)^k.$$

Before closing this section for the sake of completeness we like to present the already known formulae for the right and left representations of the quantum algebra $U_q(e(2))$ obtained from the representation of $U_q(su(2))$ by contraction [@dob] $$\label{eq: c6}{\cal R}(E_{\pm })t_{ij}^p=pt_{i\pm 1,j}^p,\ \ \ {\cal R}
(k)t_{ij}^p=q^{-i}t_{ij}^p$$ and $$\label{eq: c8}{\cal L}(E_{\pm })t_{ij}^p=pt_{i,j\mp 1}^p,\ \ \ {\cal L}
(k)t_{ij}^p=q^{-j}t_{ij}^p.$$
