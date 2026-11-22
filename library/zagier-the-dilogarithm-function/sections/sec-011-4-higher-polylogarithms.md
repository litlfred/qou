---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-011-4-higher-polylogarithms
section_title: "Higher polylogarithms"
section_number: 4
pages: 56-61
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
In Chapter I we already introduced the higher polylogarithm functions Lim(z),
their one-valued modiﬁcations Dm(z), and the idea that there might be rela-
tions among special values of Dedekind zeta functions at integral arguments
and the values of polylogarithms at algebraic arguments, analogous to those
existing for the dilogarithm. But at the time when that text was written, I
knew only a few sporadic results, and the chapter ends with the sentence “the
general picture is not yet clear.” After it was written I did a lot of numeri-
cal calculations with special values of higher polylogarithm functions and was
able to formulate a general conjecture which has now been proved in a small
number and numerically veriﬁed in a large number of cases. Since there are
already several expositions of these conjectures ([45], [46], Chapter 1 of [47]), I
The Dilogarithm Function
59
give only a sketch here, the more so because higher polylogarithms seem so far
to play much less of a role in mathematical physics than the dilogarithm. (See,
however, [35].) Nevertheless, the higher polylogarithm story is very pretty and
it seemed a pity to omit it entirely.
We describe the conjectures in Section A and some supporting examples
in Section B. It turns out that the theory works better if one replaces the
function Dm(z) deﬁned in Chapter I by the slightly diﬀerent function
Lm(z) = ℜm
 m−1

k=0
Bk
(log |z|2)k
k!
Lim−k(z)

,
where ℜm denotes ℜfor m odd and ℑfor m even and Bk is the kth Bernoulli
number. Thus L2(z) = D2(z) = D(z), but L3(z) = D3(z)+ 1
6 log2 |z| log
 1−z
√z
.
Like Dm, Lm is a single-valued real-analytic function on P1(C) ∖{0, 1, ∞},
but it is has the advantages of being continuous at the three singular points,
of having clean functional equations (for instance, the logarithmic terms in
the two functional equations for D3 given in §3 of Chapter I are absent when
these are written in terms of L3), and of leading to a simpler formulation of
the conjectures relating the polylogarithms to zeta values and to algebraic
K-theory.
A. Higher Bloch groups and higher K-groups. In Chapter I we deﬁned
the Bloch group B(F) of a ﬁeld F (where we have changed the notation from
the previous BF , because we will have higher Bloch groups Bm(F) as well)
as A(F)/C(F), where A(F) is the set of all elements ξ = 
 ni[xi] ∈Z[F]
satisfying ∂(ξ) := 
 ni(xi) ∧(1 −xi) = 0 and C(F) the subgroup generated
