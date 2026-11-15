---
doc_id: ant-v14-n7-s-p02
doc_title: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values"
section_id: sec-002-2-iteration-of-the-harmonic-frobenius-of-integra
section_title: "Iteration of the harmonic Frobenius of integrals at (1, 0)"
section_number: 2
pages: 14-21
source_pdf: ant-v14-n7-s-p02.pdf
source_sha256: fd2121feb180b282
toc_source: inferred
doc_brief: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values — 10 sections: Front matter; Introduction; Preliminaries"
---
We prove (0-3) in Section 2A, and we prove (0-4) in Section 2B.
2A. The ﬁxed point equation of the harmonic Frobenius of integrals at (1, 0).
2A1. The ﬁxed point equation for the Frobenius of integrals. We express the iterated Frobenius at
base-points of (1, 0) as a function of the number of iterations.
Proposition 2A.1.
(a) For all ˜α ∈N∗, we have 8q,−∞= ﬁxq ˜α0,8q,−˜α i.e.,
8q,−˜α ◦∫1,0 τ(q ˜α)8q,−∞= 8q,−∞,
i.e.,
τ(q ˜α)8q,∞◦∫1,0 8q,˜α = 8q,∞.
(b) For the topology deﬁned by ND on 51,0(K) we have
8q,−˜α
˜α→∞
−−−→8q,−∞,
and
8q,˜α
˜α→∞
−−−→8q,∞.
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1725
(c) For any ˜α ∈N∗, f ∈51,0(K), g ∈5(pα)
1,0 (K),
φ−˜α
log(q)
log(p)
( f ) =
∞
X
n=0
8q,∞◦∫1,0 (τn(8q,−∞◦∫1,0 f )).(q ˜α)n,
φ ˜α
log(q)
log(p) (g) =
∞
X
n=0
8q,∞◦∫1,0 (τn(8q,−∞◦∫1,0 g)).(q ˜α)n.
Proof. (a) (1-4) and (1-5) imply the ﬁrst equation. (1-4) and (1-5) imply the second equation via
Notation 1A.1(ii).
(b) The ﬁrst equation follows from Lemma 1B.7 and the discussion after Proposition 1B.4, and the
second equation is deduced from the ﬁrst one by applying the inversion for ◦∫1,0, knowing the structure of
topological group of (51,0(K), ◦∫1,0) for ND. Alternatively, the two equations follow from (i), the fact
that τ(q ˜α)8q,∞
˜α→∞
−−−→1, τ(q ˜α)8q,−∞
˜α→∞
−−−→1 and that structure of topological group.
(c) Follows from (1-3), (1-4), in which we replace 8q,˜α and 8q,−˜α by their expressions given by (i), and
in which we express τ in terms of the maps τn deﬁned in Section 1A2 just after (1-2).
□
In particular, by Proposition 2B.1(i), the existence and uniqueness of a Frobenius-invariant path, which
follows from the theory of Coleman integration, is reproved and made more precise in the very particular
example of 51,0(K).
2A2. Pro-unipotent harmonic action and harmonic Frobenius of integrals at (1, 0). We move from
discussing the Frobenius at (1, 0) to discussing the harmonic Frobenius of integrals, in the framework
R
1,0 in the sense of Section 1C1. In view of this result, we introduce new objects.
Deﬁnition 2A.2. Let K⟨⟨e0∪µN ⟩⟩g
o(1) ⊂K⟨⟨e0∪µN ⟩⟩be the set of elements h such that all series of the type
P∞
l=0 h[el
0eξd+1end−1
0
eξd · · · en1−1
0
eξ1], where d and the ni are positive integers and the ξi are N-th roots
of unity, are convergent in K. Let the summation map be S : K⟨⟨e0∪µN ⟩⟩g
o(1) →K⟨⟨e0∪µN ⟩⟩
∫1,0
har,0 deﬁned by
h 7→
X
ξ∈µN(K)
ξ −1
X
d∈N∗
ξ1,...,ξd+1∈µN(K)
n1,...,nd∈N∗
h(ξ)

