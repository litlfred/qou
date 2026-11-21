---
doc_id: reshetikhin-turaev
doc_title: "Ribbon graphs and their invariants derived from quantum groups"
section_id: sec-002-3-quasitriangular-and-ribbon-hopf-algebras
section_title: "Quasitriangular and Ribbon Hopf Algebras"
section_number: 3
pages: 4-8
source_pdf: Reshetikhin_Turaev.pdf
source_sha256: 7ead97555a25d357
toc_source: inferred
doc_brief: "Ribbon graphs and their invariants derived from quantum groups — The generalization of Jones polynomial of links to the case of graphs in R 3 is presented."
---
3.1. Quasitriangular HopfAlgebras (see [Dr]). Let A be a Hopf algebra with the 
comultiplication A, counit ~ and antipodal mapping s. Let R be an invertible 
element 
of 
A |174 
Denote 
the 
permutation 
homomorphism 
a|174 
: A|174 
by P. The pair (A, R) is called a quasitriangular Hopf 
Ribbon Graphs Derived from Their Invariants 
algebra if for any a ~ A, 
A'(a)=RA(a)R -~ , 
(A | 
(R) -- R 13R23, 
(id a| 
(R) = R 13R12. 
(3.1.1) 
(3.1.2) 
(3.1.3) 
Here A'= Po A, R12 ~- R@ I s A | 
Rls =Od@ P)(R~2), R23 =-1 | 
Note that ifR 
is a (finite) sum ~ ai| 
with @, fli ~ A, then R, 2 = ~ ~|174 
1, R ~ s = ~ ai| 1 | 
i 
i 
i 
R23--- ~ 1 |174 
i 
The element R is called the universal R-matrix of A. This element satisfies the 
Yang-Baxter equation 
R12R13R23 = R2aR13R12. 
(3.1.4) 
Indeed, it follows from (3.1.1) and (3.1.2) that 
R,2R13R23 = Rlz(A|174 
= R23R13R12 . 
Let us note the following important equalities: 
(eNid)(R)= (idN~)(R)= 1, 
(s | 
(R) = (id | s- 1) (R) = R-l, 
(s| s) (R) = R. 
(3.1.5) 
(3.1.6) 
(3.1.7) 
Indeed, from the axiom of counit we have (e| 
=id =(id| 
Therefore 
R = (e |174 
(A | 
(e|174 
3R23) = (e | 
R, 
R = (id| 
| 
(A | 
(R) = (id| e | 
= (id| e) (R)" R. 
Since R is invertible, these equalities imply (3.1.5). To prove (3.1.6) note that if 
m:A| 
is the algebra multiplication then the axiom of antipode states that 
m(s | 
(A (a)) = m(id | s) (A (a)) = e(a) 1 a 
(3.1.8) 
for any a cA. Put m12 =m|174174 
and m23 =id|174 
| 
We have 
m~ 2((s|174 
| 
---(eNid)(R) = 1, 
m2s((idQid | 
~) (id@ A')(R)) = (id| 
1) (id| e) (R) = 1. 
(Note that s-1 and s are antiautomorphism of A.) On the other hand (3.1.2, 3.1.3) 
imply that 
m~z((s|174 
(A | 
(R)) --- (s| 
(R). R, 
(3.1.9) 
m23((id| 
| 
1)(id | A')(R)) --- n. (id | 
~)(R). 
(3.1.10) 
Clearly, (3.19), (3.1.10) imply (3.1.6). Also, (3.1.6) implies (3.1.7). 
With each quasitriangular Hopf algebra (A, R) we associate the element u = ua 
= ~ s(fl~)e i, where as above R = ~ ei@fli. This element is invertible and satisfies the 
i 
i 
6 
N. Yu. Reshetikhin and V. G. Turaev 
following identities (see [Dr]): 
sZ(a)=uau -1 
for all 
a~A, 
(3.1.11) 
us(u) ~ (centre of A), 
(3.1.12) 
A(u) = (R21Rlz)- 1 (u| 
(u| 
-1 , 
(3.1.13) 
U- i = 2 fiiS2((~i) " 
(3.1.14) 
i 
Remark. One may more generally define topological quasitriangular Hopf 
algebras so that the comultiplication A takes values not in A| 
but rather in its 
certain completion A~A. One also has to assume that R ~ AQA. The properties of 
quasitriangular Hopf algebras mentioned above may be extended to the 
topological case (cf. [Dr]). 
3.2. Category RepA. With each algebra A one associates the category RepA of its 
finite dimensional linear representations. The objects of RepA are left A-modules 
finitely generated over the ground field. The morphisms of RepA are A-linear 
homomorphisms. Note that the action of A in A-module V induces an algebra 
homomorphism A--*End V, denoted by ~v. 
Let (A, R) be a quasitriangular Hopf algebra. We shall provide RepA with a 
structure of compact braided monoidal category. The comultiplication A in A 
induces the tensor product in RepA: for objects V, W their tensor product is the 
ordinary tensor product V| W of vector spaces equipped with the (left) A-action 
by the formula Qv| 
= (~v| 
(A(a)) for a ~ A. The unit object I of RepA is the 
ground field equipped with the action of A by means of the counit of A. The 
homomorphisms a, r, # (see Sect. 2.1) are given respectively by the formulas 
(x|174174174 
x| 
j| 
Thus RepA is a monoidal category. 
It follows from (3.1.1) that for any A-modules V, W the mapping 
Cv, w = pV, w o (ffv| 
(R): V| W~ W| V, 
where P is the permutation homomorphism x|174 
is an A-linear homo- 
morphism, i.e. a morphism of RepA. The formulas (3.1.2), (3.1.3) imply the 
commutativity of the diagrams (2.1.3), (2.1.4) so that RepA becomes a braided 
monoidal category. 
For any A-module V we provide the dual linear space V * with the (left) action of 
A by the formula 
Qvv(a) = (Qv(s(a)))* E End V v 
(3.2.1) 
for a ~ A. Denote by e v the canonical pairing (x, y)~-+y(x) : V| VV~I. Denote by nv 
the homomorphism I~Vv| 
which sends 1 into ~ei| 
where {ei} is an 
i 
arbitrary basis in V and {e ~} is the dual basis in V v. It is easy to deduce from 
definitions that ev, nv are A-linear and that the conditions of the compact category 
are fulfilled. 
Therefore, RepA is a compact braided monoidal category. Its strict extension 
(RepA)[] will be denoted by Repn(A). 
Remark. All objects of Rep A are reflexive up to a canonical isomorphism. Indeed, 
Qwv(a) = Ov(sZ(a)) = UvQv(a)Uv 1, where we have identified the vector spaces V"" and 
Ribbon Graphs Derived from Their Invariants 
7 
V and where Uv = Or(U). Therefore, the composition of the canonical identification 
V~ 
V and the homomorphism x~--~Uv ~x:V--+ V is an A-isomorphism. 
3.3. Ribbon Hopf Algebras. Let (A, R) be a quasitriangular Hopf algebra with the 
comultiplication A, counit e and antipode s. Put u = UA ~ A. We call the triple (A, R, 
a central element v e A) a ribbon Hopf algebra if 
v 2 =- us(u), 
s(v) = v, 
e(v) = 1, 
(3.3.1) 
A(v) = (R21R12)- 1(/)@ v), 
(3.3.2) 
where R12 =R and R21 =Perm(R). Since u is invertible, v is also invertible in A. 
There exist quasitriangular Hopf algebras which do not contain v as above. If v 
exists it may be non-unique. To describe non-uniqueness ofv we define the abelian 
group E(A)C A consisting of central elements E e A such that 
E 2 = 1, 
s(E) = E, 
e(E) = 1, 
A(E) = E| 
(3.3.3) 
It is obvious that for any ribbon Hopf algebra (A, R, v) and any E e A the triple 
(A, R, Ev) is a ribbon Hopf algebra iff E ~ E(A). 
Each quasitriangular Hopf algebra (A, R) canonically extends to a ribbon Hopf 
algebra (7t, R,/)). Namely, let A be the module whose elements are formal 
expressions a + b/) with a, b ~ A. We provide A with the Hopf algebra structure by 
the formulas 
(a + by) (a' + b' /)) = (aa' + bb' us(u)) + (ab' + ba')/), 
A (a + b/)) = A (a) + A (b) (R2 a R a 2) - x (v | 
s(a + by) = s(a) + s(b)v, 
e(a + by) = e(a) + e(b). 
We identify A with a subset of A by the formula a=a+Ov. Clearly, ReA| 
CA| 
3.4. Theorem. (A, R, v) is a ribbon Hopf algebra containing A as a Hopf subatgebra. 
Proof. The equalities (3.1.1-3.1.3, 3.3.1, 3.3.2) follow directly from definitions. Thus 
we have to check only the axioms of Hopf algebra for ,4. The associativity of .4 
follows from (3.1.12). Clearly, v ~ (centre of ,4). Let us show that A : A--+,4 | 
is an 
algebra homomorphism. It follows from (3.1.1) that for any a s A, 
(R2xR12)- XA(a) --- A(a) (RzxRlz)- 1. 
Since s is a coalgebra antihomomorphism, 
A(s(u)) = Perm((s| 
(A(u))) = (s(u)| 
(s | 
(RzlR ~ 2) -1 
= (s(u)| 
(R 2~R12)-1. 
[The last equality follows from (3.1.7).3 Therefore, 
A (us(u)) = (R 2 ~ R 12) - 1(us( u ) | us(u)) (R 2 j. R 12) - i _ (R 21 R 12 ) - Z(us(u) | us(u)). 
Now we can prove that for any a, b, a', b'G A, 
3((a + by) (a' + b'v)) = d(a + bv)A(a' + b'v). 
8 
N. Yu. Reshetikhin and V. G. Turaev 
Indeed 
A((a + by) (a" + b'v)) 
= A(aa' + bb'us(u)) + A(ab' + ba') (R 21R 12)- ~(v| v) 
= A(aa') + A(bb') (R2 tR12)- 2(us(u)| us(u)) 
+ A(ab') (R z aR 12) - l(v| v) + A(b) (R 2 ~ R a 2) - l(v| 
a' ) 
= A(a)A(a') + A(b) (R 21R12)- ~(v| 
(R21R12)- l(v| v) 
+ A(a)A(b'v) + A(bv)A(a') = A(a + bv)A(a'+ b'v). 
The eounit axiom for .4 follows from (3.1.5). It is easy to verify (using 3.1.11) and the 
fact that the antipode of A is an antiautomorphism of the algebra structure) that s 
is an antiautomorphism of A. Therefore, to check the axiom of antipode (3.1.8) it 
suffices to consider the case a=v. Let R= ~ cq| 
In view of (3.1.6) R~-21 
i 
= ~ s(~)| 
i and R2( = ~ fljNs(ei). Therefore, 
i 
j 
m(id| 
(A(v)) = m(id | 
1) (v| 
= v 2 2. s(~i)fljs2(eJ )s(fli) 
t,J 
= v~ E s(~3u- ~s(l~,) = v ~ Y "- Is~(~,)s(/~,) 
i 
i 
= v2u- 1s(u- l) = v2(s(u)u) - ~ = v2(us(u))- ~ = 1. 
Here we have used (3.1.11) and (3.1.14). A similar argument shows that 
m(s| 
(A(v))= I. Here one should use the equalities Z sa(~i)//i =s(u-t) (which 
follows from 3.1.7 and 3.1.14) and v 2 ~ s(~iu-1/3i)= 1 (which follows from 3.1.11). 
3.5. Remark. If(A, R, w) is a ribbon Hopf algebra then w e A C A, so that v = Ew for 
some EEA, E#I. In view of (3.3.3) E generates a two-dimensional Hopf 
subalgebra, say,/~ of A with the basis { 1, E}. Clearly, .4 = A | E in the class of Hopf 
algebras.
