---
doc_id: arxiv-hep-ph-9302246v1
doc_title: "arXiv:hep-ph/9302246v1 11 Feb 1993"
section_id: sec-001-2-the-low-energy-chiral-lagrangians
section_title: "The low-energy chiral Lagrangians"
section_number: 2
pages: 2-12
source_pdf: 9302246v1.pdf
source_sha256: 2d352297255be8de
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.98
---
[]{#2b label="2b"}

We shall give a summary of what is known at present about low-energy mesonic Lagrangians, from the chiral invariance properties of ${\cal L}_{\rm QCD}$ alone. In the pseudoscalar sector, the terms in the effective Lagrangian ${\cal L}_{\rm eff}$ with the lowest chiral dimension, *i.e.* ${\cal O} (p^2)$, are

$$\label{22}
{\cal L}_{\rm eff}^{(2)} = {1\over 4} \, f^2_0 \, \Big
\{ \hbox{tr}\,\left( D_\mu U D^\mu \, U^\dagger \right)\, + \,
\hbox{tr}\, (\chi U^{\dagger} + U \chi^\dagger) \Big \}$$

where $D_{\mu}$ denotes the covariant derivative

$$\label{23}
D_{\mu} U = \partial_\mu U -i( v_\mu + a_\mu)U
+ i U(v_\mu - a_\mu)\,,$$

and $U \equiv \exp \left( -\frac{\displaystyle\sqrt 2 i
\Phi}{\displaystyle f_0} \right)$ an SU(3) matrix incorporating the octet of pseudoscalar mesons

$$\label{eta8}
\begin{array}{c}\Phi (x)\,=\,\frac{\displaystyle\vec{\lambda}}{\displaystyle\sqrt 2}
\, \vec{\varphi}
\, = \, \left( \begin{array}{ccc} \frac{\displaystyle\pi^0}{\displaystyle\sqrt 2}
\, + \, \frac{\displaystyle\eta_8}{\displaystyle\sqrt 6}
 & \pi^+ & K^+ \\ \pi^- & - \frac{\displaystyle\pi^0}{\displaystyle\sqrt 2} \,
+ \, \frac{\displaystyle\eta_8} {\displaystyle\sqrt 6}  & K^0 \\ K^- & \overline
{K^0} & - \frac{\displaystyle 2 \, \eta_8}{\displaystyle\sqrt 6} \end{array}
\right) \end{array}.$$

In Eq. ([\[23\]](#23){reference-type="ref" reference="23"}) $v_\mu$, $a_\mu$ are external 3 $\times$ 3 vector and axial-vector field matrices. In Eq. ([\[22\]](#22){reference-type="ref" reference="22"})

$$\label{24} \matrix{
\chi \, = \, 2 \, B_0\, (s(x)\, +\, i\, p(x))\,, \hfill \cr\cr}$$

with $s$ and $p$ external scalar and pseudoscalar 3 $\times$ 3 field matrices. In practice

$$\label{mass1} \matrix{
\chi\,=\,2\, B_0\, {\cal M} \hfill\cr\cr}$$

with ${\cal M}$ the 3 $\times$ 3 flavour matrix ${\cal M} \,=\, {\rm diag} (m_u, m_d, m_s)$ which collects the light-quark masses. The constants $f_0$ and $B_0$ are not fixed by chiral symmetry requirements. The constant $f_0$ can be obtained from $\pi \to \mu \nu$ decay [@pdg],

$$\label{25}
f_0 \simeq f_{\pi} \simeq 93  \, {\rm MeV}.$$

The constant $B_0$ is related to the vacuum expectation value

$$\label{26}
\langle 0 \vert \bar {q} q
\vert 0 \rangle_{\vert q=u,d,s} = \,-\, f_0^2 \, B_0
\, (1\, +\, {\cal O} ({\cal M})).$$

In the absence of the U(1)$_A$ anomaly, the SU(3) singlet $\eta_1$ field becomes the ninth Goldstone boson which is incorporated in the $\Phi(x)$ field as

$$\label{eta1}
\Phi(x) \,=\,\frac{\displaystyle\vec{\lambda}}{\displaystyle\sqrt 2} \,
\vec{\varphi} \,+\, \frac{\displaystyle\eta_1}{\displaystyle\sqrt 3}
\,\mbox{\LARGE\bf 1}\,.$$

The terms in ${\cal L}_{\rm eff}$ of ${\cal O}(p^4)$ are also known. They have been discussed extensively by Gasser and Leutwyler [@gl].

We are interested in an effective Lagrangian ${\cal L}^R_{\rm eff}$ which also incorporates chiral couplings of fields of massive $1^-$, $1^+$ and $0^+$ states to the Goldstone fields. We shall restrict ourselves to the sector of spin-1 particles. The general method to construct these couplings was described a long time ago in Ref. [@cwz]. An explicit construction can be found in Refs. [@egpr] and [@eglpr]. As discussed in Ref. [@eglpr], the choice of fields to describe chiral invariant couplings involving spin-1 particles is not unique and, when the vector modes are integrated out, leads to ambiguities in the context of chiral perturbation theory to ${\cal O} (p^4)$ and higher. As shown in [@eglpr], these ambiguities are, however, removed when consistency with the short-distance behaviour of QCD is incorporated. The effective Lagrangian which we shall choose here to describe spin-1 particle couplings corresponds to the so-called model II in Ref. [@eglpr]. In this model the linear couplings of vector and axial-vector fields to the pseudoscalar mesons and external fields start at chiral ${\cal O} (p^3)$. The most general Lagrangian ${\cal L}^R_{\rm eff}$ for spin-1 particles to lowest non-trivial order in the chiral expansion and linear in the spin-1 fields for the interaction terms is then obtained by adding to ${\cal L}^{(2)}_{\rm eff}$ in Eq. ([\[22\]](#22){reference-type="ref" reference="22"}) the vector Lagrangian

$$\label{47} \matrix{
{\cal L}_V = & -\, \frac{\displaystyle 1}{\displaystyle 4} \,
\hbox{tr}\left(V_{\mu \nu} V^{\mu \nu} - 2\, M_V^2 \, V_{\mu}V^{\mu}\right)
\hfill \cr\cr \hphantom{{\cal L}_V =}&
\, - \, \frac{\displaystyle 1}{\displaystyle 2 \sqrt 2} \,
\left[f_V \, \hbox{tr}\left(V_{\mu \nu} f_{(+)}^{\mu \nu} \right)
+ \, i g_V \, \hbox{tr}\left(V_{\mu \nu}[\xi^{\mu},\xi^{\nu}]\right)\right]
\hfill \cr\cr \hphantom{{\cal L}_V =}&
+ \, i \, \alpha_V \, \hbox{tr}\left(V_\mu [\xi_\nu, f_{(-)}^{\mu \nu}]
\right)
\, + \, \beta_V \, \hbox{tr}\left(V_\mu [\xi^\mu, \chi_{(-)}]\right) \,
+ \, i \, \theta_V \, \epsilon_{\mu \nu \alpha \beta} \,
\hbox{tr}\left(V^\mu \xi^\nu \xi^\alpha \xi^\beta \right)
\hfill \cr\cr \hphantom{{\cal L}_V =}&
+ \, h_V \, \epsilon_{\mu \nu \alpha \beta} \, \hbox{tr}\left(
V^\mu \left\{ \xi^\nu, f_{(+)}^{\alpha \beta} \right\} \right)\,,
\hfill \cr}$$

and the axial-vector Lagrangian

$$\label{48} \matrix{
{\cal L}_A = & -\, \frac{\displaystyle 1}{\displaystyle 4} \,
\hbox{tr}\left(A_{\mu \nu} A^{\mu \nu} -
2M_A^2 A_{\mu}A^{\mu}\right) \, - \, \frac{\displaystyle 1}{\displaystyle 2 \sqrt 2} \,
f_A \, \hbox{tr}\left( A_{\mu \nu} f_{(-)}^{\mu \nu} \right)
\hfill \cr\cr \hphantom{{\cal L}_A =}&
+ \, i \, \alpha_A \, \hbox{tr}\left(A_\mu [\xi_\nu, f_{(+)}^{\mu \nu}]
\right)
\, + \, \gamma^{(1)}_A \, \hbox{tr}\left( A_\mu \xi_\nu \xi^\mu \xi^\nu
\right) \, + \, \gamma^{(2)}_A \, \hbox{tr}\left( A_\mu \left \{ \xi^\mu,
 \xi^\nu \xi_\nu \right \} \right)
\hfill \cr\cr \hphantom{{\cal L}_A =}&
+ \, \gamma^{(3)}_A \, \hbox{tr}\left( A_\mu \xi_\nu \right) \, \hbox{tr}
\left( \xi^\mu \xi^\nu \right) \,
+ \, \gamma^{(4)}_A \, \hbox{tr}\left( A_\mu \xi^\mu \right) \, \hbox{tr}
\left( \xi^\nu \xi_\nu \right)
\hfill \cr\cr \hphantom{{\cal L}_A =}&
\, + \,h_A \, \epsilon_{\mu \nu \alpha \beta} \, \hbox{tr}
\left( A^\mu \left\{ \xi^\nu, f_{(-)}^{\alpha \beta} \right\} \right)
\,. \hfill \cr}$$

The notation here is the following. We assume nonet symmetry for the spin-1 particles, so that the spin-1 fields we consider are

$$\label{nonet} \matrix{
V^\mu \,=\, V^\mu_8\,+\, V^\mu_1 \hfill\cr\cr
A^\mu \,=\, A^\mu_8\,+\, A^\mu_1
\hfill\cr\cr}$$

where $V^\mu_8$ and $A^\mu_8$ are SU(3)$_V$ octets while $V^\mu_1$ and $A^\mu_1$ are singlets. The vector field matrix $V^{\mu}_8(x)$:

$$\label{w8} \begin{array}{c}V^\mu_8 (x) \equiv
\left( \begin{array}{ccc} \frac{\displaystyle\rho^0}{\displaystyle\sqrt 2}
\, + \, \frac{\displaystyle\omega_8}{\displaystyle\sqrt 6}
 & \rho^+ & K^{* +} \\ \rho^- & - \frac{\displaystyle\rho^0}{\displaystyle\sqrt 2} \,
+ \, \frac{\displaystyle\omega_8} {\displaystyle\sqrt 6}  & K^{* 0} \\ K^{*
-} & \overline {K^{* 0}} & - \frac{\displaystyle 2 \, \omega_8}{\displaystyle\sqrt 6}
\end{array} \right)^\mu \, ,\end{array}$$

represents the SU(3)$_V$ octet of spin-parity $1^-$-particles and the axial-vector field matrix $A^{\mu}_8(x)$:

$$\begin{array}{c}A^\mu_8 (x) \equiv
\left( \begin{array}{ccc} \frac{\displaystyle a_1^0}{\displaystyle\sqrt 2}
\, + \, \frac{\displaystyle(f_1)_8}{\displaystyle\sqrt 6}
 & a_1^+ & K_1^{+} \\ a_1^- & - \frac{\displaystyle a_1^0}{\displaystyle\sqrt 2} \,
+ \, \frac{\displaystyle(f_1)_8} {\displaystyle\sqrt 6}  & K_1^{0} \\ K_1^{-} &
\overline {K_1^{0}} & - \frac{\displaystyle 2 \, (f_1)_8}{\displaystyle\sqrt 6}
\end{array} \right)^\mu \, ,\end{array}$$

represents the SU(3)$_V$ octet of spin-parity $1^+$-particles. The vector field matrix $V_1(x)$:

$$\label{w1} \begin{array}{c}
V_1 (x) \equiv \frac{\displaystyle\omega_1}{\displaystyle\sqrt 3} \,
\mbox{\LARGE\bf 1} \, ,\end{array}$$

represents the SU(3)$_V$ singlet of spin-parity $1^-$-particles and the axial-vector field matrix $A_1(x)$ represents the corresponding SU(3)$_V$ singlet of spin-parity $1^+$-particles.

The vector and axial-vector field strength tensors are defined as follows

$$\label{39}
V_{\mu\nu}=d_{\mu}V_{\nu}-d_{\nu}V_{\mu}
\hspace*{2cm} {\hbox{and}}\hspace*{2cm}
A_{\mu\nu}=d_{\mu}A_{\nu}-d_{\nu}A_{\mu}\;.$$

Here, the covariant derivative $d_\mu$ acts on the octet multiplets denoted by $R_8$ as follows

$$\label{36}
d_{\mu}R_8 = \partial_{\mu}R_8 + [\Gamma_{\mu},R_8]$$

and trivially on the singlets. The connection $\Gamma_\mu$ is given by

$$\label{37}
\Gamma_{\mu} = {1 \over 2}\, \left\{ \xi^{\dagger}
\, \left[ \partial_{\mu} - i (v_{\mu}+a_{\mu}) \right]
\, \xi + \xi\, \left[ \partial_{\mu} - i (v_{\mu}-a_{\mu})
\right] \, \xi^{\dagger} \right\} \, .$$

The axial-vector field matrix $\xi_\mu$ is defined by

$$\label{41}
\xi_{\mu} = i\, \left\{ \xi^{\dagger} \, \left[ \partial_{\mu}
- i (v_{\mu}+a_{\mu}) \right] \, \xi - \xi \, \left[
\partial_{\mu} - i (v_{\mu}-a_{\mu}) \right] \,
\xi^{\dagger} \right\} = i\, \xi^{\dagger} D_{\mu} U
\xi^{\dagger} = \xi_{\mu}^{\dagger} \,.$$

Finally, in Eqs. ([\[47\]](#47){reference-type="ref" reference="47"}) and ([\[48\]](#48){reference-type="ref" reference="48"}), we have also introduced the following objects

$$\label{43}
\chi_{(\pm)} = \xi^{\dagger}\chi\xi^{\dagger} \pm \xi\chi^{\dagger}
\xi \, ,$$

and

$$\label{44}
f^{\mu\nu}_{(\pm)} = \xi F_L^{\mu \nu} \xi^{\dagger} \pm
\xi^{\dagger} F_R^{\mu \nu} \xi\,,$$

with $F_L^{\mu \nu}$ and $F_R^{\mu \nu}$ the external field-strength tensors

$$\label{28}
F_L^{\mu \nu} = \partial^{\mu} l^{\nu} - \partial^{\nu} l^{\mu}
- i \, [l^{\mu}, l^{\nu}] \, ,$$

$$\label{29}
F_R^{\mu \nu} = \partial^{\mu} r^{\nu} - \partial^{\nu} r^{\mu}
- i \, [r^{\mu},r^{\nu}]$$

associated with the external left ($l_{\mu}$) and right ($r_{\mu}$) field sources

$$\label{30}
l_{\mu} = v_{\mu} - a_{\mu}{\,\,\,},\;\;\;r_{\mu} =
v_{\mu} + a_{\mu}\, .$$

In this paper, we are also interested in couplings of vector and axial-vector quadratic in the spin-1 fields. The complete set of these quadratic interaction terms for vector meson fields, to lowest chiral ${\cal O} (p^2)$, is

$$\label{49} \matrix{
{\cal L}_{VV}^{(2)} = &
\frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(1)}_V \, \hbox{tr}\left(\left[ \xi_\mu, \xi_\nu \right]
\left[ V^\mu, V^\nu \right] \right) \, + \,
\frac{\displaystyle 1}{\displaystyle 2} \,\delta^{(2)}_V \,
\hbox{tr}\left( \left[ V_\mu, \xi_\nu \right] \left[ V^\nu,
\xi^\mu \right] \right)
\hfill \cr\cr \hphantom{{\cal L}_V^{(2)} =}& + \,
\frac{\displaystyle 1}{\displaystyle 2} \, \delta^{(3)}_V \, \hbox{tr}\left( \left[
V_\mu, \xi^\mu \right] \left[ V_\nu, \xi^\nu \right] \right)
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(4)}_V \, \hbox{tr}\left( V^\mu V^\nu \xi_\mu \xi_\nu \right)
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(5)}_V \, \hbox{tr}\left( V^\mu V_\mu \xi^\nu \xi_\nu \right)
\hfill \cr\cr \hphantom{{\cal L}_V^{(2)} =}&
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(6)}_V \, \hbox{tr}\left( V^\mu \xi^\nu V_\mu \xi_\nu \right)
\, + \,\frac{\displaystyle 1}{\displaystyle 2} \,
i\, \phi_V \, \hbox{tr}\left( V_\mu \left[ V_\nu , f_{(+)}^{\mu \nu}
\right] \right) \hfill \cr\cr \hphantom{{\cal L}_V^{(2)} =}&
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\sigma_V \, \epsilon_{\mu \nu \alpha \beta}
\, \hbox{tr}\left( V^\mu \left\{ \xi^\nu, V^{\alpha \beta} \right\}
\right) \,. \hfill \cr\cr}$$

The corresponding interaction terms for axial-vector meson fields are

$$\label{50} \matrix{
{\cal L}_{AA}^{(2)} = &
\frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(1)}_A \, \hbox{tr}\left(\left[ \xi_\mu, \xi_\nu \right]
\left[ A^\mu, A^\nu \right] \right) + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(2)}_A \,
\hbox{tr}\left( \left[ A_\mu, \xi_\nu \right] \left[ A^\nu,
\xi^\mu \right] \right)
\hfill \cr\cr \hphantom{{\cal L}_V^{(2)} =}&
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(3)}_A \, \hbox{tr}\left( \left[ A_\mu, \xi^\mu \right]
\left[ A_\nu, \xi^\nu \right] \right)
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(4)}_A \, \hbox{tr}\left( A^\mu A^\nu \xi_\mu \xi_\nu \right)
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(5)}_A \, \hbox{tr}\left( A^\mu A_\mu \xi^\nu \xi_\nu \right)
\hfill \cr\cr \hphantom{{\cal L}_V^{(2)} =}&
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\delta^{(6)}_A \, \hbox{tr}\left( A^\mu \xi^\nu A_\mu \xi_\nu \right)
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,i\,
\phi_A \, \hbox{tr}\left( A_\mu \left[ A_\nu , f_{(+)}^{\mu \nu}
\right] \right) \hfill\cr\cr \hphantom{{\cal L}_A^{(2)} =}&
\, + \, \frac{\displaystyle 1}{\displaystyle 2} \,
\sigma_A \, \epsilon_{\mu \nu \alpha \beta}
\, \hbox{tr}\left( A^\mu \left\{ \xi^\nu, A^{\alpha \beta} \right\} \right)
\,. \hfill \cr }$$

