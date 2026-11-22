---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-006-31-the-hecke-algebra-of-type-a
section_title: "The Hecke Algebra of type $A$"
section_number: 3.1
pages: 9-10
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.724
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempotents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
By the Hecke algebra of type $A_{n-1}$, $H_n(q)$, we mean the free complex algebra with generators $\tilde{g}_1$, ..., $\tilde{g}_{n-1}$ and 1 with parameter $q\in \mathbb{C}$ and defining relations

1.     $\tilde{g}_{i}\tilde{g}_{i+1}\tilde{g}_{i}=\tilde{g}_{i+1}\tilde{g}_{i}\tilde{g}_{i+1}$    for $i=1,2, \ldots, n-2$;

2.     $\tilde{g}_{i}\tilde{g}_{j}= \tilde{g}_{j}\tilde{g}_{i}$,    whenever $\mid i-j \mid \geq 2$;

3.     $\tilde{g}_i^2 = (q-1)\tilde{g}_i +q$     for $i=1,2, \ldots, n-1$;

$H_n(q)$ is semisimple whenever $q$ is not a root of unity. If $\mu \vdash n$, then $(\pi_{\mu}, V_{\mu})$ denotes the irreducible representation of $H_n(q)$ indexed by $\mu$. Here $V_{\mu}$ is the vector space with orthonormal basis given by $\{v_{t^{\mu}}\}$ where $t^{\mu}$ is a standard tableau of shape $\mu$. These representations can be considered as $q$-analogs of Young's orthogonal representations of the Symmetric group (see [@h] or [@w1]). We now describe these representations in more detail. Let $d(t^{\mu},i)=c(i+1)-c(i)-r(i+1)+r(i)$ where $c(i)$ and $r(i)$ denote respectively, the column and row of the box containing the number $i$, and for $d\in \mathbb{Z}\setminus\{0\}$ let $$a_d(q)={q^d(1-q)\over{1-q^d}} \ \ \   \mbox{and} \ \ \  c_d(q)={\sqrt{(1-q^{d+1})(1-q^{d-1})}\over{1-q^d}}.$$ Then one defines $\pi_{\mu}$ on the vector space $V_{\mu}$ by $$\pi_{\mu}(\tilde{g}_{i})v_{t^{\mu}}=a_d(q)v_{t^{\mu}}+c_d(q)v_{\tilde{g}_i(t^{\mu})}$$ where $d=d(t^{\mu},i)$ and $\tilde{g}_i(t^{\mu})$ is the tableau obtained by interchanging $i$ and $i+1$ in $t^{\mu}$. This representation follows from the ones defined in [@w1] by setting $\pi_{\mu}(\tilde{g}_i)=(q+1)\pi_{\mu}(e_i)-Id_{V_{\mu}}$, where $e_i$ is the eigenprojection corresponding to the characteristic value $q$ of $\tilde{g}_i$. Moreover $\pi_n=\bigoplus_{\mu\vdash n}\pi_{\mu}$ is a faithful representation of $H_n(q)$. Thus we have that $H_n(q)\cong \bigoplus_{\mu\vdash n}\pi_{\mu}(H_n(q))$, where $\pi_{\mu}(H_n(q))\cong M_{f^{\mu}}$ and $M_{f^{\mu}}$ is the ring of complex $f^{\mu}\times f^{\mu}$ matrices, and $f^{\mu}$ is the number of standard tableaux of shape $\mu$. If $\mu$ is a partition of $n$ then denote by $\mu'$ the partition obtained by decreasing one part of $\mu$ by one; and $\mu''$ is obtained by decreasing one part of $\mu'$ by one. Let $t^{\mu}$ be a standard tableau of shape $\mu$, then $t^{\mu}\rightarrow (t^{\mu})'$ defines a bijection between $T_{\mu}$ and $\bigcup_{\mu'\subset \mu}T_{\mu'}$, where $(t^{\mu})'$ is the Young tableau obtained by removing the box containing $n$ from $t^{\mu}$. This in turn yields the following isomorphism of modules $$\label{eq:modA}
V_{\mu}{\Big|}_{H_{n-1}(q)}\cong\bigoplus_{\mu'\subset\mu}V_{\mu'}.$$ A special element in $H_f(q)$ is the *full-twist* defined algebraically by $\Delta_f^2:=(\tilde{g}_{f-1}\ldots \tilde{g}_1)^f$. The full-twist is an element in the center of $H_f(q)$. The action of $\Delta_f^2$ on $(\pi_{\nu}, V_{\nu})$ is described in the following lemma, the proof of which appears in [@w2], pg. 261.

::: lemma
[]{#prop:ftr label="prop:ftr"} Let $\nu \vdash f$. Then the full-twist acts by a scalar $\alpha_{\nu}$ on the irreducible representation $(\pi_{\nu},V_{\nu})$ of $H_f(q)$ where $$\alpha_{\nu}=q^{f(f-1)-\sum_{i<j}(\nu_i+1)\nu_j}.$$
:::
