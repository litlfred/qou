---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-025-l-now-use-the-fact-that
section_title: "Now use the fact that"
section_number: L
pages: 37-39
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
AR ∋xR ↦→(ˆ1↼xR) ∈ ˆAL is a ∗-algebra isomorphism. Hence passing to the square roots we
obtain 1↼gR = ˆgL. All the remaining identities are simple consequences of th is. Q.e.d.
Proposition 4.14 LetA be a C ∗-WHA with dual ˆA and let h ∈A, ˆh ∈ ˆA be the corresponding
Haar measures. Then
i) the modular automorphism of the Haar functional ˆh is implemented by gLgR, i.e. for all
x ∈A we have θˆh(x) = gLgRxg −1
R g−1
L ;
ii) the dual left integral of h can be expressed as χ = ˆhˆg−2
R ;
iii) the S-invariant trace functional τ =g−1⇀χ and the Haar functional ˆh are related by
τ = ˆ g−1
L ˆhˆg−1
R (4.39)
ˆh = gLgR⇀τ (4.40)
Proof: i): Using identities like ˆ gL⇀x =gRx,... etc, which follow from Scholium 2.7, one can
easily verify ˆg⇀x↼ ˆg =gLgRxg−1
R g−1
L , for x ∈A.
ii): The identity ˆh⇀h = g2
L = 1 ↼ ˆg2
R implies 1 = ˆh⇀h↼ ˆg−2
R = ˆh⇀hg −2
L , hence
hg−2
L =hg−2
R is the dual left integral of ˆh. By duality, ˆhˆg−2
R is the dual left integral χ of h.
iii): τ = g−1⇀ ˆhˆg−2
R = ˆg−1
R (ˆhˆg−2
R )ˆgR = ˆg−1
L ˆhˆg−1
R and τ = g−1⇀ (g−2
R ⇀ ˆh) = g−1
L g−1
R ⇀ ˆh
completes the proof. Q.e.d.
Cyclicity and separability of the vector h in the right AL,R-module IL (cf. Scholium 3.17)
allows us to introduce ˆAR-valued ”Radon-Nikodym derivatives” of left integrals l with respect
to the Haar measure. At ﬁrst note that l = ⊓L(h)l = hl = h ⊓R (l) = hS−1(⊓R(l)) therefore
using Scholium 2.7 we have
⟨ϕ, l⟩= ⟨ϕρR, h⟩= ⟨ρLϕ, h⟩ (4.41)
where ρR = ⊓R(l)⇀ ˆ1 and ρL =S−1(⊓R(l))⇀ ˆ1 = ˆS2(ρR).
Proposition 4.15 The bijections IL(A) → ˆAR provided by the left and right Radon-Nikodym
derivatives l ↦→ρL and l ↦→ρR, respectively, obey the following properties.
37
i) l is non-degenerate iﬀ ρR,L is invertible.
ii) If l is non-degenerate then l is normalized iﬀ l2 =l.
iii) l is of positive type, i.e. ⟨ϕ∗ϕ,l ⟩ ≥ 0 for all ϕ ∈ ˆA, iﬀ ⊓R(l) ≥ 0 iﬀ ρR ∈ ˆg1/2
R ˆAR
+ˆg−1/2
R
where ˆAR
+ is the cone of positive elements in ˆAR. In this case ρL =ρ∗
R and there exists a
ξ ∈ ˆA such that ⟨ϕ, l⟩= ⟨ξ∗ϕξ, h⟩ for ϕ ∈ ˆA.
iv) Let λ be the dual left integral of l. Then the Radon-Nikodym derivatives of λ and l are
related by ⊓R(l)(ˆ⊓R(λ)⇀ 1) = g−2
R .
Proof: i) follows from cyclicity of h in IL
AR. ii): l2 =l implies ( ⊓L(l) − 1)l = 0 and acting with
λ⇀, where λ is the dual left integral of l, one obtains ⊓L(l) = 1. The converse implication
is trivial. iii): As in the proof of Theorem 4.5 l is of positive type iﬀ S(l(1)) ⊗l(2) belongs
to the positive cone (4.12). If it does then ⊓R(l) = S(l(1))l(2) ≥ 0. Now assume ⊓R(l) ≥ 0.
Then introducing ξ = ⊓R(l)1/2⇀ ˆ1 we have ⊓R(l)1/2 = ξ⇀ 1, S−1(⊓R(l)1/2) = S(ξ⇀ 1)∗ =
(1↼ ˆS−1(ξ))∗ = 1↼ξ ∗ therefore l = hS−1(⊓R(l)1/2) ⊓R (l)1/2 = ξ⇀h↼ξ ∗ proving that l is
of positive type. It remained to reformulate positivity of ⊓R(l) in terms of ρR. Use the fact
that the antimultiplicative map xR ↦→(xR⇀ ˆ1) from AR to ˆAR sends the ∗-operation into a
new involution, xR∗⇀ ˆ1 = (S−1(xR)⇀ ˆ1)∗ = (S−2(xR)⇀ ˆ1)∗ = (gRxRg−1
R ⇀ ˆ1)∗ = ˆgR(xR⇀
ˆ1)∗ˆg−1
R . Therefore the equality ⊓R(l) = xR∗xR for some xR ∈AR is equivalent to the equality
ρR = (xR⇀ ˆ1)(xR∗⇀ ˆ1) = ˆg1/2
R ηη∗ˆg−1/2
R with η = ˆg−1/2
R (xR⇀ ˆ1)ˆg1/2
R ∈ ˆAR. iv) follows by an
elementary calculus starting from the identity 1 = λ⇀l = ˆhˆ⊓R(λ)⇀hS −1(⊓R(l)). Q.e.d.
A Appendix: The Weak Hopf Algebra B ⊗ Bop
LetB be a separable algebra over the ﬁeld K and let E:B →K be a non-degenerate functional
with index 1. These are the data needed for constructing a WHA structure on the algebra
B ⊗Bop. For a similar construction of a WBA see [14].
At ﬁrst choose a basis {ei} of B over K and let {fi} be its dual basis w.r.t. E, i.e.
E(eifj) = δij. Then
a) ∑
ifi ⊗ei ∈B ⊗B is independent of the choice of {ei};
b) ∑
iE(xfi)ei = x = ∑
ifiE(eix), x ∈B;
c) ∑ fiei = 1;
d) ∑
ixfi ⊗ei = ∑
ifi ⊗eix, x ∈B;
e) if θ denotes the modular automorphism of E, i.e. E(xy) = E(yθ(x)), x,y ∈B, then
∑
i
fi ⊗xei =
∑
i
fiθ(x) ⊗ei, x ∈B ;
f ) ∑
ifi ⊗ei = ∑
iei ⊗θ−1(fi) = ∑
iθ(ei) ⊗fi.
The algebra B ⊗Bop is the K-spaceB ⊗B with multiplication (a ⊗b)(x ⊗y) := (ax ⊗yb). Its
WHA structure is deﬁned by
∆( x ⊗y) =
∑
i
(x ⊗fi) ⊗ (ei ⊗y) (A.1)
ε(x ⊗y) = E(xy) (A.2)
S(x ⊗y) = y ⊗θ(x) (A.3)
38
The veriﬁcation of the WHA axioms is left to the reader. The le ft and right subalgebras of
B ⊗Bop are B ⊗ 1 and 1 ⊗B, respectively, because we have
⊓L (x ⊗y) = xy ⊗ 1, ⊓R(x ⊗y) = 1 ⊗yθ(x) . (A.4)
Let A be an arbitrary WHA over K. Then ALAR is a sub-WHA with hypercenter AL ∩AR.
Thus ALAR decomposes into a direct sum of WHA-s each summand being isom orphic to a
WHA of the type B ⊗Bop.
Since B ⊗Bop is separable, by Theorem 3.13, it must contain a normalized l eft integral.
Indeed,
l :=
∑
i
fi ⊗ei ≡ S2(1(2))1(1) (A.5)
is such a left integral. What is more, it is non-degenerate.
Before looking for Haar integrals some remarks about innern ess of θ are in order. The
quantityq =∑
ieifi always implementsθ−1, i.e. xq =qθ(x) for x ∈B, but it is not necessarily
invertible. (For example for B = M2(Z Z2) and for any non-degenerate functional E the q
is identically zero.) In fact q is invertible iﬀ the left regular trace on B is non-degenerate
(especially if K is of characteristic zero). Fortunately one can circumvent this nuisance by
using the existence of a non-degenerate trace tr on any separ able algebra B (see [5]). Then the
Radon-Nykodim derivative γ of E w.r.t. tr provides an invertible element implementing θ,
E(x) = tr (xγ) , θ (x) = γxγ −1 , x ∈B . (A.6)
This proves that θ is inner and therefore so is the square of the antipode, S2 =θ ⊗θ.
Omitting the details we can now formulate the condition for t he existence of the Haar
measures h and ˆh as follows. Haar measure in B ⊗Bop exists iﬀ ∑
ifiγ2ei is invertible and
Haar measure in ˆB ⊗Bop exists iﬀ E(1B) ⁄= 0.