At ${\cal O} (p^2)$ there are also terms which mix axial-vector and vector fields. The corresponding interaction Lagrangian has the following form,

$$\label{51} \matrix{
{\cal L}_{VA}^{(2)} =&
i \, A^{(1)} \, \hbox{tr}\left( V_\mu \left[ A_\nu , f_{(-)}^{\mu \nu}
\right] \right) \, + \, i \, A^{(2)} \, \hbox{tr}\left( V_\mu
\left[\xi_\nu, A^{\mu \nu} \right] \right) \, + \, i \, A^{(3)} \, \hbox{tr}
\left( A_\mu \left[ \xi_\nu, V^{\mu \nu} \right] \right)
\hfill\cr\cr \hphantom{{\cal L}_{VA}^{(2)} =}&
\, + \, B \, \hbox{tr}\left( V_\mu \left[ A^\mu, \chi_{(-)} \right]
\right) \, + \, H \, \epsilon_{\mu \nu \alpha \beta} \, \hbox{tr}
\left( V^\mu \left\{ A^\nu , f^{\alpha \beta}_{(+)} \right\} \right)
\hfill\cr\cr \hphantom{{\cal L}_{VA}^{(2)} =}&
\, + \, i \, Z^{(1)} \, \epsilon_{\mu \nu \alpha \beta} \, \hbox{tr}\left(
\xi^\mu \xi^\nu \left\{ A^\alpha, V^\beta \right\} \right) \,
+ i \, Z^{(2)} \, \epsilon_{\mu \nu \alpha \beta} \, \hbox{tr}\left(
\xi^\mu A^\nu \xi^\alpha V^\beta \right) \,. \hfill \cr}$$

