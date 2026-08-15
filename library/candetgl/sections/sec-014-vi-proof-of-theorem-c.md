---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-014-vi-proof-of-theorem-c
section_title: "PROOF OF THEOREM C"
section_number: VI
pages: 21-23
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
A. Statement and proof of Theorem C
Recall the statement:
Theorem C: The image of the Biot –Savart operator is a proper subspace of the image of
curl, whose orthogonal projection into the subspace of ‘‘ﬂuxless knots’’ is one-to-one .
This will follow immediately from Theorems B and B 8 and ~borrowing from the future! from
Theorem D.
Proof:
Keep in mind the Hodge decomposition,
VF~V!5FK% HK% CG% HG% GG. ~6.1!
We know from Theorem B that the kernel of the Biot–Savart operator BS is the subspace
HG%GG of VF ~V!.
We know from Theorem D that this operator is self-adjoint.
It follows that the image of BS lies within the orthogonal complement of its kernel, that is,
within the subspace FK
% HK% CG, which is precisely the image of curl.
895J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
Alternatively, the formula „ 3A(V)5BS(V), which appeared as item ~4! on our list of
Standard Information in Sec. III A, also tells us that the image of BS lies within the image of curl.
Now it follows from Theorems B and B 8 together that
Image~BS!øKer~curl!5$0%, ~6.2!
and since, by the Hodge Decomposition Theorem, the kernel of curl is HK % CG% HG% GG, the
orthogonal projection of the image of BS into FK must be one-to-one.
From this it also follows that the image of the BS is a proper subspace of the image of curl.
This completes the proof of Theorem C.
B. Impossible magnetic ﬁelds
We are looking for smooth vector ﬁelds U on a compact, smoothly bounded domain V in
3-space, for which it is impossible to ﬁnd a smooth vector ﬁeld V on V satisfying the equation
U5BS(V). We will call such a ﬁeld U an impossible magnetic ﬁeld.
Of course, Eq. ~6.2! tells us that any nonzero vector ﬁeld U in HK % CG% HG% GG is an
impossible magnetic ﬁeld.
But here is a more interesting example.
Consider the velocity vector ﬁeld U of a ‘‘speeding bullet,’’ as pictured below ~see Fig. 3 !.
We visualize the unit ball V in 3-space as a lead bullet sitting in a cartridge which has been
shot directly upwards from a riﬂed barrel, so that it spins as it moves forward. In cylindrical
coordinates r,
w, z, the velocity vector ﬁeld U is given by
U5rwˆ1zˆ. ~6.3!
Note that the ﬁrst summand rwˆ lies in FK, while the second summand zˆ lies in CG.
Now look back to Example 1 in Sec. III C. There we started with the vector ﬁeld V5zˆ on the
unit ball V and computed its magnetic ﬁeld within the ball,
FIG. 3. An impossible magnetic ﬁeld on the unit ball V.
896 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
BS~V! 5~1/3!r sin uwˆ ~spherical coordinates !
5~1/3!rwˆ ~cylindrical coordinates !. ~6.4!
So of course ~settling back to cylindrical coordinates !,
BS~3V!5rwˆ. ~6.5!
But this magnetic ﬁeld on the unit ball ‘‘poisons’’ U as a candidate magnetic ﬁeld, since U and
BS(3 V) have the same orthogonal projection into the space FK of ﬂuxless knots. By Theorem C,
the vector ﬁeld U cannot possibly be the Biot–Savart transform of any smooth vector ﬁeld on V.
