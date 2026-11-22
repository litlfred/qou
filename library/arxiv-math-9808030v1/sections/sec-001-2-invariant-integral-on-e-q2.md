---
doc_id: arxiv-math-9808030v1
doc_title: "Planscherel Measure on Eq(2)"
section_id: sec-001-2-invariant-integral-on-e-q2
section_title: "Invariant Integral on $E_q(2)$"
section_number: 2
pages: 3-6
source_pdf: 9808030v1.pdf
source_sha256: 7889d6481b876b12
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "Planscherel Measure on Eq(2) — Following the construction of the invariant integral and the scalar product for the quantum Euclidean group Eq(2), we obtained the full matrix elements of its unitary"
---
Let us start by reviewing the construction of the invariant integral for $SU_q(2)$ which will guide in $E_q(2)$ case.

::: flushleft
**Rewiev of the invariant integral on $SU_q(2)$**
:::

The coordinate functions $x$, $u$, $x^*$, $u^*$ generating the $*$--Hopf algebra $A(SU_q(2))$ satisfy the following relations [@2] $$\begin{aligned}
\label{com}
u(x)=qx u, \ \  x^*u=qux^*,  \ \  uu^*=u^*u, \nonumber \\  
xx^* + uu^*={\bf 1}, \ \ x^*x+ q^2uu^*={\bf 1}. \ \ \ 
\end{aligned}$$ In $q\rightarrow 1$ limit the above relations define the three dimensional sphere $S^3$ which is the topological manifold of $SU(2)$. In $q\neq 1$ case we consider irreducible $*$--representation $\pi$ of the associative algebra $A(SU_q(2))$ in the Hilbert space ${\cal L}^2(Z)$ with the orthonormal basis $\{\mid n\rangle \}_{n\in Z}$ [@3] $$\begin{aligned}
\label{rep} 
\pi (x)\mid n\rangle=(1-q^{2n})^{1/2}\mid n-1\rangle, \ \ \ \ \ \
\pi (u)\mid n\rangle=q^n\mid n\rangle, \nonumber \\
\pi (u^*)\mid n\rangle=q^{n}\mid n\rangle, \ \ \ \ \ \
\pi (x^*)\mid n\rangle=(1-q^{2n+2})^{1/2}\mid n+1\rangle
\end{aligned}$$ for $0<q<1$. We associate a vector $v\in {\cal L}^2(Z)$ to each point of the "topological space\" $SU_q(2)$. Then $$f_v=\langle v\mid \pi(f) \mid v \rangle$$ gives the value of any function $f\in A(SU_q(2))$ at this point. Thus by topological space of the quantum group $SU_q(2)$ we mean the carrier space ${\cal L}^2(Z)$ of the $*$--representation of $A(SU_q(2))$. By the subspace $X_q$ of $SU_q(2)$ we mean the subspace $H^\prime$ of the Hilbert space ${\cal L}^2(Z)$. The empty set in $SU_q(2)$ is the empty set in ${\cal L}^2(Z)$. Two subspaces $X_q$ and $X_q^\prime$ of $SU_q(2)$ are said to have zero intersection ($X_q\bigcap X^\prime_q =\emptyset$ ) if the corresponding subspaces $H$ and $H^\prime$ of the Hilbert space ${\cal L}^2(Z)$ has zero intersection. The union and intersection of subspaces $X_q$, $X_q^\prime\subset SU_q(2)$ are understood as the union and intersection of corresponding subspaces $H$, $H^\prime\subset {\cal L}^2(Z)$.

