---
doc_id: schechtman-varchenko1991-arrangements
doc_title: "Arrangements of hyperplanes and Lie algebra homology"
section_id: sec-004-4-topology
section_title: "Topology"
section_number: "4"
pages: 19-25
source_pdf: schechtman-varchenko1991-arrangements.pdf
source_sha256: 0100fd32438740f0
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "Arrangements of hyperplanes and Lie algebra homology — 10 sections: Front matter; Introduction; Orlik-Solomon algebra (Part I. Coh"
---
4 Topology
Let  be an arrangement in V, dim V - N. Put Y() =- () H  V; U()= V/Y()
4.1 Orlik-Solomon theorem. Denote by 2'(U() the de Rham complex of holo-
morphic forms over U(6). One has canonical isomorphism
(4.1.1) H(2(U()=H(U (); C)
For any He& choose an affine equation t =O of H; assign to H a l-form
(4.1.2) (H) = d log teQ (U (C)
i(H) doesn't depend on the choice of tu. This assignment defines an inclusion
of graded -algebras
(4.1.3) (%)n).0←(). :1
which is compatible with differentials if we imply the zero differential on α'()
[Br, OS].
4.1.4 Theorem (Brieskorn-Orlik-Solomon). 1 is a quasi-isomorphism, i.e. it induces
the isomorphism
α()= H(U(); C
which maps P()z isomorphically to HP(U(); (2πi)PZ)
Proof. Follows from [Br, OS] and 1.3.2.
4.1.5 Corollary.
(Z:(%)n);H -N(I -)  =(%)X
i-0
4.2 For a topological space X denote by C.(X) (resp., C(X)) the complex of
integer-valued singular chains (resp., cochains) of X. Put C.(V, Y(C):=C.(V)
*(((%)X 4)0)=(%)X ).0 (%)X)0
158 V.V. Schechtman and A.N. Varchenko
The aim of this and the next n° is to construct (well defined up to a homotopy)
quasiisomorphisms
C (V, Y() -→(g(C)z, d).
For an edge L of 6 put
(4.2.1) L=L\(U HL); (%)n= 0A
%3H
H+L
Let us call a marking x of  a choice of a point x(L)eL for every edge
L (including V). Fix such a marking x. To every flag F-(L  ... LP), Liegit;
let us assign the singular p-simplex 4(F)=△x(F): P-→V, where 4p
= (to, ..., t,)eIRp+1 It;≥0; Zt; = 1) is the standard oriented p-simplex. Namely,
if x; -(0, ... 0, 1, 0... 0) with 1 on i-th place, put
(4.2.2) 4(F)(x;) = x(L) 4(F)(0) = x(V),
and extend this map to △p by IR-affinity.
Now define maps
(4.2.3) uP =uP: CP(V, Y(C) -→P(C)z
by the rule
(4.2.4) uP(β) = Φ(4(F)
FeFIP(C)
for βeCp(V, Y(). One verifies directly that up define the map of complexes
(4.2.5) u =ux: C'(V, Y() -→(g'(C)z, d)
4.2.6 Lemma. Any pair of markings x, x' defines a canonical homotopy
(4.2.6.1) h(x, x): C(V, Y() -→(C)z[- 1]
between ux and ux. In particular, the map induced by (4.2.5) in homology is indepen-
dent of the choice of the marking.
For a triple of markings x, x', x" h(x, x')+ h(x', x) is homotopic to h(x, x").
(Recall that for a graded group A = @ AP A[n] denotes the shifted graded group
(A[n])P= Ap+n)
Proof. To construct h(x, x'), it is sufficient to suppose that x(L)= x'(L) for all
edges L except for a one. Suppose for example that x(L) = x'(L) for all L except
() s()  )    ss     
- an affine span of (x'(V), x(V), x(L), ..:, x(LP). This defines the map (4.2.6.1).
Details are left to the reader.
4.3 Theorem. Maps (4.2.5) are quasisomorphisms
Proof. We'll prove that the adjoint maps
(4.3.1) u*: (α'(C)z, d*) -→C.(V, Y(C))
are quasiisomorphisms.
Arrangements of hyperplanes and Lie algebra homology 159
Let us choose some linear order on 6. Consider the bicomplex C.. with
Cpq= Cp(Hi,n...nHi.);
i1 <...<iq
Cpo = Cp(V).
Differentials Cpg →Cp-1,g are boundary operators is C., and Cpq →Cp.q-1
are Cech differentiais. Denote by Tot C.. the corresponding simple complex.
We have evident map Tot C.. -→C.(V, Y(6) which is quasisomorphism by
Mayer-Vietoris. The spectral sequence associated with C.. degenerates at E1
and E1 is isomorphic to the complex (8.(6), ), studied in 1.9. So, by 1.9.6
we have canonical isomorphisms H'(αl ()z, d*) = H.(V, Y().
Any marking of  induces the map .'()z-→ Tot C.. whose composition
with Tot C.. -→C.(V, Y() is equal to the map (4.3.1). One easily sees that the
induced map in homology is inverse to the one constructed by using the spectral
sequence.
4.4 By 4.1.4 and 2.4 we have natural isomorphisms
(4.4.1) g P(C)z= H,(U(C), Z).
Let us construct these isomorphisms explicitly. Namely, to each flag F -
(Ll  ...  LP) we associate a map (defined up to a homotopy)
(4.4.2) c(F): (SI)P → U(C)
from a p-dimensional torus to U(). The image under c(F) of a canonical genera-
tor of H,((S1)p, Z) in H,(U(), Z) will give the map (4.4.1).
We define c(F) by induction on p. For p=1 it is a small circle around
Ll. For p>1 c(F) is a product of a circle around Ll by c(F') where F'=
(L? - ...  LP) considered as a flag in Ll.
Alternatively, one may define c(F) as follows. Suppose that p= N. Choose
some He such that HLN-1 - LN. Such a choice defines a diffeomorphism
of U(6)(small neighbourhood of L) with C* × U() where  - H (see 1.4).
We put c(F) to be the product of a circle around zero in C* by c(Ll - ...  LN -1):
(S )p- 1 -→ U() defined by induction.
From the second description one can show that
(4.4.3)  1(Hi... H,)=(-1)loj
c(F)
if F = F(Ho(1), .., Ho(p) for some ceZp, and zero otherwise. It follows that
the assignment F>c(F) induces the isomorphism (4.4.1). Note that we have
obtained the geometric interpretation of isomorphisms 2.3.3.
4.5 Now suppose that a collection of exponents a: & -→C is given. Denote by
(a) a line bundle over U() with an integrable connection which is trivial
as a bundle and whose connection
(4.5.1) d(a): 0 →21
is equal to d+i(o)=d+ ZH a(H) d log tH, d being the de Rham differential.
Denote by 2'((a) the complex of U(%)-sections of the holomorphic de Rham
160 V.V. Schechtman and A.N. Varchenko
complex of (a). Thus, 2'((a) = 2'(U() as a graded vector space, with the
differential d(a),
(4.5.2) d(a)(x)=d x + i() ^ x.
We'll denote by (a) the sheaf (over U() of horizontal sections of (a).
Thus, we have the de Rham isomorphism
(4.5.3) H(2((a)= H(U(); (a)
The inclusion (4.1.3) induces the map of complexes
(4.5.4) 1(a): (α (), d(a) -→2((a)
When a =O, we return to the situation of n° 4.1. Simple examples for dim V
 1 show that (4.5.4) is not always a quasisomorphism.
(aa)(H) =- aa(H). Here is the main result of this section.
4.6 Theorem. There exists an open set Wc  containing O, which is a complement
of the set of zeroes of some holomorphic function and such that i(aa) is a quasiiso-
morphism for all Ae W.
Proof. Let us choose a finite subcomplex X U() such that this inclusion
is a homotopy equivalence. Let us consider the cochain complex of X with
coefficients in (aa): C'=C(X; (aa)lx). Let us choose over each cell of X
branches of logth for all He&. This gives branches of taa
:= II exp(aa(H) log th), hence a base in each finite dimensional space Cp, enu-
merated by p-cells of X. Differentials d(2): Cp -→Cp+1 are matrices with entries
of the form ±exp(ab), beC.
By the de Rham theorem, the integration map
(4.6.1) f: 2((aa)→C
is a quasiisomorphism. Denote by
(4.6.2) I(2): (α(), ad(a) -→(C, d(2)
the composition of i(aa) and (4.6.1).
I(a) is a map of complexes of finite dimensional vector spaces. I(a) may
be represented as a convergent in some neighbourhood of O power series
(4.6.3) I(a)= Z I;·2i.
0=1
The same is true for d(a):
(4.6.4) d(a)= Z d;·ai.
i=0
Arrangements of hyperplanes and Lie algebra homology 161
4.6.5 Lemma. Let (A', d(2) be a complex of finite dimensional complex vector
spaces with the differential depending on a complex parameter a holomorphic in
a neighbourhood of zero. Suppose that (A', d(O) is acyclic.
Then (A', d(2) is acyclic for sufficiently small 2.
Proof. Let d(2)= Z d; ai be the Taylor series of d(2) at 0. We have d(a)2 =0
i≥0
which means that
(4.6.5.1)  d,di-p=0
p=0
for all i≥0.
Let us consider the space of cocycles Zp(2)-Ker(dp(2): AP -→ Ap+1). One
can see that Zp(2) for sufficiently small a is generated by x(2)= Z x; i, MeZ,
Wz!
such that d(a)x(2)=O. Let x(2) be such a cocycle; we have to show that it
is a coboundary for small 2. Multiplying it by aM we may suppose that M -O,
i.e. x(2)- Z x; ai. We have
i≥0
(4.6.5.2)  d,Xi-p=0
p=0
for all i≥0.
Let us look for y(a)= Z y; ai such that
1≥0
(4.6.5.3) d(2) y(2) = x(2)
Step I. There exists a formal solution of (4.6.5.3). In fact, (4.6.5.3) is equivalent
to the infinite system
(4.6.5.3); Z dpyi-p=xi,
p=0
i≥O. Let us solve it by induction on i. We have do xo=O, so xo=do yo for
some yo since (A', do) is acyclic. Suppose we have solved (4.6.5.3) for i<k. We
have to find yk such that
(4.6.5.4) Xk=dk yo +dk-1 y1 +... +do Yk.
It suffices to show that
do(xk-  dn yk-n)
h= 1
162 V.V. Schechtman and A.N. Varchenko
We have by induction
ki
do X=- d; xk-i=-  did, yk-i-p
i1 i=1 p=0
k-1
Z dn- dp) yk-n=  do d yk-n.
n= 1 n= 1
and we are done.
Step II. We can choose a solution y(2) to (4.6.5.3) convergent in a neighbourhood
of zero.
A, M>1 such that Ixil, Id;l<AMi for all i. On every step of solving (4.6.5.4)
we solve an equation of the form x=do y. We may suppose that, given x such
that do x =O, we choose y such that lyl≤Mlxl. Then one shows by induction
that lyil< A 2i M2i+1. The Lemma is proved.
4.6.6 Corollary. Let f(a): (A', d(2) -→(A', d'(2) be a map of complexes of finite
dimensional complex vector spaces with f (2), d(2), d'(2) depending holomorphically
on a for small 2. Suppose that f (O) is a quasiisomorphism.
Then f (a) is a quasisomorphism for small a.
Proof. Apply 4.6.5 to the cone of f (a).
Now, applying the above corollary to I(2) (4.6.2) we get the assertion of
Theorem 4.6.
4.6.7 Remark. The idea of the above proof arose from the discussion with Misha
Kapranov who explained to us the work [NJ. We are very gratefull to him.
4.6.8 Remark. Theorem 4.6 proves a weak form of a conjecture made by Aomoto
[A].
4.7 Remarks on relative cohomology. Let us denote by C.t y(U(6); (a) the
complex of complex singular chains whose symplices may have a boundary
on Y(). Let C: f be the corresponding cochain complex. By definition
(4.7.1) H(Cr(U(); (a) = H(V, j: (a)
where j: U()  V.
Fix a marking x of  as in 4.2, and branches of log tu, he in a neighbour-
hood of x(V). Then the rule (4.2.4) defines the map of complexes
(4.7.2) u(a): Cis(U(6); (a) →(g(C), d),
It seems very probable that it is always a quasiisomorphism (cf. 4.3)
Consider a symplex △(F) for some FeF[p(). Put as usually taa--
II exp(aa(H) log th)
Arrangements of hyperplanes and Lie algebra homology 163
4.7.3 Lemma. Suppose that a(F)+0 (cf. (3.4.1). For any H1, ..., H,e6
S1(Hi ... H,) taa +0(α-p+1) )(α→0)
4(F)
where
( 1)0l
a(F)
if F = F(He(1), ..., Ho(p) for some eZp, and A =0 otherwise (cf. 3.4.2).
Proof. The case p= 1 is elementary. The general case is reduced to the p-th
power of this one, using the monoidal transformation associated with F. 
Suppose that  has a vertex, dim V -- N. Consider the canonical map
S(aa): HN(V,j. S(aa)-→ HN(V, jx (aa)
Suppose that (4.7.2) is a quasisomorphism, and a(L)+0 for every edge L
of &.
If we identify HN(V, j (aa) with HN('() and HN(V, j* (aa) with
Hn(l'(), d(aa) for small 2 by 4.6, then from 4.7.3 and 3.4.4 follows that
(4.7.4) S(aa) =aN s(a)+O(aN-1) (2→0)
(Note that SN(aa)= aN sN(a).)
Presumably, the same holds without the assumption that a(L)+O for
all L.
4.8 Remarks on Jantzen filtration. Using the form S(a), one can define the Jant-
it gives in particular the usual Jantzen filtration on Verma modules. Consider
an arrangement @ defined after (1.4.2). Put a(H ) - Z a(H). We have l(@)=
'()@ '() [1]. Suppose that conditions of 4.6 fulfilled, so that we can iden-
tify H'('(), d(a) with H'(U (),  (a). It seems then plausible that the filtration
on H'('() [1]) induced by the Jantzen filtration on H'('() coincides with
the weight filtration on H'(U(); (a) when the last one is defined. cf. [BB,
$ 51.
( ) ())   s    ! d 
with the Goresky-MacPherson cohomology H'(U(6); j* (a).