In the present work we shall concentrate on processes involving spin-1 particles and we shall not consider possible spin-1 particle decays to scalar particles. Whenever scalar particles can contribute as intermediate resonances to these transitions, in particular for $a_1$-decays, we cannot integrate them out since their masses are lower than those of the axial-vector particles and they have to be taken into account as propagating particles described by the corresponding Lagrangian. The effective Lagrangian for scalar particles that may contribute to the transitions we are interested in is of chiral ${\cal O}
(p^2)$. To this order, the most general Lagrangian for $0^+$-particles involving at most one scalar and two spin-1 fields is

$$\label{52} \matrix{
{\cal L}_{S} =& \frac{\displaystyle 1}{\displaystyle 2} \,
\hbox{tr}\left( d_\mu S \, d^\mu S
\,-\,M_S^2 \, S^2 \right)
\,+\,c_m \, \hbox{tr}\left(S\, \chi^+
\right)\,+\,c_d\,\hbox{tr}\left(S\xi^\mu\xi_\mu\right)\hfill\cr\cr
\hphantom{{\cal L}_{S} =} &
+\,C^{(1)}\,\hbox{tr}\left(S\left\{A_\mu,\xi^\mu\right\}\right)\,+\,
\frac{\displaystyle 1}{\displaystyle 2}\,C^{(2)}\,\hbox{tr}\left(S A^\mu A_\mu\right)
\,+\,\frac{\displaystyle 1}{\displaystyle 2}\,D\,\hbox{tr}\left(S V^\mu V_\mu\right)
 \,. \hfill \cr}$$

