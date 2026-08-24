---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-192-7112-birkhoﬀ-guenther-normal-form-there-is-a-uni
section_title: "Birkhoﬀ-Guenther normal form . — There is a unique α∈ C such"
section_number: 7.1.1.2
pages: 119-121
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
that, setting v := u− α, the unique formal solution of azσqf − f =
v is convergent. Indeed, putting v = ∑
k>>−∞
vkzk, from the relation
aqn−1fn−1− fn = vn, we draw that ∑
n∈Z
anq−n(n−1)/2vn = 0, which also
writes: α = Bq,1u(a−1), where, as usual (see deﬁnition 2.3.3, page 23),
Bq,1u(ξ) = ∑
k>>−∞
ukq−k(k−1)/2ξk. (The letter ξ is traditional for the Borel
plane.) Note that the value Bq,1u(a−1) is well deﬁned, for Bq,1u is an en-
tire function. The Birkhoﬀ-Guenther normal form of
(1 u
0 az
)
is therefore
(1 Bq,1u(a−1)
0 az
)
.
7.1.1.3. “Algebraic” summation . — For any a∈ C∗, we shall set:
θq,a(z) :=θq(z/a).
(See (1.3) in the general notations of section 1.3.) One look s for a solution
of (7.3) in the form f = g/θq,λ, with g∈O (C∗) and λ adequately chosen in
114 CHAPTER 7. EXAMPLES OF THE STOKES PHENOMENON
C∗. We are led to solve the equation: aλσqg−g = uθq,λ. Identifying the
coeﬃcients of the Laurent series, one gets the unique soluti on:
g =
∑
n∈Z
[uθq,λ]n
aλqn− 1zn,
which makes sense if, and only if, λ⁄∈[a−1;q]. (Note that we write [ h]n :=an
when h =∑ anzn.) Thus, for all “authorized directions of summation” λ, we
get the unique solution for (7.3) with only simple poles over [−λ;q]:
Sλ ˆf := 1
θq,λ
∑
n∈Z
[uθq,λ]n
aλqn− 1zn,
7.1.1.4. “True” summation . — Since the polar condition that uniquely char-
acterizes the solution Sλ ˆf only depends on λ :=λ (mod qZ)∈ Eq, or (equiv-
alently) on Λ := [λ;q], we shall also write:
Sλ
ˆf :=SΛ ˆf :=Sλ ˆf.
We now make this dependency explicit. From the equality uθq,λ =∑ ukq−ℓ(ℓ+1)/2zk(z/λ)ℓ, we draw:
[uθq,λ]n =
∑
k+ℓ=n
ukq−ℓ(ℓ+1)/2λ−ℓ =
∑
k
ukq−(n−k)(n−k+1)/2λk−n,
so that:
qn(n+1)/2λn [uθq,λ]n =
∑
k
ukqnk−k(k−1)/2λk =Bq,1u(qnλ).
On the other hand, iterating the relation θq,λ(z) = z
qλθq,qλ(z) yields θq,λ(z) =
zn
qn(n+1)/ 2λnθq,q nλ(z), whence:
Sλ
ˆf =SΛ ˆf =
∑
n∈Z
q−n(n+1)/2λ−nBq,1u(qnλ)
znq−n(n+1)/2λ−nθq,q nλ(z)(aλqn− 1) zn =
∑
µ∈Λ
Bq,1u(µ)
(aµ− 1)θq,µ(z) zn.
Remark 7.1.1 . — In [ 38, 39, 40 ], one computes the residue of the mero-
morphic function λ↦→Sλ
ˆf at the pole a−1∈ Eq. According to the above
formula, one ﬁnds:
Resλ=a−1Sλ
ˆf = 1
2iπ
Bq,1u(a−1)
θq(az) ·
Indeed, for anyb∈ C∗ and for any mapf : C∗→ C analytic in a neighborhood
of [b;q], setting:
∀λ∈ Eq , F
(
λ
)
:=
∑
µ∈[λ;q]
f(µ)
µ−b,