1
1 −e0
eξd+1end−1
0
eξd · · · en1−1
0
eξ1

eξd+1end−1
0
eξd · · · en1−1
0
eξ1.
We note that K⟨⟨e0∪µN ⟩⟩g
o(1) contains K⟨⟨e0∪µN ⟩⟩o(1) deﬁned in Section 1B. We now deﬁne a variant of
the pro-unipotent harmonic action of integrals ◦∫
har. In the next statement, we denote by ◦
∫1,0
Ad the extension
of the adjoint Ihara product ◦
∫1,0
Ad into a map K⟨⟨e0∪µN ⟩⟩× K⟨⟨e0∪µN ⟩⟩→K⟨⟨e0∪µN ⟩⟩deﬁned again by the
formula of (1-6).
Deﬁnition 2A.3. Let the map
◦
∫1,0
har,0 : Ad ˜51,0(K)o(1)(e1) × K⟨⟨e0∪µN ⟩⟩
∫1,0
har,0 →K⟨⟨e0∪µN ⟩⟩
∫1,0
har,0
1726
David Jarossay
be characterized by the commutativity of the diagram:
Ad ˜51,0(K)o(1)(e1) × K⟨⟨e0∪µN ⟩⟩g
o(1)
id ×S

◦
∫1,0
Ad
/ K⟨⟨e0∪µN ⟩⟩g
o(1)
S
Ad ˜51,0(K)o(1)(e1) × K⟨⟨e0∪µN ⟩⟩
∫1,0
har
◦
∫1,0
har
/ K⟨⟨e0∪µN ⟩⟩
∫1,0
har
(2-1)
The pro-unipotent harmonic action of integrals at (1, 0) is the map
◦
∫1,0
har : Ad ˜51,0(K)o(1)(e1) × K⟨⟨e0∪µN ⟩⟩
∫1,0
har →K⟨⟨e0∪µN ⟩⟩
∫1,0
har
deﬁned by the same formula as the one of ◦
∫1,0
har .
The basic properties of ◦
∫1,0
har are summarized in the next proposition.
Proposition 2A.4.
(i) ◦
∫1,0
har is a well-deﬁned group action of (Ad ˜51,0(K)o(1), ◦
∫1,0
Ad ) on K⟨⟨e0∪µN ⟩⟩
∫1,0
har , con-
tinuous for the topology deﬁned by ND.
(ii) The isomorphism K⟨⟨e0∪µN ⟩⟩
∫1,0
har
∼
−→K⟨⟨e0∪µN ⟩⟩∫
har, f 7→P
w∈Wdhar(e0∪µN ) f [w]1/(1−e0)·w induces,
for all m ∈N∗, a natural isomorphism of continuous group actions between the m-th term of ◦∫
har,
namely (g, hm) 7→lim(τ(m)(g) ◦
∫0,0
Ad hm), and the action (g, h) 7→τ(m)g ◦
∫1,0
har h.
Proof. (i) For any g in Ad ˜51,0(K)(e1), and any word w, the map f 7→S(g ◦
∫1,0
Ad f )[w] factors in a natural
way through the map f 7→Sf . This can be seen by writing the formula for the dual of ◦
∫1,0
Ad . The fact
that ◦
∫1,0
Ad sends Ad ˜51,0(K)o(1)(e1) × K⟨⟨e0∪µN ⟩⟩g
o(1) to K⟨⟨e0∪µN ⟩⟩g
o(1) follows from the shufﬂe equation for
elements of ˜51,0(K)o(1) and from the formula for the dual of ◦
∫1,0
Ad . Finally, S is surjective: any h in
K⟨⟨e0∪µN ⟩⟩
∫1,0
har,0 is equal to
S

X
ξ1,...,ξd+1∈µN(K)
n1,...,nd∈N∗
h[eξd+1end−1
0
eξd · · · en1−1
0
eξ1]eξd+1end−1
0
eξd · · · en1−1
0
eξ1

