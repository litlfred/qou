---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-002-21-a-quantum-black-hole-from-the-outside
section_title: "A Quantum Black Hole from the Outside"
section_number: 2.1
pages: 9-11
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.992
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
We'll first discuss Charlie's description, which is based on the following three postulates:

-   According to Charlie, the formation and evaporation of the black hole is a unitary process. Moreover, in addition to an asymptotic S-matrix, we can also think about either continuous or discrete time evolution in which at any given time there is a pure quantum state $|\Psi\rangle$ in some Hilbert space $\mathcal{H}_{outside}$.

-   At any given time in this unitary evolution we can factorize $\mathcal{H}_{outside}$ into subfactors with simple semiclassical interpretations: $$\label{outfactor}
    \mathcal{H}_{outside}=\mathcal{H}_H\otimes \mathcal{H}_B\otimes \mathcal{H}_R.$$ Here $\mathcal{H}_R$ are the modes of the radiation field outside of the the black hole, roughly with Schwarzschild coordinate radius $r>3GM$. $\mathcal{H}_B$ are the field theory modes in the near-horizon region, roughly with support over $2GM+\epsilon<r<3GM$ where $\epsilon$ is some UV cutoff. The geometry in this region is close to Rindler space. $\mathcal{H}_H$ are the remaining degrees of freedom in the black hole, which we can heuristically think of as being at the stretched horizon at $r=2GM+\epsilon$. Clearly the distinctions between these subfactors are somewhat arbitrary. In particular, it will be convenient to restrict the modes in $\mathcal{H}_B$ to have Schwarzschild energy less than the black hole temperature $T=\frac{1}{4\pi G M}$. Those with higher energy are not really confined to the near-horizon region and we will include them as part of $\mathcal{H}_R$. The time evolution of $|\Psi\rangle$ does not respect this factorization and cannot be computed using low energy field theory, but for our purposes it is enough to consider the state at a given time.

-   If $|H|$ and $|B|$ are the dimensionalities of $\mathcal{H}_H$ and $\mathcal{H}_B$ respectively, then $\log|H|$ and $\log|B|$ are both proportional to the area of the black hole horizon in Planck units at the time at which we study $|\Psi\rangle$. Thus their size decreases with time. Naively $\mathcal{H}_R$ is infinite dimensional since all sorts of things could be going on far from the black hole, but we will restrict its definition to only run over the subfactor which in $|\Psi\rangle$ is nontrivially involved in the black hole dynamics. Thus the size of $\mathcal{H}_R$ grows with time.

The third assumption leads to an interesting distinction between "young" and "old" black holes [@HaydenPreskill], with the separation based on whether $|R|$ is bigger or smaller than $|H||B|$. When the black hole is young, $|R|$ is quite small and $B$ and $H$ are entangled significantly. As the black hole becomes old however, $|R|$ becomes large and $B$ and $H$ taken together become a small subsystem of the full Hilbert space $\mathcal{H}_{outside}$. Page's theorem [@pagethm] then suggests that the combined system $BH$ has a density operator which is close to being proportional to the identity operator:[^1]

$$\label{rhoBH}
\rho_{BH}\approx \frac{1}{|B||H|}I_B\otimes I_H.$$ The time beyond which this is true has come to be called the Page time. More carefully we would expect a thermal distribution in the Schwarzschild energy at the usual temperature $T=\frac{1}{4\pi G M}$, but since we have put high-frequency modes in $\mathcal{H}_R$ the thermal density matrix for $\mathcal{H}_H\otimes\mathcal{H}_B$ is quite close to [\[rhoBH\]](#rhoBH){reference-type="eqref" reference="rhoBH"}.[^2]

We can describe the state concisely by saying that $BH$ is maximally entangled with a subspace in $R$. More precisely, there is a $|\Psi\rangle$-dependent decomposition of $\mathcal{H}_R$ $$\mathcal{H}_R=\left(\mathcal{H}_{R_H}\otimes\mathcal{H}_{R_B}\right)\oplus \mathcal{H}_{other},$$ with $|R_H|=|H|$ and $|R_B|=|B|$, such that we can write the state of the full system, to a good approximation, as[^3] $$\label{Psi}
|\Psi\rangle=\left(\frac{1}{\sqrt{|H|}}\sum_h|h\rangle_H |h\rangle_{R_H}\right)\otimes \left(\frac{1}{\sqrt{|B|}}\sum_b|b\rangle_B |b\rangle_{R_B}\right).$$ Here $h$ and $b$ label orthonormal bases for $\mathcal{H}_H$ and $\mathcal{H}_B$ respectively, and we have chosen convenient complementary bases for $\mathcal{H}_{R_H}$ and $\mathcal{H}_{R_B}$. $R_H$ and $R_B$ are called the *purifications* of $H$ and $B$ respectively. The state has zero projection onto $\mathcal{H}_{other}$.

This form of $|\Psi\rangle$ makes it clear that any measurement done on $B$ is perfectly correlated with some other measurement done on $R_B$. This consequence of the entanglement was emphasized in [@Almheiri:2012rt]; in their language measurements done on $R_B$ project onto particular states in the basis $|b\rangle_B$. We hope that it is clear however that the presence of this entanglement does not *require* any such measurement to be done; once we accept the three assumptions the entanglement follows directly. Indeed we would argue that Charlie's ability to measure $R_B$ provides justification for accepting the Hilbert space structure of the model.[^4]

[^1]: Page's theorem says that in a Hilbert space which can be factorized into $\mathcal{H}_A\otimes \mathcal{H}_B$, with $|A|\leq|B|$, a typical pure state has $S_A=\log|A|-\frac{|A|}{2|B|}+O\left(\frac{1}{|A|}\right)$.

[^2]: It is important in what follows that these "low-energy" modes can have quite high proper energy near the horizon, so they are relevant to the experience of an observer who is near the horizon even though the Schwarzschild temperature is typically very small compared to any scale relevant to that observer.

[^3]: This representation of the state is called the Schmidt decomposition.

[^4]: Remember Charlie stays outside the black hole and has an arbitrarily large amount of time and resources, so there seems to be no limit on his experimental ability. This will be different for Alice, whom we discuss now.
