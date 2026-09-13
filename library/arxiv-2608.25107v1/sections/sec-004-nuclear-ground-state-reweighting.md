---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-004-nuclear-ground-state-reweighting
section_title: "Nuclear ground-state reweighting"
section_number: null
pages: 4-4
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
The target nucleus is described by a spectral function,
the probability density for finding the struck nucleon with
momentum|p|and removal energyE[99]. At genera-
tion, the struck nucleon is sampled from the tabulated
spectral function by importance sampling, with density
proportional to|p| 2S(|p|,E), and its momentum and re-
moval energyE=m N−E in are recorded. Because that
point is stored, a deformation ofSreweights the event
by the ratio of the deformed to the original density there,
exactly and without resampling,
rSF
i (θ) =N SF

1 + (NSRC−1)σ
|p|−p src
wsrc

× S(|p|/kF, E−∆E b)
S(|p|, E) ,(2)
whereσis the logistic function,p src = 300 MeV,w src =
80 MeV, and (|p|,E) are the values stored for eventi.
Because the factor is evaluated pointwise on that stored
point, it is differentiable with respect to all four ground-
state parameters without re-sampling the nucleus.
The four parameters act on different features of the
same distribution.k F scales the momentum axis, widen-
ing or narrowing the Fermi motion of the struck nucleon.
∆Eb shifts the removal-energy axis, and so moves the po-
sition of the quasi-elastic peak; it is the parameter most
directly tied to the reconstructed neutrino energy.N SF
is an overall normalisation.N SRC raises or lowers the
region abovep src, where the high-momentum tail gener-
ated by short-range correlations lives; those correlations
are carried by the tabulated spectral function itself, and
NSRC deforms the tail rather than modelling it.
Two properties of the construction deserve particular
attention. The first is that ∆E b is one-sided, and il-
lustrates a subtlety common to any physically bounded
parameter. Negative values are clamped to zero, because
the ratio has a corner where the shifted and unshifted
grids part company; once the shift would pushEbe-
low zero the model is flat, with an identically vanishing
gradient. We anchor the nominal value on the smooth,
one-sided branch of the response, an offset of 10 −2 MeV
from the wall, so that a well-defined one-sided gradient
is always available to the optimiser; the resulting trun-
cated, non-Gaussian posterior at the boundary is studied
explicitly later in Sec. V. The second is that the interpo-
lation ofSis cubic in momentum and linear in removal
energy, mirroring ACHILLES; smoother interpolation in
removal energy overshoots the steep low-Erise, produc-
ing negative densities.
