---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: sec-003-14-asymptotics
section_title: "Asymptotics"
section_number: 1.4
pages: 5-6
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
---
Again we take $J=(0,s)$ and consider asymptotics as $s\ra\iy$. From the random matrix point of view the interesting quantities are E(n;s) :=    D(J;) \_. []{#E_n label="E_n"} This is the probability that exactly $n$ eigenvalues lie in $J$. The asymptotics of $E(0,s)=D(J;1)$ are obtained from ([\[Drep\]](#Drep){reference-type="ref" reference="Drep"}) using the asymptotics of $q(s;1)$ or equivalently $\sigma(s;1)$ obtained from ([\[qeq\]](#qeq){reference-type="ref" reference="qeq"}) or ([\[sigma_eq\]](#sigma_eq){reference-type="ref" reference="sigma_eq"}), respectively. (Our derivation is heuristic since as far as we are aware the corresponding Painlevé connection problem has not been rigorously solved.) We find that as $s\ra\iy$, $$\begin{aligned}
E(0;s)&=&\tau_{\al}\,  {e^{-s/4+\al\st{s}}\over
s^{\al^2/4}} \label{E_asy}\\ \noalign{\vskip3pt}
&& \times\left(1+\frac{\al}{8}s^{-\hf}+\frac{9\al^{2}}{128}s^{-1}+(\frac{3\al}{128}+
\frac{51\al^{3}}{1024})s^{-\frac{3}{2}}+(\frac{75\al^{2}}{1024}
+\frac{1275\al^{4}}{32768})s^{-2}+\cdots\right),\nonumber
\end{aligned}$$ where $\tau_{\al}$ is a constant which cannot be determined from the asymptotics of $q$ (or $\sigma$) alone. However, as we mentioned above, when $\al=\mp\hf$ this expansion must agree with those obtained from formulas (12.2.6) of [@mehta_book] (see also (12.6.17)--(12.6.19) in [@mehta_book]) after replacing $s$ by $\pi^{2}t^{2}$. This leads to the conjecture $$\tau_{\al}\,=\,\frac{G(1+\al)}{(2\pi)^{\al /2}}$$ where $G$ is the Barnes $G$-function [@barnes]. This conjecture is further supported by numerical work similar to that described for the analogous conjecture in [@tw2].

As in [@tw2], there are two approaches to the asymptotics of $E(n;s)$ for general $n$. We use the notation r(n;s) := . []{#ratio label="ratio"}

In the first approach (see also [@btw; @tw1]) one differentiates ([\[sigma_eq\]](#sigma_eq){reference-type="ref" reference="sigma_eq"}) successively with respect to $\la$. Using the known asymptotics of $\sigma(s;1)$ and the differential equation ([\[sigma_eq\]](#sigma_eq){reference-type="ref" reference="sigma_eq"}) satisfied by $\sigma(s;\la)$ for all $\la$, one can find asymptotic expansions for the quantities $$\sigma_{n}(s)\,:=\,\frac{\pl^{n}\sigma}{\pl\la^{n}}\biggr\vert_{\la=1},$$ and these in turn can be used to find expansions for the $r(n;s)$. This approach is inherently incomplete since yet another undetermined constant enters the picture. And there are also computational problems since when one expresses the $r(n,s)$ in terms of the $\sigma_{n}(s)$ a large amount of cancellation occurs, with the result that even the first-order asymptotics of $r(n;s)$ are out of reach by this method when $n$ is large.

The second approach uses the easily-established identity r(n;s) = \_i\_1\<...\<i\_n (1-\_i\_1)(1-\_i\_n) []{#rexp label="rexp"} where $\la_{0}>\la_{1}>\cdots$ are the eigenvalues of the integral operator $K$ with $\la=1$ acting on $(0,s)$. It turns out that this operator, rescaled so that it acts on $(0,1)$, commutes with the differential operator ${\cal L}$ defined by $${\cal L}f(x)\,=\,(x(1-x)f'(x))'\,-\,(\frac{\al^{2}}{4x}+\frac{sx}{4})\,f(x),$$ with appropriate boundary conditions on $f$. Applying the WKB method to the equation, and a simple relationship between the eigenvalues of $K$ (as functions of $s$) and its eigenfunctions, we are able to derive the following asymptotic formula for the eigenvalues as $s\ra\iy$:  - \_i\~  s\^i+ e\^-2 2\^4i+2+2. From this and ([\[rexp\]](#rexp){reference-type="ref" reference="rexp"}) we deduce r(n;s)  \~{\_k=0\^n-1(+k+1) k!}\^-n  2\^-n(2n+2+1) s\^\--n e\^2n~~s~~.

For the special case $\al=0$, the quantity $r(1;s)$ can be expressed exactly in terms of Bessel functions (see ([\[bessel_r\]](#bessel_r){reference-type="ref" reference="bessel_r"}) below).
