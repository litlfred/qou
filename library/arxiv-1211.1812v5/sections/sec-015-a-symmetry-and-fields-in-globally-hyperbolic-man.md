---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-015-a-symmetry-and-fields-in-globally-hyperbolic-man
section_title: "A Symmetry and fields in globally hyperbolic manifolds."
section_number: null
pages: 30-37
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
Symmetry and ﬁelds in globally hyperbolic manifolds.
The proof of the symmetry relations (3.10).
Before to make the necessary computations we
need two Lemmata:
Lemma A.1. For any a ∈∆, cocycle zρ ∈obj Z1
c (R)<a and paths p, p′ : e →o in ∆a , we have
z(p) = z(p′).
30
Proof. Let p′ : o →e denote the opposite path. Then p ∗p′ : o →o is a loop in ∆a and, since
π1(∆) = π1(a) = 0, we have that p ∗p′ is homotopic to the trivial loop bo : o →o, bo := (o, o; o).
By [35, Lemma 2.6-7] we conclude that z(p)z(p′)∗= z(p ∗p′) = z(bo) = 1.
The independence of p allows us to write zoe := z(p), p : e →o; note that zeo = z∗
oe .
Lemma A.2. The symmetry operator (3.9) is independent of the choice of poe, po′e , o and o′ ,
for any e < a.
Proof. The independence of poe, po′e follows by the previous Lemma, so it remains to verify the
independence of o, o′ . To this end, we have to verify that deﬁning ǫ(z, w)e with ω, ω′ < a, ω ⊥ω′ ,
in place of o, o′ we obtain the same symmetry operator. As an intermediate step, we consider a
region ¯ω′ < a such that ¯ω′ ⊥ω, o. Then
ǫ(z, w)e
LemmaA.1
=
w∗
ωew∗
oωσo(zo′ ¯ω′z¯ω′e)∗· zo′ ¯ω′z¯ω′eρe(woωwωe)
o′,¯ω′⊥o
=
w∗
ωew∗
oωσo(z¯ω′e)∗· z∗
o′ ¯ω′zo′ ¯ω′z¯ω′eρe(woω)ρe(wωe)
(3.4)
=
w∗
ωeσω(z¯ω′e)∗w∗
oω · z∗
o′ ¯ω′zo′ ¯ω′z¯ω′eρe(woω)ρe(wωe)
(3.3)
=
w∗
ωeσω(z¯ω′e)∗· ρ¯ω′(woω)∗z¯ω′eρe(woω)ρe(wωe)
(3.4)
=
w∗
ωeσω(z¯ω′e)∗· z¯ω′eρe(w∗
oωwoω)ρe(wωe)
=
w∗
ωeσω(z¯ω′e)∗· z¯ω′eρe(wωe) .
Let us write ǫoo′
e
to denote the symmetry obtained by by using o, o′ < a.
Then the previous
computations say that
ǫoo′
e
= ǫω¯ω′
e
,
∀¯ω′ < a : ¯ω′ ⊥ω, o .
(A.1)
Let us now return to our ω′ < a such that ω′ ⊥ω. Then the argument for proving (A.1) applies,
and we have
ǫω¯ω′
e
= ǫωω′
e
;
but by (A.1) we also ﬁnd ǫoo′
e
= ǫωω′
e
, as desired.
In the sequel, to be concise, we shall write z ≡zρ, wσ ≡w, v ≡vτ ∈Z1
c (R)<a . To prove (3.10.1)
we compute
ǫ(z, w)∂0b · z(b)ρ∂1b(w(b))
(3.4)
=
w∗
o∂0bσo(zo′∂0b)∗· zo′∂0bz(b)ρ∂1b(wo∂0bw(b))
LemmaA.2
=
w(b)σ∂1b(z(b)) · σ∂1b(z(b))∗w(b)∗w∗
o∂0bσo(zo′∂0b)∗· zo′∂1bρ∂1b(wo∂1b)
LemmaA.2
=
w(b)σ∂1b(z(b)) · σ∂1b(z(b))∗w∗
o∂1bσo(zo′∂0b)∗· zo′∂1bρ∂1b(wo∂1b)
(3.5)
=
w(b)σ∂1b(z(b)) · w∗
o∂1bσo(z(b))∗σo(zo′∂0b)∗· zo′∂1bρ∂1b(wo∂1b)
=
w(b)σ∂1b(z(b)) · w∗
o∂1bσo(zo′∂1b)∗· zo′∂1bρ∂1b(wo∂1b)
LemmaA.2
=
w(b)σ∂1b(z(b)) · ǫ(z, w)∂1b .
31
To prove (3.10.2) we compute
seσe(te) · ǫ(z, w)e
=
seσe(te) · w∗
oeσo(zo′e)∗· zo′eρe(woe)
(3.7)
=
σ′
e(te)se · w∗
oeσo(zo′e)∗· zo′eρe(woe)
(3.6)
=
σ′
e(te)w′∗
oe · soσo(zo′e)∗· zo′eρe(woe)
(3.5),(3.7)
=
w′∗
oeσ′
o(te) · σ′
o(zo′e)∗so · zo′eρe(woe)
o⊥o′,(3.3)
=
w′∗
oeσ′
o(tez∗
o′e) · ρo′(so)zo′eρe(woe)
(3.6),(3.5)
=
w′∗
oe · σ′
o(z′o′e)∗σ′
o(to′) · zo′eρe(sowoe)
o⊥o′,(3.3)
=
w′∗
oe · σ′
o(z′o′e)∗to′ · zo′eρe(sowoe)
(3.6)
=
w′∗
oeσ′
o(z′o′e)∗· to′zo′eρe(w′
oe) · ρe(se)
(3.6)
=
w′∗
oeσ′
o(z′o′e)∗· z′
o′eteρe(w′
oe) · ρe(se)
(3.7)
=
w′∗
oeσ′
o(z′o′e)∗z′
o′eρ′
e(w′
oe) · teρe(se)
=
ǫ(z′, w′)e · teρe(se) .
To prove (3.10.3) we compute
ǫ(z, w)eǫ(w, z)
=
w∗
oeσo(zo′e)∗· zo′eρe(woe) · z∗
oeρo(wo′e)∗· wo′eσe(zoe)
LemmaA.2
=
w∗
oeσo(zo′e)∗· zo′e · ρe(woe)z∗
o′eρo′(woe)∗· woeσe(zo′e)
(3.4)
=
w∗
oeσo(zo′e)∗· zo′ez∗
o′e · ρo′(woe)ρo′(woe)∗· woeσe(zo′e)
(3.4)
=
w∗
oeσo(zo′e)∗· woeσe(zo′e)
(3.4)
=
w∗
oewoeσe(zo′e)∗σe(zo′e)
=
1 .
The second of (3.10.3) is trivial to verify. Finally we prove (3.10.4). To this end, we note that by
[9, Lemma B.5], given e < a we can pick o ⊥o′ , o, o′ < a, such that:
• o ⊥e;
• there is ω ⊇e, o′ such that ω ⊥o.
The second point implies, using Lemma A.1, that wo′e = w(b0) ∈Rω , where b0 = (o′, e; ω) ∈Σ1(∆a)
can be regarded as a path from e to o′ . So (3.3) implies
ρo′(wo′e) ∈Rω , τo(wo′e) = wo′e
⇒
τo ◦ρo′(wo′e) = ρo′(wo′e) = ρo′ ◦τo(wo′e) ,
(A.2)
and we can compute
ǫ((z ⊗w), v)e
=
v∗
oeτo(zo′eρe(wo′e))∗· zo′eρe(wo′e) · {ρe ◦σe}(voe)
(3.4)
=
v∗
oeτo(ρo′(wo′e)zo′e)∗· zo′eρe(wo′e) · {ρe ◦σe}(voe)
(A.2)
=
v∗
oeτo(zo′e)∗· {ρo′ ◦τo}(wo′e))∗zo′e · ρe(wo′eσe(voe))
(3.4)
=
v∗
oeτo(zo′e)∗· zo′eρe(τo(wo′e))∗· ρe(wo′eσe(voe))
=
v∗
oeτo(zo′e)∗zo′eρe(voe) · ρe(v∗
oeτo(wo′e)∗wo′eσe(voe))
=
ǫ(z, v)e · ρe(ǫ(w, v)e) .
32
Field nets on globally hyperbolic manifolds: the proof of Lemma 4.4.
We apply the
construction of [14] to the quantum ﬁelds deﬁned in [11, 12] (in the following, we maintain the
notation of §4.4 for λ, L±
λ , L+,J
λ
, DM , D+ and D−). To this end, following [14] we introduce a
mass function
µ : λ →(0, ∞)
:
inf µ > 0 ,
µ(̺ ) = µ(̺ ) .
Given a smooth Cauchy hypersurface Σ ⊂M , we consider the restriction operator and the forward
normal derivative respectively,
ρ0 , ρ1 : C∞(M) →C∞(Σ) ,
and, given m > 0, the linear operator
Em : C∞
c (M) →C∞(M)
deﬁned by the fundamental solution of the Klein-Gordon equation with mass m and initial data in
Σ (see [11, §2]).
Let f ∈D+ and v ∈L+,J
λ
. We consider the decompositions f(x) = {f̺ (x) ∈L̺ }, v = {v̺ ∈
L̺ }, and deﬁne the C∞, compactly supported functions f̺ ,v(x) := (f̺ (x), v̺ )̺ ∈R, x ∈M . Note
that f̺ ,v is linear in v, and
(f(x), v) =
X̺
f̺ ,v(x) , ∀x ∈M ,
where the sum is ﬁnite because f ∈D+. Let now C∞
ﬁn(M, L+,J
λ
) denote the linear space of compactly
supported, L+,J
λ
-valued functions having a ﬁnite set of non-zero components on̺
∈λ. By Riesz
duality in L+,J
λ
and linearity of ρ0, ρ1, Em we can deﬁne the extensions



