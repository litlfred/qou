---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-060-247-then
section_title: "Then"
section_number: 2.4.7
pages: 79-82
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
Computational evidences suggest that it is always the case. Remark that in this
case, the eigenvalues of¯ρΣ(∂Σ) are necessarily±1 because they are roots of unity
with order that divides the number of boundary components of the surfaceΣ.
The main diﬀerence with the previous case is the following :
Lemma 2.4.12.TheOv-moduleH1(Σ, Ad◦ρΣ)v is isomorphic toO−3χ(Σ)
v ⊕Ov/(tm)
for some positive integerm.
Proof. AgainH0(Σ, Ad◦ρΣ) is trivial becauseρΣ is not abelian, but in this case we
haveH0(Σ, Ad◦¯ρΣ)≃k. The Universal Coeﬃcients theorem gives
0→H0(Σ, Ad◦ρΣ)v⊗OvOv/(t)→H0(Σ, Ad◦¯ρΣ)→
Tor(H1(Σ, Ad◦ρΣ)v,Ov/(t))→ 0
It follows that the torsion part of the module H1(Σ, Ad◦ρΣ)v is isomorphic to
Ov/(tm) for somem, and the lemma follows.
Again, we pick basisci,c Σ of the complexes ofk(Y )-vector spacesC∗(Mi, Ad◦ρi),
C∗(Σ, Ad◦ρΣ) and basishi,h Σ of their ﬁrst homology group (the only one that is
not trivial). We want to use the formula :
tor(M, Ad◦ρ) = tor(M1) tor(M2)
tor(Σ) tor(H)
Proposition 2.4.13. The terms tor(M1) and tor(M2) lie inO∗
v, but tor(Σ) has
valuation m.
Proof. The ﬁrst part of the statement works in the same way than the proof of
Proposition 2.4.4.
Recall thatΣ has the same homotopy type that a wedge of−χ(Σ) + 1circles, hence
the complexC∗(Σ, Ad◦ρΣ) looks like
sl2(k(Y ))→ sl2(k(Y ))−χ(Σ)+1
78
and to compute its torsion it is enough to compute the determinant of the co-
restricted isomorphismk(Y )3→ k(Y )3. But this map induces a morphism ofOv-
modulesO3
v→O 3
v whose co-kernel is isomorphic toOv/(tm), hence the result.
Again, we need to focus on the termtor(H), where the exact sequenceH is :
0→H1(M, Ad◦ρ)→H1(M1, Ad◦ρ1)⊕H1(M2, Ad◦ρ2)
→H1(Σ, Ad◦ρΣ)→H2(M, Ad◦ρ)→ 0
We consider rather the sequenceHt :
0→k(Y )
d1
− →H1(M1, Ad◦ρ1)⊕H1(M2, Ad◦ρ′
2)
tn.d2
− −− →H1(Σ, Ad◦ρΣ)
δ
− →k(Y )→ 0
forn the number of parallel components inΣ, and the very same arguments that in
the previous section lead to the lemma :
Lemma 2.4.14 (Lemma 2.4.7). Let ∆2 be the restriction oftd2 as above Lemma
2.4.7. Then
tor(Ht) = 1
det ∆2
c, withc∈O∗
v
Since ¯ρΣ = ¯ρ1,Σ is abelian, so is¯ρ2,Σ, hence we can write¯ρΣ(γ) =
(
λ(γ) 0
0 λ−1(γ)
)
for
all γ∈π1(Σ), withλ∈H1(Σ,k∗). Consequently we have the decomposition
H1(Σ, Ad◦¯ρΣ) =H1(Σ,λ 2)⊕H1(Σ,k )⊕H1(Σ,λ−2)
Lemma 2.4.15.The dimension of the kernel of the induced map
H1(M2, Ad◦¯ρ2)→H1(Σ, Ad◦¯ρΣ)
ζ2 =
(
x2 y2
z2 −x2
)
↦→z2,ΣF
is d≥−χ(Σ)/2.
Proof. We observe that this map factors through the maps H1(M2, Ad◦¯ρ2) ↪→
H1(Σ, Ad◦¯ρΣ)
p
− →H1(Σ,λ−2)↪→H1(Σ, Ad◦¯ρΣ). Sincekerp =H1(Σ,λ 2)⊕H1(Σ,k )
79
we ﬁnd that the dimensiond is at least
d≥ dimH1(M2, Ad◦¯ρ2) + dimH1(Σ,λ ) + dimH1(Σ,k )− dimH1(Σ, Ad◦¯ρΣ)
=−3/2χ(Σ)−χ(Σ)−χ(Σ) + 1− (−3χ(Σ) + 1)
=−χ(Σ)/2
Lemma 2.4.16.The valuation of the torsionv(Ht) is smaller thann(2χ(Σ) + 1).
Proof. By Lemma 2.4.8, the map
∆2 : (H1(M1, Ad◦ρ1)⊕H1(M2, Ad◦ρ′
2))/(imH1(M, Ad◦ρ))→ im(∆2)
has determinant greater that the sum of the dimensions of the kernels of the residual
maps
¯D2 = ∆2|t=0 : (H1(M1, Ad◦¯ρ1)⊕H1(M2, Ad◦¯ρ2))/k→H1(Σ, Ad◦¯ρΣ)
[ζ1,ζ 2]↦→z2,ΣF
and
di
dti|t=0∆2 : ker(di−1
dti−1|t=0∆2)→H1(Σ, Ad◦¯ρΣ)
for i = 1,...,n − 1.
But dim ker ¯D2 is at leastdimH1(M1, Ad◦¯ρ1) +d− 1 =−2χ(Σ)− 1, and the maps
di
dti|t=0∆2 are identically zero onker ¯D2, hence the sum of the kernels dimensions is
at least−n(2χ(Σ) + 1). The lemma follows now from Lemma 2.4.7 above.
Lemma 2.4.17.The valuation of the sequenceH is v(tor(H))≤−nχ(Σ)
Proof. It follows from the fact thattrk(d2) tor(Ht) = tor(H), andrk(d2) =−3χ(Σ)−
1
Proof of Theorem 2.0.2, second part.Using Milnor’s formlula, we know that
v(tor(M, Ad◦ρ)) =v(tor(H))−v(tor(Σ))≤−nχ(Σ)−m
80
