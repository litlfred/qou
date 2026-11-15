---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-004-the-witten--reshetikhin--turaev-invariant-and-th
section_title: "The Witten--Reshetikhin--Turaev Invariant and the Eichler Integral"
section_number: null
pages: 14-17
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.991
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshetikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ(p1, p2, p3)"
---
[]{#sec:WRT label="sec:WRT"}

We have shown that the Eichler integral at $\tau\to N \in \mathbb{Z}$ gives the Chern--Simons invariant of the Brieskorn homology spheres $\Sigma(p_1,p_2,p_3)$. We shall show that the WRT invariant for the Brieskorn homology spheres can be expressed in terms of a limiting value of the Eichler integral at $\tau\to 1/N$ which is given in eq. [\[Eichler_fraction\]](#Eichler_fraction){reference-type="eqref" reference="Eichler_fraction"}.

::: theorem
[]{#theorem:invariant_Eichler label="theorem:invariant_Eichler"} For the Brieskorn homology spheres $\Sigma(p_1,p_2,p_3)$ such that $$\frac{1}{p_1} +     \frac{1}{p_2}+     \frac{1}{p_3} <1$$ we have $$\label{invariant_and_Eichler}
    \mathrm{e}^{
      \frac{2 \pi \mathrm{i}}{N}
      ( \frac{\phi(p_1,p_2,p_3)}{4} - \frac{1}{2} )
    } \,
    \left(
      \mathrm{e}^{\frac{2 \pi \mathrm{i}}{N}} - 1
    \right)
    \,    \tau_N \bigl( \Sigma(p_1, p_2, p_3) \bigr)

    =
    \frac{1}{2} \,
    \widetilde{\Phi}_{\boldsymbol{p}}^{(1,1,1)}(1/N)$$
:::

::: proof
*Proof.* Proof is essentially same with one given in Ref. .

We use the Gauss sum; $$\label{Gauss_sum}
    G(N)=
    \sum_{n=0}^{2  N -1}
    \mathrm{e}^{- \frac{1}{2  N} n^2 \pi \mathrm{i}}
    =
    \sqrt{2 \,  N} \,
    \mathrm{e}^{-\pi \mathrm{i}/4}$$ We see that $$\begin{aligned}
    G(N) &=
    \sum_{k=0}^{2  N-1} \mathrm{e}^{
      -\frac{1}{2  N} (k-n)^2 \pi \mathrm{i}
    }
    \nonumber
    \\
    & =
    \mathrm{e}^{-\frac{1}{2  N} n^2 \pi \mathrm{i}} \,
    \sum_{k=0}^{2  N-1}
    \mathrm{e}^{-\frac{1}{2  N} k^2 \pi \mathrm{i}
      + \frac{1}{ N} k n \pi \mathrm{i}
    }
    \label{Gauss_sum_identity}
  
\end{aligned}$$ These identities follow from the reciprocity formula [\[Gauss_sum_formula\]](#Gauss_sum_formula){reference-type="eqref" reference="Gauss_sum_formula"}.

As we see that $\widetilde{\Phi}_{\boldsymbol{p}}^{(1,1,1)}(1/N)$ is given by eq. [\[Eichler_and_L\]](#Eichler_and_L){reference-type="eqref" reference="Eichler_and_L"}, we have using Prop. [\[prop:L_function\]](#prop:L_function){reference-type="ref" reference="prop:L_function"} as follows; $$\begin{aligned}
    \widetilde{\Phi}_{\boldsymbol{p}}^{(1,1,1)}(1/N)
    & =
    \lim_{t \searrow 0} \sum_{n=0}^\infty
    \chi_{2 P}^{(1,1,1)}(n) \,
    \mathrm{e}^{\frac{1}{2 P N} n^2 \pi \mathrm{i}}  \,
    \mathrm{e}^{- n t}
    \\
    & =
    \lim_{t \searrow 0}
    \frac{1}{G(P \, N)}
    \sum_{n=0}^\infty \sum_{k=0}^{2 P N-1}
    \chi_{2 P}^{(1,1,1)}(n) \,
    \mathrm{e}^{
      -\frac{1}{2 P N} k^2 \pi \mathrm{i} 
      +
      n \left(
        \frac{k}{P N} \pi \mathrm{i} - t
      \right)
    }
  
\end{aligned}$$ where in the second equality we have applied eq. [\[Gauss_sum_identity\]](#Gauss_sum_identity){reference-type="eqref" reference="Gauss_sum_identity"}.

We recall that we have the generating function of the odd periodic function $\chi_{2P}^{(1,1,1)}(n)$ as $$\label{generate_chi_general}
    \frac{
      (z^{p_1 p_2} - z^{-p_1 p_2}) \,
      (z^{p_2 p_3} - z^{-p_2 p_3}) \,
      (z^{p_1 p_3} - z^{-p_1 p_3})
    }{
      z^{p_1 p_2 p_3} - z^{-p_1 p_2 p_3}
    }
    =
    \sum_{n=0}^\infty
    \chi_{2 P}^{(1,1,1)}(n) \, z^{n}$$ Thus we get $$\widetilde{\Phi}_{\boldsymbol{p}}^{(1,1,1)}(1/N)
    =
    \frac{1}{G(P \, N)}
    \sum_{\substack{
        k=0 \\
      N \nmid k
    }}^{2 P N-1}
    \mathrm{e}^{- \frac{1}{2 P N} k^2 \pi \mathrm{i}} \,
    \frac{
      \prod_{j=1}^3
      \left(
        \mathrm{e}^{\frac{k}{N p_j} \pi \mathrm{i}}
        -
        \mathrm{e}^{-\frac{k}{N p_j} \pi \mathrm{i}}
      \right)
    }{
      \mathrm{e}^{\frac{k}{N} \pi \mathrm{i}}
      -
      \mathrm{e}^{ -\frac{k}{N} \pi \mathrm{i}}
    }$$ Here a contribution from the sum over $N \mid k$ is written by use of eq. [\[Gauss_sum_formula\]](#Gauss_sum_formula){reference-type="eqref" reference="Gauss_sum_formula"} as $$\begin{aligned}
    & \lim_{t \searrow 0} \frac{1}{G(P \, N)}
    \sum_{n=0}^\infty \sum_{m \mod 2 P}
    \chi_{2 P}^{(1,1,1)}(n) \,
    \mathrm{e}^{-\frac{N}{2 P} m^2 \pi \mathrm{i}
      +
      \frac{m n}{P} \pi \mathrm{i} - n t
    }
    \\
    & =
    \lim_{t\searrow 0}
    \frac{1}{N}
    \sum_{n=0}^\infty \sum_{k \mod N}
    \chi_{2 P}^{(1,1,1)}(n) \,
    \mathrm{e}^{\frac{2 P}{N} \pi \mathrm{i}
      \left(
        k+\frac{n}{2P}
      \right)^2
      -n t
    }
  
\end{aligned}$$ which vanishes due to the odd periodicity $\chi_{2 P}^{(1,1,1)}(n)
  =
  -
  \chi_{2 P}^{(1,1,1)}(2 \, P-n)$. Comparing with an expression [\[Rozansky\]](#Rozansky){reference-type="eqref" reference="Rozansky"}, this completes a proof of eq. [\[invariant_and_Eichler\]](#invariant_and_Eichler){reference-type="eqref" reference="invariant_and_Eichler"}. ◻
:::

::: theorem
For the Poincaré homology sphere with $\boldsymbol{p} =(2,3,5)$, we have $$\mathrm{e}^{
      \frac{2 \pi \mathrm{i}}{N} 
    } \,
    \left(
      \mathrm{e}^{\frac{2 \pi \mathrm{i}}{N}} - 1
    \right)
    \,    \tau_N \bigl( \Sigma(2,3,5) \bigr)
    =
    1
    +
    \frac{1}{2} \,
    \mathrm{e}^{- \frac{1}{60 N} \pi \mathrm{i}}
    \cdot
    \widetilde{\Phi}_{\boldsymbol{p}}^{(1,1,1)}(1/N)$$
:::

::: proof
*Proof.* A proof is same with Theorem [\[theorem:invariant_Eichler\]](#theorem:invariant_Eichler){reference-type="ref" reference="theorem:invariant_Eichler"} and was done in Ref. . A difference follows from a fact that the odd periodic function satisfies $$\frac{
      (z^{6} - z^{- 6}) \,
      (z^{10} - z^{- 10}) \,
      (z^{15} - z^{- 15})
    }{
      z^{30} - z^{- 30}
    }
    =
    \frac{1}{z} + z +
    \sum_{n=0}^\infty
    \chi_{60}^{(1,1,1)}(n) \, z^{n}$$ in place of eq. [\[generate_chi_general\]](#generate_chi_general){reference-type="eqref" reference="generate_chi_general"}. ◻
:::

Combining these theorems with a nearly modular property of the Eichler integral [\[asymptotics_Eichler\]](#asymptotics_Eichler){reference-type="eqref" reference="asymptotics_Eichler"}, we obtain an asymptotic expansion of the quantum invariant in $N\to\infty$.

::: coro
For a case of $\frac{1}{p_1}+\frac{1}{p_2}+\frac{1}{p_3}<1$ we have $$\begin{gathered}
    \label{tau_limit}
    \mathrm{e}^{
      \frac{2 \pi \mathrm{i}}{N}
      ( \frac{\phi(p_1,p_2,p_3)}{4} - \frac{1}{2} )
    } \,
    \left(
      \mathrm{e}^{\frac{2 \pi \mathrm{i}}{N}} - 1
    \right)
    \,    \tau_N \bigl( \Sigma(p_1, p_2, p_3) \bigr)
    \\
    \simeq
    \sqrt{\frac{N}{ \mathrm{i}} }
    \sum_{\ell_1, \ell_2, \ell_3}
    \mathbf{S}_{1,1,1}^{\ell_1, \ell_2, \ell_3} \,
    \mathrm{e}^{- \frac{1}{2} \pi \mathrm{i} P N
      \left(
        1+\sum_j \frac{\ell_j}{p_j}
      \right)^2
    }
    + \frac{1}{2} \sum_{k=0}^\infty
    \frac{L(-2 \, k , \chi_{2 P}^{(1,1,1)})}{k!}
    \,
    \left(
      \frac{\pi \, \mathrm{i}}{
        2 \, P \, N
      }
    \right)^k
  
\end{gathered}$$
:::

Here the sum in the first term runs over $\gamma(p_1, p_2, p_3)$ distinct triples, *i.e.*, the triple $(\ell_1, \ell_2, \ell_3)$ satisfies a constraint [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"} under a symmetry [\[ell_symmetry\]](#ell_symmetry){reference-type="eqref" reference="ell_symmetry"}, and we have used eq. [\[integer_Chern\]](#integer_Chern){reference-type="eqref" reference="integer_Chern"}.

We give some examples below:

-   $\Sigma(2,3,7)$:

    The function $\Phi^{(\ell_1, \ell_2, \ell_3)}(\tau)$ spans a $D(2,3,7)=3$-dimensional space, and the independent functions are given for $(\ell_1, \ell_2, \ell_3)=(1,1,1), (1,1,2)$, and $(1,1,3)$. For these triples we have from eq. [\[Eichler_integer\]](#Eichler_integer){reference-type="eqref" reference="Eichler_integer"} that $\widetilde{\Phi}^{(\ell_1, \ell_2, \ell_3)}(N)
      =0,
      -2 \, \mathrm{e}^{\frac{25}{84} \pi \mathrm{i} N},
      -2 \, \mathrm{e}^{-\frac{47}{84} \pi \mathrm{i} N}$, which shows $\mathop{\mathrm{CS}}(A)=-\frac{25}{168},
      \frac{47}{168}$. Indeed we see that $(\ell_1,\ell_2,\ell_3)=
      (1,1,1)$ does not satisfy a condition [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"}. This fact shows $\gamma(2,3,7)=2$, and is consistent with eq. [\[gamma_Casson\]](#gamma_Casson){reference-type="eqref" reference="gamma_Casson"} as we have $\lambda_C\bigl( \Sigma(2,3,7) \bigr)=-1$. As a result, we have $$\begin{gathered}
        \mathrm{e}^{
          - \frac{2 \pi \mathrm{i}}{N}
          \frac{167}{168} 
        } \,
        \left(
          \mathrm{e}^{\frac{2 \pi \mathrm{i}}{N}} - 1
        \right)
        \,    \tau_N \bigl( \Sigma(2,3,7) \bigr)
        \\
        \simeq
        \sqrt{\frac{N}{ \mathrm{i} }} \,
        \frac{2}{\sqrt{7}} \,
        \left(
          - \sin \left(     \frac{2 \, \pi }{7}  \right)
          \mathrm{e}^{- \frac{25}{84} \pi \mathrm{i}  N}
          -
          \sin \left(     \frac{3 \, \pi }{7}  \right)
          \mathrm{e}^{ \frac{47}{84} \pi \mathrm{i}  N}
        \right)
        \\
        + \frac{1}{2} \sum_{k=0}^\infty
        \frac{L(-2 \, k , \chi_{84}^{(1,1,1)})}{k!}
        \,
        \left(
          \frac{\pi \, \mathrm{i}}{
            84 \, N
          }
        \right)^k
      
    \end{gathered}$$ where $$\begin{array}{c||ccccccccc}
          n \mod 84 &
          1 & 13 & 29 & 41 & 43 & 55 & 71 & 83 &
          \text{others}
          \\
          \hline
          \chi_{84}^{(1,1,1)}(n)
          & 1 & -1 &-1 & 1 & -1 & 1 & 1 & -1 & 0
        \end{array}$$

-   $\Sigma(3,4,5)$:

    There are $D(3,4,5)=6$ independent functions $\Phi^{(\ell_1, \ell_2, \ell_3)}(\tau)$; $(\ell_1, \ell_2, \ell_3)
      =
      (1,1,1),
      (1,1,2),
      (1,1,3),
      (1,1,4),
      (1,2,1)$, and $(1,2,2)$. For these triples, we have the Eichler integral $\widetilde{\Phi}^{(\ell_1, \ell_2, \ell_3)}(N)
      =
      0,
      0,
      -2 \, \mathrm{e}^{-\frac{119}{120} \pi \mathrm{i} N},
      -2 \, \mathrm{e}^{\frac{49}{120} \pi \mathrm{i} N},
      -2 \, \mathrm{e}^{\frac{1}{30} \pi \mathrm{i} N},
      -2 \, \mathrm{e}^{-\frac{11}{30} \pi \mathrm{i} N}$ respectively, which indicates $\mathop{\mathrm{CS}}(A)
      = \frac{119}{240},
      -\frac{49}{240},
      -\frac{1}{60},
      \frac{11}{60}$. We can check that two triples, $(1,1,1)$ and $(1,1,2)$, do not satisfy a constraint [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"}. We thus have $\gamma(3,4,5)=4$, which is consistent with $\lambda_C\bigl(\Sigma(3,4,5)\bigr)=-2$. Then we obtain $$\begin{gathered}
        \mathrm{e}^{
          - \frac{2 \pi \mathrm{i}}{N}
          \frac{71}{240} 
        } \,
        \left(
          \mathrm{e}^{\frac{2 \pi \mathrm{i}}{N}} - 1
        \right)
        \,    \tau_N \bigl( \Sigma(3,4,5) \bigr)
        \\
        \simeq
        \sqrt{\frac{N}{ \mathrm{i} }} \,
        \frac{1}{\sqrt{5}} \,
        \Biggl(
          - \sin \left(     \frac{ \pi }{5}  \right)
          \mathrm{e}^{ \frac{119}{120} \pi \mathrm{i}  N}
          +
          \sin \left(     \frac{2 \, \pi }{5}  \right)
          \mathrm{e}^{- \frac{49}{120} \pi \mathrm{i}  N}
          \\
          -
          \sqrt{2} \,
          \sin \left(     \frac{2\, \pi }{5} \right)
          \mathrm{e}^{ -\frac{1}{30} \pi \mathrm{i}  N}
          +
          \sqrt{2} \,
          \sin \left(     \frac{ \pi }{5}  \right)
          \mathrm{e}^{ \frac{11}{30} \pi \mathrm{i}  N}
        \Biggr)
        \\
        + \frac{1}{2} \sum_{k=0}^\infty
        \frac{L(-2 \, k , \chi_{120}^{(1,1,1)})}{k!}
        \,
        \left(
          \frac{\pi \, \mathrm{i}}{
            120 \, N
          }
        \right)^k
      
    \end{gathered}$$ where $$\begin{array}{c||ccccccccc}
          n \mod 120 &
          13 & 37 & 43 & 53 & 67 & 77 & 83 & 107 &
          \text{others}
          \\
          \hline
          \chi_{120}^{(1,1,1)}(n)
          & 1 & -1 &-1 & -1 & 1 & 1 & 1 & -1 & 0
        \end{array}$$

The Poincaré homology sphere $\Sigma(2,3,5)$ was studied in Ref. . In this case we have a $D(2,3,5)=2$ dimensional representation of the modular group $PSL(2;\mathbb{Z})$, and independent functions $\widetilde{\Phi}^{(\ell_1,\ell_2,\ell_3)}(\tau)$ can be defined for $(\ell_1,\ell_2, \ell_3)=
(1,1,1)$ and $(1,1,2)$. We can check that both triples fulfill a condition [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"}, and that we have $\widetilde{\Phi}^{(\ell_1, \ell_2, \ell_3)}(N)
=
  -2 \, \mathrm{e}^{\frac{1}{60} \pi \mathrm{i} N},
  -2 \, \mathrm{e}^{\frac{49}{60} \pi \mathrm{i} N}$, which indicates that the Chern--Simons invariant is given by $-\frac{1}{120}$ and $-\frac{49}{120}$ respectively. As we have $\phi(2,3,5)=\frac{181}{30}$, we obtain an exact asymptotic expansion as follows;

::: coro
$$\begin{gathered}
    \label{tau_Poincare_limit}
    \mathrm{e}^{
      \frac{2 \pi \mathrm{i}}{N}
      \frac{121}{120}
    } \,
    \left(
      \mathrm{e}^{\frac{2 \pi \mathrm{i}}{N}} - 1
    \right)
    \,    \tau_N \bigl( \Sigma(2,3,5) \bigr)
    \\
    \simeq
    \sqrt{\frac{N}{ \mathrm{i} }} \,
    \frac{2}{\sqrt{5}} \,
    \left(
      \sin \Bigl( \frac{\pi}{5}  \Bigr) \,
      \mathrm{e}^{- \frac{1}{60} \pi \mathrm{i} N}
      +
      \sin \Bigl( \frac{2 \, \pi}{5}  \Bigr) \,
      \mathrm{e}^{- \frac{49}{60} \pi \mathrm{i} N}
    \right)
    \\
    + \mathrm{e}^{\frac{\pi \mathrm{i}}{60 N} }
    +
    \frac{1}{2}
    \sum_{k=0}^\infty
    \frac{L(-2 \, k , \chi_{60}^{(1,1,1)})}{k!} \,
    \left(
      \frac{\pi \, \mathrm{i}}{60 \, N}
    \right)^k  
  
\end{gathered}$$ where $$\begin{array}{c||ccccccccc}
      n \mod 60 &
      1 & 11 & 19 & 29 & 31 & 41 & 49 & 59 &
      \text{others}
      \\
      \hline
      \chi_{60}^{(1,1,1)}(n)
      & -1 & -1 &-1 & -1 & 1 & 1 & 1 & 1 & 0
    \end{array}$$
:::
