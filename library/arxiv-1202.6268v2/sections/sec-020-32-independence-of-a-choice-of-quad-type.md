---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-020-32-independence-of-a-choice-of-quad-type
section_title: "Independence of a choice of quad type"
section_number: 3.2
pages: 16-17
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.946
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.invgauge label="sec.invgauge"}

Now, let us fix a manifold $M$, a triangulation $\mathcal{T}$ with $N$ tetrahedra, and an enhanced Neumann-Zagier datum $\widehat\beta_\mathcal{T}=(z,\mathbf A,\mathbf B,f)$.

To prove independence of quad type, it is sufficient to check that $\tau_\mathcal{T}$ is invariant under a cyclic permutation of the first triple of shape parameters $(z_1,z_1',z_1'')$, while holding fixed the choice of meridian loop and redundant edge. Let us write $z=(z_1,\dots,z_N)$, $\nu=(\nu_1,\dots,\nu_N)^T$, $f=(f_1,...,f_N)^T$, and

$$\mathbf A = \big(a_1,\,a_2,\,\cdots,a_N\big)\,,\quad \mathbf B 
= \big(b_1,\,b_2,\,\cdots,b_N\big)\,,$$

in column notation. After the permutation, a new Neumann-Zagier datum is given by $(\widetilde z, \widetilde{\mathbf A} ,\,\widetilde{\mathbf B},\widetilde f )$ where

$$\widetilde z = (z_1',z_2,...,z_N)\,,\quad \widetilde z'=(z_1'',z_2',...,z_N')\,,
\quad \widetilde z'' = (z_1,z_2'',...,z_N'')\,,$$

$$\widetilde{\mathbf A} = \big(-b_1,\,a_2,\,\cdots,a_N\big)\,,\quad \widetilde{\mathbf B} 
= \big(a_1-b_1,\,b_2,\,\cdots,b_N\big)\,,\quad  \widetilde
\nu= (n_1-b_1,n_2,...,n_N)^T\,.$$

The new shapes satisfy $\widetilde z^{\tilde{\mathbf A}}\widetilde z''^{\tilde{\mathbf B}}=(-1)^{\tilde \nu}$.

We also naturally obtain a new flattening $(\widetilde f,\widetilde f',\widetilde f'')$ by permuting

$$\widetilde f=(f_1',f_2,...,f_N)^T\,,\quad \widetilde f'=(f_1'',f_2',...,f_N')^T\,,
\quad \widetilde f''=(f_1,f_2'',...,f_N'')^T\,;$$

this is an integer solution to $\widetilde{\mathbf A}\tilde f+\widetilde{\mathbf B}\tilde f''= \widetilde\nu$ and $\tilde f+\tilde f'+\tilde f''=1$.

The torsion $\tau_{\mathcal{T}}$ [\[torintro\]](#torintro){reference-type="eqref" reference="torintro"} consists of two parts, a determinant and a monomial correction. By making use of the relations $z_1+z_1'{}^{-1}-1=0$ and $z_1z_1'z_1''=-1$, we find the determinant with the permuted Neumann-Zagier datum to be

$$\begin{aligned}
\det\big(\widetilde{\mathbf A}\Delta_{\tilde z''}+\widetilde{\mathbf B}\Delta_{\tilde z}^{-1}\big) &= 
\det \big( -b_1z_1 +(a_1-b_1)z_1'^{-1},\; a_2 z_2''+b_2 z_2^{-1} ,\;\cdots ,\; 
a_N z_N''+b_N z_N^{-1} \big) \notag\\
 &= \det\big( a_1 z_1'^{-1}-b_1 ,\; a_2 z_2''+b_2 z_2^{-1} ,\;\cdots ,\; 
a_N z_N''+b_N z_N^{-1} \big) \notag\\
 &= -z_1 \det\big( a_1 z_1''+b_1 z_1^{-1} ,\; a_2 z_2''+b_2 z_2^{-1} ,\;
\cdots ,\; a_N z_N''+b_N z_N^{-1} \big) \notag\\
 &= -z_1\det\big(\mathbf A\Delta_{z''}+\mathbf B\Delta_{z}^{-1}\big)\,.
\end{aligned}$$

By simply using $z_1z_1'z_1''=-1$ and $f_1+f_1'+f_1''=1$, we also see that the monomial correction transforms as

$$\begin{aligned}
 \widetilde z^{\tilde f''}\widetilde z''{}^{-\tilde f} &=
 z^{f''}z''{}^{-f} \frac{ z_1'{}^{f_1}z_1{}^{-f_1'} }{z_1{}^{f_1''}z_1''{}^{-f_1}} 
\notag\\
 &= z^{f''}z''{}^{-f} 
(-1)^{f_1}\frac{(z_1z_1'')^{-f_1}z_1{}^{f_1+f_1''-1}}{z_1{}^{f_1''}z_1''{}^{-f_1}} 
\notag \\
 &= z^{f''}z''{}^{-f}\,(-1)^{f_1}z_1^{-1}\,.
\end{aligned}$$

The extra factors $z_1^{\pm 1}$ in the two parts of the torsion precisely cancel each other, leading in the end to

$$\det\big(\widetilde{\mathbf A}\Delta_{\tilde z''}
+\widetilde{\mathbf B}\Delta_{\tilde z}^{-1}\big)\widetilde z^{\tilde f''}
\widetilde z''{}^{-\tilde f} = (-1)^{f_1+1}\det\big(\mathbf A\Delta_{z''}
+\mathbf B\Delta_{z}^{-1}\big)z^{f''}z''{}^{-f}\,.$$

This is just as desired, showing that the torsion is invariant up to a sign.
