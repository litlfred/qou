---
doc_id: cherednik1991-kz-dunkl
doc_title: "A unification of Knizhnik-Zamolodchikov and Dunkl operators via affine Hecke algebras"
section_id: sec-003-3-the-unification-some-examples
section_title: "The unification, some examples"
section_number: "3"
pages: 14-20
source_pdf: cherednik1991-kz-dunkl.pdf
source_sha256: cae9cf747bb98a46
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
---
3 The unification, some examples
We keep to the notations of the beginning of Sect. 1. Let A be some C-algebra
equipped with a homomorphism vo: W-→ A*, (ra, αe Z)  A. Let us define the
elements
Du = Z (u, α)ra, ueCn . (3.1)
α>0
One has Dru+5u = Du + D,, u, veC", , eC. In particular,
def
D; = Da* = Z μara, Du =Z(u, αi)Di, 1≤i≤n, (3.2)
α>0
Affine Hecke algebras 425
where [α*} are dual weights ((αi, α*) =- Si, for the Kronecker symbol Sii), μ is the
multiplicity of α; in α. We put Da - Z.(u, aα)ra, where αe a E+, a is a subset in R".
Definition 3.1 The set (r} is a classical A-valued r-matrix of type An, : . : , G2, if
rw(a) = Vo(w)ravo(w)-1 for αeZ, weW, (3.3)
[Di, D] = O, = Rαi + Rαj. (3.4)
Here (αi, αj) runs over all classes of pairs of simple roots modulo the action of
W on the latter (one pair for A2, B2, C2, G2, two for An, Dn, E6-8, three for B3, C3
four for Bn, Cn, F4, n > 2).
Proposition 3.2 (see [Ch 1, Ch 2]) Elements {Du, uE Cn} are pairwise commutative
for (r.} from Definition 3.1.
Proof. It is sufficient to consider the elements Di, : : : , Dn. One has:
[Di, D;] =da, dä= μμ[ra, r],
α, βe+
where + = a  Z+, ^ runs over all two-dimensional subspaces in Rn. Indeed, only
trivial pairs {α = β) can belong to some  a' for a + 2'. Let ,  be the pair of
simple roots in a+ = ^ Z+ (if the latter is two-dimensional) and a, , be the
multiplicities of , S in αe a+ respectively. Then μa = aμ, + S。μ. Hence,
da = Z (, +)(βu, + p)[ra, rp]
α, βe^+
= μi,μj[D1, D1] + μou[D2, D2] +(u, μ - μjμ)[D1, D2] ,
where D1, D2 are from (3.2) but for a+ and (?, 3) in place of E+ and {α1, . . . , αn)
Therefore the identity [Di, D2J = O is sufficient to prove the proposition.
The roots y,  can be included into the system of simple roots corresponding to
a certain Weyl chamber (see [Bo]). Hence,  = w(αs),  = w(αm) for a suitable
we W and appropriate simple αk, αm. We arrive at (3.4). 
Proposition 3.3 [Ch 1] Let {Ra, αE E}  A* be a quantum W-invariant R-matrix in
def
the sense of [Ch 5], ie. the set {R.} satisfies conditions (3.3) and t;  R;vo(si)e A*
for R; =- Ra, satisfy the braid relations (1.1). Assume that R depend on some parameter
heC and
R; = 1 + hr; + o(h), 1 ≤i≤n, riEA, (3.5)
in a neighbourhood of h = O. Let [Ra, R] = O if (α, β) = O. In the case of G2 we
suppose additionally that R Ra+pRp = RgRa+pRa for long positive roots α, β, α + β.
Then (ri, 1 ≤i ≤ n) can be uniquely extended to a classical r-matrix (ra, aeE) by
means of (3.3).
Proof. The cases A2, B2, G2 are enough to consider. Let α = α1, β = α2. For A2
one has the following (quantum Yang-Baxter) identity
R.Ra+βR = RpRα+βRα '
426 I. Cherednik
which gives (see (3.5) the well-known classical "abstract" Yang-Baxter relation
[ra, ra+p] + [ra, rg] + [ra+β, rp]  O. (3.6)
For B2 we obtain the relation
R.Ra+βRα+2βRβ = RpRa+2βRα+βRα 
which results in
[ra, rg + raα+p]  [ra+2β, ra+β - rp] (3.7)
because of the orthogonality conditions [ra, ra+ 2p] -- O = [ra+β, rg], which follow
from the corresponding conditions for R. For G2 one has (see [Bo])
RR3α+βR2α+βR2β+ 3αRα+βRβ = RpRa+βR2β+ 3αR2α+βR3α+β Ra
and the relations
[rp, rα + ra+β] + [r2a+β, r3a+β - r3α+2β] = [ra, r3α+β] + [r3α+2β, rα+β] (3.8)
together with (3.6) for rp, r3a+β, r3a+ 2β and
[rg, r2α+β] = [ra+β, r3α+β] = [rα, r3α+2β] = 0 .
Relations (3.6-8) modulo the orthogonality y conditions (α, β) = O=)
[ra, rp] = O) are equivalent to Definition 3.1. Owing to (3.3) we have only one
unknown element r. in the case of A2 and two of them (ra and rg) for B2, G2. 
Let us consider A - EndcC(Y)@c A or A = EndcC(y) c A instead of A,
where C(Y) and C(y) are from Sect. 1. We have the homomorphism W × W -→ A
taking 1 × w to Vo(w)e 1@A and w × 1 to the corresponding automorphism of C(Y)
or C(y). By definition
To(w) = wVo(w), we W, (3.9)
where w, vo(w) are identified respectively with w × 1 and 1 × vo(w). One has:
wvo(w') -- vo(w')w for any w, w'e W.
Let (pa, αeE) be a classical A-valued (i.e. “constant") r-matrix with the
following "quasi-unitary" condition
Pα + Vo(sa)pαVo(ss) = 1 + Vo(sα) or = 0 (3.10)
respectively in the case of Y or y. We fix k', k", S', S" e C and denote by K. either k' or
k" for short or long roots, K; =- Ka (the same notations hold for §).
Theorem 3.4 The set
rα = Ka(pα + (Yα- 1)-1 vo(ss)(1 - sα)), αeZ, (3.11)
ro = Ke(pα + y 1 vo(s)(1 - Sas) for y (3.12)
is a classical A-valued r-matrix with respect to Vo.
The proof is based on the following lemma directly resulting from formulas (2.1),
(2.3).
Affine Hecke algebras 427
Lemma 3.5 In the setup of Sect. 2 let A =- EndcV,
qi - 1 = hi = kih, heC, 1≤i≤n. (3.13)
We will assume that the homomorphism v: H -→ Endc V from Sect. 2 (or its counter-
W-→ A* = Autc V above
v(Ti) = Vo(si) + hipiVo(si) + o(h) (3.14)
or
v(si) = Vo(si) + hipiVo(si) + o(h) (3.15)
and
Vo(w)v(Ti)vo(w)-1 = v(T;) if w(αi) = αj (3.16)
or
Vo(w)v(si)vo(w)-1 = v(sj) if w(αi) = αj , (3.17)
where 1 ≤ i,j ≤ n. Then Pa, = pi satisfy (3.10) because of (1.2) and the set
R; = To(si) or R;= so(si),1≤i≤n, (3.18)
for T! , s? from Theorem 2.1 and o from (3.9) can be uniquely extended to a quantum
A-valued W-invariant R-matrix with respect to o. The corresponding classical
r-matrix (see Proposition 3.3) coincides with (3.11), (3.12) for S' = 1 =- S".
Thanks to the lemma we obtain the statement of Theorem 3.4 for A -- EndcV
and ' - 1 = 8". Really,
R; = T?vo(s;) = 1 + hk;(Y; - 1)-1(1 - si)vo(si) + hkiPi
(see (2.1). Here and further we will identify Y? and Y:. As for (3.12), we can apply
(2.3). In the case S' = 0 = S" Theorem 3.4 was proven in [Ch 1, Ch 2]. The case
' -- S" -→co is completely analogous to the previous one. A direct consideration
for A2, B2, G2 shows that this is enough to prove the theorem. 
Now let us first combine all p. in Du (r. are as above), then secondly add some
"scalar" terms to Du.
Corollary 3.6 The following elements from A are pairwise commutative (1 ≤ i ≤ n):
D; = Y,og/Y; + Vo(xi) + Z Kαμ(Yα- 1)-1 vo(ss)(1 - &s), ( (3.19)
ae+
D; = dg/oy; + Vo(x) + Z Kαμa y1 vo(1 - Oasα) (3.20)
for Y and y respectively and g from C(Y)w or C(y)w. Here [xi, x;] =- O for 1 ≤ i, j ≤ n
and X; satisfy relation (1.5) for y* = ya*, h; = - (αi, αi) Ki/2 ((α*}-are the dual
weights), (x} obey the same relations but for h; = O (1 ≤ i ≤ n). These {xi} or [x?]
are added to (si} and the homomorphism vo: C[WJ -→ A is assumed to be extended to
(xi), (x].
Proof. We will only check here that
def
Vo(xi) : Z Kα(pα-1/2), αeZ, 1≤i≤n
α>0
428 I. Cherednik
satisfy relations (1.5) for y* with the constants h; above, where p. are from Theorem
=     ! ()'s sn 1     =[(ix)o ('s)  
(α, α*) = (s;(α), α*). Similarly,
Vo(si) vo(xi)vo(si) - K;(pi + Vo(si) p;Vo(si) - 1) = Z Ke(α, Si;(α*)) (pα - 1/2) .
α>0
Here we have used that s; does not change the terms μdα; in α for j + i and therefore
takes O < α + α; to some positive root. Hence, (3.1O) results in
SiXi - Z (s(α*), αu)x )s = - Ki, 1≤i≤n,
(k=1
which is (1.5) for xi = y* and h = - (αi, αi)Ki/2, 1 ≤ i ≤ n.
The commutativity relations [xi, xj] -- O are valid because the set (p.} is an
r-matrix. For (x?} (without g) reasoning is the same. One can deduce the general
statement (without g) from this partial results, but the direct calculation of the
commutativity is a more natural way and is not dificult. As for the introduction of
g, it is due to the relations μa[ra, y*］ + μdly*, ra] = O. This proves the required
commutativity. 
Now we are in a position to explain the main theorem of this section. Later on,
A =- Endc V. Let us introduce partial derivatives ou, ue Cw, on Vo - C( Y)c V or
= C(y)@c V (see Sect. 2 and Lemma 3.5) by
Qu(Yα) = (u, α)Yα, Qu(yα) = (u, α), Qu(V) = O , (3.21)
where αe E. In particular, O; = Oα*(1 ≤ i, j ≤ n). One has
Oau+βu = αQu + βOu, wOuw-1 = Ow(u) (3.22)
for u, u'eCn, α, βeC, we W.
Theorem 3.7 Put
Vu= Ou + Du, Du=  (u, αi)Di, ueCn (3.23)
i= 1
where D; are from (3.19) or (3.20). Then Vu, ueCn, form a commutative family of
operators in Endc Vo for arbitrary k', k", S', S", g. For (D;} of type (3.20) or in the case
" = O = S" one has: Do(w)Duvo(w)-1 = Dw(u), where vo is from (3.9), ue Cn, we W.
Proof. Let us check the identities [Oi, μdra] = [oj, μra] for 1 ≤ i,j ≤ n, αe E+. By
(3.22) μio; - μd, = Qu, where u = μiα* - μα . Hence, ou(Y - 1) = (u, α)Y = 0
 Qu(y) and [ou, 1 -- Sas.]  Sa(Ou -- Osa(u)) -- 0.
We will discuss now some particular cases. Let us consider first the “rational"
case of C(y) with x? = O for all i. If S' = O = ", g = O, then one arrives at the
generalized Knizhnik-Zamolodchikov equation from [Ch 1, Ch 2]. The Dunkl
operators (see [Du, He2]) can be obtained for V = Cand ' -- 1 =- S", g = 0. In this
case
rα= Ky1(1 - Ss), αeE+. (3.24)
The Lusztig-Lascoux-Schitzenberger operators give a natural proof of the com-
mutativity of the corresponding family (3.23)
Affine Hecke algebras 429
To get the “trigonometric" operators {Vu) we need some ( p.} (Theorem 3.4) or,
more generally, an extension of our initial representation vo : W -→ Endc V to some
representation of the algebra Jf', generated by C[WJ and x1 : : . xn above. The
quantum counterpart of the first problem is in constructing representations of
H satisfying conditions (3.14) and (3.16). For example, the well-known Baxter
basic representations Vo for one-dimensional V, are other examples. They satisfy
conditions (3.14), (3.16) and look to be very universal for many purposes.
The trigonometric Vu) without (s.} (i.e. for S' -- O = S") are new and general-
ize directly the affine system from [Ch 2 in the case of An, although the latter was
written down in a rational form. This system is a natural candidate to obtain some
interpretation of Lusztig's isomorphisms (see (2.13), (2.14) and Sect. O) via mono-
dromy matrices.
Till the end of this paper we will consider C[Y], $' - 1 = s", V = C, g = O.
Then both (2.9) and (2.10) modulo some multipliers and constants are equivalent
and can be written as follows:
r= (Y- 1)-1(Sα- 1)+ C, αZ, cEC, (3.25)
and Vu = u + Zα>o(u, α)ra, ueC. These (ra} are analogous to
rα= ka(Yα+ 1)(Yα- 1)-1 (sα- 1) (3.26)
from Heckman's paper [He1]: r. -- r = k.(s. -- 1)/2. Our (ra} are not “unitary"
(r + Sar& s. = K(i - s)+ O). Hence, Vw(u) + wVuw-1 for some w, u. However
Theorem 3.7 is valid for them. Heckman's Vu = Ou + Za>o (u, α)r. are W-invariant
in the above sense, but do not form a commutative family. Let us show that Vu have
the two main properties of Heckman's Vu. Namely, they are self-adjoint with
Calogero-Moser-Olshanetsky-Perelomov type. We follow [He2] very closely. Let
mEX(Z--" +"X)  =
αe+
cmYm, if P= Co + Zα,m+ocm YmeC[Y],
<P>= Co:
Proposition 3.8 (a) (VuP, P') = (P, VuP'), where (P, P') =<PP'△>, P, P'eC[Y],
ue C.
(b) The operator  = Er"=1 Va, V; -  for c  --  is equal to Zr- V, V; and to
Z 0a, 0; -- Z ka(Yα + 1)(Yα - 1)-1 0
i=1 α>0
after the restriction to C[Y]w.
Proof. The adjoint V* of Vu for c =- O with respect to (,) is equal to
4-1( u +  ka(u, α)(1 - sa)(Y1 - 1)-
α>0
430 I. Cherednik
For Heckman's one (which is self adjoint-see [He1J) the corresponding formula is
with (Y-1 + 1)(Y=1 -- 1)-1 instead of (Y-1 - 1)-1. Hence,
Z ka(u, )(sa - 1)4
α>0
α>0
and
V* = Vu·
One has
=  a,0 - 2  ka(Y- 1)-1α + 2c c  K.0+c?
α>0 α>0
because re -- c acts trivially on C[Yjw and
Z (u, αi)0; =- Z (u, α*)0a, = 0a
i=1 i 1
(see [He1, Ex. 3.9]).
Acknowledgements. This paper was written during my stay at RIMS (Kyoto University) and is
partially based on my lectures at RIMS on Hecke algebras. I am grateful for the kind invitation
and for hospitality. I should like to acknowledge my special indebtednes to T. Miwa. I thank S.
Kato for a useful discussion on his and Lusztig's works, G. Heckman for the explanation of the
main points of his last papers, V. Jones, who helped me understand the Lascoux-Schitzenberger
results and supplied me with his new notes, and A. Matsuo for many interesting talks about the
Heckman, Opdam works and his own results. I express also appreciation to E. Date, Y. Ihara, M.
Jimbo, M. Kashiwara, M. Sato, D. Zagier for their kind interest in my work, to the participants of
my talks for encouragement, to my other colleagues at RIMS for many useful discussions and to
S. Miwa for her assistance in preparing the manuscript for publication.
