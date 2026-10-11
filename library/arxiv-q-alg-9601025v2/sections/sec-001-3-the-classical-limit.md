---
doc_id: arxiv-q-alg-9601025v2
doc_title: "arXiv:q-alg/9601025v2 25 Mar 1996"
section_id: sec-001-3-the-classical-limit
section_title: "The classical limit"
section_number: 3
pages: 3-7
source_pdf: 9601025v2.pdf
source_sha256: 369b0a1a92ce67a8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 1.0
---
Here we calculate explicitly the leading asymptotics at $N\to\infty$ of the invariant for the hyperbolic knots from section [\[sec1\]](#sec1){reference-type="ref" reference="sec1"} and justify formula ([\[main\]](#main){reference-type="ref" reference="main"}).

First, for a positive real $\gamma$ and complex $p$ with \|Re p\|\<+, define two functions []{#mainfun label="mainfun"} f\_(p)=S\_(-)/S\_(p), f\_(p)=S\_(-p)/S\_(-), where []{#fad label="fad"} S\_(p)=\_-\^+ (x)(x), the singularity of the integrand at $x=0$ being put below the contour of integration. In [@F1] the function ([\[fad\]](#fad){reference-type="ref" reference="fad"}) is shown to be a particular solution to the functional equation: []{#funeq label="funeq"} (1+e\^ip)S\_(p+)=S\_(p-). Via this functional equation the definition of the function $S_\gamma(p)$ can be extended to the whole complex plane.

For fixed $p$ the leading asymptotics of $S_\gamma(p)$ at $\gamma\to 0$ is given by Euler's dilogarithm: []{#as label="as"} S\_(p)\~Li_2(-e\^ip),, where Li_2(z)=-\_0\^zdu. For numerical calculations the following formula will be useful (see, for example, [@K]) : Im Li_2(re\^i)= (r)+()+()-(+), where $0<r\le1$, =(r,)=(), and []{#lob label="lob"} ()=-\_0\^\|2\| d, is Lobachevsky's function.

From ([\[mainfun\]](#mainfun){reference-type="ref" reference="mainfun"}) and ([\[funeq\]](#funeq){reference-type="ref" reference="funeq"}) it is easy to see that $f_\gamma(p)$ and $\overline f_\gamma(p)$ are analytic continuations of the symbols $(\omega)_k$ and $(\omega)_k^*$ in the sense that []{#anal label="anal"} ()\_k=f\_(-++2k), ()\_k\^\*=f\_(-++2k), where []{#gamma label="gamma"} =/N. Formulae ([\[anal\]](#anal){reference-type="ref" reference="anal"}) enable us to rewrite the summations in ([\[4_1\]](#4_1){reference-type="ref" reference="4_1"}), ([\[5_2\]](#5_2){reference-type="ref" reference="5_2"}), ([\[6_1\]](#6_1){reference-type="ref" reference="6_1"}) as contour integrals, one has just to replace symbols $(\omega)_k$ and $(\omega)_k^*$ by their analytic continuations, and each summation, by a contour integral: \_kdp () with an appropriately chosen contour.

In what follows $\gamma$ will be assumed to be specified as in ([\[gamma\]](#gamma){reference-type="ref" reference="gamma"}).

##  Knot $4_1$ (figure-eight knot)

The exact formula ([\[4_1\]](#4_1){reference-type="ref" reference="4_1"}) can be rewritten as a contour integral: []{#contour4_1 label="contour4_1"} \_1=\_Cdp ()f\_(p)f\_(p), Where contour $C$ encircles $N$ points: -++2kk\<N, in the counterclockwise direction. In the large $N$ (small $\gamma$) limit integral ([\[contour4_1\]](#contour4_1){reference-type="ref" reference="contour4_1"}), by using ([\[as\]](#as){reference-type="ref" reference="as"}), asymptotically can be approximated by \_1\~dz \[Li_2(z)-Li_2(1/z)\]. The saddle point approximation of the last integral gives the result: []{#as41 label="as41"} \_1\~ ,=/N, where []{#vol4_1 label="vol4_1"} V(4_1)=4(/6)=2.02988321... Formula ([\[vol4_1\]](#vol4_1){reference-type="ref" reference="vol4_1"}) is in agreement with the known hyperbolic volume of the figure-eight knot complement [@AHW].

## Knot $5_2$

The sum ([\[5_2\]](#5_2){reference-type="ref" reference="5_2"}) at large $N$ is approximated by the double contour integral []{#contour5_2 label="contour5_2"} \_2\~dzdu \[2Li_2(z)+Li_2(1/u)+(z,u) -\^2/2\], where []{#alpha label="alpha"} (z,u)=(z)(u). The stationary points are described by the algebraic equations: []{#stat1 label="stat1"} u+z=uz,u=(1-z)\^2. The maximal contribution to the integral comes from the solution $(z_0,u_0)$ to ([\[stat1\]](#stat1){reference-type="ref" reference="stat1"}) with the property: Im z_0\<0\<Im u_0. Thus, we obtain for asymtotics of the absolute value of the invariant: \|\_2\|\~,=/N, where V(5_2)=-Im (2Li_2(z_0)+Li_2(1/u_0)+(z_0,u_0)) =2.82812208\... in agreement with [@AHW].

## Knot $6_1$

The sum ([\[6_1\]](#6_1){reference-type="ref" reference="6_1"}) at large $N$ is approximated by the triple integral $$\begin{aligned}
\label{contour6_1}
\langle6_1\rangle&\sim&\int dzdudv\  
\exp\frac{i}{2\gamma}[
\mbox{Li}_2(z)-\mbox{Li}_2(1/z)-\mbox{Li}_2(u)
+\mbox{Li}_2(1/v)\nonumber\\
&+&\alpha(uv/z,z/u)+2\pi i\log(u/z)],
\end{aligned}$$ where $\alpha(z,u)$ is defined in ([\[alpha\]](#alpha){reference-type="ref" reference="alpha"}). The stationary points are solutions to the algebraic system of equations: z(1-z)\^2=-u\^2v,z\^2(1-u)=u\^2v,z(1-v)=-uv. The maximal contribution to the integral comes from the solution $(z_0,u_0,v_0)$ with Im z_0\<0\<Im (u_0v_0). Thus, the asymptotics of the absolute value of the integral reads \|\_1\|\~,=/N, where $$\begin{aligned}
V(6_1)=-\mbox{Im}\ (\mbox{Li}_2(z_0)-\mbox{Li}_2(1/z_0)-\mbox{Li}_2(u_0)
+\mbox{Li}_2(1/v_0)\nonumber\\
+\alpha(u_0v_0/z_0,z_0/u_0)+2\pi i\log(u_0/z_0))=3.16396322...
\end{aligned}$$ again in agreement with [@AHW].
