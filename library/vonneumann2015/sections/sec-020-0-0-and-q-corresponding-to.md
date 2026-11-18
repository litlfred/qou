---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-020-0-0-and-q-corresponding-to
section_title: "0 ) and q corresponding to"
section_number: 0
pages: 47-49
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---

b
√
b(1−b)
√
b(1−b)
1−b

47
Now drop the hypothesis that p and q are in general position.
Exercise 7.3.9. Show that p ∨q −p ∼= q −p ∧q in M
Exercise 7.3.10. Show that if e and f are ﬁnite projections in a factor M
then p ∨q is also ﬁnite. (In fact it’s true for a non-factor as well.)
(Here’s how to do it: use the previous exercise to reduce it to the case
where e and f are orthogonal. Then one can assume f = e⊥. Suppose we
could ﬁnd an inﬁnite projection p so that e ∧p ⪯e⊥∧p⊥. Then
p = e ∧p + p −e ∧p
⪯e⊥∧p⊥+ p ∨e −e ( remembering that e⊥∧p⊥= (e ∨p)⊥)
≤e⊥
so that p is ﬁnite.
To ﬁnd such an e and p, construct an inﬁnite projection p equivalent to
1 −p (“halving”). Then either e ∧p ⪯e⊥∧p⊥in which case we are done, or
e⊥∧p⊥⪯e ∧p in which case we simply switch to e⊥and p⊥.)
Alternative approach using group representations.
Exercise 7.3.11. Show that (Z/2Z)∗(Z/2Z) ∼= Z⋊(Z/2Z) (inﬁnite dihedral
group).
Exercise 7.3.12. Classify all unitary representations of Z⋊(Z/2Z). (Hint—
use the spectral theorem for unitaries.)
Exercise 7.3.13. Observe that 2p −1 and 2q −1 are self-adjoint unitaries.
Exercise 7.3.14. Obtain the structure of 7.3.8 using the last 3 exercises.
48
Chapter 8
The Predual
An ultraweakly continuous linear functional φ on a von Neumann algebra M
is norm continuous so deﬁnes an element of M ∗. Our goal in this chapter is
to show that the set of all such φ is a closed subspace M∗of M ∗and that
the duality between M∗and M makes M equal to the Banach space dual of
M∗. We will ﬁrst establish this in the special case M = B(H).
