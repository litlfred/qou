---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-032-61-the-definition
section_title: "The definition"
section_number: 6.1
pages: 24-25
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.968
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let $A$ be a weak Hopf algebra and let $B \subset A$ be a weak Hopf subalgebra. We will define a complex $C^\bullet(A, B)$ that generalizes the subcomplex of the co-Hochschild complex of a Hopf algebra consisting of invariants of the adjoint action, cf. [@S; @Sch].

We set $C^0(A, B) = A_t \cap Z(A)$, the algebra of endomorphisms of the trivial $A$-module; and for all $n\geq 1$, we set $$\label{Cn}
C^n(A, B) := \{ f\in A^{\otimes n} \mid f = \text{Ad}(1)f \mbox{ and }
\text{Ad}(h)f = \text{Ad}(\varepsilon_t(h))f,\, \forall h\in B \},$$ where $\text{Ad}(h)$ denotes the adjoint action of $h$, i.e., $\text{Ad}(h)f = \Delta^n(h_{(1)}) f \Delta^n(S(h_{(2)}))$ for all $h\in B$ and $f\in A^{\otimes n}$. Here $\Delta^n : A \to A^{\otimes n}$ is the iteration of the comultiplication (we set $\Delta^1 =\text{id}$). Note that $A^{\otimes n}$ is a non-unital $B$-module with respect to $\text{Ad}$. The conditions of [\[Cn\]](#Cn){reference-type="eqref" reference="Cn"} mean that $A$ lies in $A\otimes_{A_t}\cdots \otimes_{A_t} A$ (where $A$ is an $A_t$-bimodule via $z_1\cdot h\cdot z_2 = z_1 S(z_2) h$ for $h\in A,\, z_1,z_2, \in A_t$) viewed as a subspace of $A^{\otimes n}$ and that $f$ commutes with $\Delta ^n(h)$ for all $h\in A$.

Let us define a linear map $\delta^n : C^n(A, B)\to A^{\otimes (n+1)}$ by $\delta^0(f) = f - S(f)$ and $$\begin{aligned}
\label{delta}
\delta^n(f)
&=& \text{Ad}(1) \{1\otimes f +\sum_{i=1}^n\, (-1)^i (\text{id}_{i-1}\otimes \Delta
\otimes \text{id}_{n-i})(f) +(-1)^{n+1} f\otimes 1\}
\end{aligned}$$ for $n \geq 1$.

::: lemma
For all $n\geq 0$ we have $\text{Im}(\delta^n) \subset C^{n+1}(A, B)$ and $\delta^{n+1}\circ \delta^n =0$, i.e., the collection $\{C^n(A, B),\,\delta^n\}_{n\geq 0}$ is a complex.
:::

::: proof
*Proof.* That $\delta^n(f),\, f\in C^n(A, B)$ is $\text{Ad}(1)$ stable is a part of definition [\[delta\]](#delta){reference-type="eqref" reference="delta"}. For all $h\in B$ we compute $$\begin{aligned}
\lefteqn{\text{Ad}(h)\delta^n(f) =} \\
&=& \text{Ad}(h)(1\otimes f) - \text{Ad}(h)(\Delta\otimes \text{id}_{n-1})f + \cdots \\
& & \cdots + (-1)^n\text{Ad}(h) (\text{id}_{n-1}\otimes \Delta)f 
    + (-1)^{n+1}\text{Ad}(h)(f\otimes 1) \\
&=& h_{(1)} S(h_{(3)}) \otimes \text{Ad}(h_{(2)})f - (\Delta\otimes\text{id}_{n-1})(\text{Ad}(h)f) +\cdots\\
& & \cdots + (-1)^n (\text{id}_{n-1}\otimes \Delta)\text{Ad}(h)f
    + (-1)^{n+1} \Delta^n(h_{(1)}) f \Delta^n(S(h_{(3)}))\otimes \varepsilon_t(h_{(2)})\\
&=& 1_{(1)}\varepsilon_t(h)\otimes \text{Ad}(1_{(2)})f - (\Delta\otimes\text{id}_{n-1})
    (\text{Ad}(\varepsilon_t(h))f) +\cdots\\
& &  \cdots + (-1)^n (\text{id}_{n-1}\otimes \Delta)\text{Ad}(\varepsilon_t(h))f 
    + (-1)^{n+1} \Delta^n(1_{(1)})\text{Ad}(\varepsilon_t(h))f \otimes 1_{(2)} \\
&=& \text{Ad}(\varepsilon_t(h))\delta^n(f),
\end{aligned}$$ where we used the identity $(\text{id}\otimes\varepsilon_t)\Delta(x) =
(1\otimes x)\Delta(1)$ for all $x\in A$. Therefore, $\delta^n(f)\in {C}^{n+1}(A, B)$. Thus, $\delta^n(C^n(A, B)) \subset C^{n+1}(A, B)$.

That $\delta^{n+1}\circ \delta^n =0$ can be checked in a direct standard way, by cancelling the similar terms with opposite signs among $(n+3)(n+2)$ tensors in $\delta^{n+1}\circ\delta^n(f)$. ◻
:::

The $n$-th cohomology group of the pair $A,\, B$ is $$\label{Hn}
H^n (A,\,B) := H^n(C^\bullet(A, B))= \mbox{Ker}(\delta^n)/\mbox{Im}(\delta^{n-1}), \qquad
\mbox{ for } n\geq 0.$$
