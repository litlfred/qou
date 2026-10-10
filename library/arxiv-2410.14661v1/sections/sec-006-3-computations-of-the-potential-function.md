---
doc_id: arxiv-2410.14661v1
doc_title: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eigh"
section_id: sec-006-3-computations-of-the-potential-function
section_title: "Computations of the potential function"
section_number: 3
pages: 8-15
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
text_source: latex
latex_prose_ratio: 0.901
latex_coverage_ratio: 0.792
doc_brief: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eight knot — This is"
---
[]{#Section-Potentialfunction label="Section-Potentialfunction"}

Let $M_{p,q}$ be the 3-manifold obtained by the doing $q$-surgery along the twist knot $\mathcal{K}_p$, (see Figure [1](#figure-twistknot){reference-type="ref" reference="figure-twistknot"}) where the index $p$ represents $2p$ crossings (half-twists). For example, $\mathcal{K}_{-1}=4_1$, $\mathcal{K}_1=3_1$, $\mathcal{K}_2=5_2$.

<figure id="figure-twistknot" data-latex-placement="!htb">
<p>.</p>
<figcaption>Twist knot <span class="math inline">𝒦<sub><em>p</em></sub></span></figcaption>
</figure>

Denoted by $(\mathcal{K}_p)_q$ the twist knot $\mathcal{K}_p$ with framing $q$, and $D_{(\mathcal{K}_p)_q}$ be its link diagram. By formula ([\[formula-RT\]](#formula-RT){reference-type="ref" reference="formula-RT"}), the $r$-th Reshetikhin-Turaev invariant of $M_{p,q}$ is given by $$\begin{align}
RT_r(M)=\mu_r\langle\Omega_r\rangle_{D_{(\mathcal{K}_p)_q}}\langle\Omega_r\rangle_{U_+}^{-\sigma((\mathcal{K}_p)_q)}.
\end{align}$$ A direct computation shows that $\langle\Omega_r\rangle_{U_+}=e^{\left(-\frac{3}{r}-\frac{r+1}{4}\right)\pi \sqrt{-1}}$. Let $\sigma_{p,q}=\sigma((\mathcal{K}_p)_q)$ and $$\begin{align}
    \kappa_r=\mu_r^2\langle\Omega_r\rangle_{U_+}^{-\sigma_{p,q}}=\left(\frac{\sin\frac{2\pi}{r}}{\sqrt{r}}\right)^2e^{\sigma_{p,q}\left(\frac{3}{r}+\frac{r+1}{4}\right)\pi\sqrt{-1}}.
\end{align}$$

Then we have $$\begin{align}
    RT_r(M_{p,q})&=\kappa_r\langle \omega_r\rangle_{D_{(\mathcal{K}_p)_q}}=\kappa_r\sum_{m=0}^{r-2}[m+1](-1)^{qm+1}t^{q\frac{m(m+2)}{4}}\langle e_{m}\rangle_{D_{(\mathcal{K}_p)_0}}.
\end{align}$$

Recall the definition of colored Jones polynomial [@CZ23-1], for a knot $\mathcal{K}$ with zero-framing, we have $$\begin{align}
[m+1]J_{m+1}(\mathcal{K};t)=\langle (-1)^me_m\rangle_{D_{\mathcal{K}}},
\end{align}$$ then we get $$\begin{align}
   RT_r(M)&=\kappa_r \sum_{m=0}^{r-2}[m+1]^2(-1)^{qm}t^{q\frac{m(m+2)}{4}}J_{m+1}(\mathcal{K}_p;t)\\\nonumber
   &=\frac{\kappa_r}{\sin^2 \left(\frac{\pi}{N+\frac{1}{2}}\right)}\sum_{m=0}^{2N-1}(-1)^{qm}\sin^2\left(\frac{(m+1)\pi}{N+\frac{1}{2}}\right)e^{\frac{qm(m+2)\pi\sqrt{-1}}{2(N+\frac{1}{2})}}J_{m+1}(\mathcal{K}_p;t)
\end{align}$$

And at the root of unity $t=e^{\frac{2\pi\sqrt{-1}}{N+\frac{1}{2}}}$, we have $$\begin{align}
  \label{formula-sumkl}
 J_{m}(\mathcal{K}_p;t)&=\sum_{k=0}^{m-1}\sum_{l=0}^k\frac{(-1)^{k+l}\sin \frac{\pi(2l+1)}{N+\frac{1}{2}}}{\sin \frac{m\pi }{N+\frac{1}{2}}}t^{(p+\frac{1}{2})l(l+1)-m(k+\frac{1}{2})+\frac{1}{2}k^2+\frac{3}{2}k+\frac{1}{2}}\\\nonumber
 &\cdot\frac{(t)_k(t)_{m+k}}{(t)_{k+l+1}(t)_{k-l}(t)_{m-k-1}}.
\end{align}$$

Therefore, let $a=N-1-m$, we obtain $$\begin{align}
RT_{r}(M_{p,q})&=\kappa_r'\sum_{a=-N}^{N-1}\sum_{k=0}^{N-a-1}\sum_{l=0}^k  (-1)^{q(N-1-a)+k+l}\sin\left(\frac{(a+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)\sin\left(\frac{2\pi(l+\frac{1}{2})}{N+\frac{1}{2}}\right)\\\nonumber
&\cdot t^{q\frac{(N-1-a)(N+1-a)}{4}+(p+\frac{1}{2})l(l+1)-(N-a)(k+\frac{1}{2})+\frac{1}{2}k^2+\frac{3}{2}k+\frac{1}{2}}  \frac{(t)_k(t)_{N-a+k}}{(t)_{k+l+1}(t)_{k-l}(t)_{N-a-k-1}},
\end{align}$$ where $$\begin{align}
 \label{formula-kappa'r}
\kappa'_r=\frac{\kappa_r}{\sin^2 \left(\frac{\pi}{N+\frac{1}{2}}\right)}.
\end{align}$$

Let $$\begin{align}
\theta_1=\frac{a+\frac{1}{2}}{N+\frac{1}{2}}, \ 
\theta_2=\frac{k+\frac{1}{2}}{N+\frac{1}{2}},  \ \theta_3=\frac{l+\frac{1}{2}}{N+\frac{1}{2}}.
\end{align}$$ Then we have $$\begin{align}
    &t^{q\frac{(N-1-a)(N+1-a)}{4}+(p+\frac{1}{2})l(l+1)-(N-a)(k+\frac{1}{2})+\frac{1}{2}k^2+\frac{3}{2}k+\frac{1}{2}}\\\nonumber
    &=e^{(N+\frac{1}{2})2\pi\sqrt{-1}\left(\frac{q}{4}(1+\theta_1^2-2\theta_1-\frac{1}{(N+\frac{1}{2})^2})+(p+\frac{1}{2})(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2})-\theta_2+\theta_2\theta_1+\frac{1}{2}\theta_2^2+\frac{\theta_2}{(N+\frac{1}{2})}-\frac{1}{8(N+\frac{1}{2})^2}\right)}.
\end{align}$$ Moreover, by using Lemma [\[lemma-varphixi\]](#lemma-varphixi){reference-type="ref" reference="lemma-varphixi"}, we have $$\begin{align}
    &\frac{(t)_k(t)_{N-a+k}}{(t)_{k+l+1}(t)_{k-l}(t)_{N-a-k-1}}\\\nonumber
    &=\exp\left(\varphi_N\left(\frac{(k+l+1)+\frac{1}{2}}{N+\frac{1}{2}}\right)+\varphi_N\left(\frac{(k-l)+\frac{1}{2}}{N+\frac{1}{2}}\right)-\varphi_N\left(\frac{\frac{1}{2}}{N+\frac{1}{2}}\right)\right.\\\nonumber
    &\left.-\varphi_N\left(\frac{k+\frac{1}{2}}{N+\frac{1}{2}}\right)-\varphi_N\left(\frac{(N-a+k)+\frac{1}{2}}{N+\frac{1}{2}}\right)+\varphi_N\left(\frac{(N-a-k-1)+\frac{1}{2}}{N+\frac{1}{2}}\right)\right)\\\nonumber
    &=e^{\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)-\varphi_N(\theta_2)-\varphi_N(1+\theta_2-\theta_1)}\\\nonumber
    &\cdot e^{(N+\frac{1}{2})(\frac{\pi\sqrt{-1}}{12}-\frac{\pi\sqrt{-1}}{4(N+\frac{1}{2})}+\frac{\pi\sqrt{-1}}{12(N+\frac{1}{2})^2})}(N+\frac{1}{2})^{-\frac{1}{2}}
\end{align}$$ for $0<k+l+1\leq N$ and $0<N-a+k<N$,

$$\begin{align}
    &\frac{(t)_k(t)_{N-a+k}}{(t)_{k+l+1}(t)_{k-l}(t)_{N-a-k-1}}\\\nonumber
    &=\exp\left(\varphi_N\left(\frac{(k+l+1)+\frac{1}{2}}{N+\frac{1}{2}}\right)+\varphi_N\left(\frac{(k-l)+\frac{1}{2}}{N+\frac{1}{2}}\right)+\varphi_N\left(\frac{(N-a-k-1)+\frac{1}{2}}{N+\frac{1}{2}}\right)\right.\\\nonumber
    &\left.-\varphi_N\left(\frac{k+\frac{1}{2}}{N+\frac{1}{2}}\right)-\varphi_N\left(\frac{(N-a+k)+\frac{1}{2}}{N+\frac{1}{2}}-1\right)-\varphi_N\left(\frac{\frac{1}{2}}{N+\frac{1}{2}}\right)+\log 2\right)\\\nonumber
    &=2e^{\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)}\\\nonumber
    &\cdot e^{(N+\frac{1}{2})(\frac{\pi\sqrt{-1}}{12}-\frac{\pi\sqrt{-1}}{4(N+\frac{1}{2})}+\frac{\pi\sqrt{-1}}{12(N+\frac{1}{2})^2})}(N+\frac{1}{2})^{-\frac{1}{2}}
\end{align}$$ for $0<k+l+1\leq N$ and $N<N-a+k<2N$,

$$\begin{align}
    &\frac{(t)_k(t)_{N-a+k}}{(t)_{k+l+1}(t)_{k-l}(t)_{N-a-k-1}}\\\nonumber
    &=\exp\left(\varphi_N\left(\frac{(k+l+1)+\frac{1}{2}}{N+\frac{1}{2}}-1\right)+\varphi_N\left(\frac{(k-l)+\frac{1}{2}}{N+\frac{1}{2}}\right)+\varphi_N\left(\frac{(N-a-k-1)+\frac{1}{2}}{N+\frac{1}{2}}\right)\right.\\\nonumber
    &\left.-\varphi_N\left(\frac{k+\frac{1}{2}}{N+\frac{1}{2}}\right)-\varphi_N\left(\frac{(N-a+k)+\frac{1}{2}}{N+\frac{1}{2}}\right)-\varphi_N\left(\frac{\frac{1}{2}}{N+\frac{1}{2}}\right)-\log 2\right)\\\nonumber
    &=\frac{1}{2}e^{\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)-\varphi_N(\theta_2)-\varphi_N(1+\theta_2-\theta_1)}\\\nonumber
    &\cdot e^{(N+\frac{1}{2})(\frac{\pi\sqrt{-1}}{12}-\frac{\pi\sqrt{-1}}{4(N+\frac{1}{2})}+\frac{\pi\sqrt{-1}}{12(N+\frac{1}{2})^2})}(N+\frac{1}{2})^{-\frac{1}{2}}
\end{align}$$ for $N<k+l+1\leq 2N$ and $0<N-a+k<N$,

$$\begin{align}
    &\frac{(t)_k(t)_{N-a+k}}{(t)_{k+l+1}(t)_{k-l}(t)_{N-a-k-1}}\\\nonumber
    &=\exp\left(\varphi_N\left(\frac{(k+l+1)+\frac{1}{2}}{N+\frac{1}{2}}-1\right)+\varphi_N\left(\frac{(k-l)+\frac{1}{2}}{N+\frac{1}{2}}\right)+\varphi_N\left(\frac{(N-a-k-1)+\frac{1}{2}}{N+\frac{1}{2}}\right)\right.\\\nonumber
    &\left.-\varphi_N\left(\frac{k+\frac{1}{2}}{N+\frac{1}{2}}\right)-\varphi_N\left(\frac{(N-a+k)+\frac{1}{2}}{N+\frac{1}{2}}-1\right)-\varphi_N\left(\frac{\frac{1}{2}}{N+\frac{1}{2}}\right)\right)\\\nonumber
    &=e^{\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)}\\\nonumber
    &\cdot e^{(N+\frac{1}{2})(\frac{\pi\sqrt{-1}}{12}-\frac{\pi\sqrt{-1}}{4(N+\frac{1}{2})}+\frac{\pi\sqrt{-1}}{12(N+\frac{1}{2})^2})}(N+\frac{1}{2})^{-\frac{1}{2}}
\end{align}$$ for $N<k+l+1\leq 2N$ and $N<N-a+k<2N$.

Since $$\begin{align}
     &e^{(N+\frac{1}{2})2\pi\sqrt{-1}\left(\frac{q}{2}(1-\theta_1-\frac{1}{N+\frac{1}{2}})+\frac{\theta_2+\theta_3}{2}-\frac{1}{2(N+\frac{1}{2})}\right)}\\\nonumber
     &
     \cdot e^{(N+\frac{1}{2})2\pi\sqrt{-1}\left(\frac{q}{4}(1+\theta_1^2-2\theta_1-\frac{1}{(N+\frac{1}{2})^2})+(p+\frac{1}{2})(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2})+\theta_2-\theta_2\theta_1+\frac{1}{2}\theta_2^2+\frac{\theta_2}{(N+\frac{1}{2})}-\frac{1}{8(N+\frac{1}{2})^2}\right)}
     \\\nonumber
     &\cdot e^{\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)}\\\nonumber
    &\cdot e^{(N+\frac{1}{2})(\frac{\pi\sqrt{-1}}{12}-\frac{\pi\sqrt{-1}}{4(N+\frac{1}{2})}+\frac{\pi\sqrt{-1}}{12(N+\frac{1}{2})^2})}(N+\frac{1}{2})^{-\frac{1}{2}}\\\nonumber
    &=(N+\frac{1}{2})^{-\frac{1}{2}}e^{(N+\frac{1}{2})\pi\sqrt{-1}\left(q(\frac{3}{2}-2\theta_1+\frac{\theta_1^2}{2}-\frac{1}{N+\frac{1}{2}}-\frac{1}{2(N+\frac{1}{2})^2})+(2p+1)(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2})-\theta_1+2\theta_2\theta_1+\theta_2^2+\theta_3+\frac{2\theta_2}{(N+\frac{1}{2})}\right)}\\\nonumber
    &\cdot e^{(N+\frac{1}{2})\pi\sqrt{-1}(-\frac{5}{4(N+\frac{1}{2})}-\frac{1}{6(N+\frac{1}{2})^2}+\frac{1}{12})},
