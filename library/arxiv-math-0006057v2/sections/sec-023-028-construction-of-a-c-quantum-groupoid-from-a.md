---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-023-028-construction-of-a-c-quantum-groupoid-from-a
section_title: "Construction of a $C^*$-quantum groupoid from a depth 2 subfactor"
section_number: 0.28
pages: 33-35
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.809
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
Let $N\subset M$ be a finite index ($[M:N]= \lambda^{-1}$) depth 2 II${}_1$ subfactor and $$N \subset M \subset M_1 \subset M_2 \subset \cdots$$ the corresponding Jones tower, $M_1 = \langle M,\,e_1 \rangle,\,
M_2 = \langle M_1,\,e_2 \rangle,\dots,$ where $e_1 \in N^\prime
\cap M_1,\,e_2 \in M^\prime \cap M_2,\cdots$ are the Jones projections. The depth 2 condition means that $N^\prime \cap M_{2}$ is the basic construction of the inclusion $N^\prime \cap M  \subset  N^\prime \cap M_{1}$. Let $\tau$ be the trace on $M_2$ normalized by $\tau(1)=1$.

Let us denote $$A=N'\cap M_1, \quad B=M'\cap M_2, \quad B_t=M'\cap M_1, \quad B_s=M_1'\cap M_2$$ and let $\mbox{Tr}\,$ be the trace of the regular representation of $B_t$ on itself. Since both $\tau$ and $\mbox{Tr}\,$ are non-degenerate, there exists a positive invertible element $w\in Z(B_t)$ such that $\tau(wz)=\mbox{Tr}\,(z)$ for all $z\in B_t$ (the index of $\tau\vert_{M'\cap M_1}$ in the sense of [@W]).

::: proposition
[]{#duality label="duality"} There is a canonical non-degenerate duality form between $A$ and $B$ defined by $$\langle\,a,\, b \,\rangle= \lambda^{-2}\tau(ae_2e_1wb)= \lambda^{-2}Tr E_{B_t}(bae_2e_1),$$ for all $a\in A$ and $b\in B$.
:::

::: proof
*Proof.* If $a\in A$ is such that $\langle\,a,\, B\,\rangle= 0$ , then, using [@PP1], 1.2, one has $$\tau(a e_2 e_1 B) = \tau(a e_2 e_1 (N^\prime \cap M_2)) = 0,$$ therefore, using the properties of $\tau$ and Jones projections, we get $$\begin{aligned}
\tau(a a^*) &=& \lambda^{-1} \tau(a e_2 a^*) =
\lambda^{-2}\tau(a e_2 e_1 (e_2 a^* ) ) = 0,
\end{aligned}$$ so $a=0$. Similarly for $b\in B$. ◻
:::

Using the duality $\langle\,a,\, b \,\rangle$, one defines a coalgebra structure on $B$ : $$\begin{aligned}
\langle\,a_1\otimes a_2,\, \Delta(b) \,\rangle&=&   \langle\,a_1 a_2,\, b \,\rangle, \\
\varepsilon(b) &=& \langle\,1,\, b\,\rangle, 
\end{aligned}$$ for all $a,a_1,a_2\in A$ and $b\in B$. Similarly, one defines a coalgebra structure on $A$.

We define a linear endomorphism $S_B:B\to B$ by $$E_{M_1}( b e_1 e_2) = E_{M_1}(e_2 e_1 S_B(b)),$$ Note that $\tau\circ S_B =\tau$. Similarly one can define a linear endomorphism $S_A:A\to A$ such that $E_{M^\prime}(S_A(a)e_2 e_1) = E_{M^\prime}(e_1 e_2 a)$ and $\tau\circ S_A =\tau$.

::: proposition
[]{#properties of S (1) label="properties of S (1)"} ([@NV2], 4.5, 5.2): The following identities hold :

1.  $S_B(B_s)=B_t$,

2.  $S_B^2(b) =b$ and $S_B(b)^* = S_B(b^*)$,

3.  $\Delta(b)(S_B(z)\otimes 1) = \Delta(b)(1\otimes z), \qquad 
    \Delta(bz)= \Delta(b)(z\otimes 1),\ (\forall z\in B_t)$,

4.  $S_B(bc) = S_B(c)S_B(b)$, $\Delta(S_B(b)) = (1\otimes w^{-1})(S_B(b_{(2)})\otimes S_B(b_{(1)}))
          (S_B(w)\otimes 1)$.
:::

Define an antipode and new involution of $B$ by $$S(b)=S_B(wbw^{-1}), \qquad
b^{\dag}= S(w)^{-1}b^*S(w).$$

::: theorem
[]{#B is a quantum groupoid label="B is a quantum groupoid"} With the above operations $B$ becomes a biconnected $C^*$-quantum groupoid with the counital subalgebras $B_s$ and $B_t$.
:::

::: proof
*Proof.* One can check ([@NV2], 4.6) that $\Delta(1)\in B_s\otimes B_t$, hence, since $\Delta(1)\in B_s\otimes B_t$ and $B_t$ commutes with $B_s$, we have $$\begin{aligned}
(\mbox{id}\otimes\Delta)\Delta(1) 
&=& 1_{(1)} \otimes \Delta(1)(1_{(2)} \otimes 1) \\
&=& (1 \otimes \Delta(1))(\Delta(1)\otimes 1)
    = (\Delta(1)\otimes 1) (1 \otimes \Delta(1))
\end{aligned}$$ which is axiom ([\[Delta 1\]](#Delta 1){reference-type="ref" reference="Delta 1"}) of Definition [\[finite quantum groupoid\]](#finite quantum groupoid){reference-type="ref" reference="finite quantum groupoid"}. The axiom ([\[eps m\]](#eps m){reference-type="ref" reference="eps m"}) dual to it is obtained similarly, considering the comultiplication in $A$.

As a consequence of the "symmetric square" relations $BM_1 =M_1B =M_2$ one obtains ([@NV2], 4.12) the identity $$\label{crucial}
bx =\lambda^{-1} E_{M_1}(b_{(1)} x e_2) b_{(2)} \quad \mbox{ for all } \quad
b\in B,\,  x\in M_1,$$ from where it follows that $$\label{good property}
E_{M_1}(bxye_2)  =\lambda^{-1} E_{M_1}(b_{(1)} x e_2) E_{M_1}(b_{(2)}ye_2) 
\quad \mbox{ for all } \quad b\in B,\,x,y\in M_1.$$ We use this identity to prove that $\Delta$ is a homomorphism : $$\begin{aligned}
\langle\,a_1a_2,\, bc \,\rangle
&=& \langle\,\lambda^{-1}E_{M_1}(ca_1a_2e_2),\, b \,\rangle\\
&=& \langle\,\lambda^{-2}E_{M_1}(c_{(1)} a_1e_2)E_{M_1}(c_{(2)} a_2e_2),\, b \,\rangle\\
&=& \langle\,\lambda^{-1}E_{M_1}(c_{(1)} a_1e_2), b_{(1)} \,\rangle
    \langle\,\lambda^{-1}E_{M_1}(c_{(2)} a_2 e_2),\, b_{(2)} \,\rangle\\
&=& \langle\,a_1,\, b_{(1)}c_{(1)} \,\rangle\langle\,a_2,\, b_{(2)} c_{(2)} \,\rangle,
\end{aligned}$$ for all $a_1,a_2 \in A$, whence $\Delta(bc) =  \Delta(b)\Delta(c)$. Next, $$\begin{aligned}
\langle\,a,\, \varepsilon(1_{(1)}b)1_{(2)} \,\rangle
&=& \langle\,1,\,1_{(1)}b \,\rangle\langle\,a,\, 1_{(2)} \,\rangle\\
&=& \langle\,\lambda^{-1}E_{M_1}(be_2), 1_{(1)} \,\rangle\langle\,a,\, 1_{(2)} \,\rangle\\
&=& \langle\,\lambda^{-1}E_{M_1}(be_2)a, 1 \,\rangle
 = \langle\,a,\, \lambda^{-1}E_{M_1}(be_2) \,\rangle, 
\end{aligned}$$ therefore $\varepsilon_t(b) = \lambda^{-1}E_{M_1}(be_2)$ (similarly, $\varepsilon_s(b) = \lambda^{-1}E_{M_1'}(e_2b)$). Using Equation ([\[good property\]](#good property){reference-type="ref" reference="good property"}) we have $$\begin{aligned}
\langle\,a,\, b_{(1)} S(b_{(2)}) \,\rangle
&=& \langle\,a,\, b_{(1)} S_B(wb_{(2)} w^{-1}) \,\rangle\\
&=&  \lambda^{-3} \tau (E_{M_1}(S_B(w b_{(2)} w^{-1}) a e_2) e_2 e_1 wb_{(1)}) \\
&=&  \lambda^{-3} \tau (E_{M_1}(e_2 a wb_{(2)} w^{-1}) e_2 e_1 wb_{(1)}) \\
&=& \lambda^{-3} \tau (E_{M_1}(e_2 a wb_{(2)} w^{-1})E_{M_1}(e_2 e_1 wb_{(1)}) ) \\
&=& \lambda^{-2} \tau (E_{M_1}(e_2 a e_1 wb)) = \langle\,a,\, \varepsilon_t(b) \,\rangle. 
\end{aligned}$$ The antipode $S$ is anti-multiplicative and anti-comultiplicative, therefore axiom ([\[S id S\]](#S id S){reference-type="ref" reference="S id S"}) of Definition [\[finite quantum groupoid\]](#finite quantum groupoid){reference-type="ref" reference="finite quantum groupoid"} follows from the other axioms. Clearly, $\varepsilon_t(B) = M'\cap M_1$ and $\varepsilon_s(B) = M_1'\cap M_2$. $B$ is biconnected, since the inclusion $B_t=M^\prime \cap M_1 \subset B =M^\prime \cap M_2$ is connected ([@GHJ], 4.6.3) and $B_t \cap B_s =(M^\prime \cap M_1)\cap
(M_1^\prime \cap M_2)= \mathbb{C}$.

Finally, from the properties of $\Delta$ and $S_B$ we have $\Delta(b^{\dag})=\Delta(b)^{{\dag}\otimes{\dag}}$. ◻
:::

::: remark
[]{#properties of B label="properties of B"}

1.  $S^2(b) = gbg^{-1}$, where $g=S(w)^{-1}w$.

2.  The Haar projection of $B$ is $e_2w$ and the normalized Haar functional is $\phi(b) =$ $= \tau(S(w)wb)$.

3.  The non-degenerate duality $\langle\,\, ,\,\,\rangle$ makes $A=N^\prime \cap M_1$ the $C^*$-quantum groupoid dual to $B$.

4.  Since the Markov trace ([@GHJ], 3.2.4) of the inclusion $N\subset M$ is also the Markov trace of the finite-dimensional inclusion $A_t\subset A$, it is clear that $[M:N]=[A:A_t]=[B:B_t]$. We call last number *the index of the quantum groupoid* $B$.

5.  Let us mention two classification results obtained in ([@NV2], 4.18, 4.19) by quantum groupoid methods: (a) If $N\subset M$ is a depth 2 subfactor such that $[M:N]$ is a square free integer (i.e., $[M:N]$ is an integer which has no divisors of the form $n^2,\, n > 1$), then $N^\prime\cap M=\mathbb{C}$, and there is a (canonical) minimal action of a Kac algebra $B$ on $M_1$ such that $M_2 \cong  M_1{>\!\!\!\triangleleft}B$ and $M=M_1^B$. (b) If $N\subset M$ is a depth 2 II${}_1~$subfactor such that $[M:N]=p$ is prime, then $N^\prime\cap M=\mathbb{C}$, and there is an outer action of the cyclic group $G=\mathbb{Z}/p\mathbb{Z}$ on $M_1$ such that $M_2 \cong  M_1{>\!\!\!\triangleleft}G$ and $M=M_1^G$.
:::
