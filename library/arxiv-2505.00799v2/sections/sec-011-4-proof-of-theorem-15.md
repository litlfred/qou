---
doc_id: arxiv-2505.00799v2
doc_title: "QUANTUM MODULAR FORMS AND RESURGENCE"
section_id: sec-011-4-proof-of-theorem-15
section_title: "Proof of Theorem 1.5"
section_number: 4
pages: 27-28
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
doc_brief: "QUANTUM MODULAR FORMS AND RESURGENCE — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
We now prove our main theorem. We proceed by analyzing each case in order. For g of
Type 1 or 2, by Section 3.1, we know that the Borel–Laplace sum
1p
z +d/c
Z ∞
0
e−u/(z+d/c)B1/2(φ−d/c(z)) du√πu
equals zero. Since in these cases g is modular, this equals their obstruction to modularity.
Moreover, we have that
g(z) = 1
2
p
z +d/c
Z
Γ
e−u/(z+d/c)ˆg−d/c(u) du√u = 1
2
p
z +d/c
Z
Γ
e−u/(z+d/c)ˆgodd
−d/c(u)du√u.
Lastly, by Proposition 3.8, we have that
g|κγ(z) = 1
2
p
z +d/c
Z
Γ
e−u/(z+d/c)ˆgodd
−d/c(u)du√u.
Thus we have that g(z) =g|κγ(z).
When g is of Type 3, the argument is essentially the same, except the integral
1p
z +d/c
Z ∞
0
e−u/(z+d/c)B1/2(φ−d/c(z)) du√πu
is not zero. We note that this is precisely the Borel resummation of φd/c with shift 1/2, and
so it is equal to the Borel resummation of φd/c with shift 1. We will show explicitly that this
equals the expected period polynomial in Proposition prop: polynomial.
Forg of Type 4 or 5, we have already shown that g(z) =Sπ/2
med(φ−d/c)(z) in Proposition
3.4. From Section 2.1, we have that
Sπ/2
med(φ−d/c) =S0(φ−d/c) + 1
2discπ/2
κ (Bκ(φ−d/c))
28 ELEANOR MCSPIRIT AND LARRY ROLEN
for z +d/c in the first quadrant. By Proposition 3.6, we have that
1
2discπ/2
κ (Bκ(φ−d/c)) =g|κγ(z)
where γ = ( a b
c d). This tells us that g(z)−g|κγ(z) =S0(φ−d/c) in this region. By analytic
continuation, we get the desired equality on H. The analytic continuation of S0(φ−d/c) to
Cγ is guaranteed by the location of the Stokes rays for Bκ(φ−d/c). The case where g is of
Type 6 is identical except for the addition of the integral
1
2√z
Z
Γ
e−u/z
−4 + 2 log(8πiu)
2πiu
 du√πu,
which contributes to the obstruction to modularity. □
