---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-024-46-invariance-of-the-perturbation-series-pnr
section_title: "Invariance of the Perturbation Series PN(r)"
section_number: 4.6
pages: 89-93
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.974
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Let us write $$\mathcal{P}_N(r)\, =\, \sum_{\sigma \in \{+1,-1\}^{N-1}} \mathcal{P}_N(\sigma;r)\, ,$$ for $$\mathcal{P}_N(\sigma;r)\,
=\, 
\left(\prod_{n=0}^{N-2} \frac{\lambda_n^{\sigma(n)}}{\lambda_n^+}\right)
\frac{([W_0^{\sigma(0)}]^* e_2) (e_2^* V_{N-2}^{\sigma(N-2)})}{([W_0^{+}]^* e_2) (e_2^* V_{N-2}^{+})}
\cdot \left(\prod_{n=0}^{N-1} \frac{[W_{n+1}^{\sigma(n+1)}]^* V_n^{\sigma(n)}}
{[W_{n+1}^{+}]^* V_n^{+}}\right)\, .$$ Let us think of $\sigma$ as a sequence of switches, from the $+$ state to the $-$ state, or vice-versa.

Using the notation $t_n = n/N$ and $T_n = N^{1/2} (t_n-r^2)$, we may write $$\begin{split}
[W_{n+1}^{\tau}]^* (V_n^{\sigma}-V_{n+1}^{\sigma})\,
&=\, -\frac{\tau N^{-1/2}}{2 \sqrt{T_{n+1}^2+4r^2}}
\left(1+\sigma\, \frac{T_{n}+T_{n+1}}{\sqrt{T_{n}^2+4r^2}+\sqrt{T_{n+1}^2+4r^2}}\right)\\
&=\, -\frac{\tau}{2 \sqrt{T_{n+1}^2+4r^2}}
\left(1+\sigma\, \frac{T_{n}+T_{n+1}}{\sqrt{T_{n}^2+4r^2}+\sqrt{T_{n+1}^2+4r^2}}\right)\, \Delta T_n\, ,
\end{split}$$ where we define $\Delta T_n = T_{n+1}-T_n=N^{-1/2}$. This means that in a time $\Delta T_n$ there is a factor proportional to $\Delta T_n$ contributing to $\mathcal{P}_N(\sigma;r)$, if we switch from $\sigma=+$ to $\tau=-$ or from $\sigma=-$ to $\tau=+$ because in these cases $[W_{n+1}^{\tau}]^*V_{n+1}^{\sigma}=0$. This is representative of a Poisson process of jumps.

