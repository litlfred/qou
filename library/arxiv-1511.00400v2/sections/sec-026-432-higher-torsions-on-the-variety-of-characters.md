---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-026-432-higher-torsions-on-the-variety-of-characters
section_title: "Higher torsions on the variety of characters"
section_number: 4.3.2
pages: 30-32
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.985
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Again assume that $M^3$ is an oriented hyperbolic 3-manifold of finite volume with a single cusp. We define the Reidemeister torsion on the distinguished curve of characters $X_0(M^3)$.

::: definition
For $k_1$ or $k_2$ odd, with $k_1\neq k_2$, and for $\chi_\rho\in X_0(M^3)- \mathrm{E}^{k_1,k_2}$, where $\mathrm{E}^{k_1,k_2}$ is as in Definition [\[def:exceptional\]](#def:exceptional){reference-type="ref" reference="def:exceptional"}, define $$\mathbb{T}_M^{k_1,k_2}(\chi_\rho)=
 \begin{cases}
\operatorname{tor}(M^3, \rho^{k_1,k_2})   & \textrm{if } \rho^{k_1,k_2} \textrm{ is acyclic;} \\ 
   0                & \textrm{otherwise.}
 \end{cases}$$ For $k_1$ and $k_2$ even, with $k_1\neq k_2$, $\gamma$ a peripheral curve, and $\chi_\rho\in X_0(M^3)- \mathrm{F}^{k_1,k_2}$ (where $\mathrm{F}^{k_1,k_2}$ is as in [\[eqn:FF\]](#eqn:FF){reference-type="eqref" reference="eqn:FF"}), define $$\mathbb{T}_{M,\gamma}^{k_1,k_2}(\chi_\rho)=
\begin{cases} \operatorname{tor}(M^3, \rho^{k_1,k_2}, \{a\cap \gamma, a\cap [T^2]\}) &  \textrm{if } \langle a\cap \gamma \rangle= H_1(M^3; \rho^{k_1,k_2}),  \\
                & \quad  \langle  a\cap [T^2] \rangle= H_2(M^3; 
                \rho^{k_1,k_2});  \\
   0                & \textrm{otherwise.} 
\end{cases}$$
:::

We also use the notation $$\mathbb{T}_M^{k}=  \mathbb{T}_M^{k,0} \qquad\textrm{ and }\qquad \mathbb{T}^{k}_{M, \gamma}=  
\mathbb{T}_{M,\gamma}^{k,0}$$ for $k$ odd or even respectively.

The proof of Proposition [\[prop:rational\]](#prop:rational){reference-type="ref" reference="prop:rational"} with minor changes yields the following:

::: prop
For $k_1\neq k_2$, $\mathbb{T}_M^{k_1,k_2}$ and $\mathbb{T}_{M,\gamma}^{k_1,k_2}$ are nonzero (real) analytic functions on $X_0(M^3)- \mathrm{E}^{k_1,k_2}$ for $k_1$ or $k_1$ odd, or $X_0(M^3)- \mathrm{F}^{k_1,k_2}$ for $k_1$ and $k_2$ even, holomorphic when $k_2=0$ and antiholomorphic when $k_1=0$.
:::

When $H^1(M^3;\mathbb{Z})\cong \mathbb{Z}$ there is a well defined Alexander polynomial $\Delta(t)$, and we can give conditions for the regularity of $\mathbb{T}_M^{k}$ and $\mathbb{T}_M^{k, \gamma}$ on the whole curve $X_0(M^3)$.

::: prop
[]{#prop:koddEemplty label="prop:koddEemplty"} Assume that $H^1(M^3;\mathbb{Z})\cong \mathbb{Z}$ and that no root of $\Delta(t)$ is a root of unity. Then for $k$ odd $\mathrm{E}^{k,0}=\emptyset$. Hence for $k$ odd $\mathbb{T}_{M}^{k}$ is a holomorphic function on $X_0(M^3)$.
:::

::: proof
*Proof.* The proof of Proposition [\[prop:rational\]](#prop:rational){reference-type="ref" reference="prop:rational"} applies here with a minor modification. Notice that the condition on the homology implies that the trivial character does not lie in $X_0(M^3)$. On the other hand, the reducible characters in $X_0(M^3)$ are the characters of the composition of a surjection $$\pi_1 M^3\to \mathbb{Z}$$ with a representation that maps the generator of the cyclic group to $$A= \begin{pmatrix}
  \lambda & 0 \\
  0 & \lambda^{-1}
 \end{pmatrix}$$ with $\Delta(\lambda^2)=0$ [@Burde1967; @dR1967]. Since $\lambda$ is not a root of unity and $k$ is odd, $\operatorname{Sym}^k(A)$ has no eigenvalue equal to one, hence $H^0(M^3;\rho^k)=0$ for every $\rho$ with character in $X_0(M^3)$. ◻
:::

::: prop
Assume that $M^3=S^3-\mathcal{K}$ is a knot exterior in the sphere. Assume also that no root of $\Delta(t)$ is a root of unity and all roots have multiplicity one. Then for $k$ even, $\mathbb{T}^k_{M, \gamma}$ can be extended to the whole curve $X_0(M^3)$.
:::

::: proof
*Proof.* There are two issues to discus: the dimension of $H^0(T^2;\rho)$ and the vanishing or not of $H^0(M^3;\rho)$. For the first one, the assumption $M^3=S^3-\mathcal{K}$ implies that $\rho$ is never trivial on the peripheral torus $T^2$. It my happen that $\rho(\pi_1T^2)$ is non-trivial but $\operatorname{Sym}^{k}(\rho(\pi_1T^2))$ has an invariant subspace of dimension $\geq 2$. However, this issue only occurs when $\rho(\pi_1T^2)$ is contained in a 1-parameter subgroup $G$ of $\mathrm{SL}_2(\mathbb{C})$ conjugate to the group of diagonal matrices. Then $\operatorname{Sym}^{k}(G)$ has only one invariant subspace, that varies analytically on $\rho$. Thus the element $a$ in the expression of the cup products can be chosen to depend analytically on $\rho$.

Next discuss $H^0(M^3;\rho)$. The argument in Proposition [\[prop:koddEemplty\]](#prop:koddEemplty){reference-type="ref" reference="prop:koddEemplty"} fails in the case $k$ even because $\operatorname{Sym}^k$ has always an invariant subspace, thus for those reducible representations $H^0(M^3;\rho^k)\neq 0$ and further discussion on reducible representations is required. Namely, at a reducible representation, for the corresponding abelian representation $\rho$ as in the proof of Proposition [\[prop:koddEemplty\]](#prop:koddEemplty){reference-type="ref" reference="prop:koddEemplty"}, the hypothesis that $\lambda$ is not a root of unity implies that $\operatorname{Sym}^k(A)$ has a single eigenvalue equal to one, hence $\dim H^0(M^3;\rho^k)=1$. The results of [@HPS2001; @HP05], and the hypothesis that the root is simple, yield that there are, up to conjugation, two representations $\rho'$ and $\rho''$ that are non abelian and have the same character as $\rho$. In particular $H^0(M^3;(\rho')^{k_1,k_2})\cong H^0(M^3;(\rho'')^{k_1,k_2})=0$. Now, using the arguments of Proposition [\[prop:rational\]](#prop:rational){reference-type="ref" reference="prop:rational"}, we may define the torsion in a Zariski dense subset of the component of $\hom(\pi_1M^3, \mathrm{SL}_2(\mathbb{C}))$ that corresponds to $X_0(M^3)$. It suffices to consider an open neighborhood of $\rho'$ for the usual topology that projects to a neighborhood of $\chi_\rho$ [@HPS2001; @HP05], which proves that the torsion on a punctured neighborhood of $\chi_\rho$ extends to $\chi_\rho$. ◻
:::

The assertion for the case $k=2$ has been proved by Yamaguchi in [@Yamaguchi07]. More precisely he computes the precise value of $\mathbb{T}^{2}_{M,\gamma}$ at the reducible character.

::: example
Some torsion functions are computed here for the figure eight knot exterior. Let $\theta=\theta_m$ denote the evaluation of a character of a meridian: $\theta_m(\chi)=\chi(m)$ (i.e. the trace of a meridian). As mentioned in Example [\[ex:fig8sl2\]](#ex:fig8sl2){reference-type="ref" reference="ex:fig8sl2"}, in [@Kitano94b] Kitano computes: $$\mathbb{T}_M=\mathbb{T}_M^{1} =2-2 {\theta}.$$ Further computations with the help of symbolic software yield: $$\begin{aligned}
 \mathbb{T}_M^{3} &= &- \left( {\theta}^{2}-2\,{\theta}-2 \right) ^{2}\\
  \mathbb{T}_M^{5} &=&
2\, \left( {\theta}-1 \right)  \left( {\theta}^{8}+2\,{\theta}^{7}-13\,{\theta}^{6}-20\,{\theta}^
{5}+49\,{\theta}^{4}+48\,{\theta}^{3}-33\,{\theta}^{2}-18\,{\theta}-18 \right) \\
 \mathbb{T}_M^{7} &=&
- \left( {\theta}-1 \right) ^{2} \left( 2\,{\theta}^{7}-4\,{\theta}^{6}-21\,{\theta}^{5}+19
\,{\theta}^{4}+57\,{\theta}^{3}+13\,{\theta}^{2}-18\,{\theta}-6 \right) ^{2}\\
 \mathbb{T}_M^{9} &=& 
  2\, \left( {\theta}-1 \right)  \left( {\theta}^{12}+2\,{\theta}^{11}-13\,{\theta}^{10}-13\,{
{\theta} }^{9}+27\,{\theta}^{8}-{\theta}^{7}+95\,{\theta}^{6} +90\,{\theta}^{5}
\right.\\ & & \left. 
-148\,{\theta}^{4}-74\,{{\theta}
}^{3}+61\,{\theta}^{2}+12\,{\theta}-6 \right) ^{2}.
\end{aligned}$$ Remark that these torsions are functions on the variable $\theta=\theta_m$, the trace of the meridian. This is not always the case, for instance for $\mathbb{T}_{M,\gamma}^2$, computed in [@Memoirs] (and in Section [\[sec:adj\]](#sec:adj){reference-type="ref" reference="sec:adj"}) and described below. We also computed: $$\begin{gathered}
  \mathbb{T}_M^{2,1}=
  13+3\,{\theta}^{4}-3\,  \overline{\theta}  ^{3}-14\,{\theta}^{2}-3\,
  \overline{\theta}   ^{2}+13\,\overline{\theta}+{\theta}^{4}\overline{\theta}
+4\,{\theta}^{2}  \overline{\theta}   ^{3}+2\,{\theta}^{2}  
\overline{\theta}  ^{2} \\ -16\,{\theta}^{2}\overline{\theta}-{\theta}^{4}  
\overline{\theta}   ^{3}+{\theta}^{4}   \overline{\theta}  ^{2}
+
\eta\overline{\eta} \left( {\theta}^{2}\overline{\theta}-{\theta}^{2}-\overline{\theta}-1
 \right) 
\end{gathered}$$ where $\eta$ is a variable that satisfies $\eta^2= ({\theta}^2-1)({\theta}^2-5)$. This variable can be written in terms of the traces of other elements, see Equation [\[eqn:x1+x2\]](#eqn:x1+x2){reference-type="eqref" reference="eqn:x1+x2"}.
:::

In subsection [\[subsection:eight\]](#subsection:eight){reference-type="ref" reference="subsection:eight"} other torsions are computed. If $m$ and $l$ denote respectively the meridian and the longitude, by [\[eqn:T2l\]](#eqn:T2l){reference-type="eqref" reference="eqn:T2l"}, [\[eqn:T2m\]](#eqn:T2m){reference-type="eqref" reference="eqn:T2m"}, [\[eqn:t84\]](#eqn:t84){reference-type="eqref" reference="eqn:t84"}: $$\mathbb{T}_{M,l}^2= 5-2\theta^2, \qquad \mathbb{T}_{M,m}^2= \frac12 \eta, \quad   \textrm{ and }  \quad  \mathbb{T}_{M,l}^4=8 (2-\theta^2).$$
