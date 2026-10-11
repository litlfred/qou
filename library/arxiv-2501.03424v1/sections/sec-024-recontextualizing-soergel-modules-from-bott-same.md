---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner"
section_id: sec-024-recontextualizing-soergel-modules-from-bott-same
section_title: "Recontextualizing Soergel modules from Bott-Samelson modules"
section_number: null
pages: 16-17
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner — This paper presents an exposition of Soergel bimodules, the categ oriﬁcation of Hecke alge- bras, and their applications to"
text_source: latex
latex_prose_ratio: 0.686
latex_coverage_ratio: 0.972
---
We now take an arbitrary Coxeter system $(W,S)$ and a $W$-representation $\h$ over some field $\mathbf{k}.$ Let $R = \text{Sym}(\h^*)$ with $\deg(\h^*) = 2.$ Consider the subcategories $\overline{\mathbb{S}\text{Bim}}(\h, W)$ of Soergel bimodules and $\overline{\mathbb{BS}\text{Bim}}(\h, W)$ of Bott-Samelson bimodules. Recall that Soergel modules are obtained via these respective bimodules. We have to be a little tricky here and view $\mathbf{k}$ as a graded $R$-module with all positive degree polynomials acting by zero. 
 
\subsubsection{Definition}
 Let $\underline{w} = (s_1, \ldots, s_m)$ be a reduced expression for $w.$ The \textit{Bott-Samelson module} $\overline{BS}(\underline{w})$ is the graded right $R$-module 
 $$\overline{BS}(\underline{w}) = \mathbf{k} \otimes_R BS(\underline{w}) = \mathbf{k} \otimes_R B_{s_1} \otimes_R \cdots \otimes_R B_{s_m}$$
 $$\simeq \mathbf{k} \otimes_R R \otimes_{R^{s_1}} R \otimes_{R^{s_2}} \cdots \otimes_{R^{s_m}} R(m).$$
 Now we can see more clearly how we get our Soergel modules. Explicitly, they're any graded right $R$-modules isomorphic to a finite direct sum of shifts of direct summands of Bott-Samelson modules. Our subcategory $\overline{\mathbb{S}\text{Bim}}(\h, W)$ from earlier is in fact a full subcategory of gmod-$R$. We can now consider the functor 
 $$\mathbf{k} \otimes_R (-): R\text{-gmod-}R \rightarrow \text{gmod-}R,$$
 which is an additive functor sending $\overline{BS}(\underline{w}) \mapsto \overline{BS}(\underline{w}).$ Thus it restricts to 
 $$\mathbf{k} \otimes_R (-): \mathbb{S}\text{Bim}(\h, W) \longrightarrow \overline{\mathbb{S}\text{Bim}}(\h, W).$$
 This gives us the idea that Soergel modules can equivalently be thought of as graded $R$-modules that come from direct summands of $\mathbf{k} \otimes_R B,$ where $B$ is a Soergel bimodule. To make use of this functor, we give the following

 
\subsubsection{Proposition}
 If $W$ is finite, and $\h$ is reflection faithful, the assignment 
 $$\mathbf{k} \otimes_R \Hom^\bullet_{R\text{-gmod-}R}(B, B') \longrightarrow \Hom^\bullet_{\text{gmod-}R}(\mathbf{k} \otimes_R B, \mathbf{k} \otimes_R B')$$
 is an isomorphism for any Soergel bimodules $B, B'.$

 
\subsubsection{}
 Before we move into the final part of the story, recall that Soergel bimodules give the categorification of the Hecke algebra $\mathcal{H},$ and that the split Grothendieck group is a $\Z[v, v^{-1}]$-algebra with the isomorphism 
 $$[\mathbb{S}\text{Bim}(\h, W)]_\oplus \simeq \mathcal{H}.$$
 When we descend to Soergel modules, we notice that the category $\overline{\mathbb{S}\text{Bim}}(\h, W)$ is not monoidal. But we still take $\overline{\mathbb{S}\text{Bim}}(\h, W)$ to be a right module category of $\mathbb{S}\text{Bim}(\h, W),$ furnished by 
 $$(-) \otimes_R (-): \overline{\mathbb{S}\text{Bim}}(\h, W) \times \mathbb{S}\text{Bim}(\h, W) \longrightarrow \overline{\mathbb{S}\text{Bim}}(\h, W). $$
 Thus we take the split Grothendieck group $[\overline{\mathbb{S}\text{Bim}}(\h, W)]_\oplus$ to be a right $[\mathbb{S}\text{Bim}(\h, W)]_\oplus$-module. 
 
 
\subsubsection{}
 Now we can introduce the climax of our tale: proof that Soergel's conjecture implies the Kazhdan-Lusztig conjecture. Following from [Elias et. al],