by the ﬁve-term relations V (x, y) and by its degenerations [x] + [1/x] and
[x]+[1−x]. Because the elements of C(C) are in the kernel of the Bloch-Wigner
dilogarithm D we have a map D : B(C) →R. The key statement is that for a
number ﬁeld F of degree r1+2r2 over Q (r1 real and 2r2 complex embeddings),
the group B(F) has rank r2 and the map LF : B(F)/(torsion) →Rr2 induced
by the values of D on the various conjugates of ξ ∈B(F) (there are only r2
essentially diﬀerent such values because D(¯x) = −D(x) ) is an isomorphism
onto a lattice whose covolume is essentially equal to ζF (2).
The conjectural picture for the mth polylogarithm, m ≥3, is that we can
introduce similarly deﬁned higher Bloch groups Bm(F) = Am(F)/Cm(F),
where Am(F) is a suitably deﬁned subgroup of Z[F] and Cm(F) ⊆Am(F)
is the subgroup corresponding to the functional equations of the higher poly-
logarithm function Lm, in such a way that the rank of Bm(F) is equal to
r2 or r1 + r2 (depending whether m is even or odd) and that the map
Lm,F : Bm(F)/(torsion) →R(r1+)r2 induced by the values of Lm on the
various conjugates of ξ ∈Z[F] is an isomorphism onto a lattice of ﬁnite co-
volume. (Note that Lm(¯x) = (−1)m−1Lm(x), which is why there are only r2
essentially diﬀerent values of Lm if m is even, but r1 + r2 if m is odd.) Again,
this implies the existence of numerous Q-linear relations among the values of
60
Don Zagier
Lm(x), x ∈F. Moreover, the covolume of the lattice Im(Lm,F ) is supposed to
be a simple multiple of ζF (m), so that one also obtains (conjectural) formulas
for the values of the Dedekind zeta functions of arbitrary number ﬁelds at
s = m in terms of the mth polylogarithm function with algebraic arguments.
Furthermore, the whole picture is supposed to correspond to the higher
K-groups of F, as already mentioned at the end of Chapter I. For each i ≥0
one has K-groups Ki(F) and Ki(OF ) which for i ≥2 become isomorphic
after tensoring with Q. The group Ki(OF ) is ﬁnitely generated and its rank
was determined by Borel [5]: it is 0 for i even and is r2 or r1 + r2 (depending
as before whether m is even or odd) if i = 2m −1, m ≥2. Moreover, Borel
showed that there is a natural “regulator” map Rm,F : K2m−1(F) →R(r1+)r2
which gives an isomorphism of K2m−1(F)/(torsion) onto a sublattice whose
covolume is a simple multiple of ζF (m). The motivation for the polylogarithm
conjectures as stated above is that we expect there to be an isomorphism
(at least after tensoring with Q) between K2m−1(F) and Bm(F) such that
the Borel regulator map Rm,F and the polylogarithm map Lm,F correspond.
This is not known at all in general, but de Jeu [12] and Beilinson–Deligne [2]
deﬁned a map compatible with Rm,F and Lm,F from (a version of) Bm(F) to
K2m−1(F), and for m = 3 Goncharov [20] proved the surjectivity of this map,
establishing in this special case my conjecture that ζF (3) for any number ﬁeld
F can be expressed in terms of polylogarithms.
In the rest of this subsection, we describe the inductive deﬁnition of the
groups Bm(F) in a way which is algorithmically workable, though theoretically
unfounded.
The ﬁrst case is m = 3. A ﬁrst candidate for A3(F) is Ker(∂3), where
∂3 : Z[F] →F × ⊗Λ2F × is the map sending [x] to (x) ⊗((x) ∧(1 −x)) if
x̸ = 0, 1 (and to 0 if x = 0 or 1). If this deﬁnition and the above hypothetical
statements are correct, we deduce—even without knowing the deﬁnitions of
C3(F) and B3(F)—that any r1 + r2 + 1 values L3(σ(x)), where σ : F →C
is a ﬁxed embedding and x ranges over values in F, should be Q-linearly
dependent. Numerical evidence supported this for totally real ﬁelds. For in-
stance, if F = Q(
√
5) then the three one-term elements [1], [(1 +
√
5)/2] and
[(1 −
√
5)/2] belong to Ker(∂3) and we ﬁnd (numerically, but here provably)
that L3
 1+
√
5
2

+L3
 1−
√
5
2

= 1
5 L3(1). For r2 > 0, however, the correct A3(F)
turns out to be a subgroup of Ker(∂3), as we now explain.
Let φ be any homomorphism from F × to Z. If ξ = 
 ni[xi] belongs to
Ker(∂3), then the element ιφ(ξ) = 
 niφ(xi)[xi] of Z[F] belongs to Ker(∂),
