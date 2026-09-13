---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-006-intranuclear-cascade
section_title: "Intranuclear cascade"
section_number: null
pages: 6-6
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
The hadrons produced at the vertex propagate through
the residual nucleus and undergo final-state interactions,
modelled with a JAX re-implementation of the intranu-
clear cascade used in ACHILLES [99]: elastic and inelas-
tic nucleon–nucleon and pion–nucleon scattering, pion
absorption, and charge exchange. Everything at the ver-
tex is a smooth function of the parameters once the kine-
matics are fixed. The cascade is not: a hadron leaving
the vertex takes a variable-length sequence of sampled
re-interactions, and the number, position and identity of
those interactions are themselves random. Differentiat-
ing any single realised history gives nothing, because a
parameter change does not move that history, it changes
how probable it was.
The construction.ADoNIScompactly stores the his-
tory each event actually took, and recomputes its proba-
bility under new parameters. The cascade factor in Eq. 1
is the likelihood ratio of that history,
rFSI
i (θ) =
Y
n∈history i
pn(θ)
pn(nominal),(12)
a product over the interaction and survival probabili-
ties of every step, each a smooth function of the cor-
responding rate parameter and equal to unity at nom-
inal. Reweighting the stored history in this way is
the importance-weight expression of the change of rates,
and it is differentiable in the cascade parameters with-
out re-running the cascade. It is closely related to the
score-function construction for stochastic computation
graphs [136]: there the derivative of an expectation is
obtained from the log-probability of the realised choices,
whereas here the full likelihood ratio of each stored his-
tory is written down directly. The finite parameter de-
pendence is therefore available explicitly, and its deriva-
tives at anyθfollow by automatic differentiation.
The step probabilities.A propagating hadron advances
in small steps. At each step the nucleons within reach are
candidates, and the hadron interacts with the closest of
them with probability
p0 = exp(−a), a= πb2
σtot
,(13)
wherebis the impact parameter to that nucleon andσ tot
the total cross section there. A rate parameter enters
throughσ tot and so has two distinct effects. First, it
changeswhetherthe hadron interacts: rescaling the total
by a factorgmapsa→a/gand gives an interaction-
probability factorp g/p0 on a step that interacted and a
survival-probability factor (1−p g)/(1−p 0) on one that
did not, withp g = exp(−a/g). Second, it changeswhich
channel occurred, contributings realised/gon a step that
interacted. A common rescaling of every channel leaves
the second factor at unity but not the first, which is the
mean-free-path effect.
Pion channels.A pion may scatter elastically, charge
exchange, be absorbed on a nucleon pair, or convert to
ηN; the four parameterss el
πN ,s cex
πN ,s π
abs ands conv scale
those four rates respectively, and
g= 1 + (s π
abs−1)f abs + (sel
πN−1)f el
+ (scex
πN−1)f cex + (sconv−1)f conv,(14)
withf i the fraction of the total cross section carried by
channeliat that step. Written in this formgis exactly
unity at nominal in any precision, which matters because
exp(−a/g) amplifies any error ing. A pion converted
throughπN→ηNproduces a propagatingη, which may
subsequently back-convert to a pion or leave the nucleus;
the strangeness-producing branch is treated as terminal.
The underlying cross sections are those of ACHILLES:
the ANL–Osaka amplitudes of Sec. II C for meson–baryon
scattering [28], and the optical-potential model of Oset
and Salcedo for absorption [133], in which the pion is
absorbed through the imaginary part of its self-energy in
nuclear matter.
Nucleon channels.A nucleon may scatter elastically or
inelastically, the latter proceeding throughNN→N∆
with the ∆ decaying immediately toNπ; this is the chan-
nel that degrades fast nucleons and creates pions inside
the nucleus. Both rates are resolved by isospin pair, since
pp,pnandnncross sections differ, giving six parameters
sel
NN,ij ands inel
NN,ij that act only on steps of the match-
ing pair, withg=s el(1−f inel) +s inelfinel. The elastic
cross section follows the GiBUU parametrisation [80] and
the inelastic one theNN→N∆ model of Dmitriev and
Sushkov [137].
Charge exchange.The last cascade parameter is not
a rate but a probability. When a proton and a neu-
tron scatter elastically the outgoing pair may or may not
exchange identity, and ACHILLES assigns the two out-
comes equal weight.f cex
NN varies that split, contributing
fcex
NN/0.5 on a step that exchanged and (1−f cex
NN )/0.5 on
one that did not. Identical pairs cannot exchange, sopp
andnnsteps are unaffected and carry no factor. Its nom-
inal value is 0.5 rather than unity because it is a fraction,
not a scale.
