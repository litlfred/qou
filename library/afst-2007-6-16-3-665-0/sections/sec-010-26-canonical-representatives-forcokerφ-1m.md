---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-010-26-canonical-representatives-forcokerφ-1m
section_title: "(Canonical representatives forcoker(Φ −1,M"
section_number: 2.6
pages: 20-21
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
global)).—
Let M be a pure diﬀerence module overK with slope −t/n and n,t /greaterorequalslant1,
g.c.d.(t,n) = 1. As in the proof of Theorem 2.5, one writesMglobal =
C[z1/n,z −1/n] ⊗W with Φ action given by Φ(f ⊗w)= z−t/nφ(f) ⊗A(w).
One requires that|q|1/n < |c| ⩽1 for every eigenvalue ofA. This makes the
presentation unique.
DeﬁneW + := (C1+ Cz1/n + ··· + Cz(t−1)/n) ⊗W. We claim that
W + →coker(Φ −1,Mglobal) is a bijection.
Indeed, writew+ ∈W + asw+ = ∑t−1
i=0 zi/n ⊗wi. Thenw+ lies in the image
ofΦ −1ifandonlyifforall k0 ∈{0,1,...,t −1}onehas ∑
s∈Zqm(k0,s)wk0+st
= 0. This implies thatw+ = 0. Hence W + → coker(Φ − 1,Mglobal)i s
injective. Since both spaces have dimensiont·dimW, the map is a bijection.
For anyC-linear operatorT on M, one writesEigen(T,c) for the gen-
eralized eigenspace of T for the eigenvaluec ∈ C.T h u sEigen(T,c)=⋃
s/greaterorequalslant1 ker((T −c)s,M). With this notation one observes that
W += ⊕|q|t/n<|c|⩽1Eigen(zt/nΦ,c) andW += ⊕|q|t<|c|⩽1Eigen((zt/nΦ)n,c).
We writeRepr(Mglobal)o rRepr(M) for the vector spaceW + of repre-
sentative of coker(Φ−1,M). We note thatRepr(M) does not depend on
the choice of the moduleN overKn withM =Res(N).
M ↦→Repr(M) has some functorial properties, namely:
A morphismf :M1 →M2 between pure modules of the same negative slope
maps Repr(M1) to Repr(M2).
This follows easily from the second description ofW +.
– 683 –
Marius van der Put, Marc Reversat
LetM1,M 2 denote pure modules of slopesλ1,λ 2 <0. Then
Repr(M1) ⊗CRepr(M2) is mapped toRepr(M1 ⊗M2) ⊂M1 ⊗M2.
Theproofgoesasfollows.Thepuremodule M3 :=M1 ⊗KM2 hasslope λ3 =
λ1+λ2.Chooseaninteger n /greaterorequalslant1suchthat nλ1,nλ 2 ∈ Z.Foreach i=1,2,3,
thevectorspace Repr(Mi)isequalto ⊕|q|−nλi<|c|⩽1Eigen((z−λiΦ)n,c).The
statementthatwewanttoprovefollowsfrom( zλiΦ)n=q−λin(n−1)/2z−nλiΦn
and the observation thatq−λ3n(n−1)/2z−nλ3Φn(w1 ⊗w2) equals
q−λ1n(n−1)/2z−nλ1Φn(w1) ⊗q−λ2n(n−1)/2z−nλ2Φn(w2)
forw1 ∈Repr(M1),w 2 ∈Repr(M2).
Thereisasecondmethod,basedonsubsection1.4.1,todeﬁneasubspace
of representatives for coker(Φ− 1,N) with N pure of slopeλ< 0. Let
data(N)=( λ,V,A, {D(σ)}) andK∞ ⊗N =K∞ ⊗C V. Then
V + :=
∑
s∈Q, 0⩽s<−λ
zs ⊗V
can be seen to be a vector space of representative for coker(Φ−1,K ∞ ⊗V).
This set of representatives is invariant under the action ofGal and therefore
Repr∗(N): =(V +)Gal (depending on the choice ofL ⊂ C)i sa C-subspace
of Nglobal representing coker(Φ − 1,N). Again N ↦→Repr∗(N) has the
same functorial properties asM ↦→Repr(M). However the behaviour of
Repr∗(N) with respect to tensor products is more transparent.