as is easily checked, so ιφ(ξ) ∈A2(F). The additional requirement for ξ to
belong to A3(F) is then that ιφ(ξ), for every φ, should belong to the subgroup
C2(F) = C(F) of A2(F) = A(F). Since we know that elements of the quotient
B2(F) = A2(F)/C2(F) are detected (up to torsion) by the values of D on the
various conjugates, we can check this condition numerically by calculating
D(σ(ιφ(ξ))) for all embeddings σ : F →C. This gives at least an algorithmic
way to get A3(F).
The Dilogarithm Function
61
The construction of C3(F), and of the higher Am and Cm groups, now
proceeds by induction on m, assuming at each stage that the conjectural
picture as described above holds. We would like to deﬁne each Cm(F) as
the free abelian group generated by the specialization to F of all functional
equations of Lm, but we cannot do this because these functional equations are
not known except for m = 2. (Goncharov [20] has given a functional equation
for m = 3 which is conjectured, but not known, to be generic, and Gangl [16]
has given isolated functional equations up to m = 7, but for higher m nothing
is known.) Instead we proceed as follows. We deﬁne A3(F) as above and let
L3,F : A3(F) →Rr1+r2 be the map sending 
 ni[xi] to

 niL3(σ(xi))

σ . If
the conjectures are correct, then the image of this map should be a lattice of
full rank r1 + r2 and the kernel (at least up to torsion) should be C3(F). The
ﬁrst statement can be checked empirically by computing L3,F (ξ) numerically
for a large number of elements ξ of A3(F). If all is well—and in practice
it is—we soon ﬁnd that these vectors, to high precision, are all elements of
a certain lattice (of full rank) L3 ⊂Rr1+r2. This conﬁrms the conjecture
and at the same time allows us to deﬁne C3(F) as the set of ξ ∈A3(F)
whose image under L3,F is the zero vector of L3, something which can be
veriﬁed numerically because L3 ⊂Rr1+r2 is discrete. The deﬁnition of the
higher groups Am(F) and Cm(F) now proceeds the same way. Once we know
Cm−1(F), we deﬁne Am(F) as the set of ξ ∈Z[F] for which ιφ(ξ) belongs
to Cm−1(F) for every homomorphism φ : F × →Z. (This is automatically a
subgroup of Ker(∂m), where ∂m : Z[F] →Symm−2(F ×)⊗Λ2(F ×) takes [x] to
(x)m−1⊗((x)∧(1−x)), so in practise we start by ﬁnding elements of Ker(∂m)
and only check the condition ιφ(ξ) ∈Cm−1(F) for these. Note also that for a
given ξ = 
 ni[xi] the condition on ιφ(ξ) only has to be checked for ﬁnitely
many maps φ, namely for a basis of the dual group of the group generated
by the xi.) We then deﬁne Lm,F : Am(F) →R(r1+)r2 as before and compute
the images of many elements of Am(F) under Lm,F to high precision. If the
image vectors do not lie in some lattice Lm ⊂R(r1+)r2 within the precision
of the calculation, then the conjectural picture is wrong and we stop. If they
do—and in practise this always happens—then we deﬁne Cm(F) as the kernel
of the map Lm,F from Am(F) to the discrete group Lm ≈Z(r1+)r2, and the
mth Bloch group Bm(F) as the quotient Am(F)/Cm(F).
B. Examples. We start with a numerical example for m = 3 showing that the
condition ∂3(ξ) = 0 is not enough to ensure ξ ∈A3(F) when F is not totally
real. Let θ be the real root of θ3−θ−1 = 0. The ﬁeld F = Q(θ) has r1 = r2 = 1.
The six numbers x0 = 1, x1 = θ, x2 = −θ, x3 = θ3, x4 = −θ4 and x5 = θ5 have
the property that xi and 1−xi belong to the group generated by −1 and θ. (So
does θ2, but its polylogarithms of all orders are related to those of θ and −θ by
the “distribution” property of polylogarithms, so we have omitted it.) Hence
∂3(xi) = 0 (up to torsion) for each i, but numerically we ﬁnd that 3 of the 6
vectors L3,F (xi) = (L3(xi), L3(x′
i)) ∈R2 (where ′ denotes one of the non-real
embeddings of F into C) are linearly independent, rather than only r1 + r2 =
62
Don Zagier
2. If we observe that D(x′
i) = ℓiD(θ′) with (ℓ0, . . . , ℓ5) = (0, 1, −1, 2, 1, −1)
and that the values of φ(xi) for any φ : F × →Z are proportional to the
integers (m0, . . . , m5) = (0, 1, 1, 3, 4, 5), then we ﬁnd that the condition for an
integral linear combination ξ = 
 ni[xi] of the [xi]’s to belong to A3(F) is
