---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-052-2a2-pro-unipotent-harmonic-action-and-harmonic-f
section_title: "2A2. Pro-unipotent harmonic action and harmonic Frobenius of integrals at (1,0)"
section_number: null
pages: 59-62
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
discussing the Frobenius at(1, 0) to discussing the harmonic Frobenius of integrals, in the framework∫
1,0 in the sense of Section 1C1. In view of this result, we introduce new objects.
Deﬁnition 2A.2. Let K⟨⟨e0∪µN⟩⟩~o(1)⊂ K⟨⟨e0∪µN⟩⟩be the set of elements h such that all series of the type∑∞
l=0 h[el
0eξd+1end−1
0 eξd··· en1−1
0 eξ1], where d and the ni are positive integers and theξi are N-th roots
of unity, are convergent in K . Let the summation map be S: K⟨⟨e0∪µN⟩⟩~o(1)→ K⟨⟨e0∪µN⟩⟩
∫1,0
har,0 deﬁned by
h↦→
∑
ξ∈µN(K)
ξ−1 ∑
d∈N∗
ξ1,...,ξd+1∈µN(K)
n1,...,nd∈N∗
h(ξ)
[ 1
1− e0
eξd+1end−1
0 eξd··· en1−1
0 eξ1
]
eξd+1end−1
0 eξd··· en1−1
0 eξ1.
We note that K⟨⟨e0∪µN⟩⟩~o(1) contains K⟨⟨e0∪µN⟩⟩o(1) deﬁned in Section 1B. We now deﬁne a variant of
the pro-unipotent harmonic action of integrals◦∫
har. In the next statement, we denote by◦
∫1,0
Ad the extension
of the adjoint Ihara product◦
∫1,0
Ad into a map K⟨⟨e0∪µN⟩⟩× K⟨⟨e0∪µN⟩⟩→ K⟨⟨e0∪µN⟩⟩deﬁned again by the
formula of (1-6).
Deﬁnition 2A.3. Let the map
◦
∫1,0
har,0: Ad˜51,0(K)o(1)(e1)× K⟨⟨e0∪µN⟩⟩
∫1,0
har,0→ K⟨⟨e0∪µN⟩⟩
∫1,0
har,0
1726 David Jarossay
be characterized by the commutativity of the diagram:
Ad˜51,0(K)o(1)(e1)× K⟨⟨e0∪µN⟩⟩~o(1)
id×S

◦
∫1,0
Ad // K⟨⟨e0∪µN⟩⟩~o(1)
S

