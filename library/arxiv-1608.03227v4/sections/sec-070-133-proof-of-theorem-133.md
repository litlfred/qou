---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-070-133-proof-of-theorem-133
section_title: "Proof of theorem 13.3"
section_number: 13.3
pages: 75-78
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
β as a product of the elementary braids. Let us explain why Hk(β) actually only depends only conjugacy
class of β. First let us notice that because of the equality (13.61) we have a construction for Hk(β) as
hyper-cohomology of the complex on X1,fc:
Hk(β) = H(ΛkB ⊗Cβ),
here B is the vector bundle over X1,fc with ﬁber over (X, g, Y, v) equal V .
Thus given a presentation β = σǫ1
i1 · · · · · σǫℓ
iℓwe have
Hk(β) = H(Λkπ∗
1(B) ⊗CEnℓ(π∗
12(Cσǫ1
i1 ) ⊗. . . π∗
ℓ,1(Cσ
ǫℓ
iℓ))).
where πij : Xℓ,fc →X2,fr are the natural projections. The LHS of the last formula only depends on the
cyclic order of the elements σǫk
ik , because the space Xℓ,fc has Zℓcyclic symmetry and the group element
gi,i+1 provides an isomorphism of the vector bundles π∗
i (B) and π∗
i+1(B) for all i. Hence we showed that
Hk(β) only depends on the conjugacy class of β.
To complete our proof we need to show that
(13.62)
Hk(β · σ1) = Hk(β′),
Hk(β · σ−1
1 ) = Hk−1(β′)
for β′ ∈Brn−1 and β = 1 ⊠β′ ∈Brn is the inclusion of β′ in the braid with n strings in a such way it
tangles only the last n −1 strings.
Next we can use proposition 8.3 to conclude:
Hk(β · σ±1
1 ) = H(fgt∗(CEn(cl∗(¯π13∗(CEnn(¯π12 ⊗Bn ¯π23)∗( ¯Cβ ⊠¯Cσ±1
1 ))Tn))Tn ⊗ΛkB)
= H(fgt∗(CEn(cl∗(¯π13∗(CEn2(¯π12 ⊗B2 ¯π23)∗( ¯Cβ ⊠¯Cσ±1
1 ))T2))Tn ⊗ΛkB)
Thus we have shown that
Hk(β · σ±1
n−1) = H(fgt∗(CEn⊕n2(j∗
e (¯π12 ⊗B2 ¯π23)∗( ¯Cβ ⊠¯Cσ±1
1 ))Tn×T2 ⊗∧kBn),
where je : b × G2 × n →X 3(Gn, Gn,n−1) is the embedding that identiﬁes b × G2 × n with the subvariety of
X 3(Gn, Gn,n−1) deﬁned by the equation je(X, g, Y ) = (X, g−1, g, Y ).
75
Let us simplify the complex (j∗
e (¯π12 ⊗B2 ¯π23)∗( ¯Cβ ⊠¯Cσ±1
1 ) ∈MFsc
Bn×B2(b × G2 × n, 0).
Since ¯Cβ =
indn−1(1 ⊗¯Cβ′) ∈MFsc
B2(X 2, W) it has the following description
¯Cβ = (M ⊗Λ∗V, D + d+ + d−, ∂l, ∂r) ∈MFsc
B2(X 2, W),
where V
= Cn−1 = ⟨θ2, . . . , θn⟩; (M, D) ∈Modper(X 2) such that D2 = W modulo ideal In−1 =
(g12, . . . , g1n) ⊂C[X 2]; d+ = Pn
i=2 g1iθi and d−= P⃗
i d−⃗
i
∂
∂θ⃗i ; ∂l, ∂r deﬁne equivariant structure such
that (M, D, ∂l, ∂r) modulo the ideal In−1 is an equivariant matrix factorization p∗
1( ¯Cβ′).
As we explained previously in the subsection 5.5 conjugation by exp(φ ∂
∂θ2 ) of the diﬀerential of (¯π12 ⊗B2
¯π23)∗( ¯Cβ ⊠¯Cσ±1
n−1) results in the row transformation of of the ﬁrst type. Using these transformations we
can obtain a complex C′ that is homotopic to (¯π12 ⊗B2 ¯π23)∗( ¯Cβ ⊠¯Cσ±1
n−1) and the only dependence of it
diﬀerentials on g12 comes from the term g12θ2 of d+. Then we can contract C′ along the diﬀerential g12θ2 to
obtain a homotopy equivalence
(¯π12 ⊗B2 ¯π23)∗( ¯Cβ ⊠¯Cσ±1
n−1) ∼C′′ ∼( ¯Cβ,12 ⊗¯π∗
23( ¯C±)),
where the last complex is the complex of C[b × B2 × Gn × n]-modules and ¯Cβ,12 ∈MFsc
B×B2(b × B2 × n, 0) is
the matrix factorization deﬁned by the data
¯Cβ,12 = (j∗
12(M) ⊗Λ∗V12, d+
12 + j∗
12(D + d+ + d−), j∗
12(∂l), j∗
12(∂r)),
where j12 : b × B2 × Gn × n →b × G2 × Gn × n is the embedding; V12 = ⟨θ3, . . . , θn⟩and d+
12 = Pn
i=3 g1iθi.
Next note that since CEn2(C[B2])T2 = C there is a homotopy equivalence
CEn2(j∗
e (¯π12 ⊗B2 ¯π23)∗( ¯Cβ ⊠¯Cσ±1
n−1))T2 ∼j∗
e,e( ¯C12,β ⊗¯π∗
23( ¯C±))
= j∗
e,e( ¯Cβ,12) ⊗j∗
e,e(¯π∗
23( ¯C±)),
where je,e : b × 1 × 1 × n →n × B2 × Gn × n. Below we analyze two terms in the last tensor product.
Let us notice that ¯C±|g=1 = [x11 −x22, 0]± where where [x11 −x22, 0]+ = [x11 −x22, 0] and [x11 −
x22, 0]⟨−1⟩.Thus we obtain
j∗
e,e(¯π∗
23( ¯C+)) = [x11 −x22, 0]+ := [x11 −x22, 0],
j∗
e,e(¯π∗
23( ¯C−)) = [x11 −x22, 0]−:= [x11 −x22, 0] ⊗χ−1
n .
Let us denote by p the natural projection map bn × nn →bn−1 × nn−1 that gives the map p : ﬁ
Hilb
free
1,n
→
ﬁ
Hilb
free
1,n−1 when restricted to the stable locus. The key observation about the other term in the last tensor
product of the matrix factorization is that it contains a sub complex p∗(j∗
e ( ¯Cβ′)) = (M ′, D′, ∂′
l +∂′
r), ∂′
l +∂′
r :
M ′ ⊗Λ•(nn−1) →M ′ ⊗Λ<•(nn−1)
j∗
e,e( ¯C12,β) = (M ′ ⊗Λ•V12, D′ + d′
−, ∂′
l + ∂′
r + ∂f)
where d′
−= j∗
e,e(j∗
12(d−)) and
∂f + ∂′
l + ∂′
r : M ′ ⊗Λ•(nn) ⊗Λ∗V12 →M ′ ⊗Λ<•(nn) ⊗Λ∗V12,
with (M ′ ⊗Λ•(nn−1), ∂′
l +∂′
r)⊗Λ∗V12 being a sub complex of (M ′ ⊗Λ•(nn)⊗Λ∗V12, ∂f +∂′
l +∂′
r). Moreover
∂f has a non-trivial degree along with respect to the exterior power Λ∗V12:
∂f : M ′ ⊗Λ∗(nn) ⊗Λ•V12 →M ′ ⊗Λ∗(nn) ⊗Λ<•V12,
76
We complete our argument with an analysis of spectral sequence for the diﬀerential Dtot = (D′ + ∂′
l +
∂′
r) + dce + dc + ∂f + d′
−by ﬁrst computing homology with respect to dce then with respect to dc, we give
details below.
Let us summarize the previous discussion, we have shown that
Hk(β · σ±1
1 ) = H(M ′ ⊗V12 ⊗[x11 −x22, 0]± ⊗ΛkBn, Dtot),
Dtot = (D′ + ∂′
l + ∂′
r) + (dce + dc + ∂f + d′
−).
In the total diﬀerential Dtot the term dc is the Cech diﬀerential for some Cech cover of ﬁ
Hilb1,n.
In
particular, if we choose Cech cover of ﬁ
Hilb
free
1,n
by the aﬃne varieties U⃗S1,⃗S2 = B · A⃗S1,⃗S2 from the proof of
proposition 13.1, we can derive from fact that B-action on U⃗S1,⃗S2 is free that
Hk(C[U⃗S1,⃗S2], dce) =



C[T · A⃗S1,⃗S2], if k = 0
0, if k > 0.
.
Thus we can conclude that H(β · σ±1
1 ) is equal to
H(Hilbfree
1,n , (M ′ ⊗V12 ⊗[x11 −x22, 0]±)B ⊗ΛkBn, (D′ + ∂′
l + ∂′
r) + dc + ∂f + d′
−).
where superscript B indicate the descend of the complex to the quotient ﬁ
Hilb
free
1,n /B = Hilbfree
1,n .
Let ∆1,2 ⊂h be the root hyperplane for the root ǫ1 −ǫ2 and Hilbfree
1,n (∆1,2) := χ−1(∆1,2). By contracting
the diﬀerential of the complex [x11 −x22, 0] we obtain the last simpliﬁcation for Hk(β · σ±1
1 ):
H(Hilbfree
1,n (∆1,2), (M ′ ⊗Λ∗V12 ⊗χ−1/2±1/2
n
)B ⊗ΛkBn, (D′ + ∂′
l + ∂′
r) + dc + ∂f + d′
−).
Let us present the torus Tn of Bn as a product T1 × Tn−1 where T1 is the one-dimensional torus that
preserves Bn−1 and Tn−1 is the torus of Bn−1.
Hence the torus T1 acts non-trivially on the ﬁbers of
p : ﬁ
Hilb
free
1,n
→ﬁ
Hilb
free
1,n−1 and Tn−1 ﬁxes these ﬁbers.
As the ﬁnal step we push forward the last complex along the morphism p. For that let us observe that
the elements θ3, . . . , θn have weight −1 with respect to T1 and 0 with respect to Tn−1 thus
(Λ∗V12)B = Λ∗On(−1)⊕n−2.
Since χ−1
n descends to On(−1) we can use proposition 13.2 to conclude that for the map p : Hilbfree
1,n (∆n,n−1) →
Hilbfree
1,n
we have
p∗(∧kBn ⊗Λ∗(V12)B) = ∧kBn−1,
p∗(∧kBn ⊗On(−1) ⊗Λ∗(V12)B) = ∧k−1Bn−1[n].
Since (M ′, D′, ∂′
l + ∂′
r) = p∗(je( ¯Cβ′)) and both ∂f and d′
−have non-trivial degree along the exterior power
Λ∗V12 we can apply the projection formula to conclude
Hk(β · σ1) = H(Hilbfree
1,n−1, j∗
e( ¯Cβ′) ⊗ΛkBn−1),
Hk(β · σ−1
1 ) = H(Hilbfree
1,n−1, j∗
e( ¯Cβ′) ⊗Λk−1Bn−1[n]).
The last formula implies the desired equation (13.62).
77
