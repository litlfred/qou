---
doc_id: arxiv-hep-ph-9511320v1
doc_title: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields"
section_id: sec-002-21-addition-of-spin--1-fields-tensor-field-formu
section_title: "Addition of Spin--1 Fields: Tensor Field Formulation"
section_number: 2.1
pages: 6-8
source_pdf: 9511320v1.pdf
source_sha256: 4336112cecabdfdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.995
doc_brief: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields — We analyze the eﬀective low–energy ﬁeld theory of Goldstone bosons and baryons chirally coupled to massive spin–1 ﬁelds."
---
First, let us discuss the chiral couplings of spin--1 fields to the Goldstone bosons in the tensor field formulation. We use the notation of Refs.[@reso; @reso1] and only write down the necessary definitions for our extension to include baryons. Representing massive spin--1 fields by an antisymmetric tensor is quite common in e.g. supergravity theories. One of the main advantages in the hadron sector is that there is no mixing between axials and pseudoscalars in such an approach. Our basic object is the antisymmetric tensor field $W_{\mu \nu}$ (which is a generic symbol for any vector or axial--vector), $$W_{\mu \nu} = - W_{\nu \mu} \, \, \, .
\label{defwmunu}$$ This tensor has six degress of freedom. Freezing out the three fields $W^{ij}$, one reduces this number to three as necessary for massive spin--1 fields. The free Lagrangian takes the form [@reso] $${\cal L}_0 = - \frac{1}{2} \partial^\mu W_{\mu \nu}^a \, \partial_\rho
W^{\rho \nu, a} + \frac{1}{4} M_V^2 \, W_{\mu \nu}^a W^{\mu \nu , a}
\, \, \, \, ,
\label{ltfree}$$ with $M_V$ the average mass of the spin--1 octet (in the chiral limit) and the flavor index $a$ runs from 1 to 8.. For non-linearly realized chiral symmetry, $W_{\mu \nu}$ transforms as any matter field under the chiral group ${\cal G}$, $$W_{\mu \nu} \to h(\phi,g) \, W_{\mu \nu} \, h(\phi,g)^{-1} \, \, \, .
\label{ccwzw}$$ We point out that other spin--1 field representations like e.g. massive Yang--Mills fields, have more complicated transformation properties, see e.g. [@ulfpr; @reso1]. Without any assumptions about the nature of the massive vectors or axials, chiral symmetry leads to Eq.([\[ccwzw\]](#ccwzw){reference-type="ref" reference="ccwzw"}). From the Lagrangian, Eq.([\[ltfree\]](#ltfree){reference-type="ref" reference="ltfree"}), one easily constructs the propagator, $$\begin{aligned}
& & G_{\mu \nu , \rho \sigma} (x,y) \, \, \, = \, \, \,
< 0 | T \{ W_{\mu \nu} (x) \, , W_{\rho \sigma} (y) \} |0> \, = \nonumber \\
& = &\frac{i}{M_V^2} \, \int \frac{d^4k}{(2\pi)^4} \,
\frac{e^{i \, k \cdot (x-y)}}{M_V^2 -k^2 - i\epsilon} \,
\bigl[ g_{\mu
  \rho} g_{\nu \sigma} (M_V^2 - k^2) + g_{\mu \rho} k_\nu k_\sigma -
g_{\mu \sigma} k_\nu k_\rho \nonumber \\
& & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad
- (\mu \leftrightarrow \nu) \, \bigr]
 \, \, \, .
\label{propw}
\end{aligned}$$ The lowest order interaction Lagrangian with Goldstones and external vector and axial--vector sources is given by $${\cal L}_{\rm int} = \frac{1}{2\sqrt{2}} \, \biggl( F_V \, {\rm Tr} (
W_{\mu \nu} \, f_+^{\mu \nu} ) + i G_V \, {\rm Tr} (W_{\mu \nu} \, [
u^\mu , u^\nu] ) \biggr)
\, \, \, ,
\label{ltint}$$ with $$f_+^{\mu \nu}  = u F_L^{\mu \nu} u^\dagger + u^\dagger F_R^{\mu \nu} u
\, \, , \, \, u_\mu = i u^\dagger \nabla_\mu U u^\dagger = u_\mu^\dagger
\, \, \, ,
\label{fmnu}$$ where $F_L^{\mu \nu}$ ($F_R^{\mu \nu}$) are the field strengths associated to $v_\mu +a _\mu$ ($v_\mu - a _\mu$) and $\nabla_\mu$ is the chiral covariant derivative acting on the Goldstone bosons. The two real constants $F_V$ and $G_V$ are not fixed by chiral symmetry. Their numerical values are $F_V = 154 \,$MeV and $G_V = 69
\,$MeV inferred from $\Gamma (\rho^0 \to e^+ e^-)$ and $\Gamma (\rho \to \pi \pi)$, in order [@reso]. These are all the ingredients we need from the mesonic sector. For more details, see Refs.[@reso; @reso1].

We now turn to the inclusion of baryons, i.e. the construction of the lowest order $B\phi W$ couplings. For the resonance exchange processes to be discussed here, it sufficient to list all terms to order ${\cal O}(q)$. From these, we can construct all Feynman graphs to ${\cal O}(q^3)$ since we have at least two pions (two $u_\mu$'s of order $q$) or one field strength tensor of order $q^2$ attached to the propagating spin--1 field (which also couples to the baryons). Imposing chiral symmetry, $P$, $C$ and $T$, hermiticity and so on, one finds (some details are given in Appendix A) $$\begin{aligned}
{\cal L}_{B\phi W}^{(1)}
& = & R_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \sigma^{\mu \nu} \, (
W_{\mu \nu} \, , \, B) \, \bigr] \nonumber \\
& + & S_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \gamma^\mu \, ( [D^\nu,
W_{\mu \nu}]\, , \, B) \, \bigr] \nonumber \\
& + & T_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \gamma^\mu \, ( [D_\lambda,
W_{\mu \nu}]\, , \, [D^\lambda ,[D^\nu , B]] \, ) \, \bigr]
\nonumber \\
& + & U_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \sigma^{\lambda \nu} \, (
W_{\mu \nu} \, , \, [ D_\lambda , [ D^\mu , B]] \, ) \, \bigr]
\, \, \, ,
\label{Pit}
\end{aligned}$$ where we have introduced a compact notation. The symbol $(A,B)$ denotes either the commutator, $(A,B) = [A,B]$, or the anticommutator, $(A,B) = \{A,B\}$. In the first case, the coupling constant has the subscript $'F'$, in the second one the subscript $'D'$ applies. To be specific, the first term in Eq.([\[Pit\]](#Pit){reference-type="ref" reference="Pit"}) thus means $$R_D \, {\rm Tr} \bigl[ \bar{B} \, \sigma^{\mu \nu} \, \{
W_{\mu \nu} \, , \, B \} \, \bigr] +
R_F \, {\rm Tr} \bigl[ \bar{B} \, \sigma^{\mu \nu} \, [
W_{\mu \nu} \, , \, B ] \, \bigr] \, \, \, .
\label{Pitex}$$ The real constants $(R,S,T,U)_{D/F}$ are not fixed by chiral symmetry, their numerical values will be discussed later. At this stage, we only assume that they are non--vanishing. From this Lagrangian, we can immediately construct the effective action for single spin--1 meson exchange (we specialize here to the vectors without any loss of generality) $$\begin{aligned}
S_{\rm eff} &  = & i  \int  d^4x  d^4y
  \biggl\{ R_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \, \sigma^{\rho \sigma} \,
G_{\mu \nu , \rho \sigma} (x,y) \, ( \, J^{\mu \nu} (x) \, , \, B(y)
\, ) \biggr] \nonumber \\
& + &  S_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \, \gamma^\rho \,
\partial^\sigma_y G_{\mu \nu , \rho \sigma} (x,y) \, ( \, J^{\mu \nu}
(x) \, , \, B(y) \, ) \biggr] \nonumber \\
& + & T_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \, \gamma^\rho \,
\partial_{y,\lambda} G_{\mu \nu , \rho \sigma} (x,y) \, ( \, J^{\mu \nu}
(x) \, , \, [ D^\lambda , [D^\sigma ,B(y)]] \, ) \biggr] \nonumber \\
&  + & U_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \, \sigma^{\lambda \sigma} \,
G_{\mu \nu , \rho \sigma} (x,y) \, ( \, J^{\mu \nu} (x) \, , \,
[D_\lambda , [ D^\rho , B(y) ]] \, ) \biggr] \biggr\} \, \, \, ,
\nonumber \\ & &
\label{sefft}
\end{aligned}$$ where the antisymmetric currents $J^{\mu \nu}= -J^{\nu \mu}$ are defined via $$J^{\mu \nu} = \frac{1}{2 \sqrt{2} } \, \biggl( F_V \,
f_+^{\mu \nu} + i \, G_V \, [u^\mu , u^\nu] \, \biggr) \,
\, \, . \label{Jt}$$ The currents $J^{\mu \nu}$ obviously are of chiral dimension two. With the effective action Eq.([\[sefft\]](#sefft){reference-type="ref" reference="sefft"}) at hand, we are now in the position of calculating the desired matrix--elements involving single vector meson exchange contributions to e.g. the nucleon electromagnetic form factors or elastic pion--nucleon scattering (in the tensor field formulation). Notice that for these processes it is sufficient to keep the partial derivatives acting on the $G_{\mu \nu , \rho \sigma}$ in Eq.([\[sefft\]](#sefft){reference-type="ref" reference="sefft"}) and not the chiral covariant ones. The generalization is obvious and not treated here.