Eµ : D+ →C∞
ﬁn(M, L+,J
λ
)
:
({Eµf}(x), v) := P̺
∈λ{Eµ(̺ )f̺ ,v}(x)
ρλ
• : C∞
ﬁn(M, L+,J
λ
) →C∞
ﬁn(Σ, L+,J
λ
)
:
({ρλ
•f}(x), v) := P̺
∈λ{ρ•f̺ ,v}(x) ,
• = 0, 1 ,
where v, x vary in L+,J
λ
, M respectively.
We now consider the Hilbert space L2(Σ, L+
λ ) and the associated bosonic Fock space, written
H+
Σ , carrying the representation of the canonical commutation relations
[a(h), a∗(h′)] =
Z
Σ
(h, h′) ,
h, ˜h ∈L2(Σ, L+
λ ) .
The argument of [11, Theorem 2] shows that a representation of the canonical commutation relations
is realized on the Hilbert space Hφ
∗:= H+
Σ ,
[φ(f), φ(f ′)] = −i
Z
M
(f, Eµf ′) ,
∀f, f ′ ∈D+ ,
where
φ(f) := θ(ρλ
1Eµf) −π(ρλ
0Eµf)
,
θ := 2−1/2(a∗+ a) , π := i2−1/2(a∗−a) ,
is well-deﬁned because ρλ
1Eµf, ρλ
0Eµf have compact support in Σ (see the proof of [11, Cor.1.3]).
33
We now consider the Dirac ﬁeld, following [12]. The strategy is the same of the scalar ﬁeld,
with the technical complications due to the spinor structures. As a ﬁrst step we consider the dual
bundle DM ∗→M of DM and denote the set of C∞, compactly supported sections (cospinors) by
S∞
c (M, DM ∗), so we have the pairing ⟨ω, s⟩∈C∞
c (M, C), ω ∈S∞
c (M, DM ∗), s ∈S∞
c (M, DM).
Again, we consider the restriction operator to the Cauchy hypersurface Σ ⊂M (endowed with the
spin structure induced by M ),
ρ : S∞(M, DM) →S∞(Σ, DΣ) ,
(A.3)
and the fundamental solution of the Dirac equation with mass m > 0,
Sm : S∞
c (M, DM) →S∞(M, DM)
(A.4)
(see [12, §II.A]). Moreover we consider the representation of vector ﬁelds as operators on the space
of spinors, deﬁned, in local frames, by contraction with the Cliﬀord-Dirac γ -matrices ([12, §I.A]),
S∞(M, T M) × S∞
c (M, DM) →S∞
c (M, DM) ,
v, s 7→¯vs := (vhγi
hksk)i ,
(A.5)
and the Dirac conjugation, deﬁned (in local frames) by applying to spinors the matrix β ∈SU(4)
intertwining the γ -matrices with their adjoints ([12, §I.B]),
S∞
c (M, DM) →S∞
c (M, DM ∗) ,
s 7→s+ := (shβhk)k .
(A.6)
If n is the vector ﬁeld forward normal to Σ, then we consider the integral
Z
Σ

