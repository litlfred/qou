---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-025-45-invariance-of-the-generalized-torsion
section_title: "Invariance of the generalized torsion"
section_number: 4.5
pages: 26-29
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
for the generalized torsion formula. Let M be a three-manifold with torus boundary, and ρm :
π1(M)→ (P)SL(2, C) a representation with meridian eigenvalue m. Let T be a ρm-regular
triangulation of M, which exists by Lemma 4.3 at least for a dense set of representations
on the geometric component of the character variety. Choose an enhanced Neumann-Zagier
datum (z, A, B,f ), with z = z(ρm) satisfying the deformed gluing equations ( 4.5) and f
satisfying ( 4.10). Then, as in ( 4.1), we deﬁne
τT (ρm) :=±1
2 det
(
A∆ z′′ + B∆ −1
z
)
zf ′′
z′′−f.
We can now prove Theorem 4.1.
Repeating verbatim the arguments of Section 3, it is easy to see that τT is independent of
a choice of quad type, a choice of an edge of T and a choice of a meridian loop. The crucial
observation is that the equations AZ + BZ ′′ = iπν (including the meridian equation) are
never used in the respective proofs. Therefore, deforming the m eridian equation by u⁄= 0
does not aﬀect anything. For the same reason, it is not hard to see that the formula is
invariant under ρm-regular 2–3 moves, by repeating the argument of Section 3.6.
The only nontrivial veriﬁcation required is that τT is independent of the choice of ﬂatten-
ing. This does use the gluing equations in a crucial way. We check it now for m⁄= 1.
Choose logarithms (Z,Z ′,Z ′′) of the shape parameters and a logarithm u of m such that
Z +Z ′ +Z ′′ =iπ and
(4.14) AZ + BZ ′′ = 2u +iπν,
where u denote the N-dimensional vector (0 , 0,...., 0,u )T . By independence of quad type
and Lemma A.3, we may assume we are using a quad type with non-degenerate B. Now,
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 27
suppose that (f,f ′,f ′′) and ( ~f, ~f ′,~f ′′) are two diﬀerent generalized ﬂattenings. Then:
(Z·f ′′−Z ′′·f )−(Z· ~f ′′−Z ′′· ~f )
=Z· (f ′′− ~f ′′) + B−1(AZ−iπν− 2u)· (f− ~f )
=Z· (f ′′− ~f ′′) +Z· B−1A(f− ~f )−iπB−1ν· (f− ~f )− 2B−1u· (f− ˜f )
=−iπB−1ν· (f− ~f )− 2B−1u· (f− ˜f )
=iπ(f ′′· ~f−f· ~f ′′)− 2B−1u· (f− ˜f ),
by manipulations similar to those of Section 3.5. The new term 2 B−1u· (f− ˜f ) is now dealt
with with by completing the Neumann-Zagier matrices ( A B ) to a full symplectic matrix
( A B
C D )∈ Sp(2N, Q), whose bottom row agrees with ( C,D ). The symplectic condition implies
that ADT− BCT =I, or B−1 = B−1ADT− CT . Then
B−1u· (f− ˜f ) = B−1ADT u· (f− ˜f )− CT u· (f− ˜f )
= u· DB−1A(f− ˜f )− u· C(f− ˜f )
=−u·
(
C(f− ˜f ) + D(f ′′− ˜f ′′)
)
=−u
(
C· (f− ˜f ) +D· (f ′′− ˜f ′′)
)
.
In this last equation, only the bottom row of C and D appears, due to the contraction with
u = (0, 0,..., 0,u ). But this bottom row is precisely what enters the generalized ﬂatt ening
equations (4.10); since both ﬂattenings satisfy these equations, we must have B−1u·(f− ˜f ) =
0. Therefore, upon exponentiating, we ﬁnd
(4.15) zf ′′
z′′−f = (−1)f ′′· ˜f −f · ˜f ′′
z
˜f ′′
z′′− ˜f =±z
˜f ′′
z′′− ˜f,
which demonstrates that τT is independent of the choice of ﬂattening. Theorem
4.1 follows.
□
4.6. Example: 4 1 continued. We brieﬂy demonstrate the generalized torsion formula,
using representations on the geometric component of the charac ter varietyX41 for the ﬁgure-
eight knot complement.
z z′
z′′ w
w ′
w ′′ 
µ
z
z′
z′′ 
ww ′
w ′′ 
z z′
z′′ w
w ′
w ′′ 
z
z′
z′′ 
ww ′
w ′′ 
λ
Figure 8. Longitude path for the ﬁgure-eight knot complement.
We may consider the same triangulation as in Section 2.6. The edge and meridian equa-
tions ( 2.14) are deformed to
(4.16) z2w2z′′w′′ = 1, zwz ′′ =−m2,
28 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
with z′′ = 1−z−1, w′′ = 1−w−1 as usual. In addition, there is a longitude equation that
may be read oﬀ from the longitude path in Figure
8. In logarithmic (combinatorial) form,
we have−2Z + 2Z ′ = 2v, or
(4.17) − 4Z− 2Z ′′ = 2v− 2πi,
from which we identify
(4.18) C = (−2, 0), D = (−1, 0), ν λ =−1.
Dividing (
4.17) by two and exponentiating, we ﬁnd
(4.19) z−2z′′−1 =ℓ,
with ℓ =−ev. This is the appropriate square root of ( 4.6) for lifting the geometric repre-
sentations to SL(2, C). We can easily check it: by eliminating shape parameters from ( 4.16)
and ( 4.19), we recover the geometric SL(2 , C) A-polynomial for the ﬁgure-eight knot,
(4.20) Ageom
41 (ℓ,m ) = m4− (1−m2− 2m4−m6 +m8)ℓ +m4ℓ2.
We may also use equations (
4.16)–(4.19) to express the shape parameters as functions of
ℓ and m. We ﬁnd
(4.21) z =−m2−m−2
1 +m2ℓ , w = m2 +ℓ
m2−m−2 .
These are functions on the curve Y geom
41 ={Ageom
41 (ℓ,m ) = 0}.
The ﬂattening (
2.15) does not satisfy the new longitude constraint C·f +D·f ′′ =νλ , so
we must ﬁnd one that does. The choice
(4.22) ( fz,f ′
z,f ′′
z ;fw,f ′
w,f ′′
w) = (0, 0, 1; 0, 0, 1)
will work. Repeating the calculation of Section
3.1 with the same A and B but the new
generalized ﬂattening, we now obtain
τ41(ρm) =±1
2 det
(
z′′ + 1 w′′ + 1
1 w′′
)
zw
=±1
2 (z′′w′′− 1)zw
=±1−m2− 2m4−m6 +m8− 2m4ℓ
2m4(m2−m−2) .(4.23)
This is in full agreement with the torsion found by [
GM08, DGLZ09]. Note that for ﬁxed
m there are two choices of representation ρm on the geometric component of the character
variety; they correspond to the two solutions of Ageom
41 (ℓ,m ) = 0 in ℓ.
Remark 4.5. It is interesting to observe that the numerator of (
4.23) is exactly ∂Ageom
41 /∂ℓ.
That the numerator of the geometric torsion typically carries a fac tor of ∂Ageom
41 /∂ℓ might be
gleaned from the structure of “ ˆA-polynomials” in [
DGLZ09, GS], and will also be explored
elsewhere.
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 29
