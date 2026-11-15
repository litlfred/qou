---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-020-48-a-new-state-integral-for-the-52-knot
section_title: "A new state-integral for the 52 knot?"
section_number: 4.8
pages: 53-54
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.939
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sec:newstateint label="sec:newstateint"}

In the case of the figure eight knot, the new state-integral was obtained by first writing down an integral formula for its colored Jones polynomial, in Habiro form, and then changing the integration contour to pick the contribution from the poles in the lower half plane. This led in particular to the "inverted" Habiro series $\mathcal{C}_0(x,q)$ in ([\[eq:Ixq\]](#eq:Ixq){reference-type="ref" reference="eq:Ixq"}). Although we do not have a similar complete theory for the ${\mathbf{5}_2}$ knot, we can however write down an integral formula for its colored Jones polynomial which lead, after a change of contour, to the corresponding inverted Habiro series. In fact, it is possible to write such an integral for all twist knots $K_p$ (the ${\mathbf{5}_2}$ knot corresponds to $p=2$).

Let us then consider the colored Jones polynomial of the twist knot $K_p$ in Habiro's form [@Mas:HabPol]:

$$\label{gen-habiro}
J^{K_p}_N (q;x)= \sum_{n=0}^{N-1} C^{K_p}_n (q) (qx;q)_n (q x^{-1};q)_n,$$

where

$$C^{K_p}_n(q)= -q^n \sum_{k=0}^n (-1)^k
q^{(p+1/2)k(k+1) +k } (q^{2k+1}-1) {(q;q)_n \over (q;q)_{n+k+1} (q;q)_{n-k}}.$$

It is easy to see that ([\[gen-habiro\]](#gen-habiro){reference-type="ref" reference="gen-habiro"}) can be written as a double contour integral

$$\int_{\mathcal{A}_z} \int_{\mathcal{A}_w} \mathcal{I}_{K_p}(z,w) {\rm d} z {\rm d} w,$$

where

$$\begin{aligned}
  &\mathcal{I}_{K_p} (z, w)=-\operatorname{\Phi}_{\mathsf{b}}^{-1} \left(z-{{\rm i}\over 2 {\mathsf{b}}} + u \right)
  \operatorname{\Phi}_{\mathsf{b}}^{-1} \left(z-{{\rm i}\over 2 {\mathsf{b}}} - u\right) \operatorname{\Phi}_{\mathsf{b}}^{-1}
  \left(z-{{\rm i}\over 2 {\mathsf{b}}} \right) \operatorname{\Phi}_{\mathsf{b}}
  \left(z-w+ {{\rm i}{\mathsf{b}}\over 2} -{{\rm i}\over  2 {\mathsf{b}}} \right)  \\
& \times 
\operatorname{\Phi}_{\mathsf{b}}\left(z+w+ {{\rm i}{\mathsf{b}}\over 2} -{{\rm i}\over  2{\mathsf{b}}}  \right)
{\rm e}^{-2 \pi {\rm i}(p+1/2)(w+ {{\rm i}\over 2 {\mathsf{b}}})^2} \left( {\rm e}^{ 2 \pi {\mathsf{b}}(z+w)}
  - {\rm e}^{ 2 \pi {\mathsf{b}}(z-w)} \right) \tanh\left( {\pi z \over {\mathsf{b}}} \right)
\tanh\left( {\pi w \over {\mathsf{b}}} \right),
\end{aligned}$$

and the contours $\mathcal{A}_{z,w}$ encircle the poles of the form ([\[jones-poles\]](#jones-poles){reference-type="ref" reference="jones-poles"}) in the upper complex planes of the $z$ and the $w$ variables, respectively. We can now deform the contour to pick the poles in the lower half planes of $z$, $w$. The contribution from the simple poles of the $\tanh$ functions in those half planes can be easily computed, and one finds in this way the inverted Habiro series,

$$\label{CKp}
\begin{aligned}
  \mathcal{C}_{K_p} (q, x)&={1 \over (x^{1\over 2}- x^{-{1\over 2}})^2}
  \sum_{n \ge 0} { q^{n (n+1)/2} \over (q x;q)_n (q x^{-1};q)_n} \\
  & \times \sum_{k \ge n}  q^{n (n+1)/2 + (p+1/2) k(k+1)- (n+k)(n+k+1)/2-n}
  (q^k - q^{-k-1}) {(q;q)_{n+k} \over (q;q)_n (q;q)_{k-n}}. 
\end{aligned}$$

This gives a general formula for all twist knots which agrees with the results of [@park-inverted] for $p=2$ (the ${\mathbf{5}_2}$ knot) and $p=3$ (the ${\mathbf{7}_2}$ knot).

It might be possible to find appropriate integration contours so that the integral of $\mathcal{I}_{K_p} (z, w)$ converges and provides the sought-for new state-integral which sees the series $\Phi^{(\sigma_0)} (x, \tau)$, as it happened in the case of the ${\mathbf{4}_1}$ knot. In the case of the ${\mathbf{5}_2}$ knot, these contours do exist and lead to a well-defined integral. We expect that an evaluation of such an integral by summing over the appropriate set of residues will give the inverted Habiro series [\[CKp\]](#CKp){reference-type="eqref" reference="CKp"}, together with additional contributions, as in [\[eq:Ixq\]](#eq:Ixq){reference-type="eqref" reference="eq:Ixq"}. However, the fact that the integrals are two-dimensional makes them more difficult to analyze. We expect to come back to this problem in the near future.
