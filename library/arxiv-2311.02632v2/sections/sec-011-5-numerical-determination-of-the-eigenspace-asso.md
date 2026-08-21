---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-011-5-numerical-determination-of-the-eigenspace-asso
section_title: "Numerical determination of the eigenspace associated to 1"
section_number: 5
pages: 32-37
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
Having established that the first eigenvalue of the Fricke-Macbeath surface has a
multiplicity of 7, our objective in this section is to numerically determine which 7-
dimensional representation of Aut(X ) = ∆ +(2, 3, 7)/Γ corresponds to the eigenspace
associated toλ1. There are four 7-dimensional irreducible representations of Aut(X )∼=
PSL2(8). Refer to Table 3 for the character table of Aut( X ). You can find the GAP
code in Appendix B to obtain the character table. See [CCN +85, p. 6] for more
information about the character table. In the character table, A,B,C,D,E, andF are
defined as follows:
(5.1)
A =ζ3
7 +ζ4
7, B =ζ2
7 +ζ5
7, C =ζ7 +ζ6
7,
D =−ζ4
9−ζ5
9, E =−ζ2
9−ζ7
9,
F =ζ2
9 +ζ4
9 +ζ5
9 +ζ7
9.
SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURF ACE 33
Here, ζn =e2πı/n.
1A 2A 3A 7A 7B 7C 9A 9B 9C
χ1 1 1 1 1 1 1 1 1 1
χ2 7 -1 -2 0 0 0 1 1 1
χ3 7 -1 1 0 0 0 D F E
χ4 7 -1 1 0 0 0 E D F
χ5 7 -1 1 0 0 0 F E D
χ6 8 0 -1 1 1 1 -1 -1 -1
χ7 9 1 0 A C B 0 0 0
χ8 9 1 0 B A C 0 0 0
χ9 9 1 0 C B A 0 0 0
Table 3. Character table of Aut( X ) ∼= PSL2(8); the values of
A,B,C,D,E, and F are given in (5.1)
GAP enumerates representative elements from each conjugacy class as follows:
1A. id
2A. a2b(ba2)2b3a2b
3A. a
7A. a2b(ba2)2b3a2
7B. b4a2(ba2b)2
7C. a2b3(ba2)2b2
9A. (ab2a)2ab3a
9B. a(ba2b)2b2a2
9C. ab2(b2a2)2b
For the actions of the generators a and b on D, recall (3.5) and (3.6).
It is noteworthy that the outer automorphism group of PSL 2(8) has order 3. An
outer automorphism interchanges the conjugacy classes of elements of order 9 with each
other and similarly for those of order 7. Consequently, there is an inherent ambiguity in
assigning specific labels like 9A, 9B, 9C to elements of order 9, and similarly, 7A, 7B,
7C to those of order 7. Throughout this section, we will adhere to the aforementioned
convention for naming conjugacy classes.
Here we present a numerical method to compute the character of a representation
obtained from a set of eigenfunctions. Assume that we have a set of eigenfunctions,
denoted as L ={f1,...,f n}, which have close eigenvalues. These eigenfunctions are
expected to form a basis for a representation of Aut(X ), which may not necessarily be
irreducible.
One of the core assumptions in our approach is that we can approximate the value
fi(z) for a given point z∈F . For instance, by employing the finite element method
34 CHUL-HEE LEE
onF, along with periodic boundary conditions determined by side-pairing transfor-
mations, we can achieve such approximations for eigenfunctions of hyperbolic surfaces.
The application of these methods to the Bolza surface, a genus 2 Riemann surface with
the highest number of symmetries, has been introduced in [AS89]. Cook’s disserta-
tion [Coo18] provides FreeFEM++ [Hec12] code to compute low-lying eigenvalues and
eigenfunctions for certain compact Riemann surfaces of low genera, albeit not including
the Fricke-Macbeath surface. For further details, see appendices C, D, and E in [Coo18].
Meanwhile, an alternative approach detailed in [SU13] delivers exceptionally accurate
numerical eigenvalues and eigenfunctions. Although this method promises accuracy,
its implementation seems to be quite challenging.
For our numerical evaluations, we have utilized Mathematica [Inc20]. Within this
environment, the NDEigensystem function serves as an instrumental tool for determin-
ing the eigenvalues and eigenfunctions of differential operators over a given region. A
distinctive capability of this function is its adeptness in handling periodic boundary
conditions. With the PeriodicBoundaryCondition option, the function allows specific
boundary pairs to be treated as if they were identical.
To begin, we initiate the following preliminary procedures:
• Select an interior pointz0 withinF that is not fixed by any element of ∆(2, 3, 7).
Additionally, ensure that the orbits of z0 under ∆(2, 3, 7) do not intersect the
boundary ofF. An appropriate point can readily be located within the funda-
mental triangle of ∆(2, 3, 7), as shown in Figure 3.
• Determine representatives S = {M1,...,M d} ⊆ ∆+(2, 3, 7) for Aut(X ) =
∆+(2, 3, 7)/Γ such that each zk := Mkz0 lies within F for all k∈{ 1,...,d }.
Here, d =| Aut(X )|. We can find such a list, for example, as follows :
– Enumerate elements of the Coxeter group ∆(2, 3, 7) based on length.
– Collect all elements M∈ ∆(2, 3, 7) of even length such Mz 0 is contained
in the interior ofF.
– Given our choice ofz0, these collected elements serve as representatives for
Aut(X ) = ∆+(2, 3, 7)/Γ.
• For each eigenfunctionf inL, compute the approximate values of f(zk) for all
k∈{ 1,...,d }.
GivenMl∈S and fi∈L, we want to express the transformed function Ml·fi as a
linear combination of{f1,...,f n}, meaning that
(Ml·fi)(z) =fi(M−1
l z) =
nX
j=1
ρ(Ml,i,j )fj(z), z∈F .
Here, the matrix (ρ(Ml,i,j ))i,j serves as the representation matrix for Ml. Our goal is
to approximate these matrix entries, treating {ρ(Ml,i,j )} as the unknowns we want
to determine.
SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURF ACE 35
For a given pair (l,i ), the equation
(5.2)
nX
j=1
ρ(Ml,i,j )fj(zk) =fi(M−1
l zk), k= 1,...,d
yields d relations with n unknowns{ρ(Ml,i,j ) : j = 1,...,n }. Therefore, when d
significantly exceeds n, we obtain an overdetermined system of linear equations for
those unknowns. For our particular case, the values are d = 504 and n = 7. To handle
such overdetermined systems, a common approach is to use the least squares method.
This method seeks to minimize the sum of the squares of the residuals, which are the
differences between the left and the right sides of (5.2). By applying this method, we
can approximate the values of{ρ(Ml,i,j )}.
To enhance the system’s robustness further, one could perturb the initial point z0 to
obtainz′
0 and then consider its orbits z′
k under the action of Aut(X ). This leads to an
extended set of relations, in addition to those in (5.2):
nX
j=1
ρ(Ml,i,j )fj(z′
k) =fi(M−1
l z′
k), k= 1,...,d.
By doing so, we can also increase the number of equations, even when d is small
compared to n.
Note that on the right-hand side of (5.2), M−1
l zk = M−1
l Mkz0 may not be a point
inF. Since our approach relies on knowing approximate values of fi(zj) for orbits
zj∈F of z0, calculating fi(M−1
l zk) presents a challenge. Given ( l,k ), we need to find
p∈{ 1,...,d } and γ∈ Γ such that
(5.3) γM−1
l Mk =Mp.
Once we find ( p,γ ), we can simply set fi(M−1
l zk) = fi(Mpz0) = fi(zp) due to the
Γ-invariance offi.
Equation (5.3) can be equivalently stated as:
γM−1
l Mkz0 =Mpz0.
This formulation is essentially about moving the point M−1
l Mkz0 = M−1
l zk into the
fundamental domainF through the action of Γ. Notably,F is also the Dirichlet domain
D(0) from Theorem 3.8. In [Voi09], Voight explored various algorithms related to such
fundamental domains for Fuchsian groups. Of particular interest is an algorithm that,
when given a point z∈ D, returns a point z′∈F and an element γ∈ Γ such that
z′ =γ(z). This algorithm is detailed further in [Voi09, Algorithm 4.3]. In the context
of our study, we begin by setting z =M−1
l zk. Subsequently, we identify a side-pairing
transformationγi such thatγiz is closer to the fundamental polygonF than the original
location of z, meeting the condition:
dD(0,γiz)≤dD(0,z ).
36 CHUL-HEE LEE
As long as the pointz is not located inside the fundamental domainF, such a transfor-
mationγi exists. This procedure can be iterated until we identify a Γ-orbit of z inside
F. By employing this method, we can effectively relocate z toF using the generators
{γi} of Γ. While determining γ and Mp for (5.3) may involve numerical calculations,
we can verify its correctness in a symbolic manner using (3.1).
Once we apply the method described above to determine the 7-dimensional repre-
sentation Vλ1 formed by eigenfunctions with eigenvalue λ1, we obtain the following
numerical values for its character χλ1:
1A 2A 3A 7A 7B 7C 9A 9B 9C
7.0000 −1.0163 0.9614 0.0778 0.0231 0.0059 −1.4985 −0.3453 1.8829
Recall that the inner product of two characters χ,χ′ of G are defined by
⟨χ,χ′⟩ = 1
|G|
X
g∈G
χ(g)χ′(g).
When we compute the inner product of characters χλ1 andχi, we obtain the following
approximate values of mi =⟨χλ1,χi⟩ for each i:
i 1 2 3 4 5 6 7 8 9
mi 0.0133 0.0150 0.0043 −0.0037 0.9927 0.0152 −0.0183 −0.0119 0.0088
Note that mi is the multiplicity of χi in the decomposition of χλ1 into irreducible rep-
resentations. Given that these values are close approximations of integers, it becomes
straightforward to guess their exact integer values. Hence we propose the following
conjecture:
Conjecture 5.1. Let Vλ1 be the 7-dimensional representation of Aut(X ) formed by
eigenfunctions with eigenvalue λ1. The character of Vλ1 is equal to χ5.
From our numerical computations, we have obtained the following 7 approximate
values for λ1,...,λ 7:
1.25065, 1.25336, 1.25336, 1.26103, 1.26103, 1.28662, 1.38342.
Despite the lack of precision in these values, it is evident that we can still obtain
convincing evidence for the true values ofχλ1. Similarly, we have obtained the following
9 approximate values for λ8,...,λ 16:
2.05821, 2.0602, 2.06123, 2.06488, 2.0661, 2.08243, 2.09857, 2.09857, 2.2991.
While the accuracy of these values remains uncertain, the eigenfunctions for these
eigenvalues appear to span a 9-dimensional representation of Aut( X ). Its character
seems to be a good approximation to χ9 in Table 3.
SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURF ACE 37
