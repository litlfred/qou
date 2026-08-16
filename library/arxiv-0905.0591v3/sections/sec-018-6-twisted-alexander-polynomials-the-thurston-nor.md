---
doc_id: arxiv-0905.0591v3
doc_title: "A SUR VEY OF TWISTED ALEXANDER POL YNOMIALS"
section_id: sec-018-6-twisted-alexander-polynomials-the-thurston-nor
section_title: "Twisted Alexander polynomials, the Thurston norm and fibered manifolds"
section_number: 6
pages: 18-21
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
manifolds
6.1. Twisted Alexander polynomials and ﬁbered manifolds. Let φ ∈ H 1(N ; Z) =
Hom(π1(N ), Z) be non–trivial. We say ( N,φ ) ﬁbers over S1 if there exists a ﬁbration
p : N → S1 such that the induced map p∗ : π1(N ) → π1(S1) = Z coincides with φ.
If K is a ﬁbered knot, then it is a classical result of Neuwirth tha t ∆ K is monic and
that deg(∆ K ) = 2 genus(K). Similarly, twisted Alexander polynomials provide neces sary
conditions to the ﬁberability of a pair ( N,φ ).
In order to state the ﬁbering obstructions for a pair ( N,φ ) we need to introduce the
Thurston norm. Given ( N,φ ) the Thurston norm of φ is deﬁned as
||φ||T = min{χ−(S) |S ⊂N properly embedded surface dual to φ}.
Here, given a surface S with connected components S1 ∪ · · · ∪Sk, we deﬁne χ−(S) =∑ k
i=1 max{−χ(Si), 0}. Thurston [Th86] showed that this deﬁnes a seminorm on H 1(N ; Z)
which can be extended to a seminorm on H 1(N ; R). As an example consider S3 \νK ,
where K ⊂S3 is a non–trivial knot. Let φ ∈H 1(S3 \νK ; Z) be a generator, then ||φ||T =
2 genus(K) − 1.
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 19
Let N be a 3–manifold N with empty or toroidal boundary and let φ ∈H 1(N ; Z). Re-
call that we identify the group ring R[Z] with the Laurent polynomial ring R[t±1] and
we will now identify Q(R[Z]) with the ﬁeld of rational functions Q(t). Given a represen-
tation γ : π1(N ) → GL(k,R ) we therefore view the corresponding twisted Reidemeister
torsionτ (N,γ ⊗φ) as an element in Q(t) and we view the corresponding twisted Alexander
polynomials ∆ γ⊗φ
N,i as elements in R[t±1].
We say that the twisted Reidemeister torsion τ (N,γ ⊗φ) is monic if there exist polyno-
mials p(t),q (t) ∈ R[t±1] with p(t)
q(t)
.= τ (N,γ ⊗φ) such that the top coeﬃcients of p(t) and
q(t) lie in
{± det(γ(g)) |g ∈π1(N )}.
We also say that the twisted Alexander polynomial ∆ γ⊗φ
N,i is monic if one (and equivalently
any) representative has a top coeﬃcient which is a unit in R.
We recall the following basic lemma:
Lemma 6.1. Let N be a 3–manifold with empty or toroidal boundary. Let φ ∈ H 1(N ; Z)
be non–trivial and let γ :π1(N ) → GL(k,R ) be a representation with R a Noetherian UFD.
Then the following hold:
(1) ∆ γ⊗φ
N,0 is monic,
(2) If ∆ γ⊗φ
N,1 is non–zero, then ∆ γ⊗φ
N,2 is monic.
Proof. As in Section 2.2 we pick a cell decomposition of N with one 0–cell x0 and n 1–
cells c1,...,c n. We denote the corresponding elements in π1(N,x 0) by c1,...,c n as well.
Without loss of generality we can assume that φ(c1) > 0. We then get a resolution for
H0(N ;R[t±1]n) with presentation matrix
(
idn − (γ ⊗φ)(c1) ... idn − (γ ⊗φ)(cn)
)
.
We refer to [FK06, Proof of Proposition 6.1] for details. We h ave
det(idn − (γ ⊗φ)(c1)) = det(idn −tφ(c1)γ(c1)) ∈R[t±1],
which is monic since the top coeﬃcient equals det( γ(c1)). By deﬁnition ∆ γ⊗φ
N,0 divides
det(idn − (γ ⊗φ)(c1)), we therefore see that ∆ γ⊗φ
N,0 is monic. The claim that ∆ γ⊗φ
N,2 is monic
now follows from Proposition 3.7. □
Remark. Note that if τ (N,γ ⊗φ) is monic, then it follows from the previous lemma and
from Proposition 3.2 that ∆ γ⊗φ
N,i ∈ R[t±1] is monic for i = 0, 1, 2. Note though that the
converse does not hold in general since twisted Alexander po lynomials have in general a
higher indeterminacy than twisted Reidemeister torsion. F or example, let F be a ﬁeld and
let γ :π1(N ) → GL(k, F) be a representation such that ∆ γ⊗φ
N,i ⁄= 0. It follows immediately
from the deﬁnition that ∆ γ⊗φ
N,i is monic. However, τ (N,γ ⊗ψ) is not necessarily monic (cf.
e.g. [GKM05, Example 4.2]).
We can now formulate the following ﬁbering obstruction theo rem which was proved in
various levels of generality by Cha [Ch03], Kitano and Morif uji [KM05], Goda, Kitano and
Morifuji [GKM05], Pajitnov [Pa07], Kitayama [Kiy08a] and [ FK06].
20 STEF AN FRIEDL AND STEF ANO VIDUSSI
Theorem 6.2. Let N be a 3–manifold. Let φ ∈H 1(N ; Z) be non–trivial such that (N,φ )
ﬁbers over S1 and such that N ⁄=S1 ×D2,N ⁄= S1 ×S2. Let γ : π1(N ) → GL(k,R ) be a
representation. Then τ (N,γ ⊗φ) ∈Q(t) is monic and we have
k||φ||T = deg(τ (N,γ ⊗φ)).
Remark. (1) If R is a Noetherian UFD, then the last equality can be rewritten a s
k||φ||T = deg ∆ γ⊗φ
N,1 − deg ∆ γ⊗φ
N,0 − deg ∆ γ⊗φ
N,2.
(2) Recall that an alternating knot is ﬁbered if and only if it s ordinary Alexander
polynomial is monic. In contrast to this classical result it follows from calculations
by Goda and Morifuji [GM03] (cf. also [Mo08]) that there exis ts an alternating knot
such that a twisted Reidemeister torsion is monic, but which is not ﬁbered.
(3) Theorem 6.2 has been generalized by Silver and Williams [ SW09d] to give an ob-
struction for a general group to admit an epimorphism onto Z such that the kernel
is a ﬁnitely generated free group.
Proof. The condition on the degrees is proved in [FK06, Theorem 1.3] for R a Noetherian
UFD. The monicness of twisted Reidemeister torsion was prov ed by Goda, Kitano and
Morifuji [GKM05] in the case of a knot complement. The monicn ess of ∆ γ⊗φ
N,1 was proved
in [FK06, Theorem 1.3]. The general case of Theorem 6.2 can be obtained by a direct
calculation as follows. Let S be the ﬁber and f :S →S the monodromy. We endow S with
a CW–structure such that f is a cellular map. Denote by Di the set of i–cells of S and
denote by ni the number of i–cells. We can then endow N = (S × [0, 1])/(x, 0) ∼ (f (x), 1)
with a CW–structure where the i–cells are given by Di and Ei := {c × (0, 1) |c ∈Di−1}. A
direct calculation using [Tu01, Theorem 2.2] now shows that τ (N,γ ⊗φ) ∈ Q(t) is monic
and that
deg(τ (N,γ ⊗φ)) = −kχ(S) = k||φ||T.
□
The calculations in [Ch03], [GKM05] and [FK06] gave evidenc e that twisted Alexander
polynomials are very successful at detecting non–ﬁbered ma nifolds. The results of Morifuji
[Mo08, p. 452] also give evidence to the conjecture that the t wisted Alexander polynomial
corresponding to a ‘generic’ representation detect ﬁbered ness.
Using a deep result of Agol [Ag08] the authors proved in [FV08 c] (see also [FV10] for an
outline of the proof) the following converse to Theorem 6.2.
Theorem 6.3. LetN be a 3–manifold with empty or toroidal boundary. Let φ ∈H 1(N ; Z)
a nontrivial class. If for any epimorphism γ : π1(N ) → G onto a ﬁnite group the twisted
Alexander polynomial ∆ γ⊗φ
N ∈ Z[t±1] is monic and
k||φ||T = deg(τ (N,γ ⊗φ))
holds, then (N,φ ) ﬁbers over S1.
Remark. Building on work of Taubes [Ta94, Ta95], Donaldson [Do96] an d Kronheimer
[Kr99] the authors also show that Theorem 6.3 implies the fol lowing: If N is a closed 3–
manifold and if S1 ×N is symplectic, then N ﬁbers over S1. This provides a converse to
a theorem of Thurston [Th76]. We refer to [FV06, FV08a, FV08b , FV08c] for details, and
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 21
we refer to Kutluhan–Taubes [KT09], Kronheimer–Mrowka [KM 08] and Ni [Ni08] for an
alternative proof in the case that b1(N ) = 1.
It is natural to ask whether ( N,φ ) ﬁbers if all twisted Alexander polynomials are monic.
An aﬃrmative answer would be of great interest in the study of symplectic structures of
4–manifolds with a free circle action (cf. [FV07b]). An equi valent question has also been
raised as a conjecture by Goda and Pajitnov [GP05, Conjectur e 13.2] in the study of Morse–
Novikov numbers. We refer to [GP05] and [Pa07] for more infor mation on the relationship
between twisted Alexander polynomials, twisted Novikov ho mology and Morse–Novikov
numbers.
Somewhat surprisingly, there is strong evidence to the foll owing much weaker conjecture:
A pair (N,φ ) ﬁbers if all twisted Alexander polynomials are non–zero. I n fact the authors
showed the following theorem (cf. [FV07a, Theorem 1.3] and [ FV08b, Theorem 1, Proposi-
tion 4.6, Corollary 5.6]).
Theorem 6.4. LetN be a 3–manifold with empty or toroidal boundary and φ ∈H 1(N ; Z)
non–trivial. Suppose that ∆ γ⊗φ
N is non–zero for any epimorphism γ : π1(N ) → G onto a
ﬁnite group. Furthermore suppose that one of the following h olds:
(1) N =S3 \νK and K is a genus one knot,
(2) ||φ||T = 0,
(3) N is a graph manifold,
(4) φ is dual to a connected incompressible surface S such that π1(S) ⊂π1(N ) is sepa-
rable,
then (N,φ ) ﬁbers over S1.
Here we say that a subgroup A of a group π is separable if for any g ∈π \A there exists an
epimorphism γ :π →G onto a ﬁnite group G such that γ(g) ⁄∈γ(A). It is conjectured (cf.
[Th82]) that given a hyperbolic 3–manifold N any ﬁnitely generated subgroup A ⊂π1(N )
is separable. In particular, if Thurston’s conjecture is tr ue, then Condition (4) of Theorem
6.4 is satisﬁed for any hyperbolic N .
The following theorem of Silver–Williams [SW09b] (cf. also [SW09a]) gives an interesting
criterion for a knot to have vanishing twisted Alexander pol ynomial.
Theorem 6.5. LetK ⊂S3 a knot. Then there exists an epimorphism γ :π1(S3 \νK ) →G
to a ﬁnite group such that ∆ γ
K = 0 if and only if the universal abelian cover of S3 \νK has
uncountably many ﬁnite covers.
