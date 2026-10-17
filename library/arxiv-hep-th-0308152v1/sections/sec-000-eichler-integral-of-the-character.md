---
doc_id: arxiv-hep-th-0308152v1
doc_title: "TORUS KNOT AND MINIMAL MODEL"
section_id: sec-000-eichler-integral-of-the-character
section_title: "Eichler Integral of the Character"
section_number: null
pages: 1-10
source_pdf: 0308152v1.pdf
source_sha256: 93bcc14b8be91257
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.691
doc_brief: "TORUS KNOT AND MINIMAL MODEL — 2 sections: Front matter; Eichler Integral of the Character"
---
[]{#sec:character label="sec:character"}

We study the character of the minimal model $\mathcal{M}(s,t)$, where $s$ and $t$ are coprime integers. The central charge of the minimal model $\mathcal{M}(s, t)$ is $$c(s,t) = 1 - \frac{6 \, (s-t)^2}{s \, t} ,$$ and the irreducible highest weight representation of the Virasoro algebra is given for the conformal weight $$\Delta^{s,t}_{n,m}
  =
  \frac{(n \, t - m \, s)^2 - (s-t)^2}{4 \, s \, t} ,$$ where integers $m$ and $n$ are $$\begin{aligned}
  & 1 \leq n \leq s-1,
  &
  & 1 \leq m \leq t- 1.
\end{aligned}$$ The number of distinct fields in the theory is $$D(s,t) = \frac{1}{2} \, (s-1 ) \, (t-1) .$$

The character $\mathop{\mathrm{ch}}_{n,m}^{s,t}(\tau)$ for an irreducible highest weight representation of the Virasoro algebra with above central charge and weight, is computed as [@Rocha84a; @BFeigDBFuk83a] $$\begin{aligned}
  \mathop{\mathrm{ch}}_{n,m}^{s,t}(\tau)
  & =
  \mathop{\mathrm{Tr}}q^{L_0 - \frac{1}{24} c(s,t)}
  \nonumber \\
  & =
  \frac{q^{\Delta^{s,t}_{n,m} - \frac{1}{24} c(s,t)}}{(q)_\infty} \,
  \sum_{k \in \mathbb{Z}}
  q^{s t k^2} \,
  \left(
    q^{k ( n t - m s)} - q^{k ( n t +m s)+ m n}
  \right) ,
\end{aligned}$$ where we set $q=\mathrm{e}^{2 \pi \mathrm{i} \tau}$. We see that $$\mathop{\mathrm{ch}}_{n,m}^{s,t}(\tau)
  =
  \mathop{\mathrm{ch}}_{s-n,t-m}^{s,t}(\tau)
  =
  \mathop{\mathrm{ch}}_{m,n}^{t,s}(\tau)
  =
  \mathop{\mathrm{ch}}_{t-m,s-n}^{t,s}(\tau) .$$ The character is modular covariant [@ItzyZube86; @CappItzyZube87b] as $$\mathop{\mathrm{ch}}_{n,m}^{s,t}(\tau)
  =
  \sum_{n^\prime , m^\prime}
  \mathbf{S}_{n,m}^{n^\prime , m^\prime} \,
  \mathop{\mathrm{ch}}_{n^\prime , m^\prime}^{s,t} (-1 / \tau) ,$$ where sum runs over $D(s,t)$ distinct fields, and a matrix is explicitly written as $$\mathbf{S}_{n,m}^{n^\prime , m^\prime}
  =
  \sqrt{\frac{8}{\   s \, t   \  }} \,
  (-1)^{n  m^\prime + m n^\prime +1} \,
  \sin
  \left(
     n \, n^\prime \, \frac{\ t  \  }{s}  \,  \pi 
  \right) \,
  \sin
  \left(
      m \, m^\prime \, \frac{ s}{ \  t  \  } \, \pi
  \right) .$$

We rewrite the character of the minimal model as $$\mathop{\mathrm{ch}}_{n,m}^{s,t}(\tau)
  =
  \frac{
    \Phi^{(n,m)}(\tau)
  }{\eta(\tau)} .$$ Here we have set the Dedekind $\eta$-function and $\Phi^{(n,m)}(\tau)$ as $$\begin{gathered}
  \eta(\tau)
  =
  q^{1/24} \, (q)_\infty, 
  \nonumber
  \\[2mm]

  \Phi^{(n,m)}(\tau)
  =
  \sum_{k=0}^\infty \chi_{2 s t}^{(n,m)}(k) \, q^{\frac{1}{4 s t} k^2} ,
  \label{define_Phi}
\end{gathered}$$ where the function $\chi_{2 s t}^{(n,m)}(k)$ is periodic with modulus $2\, s \, t$ as $$\begin{array}{c|ccccc}
    k
    \mod 2 \, s \, t
    & n \, t - m \, s & n \, t + m \, s &
    2 \, s \, t - ( n \, t + m \, s)
    & 2 \, s \, t - (n \, t - m \, s) &
    \text{others}
    \\
    \hline
    \chi_{2 s t}^{(n,m)}(k)
    &
    1 & -1 & -1 & 1 & 0
  \end{array}$$ From the modular property of the Dedekind $\eta$-function, we see that $\Phi^{(n,m)}(\tau)$ is modular with weight $1/2$, and spans $D(s,t)$ dimensional space; modular $T$- and $S$-transformations are respectively written as $$\begin{gathered}
  \Phi^{(n,m)}(\tau+1)
  =
  \mathrm{e}^{\frac{(n t - m s)^2}{2 s t} \pi \mathrm{i}} \,
  \Phi^{(n,m)}(\tau) ,
  \\[2mm]

  \Phi^{(n,m)}(\tau)
  =
  \sqrt{\frac{\   \mathrm{i}  \  }{\tau}} \,
  \sum_{n^\prime , m^\prime}
  \mathbf{S}_{n,m}^{n^\prime , m^\prime} \,
  \Phi^{(n^\prime  ,   m^\prime)}(-1/\tau) .
  \label{Phi_S_transform}
\end{gathered}$$

For the modular form with weight $w \in \mathbb{Z}_{>2}$, the period is defined by use of the classical Eichler integral, which is $w-1$ integrations of the modular form with respect to $\tau$ [@SLang76Book]. In a case of the half-integral weight modular form $\Phi^{(n,m)}(\tau)$, the Eichler integral is thus naively defined by the $q$-series as [@DZagie01a] $$\label{define_tilde}
  \widetilde{\Phi}^{(n,m)}(\tau)
  =
  -\frac{1}{2} \, \sum_{k=0}^\infty k \, 
  \chi_{2 s t}^{(n,m)}(k) \, q^{\frac{1}{4 s t} k^2} .$$ A prefactor is for our convention. It can be seen that the former is regarded as a "half-derivative" ($\frac{1}{2}-1$ integration) of the modular form $\Phi^{(n,m)}(\tau)$ with respect to $\tau$, as was originally studied in Ref. . We consider a limiting value of the Eichler integral $\widetilde{\Phi}^{(n,m)}(\alpha)$ at $\alpha  \in \mathbb{Q}$. Applying the Mellin transformation, we have $$\widetilde{\Phi}^{(n,m)}
  \left(
    \frac{M}{N} +
    \mathrm{i} \, \frac{y}{2 \,  \pi}
  \right)
  \simeq
  - \frac{1}{2} \, \sum_{k=0}^\infty
  \frac{L_\omega(- 2 \, k -1 , \chi_{2 s t}^{(n,m)} )}{k!} \,
  \left(
    - \frac{y}{4 \,s \, t}
  \right)^k ,$$ where $y\searrow 0$, and $M,N$ are coprime integers. We mean that $L_\omega (k,\chi_{2 s t }^{(n,m)})$ is the twisted $L$-function defined by $$\begin{aligned}
  L_\omega(k, \chi_{2 s t}^{(n,m)})
  & =
  \sum_{j=1}^\infty \chi_{2 s t}^{(n,m)} (j) \,
  \mathrm{e}^{ \frac{M}{N} \frac{j^2}{2 s t}  \pi \mathrm{i}} \,
  j^{-k}
  \\
  & =
  \frac{1}{(2 \, s \, t \, N)^k} \,
  \sum_{j=1}^{2 s t N}
  \chi_{2 s t}^{(n,m)}(j) \,
  \mathrm{e}^{ \frac{M}{N} \frac{j^2}{2 s t} \pi \mathrm{i}} \,
  \zeta \left(k, \frac{j}{2 \, s \, t \, N}\right)
  ,
\end{aligned}$$ where $\zeta(k,x)$ is the Hurwitz $\zeta$ function. By the analytic continuation, limiting value at $\tau \to M/N$ is then computed as $$\label{Eichler_for_MN}
  \widetilde{\Phi}^{(n,m)}(M/N)
  =
  \frac{s \, t \, N}{2}
  \sum_{k=1}^{2 s t N}
  \chi_{2 s t}^{(n,m)}(k) \,
  \mathrm{e}^{\frac{k^2 M}{2 s t N} \pi \mathrm{i}} \, 
  B_2\left(\frac{k}{2 \, s \, t \, N}\right) ,$$ where $B_k(x)$ is the $k$-th Bernoulli polynomial, $\displaystyle
\frac{t \, \mathrm{e}^{x t}}{\mathrm{e}^t - 1}
=
\sum_{k=0}^\infty  \frac{t^k}{k!} \, B_k(x)$, and especially $B_2(x) = x^2 - x + \frac{1}{6}$.

This function fulfills a *nearly* modular property; for $N \in \mathbb{Z}$ we have an asymptotic expansion in $N\to \infty$, $$\begin{gathered}
  \label{nearly_modular_Phi}
  \widetilde{\Phi}^{(n,m)}(1/N)
  + ( - \mathrm{i} \, N)^{3/2} \,
  \sum_{n^\prime , m^\prime}
  \mathbf{S}_{n,m}^{n^\prime , m^\prime} \,
  \phi(n^\prime , m^\prime) \,
  \mathrm{e}^{
    - \frac{(n^\prime t - m^\prime s)^2}{2 s t} \pi \mathrm{i} N
  }
  \\
  \simeq
  \sum_{k=0}^\infty
  \frac{T^{(n,m)}(k)}{k!} \,
  \left(
    \frac{\pi}{2 \, s \, t \, \mathrm{i} \, N}
  \right)^k .
\end{gathered}$$ Here we have set $$\phi(n,m)
  =
  \begin{cases}
    (s-n) \, m ,
    &
    \text{if  $n \,t > m \, s$,}
    \\[2mm]

    n \, (t-m) ,
    &
    \text{if  $n \, t < m \, s$,}
  \end{cases}$$ and $T$-series is written in terms of the $L$-function associated with $\chi_{2 s t}^{(n,m)}$ as $$\begin{aligned}
  T^{(n,m)}(k)
  & =
  \frac{1}{2} \, (-1)^{k+1} \, L(-2 \, k -1 , \chi_{2 s t}^{(n,m)})
  \nonumber \\
  & =
  \frac{1}{2} \, (-1)^k \, \frac{(2 \, s \, t)^{2 k+1}}{2 \, k +2} \,
  \sum_{j=1}^{2 s t}
  \chi_{2 s t}^{(n,m)}(j) \,
  B_{2 k +2} \left( \frac{j}{2 \, s \, t} \right) .
\end{aligned}$$ This can be shown as follows (see Refs. ). We define a variant of the Eichler integral $$\label{variant_Eichler}
  \widehat{\Phi}^{(n,m)}(z)
  =
  \sqrt{\frac{s \, t \, \mathrm{i}}{8 \, \pi^2}}
  \,
  \int_{z^*}^\infty
  \frac{
    \Phi^{(n,m)}(\tau)
  }{
    (\tau - z)^{3/2}
  } \,
  \mathrm{d} \tau .$$ This function is defined for $z$ in the lower half plane, $z \in \mathbb{H}^-$, while the Eichler integral $\widetilde{\Phi}^{(n,m)}(z)$ is for the upper half plane, $z \in \mathbb{H}$. Using $S$-transformation [\[Phi_S_transform\]](#Phi_S_transform){reference-type="eqref" reference="Phi_S_transform"}, we have $$\label{Eichler_S_transform}
  \widehat{\Phi}^{(n,m)}(z)
  +
  \left(
    \frac{1}{\mathrm{i} \, z}
  \right)^{3/2} \,
  \sum_{n^\prime , m^\prime} \mathbf{S}_{n,m}^{n^\prime , m^\prime} \,
  \widehat{\Phi}^{(n^\prime , m^\prime)}(-1/z)
  =
  r^{(n,m)}(z; 0),$$ where we have defined the period function $$r^{(n,m)}(z; \alpha )
  =
  \sqrt{\frac{s \, t \, \mathrm{i}}{8 \, \pi^2}}
  \,
  \int_{\alpha}^\infty
  \frac{
    \Phi^{(n,m)}(\tau)
  }{
    (\tau - z)^{3/2}
  } \,
  \mathrm{d} \tau ,$$ for $z \in \mathbb{H}^-$ and $\alpha \in \mathbb{Q}$. More generally, for $\gamma = 
\begin{pmatrix}
  a & b \\
  c & d
\end{pmatrix}
\in
SL(2; \mathbb{Z})$, we have $$\widehat{\Phi}^{(n,m)}(z)
  -
  \frac{1}{v^{(n,m)}(\gamma)} \, (c \, z+ d)^{-3/2} \,
  \sum_{n^\prime , m^\prime}
  \left(
    \mathbf{M}_\gamma
  \right)_{n,m}^{n^\prime , m^\prime} \,
  \widehat{\Phi}^{(n^\prime , m^\prime)}  ( \gamma(z) )
  =
  r^{(n,m)}(z ; \gamma^{-1}(\infty)) ,$$ where a matrix $\mathbf{M}_\gamma$ and $v^{(n,m)}(\gamma)$ are given from the modular transformation, $$\sum_{n^\prime , m^\prime}
  \left(
    \mathbf{M}_\gamma
  \right)_{n, m}^{n^\prime ,m^\prime}
  \,
  \Phi^{(n^\prime, m^\prime)}(\gamma(z))
  =
  v^{(n, m)}(\gamma) \,
  \sqrt{c \, z + d} \,
  \Phi^{(n,m)}(z) .$$ When we substitute eq. [\[define_Phi\]](#define_Phi){reference-type="eqref" reference="define_Phi"} into eq. [\[variant_Eichler\]](#variant_Eichler){reference-type="eqref" reference="variant_Eichler"} and perform an integration term by term in a limit $z \to \alpha  \in \mathbb{Q}$, we see that $$\widetilde{\Phi}^{(n,m)}(\alpha)
  =
  \widehat{\Phi}^{(n,m)}(\alpha) ,$$ Note that the left hand side is given by eq. [\[Eichler_for_MN\]](#Eichler_for_MN){reference-type="eqref" reference="Eichler_for_MN"} as a limit value from $\mathbb{H}$ while the right hand side is a limit from $\mathbb{H}^-$. We can check for $N\in \mathbb{Z}$ that an asymptotic expansion of $r^{(n,m)}(1/N;0)$ gives a right hand side of eq. [\[nearly_modular_Phi\]](#nearly_modular_Phi){reference-type="eqref" reference="nearly_modular_Phi"}, and that from eq. [\[Eichler_for_MN\]](#Eichler_for_MN){reference-type="eqref" reference="Eichler_for_MN"} we have $$\begin{gathered}
  \widetilde{\Phi}^{(n,m)}(N+1)
  =
  \mathrm{e}^{\frac{(n t - m s)^2}{2 s t} \pi \mathrm{i}} \,
  \widetilde{\Phi}^{(n,m)}(N),
  \\[2mm]

  \widetilde{\Phi}^{(n,m)}(0)
  =
  \phi(n,m) ,
\end{gathered}$$ which shows $$\widetilde{\Phi}^{(n,m)}(N)
  =
  \phi(n,m) \,
  \mathrm{e}^{\frac{(n t - m s)^2}{2 s t} \pi \mathrm{i} N} .$$ Combining these results we recover eq. [\[nearly_modular_Phi\]](#nearly_modular_Phi){reference-type="eqref" reference="nearly_modular_Phi"}.

# Quantum Knot Invariant for Torus Knot {#sec_invariant}

We study the $N$-colored Jones polynomial $J_N(\mathcal{K})$ for the torus knot $\mathcal{K}=T(s,t)$. The torus knot $T(s,t)$ for coprime integers $s, t$ is the knot which wraps around the solid torus in the longitudinal direction $s$ times and in the meridinal direction $t$ times. See Fig. [\[fig:torus\]](#fig:torus){reference-type="ref" reference="fig:torus"}. It is also represented as $( \sigma_1 \, \sigma_2 \cdots \sigma_{s-1} )^t$ in terms of generators $\sigma_j$ of the Artin braid group. An explicit form of the $N$-colored Jones polynomial is read as [@Mort95a; @RossJone93a] $$\label{colored_polynomial}
  2 \mathop{\mathrm{sh}}(N \, \hbar /2) \,
  \frac{J_N(\mathcal{K})}{J_N(\mathcal{O})}
  = \mathrm{e}^{- \frac{\hbar}{4} (\frac{t}{s} + \frac{s}{t})} \,
  \sum_{\varepsilon = \pm 1}
  \sum_{k=-\frac{N-1}{2}}^{\frac{N-1}{2}}
  \varepsilon \,
  \exp
  \left(
    \hbar \, s \, t \,
    \left(
      k + \frac{ s + \varepsilon \, t}{2 \, s \, t}
    \right)^2
  \right) ,$$ where we have set a parameter $q=\mathrm{e}^\hbar$, and $\mathcal{O}$ denotes unknot. As was shown in Ref. , Kashaev's invariant [@Kasha95; @Kasha96b] coincides with a specialization $q \to \mathrm{e}^{2 \pi \mathrm{i}/N}$ of the colored Jones polynomial. As the left hand side of eq. [\[colored_polynomial\]](#colored_polynomial){reference-type="eqref" reference="colored_polynomial"} vanishes in this substitution, Kashaev's invariant for the torus knot can be computed as a derivative of the right hand side with respect to $\hbar$.

Here we recall the Eichler integral $\widetilde{\Phi}^{(n,m)}(1/N)$ which was computed in eq. [\[Eichler_for_MN\]](#Eichler_for_MN){reference-type="eqref" reference="Eichler_for_MN"}, and especially pay attention to a case of $(n,m)=(s-1, 1)$. Using a property of the Gauss sum, we obtain from eq. [\[Eichler_for_MN\]](#Eichler_for_MN){reference-type="eqref" reference="Eichler_for_MN"} $$\widetilde{\Phi}^{(s-1,1)}(1/N)
  =
  \frac{s \, t}{N} \,
  \mathrm{e}^{
    \frac{s t}{2} N \pi \mathrm{i} + (s+t)
    \pi \mathrm{i}
  }
  \sum_{\varepsilon=\pm 1}
  \sum_{k=-\frac{N-1}{2}}^{\frac{N-1}{2}}
  \varepsilon \,
  \left(
    k+ \frac{s + \varepsilon \, t}{2 \, s \, t}
  \right)^2 \,
  \mathrm{e}^{
    \frac{2 \pi \mathrm{i}}{N} s t
    \left( k + \frac{s + \varepsilon t}{2 s t} \right)^2
  } .$$ As seen from eq. [\[colored_polynomial\]](#colored_polynomial){reference-type="eqref" reference="colored_polynomial"}, this expression is proportional to the colored Jones polynomial at $\hbar \to 2 \, \pi \, \mathrm{i}/N$. To conclude Kashaev's invariant $\langle \mathcal{K} \rangle_N$ for torus knot $\mathcal{K}=T(s,t)$ is identified with $$\label{invariant_character}
  \mathrm{e}^{-\frac{(s t - s - t)^2}{2 s t N} \pi \mathrm{i}}
  \cdot
  \widetilde{\Phi}^{(s-1,1)}(1/N)
  =
  \langle T(s,t) \rangle_N .$$ We expect that the Eichler integrals $\widetilde{\Phi}^{(n,m)}(1/N)$ for other cases $(n,m)$ are related with the quantum invariants of 3-manifolds. As a result eq. [\[nearly_modular_Phi\]](#nearly_modular_Phi){reference-type="eqref" reference="nearly_modular_Phi"} denotes an asymptotic expansion of Kashaev's invariant in $N\to\infty$. Note that an asymptotic behavior was studied in Refs.  in a different manner.

In general, we can construct $q$-series for the Eichler integrals based on the $R$-matrix [@Kasha95]. We give some examples below (see Fig. [\[fig:torus\]](#fig:torus){reference-type="ref" reference="fig:torus"}). Hereafter we use a standard notation, $$\begin{gathered}
  (x)_k = (x ; q)_k = \prod_{j=1}^k (1- x \, q^{j-1}) ,
  \\[2mm]

  \begin{bmatrix}
    \  k  \  \\
    j
  \end{bmatrix}
  =
  \frac{ (q)_k}{ (q)_j \, (q)_{k-j} } .
\end{gathered}$$

-   Trefoil $T(2,3)$, $$\begin{aligned}
        \widetilde{\Phi}^{(1,1)}(\tau)
        & \equiv
        -\frac{1}{2} \, \sum_{k=0}^\infty k \, 
        \chi_{12}^{(1,1)}(k) \, q^{ k^2 / 24} 
        \\
        & =
        q^{1/24} \,
        \sum_{k=0}^\infty (q)_k .
      
    \end{aligned}$$ This equality is Zagier's "strange" identity [@DZagie01a]; though both expressions do not converge simultaneously, the limiting values in $q$ being roots of unity coincide. It is the Eichler integral of the Dedekind $\eta$-function.

-   Solomon's Seal knot $T(2,5)$, $$\begin{aligned}
          \widetilde{\Phi}^{(1,1)}(\tau)
          & \equiv
          -\frac{1}{2} \, \sum_{k=0}^\infty k \, 
          \chi_{20}^{(1,1)}(k) \, q^{ k^2 / 40} 
          \\
          & =
          q^{9/40} \,
          \sum_{k=0}^\infty (q)_k \,
          \sum_{j=0}^k q^{j (j+1)} \,
          \begin{bmatrix}
            \  k  \  \\
            j
          \end{bmatrix} ,
          \displaybreak[0]
          \\[2mm]

          \widetilde{\Phi}^{(1,2)}(\tau)
          & \equiv 
          -\frac{1}{2} \, \sum_{k=0}^\infty k \, 
          \chi_{20}^{(1,2)}(k) \, q^{ k^2 / 40} 
          \\
          & =
          q^{1/40} \,
          \sum_{k=0}^\infty (q)_k \,
          \sum_{j=0}^{k+1} q^{j^2} \,
          \begin{bmatrix}
            k+1 \\
            j
          \end{bmatrix}
          .
        
    \end{aligned}$$ The equalities in above formulae have same meaning with a case of trefoil [@KHikami02c]. These are the Eichler integral of the Rogers--Ramanujan $q$-series, which is the character of the Lee--Yang theory $\mathcal{M}(2,5)$.

-   Knot $T(3,4)$, $$\begin{aligned}
          \widetilde{\Phi}^{(1,1)}(\tau)
          & \equiv 
          -\frac{1}{2} \, \sum_{k=0}^\infty k \, 
          \chi_{24}^{(1,1)}(k) \, q^{ k^2 / 48} 
          \\
          & =
          q^{1/48} \,
          \sum_{k=0}^\infty (q)_k
          \,
          \left(
            \sum_{j=0}^{\lfloor k/2 \rfloor} q^{2 j^2} \, 
            \begin{bmatrix}
              k \\
              2 \, j
            \end{bmatrix}
            +
            \sum_{j=0}^{\lfloor (k+1)/2 \rfloor} q^{2 j^2} \, 
            \begin{bmatrix}
              k+1 \\
              2 \, j
            \end{bmatrix}
          \right) ,
          \displaybreak[0]
          \\[2mm]

          \widetilde{\Phi}^{(1,2)}(\tau)
          & \equiv 
          -\frac{1}{2} \, \sum_{k=0}^\infty k \, 
          \chi_{24}^{(1,2)}(k) \, q^{ k^2 / 48} 
          \\
          & =
          2 \, q^{1/12} \,
          \sum_{k=0}^\infty
          (q^2; q^2)_k ,
          \displaybreak[0]
          \\[2mm]

          \widetilde{\Phi}^{(1,3)}(\tau)
          & \equiv 
          -\frac{1}{2} \, \sum_{k=0}^\infty k \, 
          \chi_{24}^{(1,3)}(k) \, q^{ k^2 / 48} 
          \\
          & =
          q^{25/48} \,
          \sum_{k=0}^\infty (q)_k
          \,
          \left(
            \sum_{j=0}^{\lfloor (k-1)/2 \rfloor} q^{2 j (j+1)} \, 
            \begin{bmatrix}
              k \\
              2 \, j +1
            \end{bmatrix}
            +
            \sum_{j=0}^{\lfloor k /2 \rfloor} q^{2 j (j+1)} \, 
            \begin{bmatrix}
              k+1 \\
              2 \, j +1
            \end{bmatrix}
          \right) ,

        
    \end{aligned}$$ These are the Eichler integral of the Slater's $q$-series [@KHikami03b], which is the character of the Ising model $\mathcal{M}(3,4)$.

See that infinite sums in all those expressions reduce to a finite sum in a case $q \to \mathrm{e}^{2 \pi \mathrm{i}/N}$.

Asymptotic behavior of Kashaev's invariant, $$\lim_{N\to \infty} \frac{2 \, \pi}{N} \,
  \log
  \langle \mathcal{K} \rangle_N ,$$ is conjectured [@Kasha96b; @MuraMura99a] to give the hyperbolic volume of the knot complement $M= S^3 \setminus \mathcal{K}$. In our case, the torus knot is not hyperbolic. We can rather expect from eqs. [\[nearly_modular_Phi\]](#nearly_modular_Phi){reference-type="eqref" reference="nearly_modular_Phi"} and [\[invariant_character\]](#invariant_character){reference-type="eqref" reference="invariant_character"} that a value $$\label{log_limit_T}
  -\frac{(n  t - m  s)^2}{ s t} \, \pi^2 
  =
  - 4 \, \pi^2 \,
  \left(
    \Delta_{n,m}^{s,t} - \frac{c(s,t)-1}{24}
  \right) ,$$ is related to the SU(2) Chern--Simons invariant, $$\mathop{\mathrm{CS}}(M)
  =
  \frac{1}{4} \int\limits_{M} \mathop{\mathrm{Tr}}
  \left(
    A \land \mathrm{d} A +
    \frac{2}{3} \, A \land A \land A
  \right) .$$

To see this fact, we recall that the fundamental group of $M=S^3 \setminus T(s,t)$ has a presentation $$\label{group_torus}
  \pi_1(M)
  =
  \langle x , y | x^s = y^t \rangle .$$ As was shown in Ref. , the Chern--Simons invariant from two SU(2) representation $\rho_0$ and $\rho_1$ of $\pi_1(M)$ satisfies $$\label{CS_difference}
  \mathop{\mathrm{CS}}(M ; \rho_1)
  - \mathop{\mathrm{CS}}(M ; \rho_0)
  =
  - 4 \, \pi^2 \,
  \int_0^1 \beta(z) \, \alpha^\prime(z) \,
  \mathrm{d} z .$$ Here $\alpha(z)$ and $\beta(z)$ are from the representation $\rho_z$, $z \in [0,1]$, of the meridian $\mu$ and the longitude $\lambda$ up to conjugation, $$\begin{aligned}
  \rho_z(\mu)
  & =
  \begin{pmatrix}
    \mathrm{e}^{2 \pi \mathrm{i} \alpha(z)} &
    \\
    & \mathrm{e}^{-2 \pi \mathrm{i} \alpha(z)} 
  \end{pmatrix},

  &

  \rho_z(\lambda)
  & =
  \begin{pmatrix}
    \mathrm{e}^{2 \pi \mathrm{i} \beta(z)} &
    \\
    & \mathrm{e}^{-2 \pi \mathrm{i} \beta(z)} 
  \end{pmatrix} .
\end{aligned}$$ In a case of complement [\[group_torus\]](#group_torus){reference-type="eqref" reference="group_torus"} of the torus knot, the longitude $\lambda$ and the meridian $\mu$ are respectively given by $x^s$ and $x^a \, y^b$, where $a, b \in \mathbb{Z}$ satisfies $a \, s + b \,t =1$. As the longitude $\lambda=x^s=y^t$ is a center of group, it is sent to $\pm 1$. From relations $(x^a)^s = (x^s)^a$ and $(y^b)^t = (x^s)^b$ we see that $x^a$ and $y^b$ is conjugate to $$\begin{aligned}
  \rho(x^a)
  & \to 
  \begin{pmatrix}
    \mathrm{e}^{\pi \mathrm{i} n/s} &
    \\
    & \mathrm{e}^{- \pi \mathrm{i} n/s} 
  \end{pmatrix}  ,

  &

  \rho(y^b)
  & \to 
  \begin{pmatrix}
    \mathrm{e}^{\pi \mathrm{i} m/t} &
    \\
    & \mathrm{e}^{- \pi \mathrm{i} m/t} 
  \end{pmatrix}  ,
\end{aligned}$$ where $n, m$ are integers. Correspondingly we find that a path of representation from a trivial representation $z=0$ is given by $$\begin{aligned}
  \alpha(z)
  & =
  \frac{1}{2} \,
  \left(
    \frac{n}{s} + \frac{m}{t}
  \right)  \, z ,
  &

  \beta(z)
  & =
  \frac{s \, t}{2} \,
  \left(
    \frac{n}{s} + \frac{m}{t}
  \right)  .
\end{aligned}$$ Here $\beta(z)$ is constant along this path representation since the longitude is fixed to be $\pm 1$. Substituting into eq. [\[CS_difference\]](#CS_difference){reference-type="eqref" reference="CS_difference"}, we get a quantity [\[log_limit_T\]](#log_limit_T){reference-type="eqref" reference="log_limit_T"} as the Chern--Simons invariant of $M$ modulo $2 \, \pi^2$.

# Concluding Remarks

We have revealed intriguing properties of the character of the minimal model $\mathcal{M}(s,t)$. We have shown that Kashaev's invariant, *i.e.*, a specific value of the $N$-colored Jones polynomial, for the torus knot $T(s,t)$ is regarded as the Eichler integral of the character for $(n,m)=(s-1,1)$ with $q$ being the $N$-th root of unity. It is natural to expect that general $(n,m)$ case is also related to the quantum invariant of the 3-manifold.

As was shown in Ref. , the Eichler integral of the affine $\widehat{\mathrm{su}}(2)_{m+2}$ character,

which is modular covariant with weight $3/2$, gives Kashaev's invariant for torus link $T(2, 2\, m)$ when $q$ is the $N$-th primitive root of unity. As the torus knot and link are not hyperbolic, we may regard the hyperbolic manifold as a (massive) deformation of the conformal field theory.

# Acknowledgment

The authors would like to thank to H. Murakami for useful comments on early version of manuscript. The work of KH is supported in part by the Sumitomo Foundation, and Grant-in-Aid for Young Scientists from the Ministry of Education, Culture, Sports, Science and Technology of Japan.
