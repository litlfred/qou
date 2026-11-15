---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-006-15-quantization
section_title: "Quantization"
section_number: 1.5
pages: 5-5
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.973
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
[]{#subsec:goquant label="subsec:goquant"} Going quantum, bracket $_\downarrow$ ought to become Weyl-style exchange relations $$u_mu_n=q^{2(\delta_{m+1,n}
  -\delta_{m-1,n})}u_nu_m\;.$$ We do not want to discuss before time the nature of quantization constant $q$ or the exact degree of formality implied in what follows, but we want to be very clear about boundary conditions: the $u$'s are strictly periodic and so is the Kronecker symbol of course $$u_{n+N}=u_n\qquad\qquad\delta_{m,n}
=\begin{cases}1&\text{if }m\equiv n\pmod{N}\\
  0&\text{otherwise,}\end{cases}$$ on top of that, for the reason to surface shortly, we want period $N$ to be even and an additional condition $$\label{eq:c1c2}
u_1u_3\ldots u_{N-1}=u_2u_4\ldots u_N$$ to be met, it makes sense because the elements in both sides are central. With all this in place, the following relation $$\hat u_n=u_{n-1}=Q^{-1}u_nQ,$$ with $$Q=b_1b_2\ldots b_{N-1}\qquad\qquad
b_n=\sum_{a=-\infty}^\infty q^{a^2}u_n^a\;,$$ proves to hold for all $n\in\mathbb Z$. So, with automorphism $\hat{}:u_n\mapsto u_{n-1}$ interpreted as a jump in time, the above relation replaces the (lower) Volterra system with a free and fully discrete Heisenberg quantum motion, employing the element $Q$ as an "evolution operator".
