---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-004-23-invariant
section_title: "Invariant"
section_number: 2.3
pages: 5-8
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.932
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
Let $(R,\mu,a,b)$ be an enhanced Yang--Baxter operator on an $N$-dimensional vector space $V$.

::: definition
For an $n$-braid $\beta$, we define $T_{(R,\mu,a,b)}(\beta)\in\mathbb{C}$ by the following formula. $$T_{(R,\mu,a,b)}(\beta)
  :=
  a^{-w(\beta)}
  b^{-n}
  \operatorname{Tr}_1
  \Bigl(
    \operatorname{Tr}_2
    \bigl(
      \cdots
      \left(
        \operatorname{Tr}_n\left(\Phi(\beta)\mu^{\otimes n}\right)
      \right)
      \cdots
    \bigr)
  \Bigr),$$ where $w(\beta)$ is the sum of the exponents in $\beta$. Note that $\operatorname{Tr}_1\colon\operatorname{End}(V)\to\mathbb{C}$ is the usual trace.
:::

::: example
For the braid $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$, we have $$\begin{gathered}
  T_{(R,\mu,a,b)}(\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1})
  \\
  =
  b^{-2}
  \operatorname{Tr}_1\bigl(\operatorname{Tr}_2(\operatorname{Tr}_3(
  (R\otimes\operatorname{Id}_V)(\operatorname{Id}_V\otimes R^{-1})(R\otimes\operatorname{Id}_V)(\operatorname{Id}_V\otimes R^{-1})
  (\mu\otimes\mu\otimes\mu)))\bigr)
