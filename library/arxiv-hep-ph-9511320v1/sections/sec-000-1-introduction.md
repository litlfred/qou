---
doc_id: arxiv-hep-ph-9511320v1
doc_title: "arXiv:hep-ph/9511320v1 15 Nov 1995"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-12
source_pdf: 9511320v1.pdf
source_sha256: 4336112cecabdfdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.978
---
Over the last years, there has been considerable activity in the formulation of effective chiral Lagrangians including baryons, see e.g. [@gss; @jm; @dobo; @bkkm] or the recent review [@bkmrev]. Beyond leading order, such effective Lagrangians contain coefficients not fixed by symmetry, the so--called low--energy constants (LECs) [@wein79; @gl84]. In general, these LECs should be determined from phenomenology. However, in the baryon sector, there do not yet exist sufficiently many accurate data which allow to independently determine all these LECs. That is quite different from the meson sector. There, Gasser and Leutwyler [@gl84; @gl85] performed a systematic study of S-matrix and transition current matrix elements to pin down the LECs. It was already argued in Ref.[@gl84] that the numerical values of certain LECs can be understood to a high degree of accuracy from vector meson exchange. This picture was later sharpened by Ecker et al. [@reso; @reso1] who showed that *all* of the mesonic LECs are indeed saturated by resonance exchange of vector, axial--vector, scalar and pseudoscalar type (some of these aspects were also discussed in [@reso2]). However, there is a potential problem related to the massive spin--1 fields. In Ref.[@reso], an antisymmetric tensor field formulation well--known in supergravity was used to represent these degrees of freedom. One could, however, choose as well a more conventional vector field approach (for a review, see [@ulfpr]). At first sight, these two formulations lead to very different results, like e.g. the pion radius is zero and non-vanishing for the vector and tensor field formulation, respectively. In Ref.[@reso1], high energy constraints were used to show that there are local terms at next--to--leading order in the vector field approach which lead to a full equivalence between the two schemes, as intuitively expected. A path integral approach, which gives a formal transformation between the two representations, has also been given recently [@bp] (we give some clarification in appendix B).

In the baryon sector, the situation is in a much less satisfactory state. Only recently, the renormalization of all divergences at order $q^3$ (where $q$ denotes a small momentum or meson mass) has been performed [@eckerr] and all finite terms at that order have been enumerated [@eckmoj] (in the heavy baryon formalism and for two flavors). Previously, Krause [@krause] had listed all terms up--to--and--including ${\cal O}(q^3)$ in three-flavor relativistic baryon CHPT. The best studied baryon chiral perturbation theory LECs are the ones related to the dimension two Goldstone boson ($\phi$)--baryon ($B$) Lagrangian ${\cal L}_{\phi B}^{(2)}$ for the two flavor case, see e.g. [@bkmrev; @bkmpin; @bkmppn]. These can be understood from resonance exchange saturation as detailed in [@ulfmit], but not to the same degree of accuracy as it is the case in the meson sector. The concept of resonance exchange saturation of the low--energy constants is more complicated when baryons are present. One does not only have to consider $s$--channel baryon excitations (like the $\Delta (1232)$,[^1] the $N^* (1440)$, and so on) but also $t$--channel meson excitations (like scalars, vectors or axials). Therefore, the problem of how to couple the spin--1 fields to the baryons arises. This was already mentioned by Gasser et al. [@gss] and further elaborated on in Ref.[@ulfsea]. In the framework of relativistic baryon CHPT, one finds a LEC contributing to the isovector magnetic moment very close to zero, at odds with the expectation of a large $\rho$--meson induced higher dimension operator. It is thus appropriate to address the problem of the equivalence of the vector and tensor field formulation for the spin--1 mesons in the presence of baryons (which are treated relativistically here. Only after calculating the spin--1 field contribution to a certain LEC, one is allowed to take the heavy fermion limit for the baryons). Here, we will show how to couple massive spin--1 mesons to the effective Goldstone boson--baryon Lagrangian consistent with chiral symmetry and demonstrate that physics does not depend on the particular choice of representation for the spin--1 fields.

