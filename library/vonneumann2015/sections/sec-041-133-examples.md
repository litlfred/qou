---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-041-133-examples
section_title: "Examples."
section_number: 13.3
pages: 98-102
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Examples.
Example 13.3.1. ITPFI
The acronym ITPFI stands for “inﬁnite tensor product of ﬁnite type I”.
These von Neumann algebras are formed by taking the *-algebra A∞as the
union A∞of tensor products Am =
m
O
k=1
Mnk(C), the inclusion of Am in Am+1
being diagonal. The state φ on A∞is then the tensor product of states on
each Mnk. One may then perform the GNS construction with cyclic and
separating vector Ωgiven by 1 ∈A∞, to obtain the von Neumann algebra
M =
∞
O
k=1
Mnk(C) as the weak closure of A∞acting on Hφ. The case where
all the nk are equal to 2 and all the states are the same is called the “Powers
factor” and the product state the “Powers state” as it was R.Powers who ﬁrst
showed that they give a continuum of non-isomorphic type III factors.
A slight snag here is that we do not know that Ωdeﬁnes a faithful state
on M. But if we proceed anyway to construct what have to be J and ∆we
will soon see that the state is indeed faithful, i.e. Ωis cyclic for M ′Ω.
Recall from exercise 13.0.6 that, for Mn(C), and φh(x) = trace(xh) where
h is the diagonal matrix (density matrix) with hii = µi, P µi = 1, µi > 0,
then Jn(eij) =
q
µj
µi eji and ∆n(eij) = µi
µj eij (where dependence on h has been
suppressed).
To diagonalise the modular operators on Hφ completely it is most con-
vincing to choose an orthonormal basis di of the diagonal matrices, with
d1 = 1. Then a basis for the Hilbert space Hφ is formed by tensors ⊗∞
k=1vkΩ
where vk = 1 for large k, and is otherwise a di or an eij with i̸ = j.
We can guess that J is, on each basis vector, the tensor product of the J’s
coming from the matrix algebras. Deﬁning it as such it is clearly an isometry
on A∞Ωand thus extends to all of Hφ. But then, for any x ∈A∞, JxJ is in
M ′ by the ﬁnite dimensional calculation! But the linear span of these JxJΩ
is dense so Ωis cyclic for M ′ and hence separating for M. We are hence in
a position to apply Tomita-Takesaki theory. Each of the basis elements is in
MΩso S(⊗∞
k=1vkΩ) = ⊗∞
k=1wkΩwhere wk is vk if vk is diagonal, and eji if
98
vk = eij. So JS is diagonal and hence essentially self-adjoint. We conclude
that
J(xΩ) = Jm(x)Ω
and
∆(xΩ) = ∆m(x)Ω
for x ∈Am,
and
σφ
t =
∞
O
k=1
σφhk
.
Example 13.3.2. Group-measure-space construction.
Let Γ be a discrete group acting on the ﬁnite measure space (X, µ) pre-
serving the class of the ﬁnite measure µ. The Hilbert space of the crossed
product L∞(X, µ) is L2(X, µ)⊗ℓ2(Γ) and as we saw in chapter 11 the vector
1 ⊗εid is a cylic and separating vector Ωfor M = L∞(X, µ) ⋊Γ.
Since the class of µ is preserved by the γ ∈Γ the Radon Nikodym theorem
guarantees positive L1 functions hγ so that φ(hγαγ(y)) = φ(x) where φ(y) =
R
X ydµ. We know that, if x ∈L∞(X, µ) then S(uγx) = x∗uγ−1. In general
we will not be able to completely diagonalise ∆but the same argument as
in the previous example gives that the domain of ∆is
{f : Γ →L2(X, µ) :
X
γ
Z
X
|hγ(x)f(x)|2dµ(x) < ∞}
on which
(∆f)(γ) = hγf(γ),
and
(Jf)(γ) = h−1/2
γ
f(γ).
We can now ﬁnally answer the question as to which sums P
γ xγuγ deﬁne
elements of M = L∞(X, µ) ⋊Γ.
Theorem 13.3.3. With notation as above, if the function γ 7→xγ ∈L∞(X, µ)
is such that P
γ xγuγ, interpreted as a matrix of operators as in section 11.2,
deﬁnes a bounded operator, then that operator is in M = L∞(X, µ) ⋊Γ.
Proof. By 13.2.3 it suﬃces to show that P
γ xγuγ commutes with JxuγJ for
all x ∈L∞(X, µ) and γ ∈Γ.
And for this it suﬃces to check that the
commutation holds on functions of the form f ⊗εγ for f ∈L2. This is just
a routine computation.
Exercise 13.3.4. Show that example 13.3.1 is in fact a special case of this
group-measure-space example in which L∞(X, µ) is provided by the tensor
products of the diagonal elements and the group Γ is a restricted inﬁnite
Cartesian product of cyclic groups, constructed from the non-diagonal eij’s.
Conclude by the method of 11.2.15 that ITPFI algbras are factors.
99
This example brings to light a signiﬁcant inadequacy of our treatment of
Tomita-Takesaki theory. We would like to treat the case where the measure
of the space is inﬁnite. Although of course we could choose an equivalent
ﬁnite measure, this choice may not be natural. To do this we would have
to consider the theory of “weights” which are to states as the trace on a II∞
factor is to the trace on a type II1 factor. We need the same notion in order
to understand the origin of the term “modular” used above as coming from
the modular function on a non-unimodular locally compact group. But a
serious treatment of weights would take many pages so we simply refer the
reader to Takesaki’s book [3].
Example 13.3.5. Hecke algebras à la Bost-Connes.
If G is a ﬁnite group let ug and vg be the unitaries of the left and right
regular representations respectively. If H is a subgroup, the projection pH =
1
|H|
P
h∈H vh projects from ℓ2(G) onto functions that are right translation
invariant under H, i.e. functions on the quotient space G/H. Thus the so-
called “quasi-regular” representation of G on G/H is a direct summand of
the left regular representation and we have from EP7 of chapter 3.4 that the
commutant of the action of G on ℓ2(G/H) is pHρ(G)pH where ρ(G) is the
algebra generated by the right regular representation (of course isomorphic
to C).
This commutant is spanned by the pHvgpH which, thought of as
functions on G, are multiples of the characteristic functions of the double
cosets HgH which form the double coset space H\G/H. The subalgebra
of ρ(G) spanned by these double cosets is the space of H −H bi-invariant
functions and we see it is the commutant of G on ℓ2(G/H). It is known as
the Hecke algebra for the pair (G, H) and has a considerable role to play
in the representation theory of ﬁnite groups. A famous example is the case
where G is the general linear group over a ﬁnite ﬁeld and H is the group of
upper triangular matrices. The coset space is then the so-called “ﬂag variety”
and the Hecke algebra in this case leads to a lot of beautiful mathemtatics.
See Bourbaki [].
Nothing could better indicate how diﬀerently things work for inﬁnite dis-
crete groups than how the Hecke algebra works. Far from being direct sum-
mands, the quasiregular representations can be totally diﬀerent from the left
regular representations and can even generate type III factors! These Hecke
algebras give nice examples where the modular operators can be calculated
explicitly.
Deﬁnition 13.3.6. A subgroup H of the discrete group G is called almost
normal if either of the two equivalent conditions below is satisﬁed.
(a) gHg−1 ∩H is of ﬁnite index in H for all g ∈G.
100
(b) Each double coset of H is a ﬁnite union of left cosets of H (i.e. the
orbits of H on G/H are all ﬁnite).
If H is almost normal in G one may construct operators in the commutant
of the quasiregular representation of G on ℓ2(G/H) as follows:
Given an element x of G/H let εx be the characteristic function of x.
These functions form an orthonormal basis of ℓ2(G/H). Moreover each vector
εx is cyclic for the action of G hence separating for the commutant. If D is
a double coset of H deﬁne TD by the matrix
(TD)x,y =
(
1
if y−1x = D;
0
otherwise.
check this typesetting
Clearly TD is bounded since H is almost normal and it obviously com-
mutes with the action of G. From the deﬁnition we have
T ∗
D = TD−1.
It is also easy to check that
TDTE =
X
F
nF
D,ETF
where the structure constants are deﬁned by
nF
D,E =
(
#(E/H)
if F ⊆ED;
0
otherwise.
x
check typesetting here
We will call the von Neumann algebra generated by the TD’s the Hecke-
von Neumann algebra of the pair H ⊆G and write it HvN(G, H). The
vector state φ deﬁned on HvN(G, H) by εH is faithful and normal, and
⟨TDεH, TD′εH⟩= 0 unless D = D′ so that the TD’s are orthogonal. It is thus
easy to calculate the operators for the modular theory on Hφ (note that this
is not ℓ2(G/H)). We guess as usual that J(TDΩ) = (constant)TD−1Ωand
by counting cosets in double cosets (or sizes of orbits of H on G/H) we ﬁnd
that the constant has to be (#(D/H))1/2(#(H\D))−1/2. Thus as before JS
is diagonal on the basis TDΩof Hφ so essentially self-adjoint and
∆(TDΩ) = #(H\D)
#(D/H)TDΩ
with the obvious domain. Thus
σφ
t (TD) =
 
#(H\D)
#(D/H)
!it
TD.
101
Examples of almost normal subgroups are not hard to ﬁnd. The classical
example of Hecke himself is the case where G = SL(2, Q) and H = SL(2, Z).
In this case the Hecke algebra is abelian. Bost and Connes in [4] examined
the case of the ax+b group over the rationals with the subgroup being integer
translations. They showed that HvN(G, H) in this case is a type III factor
and made a connection with prime numbers.
