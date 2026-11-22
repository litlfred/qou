---
doc_id: arxiv-hep-ph-9302246v1
doc_title: "Massive Spin-1 Field Chiral Lagrangian from an Extended Nambu-Jona-Lasinio Model of QCD"
section_id: sec-003-4-the-anomalous-sector
section_title: "The anomalous sector"
section_number: 4
pages: 12-16
source_pdf: 9302246v1.pdf
source_sha256: 2d352297255be8de
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "Massive Spin-1 Field Chiral Lagrangian from an Extended Nambu-Jona-Lasinio Model of QCD — We present a calculation of the coupling constants in the massive spin-1 ﬁeld chiral Lagrangian to chiral"
---
[]{#3 label="3"}

Here we are concerned with the imaginary part of the effective action. The lowest order Lagrangian in the abnormal intrinsic parity sector describing the interaction of pseudoscalar mesons and external $l_\mu$ and $r_\mu$ sources is the one given by the Wess-Zumino (WZ) effective action [@wz; @ew]. The ${\cal O} (p^6)$ imaginary part of the effective action has been obtained in Ref. [@bij2] in the mean-field approximation of the model we consider here. Using the formal symmetry in the ENJL cut-off model described above in Section [\[2\]](#2){reference-type="ref" reference="2"}, we can obtain to ${\cal O} (p^3)$ the abnormal intrinsic parity interaction terms for spin-1 particles from an effective action that formally has the same expression as that of the WZ action but with the external sources $l_\mu$ and $r_\mu$ replaced by the primed sources in Eq. ([\[92\]](#92){reference-type="ref" reference="92"}).

The WZ effective action [@wz; @ew] has the following explicit form in a scheme where vector currents are conserved:

$$\label{wz} \matrix{
S_{WZ} \left[ U, l, r \right] = & - \frac{\displaystyle i \, N_c}
{\displaystyle 240 \pi^2} \, {\displaystyle\int} \, d \sigma^{ijklm} \, \hbox{tr}\left(
\Sigma_i^L \, \Sigma_j^L \, \Sigma_k^L \, \Sigma_l^L \, \Sigma_m^L
\right) \hfill \cr \cr \cr
 \hphantom{S \left[ U, l, r \right]_{WZ} =} &
- \, \frac{\displaystyle i \, N_c}{\displaystyle 48 \pi^2} \, {\displaystyle\int} \, d^4 x \,
\epsilon_{\mu \nu \alpha \beta} \, \left( W ( U, l, r)
^{\mu \nu \alpha \beta} \, - \, W ( \mbox{\LARGE \bf 1}, l, r)
^{\mu \nu \alpha \beta} \right) \,,\hfill \cr \cr}$$

where

$$\matrix{ W ( U, l, r)_{\mu \nu \alpha \beta} = &
\hbox{tr}\left( U \, l_\mu \, l_\nu \, l_\alpha \, U^\dagger \, r_\beta \,
+ \, \frac{\displaystyle 1}{\displaystyle 4} \, U \, l_\mu \, U^\dagger \, r_\nu \,
U \, l_\alpha \, U^\dagger \, r_\beta \, + \, i \, U \, \partial_\mu
\, l_\nu \, l_\alpha \, U^\dagger \, r_\beta \hfill \right. \cr \cr
\hphantom{W ( U, l_\mu, r_\mu)_{\mu \nu \alpha \beta} = } &
+ \, i \, \partial_\mu \, r_\nu \, U \, l_\alpha \, U^\dagger \,
r_\beta \, - \, i \, \Sigma_\mu^L \, l_\nu \, U^\dagger \, r_\alpha \,
U \, l_\beta \, + \, \Sigma_\mu^L \, U^\dagger \partial_\nu \,
r_\alpha \, U \, l_\beta \hfill \cr \cr
\hphantom{W ( U, l_\mu, r_\mu)_{\mu \nu \alpha \beta} = } &
- \, \Sigma^L_\mu \, \Sigma^L_\nu \, U^\dagger \, r_\alpha \, U \,
l_\beta \, + \, \Sigma^L_\mu \, l_\nu \, \partial_\alpha \, l_\beta
\, + \, \Sigma^L_\mu \, \partial_\nu \, l_\alpha \, l_\beta
\hfill \cr \cr
\hphantom{W ( U, l_\mu, r_\mu)_{\mu \nu \alpha \beta} = } &
\left. - \, i \, \Sigma^L_\mu \, l_\nu \, l_\alpha \, l_\beta \, + \,
\frac{\displaystyle 1}{\displaystyle 2} \, \Sigma^L_\mu \, l_\nu \, \Sigma^L_\alpha \,
l_\beta \, - \, i \, \Sigma^L_\mu \, \Sigma^L_\nu \, \Sigma^L_\alpha
\, l_\beta \right) \hfill \cr \cr
\hphantom{W ( U, l_\mu, r_\mu)_{\mu \nu \alpha \beta} = } &
- \, \left( L \leftrightarrow R \right) \hfill \cr \cr
{\rm with}& \Sigma^L_\mu = U^\dagger \, \partial_\mu \, U\,,
\hspace*{1cm} \Sigma^R_\mu = U \, \partial_\mu \, U^\dagger
\hspace*{0.5cm} {\rm and} \hspace*{0.5cm} \epsilon_{0123} = 1\,.
\hfill \cr \cr }$$

Here, $\left( L \leftrightarrow R \right)$ stands for the interchanges

$$\label{inter}
U \leftrightarrow U^\dagger\,, \hspace*{0.5cm} l_\mu \leftrightarrow
r_\mu\,, \hspace*{0.5cm} \Sigma^L_\mu \leftrightarrow \Sigma^R_\mu\,.$$

The first term in Eq. ([\[wz\]](#wz){reference-type="ref" reference="wz"}) is an integration of an antisymmetric SU(3)$_L$ $\times$ SU(3)$_R$ invariant fifth-rank tensor that does not contain external sources over a five-dimensional sphere whose boundary is four-dimensional Minkowski space [@ew].

We can now show how the formal symmetry of the ENJL cut-off version of QCD explained in Section [\[2\]](#2){reference-type="ref" reference="2"} works. As an example we are going to calculate the term that is modulated by the coupling constant $h_V$ in Eq. ([\[47\]](#47){reference-type="ref" reference="47"}). We can write down the interaction Lagrangian linear in the $W^{(+)}_\mu$ field as

$$\label{exan}
{\cal L}_I^{W^{(+)}} \equiv \hbox{tr}\, \left(
W^{(+)}_\mu J^\mu \right)\,.$$

To obtain the current $J^\mu$, first we calculate the left ($L_\mu$) and right ($R_\mu$) anomalous chiral currents from the WZ effective action above, *i.e.*

$$\label{leftr} \matrix{
\widetilde L^\mu \, \equiv \,
\frac{\displaystyle\delta S_{WZ}}{\displaystyle\delta l_\mu}
\equiv L^\mu \, +\,& {\rm non-chirally \,\, covariant
\,\, polynomial} \hfill\cr
\hphantom{\widetilde L^\mu \, \equiv \,
\frac{\displaystyle\delta S_{WZ}}{\displaystyle\delta l_\mu} \equiv
L^\mu \, +\,} &{\rm in \,\, external \,\,sources}\, ,
\hfill\cr\cr \widetilde R^\mu \, \equiv \,
\frac{\displaystyle\delta S_{WZ}}{\displaystyle\delta r_\mu}
\equiv R^\mu \, +\,& {\rm non-chirally \,\, covariant
\,\, polynomial} \hfill\cr \hphantom{
\widetilde R^\mu \, \equiv \,
\frac{\displaystyle\delta S_{WZ}}{\displaystyle\delta r_\mu}
\equiv R^\mu \, +\,}&{\rm in \,\, external \,\,sources}\,
. \hfill\cr\cr}$$

The anomalous currents $\widetilde L^\mu$ and $\widetilde R^\mu$ have the well known structure [@bz; @le] which consists of a chirally covariant part ($L^\mu$ and $R^\mu$) that is scheme independent and a non-chirally covariant polynomial in external sources that depends on the scheme. Of course, the physics is contained in the chirally covariant part and does not change with the scheme. It is then easy to see that the current $J^\mu$ we want in Eq. ([\[exan\]](#exan){reference-type="ref" reference="exan"}) can be obtained as follows,

$$\label{symm}
J^\mu\,=\, \frac{\displaystyle 1}{\displaystyle 2}\, \left[ \xi L^\mu
\xi^\dagger \,+\, \xi^\dagger R^\mu
\xi \right]_{\left| \begin{array}{c}
 l_\mu \to l_\mu + \frac{1}{2} \xi^\dagger
W_\mu^{(-)} \xi \\ r_\mu \to r_\mu - \frac{1}{2}
\xi W_\mu^{(-)} \xi^\dagger \end{array} \right.} \,.$$

The result we get for the term we are interested in is

$$\label{res}
{\cal L}_I^{W^{(+)}} \doteq \frac{\displaystyle N_c}{\displaystyle 48 \pi^2}
\, \frac{\displaystyle 1}{\displaystyle 4} \,
\epsilon^{\mu \nu \alpha \beta} \, \hbox{tr}\, \left(
W^{(+)}_\mu \left\{ 3 \, \xi_\nu \,-\, 2\, W^{(-)}_\nu
, f^{(+)}_{\alpha \beta} \right\} \right) \,.$$

As was explained in Section [\[2\]](#2){reference-type="ref" reference="2"}, to obtain the interaction Lagrangian of the physical vector field $V_\mu$ from ${\cal L}^{W^{(+)}}_I$ we have to perform the shift in Eq. ([\[ga\]](#ga){reference-type="ref" reference="ga"}) and the scale redefinition in Eq. ([\[scale\]](#scale){reference-type="ref" reference="scale"}). These two operations introduce the couplings $g_A$, $f_V$ and $f_A$ which collect the information of the underlying theory that has been integrated out. The Lagrangian that we obtain then for the term we are considering is

$$\label{resf}
{\cal L}_I^V \doteq \frac{\displaystyle N_c}{\displaystyle 16 \pi^2}
\, \frac{\displaystyle\sqrt 2}{\displaystyle 4 f_V} \, \left(1\,-\,
\frac{\displaystyle 2}{\displaystyle 3} \, (1\,-\,g_A) \right) \,
\epsilon^{\mu \nu \alpha \beta} \, \hbox{tr}\, \left(
V_\mu \left\{ \xi_\nu, f^{(+)}_{\alpha \beta} \right\}
\right) \,.$$

After performing the same kind of calculations as in the example above, for the other abnormal intrinsic parity terms in Eqs. ([\[47\]](#47){reference-type="ref" reference="47"}), ([\[48\]](#48){reference-type="ref" reference="48"}), ([\[49\]](#49){reference-type="ref" reference="49"}), ([\[50\]](#50){reference-type="ref" reference="50"}) and ([\[51\]](#51){reference-type="ref" reference="51"}) we get the following results for these couplings:

$$\label{coup} \matrix{
\theta_V = \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle\sqrt 2}{\displaystyle 3 \, f_V} \, \left( 1 +
\frac{\displaystyle\left(1 + g_A \right)
\left(1 - g_A^2 \right) }{\displaystyle 8} \right)\,, &
h_V  =  \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle\sqrt 2}{\displaystyle 4 \, f_V} \, \left( 1 -
\frac{\displaystyle 2}{\displaystyle 3} \, \left( 1-g_A \right) \right)\,,
\hfill \cr \cr h_A \, = \, \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle g_A^2 \, \sqrt 2}{\displaystyle 12 \, f_A} \,, &
\sigma_V \, = \, \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \, \frac{\displaystyle
1}{\displaystyle 2 \, f_V^2} \, \left( 1 - \frac{\displaystyle 2}{\displaystyle 3}
\left( 1 - g_A \right) \right)\,, \hfill \cr \cr
\sigma_A \, = \, \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle g_A^2}{\displaystyle 6 \, f_A^2} \,, &
H \, = \, - \, \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \, \frac{\displaystyle
g_A}{\displaystyle 6 \, f_A \, f_V}\,, \hfill \cr \cr
Z^{(1)} \, = \, - \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle g_A (5 \, + \,4\, g_A \,-\, g_A^2)}
{\displaystyle 12 \, f_A \, f_V} \,, &  Z^{(2)} \, =
\, - \frac{\displaystyle N_c}{\displaystyle 16 \pi^2} \,
\frac{\displaystyle g_A (1 \, + \, g_A)^2}
{\displaystyle 12 \, f_A \, f_V} \,. \hfill \cr\cr }$$

We therefore find that these couplings, in the ENJL model we are considering, are completely fixed by the constants $f_V$, $f_A$ and $g_A$. This is due to the fact that the terms in the abnormal intrinsic parity sector for the interaction of spin-1 fields with pseudoscalar mesons and external sources to chiral ${\cal O} (p^3)$ and the WZ effective action come from the same formal expression.

From the expressions in Eq. ([\[coup\]](#coup){reference-type="ref" reference="coup"}), we find relations between the various couplings that are independent of $g_A$,

$$\label{relab} \matrix{
\frac{\displaystyle h_V}{\displaystyle\sigma_V}
\,=\, \frac{\displaystyle f_V}{\displaystyle\sqrt 2} \hfill \cr\cr
\frac{\displaystyle h_A}{\displaystyle\sigma_A} \,=\, \frac{\displaystyle f_A}{\displaystyle
\sqrt 2} \,. \hfill \cr\cr }$$

These relations appear because of the formal symmetry between the expression for the mean-field approximation effective action and the effective action including spin-1 particle fields explained in Section [\[2\]](#2){reference-type="ref" reference="2"}. Because of that symmetry we have, for instance, that in the effective action $f^{(+)}_{\mu \nu}$ and $V_{\mu \nu}$ always appear in the following combination

$$\label{combi}
f^{(+)}_{\mu \nu} \,+\, \frac{\displaystyle\sqrt 2}
{\displaystyle f_V} \, V_{\mu \nu} \, ,$$

therefore the couplings $\sigma_V$ and $h_V$ are related as given in Eq. ([\[relab\]](#relab){reference-type="ref" reference="relab"}).

The abnormal intrinsic parity couplings involving spin-1 particles have been considered in the literature in the context of different models [@ban]-[@meis]. A common feature of these models which differentiates them from the ENJL cut-off model we are studying here is that the spin-1 particles are introduced there as the gauge bosons either of a hidden local symmetry [@ban; @fuji] or of the U(3)$_L$ $\times$ U(3)$_R$ chiral symmetry [@kay]. The derivation of the models in Refs. [@ban]-[@kay] from an ENJL model in the presence of the chiral anomaly is studied in Ref. [@waka]. In this Reference, special attention is given to the equivalence of these models for the physics in the anomalous and non-anomalous sectors of the theory. The most interesting of these models is the so-called Hidden Gauge Symmetry (HGS) model [@ban; @fuji]. In this model, vector mesons are the dynamical gauge bosons of a hidden local U(3)$_V$ symmetry of the chiral Lagrangian. Ref. [@fuji] gives the general solution for the chiral anomaly in the presence of vector mesons when considered as gauge bosons. The solution is a linear combination of six invariants which, in general, introduce interaction terms between Goldstone bosons and external sources apart from those contained in the WZ action. It was also shown there that these new interaction terms do not change the low-energy theorems for $\pi^0 \to \gamma \gamma$ and $\gamma \to \pi \pi \pi$ transitions. The ENJL model we consider here does not introduce any coupling between Goldstone bosons and external sources apart from those in the WZ action. Thus, in order to compare both models, we shall require that the linear combination of six invariants which is a solution of the anomaly in the HGS model does not introduce couplings between Goldstone bosons and external sources apart from those in the WZ action. In this limit we have that the following relation, already found in the ENJL model in Eq. ([\[relab\]](#relab){reference-type="ref" reference="relab"}),

$$\matrix{
\frac{\displaystyle h_V}{\displaystyle\sigma_V}\,=\,\frac{\displaystyle f_V}{\displaystyle
\sqrt 2}
\hfill\cr\cr}$$

is also present in the HGS model. In the same limit one also finds the following relation in the HGS model

$$\matrix{
\frac{\displaystyle\theta_V}{\displaystyle h_V}\,=\,2\,,
\hfill\cr\cr}$$

which in the ENJL model is only true for a particular value of the $g_A$ coupling. This value is a solution of the following equation,

$$\label{easo} \matrix{
5\,-\, 7\, g_A\,-\, g_A^2\,-\,g_A^3\,=\,0\,
\hfill \cr\cr}$$

and is $g_A\simeq 0.63$ . (The other two solutions are not real.)