that 
i ℓimini = 0. These elements form an abelian group of rank 5 whose
image in R2 under the map L3,F : [x] →(L3(x), L3(x′)) now does turn out
numerically to be a lattice L3 of rank 2, as predicted, with the covolume
of L3 being related to ζF (3) in the expected way. Moreover, since we now
have a rank 3 group of elements mapping to 0 in L3, and since the space of
relevant maps φ is only 1-dimensional, we can continue the inductive process
for two more steps with the same elements xi, obtaining ﬁnally two elements
[x0] and [x5] −5([x4] −[x3] + 46[x2] + 57[x1] + [x0]) whose images under the
map L5,F : [x] →(L5(x), L5(x′)) from Z[F] to R2 are ζ(5)
 1
1

and (to high
precision) 2−7π−5239/2ζF (5)ζ(5)−1 −2
1

, respectively.
In general, in order to construct elements in the higher Bloch groups of a
number ﬁeld F, we have to ﬁnd as many elements xi of F as possible such
that all of the numbers xi and 1 −xi belong to a subgroup G ⊂F × of small
rank. For instance, if we start with F = Q and let G be the rank 2 subgroup
of Q× generated by −1, 2 and 3, then there are exactly 18 elements x ∈Q
for which both x and 1 −x belong to G, namely the numbers 2, 3, 4 and
9 and their images under the group of order 6 generated by x →1/x and
x →1 −x. If we want to make elements of the 3rd Bloch group, we need
only ﬁnd combinations ξ = 
 ni[xi] for which 
 ni(xi) ⊗((xi) ∧(1 −xi))
vanishes: there is no further condition of vanishing in the previous Bloch
group B2(Q) because it is zero (up to torsion). If all xi belong to the set of
18 elements described above, then each element (xi) ⊗((xi) ∧(1 −xi)) is a
linear combination of only two elements (2)⊗((2)∧(3)) and (3)⊗((2)∧(3)) of
Q× ⊗Λ2(Q×). We therefore get many non-trivial elements of B3(Q), a typical
one being [8/9]−3[3/4]−6[2/3], and since B3(Q) is supposed to be of rank 1,
each of them should map under L3 to a rational multiple of ζ(3), something
that can be checked numerically. (For the element just given, for instance, we
ﬁnd L3(8/9) −3L3(3/4) −6L3(2/3) = −91
12ζ(3).) To get interesting examples
for F = Q and higher values of m, we have to allow more prime factors in
xi and 1 −xi. On p. 386 of [46] one can ﬁnd a numerical relation over Z
(conjecturally the only one, and with very large coeﬃcients) among 29 values
L7(xi) where xi ∈Q has only the prime factors 2 and 3 and 1 −xi only the
prime factors 2, 3, 5 and 7.
To get examples for even higher values of m, it is advantageous to go to
higher number ﬁelds and choose all xi to belong to a group ⟨−1, α⟩of rank 1,
where α is chosen to be an algebraic number of very small height, so that there
are as many multiplicative relations as possible among the numbers 1 ± αn
(“ladder”). The algebraic number of conjecturally smallest positive height
(according to the famous Lehmer conjecture) is the root of the 10th degree
equation α10+α9−α7−α6−α5−α4−α3+α+1 = 0. This example was studied
in [10], where 71 multiplicatively independent multiplicative relations were
The Dilogarithm Function
63
found among the numbers α and 1−αn (n ∈N), the largest n occurring in such
a relation being 360, and these were used to detect numerical polylogarithm
relations up to m = 16. Subsequently, Bailey and Broadhurst [6] noticed that
there was one further multiplicative relation (this one with n = 630), and used
it to ﬁnd a relation among values of polylogarithms of order 17, the present
world record.
