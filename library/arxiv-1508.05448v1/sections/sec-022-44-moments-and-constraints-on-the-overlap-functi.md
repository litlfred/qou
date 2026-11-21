---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-022-44-moments-and-constraints-on-the-overlap-functi
section_title: "Moments and Constraints on the Overlap Functions"
section_number: 4.4
pages: 74-83
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.993
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
An ideal situation would be to find an explict sum-formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$, just as Lemma [\[lem:G\]](#lem:G){reference-type="ref" reference="lem:G"} provides for $\mathcal{O}_N^{(1)}(z)$, but so far, this has not been discovered. In the next section, we will suggest a rigorous approach which may work to give the asymptotics, even when no explicit formula is known. For now, let us state the constraints imposed by the moment formula from before.

Recall from ([\[eq:mnpq\]](#eq:mnpq){reference-type="ref" reference="eq:mnpq"}) for any nonnegative integers $p$ and $q$, $$m_N((p);(q))\, =\, \int_{\mathbb{C}} z^p \overline{z}^q \mathcal{O}_N^{(1)}(z)\, d^2z 
+ \int_{\mathbb{C}} \int_{\mathbb{C}} z^p \overline{w}^q \mathcal{O}_N^{(2)}(z,w)\, d^2z\, d^2w\, .$$ Moreover, from the discussion at the end of Section [\[subsec:Argument\]](#subsec:Argument){reference-type="ref" reference="subsec:Argument"}, $m_N((p);(q))$ equals $0$ unless $p=q$, and as noted at the end of Section [\[sec:Expected\]](#sec:Expected){reference-type="ref" reference="sec:Expected"}, this is already reflected in the rotational invariance properties of $\mathcal{O}_N^{(1)}(z)$ and $\mathcal{O}_N^{(2)}(z_1,z_2)$. Therefore, specializing, we see that $$\label{eq:MoTot}
\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z 
+ \int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\, =\, 1\, ,$$ for each nonnegative integer $p$. This is the constraint formula. Let us now analyze this formula, starting with the leading order terms, and going down in order.

## Cancelling Divergences at Leading Order

For any fixed $z$ with $|z|<1$, we have $$\mathcal{O}_N^{(1)}(z)\, \sim\, N \pi^{-1} (1-|z|^2)\, ,$$ and the corrections are actually exponentially small in $N$ (since they arise as the deep part of the right tail of the series for the exponential). Therefore, integrating, we obtain the leading-order part of the contribution from $\mathcal{O}_N^{(1)}(z)$ from the formula above $$\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z\, \sim\, N \pi^{-1} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\, d^2z\, .$$ The corrections to this formula are not exponentially small, incidentally. This is because the formula for $\mathcal{O}_N^{(1)}(z)$ is not exponentially close to the exact formula for all $z$ in the complex plane. For a fixed $|z|>1$ it is easy to see that $\mathcal{O}_N^{(1)}(z)$ is exponentially small (hence exponentially close to the approximating function of $0$ there). That is because one only has the series for the exponential up to a small number of terms, deep in the left tail. Near the circle, there are algebraic corrections, not exponential ones.

Nevertheless, let us note that, by making a polar decomposition, $z=r e^{i\theta}$, we obtain $$N \pi^{-1} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\, d^2z\, 
=\, N \int_0^1 t^p (1-t)\, dt\, =\, \frac{N}{(p+1)(p+2)}\, .$$ Let us see how this cancels with the leading-order part of the $\mathcal{O}_N^{(2)}$ integral.

We will use Chalker and Mehlig's formula here for the leading-order part, even though we do not yet know the corrections for the lower-order part near the circle. Then we get $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\\
\sim\, - \int_{\mathbb{C}} \int_{\mathbb{C}} \left(z+\frac{\omega}{2N^{1/2}}\right)^p \left(\overline{z}-\frac{\overline{\omega}}{2N^{1/2}}\right)^p N^2 \pi^{-2} (1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\,\\ \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\, N^{-1} d^2\omega\, d^2z\, ,
\end{gathered}$$ where the $N^{-1}$ associated to the volume-element $d^2\omega$-times-$d^2z$ is to account for the Jacobian of the transformation from $(z_1,z_2)$ to $(z,\omega)$. Now we will begin to separate this formula into even another decomposition into leading terms, and sub-leading terms. This is because, in the formulas $z_1^p = (z+\frac{1}{2}N^{-1/2}\omega)^p$ and $\overline{z}_2^p = (\overline{z}-\frac{1}{2}N^{-1/2}\overline{\omega})^p$, clearly the leading order arises by ignoring the contributions of $\omega$ which each are accompanied by negative powers of $N$. We really obtain, what we might call the "leading order, leading order" term: $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,
\sim\, \\ - N \pi^{-2} \int_{\mathbb{C}} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\, \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\, N^{-1} d^2\omega\, d^2z\, .
\end{gathered}$$ Then it is easy to see that this splits. The integral over $\omega$ is $$\int_{\mathbb{C}} \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\, d^2\omega\,
=\, \pi \int_0^{\infty} \frac{1-(1+t)e^{-t}}{t^2}\, dt\,
=\, \pi \int_0^{\infty} \frac{1}{t^2} \left(\int_0^t s e^{-s}\, ds\right)\, dt\, .$$ Integrating-by-parts, it is easy to see that this gives $\pi$. Therefore, we end up with the exact negative of the leading order contribution by $\mathcal{O}_N^{(1)}$: $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,
\sim\, - N \pi^{-1} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\,  d^2z\, \\ =\, -\frac{N}{(p+1)(p+2)}\, .
\end{gathered}$$ The fact that these two terms cancel is good, because each diverges, separately; whereas, according to the formula, the exact answer is supposed to be $1$.

## The Sub-Leading Contribution from $\mathcal{O}_N^{(1)}$ {#subsec:sLO1}

For the first integral, we are fortunate that the exact correction is known near the circle. We will not attempt to keep track of the exponentially-small corrections which are present away from the circle. Near the circle, the exact corrections are relevant because they are not exponentially small.

Using Corollary 4.3, we know that $$\begin{gathered}
\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z
- \frac{N}{(p+1)(p+2)}\, =\,\\ \frac{N^{1/2}}{\pi}\, \int_{\mathbb{C}} \left[\frac{e^{-2u^2}}{\sqrt{2\pi}} - 2 u \Phi(-2u)\right]\Bigg|_{u = N^{1/2} (1-|z|)} |z|^{2p}\, d^2z
+ o(1)\, ,
\end{gathered}$$ where the small term $o(1)$ means that the remainder converges to $0$ as $N \to \infty$. This remainder includes exponentially small corrections to $\mathcal{O}_N^{(1)}(z)$ away from the circle, as well as the systematic correction terms to the leading-order behavior near the circle that arise from the Euler-Maclaurin series. The reason that these correction terms to the Euler-Maclaurin summation formula are $o(1)$ will arise momentarily: even the leading order term is only order-1, constant.

Making the polar decomposition of $z$ and then rewriting $r = 1-N^{-1/2}u$ so that $dr=N^{-1/2}\, du$ (and reversing orientation of the integral), we have $$\begin{split}
\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z
- \frac{N}{(p+1)(p+2)}\, \\
=\, 2 \int_{-\infty}^{N^{1/2}} \left[\frac{e^{-2u^2}}{\sqrt{2\pi}} - 2 u \Phi(-2u)\right](1-N^{-1/2}u)^{2p+1}\, du+ o(1)\\
=\, 2 \int_{-\infty}^{\infty} \left[\frac{e^{-2u^2}}{\sqrt{2\pi}} - 2 u \Phi(-2u)\right]\, du+ o(1)\, .
\end{split}$$ In particular, this correction is independent of $p$, modulo vanishingly small remainder terms which are accumulated in the $o(1)$. Rewriting $u=x/2$ and integrating by parts gives a constant which is equal to $3/2$.

We will not be able to make it to the order-1, constant terms in the $N\to \infty$ asymptotics series (in decreasing powers of $N$). The reason is that for $\mathcal{O}_N^{(2)}$, we do not have sufficiently precise asymptotics to get to that level. Instead, what we will do next is to consider what constraints the formula for the moments imposes on $\mathcal{O}_N^{(2)}$.

## Sub-Leading Divergences in the $\mathcal{O}_N^{(2)}$ Term

We have now accounted for all the non-vanishing contributions from the $\mathcal{O}_N^{(1)}$ term. The leading-order divergence cancels with the leading-order divergence of the $\mathcal{O}_N^{(2)}$ term. The sub-leading order part of the $\mathcal{O}_N^{(1)}$ contribution to the moment is already order-1, constant, and it is independent of $p$. It equals $3/2$. Note that the moment itself is also independent of $p$, it is $1$.

Since we do not know the actual formula for $\mathcal{O}_N^{(2)}$, our plan for this section is to consider the proposed formula for $\mathcal{O}_N^{(2)}$ in the bulk. That still leads to one other divergent contribution, diverging logarithmically in $N$. What this must mean is that in the formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ for $z_1$ and $z_2$ close, and both near the circle, there must be an edge correction, which leads to a counter-balancing divergence. This is what we explain in some more detail, now. This subsection is detailed and technical.

We consider the proposed formula for $\mathcal{O}_N^{(2)}$ that Chalker and Mehlig derived. This is the correct formula in the bulk, following the argument of their paper, although there is a lower-order correction near the circle. We will not include the correction on the circle. Instead our calculations will show constraints that must be satisfied for this correction formula. We use $z_1 = z+\frac{1}{2}N^{-1/2}\omega$ and $z_2 = z-\frac{1}{2}N^{-1/2}\omega$ so that $$z_1 \overline{z}_2\,
=\, |z|^2 + \frac{i \mathrm{Im}[\omega \overline{z}]}{N^{1/2}} - \frac{|\omega|^2}{4N}\, .$$ Therefore, using the bulk formula we would have $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,\\
\approx\, -\frac{N^2}{\pi^2} \int_{\mathbb{C}} \int_{\mathbb{C}} \left[|z|^2 + \frac{i \mathrm{Im}[\omega \overline{z}]}{N^{1/2}} - \frac{|\omega|^2}{4N}\right]^p
\left(1 -  \left[|z|^2 + \frac{i \mathrm{Im}[\omega \overline{z}]}{N^{1/2}} - \frac{|\omega|^2}{4N}\right]\right)\\
\cdot \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\,
\mathbf{1}_{[0,1]}\Big(\Big|z\pm\frac{1}{2}N^{-1/2}\omega\Big|^2\Big)\, 
N^{-1} d^2\omega\, d^2z\, ,
\end{gathered}$$ where we use the approximation symbol $\approx$ to remind ourselves that this is only one part of the eventual formula. Simplifying this, and writing $z = r e^{i\theta}$ and $\omega = \rho e^{i t}$, we have $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\, \\ \approx\, -\frac{N}{\pi^2} \int_{\mathbb{C}} \int_{\mathbb{C}} \left[r^2 + \frac{i r\rho \sin(\theta-t)}{N^{1/2}} - \frac{\rho^2}{4N}\right]^p
\left(1 -  \left[r^2 + \frac{i r\rho \sin(\theta-t)}{N^{1/2}} - \frac{\rho^2}{4N}\right]\right)\\
\cdot \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho^4}\,
\mathbf{1}_{[0,4N]}\Big(\Big|\rho \pm 2N^{1/2}re^{i(t-\theta)}\Big|^2\Big)\, 
r\rho\, dr\, d\rho\, d\theta\, dt\, .
\end{gathered}$$

Let us denote $\phi = t-\theta$. Integrating over the extra angular variable, simplifying the power of $\rho$ in the second line, and simplifying the indicator in the second line, we obtain$$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,
 \\ \approx\, -\frac{2N}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\rho>0} \int\limits_{\phi \in [0,2\pi)} \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]^p
\left(1 -  \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]\right)\\
\cdot \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho^3}\,
\mathbf{1}_{[0,N^{1/2} R(r,\phi)]}(\rho)\, 
r dr\, d\rho\, d\phi\, ,
\end{gathered}$$ for $$R(r,\phi)\, =\, 2 \left(\sqrt{1-r^2\sin^2(\phi)}-r|\cos(\phi)|\right)\, ,$$ arising from the condition $|\rho \pm 2 N^{1/2} r e^{i\phi}| \leq 2N^{1/2} \Leftrightarrow \rho \leq R(r,\phi) N^{1/2}$

