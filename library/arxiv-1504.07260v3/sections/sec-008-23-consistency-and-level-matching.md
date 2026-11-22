---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-008-23-consistency-and-level-matching
section_title: "Consistency and level matching"
section_number: 2.3
pages: 14-15
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.99
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
[]{#s:levelmatch label="s:levelmatch"}

In order for the model to be consistent, the level matching condition has to be satisfied, namely the eigenvalues of $L_0-\bar L_0$ in each $g^r$-twisted sector should take values in $\mathbb{Z}/\hat{N}\mathbb{Z}$, where $\hat N$ is the order of the symmetry. For $\hat g=(g,\delta)$, with $g\in O(\Gamma^{6,22})$ of order $N$ and $\delta\in \Gamma^{6,22}\otimes \mathbb{R}$ fixed by $g$, this means $$\label{levelmatch} \Delta E_g+\frac{\delta^2}{2}\in \frac{1}{\hat N}\mathbb{Z}\ ,$$where $\Delta E_g:= E_{g,L}-E_{g,R}$ is the level mismatch for the $g$-twisted ground state in the heterotic model and $\hat N$ is the least common multiple of the orders of $g$ and $\delta$. In general, $$\label{Elev2} \Delta E_g\equiv \frac{\mathcal{E}_g}{N\lambda}\mod \frac{1}{N}\mathbb{Z}\ ,$$where $\lambda$ is a divisor of $N$ and $\mathcal{E}_g\in \mathbb{Z}/\lambda\mathbb{Z}$ is coprime to $\lambda$. If $g$ has Frame shape $\prod_{a|N} a^{m(a)}$, then the corresponding level mismatch $\Delta E_g$ for heterotic strings on $T^6$ is easily computed to be $$\label{Elevel} \Delta E_g\equiv \frac{\mathcal{E}_g}{N\lambda}\equiv  -\frac{1}{24}\sum_{a|N}m(a)(a-\frac{1}{a})\equiv \frac{1}{24}\sum_{a|N}\frac{m(a)}{a}\equiv \frac{1}{24N}\sum_{a|N} m(N/a)a\mod \frac{1}{N}\ .$$

In the type IIA picture, $g$ is interpreted as a symmetry of the corresponding non-linear sigma model on K3. In appendix [\[s:genlatticeem\]](#s:genlatticeem){reference-type="ref" reference="s:genlatticeem"} we will show that string-string duality implies that the level mismatch $\Delta E_g'$ in the type IIA frame satisfies $$\Delta E_g'\equiv  \frac{\mathcal{E}'_g}{N\lambda} \mod \frac{1}{N}\mathbb{Z}$$where $\lambda$ is the same as in the heterotic frame and $\mathcal{E}'_g\in \mathbb{Z}/\lambda\mathbb{Z}$ is coprime relative to $\lambda$ (but not necessarily equal to $\mathcal{E}_g$).

A standard construction of the CHL model consists in choosing $\delta$ of the same order $N$ as $g$ (that is $N\delta\in \Gamma^{6,22}$), so that $\hat N=N$ [@Chaudhuri:1995ee]. With this choice, the level matching condition [\[levelmatch\]](#levelmatch){reference-type="eqref" reference="levelmatch"} requires $\delta^2\equiv -\frac{2\mathcal{E}_g}{N\lambda}\mod \frac{1}{N}\mathbb{Z}$, so that $\delta$ can be a null vector only when $\lambda=1$. In this paper, we choose $\delta$ to have order $N\lambda$, so that the order of $(g,\delta)$ is $$\hat N=N\lambda\ .$$In this case, [\[levelmatch\]](#levelmatch){reference-type="eqref" reference="levelmatch"} requires $\delta^2\equiv 0\mod \frac{1}{N\lambda}\mathbb{Z}$. Since the action of the shift symmetry on the original (unorbifolded) theory is only defined by $\delta$ modulo vectors in $\Gamma^{6,22}$, we can choose $\delta$ to be null. The two constructions ($\delta$ of order $N$ or $\delta$ of order $N\lambda$) are physically equivalent, in the sense that they lead to the same CHL model at different points in the moduli space. However, the second choice has the advantage that a null $\delta$ admits a geometric interpretation as a shift along one of the circles of $S^1$ both in the type IIA and the heterotic frame.
