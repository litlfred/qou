---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-008-differentiable-events-and-observables
section_title: "Differentiable events and observables"
section_number: null
pages: 7-7
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
The result of the generation is a bank in which ev-
ery event carries, alongside its final-state kinematics, the
records of Secs. II B–II D that render its weightw i(θ)
of Eq. 1 an exact, differentiable function of the physics
parameters. Differentiability is thus a property of each
stored event individually: for any event one can ask, and
answer exactly, how its weight responds to any physics
parameter.
This event-by-event differentiability is what makes the
downstream analysis differentiable for free. Physics ob-
servables are built from the events by operations that do
not depend onθ: a signal or topology definition selects
events by their final state, a choice of kinematic variable
maps each event to an axis value, and a binning assigns
each event to a bin. None of these touches the weights, so
a binned prediction is simply the sum of the differentiable
per-event weights falling in each bin,
mb(θ) =
X
i∈b
wi(θ), ∂mb
∂θ =
X
i∈b
∂wi
∂θ .(15)
The gradient of any histogram, and therefore of any dif-
ferentiable downstream statistic built from it, is obtained
by propagating the gradients of the weights through the
same selection and binning. Changing the signal defi-
nition, the observable, or the bin edges changes which
events enter each sum but not the differentiability of the
result. In sum, an analysis is free to define its observ-
ables however it wishes and retains exact gradients with
respect to the physics parameters throughout.
Nothing in Eq. 15 requires an event to belong to a sin-
gle bin. The sum may equally be taken over a weightα ib
that spreads each event across bins,m b =P
iαibwi(θ),
and the gradient follows unchanged. When an event’s
observable is known only to within a reconstruction un-
certainty, that uncertainty can therefore be carried into
the prediction as a soft assignment rather than collapsed
into a hard choice of bin.
