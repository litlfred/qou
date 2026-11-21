---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-013-35-an-analytic-extension-of-the-colored-jones-po
section_title: "An analytic extension of the colored Jones polynomial"
section_number: 3.5
pages: 35-36
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.64
latex_coverage_ratio: 0.92
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sub.CJ41analytic label="sub.CJ41analytic"}

In this section we discuss a Borel resummation formula for the colored Jones polynomial of the $\mathbf{4}_1$ knot. The latter is defined by $$J^{\mathbf{4}_1}_N(q) = \sum_{k=0}^{N-1}(-1)^k
  q^{-k(k+1)/2}(q^{1+N};q)_k(q^{1-N};q)_k \,.$$ Let $u \sim 0$ be in a small neighborhood of the origin in the complex plane. It is related to $x = q^N$ and $\tau$ by $$x = {\rm e}^{u},\quad \tau = \frac{u}{2\pi{\rm i}N}+\frac{1}{N}.
  \label{eq:x-n-tau}$$ Then $u$ is near $0$, then $x$ is close to $1$, which is the regime that we studied in Section [\[sub.41borelx\]](#sub.41borelx){reference-type="ref" reference="sub.41borelx"}, and $\tau$ is close to $1/N$. Note that $N\tau = 1+\frac{u}{2\pi{\rm i}}$ is the analogue of $n/k$ in [@gukov], and here we are considering a deformation from the case of $n/k=1$.

Experimentally, we found that in cones $I$ and $IV$ respectively, we have $$\begin{align}
    J^{\mathbf{4}_1}_N(q) =
    &s_{I}(\Phi^{(\sigma_0)})(x;\tau)
      +\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}
      \tau^{-1/2}s_{I}(\Phi^{(\sigma_1)})(x;\tau)
      \nonumber \\
    &-(1+\tilde{x})\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}\tau^{-1/2}
      s_{I}(\Phi^{(\sigma_2)})(x;\tau)
      \label{eq:Jn-s1}
    \\=
    &s_{IV}(\Phi^{(\sigma_0)})(x;\tau)
      +\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}
      \tau^{-1/2}s_{IV}(\Phi^{(\sigma_1)})(x;\tau)\nonumber \\
    &+(1+\tilde{x}^{-1})\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}\tau^{-1/2}
      s_{IV}(\Phi^{(\sigma_2)})(x;\tau)
      \label{eq:Jn-s2}
  \end{align}$$ where $\tilde{x}=e^{u/\tau}=e^{2\pi{\rm i}N u/(u+2\pi{\rm i})}$. This, together with Conjecture [\[conj-exact-regions\]](#conj-exact-regions){reference-type="ref" reference="conj-exact-regions"} implies $$\begin{aligned}
  J^{\mathbf{4}_1}_N(q) =
  &s_{\text{med}}(\Phi^{(\sigma_0)})(x;\tau)
    +\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}
    \tau^{-1/2}s_{\text{med}}(\Phi^{(\sigma_1)})(x;\tau)\nonumber \\
  &-\frac{\tilde{x}-\tilde{x}^{-1}}{2}\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}
    \tau^{-1/2}s_{\text{med}}(\Phi^{(\sigma_2)})(x;\tau) ,
  \label{eq:Jn-smed}
