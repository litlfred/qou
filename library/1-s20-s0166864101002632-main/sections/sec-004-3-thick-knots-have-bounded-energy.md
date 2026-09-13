---
doc_id: 1-s20-s0166864101002632-main
doc_title: "Möbius energy of thick knots"
section_id: sec-004-3-thick-knots-have-bounded-energy
section_title: "Thick knots have bounded energy"
section_number: 3
pages: 7-8
source_pdf: 1-s2.0-S0166864101002632-main.pdf
source_sha256: bc5aa8a7663b2a9f
doc_brief: "Möbius energy of thick knots — The Möbius energy of a knot is an energy functional for smooth curves based on an idea of self- repelling."
---
In this section, we prove that the Möbius energy of a knot is bounded by the ropelength.
Our goal is partly the theorem itself and partly the paradigm: any “energy” deﬁned in terms
of inverse-square distances should have an analogous bound, with the proof following this
model.
Theorem 8. If K is a smooth knot in R3 then
EO4(K) <4.57EL(K)4/3. (3)
Theorem 9. If K is a smooth knot in R3 then
EO4(K) ⩽ 1
4EL(K)2. (4)
Remark. For short knots, the quadratic bound is better than the 4 /3 power bound.
Comparing (3) to (4), we see that one needs ropelengths over 79 before the advantage
of the lower exponent is evident. If one uses the actual bound (12) we obtain in the proof,
which is a complicated expression dominated by a 4 /3 power term, then that bound is
lower than (4) for ropelengths > 41. Computer simulations suggest [23,35] the only knots
that can be realized with a ropelength ⩽ 41 are the unknot and the trefoil.
Proof of Theorems 8 and 9. We will obtain the quadratic bound en route to the 4/3p o w e r
bound.
We follow an overall plan similar to [5,6], but introduce a limit process in the main
argument. Since EO4 and EL are both invariant under change of scale, we begin by
rescaling K to have thickness R(K) = 1, so that EL(K) is just the total arclength of K,
which we abbreviate L.
The energyEO4(K) is deﬁned as a double-integral overK ×K. We bound separately the
integral over the portion ofK ×K consisting of pairs(x,y) with arc(x,y) ⩽ πR(K) = π,
and the integral over the rest of K ×K.
Let
Eprox =
∫
x∈K
∫
arc(x,y) ⩽π
1
|x −y|2 − 1
arc(x,y) 2 ,
104 E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
Edist =
∫
x∈K
∫
arc(x,y) /greaterorequalslantπ
1
|x −y|2 ,
and
Ereg =
∫
x∈K
∫
arc(x,y) /greaterorequalslantπ
1
arc(x,y) 2 .
So we have
EO4 = Eprox +Edist −Ereg.
By Lemma 5,
Eprox ⩽ 2
π L.
Also, by symmetry of the circle,
Ereg =
∫
x∈K
(
2
L
2∫
π
1
t2 dt
)
dx = L
(
2
L
2∫
π
1
t2 dt
)
= 2
π L − 4,
so
EO4 ⩽ Edist + 4. (5)
We now bound Edist. We shall bound the inner integral and then multiply by the length
of K to bound the energy. The inner integral, for eachx,i s
Ix
dist =
∫
arc(x,y) /greaterorequalslantπ
1
|x −y|2 .
Here ﬁrst is the quadratic bound.
By Lemma 3, and our rescaling to R(K) = 1, we have for each point y ∈ K,
arc(x,y) /greaterorequalslantπ ⇒| x −y| /greaterorequalslant2.
Thus,
Ix
dist ⩽ 1
22 (L − 2π).
Multiplying by L,w eg e t
Edist ⩽ 1
4L2 − π
