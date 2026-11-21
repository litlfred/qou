---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-025-030-a-galois-correspondence
section_title: "A Galois correspondence"
section_number: 0.30
pages: 37-38
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.956
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
The following simple observation gives a natural passage from arbitrary finite depth subfactors to depth $2$ subfactors.

::: proposition
[]{#reducing depth label="reducing depth"} For all $k\geq 0$ the inclusion $N\subset M_k$ has depth $d+1$, where $d$ is the smallest positive integer $\geq
\frac{n-1}{k+1}$. In particular, $N\subset M_i$ has depth $2$ for all $i\geq n-2$, i.e., any finite depth subfactor is an intermediate subfactor of some depth $2$ inclusion.
:::

::: proof
*Proof.* Note that $\dim Z(N'\cap M_i) = \dim Z(N'\cap M_{i+2})$ for all $i\geq n-2$. By [@PP2], the tower of basic construction for $N\subset M_k$ is $$N\subset M_k \subset M_{2k+1} \subset M_{3k+2} \subset \cdots,$$ therefore, the depth of this inclusion is equal to $d+1$, where $d$ is the smallest positive integer such that $d(k+1)-1 \geq n-2$. ◻
:::

This result means that $N\subset M$ can be realized as an intermediate subfactor of a crossed product inclusion $N\subset N{>\!\!\!\triangleleft}B$ for some quantum groupoid $B$ : $$N\subset M \subset N{>\!\!\!\triangleleft}B.$$ Recall that in the case of a Kac algebra action there is a Galois correspondence between intermediate von Neumann subalgebras of $N\subset N{>\!\!\!\triangleleft}B$ and left coideal $*$-subalgebras of $B$ [@ILP],[@E1]. Thus, it is natural to ask about a quantum groupoid analogue of this correspondence.

A unital $*$-subalgebra $I\subset B$ such that $\Delta(I) \subset B\otimes I$ (resp. $\Delta(I) \subset I\otimes B$) is said to be a left (resp. right) *coideal $*$-subalgebra*. The set $\ell(B)$ of left coideal $*$-subalgebras is a lattice under the usual operations: $$I_1 \wedge I_2 = I_1\cap I_2, \qquad I_1 \vee I_2 = (I_1\cup I_2)''$$ for all $I_1,I_2\in \ell(B)$. The smallest element of $\ell(B)$ is $B_t$ and the greatest element is $B$. $I\in \ell(B)$ is said to be *connected* if $Z(I)\cap B_s =\mathbb{C}$.

To justify this definition, note that if $I=B$, then this is precisely the definition of a connected quantum groupoid, and if $I=B_t$, then this definition is equivalent to $\widehat B$ being connected ([@N1], 3.10, 3.11, [@BNSz], 2.4).

On the other hand, the set $\ell(M_1\subset M_2)$ of intermediate von Neumann subalgebras of $M_1\subset M_2$ also forms a lattice under the operations $$K_1 \wedge K_2 = K_1\cap K_2, \qquad K_1 \vee K_2 = (K_1\cup K_2)''$$ for all $K_1,K_2\in \ell(M_1\subset M_2)$. The smallest element of this lattice is $M_1$ and the greatest element is $M_2$.

Given a left (resp. right) action of $B$ on a von Neumann algebra $N$, we will denote (by an abuse of notation) $$N{>\!\!\!\triangleleft}I = \mbox{span}\{ [x\otimes b] \mid x\in N,\, b\in I\} \subset
N{>\!\!\!\triangleleft}B.$$ The next theorem establishes a *Galois correspondence*, i.e., a lattice isomorphism between $\ell(M_1\subset M_2)$ and $\ell(B)$.

::: theorem
[]{#galois correspondence label="galois correspondence"} Let $N\subset M\subset M_1\subset M_2\subset\cdots$ be the tower constructed from a depth $2$ subfactor $N\subset M$, $B=M'\cap M_2$ be the corresponding quantum groupoid, and $\theta$ be the isomorphism between $M_1{>\!\!\!\triangleleft}B$ and $M_2$ (Proposition [\[crossproduct\]](#crossproduct){reference-type="ref" reference="crossproduct"}). Then $$\begin{aligned}
\phi &:& \ell(M_1\subset M_2) \to \ell(B) :
     K\mapsto \theta^{-1}(M'\cap K) \subset B\\
\psi &:& \ell(B) \to \ell(M_1\subset M_2) :
     I \mapsto \theta(M_1{>\!\!\!\triangleleft}I)\subset M_2.
\end{aligned}$$ define isomorphisms between $\ell(M_1\subset M_2)$ and $\ell(B)$ inverse to each other.
:::

::: proof
*Proof.* First, let us check that $\phi$ and $\psi$ are indeed maps between the specified lattices. It follows from the definition of the crossed product that $M_1{>\!\!\!\triangleleft}I$ is a von Neumann subalgebra of $M_1{>\!\!\!\triangleleft}B$, therefore $\theta(M_1{>\!\!\!\triangleleft}I)$ is a von Neumann subalgebra of $M_2=\theta(M_1{>\!\!\!\triangleleft}B)$, so $\psi$ is a map to $\ell(M_1\subset M_2)$. To show that $\phi$ maps to $\ell(B)$, let us show that the annihilator $(M'\cap K)^0 \subset \widehat B$ is a left ideal in $\widehat B$.

For all $x\in A,\, y\in (M'\cap K)^0$, and $b\in M'\cap K$ we have $$\begin{aligned}
\langle\,xy,\, b\,\rangle
&=& \lambda^{-2}\tau(xye_2e_1wb) = \lambda^{-2}\tau(ye_2e_1wbx)\\
&=& \lambda^{-3} \tau(ye_2e_1E_{M'}(e_1wbx))
  = \langle\,y,\,\lambda^{-1}E_{M'}(e_1wbx)\,\rangle,
\end{aligned}$$ and it remains to show that $E_{M'}(e_1wbx) \in M'\cap K$. By ([@GHJ], 4.2.7), the square $$\begin{array}{ccc}
K & \subset & M_2 \\
\cup &      & \cup \\
M'\cap K &\subset & M'\cap M_2
\end{array}$$ is commuting, so $E_{M'}(K) \subset M'\cap K$. Since $e_1wbx\in K$, then $xy \in (M'\cap K)^0$, i.e., $(M'\cap K)^0$ is a left ideal and $\phi(K)= \theta^{-1}(M'\cap K)$ is a left coideal $*$-subalgebra.

Clearly, $\phi$ and $\psi$ preserve $\wedge$ and $\vee$, moreover $\phi(M_1) =B_t,\,\phi(M_2)=B$ and $\psi(B_t)=M_1,\,
\psi(B) = M_2$, therefore they are morphisms of lattices.

To see that they are inverses for each other, we first observe that the condition $\psi\circ\phi =\mbox{id}$ is equivalent to $M_1(M'\cap K)= K$, and the latter follows from applying the conditional expectation $E_K$ to $M_1(M'\cap M_2)= M_1B = M_2$. The condition $\phi\circ\psi =\mbox{id}$ translates into $\theta(I) = M'\cap \theta(M_1 {>\!\!\!\triangleleft}I)$. If $b\in I,\, x\in M=M_1^B$, then $$\begin{aligned}
\theta(b)x
&=& \theta([1\otimes b][x\otimes 1])
     = \theta([(b_{(1)}\triangleright x) \otimes b_{(2)}]) \\
&=& \theta([x(1_{(2)}\triangleright 1)\otimes \varepsilon(1_{(1)} b_{(1)})b_{(2)} ])
     = \theta([x\otimes b]) =x\theta(b),
\end{aligned}$$ i.e., $\theta(I)$ commutes with $M$. Conversely, if $x\in M'\cap \theta(M_1 {>\!\!\!\triangleleft}I)\subset B$, then $x=\theta(y)$ for some $y\in (M_1 {>\!\!\!\triangleleft}I) \cap B = I$, therefore $x\in \theta(I)$. ◻
:::

::: corollary
([@NV3], 4.5)

1.  $K = M{>\!\!\!\triangleleft}I$ is a factor iff $Z(I)\cap B_s =\mathbb{C}$.

2.  The inclusion $M_1 \subset K = M_1{>\!\!\!\triangleleft}I$ is irreducible iff $B_s \cap I=\mathbb{C}$.
:::
