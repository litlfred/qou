---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT"
section_id: sec-018-5-deforming-representations-another-way-to-param
section_title: "Deforming representations: another way to parametrize the components"
section_number: 5
pages: 22-28
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
doc_brief: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
components
Having found a speciﬁc representation ρ : Γ 8 → SL(3, C) by algebraic
means, there is a complementary method we can often use to determine
the componentV of the variety containing ρ. We apply this procedure to a
representation in each of the three components found in the previous section.
As a product, we get an explicit parametrisation of the representations, i.e.
an explicit parametrisation of matrices generating the representation, at
least for a Zariski-open subset of the studied component. This information
is of course very valuable for the study of the representations found, as in
[7].
The procedure may be broken down into four steps, which we now describe
brieﬂy; a detailed account of the method is given in [4]. Repeated use is made
of the LLL algorithm [16] for ﬁnding an algebraic number of low degree, close
to a number given numerically to high precision. For ease of exposition, we
shall assume that V has dimension 2; in advance we might not know this
dimension, but usually with experimentation it quickly becomes evident.
Also, the dimension of the Zariski tangent space atρ ([5]) provides an upper
bound for the dimension of V.
(i) First, we perturb the images of the group generators underρ slightly,
and use these perturbed matrices as a starting point for Newton’s
23
method in conjunction with the group relators, so as to converge
numerically to a representation σ. If the original representation ρ is
not isolated, σ will typically be some generic representation close to
ρ; however, by carefully imposing extra constraints one can “steer”
the Newton process so that σ has some speciﬁed character. In this
way we can obtain a ﬁnite array of representations{σij} such that for
each generatorgk of Γ8 the traces of the matrices αij =σij(gk) form
a suitable array of (numerical approximations to) rational numbers.
Of course the matrix αij depends on the index k ofgk, but to avoid
excess of notation we omit mention of this index.
(ii) Matrices βij are chosen (independently of k) so that the conjugates
α′
ij = β−1
ij αijβij have entries that are all algebraic. This is always
possible, owing to the fact that V is an algebraic set; in practice we
desire that the degrees of these algebraic numbers should be as small
as possible.
(iii) So far, for each group generator gk we have a two-dimensional array
of matrices α′
ij whose entries are numerical approximations to ele-
ments of a number ﬁeldFij. We choose a suitable basis for Fij over
the ﬁeld of rationals, noting that the ﬁeld depends on the parame-
tersi,j . Next, LLL allows us to emerge from the world of numerical
approximations to that of exact quantities by guessing an expres-
sion for each matrix entry as a linear combination of basis elements.
Of course we wish also to be freed from the discrete coordinates
(i,j ) to general (complex) coordinates ( u,v ) for the variety V, and
this is achieved, up to judicious guesswork, by means of polynomial
interpolation across the (i,j )–lattice.
(iv) The reader will note that guesswork has been employed at several
points of this procedure, and that substantial use was made of nu-
merical approximations to algebraic numbers. However, we have
arrived at a function Φ that associates to each generator gk of Γ8 an
exact matrix, whose entries lie in an algebraic extension of Q(u,v ),
where u,v are independent transcendentals. Using software such as
Mathematica or Maple, it is relatively straightforward to verify by
formal manipulation that the matrices Φ(gk) satisfy the group rela-
tions, i.e. that Φ extends to a representation of Γ 8. Following the
nomenclature of M. Culler and P. Shalen, we call Φ the tautological
represention of Γ 8 associated to V. A tautological representation
depends of course on a chosen parametrization, i.e. a coordinate
system for the variety; also, two matrix representations are consid-
ered to be equivalent if they agree up to postmultiplication by an
inner automorphism of the target linear group.
The method just described would appear at ﬁrst sight to be remarkably
ad hoc; however, it often works well. It was applied to three representations
ρ1, ρ2, ρ3 given in§4.2 – one in each of the components found in the previous
24 E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
section. It produces tautological representationsRi (i = 1, 2, 3) of the ﬁgure-
eight knot group Γ8 into SL(3,F), where the ﬁeldF is an algebraic extension
of Q(u,v ). Our brief descriptions of the salient properties of theRi are given
mostly without proof; however, the reader can check most of them with the
aid of suitable computer algebra software.
5.1. The ﬁrst component, R1. We use the presentation
Γ8 = ⟨a, b|abbbaBAAB ⟩ ,
where uppercase denotes inverse (see section 2). The group Γ 8 is generated
by meridians ab, abb , and we may take
m =ab , 𝓁 =abABaBAb
as commuting (meridian, longitude) pair. Our choice of parameters for the
variety is
u = tr(A) , v = tr(b) ,
this choice being justiﬁed by the fact that all matrix entries for the tauto-
logical representation lie in Q(u,v ) itself:
a ↦→


