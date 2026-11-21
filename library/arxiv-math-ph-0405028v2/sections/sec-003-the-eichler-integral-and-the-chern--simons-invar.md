---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-003-the-eichler-integral-and-the-chern--simons-invar
section_title: "The Eichler Integral and the Chern--Simons Invariant"
section_number: null
pages: 8-14
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.841
latex_coverage_ratio: 1.0
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshetikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ(p1, p2, p3)"
---
[]{#sec:Eichler label="sec:Eichler"}

The Eichler integral was originally defined as a $k-1$-fold integration of a modular form with integral weight $k\in \mathbb{Z}_{\geq 2}$ (see, *e.g.*, Ref. ). Following Refs.  (see also Refs. ), we define the Eichler integral of the modular form $\Phi_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}(\tau)$ with *half-integral* weight $3/2$ by $$\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)
  =
  \sum_{n=0}^\infty
  \chi_{2 P}^{(\ell_1 , \ell_2, \ell_3)}(n) \,
  q^{\frac{n^2}{4 P}}$$

We should remark that there are $D(p_1,p_2,p_3)$ independent Eichler integrals due to the symmetry [\[symmetry_chi\]](#symmetry_chi){reference-type="eqref" reference="symmetry_chi"}.

::: prop
[]{#prop:Eichler_limit label="prop:Eichler_limit"} The function $\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)$ has a limiting value in $\tau \to 1/N$ for $N\in \mathbb{Z}$ as $$\label{Eichler_fraction}
    \widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(1/N)
    =
    \sum_{n=0}^{P N}
    \chi_{2 P}^{(\ell_1 , \ell_2, \ell_3)}(n) \,
    \left(
      1 - \frac{n}{P \, N}
    \right) \,
    \mathrm{e}^{\frac{1}{2 P N} n^2 \pi \mathrm{i}}$$ We also have $$\begin{aligned}
    \label{Eichler_integer}
    \widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(N)
    & =
    - \frac{1}{2 \, P} \,
    \left(
      \sum_{n=1}^{2 P}
      n \,
      \chi_{2 P}^{(\ell_1 , \ell_2, \ell_3)}(n) \,
    \right) \,
    \mathrm{e}^{\frac{\pi \mathrm{i}}{2} P N
      \left(
        1+\sum_j \frac{\ell_j}{p_j}
      \right)^2
    }
    \\
    & =
    - \frac{1}{2 \, P} \,
    \left(
      \sum_{n=1}^{2 P}
      n \,
      \chi_{2 P}^{(\ell_1 , \ell_2, \ell_3)}(n) \,
    \right) \,
    \left(
      \mathbf{T}^{\ell_1 , \ell_2, \ell_3}
    \right)^N
    \nonumber







  
\end{aligned}$$
:::

To prove this proposition, we use the following formula for asymptotic expansions (see Refs. );

::: prop
[]{#prop:L_function label="prop:L_function"} Let $C_f(n)$ be a periodic function with mean value $0$ and modulus $f$. Then we have an asymptotic expansion as $t \searrow 0$; $$\begin{gathered}
    \sum_{n=1}^\infty C_f(n) \, \mathrm{e}^{-n   t}
    \simeq
    \sum_{k=0}^\infty
    L(- k, C_f) \,
    \frac{(-t)^k}{k!} 
    \\[2mm]

    \sum_{n=1}^\infty C_f(n) \, \mathrm{e}^{-n^2  t}
    \simeq
    \sum_{k=0}^\infty
    L(-2 \, k, C_f) \,
    \frac{(-t)^k}{k!} 
  
\end{gathered}$$ Here $L(k,C_f)$ is the Dirichlet $L$-function associated with $C_f(n)$, and is given by $$L(-k, C_f)
    =
    - \frac{f^k}{k+1} \,
    \sum_{n=1}^f
    C_f(n) \, B_{k+1} \left( \frac{\ n \ }{f} \right)$$ where $B_n(x)$ is the $n$-th Bernoulli polynomial defined from $$\frac{
      t \, \mathrm{e}^{x t}
    }{
      \mathrm{e}^t -1
    }
    =
    \sum_{n=0}^\infty
    \frac{B_n(x)}{n!} \,
    t^n$$
:::

See, *e.g.*, Ref.  for a proof.

::: proof
*Proof of Proposition [\[prop:Eichler_limit\]](#prop:Eichler_limit){reference-type="ref" reference="prop:Eichler_limit"}.* We assume $M$ and $N$ are coprime integers, and $N>0$. By definition, we have $$\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}
    \left(
    \frac{M}{N} + \mathrm{i} \, \frac{y}{2 \, \pi}
    \right)
    =
    \sum_{n=0}^\infty C_{2 P N}^{(\ell_1,\ell_2,\ell_3)}(n) \,
    \mathrm{e}^{- \frac{y}{4 P} n^2}$$ where $y>0$ and $$C_{2 P N}^{(\ell_1,\ell_2,\ell_3)}(n) 
    =
    \chi_{2 P}^{(\ell_1,\ell_2,\ell_3)}(n) \,
    \mathrm{e}^{\frac{M}{2 P N} n^2 \pi \mathrm{i}}$$ We see that $C_{2 P N}^{(\ell_1,\ell_2,\ell_3)}(n+2 \, P \, N) 
  =  C_{2 P N}^{(\ell_1,\ell_2,\ell_3)}(n)$, and $C_{2 P N}^{(\ell_1,\ell_2,\ell_3)}(2 \, P \, N -n) 
  = - C_{2 P N}^{(\ell_1,\ell_2,\ell_3)}(n)$. Then we can apply Prop. [\[prop:L_function\]](#prop:L_function){reference-type="ref" reference="prop:L_function"}, and we have an asymptotic expansion in $y\searrow 0$ as $$\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}
    \left(
    \frac{M}{N} + \mathrm{i} \, \frac{y}{2 \, \pi}
    \right)
    \simeq
    \sum_{k=0}^\infty
    \frac{L(-2 \, k , C_{2 P N}^{(\ell_1,\ell_2,\ell_3)})}{k!} \,
    \left(
      - \frac{y}{4 P}
    \right)^k$$ which gives a limiting value as $$\label{Eichler_and_L}
    \widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}
    (M/N)
    =
    L(0 , C_{2 P N}^{(\ell_1,\ell_2,\ell_3)})$$ Using a fact that $\chi_{2P}^{(\ell_1,\ell_2,\ell_3)}(2 \, P - n)
  =
  -  \chi_{2P}^{(\ell_1,\ell_2,\ell_3)}(n)$ and that an explicit form of the Bernoulli polynomial is $B_1(x)=x-\frac{1}{2}$, we get $$\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}
    (M/N)
    =
    \sum_{n=0}^{P N}
    \chi_{2 P}^{(\ell_1,\ell_2,\ell_3)}(n) \,
    \left(
      1- \frac{n}{P \, N}
    \right) \,
    \mathrm{e}^{
      \frac{M}{2 P N} n^2 \pi \mathrm{i}
    }$$ Eq. [\[Eichler_fraction\]](#Eichler_fraction){reference-type="eqref" reference="Eichler_fraction"} directly follows from this formula. Eq. [\[Eichler_integer\]](#Eichler_integer){reference-type="eqref" reference="Eichler_integer"} can also be given from the above formula when we recall $\sum_{n=1}^{2 P}       \chi_{2 P}^{(\ell_1 , \ell_2, \ell_3)}(n) 
  =0$. ◻
:::

We can see that, though we have $D(p_1, p_2, p_3)$ independent Eichler integrals, the limiting value $\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(N)$ at $N\in \mathbb{Z}$ computed in eq. [\[Eichler_integer\]](#Eichler_integer){reference-type="eqref" reference="Eichler_integer"} becomes identically zero for some triples $(\ell_1,\ell_2,\ell_3)$.

::: prop
Let $\gamma(p_1,p_2,p_3)$ be the number of independent Eichler integrals

such that $\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}(N) \not\equiv 0$ for $N\in\mathbb{Z}$, namely $$\label{zero_condition}
    \sum_{n=1}^{2 P} n \, 
    \chi_{2 P}^{(\ell_1,\ell_2,\ell_3)}(n)
    \neq 0$$ We then have $$\begin{gathered}
    \label{value_gamma}
    \gamma(p_1, p_2, p_3)
    =
    s(p_1 \, p_2, p_3)+    s(p_2 \, p_3, p_1)+    s(p_1 \, p_3, p_2)
    \\
    +

    \frac{P}{12} \,
    \left(
      1-
      \frac{1}{p_1^{~2}}
      -   \frac{1}{p_2^{~2}}
      -  \frac{1}{p_3^{~2}}
    \right)
    -\frac{1}{12  \, P}

    +
    \frac{1}{4}
  
\end{gathered}$$ where $s(b,a)$ is the Dedekind sum defined in eq. [\[Dedekind_sum\]](#Dedekind_sum){reference-type="eqref" reference="Dedekind_sum"}.
:::

::: proof
*Proof.* For a sake of our brevity we set $A_k=\frac{\ell_i}{p_i}+\frac{\ell_j}{p_j}-\frac{\ell_k}{p_k}$ for $i\neq j \neq k \neq i$ and $i,j,k\in \{1,2,3\}$. As we have $0 < \frac{\ell_k}{p_k}<1$ by definition, we have $0 < \sum_j  \frac{\ell_j}{p_j} < 3$ and $-1 < A_k <2$.

When $0<  \sum_j \frac{\ell_j}{p_j} < 1$, we have $0< A_k  +1 < 2 \left( 1-\frac{\ell_k}{p_k} \right)<2$. Then in a domain $0<n<2 \, P$, the periodic function $\chi_{2 P}^{(\ell_1,\ell_2,\ell_3)}(n)$ defined in eq. [\[define_chi\]](#define_chi){reference-type="eqref" reference="define_chi"} takes a value $1$ when $n= P \, \left(1-\sum_j \frac{\ell_j}{p_j} \right),
  P (1 + A_k)$, while it is $-1$ when $n= P \, \left( 1+\sum_j \frac{\ell_j}{p_j} \right),
  P \, \left( 1 - A_k \right)$. Then we find $\sum_{n=1}^{2 P} n \chi_{2 P}^{(\ell_1,\ell_2,\ell_3)}(n)=0$, and it is inconsistent with eq. [\[zero_condition\]](#zero_condition){reference-type="eqref" reference="zero_condition"}.

We thus have a condition $1 < \sum_j  \frac{\ell_j}{p_j} < 3$ to fulfill eq. [\[zero_condition\]](#zero_condition){reference-type="eqref" reference="zero_condition"}, because it is impossible to have $\sum_j \frac{\ell_j}{p_j} \in \mathbb{Z}$. Under this condition there are two possibilities for a condition of $A_k$; (i) $-1 < A_k <1$ for all $k$, or (ii) $-1 < A_k <1$ for two $k$'s and $1<A_i<2$ for another $i$. By the same computation we can check $$\label{non_zero_integer}
    \sum_{n=1}^{2 P} n \, \chi_{2 P}^{(\ell_1,\ell_2,\ell_3)}(n)=4 \, P$$ for the former case, while we have $\sum_{n=1}^{2 P} n \chi_{2 P}^{(\ell_1,\ell_2,\ell_3)}(n)=0$ for the latter. To conclude, a condition [\[zero_condition\]](#zero_condition){reference-type="eqref" reference="zero_condition"} is fulfilled when the triple of integers satisfies $$\label{ell_condition}
    \begin{aligned}
      & 1<\frac{\ell_1}{p_1}+ \frac{\ell_2}{p_2} + \frac{\ell_3}{p_3}<3
      & &
      -1<\frac{\ell_1}{p_1}+ \frac{\ell_2}{p_2} - \frac{\ell_3}{p_3}<1
      \\[2mm]
      &
      -1<\frac{\ell_1}{p_1} - \frac{\ell_2}{p_2} + \frac{\ell_3}{p_3}<1
      & &
      -1<- \frac{\ell_1}{p_1}+ \frac{\ell_2}{p_2} + \frac{\ell_3}{p_3}<1
    \end{aligned}$$ This constraint is depicted as the number of the integral lattice points of an interior of the tetrahedron (see Fig. [1](#fig:tetrahedron){reference-type="ref" reference="fig:tetrahedron"}).

<figure id="fig:tetrahedron">
<div class="pspicture">
<p>(-4,-2.2)(4,5)</p>
<p>(6,5,4)(6,0,0)(0,5,0) (6,5,4)(6,0,0)(0,0,4) (6,5,4)(0,0,4)(0,5,0)</p>
<p>(0,0,0)(6,0,0)(0,5,0)(0,0,4) (6,0,0)(0,5,0)(0,0,4) (6,5,4)(0,0,4) (6,5,4)(0,5,0) (6,5,4)(6,0,0)</p>
<p>(6,0,0) (0,5,0) (0,0,4) (6,5,4)</p>
<p>(8,0,0.9)<span><span class="math inline">(<em>p</em><sub>1</sub>,0,0)</span></span> (0,6.1,0.7)<span><span class="math inline">(0,<em>p</em><sub>2</sub>,0)</span></span> (0,1.2,4.5)<span><span class="math inline">(0,0,<em>p</em><sub>3</sub>)</span></span></p>
</div>
<figcaption>The number of the integral lattice points in the tetrahedron coincides with <span class="math inline"><em>γ</em>(<em>p</em><sub>1</sub>,<em>p</em><sub>2</sub>,<em>p</em><sub>3</sub>)</span>. </figcaption>
</figure>

Let $N_3(p_1,p_2,p_3)$ be the number of the integral lattice points $(\ell_1, \ell_2, \ell_3)$ such that $0<\ell_k<p_k$ and $0< \sum_j \frac{\ell_j}{p_j} <1$. Then by the symmetry of the triple, $$\label{ell_symmetry}
    \begin{aligned}
      & (\ell_1,\ell_2,\ell_3) 
      & & (\ell_1, p_2 - \ell_2, p_3  -\ell_3) 
      \\
      & (p_1 -\ell_1,  \ell_2, p_3 - \ell_3) 
      & & (p_1 - \ell_1, p_2 - \ell_2, \ell_3) 
    \end{aligned}$$ we have $$\gamma(p_1, p_2, p_3 )
    =
    D(p_1, p_2 , p_3) - N_3 (p_1 , p_2, p_3)$$ It is well known that $N_3(p_1, p_2, p_3)$ was computed by Mordell [@Morde51] (see also Ref. ), and by substituting this result, we get eq. [\[value_gamma\]](#value_gamma){reference-type="eqref" reference="value_gamma"}. ◻
:::

The Casson invariant $\lambda_C(\mathcal{M})$ for the Brieskorn homology spheres $\mathcal{M}= \Sigma(p_1, p_2, p_3)$ is given by [@FintuStern90a; @FukuMatsSaka90] (also see, *e.g.*, Ref. ) $$\begin{gathered}
  \label{Casson_sphere}
  \lambda_C\bigl(\Sigma(p_1, p_2, p_3) \bigr)
  =
  -\frac{1}{2}
  \left(
    s(p_1 \, p_2, p_3)+    s(p_2 \, p_3, p_1)+    s(p_1 \, p_3, p_2)
  \right)
    \\
    -
    \frac{P}{24} \,
    \left(
      1-
      \frac{1}{p_1^{~2}}
      -   \frac{1}{p_2^{~2}}
      -  \frac{1}{p_3^{~2}}
    \right)
    + \frac{1}{24  \, P}

    -
    \frac{1}{8}
\end{gathered}$$ With this result, we have the following theorem.

::: theorem
The Casson invariant is a minus half of the number of the Eichler integrals which do not vanish at $\tau\to N\in\mathbb{Z}$; $$\label{gamma_Casson}
    \lambda_C \bigl(\Sigma(p_1, p_2, p_3) \bigr)
    =
    -\frac{1}{2} \,
    \gamma(p_1, p_2, p_3)$$
:::

The fundamental group of the Brieskorn homology spheres has the presentation [\[presentation\]](#presentation){reference-type="eqref" reference="presentation"}, and the Casson invariant is related to the representation space of the fundamental group [@FintuStern90a]. That is to say, we see that $\gamma(p_1, p_2, p_3)$ coincides with the cardinality of the SU(2) representation space of $\pi_1\bigl( \Sigma(p_1, p_2, p_3) \bigr)$, and that the triple $(\ell_1, \ell_2, \ell_3)$ has a one-to-one correspondence with the irreducible representation. Explicitly when we have an irreducible representation $\alpha$ of $\pi_1\bigl( \Sigma(p_1, p_2, p_3) \bigr)$, the conjugacy class of $\alpha(x_k)$ is $$\label{conjugacy}
  \begin{pmatrix}
    \mathrm{e}^{\frac{p_k - \ell_k}{p_k} \pi \mathrm{i}} &
    \\
    & \mathrm{e}^{- \frac{p_k - \ell_k}{p_k} \pi \mathrm{i}} 
  \end{pmatrix}$$ where the triple of integers $(\ell_1, \ell_2, \ell_3)$ satisfies a condition [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"}.

Using this correspondence with the irreducible representation of the fundamental group, we can read off the Chern--Simons invariant of the Brieskorn homology spheres [@FintuStern90a] (see also Ref. ); $$\label{CS_B}
  \mathop{\mathrm{CS}}(A)
  =
  - \frac{P}{4} \, 
  \left(
    1+ \sum_{j=1}^3 \frac{\ell_j}{p_j}
  \right)^2
  \mod 1$$

::: theorem
The Chern--Simons invariant [\[CS_B\]](#CS_B){reference-type="eqref" reference="CS_B"} for the Brieskorn homology spheres $\Sigma(p_1,p_2,p_3)$ is related to a limit value of the Eichler integral which can be regarded as the $\mathbf{T}$-matrix of the modular group; for $N\in\mathbb{Z}$ we have $$\begin{aligned}
    \widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}
    (N)
    & =
    -2 \,
    \left(
      \mathbf{T}^{\ell_1 , \ell_2, \ell_3}
    \right)^N
    \nonumber
    \\
    & =
    - 2 \,
    \mathrm{e}^{ - 2 \pi \mathrm{i} \mathop{\mathrm{CS}}(A) N}
    \label{integer_Chern}
  
\end{aligned}$$ where the triple of integers $(\ell_1,\ell_2,\ell_3)$ satisfies eq. [\[ell_condition\]](#ell_condition){reference-type="eqref" reference="ell_condition"}. The triple $(\ell_1,\ell_2,\ell_3)$ also gives a $SU(2)$ representation $\alpha$ of the fundamental group [\[presentation\]](#presentation){reference-type="eqref" reference="presentation"}, where the conjugacy class of $\alpha(x_k)$ is as in eq. [\[conjugacy\]](#conjugacy){reference-type="eqref" reference="conjugacy"}.
:::

We should point out that, with $s$ and $t$ being coprime positive integers. the number, $(s-1) \, (t-1)/2$, of integral lattice points in the 2-dimensional space has appeared as the number of the irreducible highest weight representation of the Virasoro algebra of the minimal model $\mathcal{M}(s,t)$ in the conformal field theory [@BPZ84a]. The character of the minimal model $\mathcal{M}(s,t)$ is modular with weight $1/2$, and it was shown [@KHikami03c; @KHikami03b] that the Eichler integral thereof is a specific value of the colored Jones polynomial for the torus knot $\mathcal{T}_{s,t}$. Also we may say that a one-dimensional analogue of the number of the integral lattice points is realized in a torus link; the colored Jones polynomial for the torus link $\mathcal{T}_{2,2  N}$ coincides with the Eichler integral of the $\widehat{su}(2)_{N-2}$ character [@KHikami03a], which is a ($N-1$)-dimensional representation [\[affine_su\]](#affine_su){reference-type="eqref" reference="affine_su"} of the modular group with weight $3/2$. In this sense, the Brieskorn homology spheres may be regarded as a

generalization of the torus knot and link from the viewpoint of the modular form. This may indicate the fact that the Brieskorn homology sphere $\Sigma(p_1,p_2,p_3)$ is homeomorphic to the $p_3$-fold cyclic branched covering of $S^3$ branched along a torus knot $\mathcal{T}_{p_1,p_2}$ [@JMiln75a], and that the manifold $\Sigma(p, q, p \, q \,n \pm 1)$ can be alternatively constructed by $\pm 1/n$-surgery of the torus knot $\mathcal{T}_{p,q}$.

For our purpose to give an exact asymptotic behavior of the WRT invariant, we shall give an asymptotic expansion of the Eichler integral at $\tau\to 1/N$. The Eichler integral is no longer modular, but it has a *nearly* modular property when $\tau\in \mathbb{Q}$ as was studied in Ref. .

::: prop
The Eichler integral $\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}(\tau)$ in $\tau \to 1/N$ for $N\in\mathbb{Z}_{>0}$ fulfills a nearly modular property. Namely, under the $S$-transformation, we have an asymptotic expansion in $N\to\infty$ as follows; $$\begin{gathered}
    \label{asymptotics_Eichler}
    \widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(1/N)
    \simeq
    -
    \sqrt{\frac{N}{ \mathrm{i}}}
    \sum_{\ell_1^\prime, \ell_2^\prime, \ell_3^\prime}
    \mathbf{S}_{\ell_1, \ell_2, \ell_3}^{\ell_1^\prime, \ell_2^\prime,
      \ell_3^\prime} \,
    \widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1^\prime, \ell_2^\prime,
      \ell_3^\prime)}(-N)
    \\
    +
    \sum_{k=0}^\infty
    \frac{
      L(-2 \, k , \chi_{2 P}^{(\ell_1, \ell_2, \ell_3)})
    }{
      k!
    }
    \,
    \left(
      \frac{\pi \, \mathrm{i}}{
        2 \, P \, N
      }
    \right)^k
  
\end{gathered}$$

Here the $L$-function is given by $$\label{L_and_Bernoulli}
    L(-2 \, k , \chi_{2 P}^{(\ell_1, \ell_2, \ell_3)})
    =
    - \frac{(2 \, P)^{2 k}}{2 \, k +1}
    \sum_{j=1}^{2 P}
    \chi_{2 P}^{(\ell_1 , \ell_2 ,\ell_3)}(j) \,
    B_{2 k +1}
    \left( \frac{j}{2 \, P} \right)$$
:::

::: proof
*Proof.* A proof is essentially the same with one given in Ref.  (see also Refs. ). We use $$\label{define_Phi_hat}
    \widehat{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}(z)
    =
    \frac{1}{\sqrt{2 \, P \, \mathrm{i}}} \,
    \int_{z^*}^\infty
    \frac{
      \Phi_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}(\tau)
    }{
      \sqrt{\tau - z}
    }
    \,
    \mathrm{d} \tau$$ which is defined for $z$ in the lower half plane, $z \in \mathbb{H}^-$. We mean that $z^*$ denotes a complex conjugate, and we do not have a singularity in integral. Applying the modular ${S}$-transformation [\[S_transformation\]](#S_transformation){reference-type="eqref" reference="S_transformation"}, we see that the function $\widehat{\Phi}_{\boldsymbol{p}}^{(\ell_1,\ell_2,\ell_3)}(z)$ has a nearly modular property; $$\label{modular_Phi_hat}
    \frac{1}{\sqrt{\mathrm{i} \, z}} \,
    \sum_{\ell_1^\prime, \ell_2^\prime, \ell_3^\prime}
    \mathbf{S}_{\ell_1, \ell_2, \ell_3}^{\ell_1^\prime, \ell_2^\prime,
      \ell_3^\prime} \,
    \widehat{\Phi}_{\boldsymbol{p}}^{(\ell_1^\prime, \ell_2^\prime,
      \ell_3^\prime)}(-1/z)
    +
    \widehat{\Phi}_{\boldsymbol{p}}^{(\ell_1, \ell_2 , \ell_3)}(z)
    =
    r_{\boldsymbol{p}}^{(\ell_1, \ell_2 , \ell_3)}(z;0)$$ where we have an analogue of the period function $$\label{define_r_function}
    r_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(z ; \alpha)
    =
    \frac{1}{
      \sqrt{2 \, P \, \mathrm{i}}
    } \,
    \int_\alpha^\infty
    \frac{\Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)}{
      \sqrt{\tau-z}
    } \,
    \mathrm{d} \tau$$ for $\alpha \in \mathbb{Q}$ and $z\in \mathbb{H}^-$. On the other hand, substituting eq. [\[modular_Phi\]](#modular_Phi){reference-type="eqref" reference="modular_Phi"} for eq. [\[define_Phi_hat\]](#define_Phi_hat){reference-type="eqref" reference="define_Phi_hat"}, we get for $z= x + \mathrm{i} \, y$ with $y < 0$ as follows; $$\begin{aligned}
    \widehat{\Phi}_{\boldsymbol{p}}^{(\ell_1 , \ell_2, \ell_3)}(z)
    & =
    \frac{1}{\sqrt{2 \, P \, \mathrm{i}}}
    \sum_{n \in \mathbb{Z}}
    n \,
    \chi_{2 P}^{(\ell_1 , \ell_2 ,\ell_3)}(n) \,
    \int_{z^*}^\infty
    \frac{
      \mathrm{e}^{\frac{n^2}{2 P} \pi \mathrm{i} \tau}
    }{
      \sqrt{\tau - z}
    } \,
    \mathrm{d} \tau
    \\
    & =
    \sum_{n=0}^{\infty}
    \chi_{2 P}^{(\ell_1 , \ell_2 ,\ell_3)}(n) \,
    \mathrm{e}^{
      \frac{n^2}{2 P} \pi \mathrm{i} z
    } \,
    \mathop{\mathrm{erfc}}
    \left(
      n \,
      \sqrt{
        -\frac{\pi \, y}{P}
      }
    \right)
  
\end{aligned}$$ As a limit of $z \to \alpha \in \mathbb{Q}$, we find that $$\widehat{\Phi}_{\boldsymbol{p}}^{(\ell_1 , \ell_2, \ell_3)}(\alpha)
    =
    \widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1 , \ell_2, \ell_3)}(\alpha)$$ Then a nearly modular property [\[asymptotics_Eichler\]](#asymptotics_Eichler){reference-type="eqref" reference="asymptotics_Eichler"} of $\widetilde{\Phi}_{\boldsymbol{p}}^{(\ell_1 , \ell_2, \ell_3)}(1/N)$ follows from eq. [\[modular_Phi_hat\]](#modular_Phi_hat){reference-type="eqref" reference="modular_Phi_hat"} by setting $z \to 1/N$ and taking an asymptotic expansion of the integral [\[define_r_function\]](#define_r_function){reference-type="eqref" reference="define_r_function"} in $N\to\infty$. ◻
:::

It should be noted that the sum in the first term in the right hand side of eq. [\[asymptotics_Eichler\]](#asymptotics_Eichler){reference-type="eqref" reference="asymptotics_Eichler"} runs over $D(p_1,p_2,p_3)$ distinct triples, but, as was clarified in the preceding sections, some of them vanish and there are $\gamma(p_1,p_2,p_3)$ non-zero contributions, which correspond to a sum of the flat connection [\[asymptotic_Witten\]](#asymptotic_Witten){reference-type="eqref" reference="asymptotic_Witten"}.
