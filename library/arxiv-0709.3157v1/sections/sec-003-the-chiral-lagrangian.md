---
doc_id: arxiv-0709.3157v1
doc_title: "V . Mateu"
section_id: sec-003-the-chiral-lagrangian
section_title: "The chiral Lagrangian"
section_number: null
pages: 3-5
source_pdf: 0709.3157v1.pdf
source_sha256: 22a0d9a93c9dcb8d
doc_brief: "V . Mateu — The implementation of tensor sources in Chiral Lagrangians allows the computation of Green functions and form factors involving tensor currents , that is, quark bilinears of the form ¯qi"
---
The number of operators entering in the chiral Lagrangian is of course not restricted by
symmetry. So in principle there are an inﬁnite number of them , each one multiplied by
an unknown coefﬁcient (this is in agreement with the fact tha t χPT is not normalizable
stricto sensu). So if one has to take them all into account in any calculatio n, loses all
predictive power. At low energies (compared with the chiral scale Λ χ ∼ 4πF ∼ 1GeV)
pieces with lower powers of momentum and quark masses domina te, and this allows
to truncate the number of operators. This idea is systematiz ed by the Weinberg power
counting scheme [1].
So all of the building blocks must be endowed with a power counting, determined by
the number of derivatives and masses : ℓμ and rμ appear as covariant derivatives and
this ﬁxes its counting; masses count as two power of derivati ves, and this dictates the
counting of s and p. Since the tensor source does not have a physical realizatio n, its
counting is arbitrary. We have then
u ∼ O(p0) , vμ , aμ ∼ O(p1) , χ , t μν ∼ O(p2) , (11)
Using the tracelessness properties ⟨r μ⟩ = ⟨ℓ μ⟩= ⟨F μν
L R ⟩ = ⟨f μν
± ⟩ = ⟨u μ⟩ = 0 we ﬁnd
four new terms [8] at O(p4) [tensor sources do not appear at O(p2)]
L χPT
4 = Λ1 ⟨t μν
+ f+μν ⟩ − i Λ2 ⟨t μν
+ u μu ν ⟩ + Λ3 ⟨t μν
+ t+ μν ⟩ + Λ4 ⟨t μν
+ ⟩2 , (12)
where ⟨· · ·⟩stands for the trace in n f ﬂavour space. At this order there is no contact term
because of the identities t μν
+ t+
μν = t μν
− t−
μν and t μν
+ t−
μν = t μν
− t+
μν.
At O(p6) there are more than a hundred operators involving tensor sou rces, but not
all of them are independent. The steps one must follow for the reduction of the number
of operators were given in Ref. [4] and we brieﬂy review them now :
(a) Partial integration and lowest order equations of motion
Terms connected by partial integration leave the action invariant, and should be consid-
ered only once. The lowest order equation of motion must be used to reduce the basis (it
is equivalent to a ﬁeld redeﬁnition [4]). It reads
∇ μu μ = 1
2i
( ⟨χ−⟩
n f
− χ−
)
. (13)
(b) Bianchi identities
There is an associated bianchi identity to the covariant derivative (10) that translates into
one relation that allows to eliminate one operator
∇ μ f+να + ∇ ν f+α μ + ∇ α f+μν = i
2
([
f−μν ,uα
]
+
[
f−να ,uμ
]
+
[
f−α μ,uν
])
. (14)
(c) Isolation of contact terms
In our basis there are linear combinations of operators whic h only depend on external
sources. They are unphysical but however necessary to make the theory renormalizable.
One has to isolate such terms, and at this order there appear only three.
(c) Cayley–Hamilton relations
The three ﬁrst steps are generic for an arbitrary number of li ght ﬂavours n f , but the
only phenomenologically interesting values are n f = 2, 3. For such values additional
matrix relations (based on the Cayley–Hamilton theorem) further reduce the number of
independent operators. The full list of such relations can be found in Ref. [8].
So we end up with 117 operators plus three contat terms for n f ﬂavours, 110+3 for
n f = 3 and 75+3 for 2. These operators are listed in Ref. [8]. In Ref . [12] a caveat is
given, and it is claimed that the above procedure does not nec essarily yield a minimal
basis. However we believe that tensor sources are not affected by their considerations.
