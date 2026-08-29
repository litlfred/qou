---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-021-41-the-objects-soergel-bimodules
section_title: "The objects: Soergel bimodules"
section_number: 4.1
pages: 20-22
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
In this section we will introduce Soergel bimodules in the baby example A, i.e.
the symmetric group S3. This case is hard enough to start with and most of
the features of general Soergel bimodules are already visible in this example.
Consider the polynomial ring R =R[x,y,z ] (we could replaceR by any ﬁeld
of characteristic different from 2 in this section and the results would stay
true). We have a natural action of S3 on R. The simple reﬂection s inter-
changesx andy. In formulas
s·f(x,y,z ) =f(y,x,z ).
The simple reﬂection r interchangesy and z. So Rs (the subset of R ﬁxed by
the action of s) is the polynomial ringR[x +y,xy,z ] and Rr =R[x,y +z,yz ].
The subring ﬁxed by both simple reﬂections s and r (or, what is the same, by
the whole groupS3) is
Rs,r =R[x +y +z,xy +xz +yz,xyz ].
20
If we want to enter into Soergel-bimoduland (this is an invented word) we
have to take the grading into account. For technical reasons we need R to
have the usual Z-grading multiplied by two. So x,y and z will be in degree
2 (there are no elements of odd degree). The polynomials x2 and xz have
degree 4, the polynomial 3xy2z7 has degree 20. And we deﬁne the ring R
shifted “down” by one R(1) by declaring that x is in degree 1, x2 in degree
3 and 3xy2z7 in degree 19. Formally, if B =⊕i∈ZBi is a graded object, we
declare that the shifted objectB(m) in degreei isB(m)i :=Bm+i.
The Z-graded R−bimodule R is the easiest example of a Soergel bimodule.
The second example of a Soergel bimodule is the Z-graded R−bimodules
Bs := R⊗Rs R(1), for s∈ S . Just for pedagogical reasons we insist that in
Bs the elements x⊗y and z2⊗ 1 + 1⊗xz have degree 3 and x3⊗zx has
degree 9.
Another example is the product Bs⊗RBr , that we will call (for reasons that
will be clear later) Bsr. Another example of a Soergel bimodule for S3 is the
Z-gradedR−bimoduleBsrs :=R⊗Rs,r R(3).
We will use the convention that ifM and N are twoR−bimodules then their
“product” is deﬁned by
MN :=M⊗RN.
We can now introduce the category of Soergel bimodules B(S3) in our baby
example S3. They are Z-graded R−bimodules that are isomorphic to direct
sums and grading shifts of the following set ofZ-gradedR−bimodules
I ={R,B s,B r,B sr,B rs,B srs}.
Philosphy: One should think of Bs, BsBr and Bsrs as analogous objects to the
elements bs, bsr and bsrs respectively in the Hecke algebra. One should also think of
the product (resp. direct sum) between Soergel bimodules as an analogue of product
(resp. sum) in the Hecke algebra. Shifting the degree of a Soergel bimodule by one
should be seen as multiplying the corresponding element in the Hecke algebra by v.
We will make this statement precise at some point.
This philosophy will gently emerge in the following pages. Recall that the
Hecke algebraH(S3) is free overZ[v,v−1] with basis
{1,b s,b r,b sr,b rs,b srs}.
21
