---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-003-22-dilogarithm-and-lobachevsky-functions
section_title: "Dilogarithm and Lobachevsky functions"
section_number: 2.2
pages: 6-7
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.872
---
Let $\log: \mathbb{C}\setminus (-\infty,0]\rightarrow \mathbb{C}$ be the standard logarithm function defined by $$\begin{aligned}
    \log z=\log |z|+\sqrt{-1}\arg z
\end{aligned}$$ with $-\pi <\arg z<\pi$.

The dilogarithm function $\text{Li}_2: \mathbb{C}\setminus (1,\infty)\rightarrow \mathbb{C}$ is defined by $$\begin{aligned}
    \text{Li}_2(z)=-\int_0^{z}\frac{\log(1-x)}{x}dx
\end{aligned}$$ where the integral is along any path in $\mathbb{C}\setminus (1,\infty)$ connecting $0$ and $z$, which is holomorphic in $\mathbb{C}\setminus [1,\infty)$ and continuous in $\mathbb{C}\setminus (1,\infty)$.

The dilogarithm function satisfies the following properties $$\begin{aligned}
    \text{Li}_2\left(\frac{1}{z}\right)=-\text{Li}_2(z)-\frac{\pi^2}{6}-\frac{1}{2}(\log(-z) )^2.
\end{aligned}$$ In the unit disk $\{z\in \mathbb{C}| |z|<1\}$, $\text{Li}_2(z)=\sum_{n=1}^{\infty}\frac{z^n}{n^2}$, and on the unit circle $$\begin{aligned}
 \{z=e^{2\pi \sqrt{-1}\theta}|0 \leq \theta\leq 1\},    
\end{aligned}$$ we have $$\begin{aligned}
    \text{Li}_2(e^{2\pi\sqrt{-1} \theta})=\frac{\pi^2}{6}+\pi^2\theta(\theta-1)+2\pi \sqrt{-1}\Lambda(\theta)
\end{aligned}$$ where $$\begin{aligned}
 \label{formula-Lambda(t)}
\Lambda(\theta)=\text{Re}\left(\frac{\text{Li}_2(e^{2\pi \sqrt{-1}\theta})}{2\pi \sqrt{-1}}\right)=-\int_{0}^{\theta}\log|2 \sin \pi \theta|d \theta 
\end{aligned}$$ for $\theta\in \mathbb{R}$. The function $\Lambda(\theta)$ is an odd function which has period $1$ and satisfies $\Lambda(1)=\Lambda(\frac{1}{2})=0.$

Furthermore, we have the follow estimation for the function $$\text{Re}\left(\frac{1}{2\pi\sqrt{-1}}\text{Li}_2\left(e^{2\pi\sqrt{-1}(\theta+X\sqrt{-1})}\right)\right)$$ with $\theta,X\in \mathbb{R}$.

::: lemma
(see Lemma 2.2 in [@OhtYok18]) []{#lemma-Li2 label="lemma-Li2"} Let $\theta$ be a real number with $0<\theta<1$. Then there exists a constant $C>0$ such that $$\begin{aligned}
    \left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X\geq 0) \\
         &2\pi \left(\theta-\frac{1}{2}\right)X & \ (\text{if} \ X<0)
                          \end{aligned} \right.-C<\text{Re}\left(\frac{1}{2\pi\sqrt{-1}}\text{Li}_2\left(e^{2\pi\sqrt{-1}(\theta+X\sqrt{-1})}\right)\right)
\end{aligned}$$ $$\begin{aligned}
    <\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X\geq 0) \\
         &2\pi \left(\theta-\frac{1}{2}\right)X & \ (\text{if} \ X<0)
                          \end{aligned}\right.+C.
\end{aligned}$$.
:::
