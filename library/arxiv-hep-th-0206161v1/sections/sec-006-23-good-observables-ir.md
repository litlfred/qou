---
doc_id: arxiv-hep-th-0206161v1
doc_title: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING"
section_id: sec-006-23-good-observables-ir
section_title: "Good observables: IR"
section_number: 2.3
pages: 12-13
source_pdf: 0206161v1.pdf
source_sha256: 9530c40215baa02d
toc_source: inferred
doc_brief: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING — 24 sections: Front matter; Jourdain:; Introduction"
---
The nice feature of the correlator (2.10) is it simple relation to the prepotential of the
low-energy eﬀective theory. In order to derive it let us think of the observable (2.10) as
of a slow varying changing of the microscopic coupling constant. If we could completely
neglect the fact that H is not constant, then its addition would simply renormalize the
eﬀective low-energy scale Λ →Λe−H.
However, we should remember that H is not constant, and regard this renormalization
as valid up to terms in the eﬀective action containing derivatives of H.
Moreover, H
is really a bosonic part of the function H(x, θ) on the (chiral part of) superspace (in
[1] such superspace-dependent deformations of the theory on curved four-manifolds were
considered):
H(x, θ) = H(x) + 1
2ωµνθµθν
Together these terms add up to the making the standard Seiberg-Witten eﬀective action
determined by the prepotential F(a; Λ) to the one with the superspace-dependent prepo-
tential
F(a; Λe−H(x,θ)) = F(a; Λe−H) + ω Λ∂ΛF(a; Λe−H) + 1
2ω2 (Λ∂Λ)2 F(a; Λe−H)
(2.11)
This prepotential is then integrated over the superspace (together with the conjugate
terms) to produce the eﬀective action.
Now, let us go to the extreme infrared, that is let us scale the metric on IR4 by a very
large factor t (keeping ω intact). On ﬂat IR4 the only term which may contribute to the
correlation function in question in the limit t →∞is the last term in (2.10) as the rest
will (after integration over superspace) necessarily contain couplings to the gauge ﬁelds
which will require some loop diagrams to get non-trivial contractions, which all will be
suppressed by inverse powers of t. The last term, on the other hand, gives:
11
Z(a; ǫ) = exp −
1
8π2
Z
IR4 ω ∧ω ∂2 F(a; Λe−H)
(∂logΛ)2
+ O(ǫ)
(2.12)
where we used the fact that the derivatives of H are proportional to ǫ1,2.
Recalling
(2.7)(2.8) the integral in (2.12) reduces to:
Z(a; ǫ1, ǫ2) = exp Finst(a; Λ) + O(ǫ)
ǫ1ǫ2
(2.13)
where
Finst(a; Λ) =
Z ∞
0
∂2
HF(a; Λe−H) HdH
thereby explaining our claim about the analytic properties of Z and F.