\end{align}$$ finally, combining above formulas together, we obtain $$\begin{align}
&RT_{r}(M_{p,q})\\\nonumber
&=\kappa_r'(N+\frac{1}{2})^{-\frac{1}{2}}\sum_{a=-N}^{N-1}\sum_{k=0}^{N-a-1}\sum_{l=0}^k  (-1)^{q(N-1-a)+k+l}\sin\left(\frac{(a+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)\sin\left(\frac{2\pi(l+\frac{1}{2})}{N+\frac{1}{2}}\right)\\\nonumber
&\cdot t^{q\frac{(N-1-a)(N+1-a)}{4}+(p+\frac{1}{2})l(l+1)-(N-a)(k+\frac{1}{2})+\frac{1}{2}k^2+\frac{3}{2}k+\frac{1}{2}}  \frac{(t)_k(t)_{N-a+k}}{(t)_{k+l+1}(t)_{k-l}(t)_{N-a-k-1}}\\\nonumber
&=\kappa_r'(N+\frac{1}{2})^{-\frac{1}{2}}\sum_{a=-N}^{N-1}\sum_{k=0}^{N-a-1}\sum_{l=0}^k  \sin\left(\frac{(a+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)\sin\left(\frac{2\pi(l+\frac{1}{2})}{N+\frac{1}{2}}\right)e^{(N+\frac{1}{2})\tilde{V}_N(\frac{a+\frac{1}{2}}{N+\frac{1}{2}},\frac{k+\frac{1}{2}}{N+\frac{1}{2}},\frac{l+\frac{1}{2}}{N+\frac{1}{2}})},
\end{align}$$ where $\tilde{V}_{N}(\theta_1,\theta_2,\theta_3)$ is given by

