---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-012-the-hadron-spectrum
section_title: "The hadron spectrum"
section_number: null
pages: 17-19
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.924
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsec_hs label="subsec_hs"} We saw in Section [\[subsubsec_agsl\]](#subsubsec_agsl){reference-type="ref" reference="subsubsec_agsl"} that the QCD Lagrangian possesses an $\mbox{SU(3)}_L\times\mbox{SU(3)}_R\times \mbox{U(1)}_V$ symmetry in the chiral limit in which the light quark masses vanish. From symmetry considerations involving the Hamiltonian $H^0_{\rm QCD}$ only, one would naively expect that hadrons organize themselves into approximately degenerate multiplets fitting the dimensionalities of irreducible representations of the group $\mbox{SU(3)}_L\times\mbox{SU(3)}_R\times\mbox{U(1)}_V$. The $\mbox{U(1)}_V$ symmetry results in baryon number conservation and leads to a classification of hadrons into mesons ($B=0$) and baryons ($B=1$). The linear combinations $Q_{aV}=Q_{aR}+Q_{aL}$ and $Q_{aA}=Q_{aR}-Q_{aL}$ of the left- and right-handed charge operators commute with $H^0_{\rm QCD}$, have opposite parity, and thus for states of positive parity one would expect the existence of degenerate states of negative parity (parity doubling) which can be seen as follows.

Let $|\alpha,+\rangle$ denote an eigenstate of $H^0_{\rm QCD}$ and parity with eigenvalues $E_\alpha$ and $+1$, respectively, $$\begin{aligned}
H^0_{\rm QCD}|\alpha,+\rangle&=&E_\alpha|\alpha,+\rangle,\\
P|\alpha,+\rangle&=&|\alpha,+\rangle,
\end{aligned}$$ such as, e.g., a member of the ground-state baryon octet (in the chiral limit). Defining $|\phi_{a\alpha}\rangle= Q_{aA}|\alpha,+\rangle$, because of $[H^0_{\rm QCD},Q_{aA}]=0$, we have $$\begin{aligned}
H^0_{\rm QCD}|\phi_{a\alpha}\rangle
&=&H^0_{\rm QCD} Q_{aA}|\alpha,+\rangle
= Q_{aA} H^0_{\rm QCD}|\alpha,+\rangle
= E_\alpha Q_{aA}|\alpha,+\rangle
= E_\alpha |\phi_{a\alpha}\rangle,\\
P|\phi_{a\alpha}\rangle&=& PQ_{aA} P^{-1} P|\alpha,+\rangle=-Q_{aA}(+|\alpha,+\rangle)
=-|\phi_{a\alpha}\rangle.
\end{aligned}$$ The state $|\phi_{a\alpha}\rangle$ can be expanded in terms of the members of a multiplet with negative parity, $$|\phi_{a\alpha}\rangle=Q_{aA}|\alpha,+\rangle=|\beta,-\rangle\langle\beta,-|
Q_{aA}|\alpha,+\rangle={t_a}_{\beta\alpha}|\beta,-\rangle.$$ However, the low-energy spectrum of baryons does not contain a degenerate baryon octet of negative parity. Naturally the question arises whether the above chain of arguments is incomplete. Indeed, we have tacitly assumed that the ground state of QCD is annihilated by the generators $Q_{aA}$. Let $b^\dagger_{\alpha+}$ denote an operator creating quanta with the quantum numbers of the state $|\alpha,+\rangle$. Similarly, let $b^\dagger_{\alpha-}$ create degenerate quanta of opposite parity. Expanding $$[Q_{aA},b^\dagger_{\alpha+}]= b^\dagger_{\beta-}{t_a}_{\beta\alpha},$$ the usual chain of arguments then works as $$\begin{aligned}
\label{2:2:2:pardoub}
Q_{aA}|\alpha,+\rangle=Q_{aA} b^\dagger_{\alpha+}|0\rangle
=\Big([Q_{aA},b^\dagger_{\alpha+}]+b_{\alpha+}^\dagger
\underbrace{Q_{aA}}_{
\mbox{$\hookrightarrow 0$}}\Big)|0\rangle
= {t_a}_{\beta\alpha} b_{\beta-}^\dagger |0\rangle.
\end{aligned}$$ However, if the ground state is *not* annihilated by $Q_{aA}$, the reasoning of Eq. ([\[2:2:2:pardoub\]](#2:2:2:pardoub){reference-type="ref" reference="2:2:2:pardoub"}) does no longer apply. In that case the ground state is not invariant under the full symmetry group of the Lagrangian resulting in a spontaneous symmetry breaking. In other words, the non-existence of degenerate multiplets of opposite parity points to the fact that $\mbox{SU(3)}_V$ instead of $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ is approximately realized as a symmetry of the hadrons. Furthermore, the octet of the pseudoscalar mesons is special in the sense that the masses of its members are small in comparison with the corresponding $1^-$ vector mesons. They are the candidates for the Goldstone bosons of a spontaneous symmetry breaking.

According to the Coleman theorem [@Coleman:1966:1:1], the symmetry of the ground state determines the symmetry of the spectrum, i.e. $$Q_{aV}|0\rangle =Q_V|0\rangle =0$$ implies $\mbox{SU(3)}_V$ multiplets which can be classified according to their baryon number. In the reverse conclusion, the symmetry of the ground state can be inferred from the symmetry of the spectrum. Figures [1](#2:2:2:fig:meson_octet){reference-type="ref" reference="2:2:2:fig:meson_octet"} and [2](#2:2:2:fig:baryon_octet){reference-type="ref" reference="2:2:2:fig:baryon_octet"} show the octets of the lowest-lying pseudoscalar-meson states and the lowest-lying baryon states of spin-parity $\frac{1}{2}^+$, respectively.

<figure id="2:2:2:fig:meson_octet">
<div class="center">
<div class="picture">
<p>(10,6) (0,0)<span>(1,0)<span>10</span></span> (10,-1)<span><span class="math inline"><em>I</em><sub>3</sub></span></span> (0,0)<span>(0,1)<span>6</span></span> (-1,6)<span><span class="math inline"><em>S</em></span></span> (3,1) (2.5,0.5)<span><span class="math inline"><em>K</em><sup>−</sup>(494)</span></span> (7,1) (6.5,0.5)<span><span class="math inline"><em>K̄</em><sup>0</sup>(498)</span></span> (1,3) (0.5,3.5)<span><span class="math inline"><em>π</em><sup>−</sup>(140)</span></span> (5,3) (5,3) (4.5,3.5)<span><span class="math inline"><em>π</em><sup>0</sup>(135)</span></span> (4.5,2)<span><span class="math inline"><em>η</em>(549)</span></span> (9,3) (8.5,3.5)<span><span class="math inline"><em>π</em><sup>+</sup>(140)</span></span> (3,5) (2.5,4.5)<span><span class="math inline"><em>K</em><sup>0</sup>(498)</span></span> (7,5) (6.5,4.5)<span><span class="math inline"><em>K</em><sup>+</sup>(494)</span></span> (0,1) (-0.5,1)<span>-1</span> (0,3) (-0.5,3)<span>0</span> (0,5) (-0.5,5)<span>1</span> (1,0) (1,-0.5)<span>-1</span> (3,0) (3,-0.5)<span>-1/2</span> (5,0) (5,-0.5)<span>0</span> (7,0) (7,-0.5)<span>1/2</span> (9,0) (9,-0.5)<span>1</span></p>
</div>
</div>
<figcaption><span id="2:2:2:fig:meson_octet" label="2:2:2:fig:meson_octet"></span> Pseudoscalar meson octet in an <span class="math inline">(<em>I</em><sub>3</sub>,<em>S</em>)</span> diagram. Baryon number <span class="math inline"><em>B</em> = 0</span>. Masses in MeV.</figcaption>
</figure>

<figure id="2:2:2:fig:baryon_octet">
<div class="center">
<div class="picture">
<p>(10,6) (0,0)<span>(1,0)<span>10</span></span> (10,-1)<span><span class="math inline"><em>I</em><sub>3</sub></span></span> (0,0)<span>(0,1)<span>6</span></span> (-1,6)<span><span class="math inline"><em>S</em></span></span> (3,1) (2.5,0.5)<span><span class="math inline"><em>n</em>(940)</span></span> (7,1) (6.5,0.5)<span><span class="math inline"><em>p</em>(938)</span></span> (1,3) (0.5,3.5)<span><span class="math inline"><em>Σ</em><sup>−</sup>(1197)</span></span> (5,3) (5,3) (4.5,3.5)<span><span class="math inline"><em>Σ</em><sup>0</sup>(1193)</span></span> (4.5,2)<span><span class="math inline"><em>Λ</em>(1116)</span></span> (9,3) (8.5,3.5)<span><span class="math inline"><em>Σ</em><sup>+</sup>(1189)</span></span> (3,5) (2.5,4.5)<span><span class="math inline"><em>Ξ</em><sup>−</sup>(1321)</span></span> (7,5) (6.5,4.5)<span><span class="math inline"><em>Ξ</em><sup>0</sup>(1315)</span></span> (0,1) (-0.5,1)<span>0</span> (0,3) (-0.5,3)<span>-1</span> (0,5) (-0.5,5)<span>-2</span> (1,0) (1,-0.5)<span>-1</span> (3,0) (3,-0.5)<span>-1/2</span> (5,0) (5,-0.5)<span>0</span> (7,0) (7,-0.5)<span>1/2</span> (9,0) (9,-0.5)<span>1</span></p>
</div>
</div>
<figcaption><span id="2:2:2:fig:baryon_octet" label="2:2:2:fig:baryon_octet"></span> Baryon octet (<span class="math inline">$J=\frac{1}{2}$</span>) in an <span class="math inline">(<em>I</em><sub>3</sub>,<em>S</em>)</span> diagram. Masses in MeV. Baryon number <span class="math inline"><em>B</em> = 1</span>.</figcaption>
</figure>

The axial charges satisfy the commutation relations $$\begin{aligned}
\label{2:2:2:crqaa}
[Q_{aA},Q_{bA}]&=&if_{abc}Q_{cV},\\
\label{2:2:2:crqva}
{[Q_{aV},Q_{bA}]}&=&if_{abc}Q_{cA}.
\end{aligned}$$ Since the parity doubling is not observed for the low-lying states, one assumes that the $Q_{aA}$ do *not* annihilate the ground state, $$\label{2:2:2:qav}
Q_{aA}|0\rangle\neq 0,$$ i.e., the ground state of QCD is not invariant under "axial" transformations. In the present case, $G=\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ with $n_G=16$ and $H=\mbox{SU(3)}_V$ with $n_H=8$ and we expect eight Goldstone bosons. According to the Goldstone theorem [@Goldstone:eq:1:1], [@Goldstone:es:1:1], to each axial generator $Q_{aA}$, which does not annihilate the ground state, corresponds a massless Goldstone boson field $\phi_a(x)$ with spin 0, whose symmetry properties are tightly connected to the generator in question. The Goldstone bosons have the same transformation behavior under parity, $$\label{2:2:2:parityphi}
\phi_a(t,\vec{x})\stackrel{P}{\mapsto}-\phi_a(t,-\vec{x}),$$ i.e., they are pseudoscalars, and transform under the subgroup $H=\mbox{SU(3)}_V$, which leaves the vacuum invariant, as an octet \[see Eq. ([\[2:2:2:crqva\]](#2:2:2:crqva){reference-type="ref" reference="2:2:2:crqva"})\]: $$\label{2:2:2:transformationphiqv}
[Q_{aV},\phi_b(x)]=if_{abc}\phi_c(x).$$
