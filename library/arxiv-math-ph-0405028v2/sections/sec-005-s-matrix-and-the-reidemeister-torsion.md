---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-005-s-matrix-and-the-reidemeister-torsion
section_title: "S-matrix and the Reidemeister Torsion"
section_number: null
pages: 17-20
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.98
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshetikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ(p1, p2, p3)"
---
[]{#sec:torsion label="sec:torsion"}

An asymptotic behavior of the Witten invariant $Z_k(\mathcal{M})$ can be given from the definition [\[Witten_and_tau\]](#Witten_and_tau){reference-type="eqref" reference="Witten_and_tau"}. In a large $N$ limit, the first term in eqs. [\[tau_limit\]](#tau_limit){reference-type="eqref" reference="tau_limit"} and [\[tau_Poincare_limit\]](#tau_Poincare_limit){reference-type="eqref" reference="tau_Poincare_limit"} dominate an asymptotic behavior of the quantum invariant, which will be shown to denote a contribution from flat connections. We obtain the following;

::: coro
We have an asymptotic behavior of the Witten invariant [\[Witten\]](#Witten){reference-type="eqref" reference="Witten"} for the Brieskorn homology spheres in $N\to\infty$ as $$\begin{gathered}
    Z_{N-2}\bigl( \Sigma(p_1,p_2, p_3) \bigr)
    \\
    \sim
    \frac{1}{2} \, \mathrm{e}^{-\frac{3}{4} \pi \mathrm{i}} \,
    \mathrm{e}^{-\frac{\phi(p_1,p_2,p_3)}{2 N} \pi \mathrm{i}}
    \,
    \sum_{\ell_1, \ell_2, \ell_3}
    \Bigl(
    \sqrt{2} \, \mathbf{S}_{1,1,1}^{\ell_1, \ell_2, \ell_3}
    \Bigr) \,
    \mathrm{e}^{-\frac{P}{2}
      \left(
        1+ \sum_{j=1}^3 \frac{\ell_j}{p_j}
      \right)^2 
      \pi \mathrm{i} N
    }
  
\end{gathered}$$ where the $\mathbf{S}$-matrix is defined in eq. [\[S_transformation\]](#S_transformation){reference-type="eqref" reference="S_transformation"}, and the sum runs over $\gamma(p_1,p_2,p_3)$ distinct triples satisfying eq. [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"}.
:::

We see that, except a decaying factor $\mathrm{e}^{-\frac{\phi(p_1,p_2,p_3)}{2 N} \pi  \mathrm{i}}$, our result proves eq. [\[asymptotic_Witten\]](#asymptotic_Witten){reference-type="eqref" reference="asymptotic_Witten"} exactly as we have seen that a dominating exponential factor denotes the Chern--Simons invariant [\[CS_B\]](#CS_B){reference-type="eqref" reference="CS_B"} for the Brieskorn homology spheres.

In fact we can establish a relationship among the $\mathbf{S}$-matrix, the Reidemeister torsion, and the spectral flow;

::: theorem
$$\label{S_and_torsion}
    \sqrt{2} \,
    \mathbf{S}_{1,1,1}^{\ell_1, \ell_2, \ell_3}
    =
    \sqrt{T_\alpha} \,
    \mathrm{e}^{-2 \pi \mathrm{i}  I_\alpha/4}$$ where the triple $(\ell_1,\ell_2,\ell_3)$ satisfies eq. [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"}.
:::

::: proof
*Proof.* A proof of the absolute value of $\sqrt{2} \,
\mathbf{S}_{1,1,1}^{\ell_1,\ell_2,\ell_3}$ is straightforward since it is known [@DFreed92a] that the Reidemeister torsion of the Brieskorn homology sphere is given by $$\sqrt{T_\alpha}
  =
  \frac{8}{\sqrt{P}} \,
  \prod_{j=1}^3
  \left|
    \sin \Bigl(
    P \,
    \frac{\ell_j}{p_j^{~2}}
    \Bigr)
  \right|$$

To prove a part of the phase factor, we recall that the spectral flow of the Brieskorn homology spheres is given by [@FintuStern90a] $$\begin{gathered}
  I_\alpha
  =
  -3 - 
  \Biggl(
    \frac{2 \,
      \bigl(e (\ell_1, \ell_2, \ell_3) \bigr)^2
    }{P}
    \\
    +
    \sum_{j=1}^3
    \frac{2}{p_j} \,
    \sum_{k=1}^{p_j-1}
    \cot
    \Bigl( \frac{k \, P  \, \pi}{p_j^{~2}} \Bigr) \,
    \cot
    \Bigl( \frac{k \, \pi}{p_j} \Bigr) \,
    \sin^2
    \Bigl( \frac{k \,
      e(\ell_1, \ell_2, \ell_3)
      \, \pi}{p_j} \Bigr) 
  \Biggr)
  \mod 8
  \label{spectral}
\end{gathered}$$ where $$e \equiv
  e(\ell_1,\ell_2, \ell_3)
  = P \sum_{j=1}^3 \frac{p_j - \ell_j}{p_j}$$

Using this we have $$\begin{aligned}
  \mathrm{e}^{-2 \pi \mathrm{i} I_\alpha/4}
  & =
  \mathrm{e}^{\frac{\pi \mathrm{i}}{2}
    \left( 3 + 2 \frac{e^2}{P} \right)
  } \,
  \prod_{j=1}^3 \exp
  \left(
    \frac{\pi \mathrm{i}}{2} \cdot
    \frac{2}{p_j}
    \sum_{k=1}^{p_j-1}
    \cot
    \left(
      \frac{k \, P \, \pi}{p_j^{~2}}  
    \right)
    \cot
    \left(
      \frac{k \, \pi}{p_j}
    \right)
    \sin^2
    \left(
      \frac{k \, e \, \pi}{p_j} 
    \right)
  \right)
  \\
  & =
  \mathrm{e}^{\pi \mathrm{i} e}
  \,
  \prod_{j=1}^3
  \mathop{\mathrm{sign}}
  \left(
    \sin \left( \frac{q_j \, e \, \pi}{p_j}  \right)
    \,
    \sin \left( \frac{ e \, \pi}{p_j}  \right)
  \right)
\end{aligned}$$ Here in the second equality we have used $\frac{P}{p_j} \cdot q_j =1 \pmod {p_j}$, and an identity [@LCJeff92a; @Rozan95a], $$\begin{gathered}
  -\mathrm{i} \,
  \mathop{\mathrm{sign}}
  \left(
    \sin \left(\frac{r \, n \, \pi}{p}\right) \,
    \sin \left(\frac{n \, \pi}{p}      \right)
  \right) \,
  \mathrm{e}^{\pi \mathrm{i} n}
  \\
  =
  \exp\left(
    -\frac{\pi \mathrm{i}}{2} \,
    \left(
      -2 + \frac{2 \, r \, n^2}{p}
      +
      \frac{2}{p}
      \sum_{k=1}^{p-1}
      \cot \left(\frac{k \, q \, \pi}{p}\right) \,
      \cot \left(\frac{k \, \pi}{p}\right) \,
      \sin^2 \left(\frac{k \, n \, \pi}{p}\right) 
    \right)
  \right)
\end{gathered}$$ where we suppose $n\in\mathbb{Z}$ and $q \, r =1 \pmod p$. We further see that $$\prod_{j=1}^3 
  \sin \left(
    \frac{ e \, \pi}{p_j}
  \right)
  =
  (-1)^{1 + 
    \sum_{j <k}
    \left(
      p_j p_k + \ell_j p_k + p_j \ell_k
    \right)
  }
  \prod_{j=1}^3
  \sin\left(
    \pi \, P \, \frac{\ell_j}{p_j^{~2}}
  \right)$$ and $$\begin{aligned}
  \prod_{j=1}^3 
  \mathop{\mathrm{sign}}\left(
    \sin \left(
      \frac{q_j \, e \, \pi}{p_j}
    \right)
  \right)
  & =
  1
\end{aligned}$$ which follows from $$\begin{aligned}
  \sin \left( \frac{ q_1 \, e \, \pi}{p_1} \right)
  & =
  (-1)^{1 + q_1 ( p_2 p_3 + \ell_2 p_3 + p_2\ell_3)} 
  \sin\left(
    \pi \, \frac{\ell_1}{p_1}
    \cdot  q_1  \, \frac{P}{p_1} 
  \right)
  \\
  & =
  (-1)^{1+  q_1 ( p_2 p_3 + \ell_2 p_3 + p_2\ell_3) 
    -\ell_1 (p_2 q_3 + q_2 p_3)} \,
  \sin
  \left(
    \frac{\ell_1 \, \pi}{p_1}
  \right)
\end{aligned}$$ Collecting these results, we obtain $$\mathrm{e}^{-2 \pi \mathrm{i} I_\alpha/4}
  =
  (-1)^{
    1+ P + P \sum_{j=1}^3 \frac{\ell_j}{p_j}
    +
    \sum_{j<k}
    \left(
      p_j p_k + \ell_j p_k + p_j \ell_k
    \right)
  } \,
  \prod_{j=1}^3
  \mathop{\mathrm{sign}}
  \left(
    \sin
    \left(
      \frac{ P \, \ell_j \, \pi}{p_j^{~2}}
    \right)
  \right)$$ which proves a phase factor of eq. [\[S_and_torsion\]](#S_and_torsion){reference-type="eqref" reference="S_and_torsion"}. ◻
:::

We reconsider some examples from section [\[sec:WRT\]](#sec:WRT){reference-type="ref" reference="sec:WRT"};

-   the Poincaré homology sphere $\Sigma(2,3,5)$:

    We have two triples $(\ell_1, \ell_2, \ell_3)
      =(1,1,1)$ and $(1,1,2)$. These respectively give the spectral flow [\[spectral\]](#spectral){reference-type="eqref" reference="spectral"} $I_\alpha = 4$ and $0$, which supports eq. [\[tau_Poincare_limit\]](#tau_Poincare_limit){reference-type="eqref" reference="tau_Poincare_limit"}.

-   $\Sigma(2,3,7)$:

    We have $(\ell_1, \ell_2, \ell_3)
      =
      (1,1,2)$ and $(1,1,3)$, which give $I_\alpha = 6$ and $2$ respectively. This is consistent with a result in previous section.

-   $\Sigma(3,4,5)$:

    We have four triples $(\ell_1, \ell_2, \ell_3)
      =(1,1,3),
      (1,1,4),
      (1,2,1)$, and $(1,2,2)$. For these irreducible representations, we get from eq. [\[spectral\]](#spectral){reference-type="eqref" reference="spectral"} $I_\alpha = 2, 4, 6,$ and $0$. This result is consistent with an asymptotic expansion given before.
