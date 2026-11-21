---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-021-52-helicity-supertrace-for-type-iia-chl-models
section_title: "Helicity supertrace for type IIA CHL models"
section_number: 5.2
pages: 32-33
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.937
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
Let us now generalize the previous analysis to CHL models in type IIA string theory. We are interested in the case where the orbifold group $G$ is cyclic of order $\hat N$, with generator $\hat g$ acting by a shift $\delta$ of a $1/\hat N$ period along one of the cycles of $T^2$ and by a symmetry $g$ of the K3 sigma model. Then, the generating function $Z^{\text{IIA}}_{\text{CHL}[\hat g]}$ is obtained from [\[ZIIA\]](#ZIIA){reference-type="eqref" reference="ZIIA"} by the usual orbifold formula $$Z^{\text{IIA}}_{\text{CHL}[\hat g]}(\upsilon,\bar \upsilon)=\frac{\vartheta_1(\upsilon/2)^2\bar\vartheta_1(\bar\upsilon/2)^2  }{\eta^6\bar\eta^6\tau_2}\xi(\upsilon)\bar\xi(\bar\upsilon)\frac{1}{|\hat N|}\sum_{r,s=1}^{\hat N}C_{g^r,g^s}
(\upsilon/2,\bar\upsilon/2)\Theta_{\Gamma^{2,2}} \bigl[{}^r_s\bigr]\ ,
\label{CHLpartfun}$$ where $$\Theta_{\Gamma^{2,2}} \bigl[{}^r_s\bigr]:=\sum_{(p_L,p_R)\in r\delta+\Gamma^{2,2}} e^{2\pi is \delta \cdot (p_L,p_R)} q^{\frac{p_L^2}{2}}
\bar q^{\frac{p_R^2}{2}}\ .$$ Here we used the fact that the orbifold group acts only on the winding-momenta along $T^2$ and on the internal K3 sigma model. The fourth helicity trace is then evaluated to $$B_4^{\text{CHL}[\hat g]}=\frac{3}{2\tau_2}\frac{1}{\hat N}\sum_{r,s=1}^{ \hat N}C_{g^r,g^s}
(0,0)\Theta_{\Gamma^{2,2}} \bigl[{}^r_s\bigr]\ .$$We have $$C_{g^r,g^s}
(0,0) = \mathop{\mathrm{Tr}}_{\bf 24} (g^{\gcd(r,s,N)})\ ,$$where ${\bf 24}$ denotes the $24$ dimensional representation of R-R ground states in the K3 sigma model. Therefore, if $g$ has Frame shape $\prod_{a|N} a^{m(a)}$, we obtain $$\mathop{\mathrm{Tr}}_{\bf 24} (g^d)=\sum_{a|d}m(a)a$$for all $d|\hat N$. Assembling the pieces we find that the fourth helicity supertrace of the CHL model becomes $$\begin{aligned}
 B_4^{\text{CHL}[\hat g]}= &\frac{3}{2\tau_2}\frac{1}{\hat N}\sum_{d|\hat N} \mathop{\mathrm{Tr}}_{\bf 24} (g^d)\sum_{\substack{r,s=1\\ \gcd(r,s,\hat N/d)=1}}^{ \hat N/d}\Theta_{\Gamma^{2,2}} \bigl[{}^{dr}_{ds}\bigr]\\= &\frac{3}{2\tau_2}\frac{1}{\hat N}\sum_{d|\hat N} \mathop{\mathrm{Tr}}_{\bf 24} (g^d)\sum_{l|\frac{\hat N}{d}}\mu(l)\sum_{r,s=1}^{ \hat N/ld}\Theta_{\Gamma^{2,2}} \bigl[{}^{ldr}_{lds}\bigr]\\
\stackrel{n:=ld}{=}&\frac{3}{2\tau_2}\frac{1}{\hat N}\sum_{n|\hat N}\Bigl(\sum_{d|n} \mathop{\mathrm{Tr}}_{\bf 24} (g^d)\mu(n/d)\Bigr)\sum_{r,s=1}^{ \hat N/n}\Theta_{\Gamma^{2,2}} \bigl[{}^{nr}_{ns}\bigr]
\\
=&\frac{3}{2\tau_2}\frac{1}{\hat N}\sum_{n|\hat N}\Bigl(\sum_{d|n} \mu(n/d)\sum_{a|d}m(a)a\Bigr)\sum_{r,s=1}^{ \hat N/n}\Theta_{\Gamma^{2,2}} \bigl[{}^{nr}_{ns}\bigr]
\end{aligned}$$ where $\mu$ is the Möbius function. Using the property $$\sum_{x|y}\mu(x)=\begin{cases}1 &\text{if }y=1\ ,\\ 0 &\text{otherwise}\ ,\end{cases}$$ the divisor sum simplifies: $$\sum_{d|n} \mu(n/d)\sum_{a|d}m(a)a\stackrel{t:=n/d}{=}\sum_{a|n}m(a) a\sum_{t|\frac{n}{a}}\mu(t)=m(n)n$$so that $$B_4^{\text{CHL}[\hat g]}=\frac{3}{2\tau_2}\sum_{n|\hat N}m(n)\frac{n}{\hat N}\sum_{r,s=1}^{ \hat N/n}\Theta_{\Gamma^{2,2}} \bigl[{}^{nr}_{ns}\bigr]$$ Finally, we note that, if $T,U$ are the Kähler and complex moduli of $T^2$ in the original (unorbifolded) model, then $$\frac{n}{\hat N}\sum_{r,s=1}^{ \hat N/n}\Theta_{\Gamma^{2,2}} \bigl[{}^{nr}_{ns}\bigr](T,U)=\Theta_{\Gamma^{2,2}}(Tn/\hat N,Un/\hat N)\ ,$$because the LHS is simply (up to a factor $1/|\eta|^4$) the partition function for a bosonic sigma model on a torus $T^2$ with moduli $(T,U)$, orbifolded by a shift of order $\hat N/n$ along one of the cycles; this orbifold is again a sigma model on $T^2$, with the $T$ and $U$ moduli divided by $\hat N/n$. Notice that, in our conventions the Kähler and complex structure moduli $T_{\text{IIA}}$ and $U_{\text{IIA}}$ of $T^2$ in the CHL model are related to $T,U$ via $$T_{\text{IIA}}\equiv \frac{T}{\hat N}\qquad U_{\text{IIA}}\equiv \frac{U}{\hat N}\ .$$ Therefore the final result for the helicity supertrace is $$B_4^{\text{CHL}[\hat g]}=\frac{3}{2\tau_2}\sum_{n|\hat N}m(n)\Theta_{\Gamma^{2,2}}(nT_{\text{IIA}},nU_{\text{IIA}}).$$
