---
doc_id: 1104248094
doc_title: "Hochschild and cyclic homology of quantum groups"
section_id: sec-010-appendix-b-example-g-sl2-c
section_title: "Example G = SL(2, C)"
section_number: Appendix B
pages: 36-42
source_pdf: 1104248094.pdf
source_sha256: c1fdb4791afcad3b
toc_source: inferred
doc_brief: "Hochschild and cyclic homology of quantum groups — For an arbitrary complex linear semisimple Lie group G, we consider Hopf algebras of the deformations of the formal and algebraic functions on G."
---
The quantum algebraic group structure is as discussed in Sect. 3, specifically in
Example (3.14). So we will not repeat those definitions.
B.I. The Quasiclassical Limit. We start with the computation of #n(g*,C[G]).
i/i 
o \ 
i/o ι\ 
i/o o\ . 
, . f
H = - 
, E+ = - 
, JE_ =- 
is a basis for g,L ,L ,L the
4\o -i/ 
2\o o; 
2\ι oy
dual basis for g*. The action of g* on C[G] as defined in Proposition (4.4) is as
follows:
\-b—, 
(B.I)
dd 
l '
a
da
u 
,r 
3
 
L
 d 
d 
j d
where N = a 
\-b 
\-c 
\-d —.
da 
db 
dc 
dd
We choose a basis for C[G] as follows
Xp^n:=a
pb
q(bc)
n, 
p,qeZ, 
n^O, 
(B.2)
where a
p\= d~
p, b
q:= c~
q if p,q < 0. On this basis we get
-f 
X
P»<3>H 
J P,Q>n 
p,g,π+l'
Hochschild and Cyclic Homology of Quantum Groups
517
p + l,q
'/P,
/
Y^
p,q,π 
p + 1,9
fp,q,n^p+ί,q
/PΛΛ+1.,
fπ.a.n
XpΊ,a
-2σ(L_)A MiI1 =
p- l,q- l
X
p,q,n 
p
P^O,
P<0,
P>0,
p>0,
P^O,
P^O,
where fpΛJΛ = |p| + |9| + 2n + 2,0^,, = - |p| + \q\ + 2n + 2.
Note
(B.3)
(B.4)
and Vλ is invariant under the action of g* as expected.
#n(g*, Vλ) is computed by the double complex given in Lemma (4.11), and we
choose to compute the nc-homology first. Note [L
+,L~] =0, this again can be
computed by a double complex. The calculation is straightforward and we simply
write down the result here.
Case 1. λ = 0
ac acts on HQ(nc, K0) non-semisimply,
σ(L°)l = -2c,
σ(L°)6c - - 2bc - 4(bc)
2 = - 2σ(L
+ )dc * 0.
Therefore
Case 2. A = p — ^f > 0
H1(nc,KJ =
H0(nc, Vλ) =
(B.5)
(B.6)
(B.7)
(B.8)
Of course terms involving - are there only when - makes sense, i.e., is an integer.
Even when they exist, ac acts with non-zero eigenvalue. So they do not survive to
be in the g*-homology. On the other hand
(B.9)
σ(L°)a
λ= -(λ + 2)a
λ(bc)= -
σ(L°)c
λ = - λc
λ - (λ + 2)c
λ(bc) = 2σ(L_)ac
λ~
l ^ 0.
518 
P. Feng and B. Tsygan
Thus
Case 3. λ < 0 is similar to case 2.
B.2. The Traces for the Quantum Algebra. We want to check that the linear
functionals defined in Lemma (6.2.6) are indeed traces, i.e., they vanish on the
commutators [CΛ[SL2], CΛ[SL2]]. By Proposition (2.4), the commutator of a Hopf
algebra A is the same as the image of A under the right action of A via p. So we
only need to check that the linear functionals in Lemma (6.2.6) vanish on
ρ(tij)(Ch[_SL2~\\ where (ίy) = ί a 
j are the generators of CΛ[SL2]. Recall
and
'a b
S[ , c 
dJJ 
\—q~
1c 
a
where we denote q = e
h. We have
p(b)(a
kb
mc
n) = q~
k(l - q
k+m+n + 2)(ab)(a
kb
mc")
f}( f*\( fj*h^f*^\ 
ί 1 
ft 
"* " 
\ft 
h™f^ 
~^~ 
—I— n 
Γ1 
π 
"* " 
^/7 
r>"* ~^" f^ ~^~
p(c)(d*&
wc") = 4*(l-ι
p(d)(d
kb
mc
n) = q'
m-
nd
kb
mc
n -q~
k+ΐ(l - q~
k~
m-
n'
2)d
kb
m+ic
n+1. 
(B.I 1)
From this it is easy to see the tracial properties of the linear functionals in
Lemma (6.2.6).
The family of traces τ
e
n is easy to understand. They correspond to the
unquantized Cartan subgroup. How to understand the τ*, n Φ 0? The answer is
that while τ
e
n corresponds to the point-like symplectic leaves, τ^ corresponds to
the extended symplectic leaves in the Poisson Lie group (SL2, π). In [42] Soibelman
and Vaksman construct irreducible modules for Ch[Sl/(2)] corresponding to the
symplectic leaves of the Poisson Lie group SU(2). They work with the compact
quantum group and we work with the complex quantum group. The difference is
not important in the discussion here. For the trivial symplectic leaves corresponding
to the Cartan subgroup, they get one-dimensional representations. This provides
the family of traces τ*. For the non-trivial symplectic leaves, the corresponding
Levendorski-Soibelman-Vaksman 
modules are infinite dimensional. Specifically,
they are
Hochschild and Cyclic Homology of Quantum Groups 
519
with the module structure given by
d-e0 = Q9 
a en = en + 1, b-en = aq
nen, c en = βq"en, 
(B.12)
where αβ = — q. From this module we can get formally the following "trace," with
the only non-zero value given by
m,n^0. 
(B.I 3)
But this is not really a trace on Ch[SL2], since
τa(ad -da) = (q-
1- q)τ.(bc) = -q~
2^Q.
This is due to the fact that α, d are not of "trace class." The way out of this difficulty
is to look at the weight decomposition of τα,
We find that τ*, n Φ 0 are traces and τ
s
0 is not a trace. As we have seen in
Subsect. 6.2, this weight space decomposition proves to be very effective in the
general case.
B3. The Results. As we remarked in Subsect. 6.2, the construction of the traces
in the previous subsection actually shows that the spectral sequence is degenerate
at E
2 for CΛ[SL2]. Thus
HHn(Ch[G}) s HB(g*, C[G])® C((Λ)). 
(B.14)
As for the cyclic homology, the direct computation is actually not hard to
carry out for quantum SL2. Corresponding to the new complex for the Hochschild
homology (2.16), there is a new double complex (C^(A\d,D) for the cyclic
homology, where D = ξ'Bξ just as d = ξ'bξ. We consider the spectral sequence
associated with this new double complex whose E
1 term is the Hochschild
homology. Since only HH0 and HHl is non-zero, the double complex for the E
2
becomes
where D2(f) = η ( Σ f j ® f j 
+ f® 1) = Σ//®(dfj)(e) with Δ(f) = Σfj®?J
It is easy to calculate
D2(a
λ) = λ(a
λ®L° + 2a
λ~
 lc® L
+\
520 
P. Feng and B. Tsygan
Therefore we get
H0(g*,C[G])(χ)C((/ι)) 
n = 0
n= 1,3,5,... 
(B.17)
H°ΌR(Tc)®C((h)) 
n = 2,4,6,...
as expected.
References
1. Alvarez-Gaume, L., Gomez, G., Sierra, G.: Quantum group interpretation of some conformal
field theories. Phys. Lett. 220B, 142-152 (1989); Hidden quantum symmetries in rational
conformal field theories. Nucl. Phys. B319, 155-186 (1989)
2. Brylinski, J.: Some examples of Hochschild and cyclic homology. In: Lecture Notes in Math.
vol. 1271, pp. 33-72. Berlin, Heidelberg, New York: Springer 1987
3. Brylinski, J.: A differential complex for Poisson manifold. J. Diff. Goem. 28, 93-114 (1988)
4. Brylinski, J., Getzler, E.: The homology of algebras of pseudodifferential symbols and the
non-commutative residue. K-theory 1, 385-403 (1987)
5. Casselman, W.: Jacquet modules for real reductive groups. In: Proceedings ICM, Helsinki,
1978
6. Casselman, W., Osborne, M. S.: The n-cohomology of representations with an infinitesimal
character. Compositio Math. 31, 219-227 (1975)
7. Casselman, W., Osborne, M. S.: The restriction of admissible representations to n. Math.
Ann. 233, 193-198 (1978)
8. Connes, A.: Non-commutative differential geometry. Publ. Math. IHES 62, 257-360 (1985)
9. Connes, A.: Essay on physics and non-commutative differential geometry. In: The Interface
of mathematics and particle physics. Quillen, D. G., Segal, G. B., Tsou, S. T., (eds.), Oxford:
Oxford University Press 1990
10. Daletskiy, Yu. L., Tsygan, B. L.: Hamiltonian operator and Hochschild homology. Funct.
Anal. Appl. 19, (4) 82-83 (1985)
11. Drinfeld, V. G.: Quantum groups. In: Proceedings ICM, Berkeley, 1986
12. Drinfeld, V. G.: Hamiltonian structure on Lie groups, Lie bialgebras and the geometric
meaning of the classical Yang-Baxter equation. Sov. Math. Dokl. 27, 68-71 (1982)
13. Feigin, B. L., Tsygan, B. L.: Lie algebra homology of generalized Jacobi matrices. Funct.
Anal. Appl. 17, no. (2) 86-87 (1983)
14. Feigin, B. L, Tsygan, B. I.: Additive X-theory. In: Lecture Notes in Math. vol. 1289, pp. 67-209.
Berlin, Heidelberg, New York: Springer 1988
15. Feigin, B. I., Tsygan, B. I.: Cyclic homology of algebras with quadratic relations, universal
enveloping algebras and group algebras. In: Lecture Notes in Math. vol. 1289, pp. 210-239.
Berlin, Heidelberg, New York: Springer 1988
16. Feigin, B. L., Tsygan, B. L.: Riemann-Roch theorem and Lie algebra cohomology. In:
Proceedings of Second Winter School at Crni, Rend. Math. Palermo (1989)
17. Goodwillie, T.: Cyclic homology, derivations and free loop space. Topology 24, 187-216 (1985)
18. Hecht, H., Schmid, W.: Characters, asymptotics and n-homology of Harish-Chandra modules.
Acta. Math. 151, 49-151 (1983)
19. Helgason, S.: Differential geometry, Lie groups, and symmetric spaces. New York:, London:
Academic Press 1978
20. Hilton, P. J., Stammbach, U.: A course in homological algebra. Berlin, Heidelberg, New
York: Springer 1970
21. Jimbo, M.: A ^-difference analogue of t/(g) and Yang-Baxter equation. Lett. Math. Phys.
10, 63-69 (1985)
22. Kassel, C: L'homologie cyclique des algebres enveloppantes. Invent. Math. 91, 221-25 1 (1988)
23. Kirillov, A. N., Reshetikhin, N. Yu.: Representations of the algebra Uq(sl2), ^-orthogonal
polynomials and invariants of links. LOMI-Preprint E-9-88, 1988
Hochschild and Cyclic Homology of Quantum Groups 
521
24. Kirllov, A. N., Reshetikhin, N. Yu.: g-Weyl group and a multiplicative formula for R-matrix.
Commun. Math. Phys. 134, 421-431 (1991)
25. Knapp, A. W.: Representation theory of semisimple groups. Princeton, NJ: Princeton
University Press 1986
26. Levendorski, S., Soibelman, Ya.: Algebras of functions on compact quantum groups, Schubert
cells and quantum tori, Preprint
27. Loday, J.-L., Quillen, D.: Cyclic homology and Lie algebra homology of matrices. Comment.
Math. Helv. 59, 565-591 (1984)
28. Lu, J.-H., Weinstein, A.: Poisson Lie groups, dressing transformations and the Bruhat
decomposition. J. Diίϊ. Geom. 31, 501-526 (1990)
29. Lusztig, G.: Quantum groups at 'roots of 1, to appear in Geom. Ded. (1990)
30. Mack, G., Schomerus, V.: Conformal field algebras with quantum symmetry from the theory
of superselection sectors. Commun. Math. Phys. 134, 139-196 (1990)
31. Manin, Yu. I.: Quantum groups and non-commutative geometry. Centre de Recherches
Mathematiques, Universite de Montreal, 1988
32. Masuda, T., Natsume, T.: Cyclic cohomology of certain affine schemes. Publ. RIMS 21,
1261-1279 (1985)
33. Masuda, T., Nakagami, Y., Watanabe, J.: Non-commutative differential geometry on the
quantum 517(2), I, K-theory 4, 157-180 (1990)
34. Moore, G., Seiberg, N.: Naturality in conformal field theory. Nucl. Phys. B313, 16-40 (1989);
Classical and quantum conformal field theory. Commun. Math. Phys. 123, 177-254 (1989)
35. Parshall, B., Wang, J.-P.: Quantum linear groups. Memoirs of AMS, no. 439
36. Rosenberg, A.: Private communications
37. Rosso, M.: An analogue of P.B.W. theorem and the universal K-matrix for Uh(sl(N + 1)).
Commun. Math. Phys. 124, 307-718 (1989)
38. Schmid, W.: Vanishing theorems for Lie algebra cohomology and the cohomology of the
discrete subgroups of semisimple Lie groups. Adv. Math. 41, 78-113 (1981)
39. Semenov-1 ian-Shansky, M.: Dressing transformation and Poisson group actions. Publ. RIMS
21, 1237-1260 (1985)
40. Serre, J.-P.: Algebra locale, multiplicites: cours an College de France, 1957-1958. Lecture
Notes in Math. vol. 11. Berlin, Heidelberg, New York: Springer 1975
41. Soibelman, Ya. S.: Irreducible representations of the function algebra on the quantum group
5C7(n) and Schubert cells, Sov. Math. Dokl. 40, 34-38 (1990)
42. Soibelman, Y., Vaksman, L.: Algebra of functions on the quantum group SU(2). Funct. Anal.
Appl. 22 (3), 1-14 (1988)
43. Takhtajan, L. A.: Non-commutative homology of quantum tori. Funct. Anal. Appl. 23,
147-149(1989)
44. Tsygan, B. L.: Homology of matrix Lie algebras over rings and Hochschild homology. Usp.
Mat. Nauk. 38, (2) 217-218 (1983)
45. Warner, G.: Harmonic Analysis on Semi-simple Lie Groups, Vol. I. Berlin, Heidelberg,
New York: Springer 1972
46. Wodzicki, M.: Cyclic homology of pseudodifferential operators and noncommutative Euler
class. C. R. Acad. Sci. Paris Ser. I Math. 306, 321-325 (1988)
Communicated by N. Yu. Reshetikhin
