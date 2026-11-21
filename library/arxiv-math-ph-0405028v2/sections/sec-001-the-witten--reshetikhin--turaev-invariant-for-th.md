---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-001-the-witten--reshetikhin--turaev-invariant-for-th
section_title: "The Witten--Reshetikhin--Turaev Invariant for the Brieskorn Homology Spheres"
section_number: null
pages: 3-7
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.982
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshetikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ(p1, p2, p3)"
---
[]{#sec:invariant label="sec:invariant"}

We introduce the Reshetikhin--Turaev invariant $\tau_N(\mathcal{M})$ [@ResheTurae91a] for $N\in\mathbb{Z}_+$. This is related to the Witten invariant $Z_k(\mathcal{M})$ defined in eq. [\[Witten\]](#Witten){reference-type="eqref" reference="Witten"} as $$\label{Witten_and_tau}
  Z_k(\mathcal{M})
  =
  \frac{
    \tau_{k+2}(\mathcal{M})
  }{
    \tau_{k+2}(S^2 \times S^1)
  }$$ Here the invariant is normalized to be $$\begin{gathered}
  \tau_N (S^3) =1
\end{gathered}$$ and we have $$\begin{gathered}

  \tau_N(S^2 \times S^1)
  =
  \sqrt{\frac{N}{2}} \, \frac{1}{\sin(\pi/N)}
\end{gathered}$$

When the 3-manifold $\mathcal{M}$ is constructed by the rational surgeries $p_j / q_j$ on the $j$-th component of $n$-component link $\mathcal{L}$, it was shown [@ResheTurae91a; @LCJeff92a] that the invariant $\tau_N(\mathcal{M})$ is given by $$\label{define_invariant}
  \tau_N(\mathcal{M})
  =
  \mathrm{e}^{
    \frac{\pi \mathrm{i}}{4} \frac{N-2}{N}
    \left(
      \sum_{j=1}^n \Phi(U^{(p_j,q_j)})
      -3 \mathop{\mathrm{sign}}(\mathbf{L})
    \right)
  }


  \sum_{k_1, \dots, k_n=1}^{N-1}
  J_{k_1,\dots,  k_n}(\mathcal{L}) \,
  \prod_{j=1}^n
  \rho(U^{(p_j,q_j)})_{k_j, 1}$$ Here the surgery $p_j/q_j$ is described by an $SL(2; \mathbb{Z})$ matrix $$U^{(p_j,q_j)}=
  \begin{pmatrix}
    p_j & r_j \\
    q_j & s_j
  \end{pmatrix}$$ and $\Phi(U)$ is the Rademacher $\Phi$-function defined by (see, *e.g.*, Ref. ) $$\Phi
  \left[
    \begin{pmatrix}
      p & r \\
      q & s
    \end{pmatrix}
  \right]
  =
  \begin{cases}
    \displaystyle
    \frac{p+s}{q} - 12 \, s(p, q) &
    \text{for $q \neq 0$}
    \\[3mm]

    \displaystyle
    \frac{r}{s}
    &
    \text{for $q=0$}
  \end{cases}$$ where $s(b,a)$ denotes the Dedekind sum (see, *e.g.*, Ref. , and also Ref. ) $$\begin{aligned}
  \label{Dedekind_sum}
  s(b,a)
  & =
  \mathop{\mathrm{sign}}(a)
  \sum_{k=1}^{|a|-1}
  \Bigl(\Bigl( \frac{k}{a} \Bigr) \Bigr) \cdot
  \Bigl(\Bigl( \frac{k \, b}{a} \Bigr) \Bigr) 
\end{aligned}$$ with $$((x))
  =
  \begin{cases}
    x - \lfloor x \rfloor - \frac{1}{2}
    &
    \text{if $x \not\in \mathbb{Z}$}
    \\[3mm]
    0
    &
    \text{if $x \in \mathbb{Z}$}
  \end{cases}$$ and $\lfloor x \rfloor$ is the greatest integer not exceeding $x$. It is known that the Dedekind sum is rewritten as $$s(b,a)
  =
  \frac{1}{4 \, a}
  \sum_{k=1}^{a-1}
  \cot \left( \frac{ k}{a}  \, \pi \right) \,
  \cot \left( \frac{ k \, b }{a} \, \pi \right)$$ An $n\times n$ matrix $\mathbf{L}$ is a linking matrix $\mathbf{L}_{j,k} = \mathrm{lk}_{j,k} + {p_j}/{q_j} \cdot \delta_{j,k}$, and $\mathop{\mathrm{sign}}(\mathbf{L})$ is a signature of $\mathbf{L}$, *i.e.*, the difference between the number of positive and negative eigenvalues of $\mathbf{L}$. The polynomial $J_{k_1,\dots,k_n}(\mathcal{L})$ is the colored Jone polynomial for link $\mathcal{L}$ with the color $k_j$ for the $j$-th component link, and $\rho(U^{(p,q)})$ is a representation $\rho$ of $PSL(2;\mathbb{Z})$; $$\begin{gathered}
  \rho(U^{(p,q)})_{a,b}
  \\
  =
  - \mathrm{i} \frac{\mathop{\mathrm{sign}}(q)}{\sqrt{2 \, N \, | q|}} \,
  \mathrm{e}^{
    -\frac{\pi \mathrm{i}}{4} \, \Phi(U^{(p,q)})
  } \,
  \mathrm{e}^{
    \frac{\pi \mathrm{i}}{2 N q} s b^2 
  } \,
  \sum_{
    \substack{
      \gamma \mod 2 N q
      \\
      \gamma = a \mod 2 N}
  }
  \mathrm{e}^{
    \frac{\pi \mathrm{i}}{2 N q}
    p \gamma^2
  } \,
  \left(
    \mathrm{e}^{
      \frac{\pi \mathrm{i}}{ N q}
       \gamma b
    }
    -
    \mathrm{e}^{
      - \frac{\pi \mathrm{i}}{ N q}
      \gamma b
    }
  \right)
\end{gathered}$$ for $1 \leq a, b \leq N-1$ [@LCJeff92a], and we have $$\label{affine_su}
  \begin{gathered}
    \rho(S)_{a,b}
    =
    \sqrt{\frac{2}{N}} \,
    \sin
    \left( \frac{ a \, b \, \pi}{N} \right)
    \\[2mm]

    \rho(T)_{a,b}
    =
    \mathrm{e}^{\frac{\pi \mathrm{i}}{2 N} a^2 - \frac{\pi \mathrm{i}}{4}}
    \,
    \delta_{a,b}
  \end{gathered}$$ with $$\begin{aligned}
  \label{PSL_ST}
  S
  &=
  \begin{pmatrix}
    0 & -1 \\
    1 & 0
  \end{pmatrix}
  &
  T 
  & =
  \begin{pmatrix}
    1 & 1 \\
    0 & 1
  \end{pmatrix}
\end{aligned}$$ satisfying $$S^2 = (S \, T)^3 = 1$$

We should note [@RademGross72] that the Dedekind sum satisfies $$\begin{gathered}
  s(-b, a )= - s (b,a)
  \\[2mm]

  s(b,a) = s(b^\prime, a) \quad
  \text{for $b \, b^\prime \equiv 1 \pmod{a}$
  }
\end{gathered}$$ and that the Rademacher $\Phi$-function fulfills $$\Phi
  (S \,  U^{(p, q)})
  =
  \Phi
  (  U^{(p, q)})
  - 3 \, \mathop{\mathrm{sign}}(p \, q)$$

::: prop
The WRT invariant for the Brieskorn homology spheres is given by $$\begin{gathered}
    \label{Rozansky}
    \mathrm{e}^{
      \frac{2 \pi \mathrm{i}}{N}
      ( \frac{\phi}{4} - \frac{1}{2} )
    } \,
    \left(
      \mathrm{e}^{\frac{2 \pi \mathrm{i}}{N}} - 1
    \right)
    \,    \tau_N \bigl( \Sigma(p_1,p_2,p_3) \bigr)
    \\
    =
    \frac{\mathrm{e}^{\pi \mathrm{i}/4}}{2 \, \sqrt{2 \, P \, N}}
    \,
    \sum_{\substack{
        n= 0 \\
        N \, \nmid \, n
    }}^{2 \, P \, N-1 }
    \mathrm{e}^{- \frac{1}{2 P N} n^2 \pi \mathrm{i} }
    \frac{
      \prod_{j=1}^3
      \left(
        \mathrm{e}^{\frac{  n}{N p_j} \pi \mathrm{i}}
        -
        \mathrm{e}^{- \frac{ n}{N p_j} \pi \mathrm{i} }
      \right)
    }{
      \mathrm{e}^{\frac{n}{N} \pi \mathrm{i}}
      -
      \mathrm{e}^{ - \frac{ n}{N} \pi \mathrm{i}}
    }
  
\end{gathered}$$ where $$\label{phi_definition}
    \phi
    =
    \phi(p_1, p_2, p_3)
    =
    3 - \frac{1}{P}
    +
    12 \, \bigl(
    s(p_2 \, p_3 , p_1) +
    s(p_1 \, p_3 , p_2) +
    s(p_1 \, p_2 , p_3) 
    \bigr)$$
:::

::: proof
*Proof.* This was proved in Refs.  for a general $n$-fibered manifold, but we give a proof here again for completion.

The Jones polynomial for a link $\mathcal{L}$ depicted in Fig. [\[fig:Brieskorn\]](#fig:Brieskorn){reference-type="ref" reference="fig:Brieskorn"} is given by $$J_{k_0, k_1,k_2,k_3}(\mathcal{L})
    =
    \frac{1}{\sin (\pi/N)} \cdot
    \frac{
      \prod_{j=1}^3
      \sin
      \left( k_0 \, k_j \, \pi/N \right)
    }{
      \sin^2 \left(
        k_0 \, \pi / N
      \right)
    }$$ where $k_0$ is a color of an unknotted component whose linking number with other components is $1$, and $k_j$ (for $j=1,2,3$) denotes a color of a component of link $\mathcal{L}$ which is to be $p_j/q_j$-surgery. With this setting we have $$\mathop{\mathrm{sign}}(\mathbf{L})
    = 
    \sum_{j=1}^3 \mathop{\mathrm{sign}}\left(\frac{q_j}{p_j}\right)
    -1$$ From [\[define_invariant\]](#define_invariant){reference-type="eqref" reference="define_invariant"} we get the quantum invariant as $$\begin{gathered}
    \left(
      \mathrm{e}^{\pi \mathrm{i}/N}
      -
      \mathrm{e}^{- \pi \mathrm{i}/N}
    \right) \cdot
    \tau_N \bigl(
    \Sigma(p_1, p_2, p_3)
    \bigr)
    \\
    =
    \mathrm{e}^{
      \frac{\pi \mathrm{i}}{4} \frac{N-2}{N}
      \left(
        3  + \sum_{j=1}^3 \Phi(S U^{(p_j,q_j)})
      \right)
    }


    \sum_{k_0=1}^{N-1}
    \frac{
      \rho(S)_{k_0,1}
    }{
      \left(
        \mathrm{e}^{\frac{\pi \mathrm{i}}{N} k_0}
        -
        \mathrm{e}^{- \frac{\pi \mathrm{i}}{N} k_0}
      \right)^2
    } \,
    \\
    \times
    \prod_{j=1}^3 \sum_{k_j=1}^{N-1}
    \rho(U^{(p_j,q_j)})_{k_j,1} \,
    \left(
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N} k_0 k_j}
      -
      \mathrm{e}^{ -\frac{\pi \mathrm{i}}{N} k_0 k_j}
    \right)
  
\end{gathered}$$ In this expression we have by definition $$\rho(S)_{k_0,1}
    =
    \frac{- \mathrm{i}}{\sqrt{2 \, N}} \,
    \left(
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N} k_0}
      -
      \mathrm{e}^{-\frac{\pi \mathrm{i}}{N} k_0}
    \right)$$ and for $\ell \in \mathbb{Z}$ we have $$\begin{aligned}
    & \sum_{k=1}^{N-1}
    \rho(U^{(p,q)})_{k,1} \,
    \left(
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N} \ell k}
      -
      \mathrm{e}^{ -\frac{\pi \mathrm{i}}{N} \ell k}
    \right)
    \\
    & =
    -\mathrm{i} \,
    \mathrm{e}^{-\frac{\pi \mathrm{i}}{4} \Phi(U^{(p,q)})
      +
      \frac{\pi \mathrm{i} s}{2 N q}}
    \,
    \frac{\mathop{\mathrm{sign}}(q)}{\sqrt{2 \, N \, | q|}} \,
    \sum_{k=1}^{N-1}
    \sum_{
      \substack{
        \gamma \mod 2 N q \\
        \gamma \equiv k \mod 2 N}}
    \mathrm{e}^{\frac{ \pi \mathrm{i} p}{2 N q} \gamma^2}
    \left(
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N q} \gamma}
      -
      \mathrm{e}^{ -\frac{\pi \mathrm{i}}{N q} \gamma}
    \right) \,
    \left(
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N} \ell \gamma}
      -
      \mathrm{e}^{ -\frac{\pi \mathrm{i}}{N} \ell \gamma}
    \right)       
    \\
    & =
    -\mathrm{i} \,
    \mathrm{e}^{-\frac{\pi \mathrm{i}}{4} \Phi(U^{(p,q)})
      +
      \frac{\pi \mathrm{i} s}{2 N q}
    }
    \,
    \frac{\mathop{\mathrm{sign}}(q)}{\sqrt{2 \, N \, | q|}} \,
    \sum_{\gamma \mod 2 N q}
    \mathrm{e}^{\frac{\pi \mathrm{i}}{2 N q} p \gamma^2} \,
    \left(
      \mathrm{e}^{2 \pi \mathrm{i} \frac{q \ell +1 }{2 N q}  \gamma}
      -
      \mathrm{e}^{2 \pi \mathrm{i} \frac{q \ell -1 }{2 N q}  \gamma}
    \right)
    \\
    & =
    -\frac{\mathop{\mathrm{sign}}(p)}{\sqrt{|p|}} \,
    \mathrm{e}^{
      -\frac{\pi \mathrm{i}}{4} 
      \Phi(S U^{(p,q)})
      +
      \frac{\pi \mathrm{i} s}{2 N q}
    }
    \sum_{n \mod p}
    \left(
      \mathrm{e}^{-\frac{\pi \mathrm{i}}{2 p q N}
        (2 N q n + q \ell+1)^2
      }
      -
      \mathrm{e}^{-\frac{\pi \mathrm{i}}{2 p q N}
        (2 N q n + q \ell-1)^2
      }
    \right)
  
