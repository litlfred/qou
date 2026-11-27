---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-013-341-the-constraints-at-second-order
section_title: "The constraints at second order"
section_number: 3.4.1
pages: 15-16
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
The general discussion of § 3.2 allows us to obtain the second order solution to Einstein ’s
equations once we have solved the ﬁrst order system as outlin ed in § 3.3. However, we
need to confront an important issue before proceeding, owin g to the way we have set up
the perturbation expansion. Of course perturbation theory at second order is well deﬁned
only once the ﬁrst order equations have been solved. While in principle we should solve
these equations everywhere in R3, 1, in the previous subsection we did not quite achieve
that; we were content to solve the constraint equation (3.6) only to ﬁrst order in the Taylor
expansion about our special point yµ . While that was good enough to obtain g(1), in order
to carry out the second order calculation we ﬁrst need to do be tter; we must ensure that
the ﬁrst order constraint is obeyed to second order in the Tay lor expansion of the ﬁelds
b(0) and β(0)
i about yµ . That is, we require
∂λ ∂µ T µν
(0) (yα ) = 0 . (3.12)
15Conventionally, one writes in ﬂuid mechanics the stress ten sor as the perfect ﬂuid part and a dissipative
part i.e., T µν = T µν
perf ect + T µν
dissipative. The Landau gauge condition we choose at every order simply
amounts to uµ T µν
dissipative = 0.
Essentially, we require that T µν
(0) satisfy the conservation equation (3.6) to order ε2 before
we attempt to ﬁnd the second order stress tensor. In general, we would have need (3.6)
to be satisﬁed globally before proceeding; however, the ult ralocality manifest in our set-up
implies that it suﬃces that the conservation holds only to th e order we are working. If we
were interested in say the nth order stress tensor T µν
(n) we would need to ensure that the
stress tensor up to order n − 1 satisﬁes the conservation equation to order O (εn−1).
The equations (3.12) may be thought of as a set of 16 linear con straints on the coeﬃ-
cients of the (40+78) two derivative terms involving b(0) and β(0)
i . We use these equations
to solve for 16 coeﬃcients, and treat the remaining coeﬃcien ts as independent. This pro-
cess is the conceptual analogue of our zeroth order ‘solutio n’ of ﬂuid dynamics at the point
yµ (described in the previous subsection), obtained by solvin g for the ﬁrst derivatives of
temperature in terms of the ﬁrst derivatives of velocities. Indeed it is an extension of that
procedure to the next order in derivatives. See § 5 for the details of the implementation
of this procedure. In summary, before we even start trying to solve for g(2), we need to
plug a solution of (3.12) into g(0) + g(1) expanded in a Taylor series expansion about yµ .
Otherwise we would be expanding the second order equations a bout a background that
does not solve the ﬁrst order ﬂuid dynamics.
