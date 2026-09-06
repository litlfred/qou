---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-019-22-the-kazhdan-lusztig-basis-the-hecke-algebra-i
section_title: "The Kazhdan-Lusztig basis. The Hecke algebra is equipped with a /CI -linear bar"
section_number: 2.2
pages: 14-15
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
involution, denoted h ↦→h and uniquely speciﬁed as an algebra homomorphism by
v ↦→v−1 andHs ↦→H −1
s . A simple calculation shows that Hs +v =H −1
s +v−1, so that
the elementH s =Hs +v is bar-invariant.
SOERGEL CALCULUS 15
Theorem 2.3. (Kazhdan-Lusztig [KL79]) There exists a unique basis {H w}w∈W of H as a
Z[v±1]-module, called the Kazhdan-Lusztig basis, which satisﬁes:
• H w =H w;
• H w =Hw + ∑
x<whx,wHx wherehx,w ∈vZ[v].
The polynomialshx,w ∈ Z[v] are Kazhdan-Lusztig polynomials.
Remark 2.4. In this paper we follow the normalization of Soergel [Soe97] rather than
the original normalization of [KL79]. In particular, the Ka zhdan-Lusztig polyno-
mials Px,w in [KL79] are related to the Kazhdan-Lusztig polynomials ab ove by the
formula
hx,w =v2(ℓ(w)−ℓ(x))Px,w(v−2).
Givenw = s1s2...s m we set H w
def= H s1...H sm. Note that H w ⁄= H w in general,
but equality does hold when ℓ(w) ≤ 2 ands1 ⁄=s2.
An element w ∈ W is called (rationally) smooth if H w = ∑
y≤wvℓ(w)−ℓ(y)Hy. The
longest element of any ﬁnite parabolic subgroup is smooth. A ny element of a rank 2
parabolic subgroup is smooth.
We pause to present three conjectures of Kazhdan and Lusztig :
Conjecture 2.5. The polynomialshx,y have positive coefﬁcients, i.e. they lie in Z≥0[v].
Conjecture 2.6. The structure coefﬁcients of the Kazhdan-Lusztig basis H are positive. In
other words,H uH v = ∑ cw
u,vH w for somecw
u,v ∈ Z≥0[v,v −1].
These ﬁrst two conjectures are commonly referred to as the Kazhdan-Lusztig posi-
tivity conjectures. The following conjecture is the Kazhdan-Lusztig conjecture. It and its
many generalizations account to a large extent for the inter est in Kazhdan-Lusztig
polynomials. (For a precise statement of the Kazhdan-Lusztig conjecture see [KL79].)
Conjecture 2.7. (The Kazhdan-Lusztig Conjecture) If W is the Weyl group of a complex
semi-simple Lie algebra, then the Kazhdan-Lusztig polynom ials give the multiplicities of
simple modules in Verma modules in the principal block of cat egory O.
These three conjectures are themselves implications of the Soergel conjecture. We
will discuss this in section 3.5.
