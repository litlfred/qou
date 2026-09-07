---
doc_id: arxiv-0705.2975v1
doc_title: "On the Definitions of Difference Galois Groups"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
doc_brief: "On the Definitions of Difference Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and sh ow"
---
In the modern Galois theory of polynomials of degree n with coeﬃcients in a ﬁeld k1, one
associates to a polynomial p(x) a splitting ﬁeld K, that is a ﬁeld K that is generated over k
by the roots of p(x). All such ﬁelds are k-isomorphic and this allows one to deﬁne the Galois
group of p(x) to be the group of k-automorphisms of such a K. If k is a diﬀerential ﬁeld
and Y ′ =AY,A an n ×n matrix with entries in k, one may be tempted to naively deﬁne
a “splitting ﬁeld” for this equation to be a diﬀerential ﬁeld K containingk and generated
(as a diﬀerential ﬁeld) by the entries of a fundamental solution mat rixZ of the diﬀerential
equation2. Regrettably, such a ﬁeld is not unique in general. For example, for t he equation
y′ = 1
2xy over k = C(x),x ′ = 1, the ﬁelds k(x1/2) and k(z),z transcendental over k and
z′ = 1
2xz are not k-isomorphic. If one insists that the constants Ck = {c ∈k | c′ = 0 } are
algebraically closed and that K has no new constants, then Kolchin [16] showed that such
a K exists (and is called the Picard-Vessiot associated with the equation) and is unique
up to k-diﬀerential isomorphism. Kolchin [15] deﬁned the Galois group of suc h a ﬁeld to
∗The author thanks the Isaac Newton Institute for Mathematical Sciences for its hospitality and ﬁnancial
support during spring 2005.
†The preparation of this paper was supported by NSF Grant CCR- 00 96842 and by funds from the
Isaac Newton Institute for Mathematical Sciences during a visit in M ay 2005.
1All ﬁelds in this paper are assumed to be of characteristic zero
2that is, an invertible n × n matrix Z such that Z ′ = AZ. Note that the columns of Z form a basis of
the solution space
1
be the group of k-diﬀerential automorphisms of K and developed an appropriate Galois
theory3.
When one turns to diﬀerence ﬁelds k with automorphism σ and diﬀerence equations σY =
AY, A ∈ GLn(k), the situation becomes more complicated. One can consider diﬀere nce
ﬁelds K such that K is generated as a diﬀerence ﬁeld by the entries of a fundamental
solution matrix. If the ﬁeld of constants Ck = {c ∈k |σ(c) = c} is algebraically closed and
K has no new constants, then such a K is indeed unique and is again called a Picard-Vessiot
extension ([23], Proposition 1.23 and Proposition 1.9). Unlike the diﬀer ential case, there are
equations for which such a ﬁeld does not exist. In fact there are diﬀ erence equations that
do not have any nonzero solution in a diﬀerence ﬁeld with algebraically c losed constants.
For example, let K be a diﬀerence ﬁeld containing an element z ⁄= 0 such that σ(z) = −z.
One then has that z2 is a constant. If, in addition, the constants CK ofK are algebraically
closed, then z ∈CK soσ(z) = z, a contradiction. This example means that either one must
consider “splitting ﬁelds” with subﬁelds of constants that are not n ecessarily algebraically
closed or consider “splitting rings” that are not necessarily domains . Both paths have been
explored and the aim of this paper is to show that they lead, in essenc e, to the same Galois
groups.
The ﬁeld theoretic approach was developed by Franke 4 in [10] and succeeding papers.
He showed that for Picard-Vessiot extension ﬁelds the Galois group is a linear algebraic
group deﬁned over the constants and that there is the usual cor respondence between closed
subgroups and intermediate diﬀerence ﬁelds. Franke notes that P icard-Vessiot extension
ﬁelds do not always exist but does discuss situations when they do ex ist and results that
can be used when adjoining solutions of a linear diﬀerence equation fo rces one to have new
constants.
Another ﬁeld theoretic approach is contained in the work of Chatzid akis and Hrushovski
[4]. Starting from a diﬀerence ﬁeld k, they form a certain large diﬀerence extension U
having the properties (among others) that for any element in U but not in k, there is an
automorphism of U that moves this element and that any set of diﬀerence equations (n ot
necessarily linear) that have a solution in some extension of U already have a solution
in U. The subﬁeld of constants CU is not an algebraically closed ﬁeld. Given a linear
diﬀerence equation with coeﬃcients in k, there exists a fundamental solution matrix with
entries in U. Adjoining the entries of these to k(CU ) yields a diﬀerence ﬁeld K. A natural
candidate for a Galois group is the group of diﬀerence automorphism s of K over k(CU )
and these do indeed correspond to points in a linear algebraic group. Equality of this
automorphism group with the Galois group coming from Picard-Vessio t rings is shown in
4.15 under certain conditions (which are always veriﬁed when Ck is algebraically closed).
Proofs are very algebraic in nature, and along the way produce som e new algebraic results
3It is interesting to note that the Galois theory was developed befor e it was known if such K always
exist. See the footnote on p.29 of [15]
4Bialynicki-Birula [2] developed a general Galois theory for ﬁelds with op erators but with restrictions
that forced his Galois groups to be connected.
2
on Picard-Vessiot rings: we ﬁnd numerical invariants of Picard-Ves siot rings of the equation
σ(X) = AX, and show how to compute them (see 4.9 and 4.11). Furthermore, w e show
how to compute the number of primitive idempotents of a Picard-Ves siot ring when the
ﬁeld Ck is algebraically closed (4.13). This situation will be further discussed in Section 4.
The ﬁeld theoretic approach also seems most natural in the analytic situation. For example,
let M(C) be the ﬁeld of functions f (x) meromorphic on the complex plain endowed with
the automorphism deﬁned by the shift σ(x) = x + 1. Note that the constants CM(C) are
the periodic meromorphic functions. A theorem of Praagman [21] st ates that a diﬀerence
equation with coeﬃcients in M(C) will have a fundamental solution matrix with entries in
M(C). If k is the smallest diﬀerence ﬁeld containing the coeﬃcients of the equat ion and
CM(C) and K is the smallest diﬀerence ﬁeld containing k and the entries of fundamental
solution matrix, then, in this context, the natural Galois group is th e set of diﬀerence
automorphisms of K over k. For example, the diﬀerence equation σ(y) = −y has the
solution y = eπix. This function is algebraic of degree 2 over the periodic functions k =
CM(C). Therefore, in this context the Galois group of K =k(eπix) over k is Z/2Z.
One can also consider the ﬁeld M(C∗) of meromorphic functions on the punctured plane
C∗ = C\{0} with q−automorphism σq(x) = qx, |q| ⁄= 1. Diﬀerence equations in this
context are q-diﬀerence equations and Praagman proved a global existence the orem in this
context as well. The constants CM(C∗) naturally correspond to meromorphic functions on
the elliptic curve C∗/qZ and one can proceed as in the case of the shift. One can also
deﬁne local versions (at inﬁnity in the case of the shift and at zero o r inﬁnity in the case
of q-diﬀerence equations). In the local case and for certain restrict ed equations one does
not necessarily need constants beyond those in C (see [9], [22], [23] as well as connections
between the local and global cases. Another approach to q-diﬀerence equations is given
by Sauloy in [26] and Ramis and Sauloy in [25] where a Galois group is prod uced using a
combination of analytic and tannakian tools. The Galois groups discus sed in these papers
do not appear to act on rings or ﬁelds and, at present, it is not appa rent how the techniques
presented here can be used to compare these groups to other pu tative Galois groups.)
An approach to the Galois theory of diﬀerence equations with coeﬃc ients in diﬀerence ﬁelds
based on rings that are not necessarily integral was presented in [2 3] (and generalized by
Andr´ e in [1] to include diﬀerential and diﬀerence equations with coeﬃ cients in fairly general
rings as well). One deﬁnes a Picard-Vessiot ring associated with a diﬀerence equation
σY = AY with coeﬃcients in a diﬀerence ﬁeld k to be a simple diﬀerence ring (i.e., no
σ-invariant ideals) R of the form R = k[zi,j, 1/ det(Z)] where Z = (zi,j) is a fundamental
solution matrix of σY =AY . Assuming that Ck is algebraically closed, it is shown in [23]
that such a ring always exists and is unique up to k-diﬀerence isomorphism. A similar
deﬁnition for diﬀerential equations yields a ring that is an integral do main and leads (by
taking the ﬁeld of quotients) to the usual theory of Picard-Vessio t extensions (see [24]). In
the diﬀerence case, Picard-Vessiot rings need not be domains. For example, for the ﬁeld
k = C with the trivial automorphism, the Picard-Vessiot ring correspond ing to σy = −y
is C[Y ]/(Y 2 − 1),σ (Y ) = −Y . Nonetheless, one deﬁnes the diﬀerence Galois group of
3
σY = AY to be the k-diﬀerence automorphisms of R and one can shows that this is a
linear algebraic group deﬁned over Ck. In the example above, the Galois group is easily
seen to be Z/2Z. Furthermore, in general there is a Galois correspondence betwe en certain
subrings of the total quotient ring and closed subgroups of the Ga lois group.
The natural question arises: How do these various groups relate to each other? The example
of σ(y) = −y suggests that the groups may be the same. Our main result, Theor em 2.9,
states that all these groups are isomorphic as algebraic groups ov er a suitable extension of
the constants. This result has interesting ramiﬁcations for the an alytic theory of diﬀerence
equations. In [11], the second author gave criteria to insure that s olutions, meromorphic in
C∗, of a ﬁrst order q-diﬀerence equation over C(x) satisfy no algebraic diﬀerential relation
over CM(C∗)(x), where CM(C∗) is the ﬁeld of meromorphic functions on the elliptic curve
C∗/qZ. The proof of this result presented in [11] depended on knowing th e dimension of
Galois groups in the analytic (i.e., ﬁeld-theoretic) setting. These gro ups could be calculated
in the ring theoretic setting of [23] and the results of the present p aper allow one to transfer
this information to the analytic setting. Although we will not go into mo re detail concerning
the results of [11], we will give an example of how one can deduce trans cendence results in
the analytic setting from their counterparts in the formal setting .
The rest of the paper is organized as follows. In Section 2, we show h ow results of [23] and
[24] can be modiﬁed to prove the correspondence of various Galois g roups. In Section 3 we
prove this result again in the special case of q-diﬀerence equations over C(x) using tannakian
tools in the spirit of Proposition 1.3.2 of [14]. In Section 4, we discuss th e model-theoretic
approach in more detail and, from this point of view, show the corre spondence of the Galois
groups. In addition, we consider some additional properties of Pica rd-Vessiot rings over
ﬁelds with constant subﬁelds that are not necessarily algebraically c losed. The diﬀerent
approaches and proofs have points of contacts (in particular, Pr oposition 2.4) and we hope
comparisons of these techniques are enlightening.
The authors would like to thank Daniel Bertrand for suggesting the approach of Section 3
and his many other useful comments concerning this paper.
