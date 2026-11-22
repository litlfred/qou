---
doc_id: arxiv-0709.3157v1
doc_title: "Chiral Lagrangians with tensor sources"
section_id: sec-002-chiral-building-blocks
section_title: "Chiral building blocks"
section_number: null
pages: 3-3
source_pdf: 0709.3157v1.pdf
source_sha256: 22a0d9a93c9dcb8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.988
doc_brief: "Chiral Lagrangians with tensor sources — The implementation of tensor sources in Chiral Lagrangians allows the computation of Green functions and form factors involving tensor currents, that is"
---
$\chi$PT is based on the spontaneous breakdown of the global $G=SU(n_f)_L\otimes SU(n_f)_R$ flavour symmetry down to its subgroup $SU(n_f)_V$. The dynamical fields $\phi^a=(\pi,K,\eta)$ are assumed to be the (pseudo--)Goldstone bosons associated to this breakdown. The general formalism for effective Lagrangians with spontaneously broken symmetries was worked out by Callan, Coleman, Wess and Zumino [@CWZ], and for our case groups the $n_f^2-1$ fields in the matrix $u$ transforming under $G$ as $$u(\phi^a)\,=\,{\mathrm{exp}}\left(\frac{i}{2\,F_0}\,\,\phi^a\,\lambda^a\right)\,,\quad u(\phi^a)\rightarrow g_R\,u(\phi^a)\,h^{\dagger}\,=\,h\,u(\phi^a)\,g_L^{\dagger}\, .\label{CCWZ}$$ $h$ is the so called compensating field and depends on $g_{L\,R}$ and $u$ itself. Eq. ([\[CCWZ\]](#CCWZ){reference-type="ref" reference="CCWZ"}) defines a non--linear representation of the chiral group $G$.

At very low energies, $\phi^a$ are the only active fields and thence $u$ is the only building block of the theory. Then the QCD action in this regime reads $$Z[v_{\mu},a_{\mu},s,p,{\bar{t}}_{\,\mu\nu}]\,=\,\int {\cal{D}}\,u{\cal{D}}u^{\dagger} \,{\mathrm{exp}}\left[i\int d^4x\,{\cal{L}}_{\chi}(u
;v_{\mu},a_{\mu},s,p,{\bar{t}}_{\mu\nu})\right]\,,$$ where ${\cal{L}}_{\chi}$ necessarily is invariant under the same set of transformations as ${\cal{L}}_{ext}+{\cal{L}}^0_{QCD}$ is invariant.

The first step to find the most efficient set of building blocks is to manipulate $\ell_\mu$ and $r_\mu$ in such a way that the derivative is not explicit : $$\begin{aligned}
&& F_L^{\mu\nu}\,=\,\partial^{\mu}\ell^{\nu}-\partial^{\nu}\ell^{\mu}-i\,[\ell^{\mu},\ell^{\nu}]\, , \quad F_R^{\mu\nu}\,=\,\partial^{\mu}r^{\nu}-\partial^{\nu}r^{\mu}-i\,[r^{\mu},r^{\nu}]\, .\nonumber\\
&&u_\mu=i\left\{ u^{\dagger}(\partial_{\mu}-i\,r_{\mu})u-u(\partial_{\mu}-i\,\ell_{\mu})u^{\dagger}\right\}\quad u_\mu\to h\,u_\mu \,h^\dagger\,.
\end{aligned}$$ Since it will prove to be very convenient to have a set of operators transforming as $u_\mu$ under $G$, we use the set introduced in Refs. [@Bij; @EGPR] $$\begin{aligned}
\label{listinv}
h_{\mu\nu}=\nabla_{\mu}u_{\nu}+\nabla_{\nu}u_{\mu}\, ,&&
f_{\pm}^{\mu\nu}=u\,F_L^{\mu\nu}\,u^{\dagger}\, \pm \, u^{\dagger}\, F_R^{\mu\nu}\, u\, ,\nonumber\\
t_{\pm}^{\mu\nu}=u^{\dagger}\, t^{\mu\nu}\, u^{\dagger}\, \pm \, u\, t^{\mu\nu\,\dagger} \, u\, ,&&
\chi_{\pm}=u^{\dagger} \, \chi \, u^{\dagger}\, \pm \, u\, \chi^{\dagger}\, u\, .
\end{aligned}$$ As a result, one can define a unique covariant derivative for them all, *e.g.*, $$\label{conn}
\nabla_{\rho}X=\partial_{\rho}X+[\Gamma_{\rho},X]\, , \qquad \Gamma_{\rho}=\frac{1}{2}\left\{u^{\dagger}(\partial_{\rho}-i\,r_{\rho})u+u(\partial_{\rho}-i\,\ell_{\rho})u^{\dagger}\right\}\, ,$$
