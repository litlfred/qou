---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-007-53-lebowitz-penrose
section_title: "Lebowitz-Penrose"
section_number: 5.3
pages: 8-10
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.986
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
We again use the same bounds on the cluster expansion and follow the method outlined in [@LPen64] and starting with [\[uform\]](#uform){reference-type="eqref" reference="uform"}, we arrange our expression $r(s)$ into the form: $$r(s)=\frac{C(\beta)^{-1}}{1+u}\frac{s}{u^2}\left((1+u)^2e^{-s}-(1+u)\right) \label{lebpenstart}$$ We use the identity: $\frac{1+u}{u^2}=\frac{(1+u)^2}{u^2}-\frac{1+u}{u}$, to rewrite it as: $$r(s)=\frac{C(\beta)^{-1}}{1+u}\left(s\frac{1+u}{u}-s^2\frac{(1+u)^2}{u^2}\left(\frac{1-e^{-s}}{s}\right)\right)$$ We make the change of variables $v= s\frac{1+u}{u}$ and define $g(w):=\frac{1-e^{-w}}{w}$ and obtain: $$\hat{r}(s)=\frac{C(\beta)^{-1}}{1+u}(v-v^2g\left(\frac{uv}{1+u}\right))$$ We note that $g'(w)=\frac{we^{-w}-(1-e^{-w})}{w^2}=\frac{(w+1)e^{-w}-1}{w^2}$

If we use the inequality $e^w \geq 1+w$, then $1 \geq (1+w)e^{-w}$ and so $0 \geq (1+w)e^{-w}-1$ and hence $g$ is decreasing. We note that $u \in (1,\infty)$ and so $\frac{u}{u+1} \in (\frac{1}{2},1)$. Since $g$ is decreasing, we get maximum value at $g(\frac{v}{2})$, which would give a minimum value for the expression in brackets, which gives a bound uniform in $u$. This is an extra approximation in the derivation of the virial coefficient bounds, which is not made in the general derivation. This is equivalent to realising that the $g$-function is dominated by its contribution at $u=1$, that is, when $\beta=0$, so at high temperatures.

We then seek to maximise: $f(v)=v-v^2g(\frac{1}{2}v)$. Upon differentiation we get: $$\begin{aligned}
 f'(v) &= 1-2vg(\frac{1}{2}v)-\frac{1}{2}v^2g'(\frac{1}{2}v) \notag \\ &=1-2v\left(\frac{1-e^{-\frac{1}{2}v}}{\frac{1}{2}v}\right) -\frac{1}{2}v^2\left(\frac{(\frac{1}{2}v+1)e^{-\frac{1}{2}v}-1}{\frac{1}{4}v^2}\right) \notag \\ &= 1-4(1-e^{-\frac{1}{2}v})-2(\frac{1}{2}v+1)e^{-\frac{1}{2}v}+2 \notag \\ &=-1+2e^{-\frac{1}{2}v}-ve^{-\frac{1}{2}v} 
\end{aligned}$$ When we set this to zero we get: $$1=(2-v)e^{-\frac{1}{2}v}$$ changing parameters to $\delta=1-\frac{1}{2}v$, we have: $$\frac{e}{2}=\delta e^{\delta}$$ and so using the Lambert W-function again we get: $$\delta=W\left(\frac{e}{2}\right)$$ In our original expression: $$\begin{aligned}
 \tilde{f}(\delta)&=2-2\delta-(2-2\delta)^2g(1-\delta) \notag \\ &=2(1 - \delta)-4(1-\delta)^2\left(\frac{1-e^{\delta-1}}{1-\delta}\right) \notag \\ &= (1-\delta)(2-4(1-e^{\delta}e^{-1})) \notag \\ &= 2(-1+\delta+\frac{1}{\delta}-1) \notag \\ &=2\frac{(W(\frac{e}{2})-1)^2}{W(\frac{e}{2})} 
\end{aligned}$$ This therefore gives us the bound $$|\rho| \geq \frac{2C(\beta)^{-1}}{1+u}\frac{W(\frac{e}{2})-1)^2}{W(\frac{e}{2})}$$ Leading to the coefficient bound of: $$|c_n| \leq \frac{\beta^{-1}}{n}C(\beta)^{n-1}(1+e^{2\beta B})^{n-1}\left(\frac{W(\frac{e}{2})}{2(W(\frac{e}{2})-1)^2}\right)^{n-1}$$ and the lower bound on the radius of convergence as: $$C(\beta)^{-1}\frac{1}{1+e^{2\beta B}}2\frac{(W(\frac{e}{2})-1)^2}{W(\frac{e}{2})} \label{LPenradius}$$
