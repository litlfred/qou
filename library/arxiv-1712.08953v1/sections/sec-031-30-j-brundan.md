---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-031-30-j-brundan
section_title: "J. BRUNDAN"
section_number: 30
pages: 30-36
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
---
for any λ ∈ e-Bip. In particular, this means that L( λ ) can also be realized as the
irreducible socle of ¯∇(λ ).
Lemma 5.5. The functors ∆ and∇ send ﬁnite-dimensional OS◦-modules to locally
ﬁnite-dimensional OS-modules. Moreover, the functors ⊛◦∆ and∇◦⊛ are isomorphic
on ﬁnite-dimensional OS◦-modules.
Proof. The ﬁrst statement is easy to see from the deﬁnitions; for ∇, one needs to
know that 1 aOS is a ﬁnitely generated right OS♭-module by Lemma 5.1. Then, for a
ﬁnite-dimensional OS◦-module M , we deﬁne an OS-module homomorphism
(inﬂ♯M⊗OS ♯ OS)⊛→
⨁
a∈⟨↑,↓⟩
HomOS ♭ (1aOS, inﬂ♭(M⊛)), θ ↦→ˆθ
whereˆθ(f )(v) = θ(v⊗τ (f )) for v∈M,f ∈ 1aOS. There is a two-sided inverse
⨁
a∈⟨↑,↓⟩
HomOS ♭(1aOS, inﬂ♭(M⊛))→ (inﬂ♯M⊗OS ♯OS)⊛, ψ ↦→~ψ
where ~ψ(v⊗f ) = ψ(τ (f ))(v). □
We say that anOS-moduleM has a ﬁnite ∆ -ﬂag if it has a ﬁnite ﬁltration whose sec-
tions are isomorphic to standard modules ∆( λ ) for various λ∈e-Bip. Let ∆Mod- OS
be the full subcategory of Mod- OS consisting of all modules with a ﬁnite ∆-ﬂag. We
view it as an exact category with admissible sequences being the ones that are exact
in Mod-OS. The next three lemmas are all well known in this sort of situation.
Lemma 5.6. The restriction of ∆( λ ) toOS♭ is isomorphic to Y(λ )⊗OS ◦OS♭. These
modules give all of the indecomposable projective OS♭-modules (up to isomorphism).
Proof. The ﬁrst statement is clear from Lemma 5.1. For the second, obser ve that the
OS♭-modules Y( λ )⊗OS ◦ OS♭ are induced from the projective OS◦-modules, hence,
they are projective and every indecomposable projective OS♭-module is isomorphic to
a summand of one of them. It remains to show that Y( λ )⊗OS ◦OS♭ is indecomposable.
This follows because EndOS ♭(Y(λ )⊗OS ◦OS♭)∼= EndOS ◦ (Y(λ )), which is local as Y( λ )
is indecomposable. □
In view of the following lemma, the Grothendieck group K0(∆Mod- OS) of the exact
category ∆Mod- OS is the free Z-module on basis {[∆( λ )]| λ∈e-Bip}.
Lemma 5.7. For λ, µ∈e-Bip and d≥ 0, we have that
dim Extd
OS (∆( λ ), ¯∇(µ )) =
{
1 if d = 0 and λ = µ ,
0 otherwise.
Hence, for any M∈ Mod-OS with a ﬁnite ∆ -ﬂag, the multiplicity (M : ∆( λ )) of ∆( λ )
as a section of such a ﬂag is well deﬁned independent of the par ticular choice of ﬂag,
and it satisﬁes (M : ∆( λ )) = dim HomOS (M, ¯∇(λ )).
Proof. For the ﬁrst statement, we have natural isomorphisms
Extd
OS (∆( λ ), ¯∇(µ ))∼= Extd
OS
(
∆( λ ),
⨁
a∈⟨↑,↓⟩
HomOS ♭
(
1aOS, inﬂ♭ D(µ )
) )
∼= Extd
OS ♭(Y(λ )⊗OS ◦OS♭, inﬂ♭ D(µ ))
∼= Extd
OS ◦ (Y(λ ), D(µ )).
This is zero unless λ = µ andd = 0 as Y( λ ) is the projective cover of D( λ ). It follows
that dim HomOS (M, ¯∇(λ )) counts the multiplicity of ∆( λ ) in a ∆-ﬂag of M , giving
the second statement. □
ORIENTED SKEIN CATEGORY 31
The next lemma shows that ∆Mod- OS is Karoubian.
Lemma 5.8. AnOS-moduleM has a ﬁnite ∆ -ﬂag if and only if it is ﬁnitely generated
and projective as an OS♭-module. Hence, any direct summand of a module with a ﬁnite
∆ -ﬂag also has a ﬁnite ∆ -ﬂag.
Proof. If M has a ﬁnite ∆-ﬂag, then it is ﬁnitely generated and projective over OS♭
thanks to Lemma 5.6. Conversely, suppose that M is ﬁnitely generated and projective
overOS♭, so that the restriction of M to OS♭ is isomorphic to a direct sum of some
numbern ofOS♭-modules of the form Y( λ )⊗OS ◦OS♭. We show that M has a ﬁnite ∆-
ﬂag by induction on n. The case n = 0 is trivial. If n> 0, we choose r,s≥ 0 with r +s
minimal such that the restriction of M toOS♭ has a summand M′∼= Y(λ )⊗OS ◦OS♭ for
some λ∈e-Bipr,s. The OS◦-module homomorphism Y( λ )∼= Y(λ )⊗OS ◦OS♭[0]֒→M′
is actually an OS♯-module homomorphism inﬂ ♯ Y(λ )֒→M since its image is in the
shortest word space of M . Hence, we get induced an OS-module homomorphism
∆( λ )→ M with image M′. This shows that M′ is actually an OS-submodule of M
and M′∼= ∆( λ ). The quotient M/M′ is ﬁnitely generated and projective over OS♭
with one fewer indecomposable summand. It remains to apply the indu ction hypothesis
to deduce that M/M′ has a ﬁnite ∆-ﬂag, hence, so does M . □
Now we look at projectives. Let P( λ ) be a projective cover of L( λ ). The classes
{[P(λ )]| λ∈e-Bip} give a basis for K0(pMod-OS). The OS-module
Q(λ ) := Y( λ )⊗OS ◦OS (5.11)
described by the following theorem should be viewed as a ﬁrst approx imation to P( λ ).
Theorem 5.9. For λ ∈ e-Bipr,s, the module Q(λ ) has a canonical ﬁltration with
sections indexed by d = 0, 1,..., min(r,s ) appearing in order from top to bottom, such
that the dth section is isomorphic to
⨁
µ∈e-Bipr−d,s−d
∆( µ )⊕M λ
µ (e,p) (5.12)
where M λ
µ (e,p ) := ∑
ν∈e-Bipd,d
[
Dµ↑◦ Dν↑ : Dλ↑
][
Dµ↓◦ Dν↓ : Dλ↓
]
[Yν↑ : Dν↓ ] (which
depends on e and the characteristic p of the ﬁeld k ).
Proof. Take 0 ≤ d≤ min(r,s ). We always view Hd as a subalgebra of Hr or Hs
via the natural embeddings. We also need the “unnatural” embeddin gs Hr−d֒→Hr
and Hs−d֒→Hs which send Si↦→Sd+i; the images of these embeddings centralize
Hd. Let Hom Hd (Hs,Hr) be the space of all right Hd-module homomorphisms. Using
the unnatural embeddings for Hr−d and Hs−d, this is an ( Hr⊗Hs−d,Hr−d⊗Hs)-
bimodule. Let τ -HomHd (Hs,Hr) be the the same space but with the left action of
Hs−d and right action of Hs twisted into right and left actions, respectively, using the
anti-automorphism τ which sends Sw ↦→Sw−1. This means that τ -HomHd (Hs,Hr)
is an ( Hr,s,Hr−d,s−d)-bimodule. The space 1 ↓s↑rOS♯1↓s−d↑r−d is also naturally an
(Hr,s,Hr−d,s−d)-bimodule. We claim that these two bimodules are isomorphic.
To prove the claim, Hs is a free right Hd-module with basis {Sy|y∈ D} where
D is the set of minimal length Ss/Sd-coset representatives. So the Hd-module ho-
momorphisms{fx,y :Hs→Hr|x∈ Sr,y∈ D} deﬁned from fx,y(Sz) := δy,zSx for
x∈ Sr,y,z ∈ D give a linear basis for τ -HomHd (Hs,Hr). Let
c :=
r−d
d
s−d
∈ 1↓s↑rOS♯1↓s−d↑r−d,
32 J. BRUNDAN
where the thick arrows labelled by a number represent that number of parallel thin
ones. We will show that the linear map
θ :τ -HomHd (Hs,Hr)→ 1↓s↑rOS♯1↓s−d↑r−d, f x,y↦→ır,s(Sx⊗Sy)c
is an (Hr,s,Hr−d,s−d)-bimodule isomorphism. To see this, it is clear from Theorem 1.2
that θ is a vector space isomorphism. We must check that it is a bimodule homo mor-
phism. This is straightforward for the left action of Hr and the right action of Hr−d.
In the next two paragraphs, we check it for the left action of Hs and the right action
of Hs−d, respectively.
To show θ is a left Hs-module homomorphism, take x∈ Sr,y ∈ D and 1≤ i < s.
By [DJ1, Lemma 1.1], exactly one of the following holds: (a) siy∈ D; (b) sy−1(i)∈ Sd.
In case (a), SiSy =Ssiy if ℓ(siy)>ℓ (y) or Ssiy + (q−q−1)Sy if ℓ(siy)<ℓ (y). In case
(b), SiSy =SySy−1(i) and
ır,s(Sx⊗SiSy)c =ır,s(Sx⊗SySy−1(i))c =ır,s(SxSy−1(i)⊗Sy)c.
We deduce for z∈ D that
(θ−1(Siθ(fx,y)))(Sz) = (θ−1(ır,s(Sx⊗SiSy)c))(Sz )
=



fx,siy(Sz) if siy∈ D,ℓ (siy)>ℓ (y),
(fx,siy + (q−q−1)fx,y)(Sz) if siy∈ D,ℓ (siy)<ℓ (y),
fxsy−1 (i),y(Sz) if siy /∈ D,ℓ (xsy−1(i))>ℓ (x),
(fxsy−1 (i),y + (q−q−1)fx,y)(Sz) if siy /∈ D,ℓ (xsy−1(i))<ℓ (x)
=



δsiy,zSx if siy∈ D,ℓ (siy)>ℓ (y),
δsiy,zSx + (q−q−1)δy,zSx if siy∈ D,ℓ (siy)<ℓ (y),
δy,zSxSy−1(i) if siy /∈ D.
We need to show this is equal to
(Sifx,y)(Sz) = fx,y(SiSz) =



δy,sizSx if siz∈ D,ℓ (siz)>ℓ (z),
δy,sizSx + (q−q−1)δy,zSx if siz∈ D,ℓ (siz)<ℓ (z),
δy,zSxSy−1(i) if siz /∈ D.
This follows easily by considering several cases: (a) y =z; (b) y =siz; (c) siy =z; (d)
none of the above.
To show that θ is a right Hs−d-module homomorphism, take x∈ Sr,y,z ∈ D and
1≤i<s −d. We must show that ( θ−1(θ(fx,y)Si))(Sz) = (fx,ySd+i)(Sz), i.e.,
(θ−1(ır,s(Sx⊗SySd+i)c)(Sz) = fx,y(SzSd+i).
This time, ysd+i∈ D always. So the left hand side of the identity to be proved equals{ δysd+i,zSx if ℓ(ysd+i)>ℓ (y),
δysd+i,zSx +δy,z (q−q−1)Sx if ℓ(ysd+i)<ℓ (y).
Similarly, the right hand side is{ δy,zs d+iSx if ℓ(zsd+i)>ℓ (z),
δy,zs d+iSx +δy,z (q−q−1)Sx if ℓ(zsd+i)<ℓ (z).
The two sides are equal by considering four cases like before.
We have now proved the claim made in the opening paragraph. To prov e the theo-
rem, we must construct the ﬁltration of Q( λ ). By transitivity of induction,
Q(λ ) = (Y( λ )⊗OS ◦ OS♯)⊗OS ♯OS.
SinceOS♯ is positively graded, the grading gives us a ﬁltration of Y( λ )⊗OS ◦OS♯ as an
OS♯-module with sections Y( λ )⊗OS ◦OS♯[d] for d = 0, 1,... appearing in order from
ORIENTED SKEIN CATEGORY 33
top to bottom. The dth section is clearly zero unless d≤ min(r,s ). Since the functor
?⊗OS ♯ OS is exact, we are thus reduced to checking for 0 ≤d≤ min(r,s ) that
Y(λ )⊗OS ◦ OS♯[d]∼=
⨁
µ∈e-Bipr−d,s−d
Y(µ )⊕M λ
µ (e,p)
as a right OS◦-module. Using Lemma 5.2, we show equivalently that
(Yλ↑⊠ Yλ↓ )⊗Hr,s 1↓s↑rOS♯1↓s−d↑r−d∼=
⨁
µ∈e-Bipr−d,s−d
(Yµ↑⊗ Yµ↓ )
⨁ M λ
µ (e,p)
as a right Hr−d,s−d-module. By the opening claim, the module on the left hand side
is isomorphic to
(Yλ↑⊠ Yλ↓ )⊗Hr,sτ -HomHd (Hs,Hr)∼=τ -HomHd (Yλ↓, Yλ↑ ),
where we have used the self-duality of Y λ↓ . Then we note by Frobenius reciprocity
that
resHr
Hr−d,d Yλ↑∼=
⨁
µ↑⊢(r−d),ν↑⊢d
(Yµ↑⊠ Yν↑ )⊕[Dµ↑◦Dν↑ :Dλ↑ ],
resHs
Hs−d,d Yλ↓∼=
⨁
µ↓⊢(s−d),ν↓⊢d
(Yµ↓⊠ Yν↓ )⊕[Dµ↓◦Dν↓ :Dλ↓ ].
Making these substitutions in τ -HomHd (Yλ↓, Yλ↑ ), using also dim HomHd (Yν↓, Yν↑ ) =
[Yν↑ : Dν↓ ] and self-duality of Y µ↓ , gives the conclusion. □
Corollary 5.10. For λ∈e-Bipr,s, the module Q(λ ) is isomorphic P(λ ) plus a ﬁnite
direct sum of projectives P(µ ) for bipartitions µ ∈ ∐ min(r,s)−1
d=0 e-Bipr−d,s−d. Hence,
the classes {[Q(λ )]| λ∈e-Bip} give another basis for K0(pMod-OS).
Proof. Note that Q( λ ) is projective since the functor ? ⊗OS ◦ OS sends projectives to
projectives. Also the top section of the ∆-ﬂag of Q( λ ) constructed in Theorem 5.9
is ∆( λ ), so Q( λ ) has P( λ ) as an indecomposable summand. The other sections only
involve ∆( µ ) for µ ∈∐ min(r,s)−1
d=0 Bipr−d,s−d, so all other summands are of the form
P(µ ) for such µ . □
Corollary 5.11. The projective cover P(λ ) of L(λ ) has a ﬁnite ∆ -ﬂag such that
(P(λ ) : ∆( µ )) = [ ¯∆( µ ) : L( λ )].
Proof. By Corollary 5.10 and Theorem 5.9, P( λ ) is a summand of Q( λ ), and Q( λ )
has a ﬁnite ∆-ﬂag. Hence, P( λ ) has one too due to Lemma 5.8. To deduce the BGG
reciprocity formula, we use Lemma 5.7: (P( λ ) : ∆( µ )) = dim HomOS (P(λ ), ¯∇(µ )) =
[ ¯∇(µ ) : L( λ )]. This equals [ ¯∆( µ ) : L( λ )] by (5.10). □
Corollary 5.12. By Corollary 5.11, there is an embedding pMod-OS→ ∆Mod- OS.
This induces an isomorphism K0(pMod-OS)
∼
→K0(∆Mod- OS).
Proof. The transition matrix arising from (5.12) can be inverted to express each [∆( λ )]
as a ﬁnite linear combination of [Q( µ )]’s. □
Corollary 5.13. For λ∈e-Bipr,s, P(λ ) has a ﬁnite ﬁltration with sections ˜∆( µ ) for
µ∈∐ min(r,s)
d=0 Bipr−d,s−d, each appearing [ ˜∆( µ ) : L( λ )] times.
Proof. Recall for λ∈e-Bipr,s that Y( λ ) has a ﬁnite ﬁltration with sections S( µ ), each
appearing [S( µ ) : D( λ )] times. Applying the exact standardization functor, we deduce
that ∆( λ ) has a ﬁnite ﬁltration with sections ˜∆( µ ), each appearing [S( µ ) : D( λ )] times.
34 J. BRUNDAN
Combined with Corollary 5.11, it follows that P( λ ) has a ﬁnite ﬁltration with sections
˜∆( µ ), each appearing with multiplicity
∑
ν∈e-Bip
[ ¯∆( ν ) : L( λ )][S(µ ) : D( ν )].
Also, applying ∆ to a composition series of S( µ ), we see that ˜∆( µ ) has a ﬁltration
with sections ¯∆( ν ), each appearing [S( µ ) : D( ν )] times. Hence, the multiplicity just
displayed is equal to [ ˜∆( µ ) : L( λ )]. □
Proof of Theorem 1.7. The monoidal functor OS◦(z,t )→OS (z,t ) corresponds to the
induction functor ?⊗OS ◦OS : pMod-OS◦→ pMod-OS, since the latter sends eOS◦ to
eOS for any idempotent e. So by the deﬁnition (5.11) it sends Y( λ ) to Q( λ ). Theo-
rem 1.7 follows because the classes {[Q(λ )]| λ∈e-Bip} form a basis for K0(pMod-OS)
according to Corollary 5.10. □
For the next lemma, we return to the situation of Theorem 1.3. We wa nt to relate
the labelling of irreducible OS-modules obtained thus far with the usual labelling of
irreducible Uq(gln)-modules via their highest weights. Take λ ∈ Bipr,s. Since e = 0,
Theorem 5.9 tells us simply that Q( λ ) has a ﬁltration with sections
⨁
µ∈Bipr−d,s−d
∆( µ )⊕M λ
µ where M λ
µ :=M λ
µ (0, 0) =
∑
ν⊢d
LRλ↑
µ↑,νLRλ↓
µ↓,ν (5.13)
for d = 0,..., min(r,s ), and it decomposes as P( λ ) plus a direct sum of projectives
P(µ ) for various bipartitions µ obtained from λ by removing the same number d >0
of boxes from both λ↑ and λ↓. Recalling the Young symmetrizer (3.9), we have that
Y(λ ) = S( λ ) = D( λ ) = ır,s(eλ↑⊗eλ↓ )OS◦. Hence,
Q(λ ) = ır,s(eλ↑⊗eλ↓ )OS. (5.14)
Leteλ be the projection of Q( λ ) onto its unique summand that is isomorphic to P( λ ).
Thus, eλ is a primitive idempotent in the quantized walled Brauer algebra Br,s. The
following recovers results of [KM1, KM2].
Lemma 5.14. Let notation be as in Theorem 1.3 and assume n≥ 0. Take λ∈ Bipr,s
such that h(λ ), its total number of non-zero parts, is ≤ n. Consider the idempotent
Ψ(eλ )∈ EndUq (gln) ((V−)⊗s⊗ (V +)⊗r). Its image is the irreducible Uq(gln)-module
V(λ ) labelled by the dominant weight
(λ↑
1−λ↓
n)ε1 + (λ↑
2−λ↓
n−1)ε2 +··· + (λ↑
n−λ↓
1)εn, (5.15)
using standard conventions for the root system of gln.
Proof. We proceed by induction onr+s, the case r+s = 0 being trivial. Since eλ↑ is the
Young symmetrizer, the image of Ψ( eλ↑)∈ EndUq(gln) ((V +)⊗r) is the irreducible poly-
nomial representation V(λ↑) of Uq(gln) of highest weight λ↑
1ε1 +··· +λ↑
nεn. Similarly,
the image of Ψ( eλ↓ ) is the dual irreducible polynomial representation V( λ↓)∗ of highest
weight−λ↓
nε1 +··· +λ↓
1εn. Hence, the image of Ψ( ır,s(eλ↑⊗eλ↓ )) is V(λ↓)∗⊗ V(λ↑).
Using characters, it is easy to see that this tensor product has a u nique irreducible
constituent V( λ ) of highest weight (5.15), plus a sum of irreducible modules V( µ ) for
bipartitions µ ∈ ∐
d>0 Bipr−d,s−d with h(µ )≤ n. Now using induction, we deduce
that Ψ( eλ ) must be the projection onto V( λ ). □
Remark 5.15. A helpful picture of the weight (5.15) is displayed in [Ko, Figure 2].
It is also worth noting that multiplicities M λ
µ appearing in (5.13) are the same as the
Uq(gln)-composition multiplicities [V(λ↓)∗⊗ V(λ↑) : V( µ )] computed in [Ko, Corollary
2.3.1]. Given this, the same induction as used to prove Lemma 5.14 can b e used to
ORIENTED SKEIN CATEGORY 35
show that ∆( λ ) = P( λ ) when in the situation of the lemma. We will prove this in a
diﬀerent way in Corollary 6.13 below.
Remark 5.16. To get the appropriate analog of Lemma 5.14 when n≤ 0, one just
needs to twist by the isomorphism #. Recalling at the level of the Heck e algebra that
this is “tensoring with sign,” one can show that # maps the primitive idem potenteλ to
a conjugate of eλ t, where λt :=
(
(λ↑)t, (λ↓)t)
. So, for negative n, the Uq(gln)-module
V (λ ) arises as the image of Ψ( eλ t) (instead of Ψ( eλ )).
The ﬁnal result in the section justiﬁes the description of K0( ˙OS (z,t )) made after
Theorem 1.7 in the introduction; the discussion there also depends o n Theorem 1.6
which will be proved in the next section, and the highest weight/stan dardly stratiﬁed
structure which will be explained in section 7.
Lemma 5.17. For λ∈e-Bipr,s and ν∈ Bipr−d,s−d, we have that
∑
µ∈Bipr,s
[S(µ ) : D( λ )]M µ
ν =
∑
µ∈e-Bipr−d,s−d
M λ
µ (e,p )[S(ν ) : D( µ )].
Proof. We have that
∑
µ∈e-Bipr−d,s−d
M λ
µ (e,p )[S(ν ) : D( µ )]
=
∑
µ∈e-Bipr−d,s−d
κ∈e-Bipd,d,γ⊢d
[
Dµ↑◦ Dκ↑ : Dλ↑
][
Sν↑ : Dµ↑
][
Sγ : Dκ↑
]
×[
Dµ↓◦ Dκ↓ : Dλ↓
][
Sν↓ : Dµ↓
][
Sγ : Dκ↓
]
=
∑
κ∈e-Bipd,d,γ⊢d
[
Sν↑◦ Dκ↑ : Dλ↑
][
Sγ : Dκ↑
][
Sν↓◦ Dκ↓ : Dλ↓
][
Sγ : Dκ↓
]
=
∑
γ⊢d
[
Sν↑◦ Sγ : Dλ↑
][
Sν↓◦ Sγ : Dλ↓
]
=
∑
µ∈Bipr,s,γ⊢d
[
Sν↑◦ Sγ : Sµ↑
][
Sµ↑ : Dλ↑ ]
[
Sν↓◦ Sγ : Sµ↓
][
Sµ↓ : Dλ↓ ]
=
∑
µ∈Bipr,s
[S(µ ) : D( λ )]M µ
ν .
□
Theorem 5.18. For any choices of q and t, the ring K0(pMod-OS) may be identiﬁed
with a subring of Sym⊗Z Sym so that (1.14) and (1.15) hold.
Proof. When e = 0, Lemma 5.2 and the well-known representation theory of Hecke
algebras imply that the rings K0(pMod-OS◦) and Sym ⊗Z Sym may be identiﬁed so
that [S( λ )]↔ χλ↑⊗χλ↓. For general e, using also Brauer reciprocity for the Hecke
algebra, we may identify K0(pMod-OS◦) with a subring of Sym ⊗Z Sym so that
[Y(λ )]↔
∑
µ∈Bipr,s
[S(µ ) : D( λ )]χµ↑⊗χµ↓
for λ∈e-Bipr,s and r,s≥ 0. In view of Theorem 1.7 (and its proof), we deduce that
K0(pMod-OS) is identiﬁed with a subring of Sym ⊗Z Sym so that
[Q(λ )]↔
∑
µ∈Bipr,s
[S(µ ) : D( λ )]χµ↑⊗χµ↓
36 J. BRUNDAN
for λ∈e-Bipr,s and r,s≥ 0. Now recall the deﬁnition (1.9) and (5.13). Setting N λ
µ =
M λ
µ := 0 whenever λ∈ Bipr,s and µ /∈∐ min(r,s)
d=0 Bipr−d,s−d, the matrix ( N λ
µ )λ,µ∈Bip
is inverse to the matrix ( M λ
µ )λ,µ∈Bip by [Ko, Theorem 2.3]. So
[Q(λ )]↔
∑
µ∈Bipr,s
0≤d≤min(r,s)
ν∈Bipr−d,s−d
[S(µ ) : D( λ )]M µ
ν χν
for λ∈e-Bipr,s and r,s≥ 0. By Lemma 5.17, this gives
[Q(λ )]↔
∑
0≤d≤min(r,s)
λ∈e-Bipr−d,s−d
ν∈Bipr−d,s−d
M λ
µ (e,p )[S(ν ) : D( µ )]χν.
Now use Corollary 5.12 to identify K0(pMod-OS) = K0(∆Mod- OS). Comparing with
(5.12), we deduce that
[∆( λ )]↔
∑
ν∈Bipr,s
[S(ν ) : D( λ )]χν
for λ∈e-Bipr,s. This establishes (1.14). To get (1.15) too, use Corollary 5.11. □
