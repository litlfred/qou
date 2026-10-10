---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-009-gradients-and-higher-order-derivatives
section_title: "Gradients and higher-order derivatives"
section_number: null
pages: 7-7
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
Becauseθ7→{w i}is a JAX function, the Jacobian of
the binned prediction,
Jbk = ∂mb
∂θk
,(16)
is obtained by automatic differentiation. As the map
takes few inputs (the parameter vector) to many outputs
(the per-event weights, reduced to bins), we evaluate it
in forward mode. A single Jacobian-vector product with
a unit tangente k returns the full per-event derivative in
thek-th parameter direction in one forward pass, and
the columns for all parameters are batched into one vec-
torised evaluation whose cost is a small multiple of a
single forward reweight.
The same construction extends to arbitrary derivative
order by nesting Jacobian-vector products along the de-
sired parameter directions, with no symbolic derivative
code required. The first derivatives form the Gauss–
Newton, or Fisher, matrix
Fkl =
X
b
1
σ2
b
∂mb
∂θk
∂mb
∂θl
,(17)
withσ b the per-bin uncertainty. This is the positive-
semidefinite curvature approximation underlying the fits
of Sec. V.