Here, the 3 $\times$ 3 field matrix $S$ represents the SU(3)$_V$ nonet of scalar fields. The chiral ${\cal O}(p^2)$ couplings $c_m$ and $c_d$ in the ENJL cut-off model have been calculated in Ref. [@bbr].

# The ENJL cut-off model of QCD {#2}

Reference [@bbr] gives a systematic study of the low-energy effective action of the extended Nambu--Jona-Lasinio model which, at intermediate energies below or of the order of a cut-off scale $\Lambda_\chi$, is expected to be a good effective realization of the standard QCD Lagrangian ${\cal L}_{\rm QCD}$. Here we give a brief summary of the results found there. The Lagrangian in question is

$$\label{qcd} \begin{array}{c}
{\cal L}_{\rm QCD} \rightarrow
{\cal L}^{\Lambda_\chi}_{\rm QCD} \, + \,
{\cal L}^{\rm S,P}_{\rm NJL}
\, + \, {\cal L}^{\rm V,A}_{\rm NJL} \, + \, {\cal O} \,
\left( \frac{\displaystyle 1} {\displaystyle\Lambda^4_\chi} \right)\,, \cr \cr
{\rm with} \hspace*{0.5cm} {\cal L}^{\rm S,P}_{{\rm NJL}}
\, =\,
\frac{\displaystyle 8 \pi^2 \, G_{\rm S} (\Lambda_\chi)}
{\displaystyle N_c \, \Lambda_\chi^2} \, {\displaystyle\sum_{i, j}}
\, (\bar q^i_R q^j_L)(\bar q^j_L q^i_R)
\cr \cr
{\rm and} \hfill \cr \cr {\cal L}^{\rm V,A}_{{\rm NJL}}
\, =\,
-\, \frac{\displaystyle 8 \pi^2 \, G_{\rm V} (\Lambda_\chi)}
{\displaystyle N_c \, \Lambda_\chi^2} \, {\displaystyle\sum_{i, j}}
\, \left[ (\bar q^i_L \gamma^\mu q^j_L)
(\bar q^j_L \gamma_\mu q^i_L)
\, + \, (L \to R) \right] .
\end{array}$$