- $$\begin{align*}
          &\pi\sqrt{-1}\left(q\left(\frac{3}{2}-2\theta_1+\frac{\theta_1^2}{2}-\frac{1}{N+\frac{1}{2}}-\frac{1}{2(N+\frac{1}{2})^2}\right)+(2p+1)\left(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2}\right)\right.\\\
      &\left.-\theta_2+2\theta_2\theta_1+\theta_2^2+\theta_3+\frac{2\theta_2}{N+\frac{1}{2}}-\frac{5}{4(N+\frac{1}{2})}-\frac{1}{6(N+\frac{1}{2})^2}+\frac{1}{12}\right)\\\nonumber
      &+\frac{1}{N+\frac{1}{2}}\left(\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)\right. \\\nonumber
      &\left.-\varphi_N(\theta_2)-\varphi_N(1+\theta_2-\theta_1)\right),
  \end{align*}$$ when $0<\theta_2+\theta_3<1$ and $0<1-\theta_1+\theta_2<1$;

- $$\begin{align*}
         &\pi\sqrt{-1}\left(q\left(\frac{3}{2}-2\theta_1+\frac{\theta_1^2}{2}-\frac{1}{N+\frac{1}{2}}-\frac{1}{2(N+\frac{1}{2})^2}\right)+(2p+1)\left(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2}\right)\right.\\\
      &\left.-\theta_2+2\theta_2\theta_1+\theta_2^2+\theta_3+\frac{2\theta_2}{N+\frac{1}{2}}-\frac{5}{4(N+\frac{1}{2})}-\frac{1}{6(N+\frac{1}{2})^2}+\frac{1}{12}\right)\\\nonumber
      &+\frac{1}{N+\frac{1}{2}}\left(\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)-\varphi_N(\theta_2)\right.\\\nonumber
      &\left.-\varphi_N(\theta_2-\theta_1)\right),
  \end{align*}$$ when $0<\theta_2+\theta_3<1$ and $1<1-\theta_1+\theta_2<2$;

