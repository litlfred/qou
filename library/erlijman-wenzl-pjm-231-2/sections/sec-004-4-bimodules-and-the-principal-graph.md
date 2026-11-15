---
doc_id: erlijman-wenzl-pjm-231-2
doc_title: "Subfactors from braided C* tensor categories"
section_id: sec-004-4-bimodules-and-the-principal-graph
section_title: "Bimodules and the principal graph"
section_number: 4
pages: 25-28
source_pdf: erlijman-wenzl-pjm-231-2.pdf
source_sha256: 1ee590e6f087b681
toc_source: inferred
doc_brief: "Subfactors from braided C* tensor categories — 10 sections: Front matter; Bimodules; Categories"
---
4A. Examples of bimodules. We are going to construct systems of bimodules in
order to calculate the principal and the dual principal graph, as described in Propo-
sition 1.8. This will be done using the endomorphisms Shift deﬁned in the last
section.
The N–N-bimodules. Let λi ∈3 and let Ami,λi be the simple component of Ami
corresponding to the simple object Xλi ⊂X⊗mi with mi being large multiples
of k for i = 1, 2, . . . , s. We ﬁrst ﬁx minimal projections pλi ∈Ami,λi. Deﬁne
p⃗λ = pλ1 ⊗· · · ⊗pλs, where⃗λ = (λ1, . . . , λs). The underlying Hilbert space will
be given by
L2(N, tr)p⃗λ := {ζ p⃗λ, ζ ∈L2(N, tr)}.
The N–N bimodule structure is deﬁned by
x.ξ.y = xξShiftN⃗
m(y),
for x, y ∈N, ξ ∈L2(N, tr)p⃗λ,
384
JULIANA ERLIJMAN AND HANS WENZL
where we use the usual right and left multiplication in N on the right hand side. It
follows from Proposition 3.6 that this indeed deﬁnes an N–N bimodule structure
on L2(N, tr)p⃗λ.
Deﬁnition 4.1. The N–N bimodules deﬁned above will be denoted by N⃗λ,⃗m.
The M–N-bimodules. Again let⃗m := (m1, . . . , ms) ∈Ns, with m := m1+· · ·+ms.
We ﬁx a minimal projection pµ ∈(ShiftM⃗
m ◦ˆu)(N)′ ∩M ∼= Am (see Proposition 3.6)
belonging to the simple component of Am labeled µ ∈3. The underlying Hilbert
space for all these bimodules will be given by
L2(M, tr)pµ := {ζ pµ / ζ ∈L2(M, tr)}.
The M–N bimodule structure is deﬁned by
x.ξ.y = xξ(ShiftM⃗
m ◦ˆu)(y),
for x ∈M, y ∈N, ξ ∈L2(M, tr)pµ.
Deﬁnition 4.2. The M–N-bimodules deﬁned above will be denoted by Hµ,⃗m.
The N–M-bimodules. With notations as in the last deﬁnition, we deﬁne similarly
N–M-bimodules based on Hilbert spaces pµL2(M, tr) := {pµζ / ζ ∈L2(M, tr)},
and with the N–M bimodule structure deﬁned by
x.ξ.y = (ShiftM⃗
m ◦ˆu)(x)ξy,
for x ∈N, y ∈M, ξ ∈pµL2(M, tr).
Deﬁnition 4.3. The N–M-bimodules deﬁned above will be denoted by Kµ,⃗m.
The M–M-bimodules. Similarly as for the N–N-bimodules, we ﬁx minimal projec-
tions pλi ∈Ami,λi, with λi ∈3, but now only requiring that P mi being divisible
by k. The underlying Hilbert space for all these bimodules will be given by
p⃗λL2(M, tr) := {p⃗λζ/ ζ ∈L2(M, tr)}.
The M–M bimodule structure is deﬁned by
x.ξ.y = ShiftM⃗
m(x)ξy,
for x, y ∈M, ξ ∈p⃗λL2(M, tr),
Deﬁnition 4.4. The M–M-bimodules deﬁned above will be denoted by M⃗λ,⃗m.
Lemma 4.5. Let the notation be as above.
(a) If we view both N⃗λ,⃗m and Hν,⃗m as left N-modules, then
dimN N⃗λ,⃗m = d⃗λ/(dim X)|⃗m|
and dimN Hν,⃗m = dν[M : N]/(dim X)|⃗m|.
Moreover, we have ind(N⃗λ,⃗m) = d2⃗
λ = ind(M⃗λ,⃗m), where d⃗λ = Q dλi, and
ind(Hν,⃗m) = d2
ν[M : N].
(b) If |⃗m| = |⃗k|, then Hµ,⃗m ∼= Hµ,⃗k as M–N-bimodules, and Kµ,⃗m ∼= Kµ,⃗k as
N–M-bimodules.
SUBFACTORS FROM BRAIDED C∗TENSOR CATEGORIES
385
(c) If |⃗m| = |⃗k|, we have
HomM–M(M⃗λ,⃗m, M⃗µ,⃗k) ⊂HomN–M(M⃗λ,⃗m, M⃗µ,⃗k) ∼= HomC(X⃗λ, X⃗µ),
where X⃗λ = ⊗s
i=1Xλi and X⃗µ = ⊗s
i=1Xµi.
Proof. It is well known (see [Jones 1983], for instance) that dimN L2(N, tr)p =
tr(p) and dimN L2(M, tr)q = tr(q)[M : N] for any projections p ∈N, q ∈M. The
dimension statements in (a) follow. For the index statements in (a), let ℓand r
denote left and right multiplication by N on L2(N, tr) or suitable submodules of it.
Observe that ℓ(N)′
|L2(N,tr)p is equal to r(pNp) for any p ∈Shift⃗m(N)′ ∩N. Recall
that Shift⃗m(N) ⊂N has index (dim X)2|⃗m|. Moreover, tr(p⃗λ) = d⃗λ/(dim X)|⃗m| for a
minimal idempotent p⃗λ ∈Shift⃗m(N)′∩N; see Proposition 3.6. Using the formula for
local indices [Wenzl 1988, Theorem 1.5(iii)] and the index formula in Proposition
3.6(c), we obtain
ind(N⃗λ,⃗m) = [p⃗λNp⃗λ : p⃗λShift⃗m(N)] = tr(p⃗λ)2(dim X)2|⃗m| = (d⃗λ)2.
The indices for Hν,⃗m and M⃗λ,⃗m are computed similarly. By Lemma 3.5, (c), we
have ShiftN⃗
m = ShiftN⃗
k , from which (b) follows.
Let⃗mL2(M, tr) be the Hilbert space L2(M, tr) with M–M bimodule structure
x.ξ.y = ShiftM⃗
m(x)ξy for x, y ∈M and ξ ∈L2(M, tr). Deﬁne⃗kL2(M, tr) similarly.
These bimodules are isomorphic as N–M bimodules, again by Lemma 3.5(c). This,
combined with Lemma 3.5(b), results in
HomM–M(⃗mL2(M, tr),⃗kL2(M, tr)) ⊂HomN–M(⃗mL2(M, tr),⃗kL2(M, tr)) ∼=
∼= EndN–M(⃗mL2(M, tr)) ∼= A|⃗m| = EndC(X⊗|⃗m|),
(∗)
where the second isomorphism follows from Proposition 3.6(b), and (b). By con-
struction, we have M⃗λ,⃗m = p⃗λ(⃗mL2(M, tr)) and M⃗µ,⃗k = p⃗µ(⃗kL2(M, tr)), where
p⃗λ = pλ1 ⊗· · ·⊗pλs and p⃗µ = pµ1 ⊗· · ·⊗pµs. Hence we can interpret an element
f ∈HomM–M(M⃗λ, M⃗µ) as an element in HomN–M(⃗mL2(M, tr),⃗kL2(M, tr)) which
satisﬁes p⃗µ f p⃗λ = f . Using this together with (∗) proves claim (c).
□
4B. Principal graph. Let⃗λ = (λ1, . . . , λs) ∈(3′)s, and let Lν⃗
λ be the multiplicity
of the object Xν in ⊗Xλi. Observe that Lν⃗
λ is also equal to the rank of the projection
N pλi in the simple component of A|⃗λ| labeled by ν.
In the following we will ﬁx a vector⃗m = (mi) where all its coordinates are
divisible by k, and with mi large enough that all simple objects of C′ will appear
in X⊗mi for i = 1, . . . , s. We shall hence omit⃗m in the indices of the bimodules
and will just write N⃗λ and Kν for N⃗λ,⃗m and Kν,⃗m, respectively.
Theorem 4.6. With the notation as above:
(a) The bimodules N⃗λ and Hν deﬁned above are irreducible.
386
JULIANA ERLIJMAN AND HANS WENZL
(b) The principal graph for N ⊂M is the connected component of the fusion
graph from (C′)s to C′ which contains the trivial object of C. Recall that the
even vertices of the fusion graph are labeled by s-tuples of elements of 3′,
the odd vertices are labeled by the elements of 3′, and the vertex labeled by⃗
λ = (λ1, . . . , λs) is connected with the vertex labeled by ν by Lν⃗
λ edges.
(c) The subfactor N ⊂M has ﬁnite depth.
Proof. Statement (a) follows from Proposition 3.6. For (b), it sufﬁces to calculate
the principal graph for the isomorphic inclusion N ⊂M given by ˆu⃗m (see Lemma
3.4). In this case the M–N bimodule structure of L2(M, tr) is given by x.ξ.y =
xξ ˆu⃗m(y). It follows from the deﬁnitions that L2(M, tr) ⊗N N⃗λ ∼= L2(M, tr)p⃗λ ∼=
⊕Lν⃗
λHν; the decomposition of L2(M, tr)p⃗λ into irreducible M–N bimodules fol-
lows from Proposition 3.6(b) and the remarks at the beginning of this subsection.
Hence our system of bimodules (N⃗λ)⃗λ∈(3′)s and (Hν)ν∈3′ is closed under induction.
To prove closedness under restriction, observe that the multiplicity of the N–N
bimodule N⃗λ in the M–N-bimodule Hν, viewed as an N–N-bimodule, is equal to
Lν⃗
λ, by Frobenius reciprocity. To show that Hν ∼= L⃗
λ Lν⃗
λN⃗λ as an N–N-bimodule,
it sufﬁces to prove that both sides have the same dimension, i.e., by Lemma 4.5(a),
that
(4-1)
[M : N]dν =
X⃗
λ
Lν⃗
λd⃗λ.
For this observe that the dimension vectors for A⊗s
n
and Ans, with n a multiple of k,
are given by⃗tns = (d⃗λ/(dim X)ns)⃗λ and⃗vns = (dν/(dim X)ns)ν, with⃗λ ∈(3′)s and
ν ∈3′. Observe that the subfactor N ⊂M is generated by the periodic sequence
(A⊗s
n ⊂Ans), with the inclusion matrix for A⊗s
n ⊂Ans given by G =(Lν⃗
λ) with⃗λ and
ν as above, provided k|n. Hence it follows from [Wenzl 1988], Theorem 1.5(ii),
that G⃗vns = [M : N]⃗tns. This implies (4-1). Finally, if we choose⃗λ = (1, 1, . . . , 1)
(s times), where 1 stands for the trivial object of C, ind(N⃗λ) = 1 and hence N⃗λ is
weakly reduced from the trivial N–N bimodule by Proposition 1.8(c). This shows
(b), by Proposition 1.8(a). Statement (c) is a consequence of (b).
□
Remark 4.7. The fusion graph from (C′)s to C′ may not be connected. An easy
example is obtained for C being the representation category of a ﬁnite abelian
group G, where it decomposes into |G| connected components.