Ad˜51,0(K)o(1)(e1)× K⟨⟨e0∪µN⟩⟩
∫1,0
har
◦
∫1,0
har // K⟨⟨e0∪µN⟩⟩
∫1,0
har
(2-1)
The pro-unipotent harmonic action of integrals at (1, 0) is the map
◦
∫1,0
har: Ad˜51,0(K)o(1)(e1)× K⟨⟨e0∪µN⟩⟩
∫1,0
har→ K⟨⟨e0∪µN⟩⟩
∫1,0
har
deﬁned by the same formula as the one of◦
∫1,0
har .
The basic properties of◦
∫1,0
har are summarized in the next proposition.
Proposition 2A.4. (i)◦
∫1,0
har is a well-deﬁned group action of(Ad˜51,0(K)o(1),◦
∫1,0
Ad) on K⟨⟨e0∪µN⟩⟩
∫1,0
har , con-
tinuous for the topology deﬁned by ND.
(ii) The isomorphism K⟨⟨e0∪µN⟩⟩
∫1,0
har
∼−→K⟨⟨e0∪µN⟩⟩∫
har, f↦→∑
w∈Wdhar(e0∪µN) f[w]1/(1−e0)·w induces,
for all m∈ N∗, a natural isomorphism of continuous group actions between the m-th term of◦∫
har,
namely(g, hm)↦→ lim(τ(m)(g)◦
∫0,0
Ad hm), and the action(g, h)↦→τ(m)g◦
∫1,0
har h.
Proof. (i) For any g in Ad˜51,0(K)(e1), and any wordw, the map f↦→ S(g◦
∫1,0
Ad f)[w] factors in a natural
way through the map f↦→ S f. This can be seen by writing the formula for the dual of ◦
∫1,0
Ad . The fact
that◦
∫1,0
Ad sends Ad˜51,0(K)o(1)(e1)× K⟨⟨e0∪µN⟩⟩~o(1) to K⟨⟨e0∪µN⟩⟩~o(1) follows from the shufﬂe equation for
elements of ˜51,0(K)o(1) and from the formula for the dual of ◦
∫1,0
Ad . Finally, S is surjective: any h in
K⟨⟨e0∪µN⟩⟩
∫1,0
har,0 is equal to
S
( ∑
ξ1,...,ξd+1∈µN(K)
n1,...,nd∈N∗
h[eξd+1end−1
0 eξd··· en1−1
0 eξ1]eξd+1end−1
0 eξd··· en1−1
0 eξ1
)
.
This proves that◦
∫1,0
har,0 is well-deﬁned, and that one can write a formula for it, which is linear with respect
to the second argument; thus,◦
∫1,0
har is well-deﬁned.
Let g1, g2∈ Ad˜51,0(K)o(1)(e1) and f∈ K⟨⟨e0∪µN⟩⟩o(1); we have
g2◦
∫1,0
Ad (g1◦
∫1,0
Ad f)=(g2◦
∫1,0
Ad g1)◦
∫1,0
Ad f.
Applying the map S and the commutativity of (2-1) gives
g2◦
∫1,0
har (S(g1◦
∫1,0
Ad f))=(g2◦
∫1,0
Ad g1)◦
∫1,0
har S( f),
and applying again the commutativity of (2-1) we deduce
g2◦
∫1,0
har (g1◦
∫1,0
har S( f))=(g2◦
∫1,0
Ad g1)◦
∫1,0
har S( f).
This proves that◦
∫1,0
har is a group action.
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1727
The map◦
∫1,0
Ad is continuous and each sequence (wl)l∈N such that wl= el
0eξd+1end−1
0 eξd··· en1−1
0 eξ1
for all l with eξd+1end−1
0 eξd··· en1−1
0 eξ1 independent of l satisﬁes lim supl→∞ depth(wl) <+∞ and
weight(wl) l→∞−−−→+∞; thus the map S is continuous. By the commutativity of (2 -1), this implies
that◦
∫1,0
har◦(id×S) is continuous. If a sequence (hu)u∈N in K⟨⟨e0∪µN⟩⟩
∫1,0
har tends to h∈ K⟨⟨e0∪µN⟩⟩
∫1,0
har , we
can ﬁnd a sequence ( fu)u∈N and f in K⟨⟨e0∪µN⟩⟩~o(1) such that hu= S fu for all u, h= f and fu→ f . We
deduce that◦
∫1,0
har is continuous.
(ii) The relation between ◦
∫1,0
har and◦∫
har follows from the deﬁnitions of these two objects and the fol-
lowing property of ◦
∫1,0
Ad , which is itself a consequence of the formula for the dual of ◦
∫1,0
Ad : for all
h∈ Ad˜51,0(K)o(1)(e1) and g∈ Ad˜51,0(K)o(1)(e1), and for any wordw over e0∪µN , we have
(g◦
∫1,0
Ad h)
[ 1
1− e0
w
]
= lim
l→∞
(g◦
∫1,0
Ad Sh)[el
0w]. □
In the next example, the indices (n1) and(n1, n2) are harmonic words in the sense of Deﬁnition 1C.1.
Example 2A.5. If N= 1, the terms of depth one and two of g◦
∫1,0
har h are given as follows:
(g◦
∫1,0
har h)(n1)= h(n1)+ g
[ 1
1− e0
e1en1−1
0 e1
]
,
(g◦
∫1,0
har h)(n1, n2)= h(n1, n2)+ g
[ 1
1− e0
e1en2−1
0 e1en1−1
0 e1
]
+
n1−1∑
r=0
g
[ 1
1− e0
e1en2−1
0 e1er
0
]
h(n1− r)
+
n2−1∑
r=0
g[er
0e1en1−1
0 e1]h(n2− r).
We now deduce from Deﬁnition 2A.3 the counterpart of the harmonic Frobenius of integrals in the
framework
∫
1,0.
Deﬁnition 2A.6. For any α∈ N∗ divisible by log(q)/log(p), let the harmonic Frobenius of integrals
at(1, 0), iterated α times, be the map (τ( pα)φα)
∫1,0
har : K⟨⟨e0∪µN⟩⟩
∫1,0
har → K⟨⟨e0∪µN⟩⟩
∫1,0
har deﬁned by f↦→
Ad8p,α(e1)◦
∫1,0
har f .
Corollary 2A.7. The isomorphism
K⟨⟨e0∪µN⟩⟩
∫1,0
har
∼−→K⟨⟨e0∪µN⟩⟩∫
har, f↦→
∑
w∈Wdhar(e0∪µN)
f[w] 1
1− e0
w
induces, for all m∈ N, an isomorphism of continuous maps between(τ( pα)φα)
∫1,0
har and the m= 1 term of
(τ( pα)φα)har.
Proof. Direct consequence of Proposition 2A.4 and the deﬁnitions of the two harmonic Frobeniuses. □
1728 David Jarossay