s+, ¯ns′

,
s, s′ ∈S∞
c (Σ, DΣ) ,
(A.7)
that is a scalar product on S∞
c (Σ, DΣ) ([12, §III.A]).
We now extend the coeﬃcients considering the Hilbert bundles D−
λ M →M (generalized spinors)
and D−,∗
λ
M →M , where D−,∗
λ
M := L−,∗
λ
⊗DM ∗is the tensor product of the conjugate space
L−,∗
λ
by the cospinor bundle (generalized cospinors). The restrictions to Σ shall be denoted with
analogous notations. We have pairings
S∞
c,ﬁn(X, D−,∗
λ
X) × S∞
c,ﬁn(X, D−
λ X) →C∞
c (X, C) ,
ω, s 7→⟨ω, s⟩−
λ
,
X = M, Σ ,
where the symbol ”ﬁn” indicates that we are considering (co)spinors with ﬁnitely many components
on̺
∈λ. We also have extensions of (A.3) and (A.4), respectively,



ρλ : S∞(M, D−
λ M) →S∞(Σ, D−
λ Σ) ,
ρλ := ρ ⊗1−,
Sµ : D−→S∞(M, D−
λ M) ,
Sµs := P⊕̺{Sµ(̺ ) ⊗1−}s̺
(The sum of the previous expression is ﬁnite for any s ∈D−, so no convergence questions arise).
Moreover, (A.7) yields a scalar product on S∞
c (Σ, D−
λ Σ) deﬁned, on elementary tensors of the
type s = s1 ⊗s2 ∈S∞
c (Σ, D−
λ Σ), s1 ∈S∞
c (Σ, DΣ), s2 ∈C∞
c (Σ, L−
λ ), as
Z
Σ