Let us rewrite this once again, this time isolating different functional terms that we wish to consider in more detail: $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\, \\ \approx\, -\frac{2N}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} \left(\int_0^{N^{1/2}R(r,\phi)} F_p(r,\phi,\rho) W(\rho)\, d\rho\right)\, r\, dr\, d\phi\, ,
\end{gathered}$$ where $$\label{eq:Fp}
F_p(r,\phi,\rho)\, =\, \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]^p
\left(1 -  \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]\right)\, ,$$ and $$W(\rho)\, =\,  \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho^3}\, .$$ Now we note that we can expand $$\label{eq:expand}
F_p(r,\phi,\rho)\, =\, \sum_{k=0}^{2p} f_p^{(k)}(r,\phi)\, \frac{\rho^k}{N^{k/2}}\, .$$ Odd powers of $k$ have $f_p^{(k)}(r,\phi)$ which is an odd function of $\sin(\phi)$. Since the rest of the integral will contribute even factors, this means all odd powers will integrate to zero, so we only keep track of even powers. We have already taken account of $f_p^{(0)}(r,\phi)$ which is just $f_p^{(0)}(r) = r^{2p} (1-r^2)$. This was what gave us the leading order divergence we considered in a past subsection.

Moreover, starting from the even power $k=4$, we have $$-\frac{2N}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} \left(\int_0^{N^{1/2}R(r,\phi)} f_p^{(k)}(r,\phi)\, \frac{\rho^k}{N^{k/2}} W(\rho)\, d\rho\right)\, r\, dr\, d\phi\, 
=\, O(1)\, .$$ The reason is that $N \cdot N^{-k/2} = N^{-(k-2)/2}$ which is vanishing. This means that the lower limit of integration is actually contributing a negligible correction, asymptotically for large $N$. Near the upper limit of integration, we may expand $W(\rho) \sim \rho^{-3}$. Therefore we obtain near the upper limit, for $k=4,6,\dots$, $$\begin{gathered}
\label{eq:largek}
-\frac{2}{\pi N^{(k-2)/2}} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(k)}(r,\phi)\,\left(\int_0^{N^{1/2}R(r,\phi)}  \rho^{k-3}\, d\rho\right)\, r\, dr\, d\phi\\
=\, -\frac{2}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(k)}(r,\phi)\, \frac{[R(r,\phi)]^{(k-2)/2}}{k-2}\, r\, dr\, d\phi
+o(1)\, =\, O(1)\, .
\end{gathered}$$

