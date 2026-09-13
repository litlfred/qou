---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-015-73-reconciling-the-two-cactus-group-actions
section_title: "Reconciling the two cactus group actions"
section_number: 7.3
pages: 20-21
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
and consider the g-crystal B = Irr(C). There are two actions of the cactus group on B, the ﬁrst
arising combinatorially via Sch¨ utzenberger involutions (Theorem 7.3) and the other categorically
via Theorem 7.7.
Theorem 7.12. The two actions of the cactus group on B agree.
Proof. It suﬃces to show that ϕI =ξI . First, suppose C is a simple categoriﬁcation of type λ ∈X+.
In this case B = B(λ), and ξ =ξI is determined by:
ξ(vλ) = vlow
λ , and
ξ(rei(v)) = rfτ (i)(ξ(v)) for all v ∈ B,
so we need to show that ϕI satisﬁes these properties as well.
The ﬁrst is an immediate consequence of Corollary 6.7. To sho w that ϕI satisﬁes the second
property, ﬁx µ ∈X and i ∈I. We set n =ht(µ −w0(λ)),j =τ (i), and write Θ = Θ w0.
Consider the following diagram:
Db(Cµ) Db(Cw0(µ))
Db(Cµ+αi ) Db(Cw0(µ)−αj )
Θ /BD
µ[−n]⟨µi⟩
Ei
/BD
µ Fj
/BD
w0(µ)
Θ /BD
µ+αi [−n−1]
(7.13)
By Proposition 5.9 this diagram commutes (note that we shift ed both sides of the equation by
−n − 1). By Theorem 6.4 both horizontal arrows are in fact t-exact equivalences so this restricts
to a diagram of abelian categories:
Cµ Cw0(µ)
Cµ+αi Cw0(µ)−αj
Θ /BD
µ[−n]⟨µi⟩
Ei
/BD
µ Fj
/BD
w0(µ)
Θ /BD
µ+αi [−n−1]
(7.14)
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 21
Let L ∈ C µ be a simple object, and let L′ = Θ /BD
µ(L)[−n]⟨µi⟩. Note that L′ ∈ C w0(µ) is simple
and ϕI (L) = L′. By the above diagram we have an isomorphism
Θ /BD
µ+αi(Ei(L))[−n − 1] ∼= Fj(L′).
Now, rFj(L′) ⊂ Fj(L′) is the unique simple subobject. On the other hand, since Θ /BD
µ+αi[−n − 1]
is an abelian equivalence, Θ /BD
µ+αi(rEi(L))[−n − 1] ⊂ Θ /BD
µ+αi(Ei(L))[−n − 1] is a simple subobject.
Therefore
Θ /BD
µ+αi(rEi(L))[−n − 1] ∼= rFj(L′).
Since the equivalence class of the left hand side is ϕI ◦ rei(L), this shows that ϕI satisﬁes the
second deﬁning property, and hence the two cactus group acti ons agree in the case of a simple
categoriﬁcation.
The general case when C is not necessarily a simple categoriﬁcation follows easily using the
Jordan-H¨ older ﬁltration (Theorem 3.6) and Lemma 4.6. □
