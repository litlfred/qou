---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-083-266-the-right-hand-side-of-the-gross-koblitz-for
section_title: "The right hand side of the Gross-Koblitz formula is a special case of"
section_number: 2.6.6
pages: 36-37
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
can be written
−π−k∑
ζp−1
ζ−k
p−1Eπ(ζp−1) =−π−k
∞∑
n=0
(∑
ζp−1
ζ n−k
p−1
)
en
= (1−p)π−k
∞∑
m=0
e(p−1)m+k.
Using the expansion of Γ( α) given in 2.6.3, in the case of α = k
p−1 , we
thus have to show that
∞∑
n=0
epn+k(−π)−n
( k
p− 1
)
n
= (1−p)
∞∑
m=0
e(p−1)m+k.
Denote the left hand side by Gk (for anyk∈ N). Due to the overconvergence
ofEπ, it is not diﬃcult to see that lim
k→∞
Gk = 0. One has Robert’s formula:
Gk−Gp−1+k = (1−p)ek.
Summing up consecutive expressions, one gets a telescoping sum which yields
the desired equality Gk = Gk− lim
m→∞
G(p−1)m+k = (1 −p)
∞∑
m=0
e(p−1)m+k.
It remains to prove Robert’s formula. One ﬁrst observes that z d
dzEπ =
(πz− pπz p)Eπ(z), which yields the relation nen = π(en−1− pen−p) for
n≥p, hence πep−1+m =pπem + (m +p)em+p for m≥ 0. Then
Gk−Gp−1+k
=ek +
∞∑
0
ep(n+1)+k(−π)−n−1
( k
p− 1
)
n+1
−
∞∑
0
ep−1+pn+k(−π)−n
( k
p− 1 + 1
)
n
=ek +
∞∑
0
[ k
p− 1ep(n+1)+k +πep−1+pn+k
]
(−π)−n−1
( k
p− 1 + 1
)
n
=ek +
∞∑
0
[
p (k + (n + 1)(p− 1))
p− 1 ep(n+1)+k +pπepn+k
]
(−π)−n−1
( k
p− 1 + 1
)
n
= (1−p)ek +p
∞∑
0
(k + (n + 1)(p− 1))
p− 1 ep(n+1)+k(−π)−n−1
( k
p− 1 + 1
)
n
−p
∞∑
1
k +n(p− 1)
p− 1 epn+k(−π)−n
( k
p− 1 + 1
)
n−1
= (1−p)ek.
