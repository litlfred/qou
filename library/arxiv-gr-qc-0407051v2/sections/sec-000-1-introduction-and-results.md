---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from quantum geometry"
section_id: sec-000-1-introduction-and-results
section_title: "Introduction and results"
section_number: 1
pages: 2-4
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 1.0
doc_brief: "Black hole entropy from quantum geometry — Quantum Geometry (the modern Loop Quantum Gravity using graphs and spin-networks instead of the loops) provides microscopic degrees of freedom that account"
---
Quantum Geometry [@thiembook; @rovbook; @alrev] provides microscopic degrees of freedom that account for the black-hole entropy. The issue was raised in works by Krasnov [@krasentropy] and Rovelli [@roventropy]. The final quantum Isolated Horizon framework was introduced by Ashtekar, Baez, Corichi and Krasnov [@abk]. The framework describes a black-hole in equilibrium surrounded by a quite arbitrary space-time. In the canonical formulation of the theory, the classical phase space is restricted to the set of space-times containing a black-hole of a fixed area $a$. After quantization, the kinematic Hilbert space is the tensor product of the horizon Hilbert space ${\cal H}_{S}$ and the bulk Hilbert space ${\cal H}_{\Sigma}$. Elements of ${\cal H}_{S}$ are identified with the black-hole kinematic quantum states. They represent quantum excitations of the $U(1)$ spin connection defined on the horizon. Mathematically, they are described by the quantum Chern-Simons theories on a punctured sphere, where all possible sets of punctures are admitted. Therefore, they are labeled by certain sequences of numbers (referred to as spins) assigned to the punctures. The bulk states, that is elements of ${\cal H}_{\Sigma}$, on the other hand, are described by Quantum Geometry, and define the quantum area of the horizon [@rsarea; @alarea]. The quantum constraints commute with the quantum horizon area operator. Most importantly, all the solutions whose quantum areas fall into any given finite interval $[a -\delta a, a +\delta a]$ can be labeled by a finite number of the black-hole states (and by other labels corresponding to the bulk states). That number defines the Ashtekar-Baez-Corichi-Krasnov black-hole entropy. However, the procedure introduced in [@abk] for state counting contains a spurious constraint on admissible sequences of the labels, and the number of the relevant horizon states is underestimated. The goal of our work[^1] is to point out this error, to formulate a correct counting procedure, and to study the consequences. Several conclusions of [@abk] have to be re-examined:

-   the statement that the leading contribution to the entropy comes entirely from the simplest states (characterized by punctures with labels $\pm 1/2$),

-   the confirmation of the Bekenstein and Hawking formula [@bekhaw],

-   the determination of the value of the free parameter $\gamma$ introduced in Quantum Geometry by Barbero and Immirzi, as $$\gamma_{\rm ABCK} = \frac{\ln 2}{\pi\sqrt{3}}.\label{gammaabk}$$

The Barbero-Immirzi parameter labeles different sectors of Quantum Geometry. The spectra of all the geometric and physical operators depend on $\gamma$. For example the quantized area is proportional to $\gamma$.

Therefore, in our paper we go back to the issue of calculating the entropy within the Quantum Geometry and the Ashtekar-Baez-Corichi-Krasnov framework. We formulate an exact combinatoric problem whose solution is the entropy: we carefully define a set of sequences freely labeling the black-hole quantum states which correspond to eigenvalues of the quantum area operator equal or less than $a$. The entropy is $\ln N(a)$, where $N(a)$ is the number of elements of this set. Next, we address the issue of the proportionality of the entropy to the area. We consider the ratio $$\frac{\ln N(a)}{a}$$ which is expected to be constant in the limit as $a\rightarrow \infty$. We find that for large $a$, $$\frac{\ln 2}{4\pi\gamma{\ell}_{\rm Pl}^2}\, a\
\le\ \ln N(a) \le\ \frac{\ln 3}{4\pi\gamma{\ell}_{\rm Pl}^2}\, a\, . \label{entropyest}$$ As before (in [@abk]), the Barbero-Immirzi parameter $\gamma$ can be fixed by assuming the agreement with the Bekenstein-Hawking entropy (the proportionality of the entropy to the area in the leading order is not proved yet, at this point, but see below). Then, ([\[entropyest\]](#entropyest){reference-type="ref" reference="entropyest"}) provides lower and upper bounds for $\gamma$, $$\frac{\ln 2}{\pi} \le \gamma \le \frac{\ln 3}{\pi}\label{gammaineq}.$$ These results lead to a revision of the literature of the subject.

To begin with, they show that the number of states characterized by the lowest spin labels is essentially smaller than the number of all the states contributing to a given value of the horizon area. Therefore, the horizon states labeled by higher spins do contribute to the leading term of the entropy. In the consequence, the ABCK model of quantum black hole does not agree with Wheeler's heuristic model 'It from bit'. The (contradicted here) conclusion $(i)$ listed above, had been used in [@Dre] to point out a remarkable relation between the black hole quasi-normal modes, the Bekenshtein-Hawking entropy and the ABCK entropy provided the minimal spin of the quantum excitations of the horizon is $1$ rather then $1/2$. In view of our correction, the meaning of that observation of [@Dre] should be understood again.

Next, the conclusion $(iii)$ listed above is not true: the value of the parameter $\gamma$ can not be that of ([\[gammaabk\]](#gammaabk){reference-type="ref" reference="gammaabk"}).

We were not able to verify the proportionality of the horizon entropy to the area ourselves. However, our combinatoric formulation of the problem of calculating the entropy derived in this paper has been later solved in an exact way in the accompanying paper [@meis]. The number $\ln N(a)$ has been calculated rigorously therein, and the result is $$\ln N(a)\ =\ \frac{\gamma_{\rm M}}{\gamma}\frac{a}{4{\ell}_{\rm Pl}^2} - \frac{1}{2}\ln a
+  O(1)$$ in the limit of large horizon area $a$, where the value of the parameter $\gamma_{\rm M}$ can be calculated at arbitrary accuracy. In conclusion, taking into account the results of [@meis], the proportionality of the entropy to the area in the leading order for large $a$ is confirmed, and even the sub-leading terms are calculated.

In the last section we derive the probability distribution of the spin at a given puncture. The physical meaning of these new results will be discussed in a joint paper [@adlm].

[^1]: This project was a part of the diploma thesis of one of the authors [@pinek].
