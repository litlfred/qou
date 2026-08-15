---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-017-32-independence-of-a-choice-of-quad-type
section_title: "Independence of a choice of quad type"
section_number: 3.2
pages: 16-17
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
lationT with N tetrahedra, and an enhanced Neumann-Zagier datum ˆβT = (z, A, B,f ).
To prove independence of quad type, it is suﬃcient to check that τT is invariant under a
cyclic permutation of the ﬁrst triple of shape parameters ( z1,z ′
1,z ′′
1 ), while holding ﬁxed the
choice of meridian loop and redundant edge. Let us write z = (z1,...,z N ),ν = (ν1,...,ν N )T ,
f = (f1,...,f N )T , and
(3.3) A =
(
a1, a2,··· ,a N
)
, B =
(
b1, b2,··· ,b N
)
,
in column notation. After the permutation, a new Neumann-Zagier d atum is given by
(~z,~A, ~B,~f ) where
(3.4) ~z = (z′
1,z 2,...,z N ), ~z′ = (z′′
1,z ′
2,...,z ′
N ), ~z′′ = (z1,z ′′
2,...,z ′′
N ),
(3.5) ~A =
(
−b1, a2,··· ,a N
)
, ~B =
(
a1−b1, b2,··· ,b N
)
, ~ν = (n1−b1,n 2,...,n N )T.
The new shapes satisfy ~z ˜A~z′′ ˜B = (−1)˜ν . We also naturally obtain a new ﬂattening ( ~f, ~f ′,~f ′′)
by permuting
(3.6) ~f = (f ′
1,f 2,...,f N )T, ~f ′ = (f ′′
1,f ′
2,...,f ′
N )T, ~f ′′ = (f1,f ′′
2,...,f ′′
N )T ;
this is an integer solution to ~A ˜f +~B ˜f ′′ =~ν and ˜f + ˜f ′ + ˜f ′′ = 1.
The torsion τT (
1.8) consists of two parts, a determinant and a monomial correction. By
making use of the relations z1 +z′
1
−1− 1 = 0 and z1z′
1z′′
1 =−1, we ﬁnd the determinant with
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 17
the permuted Neumann-Zagier datum to be
det
(~A∆ ˜z′′ +~B∆ −1
˜z
)
= det
(
−b1z1 + (a1−b1)z′−1
1 , a2z′′
2 +b2z−1
2 ,··· , aNz′′
N +bNz−1
N
)
= det
(
a1z′−1
1 −b1, a2z′′
2 +b2z−1
2 ,··· , aNz′′
N +bNz−1
N
)
=−z1 det
(
a1z′′
1 +b1z−1
1 , a2z′′
2 +b2z−1
2 ,··· , aNz′′
N +bNz−1
N
)
=−z1 det
(
A∆ z′′ + B∆ −1
z
)
.(3.7)
By simply using z1z′
1z′′
1 =−1 and f1 +f ′
1 +f ′′
1 = 1, we also see that the monomial correction
transforms as
~z
˜f ′′
~z′′− ˜f =zf ′′
z′′−fz′
1
f1z1−f ′
1
z1f ′′
1z′′
1
−f1
=zf ′′
z′′−f (−1)f1 (z1z′′
1 )−f1z1f1+f ′′
1 −1
z1f ′′
1z′′
1 −f1
=zf ′′
z′′−f (−1)f1z−1
1 .(3.8)
The extra factors z±1
1 in the two parts of the torsion precisely cancel each other, leading in
the end to
(3.9) det
(~A∆ ˜z′′ +~B∆ −1
˜z
)
~z
˜f ′′
~z′′− ˜f = (−1)f1+1 det
(
A∆ z′′ + B∆ −1
z
)
zf ′′
z′′−f.
This is just as desired, showing that the torsion is invariant up to a sig n.
