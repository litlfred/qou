---
doc_id: arxiv-math-0409593v1
doc_title: "CATEGORIFICATION OF THE BRAID GROUPS"
section_id: sec-012-51-classical-results
section_title: "Classical results"
section_number: 5.1
pages: 13-14
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.926
---
Let $G$ be a semi-simple complex algebraic group with Weyl group $W$.

Let ${\mathbf{W}}=\{{\mathbf{w}}\}_{w\in W}$. The braid group $B_W$ of $W$ is isomorphic to the group with set of generators ${\mathbf{W}}$ and relations ${\mathbf{w}}{\mathbf{w}}'={\mathbf{w}}'' \text{ when } ww'=w'' \text{ and }l(w'')=l(w)+l(w')$.

Let ${\mathcal{B}}$ be the flag variety of $G$. We decompose $${\mathcal{B}}\times{\mathcal{B}}=\coprod_{w\in W}{\mathcal{O}}(w)$$ into orbits for the diagonal $G$-action. Consider the first and second projections $$\xymatrix{
 & {\mathcal{O}}(w) \ar[dl]_{p_w} \ar[dr]^{q_w} \\
{\mathcal{B}}& & {\mathcal{B}}
}$$ Then, we have a functor $$F_{{\mathbf{w}}}=R(p_w)_! (q_w)^*:D^b({\mathcal{B}})\to D^b({\mathcal{B}})$$ where $D^b({\mathcal{B}})$ is the derived category of bounded complexes of constructible sheaves of ${\mathbf{C}}$-vector spaces over ${\mathcal{B}}$.

First and last projections induce an isomorphism $${\mathcal{O}}(w)\times_{{\mathcal{B}}}{\mathcal{O}}(w')\buildrel \sim\over\to{\mathcal{O}}(ww') \text{ when } l(ww')=l(w)+l(w').$$ This induces an isomorphism (cf §[\[noyaux\]](#noyaux){reference-type="ref" reference="noyaux"}) $$\gamma_{w,w'}:F_{{\mathbf{w}}} F_{{\mathbf{w}}'}\buildrel \sim\over\to F_{{\mathbf{w}}{\mathbf{w}}'} \text{ when }
l(ww')=l(w)+l(w').$$

For $s\in S$, then $F_{\mathbf{s}}$ is obtained as in §[\[P1\]](#P1){reference-type="ref" reference="P1"} for the canonical morphism $\pi_s:{\mathcal{B}}\to{\mathcal{P}}_s$, where ${\mathcal{P}}_s$ is the variety of parabolic subgroups of type $s$. So, $F_{\mathbf{s}}$ is invertible, with inverse $F_{{\mathbf{s}}^{-1}}=R(p_s)_*(q_s)^!$. It follows that $F_{{\mathbf{w}}}$ is invertible for $w\in W$, with inverse $F_{{\mathbf{w}}^{-1}}=R(p_w)_*(q_w)^!$, hence we get a morphism from $B_W$ to the group of isomorphism classes of invertible functors on $D^b({\mathcal{B}})$.
