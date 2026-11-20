Let $\mathcal{S}$ denote Bring's surface ([Bring's surface](#def:brings-surface)). Let $q\in\mathbb{C}$ with $0<\lvert q\rvert\le 1$, and set $r=-\ln\lvert q\rvert$ so that $\lvert q\rvert=e^{-r}$. Write $\mathbf{i},\mathbf{j},\mathbf{k}$ for the standard basis of $\mathrm{Im}\mathbb{H}$. Using the Lusztig $q$-exponential and $q$-logarithm,

```tex
\begin{equation}\label{eq:q-exp}
  \exp_q(x)= \sum_{n=0}^{\infty}\frac{x^n}{[n]_q!},
  \qquad
  \ln_q(1+x)= \sum_{n=1}^{\infty}(-1)^{n+1}\frac{x^n}{[n]_q},
\end{equation}
```

define the **quaternionic spectral resolvents** $\omega_k\colon\mathcal{S}\to J^\infty E$ by

```tex
\begin{align}
  \omega_0 &= 
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}x_j\Bigr)
    \ln_q(1+r)
    &&\text{(uncertainty),}
    \label{eq:omega-0}\\[4pt]
  \omega_1 &= 
    \frac{\mathbf{i}}{\ln_q(1+r)}
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{j}x_j+i\Bigr)
    &&\text{(space-like),}
    \label{eq:omega-1}\\[4pt]
  \omega_2 &= 
    \mathbf{j}
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{2j}x_j+i\Bigr)
    \bigl(\exp_q(r)-1\bigr)
    &&\text{(time-like),}
    \label{eq:omega-2}\\[4pt]
  \omega_3 &= 
    \mathbf{k}
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{3j}x_j+i\Bigr)
    \bigl(\exp_q(r)-1\bigr)
    &&\text{(time-like).}
    \label{eq:omega-3}
\end{align}
```

By the first power sum, $\omega_0=0$ in the balanced state. The remaining coordinates embed $\mathcal{S}$ into the infinite jet shell $J^\infty E$ ([jet shell](#rem:jet-shell)).
