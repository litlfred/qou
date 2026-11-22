---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-021-54-the-fourier-transform-of-the-r-matrix
section_title: "The Fourier transform of the R-matrix"
section_number: 5.4
pages: 29-33
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.952
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:fourier-transform-R-mat label="sec:fourier-transform-R-mat"} In our computation of the $R$-matrix coefficients in [\[subsec:recurrences\]](#subsec:recurrences){reference-type="ref" reference="subsec:recurrences"} we used a nonstandard basis $\left\{ \def\given{\ \middle| \ }  \vbh n \given n \in \mathbb{Z}/N\mathbb{Z} \right\}$ Fourier dual to the usual highest-weight basis $\left\{ \def\given{\ \middle| \ }  \vb n \given n \in \mathbb{Z}/N\mathbb{Z} \right\}$. This turns out to give simpler relations that lead to the factorization of [\[thm:R-factorization\]](#thm:R-factorization){reference-type="ref" reference="thm:R-factorization"}. However to relate our construction to the standard one we need to return to the highest-weight basis. For a crossing with a geometrically degenerate coloring we explicitly recover the $R$-matrices defining the colored Jones polynomials and ADO invariants, generalizing a result of @Murakami2001.

::: definition
We say a $\chi$-colored crossing is if $a_{i} = m_{i}$ for each segment $i$ at the crossing. We say a log-coloring of it is if it satisfies $$\label{eq:standard-flattening-E-nilpotent}
    \alpha_{1} = \alpha_{1'} = \mu_{1}, \alpha_{2} = \alpha_{2'} = \mu_{2}.$$ the conditions of [\[def:standard-flattening\]](#def:standard-flattening){reference-type="ref" reference="def:standard-flattening"} on the log-parameters $\beta_{i}$ and the additional relations
:::

The generator $E \in \mathcal{U}_{\xi}$ acts nilpotently on every module $\rep{\chi_{i}, \mu_{i}}$ at an $E$-nilpotent crossing. When the holonomy $\rho$ is reducible one can always choose a $\chi$-coloring for which every crossing is pinched and $E$-nilpotent [@McPhailSnyderVolume] and a log-coloring for which every crossing is standard, i.e. satisfies both [\[eq:standard-flattening\]](#eq:standard-flattening){reference-type="eqref" reference="eq:standard-flattening"} and [\[eq:standard-flattening-E-nilpotent\]](#eq:standard-flattening-E-nilpotent){reference-type="eqref" reference="eq:standard-flattening-E-nilpotent"}.

::: theorem
[]{#thm:pinched-R-matrix-dual label="thm:pinched-R-matrix-dual"} At a positive crossing which is pinched, $E$-nilpotent, and has a standard log-coloring the coefficients of the $R$-matrix [\[eq:R-mat-positive\]](#eq:R-mat-positive){reference-type="eqref" reference="eq:R-mat-positive"} with respect to the bases $\left\{ \def\given{\ \middle| \ }  \vb{n} \right\}$ are $$\label{eq:nilpotent-R-matrix-dual}
    R_{n_1 n_2}^{n_1' n_2'}
    =
    \del{n_1 + n_2}{n_1' +  n_2'}
    \omega^{n_1'(-2 \mu_2 + n_2)}
    \frac{
      \qp{\omega^{-2\mu_2}}{n_2}
      \qp{\omega}{n_1}
      }{
      \qp{\omega^{-2\mu_2}}{n_2'}
      \qp{\omega}{n_2' - n_2}
      \qp{\omega}{n_1'}
    }$$ where we assume $n_j \in \left\{ \def\given{\ \middle| \ }  0, \dots, N-1 \right\}$.
:::

::: remark
When $\alpha_j = \mu_j = -1/2 \text{ or } (N- 1)/2$, we obtain $$\label{eq:colored-Jones-R-matrix}
    R_{n_1 n_2}^{n_1' n_2'}
    =
    \del{n_1 + n_2}{n_1' +  n_2'}
    \omega^{n_1'(1 + n_2)}
    \frac{
      \qp{\omega}{n_2}
      \qp{\omega}{n_1}
      }{
      \qp{\omega}{n_2'}
      \qp{\omega}{n_2' - n_2}
      \qp{\omega}{n_1'}
    }$$ which is the $R$-matrix defining a framed version of the $N$th colored Jones polynomial at an $N$th root of unity. This is the $n = m = -1$ case of [@Garoufalidis2021descendant eq.43]. More generally when $\mu_j$ is a half-integer our $R$-matrices appear to be equivalent to those of [@Garoufalidis2021descendant eq.43]. This may lead to a resolution of [@Garoufalidis2021descendant Conjecture 3.2].
:::

The proof (inspired by [@Garoufalidis2021descendant Section 3.2]) is a series of calculations involving terminating $q$-hypergeometric series. We break the computation into a few lemmas. Recall that the action of the $R$-matrix at a positive crossing is given by $$R(\vbh{n_1 n_2})
  =
  \sum_{n_1' n_2'}
  \widehat R_{n_1 n_2}^{n_1' n_2'}
  \vbh{n_1' n_2'}$$ where the matrix coefficients are given by [\[eq:R-mat-positive\]](#eq:R-mat-positive){reference-type="ref" reference="eq:R-mat-positive"}. From [\[eq:basis-and-dual-basis\]](#eq:basis-and-dual-basis){reference-type="eqref" reference="eq:basis-and-dual-basis"} it is immediate that the action in the highest-weight basis $$R(\vb{n_1 n_2})
  =
  \sum_{n_1' n_2'}
  R_{n_1 n_2}^{n_1' n_2'}
  \vb{n_1' n_2'}$$ has matrix coefficients $$\label{eq:fourier-dual-coefficients-definition}
  R_{n_1 n_2}^{n_1' n_2'}
  =
  \frac{1}{N^2}
  \sum_{k_1 k_2 k_1' k_2'}
  \omega^{n_1' k_1' + n_2' k_2' - n_1 k_1 - n_2 k_2}
  \rmat{k_1}{k_2}{k_1'}{k_2'}
  .$$ Our goal is to compute these in the pinched, $E$-nilpotent limit.

::: lemma
[]{#thm:fourier-dual-lemma-general label="thm:fourier-dual-lemma-general"} For any crossing the matrix coefficients [\[eq:fourier-dual-coefficients-definition\]](#eq:fourier-dual-coefficients-definition){reference-type="eqref" reference="eq:fourier-dual-coefficients-definition"} are given by $$\label{eq:fourier-dual-coefficients}
    \begin{aligned}
      R_{n_1 n_2}^{n_1' n_2'}
      =
      {}
      &
      -
      \nrdel{n_1 + n_2}{n_1' +  n_2'}
      \frac{
        \omega^{\Theta/2}
      }{
        N^{2}
      }
      \frac{
        \qlog{\nu_{2}}{N}
      }{
        \qlog{\zeta_{\lS}^{0} - \zeta_{\lW}^{0}}{N- 1}
      }
      \frac{
        \pf{\zeta_{\lN}^0}
        \pf{\zeta_{\lS}^0}
      }{
        \pf{\zeta_{\lE}^0}
        \pf{\zeta_{\lW}^0}
      }
      \\
      &\times
      \omega^{\nu_{2} + (n_{2} - 1) \zeta_{\lW}^{0} - n_{2}' (\zeta_{\lE}^{0} + 1) }
      \frac{
        \qlog{\nu_{2'}}{-n_2'}
        \qlog{-\nu_{2}}{n_2 - 1}
      }{
        \qlog{-\zeta + \nu_{2'} - 1}{- n_2'}
        \qlog{\zeta - \nu_{2} - 1}{n_2 }
      }
      \\
      &\times
      \fstack{ \zeta - \nu_{2'} + n_{2}' }{ \zeta - \nu_{2} -1 + n_{2} }{ \nu_{1'} - n_{1}' }
      \fstack{\zeta_{\lN}^0 }{\zeta_{\lE}^0}{- \nu_{2'}}
      \fstack{\zeta_{\lS}^0 }{\zeta_{\lW}^0}{\nu_{2}}
    \end{aligned}$$ where $\Theta$ is as in [\[thm:R-mat-phi-form\]](#thm:R-mat-phi-form){reference-type="ref" reference="thm:R-mat-phi-form"}, $\zeta = \zeta_{\lE}^{0} - \zeta_{\lN}^{0} = \zeta_{\lS} - \zeta_{\lW}^{0}$, and $$\fstack{\alpha}{\beta}{\gamma} \mathrel{:=}
  \sum_{n = 0}^{N-1}
  \frac{
    \qlog{\alpha}{n}
    }{
    \qlog{\beta}{n}
  }
  \omega^{n \gamma}$$ is the function studied by @Kashaev1993, discussed here in [\[sec:fusion-identities\]](#sec:fusion-identities){reference-type="ref" reference="sec:fusion-identities"}.
:::

::: proof
*Proof.* Use [\[thm:R-mat-phi-form\]](#thm:R-mat-phi-form){reference-type="ref" reference="thm:R-mat-phi-form"} to write $$\begin{aligned}
    \rmat{k_1}{k_2}{k_1'}{k_2'}
    &=
    \frac{
      \omega^{\Theta/2}
      \omega^{-N\zeta_{\lW}^0}
    }{
      N
    }
    (1 - \omega^{N\zeta_{\lW}^0})
    \\
    &\phantom{=}\times
    \omega^{
      k_1(\alpha_1-\mu_1 - 1)
      +
      k_2(\alpha_2 + \mu_2 + 1)
      -
      k_1' (\alpha_{1'} - \mu_{1})
      -
      k_2' (\alpha_{2'} + \mu_2)
    }
    \\
    &\phantom{=}\times
    \frac{
      \pf{\zeta_{\lN}^0 + k_2' - k_1}
      \pf{\zeta_{\lS}^0 + k_2 - k_1'}
      }{
        \pf{\zeta_{\lE}^0 + k_2' - k_1'}
        \pf{\zeta_{\lW}^0 + k_2 - k_1 - 1}
    }
  \end{aligned}$$ Setting $$\begin{aligned}
  \nu_{1}
    &=
    \alpha_1 - \mu_1
    &
    \nu_{1'}
    &=
    \alpha_{1'} - \mu_1
    \\
    \nu_{2}
    &=
    \alpha_2 + \mu_2
    &
    \nu_{2'}
    &=
    \alpha_{2'} + \mu_2
\end{aligned}$$ and changing summation variables to $k_2 = k_1 + t$, $k_1' = k_1 - k$, $k_2' = k_1 - k + t'$ shows that $$\begin{aligned}
    R_{n_1 n_2}^{n_1' n_2'}
    =
    &
    {}
    \frac{
      \omega^{\Theta/2}
      \omega^{-N\zeta_{\lW}^0}
    }{
      N^{3}
    }
    (1 - \omega^{N\zeta_{\lW}^0})
    \sum_{k_1}
    \omega^{k_1(n_1' + n_2' -n_1 -n_2)}
    \\
    &\times
    \sum_{k, t, t'}
    \omega^{k(\nu_{1'} + \nu_{2'} - n_1' - n_2')}
    \omega^{t(\nu_2 + 1 - n_2)}
    \omega^{t'(n_2' - \nu_{2'})}
    \frac{
      \pf{\zeta_{\lN}^0 + t' - k}
      \pf{\zeta_{\lS}^0 + t + k}
      }{
      \pf{\zeta_{\lE}^0 + t'}
      \pf{\zeta_{\lW}^0 - 1 + t}
    }
  \end{aligned}$$ We can apply the identity $$\sum_{k_1}
  \omega^{k_1(n_1' + n_2' -n_1 -n_2)}
  =
  N\nrdel{n_1 + n_2}{n_1' +  n_2'}$$ and the relation [\[eq:pf-recurrence\]](#eq:pf-recurrence){reference-type="eqref" reference="eq:pf-recurrence"} to see that $$\begin{aligned}
    R_{n_1 n_2}^{n_1' n_2'}
    =
    &
    {}
    \frac{
      \omega^{\Theta/2}
      \omega^{-N\zeta_{\lW}^0}
    }{
      N^{2}
    }
    (1 - \omega^{N\zeta_{\lW}^0})
    \nrdel{n_1 + n_2}{n_1' +  n_2'}
    \\
    &\times
    \sum_{k}
    \left\{
    \begin{aligned}
      &
      \omega^{k(\nu_{1} + \nu_{2} - n_1 - n_2)}
      \frac{
        \pf{\zeta_{\lN}^0 - k}
        \pf{\zeta_{\lS}^0 + k}
        }{
          \pf{\zeta_{\lE}^0}
          \pf{\zeta_{\lW}^0 - 1 }
      }
      \\
      &\times
      \sum_{t'}
      \omega^{t'(n_2' - \nu_{2'})}
      \frac{
        \qlog{\zeta_{\lN}^0 - k}{t'}
        }{
        \qlog{\zeta_{\lE}^0}{t'}
      }
      \\
      &\times
      \sum_{t}
      \omega^{t(\nu_2 + 1 - n_2)}
      \frac{
        \qlog{\zeta_{\lS}^0 + k}{t}
        }{
        \qlog{\zeta_{\lW}^0 - 1}{t}
      }
    \end{aligned}
    \right.
  \end{aligned}$$

The sums over $t$ and $t'$ can be written in terms of the function $\fstacksmall{\alpha}{\beta}{\gamma}$ of [\[sec:fusion-identities\]](#sec:fusion-identities){reference-type="ref" reference="sec:fusion-identities"}. As $$\fstack{\zeta_{\lN}^0 - k}{\zeta_{\lE}^0}{n_2' - \nu_{2'}}
  =
  \fstack{\zeta_{\lN}^0 }{\zeta_{\lE}^0}{- \nu_{2'}}
  \frac{
    \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 - 1}{-k}
    \qlog{\nu_{2'}}{-n_2'}
  }{
    \omega^{n_2'(\zeta_{\lE}^0 + 1)}
    \qlog{\zeta_{\lN}^0}{-k}
    \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 + \nu_{2'} - 1}{-k - n_2'}
  }$$ and $$\fstack{\zeta_{\lS}^0 + k}{\zeta_{\lW}^0 - 1}{\nu_2 - n_2 + 1}
  =
  \fstack{\zeta_{\lS}^0 }{\zeta_{\lW}^0}{\nu_{2}}
  \frac{
    \qlog{\zeta_{\lS}^0 - \zeta_{\lW}^0 - 1}{k + 1}
    \qlog{\zeta_{\lW}^{0} - 1}{-1}
    \qlog{-\nu_{2}}{n_2 - 1}
  }{
    \omega^{- \nu_{2} + (1 - n_2)\zeta_{\lW}^0}
    \qlog{\zeta_{\lS}^0}{k}
    \qlog{\zeta_{\lS}^0 - \zeta_{\lW}^0 - \nu_{2} - 1}{k + n_2}
  }$$ we can substitute and apply some algebraic manipulations to get $$\begin{aligned}
      R_{n_1 n_2}^{n_1' n_2'}
      =
      {}
      &
      \nrdel{n_1 + n_2}{n_1' +  n_2'}
      \frac{
        \omega^{\Theta/2}
      }{
        N^{2}
      }
      \frac{
        (1 - \omega^{N\zeta_{\lW}^0})
      }{
        \omega^{N\zeta_{\lW}^0}
        (1 - \omega^{\zeta_{\lS}^{0} - \zeta_{\lW}^0})
      }
      \frac{
        \pf{\zeta_{\lN}^0}
        \pf{\zeta_{\lS}^0}
      }{
        \pf{\zeta_{\lE}^0}
        \pf{\zeta_{\lW}^0}
      }
      \fstack{\zeta_{\lN}^0 }{\zeta_{\lE}^0}{- \nu_{2'}}
      \fstack{\zeta_{\lS}^0 }{\zeta_{\lW}^0}{\nu_{2}}
      \\
      &\times
      \omega^{\nu_{2} + (n_{2} - 1) \zeta_{\lW}^{0} - n_{2}' (\zeta_{\lE}^{0} + 1) }
      \qlog{\nu_{2'}}{-n_2'}
      \qlog{-\nu_{2}}{n_2 - 1}
      \\
      &\times
      \sum_{k}
      \frac{
        \omega^{k(\nu_{1} + \nu_{2} - n_1 - n_2)}
        \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0- 1}{-k}
        \qlog{\zeta_{\lS}^0 - \zeta_{\lW}^0}{k}
      }{
        \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 + \nu_{2'} - 1}{-k - n_2'}
        \qlog{\zeta_{\lS}^0 - \zeta_{\lW}^0 - \nu_{2} - 1}{k + n_2 }
      }
    \end{aligned}$$ The constant can be further simplified by applying [\[eq:b-transf-positive\]](#eq:b-transf-positive){reference-type="ref" reference="eq:b-transf-positive"} to write $$\begin{aligned}
    \frac{
      (1 - \omega^{N\zeta_{\lW}^0})
    }{
      \omega^{N\zeta_{\lW}^0}
      (1 - \omega^{\zeta_{\lS}^{0} - \zeta_{\lW}^0})
    }
    &=
    \frac{
      (1 - \omega^{N\zeta_{\lW}^0})
    }{
      \omega^{N\zeta_{\lW}^0}
      (1 - \omega^{N(\zeta_{\lS}^{0} - \zeta_{\lW}^0)})
      \qlog{\zeta_{\lS}^{0} - \zeta_{\lW}^{0}}{N- 1}
    }
    \\
    &=
    \frac{
      1
      }{
        (a_{2} m_{2} - 1)
      \qlog{\zeta_{\lS}^{0} - \zeta_{\lW}^{0}}{N- 1}
    }
    \\
    &=
    -
    \frac{
      \qlog{\nu_{2}}{N}
      }{
      \qlog{\zeta_{\lS}^{0} - \zeta_{\lW}^{0}}{N- 1}
    }
  
\end{aligned}$$ Now $$\qlog{\zeta}{m + n} = \qlog{\zeta}{m}\qlog{\zeta+m}{n}$$ and the inversion relation $$\qlog{\alpha}{-k}
    =
    \omega^{k \alpha} (-1)^{k} \omega^{k(k+1)/2} \qlog{-\alpha}{k}$$ shows that $$\begin{aligned}
    &\frac{
      \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0- 1}{-k}
    }{
      \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 + \nu_{2'} - 1}{-k - n_2'}
    }
    \\
    &=
    \frac{
      \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0- 1}{-k}
    }{
      \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 + \nu_{2'} - 1}{- n_2'}
      \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 + \nu_{2'} - 1 - n_{2}'}{-k }
    }
    \\
    &=
    \omega^{k(n_{2}' - \nu_{2'})}
    \frac{
      \qlog{\zeta_{\lE}^0 - \zeta_{\lN}^0 - \nu_{2'} + n_{2}'}{k }
    }{
      \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 + \nu_{2'} - 1}{- n_2'}
      \qlog{\zeta_{\lE}^0 - \zeta_{\lN}^0}{k}
    }
  
\end{aligned}$$ so using $\nu_{1} + \nu_{2} - \nu_{2'} = \nu_{1'}$ and $\zeta_{\lE}^{0} + \zeta_{\lW}^{0} = \zeta_{\lN}^0 + \zeta_{\lS}^0$ we get $$\begin{aligned}
      R_{n_1 n_2}^{n_1' n_2'}
      =
      {}
      &
      -
      \nrdel{n_1 + n_2}{n_1' +  n_2'}
      \frac{
        \omega^{\Theta/2}
      }{
        N^{2}
      }
      \frac{
        \qlog{\nu_{2}}{N}
      }{
        \qlog{\zeta_{\lS}^{0} - \zeta_{\lW}^{0}}{N- 1}
      }
      \frac{
        \pf{\zeta_{\lN}^0}
        \pf{\zeta_{\lS}^0}
      }{
        \pf{\zeta_{\lE}^0}
        \pf{\zeta_{\lW}^0}
      }
      \fstack{\zeta_{\lN}^0 }{\zeta_{\lE}^0}{- \nu_{2'}}
      \fstack{\zeta_{\lS}^0 }{\zeta_{\lW}^0}{\nu_{2}}
      \\
      &\times
      \omega^{\nu_{2} + (n_{2} - 1) \zeta_{\lW}^{0} - n_{2}' (\zeta_{\lE}^{0} + 1) }
      \frac{
        \qlog{\nu_{2'}}{-n_2'}
        \qlog{-\nu_{2}}{n_2 - 1}
        }{
        \qlog{\zeta_{\lN}^0 - \zeta_{\lE}^0 + \nu_{2'} - 1}{- n_2'}
        \qlog{\zeta_{\lS}^0 - \zeta_{\lW}^0 - \nu_{2} - 1}{n_2 }
      }
      \\
      &\times
      \sum_{k}
        \omega^{k(\nu_{1'} - n_1' )}
      \frac{
        \qlog{\zeta_{\lE}^0 - \zeta_{\lN}^0 - \nu_{2'} + n_{2}'}{k }
      }{
        \qlog{\zeta_{\lS}^0 - \zeta_{\lW}^0 - \nu_{2} - 1+ n_2 }{k }
      }
  
\end{aligned}$$ as claimed. ◻
:::

::: lemma
[]{#thm:fourier-dual-lemma-pinched label="thm:fourier-dual-lemma-pinched"} Suppose that our crossing is pinched and has a standard flattening. Then the matrix coefficients [\[eq:fourier-dual-coefficients-definition\]](#eq:fourier-dual-coefficients-definition){reference-type="eqref" reference="eq:fourier-dual-coefficients-definition"} are given by $$\label{eq:fourier-dual-coefficients-pinched}
    R_{n_{1} n_{2}}^{n_{1}' n_{2}'}
    =
    \frac{
      \nrdel{n_1 + n_2}{n_1' +  n_2'}
      }{
      N
    }
    \frac{
      1- \omega^{-N\nu_{2'}}
      }{
      1- \omega^{-\nu_{2'} + n_{2}'}
    }
    \fstack{- \nu_{2'} + n_{2}' }{- \nu_{2} + n_{2} - 1}{\nu_{1'} - n_{1}' }$$
:::

::: proof
*Proof.* We are taking the limit where all $\zeta_{i}^{0} \to 0$, which gives $$\begin{aligned}
      R_{n_1 n_2}^{n_1' n_2'}
      =
      {}
      &
      -
      \nrdel{n_1 + n_2}{n_1' +  n_2'}
      \frac{
        1
      }{
        N^{2}
      }
      \frac{
        \qlog{\nu_{2}}{N}
      }{
        N^{-1}
      }
      \\
      &\times
      \omega^{\nu_{2} }
      \frac{
        \qlog{\nu_{2'}}{-n_2'}
        \qlog{-\nu_{2}}{n_2 - 1}
      }{
        \qlog{\nu_{2'} - 1}{- n_2'}
        \qlog{- \nu_{2} - 1}{n_2 }
      }
      \\
      &\times
      \fstack{- \nu_{2'} + n_{2}' }{ - \nu_{2} -1 + n_{2} }{ \nu_{1'} - n_{1}' }
      \frac{
        1 - \omega^{-N\nu_{2}'}
        }{
        1 - \omega^{-\nu_{2}'}
      }
      \frac{
        1 - \omega^{N\nu_{2}}
        }{
        1 - \omega^{\nu_{2}}
      }
    \end{aligned}$$ because $$\fstack{\zeta_{\lS}^0 }{\zeta_{\lW}^0}{\nu_{2}}
    \to
    \sum_{k=0}^{N- 1}
    \frac{
      \qlog{0}{k}
      }{
      \qlog{0}{k}
    }
    \omega^{\nu_{2} k}
    =
    \frac{
      1 - \omega^{N\nu_{2}}
    }{
      1 - \omega^{\nu_{2}}
    }$$ and similarly for $-\nu_{2'}$. Simplifying gives the claim. ◻
:::

::: proof
*Proof of [\[thm:pinched-R-matrix-dual\]](#thm:pinched-R-matrix-dual){reference-type="ref" reference="thm:pinched-R-matrix-dual"}.* Finally we take the limit of the matrix coefficients [\[eq:fourier-dual-coefficients-pinched\]](#eq:fourier-dual-coefficients-pinched){reference-type="eqref" reference="eq:fourier-dual-coefficients-pinched"} where the crossing is $E$-nilpotent. Since we have a standard flattening [\[eq:standard-flattening-E-nilpotent\]](#eq:standard-flattening-E-nilpotent){reference-type="eqref" reference="eq:standard-flattening-E-nilpotent"} gives $\nu_{2} = \nu_{2'}  = 2 \mu_{2}$ and $\nu_{1'} = 0$, so using [\[eq:fusion-identity-ii\]](#eq:fusion-identity-ii){reference-type="ref" reference="eq:fusion-identity-ii"} the coefficients become $$\begin{aligned}
    R_{n_{1} n_{2}}^{n_{1}' n_{2}'}
    =
    \nrdel{n_1 + n_2}{n_1' +  n_2'}
    \frac{
      1- \omega^{-\nu_{2} + n_{2}}
      }{
      1- \omega^{-\nu_{2} + n_{2}'}
    }
    \frac{
      \omega^{ \modb{n_{1}'}(-\nu_{2} + n_{2})}
    }{
      \qlog{-\nu_{2} + n_{2}}{ \modb{n_{2}' - n_{2}} }
    }
    \frac{
      \qp{\omega}{\modb{n_2' - n_2} + \modb{n_1'}}
    }{
      \qp{\omega}{\modb{n_2' - n_2}}
      \qp{\omega}{\modb{n_1'}}
    }
  
\end{aligned}$$ Because our indices lie in $\left\{ \def\given{\ \middle| \ }  0, \dots, N-1 \right\}$ we can assume that $\modb{n_1'} = n_1'$. In addition, $\modb{n_2' - n_2} = \modb{n_1 - n_1'}$ because $n_1 + n_2 \equiv n_1' + n_2' \pmod N$. Furthermore, if $n_1 < n_1'$, then $$\modb{n_1 - n_1'} + n_1' = N+ n_1 \ge N- 1$$ so $$\qp{\omega}{\modb{n_2' - n_2} + \modb{n_1'}} = 0
    \text{ if }
    n_1 < n_1'.$$

For $n_1, n_2, n_1', n_2' \in \left\{ \def\given{\ \middle| \ }  0, \dots, N-1 \right\}$ the conditions $n_1 + n_2 \equiv n_1' + n_2' \pmod N$ and $n_1 \ge n_1'$ are equivalent to $n_1 + n_2 = n_1' + n_2'$ and $n_2' \ge n_2$, and we conclude that $$\begin{aligned}
    R_{n_{1} n_{2}}^{n_{1}' n_{2}'}
    =
    \del{n_1 + n_2}{n_1' +  n_2'}
    \frac{
      1- \omega^{-\nu_{2} + n_{2}}
      }{
      1- \omega^{-\nu_{2} + n_{2}'}
    }
    \frac{
      \omega^{ n_{1}'(n_{2} - \nu_{2})}
    }{
      \qlog{-\nu_{2} + n_{2}}{ n_{2}' - n_{2} }
    }
    \frac{
      \qp{\omega}{n_{1}}
    }{
      \qp{\omega}{n_2' - n_2}
      \qp{\omega}{n_1'}
    }
  
\end{aligned}$$ because if $n_2' < n_2$, we can use $$\frac{1}{\qp{\omega}{-k}} = (1 - 1) (1 - \omega^{-1}) \cdots (1 - \omega^{-(k-1)}) = 0 \text{ for } k > 0.$$ Finally, re-writing $$\begin{aligned}
    \frac{
      1 - \omega^{-\nu_2 + n_2}
    }{
      1 - \omega^{-\nu_2 +  n_2'}
    }
    \frac{
      1
    }{
      \qlog{-\nu_2 + n_2}{n_2' - n_2}
    }
    =
    \frac{
      \qp{\omega^{-\nu_2}}{n_2}
    }{
      \qp{\omega^{-\nu_2}}{n_2'}
    }
  
\end{aligned}$$ gives the claim. ◻
:::