\end{aligned}$$ which is Conjecture [\[conj.ejones\]](#conj.ejones){reference-type="ref" reference="conj.ejones"} for the $\mathbf{4}_1$ knot.

We now make several consistency checks of the above conjecture. The first is that equation [\[eq:Jn-smed\]](#eq:Jn-smed){reference-type="eqref" reference="eq:Jn-smed"} is invariant under complex conjugation which moves $\tau$ from cone $I$ to cone $IV$. The second is that the conjecture implies the Generalised Volume Conjecture. Indeed, in the limit $$N\rightarrow \infty, \quad \tau \rightarrow 0, \quad \log(x) =
    2\pi{\rm i}N\tau \text{ finite}$$ the right hand side of [\[eq:Jn-s1\]](#eq:Jn-s1){reference-type="eqref" reference="eq:Jn-s1"},[\[eq:Jn-s2\]](#eq:Jn-s2){reference-type="eqref" reference="eq:Jn-s2"} are dominated by the first term. If we keep only the exponential, this is the generalised Volume Conjecture [@Murakami2011:ivc; @gukov]. Recall from [@Murakami2011:ivc], the generalised Volume Conjecture reads, for $u$ in a small neighborhood of origin such that $u\not\in \pi{\rm i}\mathbb{Q}$, $$\lim_{N\rightarrow \infty}\frac{\log
      J_N^{K}(\exp((u+2\pi{\rm i})/N))}{N}
    = \frac{H(y,x)}{u+2\pi{\rm i}},
    \label{eq:gVC}$$ where $x = \exp(u+2\pi{\rm i})$ and $H(y,x) = \mathrm{Li}_2(1/(xy)) - \mathrm{Li}_2(y/x) + \log(x)\log(y)$, with $y$ a solution to $y+y^{-1} = x+x^{-1}-1$. By the identification $u + 2\pi{\rm i}= 2\pi{\rm i}(N\tau) \sim 2\pi{\rm i}$, and since $A(x)$ is identical with $H(y,x)$ (up to $\pm 1$), one can check that [\[eq:Jn-s1\]](#eq:Jn-s1){reference-type="eqref" reference="eq:Jn-s1"},[\[eq:Jn-s2\]](#eq:Jn-s2){reference-type="eqref" reference="eq:Jn-s2"} imply [\[eq:gVC\]](#eq:gVC){reference-type="eqref" reference="eq:gVC"}.

# The $\mathbf{5}_2$-knot {#sec.52}

## A $3 \times 3$ matrix of $q$-series {#sub.52q3}

The trace field of the $\mathbf{5}_2$ knot is the cubic field of discriminant $-23$, with a distinguished complex embedding $\sigma_1$ (corresponding to the geometric representation of $\mathbf{5}_2$), its complex conjugate $\sigma_2$ and a real embedding $\sigma_3$. The $\mathbf{5}_2$ knot has three boundary parabolic representations whose associated asymptotic series $\varphi^{(\sigma_j)}(h)$ for $j=1,2,3$ correspond to the three embeddings of the trace field. In [@GGM:resurgent] these asymptotic series were discussed, and a $3 \times 3$ matrix $\mathbf J^\mathrm{red}_m(q)$ of $q$-series was constructed to describe the resurgence properties of the asymptotic series. The matrix $\mathbf J^\mathrm{red}_m(q)$ is a fundamental solution to the linear $q$-difference equation [@GGM:resurgent Eqn.(23)] $$\label{52qdiff}
  f_m(q)-3f_{m+1}(q)+(3-q^{2+m})f_{m+2}(q) - f_{m+3}(q) = 0$$ and it is defined by[^1] $$\label{Jqred52}
\mathbf J^\mathrm{red}_{m}(q) =
\begin{pmatrix}
H_{m}^{(2)}(q) & H_{m+1}^{(2)}(q) & H_{m+2}^{(2)}(q) \\
H_{m}^{(1)}(q) & H_{m+1}^{(0)}(q) & H_{m+2}^{(1)}(q) \\
H_{m}^{(0)}(q) & H_{m+1}^{(0)}(q) & H_{m+2}^{(0)}(q) 
\end{pmatrix},
\qquad (|q| \neq 1)$$ where for $|q|<1$

$$\label{Hpm}
\begin{aligned}
H^{(0)}_{m}(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)+nm}}{(q;q)_n^3}\,,
\\
  H^{(1)}_{m}(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)+nm}}{(q;q)_n^3}
    \left(1+2n+m-3E_1^{(n)}(q)\right) \,,
  \\
  H^{(2)}_{m}(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)+nm}}{(q;q)_n^3}
    \left((1+2n+m-3E_1^{(n)}(q))^2-3E_2^{(n)}(q)-\frac{1}{6}E_2(q)\right) \,,
\end{aligned}$$ and $$\label{Hnm}
\begin{aligned}
  H^{(0)}_{-m}(q^{-1})
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)+nm}}{(q;q)_n^3}\,,
\\
  H^{(1)}_{-m}(q^{-1})
  &=-\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)+nm}}{(q;q)_n^3}
    \left(\frac{1}{2}+n+m-3E_1^{(n)}(q)\right) \,,
  \\
  H^{(2)}_{-m}(q^{-1})
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)+nm}}{(q;q)_n^3}
  \left(\big(\frac{1}{2}+n+m-3E_1^{(n)}(q)\big)^2-3E_2^{(n)}(q)
    -\frac{1}{12}E_2(q)\right) \,.
\end{aligned}$$

[^1]: The matrices $\mathbf J^\mathrm{red}_m(q)$ are related to the Wronskians $W_m(q)$ in [@GGM:resurgent; @GGM:peacock] by $$\mathbf J^\mathrm{red}_m(q) =
        \begin{pmatrix}
          0&0&1\\0&1&0\\1&0&0
        \end{pmatrix} W_m(q)^T.$$
