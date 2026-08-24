---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-566-5-mumfords-f-ake-projective-plane-229
section_title: "MUMFORD’S F AKE PROJECTIVE PLANE. 229"
section_number: 5
pages: 233-235
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
with Π 3 =µ and Π z =zσΠ for z∈L. The involution ∗ on D is deﬁned by
z∗ =z for z∈L and Π ∗ =µΠ 2. It is easily veriﬁed that ∗ is positive.
We introduce a non-degenerate anti-symmetric Q-bilinear form ψ =ψb
on V = D by putting b = (λ−λ)−λΠ + λΠ 2. Then deﬁne an algebraic
groupG over Q as follows: Given a Q-algebra R, we set
G(R) : = {g∈ ((D⊗R)opp)×|ψ(xg,yg ) = c(g)ψ(x,y ), c(g)∈R×, x,y∈V⊗R}.
The algebraic group GR is isomorphic to GU(2 , 1), which acts on the two
dimensional complex unit-ball B. In the following we will construct an open
compact subgroup C in G(Af ). By these data, we can deﬁne a Shimura
variety
SC : = G(Q)\ B×G(Af )/C.
The canonical model of SC is deﬁned over E : = ε(K), which we denote by
ShC.
The congruence condition. First we deﬁne an algebraic group I over Q
by
I(R) : = {g∈ (Md(K)⊗R)×| H−1 tgH∈R×}
for any Q-algebra R, where
H =


3
λ λ
λ 3 λ
λ λ 3

.
Then I is an inner form of G so that G(A2
f )∼
=I(A2
f ).
To deﬁne the level structure, it suﬃces to deﬁne the prime-2- part C 2.
We deﬁne C 2 in the form C 2 =C 2,7C7 with C7∈G(Q7)∼
=I(Q7) and C 2,7
being the maximal one:
C 2,7 : = {g∈G(A2,7
f )| Γ 2,7g⊆ Γ 2,7},
with Γ 2,7 = Γ ⊗ZˆZ2,7, where ˆZ2,7 = lim Z/mZ with the projective limit
taken over m such that (2,m ) = (7,m ) = 1.
Now the component C7 is deﬁned as follows: we have an isomorphism
G(Q7) ∼−→{g∈ GL3(~Q7)| g∗Hg =c(g)H, c(g)∈ Q×
7},
where ~Q7 is the ramiﬁed quadratic extension of Q7, and ∗ is the matrix
transposition followed by the Galois action. Let ~C7 be the maximal open
compact subgroup of G(Q7) consisiting of g which maps Γ⊗ZZ7 to itself. We
consider modulo√
−7 reduction of ~C7, which is a subgroup G0 in GL 3(F7).
The matrix H mod√−7 is of rank 1, and has 2 dimensional null space N0.
Restricting elements in G0 to N0, we obtain a homomorphism
π : ~C7−→ GL2(F7).
The last group has 2 6327 elements. Let S be a 2-Sylow subgroup of GL 2(F7)∩
{g| detg =±1}. Now we set C7 : = π−1(S).
230 B. OVER VIEW OF THEORY OF p-ADIC UNIFORMIZATION.
Theorem 5.1. The canonical model ShC of the Shimura variety obtained
by the data as above has exactly three geometrically connect ed components
deﬁned over Q(ζ7). Moreover, for any connected component S, its base
changeS⊗Q(ζ7) Q2(ζ7) is isomorphic to the Mumford’s fake projective plane
[Mu79] tensored by Q2(ζ7).
More precisely, the associated rigid analytic space to ShC⊗EEλ is iso-
morphic to Ω /Γ with
Γ = I(Q)
⋂
(J(Q2)×C 2)⊂J(Q2)∼
= PGL(3, Q2),
where I(Q) is considered as a subgroup of I(Af )∼
= J(Q2)×G(A2
f ). The
proof of the theorem is in [ Kat98], where two more fake projective planes
are discussed as examples of Shimura varieties.
APPENDIX C
p-adic symmetric domains and Totaro’s theorem
By TSUZUKI Nobuo
This appendix is a short exposition of M. Rapoport and T. Zink ’s con-
struction of p-adic symmetric domains [ RZ96] and of B. Totaro’s theorem
[T ot96]. Let G be a connected reductive algebraic group over Qp. The
setF of ﬁltrations on an F -isocrystal with G-structure has a structure of a
homogeneous space. Rapoport and Zink introduced a p-adic rigid analytic
structure on the setF wa of weakly admissible points inF. They conjectured
that the point inF wa is characterized by the semistability in the sense of the
geometric invariant theory [ MFK94] and Totaro proved this conjecture.
1. W eakly admissible ﬁltered isocrystals.
We recall J.-M. Fontaine’s deﬁnition of weakly admissible ﬁ ltered F -
isocrystals [ F on79].
