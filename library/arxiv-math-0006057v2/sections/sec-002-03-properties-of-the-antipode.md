---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-002-03-properties-of-the-antipode
section_title: "Properties of the antipode"
section_number: 0.3
pages: 5-7
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.928
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
The properties of the antipode of a quantum groupoid are similar to those of a finite-dimensional Hopf algebra.

::: proposition
[]{#properties of S label="properties of S"} The antipode $S$ is unique and bijective. Also, it is both algebra and coalgebra anti-homomorphism.
:::

::: proof
*Proof.* Let $f*g = m(f\otimes g)\Delta$ be the convolution of $f,g \in 
\mbox{End}_k(H)$. Then $S*\mbox{id}=\varepsilon_s,\, \mbox{id}*S=\varepsilon_t$, and $S*\mbox{id}*S=S$. If $S'$ is another antipode of $H$ then $$S' = S' *\mbox{id}* S' = S' *\mbox{id}* S = S*\mbox{id}*S=S.$$ To check that $S$ is an algebra anti-homomorphism, we compute $$\begin{aligned}
S(1) 
&=& S(1_{(1)})1_{(2)}S(1_{(3)})= S(1_{(1)})\varepsilon_t(1_{(2)}) =\varepsilon_t(1) =1, \\
S(hg) 
&=& S(h_{(1)}g_{(1)})\varepsilon_t(h_{(2)}g_{(2)}) = S(h_{(1)}g_{(1)}) h_{(2)} \varepsilon_t(g_{(2)}) S(h_{(3)}) \\
&=& \varepsilon_s(h_{(1)}g_{(1)})S(g_{(2)})S(h_{(2)}) = S(g_{(1)}) \varepsilon_s(h_{(1)}) \varepsilon_t(g_{(2)}) S(h_{(2)}) 
   = S(g)S(h),
\end{aligned}$$ for all $h,g\in H$, where we used Proposition [\[counital properties\]](#counital properties){reference-type="ref" reference="counital properties"}(iv) and easy identities $\varepsilon_t(hg) = \varepsilon_t(h\varepsilon_t(g))$ and $\varepsilon_s(hg) = \varepsilon_t(\varepsilon_s(h)g)$. Dualizing the above arguments we show that $S$ is also a coalgebra anti-homomorphism : $$\begin{aligned}
\varepsilon(S(h))
&=& \varepsilon(S(h_{(1)})\varepsilon_t(h_{(2)})) = \varepsilon(S(h_{(1)})h_{(2)}) =\varepsilon(\varepsilon_t(h)) =\varepsilon(h),\\
\Delta(S(h))
&=& \Delta(S(h_{(1)})\varepsilon_t(h_{(2)}))\\
&=& \Delta(S(h_{(1)})) (\varepsilon_t(h_{(2)}) \otimes 1) \\
&=& \Delta(S(h_{(1)})) (h_{(2)} S(h_{(4)}) \otimes \varepsilon_t(h_{(3)})) \\
&=& \Delta(\varepsilon_s(h_{(1)})) ( S(h_{(3)}) \otimes S(h_{(2)}) ) \\
&=& S(h_{(3)}) \otimes \varepsilon_s(h_{(1)})S(h_{(2)}) = S(h_{(2)}) \otimes S(h_{(1)}). 
\end{aligned}$$ The proof of the bijectivity of $S$ can be found in ([@BNSz], 2.10). ◻
:::

Next, we investigate the relations between the antipode and counital maps.

::: proposition
[]{#S and counital maps label="S and counital maps"} We have $S\circ \varepsilon_s = \varepsilon_t\circ S$ and $\varepsilon_s\circ S = S\circ \varepsilon_t$. The restriction of $S$ defines an algebra anti-isomorphism between counital subalgebras $H_t$ and $H_s$.
:::

::: proof
*Proof.* Using results of Proposition [\[properties of S\]](#properties of S){reference-type="ref" reference="properties of S"} we compute $$S(\varepsilon_s(h)) = S(1_{(1)}) \varepsilon(h1_{(2)}) = \varepsilon(1_{(1)}S(h))1_{(2)} =\varepsilon_t(S(h)),$$ for all $h\in H$. The second identity is proven similarly. Clearly, $S$ maps $H_t$ to $H_s$ and vice versa. Since $S$ is bijective, and $\dim H_t =\dim H_s$ by Proposition [\[base properties\]](#base properties){reference-type="ref" reference="base properties"}, therefore $S|_{H_t}$ and $S|_{H_s}$ are anti-isomorphisms. ◻
:::

::: proposition
[]{#full subcategory label="full subcategory"} Any nonzero morphism $\alpha :H \to K$ of quantum groupoids preserves counital subalgebras, i.e. $H_t \cong K_t$ and $H_s \cong K_s$. Thus, quantum groupoids with a given target (source) counital subalgebra form a full subcategory.
:::

::: proof
*Proof.* It is clear that $\alpha|_{H_t} : H_t \to K_t$ is a homomorphism. If we write $$\Delta(1_H) = \sum_{i=1}^n\, w_i\otimes z_i$$ with $\{ w_i\}_{i=1}^n$ and $\{ z_i\}_{i=1}^n$ linearly independent, then $\Delta(1_K) = \sum_{i=1}^n\, \alpha(w_i)$ $\otimes \alpha(z_i)$. By Proposition [\[base properties\]](#base properties){reference-type="ref" reference="base properties"}, $K_t =\mbox{span}\{\alpha(z_i)\}$, i.e., $\alpha|_{H_t}$ is surjective. Since $$z_j = \varepsilon_t(z_j) = \sum_{i=1}^n\, \varepsilon(w_iz_j)z_i,$$ then $\varepsilon(w_iz_j) =\delta_{ij}$, therefore, $$\begin{aligned}
\dim H_t  
&=& n = \sum_{i=1}^n\,\varepsilon_H(w_i z_i) =  \sum_{i=1}^n\,\varepsilon_H(w_i S(z_i)) \\
&=& \varepsilon_H(\varepsilon_t(1_H)) = \varepsilon_H(1_H) = \varepsilon_K(1_K) =  \dim K_t,
\end{aligned}$$ so $\alpha|_{H_t}$ is bijective. The proof for source subalgebras is similar. ◻
:::

Let us recall that a $k$-algebra $A$ is said to be *separable* [@P] if the multiplication epimorphism $m: A\otimes_k A \to A$ has a right inverse as an $A-A$ bimodule homomorphism. This is equivalent to the existence of a *separability element* $e\in A\otimes_k A$ such that $m(e) =1$ and $(a\otimes 1)e = e(1\otimes a),\ (1\otimes a)e=e(a\otimes 1)$ for all $a\in A$.

::: proposition
[]{#separability label="separability"} The counital subalgebras $H_t$ and $H_s$ are separable, their separability elements are $e_t = (S \otimes \mbox{id})\Delta(1)$ and $e_s = (\mbox{id}\otimes S)\Delta(1)$, respectively.
:::

::: proof
*Proof.* For all $z\in H_t$ we compute, using Propositions [\[counital properties\]](#counital properties){reference-type="ref" reference="counital properties"} and [\[S and counital maps\]](#S and counital maps){reference-type="ref" reference="S and counital maps"} : $$\begin{aligned}
1_{(1)} S^{-1}(z) \otimes 1_{(2)}
&=& S^{-1}(z)_{(1)} \otimes \varepsilon_t(S^{-1}(z)_{(2)}) \\
&=& 1_{(1)} \otimes \varepsilon_t(1_{(2)}S^{-1}(z)) 
    = 1_{(1)} \otimes \varepsilon_t(1_{(2)}z) = 1_{(1)} \otimes 1_{(2)}z,
\end{aligned}$$ applying $(S\otimes \mbox{id})$ to this identity we get $e_tz =ze_t$. Clearly, $m(e_t)=1$, whence $e_t$ is a separability element. The second statement follows similarly. ◻
:::
