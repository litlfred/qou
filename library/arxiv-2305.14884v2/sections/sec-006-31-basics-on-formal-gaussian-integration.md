---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-006-31-basics-on-formal-gaussian-integration
section_title: "Basics on formal Gaussian integration"
section_number: 3.1
pages: 9-18
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further"
---
erties of formal Gaussian integration, which is a combinatorial analo gue of integration of
analytic functions. This theory was introduced and studied in detail in [ 4], where it was
used to deﬁne a universal perturbative ﬁnite type invariant of rat ional homology 3-spheres,
and to identify it with the trivial connection contribution of Chern–S imons perturbation
theory.
As a warm-up, the formal Gaussian integral of a monomial xn in one variable with respect
to the quadratic form λ ⁄= 0 is deﬁned by
⟨xn⟩x,λ =
{
λ−n/2(n − 1)!! n even
0 n odd. (20)
When λ> 0, then the above bracket equals to a normalized Gaussian integral
⟨xn⟩x,λ =
∫
/CA
e− 1
2λx2
xndx∫
/CA
e− 1
2λx2
dx
, (21)
explaining the naming of formal Gaussian integration. The formal Ga ussian integration can
be extended by linearity to ⟨f (x)⟩x,λ for any polynomial f (x), or even further to a power
series f (x) = ∑
n≥0anxn whose coeﬃcients tend to zero in a local ring (such as the ring
/C9 /llbracketℏ
1
2 /rrbracket).
The formal Gaussian integral ( 20) has a multivariable extension given in Equation ( 5)
wherex is a vector of variables and Λ is an invertible matrix over a ﬁeld matching the size of
x. Throughout this paper, the entries of Λ are elements of the ﬁeld /C9 (z) wherez is a vector of
variables, the integrable functionsfℏ(x,z ) that we apply the formal Gaussian integration with
respect to x with be elements of /C9 (z)[x]/llbracketℏ
1
2 /rrbracket, and the result of formal Gaussian integration
10 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
will be an element of the ring /C9 (z)/llbracketℏ/rrbracketor /C9 (z)[x]/llbracketℏ
1
2 /rrbracket. When we specialize to the case of a
vector of algebraic numbers z, then /C9 (z) deﬁnes the corresponding number ﬁeld.
Just like integration of suﬃciently smooth functions satisﬁes certa in invariance properties
(such as change of variables, iterated integration, and even integ ration by parts [ 4]), so does
formal Gaussian integration. The corresponding identities of form al Gaussian integration
are combinatorial statements about polynomials or rational funct ions and often follow from
the corresponding statements of integration of functions.
We now give some elementary properties of formal Gaussian integra tion that we will use
in our paper.
Lemma 3.1. (a) For all invertible matrices Λ and P over
/C9 (z), we have
⟨fℏ(Px,z )⟩x,P tΛP = ⟨fℏ(x,z )⟩x,Λ . (22)
(b) For all invertible matrices Λ and vectors G over /C9 (z), we have
⟨exp(−GtΛxℏ
1
2 )fℏ(x +Gℏ
1
2,z )⟩x,Λ = exp
(GtΛG
2 ℏ
)
⟨fℏ(x,z )⟩x,Λ (23)
(c) If Λ =
(A B
Bt C
)
, and Λ and A invertible, then for any F , we have
⟨
exp(Fx ′ℏ
1
2 )fℏ(x′′,z )
⟩
x,Λ
= exp
(FA −1Ft
2 ℏ
) ⟨
exp(−FA −1Bx′′ℏ
1
2 )fℏ(x′′,z )
⟩
x′′,C−BtA−1B
.
(24)
Proof. Part (a) follows from the fact the integration is unchanged under a linear change of
variables.
Part (b) follows from the fact the integration is unchanged under a n aﬃne change of
variables.
Part (c) follows from Fubini’s theorem [ 4, Prop.2.13], combined with Equation ( 23). □
The next lemma, which will be important in the application of q-holonomic methods in
Section 3.2 and in the proofs of Theorems 3.4 and 3.6 below, concerns the behavior of formal
Gaussian integration whenz = (z1,...,z r) is shifted to eεℏz := (eε1ℏz1,...,e εrℏzr) for integers
εj.
Lemma 3.2. For all invertible matrices Λ( z) over /C9 (z) and all integrable functions fℏ, we
have
⟨fℏ(x,z )⟩x,Λ(z)|z↦→eεℏz =
√
det Λ(eεℏz)
det Λ(z)
⟨
exp
(xt(
Λ(z) − Λ(eεℏz)
)
x
2
)
fℏ(x,eεℏz)
⟩
x,Λ(z)
.
(25)
Proof. The lemma follows from recentering the Gaussian after multiplying z byeεℏ. □
3.2. q–holonomic aspects of ψℏ. It is well-known that identities of holonomic functions
can be proven algorithmically [ 36, 31]. We will use these ideas, adapted to our needs,
to prove fundamental identities between certain Gaussian integra ls involving the building
block exp(ψℏ) of our series Φ Ξ (ℏ). Since ψℏ is related to the inﬁnite Pochhammer symbol
given in Equation ( 2), its functional equations will be of fundamental importance. Fro m its
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 11
deﬁnition, it is clear that the inﬁnite Pochhammer symbol satisﬁes a s imple ﬁrst order linear
q–diﬀerence equation
(x;q)∞ = (1 −x)(qx;q)∞. (26)
To convert this into an identity of formal ℏ-series where q =eℏ, we use the fact that there is
an action of the quantum plane (also known as q–Weyl [14, Ex. 1.7] algebra) on the space
/C9 (z)[x]/llbracketℏ
1
2 /rrbracketof integrable functions by an action on the z-variable given by
(Lfℏ)(x,z ) = fℏ(x,e ℏz), (Mf ℏ)(x,z ) = eℏfℏ(x,e ℏz) (27)
where LM =qML . The next lemma asserts that the completion ˆψℏ(x,z )
ˆψℏ(x,z ) : = exp
(
− Li2(z)
ℏ − Li1(z)x
ℏ
1
2
+ 1
2 Li1(z) − Li0(z)x2
2
)
ψℏ(x,z )
= exp
(
−
∑
k,ℓ∈/CI
≥0
Bkxℓ ℏk+ ℓ
2 −1
ℓ!k! Li2−k−ℓ(z)
)
∈ exp
(
− Li2(z)
ℏ − Li1(z)x
ℏ
1
2
+ 1
2 Li1(z) − Li0(z)x2
2
)
(1 + ℏ
1
2
/C9 (z)[x]/llbracketℏ
1
2 /rrbracket)
(28)
of ψℏ(x,z ), as well as ψℏ(x,z ) itself, satisfy a corresponding ﬁrst order linear q–diﬀerence
equation, albeit with complicated coeﬃcients.
Lemma 3.3. (a) We have:
ˆψℏ(x,e ℏz) = (1 −zexℏ1/2
)ˆψℏ(x,z ). (29)
(b) We have:
ψℏ(x,e ℏz) = (1 −zexℏ1/2
)ψℏ(x,z )
√
1 −eℏz
1 −z
× exp
(Li2(eℏz)
ℏ − Li2(z)
ℏ + Li1(eℏz)x
ℏ
1
2
− Li1(z)x
ℏ
1
2
+ 1
2 Li0(eℏz)x2 − 1
2 Li0(z)x2
)
.
(30)
Note that the identity ( 29) takes place in a larger ring, which includes the symbols
exp( Li2(z)
ℏ ), exp( Li1(z)x
ℏ
1
2
), exp( Li0(z)x2
2 ) and exp( Li0(z)x2
2 ) which one can adjoin in the diﬀerential
ﬁeld /C9 (z)((ℏ)) as is standard in diﬀerential Galois theory of linear diﬀerential equ ations [35].
The symbols Li k(z) for k = 0, 1, 2 can be interpreted as normalized solutions to the linear
diﬀerential equations z d
dz Lik(z) = Li k−1(z) with Li 0(z) = z/(1 −z) and satisfy the usual
properties Lik(eℏz) =∑ ∞
r=0
1
r! Lik−r(z)ℏr. On the other hand, the coeﬃcients in identity ( 30)
are elements of the ring /C9 (z)[x]/llbracketℏ
1
2 /rrbracket.
Proof. Part (a) can be proved directly using the facts that for the Berno ulli polynomials
Br(x) we have Br(1) = Br +δr,1 andBr(x) =∑ r
k=0
(r
k
)
Bn−kxk. Applying these identities we
12 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
ﬁnd that
exp
(
−
∑
k,ℓ∈/CI
≥0
Bkxℓℏk+ ℓ
2 −1
ℓ!k! Li2−k−ℓ(zeℏ)
)
= exp
(
−
∑
r,ℓ∈/CI
≥0
r∑
k=0
Bk
(r
k
) xℓℏr+ ℓ
2 −1
ℓ!r! Li2−r−ℓ(z)
)
= exp
(
−
∑
r,ℓ∈/CI
≥0
Br(1)xℓℏr+ ℓ
2 −1
ℓ!r! Li2−r−ℓ(z)
)
= exp
(
− Li1(zexℏ1/2
) −
∑
r,ℓ∈/CI
≥0
Brxℓℏr+ ℓ
2 −1
ℓ!r! Li2−r−ℓ(z)
)
= (1 −zexℏ1/2
) exp
(
−
∑
r,ℓ∈/CI
≥0
Brxℓℏr+ ℓ
2 −1
ℓ!r! Li2−r−ℓ(z)
)
.
(31)
Part (b) follows from (a), using Equation ( 28) and expanding in ℏ to ﬁnd that
√
1 −eℏz
1 −z exp
( Li2(eℏz)
ℏ − Li2(z)
ℏ + Li1(eℏz)x
ℏ
1
2
− Li1(z)x
ℏ
1
2
+ 1
2 Li0(eℏz)x2 − 1
2 Li0(z)x2
)
∈ /C9 (z)[x]/llbracketℏ
1
2 /rrbracket. (32)
□
We end this section by discussing a useful relation between ψℏ(x,z ) and its specialization
at x = 0. It is easy to see that the completion ˆψℏ(x,z ) of ψℏ(x,z ) is regular at x = 0 and
satisﬁes
ˆψℏ(x,z ) = ˆψℏ(0,zexℏ1/2
). (33)
This implies a corresponding statement
ψℏ(x,z ) = ψℏ
(
0,zexℏ1/2)
Cℏ(x,z ), (34)
for ψℏ where
Cℏ(x,z ) = exp
(
−
∑
ℓ≥3
ℏ
ℓ
2 −1
ℓ! Li2−ℓ(z)xℓ + 1
2
∑
ℓ≥1
h
ℓ
2
ℓ! Li1−ℓ(z)xℓ
)
= exp
(
− Li2(zexℏ
1
2
)
ℏ + Li2(z)
ℏ − log(1 −z)
ℏ
1
2
x + z
1 −z
x2
2
− 1
2(log(1 −zezℏ
1
2
) − log(1 −z))
)
.
(35)
3.3. Fourier transform of ψℏ. In this section, we prove two functional identities for
ψℏ(•,z ), ψℏ(•,z ′) and ψℏ(•,z ′′) where z′ := 1/(1 −z) and z′′ := 1 − 1/z are related to
the /CI /3 /CI -symmetry of the shapes of a tetrahedron, and reﬂect the /CI /3 /CI -symmetry of the
dilogarithm function.
The next theorem is a formal Gaussian integration version of the Fo urier transform of the
Faddeev quantum dilogarithm given in Equation ( 9). The proof, however, does not follow
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 13
from the distributional identity ( 9), and instead uses q–holonomic ideas and the basics of
formal Gaussian integration.
This theorem and its Corollary 3.5 are used in Section 5 to show that the power series
Φ Ξ (ℏ) are independent of the choice of a nondegenerate quad.
Theorem 3.4. We have:
ψℏ(x,z ) = e− ℏ
24
⟨
exp
((
y + xz
1 −z
) ℏ
1
2
2
)
ψℏ
(
y + xz
1 −z, 1
1 −z
)⟩
y,1−z−1
(36)
in the ring /C9 (z)[x]/llbracketℏ
1
2 /rrbracket.
In fact, both sides of of Equation ( 36) lie in the subring /C9 [z±, (1 −z)−1][x]/llbracketℏ
1
2 /rrbracket.
Proof. It it clear from the deﬁnition that both sides of Equation ( 36) are elements of the
ring /C9 (x)[z]/llbracketℏ/rrbracket. First, we will prove the specialization of Equation ( 36) when x = 0, i.e., we
will show that
ψℏ(0,z ) = e− ℏ
24
⟨
exp
(y
2 ℏ
1
2
)
ψℏ
(
y, 1
1 −z
)⟩
y,1−z−1
∈ /C9 (z)[[ℏ]]. (37)
To prove this, we will combine q-holonomic ideas with formal Gaussian integration. From
Equation ( 29), we see that the left hand side of Equation ( 37) multiplied by exp(− Li2(z)ℏ−1)√1−z
satisﬁes a simple ﬁrst order q–diﬀerence equation. We want to show the same for the right
hand side. To do this, consider the function
Im,ℏ(w,z ) = wme− ℏ
24 + π2
6ℏ exp
(
log(w)
(
− log(w)
2ℏ + πi
ℏ − log(z)
ℏ + 1
2
))
ˆψℏ(0,w ) (38)
which is an element of a larger ring discussed in relation to ˆψℏ of Equation ( 28). Using
Equation ( 34) and the symmetry
Li2(z) = Li 2
( 1
1 −z
)
− 1
2 log(1 −z)2 +πi log(1 −z) − log(z) log(1 −z) −π2
6 (39)
of the dilogarithm [ 39], it is easy to see that the right hand side of Equation ( 37) is given by
⟨ √
−z exp
(Li2(z)
ℏ + (1 −z−1)w2
2
)
I0,ℏ
( 1
1 −zewℏ1/2
,z
)⟩
w,1−z−1
. (40)
The function Im,ℏ satisﬁes the linear q–diﬀerence equations
Im,ℏ(eℏw,z ) = −emℏw−1z−1(1 −w)Im,ℏ(w,z ),
Im,ℏ(w,e ℏz) = w−1Im,ℏ(w,z ),
Im,ℏ(w,z ) = wIm,ℏ(w,z ),
(41)
which imply that
(1 −e−mℏz)Im,ℏ
( 1
1 −zewℏ1/2+ℏ,z
)
= Im
( 1
1 −zewℏ1/2
,e ℏz
)
. (42)
If we multiply both sides of ( 42) with the factors from Equation ( 40) and take the bracket of
both sides and apply Lemma 3.1 and Lemma 3.2 to change coordinates and the Gaussian, we
ﬁnd that when m = 0 both sides of Equation ( 37) satisfy the same q–diﬀerence equation ( 29).
14 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
Moreover, it is easy to see that both sides of Equation ( 40) are power series in ℏ with
coeﬃcients rational functions of z of nonpositive degree, thus we can work with the ring
/C9 /llbracketz−1/rrbracket/llbracketℏ/rrbracketinstead. In this case, the Newton polygon of this ﬁrst order linear q-diﬀerence
equation implies that it has a unique solution in /C9 /llbracketz−1/rrbracket/llbracketℏ/rrbracketdetermined by its value at z = ∞.
Therefore, the identity in Equation ( 37) follows from its specialization at z = ∞. Since
ψℏ(0, ∞) = exp
( ℏ
12
)
,
e
−ℏ
24
⟨
exp
(w
2 ℏ
1
2
)
ψℏ (w, 0)
⟩
w,1
= e
−ℏ
24
⟨
exp
(w
2 ℏ
1
2
)⟩
w,1
= exp
( ℏ
12
)
,
(43)
this completes the proof of Equation ( 37).
Going back to the general case of z, Equation ( 36) follows from Equation ( 34) together
with ( 37) using Lemma 3.2 to shift the Gaussian and Lemma 3.1 to change integration
variable via the transformation
w ↦→w − 1
ℏ
1
2
log
( 1 −z
1 −zexℏ1/2
)
− x
1 −z−1 . (44)
The detailed calculation is given in Appendix A. □
Theorem 3.4 implies the following identity relating ψℏ(•,z ) and ψℏ(•,z ′′).
Corollary 3.5. We have:
ψℏ(x,z ) = e
ℏ
24
⟨
exp
(
− x
2 ℏ
1
2
)
ψℏ
(
y − x
1 −z, 1 −z−1
)⟩
y,z−1
(45)
in the ring /C9 (z)[x]/llbracketℏ
1
2 /rrbracket.
Proof. Apply Equation ( 36) to the ψℏ that appears on the right hand side of the same
Equation ( 36). Then apply a change of variables and Fubini’s theorem of Lemma 3.1 to
calculate the bracket for the variable that doesn’t appear in the ar gument of the remaining
ψℏ. □
3.4. Pentagon identity for ψℏ. In this section, we prove a pentagon identity for the func-
tions ψℏ(•,z ) where z takes the ﬁve values
[z1] + [z2] ↦→[z1z−1
0 ] + [z0] + [z2z−1
0 ], z 0 = z1 +z2 −z1z2 (46)
what appear in the 5-term relation for the dilogarithm. The next the orem is a formal Gauss-
ian integration version of the pentagon identity ( 8) of the Faddeev quantum dilogarithm and
will be used in Section 6 to prove that the series Φ Ξ (ℏ) is independent of 2–3 Pachner moves.
Let us denote
δ = 2 + Li 0(z1z−1
0 ) + Li0(z0) + Li0(z2z−1
0 ) = (z1 +z2 −z1z2)2
z1z2(1 −z1)(1 −z2). (47)
Theorem 3.6. We have:
ψℏ(x,z 1)ψℏ(y,z 2) = e− ℏ
24
⟨
ψℏ
(
−w −y + xz2 +yz1
z0
,z 1z−1
0
)
ψℏ
(
w +x +y −xz2 +yz1
z0
,z 0
)
ψℏ
(
−w −x + xz2 +yz1
z0
,z 2z−1
0
)⟩
w,δ
(48)
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 15
in the ring /C9 (z1,z 2)[x,y ]/llbracketℏ
1
2 /rrbracket.
Proof. It is clear from the deﬁnition that both sides of Equation ( 48) are elements of the ring
/C9 (z1,z 2)[x,y ]/llbracketℏ
1
2 /rrbracket. To prove this, we follow the same approach we used to prove Theor em 3.4.
First, we prove the identity ( 48) when u =v = 0, i.e., we will show that
ψℏ(0,z 1)ψℏ(0,z 2) = e− ℏ
24
⟨
ψℏ(−w,z 1z−1
0 )ψℏ(w,z 0)ψℏ(−w,z 2z−1
0 )
⟩
w,δ (49)
in the ring /C9 (z1,z 2)/llbracketℏ/rrbracketand to prove this we will again use q–holonomic methods. To do so,
consider the function
Im,ℏ(z1,z 2,z ) = e
π2
6ℏ − ℏ
24zmˆψℏ(0,z 1z−1)ˆψℏ(0,z )ˆψℏ(0,z 2z−1)
× exp
(
− log(z1) log(z2)
ℏ + log(z) log(z1)
ℏ + log(z) log(z2)
ℏ − log(z)2
ℏ
)
,
(50)
which is again an element of a larger ring discussed in relation to ˆψℏ of Equation ( 28). Using
Equation ( 34) and the ﬁve term relation for the dilogarithm [ 39], it is easy to see that the
right hand side of Equation ( 49) is given by
⟨ √z1z2(1 −z1)(1 −z2)
z1 +z2 −z1z2
exp
(Li2(z1)
ℏ + Li2(z2)
ℏ + δ
2z2
)
I0,ℏ(z1,z 2,z 0ewℏ1/2
)
⟩
w,δ
. (51)
The function Im,ℏ satisﬁes the system of linear q–diﬀerence equations
Im,ℏ(eℏz1,z 2,z ) = zz −1
2 (1 −z1z−1)Im,ℏ(z1,z 2,z ),
Im,ℏ(z1,e ℏz2,z ) = zz −1
1 (1 −z2z−1)Im,ℏ(z1,z 2,z ),
Im,ℏ(z1,z 2,e ℏz) = (1 −z)z1z2z−2e(m−1)ℏIm,ℏ(z1,z 2,z ),
Im+1,ℏ(z1,z 2,z ) = zIm,ℏ(z1,z 2,z ),
(52)
which can be derived from Equation ( 29). In fact, the function Im,ℏ is holonomic of rank 1,
a fact that we will not use explicitly [ 31]. Therefore, we see that
Im,ℏ (eℏz1,z 2,z ) = z−1
2 Im+1,ℏ (z1,z 2,z ) −z1z−1
2 Im,ℏ (z1,z 2,z ),
Im,ℏ (eℏz1,z 2, (eℏz1 +z2 −eℏz1z2)ewℏ 1/ 2
)
= z−1
2 Im+1,ℏ (z1,z 2, (eℏz1 +z2 −eℏz1z2)ewℏ 1/ 2
) −z1z−1
2 Im,ℏ (z1,z 2, (eℏz1 +z2 −eℏz1z2)ewℏ 1/ 2
),
Im,ℏ (z1,z 2, (z1 +z2 −z1z2)ezℏ 1/ 2+ℏ )
= z1z2e(m−1)ℏIm−2,ℏ (z1,z 2, (z1 +z2 −z1z2)ezℏ 1/ 2
) −z1z2e(m−1)ℏIm−1,ℏ (z1,z 2, (z1 +z2 −z1z2)ezℏ 1/ 2
).
(53)
Let us deﬁne ˆJm,ℏ and Jm,ℏ by the equation
ˆJm,ℏ(z1,z 2) = 1√
(1 −z1)(1 −z2)
exp
(
− Li2(z1)
ℏ − Li2(z2)
ℏ
)
Jm,ℏ(z1,z 2)
=
⟨√
z1z2(1 −z1)(1 −z2)
z1 +z2 −z1z2
exp
(δ
2z2
)
Im,ℏ(z1,z 2,z 0ewℏ1/2
)
⟩
w,δ
.
(54)
If we multiply both sides of the Equations ( 53) with the factors from Equation ( 51), take
the bracket of both sides, and apply Lemma 3.2 to change coordinates and the Gaussian, we
16 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
ﬁnd that ˆJℏ,m(z1,z 2) satisﬁes the q–diﬀerence equations
ˆJm,ℏ(eℏz1,z 2) = z−1
2 ˆJm+1,ℏ(z1,z 2) −z1z−1
2 ˆJm,ℏ(z1,z 2),
ˆJm,ℏ(z1,e ℏz2) = z−1
1 ˆJm+1,ℏ(z1,z 2) −z−1
1 z2ˆJm,ℏ(z1,z 2),
ˆJm,ℏ(z1,z 2) = z1z2e(m−1)ℏˆJm−2,ℏ(z1,z 2) −z1z2e(m−1)ℏˆJm−1,ℏ(z1,z 2).
(55)
From these relations we can derive the equations
0 = ( z1 −z1e(m+1)ℏ +z2
1e(m+1)ℏ −z1)ˆJm,ℏ(z1,z 2)
+ (z1z2e(m+1)ℏ −z2 +qz1)ˆJm,ℏ(eℏz1,z 2) +z2ˆJm,ℏ(e2ℏz1,z 2),
0 = ( z2 −z2e(m+1)ℏ +z2
2e(m+1)ℏ −z2)ˆJm,ℏ(z1,z 2)
+ (z2z1e(m+1)ℏ −z1 +qz2)ˆJm,ℏ(z1,e ℏz2) +z1ˆJm,ℏ(z1,e 2ℏz2).
(56)
These q–diﬀerence equations give rise to equations for Jm,ℏ given by
0 = ( z1 −z1eℏ +z2
1eℏ −z1)Jm,ℏ(z1,z 2)
+ (z1z2eℏ −z2 +qz1)
√
1 −z1
1 −eℏz1
exp
(Li2(z1) − Li2(eℏz1)
ℏ
)
Jm,ℏ(eℏz1,z 2)
+z2
√
1 −z1
1 −e2ℏz1
exp
(Li2(z1) − Li2(e2ℏz1)
ℏ
)
Jm,ℏ(e2ℏz1,z 2),
0 = ( z2 −z2eℏ +z2
2eℏ −z2)Jm,ℏ(z1,z 2)
+ (z2z1eℏ −z1 +qz2)
√
1 −z2
1 −eℏz2
exp
(Li2(z2) − Li2(eℏz2)
ℏ
)
Jm,ℏ(z1,e ℏz2)
+z1
√
1 −z2
1 −e2ℏz2
exp
(Li2(z2) − Li2(e2ℏz2)
ℏ
)
Jm,ℏ(z1,e 2ℏz2).
(57)
These equations are also satisﬁed by the left hand side of Equation ( 49), which follows from
repeated application of Equation ( 30).
It is easy to see that both sides of Equation ( 49) are formal power series in ℏ with co-
eﬃcients rational functions of ( z1,z 2) of nonpositive degree with respect to both z1 and
z2, thus their coeﬃcients embed in /C9 /llbracketz−1
1 ,z −1
2 /rrbracket, and it suﬃces to prove ( 49) in the ring
/C9 /llbracketz−1
1 ,z −1
2 /rrbracket/llbracketℏ/rrbracket. In this case, we consider the linear q-diﬀerence equations ( 57) over the ring
/C9 /llbracketz−1
1 ,z −1
2 /rrbracket/llbracketℏ/rrbracket. Looking at the corresponding Newton polytopes, the leading mono mials
that appear as coeﬃcients of this q–diﬀerence equation ( 57) at ∞ are z2
1(1 + O(z−1
1 )O(z0
2))
and z2
1z2(1 + O(z−1
1 )O(z0
2)) for the ﬁrst equation, and z2
2(1 + O(z0
1)O(z−1
2 )) and z1z2
2(1 +
O(z0
1)O(z−1
2 )) for the second equation, respectively. The structure of thes e monomials
and their Newton polytopes shows that there is a unique solution to t hese equations in
/C9 /llbracketz−1
1 ,z −1
2 /rrbracket/llbracketℏ/rrbracketdetermined by the value at z1 = z2 = ∞. Therefore, the identity in Equa-
tion ( 49) reduces to its specialization at z1 =z2 = ∞. Since
ψℏ(0, ∞)ψℏ(0, ∞) = e
ℏ
6 and
e− ℏ
24
⟨
ψℏ(−w, 0)2ψℏ(w, ∞)
⟩
w,δ = e− ℏ
24
⟨
exp
( ℏ
12 − zℏ
1
2
2
)⟩
w,δ
= e
ℏ
6,
(58)
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 17
this completes the proof of Equation ( 49).
Going back to the general case of x,y , Equation ( 48) follows from Equation ( 34) together
with ( 49) using Lemma 3.2 to shift the Gaussian and with a change of integration variable
w ↦→w + 1
ℏ
1
2
log
( z1 +z2 −z1z2
z1ex1ℏ1/2
+z2ex2ℏ1/2
−z1z2e(x1+x2)ℏ1/2
)
+x +y − xz1 +yz2
z0
. (59)
The detailed calculation is given in Appendix B. □
3.5. Inversion formula for ψℏ. In this section, we give an inversion formula for ψℏ analo-
gous to the inversion formula ( 11) for the Faddeev quantum dilogarithm. Although we will
not use this formula explicitly in our paper, we include it for completene ss.
Lemma 3.7. We have:
ψℏ(x,z ) 1 −z−1e−xℏ1/2
1 −z−1 ψℏ(−x, 1/z) = exp
(
−xℏ
1
2
2 + ℏ
12
)
, (60)
ˆψℏ(0,z )ˆψℏ(0, 1/z) =
√−z
1 −z exp
(π2
6ℏ + 1
2ℏ log(−z)2 + ℏ
12
)
. (61)
Proof. These formulas all follow from the well-known inversion formulas for t he polyloga-
rithms (see for example [ 30]):
Li2(z) + Li2(1/z) = −π2
6 − 1
2 log(−z)2,
Li1(z) − Li1(1/z) = − log(−z),
Li0(z) + Li0(1/z) = −1,
Li−n(z) + (−1)n Li−n(1/z) = 0 ( n> 0).
(62)
Using these relations, we have
ˆψℏ(0,z )ˆψℏ(0, 1/z) = exp
(
−
∑
k∈/CI
≥0
Bk ℏk−1
k! (Li2−k(z) + Li2−k(1/z))
)
=
√−z
1 −z exp
(π2
6ℏ + 1
2ℏ log(−z)2 + ℏ
12
)
.
(63)
Similarly, we ﬁnd that
ψℏ(x,z ) 1 −z−1e−xℏ1/2
1 −z−1 ψℏ(−x, 1/z)
= exp
(
−
∑
k,ℓ∈/CI
≥0
k+ ℓ
2 >1
Bkxℓ ℏk+ ℓ
2 −1
ℓ!k!
(
Li2−k−ℓ(z) + (−1)k+ℓ Li2−k−ℓ(1/z)
) )
= exp
(
− xℏ
1
2
2 + ℏ
12
)
.
(64)
Notice that this is exactly the factor that appeared in the remark a fter Equation ( 1), which
gave the relation between the ψℏ used in the current paper and the ones used in [ 11,
18 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
Eq. 1.9]. Indeed, 1−z−1
1−z−1e−xℏ 1/2ψℏ(−x, 1/z)−1 is exactly the series used in [ 11] where the factor
1−z−1
1−z−1e−xℏ 1/2 amounts to swapping the sign of B1 as done there. □
