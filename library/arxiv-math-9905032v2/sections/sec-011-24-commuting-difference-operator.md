---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-011-24-commuting-difference-operator
section_title: "Commuting difference operator"
section_number: 2.4
pages: 17-18
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.968
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
Consider the difference operators $\Delta$ and $\nabla$ on the lattice $\mathbb{Z}$, $$(\Delta f)(k)=f(k+1)-f(k)\,, \qquad (\nabla f)(k)=f(k)-f(k-1)\,.$$ Note that $\nabla=-\Delta^*$ as operators on $\ell^2(\mathbb{Z})$. Consider the following second order difference Sturm--Liouville operator

$$\label{e0002}
D=\Delta\circ\alpha\circ\nabla +\beta\,,$$

where $\alpha$ and $\beta$ are operators of multiplication by certain functions $\alpha(k)$, $\beta(k)$. The operator [\[e0002\]](#e0002){reference-type="eqref" reference="e0002"} is self--adjoint in $\ell^2(\mathbb{Z})$. A straightforward computation shows that

$$\begin{gathered}
\label{e0003}
\big[D f\big](k)=(-\alpha(k+1)-\alpha(k)+\beta(k))f(k)+\\
\alpha(k)f(k-1)+\alpha(k+1)f(k+1)\,.  
\end{gathered}$$

It follows that if $\alpha(s)=0$ for a certain $s\in\mathbb{Z}$ then the space of functions $f(k)$ vanishing for $k<s$ is invariant under $D$.

::: proposition
Let $[\mathsf{J}]_s$ denote the operator in $\ell^2(\{s,s+1,\dots\})$ obtained by restricting the kernel $\mathsf{J}$ to $\{s,s+1,\dots\}$. Then the difference Sturm--Liouville operator [\[e0002\]](#e0002){reference-type="eqref" reference="e0002"} commutes with $[\mathsf{J}]_s$ provided $$\alpha(k)=k-s, \qquad
\beta(k)=-\,\frac{k(k+1-s-2\sqrt\theta)}{\sqrt\theta}+\textup{const} \,.$$
:::

::: proof
*Proof.* Since $[\mathsf{J}]_s$ is the square of the operator with the kernel $J_{k+l+1-s}$, it suffices to check that the latter operator commutes with $D$, with the above choice of $\alpha$ and $\beta$. But this is readily checked using [\[e0003\]](#e0003){reference-type="eqref" reference="e0003"}. ◻
:::

This proposition is a counterpart of a known fact about the Airy kernel, see [@TW]. Moreover, in the scaling limit when $\theta\to\infty$ and $$k=2\sqrt\theta+x\,\theta^{1/6}, \qquad s=2\sqrt\theta+\varsigma\,\theta^{1/6},$$ the difference operator $D$ becomes, for a suitable choice of the constant, the differential operator $$\frac d{dx}\circ(x-\varsigma)\circ \frac d{dx} -x(x-\varsigma),$$ which commutes to the Airy operator restricted to $(\varsigma,+\infty)$. The above differential operator is exactly that of Tracy and Widom [@TW].

::: remark
Presumably, this commuting difference operator can be used to obtain, as was done in [@TW] for the Airy kernel, asymptotic formulas for the eigenvalues of $[\mathsf{J}]_s$, where $s=2\sqrt\theta+\varsigma\,\theta^{1/6}$ and $\varsigma\ll 0$. Such asymptotic formulas may be very useful if one wishes to refine Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"} and to establish convergence of moments in addition to convergence of distribution functions. For individual distributions of $\lambda_1$ and $\lambda_2$ the convergence of moments was obtained, by other methods, in [@BDJ1; @BDJ2].
:::
