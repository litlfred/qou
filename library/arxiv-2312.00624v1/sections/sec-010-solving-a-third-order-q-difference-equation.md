---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-010-solving-a-third-order-q-difference-equation
section_title: "Solving a third-order q-difference equation"
section_number: null
pages: 20-23
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 1.0
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: 3rd-order label="sec: 3rd-order"} We will show how the matrix formalism of Section [\[sec: 2nd-order\]](#sec: 2nd-order){reference-type="ref" reference="sec: 2nd-order"} can be applied to solve a third-order $q$-difference equation in closed form. In particular, let us return to the quantum $A$-polynomial equation satisfied by the resummed perturbative wave function $\chi^{(\alpha), \rm{WKB}}(u; \hbar)$ in Eq. [\[Aeq-matrix\]](#Aeq-matrix){reference-type="eqref" reference="Aeq-matrix"} and assume it is of order three. As before, after appropriately accounting for the correction due to the exponential prefactor containing the functions $s^{(\alpha)}_{0,1}(x)$ in Eq. [\[chi-matrix-2\]](#chi-matrix-2){reference-type="eqref" reference="chi-matrix-2"}, the $q$-difference equation takes the form

$$\label{Psi-eq3}
\Psi^{(\alpha), \rm{WKB}}(q X;q)+A(X)\Psi^{(\alpha), \rm{WKB}}(X;q)+B(X)\Psi^{(\alpha), \rm{WKB}}(q^{-1} X;q) +C(X)\Psi^{(\alpha), \rm{WKB}}(q^{-2} X;q)=0 \, ,$$

where $A(X), B(X), C(X)$ are functions of $X$ and $q$. We can now introduce the function $\upsilon^{(\alpha)}(X)$ as in Eq. [\[uU-def\]](#uU-def){reference-type="eqref" reference="uU-def"} and write Eq. [\[Psi-eq3\]](#Psi-eq3){reference-type="eqref" reference="Psi-eq3"} equivalently as

$$\label{VVab3}
\upsilon (X) \upsilon(q^{-1} X) \upsilon(q^{-2} X) + A(X) \upsilon(q^{-1} X)\upsilon(q^{-2} X) + B(X) \upsilon(q^{-2} X) + C(X) = 0 \, ,$$ where we have dropped the label $\alpha$ from the notation for simplicity. Let us further assume that $q$ is fixed as in Eq. [\[q-rat\]](#q-rat){reference-type="eqref" reference="q-rat"} and define the the sequence of functions $\{\upsilon_k(X) \}$, $k \in {\mathbb Z}_{\ge 0}$, of $X$ and $q$ by $$\upsilon_k = \upsilon (q^{-k} X) \, .$$ It follows from shifting $X$ into $q^{-k}X$ in Eq. [\[VVab3\]](#VVab3){reference-type="eqref" reference="VVab3"} that they satisfy the system of equations $$\label{vkvk13}
\upsilon_k \upsilon_{k+1} \upsilon_{k+2} + A(q^{-k} X) \upsilon_{k+1} \upsilon_{k+2} + B(q^{-k} X) \upsilon_{k+2} + C(q^{-k} X) = 0 \, , \quad 0 \le k \le Q-1 \, .$$ In order to solve the above system recursively, let us define the sequences $\{ a^{(k)}(X)\}$, $\{b^{(k)}(X)\}$, and $\{c^{(k)}(X)\}$, $k \in {\mathbb Z}_{\ge 0}$, via the relations $$\label{ABvprods3}
\begin{align}
&a^{(1)}(X) = A(X) \, , \\
&b^{(1)}(X) = B(X) \, , \\
&c^{(1)}(X) = C(X) \, , \\
&\upsilon_0 \upsilon_1 \cdots \upsilon_{k+1} + a^{(k)}(X) \upsilon_k \upsilon_{k+1} + b^{(k)}(X) \upsilon_{k+1} + c^{(k)}(X)=0 \, , \quad k>1 \, . \label{ABvprods3-last}
\end{align}$$ If we multiply Eq. [\[ABvprods3-last\]](#ABvprods3-last){reference-type="eqref" reference="ABvprods3-last"} by $\upsilon_{k+2}$ and apply Eq. [\[vkvk13\]](#vkvk13){reference-type="eqref" reference="vkvk13"}, we obtain a recursion relation which can be written in matrix form as

$$\begin{pmatrix}
        a^{(k+1)}(X) \\
        b^{(k+1)}(X) \\
        c^{(k+1)}(X)
    \end{pmatrix}
    =
    \begin{pmatrix}
        -A(q^{-k} X) & 1 & 0 \\
        -B(q^{-k} X)  & 0 & 1 \\
        -C(q^{-k} X) & 0 & 0
    \end{pmatrix}
    \begin{pmatrix}
        a^{(k)}(X) \\
        b^{(k)}(X) \\
        c^{(k)}(X)
    \end{pmatrix} \, ,$$

and it can be solved as $$\label{relQm13}
    \begin{pmatrix}
        a^{(Q)}(X) \\
        b^{(Q)}(X) \\
        c^{(Q)}(X)
    \end{pmatrix}
    =
    {\mathcal M}_Q(X)
    \begin{pmatrix}
        -1 \\
        0 \\
        0
    \end{pmatrix} \, .$$

Here, ${\mathcal M}_Q(X)$ is the matrix $$\label{matrix3}
{\cal M}_Q(X)    
    =
    \prod_{k=1}^{Q}
    \begin{pmatrix}
        -A(q^k X) &  1 & 0 \\
        -B(q^k X)  & 0 & 1 \\ 
        -C(q^k X) & 0 & 0
    \end{pmatrix}
    =
    \begin{pmatrix}
        {\cal M}_{11}(X) &  {\cal M}_{12}(X) & {\cal M}_{13}(X) \\
        {\cal M}_{21}(X)  & {\cal M}_{22}(X) & {\cal M}_{23}(X) \\ 
        {\cal M}_{31}(X) & {\cal M}_{32}(X) & {\cal M}_{33}(X)
    \end{pmatrix} \, ,$$

where the product is ordered from left to right as $k$ increases. As before, let us introduce

$$\Pi \upsilon  = \upsilon_0 \upsilon_1 \cdots \upsilon_{Q-1} \, ,$$ which is invariant under $q$-shifts. Moreover, as it will be useful in the following, we compute the $q$-shifted matrix $${\cal M}_Q(q^{-1} X) =
\begin{pmatrix}
  -A(X) & 1 & 0 \\
  -B(X) & 0 & 1 \\
  -C(X) & 0 & 0
\end{pmatrix}
{\cal M}_Q(X)
\begin{pmatrix}
  -A(X) & 1 & 0 \\
  -B(X) & 0 & 1 \\
  -C(X) & 0 & 0
\end{pmatrix}^{-1} \, ,$$ and we obtain in this way $$\label{dict}
  \begin{pmatrix}
  -A {\cal M}_{12} + {\cal M}_{22} & -A {\cal M}_{13} + {\cal M}_{23} & \frac{A}{C} ({\cal M}_{11}+ A {\cal M}_{12}+ B {\cal M}_{13}) - \frac{1}{C} ({\cal M}_{21}+ A {\cal M}_{22}+ B {\cal M}_{23}) \\
  -B {\cal M}_{12} + {\cal M}_{32} & -B {\cal M}_{13} + {\cal M}_{33} & \frac{B}{C} ({\cal M}_{11}+ A {\cal M}_{12}+ B {\cal M}_{13}) - \frac{1}{C} ({\cal M}_{21}+ A {\cal M}_{22}+ B {\cal M}_{23}) \\
  -C {\cal M}_{12} & -C {\cal M}_{13} & ({\cal M}_{11}+ A {\cal M}_{12}+ B {\cal M}_{13})
\end{pmatrix} \, ,$$ where we have removed the explicit dependence on $X$ for compactness. Let us now take Eq. [\[ABvprods3-last\]](#ABvprods3-last){reference-type="eqref" reference="ABvprods3-last"} for $k=Q$, which gives $$\label{start3}
\upsilon_0 \upsilon_1 (\Pi \upsilon+ a^{(Q)}(X)) + b^{(Q)}(X) \upsilon_1 + c^{(Q)}(X) = 0 \, .$$ Eq. [\[relQm13\]](#relQm13){reference-type="eqref" reference="relQm13"} allows us to express the functions $a^{(Q)}(X)$, $b^{(Q)}(X)$, and $c^{(Q)}(X)$ in terms of the entries of the matrix $\mathcal M_Q(X)$, so that Eq. [\[start3\]](#start3){reference-type="eqref" reference="start3"} becomes $$\label{case1}
\upsilon_0 \upsilon_1 (\Pi \upsilon- {\cal M}_{11}(X)) - {\cal M}_{21}(X) \upsilon_1 - {\cal M}_{31}(X) = 0 \, .$$ Shifting $X$ into $q^{-1}X$, using Eq. [\[vkvk13\]](#vkvk13){reference-type="eqref" reference="vkvk13"} with $k=0$, and applying the dictionary encoded in the matrix in Eq. [\[dict\]](#dict){reference-type="eqref" reference="dict"}, we find the second equation $$\label{case2}
\upsilon_1 (\Pi \upsilon- {\cal M}_{22}(X)) - {\cal M}_{32}(X) - {\cal M}_{12}(X) \upsilon_0 \upsilon_1 = 0 \, .$$ Subsequently shifting $X$ into $q^{-1}X$ in the equation above, again using Eqs. [\[vkvk13\]](#vkvk13){reference-type="eqref" reference="vkvk13"}, [\[dict\]](#dict){reference-type="eqref" reference="dict"}, we obtain the third equation $$\label{case3}
\Pi \upsilon- {\cal M}_{33}(X) - {\cal M}_{23}(X) \upsilon_1 - {\cal M}_{13}(X) \upsilon_0 \upsilon_1 = 0 \, .$$ Eqs. [\[case1\]](#case1){reference-type="eqref" reference="case1"}, [\[case2\]](#case2){reference-type="eqref" reference="case2"}, [\[case3\]](#case3){reference-type="eqref" reference="case3"} assemble into a cubic system which can be written in matrix form as $$\begin{pmatrix}
{\cal M}_{11}(X) - \Pi \upsilon& {\cal M}_{21}(X) & {\cal M}_{31}(X) \\
{\cal M}_{12}(X) & {\cal M}_{22}(X) - \Pi \upsilon& {\cal M}_{32}(X) \\
{\cal M}_{13}(X)  & {\cal M}_{23}(X) & {\cal M}_{33}(X) - \Pi \upsilon
\end{pmatrix}
\begin{pmatrix}
\upsilon_0 \upsilon_1 \\
\upsilon_1 \\
1
\end{pmatrix} = 
\begin{pmatrix}
0 \\
0 \\
0
\end{pmatrix} \, .$$ We conclude that $\Pi \upsilon$ is an eigenvalue of the transpose matrix ${\cal M}_Q(X)^{\rm T}$ with eigenvector $(\upsilon_0 \upsilon_1, \upsilon_1, 1)^{\rm T}$. The characteristic polynomial is $$p(z) = \det (z \mathbb{I}_3 - {\cal M}_Q^{\rm T}) = z^3 + d_2 z^2 + d_1 z + d_0 \, ,$$ where $\mathbb{I}_3$ is the 3x3 identity matrix and $$\begin{align}
d_2=& - {\cal M}_{11} - {\cal M}_{22} - {\cal M}_{33} \, , \\
d_1=& - {\cal M}_{23} {\cal M}_{32} - {\cal M}_{12} {\cal M}_{21} - {\cal M}_{13} {\cal M}_{31} + {\cal M}_{11} {\cal M}_{22} + {\cal M}_{11} {\cal M}_{33} + {\cal M}_{22} {\cal M}_{33} \, , \\
d_0=& - {\cal M}_{11} {\cal M}_{22} {\cal M}_{33} + {\cal M}_{11} {\cal M}_{23} {\cal M}_{32} + {\cal M}_{22} {\cal M}_{31} {\cal M}_{13} + {\cal M}_{33} {\cal M}_{21} {\cal M}_{12} \\
& - {\cal M}_{21} {\cal M}_{13} {\cal M}_{32} - {\cal M}_{31} {\cal M}_{12} {\cal M}_{23} \, . \nonumber
\end{align}$$ The eigenvalues of the matrix ${\cal M}_Q(X)^{\rm T}$ are the roots of $p(z)$, that is, $$\label{Pi3}
\Pi \upsilon= -\frac{1}{3} \left( d_2 + \Theta_2 + \frac{\Theta_0}{\Theta_2} \right) \, ,$$ where we have $$\begin{align}
\Theta_0 &= d_2^2 - 3 d_1 \, , \\
\Theta_1 &= 2 d_2^3 - 9 d_2 d_1 + 27 d_0 \, , \\
\Theta_2 &= { {\rm e}^{m {\pi {\rm i}\over 3}} \over 2} \sqrt[3]{\Theta_1+\sqrt{\Theta_1^4 - 4 \Theta_0^3}}\, ,  \quad m=0, 1, 2 \, . \label{theta2-m}
\end{align}$$ The function $\upsilon_0$ is obtained, for example, by solving the system of Eqs. [\[case2\]](#case2){reference-type="eqref" reference="case2"}, [\[case3\]](#case3){reference-type="eqref" reference="case3"}, yielding $$\label{u03}
\upsilon_0 =  \frac{{\cal M}_{22} {\cal M}_{33}-{\cal M}_{22} \Pi \upsilon-{\cal M}_{23} {\cal M}_{32}-{\cal M}_{33} \Pi \upsilon+ (\Pi \upsilon)^2}{-{\cal M}_{12} {\cal M}_{33}+{\cal M}_{12} \Pi \upsilon+{\cal M}_{13} {\cal M}_{32}} \, ,$$ while the functions $\upsilon_k$, $k \in {\mathbb Z}_{>0}$, are computed by successively $q$-shifting $\upsilon_0$. This gives the solution to Eq. [\[VVab3\]](#VVab3){reference-type="eqref" reference="VVab3"} for all rational values of $\hbar$. As we have done in Section [\[sec: 2nd-order\]](#sec: 2nd-order){reference-type="ref" reference="sec: 2nd-order"}, we can now fix the ambiguity in Eq. [\[Pi3\]](#Pi3){reference-type="eqref" reference="Pi3"} and correspondingly in Eq. [\[u03\]](#u03){reference-type="eqref" reference="u03"}, that is, the value of $m=0,1,2$ in the definition of $\Theta_2$, by imposing the consistency of the solution with the original choice of a non-abelian classical branch labeled by $\alpha$. Specifically, we require that Eq. [\[branch\]](#branch){reference-type="eqref" reference="branch"} holds in the case of $P=Q=1$ after accounting for the exponential prefactor in Eq. [\[chi-matrix-2\]](#chi-matrix-2){reference-type="eqref" reference="chi-matrix-2"}. Again, we conclude by observing that Eqs. [\[uU-def\]](#uU-def){reference-type="eqref" reference="uU-def"}, [\[varphi-Unew\]](#varphi-Unew){reference-type="eqref" reference="varphi-Unew"} yield $$\label{dict-end}
    \Upsilon (X) = \log \upsilon_0 \, , \quad \varphi_Q(X) = \frac{1}{Q} \log \Pi\upsilon \, .$$ Note that the procedure described here for a third-order $q$-difference equation can be generalized to higher orders.
