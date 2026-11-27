---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-009-43-reduced-jet-bundle
section_title: "Reduced jet bundle"
section_number: 4.3
pages: 20-21
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
A as built
on the degree ≤k part of a diﬀerent graded algebra, namely the ‘braided-symmetric algebra’
Sσ(Ω1) associated to σ obeying the braid relations as is the case in Theorem 4.8. This algebra
is deﬁned as
Sσ(Ω1) = TAΩ1
⊕k ker[k,σ ]! = TAΩ1
⊕k ker∑π∈Skσi1/uni22EFσil(π)
where, for the second expression, we write π =si1/uni22EFsil(π) of length l(π) as a product of simple
reﬂections si = (i,i + 1) and σi denotes σ in the i,i + 1 tensor power. These ideas are familiar
in the vector space case where the ﬁrst point of view is that of a braided-linear space [16, 19]
and the second has been called a ‘Nichols-Woronowicz algebra’. The diﬀerence is that now we
work over A rather than over a ﬁeld, in fact more in the spirit of a symmetric version of the
Woronowicz exterior algebra on a Hopf algebra [25].
In our case of interest, when ∇is torsion free, ∧-compatible, extendable and its σ obeys the
braid relations, we have
Ω1⊗k
ker[k,σ ]! ≅im[k,σ ]!⊆Ωk
S
by the inclusion in Lemma 4.3 and combining in diﬀerent degrees to an algebra inclusion
Sσ(Ω1) ⊆ΩS
QUANTUM JET BUNDLES 21
for the product in Corollary 4.5. This follows from the braided-binomial theorem cf.[16, Thm 10.4.12]
which, in our conventions, and now overA, reads [i,σ]!= /bracketleft.alt2i
j,σ/bracketright.alt2([i−j,σ]!⊗[j,σ]!). We letSi
σ(Ω1)
be the degree i component of Sσ(Ω1).
Corollary 4.9. Suppose that ∇obeys the conditions in Theorem 4.8 and that moreover
im(∇i) ⊆im[i,σ]!
for all i≤k. Let di∶A→Si
σ(Ω1) be such that ∇i(a) = [i,σ]!(di(a)). Then there is a reduced jet
bimodule
Jk
σ = /uni2295.big.disp
0≤i≤k
Si
σ(Ω1), a ●kω =jk−j
σ (a)ω, ω ●ka=ωjk−j
σ (a), j k
σ(a) = /summation.disp
0≤i≤k
di(a)
for a bimodule map jk
σ∶A →Jk
σ and all a ∈A, ω ∈Sj
σ(Ω1). There is also a bimodule map
Jk
σ→Jk−1
σ where we quotient out the top degree and which connects jk
σ to jk−1
σ .
Proof. This is immediate once we note that the product in Sσ(Ω1) corresponds to a restriction
of the product ⊙of ΩS. □
In nice cases, we will have an equality and the reduced bundle is the same but just expressed
diﬀerently, usually more algebraically by generators and relations. We will also see an example
of a strict reduction in Section 6.1.
