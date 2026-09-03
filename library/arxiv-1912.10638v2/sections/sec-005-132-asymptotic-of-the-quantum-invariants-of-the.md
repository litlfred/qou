---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-005-132-asymptotic-of-the-quantum-invariants-of-the
section_title: "Asymptotic of the quantum invariants of the Whitehead chains"
section_number: 1.3.2
pages: 5-7
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
---
In the second part of this paper, we generalize the previous results on the Whitehead link to the Whitehead
chains.
Theorem 4. We have
lim
N→∞
2π
N + 1
2
log|J⃗N(Wa,1,c,d,e
2πi
N + 1
2 )| = Vol(S3\Wa,1,c,d)
As a consequence, we can show that
Corollary 2. For any a∈ Z, b≥ 1, c,d∈ N with c +d≥ 1, Conjectures 4 is true for TVr(S3\Wa,b,c,d).
Moreover, if we colored the belt by M1 and all the clasps by M2 (see Figure 2 for an example), we
have the following result.
Theorem 5. There exists some δ >0 such that for any 1−δ <s1,s 2 < 1, we have
lim
N→∞
2π
N + 1
2
log|JM1,M2(W0,1,c,0,e
2πi
N + 1
2 )|
= Vol(S3\W0,1,c,0,u 1 = 2πi(1−s1),v 2 =v3 =...v c+1 = 4πi(1−s2))
Figure 2: the link W0,1,2,0 with belt colored by M1 and all other components colored by M2
Note that Theorem 5 gives a positive answer to Conjecture 6 for the sequence of colors (M1,M 2,...,M 2)
with s2 = 1.
1.3.3 Diﬀerential formula for the potential function and relation to hyperbolic geometry
From the discussion in subsection 1.2, we have already seen the importance of the potential function.
Thus, it is necessary to have a better understanding about how the geometric information of a link
complement is encoded in the potential function of the link. In the study of the asymptotics of the
colored Jones polynomials, we discover the following formula satisﬁed by the potential function of the
Whitehead link.
5
Lemma 1. Writezk =xk +iyk fork = 1, 2. The real part of the potential function satisﬁes the following
diﬀerential equation:
Re Φ+(s1,s2)(z1,z 2) = 1
2πV +(s1,s2)(z1,z 2) +
2∑
k=1
yk
∂
∂yk
Re Φs1,s2(z1,z 2), (3)
where
V +(s1,s2)(z1,z 2) =D(e2πi(s2−1)−2πiz1−2πiz2)−D(e2πi(s2−1)−2πiz2) +D(e2πiz2)
−D(e2πiz1+2πiz2) +D(e2πiz1)
and D(z) is the Bloch-Wigner function.
This formula has two immediate consequences. First, from Theorem 3)1)a), there exists a family
of critical point z+(s1,s2) for the potential function Φ +(s1,s2)(z1,z 2) such that the critical point equa-
tions coincide with the hyperbolic gluing equations for a particular triangulation of the Whitehead link
complement. In particular, at this crtical point, by deﬁnition we have
∂
∂yk
Re Φ+(s1,s2)(z+(s1,s2)) = 0 for k = 1, 2.
From this, using lemma above, we can see that the real part of the critical value of the potential function
is the sum of the volume of the ideal tetrahedra which satisfy the hyperbolic gluing equations, i.e. the
hyperbolic volume of the link complement.
Next, the formula relates the potential function to the theory of angle structures. Note that every
points on the subset
A =
{
(z1,z 2)| Im d
dzi
Φ+(s1,s2)(z1,z 2) = ∂
∂yk
Re Φ±(s1,s2)(z1,z 2) = 0 for k = 1, 2
}
satisﬁes the property that the sum of the angles around the vertices are 2 π. Therefore, A is a subset of
the space of angle structures and the potential function restricted on A is exactly the volume function.
In particular, by the theorem of angle structures, we know that the maximum point on A is exactly the
hyperbolic volume of the link complement.
Moreover, it is interesting to compare the diﬀerential formula (3) with the covolume function discussed
in [11]. Recall that every hyper-ideal tetrahedron is determined (up to isometry) by six dihedral angles
{aij}1≤i<j≤4, where aij is the dihedral angle between the faces i andj. Let lij be the length of the edge
between the facei and the face j. Then aij andlij uniquely determine each other. Moreover, the volume
function vol satisﬁes the Sch¨ alﬁ’s formula:
∂vol
∂aij
=−lij
2
The Legendre transform of the volume function is called the covolume function cov, which is given by
[11]
cov(lij) =vol(aij) +
∑
i<j
lij· aij
2
Note that by the Sch¨ alﬁ’s formula,
∂cov
∂lij
=
∑
i<j
∂vol
∂aij
∂aij
∂lij
+
∑
i<j
lij
2
∂aij
∂lij
+ aij
2 = aij
2
Thus, we have
cov(lij) =vol(aij) +
∑
i<j
lij
∂cov
∂lij
(4)
Now, given a triangulation {∆1,..., ∆n} of a 3-manifold M with edge lengths {l1
ij,...,l n
ij}, where we
identify la
pq with lb
rs whenever these two edges are glued together, we can deﬁne the covolume function
covM of M to be
covM(l1
ij,...,l n
ij) =
n∑
k=1
covk(lij) =
n∑
k=1
volk(aij) +
∑
i,j
lijAij (5)
6
where Aij = ∂covM
∂lij
is the sum of the dihedral angles around the edge lij. Equations (3), (4) and (5)
suggest that we should think of yk as some sort of ‘length’. We hope that this formula will help us to
understand the theory of potential function.
The ﬁnal remark for this equation is that the proof of Lemma 3 is based on some basic properties of
the dilogarithm function and the Lobachevsky function. In particular, by using the argument, one can
show that the potential functions discussed in [18, 19, 20], and the potential functions in [17, 4] after the
reparametrization z↦→e2πiz, also satisfy the same type of diﬀerential formula.