There is, however, yet another motivation. In many meson--exchange models of the nulcear force, one includes vector meson exchange. The $\rho$--contribution is believed to suppress the pion tensor force at small and intermediate separations whereas the $\omega$ makes up part of the short range repulsion. If chiral symmetry is imposed on such models, one also has a set of local operators involving pions and nucleons, in particular the two--pion--nucleon seagull, the so--called Weinberg term, with a coupling strength $\sim 1/F_\pi^2$ (with $F_\pi =
93$ MeV the pion decay constant). On the other hand, it is well known that treating the $\rho$--meson as a massive Yang--Mills boson, $\rho$--exchange in fact produces the Weinberg term with the right strength, see Fig. 1. There appears to be a double--counting problem. Let us therefore elaborate a bit on this. First, the chiral covariant derivative term acting on the nucleon fields $\Psi$ (for the moment, we restrict ourselves to the two--flavor case of pions and nucleons),

<figure id="fig1">

<figcaption><span id="fig1" label="fig1"></span> The two–pion nucleon seagull (Weinberg term). (a) shows the fundamental Feynman diagram (from the chiral covariant derivative) and (b) represents its generation via <span class="math inline"><em>t</em></span>–channel <span class="math inline"><em>ρ</em></span>–meson exchange. Solid and dashed lines denote the octet baryons and Goldstones, respectively.</figcaption>
</figure>

