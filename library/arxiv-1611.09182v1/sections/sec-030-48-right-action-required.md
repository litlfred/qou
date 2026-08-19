---
doc_id: arxiv-1611.09182v1
doc_title: ""
section_id: sec-030-48-right-action-required
section_title: "Right action required"
section_number: 4.8
pages: 36-40
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? C. Furey A thesis presented to the University of Waterloo in fulfillment of the thesis requirement for the degree of Doctor of Philosophy Physics — 57 sections"
---
Readers may have noticed that the left action of C⊗ H on itself was not enough to describe
ΨL + ΨR together as a single irreducible representation. That is, the left action alone has
only ΨL (or ΨR) as an irrep. However, the combined Dirac spinor, Ψ L + ΨR, does become
an irreducible representation of a Cliﬀord algebra when the right action of C⊗ H is also
included. Readers will ﬁnd this theme coming up again in future chapters.
4.9 Parity and the ﬁeld strength tensor
The work in this section is to appear in a joint paper, together with G. Fiore from INFN.
In Section 3.6, we introduced four-vectors, p, as generalized ideals under the hermitian
invariant-action,mh. These can be described as
p =p0 +p1iϵx +p2iϵy +p3iϵz, (4.12)
which transform under the Lorentz group as p′ =mh(L,p ) =LpL†, for L∈SL(2, C).
Furthermore, in Section 3.7, we introduced the ﬁeld strength tensor,F , as a generalized
ideal under the quaternionic invariant-action, mq. Explicitly, we had
F = (B1−iE1)ϵx + (B2−iE2)ϵy + (B3−iE3)ϵz, (4.13)
which transforms under the Lorentz group as F′ = mq(L,F ) = LF~L. Of course, we also
studied spinors and scalars in previous sections, but these will not be relevant for us at the
moment.
Given these two Lorentz representations, we might wonder how parity transformations
are to be carried out. Under a parity transformation, we would expect
28
p ↦→ p′ =p0−p1iϵx−p2iϵy−p3iϵz,
F ↦→ F′ = (B1 +iE1)ϵx + (B2 +iE2)ϵy + (B3 +iE3)ϵz.
(4.14)
Now, it might be tempting to consider the quaternionic conjugate as the parity conju-
gate, since ~ϵx =−ϵx, ~ϵy =−ϵy, and ~ϵz =−ϵz. However, the quaternionic conjugate sends
F↦→−F , which does not give the desired result: Ei↦→−Ei, and Bj↦→Bj. So how might
we deﬁne a parity transformation?
In Section 4.7, we demonstrated a representation of the Dirac algebra, C⊗Cl(1, 3),
using both left and right multiplication of C⊗ H on itself. From this Cliﬀord algebra, it is
then possible to deﬁne a parity transformation:
γ0 ↦→ γ0 = 1|iϵx, γ j ↦→ −γj =−iϵj|ϵy, (4.15)
for j = 1, 2, 3.
So, the question is now: how do we use this parity transformation on the γµ to induce
a parity transformation on p and F ?
The resolution to this question is not obvious, because p and F are objects which are
derived from C⊗ H≃ Cl(2) structure, while the γµ belong in ( C⊗ H)⊗C (C⊗ H)≃
C⊗Cl(1, 3)≃ Cl(4). One solution, which we will now show, is to generalize the Cl(2)
objects, p and F , to two new Cl(4) operators, ˆp and ˆF . We might hope, then, that under
the right conditions, ˆp and ˆF would reduce to p and F . In summary, we would like to
see the parity transformations on ˆp and ˆF , given by equation 4.15, automatically induce
parity transformations on p and F .
Let us then deﬁne ˆp to be
ˆp≡pµγµ =p0 1|iϵx +pjiϵj|ϵy, (4.16)
for pµ∈ R, for µ = 0, 1, 2, 3, and j = 1, 2, 3. This is none other than the usual pµγµ of
quantum ﬁeld theory.
Making use of the Cliﬀord algebraic description of [51], let us deﬁne ˆF to be
ˆF≡Fµνγµν =F0iγ0i +Fjkγjk =Eiϵi|ϵz−Bjϵj| 1, (4.17)
for µ,ν = 0, 1, 2, 3, Fµν∈ R, γµν≡ 1
2 [γµ,γν], and i,j = 1, 2, 3.
29
It is then trivial to see that under a parity transformation given by
γ0 ↦→ γ0 = 1|iϵx, γ j ↦→ −γj =−iϵj|ϵy, (4.18)
for j = 1, 2, 3, the operator, ˆp transforms as
ˆp ↦→ ˆp′ =p0 1|iϵx−pjiϵj|ϵy, (4.19)
and the operator, ˆF transforms as
ˆF ↦→ ˆF′ =−Eiϵi|ϵz−Bjϵj| 1, (4.20)
as we would expect.
So, we have a new description for four-momenta, ˆp, and the ﬁeld strength tensor, ˆF ,
which transform as they should under parity. We would now like to know how these relate
to the generalized ideals, p and F that we found earlier in Sections 3.6 and 3.7.
We ﬁnd that the operators ˆp and ˆF reduce to the generalized ideals p and F , when ˆp
and ˆF are taken to be operators, acting on spinors in C⊗ H. Incorporating the object γ0,
we ﬁnd that ˆp reduces to p, or p∗, on Weyl spinors,
γ0ˆp ΨL =p∗ ΨL, γ 0ˆp ΨR =p ΨR. (4.21)
Similarly, we ﬁnd that ˆF reduces to F , or F∗, on Weyl spinors as
ˆF ΨL =−F∗ ΨL, ˆF ΨR =−F ΨR. (4.22)
Readers may note that a parity transformation on ˆp and ˆF now automatically induces the
correct parity transformation on p andF , when these objects are taken to be operators on
spinors.
Finally, we point out that this deﬁnition of parity,
γ0 ↦→ γ0 = 1|iϵx, γ j ↦→ −γj =−iϵj|ϵy, (4.23)
sends γ5 ↦→ −γ5, so that left- and right-handed Weyl spinors are swapped under this
transformation, as we would expect.
30
In summary, we have shown that the parity conjugate of theC⊗Cl(1, 3)≃ (C⊗ H)⊗C
(C⊗ H) algebra may be used to induce a parity conjugate on our generalized ideals in
C⊗ H.
Note that we have also demonstrated a way to write down four-vectors, and the ﬁeld
strength tensor, in the Dirac algebra formalism, which makes use of the generalized ideals
found in Sections 3.6 and 3.7. Namely,
ˆp ΨD =γ0mc(p∗, ΨD), ˆF ΨD =mc(−F∗, ΨD). (4.24)
31
Chapter 5
