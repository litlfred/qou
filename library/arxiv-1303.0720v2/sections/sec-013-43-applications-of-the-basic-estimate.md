---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-013-43-applications-of-the-basic-estimate
section_title: "Applications of the basic estimate"
section_number: 4.3
pages: 8-9
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.898
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We can now estimate rather trivially the $\bar\partial$-derivative at the origin.

::: prop
[]{#pointwiseneg0 label="pointwiseneg0"} If $u(z)$ is bianalytic and $\psi$ is subharmonic in ${\mathbb D}$, then $$|\bar\partial u(0)|^2\le\frac{3}{\pi}\mathrm{e}^{-2\psi(0)}\int_{{\mathbb D}}|u|^2\mathrm{e}^{2\psi}\mathrm{d}A.$$
:::

::: proof
*Proof.* We apply Lemma [\[lem1\]](#lem1){reference-type="ref" reference="lem1"} to the function $v(z):=zu(z)=zu_1(z)+|z|^2(c+zu_2(z))$: $$\frac{|c|^2}{6}=\int_0^1|r^2c|^2r\mathrm{d}r 
\leq \frac{\mathrm{e}^{-2\psi(0)}}{2\pi}\int_{{\mathbb D}}|v|^2\mathrm{e}^{2\psi}\mathrm{d}A\le
\frac{\mathrm{e}^{-2\psi(0)}}{2\pi}\int_{{\mathbb D}}|u|^2\mathrm{e}^{2\psi}\mathrm{d}A.$$ It remains to observe that $c=\bar\partial u(0)$. ◻
:::

We can also estimate the value at the origin, under an additional assumption.

::: prop
[]{#pointwiseneg label="pointwiseneg"} Suppose $u$ is bianalytic and that $\psi$ is subharmonic in ${\mathbb D}$. If $\psi\le0$ in ${\mathbb D}$, then $$|u(0)|^2\leq\frac{8}{\pi}[1 + 6|\psi(0)|^2 ]\mathrm{e}^{-2\psi(0)}\int_{{\mathbb D}} |u|^2 
\mathrm{e}^{2\psi}\mathrm{d}A.$$
:::

::: proof
*Proof.* We will use the decomposition $u(z)=u_1(z)+c\bar z +|z|^2u_2(z)$, where $u_1,u_2$ are both holomorphic. Proposition [\[pointwiseneg0\]](#pointwiseneg0){reference-type="ref" reference="pointwiseneg0"} allows us estimate $c=\bar\partial u(0)$, so that

$$\begin{gathered}

\int_0^1\bigg| \frac{cr}{\pi}\int_{{\mathbb T}} \bar \zeta \psi(r \zeta)
\mathrm{d}s(\zeta) \bigg|^2 r\mathrm{d}r 
\le \int_0^1\bigg\{\frac{|c|r}{\pi}\int_{{\mathbb T}} |\psi(r \zeta)|
\mathrm{d}s(\zeta) \bigg\}^2 r\mathrm{d}r 
\\
\leq \int_0^14|c|^2r^2|\psi(0)|^2r\mathrm{d}r
=|c|^2|\psi(0)|^2\leq \frac{3}{\pi} |\psi(0)|^2 \mathrm{e}^{-2\psi(0)} 
\int_{{\mathbb D}} |u|^2 \mathrm{e}^{2\psi} \mathrm{d}A.
\label{eq-4.1.6}
\end{gathered}$$ Note that we used the subharmonicity of $\psi$, and that $\psi\le0$. By the standard Hilbert space inequality $\|x+y\|^2\le 2(\|x\|^2+\|y\|^2)$, it follows from Lemma [\[lem1\]](#lem1){reference-type="ref" reference="lem1"} and the above estimate [\[eq-4.1.6\]](#eq-4.1.6){reference-type="eqref" reference="eq-4.1.6"} that $$\begin{gathered}
\label{almostfinalform}
\int_0^1|u_1(0)+ r^2 u_2(0)|^2 r \mathrm{d}r\le 2
\int_0^1  \bigg| u_1(0) + r^2 u_2(0) + \frac{cr}{\pi} 
\int_{{\mathbb T}}\bar\zeta\psi(r\zeta)\mathrm{d}s(\zeta)\bigg|^2 r\mathrm{d}r
\\
+2\int_0^1  \bigg|\frac{cr}{\pi} 
\int_{{\mathbb T}}\bar\zeta\psi(r \zeta)\mathrm{d}s(\zeta)\bigg|^2 r\mathrm{d}r
\leq\frac{\mathrm{e}^{-2\psi(0)}}{\pi}
\int_{{\mathbb D}} |u|^2 \mathrm{e}^{2\psi} \mathrm{d}A +  \frac{6}{\pi}|\psi(0)|^2 \mathrm{e}^{-2\psi(0)} 
\int_{{\mathbb D}} |u|^2 \mathrm{e}^{2\psi} \mathrm{d}A
\\
= \frac{1}{\pi}\left\{1+6|\psi(0)|^2\right\}\mathrm{e}^{-2\psi(0)} 
\int_{{\mathbb D}} |u|^2 \mathrm{e}^{2\psi} 
\mathrm{d}A. 
\end{gathered}$$ Next, we expand the left hand side of [\[almostfinalform\]](#almostfinalform){reference-type="eqref" reference="almostfinalform"}: $$\begin{gathered}
\int_0^1|u_1(0)+ r^2 u_2(0)|^2 r \mathrm{d}r=
\int_0^1 \left\{ |u_1(0)|^2 + r^4|u_2(0)|^2 + 2r^2 
\mathrm{Re}[ \overline{u_1(0)}u_2(0)]\right\} 
r \mathrm{d}r 
\\
= \frac12 |u_1(0)|^2 + \frac16 |u_2(0)|^2 + 
\frac12 \mathrm{Re}[ \overline{u_1(0)} u_2(0)]
= \frac18  |u_1(0)|^2 +\frac16 
\left|\frac{3}{2} u_1(0)+ 
u_2(0)\right|^2 
\geq \frac18 |u_1(0)|^2. 
\label{eq-4.1.7}
\end{gathered}$$ So, [\[almostfinalform\]](#almostfinalform){reference-type="eqref" reference="almostfinalform"} and [\[eq-4.1.7\]](#eq-4.1.7){reference-type="eqref" reference="eq-4.1.7"} together give that $$|u_0(0)|^2 \le\frac{8}{\pi}\mathrm{e}^{-2\psi(0)}\left[1+6|\psi(0)|^2\right]\,\mathrm{e}^{-2\psi(0)} 
\int_{\mathbb{D}} |u|^2 \mathrm{e}^{2\psi} \mathrm{d}A,$$ as needed. ◻
:::