Moreover, if at $a$ one jumps from $+$ to $-$ and at $b$ one jumps back to $+$, then for all $n \in \{a,\dots,b-1\}$ there is a contribution to $\mathcal{P}_N(\sigma;r)$ equal to $$\begin{split}
\frac{\lambda_n^{-}}{\lambda_n^+}
\cdot \frac{[W_{n+1}^{-}]^* V_n^{-}}
{[W_{n+1}^{+}]^* V_n^{+}}\, 
&=\, \frac{r^2+\frac{1}{2}N^{-1/2}T_{n+1}-\frac{1}{2}N^{-1/2}\sqrt{T_{n+1}^2+4r^2}}
{r^2+\frac{1}{2}N^{-1/2}T_{n+1}+\frac{1}{2}N^{-1/2}\sqrt{T_{n+1}^2+4r^2}}\\
&\qquad \qquad
\cdot \frac{1 + \frac{1}{2\sqrt{T_{n+1}^2+4r^2}}
\left(1- \frac{T_{n}+T_{n+1}}{\sqrt{T_{n}^2+4r^2}+\sqrt{T_{n+1}^2+4r^2}}\right)\, \Delta T_n}
{1 - \frac{1}{2\sqrt{T_{n+1}^2+4r^2}}
\left(1+ \frac{T_{n}+T_{n+1}}{\sqrt{T_{n}^2+4r^2}+\sqrt{T_{n+1}^2+4r^2}}\right)\, \Delta T_n}\, ,
\end{split}$$ and this quantity is asymptotic to $\exp\left(-\left[\frac{\sqrt{T_{n+1}^2+4r^2}}{r^2+\frac{1}{2}N^{-1/2}T_{n+1}}
-\frac{1}{\sqrt{T_{n+1}^2+4r^2}}\right] \Delta T_n\right)$, when one takes $N \to \infty$ if one also takes a sequence of $T_{n_N}$ such that $|T_{n_N}|/N^{1/2} \to 0$. Moreover the product is decreasing very rapidly as $|T_n|$ gets large on an order-1 scale. Therefore, the correction to this asymptotic formula is neglible, for the purpose of calculating the leading order behavior of $\mathcal{P}_N(r)$. Therefore, defining $\mathcal{P}^{++}_N(r)$ to be the sum of those $\mathcal{P}_N(\sigma;r)$ with $\sigma$ starting at $+$ at the left endpoint and returning to $+$ at the right endpoint, with some number of intervals of $-$ in between, we have the effect of switching from $+$ to $-$, staying at $-$ for an interval, and then switching back. This gives $$\begin{split}
\lim_{N \to \infty} \mathcal{P}^{++}_N(r)\,
&=\, 1 + \sum_{K=1}^{\infty} \int_{-\infty<S_1<\dots<S_{2K}<\infty}
\prod_{k=1}^{K} \left[\frac{1}{2\sqrt{S_{2k-1}^2+4r^2}}\left(1+\frac{S_{2k-1}}{\sqrt{S_{2k-1}^2+4r^2}}\right)\right]\\
&\hspace{3cm}
\exp\left(-\sum_{k=1}^{K}\int_{S_{2k-1}}^{S_{2k}} \left[\frac{\sqrt{s^2+4r^2}}{r^2} - \frac{1}{\sqrt{s^2+4r^2}}\right]\, ds\right)\\
&\hspace{3cm}
\prod_{k=1}^{K} \left[-\frac{1}{2\sqrt{S_{2k}^2+4r^2}}\left(1-\frac{S_{2k}}{\sqrt{S_{2k}^2+4r^2}}\right)\right]\, 
dS_1\, \cdots\, dS_{2n}\\
&=\, 1 + \sum_{K=1}^{\infty} (-1)^K \int_{-\infty<x_1<\dots<x_{2K}<\infty}
\prod_{k=1}^{K} \left(\frac{1}{[1+\exp(-2x_{2k-1})][1+\exp(2x_{2k})]}\right)\\
&\hspace{3cm}
\exp\left(-\sum_{k=1}^{K} \int_{x_{2k-1}}^{x_{2k}} [4 \cosh^2(x)-1]\, dx\right)\, dx_1\, \cdots\, dx_{2K}\, ,
\end{split}$$ where we made the change of variables $S_k = 2r \sinh(x_k)$, which is useful, as we have also mentioned before. Let us comment on where the $r$-dependence went. In fact the limits of integration for $S_1$ and $S_{2K}$ should be $-r^2N^{1/2}<S_1$ and $S_{2K}<(1-r^2)N^{1/2}$. Since the exponentials are negative (and growing in magnitude), the integrand is converging rapidly. Therefore, we can replace the limits of integration, by allowing integrals over all space, with a correction due to the tails of the integrals which are exponentially small. Then the substitution we have made from $S_k$ to $x_k$ eliminates the $r$ dependence, entirely. Finally, we mention that we can do the integral in the exponential to simplify the formula, a bit: $$\begin{gathered}
\lim_{N \to \infty} \mathcal{P}^{++}_N(r)\, \\
=\, 1 + \sum_{K=1}^{\infty} (-1)^K \int_{-\infty<x_1<\dots<x_{2K}<\infty}
\exp\left(\sum_{k=1}^{K} \left[
-\ln\left(1+e^{-2x_{2k-1}}\right)+\sinh(2x_{2k-1})-x_{2k-1}\right]\right)
\\
\exp\left(-\sum_{k=1}^{K} \left[
\ln\left(1+e^{2x_{2k}}\right)+\sinh(2x_{2k})-x_{2k}\right]\right)
\, dx_1\, \cdots\, dx_{2K}\\
=\, 1 + \sum_{K=1}^{\infty} (-1)^K \\ \cdot\int_{-\infty<x_1<\dots<x_{2K}<\infty}
e^{-\sum_{k=1}^{K} \left(\ln[\cosh(x_{2k-1})]+\ln[\cosh(x_{2k})]+\sinh(2x_{2k})-\sinh(2x_{2k-1})\right)}
\, dx_1\, \cdots\, dx_{2K}\, .
\end{gathered}$$ Again, note that this is rapidly decreasing as $x_1 \to -\infty$ or $x_{2K} \to \infty$. To get the analogous terms $\mathcal{P}^{+-}_N(r)$, $\mathcal{P}^{-+}_N(r)$ and $\mathcal{P}^{--}_N(r)$, we can just alter this formula essentially by taking $x_1 \to -\infty$ or $x_{2K} \to \infty$ or both. (This is not entirely correct because we lose terms corresponding to the density for crossing, but morally it is still correct because the terms remaining are certainly going to $0$.) Therefore $$\lim_{N \to \infty} \mathcal{P}_N(r)\,
=\, \lim_{N \to \infty} \mathcal{P}_N^{++}(r)\, .$$ Since we know that $\lim_{N \to \infty} \mathcal{R}_N^{(1)}(r)$ must equal $\pi^{-1}$ on the disk (for instance because the area of the disk is 1) this leaves the calculation to show that $$\begin{gathered}
1  + \sum_{K=1}^{\infty} (-1)^K \int_{-\infty<x_1<\dots<x_{2K}<\infty}
e^{-\sum_{k=1}^{K} \left(\ln[\cosh(x_{2k-1})]+\ln[\cosh(x_{2k})]+\sinh(2x_{2k})-\sinh(2x_{2k-1})\right)}
dx_1\cdots dx_{2K}\\
\stackrel{?}{=}\, \frac{\sqrt{2\pi}}{e}\, .
\end{gathered}$$ At this time we cannot see a direct method to prove this, but we hope to explore it in a later paper.
