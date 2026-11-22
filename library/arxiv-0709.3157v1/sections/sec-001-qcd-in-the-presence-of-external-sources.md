---
doc_id: arxiv-0709.3157v1
doc_title: "Chiral Lagrangians with tensor sources"
section_id: sec-001-qcd-in-the-presence-of-external-sources
section_title: "QCD in the presence of external sources"
section_number: null
pages: 2-3
source_pdf: 0709.3157v1.pdf
source_sha256: 22a0d9a93c9dcb8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.98
doc_brief: "Chiral Lagrangians with tensor sources — The implementation of tensor sources in Chiral Lagrangians allows the computation of Green functions and form factors involving tensor currents, that is"
---
The external field method was first introduced by Leutwyler [@Leut], and makes easier the computation of QCD Green functions and form factors. It enforces chiral Ward identities exactly by promoting the global chiral symmetry to a local one. The basic idea is to introduce in the QCD action a set of local fields coupled to the QCD currents : $$\!Z[v_{\mu},a_{\mu},s,p,{\bar{t}}_{\,\mu\nu}]=\!\!\int\! {\cal{D}}{\bar{q}}\,{\cal{D}}q\,{\cal{D}}G_{\mu} \,{\mathrm{exp}}\!\left[i\!\int\! d^4x\,\left\{ {\cal{L}}_{QCD}^0+{\cal{L}}_{ext}(v_{\mu},a_{\mu},s,p,{\bar{t}}_{\mu\nu})\right\}\right],$$ where ${\cal{L}}^0_{QCD}$ is the massless QCD Lagrangian and $$\label{sources}
{\cal{L}}_{ext}\,=\,{\bar{q}}\,\,\gamma_{\mu}\,(v^{\mu}+\gamma_5\,a^{\mu})\,q-{\bar{q}}\,(s-i\,\gamma_5\,p)\,q+{\bar{q}}
\,\sigma_{\mu\nu}\,{\bar{t}}^{\,\mu\nu}\,q\, ,$$ where $v_{\mu}$, $a_{\mu}$, $s$, $p$ and ${\bar{t}}^{\,\mu\nu}$ are hermitian matrices in flavor space. The vector and axial-vector external fields are chosen to be traceless in flavor space, but the rest of them will in general have a non-vanishing trace.

For making the chiral symmetry transformations manifest, one uses the left-- and right--handed fermion fields. Then the tensor source is split as [@Cata:2007ns] $${\bar{q}}\,\sigma_{\mu\nu}\,{\bar{t}}^{\,\mu\nu}q\,=\,{\bar{q}}_L\sigma^{\mu\nu}t^{\dagger}_{\,\mu\nu}q_R\,+\,{\bar{q}}_R\,\sigma^{\mu\nu}t_{\,\mu\nu}q_L\, ,$$ with $$\!\!\!t^{\,\mu\nu}=P_L^{\mu\nu\lambda\rho}\,{\bar{t}}_{\,\lambda\rho}\,,\quad \!
P_R^{\mu\nu\lambda\rho}=\frac{1}{4}(g^{\mu\lambda}g^{\nu\rho}-g^{\nu\lambda}g^{\mu\rho}+i\,\varepsilon^{\mu\nu\lambda\rho})\, ,\quad\!
P_L^{\mu\nu\lambda\rho}=\left( P_R^{\mu\nu\lambda\rho}\right)^\dagger\!\!\!\!\!.\label{chiral-projector}$$ It is not difficult to check that $P_{L\,R}$ are chiral projectors, and then $t_{\,\mu\nu}$ and $t^{\,\dagger}_{\mu\nu}$ are the left-- and right--handed projections of the tensor field ${\bar{t}}_{\,\mu\nu}$. So the tensor source is its own chiral partner, as one expects from the fact that $\gamma_5\,\sigma^{\mu\nu}$ is not independent from $\sigma^{\mu\nu}$.

We want ${\cal{L}}_{ext}$ to have the same symmetries as ${\cal{L}}^0_{QCD}$. Moreover we want chiral symmetry to hold even at a local level, that is, invariance under the transformation $q_{L\,R}\to g_{L\,R}(x)\,\,q_{L\,R}$, with $g_{L\,R}(x)$ $SU(n_f)_{L\,R}$ matrices. We cannot impose local invariance on ${\cal{L}}_{ext}$ and ${\cal{L}}^0_{QCD}$ separately : it must be done on ${\cal{L}}_{ext}+{\cal{L}}^0_{QCD}$, being the $\ell_\mu=v_\mu+a_\mu$ and $r_\mu=v_\mu-a_\mu$ the analogs of gauge fields. It is customary to group the scalar and pseudoscalar sources in the combination $\chi=2\,B_0\,(s+i\,p)$, being $B_0$ related to the quark condensate. Then local chiral invariance dictates the transformation properties of the external sources to be : $$\begin{aligned}
\label{sou}
r_{\mu}\rightarrow g_R\,r_{\mu}\,g_R^{\dagger}+\,i\,g_R\,\partial_{\mu}\,g_R^{\dagger}\, ,&& 
\ell_{\mu}\rightarrow g_L\,\ell_{\mu}\,g_L^{\dagger}\,+\,i\,g_L\,\partial_{\mu}\,g_L^{\dagger}\, ,\nonumber\\
\chi \rightarrow g_R\,\chi\, g_L^{\dagger}\, ,&&
t_{\,\mu\nu} \rightarrow g_R\,\, t_{\,\mu\nu}\, g_L^{\dagger}\, .
\end{aligned}$$
