---
doc_id: arxiv-0709.3157v1
doc_title: "Chiral Lagrangians with tensor sources"
section_id: sec-003-the-chiral-lagrangian
section_title: "The chiral Lagrangian"
section_number: null
pages: 3-5
source_pdf: 0709.3157v1.pdf
source_sha256: 22a0d9a93c9dcb8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "Chiral Lagrangians with tensor sources — The implementation of tensor sources in Chiral Lagrangians allows the computation of Green functions and form factors involving tensor currents, that is"
---
The number of operators entering in the chiral Lagrangian is of course not restricted by symmetry. So in principle there are an infinite number of them, each one multiplied by an unknown coefficient (this is in agreement with the fact that $\chi$PT is not normalizable *stricto sensu*). So if one has to take them all into account in any calculation, loses all predictive power. At low energies (compared with the chiral scale $\Lambda_\chi\sim4\pi F\sim 1\, \mathrm{GeV}$) pieces with lower powers of momentum and quark masses dominate, and this allows to truncate the number of operators. This idea is systematized by the Weinberg power counting scheme [@Wei].

So all of the building blocks must be endowed with a power counting, determined by the number of derivatives and masses : $\ell_\mu$ and $r_\mu$ appear as covariant derivatives and this fixes its counting; masses count as two power of derivatives, and this dictates the counting of $s$ and $p$. Since the tensor source does not have a physical realization, its counting is arbitrary. We have then $$u \sim {\cal{O}}(p^0)\, ,\quad v_{\mu}\,,\,\,a_{\mu}\sim {\cal{O}}(p^1)\, ,\quad
\chi\,,\,\,t_{\,\mu\nu} \sim {\cal{O}}(p^2)\, ,$$  

Using the tracelessness properties $\langle r_{\,\mu}\rangle=\langle \ell_{\,\mu}\rangle=\langle F_{L\,R}^{\,\mu\nu}\rangle=\langle f_{\pm}^{\,\mu\nu}\rangle=\langle u_{\,\mu}\rangle=0$ we find four new terms [@Cata:2007ns] at $\mathcal{O}(p^4)$ \[tensor sources do not appear at $\mathcal{O}(p^2)$\] $$\label{O4}
{\cal{L}}_4^{\chi PT}\,=\,\Lambda_1\,\langle\, t_+^{\,\mu\nu}\,f_{+\mu\nu}\,\rangle\,-\,i\,\Lambda_{2}\,\langle\, t_+^{\,\mu\nu}\,u_{\,\mu}u_{\,\nu}\,\rangle\,+\,\Lambda_{3}\,\langle\, t_+^{\,\mu\nu}\,t_{+\,\mu\nu}\,\rangle\,+\,\Lambda_{4}\,\langle\, t_+^{\,\mu\nu}\,\rangle^2\, ,$$ where $\langle \cdots \rangle$ stands for the trace in $n_f$ flavour space. At this order there is no contact term because of the identities $t_+^{\mu\nu}\,t^+_{\mu\nu}=t_-^{\mu\nu}\,t^-_{\mu\nu}$ and $t_+^{\mu\nu}\,t^-_{\mu\nu}=t_-^{\mu\nu}\,t^+_{\mu\nu}$.

At $\mathcal{O}(p^6)$ there are more than a hundred operators involving tensor sources, but not all of them are independent. The steps one must follow for the reduction of the number of operators were given in Ref. [@Bij] and we briefly review them now :

**(a) Partial integration and lowest order equations of motion**

Terms connected by partial integration leave the action invariant, and should be considered only once. The lowest order equation of motion must be used to reduce the basis (it is equivalent to a field redefinition [@Bij]). It reads $$\label{EOM}
\nabla_{\mu}u^{\,\mu}\,=\,\frac{1}{2\,i}\left(\frac{\langle \chi_-\rangle}{n_f}-\chi_-\right)\, .$$

**(b) Bianchi identities**

There is an associated bianchi identity to the covariant derivative ([\[conn\]](#conn){reference-type="ref" reference="conn"}) that translates into one relation that allows to eliminate one operator $$\nabla_{\mu}f_{+\nu\alpha}+\nabla_{\nu}f_{+\alpha\mu}+\nabla_{\alpha}f_{+\mu\nu}\,=\,\frac{i}{2}\left(\left[f_{-\mu\nu},u_{\alpha}\right]+\left[f_{-\nu\alpha},u_{\mu}\right]+\left[f_{-\alpha\mu},u_{\nu}\right]\right)\,.$$

**(c) Isolation of contact terms**

In our basis there are linear combinations of operators which only depend on external sources. They are unphysical but however necessary to make the theory renormalizable. One has to isolate such terms, and at this order there appear only three.

**(c) Cayley--Hamilton relations**

The three first steps are generic for an arbitrary number of light flavours $n_f$, but the only phenomenologically interesting values are $n_f=2,\,3$. For such values additional matrix relations (based on the Cayley--Hamilton theorem) further reduce the number of independent operators. The full list of such relations can be found in Ref. [@Cata:2007ns].

So we end up with 117 operators plus three contat terms for $n_f$ flavours, 110+3 for $n_f=3$ and 75+3 for $2$. These operators are listed in Ref. [@Cata:2007ns]. In Ref. [@Haefeli:2007ty] a caveat is given, and it is claimed that the above procedure does not necessarily yield a minimal basis. However we believe that tensor sources are not affected by their considerations.
