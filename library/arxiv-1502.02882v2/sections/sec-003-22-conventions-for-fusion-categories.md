---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-003-22-conventions-for-fusion-categories
section_title: "Conventions for fusion categories"
section_number: 2.2
pages: 5-7
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
A fusion category is a rigid semisimple linear monoidal category with ﬁnitely
many isomorphism classes of simple objects and whose unit object is simple [8].
In a fusion category, the associators feature explicitly in the graphical calculus
as follows. Suppose we ﬁx a representative set of simple objects Xi, i∈I, and
choose trivalent bases
eα :Xi→Xj⊗Xk drawn as
 (3)
for each hom-set Hom(Xi,Xj⊗Xk). (We will always choose the canonical basis
elements for the 1-dimensional hom-spaces Hom(1, 1⊗ 1), Hom(Xi, 1⊗Xi) and
Hom(Xi,Xi⊗ 1)). Then we can form two diﬀerent bases for Hom( Xi,Xj⊗
(Xk⊗Xl)) and so we have a change of basis transformation
=
∑
γ,n,δ
(Fi
jkl)γnδ
αmβ
 . (4)
Note that according to our diagram conventions, in the parenthesis scheme
Xj⊗(Xk⊗Xl) for the output objects, the left-hand side diagram of (4) evaluates
5
as
Xi
eα
−→Xj⊗Xm
id⊗eβ
−→ Xj⊗ (Xk⊗Xl)
while the right-hand side diagram evaluates as
Xi
eγ
−→Xn⊗Xl
eδ⊗id
−→ (Xj⊗Xk)⊗Xl
aXj,Xk,Xl
−→ Xj⊗ (Xk⊗Xl)
where a is the associator of the fusion category. We call the scalars ( Fi
jkl)γnδ
αmβ
the associator matrix elements .
Given a trivalent basis choice (3), we deﬁne thedual basis ˆeα :Xj⊗Xk→Xi
as the one satisfying ˆeβ◦eα =δαβ idXi. Graphically, this is drawn as:






and






satisfying
 =δαβ
 . (5)
We will often write botheα and ˆeβ simply asα and ˆβ respectively; also we often
write i instead of Xi. Basis vectors satisfying (5) provide a resolution of the
identity,
∑
i,α
=
 . (6)
Example 2.3. The Yang-Lee category (see eg. [27]) has two simple objects 1
(drawn as a dotted line) and τ (drawn as a solid line) with τ 2 = 1 +τ. So, the
only nontrivial trivalent basis elements are
and
 .
The associators are
=a
 +
 (7)
=a
 −a
 (8)
and
=
 (9)
where a =− 1
2(1 +
√
5).
6
Example 2.4. The categoryE associated with the even part of theE6 subfactor
[10, 25] has 3 simple objects: 1 (drawn as a dotted line), x (drawn as a solid
line),y (drawn as a wiggly line) and fusion rules xy =yx =x,xx = 1 + 2x +y,
yy = 1. So, the nontrivial trivalent basis elements are:
,
 ,
 ,
 ,
 ,
 .
Some relevant associators are
= 1
d


 +

 + 1√
2v


 +
 +
 −


(10)
and:
= 1√
2e
−7πi
12


 +

 (11)
= 1√
2e
−7πi
12

−i
 +i

 (12)
Hered = 1 +
√
3 and v =
√
d. See [11] for a full list. Note that we are using the
inverses of the matrices in [11] due to our conventions.
