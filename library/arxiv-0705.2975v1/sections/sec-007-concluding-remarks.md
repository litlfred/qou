---
doc_id: arxiv-0705.2975v1
doc_title: "On the Definitions of Difference Galois Groups"
section_id: sec-007-concluding-remarks
section_title: "Concluding remarks"
section_number: null
pages: 25-31
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
doc_brief: "On the Definitions of Difference Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and sh ow"
---
Remark 4.16 Model-theoretic Galois groups: deﬁnition and a bit of history .
Model-theoretic Galois groups ﬁrst appeared in a paper by Zilber [28] in the context of
ℵ1-categorical theories, and under the name of binding groups . Grosso modo, the general
situation is as follows: in a saturated model M we have deﬁnable sets D and C such that,
for some ﬁnite tuple b inM,D ⊂ dcl(C,b ) (one then says that D isC-internal). The group
Aut(M/C ) induces a group of (elementary) permutations of D, and it is this group which
one calls the Galois group of D over C. In Zilber’s context, this group and its action on
D are deﬁnable in M. One issue is therefore to ﬁnd the correct assumptions so that th ese
Galois groups and their action are deﬁnable, or at least, an intersec tion of deﬁnable groups.
25
Hrushovski shows in his PhD thesis ([12]) that this is the case when th e ambient theory is
stable.
Poizat, in [20], recognized the importance of elimination of imaginaries in establishing
the Galois correspondence for these Galois groups. He also noticed that if M is a diﬀeren-
tially closed ﬁeld of characteristic 0 and D is the set of solutions of some linear diﬀerential
equation over some diﬀerential subﬁeld K ofM, and C is the ﬁeld of constants of M, then
the model-theoretic Galois group coincides with the diﬀerential Galois group introduced by
Kolchin [15]. This connection was further explored by Pillay in a series of papers, see [19].
Note that because the theory of diﬀerentially closed ﬁelds of chara cteristic 0 eliminates
quantiﬁers, this Galois group does coincide with the group of KC -automorphisms of the
diﬀerential ﬁeld KC (D).
Since then, many authors studied or used Galois groups, under var ious assumptions
on the ambient theory, and in various contexts, either purely mode l-theoretic (e.g., simple
theories) or more algebraic (e.g. ﬁelds with Hasse derivations). In t he context of generic
diﬀerence ﬁelds, (model-theoretic) Galois groups were investigate d in (5.11) of [4] (a slight
modiﬁcation in the proof then gives the Galois group described in sect ion 4.1 of this paper).
In positive characteristic p, the results generalize easily to twisted diﬀerence equations of
the form σ(X) = AX pm
, the ﬁeld Fix (σ) being then replaced by Fix (τ ), where τ : x ↦→
σ(x)p−m
.
Recent work of Kamensky ([13]) isolates the common ingredients und erlying all the
deﬁnability results on Galois groups, and in particular very much weakens the assumptions
on the ambient theory (it is not even assumed to be complete). With t he correct deﬁnition of
C-internality of the deﬁnable set D, he is able to show that a certain group of permutations
ofD is deﬁnable in M. These are just permutations, do not a priori preserve any relat ions of
the language other than equality. From this group, he is then able to show that subgroups
which preserve a (ﬁxed) ﬁnite set of relations are also deﬁnable, an d that the complexity of
the deﬁning formula does not increase, or not too much. For details , see section 3 of [13].
This approach of course applies to the set D of solutions of a linear system of dif-
ference equations (over a diﬀerence ﬁeld K), and Kamensky also obtains the result that
Aut(KFix (σ)(D)/KFix (σ)) is deﬁnable (see section 5 in [13]).
Remark 4.17 A question arises in view of the proof of the general case of Propos ition
4.11. When R′ is not a domain, we found an embedding of the σℓ-diﬀerence ring R0 into a
generic σℓ-diﬀerence ﬁeld U. It may however happen that K is not relatively algebraically
closed in R∗
0, even when DR0 =CK. Thus one can wonder: can one always ﬁnd a generic
diﬀerence ﬁeld U containingK, and such that there is a K-embedding of the σℓ-diﬀerence
ring R0 into ( U,σ ℓ)? Or are there Picard-Vessiot rings for which this is impossible?
Remark 4.18 Issues of deﬁnability . It is fairly clear that the algebraic group H is
deﬁned over ϕ(KC L). On the other hand, using the saturation of U and the fact that L is
26
a regular extension of K, we may choose another K-embeddingϕ1 ofL in U, and will obtain
an algebraic group H1, which will be isomorphic to H (via some matrix C ∈ GLn(CU )). It
follows that H is K-isomorphic to an algebraic group H0 deﬁned over the intersections of
all possible ϕ(KC L), i.e., over K.
Observe that the isomorphism between H and H1 yields an isomorphism between H(CU )
and H1(CU ), so that we will also have an isomorphism between H0(CU ) and H(CU ), i.e.,
H′ is K-isomorphic to an algebraic subgroup of H0 which is deﬁned over CK ∩CU . Thus
when CK is algebraically closed, it will be deﬁned over CK.
The Galois duality works as well for subgroups of H(CU ) deﬁned by equations (i.e., corre-
sponding to algebraic subgroups of H′, whose irreducible components are deﬁned over CU ).
It works less well for arbitrary deﬁnable subgroups of H(CU ). In order for it to work, we
need to replace K(S) by its deﬁnable closure dcl( KS), i.e., the subﬁeld of U which is ﬁxed
by all elements of Aut el(U/KS). Because the theory of U eliminates imaginaries (1.10 in
[4]), any orbit of an element of S under the action of a deﬁnable subgroup of H(CU ) has a
“code” inside dcl(KS).
Remark 4.19 Problems with the algebraic closure . Assume that U is a generic
diﬀerence ﬁeld containing K, and suﬃciently saturated. Then if K is not relatively alge-
braically closed in the ﬁeld of fractions of R0, we may not be able to ﬁnd a K-embedding of
R0 into the σℓ-diﬀerence ﬁeld U. Thus in particular, a priori not all Picard-Vessiot domains
K-embed into U. This problem of course does not arise if we assume that K is algebraically
closed, or, more precisely, if we assume that
All extensions of the automorphism σ to the algebraic closure of K deﬁne K-isomorphic
diﬀerence ﬁelds.
This is the case if K has no ﬁnite (proper) σ-stable extension, for instance when K = C(t),
with σ(t) = t + 1 and σ the identity on C.
However, in another classical case, this problem does arise: let q ∈ C be non-zero and not
a root of unity, and let K = C(t), where σ is the identity on C andσ(t) = qt. Then K has
non-trivial ﬁnite σ-stable extensions, and they are obtained by adding n-th roots of t.
Let us assume that, inside U, we have σ(
√
t) = √q
√
t. Let us consider the system
σ(Y ) = −√qY, Y ⁄= 0
over K. Then the Picard-Vessiot ring is R′ = K(y), where y2 = t and σ(y) = −√qy.
Clearly R′ does not embed in U. If instead we had considered this system over K(
√
t),
then the new Picard-Vessiot ring R′′ is not a domain anymore, because it will contain a
non-zero solution of σ(X) +X = 0 (namely, y/
√
t). In both cases however the Galois group
is Z/2Z. And because R′ embeds in R′′, it also embeds in K(T ) ⊗ϕ(CL)D′
U .
This suggests that, when CK =DK, if one takes M to be the subﬁeld of U generated over
27
KC U by all tuples of U satisfying some linear diﬀerence equation over K, then M⊗CUD′
U is a
universal (full) Picard-Vessiot ring of KD ′
U . This ring is not so diﬃcult to describe in terms
of M. Observe that M containsDU . Thus M⊗CUD′
U is isomorphic to M⊗DU (DU ⊗CUD′
U ).
It is a regular ring, with prime spectrum the Cantor space C (i.e., the prime spectrum of
DU ⊗CU D′
U ), and σ acting on C. As a ring, it is isomorphic to the ring of locally constant
functions from C to M.
It would be interesting to relate this ring to the universal Picard-Ve ssiot rings deﬁned
in [23].
Remark 4.20 Saturation hypotheses . The saturation hypothesis on U is not really
needed to deﬁne the model-theoretic Galois group, since we only nee d U to contain a copy
of L to deﬁne it. We also used it in the proof of Proposition 4.11, when we ne eded a
K-embedding of L into U. Thus, to deﬁne the model-theoretic Galois group, we only need
U to be a generic diﬀerence ﬁeld containing K. Its ﬁeld of constants will however usually
be larger than CK. Indeed, the ﬁeld CU is always a pseudo-ﬁnite ﬁeld (that is, a perfect,
pseudo-algebraically closed ﬁeld, with Galois group isomorphic to ˆZ). However, one can
show that if F is a pseudo-ﬁnite ﬁeld of characteristic 0, then there is a generic diﬀ erence
ﬁeld U containingF and such that CU =F . Thus, the ﬁeld of constants of U does not need
to be much larger than CK. In the general case, a general non-sense construction allows
one to ﬁnd a pseudo-ﬁnite ﬁeld F containing CK and of transcendence degree at most 1
overCK.
Remark 4.21 A partial description of the maximal σℓ-ideal p of R. We keep the
notation of the previous subsections, and will ﬁrst assume that th e Picard-Vessiot ring
R′ =R/q is a domain contained in U.
We will describe some of the elements of q. Write CL = CK(α1,...,α m), and αi =
fi(Y )/gi(Y ), wherefi(Y ),g i(Y ) ∈K[Y ] are relatively prime. Then σ(fi)(AY ) andσ(gi)(AY )
are also relatively prime. Looking at the divisors deﬁned by these poly nomials, we obtain
that there is some ki ∈K such that σ(fi)(AY ) = kifi(Y ) and σ(gi)(AY ) = kigi(Y ). Then
(q,f i(Y )) and (q,g i(Y )) are σ-ideals. By the maximality of q, this implies that either fi(Y )
and gi(Y ) are both in q, or else, say if fi(Y ) /∈ q, that there is some ci ∈ CR′ such that
gi(y) = cifi(y), because fi(y) is invertible in R′. If Pi(Z) is the minimal monic polynomial
of ci overCK and is of degree r, then gi(Y )rPi(gi(Y )/fi(Y )) ∈ q. In case CR′ = CK (this
is the case for instance if CK is algebraically closed), then ci ∈ CK, and gi(Y ) −cifi(Y )
will belong to q. (Note also that if ki = kj, then also for some dj ∈ CK we will have
fj(Y ) −djfi(Y ) ∈ q, and gj(Y ) −cjdjfi(Y ) ∈ q). The σ-ideal I generated by all these
polynomials in R could all of q. In any case one shows easily that q is a minimal prime
ideal containing it (because KC L[Y, det(Y )−1] and R/I have the same Krull dimension,
which is also the Krull dimension of R′).
28
A better result is obtained by Kamensky in [13] Proposition 33: if CR′ = CK, and
instead of looking at a generating set of CL overCK one applies the same procedure to all
elements of CL, one obtains a generating set of the ideal q.
In case R′ is not a domain, we reason in the same fashion to get a partial descrip tion
of the σℓ-ideal p.
References
[1] Yves Andr´ e. Diﬀ´ erentielles non commutatives et th´ eorie de Galois diﬀ´ erentielle ou aux
diﬀ´ erences.Ann. Sci. ´Ecole Norm. Sup. (4) , 34(5):685–739, 2001.
[2] Andrzej Bialynicki-Birula. On the Galois theory of ﬁelds with operat ors. Amer. J.
Math., 84:89–109, 1962.
[3] Lawrence Breen. Tannakian categories. In U. Jannsen and et a l, editors, Motives,
volume 55 of Proceedings of Symposia in Pure Mathematics , pages 337–376. American
Mathematical Society, 1994.
[4] Zo´ e Chatzidakis and Ehud Hrushovski. Model theory of diﬀeren ce ﬁelds. Trans. Amer.
Math. Soc. , 351(8):2997–3071, 1999.
[5] Richard Cohn. Diﬀerence Algebra . Tracts In Mathematics, Number 17. Interscience
Press, New York, 1965.
[6] Pierre Deligne. Cat´ egories tannakiennes. In P. Cartier et al., ed itor, Grothendieck
Festschrift, Vol. 2 , pages 111–195. Birkh¨ auser, 1990. Progress in Mathematics, V ol.
87.
[7] Pierre Deligne and James Milne. Tannakian categories. In P. Deligne et al., editor,
Hodge Cycles, Motives and Shimura Varieties , pages 101–228, 1982. Lecture Notes in
Mathematics, Vol. 900.
[8] Tobias Dyckerhoﬀ. Picard-Vessiot Extensions over Number Field s. Diplomarbeit,
Fakult¨ at f¨ ur Mathematik und Informatik der Universit¨ at Heidelberg, 2005.
[9] Pavel I. Etingof. Galois groups and connection matrices of q-diﬀerence equations.
Electron. Res. Announc. Amer. Math. Soc. , 1(1):1–9 (electronic), 1995.
[10] Charles H. Franke. Picard-Vessiot theory of linear homogeneo us diﬀerence equations.
Transactions of the AMS , 108:491–515, 1963.
[11] Charlotte Hardouin. Structure Galoisienne des Extensions
It´ er´ ees de Modules Diﬀ´ erentiels . Ph.D. thesis, Paris 6, 2005,
http://www.institut.math.jussieu.fr/theses/2005/hardouin/.
29
[12] Ehud Hrushovski. Contributions to stable model theory . PhD thesis, Berkeley, 1986.
[13] Moshe Kamensky. Deﬁnable groups of partial automorphisms. Preprint;
http://arxiv.org/abs/math.LO/0607718, 2006.
[14] Nicholas Katz. On the calculation of some diﬀerential Galois group s. Inventiones
Mathematicae, 87:13–61, 1987.
[15] Ellis R. Kolchin. Algebraic matric groups and the Picard-Vessiot th eory of homoge-
neous linear ordinary diﬀerential equations. Annals of Mathematics , 49:1–42, 1948.
[16] Ellis R. Kolchin. Existence theorems connected with the Picard-V essiot theory of
homogeneous linear ordinary diﬀerential equations. Bull. Amer. Math. Soc. , 54:927–
932, 1948.
[17] Ellis R. Kolchin. Diﬀerential Algebra and Algebraic Groups . Academic Press, New
York, 1976.
[18] Mathew A. Papanikolas. Tannakian Duality for Anderson-Drinfe ld Motives and
Algebraic Independence of Carlitz Logarithms. Preprint, Texas A& M University;
http://arxiv.org/abs/math.NT/0506078, 2005.
[19] A. Pillay. Diﬀerential Galois Theory I. Illinois J. Math. 42 (1998), 678–699.
[20] Bruno Poizat. Une th´ eorie de Galois imaginaire. J. of Symb. Logic , 48:1151–1170,
1983.
[21] Cornelius Praagman. Fundamental solutions for meromorphic lin ear diﬀerence equa-
tions in the complex plane, and related problems. J. Reine Angew. Math. , 369:101–109,
1986.
[22] Marius van der Put and Marc Reversat. Galois Theory of q-diﬀerence equations.
Preprint; http://arxiv.org/abs/math.QA/0507098, 2005.
[23] Marius van der Put and Michael F. Singer. Galois Theory of Diﬀerence Equations ,
volume 1666 of Lecture Notes in Mathematics . Springer-Verlag, Heidelberg, 1997.
[24] Marius van der Put and Michael F. Singer. Galois Theory of Linear Diﬀerential
Equations, volume 328 of Grundlehren der mathematischen Wissenshaften . Springer,
Heidelberg, 2003.
[25] Jean-Pierre Ramis and Jacques Sauloy. The q-analogue of the wild fundamental group
(I). Preprint; http://arxiv.org/abs/math.QA/0611521, 2006.
[26] Jacques Sauloy. Galois theory of Fuchsian q-diﬀerence equations. Ann. Sci. ´Ecole
Norm. Sup. (4) , 36(6):925–968 (2004), 2003.
30
[27] William C. Waterhouse. Introduction to Aﬃne Group Schemes , volume 66 of Graduate
Texts in Mathematics . Springer-Verlag, New York, 1979.
[28] Boris I. Zi’lber. Totally categorical theories; structural prop erties and the non-ﬁnite
axiomatizability. in L. Pacholski et al. editors, Model theory of algebra and arithmetic
(Proc. Conf., Karpacz, 1979) , pages 381–410. Lecture Notes in Mathematics volume
834, Springer Verlag, Berlin Heidelberg 1980.
Addresses
UFR de Math´ ematiques
Universit´ e Paris 7 - Case 7012
2 place Jussieu
75251 Paris cedex 05
France.
zoe@logique.jussieu.fr
Institut de Math´ ematiques
Universit´ e Paris 6
Tour 46 5e ´ etage
Boite 247
4 place Jussieu
75252 Paris cedex 05
France
hardouin@math.jussieu.fr
North Carolina State University
Department of Mathematics
Box 8205
Raleigh, North Carolina 27695-8205
USA
singer@math.ncsu.edu.
31
