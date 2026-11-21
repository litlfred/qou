---
doc_id: arxiv-hep-ph-9511320v1
doc_title: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields"
section_id: sec-003-22-addition-of-spin--1-fields-vector-field-formu
section_title: "Addition of Spin--1 Fields: Vector Field Formulation"
section_number: 2.2
pages: 8-11
source_pdf: 9511320v1.pdf
source_sha256: 4336112cecabdfdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.993
doc_brief: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields — We analyze the eﬀective low–energy ﬁeld theory of Goldstone bosons and baryons chirally coupled to massive spin–1 ﬁelds."
---
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
