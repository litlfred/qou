---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-006-2b-locally-symmetric-spaces
section_title: "2B. Locally symmetric spaces"
section_number: null
pages: 7-9
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Deﬁnition 2.1. Let G be the algebraic group ResF/QGL2 over Q, and let G∗ be the subgroup G×D Gm,
where D:= ResF/QGm and the map G→ D is determinant.
(Compare [Lei et al. 2018, Deﬁnition 2.1.1] in the totally real case.)
Deﬁnition 2.2. We deﬁne locally symmetric spaces attached to the groups GL 2, G and G∗ as follows:
• If U⊂ GL2(A f
Q) is an open compact subgroup, we set
YQ(U):= GL2(Q)+\[GL2(A f
Q)× H]/U,
where GL2(Q)+ acts from the left on both factors in the usual way, and U acts on the right of
GL2(A f
Q).
• If U⊂ G(A f
Q)= GL2(A f
F) is open compact, we set
YF(U):= GL2(F)\[GL2(A f
F)× H3]/U.
1674 David Loeﬄer and Chris Williams
• If U⊂ G∗(A f
Q)=
{
g∈ GL2(A f
F): det(g)∈(A f
Q)×}
is open compact, we set
Y∗
F(U):= G∗(F)+\[G∗(A f
Q)× H3]/U,
where G∗(F)+={ g∈ G∗(F): det(g)> 0} is the intersection of G∗(F) with the identity component
of G∗(R).
Each of these spaces has ﬁnitely many connected components, each of which is the quotient of H or H3
by a discrete subgroup of PSL2(R) (resp. PGL2(C)). If U is sufﬁciently small, these discrete subgroups
act freely, so in particular the quotient is a manifold.
Deﬁnition 2.3. Let K be either Q or F, and m, n, a be ideals in OK . We deﬁne:
(i) UK(m, n):=
{
γ∈ GL2(ˆOK):γ≡ I mod
(m
n
m
n
)}
,
(ii) UK(m(a), n):=
{
γ∈ GL2(ˆOK):γ≡ I mod
(m
n
ma
n
)}
,
We write YK(m, n):= YK(U(m, n)) and similarly YK(m(a), n). We will be particularly interested
YK(m, n) for m=(1), which we abbreviate as YK,1(n).
In the case K= F, we write U∗
F(m, n), U∗
F(m(a), n), U∗
F,1(n) for the intersections of the above groups
with G∗.
Example 2.4. The following three locally symmetric spaces are of particular importance in the sequel,
so here we describe them explicitly (and record some of their other basic properties) for later reference.
(i) YQ,1(N) is the usual (open) modular curve of level 01(N). It has one connected component,
isomorphic to01(N)\H.
(ii) The space Y∗
F,1(n) also has a single connected component, isomorphic to 0∗
F,1(n)\H3, where
0∗
F,1(n):= G∗(F)+∩ U∗
F,1(n)=
{( a
c
b
d
)
∈ SL2(OF): c= 0, a= d= 1 mod n
}
.
(iii) Since det(UF,1(n))=ˆO×
F, the space YF,1(n) has h F connected components, where h F is the class
number of F. The identity component is isomorphic to 0F,1(n)\H3, where
0F,1(n):= GL2(F)∩ UF,1(n).
If N= n∩ Z, then there are natural maps
YQ,1(N) ι→ Y∗
F,1(n) → YF,1(n)
induced by the natural maps H↪→ H3 and GL2(A f
Q)↪→ G∗(A f
Q)↪→ G(A f
Q). The map ι is injective in
most cases:
Proposition 2.5. If n is divisible by some integer q> 4, then Y∗
F,1(n) is a smooth manifold, and
ι: YQ,1(N)↪→ Y∗
F,1(n)
is a closed immersion.
p-adic Asai L-functions of Bianchi modular forms 1675
Proof. First, the smoothness assertion. It sufﬁces to prove that 0∗
F,1(n) has no nontrivial torsion elements.
Since0∗
1(n) is a subgroup of SL2(OF), any torsion elementγ must have eigenvaluesζ,ζ−1 whereζ is a
(nontrivial) root of unity, deﬁned over an extension of F of degree at most 2. Since ζ+ζ−1= a+ d=
2 mod n, we conclude that n dividesζ+ζ−1− 2. A case-by-case check shows that this implies ζ has
order 2, 3, 4 or 6, and n must contain one of the integers 1, 2, 3.
Let us now prove the injectivity assertion. Let z, z′∈ H3 be such that γ z= z′, for some γ∈0∗
1(n).
Thenγ−1γ z= z, so eitherγ−1γ= id, orγ−1γ is a nontrivial torsion element in SL2(OF). Sinceγ is
upper-triangular modulo some integer q> 4, the same is true of γ and thus also ofγ−1γ ; but we have
just seen that0∗
F,1(q) has no torsion elements for q> 4.
We can therefore conclude that γ−1γ= id, in other words that γ∈0∗
F,1(n)∩ SL2(Z)=0Q,1(N).
Hence z= z′ as elements of YQ,1(N). □
Remark 2.6. Henceforth, we will always assume that n is divisible by such a q, or, more generally, is
small enough to avoid the possibility that these spaces are (nonsmooth) orbifolds.
In contrast, the composition ◦ι is never injective, since
(−1
0
0
1
)
∈01(n) preserves the image of H3 in
H, and acts on H by x+ iy↦→− x+ iy , so the points−x+ iy and x+ iy of YQ,1(N) (which are distinct
for generic x, y) are identiﬁed when mapped to YF,1(n). This failure of injectivity is a key reason for
introducing the space Y∗
F,1(n). In fact, one can see directly that:
Proposition 2.7. The map: Y∗
F,1(n)→ YF,1(n) has image equal to the identity component0F,1\H3. Its
ﬁbres are the orbits of the ﬁnite group
{(ϵ
0
0
1
)
:ϵ∈ O×
F
}
acting on0∗
F,1\H3.
