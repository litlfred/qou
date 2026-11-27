---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-016-42-conjugate-states-and-bethe-roots
section_title: "Conjugate states and Bethe roots"
section_number: 4.2
pages: 19-20
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
In Section 3.4 we saw that in the degenerate case there are two possible diagrams for the structure of Virasoro
modules, reproduced here for convenience (co-Verma module to the left, Verma module to the right):
•
◦
◦
•
. (82)
Due to the sign in the conjecture (66), we see that degenerate chiral weights h (i.e., h = hr,s with r,s∈ N∗)
are obtained by charges α corresponding to states where (e−eφ) and Sz are of opposite signs, while degenerate
anti-chiral weights ¯h are obtained by charges ¯α corresponding to states where (e−eφ) and Sz are of the same
sign. With the sign conventions for magnetization and lattice momentum used in this paper, we have found the
co-Verma type for
α =αr,s ⇔ (e−eφ)< 0 and Sz > 0, (chiral) (83a)
¯α =αr,s ⇔ (e−eφ)< 0 and Sz < 0, (anti-chiral), (83b)
while the Verma type was found for the conjugate charges
α =αc
r,s ⇔ (e−eφ)> 0 and Sz < 0, (chiral) (84a)
¯α =αc
r,s ⇔ (e−eφ)> 0 and Sz > 0, (anti-chiral), (84b)
with r,s ∈ N∗ as given in (66). As an example, ( e−eφ) = −1,Sz = 1 ⇒ α = α1,1 = 0 while ( e−eφ) =
1,Sz =−1⇒ α = αc
1,1 = 2α0, which can be compared to (76). Of course the choice of conventions holds no
deeper meaning, and the important takeaway is that within each sector of Sz we expect to ﬁnd pairs of conjugate
primary states such that one has a chiral null state, the other a anti-chiral one, and the modules are of opposite
types (Verma or co-Verma).
We now show that such pairs of states, which diﬀer by the sign of ( e−eφ), correspond to Bethe states that
diﬀer only by the sign of their Bethe integers and the sign of their Bethe roots. This can be seen directly from
the shape of the Bethe equations (154) in Appendix B, reproduced here for convenience:
d(λj)
a(λj)
∏
k⁄=j
b(λk,λj)
b(λj,λk) = 1 (85)
Leaving the deﬁnitions of the various terms to the Appendix, we here need only know that b(−λk,−λj) =
b(λj,λk),a(λ) = 1 and that for φ = 0,d(−λ) = (d(λ))−1 in the homogeneous limit (our case of interest). When
φ⁄= 0, the only modiﬁcation to the Bethe equations is d(λ)→eiφd(λ), showing that one must take eφ→−eφ
in order for the roots with opposite signs to be a solution.
19
That the Bethe roots for these pairs of states diﬀer only by their sign will be important in Section 4.3, where
we show that a strong duality of the corresponding modules can be seen directly on the lattice using Bethe
ansatz techniques. To clarify the meaning of “strong”, let us for comparison write out a weaker type of duality
that is expected based only on the conjecture (66) as discussed above. We shall need a more precise notation
for conjugate states than in Section 3.4. We write V¯αc,αc for a state whose anti-chiral charge is the conjugate
of the chiral charge of Vα,¯α, and whose chiral charge is the conjugate of the anti-chiral charge of Vα,¯α. In this
notation, we have the following result:
W eak duality: Whenever Vα,¯α has a degenerate chiral charge α = αr,s or α = αc
r,s (with r,s∈ N∗) we
expect that
⟨W|Ar,s|Vα,¯α⟩ = 0 ⇔ ⟨V¯αc,αc| ¯A‡
r,s|W c⟩ = 0, (86a)
whereW,W c are the corresponding null states at levelrs,Ar,s the relevant combination of lowering operators
as in the examples (3) and A‡
r,s the “conformal conjugate” for which L‡
n = L−n. The same type of
statements hold when Vα,¯α has a degenerate anti-chiral charge ¯α =αr,s or ¯α =αc
r,s:
⟨W| ¯Ar,s|Vα,¯α⟩ = 0 ⇔ ⟨V¯αc,αc|A‡
r,s|W
c
⟩ = 0. (86b)
On the lattice, we expect that the corresponding matrix elements (with the Virasoro generators replaced by
the Koo-Saleur generators, and primary/descendant states by their corresponding scaling states) will approach
either zero or non-zero values in the limit according to this duality. Comparing to (86), the stronger duality
that will be shown below is the statement that two matrix elements have the same value already on the lattice.
Before turning to the stronger duality we note that even without the Bethe ansatz we can, in fact, see
the weaker duality already on the lattice for one particular case of interest: the modules W0,q−2 and W0,q2 as
described in Section 2.3:
W0,q−2:
[0, q−2]
[1, 1]
, W0,q2:
[0, q2]
[1, 1]
. (87)
Within these diagrams, the pair of states corresponding to Sz = 0,|e| = 1,eϕ =±α−/α+8 can be found within
[0, q±2] while their corresponding level-1 null states can be found within [1 , 1]. The duality under the action of
the Koo-Saleur generators on the lattice then follows directly from the duality of the Temperley-Lieb modules,
since the Koo-Saleur generators are built out of Temperley-Lieb generators.
