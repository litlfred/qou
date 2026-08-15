---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-004-22-resurgence-of-the-generating-function
section_title: "Resurgence of the generating function"
section_number: 2.2
pages: 18-19
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
Let G be a simple, simply connected compact Lie group, and letτG,k be the levelk Reshetikhin-
Turaev TQFT constructed from the quantum groupUq(g), where g is the complexiﬁcation of the
Lie algebrah ofG. Let ˇh be the dual Coxeter number ofh, and setˇk =k +h. For a closed oriented
three manifoldM (possibly containing a colored framed link) we consider the normalized invariant
ZG,k(M) =
τG,ˇk(M)
τG,ˇk(S2× S1).
Let z be a formal variable and consider the generating function
ZG(M;z)∈ C[[z]]
given by
ZG(M;z) =
∞∑
k=0
ZG,k(M)zk.
By work of GaroufalidisZG(M;z) is known to be convergent on the unit disc. Motivated by the
paradigm of analytic continuation and resurgence, Garoufalidis posed the following conjecture
Conjecture 1 ([26]). The generating functionZG(M;z) has an analytic continuation toC\eΛ
whereeΛ is a ﬁnite set containing zero and the exponentials of the negatives of the complex classical
Chern-Simons values.
In other words, the conjecture is that the generating functionZG(M;z) determines the germ
at zero of a resurgent function. This conjecture is formally motivated from resurgence of Laplace
integrals and the (non-rigorous) path integral formula for the WRT invariant, as explained in [26].
We now specialize to the case of the Seifert ﬁbered homology sphereX and G = SU(2). Set
K =k +2 and consider the generating function for the normalized quantum invariant˜Zk(X) given
by
˜Z(X;z) =
∞∑
k=0
˜ZK(X)zk∈ C[[z]].
Fors∈ C consider the polylogarithm
Lis(z) =
∞∑
n=1
zn
ns. (44)
Fors =−m,m∈ N the polylogarithm is exact and in fact a rational function
Li−m(z) =
(
z ∂
∂z
)m( z
1−z
)
.
We introduce the following notation for the exponentials of the negatives of the classical complex
Chern-Simons values
eΛ = exp (−2πi CS∗
C(X)).
We prove the following proposition.
Resurgence Analysis of Quantum Invariants 19
Proposition 11. The generating function˜Z(X;z) is the germ at zero of a holomorphic function
˜Z∈O (C\eΛ) given by the following formula
˜Z(X;z) =
∫ ∞
0
e−2yB(Z0)(y)
1−ze−y dy
+
∑
θ∈CS∗
C(X)
e4πiθ
n−3∑
j=0
Z(j)
θ (0)
j!
(
2j +
j∑
l=0
2j−l
(j
l
)
Li−l
(
ze2πiθ)
)
.
(45)
Proof. From Equation (43) it follows that
˜Z(X;z) =
∞∑
k=0
zk
∫ ∞
0
e−y(k+2)B(Z0)(y) dy
+
∑
θ∈CSC(X)
∞∑
k=0
zk Zθ(k + 2)e2πi(k+2)θ.
(46)
The ﬁrst term can be simpliﬁed by interchanging summation and integration and then using the
geometric series expansion
∞∑
k=0
zk
∫ ∞
0
e−y(k+2)B(Z0)(y) dy =
∫ ∞
0
∞∑
k=0
(ze−y)kB(Z0)(y)e−2y dy
=
∫ ∞
0
e−2yB(Z0)(y)
1−ze−y dy.
(47)
This can be justiﬁed by standard complex analysis arguments. To complete the proof, we can
consider seperately each term in (46) corresponding to a complex Chern-Simons valueθ∈ CSC(X).
We get that
∞∑
k=0
zk Zθ(k + 2)e2πi(k+2)θ
=e4πiθ
n−3∑
j=0
Z(j)
θ (0)
j!
∞∑
k=0
(k + 2)j(e2πiθz)k
=e4πiθ
n−3∑
j=0
Z(j)
θ (0)
j!
(
2j +
j∑
l=0
2j−l
(j
l
) ∞∑
k=1
kl(e2πiθz)k
)
=e4πiθ
n−3∑
j=0
Z(j)
θ (0)
j!
(
2j +
j∑
l=0
2j−l
(j
l
)
Li−l(e2πiθz)
)
.
(48)
In the last equality, we used the series expansion (44) of the polylogarithm. By substituting the
identities (47) and (48) into (46) we obtain the desired identity (45).
