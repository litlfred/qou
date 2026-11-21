---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-027-the-effective-wess-zumino-witten-action
section_title: "The effective Wess-Zumino-Witten action"
section_number: null
pages: 39-42
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.938
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
The Lagrangians discussed so far have a larger symmetry than QCD [@Witten:1983tw]. For example, if we consider the case of "pure" QCD, i.e., no external fields except for the quark-mass term $\chi=2B_0 {\cal M}$, ${\cal L}_2$ and ${\cal L}_4$ contain interaction terms with an even number of Goldstone bosons only (even intrinsic parity). In other words, they cannot describe, e.g, $K^+K^-\to\pi^+\pi^-\pi^0$. Analogously, ${\cal L}_2$ and ${\cal L}_4$ including a coupling to electromagnetic fields cannot describe $\pi^0\to\gamma\gamma$.

In order to overcome this shortcoming, Witten suggested to add the simplest term possible which breaks the symmetry of having only an even number of Goldstone bosons at the Lagrangian level. For the case of massless Goldstone bosons without any external fields the modified equation of motion reads $$\label{3:3:2:modeom}
\partial_\mu\left(\frac{F_0^2}{2}U\partial^\mu U^\dagger\right)
+\lambda \epsilon^{\mu\nu\rho\sigma} U\partial_\mu U^\dagger
U\partial_\nu U^\dagger U\partial_\rho U^\dagger U\partial_\sigma
U^\dagger=0,$$ where $\lambda$ is a (purely imaginary) constant. For the purpose of writing down an action corresponding to Eq. ([\[3:3:2:modeom\]](#3:3:2:modeom){reference-type="ref" reference="3:3:2:modeom"}), we extend the range of definition of the fields to a hypothetical fifth dimension, $$\label{3:2:ualpha}
U(y)=\exp\left(i\alpha\frac{\phi(x)}{F_0}\right),
\quad y^i=(x^\mu,\alpha),\,\,i=0,\cdots, 4,\,\, 0\leq\alpha\leq 1,$$ where Minkowski space is defined as the surface of the five-dimensional space for $\alpha =1$. The action in in the absence of external fields (denoted by a superscript 0) is given by [@Witten:1983tw] $$\label{3:2:2:sano}
S_{\rm ano}^0=n S_{\rm WZW}^0,\quad
S_{\rm WZW}^0=-\frac{i}{240\pi^2}\int_0^1 \mbox{d} \alpha \int \mbox{d}^4 x
\epsilon^{ijklm} \mbox{Tr}\left( {\cal U}^L_i\cdots {\cal U}^L_m
\right),$$ where $$\epsilon_{01234}=-\epsilon^{01234}=1,\quad {\cal U}^L_i=U^\dagger
\frac{\partial U}{\partial y^i},\quad \lambda=\frac{in}{48\pi^2}.$$ A rather unusual and surprising feature of Eq. ([\[3:2:2:sano\]](#3:2:2:sano){reference-type="ref" reference="3:2:2:sano"}) is that the action functional corresponding to the new term cannot be written as the four-dimensional integral of a Lagrangian expressed in terms of $U$ and its derivatives. Wess and Zumino derived consistency or integrability relations which are satisfied by the anomalous Ward identities and then explicitly constructed a functional involving the pseudoscalar octet which satisfies the anomalous Ward identities [@Wess:1971yu]. In particular, Wess and Zumino emphasized that their interaction Lagrangians cannot be obtained as part of a chiral invariant Lagrangian. Using topological arguments Witten showed that the constant $n$ appearing in Eq. ([\[3:2:2:sano\]](#3:2:2:sano){reference-type="ref" reference="3:2:2:sano"}) must be an integer. However, it was pointed out in Ref. [@Bar:2001qk] that the traditional argument relating $n$ with the number of colors $N_c$ is incomplete. Before discussing this argument, let us investigate the consequences of $S^0_{\rm WZW}$.

Expanding the SU(3) matrix $U(y)$ in terms of the Goldstone boson fields, $U(y)={\mathbbm 1}+i\alpha \phi(x)/F_0+O(\phi^2)$, one obtains an infinite series of terms, each involving an odd number of Goldstone bosons, i.e., the WZW action $S_{\rm WZW}^0$ is of odd intrinsic parity. For each individual term the $\alpha$ integration can be performed explicitly resulting in an ordinary action in terms of a four-dimensional integral of a local Lagrangian. For example, the term with the smallest number of Goldstone bosons reads $$\label{3:2:2:swzw5phi}
S_{\rm WZW}^{5\phi}
=\frac{1}{240\pi^2 F^5_0}\int \mbox{d}^4 x
\epsilon^{\mu\nu\rho\sigma}\mbox{Tr}(\phi\partial_\mu\phi\partial_\nu\phi
\partial_\rho\phi\partial_\sigma\phi),$$ which describes, e.g., $K^+K^-\to\pi^+\pi^-\pi^0$. In particular, the WZW action without external fields involves at least five Goldstone bosons [@Wess:1971yu].

The connection to the number of colors $N_c$ is established by introducing a coupling to electromagnetism [@Wess:1971yu], [@Witten:1983tw]. In the presence of external fields there will be an additional term in the anomalous action, $$\label{4:8:sanofull}
S_{\rm ano}=
S_{\rm ano}^0+
S_{\rm ano}^{\rm ext}=n(S_{\rm WZW}^0+S_{\rm WZW}^{\rm ext}),$$ given by (see, e.g., Ref. [@Bijnens:1993xi]) $$\label{3:3:2:deltaswzw}
S_{\rm WZW}^{\rm ext}= -\frac{i}{48\pi^2}\int \mbox{d}^4 x\,
\epsilon^{\mu\nu\rho\sigma}\mbox{Tr}(Z_{\mu\nu\rho\sigma})$$ with $$\begin{aligned}
\label{3:3:2:zmunialphabeta}
Z_{\mu\nu\rho\sigma}&=&
\frac{1}{2}\ U l_\mu U^\dagger r_\nu U l_\rho U^\dagger r_\sigma
+U l_\mu l_\nu l_\rho U^\dagger r_\sigma
 - U^\dagger r_\mu r_\nu r_\rho U l_\sigma\nonumber\\
&&+i  U\partial_\mu l_\nu l_\rho U^\dagger r_\sigma
 - i U^\dagger\partial_\mu r_\nu r_\rho U l_\sigma
 +i \partial_\mu r_\nu U l_\rho U^\dagger r_\sigma
 - i \partial_\mu l_\nu U^\dagger r_\rho U l_\sigma\nonumber\\
&&-i {\cal U}_\mu^L l_\nu U^\dagger r_\rho U l_\sigma
 + i {\cal U}_\mu^R r_\nu U l_\rho U^\dagger r_\sigma
 -i {\cal U}_\mu^L l_\nu l_\rho l_\sigma
 + i {\cal U}_\mu^R r_\nu r_\rho r_\sigma\nonumber\\
&&+\frac{1}{2}{\cal U}_\mu^L U^\dagger\partial_\nu r_\rho U l_\sigma
 -\frac{1}{2}{\cal U}_\mu^R U\partial_\nu l_\rho U^\dagger r_\sigma
 +\frac{1}{2}{\cal U}_\mu^L U^\dagger r_\nu U\partial_\rho l_\sigma
 -\frac{1}{2}{\cal U}_\mu^R U l_\nu U^\dagger\partial_\rho r_\sigma\nonumber\\
&&-{\cal U}_\mu^L{\cal U}_\nu^L U^\dagger r_\rho U l_\sigma
 + {\cal U}_\mu^R{\cal U}_\nu^R U l_\rho U^\dagger r_\sigma
+\frac{1}{2}\ {\cal U}_\mu^L l_\nu {\cal U}_\rho^L l_\sigma
 - \frac{1}{2}\ {\cal U}_\mu^R r_\nu {\cal U}_\rho^R r_\sigma\nonumber\\
&&+{\cal U}_\mu^L l_\nu\partial_\rho l_\sigma
 - {\cal U}_\mu^R r_\nu\partial_\rho r_\sigma+{\cal U}_\mu^L\partial_\nu  l_\rho l_\sigma
 - {\cal U}_\mu^R\partial_\nu  r_\rho r_\sigma\nonumber\\
&&-i {\cal U}_\mu^L{\cal U}_\nu^L{\cal U}_\rho^L l_\sigma
 + i {\cal U}_\mu^R{\cal U}_\nu^R{\cal U}_\rho^R r_\sigma,
\end{aligned}$$ where we defined the abbreviations ${\cal U}_\mu^L=U^\dagger\partial_\mu U$ and ${\cal U}_\mu^R=U\partial_\mu U^\dagger$.

As a special case, let us consider a coupling to external electromagnetic fields by inserting $$r_\mu=l_\mu=-e Q {\cal A}_\mu,$$ where $Q$ is the quark-charge matrix. The terms involving three and four electromagnetic four-potentials vanish upon contraction with the totally antisymmetric tensor $\epsilon^{\mu\nu\rho\sigma}$, because their contributions to $Z_{\mu\nu\rho\sigma}$ are symmetric in at least two indices, and we obtain $$\label{3:3:2:lanoelm}
n{\cal L}^{\rm ext}_{\rm WZW}=-e n {\cal A}_\mu J^\mu
+i \frac{n e^2 }{48\pi^2}\epsilon^{\mu\nu\rho\sigma}
\partial_\nu {\cal A}_\rho{\cal A}_\sigma
\mbox{Tr}[2Q^2(U\partial_\mu U^\dagger - U^\dagger \partial_\mu U)
- Q U^\dagger Q \partial_\mu U
+Q U Q \partial_\mu U^\dagger].$$ We note that the current $$\label{3:3:2:jmu}
J^\mu=\frac{\epsilon^{\mu\nu\rho\sigma}}{48\pi^2}
\mbox{Tr}(Q\partial_\nu U U^\dagger \partial_\rho U U^\dagger
\partial_\sigma U U^\dagger
+Q U^\dagger \partial_\nu U U^\dagger \partial_\rho U U^\dagger
\partial_\sigma U),\quad \epsilon_{0123}=1,$$ by itself is not gauge invariant and the additional terms of Eq. ([\[3:3:2:lanoelm\]](#3:3:2:lanoelm){reference-type="ref" reference="3:3:2:lanoelm"}) are required to obtain a gauge-invariant action. The standard procedure of determining $n$ is to investigate the interaction Lagrangian which is relevant to the decay $\pi^0\to\gamma\gamma$ by expanding $U={\mathbbm 1}+i\mbox{diag}(\pi^0,-\pi^0,0)/F_0+\cdots.$ However, as pointed out by Bär and Wiese, when considering the electromagnetic interaction for an arbitrary number of colors one should replace the ordinary quark charge matrix by $$Q=\left(
\begin{array}{rrr}
\frac{2}{3}&0&0\\
0&-\frac{1}{3}&0\\
0&0&-\frac{1}{3}
\end{array}
\right)
\to
\left(
\begin{array}{ccc}
\frac{1}{2N_c}+\frac{1}{2}&0&0\\
0&\frac{1}{2N_c}-\frac{1}{2}&0\\
0&0&\frac{1}{2N_c}-\frac{1}{2}
\end{array}
\right).$$ The corresponding effective Lagrangian for $\pi^0\to\gamma\gamma$ decay, $${\cal L}_{\pi^0\gamma\gamma}=-\frac{n}{N_c}
\frac{e^2}{32\pi^2}\epsilon^{\mu\nu \rho\sigma}{\cal
F}_{\mu\nu}{\cal F}_{\rho\sigma}\frac{\pi^0}{F_0},$$ results in the decay rate $$\Gamma_{\pi^0\to\gamma\gamma}= \frac{\alpha^2 M^3_{\pi^0}}{64 \pi^3
F^2_0}\,\frac{n^2}{N_c^2}
=7.6\,\mbox{eV}\times\left(\frac{n}{N_c}\right)^2$$ in good agreement with the experimental value $(7.7\pm 0.6)$ eV for $n=N_c$. However, the result is no indication for $N_c=3$ [@Bar:2001qk]. The conclusion from their analysis is that one should rather consider three-flavor processes such as $\eta\to\pi^+\pi^-\gamma$ or $K\gamma\to K\pi$ to test the expected $N_c$ dependence in a low-energy reaction. For example, the Lagrangian relevant to the decay $\eta\to\pi^+\pi^-\gamma$ is given by $${\cal L}_{\eta\pi^+\pi^-\gamma}=\frac{ien}{12\sqrt{3}\pi^2 F_0^3}(Q_u-Q_d)
\epsilon^{\mu\nu\rho\sigma}{\cal A}_\mu\partial_\nu\eta\partial_\rho\pi^+
\partial_\sigma\pi^-,$$ where the quark-charge difference $Q_u-Q_d=1$ is independent of $N_c$. However, by investigating the corresponding $\eta$ and $\eta'$ decays up to next-to-leading order in the framework of the combined $1/N_c$ and chiral expansions, Borasoy and Lipartia have concluded that the number of colors cannot be determined from these decays due to the importance of sub-leading terms which are needed to account for the experimental decay widths and photon spectra [@Borasoy:2004mf].

For a discussion of the ${\cal O}(q^6)$ Lagrangian of odd intrinsic parity see Refs. [@Ebertshauser:2001nj] and [@Bijnens:2001bb].