Where $i, j$ are flavour indices and $\Psi^L_R \equiv
\frac{\displaystyle 1}{\displaystyle 2} \, (1 \pm \gamma_5) \, \Psi$. The couplings $G_{\rm S}$ and $G_{\rm V}$ are dimensionless and ${\cal O} (1)$ in the $1/N_c$-expansion. In the mean-field approximation, these ${\cal L}^{\rm S,P,V,A}_{\rm NJL}$ above are equivalent to the constituent chiral quark-mass term [@ert]:

$$\label{chb} \begin{array}{c}- \, M_Q (\bar q_R \, U \,
q_L \, + \, \bar q_L \, U^\dagger \, q_R ) \, . \end{array}$$

In the presence of this term it is useful to introduce new quark fields $Q_L$ and $Q_R$, which we call "rotated basis", or constituent, chiral-quarks [@mg], defined as follows

$$\label{rotbas} \begin{array}{cc}
Q_L \, = \, \xi \, q_L \, ;& \overline Q_L \, = \, \bar
q_L \, \xi^\dagger \, ;\\ Q_R \, = \, \xi^\dagger \,
 q_R \, ;& \overline  Q_R \, = \, \bar q_R \, \xi \, .
\end{array}$$

In the rest of this Section we shall work in Euclidean space for convenience, and we shall adopt the conventions given in Ref. [@bbr]. The effective action, in the presence of external sources $l_\mu$ and $r_\mu$ and light-quark-mass matrix ${\cal M}$, can be written as [@bbr]

