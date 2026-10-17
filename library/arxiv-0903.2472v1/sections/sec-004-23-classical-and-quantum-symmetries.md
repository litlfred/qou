---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-004-23-classical-and-quantum-symmetries
section_title: "Classical and quantum symmetries"
section_number: 2.3
pages: 23-25
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.989
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
[]{#sec:symmetries label="sec:symmetries"}

A large supply of 3-manifolds with a single toral boundary can be obtained by considering knot complements [\[mkcomplement\]](#mkcomplement){reference-type="eqref" reference="mkcomplement"}; our main examples in Section [\[sec:example\]](#sec:example){reference-type="ref" reference="sec:example"} are of this type. As discussed above, the Lagrangian subvariety ${\cal L}\in{\cal M}_{\rm flat}(G_{\mathbb{C}},\Sigma)$ for any knot complement $M$ is defined by polynomial equations [\[aizero\]](#aizero){reference-type="eqref" reference="aizero"}. Such an ${\cal L}$ contains multiple branches, indexed by $\alpha$, corresponding to the different solutions to $\{A_i(l,m)=0\}$ for fixed $m$. In this section, we describe relationships among these branches and the corresponding perturbative invariants $Z^{(\alpha)}(M;\hbar,u)$ by using the symmetries of Chern-Simons theory with complex gauge group $G_{\mathbb{C}}$.

Before we begin, it is useful to summarize what we already know about the branches of ${\cal L}$. As mentioned in the previous discussion, there always exists a geometric branch --- or in the case of rank $r>1$ several geometric branches --- when $M$ is a hyperbolic knot complement. Like the geometric branch, most other branches of ${\cal L}$ correspond to genuinely nonabelian representations $\rho:\pi_1(\Sigma)\rightarrow G_{\mathbb{C}}$. However, for any knot complement $M$ there also exists an "abelian" component of ${\cal L}$, described by the equations $$l_1 = \ldots = l_r = 1\,.
\label{abell}$$ Indeed, since $H_1 (M)$ is the abelianization of $\pi_1 (M)$, the representation variety [\[mflatm\]](#mflatm){reference-type="eqref" reference="mflatm"} always has a component corresponding to abelian representations that factor through $H_1 (M) \cong {\mathbb{Z}}$, $$\pi_1 (M) \to H_1 (M) \to G_{{\mathbb{C}}}\,.$$ The corresponding flat connection, ${\cal A}^{({\rm abel})}$, is characterized by the trivial holonomy around a 1-cycle of $\Sigma = T^2$ which is trivial in homology $H_1 (M)$; choosing it to be the 1-cycle whose holonomy was denoted by $l = (l_1, \ldots, l_r)$ we obtain [\[abell\]](#abell){reference-type="eqref" reference="abell"}. Note that, under projection to the $u$-space, the abelian component of ${\cal L}$ corresponds to a single branch that we denote by $\alpha = {\rm abel}$.

The first relevant symmetry of Chern-Simons theory with complex gauge group $G_{\mathbb{C}}$ is conjugation. We observe that for every flat connection ${\cal A}^{(\rho)}$ on $M$, with $\rho=(u,\alpha)$, there is a conjugate flat connection ${\cal A}^{(\bar{\rho})}:= \overline{{\cal A}^{(\rho)}}$ corresponding to a homomorphism $\bar{\rho}=(\bar{u},\bar{\alpha})$. We use $\bar{\alpha}$ to denote the branch of ${\cal L}$ "conjugate" to branch $\alpha$; the fact that branches of ${\cal L}$ come in conjugate pairs is reflected in the fact that eqs. [\[aizero\]](#aizero){reference-type="eqref" reference="aizero"} have real (in fact, integer) coefficients. The perturbative expansions around ${\cal A}^{\rho}$ and ${\cal A}^{\bar{\rho}}$ are very simply related. Namely, by directly conjugating the perturbative path integral and noting that the Chern-Simons action has real coefficients, we find

[^1]

$\overline{Z^{\alpha}(M;\hbar,u)}=Z^{(\bar{\alpha})}(M;\bar{\hbar},\bar{u})$. The latter partition function is actually in the antiholomorphic sector of the Chern-Simons theory, but we can just rename $(\bar{\hbar},\bar{u})\mapsto (\hbar,u)$ (and use analyticity) to obtain a perturbative partition function for the conjugate branch in the holomorphic sector,

$$Z^{(\bar{\alpha})}(M;\hbar,u) = \overline{Z^{(\alpha)}}(M;\hbar,u)\,. \label{C-sym}$$

Here, for any function $f(z)$ we define $\bar{f}(z):=\overline{f(\bar{z})}$. In particular, if $f$ is analytic, $f(z)=\sum f_n z^n$, then $\bar{f}$ denotes a similar function with conjugate coefficients, $\bar{f}(z)=\sum \bar{f}_n z^n$.

In the case $r=1$, the symmetry [\[C-sym\]](#C-sym){reference-type="eqref" reference="C-sym"} implies that branches of the classical $SL(2,{\mathbb{C}})$ A-polynomial come in conjugate pairs $v_\alpha$ and $v_{\bar{\alpha}}(u)=\overline{v_\alpha}(u)$. Again, these pairs arise algebraically because the A-polynomial has integer coefficients. (See *e.g.* [@cooper-1994; @cooper-1996] for a detailed discussion of properties of $A(l,m)$.) Some branches, like the abelian branch, may be self-conjugate. For the abelian branch, this is consistent with $S_0^{(abel)}=0$. The geometric branch, on the other hand, has a distinct conjugate because ${\mbox{Vol\,}}(M;0)>0$ ; from [\[S0_volume\]](#S0_volume){reference-type="eqref" reference="S0_volume"} we see that its leading perturbative coefficient obeys

$$S_0^{({\rm conj})}(u)
= \frac{i}{2}\Big[ - {\mbox{Vol\,}}(M;\bar{u}) + i {\rm CS} (M;\bar{u}) \Big]
+\overline{v_{{\rm geom}}} (u) {\rm Re}\,(u) - i\pi u\,.
\label{S0_conj}$$

In general, we have

$$S_0^{(\bar{\alpha})}(u) = \overline{S_0^{(\alpha)}}(u)
\qquad (\mbox{mod}\;2\pi u)\,.$$

Now, let us consider symmetries that originate from geometry, *i.e.* symmetries that involve involutions of $M$, $$\tau : \quad M \to M\,.$$ Every such involution restricts to a self-map of $\Sigma = \partial M$, $$\tau \vert_{\Sigma} : \quad \Sigma \to \Sigma\,,$$ which, in turn, induces an endomorphism on homology, $H_i (\Sigma)$. Specifically, let us consider an orientation-preserving involution $\tau$ which induces an endomorphism $(-1,-1)$ on $H_1 (\Sigma) \cong {\mathbb{Z}}\times {\mathbb{Z}}$. This involution is a homeomorphism of $M$; it changes our definition of the holonomies, $$m_i \to \frac{1}{m_i}
\qquad {\rm and} \qquad
l_i \to \frac{1}{l_i}\,,
\label{lmrefl}$$ leaving the symplectic form [\[sympluv\]](#sympluv){reference-type="eqref" reference="sympluv"} invariant. Therefore, it preserves both the symplectic phase space ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}}, \Sigma)$ and the Lagrangian submanifold ${\cal L}$ (possibly permuting some of its branches).

In the basic case of rank $r=1$, the symmetry [\[lmrefl\]](#lmrefl){reference-type="eqref" reference="lmrefl"} corresponds to the simple, well-known relation $A(l^{-1},m^{-1})=A(l,m)$, up to overall powers of $l$ and $m$. Similarly, at the quantum level, $\widehat{A}(\hat{l}^{-1},\hat{m}^{-1}) = \widehat{A}(\hat{l},\hat{m})$ when $\widehat{A}(\hat{l},\hat{m})$ is properly normalized. Branches of the A-polynomial are individually preserved, implying that the perturbative partition functions (and the coefficients $S_n^{(\alpha)}$) are all *even*:

$$Z^{(\alpha)}(M;\hbar,-u) = Z^{(\alpha)}(M;\hbar,u)\,, \label{even}$$

modulo factors of $e^{2\pi u/\hbar}$ that are related to the ambiguity in $S_0^{(\alpha)}(u)$. Note that in the $r=1$ case one can also think of the symmetry [\[lmrefl\]](#lmrefl){reference-type="eqref" reference="lmrefl"} as the Weyl reflection. Since, by definition, holonomies that differ by an element of the Weyl group define the same point in the moduli space [\[mflatttwo\]](#mflatttwo){reference-type="eqref" reference="mflatttwo"}, it is clear that both ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$ and ${\cal L}$ are manifestly invariant under this symmetry. (For $r>1$, Weyl transformations on the variables $l$ and $m$ lead to new, independent relations among the branches of $\cal L$.)

Finally, let us consider a more interesting "parity" symmetry, an orientation-reversing involution $$P : \quad M \to \overline{M}$$ $$P \vert_{\Sigma} : \quad \Sigma \to \overline{\Sigma}$$ that induces a map $(1,-1)$ on $H_1 (\Sigma) \cong {\mathbb{Z}}\times {\mathbb{Z}}$. This operation by itself cannot be a symmetry of the theory because it does not preserve the symplectic form [\[sympluv\]](#sympluv){reference-type="eqref" reference="sympluv"}. We can try, however, to combine it with the transformation $\hbar \to - \hbar$ to get a symmetry of the symplectic phase space $({{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}}, \Sigma), \omega)$. We are still not done because this combined operation changes the orientation of both $\Sigma$ and $M$, and unless $\overline{M} \cong M$ the state $\vert M \rangle$ assigned to $M$ will be mapped to a different state $\vert \overline{M} \rangle$. But if $M$ is an amphicheiral[^2] manifold, then both $m_i \to \frac{1}{m_i}$ and $l_i \to \frac{1}{l_i}$ (independently) become symmetries of the theory, once combined with $\hbar \to - \hbar$. This now implies that solutions come in signed pairs, $v_{\alpha} (u)$ and $v_{\hat{\alpha}} (u) = -v_{\alpha} (u)$, such that the corresponding perturbative $G_{{\mathbb{C}}}$ invariants satisfy $$Z^{(\hat{\alpha})} (M;\hbar,u) = Z^{(\alpha)} (M;-\hbar,u)\,.$$ For the perturbative coefficients, this leads to the relations $$\begin{aligned}
S_0^{(\hat{\alpha})}(u) & = -S_0^{(\alpha)}(u) \qquad\quad (\mbox{mod}\;2\pi u)\,, \label{sym_sign} \\
S_n^{(\hat{\alpha})}(u) & = (-1)^{n+1} S_n^{(\alpha)}(u) \qquad n\ge 1\,.
\label{sym_signsn}
\end{aligned}$$

Assuming that the $\sim \pm\frac{i}{2} {\mbox{Vol\,}}(M;u)$ behavior of the geometric and conjugate branches is unique, their signed and conjugate pairs must coincide for amphicheiral 3-manifolds. $S_0^{(\rm geom)}$, then, is an even analytic function of $u$ with strictly real series coefficients; at $u \in i {\mathbb{R}}$, the Chern-Simons invariant ${\rm CS} (M;u)$ will vanish.

[^1]: More explicitly, letting $I_{CS}(\hbar,{\cal A}) = -\frac{1}{4\hbar}\int_M {\rm Tr}\big({\cal A}\wedge{\cal A}+\frac{2}{3}{\cal A}\wedge{\cal A}\wedge{\cal A}\big)$, we have $$\overline{Z^{\alpha}(M;\hbar,u)} 
    = \left(\int_{(u,\alpha)}{\cal D}{\cal A}\,e^{I_{CS}(\hbar,{\cal A})}\right)^* 
    = \int_{(\bar{u},\bar{\alpha})} {\cal D}\bar{{\cal A}}\,e^{I_{CS}(\bar{\hbar},\bar{{\cal A}})}
    = Z^{(\bar{\alpha})}(M;\bar{\hbar},\bar{u})\,.\notag$$

[^2]: A manifold is called chiral or amphicheiral according to whether the orientation cannot or can be reversed by a self-map.
