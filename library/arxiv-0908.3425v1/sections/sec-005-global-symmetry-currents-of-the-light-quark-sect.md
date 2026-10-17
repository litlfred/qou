---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-005-global-symmetry-currents-of-the-light-quark-sect
section_title: "Global symmetry currents of the light quark sector"
section_number: null
pages: 7-8
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.953
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsubsec_agsl label="subsubsec_agsl"} Due to the flavor independence of the covariant derivative, ${\cal L}^0_{\rm QCD}$ is invariant under the infinitesimal global transformations of the left- and right-handed quark fields, $$\begin{aligned}
\label{2:1:3:u3lu3r}
q_L\equiv
\left(\begin{array}{c}u_L\\d_L\\s_L\end{array}\right)&\mapsto&
\left({\mathbbm 1}-i\sum_{a=1}^8
\epsilon^L_a\frac{\lambda_a}{2}-i\epsilon^L\right)q_L,\nonumber\\
q_R\equiv\left(\begin{array}{c}u_R\\d_R\\s_R\end{array}\right) &\mapsto& \left({\mathbbm 1}-i\sum_{a=1}^8
\epsilon^R_a\frac{\lambda_a}{2}-i\epsilon^R\right)q_R.
\end{aligned}$$ Note that the Gell-Mann matrices act in flavor space. ${\cal L}^0_{\rm QCD}$ is said to have a classical *global* $\mbox{U(3)}_L\times\mbox{U(3)}_R$ symmetry. Applying Noether's theorem [@Noether:1918], [@Hill:1951], [@Gell-Mann:1960np], from such an invariance one would expect a total of $2\times(8+1)=18$ conserved currents: $$\label{2:1:3:str} L^{\mu}_a=\bar{q}_L\gamma^\mu \frac{\lambda_a}{2}q_L,\quad
L^{\mu}=\bar{q}_L\gamma^\mu q_L,\quad
R^{\mu}_a=\bar{q}_R\gamma^\mu \frac{\lambda_a}{2}q_R,\quad
R^{\mu}=\bar{q}_R\gamma^\mu q_R.$$ Making use of $$P_L\gamma^\mu P_R\pm P_R\gamma^\mu P_L
=\left\{\begin{array}{l}\gamma^\mu\\\gamma^\mu\gamma_5\end{array}\right.,$$ we introduce the linear combinations $$\begin{aligned}
\label{2:1:3:v}
V^{\mu}_a&=& R^{\mu}_a+L^{\mu}_a=\bar{q}\gamma^\mu\frac{\lambda_a}{2}q,\\
\label{2:1:3:a}
A^{\mu}_a&=&R^{\mu}_a-L^{\mu}_a=\bar{q}\gamma^\mu\gamma_5
\frac{\lambda_a}{2}q,
\end{aligned}$$ which under a parity transformation of the quark fields, $q(t,\vec x)\mapsto \gamma_0 q(t,-\vec x)$, transform as vector and axial-vector current densities, respectively, $$\begin{aligned}
\label{2:1:3:pv}
P:V^{\mu}_a(t,\vec{x})\mapsto V_{a\mu}(t,-\vec{x}),\\
\label{2:1:3pa} P: A^{\mu}_a(t,\vec{x})\mapsto -A_{a\mu}(t,-\vec{x}).
\end{aligned}$$ The conserved singlet vector current results from a transformation of all left-handed and right-handed quark fields by the *same* phase, $$\label{2:1:3:sv}
V^\mu=R^{\mu}+L^{\mu}=\bar{q}\gamma^\mu q.$$ The singlet axial-vector current originates from a transformation of all left-handed quark fields with one phase and all right-handed with the *opposite* phase, $$\label{2:1:3:sav}
A^\mu= R^{\mu}-L^{\mu}=\bar{q}\gamma^\mu\gamma_5q.$$ Quantum fluctuations destroy the singlet axial-vector current conservation and there will be extra terms, referred to as anomalies [@Bell:1969ts], [@Adler:1969gk], [@Adler:1969er], resulting in $$\partial_\mu A^\mu=\frac{3 g^2_3}{32\pi^2}\epsilon_{\mu\nu\rho\sigma}
{\cal G}^{\mu\nu}_a {\cal G}^{\rho\sigma}_a,\quad \epsilon_{0123}=1.$$ The factor of three originates from the number of flavors. In the large $N_c$ (number of colors) limit of Ref. [@{'tHooft:1973jz}] the singlet axial-vector current is conserved, because the strong coupling constant behaves as $g^2_3\sim N_c^{-1}$.
