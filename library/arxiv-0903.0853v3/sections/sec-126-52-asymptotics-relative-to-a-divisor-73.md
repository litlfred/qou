---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-126-52-asymptotics-relative-to-a-divisor-73
section_title: "ASYMPTOTICS RELATIVE TO A DIVISOR 73"
section_number: 5.2
pages: 79-79
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
Last, we note that the function t ↦→At|q|kt2/2 reaches its minimum at
t =− lnA
k ln|q|, with:
min
t∈R
At|q|kt2/2 =e− ln2 A
2k ln|q|.
From this, one deduces:
(5.6) min
m∈Z
Am|q|km2/2≤|q|
k
8 e− ln2 A
2k ln|q|
for all A > 0. Therefore, if we set A = µk|q|−n+k/2, we get the wanted
q-Gevrey estimates for|an|, which concludes the proof.
5.2. Asymptotics relative to a divisor
In this section, we ﬁx a divisor Λ := ν1[λ1] +··· +νm[λm] and we write
ν :=|Λ| =ν1 +··· +νm. Without loss of generality, we make the following
ASSUMPTION:
The complex numbers λi are pairwise distinct and such that:
(5.7) 1 ≤|λ1|≤| λ2|≤···≤| λm|<|qλ1|.
Deﬁnition 5.2.1 . — Let f ∈ BΛ . We write (2) f ∈ AΛ
q and we say that f
admits a q-Gevrey asymptotic expansion of level ν (or order s := 1/ν) along
divisor Λ at 0, if there exists a power series ∑
n≥0
anzn and constants C, A> 0
such that, for any ǫ > 0 and any integer N ≥ 0, one has, for some small
enough R> 0 and for all z∈S(Λ,ǫ ;R):
(5.8)
⏐
⏐
⏐
⏐
⏐
⏐
f(z)−
∑
0≤n<N
anzn
⏐
⏐
⏐
⏐
⏐
⏐
< C
ǫAN|q|N 2/(2ν)|z|N .
Recall that condition z∈S(Λ,ǫ ;R) means that 0 <|z|<R and dq(z, Λ)>
ǫ; see deﬁnition 5.1.4. One sees at once that, if f ∈ AΛ
q , its asymptotic
expansion, written J(f), belongs to the space of q-Gevrey series of level ν,
whence the following linear map:
J : AΛ
q → C[[z]]q;1/ν, f ↦→J(f).
(For the notation C[[z]]q;s, see paragraph 1.3.2 of the general notations, in the
introduction.) In section 5.3, we shall see that this map is o nto, providing a
