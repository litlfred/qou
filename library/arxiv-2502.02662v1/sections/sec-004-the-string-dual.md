---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-004-the-string-dual
section_title: "The String Dual"
section_number: null
pages: 6-8
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
In this subsection, we discuss the string dual to the extended Hurwitz theory [9]. See also [10].
Firstly, we describe the string theory, which is a theory of two-dimensional gravity coupled to
two-dimensional matter. The matter theory is aN = (2, 2) supersymmetric sigma model with
world-sheet Σ and a two-dimensional, closed target space X of genus G. The A-twist of the
sigma model is a topological field theory whose operators are in one-to-one correspondence
with the de Rham cohomology of the target space. We denote the observable associated
with the volume form on X by ω. The topological matter model was fully solved in [17].
Consider next the topological string theory obtained by coupling the model onX to topological
gravity [17, 18]. Its observables are given by the gravitational descendants of the observables
of the X model. We will focus on the stationary sector, namely on the half infinite tower of
descendants of the volume form. We denote the corresponding operatorsτk wherek∈ N labels
the gravitational descendant. Their correlation functions compute Gromov-Witten invariants,
which are defined by integration of classes on the moduli space of Riemann surfaces of genus
g with a number of marked points equal to the number of operator insertions [9, 17, 19]. We
stress that the observablesτk may be thought of as vertex operators. Indeed, they are defined
in terms of the pullback of the volume form on the target space to the covering space, which
is identified with the world-sheet of the theory.5 In string theory, every vertex operator comes
with a factor of the string coupling gs. Therefore, we can identify vertex operators in this
theory as
Vk =gsτk. (2.12)
4Note that on the torus, the genus of the Riemann surface is determined solely by the insertions. The
identificationp =g2G−2
s yields a trivial chemical potentialp = 1 and the normalization of partial permutations
must be put in by hand.
5We note that our identification of the world-sheet of the theory with the covering space is in accord with
the description of Hurwitz theory as a symmetric orbifold and the identification of the world-sheet of the string
in that context [20].
5
An insertion of an operatorVk on a world-sheet generates a single string state. The correlators
of the string theory may then be written as
⟨Vk1··· Vkn⟩ =
X
g
g2g−2
s ⟨Vk1··· Vkn⟩g, (2.13)
where the sum is over the genus g of the world-sheet.
A backbone to our approach is that these Gromov-Witten invariants are equal to fixed-
degree correlation functions of completed cycles in Hurwitz theory [9]. Completed single
cycles are linear combinations of orbits of partial permutations defined in [9]. They form a
multiplicative basis of the algebra. We write
¯Ak =
X
r
ρk,rAr, (2.14)
where the sum is over partitionsr of varying degree.6 The coefficientsρk,r vanish when|dr|>k
and yield a Kronecker delta for |dr| =k. The operator dictionary in fixed-degree correlation
functions between the extended Hurwitz theory and its string dual reads [9]
¯Ak+1
k! ↔τk. (2.15)
Plugging this duality into the string correlators (2.13), we translate an integral over moduli
space to a topological quantum field theory correlator:
⟨Vk1··· Vkn⟩ =
X
r1,...,rn
Y
i

g
ki+1−|dri|
s
ρki+1,ri
ki!

⟨A′
r1··· A′
rn⟩. (2.16)
Note that the factors of the string couplinggs that appear in equation (2.16) are overall factors
weighting different correlators. Therefore, they do not affect the genus expansion structure
of a given correlator. Furthermore, the completed cycles appear as subdominant corrections
to the lore according to which single cycles in a symmetric orbifold theory are dual to single
string states [10].
Conversely, since the completed cycles form a basis of the algebra of partial permuta-
tions, equation (2.15) can be inverted to express the correlators of simple partial permutation
in terms of vertex operators expectation values. We first define the coefficients ζr,s as the
coefficients of the partial permutations in the basis of completed cycles
Ar =
X
s
ζr,s
Qℓ(s)
i=1(si− 1)!
¯As. (2.17)
We then write the substitution rule
A′
r↔
X
s :
|ds|≤|dr|
g|dr|−|ds|
s ζr,sVs−1, (2.18)
6We use the charactersk,l,m,n of the latin alphabet to denote integers and the characters r,s,t to denote
partial permutations. Permutations are denoted by Greek letters.
6
where the Vs−1 := Qℓ(s)
i=1Vsi−1 are products of single string vertex operators. Correlation
functions involving such multi-vertex operators Vs are evaluated on the moduli space that
exhibits as many marked points as there are single insertions Vsi. Physically, such multi-cycle
vertex operators are identified with multi-string states. Note that completed cycles also include
single cycle corrections [9] which should survive in the connected correlators. Therefore, the
corrections from completed cycles do not trivialize when we consider connected correlators.
We stress that the identification of the extended Hurwitz correlators with the Gromov-
Witten correlation functions [9] is an important non-trivial step in the process of identifying
a string dual to two-dimensional Yang-Mills theory. It identifies an ordinary topological field
theory correlator with a well-defined integral over the moduli space of Riemann surfaces.
That these highly different concepts coincide is proven through equivariant localization [9,
21]. Exploiting this non-trivial correspondence is the second new tool that distinguishes our
approach from the literature.
To close this section, we explain how boundaries with prescribed boundary conditions
can be incorporated in the gauge/string duality. Consider a target space X with m marked
points. Hitherto, we have thought of marked points as sites of bulk operator insertions. The
operator insertions in the gauge theory translate to vertex operators in the string theory.
The requirement that a basis of bulk string vertex operators be multiplicative then imposes
that single cycles be completed. However, in this simple topological setting, these operator
insertions can equivalently be interpreted as boundaries (with an associated holonomy). The
marked points then correspond to boundary conditions 7 and there is no need to complete
the cycles. In other words, boundary conditions in a string theory should be treated as
standard Hurwitz insertions on marked points. In Gromov-Witten theory, these insertions (in
contrast to the bulk gravitational descendants of cohomology classes) are described as relative
Gromov-Witten theory. The relative theory computes Gromov-Witten invariants on surfaces
with further specified ramification profiles ηi in m marked points – see e.g. [9] –:
⟨
sY
i=1
τki,η 1,...,η m⟩g,d. (2.19)
To summarize, we have described two dual points of view: boundary conditions for open
strings specified by ordinary partial permutations and closed string states corresponding to
completed cycles.
Relative Gromov-Witten theory is particularly useful to study Wilson lines. As we shall
review in section 5.5 in the context of Yang-Mills theory, Wilson lines are computed by gluing
manifolds with boundaries and specifying a character of the gauge group on that boundary.
It will be more natural to think of this procedure in terms of boundaries rather than bulk
operator insertions.