0 0 1
1 0 −u
0 1 (−1+v)2(1+v)
u

 and
b ↦→


1 −u3(−2+v)+(−1+v)3(1+v)
u(−1+v)2v −u(−2+v)
−1+v
0 v −v+v3
u
0 u
v−v2 −1

 .
For notational convenience, let us identify a, b, A, Bwith their images
under R1. These elements have the following traces:
tr(a) = (−1 +v)2(1 +v)
u , tr(A) =u , tr(b) =v , tr(B) =v .
On can also compute that
tr(ab ) = u3 + (−1 +v)3(1 +v)2
uv(−1 +v)2 ,
from which it is evident that attempting to assign certain values to the traces
of A, b results in singularities.
The classical hyperbolic representations are those satisfying the constraint
tr(a) = tr( A), and one can compute that there are two boundary unipo-
tent hyperbolic representations, i.e. representations mapping peripheral el-
ements to unipotent matrices. These are as follows:
(u,v ) =
(
−3 + 2
√
3i , 1
2 + 3
2
√
3i
)
and
(u,v ) =
(
−3− 2
√
3i , 1
2− 3
2
√
3i
)
.
25
These form a complex conjugate pair, corresponding to the complete hyper-
bolic structure on the ﬁgure-eight knot complement. The deformation space
of the complete structure has one complex dimension, as in the classical
PSL(2, C) case.
5.2. The other two components,R2 andR3. For the other two varieties,
we choose the standard “parabolic” presentation
Γ8 = ⟨a, b|AbaBabABaB ⟩ ,
and parameters
u = tr(A) = tr(B) , v = tr(a) = tr(b) .
Some matrix entries lie in a quadratic extension of Q(u,v ), namely the ﬁeld
generated by
√
∆, where
∆ = 4 u3 + 4v3−u2v2− 16uv + 16 .
Either choice of square root of ∆ yields a valid representation. We shall
see shortly that these varieties are related via precomposition with an outer
automorphism of the knot group. Here are the tautological representations:
R2
a ↦→


v
2 1 − (1−i)(−16+8uv−2v3−4
√
∆)
8u2−6uv2+v4
1
8(1 + i)(−2u + v2) 1
4(1 + i)v 1
1
16(8− 4uv + v3− 2
√
∆) 1
8(−4u + v2) 1
4(1− i)v


b ↦→


v
2 i (1+i)(−16+8uv−2v3−4
√
∆)
8u2−6uv2+v4
− 1
8(1 + i)(−2u + v2) 1
4(1− i)v i
− 1
16(8− 4uv + v3− 2
√
∆) −i
8(−4u + v2) 1
4(1 + i)v


R3
26 E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
a ↦→


v
2 1 − (1−i)(−16+8uv−2v3+4
√
∆)
8u2−6uv2+v4
1
8(1 + i)(−2u + v2) 1
4(1 + i)v 1
1
16(8− 4uv + v3 + 2
√
∆) 1
8(−4u + v2) 1
4(1− i)v


b ↦→


v
2 1 − (1−i)(−16+8uv−2v3+4
√
∆)
8u2−6uv2+v4
1
8(1− i)(−2u + v2) 1
4(1− i)v −i
i
16(8− 4uv + v3 + 2
√
∆) i
8(−4u + v2) 1
4(1 + i)v


Our ﬁrst observation is that R2 and R3 satisfy the same relationships
with regard to automorphisms of the knot group Γ 8 as those set out in
Proposition 9.2 of [7]. In particular, if τ : Γ 8 → Γ8 is the (non-inner)
automorphism determined by the assignments a↦→a−1ba, b ↦→b, then R3
agrees with R2◦τ up to conjugation by a matrix in GL(3 ,F).
Secondly, the image of R2 (also that of R3) is a copy of the (3 , 3, 4)–
triangle group
T (3, 3, 4) = ⟨α, β, γ|α3 =β3 =γ4 =αβγ = 1⟩ .
Speciﬁcally, if c denotes the commutator abAB , we have
R2(c) =


1 0 0
0 i 0
0 0 −i

 ,