\end{gathered}$$ since $w(\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1})=+1-1+1-1=0$ (Figure [1](#fig:fig_8_invariant){reference-type="ref" reference="fig:fig_8_invariant"}).

<figure id="fig:fig_8_invariant">
<p><span class="math inline">⇒</span><span class="math inline"><em>a</em><sup>−<em>w</em>(<em>β</em>)</sup><em>b</em><sup>−<em>n</em></sup>×</span></p>
<figcaption>A braid and its invariant</figcaption>
</figure>
:::

We can show that $T_{(R,\mu,a,b)}$ gives a link invariant.

::: theorem
If $\beta$ and $\beta'$ present the same link, then $T_{R,\mu,a,b}(\beta)=T_{R,\mu,a,b}(\beta')$.
:::

::: proof
*Sketch of a proof.* By Markov's theorem (Theorem [\[thm:Markov\]](#thm:Markov){reference-type="ref" reference="thm:Markov"}) it is sufficient to prove that $T_{R,\mu,a,b}$ is invariant under a braid relation, a conjugation and a stabilization.

The invariance under a braid relation $\sigma_i\sigma_{i+1}\sigma_i=\sigma_{i+1}\sigma_i\sigma_{i+1}$ follows from Figure [2](#fig:braid_relation_YB){reference-type="ref" reference="fig:braid_relation_YB"}. Note that the left hand side depicts a braid relation [\[eq:braid_presentation\]](#eq:braid_presentation){reference-type="eqref" reference="eq:braid_presentation"} and the right hand side depicts the corresponding Yang--Baxter equation (Definition [\[def:YB\]](#def:YB){reference-type="ref" reference="def:YB"} (1)).

<figure id="fig:braid_relation_YB">
<p><span class="math inline">$\underset{\text{\raisebox{-1mm}{Yang--Baxter equation}}}
    {\includegraphics[scale=0.3]{YB1_small.eps}
     \quad\raisebox{16mm}{=}\quad
     \includegraphics[scale=0.3]{YB2_small.eps}}$</span></p>
<figcaption>braid relation corresponds to the Yang–Baxter equation</figcaption>
</figure>

The invariance under a conjugation follows from Figure [3](#fig:invariance_conjugation){reference-type="ref" reference="fig:invariance_conjugation"}. The first equality follows since $\operatorname{Tr}_k$ is invariant under a conjugation. The second equality follows since $(\mu\otimes\mu)R=R(\mu\otimes\mu)$ (Definition [\[def:YB\]](#def:YB){reference-type="ref" reference="def:YB"} (2)). Note that the equality $(\mu\otimes\mu)R=R(\mu\otimes\mu)$ means that a pair $\mu\otimes\mu$ can pass through a crossing.

<figure id="fig:invariance_conjugation">
<p><embed src="conjugate_R_abm_small.eps" /> <embed src="conjugate_R_bma_small.eps" /> <embed src="conjugate_R_bam_small.eps" /></p>
<figcaption>invariance under a conjugation</figcaption>
</figure>

To prove the invariance under a stabilization, we first note that if a homomorphism $f\colon V^{\otimes n}\to V^{\otimes n}$ given by $$f(e_{i_1}\otimes\dots\otimes e_{i_n})
  =
  \sum_{j_1,\dots,j_n=0}^{N-1}
  f_{i_1,\dots,i_n}^{j_1,\dots,j_n}(e_{j_1}\otimes\dots\otimes e_{j_n}),$$ then its $n$-fold trace is given by $$\operatorname{Tr}_1(\cdots(\operatorname{Tr}_{n}(f))\cdots)
  =
  \sum_{j_1,\dots,j_n}f_{j_1,\dots,j_n}^{j_1,\dots,j_n}.$$ Therefore if $g$ is a homomorphism $g\colon V\otimes V\to V\otimes V$ given by $g_{l_1,l_2}^{k_1,k_2}$, then we have $$\begin{gathered}
  \operatorname{Tr}_1
  \left(\cdots
    \left(\operatorname{Tr}_n
      \left(\operatorname{Tr}_{n+1}
        \bigl(
          (f\otimes\operatorname{Id}_V)(\operatorname{Id}_V^{\otimes(n-1)}\otimes g)
        \bigr)
      \right)
    \right)
  \right)
  \\
  =
  \sum_{j_1,\dots,j_n,k_n,k_{n+1}}
  f_{j_1,\dots,j_{n-1},j_n}^{j_1,\dots,j_{n-1},k_n}
  g_{k_n,k_{n+1}}^{j_n,k_{n+1}},
\end{gathered}$$ which coincides with the $n$-fold trace of the homomorphism $f\bigl(\operatorname{Id}_V^{\otimes(n-1)}\otimes\operatorname{Tr}_2(g)\bigr)\colon V^{\otimes n}\to V^{\otimes n}$.

Therefore for $\beta\in B_n$ we have $$\begin{split}
  &\operatorname{Tr}_1
  \Biggl(
    \operatorname{Tr}_2
    \biggl(
      \cdots
      \Bigl(
        \operatorname{Tr}_n
        \left(
          \operatorname{Tr}_{n+1}\left(\Phi(\beta\sigma_n^{\pm1})\mu^{\otimes(n+1)}\right)
        \right)
      \Bigr)
      \cdots
    \biggr)
  \Biggr)
  \\
  =&
  \operatorname{Tr}_1
  \Biggl(
    \operatorname{Tr}_2
    \biggl(
      \cdots
      \Bigl(
        \operatorname{Tr}_n
        \left(
          \operatorname{Tr}_{n+1}
          \left(
            (\mu^{\otimes n}\Phi(\beta)\otimes\operatorname{Id}_V)
            (\operatorname{Id}_V^{\otimes(n-1)}\otimes R^{\pm1}(\operatorname{Id}_V\otimes\mu))
          \right)
        \right)
      \Bigr)
      \cdots
    \biggr)
  \Biggr)
  \\
  =&
  \operatorname{Tr}_1
  \Biggl(
    \operatorname{Tr}_2
    \biggl(
      \cdots
      \Bigl(
        \operatorname{Tr}_n
        \left(
            (\mu^{\otimes n}\Phi(\beta))
            (\operatorname{Id}_V^{\otimes(n-1)}\otimes\operatorname{Tr}_2(R^{\pm1}(\operatorname{Id}_V\otimes\mu)))
        \right)
      \Bigr)
      \cdots
    \biggr)
  \Biggr)
  \\
  =&
  a^{\pm1}b
  \operatorname{Tr}_1
  \Biggl(
    \operatorname{Tr}_2
    \biggl(
      \cdots
      \Bigl(
        \operatorname{Tr}_n
        \left(
            (\mu^{\otimes n}\Phi(\beta))
        \right)
      \Bigr)
      \cdots
    \biggr)
  \Biggr)
  \\
  =&
  a^{\pm1}b
  \operatorname{Tr}_1
  \Biggl(
    \operatorname{Tr}_2
    \biggl(
      \cdots
      \Bigl(
        \operatorname{Tr}_n
        \left(
            (\Phi(\beta)\mu^{\otimes n})
        \right)
      \Bigr)
      \cdots
    \biggr)
  \Biggr),
\end{split}$$ since $\operatorname{Tr}_2\bigl(R^{\pm1}(\operatorname{Id}_V\otimes\mu\bigr)=a^{\pm1}b\operatorname{Id}_V$ (Definition [\[def:YB\]](#def:YB){reference-type="ref" reference="def:YB"} (3)) as depicted in Figure [4](#fig:invariance_stabilization){reference-type="ref" reference="fig:invariance_stabilization"}.

<figure id="fig:invariance_stabilization">
<p><embed src="stabilize_R2_small.eps" /> <embed src="stabilize_R3_small.eps" /></p>
<figcaption>invariance under a stabilization</figcaption>
</figure>

Since $w(\beta\sigma_n^{\pm1})=w(\beta)\pm1$, the invariance under a stabilization follows. ◻
:::

Therefore we can define a link invariant $T_{R,\mu,a,b}(L)$ to be $T_{R,\mu,a,b}(\beta)$ if $L$ is the closure of $\beta$.
