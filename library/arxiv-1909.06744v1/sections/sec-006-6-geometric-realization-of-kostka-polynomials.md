---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-006-6-geometric-realization-of-kostka-polynomials
section_title: "§6. Geometric realization of Kostka polynomials"
section_number: null
pages: 7-9
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
toc_source: inferred
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spaces."
---
§6. Geometric realization of Kostka polynomials
In this section, we will discuss the relationship between Kostka polynomials and
the theory of the Springer correspondence in the case of GLn. In [L2], Lusztig gave a
geometric realization of Kostka polynomials in terms of the intersection cohomology
associated to unipotent classes in GLn. First we review the deﬁnition of Kostka
polynomials.
Consider x = (x1, x2, . . . , ) inﬁnitely many variables, and t another parameter.
Let Λ(x) = Λ = L
n≥0 Λn be the ring of symmetric functions, where Λn is the n-th
homogeneous part, and consider Λ[t] = Λ ⊗Z Z[t], the ring over Z[t]. For λ ∈Pn,
one can consider the Schur function sλ(x) ∈Λn and the Hall-Littlewood function
Pλ(x; t) ∈Λn[t] = Λn ⊗Z Z[t]. {sλ(x) | λ ∈Pn} and {Pλ(x; t) | λ ∈Pn} give
Z[t]-bases of Λn[t]. Thus one can deﬁne the Kostka polynomial Kλ,µ(t) ∈Z[t] by
the condition that
(6.1)
sλ(x) =
X
µ∈Pn
Kλ,µ(t)Pµ(x; t).
Here we introduce two combinatorial objects. For λ, µ ∈Pn, write them as
λ = (λ1, . . . , λk), µ = (µ1, · · · , µk) with λi, µi ≥0. We deﬁne a partial order λ ≤µ
on Pn, called the dominance order, by the condition that, for any 1 ≤j ≤k,
(6.2)
j
X
i=1
λi ≤
j
X
i=1
µi.
On the other hand, for λ ∈Pn, we deﬁne an n-function n : Pn →Z≥0 by
(6.3)
n(λ) =
k
X
i=1
(i −1)λi.
Then it is known that Kλ,µ(t) is a monic polynomial with deg Kλ,µ(t) = n(µ)−n(λ).
It follows that one can deﬁne a modiﬁed Kostka polynomial eKλ,µ(t) ∈Z[t] by
(6.4)
eKλ,µ(t) = tn(µ)Kλ,µ(t−1).
Let Oλ be the unipotent class in Guni corresponding to λ ∈Pn for G = GLn
as in Section 2. The following result shows that the closure relations of unipotent
classes in GLn can be described in terms of the dominance order on Pn.
(6.5.)
Oλ =
a
µ≤λ
Oµ
The following result gives a geometric realization of Kostka polynomials.
Theorem 6.1 (Lusztig [L2]). For λ ∈Pn, put Aλ = IC(Oλ, ¯Ql). Then
(i) H iAλ = 0 for odd i.
8
(ii) For x ∈Oµ ⊂Oλ, we have
(6.6)
eKλ,µ(t) = tn(λ) X
i≥0
(dim H 2i
x Aλ)ti.
In particular, Kλ,µ(t) ∈Z≥0[t].
In the case of GLn, Borho-MacPherson’s theorem gives a decomposition
(6.7)
π∗¯Ql[dim Guni] ≃
M
λ∈Pn
Vλ ⊗Aλ[dim Oλ].
By taking the stalk of the i-th cohomology on both sides of (6.7), and by comparing
them with Theorem 6.1 (ii), we obtain the interpretation of Ksotka polynomials in
terms of the Springer representations of Sn.
Corollary 6.2. For x ∈Oµ, we have
eKλ,µ(t) = tn(λ) X
i≥0
⟨H2i(Bx, ¯Ql), Vλ⟩Sn ti,
where ⟨, ⟩Sn is the inner product of characters of Sn.
Remark 6.3.
In the case of the Springer correspondence, only Springer represen-
tations of the top cohomology H2dx(Bx, ¯Ql) are involved. While, for the description
of the Kostka polynomials, all the Springer representations H2i(Bx, ¯Ql) are used.
§7. The enhanced variety GL(V ) × V
Later we discuss the theory of the Springer correspondence for the exotic sym-
metric space associated to symplectic groups. The enhanced variety is an extension
of GLn, and is also regarded as a degenerate form of the exotic symmetric space, and
was studied extensively by Achar-Henderson [AH] and Finkelberg-Ginzburg-Travkin
[FGT]. So we will start from the exposition on the enhanced variety.
Let G = GL(V ) ≃GLn with dim V = n.
We consider the direct product
X = G × V , on which G acts as g : (x, v) 7→(gxg−1, gv), where gv is the natural
action of G on V . The role of Guni is played by Xuni = Guni×V , which is a G-invariant
closed subset of X. The varieties X,Xuni are called the enhanced varieties.
Let Pn,2 be the set of double partitions λ = (λ′, λ′′) such that |λ| = |λ′|+|λ′′| =
n. The following result is known by Achar-Henderson and Travkin. The ﬁniteness
of the G-orbits is crucial for later discussion.
Lemma 7.1. Let Xuni/∼G be the set of G-orbits in Xuni. Then we have
Xuni/∼G ≃Pn,2.
The correspondence is given as follows; take z = (x, v) ∈Guni × V . Put Ex =
{y ∈End(v) | xy = yx}. Then Ex is a subalgebra of End(V ), and x ∈Ex. Put
Vx = Exv ⊂V .
Then Vx is an x-stable subspace of V .
Let λ′ be the Jordan
type of x|Vx and λ′′ the Jordan type of x|V/Vx. Then λ = (λ′, λ′′) ∈Pn,2, and the
correspondence z 7→λ gives a bijection Xuni/∼G ∼
−→Pn,2.
9
We shall deﬁne an analogue of the dominance order on Pn,2 as follows; for
λ = (λ′, λ′′) ∈Pn,2, write it as λ′ = (λ′
1, . . . , λ′
m), λ′′ = (λ′′
1, . . . , λ′′
m) with common
m, and deﬁne c(λ) ∈Z2m
≥0 by
(7.1)
c(λ) = (λ′
1, λ′′
1, λ′
2, λ′′
2, . . . , λ′
m, λ′′
m).
Now deﬁne a dominance order λ ≤µ on Pn,2 by the condition that c(λ) ≤c(µ) in
Z2m
≥0. Note that the deﬁnition of the dominance order on Pn makes sense even for
Z2m
≥0. The following is known by [AH].
Lemma 7.2. For each λ ∈Pn,2, we have Oλ = `
µ≤λ Oµ.
Remark 7.3.
For z = (x, v) ∈Guni × V , the stabilizer ZG(z) in G is connected.
Hence the G-equivariant simple local system on a G-orbit O in Xuni is a constant
sheaf ¯Ql, and we are in a quite similar situation as in the case of GLn.