$$\label{53} \matrix{
e^{\Gamma_{\rm eff} \left(H, \xi, W_\mu^{\pm}; l_\mu,
r_\mu, {\cal M}\right)} \,=\, \hfill \cr\cr
\exp \left( -\, {\displaystyle\int} \, {\rm d}^4 x \,
\left\{ \frac{\displaystyle N_c \Lambda_\chi^2}{\displaystyle 8 \pi^2
 G_S (\Lambda_\chi)} \, \hbox{tr}\, H^2 \,+\,
\frac{\displaystyle N_c \Lambda_\chi^2}{\displaystyle 64 \pi^2 G_V
(\Lambda_\chi)} \, \hbox{tr}\left( W_\mu^+ W_\mu^+ \,+\,
W_\mu^- W_\mu^- \right) \right\} \right) \hfill \cr\cr
\hspace*{7cm} \times \, \frac{\displaystyle 1}{\displaystyle Z} \,
{\displaystyle\int} \left[ {\cal D} \, G_\mu \right] \, \exp
\Gamma_E \left( {\cal A}_\mu, M \right)
\,, \hfill \cr \cr }$$

where $W_\mu^\pm(x)$ and $H(x)$ are 3 $\times$ 3 auxiliary Hermitian field matrices which under the chiral group transform as

$$\label{54} \matrix{
W_\mu^\pm \to h (\Phi,g_{L,R})
\, W_\mu^\pm \, h^{\dagger} (\Phi,g_{L,R})
\,, \hfill \cr\cr
H \to h (\Phi,g_{L,R}) \, H \, h^\dagger (\Phi,g_{L,R})
\, , \hfill \cr\cr}$$

where $h(\Phi,g_{L,R})\equiv h$ is the compensating SU(3)$_V$ transformation which appears under the action of the chiral group $G\equiv$ SU(3)$_L$ $\times$ SU(3)$_R$ on the coset representative $\xi(\Phi)$ of the $G$/SU(3)$_V$ manifold, *i.e.*

$$\label{31}
\xi(\Phi) \to g_R \, \xi(\Phi) \, h^{\dagger}
\, = \, h \, \xi(\Phi) \, g_L^{\dagger}\;,$$

where $\xi(\Phi) \xi(\Phi) \,= \,U$ in the chosen gauge. In the mean-field approximation these field matrices are replaced by

