---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-028-63-integral-ramanujan-identity
section_title: "Integral Ramanujan identity"
section_number: 6.3
pages: 16-17
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.928
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
Consider the following Fourier integral: $$\label{ramanint}
\Psi(u,v,w)\equiv
\int_{\mathbb R}\frac{e_b(x+u)}{e_b(x+v)}e^{2\pi iwx}\, dx,$$ where $$\label{restrictions1}
\Im(v+c_b)>0,\quad\Im(-u+c_b)>0, \quad \Im(v-u)<\Im w<0.$$ Restrictions ([\[restrictions1\]](#restrictions1){reference-type="ref" reference="restrictions1"}) actually can be considerably relaxed by deforming the integration path in the complex $x$ plane, keeping the asymptotic directions of the two ends within the sectors $\pm(|\arg x|-\pi/2)>\arg b$. So, the enlarged in this way domain for the variables $u,v,w$ has the form: $$\label{restrictions2}
|\arg (iz)|<\pi-\arg b,\quad z\in\{w,v-u-w,u-v-2c_b\}.$$ Regarding $e_b(z)$ as a 'non-compact' analogue of the q-exponent $(x;q)_\infty$, definition ([\[ramanint\]](#ramanint){reference-type="ref" reference="ramanint"}) can be interpreted as the corresponding integral counterpart of the Ramanujan sum: $${}_1\!\psi_1(x,y,z)\equiv\sum_{n\in\mathbb Z}\frac{(x;q)_n}{(y;q)_n}z^n.$$ The latter is known to be evaluated explicitly, the result being the famous Ramanujan summation formula: $${}_1\!\psi_1(x,y,z)=\frac{(q;q)_\infty(y/x;q)_\infty(xz;q)_\infty
  (q/xz;q)_\infty}{(y;q)_\infty(q/x;q)_\infty(z;q)_\infty(y/xz;q)_\infty}.$$ Remarkably, integral ([\[ramanint\]](#ramanint){reference-type="ref" reference="ramanint"}) can be evaluated explicitly as well. Indeed, using the residue method, we easily come to the following result: $$\begin{gathered}
\label{ramanres1}
  \Psi(u,v,w)=
  \frac{e_b(u-v-c_b)e_b(w+c_b)}{e_b(u-v+w-c_b)}
  e^{-2\pi iw(v+c_b)+i\pi(1-4c_b^2)/12} \\\label{ramanres2}
  =\frac{e_b(v-u-w+c_b)}{e_b(v-u+c_b)e_b(-w-c_b)}
  e^{-2\pi iw(u-c_b)-i\pi(1-4c_b^2)/12},
\end{gathered}$$ where the two expressions in the right hand side are related to each other through the inversion relation ([\[inversion\]](#inversion){reference-type="ref" reference="inversion"}). The similarity of this result with Ramanujan sum becomes very transparent if we rewrite the latter in the form: $$\label{ramsum}
\sum_{n\in\mathbb Z}\frac{(yq^n;q)_\infty}{(xq^n;q)_\infty}z^n=
\frac{(y/x;q)_\infty(q/z;q)_\infty
}{(y/xz;q)_\infty}\frac{\theta_q(xz)}{\theta_q(x)\theta_q(z)}(q;q)^2_\infty,$$ where the $\theta_q$-function is defined by $$\label{raminv}
\theta_q(x)\equiv (q;q)_\infty(x;q)_\infty(q/x;q)_\infty=
\sum_{n\in\mathbb Z}q^{n(n-1)/2}(-x)^n.$$ Comparing the inversion relation ([\[inversion\]](#inversion){reference-type="ref" reference="inversion"}) with eqn ([\[raminv\]](#raminv){reference-type="ref" reference="raminv"}), we conclude that the non-compact analogue of the $\theta$-function is the Gaussian exponent, and the structures of eqns ([\[ramsum\]](#ramsum){reference-type="ref" reference="ramsum"}) and ([\[ramanres1\]](#ramanres1){reference-type="ref" reference="ramanres1"}) are now quite similar.
