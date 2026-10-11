---
doc_id: arxiv-2208.05331v6
doc_title: "PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES"
section_id: sec-004-5-the-casimir-connection
section_title: "The Casimir connection"
section_number: 5
pages: 14-18
source_pdf: 2208.05331v6.pdf
source_sha256: 54b4a400388dbf41
toc_source: outline
---
5.1. Fundamental group of root system arrangements. Let A be a sym-
metrisable generalised Cartan matrix, (hR, Π, Π∨) a realisation of A over R, and
(h = C ⊗R hR, Π, Π∨) its complexiﬁcation. Let Π⊥⊂h be the annihilator of Π, set
he = h/Π⊥, and note that he is independent of the realisation of A. Let
C = {h ∈he
R | ∀i ∈I, αi(h) > 0}
be the fundamental Weyl chamber in he
R, and YR = S
w∈W w(C) the Tits cone.
YR is a convex cone, and the Weyl group W acts properly discontinuously on its
interior ˚YR and complexiﬁcation Y = ˚YR + ιhe
R ⊆he [Loo80, Vin71]. The regular
points of this action are given by
X = Y \
[
α∈∆+
Ker(α)
The action of W on X is proper and free, and the space X/W is a complex manifold.
The following result is due to van der Lek [vdL83], and generalises Brieskorn’s
Theorem [Bri71] to the case of an arbitrary Weyl group.
Theorem. The fundamental groups of X/W and X are isomorphic to BW and PW
respectively.
PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES
15
The generators {Si}i∈I of BW may be described as follows. Let p : X →X/W
be the canonical projection, ﬁx a point x0 ∈C and use [x0] = p(x0) as a base
point in X/W. For any i ∈I, choose an open disk Di in x0 + Chi, centered in
x0 −αi(x0)
2
hi, and such that Di does not intersect any root hyperplane other than
Ker(αi). Let γi : [0, 1] →x0 + Chi be the path from x0 to si(x0) in X determined
by γi|[0,1/3]∪[2/3,1] is aﬃne and lies in x0 + Rhi \ Di, the points γi(1/3), γi(2/3) are
in ∂Di, and γi|[1/3,2/3] is a semicircular arc in ∂Di, positively oriented with respect
to the natural orientation of x0 + Chi. Then, Si = p ◦γi.
5.2. The Casimir connection. For any positive root α ∈∆+, let {e(i)
±α}mα
i=1 be
bases of g±α which are dual with respect to ⟨·, ·⟩, and
K+
α =
mα
X
i=1
e(i)
−αe(i)
α
the corresponding truncated and normally ordered Casimir operator. Let V be a g–
module in category Oℏ
∞,g and V = X × V the holomorphically trivial vector bundle
over X with ﬁbre V . Finally, set h =
ℏ
2πι.
Deﬁnition. The Casimir connection of g is the connection on V given by
∇K = d −h
X
α∈∆+
dα
α · K+
α
Note that the sum converges in the ℏ–adic topology since, for any v ∈V and n ≥0,
K+
α v ∈ℏnV for all but ﬁnitely many α ∈∆+.
The Casimir connection for a semisimple Lie algebra was discovered by De
Concini around ’95 (unpublished, though the connection is referenced in [Pro96])
and, independently, Millson–Toledano Laredo [TL02, MTL05] and Felder–Markov–
Tarasov–Varchenko [FMTV00]. In [FMTV00], the case of an arbitrary symmetris-
able Kac–Moody algebra is considered.
The connection ∇K is ﬂat (see [FMTV00] and [ATL15, Thm. 3.4]) and therefore
yields a monodromy representation
P : PW = Π1(X; x0) →GL(V)
Moreover, since the coeﬃcients of ∇K have weight zero, the action of PW preserves
the generalised weight spaces of V.
This is more conveniently expressed in terms of completions. Let f : Oℏ
∞,g →
Vectℏbe the forgetful functor. Then, the monodromy of ∇K yields an action
P : PW = Π1(X; x0) →Aut(f)
5.3. The orbifold fundamental groupoid of X. Let Π1(X; Wx0) be the funda-
mental groupoid of X based at the W–orbit of x0. Then, Π1(X/W; [x0]) is equivalent
to the orbifold fundamental groupoid W ⋉Π1(X; Wx0), which is deﬁned as follows.
• Its set of objects is Wx0.
• A morphism between x, y ∈Wx0 is a pair (w, γ), where w ∈W and γ is a
path in X from x to w−1y.
• The composition of (w, γ) : x →y and (w′, γ′) : y →z is given by
(w′, γ′) ◦(w, γ) = (w′w, w−1(γ′) ◦γ) : x →z
16
A. APPEL AND V. TOLEDANO LAREDO
The projection functor
P : W ⋉Π1(X; Wx0) −→Π1(X/W; [x0])
(5.1)
given by P(wx0) = [x0] and P(w, γ) = [γ] is fully faithful since, for any given
x, y ∈Wx0, a loop [γ] ∈Π1(X/W; [x0]) lifts uniquely to a path γ : x →w−1y, for
a unique w ∈W. Any x ∈Wx0 therefore determines a right inverse Ex of P given
by Ex([x0]) = x and Ex([γ]) = (w, γ), where γ is the lift of [γ] through x, and w is
such that γ(1) = w−1x.
5.4. Obstruction to W–equivariance [ATL15, Sec. 4]. Extend the monodromy
of ∇K to Π1(X; Wx0), and lift it to a map P : Π1(X; Wx0) →Tg, where Tg is the
holonomy algebra of the root arrangement of g. The lack of W–equivariance of ∇K
can then be described by the 1–cocycle
A : W →Hom(Π1(X; Wx0), Tg)
deﬁned by Aw(γ) = P(γ)−1 · w−1P(wγ).
The following summarises the main properties of A .
Theorem.
(1) A is abelian, that is takes values in M = Hom(Π1(X; Wx0), exp(ℏh)).
(2) A is a coboundary, that is Aw = dBw = B · (w−1B)−1 for some B ∈M,
and any w ∈W.
(3) The cochain B can be normalised so that B(γi) = exp(ℏaitαi) for any given
choice of {ai}i∈I ⊂C, and is then unique.
Remark. (1) follows from the fact that w−1P(wγ) is the parallel transport of
w∗∇K = ∇K −haw
where
aw =
X
α∈∆+:
wα∈∆−
dα
α · tα
Since ∇K and the h–valued 1–form aw commute, Aw is the parallel transport of
d −haw, and in particular takes values in M.
5.5. Equivariant monodromy [ATL15, Sec. 4]. For any b ∈BW , let τ(b) ∈
Aut(fint) be its action by the triple exponentials (2.3), and eb ∈Π1(X; Wx0) the
unique lift of b through x0. The following is a direct consequence of Theorem 5.4
Theorem. There is a unique morphism B : Π1(X; Wx0) −→exp(ℏh) such that
(1) The assignment
Pτ,B : BW →Aut(f
int)
Pτ,B(b) = τ(b) · P(eb) · B(eb)
is a group homomorphism.
(2) For any i ∈I, B(γi) = exp(ℏtαi/4).
PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES
17
Remarks.
• The normalisation of B(γi) is chosen so that, if g = sl2 with simple root αi,
Pτ,B(Si) = esi · exp(ℏK+
αi/2) · exp(ℏtαi/4) = esi · exp(ℏKαi/4)
(5.2)
where Kαi = eifi + fiei is the truncated Casimir of sl2.
• We shall refer to Pτ,B as the monodromy action of BW . This is justiﬁed by
the fact that, when g is of ﬁnite or aﬃne type, B is the monodromy of the
connection d −hA, where A is a resummation of the formal abelian 1–form
bA = 1
2
X
α∈∆+
dα
α · mαtα
(cf. [ATL15, Prop. 4.9 and Appendix A]). Thus, in these cases, Pτ,B is the
monodromy of the pushdown of the connection ∇K −hA to the quotient X/W.
5.6. Monodromy action of the pure braid group on category O∞. Let
ε : P
ab
W →Aut(f
int)
ε(pα) = exp(ιπhα)
(5.3)
be the sign character (cf. 4.3), f : Oℏ
∞,g →Vectℏthe forgetful functor, and lift ε to
a morphism P ab
W →Aut(f) as in 4.4.
Proposition. The following holds.
(1) For any α ∈∆re
+, τ(pα) = ε(pα) and B(pα) = exp(ℏtα/2).
(2) The restriction of Pτ,B to PW lifts to an action
Pε,B : PW →Aut(f)
given by
Pε,B(p) = ε(p) · P(p) · B(p)
Proof. (1) For any i ∈I, τ(S2
i ) = es2
i = exp(ιπhi) so that, for any w ∈W such that
wαi > 0, τ(SwS2
i S−1
w ) = exp(ιπhwαi). Thus, τ(p) = ε(p) for any p ∈PW .
For the second identity, it is enough to verify the relation on the loops pwαi =
w(pαi) ∈Π1(X; wx0), where pαi = si(γi) ◦γi, for i ∈I, and w ∈W is such that
wαi > 0 (cf. Section 5.1). For w = id, one has
B(pαi) = B(si(γi))B(γi) = si(Asi(γi)−1B(γi))B(γi) = si(Asi(γi))−1
where the second equality follows from A = dB, and the third one from B(γi) ∈
exp(Cℏtαi). By Remark 5.4, Av is the parallel transport of the abelian connection
d −h
X
α∈∆+:
vα∈∆−
dα
α · tα
(5.4)
For v = si, this is d −hd log αi · tαi, so that Asi(γi) = exp(ℏtαi/2).
For w̸ = id, one has
B(w(pαi)) = w(Aw(pαi)−1B(pαi)) = w(Aw(pαi))−1 exp(ℏtwαi/2)
Note that dα/α has a non–zero residue on the hyperplane αi = 0 only if α = ±αi.
It follows from (5.4) for v = w, and wαi ∈∆+ that Aw(pαi) = 1, whence the result.
(2) follows from (1) and Theorem 5.5.
□
18
A. APPEL AND V. TOLEDANO LAREDO