.
This proves that ◦
∫1,0
har,0 is well-deﬁned, and that one can write a formula for it, which is linear with respect
to the second argument; thus, ◦
∫1,0
har is well-deﬁned.
Let g1, g2 ∈Ad ˜51,0(K)o(1)(e1) and f ∈K⟨⟨e0∪µN ⟩⟩o(1); we have
g2 ◦
∫1,0
Ad (g1 ◦
∫1,0
Ad f ) = (g2 ◦
∫1,0
Ad g1) ◦
∫1,0
Ad f.
Applying the map S and the commutativity of (2-1) gives
g2 ◦
∫1,0
har (S(g1 ◦
∫1,0
Ad f )) = (g2 ◦
∫1,0
Ad g1) ◦
∫1,0
har S( f ),
and applying again the commutativity of (2-1) we deduce
g2 ◦
∫1,0
har (g1 ◦
∫1,0
har S( f )) = (g2 ◦
∫1,0
Ad g1) ◦
∫1,0
har S( f ).
This proves that ◦
∫1,0
har is a group action.
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1727
The map ◦
∫1,0
Ad is continuous and each sequence (wl)l∈N such that wl = el
0eξd+1end−1
0
eξd · · · en1−1
0
eξ1
for all l with eξd+1end−1
0
eξd · · · en1−1
0
eξ1 independent of l satisﬁes lim supl→∞depth(wl) < +∞and
weight(wl)
l→∞
−−−→+∞; thus the map S is continuous. By the commutativity of (2-1), this implies
that ◦
∫1,0
har ◦(id ×S) is continuous. If a sequence (hu)u∈N in K⟨⟨e0∪µN ⟩⟩
∫1,0
har tends to h ∈K⟨⟨e0∪µN ⟩⟩
∫1,0
har , we
can ﬁnd a sequence ( fu)u∈N and f in K⟨⟨e0∪µN ⟩⟩g
o(1) such that hu = Sfu for all u, h = f and fu →f . We
deduce that ◦
∫1,0
har is continuous.
(ii) The relation between ◦
∫1,0
har and ◦∫
har follows from the deﬁnitions of these two objects and the fol-
lowing property of ◦
∫1,0
Ad , which is itself a consequence of the formula for the dual of ◦
∫1,0
Ad : for all
h ∈Ad ˜51,0(K)o(1)(e1) and g ∈Ad ˜51,0(K)o(1)(e1), and for any word w over e0∪µN , we have
(g ◦
∫1,0
Ad h)

1
1 −e0
w

= lim
l→∞(g ◦
∫1,0
Ad Sh)[el
0w].
□
In the next example, the indices (n1) and (n1, n2) are harmonic words in the sense of Deﬁnition 1C.1.
Example 2A.5. If N = 1, the terms of depth one and two of g ◦
∫1,0
har h are given as follows:
(g ◦
∫1,0
har h)(n1) = h(n1) + g

1
1 −e0
e1en1−1
0
e1

,
(g ◦
∫1,0
har h)(n1, n2) = h(n1, n2) + g

1
1 −e0
e1en2−1
0
e1en1−1
0
e1

+
n1−1
X
r=0
g

1
1 −e0
e1en2−1
0
e1er
0

