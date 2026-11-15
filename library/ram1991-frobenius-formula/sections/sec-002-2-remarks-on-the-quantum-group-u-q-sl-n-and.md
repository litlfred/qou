---
doc_id: ram1991-frobenius-formula
doc_title: "A Frobenius formula for the characters of the Hecke algebras"
section_id: sec-002-2-remarks-on-the-quantum-group-u-q-sl-n-and
section_title: "Remarks on the quantum group U_q(sl(n)) and the solutions of the quantum Yang-Baxter equation"
section_number: "2"
pages: 4-7
source_pdf: ram1991-frobenius-formula.pdf
source_sha256: 26b2fc85338d9150
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "A Frobenius formula for the characters of the Hecke algebras — This paper uses the theory of quantum groups and the quantum Yang-Baxter equation as a guide in order to produce a method of computing"
---
2 Remarks on the quantum group U.(sl(n)) and the solutions
of the quantum Yang-Baxter equation
The purpose of this section is to describe the algebraic motivation behind the
approach to the characters of the Hecke algebra given in this paper.
In [Jil M. Jimbo describes a reciprocity between, in his notation, the quantum
group U(gl(N + 1)) and the Hecke algebra. In view of the fact that the “modern'
approach to the theory (and notation) of quantum groups and the quantum
Yang-Baxter equation is slightly different from that used in Jimbo's original paper,
I shall endeavor to give a short summary explaining how this reciprocity comes
about. The excellent (and dense) papers [Dr] and [Ji2] contain further information
on quantum groups and the quantum Yang-Baxter equation.
A Frobenius formula for the characters of the Hecke algebras 465
ators ki, ki1, Xt, Xi, 1 ≤i≤ n, and the relations:
k;ki1= k=1k; = 1,
kik; = kjki,
k;Xk=1 = q±aj/2 X,
(2.1)
k? - ki2
[X, Xj] = Oij
XX =X#X, li-jl≥2,
(X) (q+-1)X + X(X)²=0, j=i±l,
where ai = 2, aij = - 1 if j = i ± 1, and aij = 0 if li - jl ≥ 2.
α becomes a Hopf algebra with coproduct : α → α, antipode
S: α -→ α and counit : α → C(q) given by
4(ki) = k;βki， 4(X±)= k;βX + X±βki=1 
S(ki) = ki-1, S(X)= q1X, (2.2)
8(ki) = 1, 8(X±) = 0.
For any invertible element Re& α given by R =Za; bi define
R12, R13, R23 Eα @3 to be the elements
R12 =Za;βb;β1, R13 =aiβ1bi, R23 =1βaibi,
R satisfies the quantum Yang-Baxter equation (QYBE) if
12R1323 = R23R1312 : (2.3)
Let T: α @α -→α @ α be given by
T(a @ b) = b @ a, for all a, beα . (2.4)
R is a universal R-matrix if R satisfies the relations,
T4(a) = R4(a)-1, for all aEα ,
(4 @ id)(R) = R1323 ; (2.5)
(id @ 4)(R) = R13R12 :
If R is a universal R-matrix then R satisfies the QYBE.
Let V -- C(q)" and let Ei; denote the n × n matrix that is 1 in the ith row and jth
column and O everywhere else. The fundamental representation (p, V),
p: αl -→ Endc(q)(V), of Ug(sl(n)) is given by setting
p(X+) = Ei,i+1 ,
p(Xi)= Ei+1,i, (2.6)
p(ki) = qEi + q-1Ei+1,i+1 + Ej:
1 ≤j≤ n
j+,i+1
466 A. Ram
Since &l is a Hopf algebra the tensor representation (p f, vf) is well defined for
every f ≥ 1.
Let R be the universal R-matrix and let R, = p(TR), where Tis as in (2.4). The
form of the matrix R, is well known [Ji2] and is given by
R, =ZqEiβ Eii + Z (q - 1)EuEj + q1/2(Etj @Eji + Eji @Eti) .
i<j
For each 1 ≤i ≤f - 1, define R;e End(V@f) as
R;=1@...@1R,@1...?1,
R appearing as the matrix in the ith and i + 1st factor. Writing the QYBE (2.3) in
terms of the matrices R; gives that
R,Ri+1R; = R;+1 R,R;+1 ,
which implies that the R; satisfy the braid relation (B2) in the definition of the
Hecke algebra. Jimbo [Jil noticed that defining a map π: H, -→ Endc(q) (V) given
by π(gi) -- R; gives a representation of the Hecke algebra Hf :
The first equality in (2.5) can be used to show that matrices R; all commute with
the elements of p J(). Jimbo [Ji] observed that the algebras π(H y) and p @(α)
are mutual commutants of one another. This given, the double centralizer theory
gives that
(2.7) Theorem. As an H,  Ug(sl(n)) representation
vf=
aff
t(a)n
where Ha is a irreducible Hf representation and Va is an irreducible Ug(sl(n))
representation.
Remark. Actually Theorem (2.7) follows from the double centralizer theory only
for some parametrization of the irreducible representations of the Hecke algebra.
To show that the correspondence between the irreducibles is as given above with
the conventional indexing of irreducible representations one may use a Zariski
argument to reduce to the classical Schur-Weyl duality between the symmetric
group and the general linear group. An alternate approach is to use the results of s3
to give a proof of Theorem (2.7).
Let I denote the identity matrix and note that the spectral projection
p(ki) -q-1I ,p(ki) - I
Ei
q1
of p(k;) is an element of p(). Since EE p() for every i one has that the matrix
d -- Z; x;Ei is in p(&) for all xi, : : : , xne C(q). Since the value of d depends only
on the elements p(ki) and the k; are grouplike elements in the Hopf algebra .α (i.e.
4(k:) = k; @ k;) we have that the matrix D = d@f is an element of p @(α). I must
give thanks to H. Wenzl for alerting me to this fact.
The results in this paper are obtained by computing explicitly, for certain
special elements T,eHf, the trace of the action of the element
T, @ De H , @ Uq(sl(n) on each side of the isomorphism in Theorem (2.7).
A Frobenius formula for the characters of the Hecke algebras 467