s+
1 , ¯ns′
1

(s2, s′
2)
	
,
s, s′ ∈S∞
c (Σ, D−
λ Σ) .
We denote the corresponding completion by L2(Σ, D−
λ Σ). Any generalized cospinor ω ∈S∞
c (Σ, D−,∗
λ
Σ)
can be regarded as a linear functional on L2(Σ, D−
λ Σ), by extending the map
s 7→
Z
Σ
⟨ω, s⟩−
λ
,
s ∈S∞
c (Σ, D−
λ Σ) ,
34
to generic vectors in L2(Σ, D−
λ Σ). So S∞
c (Σ, D−,∗
λ
Σ) embeds in the conjugate space L2,∗(Σ, D−
λ Σ).
We now denote the fermionic Fock space of L2(Σ, D−
λ Σ) by H−
Σ . It carries a representation of
the CARs
X∗(h)X(ϕ) + X(ϕ)X∗(h) = ⟨ϕ, h⟩
,
h ∈L2(Σ, D−
λ Σ) , ϕ ∈L2,∗(Σ, D−
λ Σ) .
We set Hψ
∗:= H−
Σ and
ψ(s) := −iX∗(ρλSµs) ,
s ∈D−.
These 8 are well-deﬁned operators in BHψ
∗since ρλSµs has compact support for any s ∈D−(see
([12, III.B])). Recalling the deﬁnitions of ρλ and Sµ , and applying to them [12, Prop.2.4(d)] we
obtain, as desired, the CARs
ψ∗(s)ψ(s′) + ψ(s′)ψ∗(s) = −i
Z
M

