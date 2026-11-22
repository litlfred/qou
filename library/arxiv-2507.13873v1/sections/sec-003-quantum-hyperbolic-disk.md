---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography"
section_id: sec-003-quantum-hyperbolic-disk
section_title: "Quantum hyperbolic disk"
section_number: null
pages: 9-11
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 1.0
doc_brief: "Probing the singularity at the holographic screen via q-holography — We study the emergence of q-deformed spacetime in a lower-dimensional gravitational system whose asymptotic region geometrizes the"
---
We have up to this point only discussed the boundary quantum algebra action on boundary correlation functions. Here we show how this almost uniquely fixes the non-commutative geometrical features of the induced bulk region if this is to be the boundary theory. This roughly reverses the arguments of [@Berkooz:2022mfk; @Almheiri:2024ayc]. To match with conventional notation for quantum groups, we change the notation from the previous subsection into: $$q^{2L_0} \to K, \qquad  L_{+1} \to E^+, \qquad  L_{-1} \to E^-.$$

We introduce a new antiholomorphic coordinate $z^*$, and if we demand that the boundary is at the locus $zz^*=1$, we can deduce the full bulk structure as follows. Firstly, from compatibility of the coproduct $$\begin{gathered}
    \Delta(K) = K \otimes K, \quad \Delta(E^+) = \mathbf{1} \otimes E^+ + E^+ \otimes K^{-1}, \quad
    \Delta(E^-) =  K \otimes E^- + E^- \otimes \mathbf{1},
\end{gathered}$$ with this boundary condition, we can obtain the action of the generators on both bulk coordinates $z$ and $z^*$. The specific generators which generate quantum Möbius transformations on the coordinate $z$ can be found by looking at the spin-0 corepresentation [\[eq:corep\]](#eq:corep){reference-type="eqref" reference="eq:corep"}. The associated generators are then given by the induction procedure in Appendix [\[app:cft\]](#app:cft){reference-type="ref" reference="app:cft"}, which act on holomorphic monomials as $$\begin{aligned}
K f(z) &= f(q^2z), \\
E^- f(z) &= \frac{q^{-1/2}}{z}\frac{f(q^{2}z)-f(z)}{q-q^{-1}}, \\
E^+ f(z) &= -q^{-1/2}z \frac{f(q^{-2}z)-f(z)}{q-q^{-1}},
\end{aligned}$$ We now treat $z^*$ on the same footing as $z$, and apply these transformations on the boundary constraint $zz^*=1$ directly. This yields e.g. $$K(z \otimes z^*) \equiv K(z)K(z^*)=1,$$ where we used the grouplike coproduct structure $\Delta(K)=K\otimes K$ and $K(c) = 1$ for constants. This fixes then $K (z^*)$ which by holomorphicity holds everywhere in the bulk. This allows us to bootstrap the action of $K,E^+$ and $E^-$ on arbitrary monomials $f(z^*)$.[^1] We obtain $$\begin{aligned}
\label{eq:staractions}
K f(z^*) &= f(q^{-2} z^*), \\
E^- f(z^*) &= q^{-1/2}z^* \frac{f(q^{-2}z^*)-f(z^*)}{q-q^{-1}}, \\
\label{eq:staractions2}
E^+ f(z^*) &= -\frac{q^{-1/2}}{z^*} \frac{f(q^{2}z^*)-f(z^*)}{q-q^{-1}}.
\end{aligned}$$ These three relations, together with the previous ones acting on $z$, implement the action of the quantum group transformations on the two bulk coordinates $z$ and $z^*$. Secondly, ansatzing a non-commutativity relation $z^*z = Azz^* + B$ for $c$-numbers $A$ and $B$, and working out e.g. $E^-(z^*z) = E^-(Azz^*+ B)$ via the coproduct immediately fixes $A$ and $B$ as: $$\label{eq:noncom}
 z^*z = q^2 zz^* + 1-q^2.$$ This means that $z^*z=1=zz^*$ describes the boundary, where hence these two coordinates commute. To sum up, the boundary U$_q(\mathfrak{sl}(2,\mathbb{R}))$ quantum algebra symmetry, implies the bulk *needs* to have non-commutative coordinates [\[eq:noncom\]](#eq:noncom){reference-type="eqref" reference="eq:noncom"} to be compatible.

These two coordinates can be conveniently written by introducing a radial coordinate $y=1-zz^*$ [@Almheiri:2024ayc], with non-commutativity: $$zy=q^{-2}yz, \qquad z^*y=q^{2}yz^*.$$ The $y$-coordinate classically ranges between 1 (the origin), and 0 (the boundary). Finally introducing new coordinates as $y=e^{-r}$ (where $r$ classically ranges from 0 (the origin) and $+\infty$ (the boundary), and $z^{*^{-1}}z=e^{2i\varphi}$, we obtain $$= -2i \log q .$$ If we would have taken $0<q<1$, this would be a standard noncommutativity relation, telling us that spacetime is fundamentally fuzzy with elementary (Planckian) cell size of $2 \abs{\log q}$ (see Fig. [1](#FigQHD){reference-type="ref" reference="FigQHD"}).[^2]

![Quantum hyperbolic disk with fuzzy cells of size $2\abs{\log q}$ in $(r,\varphi)$ coordinates where $r \in [0,+\infty[$ and $\varphi\in [0,2\pi[$ where the cell sizes are uniform.](FigQHD.pdf){#FigQHD width="0.27\\linewidth"}

In the following, we will instead have $q$ on the unit circle, and the above fuzzyness is still there, but furthermore complexified.

Just as JT gravity provides an explicit realization of $\mathrm{AdS}_2$ spacetime within a quantum gravity model, can we similarly embed the quantum hyperbolic disk into a fully dynamical bulk gravitational system?

[^1]: We find $K(z^*)=q^{-2}z^*$, $E^+(z^*)=-q^{1/2}$ and $E^-(z^*)=-q^{-3/2}{z^*}^2$. By successively using the coproduct to find the action on $z^{*^n}$, one deduces ([\[eq:staractions\]](#eq:staractions){reference-type="ref" reference="eq:staractions"}) - [\[eq:staractions2\]](#eq:staractions2){reference-type="eqref" reference="eq:staractions2"}.

[^2]: The coordinate $\varphi$ is periodic with period $2\pi$, which implies the conjugate variable $r/2\abs{\log q}$ is discretized $\in \mathbb{N}$. This is identical to the DSSYK discrete chord number.
