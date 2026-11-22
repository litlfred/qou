---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-032-72-su3u1-and-lorentz-invariant-pairing
section_title: "SU(3)U(1) and Lorentz invariant pairing"
section_number: 7.2
pages: 23-23
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
We now select among the 364 terms in ([\[364-rep\]](#364-rep){reference-type="ref" reference="364-rep"}) those that are ${\rm SU}(3)$, ${\rm U}(1)_{EM}$ and Lorentz invariant.

We have the ${\rm SU}(3)$ invariant 3-forms in ${\mathbb R}^6\subset{\rm Im}({\mathbb O})$. These arise as the real and imaginary parts of an ${\rm SU}(3)$ invariant $(3,0)$ form $$\begin{aligned}
\Omega := ( e^1 - {\rm i\,}e^5)(e^2-{\rm i\,}e^6) (e^3-{\rm i\,}e^7).
\end{aligned}$$ Note, however, that $\Omega$ is a singlet with respect to ${\rm SU}(2)_L\times{\rm SU}(2)_R$, but transforms non-trivially under the ${\rm U}(1)_{B-L}$. This means that $\Omega$ is not a singlet with respect to ${\rm U}(1)_{EM}$, and cannot be used. There is then an ${\rm SU}(3)\times{\rm U}(1)_{B-L}$ invariant real 2-form $$\begin{aligned}
\omega = e^{15} + e^{26}+e^{37}.
\end{aligned}$$ The last building block we are allowed to use in the ${\mathbb R}^7$ factor is the 1-form $e^4$.

For objects in ${\rm Im}(\tilde{{\mathbb O}})$, we are only allowed to use the 1-, 2- and 3-forms built from $\tilde{e}^{1,2,3}$. These 1- and 2-forms transform as vectors under the weak ${\rm SU}(2)$, while the 3-form is invariant. We can use objects that transform non-trivially under the ${\rm SU}(2)$ because we do not intend to preserve this symmetry. In other words, objects that transform non-trivially under the ${\rm SU}(2)$ are components of a \"Higgs\" field that we know is present in the mass terms of the SM.

This leads us to consider the following \"mass\" quadratic form in $S_+$ $$\begin{aligned}
\label{mass}
\langle\!\langle\Psi, \Psi\rangle\!\rangle_M = m_1 \langle\!\langle\Psi, ( E^1 E^5 + E^2 E^6+E^3 E^7) E^4 \otimes {\mathbb I}\Psi \rangle\!\rangle
- m_2 \langle\!\langle\Psi, {\mathbb I}\otimes \tilde{E}^1 \tilde{E}^2 \tilde{E}^3 \Psi \rangle\!\rangle\\ \nonumber
+ \psi^i \langle\!\langle\Psi , ( E^1 E^5 + E^2 E^6+E^3 E^7) \otimes \tilde{E}^i \Psi \rangle\!\rangle
+ \frac{1}{2} \phi^i \epsilon^{ijk} \langle\!\langle\Psi, E^4 \otimes \tilde{E}^j \tilde{E}^k \Psi\rangle\!\rangle.
\end{aligned}$$ Here the indices $i,j,k$ run over the values $1,2,3$, and summation convention is implied. Here $\xi\in{\mathbb C}$ is a complex parameter, $m_{1,2}\in{\mathbb R}$ and $\phi^i,\psi^i$ are two real vectors.
