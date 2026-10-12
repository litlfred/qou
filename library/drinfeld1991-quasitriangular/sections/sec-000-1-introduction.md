---
doc_id: drinfeld1991-quasitriangular
doc_title: "On quasitriangular quasi-Hopf algebras and a group closely connected with Gal(Q̄/Q)"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: "1"
pages: 1-3
source_pdf: drinfeld1991-quasitriangular.pdf
source_sha256: 1a1d279e92445fdc
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime; spread split into left/right page; quality: partial, display math largely lost)
doc_brief: "On quasitriangular quasi-Hopf algebras and a group closely connected with Gal(Q̄/Q) — A previously announced theorem is proved concerning the struc- ture of quasitriangular quasi-Hopf algebras in the"
---
§1. Introduction
This paper is devoted primarily to the proof of a theorem announced in [1]
concerning the structure of quasitriangular quasi-Hopf algebras in the frame-
As a technical tool we use the pro-unipotent version of a group introduced by
Grothendieck in [2j--a group of enormous interest because of its close connec-
tion with Gal(Q/Q) .
Let us recall the basic definitions of [l]. A quasi-Hopf algebra differs from a
Hopf algebra in that the coassociativity axiom is replaced by a weaker condition.
More precisely, a quasi-Hopf algebra over a commutative ring k , as defined in
[1], is a set (A, △, &, ), where A is an associative k-algebra with unity, △
a homomorphism A → A & A,  a homomorphism A -→ k (we assume that
△(1) = 1, ε(1) = 1), and Φ an invertible element of A  A  A, all these
satisfying
(id @A)(A(a) = @ (A 8 id)(A(a) @-1  aEA. (1.1)
(id  id A)(Φ) · (△  id β id)(Φ)
= (1 αΦ) · (id α△αid)(Φ) · (Φα 1) ; (1.2)
(8 @ id) o△ = id = (id@e)oA, (1.3)
(id@ β id)(@) = 1 , (1.4)
together with an axiom which in the Hopf case, i.e., for @ -- 1 , reduces to exis-
tence and bijectivity of an antipode. In the situation of the present paper, when
(A, A, t, @) is a deformation of a Hopf algebra depending on an "infinitely
small" parameter h , this axiom is satisfied automatically by Theorem 1.6 of
[lj. As in the Hopf case, A is called the comultiplication, and  the counit.
The paper [1l generalized to the quasi-Hopf case the notion of quasitriangular
Hopf algebra defined in 910 of [3] and inspired by the quantum method for
the inverse problem [4]. Specifically, a quasitriangular quasi-Hopf algebra is a
set (A, △, &, Φ, R), where (A, △, , Φ) is a quasi-Hopf algebra and R an
1980 Mathematics Subject Classification (1985 Revision). Primary 16A24; Secondary 81E40.
Key words and phrases. Hopf algebras, quantum groups, conformal field theory, Galois group
of the rationals, braid groups, Lie algebras.
@1991 American Mathematical Society
1048-9924/91 $1.00 + $.25 per page
829

[[ spread 2, left page ]]
830 V. G. DRINFEL'D
invertible element of A  A such that
△'(a) = RA(a)R-I aEA, (1.5)
(A @ id)(R) = Q312 R13(@132)-I R23@, (1.6a)
(id @A)(R) = (@231)-1 R13@213 R12@~ (1.6b)
Here A' =  o A, where : A  A → A & A interchanges the tensor factors. If
R E,a, &b, then by definition R? - Z;a, &b,&1, Rl3 -Z;a; &1 &b,,
and R23 - E, 1 & a;  bj. We also need to explain that, for example, if @ =
Z,xj
The gist of the axioms (1.1)-(1.6) is that the representations of a quasitri-
angular quasi-Hopf algebra A form a quasitensored category in the sense of
[5] (see also g3 of [1]). This means that, firstly, there exists in the category
of representations of A a tensor-product functor: given two representations of
A, in k-modules V and V2, the representation of A in Vi & V2 is defined
as the composite A  A & A → End;(V & V2). Secondly, there exist functo-
rial isomorphisms of commutativity c: Vi  V2 -~- V  V and associativity
a: (V  V2) & V, -- Vi &(V2  V) where the V, are representations of A.
Namely, a is the operator in V & V,  V, corresponding to @, and c is the
composite of the operator in Vi  V2 corresponding to R with the usual isomor-
phism o: Vi  V2 -- V2 V . Thirdly, there exists an identity representation k
and isomorphisms V & k ~ V and k & V - V for any representation V.
Finally, (1.2), (1.4), and (1.6) guarantee the commutativity of the diagrams
A8(A0(A8 A)) 4 ~ (VαV2)α(VαV4) 二 Vα(Vα(Vα))
(A0((A8A)8A) +V8((V20)814)
(1.7)
(1.8)
(V@k)αV2V8(k8 V2)
- A0(A0A)
c@id (1.9a)
(A84)0A (V& V)@ V2
(A0A)8A  (V28 V)8 V --2V2α(V38 V)
id &c (1.9b)
+(V28 V)αv3 --+V28(V8v3)
We note that in general R21 + R-1 , and consequently the commutativity iso-
gories and tensored [6]).

[[ spread 2, right page ]]
QUASITRIANGULAR QUASI-HOPF ALGEBRAS 831
If (A, △, &, , R) is a quasitriangular quasi-Hopf algebra, and F an in-
vertible element of A A such that (id e)(F) - 1 -- (& id)(F), then, putting
△(a) = F . A(a) · F-1 (1.10)
@ = F23 . (id αA)(F) . Φ. (A id)(F-1) (1.11)
R-R21.R.F-1 (1.12)
we obtain a new quasitriangular quasi-Hopf algebra (A, 2, &, Φ, R); we say
it is obtained from (A, A, , Φ, R) by twisting via F. The quasitensored cate-
gories that correspond to (A, A, e, , R) and (A, △, , , R) are equivalent.
It is therefore natural to refer to the twisting as a “gauge transformation".
We shall study quasitriangular quasi-Hopf algebras in the framework of the
theory of perturbations with respect to h , restricting ourselives to the case of
characteristic. O. These words are given a precise meaning by the following
definition (QUE is short for "quantized universal enveloping").
DEFINrrioN. Let k be a field of characteristic O. By a guasitriangular quasi-
Hopf QUE-algebra over k[[h]l is meant a topological quasitriangular quasi-Hopf
algebra (A, A, &, Φ, R) over k[[h]] such that A/hA is a universal envelop-
ing algebra with the standard comultiplication, and A, as a topological k[h]]-
module, is isomorphic to Vl[hj] for some vector space V over k .
REMARK. Since A/h A is a universal enveloping algebra, it follows from (1.4)
and the invertibility of @ that @  l mod h. Similarly, R = 1 modh , and for
a twisting of quasitriangular quasi-Hopf QUE-algebras, F  l mod h .
Inspired by [7]-[9], the following method was proposed in [1] for constructing
quasitriangular quasi-Hopf QUE-algebras. Let g be a Lie algebra over k[[h]]
which as a kl[h]]-module is isomorphic to Vhj] for some vector space V over
k. (This condition on g means that g is a deformation of a Lie algebra go
over k , where go = g/hg ; such algebras g will therefore be called deformation
algebras.) Suppose given a symmetric g-invariant tensor t E   g, where
& is the complete tensor product. Put A - Ug, where Ug means the h-adic
completion of the universal enveloping algebra. Define in the usual way : A -
kl[h]l and A: A -→ A & A (where  is the complete tensor product), and put
satisfying (1.1), (1.2), (1.4), and (1.6) (note that (1.1) means in this situation
the g-invariance of ) . The first main result of the present paper is:
THEoREM A. Such a @ exists, and is unigue up to twisting via symmetric
g-invariant elements F E A  A.
and  and R are defined by formulas (1.10) and (1.12), then the equalities  --
A and R = R are equivalent to g-invariance and symmetry of F (t commutes
with the g-invariant elements of A  A, since t = (A(C) - C & 1 - 1  C)/2
where C e Ug is the Casimir element).
is
replaced by the at first sight weaker conditions of symmetry and g-invariance
Uniqueness in Theorem A is proved simply enough (see Propositions 3.2 and
3.4). For k - C, what is proposed in [1j is an explicit but transcendental con-
struction for @ by means of the Knizhnik-Zamolodchikov system of equations

[[ spread 3, left page ]]
832 V. G. DRINFEL'D
(for short: the KZ system) that arises in conformal feld theory [10j. This @,
i...i.j..j....
Φkz  a(m,n,p)
m,n.D
where the e, are a basis of g as a topological C[h]]-module and the tensors
a(m,n,p) a are
expressed in terms of the structural constants s of the algebra  and the
components ru of the tensor t in accordance with the rules of acyclic tensor
calculus with coefficients in C, while (1.1), (1.2). (1.4), and (1.6) follow, in
accordance with the rules of acyclic tensor calculus, from the fact that the
are the structural constants of a Lie algebra and t is symmetric and invariant.
i, j, l form a "cycle") Among the coefficients of the C-universal formula
, m E N, which
are imaginary and probably transcendental. Thus, for k  C the existence part
of Theorem A cannot foliow from the construction of @kz . However, it is
proved in g3, in conjunction with the following theorem.
THEOREM A'. There exists a Q-universal formula expressing the element @
of Theorem A in terms of t - ht . It is unique up to twisting via a symmetric
Q-universal F -- F(t).
The quasitriangular quasi-Hopf algebras supplied by Theorem A will be called
the standard algebras.
THEoREM B. Any quasitriangular quasi-Hopf QUE-algebra can be made stan-
dard by a suitable twist.
The C-universal formula expressing Pkz in terms of t = ht is of the form
with coefficients in C (see s2). Theorem A can be strengthened as follows.
THEoREM A". There exists a Lie formal series P with coefficients in Q such
that the @ of Theorem A can be taken as exp P(hti? , ht?3).
If @ has the form exp P(hti2 , ht23) where P is a Lie formal series, then the
Q defined by formula (1.11) is not, in general, of the same form. However, on
satisfy (1.2) and (1.6) we can define (see s4) a natural transitive action of a
certain group, which we call the Grothendieck-Teichmuller group and denote
by GT(k). This action forms the basis of the proof of Theorem A". The
definition of GT(k) is in essence borrowed from [2l, where, in particular, it
is shown how to construct a canonical homomorphism Gal(Q/Q) -→ GT(Q,) ,
where Q is the algebraic closure of Q in C and l is a prime number.
The plan of the paper is as follows. g2 is devoted to Φkz. In g3, the
methods of [1] are used to prove Theorems A, A', and B. In s4 we define the
Grothendieck-Teichmiller group (in several versions) and explain its connec-
tion with Gal(Q/Q). In s5 we prove Theorem A", and also reduce the study
of GT(k) to the study of an infinite-dimensional graded Lie algebra grt,(k) .

[[ spread 3, right page ]]
QUASITRIANGULAR QUASI-HOPF ALGEBRAS 833
In g6 we gather together certain facts about this algebra. s4 is independent of
$s2 and 3, and ss5 and 6 are independent of g3.
The author thanks A. A. Beilinson, G. V. Belyi, Yu. I. Manin, and G. B.
Shabat for calling his attention to the papers [2], [11]-[15].