s+, Sµs′
−
λ
,
s, s′ ∈D−.
References
[1] Y. Aharonov, D. Bohm: Signiﬁcance of electromagnetic potentials in quantum theory. Phys. Rev. 115
(1959) 485-491.
[2] S.J. Avis, C.J. Isham: Quantum ﬁeld theory and ﬁbre bundles in a general spacetime. In: Recent
Developments in Gravitation. Cargese 1978, ed. by M. Levy and S. Deser, Springer US.
[3] H. Araki: Mathematical theory of quantum ﬁelds. Oxford University Press, Oxford, 2009.
[4] R. Brunetti, L. Franceschini, V. Moretti: Topological features of massive bosons on two dimensional
Einstein space-time. Ann. Henri Poincar´e 10 (2009) 1027-1073.
[5] R. Brunetti, K. Fredenhagen, R. Verch: The generally covariant locality principle – A new paradigm
for local quantum physics. Comm. Math. Phys. 237 (2003) 31-68.
[6] D. Buchholz, G. Mack, I. Todorov: Localized automorphisms of the U(1)-current algebra on the circle.
An instructive example. In book: The algebraic theory of superselection sectors. Introduction and
recent results, Publisher: World Scientiﬁc 1990, Editors: D. Kastler, pp.356-378.
[7] D. Buchholz, G. Mack, I. Todorov: The current algebra on the circle as a germ of local ﬁeld theories.
Nuclear Physics B (Proc.Suppl.) 5B (1988) 20-56.
[8] H. Baumgaertel, F. Lled´o: Duality of compact groups and Hilbert C∗-systems for C∗-algebras with a
nontrivial center. Int. J. Math. 15 (2004) 759-812.
[9] R. Brunetti, G. Ruzzi: Quantum charges and spacetime topology: The emergence of new superselection
sectors. Comm. Math. Phys. 87 (2009) 523-563.
[10] J. Cheeger, J. Simons: Diﬀerential characters and geometric invariants. In: Geometry and Topology,
Lecture Notes in Mathematics 1167, Springer, Berlin (1985) 50-80.
[11] J.Dimock: Algebras of local observables on a manifold. Comm. Math. Phys. 77 (1980) 219-228.
[12] J. Dimock: Dirac quantum ﬁelds on a manifold. Trans. Am. Math. Soc. 269 (1982) 133-147.
[13] S. Doplicher: Spin and Statistics and First Principles. Found. Phys. 40 (2010) 719-732.
[14] S. Doplicher, G. Piacitelli: Any compact group is a gauge group. Rev. Math. Phys. 14 (2002) 873-885.
[15] S. Doplicher, J.E. Roberts: Duals of Compact Lie Groups Realized in the Cuntz Algebras and Their
Actions on C*-algebras. J. Funct. Anal. 74 (1987) 96-120.
8 In the reference [12] the analogue of the ﬁeld ψ is denoted by ψ+ , whilst the notation ψ is used for the Dirac
ﬁeld evaluated on cospinors.
35
[16] S. Doplicher, J.E. Roberts: A New Duality Theory for Compact Groups. Inv. Math. 98 (1989) 157-218.
[17] S. Doplicher and J.E. Roberts: Why there is a ﬁeld algebra with a compact gauge group describing the
superselection structure in particle physics. Commun. Math. Phys. 131 (1990) 51-107.
[18] W. Ehrenberg, R. E. Siday: The refractive index in electron optics and the principles of dynamics.
Proc. Phys. Soc. B62 (1949) 8-21.
[19] R.P.Feynman, R.B.Leighton, M.Sands: The Feynman lectures on physics (vol.2), Addison-Wesley Pub-
lishing Company, 1964.
[20] C.J. Fewster: Endomorphisms and automorphisms of locally covariant quantum ﬁeld theories. Rev.
Math. Phys. 25 (2013) 1-47.
[21] K. Fredenhagen: Generalizations of the theory of superselection sectors. In: The algebraic theory of
superselection sectors. Introduction and recent results, ed. D. Kastler World Sci. Publ., Singapore, New
Jersey, London, Hong Kong (1990) 379-387.
[22] D. Guido, R. Longo, J.E. Roberts, R. Verch: Charged sectors, spin and statistics in quantum ﬁeld
theory on curved spacetimes. Rev. Math. Phys. 13 (2001) 125-198.
[23] R. Haag. Local Quantum Physics. Springer Texts and Monographs in Physics, 1996, 2nd edition.
[24] S. Kobayashi: Diﬀerential Geometry of complex vector bundles, Princeton University Press, 1987.
[25] C.J. Isham: Spinor Fields in Four Dimensional Space-Time. Proc. Roy. Soc. Lond. A 364 (1978) 591-
599.
[26] C.J. Isham: Twisted Quantum Fields in a Curved Space-Time. Proc. R. Soc. London A. 362 (1710)
383-404.
[27] B. Lang: Twisted Quantum Fields in Curved Spacetimes ´a la C.J. Isham from the point of view of
Algebraic Quantum Field Theory. PhD Thesis, in preparation, Adv.: C.J. Fewster.
[28] S. Mac Lane: Categories for the working mathematician, Springer Verlag, Berlin - Heidelberg - New
York, 1998.
[29] D. Quillen: Higher algebraic K-theory. I, in Algebraic K-Theory, I: Higher K-Theories, Lecture Notes
in Mathematics 341 Springer, Berlin, 1973.
[30] J.E. Roberts: Lectures on Algebraic Quantum Field Theory. In: The algebraic theory of superselec-
tion sectors. Introduction and recent results, ed. D. Kastler World Sci. Publ., Singapore, New Jersey,
London, Hong Kong (1990) 1-112.
[31] J.E. Roberts: More Lectures on Algebraic Quantum Field Theory. In: Noncommutative geometry: lec-
tures given at the C.I.M.E. summer school held in Martina Franca, Italy, Lecture notes in mathematics
1831, Springer-Verlag (2000) 263-339.
[32] J.E. Roberts, G. Ruzzi: A cohomological description of connections and curvature over posets. Theory
and Applications of Categories 16 (2006) 855-895.
[33] J.E. Roberts, G. Ruzzi, E. Vasselli: A theory of bundles over posets. Adv. Math. 220 (2009) 125-153.
[34] J.E. Roberts, G. Ruzzi, E. Vasselli: Net bundles over posets and K-theory. Int. J. Math. 24 (2013) 1-34.
[35] G. Ruzzi: Homotopy of posets, net-cohomology and superselection sectors in globally hyperbolic space-
times. Rev. Math. Phys. 17 (2005) 1021-1070.
[36] G. Ruzzi: Punctured Haag duality in locally covariant quantum ﬁeld theories. Comm. Math. Phys. 256
(2005) 621-634.
[37] G. Ruzzi, E. Vasselli: A new light on nets of C*-algebras and their representations. Comm. Math.
Phys. 312 (2012) 655-694.
Representations of nets of C*-algebras over S1. Comm. Math. Phys. 316 (2012) 127-149.
[38] E. Vasselli: Bundles of C*-categories, II: C*-dynamical systems and Dixmier-Douady invariants. J.
Funct. Anal. 257 (2009) 357-387.
36
[39] E. Vasselli: Presheaves of symmetric tensor categories and nets of C*-algebras. To appear in Journal
of Noncommutative Geometry, arXiv:1210.4302.
[40] E. Vasselli: A theory of gerbes over posets. In preparation.
[41] R. Verch: Continuity of symplectically adjoint maps and the algebraic structure of Hadamard vacuum
representations for quantum ﬁelds in curved spacetime. Rev. Math. Phys. 9 (1997) 635-677.
37