\end{aligned}$$ Here in the first equality we have used $\gamma=k \pmod{ 2 \, N}$, and applied a symmetry under $\gamma \to 2 \, N \, q- \gamma$ in the second equality. In the last equality, we have used an identity $\mathrm{e}^{\frac{\pi \mathrm{i}}{2} (1-\mathop{\mathrm{sign}}(p))}
  =
  \mathop{\mathrm{sign}}(p)$, and the Gauss sum reciprocity formula [@LCJeff92a] $$\label{Gauss_sum_formula}
    \sum_{n \mod N}
    \mathrm{e}^{\frac{\pi \mathrm{i}}{N} M n^2 + 2 \pi \mathrm{i} k n}
    =
    \sqrt{
      \left|
        \frac{N}{M}
      \right|
    } \,
    \mathrm{e}^{\frac{\pi \mathrm{i}}{4} \mathop{\mathrm{sign}}(N M)}
    \sum_{n \mod M}
    \mathrm{e}^{
      -\frac{\pi \mathrm{i}}{M}
      N (n+k)^2
    }$$ where $N, M\in \mathbb{Z}$ with $N \, k \in \mathbb{Z}$ and $N \, M$ being even.

A combination of these results reduces to $$\begin{gathered}
    \left(
      \mathrm{e}^{\pi \mathrm{i}/N}
      -
      \mathrm{e}^{- \pi \mathrm{i}/N}
    \right) \cdot
    \tau_N \bigl(
    \Sigma(p_1, p_2, p_3)
    \bigr)
    \\
    =
    \frac{\mathrm{i} \, \mathop{\mathrm{sign}}(P)}{
      \sqrt{2 \, |P| \, N}}
    \,
    \mathrm{e}^{
      \frac{3}{4} \pi \mathrm{i} 
      +\frac{\pi \mathrm{i}}{2 N} \sum_j \frac{1}{p_j q_j}
      -
      \frac{\pi \mathrm{i}}{2 N} \phi
    }


    \sum_{k_0=1}^{N-1}
    \sum_{n_j \mod p_j}
    \frac{1}{
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N} k_0}
      -
      \mathrm{e}^{- \frac{\pi \mathrm{i}}{N} k_0}
    }
    \,
    \\
    \times
    \prod_{j=1}^3
    \left(
      \mathrm{e}^{-\frac{\pi \mathrm{i}}{2 N p_j q_j}
        (2 N q_j n_j + k_0 q_j +1)^2
      }
      -
      \mathrm{e}^{-\frac{\pi \mathrm{i}}{2 N p_j q_j}
        (2 N q_j n_j + k_0 q_j -1)^2
      }
    \right)
  
