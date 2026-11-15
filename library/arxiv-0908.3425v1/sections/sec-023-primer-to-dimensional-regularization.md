---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-023-primer-to-dimensional-regularization
section_title: "Primer to dimensional regularization"
section_number: null
pages: 33-35
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.979
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
If we want to use the Lagrangian of Eq. ([\[3:2:3:lol\]](#3:2:3:lol){reference-type="ref" reference="3:2:3:lol"}) beyond the tree level, we will encounter ultraviolet divergences from loop integrals. For the regularization of the loop diagrams we will make use of dimensional regularization [@{'tHooft:fi:10}], [@Leibbrandt:1975dj:10], [@{'tHooft:1978xw:10}], because it preserves algebraic relations between the Green functions (Ward identities). We will illustrate the method by considering the following simple example, $$\label{3:2:5:drb:int}
I=\int\frac{\mbox{d}^4k}{(2\pi)^4}\frac{i}{k^2-M^2+i0^+},$$ which shows up in the generic diagram of Fig. [1](#3:2:5:fig:dimregexample){reference-type="ref" reference="3:2:5:fig:dimregexample"}.

<figure id="3:2:5:fig:dimregexample">
<div class="center">

</div>
<figcaption>Generic one-loop diagram. The black box denotes some unspecified vertex structure which is irrelevant for the discussion.</figcaption>
</figure>

Introducing $a\equiv\sqrt{\vec{k}\,^2+M^2}>0$, we define $f(k_0)=\{[k_0+(a-i0^+)][k_0-(a-i0^+)]\}^{-1}$. In order to determine $\int_{-\infty}^{\infty} \mbox{d}k_0 f(k_0)$ as part of the calculation of $I$, we consider $f$ in the complex $k_0$ plane and make use of Cauchy's theorem $\oint_C \mbox{d}z f(z)=0$ for functions which are differentiable in every point inside the closed contour $C$. Choosing the path as shown in Fig. [2](#3:2:4:wickrotation_fig){reference-type="ref" reference="3:2:4:wickrotation_fig"} and taking account of the fact that the quarter circles at infinity do not contribute, we obtain the so-called Wick rotation $$\label{3:2:4:wickrotation}
\int_{-\infty}^\infty \mbox{d}t\,f(t)=-i\int_{\infty}^{-\infty}\mbox{d}t\, f(it)
=i\int_{-\infty}^\infty \mbox{d}t\, f(it).$$

<figure id="3:2:4:wickrotation_fig">
<div class="center">

</div>
<figcaption><span id="3:2:4:wickrotation_fig" label="3:2:4:wickrotation_fig"></span> Path of integration in the complex <span class="math inline"><em>k</em><sub>0</sub></span> plane.</figcaption>
</figure>

As an intermediate result, the integral of Eq. ([\[3:2:5:drb:int\]](#3:2:5:drb:int){reference-type="ref" reference="3:2:5:drb:int"}) reads $$I=\int \frac{\mbox{d}^4 l}{(2\pi)^4} \frac{1}{l^2+M^2},$$ where $l^2=l_1^2+l_2^2+l_3^2+l_4^2$ denotes a Euclidian scalar product in four dimensions. Performing the angular integration in four dimensions and introducing a cutoff $\Lambda$ for the radial integration, the integral $I$ diverges quadratically for large values of $l$ (ultraviolet divergence): $$\begin{aligned}
\label{2:2:4:Icutoff}
I(\Lambda)&=&\frac{1}{8\pi^2}\int_0^\Lambda\mbox{d}l\frac{l^3}{l^2+M^2}
=\frac{\Lambda^2}{(4\pi)^2}+\frac{M^2}{(4\pi)^2}\ln\left(\frac{M^2}{\Lambda^2+M^2}\right)\nonumber\\
&=&\frac{M^2}{(4\pi)^2}\left[\frac{1}{x}+\ln(x)-\ln(1+x)\right],
\end{aligned}$$ where $x=M^2/\Lambda^2\to 0$ as $\Lambda\to\infty$. In dimensional regularization, we generalize the integral from 4 to $n$ dimensions and introduce polar coordinates $$\begin{aligned}
l_1&=& l\cos(\theta_1),\quad l_2= l\sin(\theta_1)\cos(\theta_2),\quad
l_3=l\sin(\theta_1)\sin(\theta_2)\cos(\theta_3),\nonumber\\
&\vdots&\nonumber\\
l_{n-1}&=&l\sin(\theta_1)\sin(\theta_2)\cdots\cos(\theta_{n-1}),\quad
l_{n}=l\sin(\theta_1)\sin(\theta_2)\cdots\sin(\theta_{n-1}),
\end{aligned}$$ where $0\leq l$, $\theta_i\in[0,\pi]$ ($i=1,\cdots,n-2$), and $\theta_{n-1}\in [0,2\pi]$. A general integral is then symbolically of the form $$\begin{aligned}
\int {\rm d}^n l\cdots = \int_0^\infty {\rm d}l\,l^{n-1}
\int_0^{2\pi}{\rm d}\theta_{n-1} \int_0^\pi
{\rm d}\theta_{n-2}\sin(\theta_{n-2})\cdots\int_0^\pi {\rm d}\theta_1
\sin^{n-2}(\theta_1)\cdots.
\end{aligned}$$ If the integrand does not depend on the angles, the angular integration can explicitly be carried out: $$\int {\rm d}\Omega_n=
2\frac{\pi^{\frac{n}{2}}}{\Gamma\left(\frac{n}{2}\right)}.$$ We define the integral for $n$ dimensions ($n$ integer) as $$I_n(M^2,\mu^2)=\mu^{4-n}\int\frac{{\rm d}^nk}{(2\pi)^n}\frac{i}{k^2-M^2+i0^+},$$ where the scale $\mu$ ('t Hooft parameter, renormalization scale) has been introduced so that the integral has the same dimension for arbitrary $n$. The integral formally reads $$\begin{aligned}
\label{2:2:4:iint}
I_n(M^2,\mu^2)&=& \mu^{4-n}2\frac{\pi^{\frac{n}{2}}}{\Gamma\left(
\frac{n}{2}\right)} \frac{1}{(2\pi)^n}
\int_0^\infty {\rm d}l
\frac{l^{n-1}}{l^2+M^2}\nonumber\\[0.5em]
&=&\mu^{4-n}\,\,2\frac{\pi^{\frac{n}{2}}}{\Gamma\left( \frac{n}{2}\right)}\,\,
\frac{1}{(2\pi)^n}\,\, \frac{1}{2} (M^2)^{\frac{n}{2}-1}\frac{\Gamma
\left(\frac{n}{2}\right)\Gamma\left(1-\frac{n}{2}\right)}{
\Gamma(1)}\nonumber\\
&=&\frac{\mu^{4-n}}{(4\pi)^{\frac{n}{2}}} (M^2)^{\frac{n}{2}-1}
\Gamma\left(1-\frac{n}{2}\right).
\end{aligned}$$ Since $\Gamma(z)$ is an analytic function in the complex plane except for poles of first order in $0,-1,-2,\cdots$, and $a^z=\exp[\ln(a)z]$, $a\in {\mathbbm R}^+$ is an analytic function in $\mathbbm C$, the right-hand side of Eq. ([\[2:2:4:iint\]](#2:2:4:iint){reference-type="ref" reference="2:2:4:iint"}) can be thought of as a function of a *complex* variable $n$ which is analytic in $\mathbbm C$ except for poles of first order for $n=2,4,6,\cdots$. The analytic continuation for complex $n$ reads $$\begin{aligned}
\label{3:2:4:IMmun}
I(M^2,\mu^2,n)&=&
\frac{M^2}{(4\pi)^2}\left(\frac{4\pi\mu^2}{M^2}\right)^{2-\frac{n}{2}}
\Gamma\left(1-\frac{n}{2}\right)
=\frac{M^2}{16\pi^2}\left[
R+\ln\left(\frac{M^2}{\mu^2}\right)\right]+O(n-4),
\end{aligned}$$ where $$\label{3:2:5:R}
R=\frac{2}{n-4}
-[\mbox{ln}(4\pi)+\Gamma'(1)+1].$$ The comparison between Eqs. ([\[3:2:4:IMmun\]](#3:2:4:IMmun){reference-type="ref" reference="3:2:4:IMmun"}) and ([\[2:2:4:Icutoff\]](#2:2:4:Icutoff){reference-type="ref" reference="2:2:4:Icutoff"}) illustrates the following general observations: in dimensional regularization power-law divergences are analytically continued to zero and logarithmic ultraviolet divergences of one-loop integrals show up as single poles in $\epsilon=4-n$.
