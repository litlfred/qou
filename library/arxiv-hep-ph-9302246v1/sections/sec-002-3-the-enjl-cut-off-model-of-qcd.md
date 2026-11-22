---
doc_id: arxiv-hep-ph-9302246v1
doc_title: "Massive Spin-1 Field Chiral Lagrangian from an Extended Nambu-Jona-Lasinio Model of QCD"
section_id: sec-002-3-the-enjl-cut-off-model-of-qcd
section_title: "The ENJL cut-off model of QCD"
section_number: 3
pages: 8-12
source_pdf: 9302246v1.pdf
source_sha256: 2d352297255be8de
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.981
doc_brief: "Massive Spin-1 Field Chiral Lagrangian from an Extended Nambu-Jona-Lasinio Model of QCD — We present a calculation of the coupling constants in the massive spin-1 ﬁeld chiral Lagrangian to chiral"
---
[]{#2 label="2"}

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
