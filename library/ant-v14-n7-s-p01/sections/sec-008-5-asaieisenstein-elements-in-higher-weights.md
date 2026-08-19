---
doc_id: ant-v14-n7-s-p01
doc_title: "p-adic Asai L-functions of Bianchi modular forms David Loeﬄerand Chris Williams The Asai (or twisted tensor) L-function of a Bianchi modular form9 is the L-function attached to the"
section_id: sec-008-5-asaieisenstein-elements-in-higher-weights
section_title: "Asai–Eisenstein elements in higher weights"
section_number: 5
pages: 24-27
source_pdf: ant-v14-n7-s-p01.pdf
source_sha256: 976199bfca4ac086
doc_brief: "p-adic Asai L-functions of Bianchi modular forms David Loefflerand Chris Williams The Asai (or twisted tensor) L-function of a Bianchi modular form9 is the L-function attached to the tensor induction"
---
In the previous sections, we have deﬁned compatible systems of classes in the Betti cohomology of
the spaces Y∗
F,1(n) with trivial coefﬁcients. We now extend this to coefﬁcients arising from nontrivial
algebraic representations.
We ﬁx, for the duration of this section, a prime p and a ﬁnite extension L of Qp large enough that F
embeds into L (and we ﬁx such an embedding). We let R be the ring of integers of L. We also choose an
ideal n of OF divisible by all primes above p. For convenience, we also assume that n is divisible by
some integer q> 4; note that this is automatic if p is unramiﬁed in F and p> 5.
5A. Coefﬁcients and moment maps. As above, we let Vk(R)= Symk R2 be the left R[GL2(Z)]-module
of symmetric polynomials in 2 variables with coefﬁcients in R. We will be interested in the dual
Tk(R)= Vk(R)∗ (the module of symmetric tensors of degree k over R2). We view this as a local system
of R-modules on YQ,1(N), for any N> 4, in the usual way.
Similarly, we have R[GL2(OF)]-modules Vkk(R)= Symk R2⊗(Symk R2)σ , where GL2(OF) acts on
the ﬁrst factor via the given embeddingOF↪→ R and on the second via its Galois conjugate. We letTkk(R)
be the R-dual of Vkk(R). These give local systems on Y∗
F(U) and YF(U) for sufﬁciently small levels U.
The linear functional dual to the second basis vector of R2 deﬁnes a 0∗
F,1(npr)-invariant linear
functional on Symk(R/pr)2, or on(Symk(R/pr)2)σ, and hence an invariant vector in Tkk(R/pr)). This
can be seen as a section of the corresponding local system, deﬁning a class
eF,k,r∈ H0(
Y∗
F,1(npr), Tkk(R/pr)
)
.
Since R is p-adically complete, cup-product with this section deﬁnes a “moment” map
momkk: lim←−−t
H•(Y∗
F,1(npt), Z)⊗ R→ H•(Y∗
F,1(n), Tkk(R)).
This is the Betti cohomology analogue of the moment maps in étale cohomology of modular curves
considered in [Kings et al. 2017, §4].
By Lemma 3.12, the family of classes (8k,r
npt,a)t>0 is compatible under pushforward, so it is a valid
input to the maps mom kk (after base-extending from R to the group ring R[(Z/pr)×]).
Deﬁnition 5.1. We let c8k,r
n,a∈ H2(
Y∗
F,1(n), Tkk(R)
)
⊗R R[(Z/pr)×] be the image of the compatible
system(8k,r
npt,a)t>0 under momkk .
The action of the Hecke operator(Up)∗ is well-deﬁned both on H2(
Y∗
F,1(n), Tkk(R)
)
and on the inverse
limit lim←−−t H2(
Y∗
F,1(npt), Zp
)
, and the maps momkk commute with this operator; see [Kings et al. 2017,
Remark 4.5.3]. So we deduce immediately from Theorem 3.13 that the classes c8k,r
n,a, for any ﬁxed k> 1
and varying r, satisfy the same norm-compatibility relation as the k= 0 classes.
5B. Relation to the weight 2k Eisenstein class. We will later relate the c8k,r
n,a to values of L-functions.
For this purpose the deﬁnition above, via a p-adic limiting process, is inconvenient; so we now give
p-adic Asai L-functions of Bianchi modular forms 1693
an alternative description of the same classes via higher-weight Eisenstein series for GL2/Q, directly
generalising the classes obtained in weight 2 from realisations of Siegel units.
Let k> 0. The local system Tk(C) is exactly the ﬂat sections of a vector bundle Tk,dR with respect to a
connection∇ (the Gauss–Manin connection). The vector bundle Tk,dR is algebraic over Q, and there is a
comparison isomorphism
H1(YQ,1(N), Tk(Q))⊗ C∼= H1
dR(YQ,1(N), Tk,dR)⊗Q C. (5-1)
Moreover, the pullback of Tk,dR to the upper half-plane is the k-th symmetric tensor power of the relative
de Rham cohomology of C/(Zτ+ Z), so it has a canonical section(dw)⊗k, wherew is a coordinate on C.
Proposition 5.2. There exists a class Eisk
N∈ H1(YQ,1(N), Tk(Q)) whose image under the comparison
isomorphism (5-1) is the class of the differential form
−N k F(k+2)
1/N (τ) dw⊗k dτ.
Proof. By [Beilinson and Levin 1994], there exists a motivic Eisenstein class
Eisk
mot,N∈ H1
mot
(
YQ,1(N), Tk,mot(k+ 1)
)
,
where Tk,mot is a relative Chow motive overY1(N) with coefﬁcients in Q (cut out by a suitable idempotent
inside the relative motive of the k-fold ﬁbre product of the universal elliptic curve over Y1(N)).
This motivic cohomology group admits a realisation map rdR to H1
dR(YQ,1(N), Tk,dR), and Eisk
dR,N:=
rdR(Eisk
mot,N) is given by the class of the differential form
−N k(2πi)k+1F(k+2)
1/N (τ) dw⊗k dτ.
(This is a restatement of a result of [Beilinson and Levin 1994], but we refer to [Kings et al. 2020,
Theorem 4.3.3] for the statement in this particular form.) There is also a Betti realisation map
rB: H1
mot
(
YQ,1(N), Tk,mot(k+ 1)
)
→ H1(YQ,1(N), Tk(Q)(k+ 1)),
where the twist(k+1) in Betti cohomology denotes tensor product with Q(k+1)=(2πi)k+1Q⊂ C; and
these two realisations are compatible under the comparison isomorphism (5 -1); see [Kings et al. 2020,
§2.2]. Identifying Q(k+ 1) with Q in the obvious manner, we obtain a class Eisk
N∈ H1(YQ,1(N), Tk(Q))
whose image under the comparison isomorphism (5-1) is (2πi)−(k+1) Eisk
dR,N , as required. □
Via base-extension, we can consider Eisk
N as a class in H1(YQ,1(N), Tk(Qp)). This class does not
generally lie in the lattice H1(YQ,1(N), Tk(Zp)); but for any c > 1 as above, there exists a class
c Eisk
N∈ H1(YQ,1(N), Tk(Zp)) such that the equality
c Eisk
N=
(
c2− c−k⟨c⟩
)
Eisk
N
holds in H1(YQ,1(N), Tk(Qp)). (This follows from Kings’ theory of p-adic interpolation of Eisenstein
classes [2015]; see [Kings et al. 2017, Theorem 4.4.4].)
1694 David Loeﬄer and Chris Williams
Letting R be as in the previous section, for any j∈{ 0,..., k} we can regard T2k−2 j(R) as a SL2(Z)-
invariant submodule of the SL2(OF)-module Tkk(R), via the Clebsch–Gordan map
CG[k,k, j]: T2k−2 j(R)→ Tkk(R) (5-2)
(normalised as in [Kings et al. 2020, §5.1]). Thus we obtain a map
(ιm,n,a)∗◦ CG[k,k, j]: H1(
YQ(m, m N), T2k−2 j(Zp)
)
⊗Zp R→ H2(
Y∗
F(m, mn), Tkk(R)
)
.
Deﬁnition 5.3. Let c4k, j
m,n,a∈ H2(
Y∗
F,1(n), Tkk(R)
)
be the image of(ιm,n,a)∗ CG[k,k, j](
c Eis2k−2 j
m N
)
under
restriction to the identity component followed by (sm)∗. We similarly write 4k, j
m,n,a (without c) for the
analogous element with L-coefﬁcients, deﬁned using Eis k
m N.
This deﬁnition is convenient for p-adic interpolation, but to relate this element to special values it is con-
venient to have an alternative description involving pushforward along the mapκa/m:Y∗
F,1(m2n)→Y∗
F,1(n),
as above. (Note that if p| m, this pushforward map only acts on cohomology with coefﬁcients in Tkk(L),
not Tkk(R), since it corresponds to the action of a matrix whose entries are not p-adically integral.)
Lemma 5.4. As elements of H2(
Y∗
F,1(n), Tkk(L)
)
we have
4k, j
m,n,a= m j·(κa/m)∗
(
ι∗CG[k,k, j](Eis2k−2 j
m2 N )
)
.
Proof. This follows from the deﬁnition of c4k, j
m,n,a above in exactly the same way as Proposition 4.4
(which is the case j= k= 0), noting that the Clebsch–Gordan maps at levels Y∗
F(m, mn) and Y∗
F,1(m2n)
differ by the factor m j; compare the proof of [Kings et al. 2017, Theorem 5.4.1]. □
Proposition 5.5. For any r> 0 we have
c8k,r
n,a=
∑
t∈(Z/pr)×
c4k,0
pr,n,at⊗[ t]=
(
c2− c−2k[c]2⟨c⟩
)
·
∑
t∈(Z/pr)×
4k,0
pr,n,at⊗[ t],
where the ﬁrst equality takes place in H2(Y∗
F,1(n), Tkk(R))⊗R R[(Z/pr)×] and the second after base-
extension to L.
Proof. This proposition is very close to [Kings et al. 2017, Proposition 5.1.2] so we only brieﬂy sketch
the proof. There is a GL2/Q moment map momk for any k> 0, and one sees easily that the maps momk
and momkk are compatible via the inclusion YQ,1(N)↪→ Y∗
F,1(n). However, the main theorem of [Kings
2015] shows that the higher-weight Eisenstein classes are exactly the moments of the family of Siegel-unit
classes cCN p∞, up to a factor depending on c. □
There is an analogous statement for j⁄= 0, but this can only be formulated after reduction modulo pr:
Proposition 5.6. For r> 1, as classes in H2(Y∗
F,1(n), Tkk(R/pr)) we have
c4k, j
pr,n,a=(a− aσ) j j!
( k
j
)2
c4k,0
pr,n,a.
Proof. The proof of this proposition is identical to the corresponding statement for étale cohomology of
Hilbert modular varieties, which is Corollary 8.1.5 of [Lei et al. 2018]. □
p-adic Asai L-functions of Bianchi modular forms 1695
