---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-009-solving-a-second-order-q-difference-equation
section_title: "Solving a second-order q-difference equation"
section_number: null
pages: 17-20
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.981
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: 2nd-order label="sec: 2nd-order"} Recall that, for each choice of $\alpha$, the resummed perturbative wave function $\chi^{(\alpha), \rm{WKB}}(u; \hbar)$ is given in Eq. [\[WKB-conj\]](#WKB-conj){reference-type="eqref" reference="WKB-conj"}. Equivalently, we write $$\label{chi-matrix-2}
\chi^{(\alpha), \rm{WKB}}(u; \hbar) = {\rm e}^{\frac{{\rm i}}{\hbar} s^{(\alpha)}_0(x) +  s^{(\alpha)}_1(x)} \Psi^{(\alpha), \rm{WKB}}(X;q) \, ,$$ where we have introduced the notation $$\label{Psi}
\Psi^{(\alpha), \rm{WKB}}(X;q) = \exp\left( \phi^{(\alpha), \rm{WKB}}(X;q)\right) \, ,$$ which will be useful in the following discussion. Let us assume that the corresponding quantum $A$-polynomial equation, that is, $$\label{Aeq-matrix}
\hat{A}(\hat{P}, \hat{X}, q) \chi^{(\alpha), \rm{WKB}}(u; \hbar) = 0 \, ,$$ is of second order. After appropriately accounting for the correction due to the exponential prefactor containing the functions $s^{(\alpha)}_{0,1}(x)$ in Eq. [\[chi-matrix-2\]](#chi-matrix-2){reference-type="eqref" reference="chi-matrix-2"}, the $q$-difference equation above becomes

$$\label{Psi-eq}
\Psi^{(\alpha), \rm{WKB}}(q X;q)+A(X)\Psi^{(\alpha), \rm{WKB}}(X;q)+B(X)\Psi^{(\alpha), \rm{WKB}}(q^{-1} X;q)=0 \, ,$$

where $A(X), B(X)$ are functions of $X$ and $q$. Let us observe that, due to the conjectural structure in Eqs. [\[phi-struc\]](#phi-struc){reference-type="eqref" reference="phi-struc"}, [\[ahatf-def\]](#ahatf-def){reference-type="eqref" reference="ahatf-def"}, we have

$$\label{uU-def}
 \upsilon^{(\alpha)} (X) = {\Psi^{(\alpha), \rm{WKB}} (q X;q) \over \Psi^{(\alpha), \rm{WKB}}(X;q)}=\exp\left( \Upsilon^{(\alpha)} (X) \right) \, ,$$

and we can now write Eq. [\[Psi-eq\]](#Psi-eq){reference-type="eqref" reference="Psi-eq"} in terms of the above function $\upsilon^{(\alpha)} (X)$ as $$\label{VVab}
\upsilon (X)\upsilon(q^{-1} X)+A(X) \upsilon(q^{-1} X)+B(X)=0 \, ,$$ where we have dropped the label $\alpha$ from the notation for simplicity.

Let us further assume that $\hbar$ is fixed as in Eq. [\[rathbar\]](#rathbar){reference-type="eqref" reference="rathbar"}, that is, $$\label{q-rat}
q={\rm e}^{{\rm i}\hbar}={\rm e}^{2 \pi {\rm i}{P \over Q}} \, , \quad  P,Q \in {\mathbb Z}_{>0} \; \; \text{coprime} \, ,$$ and introduce the sequence of functions $\{\upsilon_k \}$, $k \in {\mathbb Z}_{\ge 0}$, of $X$ and $q$ defined by

$$\upsilon_k = \upsilon (q^{-k} X)\, .$$

They satisfy the system of equations

$$\label{vkvk1}
\upsilon_k \upsilon_{k+1}+A(q^{-k} X) \upsilon_{k+1}+B(q^{-k} X)=0 \, , \quad 0 \le k \le Q-1 \, ,$$

as a consequence of Eq. [\[VVab\]](#VVab){reference-type="eqref" reference="VVab"}. We solve this system recursively, as follows. We define the sequences $\{ a^{(k)}(X) \}$ and $\{ b^{(k)}(X) \}$, $k \in {\mathbb Z}_{\ge 0}$, via the relations $$\label{ABvprods}
\begin{align}
     &a^{(1)}(X) =A(X),\\
     & b^{(1)}(X) =B(X), \\
     &\upsilon_0 \upsilon_1 \cdots \upsilon_{k}+a^{(k)}(X) \upsilon_{k}+b^{(k)}(X) =0 \, , \quad k > 1 \, . \label{ABvprods-last}
\end{align}$$

If we multiply Eq. [\[ABvprods-last\]](#ABvprods-last){reference-type="eqref" reference="ABvprods-last"} by $\upsilon_{k+1}$ and apply Eq. [\[vkvk1\]](#vkvk1){reference-type="eqref" reference="vkvk1"}, we obtain a recursion relation which can be written in matrix form as

$$\begin{pmatrix}
        a^{(k+1)}(X) \\
        b^{(k+1)}(X)
    \end{pmatrix}
    =
    \begin{pmatrix}
        -A(q^{-k} X) &  1 \\
        -B(q^{-k} X)  & 0 
    \end{pmatrix}
    \begin{pmatrix}
        a^{(k)}(X) \\
        b^{(k)}(X)
    \end{pmatrix} \, ,$$

and it can be solved as $$\label{relQm1}
    \begin{pmatrix}
        a^{(Q)}(X) \\
        b^{(Q)}(X)
    \end{pmatrix}
    =
    {\mathcal M}_Q(X)
    \begin{pmatrix}
        -1 \\
        0
    \end{pmatrix} \, .$$

Here, ${\mathcal M}_Q(X)$ is the matrix $$\label{matrix2}
{\cal M}_Q(X)    
    =
    \prod_{k=1}^{Q}
    \begin{pmatrix}
        -A(q^k X) &  1 \\
        -B(q^k X)  & 0 
    \end{pmatrix} =
    \begin{pmatrix}
        {\cal M}_{11}(X) &  {\cal M}_{12}(X) \\
        {\cal M}_{21}(X)  & {\cal M}_{22}(X) 
    \end{pmatrix} \, ,$$

where the product is ordered from left to right as $k$ increases. Recalling that $q^Q=1$, we obtain

$$\label{MqM}
\begin{aligned}
    {\mathcal M}_Q(q^{-1} X) &= 
    \begin{pmatrix}
        -A(X) &  1 \\
        -B(X)  & 0 
    \end{pmatrix}
    {\mathcal M}_Q(X)
    \begin{pmatrix}
        -A( X) &  1 \\
        -B(X)  & 0 
    \end{pmatrix}^{-1} \\
    &= 
    \begin{pmatrix}
        {\cal M}_{22} -A {\cal M}_{12} & \frac{A}{B} \left({\cal M}_{11}+A {\cal M}_{12} \right) - \frac{1}{B} \left( {\cal M}_{21}+A {\cal M}_{22} \right) \\
        -B {\cal M}_{12}  & {\cal M}_{11}+A {\cal M}_{12}
    \end{pmatrix} \, , 
\end{aligned}$$

where we have removed the explicit dependence on $X$ for compactness. Following Eqs. [\[relQm1\]](#relQm1){reference-type="eqref" reference="relQm1"}, [\[MqM\]](#MqM){reference-type="eqref" reference="MqM"}, we find that[^1]

$$\label{abM2}
    \begin{pmatrix}
        a^{(Q)}(q^{-1}X) \\
        b^{(Q)}(q^{-1}X)
    \end{pmatrix}
    =\begin{pmatrix}
        {-\mathcal M}_{22}(X)+A(X){\mathcal M}_{12}(X) \\
        B(X){\mathcal M}_{12}(X)
    \end{pmatrix} \, .$$

Let us now define the function

$$\Pi \upsilon  = \upsilon_0 \upsilon_1 \cdots \upsilon_{Q-1} \, ,$$ which is invariant under $q$-shifts. We consider Eq. [\[ABvprods-last\]](#ABvprods-last){reference-type="eqref" reference="ABvprods-last"} for $k=Q$ and, shifting $X$ into $q^{-1}X$, we produce the system $$\begin{cases}
    \upsilon_0(\Pi \upsilon+ a^{(Q)}(X))+b^{(Q)}(X)=0 \, , \\
    \upsilon_1(\Pi \upsilon+a^{(Q)}(q^{-1}X))+b^{(Q)}(q^{-1}X)=0 \, .
    \end{cases}$$

By substituting the expressions for $a^{(Q)}(X), a^{(Q)}(q^{-1}X)$ and $b^{(Q)}(X), b^{(Q)}(q^{-1}X)$ in terms of the entries of the original matrix $\mathcal M_Q(X)$ in Eqs. [\[relQm1\]](#relQm1){reference-type="eqref" reference="relQm1"}, [\[abM2\]](#abM2){reference-type="eqref" reference="abM2"} and then using Eq. [\[vkvk1\]](#vkvk1){reference-type="eqref" reference="vkvk1"} with $k=0$, we can rewrite the system above as

$$\label{v0system}
    \begin{cases}
    \upsilon_0(\Pi \upsilon- {\mathcal M}_{11}(X))- {\mathcal M}_{21}(X)=0 \, , \\
    \Pi \upsilon - {\mathcal M}_{22}(X)-\upsilon_0  {\mathcal M}_{12}(X)=0\, , 
    \end{cases}$$

or, equivalently, in the matrix form

$$\begin{pmatrix}
        {\mathcal M}_{11}(X)-\Pi \upsilon & {\mathcal M}_{21}(X) \\
        {\mathcal M}_{12}(X) & {\mathcal M}_{22}(X)-\Pi \upsilon
    \end{pmatrix}
    \begin{pmatrix}
        \upsilon_0 \\
        1
    \end{pmatrix}
    =
    \begin{pmatrix}
        0 \\
        0
    \end{pmatrix} \, .$$

It follows straightforwardly that $\Pi \upsilon$ is an eigenvalue of the transpose matrix $\mathcal M_Q(X)^{\rm T}$ with eigenvector $(\upsilon_0, 1)^{\rm T}$. Specifically, we have that

$$\label{Piu-2}
\Pi \upsilon =  \frac{ {\rm tr}{\mathcal M_Q}(X) \pm \sqrt{\Delta_Q(X)} }{2} \, ,$$

where we have introduced $$\Delta_Q(X) =  ({\rm tr}{\mathcal M_Q}(X))^2 - 4 \,\, {\rm det}{\mathcal M_Q}(X) \, ,$$ while ${\rm det}{\mathcal M_Q}(X)$ and ${\rm tr}{\mathcal M_Q}(X)$ denote the trace and determinant of the matrix, respectively. Note that, following Eq. [\[matrix2\]](#matrix2){reference-type="eqref" reference="matrix2"}, both ${\rm det}{\mathcal M_Q}(X)$ and ${\rm tr}{\mathcal M_Q}(X)$ are invariant under $q$-shifts and so depend on $X$ through $X^Q$. The function $\upsilon_0$ can be found, for example, using the second line of Eq. [\[v0system\]](#v0system){reference-type="eqref" reference="v0system"}, yielding

$$\label{uo-2}
\upsilon_0 = \frac{ \Pi v - {\mathcal M}_{22}(X) }{{\mathcal M}_{12}(X)} =  \frac{ {\mathcal M}_{11}(X) - {\mathcal M}_{22}(X) \pm \sqrt{\Delta_Q(X)} }{2 {\mathcal M}_{12}(X)} \, ,$$

while the functions $\upsilon_k$, $k \in {\mathbb Z}_{>0}$, are obtained by successively $q$-shifting $\upsilon_0$. This gives the solution to Eq. [\[VVab\]](#VVab){reference-type="eqref" reference="VVab"} for all rational values of $\hbar$. However, we stress that, for such a solution to be consistent with the original choice of a classical branch labeled by $\alpha$, we must impose that, taking $P=Q=1$, we find $$\label{branch}
\upsilon_0= \Pi \upsilon= P^{(\alpha)} \, ,$$ where $P^{(\alpha)}$ is the selected non-abelian solution of the classical $A$-polynomial at fixed $X$ after taking into account the corrections due to the exponential prefactor in Eq. [\[chi-matrix-2\]](#chi-matrix-2){reference-type="eqref" reference="chi-matrix-2"}. In this way, we remove the sign ambiguity in Eq. [\[Piu-2\]](#Piu-2){reference-type="eqref" reference="Piu-2"} and correspondingly in Eq. [\[uo-2\]](#uo-2){reference-type="eqref" reference="uo-2"}. We conclude by observing that Eq. [\[uU-def\]](#uU-def){reference-type="eqref" reference="uU-def"} implies $$\label{2nd-end}
\begin{align}
    \Upsilon (X) &= \log \upsilon_0 = \log \left ( \frac{ {\mathcal M}_{11}(X)- {\mathcal M}_{22}(X) \pm \sqrt{\Delta_Q(X)} }{2 {\mathcal M}_{12}(X)} \right ) \, , \\
    \varphi_Q(X) &= \frac{1}{Q} \log \Pi\upsilon = \frac{1}{Q} \log \left ( \frac{ {\rm tr}{\mathcal M}_Q(X) \pm \sqrt{\Delta_Q(X)} }{2} \right ) \, ,
\end{align}$$ where we have applied the relation $$\label{varphi-Unew}
\Pi \upsilon= \exp \left( \sum_{m=0}^{Q-1} \Upsilon(q^m X) \right) = \exp \left(Q \varphi_Q (X) \right) \, ,$$ which is a direct consequence of Eq. [\[varphiQ-U\]](#varphiQ-U){reference-type="eqref" reference="varphiQ-U"}. Again, the sign ambiguity in Eq. [\[2nd-end\]](#2nd-end){reference-type="eqref" reference="2nd-end"} is resolved by the requirement in Eq. [\[branch\]](#branch){reference-type="eqref" reference="branch"}.

[^1]: There is a sign misprint in the corresponding equation in [@szabolcs].
