---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-014-61-geometry-of-the-critical-point
section_title: "Geometry of the critical point"
section_number: 6.1
pages: 41-43
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.889
latex_coverage_ratio: 0.8
---
[]{#Appendix-geometry label="Appendix-geometry"}

### The geometric equation

Note that the hyperbolic geometric equations (which include the gluing equations and Dehn filling equations) for the $M_{p,q}$ can be written as follows: $$\label{equantion-geom1} 
\left\{ \begin{aligned}
         &\log w+\log x+\log y+\log z = 2\pi\sqrt{-1}, \\
          &        \log(1-w)+\log(1-x)-\log(1-y)-\log(1-z)=0,\\
          &qu_1+v_1=-2\pi\sqrt{-1},  \\
          &u_2-pv_2=-2\pi\sqrt{-1},
                          \end{aligned} \right.$$ where $$\begin{aligned}
    u_1&=\log (w-1)+\log x+\log y-\log(y-1)-\pi\sqrt{-1},\\\nonumber
    v_1&=2\log x +2\log y-2\pi\sqrt{-1}, \\\nonumber
    u_2&=\log (w-1)+\log x+\log z-\log(z-1)-\pi\sqrt{-1},\\\nonumber
    v_2&=2\log x +2\log z-2\pi\sqrt{-1}.
\end{aligned}$$

It follows that $$\begin{aligned}
&xyzw=1, \label{geomequation-1}\\
&(1-w)(1-x)=(1-y)(1-z), \label{geomequation-2} \\
&(xz)^{2p-1}=-\frac{w-1}{z-1}, \label{geomequation-3} \\
&\left(\frac{-(w-1)xy}{y-1}\right)^q(xy)^2=1. \label{geomequation-4}
\end{aligned}$$

Then, we have

::: proposition
$$\begin{aligned}
      w&=1-(xz)^{2p-1}(z-1) \\\nonumber
      y&=1-(xz)^{2p-1}(x-1)
    
\end{aligned}$$ where $x,z$ is determined by the following two equations $$\begin{aligned}
    ((xz)^{2p-1}(x-1)-1)((xz)^{2p-1}(z-1)-1)xz&=1\\\nonumber
    \left(-\frac{z-1}{x-1}\right)^q(x(1-(xz)^{2p-1}(x-1)))^{q+2}=1
\end{aligned}$$
:::

::: proof
*Proof.* From equation ([\[geomequation-3\]](#geomequation-3){reference-type="ref" reference="geomequation-3"}), we obtain the first equation, $$\begin{aligned}
      w&=1-(xz)^{2p-1}(z-1). 
    
\end{aligned}$$ From equation ([\[geomequation-1\]](#geomequation-1){reference-type="ref" reference="geomequation-1"}), we obtain $$\begin{aligned}
    y=\frac{1}{xzw}=\frac{1}{xz(1-(xz)^{2p-1}(z-1))}.
\end{aligned}$$ From equation ([\[geomequation-2\]](#geomequation-2){reference-type="ref" reference="geomequation-2"}), we obtian $$\begin{aligned}
    y=\frac{z+xw-w-x}{z-1}=1-(xz)^{2p-1}(x-1).
\end{aligned}$$

Moreover, suppose $(x,y,z,w)$ is a solution to the geometric equations ([\[equantion-geom1\]](#equantion-geom1){reference-type="ref" reference="equantion-geom1"}), then the complex volume of the $M_{p,q}$ is given by the following formula $$\begin{aligned}
&Vol(M_{p,q})+\sqrt{-1}CS(M_{p,q})\\\nonumber&=-\frac{1}{\sqrt{-1}}\left(R(w)+R(x)+R\left(\frac{1}{1-y}\right)+R\left(\frac{1}{1-z}\right)\right)\\\nonumber
&+\frac{\pi}{2}\left(3\pi\sqrt{-1}\log(w-1)+\log(x)+\log(y)-\log(y-1)\right.\\\nonumber
&\left.+\frac{1}{p}(3\pi\sqrt{-1}+\log(w-1)+\log(x)+\log(z)-\log(z-1))\right) \mod \pi^2\sqrt{-1}\mathbb{Z},  
\end{aligned}$$ where $$\begin{aligned}
R(x)=\frac{1}{2}\log(x)\log(1-x)+\text{Li}_2(x).
\end{aligned}$$ ◻
:::