Consider the linear map $\mu : SU_q(2)\rightarrow [0, \infty )$ defined by $$\label{lin}\mu (X_q)=(1-q^2) \sum_{n\in J} \langle n\mid \pi (\mu_S )\mid n
\rangle,$$ where $J\subset Z$, such that the vectors $\mid n \rangle$, $n\in J$ span the subspace $H$ of ${\cal L}^2(Z)$ corresponding to the subspace $X_q$ of $SU_q(2)$, $\mu_S\in A(SU_q(2))$. Since the left hand side of the above expression is positive definite the operator $\pi(\mu_S)$ must be self--adjoint and positive definite in ${\cal L}^2(Z_0)$. To make the linear map ([\[lin\]](#lin){reference-type="ref" reference="lin"}) a measure on $SU_q(2)$ we have to impose the additivity condition $$\mu (\bigcup_j X_{qj}) =\sum_j \mu (X_{qj} )$$ for the disjoint subspaces $X_{qj}$ of $SU_q(2)$. Inspecting ([\[rep\]](#rep){reference-type="ref" reference="rep"}) and ([\[lin\]](#lin){reference-type="ref" reference="lin"}) we conclude that $\mu_S$ is a polynomial of $\xi =uu^*$. The measure on $SU_q(2)$ is then given by $$\mu (X_q) =(1-q^2) \sum_{n\in J} \langle n\mid \pi (\mu_S(\xi ))\mid n
\rangle = (1-q^2) \sum_{n\in J} \mu_S(q^{2n}).$$

By means of the measure $\mu$ on the quantum group $SU_q(2)$ we introduce the linear functional $\psi : A(SU_q(2))\rightarrow C$ as $$\label{linf}\psi (f) =(1-q^2) \sum_{n=0}^\infty \langle n\mid \pi
(f\mu_S)\mid n\rangle.$$ If $f$ is the function of $\xi$ only we can rewrite ([\[linf\]](#linf){reference-type="ref" reference="linf"}) as $$\label{linf1}\psi (f) = \int_{0}^1 f(\xi ) d_{q^2}\mu_S(\xi ).$$ On the other hand the invariant integral on $SU_q(2)$ is [@3] $$\psi (f) = \int_{0}^1 f(\xi ) d_{q^2}\xi .$$ Comparing to ([\[linf1\]](#linf1){reference-type="ref" reference="linf1"}) we see that if $$\label{eq: mej8}\mu_S(\xi )=\xi ,$$ the linear functional ([\[linf\]](#linf){reference-type="ref" reference="linf"}) defines the invariant integral on $SU_q(2)$. Hence, the invariant measure and invariant integral on the quantum group $SU_q(2)$ are given by $$\label{invm}\mu (X_q) = (1-q^2) \sum_{n\in J} q^{2n}$$ and $$\label{invin}\psi (f) =(1-q^2) \sum_{n=0}^\infty \langle n\mid \pi(f\xi
)\mid n\rangle$$ respectively. Here $J\subset Z$, such that the vectors $\mid n \rangle$, $n\in J$ span the subspace $H$ of ${\cal L}^2(Z)$ corresponding to the subspace $X_q$ of $SU_q(2)$.

::: flushleft
**Invariant integral on $E_q(2)$**
:::

In fashion parallel to $SU_q(2)$ we can define the invariant measure on $E_q(2)$. The irreducible $*$--representation $\pi$ of the algebra of polynomials on $E_q(2)$ is constructed in the Hilbert space ${\cal L}^2(S)$ of square integrable functions on the circle $S$. In the orthonormal basis $\mid j\rangle =\frac 1{\sqrt{2\pi }}e^{ij\psi }$, $-\infty <j<\infty$ we have $$\label{repe1}\pi (z)\mid j\rangle =q^{-j}\mid j-1\rangle ,\ \ \ \pi
(z^{*})\mid j\rangle =q^{-j-1}\mid j+1\rangle ,\ \ \ \pi (\delta )\mid
j\rangle =\mid j-2\rangle .$$ Thus as topological space the quantum Euclidean group $E_q(2)$ is equivalent to the Hilbert space ${\cal L}^2(S)$. The measure on $E_q(2)$ is given by $$\mu (X_q)=(1-q^2)\sum_{j\in J}\langle j\mid \pi (\mu _E)\mid j\rangle ,$$ where $\mu _E$ is polynomial of coordinate functions $z$, $z^{*}$, $\delta
^{\pm 1}$; and $J\subset Z$ such that the vectors $\mid j\rangle$, $j\in J$ , span a basis in the subspace $H\subset {\cal L}^2(S)$ corresponding to the subspace $X_q\subset E_q(2)$. Since $E_q(2)$ can be obtained from $SU_q(2)$ by contraction we define $\mu _E$ from $\mu _S$ of ([\[invm\]](#invm){reference-type="ref" reference="invm"}) as $$\mu _E=\lim _{r\rightarrow \infty }(r^2\mu _S(\frac{u_0u_0^{*}}{r^2}
))=zz^{*}=\rho ^2.$$ Thus the invariant measure on $E_q(2)$ is given by $$\mu (X_q)=(1-q^2)\sum_{j\in J}\langle j\mid \pi (\rho ^2)\mid j\rangle
=N\sum_{j\in J}q^{-2j}.$$ By the virtue of the invariant measure we define the invariant integral on $E_q(2)$ as $$\psi (f)=(1-q^2)\sum_{j=-\infty }^\infty \langle j\mid \pi (f\rho ^2)\mid
j\rangle ,$$ provided that the left--hand side is finite. If $f(g)=f(\rho )$ the above expression can be rewritten by means of $q$--integral as $$\psi (f)=\int_{-\infty }^\infty f(\rho )d_{q^2}(\rho ^2).$$ The invariant measure and invariant integral on the quantum group $E_q(2)$ are then given by $$\label{invme}\mu (X_q)=(1-q^2)\sum_{j\in J}q^{-2j}$$ and $$\label{invine}\psi (f)=(1-q^2)\sum_{j=-\infty }^\infty \langle j\mid \pi
(f\rho ^2)\mid j\rangle$$ respectively. The subset $J\subset Z$ is defined such that the vectors $\mid
j\rangle$, $j\in J$ span the subspace $H\subset {\cal L}^2(S)$ corresponding to the subspace $X_q$ of $E_q(2)$.