- $$\begin{align*}
         &\pi\sqrt{-1}\left(q\left(\frac{3}{2}-2\theta_1+\frac{\theta_1^2}{2}-\frac{1}{N+\frac{1}{2}}-\frac{1}{2(N+\frac{1}{2})^2}\right)+(2p+1)\left(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2}\right)\right.\\\
      &\left.-\theta_2+2\theta_2\theta_1+\theta_2^2+\theta_3+\frac{2\theta_2}{N+\frac{1}{2}}-\frac{5}{4(N+\frac{1}{2})}-\frac{1}{6(N+\frac{1}{2})^2}+\frac{1}{12}\right)\\\nonumber
      &+\frac{1}{N+\frac{1}{2}}\left(\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})+\varphi_N(-\theta_1-\theta_2+1)\right.\\\nonumber
      &\left.-\varphi_N(\theta_2)-\varphi_N(1+\theta_2-\theta_1)\right),
  \end{align*}$$ when $1<\theta_2+\theta_3<2$ and $0<1-\theta_1+\theta_2<1$;

- $$\begin{align*}
         &\pi\sqrt{-1}\left(q\left(\frac{3}{2}-2\theta_1+\frac{\theta_1^2}{2}-\frac{1}{N+\frac{1}{2}}-\frac{1}{2(N+\frac{1}{2})^2}\right)+(2p+1)\left(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2}\right)\right.\\\
      &\left.-\theta_2+2\theta_2\theta_1+\theta_2^2+\theta_3+\frac{2\theta_2}{N+\frac{1}{2}}-\frac{5}{4(N+\frac{1}{2})}-\frac{1}{6(N+\frac{1}{2})^2}+\frac{1}{12}\right)\\\nonumber
      &+\frac{1}{N+\frac{1}{2}}\left(\varphi_N(t+u+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})\right.\\\nonumber
      &\left.+\varphi_N(-\theta_1-\theta_2+1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)\right),
  \end{align*}$$ when $1<\theta_2+\theta_3<2$ and $1<1-\theta_1+\theta_2<2$.

