---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-079-54-neron-severi-lattices-111
section_title: "N´eron-Severi lattices 111"
section_number: 5.4
pages: 119-121
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
be the quotient of the ﬁnitely generated abelian groupH2(S,Z) by its torsion
subgroup. Since the intersection form
b : H2(S,Z)×H2(S,Z)−→ Z
takes its values in the torsion-free groupZ, it is clear that the intersection
pairing between any torsion class and any other class vanishes. Hence the
intersection form of the surface factors over a non-degenerate symmetric
bilinear formb : LS×LS−→Z, and we viewLS as a lattice with respect
to this bilinear form. Note that by Poincar´e duality this lattice is always
unimodular. We also have the following well-known
LEMMA 5.13. If for some integral classα∈ H2(S,Z) the ﬁrst Chern
class satisﬁes c1(S)≡ 2α modulo torsion, then LS is an even lattice.
Proof. By naturality, the reduction mapr : Z−→Z/2Z gives rise to a
commutative diagram
H2(S,Z)×H2(S,Z) ∪ //
(r∗,r∗)

H4(S,Z)
degS //
r∗

Z
r

H2(S,Z/2)×H2(S,Z/2) ∪ // H4(S,Z/2)
degS // Z/2
where the degree maps degS are deﬁned by evaluation on the fundamental
homology class ofS. The composite of the upper horizontal arrows is the
intersection pairing we are interested in. Now the image of the ﬁrst Chern
class c1(S) under the reduction mapr∗ : H2(S,Z)−→H2(S,Z/2Z) is the
Stiefel-Whitney classw2(S) by [77, p. 171], and for the intersection form
modulo two we have
degS(w2(S)∪r∗(β)) = r(degS(β2)) for all β∈ H2(S,Z)
by the Wu formula [45, prop. 1.4.18]. Hence the claim follows. □
After this topological digression, let us now come back to the smooth
surfacesY andY+ deﬁned by a general intersecion of translates of a smooth
theta divisor on a complex ppavX of dimensiong =4. Let us ﬁrst determine
the abstract isomorphism type of the corresponding lattices.
LEMMA 5.14. With notations as above,
LY ∼= L2⊕U9 and L Y+∼= L.
Proof. It follows from corollary 5.9 that the intersection form on the
latticesLY andLY+ is indeﬁnite of signature(35,51) resp.(13,21). An even
unimodular lattice is determined uniquely by its rank and signature [96], so
it only remains to show that bothLY and LY+ are even lattices. For this we
112 Chapter 5 – A family of surfaces
can apply lemma 5.13. Indeed, the condition of the lemma holds forLY
because
c1(Y) = 2α for the class α =−[Θ]|Y ∈ H2(Y,Z)
by lemma 5.5. Furthermore, by proposition 5.11 we can ﬁndα+∈ LY+
such thatq∗(α+) =α whereq :Y−→Y+ is the quotient morphism. It then
follows that
q∗(c1(Y+)−2α+) = q∗(c1(Y+))−2q∗(α+) = c1(Y)−2α = 0
so that by proposition 5.11 the classc1(Y+)−2α+ is a torsion class. Hence
by lemma 5.13 alsoLY+ is an even lattice. □
Now that we have found the abstract isomorphism type of the latticesLY
andLY+, the next thing to be done is to determine the relationship between
these two lattices. For this we denote by
L+
Y = H2(Y,Z)+⊂ LY = H2(Y,Z)
the invariants ofLY under the action of the involutionσ, i.e. the lattice
which occurs in the middle part of the diagram in proposition 5.12. The
relationship we are looking for is then given by
LEMMA 5.15. The pull-back under the quotient morphism q:Y−→Y+
gives rise to a lattice isomorphism
q∗ : LY+(2)
∼=−→L+
Y ⊂ LY .
Proof. By proposition 5.11 the pull-backq∗ induces an isomorphism
of the underlying abelian groups. Via this isomorphism, the intersection
form onLY induces twice the intersection form onLY+ since q : Y→Y+
is an ´etale double cover: The degree maps for the top cohomology of our
surfaces satisfy
degY(q∗(a)∪q∗(b)) = degY(q∗(a∪b)) = 2degY+(a∪b)
for all cohomology classesa,b in H2(Y+,Z). □
From the above two lemmas we obtain the middle and the right vertical
isomorphism in the diagram of proposition 5.12. These isomorphisms can
be chosen in such a way that the square on the right hand side of the diagram
commutes, indeed we have the following
LEMMA 5.16. Let L1,L2⊂ LY be sublattices of rank r≤ 34 which are
primitive in the sense that the quotients LY/L1 and LY/L2 are torsion-free
groups. Then any isomorphismϕ0 : L1−→L2 of lattices extends to a lattice
automorphismϕ : LY−→LY.
