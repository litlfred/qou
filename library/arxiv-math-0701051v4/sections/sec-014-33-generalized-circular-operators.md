---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-014-33-generalized-circular-operators
section_title: "Generalized circular operators"
section_number: 3.3
pages: 11-12
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.964
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
Let $\mathcal{D}$ be the algebra of continuous functions on $\mathbb{R}_+$. We equip it with an expected value $\phi:\mathcal{D}\rightarrow \mathbb{C}$ given by $\phi(f)=\int_0^{\infty} f(t) dt$.

We consider an operator-valued probability space, which by definition is some $\ast$-algebra $\mathcal{A}$ such that $\mathcal{D}\subseteq \mathcal{A}$ and equipped with a conditional expectation $\mathbb{E}:\mathcal{A}\rightarrow\mathcal{D}$. For a given (generalized) Young diagram $\lambda$ let $T\in\mathcal{A}$ be a generalized circular operator [@VoiculescuDykemaNica1992; @Speicher1998] with a covariance $$\begin{aligned}
\nonumber \big[ k(T,f T^\ast)\big] (s)&= \int_{t:  (t,s)\in\lambda }f(t)\ dt,
\\
\label{eq:strangesign}
\big[ k(T^\ast,f T)\big] (s)&= -\int_{t:  (s,t)\in\lambda }f(t)\ dt, \\
\nonumber \big[ k(T,f T)\big] (s)&= 0,\\
\nonumber \big[ k(T^\ast,f T^\ast)\big] (s)&= 0.
\end{aligned}$$

::: theorem
[]{#theo:free-proba-may-help label="theo:free-proba-may-help"} For any (generalized) Young diagram $\lambda$ $$R_{l+1}^{\lambda}= \phi\big[ (T^\ast T)^l \big].$$
:::

::: proof
*Proof.* It is easy to check that for permutations $\sigma_1,\sigma_2$ which contribute to [\[eq:freecumulants-come\]](#eq:freecumulants-come){reference-type="eqref" reference="eq:freecumulants-come"} the corresponding bipartite graph is a tree therefore the calculation of $N^{\lambda}(\sigma_1,\sigma_2)$ is particularly simple, namely it is a certain iterated integral. The same iterated integral appears in the nested evaluation of amalgamated free cumulants therefore $N^{\lambda}(\sigma_1,\sigma_2)=\pm
\phi\big[ k_{\sigma_2}(T^\ast,T,\cdots,T^\ast,T)\big]$. The plus/minus sign is due to the minus sign in the covariance [\[eq:strangesign\]](#eq:strangesign){reference-type="eqref" reference="eq:strangesign"}. It is easy to check that in fact $$(-1)^{|\sigma_1|} N^{\lambda}(\sigma_1,\sigma_2)=
\phi\big[ k_{\sigma_2}(T^\ast,T,\cdots,T^\ast,T)\big].$$

The moment-cumulant formula $$\mathbb{E}\big[ (T^\ast T)^l \big]= \sum_{\sigma\in\mathop{\mathrm{NC}}_2}
k_{\sigma}(T^\ast,T,\cdots,T^\ast,T)$$ finishes the proof since there is a bijective correspondence between non-crossing pair partitions and the minimal factorizations. ◻
:::

Due to the analytic machinery of free probability the calculation of the moments of $T$ in a closed form is possible in many cases therefore Theorem [\[theo:free-proba-may-help\]](#theo:free-proba-may-help){reference-type="ref" reference="theo:free-proba-may-help"} gives a practical method of calculating the free cumulants of the Young diagrams.