By Lemma [\[lemma-varphixi2\]](#lemma-varphixi2){reference-type="ref" reference="lemma-varphixi2"}, we have $$\begin{align}
    &\varphi_N(1-\theta_1-\theta_2)=-\varphi(\theta_1+\theta_2)\\\nonumber
    &+2\pi \sqrt{-1}\left(-\frac{2N+1}{4}\left((\theta_1+\theta_2)^2-(\theta_2+\theta_1)+\frac{1}{6}\right)+\frac{1}{12(2N+1)}\right)
\end{align}$$ since $\theta_1+\theta_2<1$.

Hence $$\begin{align}
&\tilde{V}_{N}(\theta_1,\theta_2,\theta_3)\\\nonumber
&=\pi\sqrt{-1}\left(q\left(\frac{3}{2}-2\theta_1+\frac{\theta_1^2}{2}-\frac{1}{N+\frac{1}{2}}-\frac{1}{2(N+\frac{1}{2})^2}\right)+(2p+1)\left(\theta_3^2-\frac{1}{4(N+\frac{1}{2})^2}\right)\right.\\\nonumber
    &\left.-\theta_1^2+\theta_1+\theta_3+\frac{2\theta_2}{N+\frac{1}{2}}-\frac{5}{4(N+\frac{1}{2})}-\frac{1}{12(N+\frac{1}{2})^2}-\frac{1}{12}\right)\\\nonumber
    &+\frac{1}{N+\frac{1}{2}}\left(\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})\right.\\\nonumber
    &\left.-\varphi_N(\theta_2+\theta_1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)\right),