$$\label{mean} \matrix{
H \Rightarrow M_Q\,\mbox{\LARGE \bf 1}\,,\hfill\cr\cr
W^\pm_\mu \Rightarrow 0\,. \hfill\cr\cr}$$

In Eq. ([\[53\]](#53){reference-type="ref" reference="53"}) we have used the short-hand notation

$$\left[ {\cal D} \, G_\mu \right] \equiv
{\cal D} \, G_\mu \, \exp \left(
-\, \frac{\displaystyle 1}{\displaystyle 4} \,
{\displaystyle\sum^{N_c^2-1}_{a=1}} \, G_{\rho \nu}^{(a)}
G_{\rho \nu}^{(a)} \right) \,$$

with $G^{(a)}_{\mu \nu}$ the gluon field strength tensor and

$$\label{effqcd} \begin{array}{c}
\exp \Gamma_E \, ({\cal A}_\mu, M) \, =\,
{\displaystyle\int} \, {\cal D} \, \overline Q \,
{\cal D} \, Q \, \exp {\displaystyle\int} \, {\rm d}^4 x
\, \overline Q D_E Q \, = \, {\rm det} \, D_E\,
\end{array}$$

where $D_E$ is the Euclidean Dirac operator

$$\label{dirac} \renewcommand{\arraystretch}{1.5}
\begin{array}{c}D_E \, = \, \gamma_\mu \nabla_\mu \, + \, M
\, = \, \gamma_\mu (\partial_\mu
\, + \, {\cal A}_\mu) \, + \, M
\end{array}\renewcommand{\arraystretch}{1}$$

with

$$\label{dcov} \matrix{
{\cal A}_\mu \, = \, i \, G_\mu \, + \, \Gamma_\mu \,
- \frac{\displaystyle i}{\displaystyle 2} \gamma_5 \,\left( \xi_\mu
\,-\, W_\mu^{-} \right) \,-\, \frac{\displaystyle i}{\displaystyle 2}
\, W^+_\mu \, ; \hfill \cr\cr
M \, = \,-\, H \,-\,
\frac{\displaystyle 1}{\displaystyle 2} \, \left( \Sigma \,-\, \gamma_5 \,
\Delta \right) \, \hfill \cr\cr }$$

and

$$\label{masa} \matrix{
\Sigma \,=\, \xi^\dagger \, {\cal M} \,\xi^\dagger \,+\,
\xi \, {\cal M}^\dagger \, \xi ; \hfill \cr\cr
\Delta \,=\, \xi^\dagger \, {\cal M}\, \xi^\dagger \,-\,
\xi \, {\cal M}^\dagger \, \xi \,. \hfill \cr\cr
}$$

In Eq. ([\[dcov\]](#dcov){reference-type="ref" reference="dcov"}) $G_\mu$ is the gluon field matrix in the fundamental SU($N_c$) representation and the connection $\Gamma_\mu$ and axial-vector field $\xi_\mu$ are given in Eqs. ([\[37\]](#37){reference-type="ref" reference="37"}) and ([\[41\]](#41){reference-type="ref" reference="41"}). In our calculation of the fermionic determinant we shall disregard the gluonic corrections due to fluctuations below the cut-off scale $\Lambda_\chi$ and shall consider a model that is more like the first alternative envisaged in Ref. [@bbr], where the formal integration over gluon fields has been done in the path-integral of the generating functional for Green functions. Our choice here is motivated by the fact that the results obtained within this alternative in Ref. [@bbr] for the couplings of the low-energy chiral Lagrangian to ${\cal O} (p^4)$ are not qualitatively different from those obtained in the same Reference when the effect of long-distance gluonic interactions was taken into account.

In Ref. [@bbr] it was pointed out that the effective action in Eq. ([\[53\]](#53){reference-type="ref" reference="53"}) obeys the following formal symmetry: the effective action $\Gamma_E ({\cal A}_\mu, M)$ with ${\cal A}_\mu$ and $M$ given in Eq. ([\[dcov\]](#dcov){reference-type="ref" reference="dcov"}) can be written formally as the mean-field approximation expression corresponding to external sources $l_\mu$ and $r_\mu$ and light-quark-mass matrix ${\cal M}$ redefined as follows,

$$\label{92} \matrix{
l_\mu \to l'_\mu \, = \, l_\mu \, + \,\frac{\displaystyle 1}{\displaystyle 2}
\, \xi^\dagger
\left( W_\mu^+ \,+\, W_\mu^- \right) \xi\,, \hfill \cr\cr
r_\mu \to r'_\mu \, = \, r_\mu \, + \, \frac{\displaystyle 1}{\displaystyle 2}
\, \xi \left( W_\mu^+ \,-\, W_\mu^- \right) \xi^\dagger\,,
\hfill\cr\cr
{\cal M} \to {\cal M}'\,=\, {\cal M}\,+\, \xi\, \sigma
\, \xi\,. \hfill \cr\cr }$$

Here,

$$\sigma \equiv H \,-\, M_Q \,
\mbox{\LARGE \bf 1}$$

is a $0^+$-field matrix. We shall use this formal symmetry in the following Sections.

Once the quarks and gluons in the effective action in Eq. ([\[53\]](#53){reference-type="ref" reference="53"}) are integrated out (see Ref. [@bbr]), one can get the correct kinetic term for spin-1 particles after two steps. The first one is the diagonalization of the quadratic form in $\xi_\mu$ and $W_\mu^{(-)}$ that defines the constant $g_A$, *i.e.*

$$\label{ga}
W_\mu^{(-)} \to \widehat W_\mu^{(-)} \, + \,
(1 \, - \, g_A) \, \xi_\mu .$$

The second one is a scale redefinition of the fields $W_\mu^{(+)}$ and $\widehat W_\mu^{(-)}$, *i.e.*

$$\label{scale}
V_\mu \, = \, \frac{\displaystyle f_V}{\displaystyle\sqrt 2} \, W_\mu^{(+)}\,,
\hspace*{1cm} A_\mu \, = \, \frac{\displaystyle f_A}{\displaystyle g_A \, \sqrt 2}
 \, \widehat W_\mu^{(-)}$$

that introduces the physical vector and axial-vector fields $V_\mu$ and $A_\mu$. All the couplings of the low-energy effective action can then be obtained as functions of three parameters only, $g_A$, $M_Q$ and $\Lambda_\chi$. The ${\cal O}(p^3)$ couplings $f_V$, $g_V$ and $f_A$ have been already calculated in Ref. [@bbr] with the results to leading ${\cal O}(N_c)$,

$$\label{fvc} \matrix{
f_V^2 \, = \, \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle 2}{\displaystyle 3} \, \Gamma (0,x)\,, \hspace*{2cm}
f_A^2 \, = \, \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle 2 \, g_A^2}{\displaystyle 3} \left[ \Gamma (0,x) \, - \,
\Gamma(1,x) \right]\, , \hfill \cr \cr
g_V \, = \, \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \, \frac{\displaystyle 1}{\displaystyle
3 \, f_V} \, \left[ (1 - g_A^2) \, \Gamma(0,x) \, + \, 2 \, g_A^2
\, \Gamma(1,x) \right] \,.\hfill\cr\cr }$$

Here,

$$\label{xd}
x \, = \, \frac{\displaystyle M_Q^2}{\displaystyle\Lambda_\chi^2}$$

and the function $\Gamma(n,x)$ is the incomplete Gamma function

$$\label{gamma} \matrix{
\Gamma(n,x) \, = \, {\displaystyle\int^\infty_x}
\frac{\displaystyle{\rm d} z}{\displaystyle z} \, e^{-z} \, z^n
 , \hspace*{1cm}  n \, = \, 0, \, 1, \ldots
\hfill \cr\cr }$$

The correct kinetic term for $0^+$-particles is obtained after a scale redefinition of the $\sigma$ field in Eq. ([\[92\]](#92){reference-type="ref" reference="92"}), *i.e.*

$$\label{scal} \matrix{
S \,=\, \lambda_S \, \sigma \hfill\cr\cr}$$

that introduces the physical $0^+$-field $S$. The constant $\lambda_S$ was calculated in this model in Ref. [@bbr],

$$\label{lambdas} \matrix{
\lambda_S^2\,=\,\frac{\displaystyle N_c}{\displaystyle 16 \pi^2}\,
\frac{\displaystyle 2}{\displaystyle 3} \, \left[3\, \Gamma(0,x)\,-\,
2\, \Gamma(1,x)\right]\,. \hfill\cr\cr}$$

In the present work we want to calculate the rest of the ${\cal O}
(p^3)$ couplings in the Lagrangians in Eqs. ([\[47\]](#47){reference-type="ref" reference="47"}), ([\[48\]](#48){reference-type="ref" reference="48"}) and ([\[52\]](#52){reference-type="ref" reference="52"}) as well as the ${\cal O} (p^2)$ couplings of the interaction Lagrangians in Eqs. ([\[49\]](#49){reference-type="ref" reference="49"}), ([\[50\]](#50){reference-type="ref" reference="50"}) and ([\[51\]](#51){reference-type="ref" reference="51"}). We shall later study some of the phenomenological applications of our results. We first consider the terms that carry a Levi-Civita pseudotensor, *i.e.* the abnormal intrinsic parity terms [@bij2].
