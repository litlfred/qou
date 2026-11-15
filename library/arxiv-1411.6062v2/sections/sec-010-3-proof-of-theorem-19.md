---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-010-3-proof-of-theorem-19
section_title: "Proof of Theorem 1.9"
section_number: 3
pages: 13-16
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.823
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
We start by taking the logarithmic derivative of Faddeev's quantum dilogarithm $$\begin{aligned}
\frac{\partial}{\partial x}\log \operatorname{\Phi}_{\mathsf{b}}(x)
& =\int_{\mathbb{R}+\mathsf{i}\epsilon}
\frac{-2\mathsf{i}e^{-2\mathsf{i}xz}}{4\sinh(z\mathsf{b})\sinh(z\mathsf{b}^{-1})}
\operatorname{d}\!z \\ \notag & 
=\int_{\mathbb{R}+\mathsf{i}\epsilon}
\frac{ e^{-2\mathsf{i}xz}}{2\mathsf{i}\sinh(z\mathsf{b})\sinh(z\mathsf{b}^{-1})}
\operatorname{d}\!z\\ \notag &
=\int_{\mathbb{R}+\mathsf{i}\epsilon}
\frac{\pi\mathsf{s}e^{-2\pi\mathsf{i}\mathsf{s}xz}}{2\mathsf{i}\sinh(\pi z\mathsf{b}\mathsf{s})
\sinh(\pi z\mathsf{b}^{-1}\mathsf{s})}\operatorname{d}\!z \\ \notag &
=\int_{\mathbb{R}+\mathsf{i}\epsilon}
\frac{ \pi\mathsf{s}e^{-2\pi\mathsf{i}\mathsf{s}xz}}{2\mathsf{i}\sinh(\pi zM)\sinh(\pi zN)}
\operatorname{d}\!z \,.
\end{aligned}$$ After rescaling $x\mapsto \frac{x}{2\pi\mathsf{s}}$ we obtain $$\label{thm1.8-1}
4\mathsf{i}\frac{\partial}{\partial x}
\log \operatorname{\Phi}_{\mathsf{b}}\left(\frac{x}{2\pi\mathsf{s}}\right)
=\int_{\mathbb{R}+\mathsf{i}\epsilon}
\frac{e^{-\mathsf{i}xz}}{ \sinh(\pi zM)\sinh(\pi zN)}\operatorname{d}\!z\,.$$ The integrand in [\[thm1.8-1\]](#thm1.8-1){reference-type="eqref" reference="thm1.8-1"}, given by the function $$\operatorname{f}(z)= \frac{e^{-\mathsf{i}xz}}{ \sinh(\pi zM)\sinh(\pi zN)}$$ satisfies Equation [\[per\]](#per){reference-type="eqref" reference="per"} with $a=\mathsf{i}$ as a direct consequence of the equalities $$\frac{\operatorname{f}(z\pm\mathsf{i})}{\operatorname{f}(z)}=(-1)^{M+N} e^{\pm x} \,.$$ Equation [\[residue1\]](#residue1){reference-type="eqref" reference="residue1"} and an application of Cauchy's residue theorem implies that $$\begin{aligned}
\notag
\frac{2}{\pi}\left(1-(-1)^{M+N} e^{x}\right)
\frac{\partial}{\partial x}
\log \operatorname{\Phi}_{\mathsf{b}}\left(\frac{x}{2\pi\mathsf{s}}\right)
&=\frac{1}{2\pi\mathsf{i}}\left( 
\int_{\mathbb{R}+\mathsf{i}\epsilon}-\int_{\mathbb{R}+\mathsf{i}(1+\epsilon)}\right)
\operatorname{f}(z)\operatorname{d}\!z\\ \label{eq.Phi123} &
=
S_1(z) + S_2(z) + S_3(z)\,,
\end{aligned}$$ where $$S_1 = \sum_{m=1}^{M-1}\operatorname{Res}_{z=\mathsf{i}\frac mM} 
\operatorname{f}(z), \qquad
S_2 = \sum_{n=1}^{N-1}\operatorname{Res}_{z=\mathsf{i}\frac nN}
\operatorname{f}(z), \qquad
S_3 = \operatorname{Res}_{z=\mathsf{i}}
\operatorname{f}(z) \,.$$ So, we have reduced the integrals to the sum of residues. Our next task is to calculate each residue. Let us introduce $C_i$ for $i=1,2,3$ by: $$\begin{aligned}
C_1 &=\frac{\left(1-e^{x+\pi\mathsf{i}(M+N)}\right)^{\frac{M-1}{2M}}}{
D_M\left(e^{(x+\pi\mathsf{i}(M+N))/M}; e^{2\pi \mathsf{i}N/M}\right)} \\
C_2 &=\frac{\left(1-e^{x+\pi\mathsf{i}(M+N)}\right)^{\frac{N-1}{2N}}}{
D_N\left(e^{(x+\pi\mathsf{i}(M+N))/N}; e^{2\pi \mathsf{i}M/N}\right)} \\
C_3 &=\left(1-(-1)^{M+N}e^x\right)^{\frac{\mathsf{i}x}{2\pi\mathsf{s}^2}} 
e^{\frac{\mathsf{i}}{2\pi\mathsf{s}^2}\operatorname{Li}_2\left((-1)^{M+N}e^x\right)} \,.
\end{aligned}$$

::: lemma
[]{#lem.SC label="lem.SC"} For $i=1,2,3$ we have: $$\label{eq.SC}
S_i = \frac{2}{\pi}\left(1-(-1)^{M+N} e^{x}\right)
\frac{\partial}{\partial x} \log C_i \,.$$
:::

::: proof
*Proof.* First we compute $S_1$. Expanding in powers of $z$ around $z=0$, we have $$\operatorname{f}\left(z+\mathsf{i}\frac mM\right) 
=\frac{(-1)^me^{mx/M}}{\pi z M\mathsf{i}\sin(\pi m N/M)}\left(1+\mathrm{O}(z)\right)=
\frac{(-1)^me^{mx/M}}{\pi z M\mathsf{i}\sin(\pi m N/M)}+\mathrm{O}(1)$$ so that $$\begin{aligned}
\operatorname{Res}_{z=\mathsf{i}\frac mM}\operatorname{f}(z)
&=\frac{\left(-e^{x/M}\right)^m}{\pi\mathsf{i}M\sin(\pi m N/M)}
=\frac{2\left(-e^{x/M}\right)^m}{
\pi M\left(e^{\pi \mathsf{i}m N/M}-e^{-\pi \mathsf{i}m N/M}\right)}\\
&=\frac{-2\left(-e^{(x+\pi\mathsf{i}N)/M}\right)^m}{\pi M\left(1-e^{2\pi \mathsf{i}m N/M}
\right)}
=\frac{-2e^{m(x+\pi\mathsf{i}(M+N))/M}}{\pi M\left(1-e^{2\pi \mathsf{i}m N/M}\right)} \,.
\end{aligned}$$ Now, by using Lemma [\[lemim\]](#lemim){reference-type="ref" reference="lemim"} (see below), we calculate $$\begin{gathered}
-\frac{\pi }2 \sum_{m=1}^{M-1}
\operatorname{Res}_{z=\mathsf{i}\frac mM}\operatorname{f}(z)=
M^{-1}\sum_{m=1}^{M-1} \frac{e^{m(x+\pi\mathsf{i}(M+N))/M}}{1-e^{2\pi \mathsf{i}m N/M}}\\
=\frac{M-1}{2M} e^{x+\pi\mathsf{i}(M+N)} +\left(1-e^{x+\pi\mathsf{i}(M+N)}\right)
\frac{\partial}{\partial x}
\log D_M\left(e^{(x+\pi\mathsf{i}(M+N))/M}; e^{2\pi \mathsf{i}N/M}\right).
\end{gathered}$$ Finally observe that $$-\int_{-\infty}^x  \frac{e^{y+\pi\mathsf{i}(M+N)}}{ \left(1-e^{y+\pi\mathsf{i}(M+N)}\right)}
\operatorname{d}\! y
= \log \left(1-e^{x+\pi\mathsf{i}(M+N)}\right)$$ This proves Equation [\[eq.SC\]](#eq.SC){reference-type="eqref" reference="eq.SC"} for $i=1$. Interchanging $M$ with $N$ proves Equation [\[eq.SC\]](#eq.SC){reference-type="eqref" reference="eq.SC"} for $i=2$. Finally we compute $S_3$. Expanding in powers of $z$ around $z=0$, we have $$\begin{aligned}
(-1)^{M+N} e^{-x} \operatorname{f}(z+\mathsf{i})
&=\operatorname{f}(z)
=\frac{1-\mathsf{i}xz +\mathrm{O}(z^2)}{
\pi z M(1+\mathrm{O}(z^2))\pi z N(1+\mathrm{O}(z^2))}\\
&=\frac{1-\mathsf{i}xz +\mathrm{O}(z^2)}{\pi^2 MN z^2}
=\frac{1}{\pi^2\mathsf{s}^2 z^2} 
-\frac{\mathsf{i}x}{\pi^2 \mathsf{s}^2 z} +\mathrm{O}(1)
\end{aligned}$$ so that $$\operatorname{Res}_{z=\mathsf{i}}\operatorname{f}(z)
=\frac{(-1)^{1+M+N}\mathsf{i}xe^x}{\pi^2 \mathsf{s}^2}\,.$$ Now we calculate $$\begin{aligned}
2\pi \mathsf{i}\mathsf{s}^2\log C_3 
&=\int_{-\infty}^x\frac{(-1)^{M+N}ye^y\operatorname{d}\! y}{1-(-1)^{M+N} e^{y}}
=-\int_{-\infty}^xy\operatorname{d}\log\left(1-(-1)^{M+N}e^y\right)\\
&=-\left[y\log\left(1-(-1)^{M+N}e^y\right)\right]_{-\infty}^{x}
+\int_{-\infty}^x\log\left(1-(-1)^{M+N}e^y\right)\operatorname{d}\! y\\
&=
-x\log\left(1-(-1)^{M+N}e^x\right)+\int_{0}^{(-1)^{M+N}e^x}
\frac{\log(1-z)}{z}\operatorname{d}\! z\\
&=
-x\log\left(1-(-1)^{M+N}e^x\right)-\operatorname{Li}_2\left((-1)^{M+N}e^x\right)
\,.
\end{aligned}$$ Equation [\[eq.SC\]](#eq.SC){reference-type="eqref" reference="eq.SC"} follows for $i=3$. ◻
:::

We now finish the proof of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}. Using $$\lim_{x\to -\infty}\operatorname{\Phi}_{\mathsf{b}}\!\left(x\right)=1$$ it follows that $$\label{eq.pfthm2}
\log\operatorname{\Phi}_{\mathsf{b}}\!\left(\frac{x}{2\pi\mathsf{s}}\right)
=\int_{-\infty}^x \frac{\partial}{\partial y}\log\operatorname{\Phi}_{\mathsf{b}}\!
\left(\frac{y}{2\pi\mathsf{s}}\right)\operatorname{d}\! y$$ Combining the above with Equation [\[eq.Phi123\]](#eq.Phi123){reference-type="eqref" reference="eq.Phi123"} and Lemma [\[lem.SC\]](#lem.SC){reference-type="ref" reference="lem.SC"}, we obtain that $$\operatorname{\Phi}_{\mathsf{b}}\!\left(\frac{x}{2\pi\mathsf{s}}\right)=C_1C_2C_3$$ Introduce a new variable $z$ related to $x$ by $$\frac{x}{2\pi\mathsf{s}}=\frac{z}{2\pi\mathsf{s}}-c_{\mathsf{b}} \,.$$ In other words, we have $$x=z-\pi\mathsf{i}(M+N) \,.$$ Equation [\[eq.pfthm2\]](#eq.pfthm2){reference-type="eqref" reference="eq.pfthm2"} implies that $$\begin{gathered}
\operatorname{\Phi}_{\mathsf{b}}\!\left(\frac{z}{2\pi\mathsf{s}}-c_{\mathsf{b}}\right)
\operatorname{D}_N(e^{z/N};q_+)\operatorname{D}_M(e^{z/M};q_-)
e^{-\frac{\mathsf{i}}{2\pi\mathsf{s}^2}\operatorname{Li_2}(e^{z})}\\=
\left(1-e^z\right)^{\frac{M-1}{2M}+\frac{N-1}{2N}+\frac{\mathsf{i}(z-\pi\mathsf{i}(M+N))}{2\pi MN}}=
\left(1-e^z\right)^{1+\frac{\mathsf{i}z}{2\pi MN}}.
\end{gathered}$$ This concludes the proof of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}. 0◻

::: lemma
[]{#lemim label="lemim"} For any complex root of unity $q$ of order $M$, we have $$\sum_{m=1}^{M-1}\frac{x^m}{1-q^m}
=\frac{M-1}{2}x^M+(1-x^M)x\frac{\partial}{\partial x}\log D_M(x; q).$$
:::

::: proof
*Proof.* We calculate $$\begin{aligned}
(1-x^M) x\frac{\partial}{\partial x}\log D_M(x; q)
&= (1-x^M)x\frac{\partial}{\partial x}\sum_{m=1}^{M-1}\frac mM\log(1-xq^m)\\
&= -\frac{(1-x^M)x}{M}\sum_{m=1}^{M-1}\frac{mq^m}{1-xq^m}
=-\frac{x}{M}\sum_{m=1}^{M-1}\frac{mq^m\left(1-(xq^m)^M\right)}{1-xq^m} \\
&= -\frac{x}{M}\sum_{m=1}^{M-1}mq^m\sum_{n=0}^{M-1}\left(xq^m\right)^n
=-\frac{1}{M}\sum_{n=0}^{M-1}x^{n+1} \sum_{m=1}^{M-1}mq^{m(n+1)}\\
&= -\frac{1}{M}\sum_{n=1}^{M}x^{n} \sum_{m=1}^{M-1}mq^{mn}
=-\frac{M-1}2 x^M-\frac{1}{M}\sum_{n=1}^{M-1}x^{n} \sum_{m=1}^{M-1}mq^{mn} \,.
\end{aligned}$$ To finish the proof, we do the final calculation $$\sum_{m=1}^{M-1}mq^{mn}
=\left.t\frac{\partial}{\partial t}\sum_{m=1}^{M-1}t^m\right\vert_{t=q^n}
=\left.t\frac{\partial}{\partial t}\left(\frac{1-t^M}{1-t}-1\right)
\right\vert_{t=q^n}
=\left.\frac{-Mt^M}{1-t}\right\vert_{t=q^n}=\frac{-M}{1-q^n}.$$ ◻
:::