\end{align}$$ for $1<\theta_2+\theta_3<2$ and $1<1-\theta_1+\theta_2<2$, and we can write the expression for $\tilde{V}_N$ for other cases similarly.

Then we introduce the functions $$\begin{align}
 \label{formula-VN}
   &\hat{V}_N(\theta_1,\theta_2,\theta_3)\\\nonumber
   &=\tilde{V}_N(\theta_1,\theta_2,\theta_3)+2(q-1)\pi\sqrt{-1}\left(\theta_1-\frac{\frac{1}{2}}{N+\frac{1}{2}}\right)-2\pi\sqrt{-1}\left(\theta_2-\frac{\frac{1}{2}}{N+\frac{1}{2}}\right)\\\nonumber
   &-2(p+2)\pi\sqrt{-1}\left(\theta_3-\frac{\frac{1}{2}}{N+\frac{1}{2}}\right) \\\nonumber
   &=\pi\sqrt{-1}\left(\left(\frac{q}{2}-1\right)\theta_1^2-\theta_1+(2p+1)\theta_3^2-(2p+3)\theta_3-2\theta_2+\frac{3}{2}q-\frac{1}{12}\right.\\\nonumber
   &\left.+\frac{2\theta_2}{N+\frac{1}{2}}+\frac{p-2q+\frac{9}{4}}{N+\frac{1}{2}}-\frac{3(p+q)+2}{6(N+\frac{1}{2})^2}\right)\\\nonumber
    &+\frac{1}{N+\frac{1}{2}}\left(\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})\right.\\\nonumber
    &\left.-\varphi_N(\theta_2+\theta_1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)\right)
\end{align}$$ and $$\begin{align}
&\hat{V}(\theta_1,\theta_2,\theta_3)\\\nonumber
&=\lim_{N\rightarrow \infty}V_{N}(\theta_1,\theta_2,\theta_3)\\\nonumber
&=\pi\sqrt{-1}\left(\left(\frac{q}{2}-1\right)\theta_1^2-\theta_1+(2p+1)\theta_3^2-(2p+3)\theta_3-2\theta_2+\frac{3}{2}q-\frac{1}{12}\right)\\\nonumber
   &+\frac{1}{2\pi\sqrt{-1}}\left(\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})\right.\\\nonumber
&\left.-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right)
\end{align}$$ for $1<\theta_2+\theta_3<2$ and $1<1-\theta_1+\theta_2<2$, and one can write the expression for $V_N$ and $V$ for other cases similarly.

::: proposition
[]{#Prop-RTN label="Prop-RTN"} Let $r=2N+1$ with $N\geq 1$, the $r$-th Reshetikhin-Turaev invariant of $M_{p,q}$ can be written as $$\begin{align}
   RT_{r}(M_{p,q})=\kappa_r'(N+\frac{1}{2})^{-\frac{1}{2}}\sum_{a=0}^{N-1}\sum_{k=0}^{N-a-1}\sum_{l=0}^kg_{N}(a,k,l)
\end{align}$$ with $$\begin{align}
 g_{N}(a,k,l)= \sin\left(\frac{(a+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)\sin\left(\frac{2\pi(l+\frac{1}{2})}{N+\frac{1}{2}}\right)e^{(N+\frac{1}{2})\hat{V}_N\left(\frac{a+\frac{1}{2}}{N+\frac{1}{2}},\frac{k+\frac{1}{2}}{N+\frac{1}{2}},\frac{l+\frac{1}{2}}{N+\frac{1}{2}}\right)},
\end{align}$$ where the function $\hat{V}_N(\theta_1,\theta_2,\theta_3)$ is given by formula ([\[formula-VN\]](#formula-VN){reference-type="ref" reference="formula-VN"}), and $\kappa'_r$ is given by ([\[formula-kappa\'r\]](#formula-kappa'r){reference-type="ref" reference="formula-kappa'r"}).
:::
