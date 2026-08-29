---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-018-52-fusion-homomorphisms
section_title: "Fusion homomorphisms"
section_number: 5.2
pages: 27-28
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
We write [ C] for the Grothendieck ring of a fusion category. The following
property of quantum dimensions is well-known.
Lemma 5.9. Given a pivotal structure γ on a fusion category C, the quan-
tum dimension map dimγ : [C]→ C which sends [V ]↦→ dimγ(V ) satisﬁes the
following:
• It is a ring homomorphism,
• dimγ[Xi] dimγ[X∗
i ] =d{i,i∗} for all simple objects Xi.
This motivates the following deﬁnition.
Deﬁnition 5.10. Let C be a fusion category. We call a function f : [C]→ C a
fusion homomorphism if it is a ring homomorphism and if f[Xi]f[X∗
i ] =d{i,i∗}
for all simple objects Xi.
For a fusion category C, it is interesting to consider whether the injective
map
Pivotal structures(C)→{ Fusion homomorphismsf : [C]→ C}
is also surjective. The following case is instructive. Fix a ﬁnite group G.
27
Proposition 5.11. The pivotal structures on Rep(G) are in 1-1 correspondence
with the fusion homomorphisms from [Rep(G)] to C.
Proof. We have
Pivotal structures(Rep(G))∼= Aut⊗(id)
∼=Z(G)
={g∈G:| TrVi(g)| = dimVi for all irreducibles Vi}
∼={Fusion homomorphismsf : [Rep(G)]→ C}.
The ﬁrst isomorphism uses the fact the fact that Rep(G) comes with a canonical
pivotal structure, and that in general the set of pivotal structures is a torsor for
Aut⊗(idC). The second isomorphism is a result of M¨ uger [20]. The equality in
the third line is a basic result of representation theory [12, Cor 2.28]. The ﬁnal
isomorphism uses two facts. Firstly, every ring homomorphism
[Rep(G)]→ C
must take the form V ↦→ TrV (g) for some ﬁxed g∈ G — because a character
like this certainly is a ring homomorphism, and there are as many such distinct
characters as there are conjugacy classes in the group, which must exhaust all
the ring homomorphisms since [Rep(G)]C is isomorphic to the space of functions
on the conjugacy classes. Secondly, in Rep(G) the paired dimensions d{i,i∗} are
just dim(Vi)2, so that a fusion homomorphism must satisfy|f(Vi)| = dimVi.