independently of u, v, from which it follows immediately that R2(c) has
order 4. Moreover, one can verify that the images under R2 of ac , cac
each have order 3. Since a, c generate the knot group Γ 8, the result follows
by taking α = R2(ac ) , β = R2(cac )−1 , γ = R2(c). It was previously
known that the images of the representations ρ2, ρ3 were isomorphic to
T (3, 3, 4), see [7].
5.3. A focus on the PU(2, 1) case. As studied e.g. in [7], the representa-
tions with image inside the real group PU(2 , 1) may carry interesting geo-
metric properties. So we seek representations preserving Hermitian forms.
In the case of the ﬁrst component R1, the following condition on traces
holds:
tr(A) = tr(a) , tr(B) = tr(b) .
In particular, we note that since tr(B) = tr(b) =v, the parameterv is forced
to be real for such representations. Then, from tr( A) = tr(a), we obtain
(−1 +v)2(1 +v)
u = u, or u = | (−1 +v)
√
1 +v|z,
27
with z lying on the unit circle.
It is in fact possible to compute a Hermitian matrix H as a function of
the coordinates v, z,
H(v,z ) =


1 r s
r 1 r
s r 1

 ,
whose associated form is respected by the representations just described;
the entries of H lie in an Abelian extension of degree 4 of Q(v, Re(z)), and
are a little too cumbersome for inclusion here. However, for speciﬁc v, z the
signature of H enables one to determine whether the representation takes
values in SU(3) or SU(2, 1), or whether the associated form is degenerate. In-
deed, the representations with degenerate forms occupy some isolated points
in the (v,z )–variety, together with some simple closed curves that separate
SU(3)–representations from SU(2, 1)–representations.
One can compute that the variety R1 gives rise to a single boundary
unipotent representation into PU(2 , 1), obtained by composing the repre-
sentation
(u,v ) = ( −
√
3i, 2)
with the natural projectivization map SU(2 , 1)→ PU(2, 1). The variety R1
also contains the other two lifts of this PU(2, 1)– representation to SU(2, 1),
at
(u,v ) = ( −ω(
√
3i), 2), (u,v ) = ( −ω2(
√
3i), 2) (where ω =e2πi/3).
The other two componentsR2 andR3 each give rise to just one bound-
ary unipotent representation into PU(2, 1), given by (u,v ) = (3, 3).
A necessary condition on traces for a representation in R2 or R3 to
respect a Hermitian forms is
tr(a) = tr(A), tr(b) = tr(B) , i.e. v =u .
Using the same technique as that described at the beginning of this sec-
tion, i.e. invoking LLL together with polynomial interpolation, the following
diagonal matrix:
H =


− 1
8(∆− 16)
(√
∆ +|u|2− 4
)
0 0
0 ∆ − 16 0
0 0 −8
(√
∆ + 4
)


was found, satisfying
Ha−1 = a†H , Hb−1 = b†H (v =u, ∆≥ 0) ,
where the superscript † denotes conjugate transpose, and ∆ = 4 u3 + 4v3−
u2v2− 16uv + 16 = 4( u3 +u3)−|u|4− 16|u|2 + 16. Clearly the condition
∆≥ 0 is required forH to be Hermitian. We note that the form represented
28 E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
byH degenerates at ∆ = 16; in the present contextv =u the corresponding
values of u are 0, 4, 4e2πi/3, 4e4πi/3.
Substituting u = x +iy, v = x−iy (x, y∈ R) in the expression for
∆(u,v ), we obtain (with mild abuse of notation)
∆(x,y ) = −x4−y4− 2x2y2− 24xy2 + 8x3− 16x2− 16y2 + 16 .
We have therefore established that representations respecting Hermitian
forms occur in the bounded complementary regions in the ( x,y )–plane of
the curve ∆(x,y ) = 0, see Figure 4. The SU(3) representations lie in the
central complementary region, and the SU(2 , 1) representations lie in the
three petals. Corresponding Hermitian representations occur also on the
curve itself, except for singularities at the three self-intersection points of the
curve, where representations are not deﬁned. The quantity ∆ has geometric
signiﬁcance in that it is related to the Brehm shape invariant [3] of the
triangle in the associated homogeneous space (complex projective plane CP2
or complex hyperbolic plane CH2), whose vertices are the ﬁxed points of the
elliptic isometries α, β, γ.
/Minus4 /Minus2 0 2 4 6
/Minus4
/Minus2
0
2
4
Figure 4. SU(3) and SU(2, 1) representations in R2