\end{gathered}$$ The summand is invariant under (i) $k_0 \to k_0 + 2 \, N$ and $n_j\to n_j -1$, (ii) $n_j  \to n_j + p_j$. Using this symmetry and recalling that $p_j$ are pairwise coprime integers, the sum, $\sum_{k_0=1}^{N-1}
  \sum_{n_j \mod{ p_j}}$, is transformed into a sum, $\sum_{
    \substack{
      k_0 = a + 2 N n \\
      1 \leq a \leq N-1 \\
      0 \leq n \leq P-1
    }}$, with setting all $n_j=0$. As a result, we find $$\begin{gathered}
    \left(
      \mathrm{e}^{\pi \mathrm{i}/N}
      -
      \mathrm{e}^{- \pi \mathrm{i}/N}
    \right) \cdot
    \tau_N \bigl(
    \Sigma(p_1, p_2, p_3)
    \bigr)
    \\
    =
    -\frac{\mathrm{i}}{
      \sqrt{2 \, P \, N}}
    \,
    \mathrm{e}^{
      \frac{3}{4} \pi \mathrm{i} 
      -
      \frac{\pi \mathrm{i}}{2 N} \phi
    }
    \,
    \sum_{
      \substack{
        k_0 = a + 2 N n \\
        1 \leq a \leq N-1 \\
        0 \leq n \leq P-1
      }}
    \mathrm{e}^{-\frac{\pi \mathrm{i}}{2 N P} k_0^{~2}}
    \,
    \frac{
    \prod_{j=1}^3
    \left(
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N p_j} k_0}
      -
      \mathrm{e}^{-\frac{\pi \mathrm{i}}{N p_j} k_0}
    \right)
    }{
      \mathrm{e}^{\frac{\pi \mathrm{i}}{N} k_0}
      -
      \mathrm{e}^{- \frac{\pi \mathrm{i}}{N} k_0}
    }
  
\end{gathered}$$ Setting $k_0\to 2 \, P \, N- k_0$, we obtain a statement of the proposition. ◻
:::