h(n1 −r)
+
n2−1
X
r=0
g[er
0e1en1−1
0
e1]h(n2 −r).
We now deduce from Deﬁnition 2A.3 the counterpart of the harmonic Frobenius of integrals in the
framework
R
1,0.
Deﬁnition 2A.6. For any α ∈N∗divisible by log(q)/log(p), let the harmonic Frobenius of integrals
at (1, 0), iterated α times, be the map (τ(pα)φα)
∫1,0
har : K⟨⟨e0∪µN ⟩⟩
∫1,0
har →K⟨⟨e0∪µN ⟩⟩
∫1,0
har deﬁned by f 7→
Ad8p,α(e1) ◦
∫1,0
har f .
Corollary 2A.7. The isomorphism
K⟨⟨e0∪µN ⟩⟩
∫1,0
har
∼
−→K⟨⟨e0∪µN ⟩⟩∫
har,
f 7→
X
w∈Wdhar(e0∪µN )
f [w]
1
1 −e0
w
induces, for all m ∈N, an isomorphism of continuous maps between (τ(pα)φα)
∫1,0
har and the m = 1 term of
(τ(pα)φα)har.
Proof. Direct consequence of Proposition 2A.4 and the deﬁnitions of the two harmonic Frobeniuses. □
1728
David Jarossay
2A3. Fixed point equation for the harmonic Frobenius. We can now deduce from Section 2A1, via
Section 2A2, an expression of the iterated harmonic Frobenius of integrals at (1, 0) as a function of its
number of iterations, whose coefﬁcients are expressed in terms of the ﬁxed point of the Frobenius at
(1, 0); this is (0-3).
By Proposition 2B.1, we have τ(q ˜α)8q,∞◦∫1,08q,˜α =8q,∞. By deﬁnition, the inverse of 8q,∞for ◦∫1,0
is 8q,−∞thus the inverse of τ(q ˜α)(8q,∞) is τ(q ˜α)(8q,−∞). Whence 8q,˜α = τ(q ˜α)8q,−∞◦∫1,0 8q,∞. By
applying Ad(e1), we deduce Ad8q,˜α(e1) = τ(q ˜α) Ad8q,−∞(e1) ◦
∫1,0
Ad Ad8q,∞(e1), whence S Ad8q,˜α(e1) =
S(τ(q ˜α) Ad8q,−∞(e1) ◦
∫1,0
Ad Ad8q,∞(e1)). By the commutative diagram in Deﬁnition 2A.3, this amounts
to S Ad8q,˜α(e1) = τ(q ˜α) Ad8q,−∞(e1) ◦
∫1,0
har S Ad8q,∞(e1)). By (1-19), we have S Ad8q,˜α(e1) = harq,˜α and
S Ad8q,∞(e1)) = harq,∞. Whence (0-3).
Remark 2A.8. The power series expansion of any harq ˜α((ni)d; (ξi)d+1) in terms of q ˜α, given by (0-3)
have coefﬁcients of degrees in {1, . . . , min1⩽i⩽d ni −1} equal to 0. This follows from 8(ξ)
q,−∞[e0] = 0
which implies Ad8(ξ)
q,−∞(eξ) = eξ + terms of depth ⩾2, for all ξ ∈µN(K).
Example 2A.9. In depth one and two and for P1 \ {0, 1, ∞}, we have
harq ˜α(n1) = harq∞(n1) +
∞
X
n=n1
(q ˜α)n Ad8q,−∞(e1)[en−n1
0
e1en1−1
0
e1],
harq ˜α(n1, n2) = harq∞(n1, n2) +
∞
X
n=n1+n2
(q ˜α)n Ad8q,−∞(e1)[en−n1−n2
0
e1en2−1
0
e1en1−1
0
e1]
+
n1−1
X
r1=0
∞
X
n=n2+r1
(q ˜α)n Ad8q,−∞(e1)[en−n2−r1
0
e1en2−1
0
e1er1
0 ] harq∞(n1 −r1)
+
n2−1
X
r2=0
(q ˜α)n1+r2 Ad8q,−∞(e1)[er
0e1en1−1
0
e1] harq∞(n2 −r2).
2B. Iteration equation of the harmonic Frobenius of integrals at (1, 0). We are now going to reexpress
the iterated harmonic Frobenius of integrals at (1, 0) as a function of the number of iterations, in a different
way, without involving the ﬁxed point.
2B1. Iteration on the Frobenius at (1, 0). As in Section 2A2, the ﬁrst step is to describe the iterated
Frobenius at base-points (1, 0) as a function of its number of iterations, this time without involving the
ﬁxed point but, instead, the map of iteration of the weighted Ihara action (Deﬁnition 1B.6).
Proposition 2B.1. For all ˜α0, ˜α ∈N∗such that ˜α0 | ˜α, we have
8q,α = iter
∫1,0
˜α/ ˜α0,q ˜α0(8q, ˜α0)
and
8q,˜α = 8q,−˜α
−1∫1,0.
More generally, for all α ∈N∗, we have 8p,−α = 8p,−1 ◦∫1,0 τ(λ)σ(8p,−1) · · ·◦∫1,0 τ(λα−1)σ α−1(8p,−1)
and 8p,−α = 8
−1∫1,0
p,α
.
Proof. This follows from (1-3), (1-4), and Deﬁnition 1B.3.
□
This generalizes a statement appearing in [Furusho 2007, proof of Proposition 3.1].
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1729
Before continuing on the study of the iterated Frobenius, we remark that, by Proposition 2A.1 and
Proposition 2B.1 considering the coefﬁcients of these noncommutative formal power series series,
one has equations relating the p-adic cyclotomic multiple zeta values ζp,α(w) and ζp,α′(w′), for any
α, α′ ∈Z ∪{±∞} \ {0}, as follows:
Corollary 2B.2. Let α ∈Z ∪{±∞} \ {0}. For any n ∈N∗, let Zp,α,n be the Q-vector space generated by
the numbers ζp,α(w) with w a word of weight n:
(1) For α ∈N∗, Zp,α,n = σ −α(Zp,1,n), and Zp,−α,n = σ α(Zp,−1,n). If α ∈Z \ {0} is such that p|α| is a
power of q then Zp,α,n = Zq,∞,n = Zq,−∞,n. In particular, the dimension of Zp,α,n is independent of
α ∈Z ∪{±∞} \ {0}.
(2) N3,D(8p,α) is independent of α ∈Z ∪{±∞} \ {0}.
Proof. For any positive integers n, d, let O
X,e0∪µN
n,d
⊂OX,e0∪µN be the subspace generated by words of
weight n and depth d. Let
O2
n,⩽d =
X
r⩾2
n1+···+nr=n
d1+···+dr⩽d
O
X,e0∪µN
n1,d1
X · · · XO
X,e0∪µN
nr,dr
.
Let λ ∈K such that |λ|p < 1 and a ∈N∗. For each w word on e0∪µN , of weight n and depth d, by (1-15),
(1-16), (1-17) we have the following congruences, where the duals refer to the duality between OX,e0∪µN
and the points of the corresponding group scheme:
(1 −λn) ﬁx∨
λ (w) ≡w mod O2
n,⩽d,
iter
∫1,0
a,λ
∨
(w) ≡1 −λan
1 −λn w mod O2
n,⩽d,
(−1∫1,0)∨(w) ≡−w mod O2
n,⩽d.
By induction on (n, d), this implies the following equalities, where Z(λ)O
X,e0∪µN
n,⩽d
is the Z(λ)-module
generated by words of weight n and of depth ⩽d:
ﬁx∨
λ (Z(λ)O
X,e0∪µN
n,⩽d
) = iter∨
a◦∫1,0 ,λ(Z(λ)O
X,e0∪µN
n,⩽d
) = (−1∫1,0)∨(Z(λ)O
X,e0∪µN
n,⩽d
) = Z(λ)O
X,e0∪µN
n,⩽d
,
and, that, for all g ∈5ξ,0(K), we have
N3,D(ﬁxλ,g) = N3,D(g
a◦∫1,0 ,λ) = N3,D(g−1∫1,0) = N3,D(g).
This implies the result via Proposition 2B.1 and Proposition 2B.1.
□
A particular case of Corollary 2B.2(i) can be found in [Yamashita 2010, Proposition 3.10] and an
explicit example is given in [Furusho 2007, Example 2.10].
Remark 2B.3. The proof of Corollary 2B.2 indicates that the equations of Corollary 2B.2 are compatible
with the depth ﬁltration and the bounds on valuations of pMZVµN’s, which are two parameters in our
computation. This can be viewed as a prerequisite for the next paragraphs in which we show a kind of
compatibility between the iteration of the Frobenius and our computation of pMZVµN’s.
1730 David Jarossay

