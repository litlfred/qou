---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-023-the-baggy-cardy-condition
section_title: "The Baggy Cardy Condition."
section_number: null
pages: 29-31
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
7.4 The Baggy Cardy Condition.
In the case of a manifold X that is not necessarily Calabi-Yau we don’t have
the same coincidence of structure as above: we no longer have a Frobenius
algebra HH•(X); rather we have an algebra HH•(X) and an inner product
space HH•(X). This means that we can not formulate the Cardy Condition
as it stands. We now state a condition which makes sense for an arbitrary,
non-Calabi-Yau manifold and which is equivalent to the Card y Condition in
the Calabi-Yau case.
Theorem 15. Suppose that O is a Calabi-Yau category and C is an inner
product space, such that for each A ∈ O there are adjoint maps iA : OA A → C
and iA : C→ OA A . Then the Cardy Condition
µBA B◦ τ ◦ δA BA = iB ◦ iA 
is equivalent to the following equality holding for all a ∈ OA A and b ∈ OBB,
where the map amb: OA B→ OA Bis the map obtained by pre-composing with
29
a and post-composing with b:
⟨
iB− , iA −
⟩
C
= Tr − m− .
Proof. The ﬁrst thing to do is examine the left-hand side of the Cardy
Condition. As O is a Calabi-Yau category there is the following equality of
morphisms OA A → OBB.
A 
B B
A 
=
A 
BB
A 
Note that this does not require any reference to C, but it does fundamentally
require the symmetry of the inner product. This is reﬂected i n the fact that
the surfaces underlying the above pictures are diﬀeomorphi c but not ambient
isotopic.
This means that the Cardy Condition is equivalent to the foll owing equal-
ity.
A 
B
A 
B
= B
A 
By the non-degeneracy of the inner product on OBB this is equivalent to the
equality of two maps OBB ⊗ OA A → k which are drawn as follows.
A B B A 
=
B A A B
The right-hand side is instantly identiﬁable as
⟨
iB− , iA −
⟩
C. The left-hand
side is identiﬁable as the trace of the triple composition ma p OBB ⊗ OBA ⊗
OA A → OBA which gives the required result.
We can now show that the alternative condition given in the ab ove the-
orem holds for the derived category and Hochschild homology of any space:
in particular, the Cardy Condition holds for Calabi-Yau spa ces.
Theorem 16 (The Baggy Cardy Condition) . Let X be a space, let E and
F be objects in D(X) and consider morphisms
e ∈ HomD(X)(E , E ) and f ∈ HomD(X)(F , F ).
Deﬁne the operator
fme: Hom•
D(X)(E , F )→ Hom•
D(X)(E , F )
30
to be post-composition by f and pre-composition by e. Then we have
Tr fme =
⟨
ιE (e), ι F (f)
⟩
M
,
where ιE , ιF are the maps deﬁned in Section 6.2, and Tr denotes the (super)
trace.
Proof. The proof is very similar to the proof of the Semi-Hirzebruch -Rie-
mann-Roch Theorem (Theorem 14). The ﬁrst thing to observe is that
Hom(E , F ) ∼= E ∨ ◦ F and that fme is just e∨ ◦ f. However, we have
τR(e) = Σpt ◦ e∨ and Σpt is trivial so e∨ = τR(e). Putting this together with
the invariance of the Serre trace under the partial trace we g et the following
sequence, and hence the required result.
Tr fme = Tr

 e∨ fpt
E F
X
pt

 = Tr

 pt
X
pt
E
e∨
F
f


= Tr

 ptf
F
X
ept
E

 = Tr

 ptf
F
X
pt
E
e


=
⟨
X
pt
E
e ,
X
ptf
F
⟩
M
=
⟨
ιE(e), ι F(f)
⟩
M
.
Observe that the Semi-Hirzebruch-Riemann-Roch Theorem is a direct con-
sequence of the Baggy Cardy Condition, with e = IdE , f = IdF .
