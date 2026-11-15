---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-030-45-invariance-of-the-generalized-torsion
section_title: "Invariance of the generalized torsion"
section_number: 4.5
pages: 26-27
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.644
latex_coverage_ratio: 0.976
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.utorsion label="sec.utorsion"}

We finally have all the required ingredients for the generalized torsion formula. Let $M$ be a three-manifold with torus boundary, and $\rho_m:\pi_1(M)\to \text{(P)SL}(2,\mathbb{C})$ a representation with meridian eigenvalue $m$. Let $\mathcal{T}$ be a $\rho_m$-regular triangulation of $M$, which exists by Lemma [\[lem.wellknown\]](#lem.wellknown){reference-type="ref" reference="lem.wellknown"} at least for a dense set of representations on the geometric component of the character variety. Choose an enhanced Neumann-Zagier datum $(z,\mathbf A,\mathbf B,f)$, with $z=z(\rho_m)$ satisfying the deformed gluing equations [\[uglue\]](#uglue){reference-type="eqref" reference="uglue"} and $f$ satisfying [\[uflat\]](#uflat){reference-type="eqref" reference="uflat"}. Then, as in [\[utor\]](#utor){reference-type="eqref" reference="utor"}, we define

$$\notag
\tau_\mathcal{T}(\rho_m) := \pm\frac12\det\big(\mathbf A\Delta_{z''}
+\mathbf B\Delta_z^{-1}\big)z^{f''}z''{}^{-f}  \,.$$

We can now prove Theorem [\[thm.utor\]](#thm.utor){reference-type="ref" reference="thm.utor"}.

Repeating verbatim the arguments of Section [\[sec.torsion\]](#sec.torsion){reference-type="ref" reference="sec.torsion"}, it is easy to see that $\tau_{\mathcal{T}}$ is independent of a choice of quad type, a choice of an edge of $\mathcal{T}$ and a choice of a meridian loop. The crucial observation is that the equations $\mathbf AZ+\mathbf B Z''=i\pi \nu$ (including the meridian equation) are never used in the respective proofs. Therefore, deforming the meridian equation by $u\neq 0$ does not affect anything. For the same reason, it is not hard to see that the formula is invariant under $\rho_m$-regular 2--3 moves, by repeating the argument of Section [\[sec.inv23\]](#sec.inv23){reference-type="ref" reference="sec.inv23"}.

The only nontrivial verification required is that $\tau_{\mathcal{T}}$ is independent of the choice of flattening. This does use the gluing equations in a crucial way. We check it now for $m\neq 1$.

Choose logarithms $(Z,Z',Z'')$ of the shape parameters and a logarithm $u$ of $m$ such that $Z+Z'+Z''=i\pi$ and

$$\label{uveceqs} 
\mathbf AZ+\mathbf BZ''=2\bm u+i\pi \nu\,,$$

where $\bm{u}$ denote the $N$-dimensional vector $(0,0,....,0,u)^T$. By independence of quad type and Lemma [\[lemma.B\]](#lemma.B){reference-type="ref" reference="lemma.B"}, we may assume we are using a quad type with non-degenerate $\mathbf B$. Now, suppose that $(f,f',f'')$ and $(\widetilde f,\widetilde f',\widetilde f'')$ are two different generalized flattenings. Then:

$$\begin{aligned}
(Z\cdot f''-Z''\cdot f)-&(Z\cdot \widetilde f''-Z''\cdot \widetilde f) \\&=
 Z\cdot (f''-\widetilde f'') + \mathbf B^{-1}(\mathbf A Z-i\pi \nu-2\bm u)\cdot (f-\widetilde f) \\
 &= Z\cdot (f''-\widetilde f'') 
+  Z\cdot \mathbf B^{-1}\mathbf A(f-\widetilde f)-i\pi\mathbf B^{-1}\nu\cdot (f-\widetilde f) 
-2\mathbf B^{-1}\bm u\cdot(f-\tilde f) \\
 &= -i\pi\mathbf B^{-1}\nu\cdot (f-\widetilde f) -2\mathbf B^{-1}\bm u\cdot(f-\tilde f)\\
 &= i\pi (f''\cdot \widetilde f-f\cdot \widetilde f'') -2\mathbf B^{-1}\bm u\cdot(f-\tilde f)\,,
\end{aligned}$$

by manipulations similar to those of Section [\[sec.invflat\]](#sec.invflat){reference-type="ref" reference="sec.invflat"}. The new term $2\mathbf B^{-1}\bm u\cdot(f-\tilde f)$ is now dealt with with by completing the Neumann-Zagier matrices $(\mathbf A\;\mathbf B)$ to a full symplectic matrix $\left(\begin{smallmatrix} \mathbf A & \mathbf B \\ \mathbf C & 
\mathbf D\end{smallmatrix}\right) \in \mathrm{Sp}(2N,\mathbb Q)$, whose bottom row agrees with $(C,D)$. The symplectic condition implies that $\mathbf A \mathbf D^T-\mathbf B \mathbf C^T=I$, or $\mathbf B^{-1}=\mathbf B^{-1}\mathbf A\mathbf D^T-\mathbf C^T$. Then

$$\begin{aligned}
\mathbf B^{-1}\bm u\cdot(f-\tilde f) &=
 \mathbf B^{-1}\mathbf A\mathbf D^T \bm u\cdot (f-\tilde f) 
- \mathbf C^T \bm u\cdot (f-\tilde f) \\
 &= \bm u\cdot \mathbf D\mathbf B^{-1}\mathbf A (f-\tilde f) 
- \bm u\cdot \mathbf C(f-\tilde f) \\
 &= -\bm u\cdot\big( \mathbf C(f-\tilde f)+\mathbf D(f''-\tilde f'')\big) \\
 &= -u\big(C\cdot(f-\tilde f)+D\cdot (f''-\tilde f'')\big)\,.
\end{aligned}$$

In this last equation, only the bottom row of $\mathbf C$ and $\mathbf D$ appears, due to the contraction with $\bm u = (0,0,...,0,u)$. But this bottom row is precisely what enters the generalized flattening equations [\[uflat\]](#uflat){reference-type="eqref" reference="uflat"}; since both flattenings satisfy these equations, we must have $\mathbf B^{-1}\bm u\cdot (f-\tilde f)=0$. Therefore, upon exponentiating, we find

$$z^{f''}z''{}^{-f} = (-1)^{f''\cdot \tilde f-f\cdot \tilde f''} 
z^{\tilde f''}z''{}^{-\tilde f} = \pm z^{\tilde f''}z''{}^{-\tilde f}\,,$$

which demonstrates that $\tau_{\mathcal{T}}$ is independent of the choice of flattening. Theorem [\[thm.utor\]](#thm.utor){reference-type="ref" reference="thm.utor"} follows. 0◻

## Example: $\mathbf 4_1$ continued {#sec.utor41}

We briefly demonstrate the generalized torsion formula, using representations on the geometric component of the character variety $X_{\mathbf{4_1}}$ for the figure-eight knot complement.

![Longitude path for the figure-eight knot complement.](cusp41L){#fig.cusp41L width="4.3in"}

We may consider the same triangulation as in Section [\[sec.41triang\]](#sec.41triang){reference-type="ref" reference="sec.41triang"}. The edge and meridian equations [\[41glue\]](#41glue){reference-type="eqref" reference="41glue"} are deformed to

$$\label{41m} z^2w^2z''w''=1\,, \qquad zwz''=-m^2\,,$$

with $z''=1-z^{-1}$, $w''=1-w^{-1}$ as usual. In addition, there is a longitude equation that may be read off from the longitude path in Figure [1](#fig.cusp41L){reference-type="ref" reference="fig.cusp41L"}. In logarithmic (combinatorial) form, we have $-2Z+2Z'=2v$, or

$$\label{41L} -4Z-2Z''=2v-2\pi i\,,$$

from which we identify

$$C = (-2,0)\,,\qquad D = (-1,0)\,,\qquad \nu_\lambda = -1.$$

Dividing [\[41L\]](#41L){reference-type="eqref" reference="41L"} by two and exponentiating, we find

$$\label{41ell} z^{-2}z''{}^{-1}=\ell\,,$$

with $\ell=-e^v$. This is the appropriate square root of [\[uglueL\]](#uglueL){reference-type="eqref" reference="uglueL"} for lifting the geometric representations to $\mathrm{SL}(2,\mathbb{C})$. We can easily check it: by eliminating shape parameters from [\[41m\]](#41m){reference-type="eqref" reference="41m"} and [\[41ell\]](#41ell){reference-type="eqref" reference="41ell"}, we recover the geometric $\mathrm{SL}(2,\mathbb{C})$ A-polynomial for the figure-eight knot,

$$A_{\mathbf{4_1}}^{\rm geom}(\ell,m) = m^4-(1-m^2-2m^4-m^6+m^8)\ell+m^4\ell^2\,.$$

We may also use equations [\[41m\]](#41m){reference-type="eqref" reference="41m"}--[\[41ell\]](#41ell){reference-type="eqref" reference="41ell"} to express the shape parameters as functions of $\ell$ and $m$. We find

$$\label{zw41m} z = -\frac{m^2-m^{-2}}{1+m^2\ell} \,,\qquad w= \frac{m^2+\ell}{m^2-m^{-2}}\,.$$

These are functions on the curve $Y_{\mathbf{4_1}}^{\rm geom}=\{A_{\mathbf{4_1}}^{\rm geom}(\ell,m)=0\}$.

The flattening [\[flat41\]](#flat41){reference-type="eqref" reference="flat41"} does *not* satisfy the new longitude constraint $C\cdot f+D\cdot f''=\nu_\lambda$, so we must find one that does. The choice

$$(f_z,f_z',f_z'';f_w,f_w',f_w'') =(0,0,1;0,0,1)$$

will work. Repeating the calculation of Section [\[sub.torexample\]](#sub.torexample){reference-type="ref" reference="sub.torexample"} with the same $\mathbf A$ and $\mathbf B$ but the new generalized flattening, we now obtain

$$\begin{aligned}
 \tau_{\mathbf{4_1}}(\rho_m) &= \pm \frac12 \det\begin{pmatrix} z''+1 & w''+1\\ 1 & w'' 
\end{pmatrix} z w \notag \\
&= \pm\frac12(z''w''-1)zw \notag \\
&= \pm\frac{1-m^2-2m^4-m^6+m^8-2m^4\ell}{2m^4(m^2-m^{-2})}\,. \label{41utor}
\end{aligned}$$

This is in full agreement with the torsion found by [@GuM; @DGLZ]. Note that for fixed $m$ there are *two* choices of representation $\rho_m$ on the geometric component of the character variety; they correspond to the two solutions of $A_{\mathbf{4_1}}^{\rm geom}(\ell,m)=0$ in $\ell$.

::: remark
It is interesting to observe that the numerator of [\[41utor\]](#41utor){reference-type="eqref" reference="41utor"} is exactly $\partial A_{\mathbf{4_1}}^{\rm geom}/\partial\ell$. That the numerator of the geometric torsion typically carries a factor of $\partial A_{\mathbf{4_1}}^{\rm geom}/\partial\ell$ might be gleaned from the structure of "$\hat A$-polynomials" in [@DGLZ; @GukovS], and will also be explored elsewhere.
:::
