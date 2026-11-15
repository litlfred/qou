---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-023-54-the-heterotic-helicity-supertrace
section_title: "The heterotic helicity supertrace"
section_number: 5.4
pages: 34-36
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.934
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
Let us now analyse the counting of BPS-states from the heterotic perspective. The generating function of helicity supertraces for heterotic strings on $T^6$ is [@Kiritsis:1997hj] $$Z^{\text{het}}(\upsilon,\bar\upsilon)=
\frac{\vartheta_1(\upsilon/2)^4  }{\eta^{12}\bar\eta^{24}}\frac{\xi(\upsilon)\bar\xi(\bar\upsilon)}{\tau_2}\Theta_{\Gamma^{6,22}}\ ,$$and the fourth helicity supertrace is[^1] $$B_4=\left(\frac{1}{2\pi i} \frac{\partial}{\partial \upsilon}+\frac{1}{2\pi i} \frac{\partial}{\partial \bar\upsilon}\right)^4 Z^{\text{het}}(\upsilon,\bar \upsilon)_{\rvert \upsilon=0}=\left(\frac{1}{2\pi i} \frac{\partial}{\partial \upsilon}\right)^4Z^{\text{het}}(\upsilon,\bar \upsilon)_{\rvert \upsilon=0}=\frac{3}{2\tau_2} \frac{\Theta_{\Gamma^{6,22}}}{\bar\eta^{24}}\ .$$

Let us consider the case where $T^6$ is the product of two orthogonal tori $T^2\times T^4$, with no Wilson lines along $T^2$. The lattice of winding momenta decomposes accordingly as $$\Gamma^{6,22}\cong \Gamma^{2,2}\oplus \Gamma^{4,20}\ .$$A CHL model is given by a orbifold by a symmetry $\hat g$ acting by a $1/\hat N$ period shift $\delta\in \Gamma^{2,2}\otimes \mathbb{R}$ along one of the circles of $T^2$ and by an automorphism $g$ on the lattice $\Gamma^{4,20}$. The generating function is given by $$Z^{\text{het}}_{\text{CHL}[g]}(\upsilon,\bar\upsilon)=
\frac{\vartheta_1(\upsilon/2)^4  }{\eta^{12}}\frac{\xi(\upsilon)\bar\xi(\bar\upsilon)}{\tau_2}\frac{1}{\hat N}\sum_{r,s=0}^{\hat N-1}\Theta_{\Gamma^{2,2}}\bigl[{}^{r}_{s}\bigr]\frac{\Theta_{\Gamma^{4,20}}^{(r,s)}}{\bar\eta_{g^r,g^s}}\ ,
\label{genhetchl}$$where

$$\Theta_{\Gamma^{4,20}}^{(0,s)}=\Theta_{(\Gamma^{4,20})^{g^s}}$$ and when $(r,s)\equiv (lc,ld)$, with $c,d,l\in \mathbb{Z}$ and $c,d$ coprime, we have $$\Theta_{\Gamma^{4,20}}^{(lc,ld)}(\tau,\bar\tau)=(c\tau+d)^{-2}(c\bar \tau+d)^{-10}\Theta_{\Gamma^{4,20}}^{(0,l)}\Bigl(\frac{a\tau+b}{c\tau+d},\frac{a\bar\tau+b}{c\bar\tau+d}\Bigr)\ ,$$for some integers $a,b$ such that $\left(\begin{smallmatrix}
a & b\\ c& d
\end{smallmatrix}\right)\in SL(2,\mathbb{Z})$. In the denominator of ([\[genhetchl\]](#genhetchl){reference-type="ref" reference="genhetchl"}) we also defined the generalized eta product which in general takes form [@Persson:2013xpa]: $$\label{etagh} \eta_{g,h}(\tau)=q^{\frac{1}{N\lambda}}\prod_{i=1}^{24}\prod_{n=0}^\infty (1-e^{\frac{2\pi it_i}{M}}q^{\frac{r_i}{N}+n})\ ,\qquad\qquad  gh=hg\ ,$$ where $M$ is the order of $h$, and the integers $0<r_1,\ldots,r_{24}\le N$ and $0<t_1,\ldots,t_{24}\le N$ are such that $\{(e^{2\pi i\frac{r_i}{N}},\,e^{2\pi i\frac{t_i}{M}})\}$ is the set of simultaneous eigenvalues of $g$ and $h$. Taking derivatives of $Z^{\text{het}}_{\text{CHL}[g]}(\upsilon,\bar\upsilon)$ we obtain the fourth helicity supertrace $$B^{\text{CHL}[g]}_{4, \text{het}}=\frac{3}{2\tau_2}\frac{1}{\hat N}\sum_{r,s=0}^{\hat N-1}\Theta_{\Gamma^{2,2}}\bigl[{}^{r}_{s}\bigr]\frac{\Theta_{\Gamma^{4,20}}^{(r,s)}}{\bar\eta_{g^r,g^s}}\ .$$

Integrating $B^{\text{CHL}[g]}_{4, \text{het}}$ against the fundamental domain of $SL(2,\mathbb{Z})$ should now yield the heterotic topological 1-loop amplitude [@Antoniadis:1997zt] $$\tilde{F}_1=\frac{2}{3}\int_{\mathcal{F}}  B^{\text{CHL}[g]}_{4, \text{het}},$$ which in particular depends on $(T_{\text{het}}, U_{\text{het}})$ but is independent of $S_{\text{het}}$. Therefore, this coupling is 1-loop exact on the heterotic side. If we expand this in the large-volume limit $\mathop{\mathrm{Im}}T_{\text{het}}\to \infty$ and map to the type IIA picture via $(U_{\text{het}} \leftrightarrow U_{\text{IIA}}, T_{\text{het}} \leftrightarrow S_{\text{IIA}})$ we obtain the one-loop IIA counterpart of $\tilde{F}_1$ supplemented with an infinite series of exponentially suppressed terms of order $\mathcal{O}(e^{-\mathop{\mathrm{Im}}S_{\text{IIA}}})$ due to D-instantons. Finally, performing the mirror map $U_{\text{IIA}} \leftrightarrow T_{\text{IIA}}$ (see [@Antoniadis:1997zt]) then reproduces precisely the coupling $f^{\text{CHL}[\hat g]}_{R^2}(T_{\text{IIA}})$ in ([\[R2couplingCHL\]](#R2couplingCHL){reference-type="ref" reference="R2couplingCHL"}). Thus, the sequence of dualities just described ensures that the counting of 1/2 BPS-states in CHL via the fourth helicity supertrace is indeed consistent with heterotic-type II duality and Fricke S-duality.

[^1]: This corrects a typo in eq. (G.9) of [@Kiritsis:1997hj] which lacks the factor $\Theta_{\Gamma^{6,22}}$.
