---
doc_id: arxiv-hep-th-0206161v1
doc_title: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING"
section_id: sec-006-23-good-observables-ir
section_title: "Good observables: IR"
section_number: 2.3
pages: 12-13
source_pdf: 0206161v1.pdf
source_sha256: 9530c40215baa02d
doc_brief: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING — 26 sections: Introduction; (1 .3); (α±"
---
The nice feature of the correlator (2.10) is it simple relati on to the prepotential of the
low-energy eﬀective theory. In order to derive it let us thin k of the observable (2.10) as
of a slow varying changing of the microscopic coupling const ant. If we could completely
neglect the fact that H is not constant, then its addition would simply renormalize the
eﬀective low-energy scale Λ → Λ e−H .
However, we should remember that H is not constant, and regard this renormalization
as valid up to terms in the eﬀective action containing deriva tives of H. Moreover, H
is really a bosonic part of the function H(x,θ ) on the (chiral part of) superspace (in
[1] such superspace-dependent deformations of the theory o n curved four-manifolds were
considered):
H(x,θ ) = H(x) + 1
2ωµνθµθν
Together these terms add up to the making the standard Seiber g-Witten eﬀective action
determined by the prepotential F (a; Λ) to the one with the superspace-dependent prepo-
tential
F (a; Λ e−H(x,θ)) = F (a; Λ e−H) +ω Λ ∂Λ F (a; Λ e−H) + 1
2ω2 (Λ ∂Λ )2 F (a; Λ e−H) (2 .11)
This prepotential is then integrated over the superspace (t ogether with the conjugate
terms) to produce the eﬀective action.
Now, let us go to the extreme infrared, that is let us scale the metric on I R4 by a very
large factor t (keeping ω intact). On ﬂat I R 4 the only term which may contribute to the
correlation function in question in the limit t → ∞ is the last term in (2.10) as the rest
will (after integration over superspace) necessarily cont ain couplings to the gauge ﬁelds
which will require some loop diagrams to get non-trivial con tractions, which all will be
suppressed by inverse powers of t. The last term, on the other hand, gives:
11
Z(a;ǫ) = exp − 1
8π2
∫
I R4
ω ∧ω∂2 F (a; Λ e−H)
(∂logΛ) 2 +O(ǫ) (2 .12)
where we used the fact that the derivatives of H are proportional to ǫ1,2. Recalling
(2.7)(2.8) the integral in (2.12) reduces to:
Z(a;ǫ1,ǫ 2) = exp F inst(a; Λ) + O(ǫ)
ǫ1ǫ2
(2.13)
where
F inst(a; Λ) =
∫ ∞
0
∂2
H F (a; Λ e−H) HdH
thereby explaining our claim about the analytic properties of Z and F .