2B2. The iteration of the harmonic Frobenius. As in Section 2A2, we move from discussing the Frobenius
at (1, 0), in Section 2A2, to discussing the harmonic Frobenius. We first describe how the map iter! "

depends on its parameters A and a.

Definition 2B.4. For any d € N*, let t,,.<a : K (@oupy)) > K(eoupy) be the map which sends f =

Vw word flwlw to Vw word, depth(w)<d flwlw.

Proposition 2B.5. Let A, A, a be three formal variables. There exists a map
iter!9(A, A,a): Ady, jc (€1) > K (eoupyLA, al(A), (2-2)

such that, for any f € Ada, (xy (1) word w,a € N* such that a > depth(w) and i € K \ {0} which is
not a root of unity, we have

JC Pw] = iter!9(A, 0", a)( fw]

iter,
Proof. With the assumptions of the statement, let d = depth(w); knowing that g[@] = 1, dualizing the
multiplication of the a factors in (1-17) gives

weal ii— ii—
iter,') (g)[w => > > grileg, (All VAd jeirt(e))e Ewa] X--+
O<d'<d 0<i, <+++<igr<a—1 Wi, AB,..., Win ~D
Wi Wi yy =W

x gM Ne, EAM iy t(Ce))e)[Wi (2-3)

We have assumed that a > d; let us thus separate the indices i; < d and i; > d:

~ bw = yy yD

O<d'<d 0<ij <--<ig<a-1_ 0d" <d!<d 0<ij <-<ign<d d<igny) <-<iy <a-1

This yields an expression of (2-3), as a K-linear combination indexed by {(d",d')|0<d” <d'<d}x
{deconcatenations of w in d’ nonempty subwords} which is independent of a but depends polynomially
of 4, and with coefficients as well independent of a and polynomial functions of A, of the numbers

DS Ae, A Ad giant (Ce) Wig] Xx (AE He0, (24! AD seigrt (Ce) EM Wigr]-
d<iyn<+-<iy<a-1

(2-4)
Let «® = g® — 1 and € = gO! — 1. For 0 <ij <a—1, we have (where t,,<q is defined in
Definition 2B.4)

ij ij \.m’ m
Ty, <a (Ad, ayi;-1(€)) = » (in Gin EE ‘eges"!

mj wn! jen
When i; > d, the collection of conditions hy Sli nce weunie x if m’, <ij,mj +m’, +1 < d} is equivalent
to {mj,m’, ¢N, mj +m, +1 <d); thus, dualizing in (2-4) each factor g(A'i—!e, (AUT! Ad .ij-1 (€e))e)

tells us that (2-4) is a linear combination, independent of a and i, of sums

EEL n Nn)

d<ign <-<iy'<a—1 j=d"
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1731

where weight; € N* arises as the weight of a certain quotient sequence of w,,, and (i) ij Ble ') are polynomials

of i;.
Finally, any function of a of the form 7) <j, <...<;<a—1 T= Panic with L,5€N*,Cy,...,C3€
N* and P;,..., Ps € K[T] polynomials, depends on a as a polynomial function of (a, A“): one can

reduce this statement to L = 0 by splitting an iterated sum over 0 < I; <--+ < Is <a—1 at L and by
induction on 4, then use, again by induction on 6 that, for all deg je N*, we have

I ;
f= yo 4) (RES 1), Oo
d(AC/) AG —1

Let us now define the map of iteration of the harmonic Frobenius of integrals at (1, 0), by using the

above iteration map and the summation map S of Definition 2A.2.

JSi,o

Definition 2B.6. Let iter," (a, 4) = So iter/.9(A, A“,a): Adar, y¢x) (€1) > K (eouny ht?

har

We can now deduce from Section 2B 1, and the previous proposition a second description of the iterated
harmonic Frobenius as a function of its number of iterations; this is (0-4).
By Proposition 2B.1, we have ®y ¢ = =iters'? 4 fa (Pq.c0)> thus by Proposition 2B.5, we have Oy 4 =

iter!.0(q®, g, &/&p)(®q,a,), whence S®,y g = S iter! (q®, q*, &/&o)(®q,a,)- By Definition 2B.6, this
amounts to S®, ¢ = = iter)!" (@/Q0, g 8) (by, ay)- Finally, by (1-19), we have S®, 4 = harg ¢. Whence (0-4).