$${\cal L}_{\phi B} = i \, \bar{\Psi} \, \gamma_\mu D^\mu \, \Psi + \ldots =
i \, \bar{\Psi} \, \gamma_\mu \, (\partial^\mu + \Gamma^\mu ) \, \Psi + \ldots
\label{chicov}$$ with $\Gamma_\mu$ the chiral connection, contains besides many others, the Weinberg term with the Feynman insertion (i.e. the nucleon and pion fields are not shown) $$\frac{1}{4 F_\pi^2} \gamma_\mu (q_1 + q_2)^\mu \, \epsilon^{abc}
\, \tau^c
\label{weinterm}$$ with $q_i$ the pion momenta and '$a,b,c$' are isospin indices. This term leads to a low--energy theorem (LET) for the isovector pion--nucleon scattering amplitude $T^-$ in forward direction, $$\frac{T^-(\nu )}{ \nu } \to \frac{1}{F_\pi^2} \, \, \, ,
\label{let}$$ as $\nu \to 0$ and $\nu = p \cdot q \, / \, m$ the standard momentum transfer variable ($p$ denotes the nucleon momentum). On the other hand, conventional $\rho$--meson exchange with the following insertions $$\rho NN: \, \, \,  -g_{\rho NN} \, \epsilon \cdot \gamma \,\frac{\tau^c}{2}
\, \, , \quad
\rho \pi \pi: \, \, \, g_{\rho \pi \pi} \, i \, \epsilon^{bac} \, \epsilon^\nu
\, (q_1 + q_2)_\nu \, \, \,  ,
\label{rhocoup}$$ where $\epsilon_\nu$ denotes the polarization vector of the spin--1 field, leads to $$\lim_{\nu \to 0} \frac{T^-(\nu )}{ \nu } = 2 \, g_{\rho NN} \,
g_{\rho \pi \pi} \frac{1}{M_\rho^2} = \frac{1}{F_\pi^2} \, \, \, ,
\label{rhowein}$$ using universality ($g_{\rho NN} = g_{\rho \pi \pi} \equiv g$) and the KSFR relation [@kfsr], $M_\rho^2 = 2 g^2 F_\pi^2$, which is fulfilled within a few percent in nature. So now there seem to be two sources to give the low--energy theorem, Eq.([\[let\]](#let){reference-type="ref" reference="let"}).[^2] In what follows, we will show that constructing the couplings of the spin--1 fields to Goldstone bosons and baryons solely based on the non--linear realization of chiral symmetry, $\rho$--exchange does not contribute to the LET but only to some of its higher order corrections. The Weinberg term will thus entirely arise from the nucleon kinetic term, Eq.([\[chicov\]](#chicov){reference-type="ref" reference="chicov"}), i.e. from the chiral covariant derivative acting on the nucleon fields (see also the footnote in ref.[@bkmpin]).

The paper is organized as follows. In section 2, we briefly summarize the effective Goldstone boson--baryon Lagrangian. We discuss in some detail the couplings of massive spin--1 fields in the vector and the tensor field formulation. We also discuss some formal equivalence between these two schemes making use of the Proca equation. In section 3, we calculate the electromagnetic form factors of the ground state baryon octet. This allows to fix the coefficients of the contact terms one has to add to the vector formulation so as to achieve complete equivalence to the tensor one up--to--and--including order $q^3$. In section 4, we return to the question of $\rho$--exchange in pion--nucleon scattering and show that chirally coupled vector mesons do not interfere with the leading order Weinberg term. Some open problems related to higher orders, in particular the effects of pion loops, are addressed in section 5. A short summary is given in section 6. Some technicalities related to the construction of the effective Lagrangian are relegated to appendix A. Appendix B contains some comments on the formal equivalence proof based on dual transformations.

# Effective Lagrangian of Goldstones, Baryons and Spin--1 Fields

To perform the calculations, we make use of the effective Goldstone boson--baryon Lagrangian. Our notation is identical to the one used in [@bkmz] and we compile here only some necessary definitions. Denoting by $\phi$ the pseudoscalar Goldstone fields ($\pi, K, \eta$) and by $B$ the baryon octet ($N,\Lambda,\Sigma,\Xi$), the effective Lagrangian takes the form (to one loop accuracy) $${\cal L}_{\rm eff} = {\cal L}_{\phi B}^{(1)} +  {\cal L}_{\phi B}^{(2)} +
  {\cal L}_{\phi B}^{(3)} +
  {\cal L}_{\phi B}^{(4)} + {\cal L}_{\phi}^{(2)}+ {\cal L}_{\phi}^{(4)}
\label{leff}$$ where the chiral dimension $(i)$ counts the number of derivatives and/or meson mass insertions. At this stage, the baryons are treated relativistically. Only after the resonance saturation of the LECs has been performed, one is allowed to go to the extreme non--relativistic limit [@jm; @bkkm], in which the baryons are characterized by a four--velocity $v_\mu$. In that case, there is a one--to--one correspondence between the expansion in small momenta and quark masses and the expansion in Goldstone boson loops, i.e. a consistent power counting scheme emerges. Denoting by $B_v$ the heavy baryons, the correct order is given by the chain $$\tilde{{\cal L}}_{\rm eff} [U, M , B, B^*] \to
\bar{{\cal L}}_{\rm eff} [U, B] \to {\cal L}_{\rm eff} [U, B_v] \, \, \, ,
\label{chain}$$ i.e. the heavy fermion limit has to be taken at the very end. In Eq.([\[chain\]](#chain){reference-type="ref" reference="chain"}), $M$ denotes the various meson resonances and $B^*$ is a generic symbol for any baryon excitation.

The transformation properties of the Goldstones and the baryons under the chiral group ${\cal G} = SU(3)_L
\times SU(3)_R$ are standard, $$U \to g_L \, U \, g_R^{-1} \, \, , \quad
B \to h(\phi,g) \, B \, h(\phi,g)^{-1}
\label{ccwz}$$ with $(g_L,g_R) \in {\cal G}$ and $h(\phi, g)$ is the so--called compensator field representing an element of the conserved subgroup $SU(3)_V$. We also need the square root of $u(\phi) = \sqrt{U(\phi )}$ with the chiral transformation $$u(\phi ) \to g_L \, u(\phi ) \, h(\phi,g)^{-1} = h(\phi, g)
u(\phi ) g_R^{-1} \,  \, \, .
\label{sqrtu}$$ The form of the lowest order meson--baryon Lagrangian is standard, see e.g. [@bkmz], and the meson Lagrangian is given in [@gl85]. We just need the form of the chiral covariant derivative $D_\mu$, $$D_\mu \, B  = \partial_\mu \, B + [ \Gamma_\mu \, , \, B ]
\equiv [D_\mu \, , \, B] \, \, \, ,
\label{cova1}$$ with the connection $\Gamma_\mu$, $$\Gamma_\mu  = \frac{1}{2} \biggl( u^\dagger [\partial_\mu
-i(v_\mu+a_\mu)]u + u [\partial_\mu-i(v_\mu-a_\mu) ]u^\dagger
\biggr) \, \, \, ,
\label{cova2}$$ and $v_\mu$ and $a_\mu$ are external vector and axial--vector sources. The covariant derivative transforms linearly under ${\cal G}$, $$D_\mu \, B \to h(\phi, g) \, (D_\mu \, B) \, h(\phi , g)^{-1}
\, \, \, .
\label{covg}$$ The explicit form of the higher dimension Goldstone boson--baryon and meson Lagrangians is not needed here. We stress that the mesonic LECs show up in ${\cal L}_{\phi}^{(4)}$ whereas ${\cal L}_{\phi
  B}^{(2,3,4)}$ contain the baryon LECs under discussion here. In what follows, we will mostly work in the chiral limit. This amounts to neglecting terms including the external scalar and pseudoscalar sources, in particular the quark mass matrix. It is straightforward to generalize our considerations to include such terms.

## Addition of Spin--1 Fields: Tensor Field Formulation

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

## Addition of Spin--1 Fields: Vector Field Formulation

We now consider the three vector $V_\mu$ representing the three degrees of freedom of a massive spin--1 vector field (the generalization to axials is straightforward). We do not assign any particular microscopic dynamics to this vector field, like it is e.g the case in the hidden symmetry [@bky] or the massive Yang--Mills approaches [@ulfpr]. $V_\mu$ is assumed to have the standard transformation properties of any matter field under the non--linearly realized chiral symmetry, $$V_{\mu} \to h(\phi,g) \, V_{\mu} \, h(\phi,g)^{-1} \, \, \, .
\label{ccwzv}$$ The corresponding free--field Lagrangian reads $${\cal L}_0 = - \frac{1}{4} {\rm Tr} \, \biggl( V_{\mu \nu} \,
V^{\mu \nu}  -  2 \,  M_V^2 \, V_{\mu} V^{\mu} \, \biggr)\, \, \, \, ,
\label{lvfree}$$ with the (abelian) field strength tensor $$V_{\mu \nu} = D_\mu \, V_\nu - D_\nu \, V_\mu
\, \, \, \, .
\label{defvmunu}$$ The relation to the massive Yang--Mills or hidden symmetry approach is discussed in Ref.[@reso1]. The propagator is readily evaluated, $$\begin{aligned}
G_{\mu \rho} (x,y) &=& <0| \,T \bigl\{ \,V_\mu (x) \, , \,  V_\rho (y)
\, \bigr\} \, |0 > \nonumber \\
&=& -i  \int  \frac{d^4k}{(2\pi )^4} \, {\rm
  e}^{-i k\cdot (x-y)} \, \frac{g_{\mu \rho} - k_\mu k_\rho/M_V^2}{k^2
  - M_V^2 + i \epsilon} \, \, \, \, .
\label{propv}
\end{aligned}$$ For the effective action discussed below, we also need the following three-- and four--point functions $$\begin{aligned}
-i \, \Delta_{\mu \nu ,  \rho} (x,y) &=& <0| \,T \bigl\{ \,V_{\mu \nu}  (x)
\, , \,  V_\rho (y)
\, \bigr\} \, |0 > \, \, \, \, , \nonumber \\
-i \, \Delta_{\mu \nu ,  \rho \sigma} (x,y) &=&
<0| \,T \bigl\{ \,V_{\mu \nu}  (x)  \, , \,  V_{\rho \sigma} (y)
\, \bigr\} \, |0 > \, \, \, \, , \nonumber \\
-i \, \Delta_{\mu \nu ,  \rho \sigma}^\dagger (x,y) &=&
<0| \,T \bigl\{ \,\bar{V}_{\mu \nu}  (x)  \, , \,  \bar{V}_{\rho \sigma} (y)
\, \bigr\} \, |0 >  \, \, \, \, ,
\label{def34pt}
\end{aligned}$$ with $\bar{V}_{\mu \nu} = D_\mu \, V_\nu + D_\nu \, V_\mu$. These three- and four--point functions are related to the tensor field propagator, Eq.([\[propw\]](#propw){reference-type="ref" reference="propw"}), and its derivative via $$\begin{aligned}
& &\frac{1}{i} \, \partial_y^\sigma \, G_{\mu \nu , \rho \sigma} ( x,y)
 = - \Delta_{\mu \nu ,  \rho} (x,y)
\, \, \, \, , \nonumber  \\
& &\frac{1}{i} \, G_{\mu \nu , \rho \sigma} ( x,y)  =
-\frac{1}{M_V^2} \, \Delta_{\mu \nu ,  \rho \sigma} (x,y)
+  \frac{1}{M_V^2} \, \bigl( \,g_{\mu \rho} \, g_{\nu \sigma}
 - g_{\mu \sigma} \, g_{\nu \rho} \, \bigr) \, \delta^{(4)}(x-y)
\nonumber \, \, \, \, ,\\ & &
\label{relat}
\end{aligned}$$ where the contact terms in the second relation will be of importance later on (see also Ref.[@reso1]). The interaction Lagrangian of the vectors with pions and external vector and axial--vector sources takes the form $${\cal L}_{\rm int} = -\frac{1}{2\sqrt{2}} \, \biggl( f_V \, {\rm Tr} (
V_{\mu \nu} \, f_+^{\mu \nu} ) + i g_V \, {\rm Tr} (V_{\mu \nu} \, [
u^\mu , u^\nu] ) \biggr)
\, \, \, ,
\label{lvint}$$ and equivalence to the tensor field formulation for the spin--1 pole contributions (which are of order $q^6$) is achieved by setting [@reso1] $$f_V = \frac{F_V}{M_V} \, \, , \quad g_V = \frac{G_V}{M_V} \, \, .
\label{equivmes}$$

Including the baryon octet $B$ leads to the following terms at order ${\cal O}(q)$ for the $B\phi V$ interactions (see again appendix A for some details on the construction of these terms) $$\begin{aligned}
{\cal L}_{B\phi V}^{(1)}
& = & K_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \sigma^{\mu \nu} \, (
V_{\mu \nu} \, , \, B) \, \bigr] \nonumber \\
& + & G_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \gamma^\mu \, (
V_\mu\, , \, B) \, \bigr] \nonumber \\
& + & L_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \sigma^{\mu \nu} \, (
V_{\mu \lambda} \, , \, [D^\lambda ,[D_\nu , B]] \, ) \, \bigr]
\nonumber \\
& + & H_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \sigma^{\mu \nu} \, (
{\bar V}_{\mu \lambda} \, , \, [ D^\lambda , [ D_\nu , B]] \, ) \, \bigr]
\, \, \, ,
\label{Piv}
\end{aligned}$$ The first term in Eq.([\[Piv\]](#Piv){reference-type="ref" reference="Piv"}) when contracted with two $u_\mu 's$ or a field strength tensor contributes to order $q^3$ while the other terms only start one order higher. However, for the equivalence of the spin--1 pole contributions they have to be retained, as shown in the next subsection (compare to the spin--1 pole terms in the meson sector which are of order $q^6$). The fourth term in Eq.([\[Piv\]](#Piv){reference-type="ref" reference="Piv"}) is of relevance for some additional $q^4$ terms. Because it includes the symmetric tensor $\bar{V}_{\mu \nu} = \bar{V}_{\nu \mu}$, it apparently has no counterparts in the tensor field formulation, where only the antisymmetric tensor $W_{\mu \nu}$ appears. That there is, however, no inequivalence is shown in appendix A. The real constants $(K,G,H,L)_{D/F}$ are not fixed by chiral symmetry, we only assume that they are non--vanishing. The corresponding effective action takes the form $$\begin{aligned}
S_{\rm eff} &  = & - \int \, d^4x \, d^4y
  \biggl\{ K_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \,
  \sigma^{\lambda \rho} \,
\Delta_{\mu \nu , \lambda \rho} (x,y) \, ( \, J^{\mu \nu} (x) \, , \, B(y)
\, ) \biggr] \nonumber \\
& + &  G_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \, \gamma^\rho \,
\Delta_{\mu \nu , \rho } (x,y) \, ( \, J^{\mu \nu}
(x) \, , \, B(y) \, ) \biggr] \nonumber \\
& + & L_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \, \sigma^{\lambda \rho} \,
\Delta_{\mu \nu , \lambda \sigma} (x,y) \, ( \, J^{\mu \nu}
(x) \, , \, [ D_\rho , [D^\sigma ,B(y)]] \, ) \biggr] \nonumber \\
&  + & H_{D/F} \, {\rm Tr} \, \biggl[ \bar{B}(y) \, \sigma^{\lambda \rho} \,
\Delta_{\mu \nu , \lambda \sigma}^\dagger (x,y) \,
( \, J^{\mu \nu} (x) \, , \,
[D^\sigma , [ D_\rho , B(y) ]] \, ) \biggr] \biggr\} \, \, \, ,
\nonumber \\ & &
\label{seffv}
\end{aligned}$$ and the antisymmetric currents $J_{\mu \nu}$ are expressed in terms of the constants $f_V$ and $g_V$. Notice that terms of the type Tr$(\bar{B} D_\mu V^\mu B)$ do not contribute to the effective action as shown in appendix A. This completes the formalism necessary to proof the equivalence between the tensor and vector field approaches.

## Equivalence for Spin--1 Pole Contributions

We are now in the position to establish in steps the equivalenve between the effective Lagrangians ${\cal L}_{B\phi W}^{(1)}$ and ${\cal L}_{B\phi V}^{(1)}$. Comparing the effective actions, Eqs.([\[sefft\]](#sefft){reference-type="ref" reference="sefft"},[\[seffv\]](#seffv){reference-type="ref" reference="seffv"}), and making use of the first relation in Eq.([\[relat\]](#relat){reference-type="ref" reference="relat"}), one establishes the complete equivalence of the terms at order $q^3$ $$S_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \gamma^\mu \, ( [D^\nu,
W_{\mu \nu}]\, , \, B) \, \bigr]
\quad {\rm and } \quad
 G_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \gamma^\mu \, (
V_\mu\, , \, B) \, \bigr]$$ if one identifies the coupling constants as follows $$G_{D/F} = - M_V \,  S_{D/F} \,  \, \, .
\label{equiv1}$$ Furthermore, the spin--1 pole contributions of the two terms $$R_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \sigma^{\mu \nu} \, (
W_{\mu \nu} \, , \, B) \, \bigr] \quad {\rm and} \quad
 K_{D/F} \, {\rm Tr} \, \bigl[ \bar{B} \, \sigma^{\mu \nu} \, (
V_{\mu \nu} \, , \, B) \, \bigr]$$ are equivalent at order $q^4$ if $$R_{D/F} = - M_V \,  K_{D/F} \,  \, \, .
\label{equiv2}$$ Similarly, one derives $$U_{D/F} =  M_V \, (\, H_{D/F} - L_{D/F} \,)  \, \, ,
\label{equiv2a}$$ making use of Eq.([\[a16\]](#a16){reference-type="ref" reference="a16"}), see appendix A. Using that decomposition, there is another term proportional to $H_{D/F}$, $H_{D/F} {\rm Tr}[\bar{B} \sigma^{\mu \nu} (D_\mu D^\rho W_{\rho
  \lambda} \, , \, D^\lambda D_\nu B ) ]$ which contributes to the processes under consideration at order $q^4$. These higher order terms we do not consider in their full generality. There is, however, also a difference at order $q^2$ due to the contact term in $G_{\mu \nu, \rho \sigma}$, compare the second relation in Eq.([\[relat\]](#relat){reference-type="ref" reference="relat"}). To pin this down, we have to compare some physical observables as explained below. It is important to stress the formal equivalence between the effective actions, Eq.([\[sefft\]](#sefft){reference-type="ref" reference="sefft"}) and Eq.([\[seffv\]](#seffv){reference-type="ref" reference="seffv"}), which follows by inspection if one sets $$V_\mu = -\frac{1}{M_V} \, \partial^\nu \, W_{\nu \mu}  \, \, \, .
\label{formeq}$$ This is a consequence of the first identity in Eq.([\[relat\]](#relat){reference-type="ref" reference="relat"}) because up to some contact terms, it means that $V_{\mu \nu} \simeq W_{\mu \nu}$. One can show that in general, the differences between the propagators in the vector and the tensor field formulation lead to different local effective actions. Physical arguments are needed to pin down the coefficients of these polynomials. What remains to be done is therefore to enumerate the local terms that differ in the vector and tensor field formulation and to determine their coefficients.

[^1]: We are not considering the decuplet states as dynamical degrees of freedom in the effective field theory here.

[^2]: We are grateful to Harry Lee for reminding us of this problem. Of course, it has already been solved long time ago but using another approach than the one advocated here, see e.g. Weinberg' s paper [@weinnon] and also section 4.
