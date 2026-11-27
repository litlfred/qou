---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-027-64-constructing-x
section_title: "Constructing X"
section_number: 6.4
pages: 33-36
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
and assume that a collection ( Xµ′ )µ′<µ∈Q+ with Xµ′ ∈U +
µ′ and X0 = 1 has already
been constructed and that this collection satisﬁes conditions (6.2) and (6.3) for all
µ′<µ and for all i ∈I. Deﬁne
Ai = −(qi −q−1
i )
(
Xµ+Θ( αi)−αiciXi +siXµ−αi
)
,(6.12)
iA = −(qi −q−1
i )
(
q−(Θ( αi),αi)ciXiXµ+Θ( αi)−αi +siXµ−αi
)
(6.13)
for all i ∈ I. We will keep the above assumptions and the deﬁnition of Ai and
iA all through this subsection. We will prove that the elements Ai,iA, which are
the right hand sides of equations (6.2), (6.3), satisfy the condition s (6.6) and (6.7).
By Proposition 6.3 this will prove the existence of an element Xµ with the desired
properties.
Lemma 6.7. The relation ri(jA) = jr(Ai) holds for all i,j ∈I.
Proof. This is a direct calculation. Note that all computations include the cas e
i = j. We expand both sides of the desired equation, using (2.13) and (2.1 4) and
the assumption that the elements Xµ′ satisfy (6.2) and (6.3) for µ′ <µ . We obtain
ri(jA) = −(qj −q−1
j )q−(Θ( αj ),αj )cjXjri(Xµ+Θ( αj )−αj )
− (qj −q−1
j )q−(Θ( αj ),αj )q(αi,µ+Θ( αj )−αj )ri(cjXj)Xµ+Θ( αj )−αj
− (qj −q−1
j )sjri
(
Xµ−αj
)
= (qj −q−1
j )q−(Θ( αj ),αj )cjXj(qi −q−1
i )Xµ+Θ( αj )−αj +Θ( αi)−αiciXi
+ (qj −q−1
j )q−(Θ( αj ),αj )cjXj(qi −q−1
i )siXµ+Θ( αj )−αj −αi
− (qj −q−1
j )q−(Θ( αj ),αj )q(αi,µ+Θ( αj )−αj )ri(cjXj)Xµ+Θ( αj )−αj
+ (qj −q−1
j )sj(qi −q−1
i )Xµ−αj +Θ( αi)−αiciXi
+ (qj −q−1
j )sj(qi −q−1
i )siXµ−αi−αj,
jr(Ai) = −(qi −q−1
i )jr(Xµ+Θ( αi )−αi)ciXi
− (qi −q−1
i )q(αj,µ+Θ( αi)−αi)Xµ+Θ( αi)−αi jr(ciXi)
− (qi −q−1
i )sijr(Xµ−αi )
= (qi −q−1
i )(qj −q−1
j )q−(Θ( αj ),αj )cjXjXµ+Θ( αi)−αi+Θ( αj )−αjciXi
+ (qi −q−1
i )(qj −q−1
j )sjXµ+Θ( αi)−αi−αjciXi
− (qi −q−1
i )q(αj,µ+Θ( αi)−αi)Xµ+Θ( αi)−αi jr(ciXi)
+ (qi −q−1
i )si(qj −q−1
j )q−(Θ( αj ),αj)cjXjXµ−αi+Θ( αj )−αj
+ (qi −q−1
i )si(qj −q−1
j )sj Xµ−αi−αj.
We see that the ﬁrst and ﬁfth summands in the above expansions of ri(jA) and
jr(Ai) coincide, the second summand of ri(jA) is the same as the fourth summand
of jr(Ai), and the fourth summand of ri(jA) coincides with the second summand
of jr(Ai). Therefore, the claim of the Lemma, ri(jA) = jr(Ai), is equivalent to
34 MARTINA BALAGOVI ´C AND STEF AN KOLB
the third summands being equal,
(6.14) − (qj −q−1
j )q−(Θ( αj ),αj )q(αi,µ+Θ( αj )−αj )ri(cjXj)Xµ+Θ( αj )−αj
= −(qi −q−1
i )q(αj,µ+Θ( αi)−αi)Xµ+Θ( αi)−αijr(ciXi).
By (5.10) and (2.24) we may assume that i = τ (j) ∈ I \ X because other-
wise both sides of the above equation vanish. By (2.24) we have jr
(
ciXi
)
=
q(αj,−Θ( αi)−αj )rj(ciXi). Substituting this and using qi = qj, we see that (6.14) is
equivalent to
(6.15) q(αj,Θ( αi)−Θ( αj ))+(αi,µ−αj )ri(cjXj)Xµ+Θ( αj )−αj
=q(αj,µ−αi−αj )Xµ+Θ( αi)−αirj (ciXi).
By Equation 5.3 one has Θ( αi) −αi = Θ( αj) −αj and hence Xµ+Θ( αj )−αj =
Xµ+Θ( αi)−αi. Moreover, ri(TwX (Ei)) lies in MX and hence it commutes with
Xµ+Θ( αi)−αi. Using this, we can rewrite (6.15) as
(6.16) q(αj,Θ( αi−αj ))+(αi,µ)Xµ+Θ( αi)−αiri(cjXj)
=q(αj,µ−αj )Xµ+Θ( αi)−αirj (ciXi).
If Xµ+Θ( αi)−αi = 0 then both sides of the above equation vanish. Hence assume
that Xµ+Θ( αi)−αi is nonzero. Corollary 6.2 states that then Θ( µ) = −µ. Along
with Θ( αi −αj) = αi −αj , this implies that ( αi −αj,µ ) = 0. Hence (6.16) is
equivalent to the relation
(6.17) q(αj,αi)ri(cjXj) = rj (ciXi).
Using the deﬁnition (5.11) of Zi the above formula follows from assumption (5.15)
about the parameters c. □
This proves that the elements Ai,iA satisfy the ﬁrst condition from Proposition
6.3.(2). Next we prove that they also satisfy the second condition.
Lemma 6.8. For all i ⁄= j ∈ I the elements Ai,Aj given by (6.12) satisfy the
relation
(6.18) −1
qi −q−1
i
1−aij∑
s=1
[ 1 −aij
s
]
qi
(−1)s
⟨
F 1−aij −s
i FjFs−1
i ,Ai
⟩
−
− 1
qj −q−1
j
⟨
F 1−aij
i ,Aj
⟩
= 0.
Proof. We may assume that µ = (1 −aij)αi +αj and that Θ( µ) = −µ, as otherwise
all terms in the above sum vanish. By Lemma 6.4 it suﬃces to consider t he following
two cases.
Case 1: Θ(αi) = −αj and aij = 0. In this case µ = αi +αj and si = sj = 0
by deﬁnition (5.7) of the parameter set S. Hence Ai = −s(j)(qi −q−1
i )ciEj and
Aj = −s(i)(qj −q−1
j )cjEi. Therefore the left hand side of (6.18) is equal to
1
qi −q−1
i
⟨Fj,Ai⟩ − 1
qj −q−1
j
⟨Fi,Aj⟩ = −s(j)ci ⟨Fj,Ej⟩ +s(i)cj ⟨Fi,Ei⟩.(6.19)
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 35
Using qi = qj, the fact that s(i) = s(j) by (5.2), and the relation ci = cj which
holds by deﬁnition of the parameter set C, one sees that the right hand side of
(6.19) vanishes.
Case 2: Θ(αi) = −αi and Θ( αj) = −αj. In this case by (5.5) one has i,j ∈Ins.
Hence, by deﬁnition (5.7) of the parameter set S, one has either sj = 0 or aij ∈
−2N0. If sj = 0 then Lemma 6.5 implies that (1 −aij)αi +αj =µ ∈ N0αi ⊕ 2N0αj,
which is not the case. If −aij is even then the left hand side of (6.18) can be written
as
(6.20) 1
qi −q−1
i
⟨
FjF −aij
i ,Ai
⟩
− 1
qj −q−1
j
⟨
F 1−aij
i ,Aj
⟩
+ −1
qi −q−1
i
−aij/2∑
s=1
[ 1 −aij
s
]
qi
(−1)s
⟨
F 1−aij −s
i FjFs−1
i −Fs
iFjF −aij −s
i ,Ai
⟩
.
By (6.12) and (6.13) one has Aj = −(qj −q−1
j )−1sjXµ−αj = jA and hence
1
qi −q−1
i
⟨
FjF −aij
i ,Ai
⟩
− 1
qj −q−1
j
⟨
F 1−aij
i ,Aj
⟩
= − 1
qi −q−1
i
1
qj −q−1
j
⟨
F −aij
i ,jr(Ai) −ri(jA)
⟩
.
In view of Lemma 6.7 the above relation shows that the sum of the ﬁrs t two terms
of (6.20) vanishes. Each of the remaining summands in (6.20) contain s a factor of
the form
⟨
F 1−aij −s
i FjFs−1
i −Fs
iFjF −aij −s
i ,Ai
⟩
= −1
qi −q−1
i
⟨
F −aij −s
i FjFs−1
i −Fs−1
i FjF −aij −s
i ,ir(Ai)
⟩
.(6.21)
Set x =F −aij −s
i FjFs−1
i −Fs−1
i FjF −aij −s
i and observe that σ(x) = −x. Inserting
the deﬁnition of Ai into (6.21) one obtains in view of Xi = −Ei the relation
⟨
F 1−aij −s
i FjFs−1
i −Fs
iFjF −aij −s
i ,Ai
⟩
=
⟨
x,ir(−Xµ−2αiciEi +siXµ−αi )
⟩
.
Using the skew derivation property (2.14) and the assumption that Xµ′ satisﬁes
(6.3) for all µ′ <µ one obtains
⟨
F 1−aij −s
i FjFs−1
i −Fs
iFjF −aij −s
i ,Ai
⟩
= −(qi −q−1
i )
⟨
x,ciq(αi,αi)ciEiXµ−4αiEi
⟩
+ (qi −q−1
i )
⟨
x,siciXµ−3αiEi
⟩
−
⟨
x,ciq(αi,µ−2αi)Xµ−2αi
⟩
+ (qi −q−1
i )
⟨
x,siq(αi,αi)ciEiXµ−3αi
⟩
− (qi −q−1
i )
⟨
x,s 2
i Xµ−2αi
⟩
Using the relations (2.20) and the property ci = q(αi,αi)ci which holds by (5.17),
the above equation becomes
⟨
F 1−aij −s
i FjFs−1
i −Fs
iFjF −aij −s
i ,Ai
⟩
= −ciq(αi,αi)ci
1
qi −q−1
i
⟨
ri(ir(x)), Xµ−4αi
⟩
−ciq(αi,µ−2αi)⟨
x, Xµ−2αi
⟩
(6.22)
−sici
⟨
ri(x) +ir(x), Xµ−3αi
⟩
− (qi −q−1
i )s2
i
⟨
x, Xµ−2αi
⟩
.
36 MARTINA BALAGOVI ´C AND STEF AN KOLB
Using the fact that σ(x) = −x we obtain from (2.22) and (2.19) that
σ(ri(ir(x))) = −ri(ir(x)), σ (ri(x) +ir(x)) = −(ri(x) +ir(x)).
By Lemma 6.6 the above relations imply that all terms in (6.22) vanish. T herefore
all summands in (6.20) vanish, which completes the proof of the Lemm a in the
second case. □
Remark 6.9. If one restricts to quantum symmetric pair coideal subalgeb rasBc,s
with s = (0, 0,..., 0) then Case 2 in the proof of Lemma 6.8 simpliﬁes signiﬁcantly
and Lemma 6.6 is not needed.