This only leaves the term with $k=2$ which might diverge. Indeed, for this, we just have $$-\frac{2}{\pi}\,
\int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(2)}(r,\phi)\,\left(\int_0^{N^{1/2}R(r,\phi)}  \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho}\, d\rho\right)\, r\, dr\, d\phi\, .$$ The only divergent part of this arises near the upper limit for the $\rho$ integral which gives $\ln(N^{1/2} R(r,\phi)) = \frac{1}{2} \ln(N) + \ln(R(r,\phi))$, so the logarithmic divergence is $$\begin{gathered}
-\frac{2}{\pi}\,
\int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(2)}(r,\phi)\,\left(\int_0^{N^{1/2}R(r,\phi)}  \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho}\, d\rho\right)\, r\, dr\, d\phi\\
=\,
-\frac{\ln(N)}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} r f_p^{(2)}(r,\phi)\, dr\, d\phi
+ O(1)\, .
\end{gathered}$$ It is easy to see that $$f_p^{(2)}(r,\phi)\, =\,
\frac{1}{4}\, r^{2p} - \frac{p}{4}\, r^{2p-2} (1-r^2) - \frac{p(p-1)}{2}\, r^{2p-2}(1-r^2) \sin^2(\phi) + p r^{2p}\sin^2(\phi)\, .$$ Therefore, we have $$\begin{split}
\int_{\phi \in [0,2\pi]} f_p^{(2)}(r,\phi)\, d\phi\, 
&=\, 2\pi
\left(\frac{1}{4}\, r^{2p} - \frac{p}{4}\, r^{2p-2} (1-r^2) - \frac{p(p-1)}{4}\, r^{2p-2}(1-r^2) + \frac{p}{2}\, r^{2p}\right)\\
&=\, \frac{\pi}{2} \left[(p+1)^2 r^{2p} - p^2 r^{2p-2}\right]\, .
\end{split}$$ Therefore, the sub-leading order divergence is now $$\label{eq:sL}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2
+ \frac{N}{(p+1)(p+2)}\,
=\, -\frac{1}{4}\, \ln(N) + O(1)\, .$$ We may consider this particular form. It is independent of $p$. Near the circle, and for $z_1$ near $z_2$, the form of $z_1^p \overline{z}_2^p$, to leading order is just $|z|^{2p}$ which is just $1$, because $z$ is near the circle. This is the same explanation for the reason that the order-1, constant term coming from $\mathcal{O}_N^{(1)}$ term is independent of $p$. We also know that the moment must be independent of $p$.

One could also try to calculate the order-1 contributions at this point, coming just from the bulk formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$. One could then check whether these combine to a constant independent of $p$. That would be yet another strong check that Chalker and Mehlig's formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ is true to very high accuracy in the bulk, and only needs an edge correction near the circle.

It would be best to have a sufficiently explict formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ to allow one to see the correction near the circle. Then we could have an answer to settle this. Next, we propose a method which we believe could potentially provide this.
