---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-019-47-an-analytic-extension-of-the-kashaev-invarian
section_title: "An analytic extension of the Kashaev invariant and the colored Jones polynomial"
section_number: 4.7
pages: 52-53
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.862
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
In this section we discuss an analytic extension of the Kashaev invariant and of the colored Jones polynomial of the $\mathbf{5}_2$ knot, illustrating Conjectures [\[conj.ekashaev\]](#conj.ekashaev){reference-type="ref" reference="conj.ekashaev"} and [\[conj.ejones\]](#conj.ejones){reference-type="ref" reference="conj.ejones"}.

Recall that the colored Jones polynomial of the $\mathbf{5}_2$ is given by $$J^{\mathbf{5}_2}_N(q) = \sum_{k=0}^{N-1}(-1)^k
  q^{-k(k+1)/2}(q^{1+N};q)_k(q^{1-N};q)_k H_k(q),\quad
  q = {\rm e}^{2\pi{\rm i}\tau},$$ where $$H_k(q) = (-1)^kq^{k(k+3)/2}\sum_{k=0}^\ell q^{\ell(\ell+1)}
  \frac{(q;q)_k}{(q;q)_\ell(q;q)_{k-\ell}}.$$ Let $u$ be in a small neighborhood of the origin. It is related to $x = q^N$ and $\tau$ by $$x = {\rm e}^{u+2\pi{\rm i}} = {\rm e}^{u},\quad \tau = \frac{u+2\pi{\rm i}}{2\pi{\rm i}N}.
  \label{eq:x-n-tau52}$$ Then $x$ is close to $1$ and $\tau$ is close to $1/N$. Note that $$N\tau = 1+\frac{u}{2\pi{\rm i}}$$ is the analogue of $n/k$ in [@gukov], and here we are considering a deformation from the case of $n/k=1$. We also have $$\tilde{x}= {\rm e}^{\log(x)/\tau} =
  \exp\left(\frac{2\pi{\rm i}N u}{u+2\pi{\rm i}}\right).$$ When $x$ is positive real, $\Phi^{(\sigma_1)}(x;\tau)$ are not Borel summable along the positive real axis. Depending on whether $\tau$ is in the first or the fourth quadrant, we have $$\begin{align}
    J^{\mathbf{5}_2}_N(q) =
    s_{I}(\Phi^{(\sigma_0)})(x;\tau)
    +\tau^{-1/2}\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}} 
    \big(
    &s_{I}(\Phi^{(\sigma_1)})(x;\tau)
      -(1+\tilde{x})s_{I}(\Phi^{(\sigma_2)})(x;\tau)\nonumber \\
    &-(1+\tilde{x})s_{I}(\Phi^{(\sigma_3)})(x;\tau)
      \big)
      \label{eq:Jn-s1-52}
    \\  =
    s_{IV}(\Phi^{(\sigma_0)})(x;\tau)  +\tau^{-1/2}
    \frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}} 
    \big(
    &s_{IV}(\Phi^{(\sigma_1)})(x;\tau)
      +(1+\tilde{x}^{-1})s_{IV}(\Phi^{(\sigma_2)})(x;\tau)\nonumber \\
    &-(1+\tilde{x})s_{IV}(\Phi^{(\sigma_3)})(x;\tau)
      \big).
      \label{eq:Jn-s2-52}
    
    
    
    
    
    
    
    
    
    
    \end{align}$$ The two equations [\[eq:Jn-s1-52\]](#eq:Jn-s1-52){reference-type="eqref" reference="eq:Jn-s1-52"}, [\[eq:Jn-s2-52\]](#eq:Jn-s2-52){reference-type="eqref" reference="eq:Jn-s2-52"} are related by the Stokes discontinuity formula $$\text{disc}_0 \Phi^{(\sigma_1)}(x;\tau) =
    s_I(\Phi^{(\sigma_1)})(x;\tau) - s_{IV}(\Phi^{(\sigma_1)})(x;\tau)= 
    (2+\tilde{x}+\tilde{x}^{-1}) s(\Phi^{(\sigma_2)})(x;\tau).$$ Combined, they imply $$\begin{aligned}
\label{52ejones}
  J_N^{\mathbf{5}_2}(q) =
  s_{\text{med}}(\Phi^{(\sigma_0)})(x;\tau)+\tau^{-1/2}
  \frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}} 
  \big(
  &s_{\text{med}}(\Phi^{(\sigma_1)})(x;\tau)
    -(1+\tilde{x})s_{\text{med}}(\Phi^{(\sigma_3)})(x;\tau)\nonumber \\
  &-\frac{\tilde{x}-\tilde{x}^{-1}}{2}s_{\text{med}}(\Phi^{(\sigma_2)})(x;\tau)
    \big) 
\end{aligned}$$ which is the assertion of Conjecture [\[conj.ejones\]](#conj.ejones){reference-type="ref" reference="conj.ejones"}.
