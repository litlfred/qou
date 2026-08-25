---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-019-5-asaieisenstein-elements-in-higher-weights
section_title: "Asai–Eisenstein elements in higher weights"
section_number: 5
pages: 26-26
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
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
