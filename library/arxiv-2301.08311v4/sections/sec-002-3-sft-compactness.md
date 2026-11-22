---
doc_id: arxiv-2301.08311v4
doc_title: "FLOER COHOMOLOGY AND HIGHER MUTATIONS"
section_id: sec-002-3-sft-compactness
section_title: "SFT Compactness"
section_number: 3
pages: 14-30
source_pdf: 2301.08311v4.pdf
source_sha256: 385139c69e18f5b0
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND HIGHER MUTATIONS — We extend the construction of higher mutation as introduced in [PT20] to local higher mutation, which is applicable to a larger class of monotone Lagrangians."
---
In this section, we will explain a version of the neck-stretching procedure where the Lagrangian
passes through the neck region and prove a compactness result with assumptions on the Legendrian
that models the Lagrangian in the neck region.
Bourgeois, Eliashberg, Hofer, Wysocki and Zehnder [BEH+03] proves compactness result for
closed holomorphic curves under neck-stretching for Morse-Bott Reeb dynamics. Abbas [Abb14]
proves compactness for open holomorphic curves with boundary on cylindrical Lagrangians for
the case of non-degenerate Reeb dynamics. We prove a version of the compactness result for
neck-stretching along a contact type hypersurface Z with a free S1 action that generates the Reeb
field for discs with boundary on a cylindrical Lagrangian that intersects Z at the Legendrian Λ in
the neck region such that Λ is a finite cover of an embedded Lagrangian in Z/S1. Notice that the
case of stretching along the boundary of a Darboux ball where we perform a local mutation falls in
this case since the boundary sphere S2n−1 has a natural S1 action that generates the Reeb field,
the Lagrangian intersects the sphere in two disjoint tori that descends to the Clifford torus in Pn−1.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
15
3.1. Setup. We begin by setting the notations and conventions for this section. Let (W, ω, J) be a
closed symplectic manifold and Z be a compact codimension 1 submanifold of contact-type, i.e. in a
tubular neighbourhood N ∼= (−ϵ, ϵ)×Z, there is a contact form λ on Z such that ω = d(ektλ) where
t ∈(−ϵ, ϵ) and k is a positive integer. In our case, we assume Z separates W into two connected
components for simplifying the combinatorial structure, but this is not a necessary assumption. Let
L be a Lagrangian such that in the tubular neighbourhood of the hypersurface Z, L is translation
invariant over a Legendrian, i.e. there is a Legendrian Λ ⊂Z such that N ∩L = (−ϵ, ϵ) × Λ, we
call such Lagrangians to be cylindrical near Z. Assume J is a compatible complex structure on
(W, ω) such that it is translation invariant on N and is adjusted to the form ω in the SFT sense,
i.e., J ∂
∂t = R where R is the Reeb field of λ . Call the metric induced by the compatible pair (ω, J)
on W to be gW . Assume there is a free S1 action on Z that generates the Reeb field, the quotient
Y = Z/S1 has a natural symplectic form induced from dλ. Assume Λ is closed under multiplying
by −1 from the S1 action (i.e. −Λ = Λ), projects to an embedded Lagrangian LY in Y and the
projection map is a finite cover.
W
L
(−ϵ, ϵ) × Z
(−ϵ, ϵ) × Λ
Figure 7. Symplectic manifold W and Lagrangian submanifold L with neck pieces
of length 2ϵ
Example 3.1. A sphere S2n−1
r
of radius r centred at 0 inside Cn has a tubular neighbourhood Φ :
(−ϵ, ϵ) × S2n−1
r
→Cn given by Φ(s, p) = esp. Clearly Φ∗J0 is a translation invariant almost complex
structure as scaling is a biholomorphism in Cn. Moreover, Φ∗ω0 = d(e2sλ) where λ =
λ0
P |xi|2+|yi|2 .
Here ω0, λ0 are the standard symplectic and contact forms respectively.
Note that Tγ for an admissible γ is cylindrical over disjoint union of two Legendrian tori. This
follows from the fact that fa(Tz)) = Tanz where fa is the scaling map, multiplication by a.
3.1.1. Neck stretching. We now explain the process of neck stretching. The τ−stretched manifold
W τ is defined by removing the tubular ‘neck’ around Z and replacing with a 2τ sized neck as defined
below -
W τ = (W \ N) ∪(−τ, τ) × Z
|
{z
}
gluing Z at the ends
.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
16
Since J is translation invariant on N, W τ can be given a complex structure Jτ adjusted to ω by
requiring Jτ on the extending the translation invariant complex structure J|N . We define the τ−
stretched Lagrangian Lτ similarly as W τ.
Lτ = (L \ N) ∪(−τ, τ) × Λ
|
{z
}
gluing Λ at the ends
.
From our assumption, the manifold with the hypersurface removed W \ Z has two connected
components.
Thus if we remove the neck N from the manifold W, there are two connected
components of W \ N, call the connected components Win, Wout. Clearly, all the τ stretched
manifolds are diffeomorphic to W by choosing a diffeomorphism between the intervals (−ϵ, ϵ) and
(−τ, τ). The metric on the stretched manifolds is defined to be gW away from the necks and
cylindrical extension of the compatible metric on Z in the neck piece.
3.1.2. Energy. For establishing compactness of a family of objects, it is essential for the family to
be bounded in some sense. The notion of energy has been used to bound families of J−holomorphic
curves, for SFT, there is a similar notion of energy which we describe now.
There are more than one way of defining energy for the neck-stretched manifolds. Cielibak-Mohnke
[CM05] defines it to be the symplectic area induced from a particular choice of diffeomorphism
between W and W τ. Bourgeois et. al. [BEH+03] defines energy analogous to Hofer energy. We will
use the approach in op. cit. for dealing with energy , see section 9.2 in [BEH+03].
We recall the definition of Hofer energy. Given a symplectic manifold M with a cylindrical end
R+ × Z where Z is a contact type hypersurface i.e. there is a contact form λ on Z such that
ω = d(etλ). Denote the compact complement of the cylindrical end by M. The Hofer energy is of a
curve u : Σ →M is defined as follows :
EH(u) =
Z
u−1(M)
u∗ω + supϕ∈T
Z
u−1(R+×Z)
u∗d(eϕ(t)λ),
where T is the family of increasing diffeomorphism from R to (0, 1) .
The horizontal energy EHor refers to the energy of the projection to Z in the cylindrical end
along with the energy away from the cylindrical end. The formula for the horizontal energy is
EHor(u) =
Z
u−1(M)
u∗ω +
Z
u−1(R+×Z)
u∗p∗
Zdλ.
Here pZ is the projection on to Z. It is clear that finiteness of Hofer energy implies finiteness of
the horizontal energy. In SFT literature this is commonly called the Eω energy, but we avoid this
notation since for us ω is a symplectic form and not a part of stable Hamiltonian structure. The
energy for the stretched manifold is defined similarly, let u : Σ →W τ be a curve, the energy is
defined by
E(u) =
Z
u−1(W)
u∗ω + supϕ∈T
Z
u−1((−τ,τ)×Z)
u∗d(eϕ(t)λ).
where W is the compact manifold obtained by removing the tubular neighborhood N from W and
T is the family of increasing diffeomorphism from (−τ, τ) to (0, 1).
Remark 3.2. Lemma 9.2 in [BEH+03] proves that the horizontal energy EHor can be used to bound
the total energy of holomorphic maps to (W τ, Jτ). More precisely, there exists a C > 0 depending
only on W, Z, λ and not on τ such that E(u) < CEHor(u) for all holomorphic u : S →(W τ, Jτ).
Later, this lets us use EHor bounds to compactify moduli of maps to neck-stretched manifold.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
17
W τ
Z × (a, b)
W
Z × (−τ, τ)
c
Win
c
Wout
Z × R
Figure 8. Breaking of W
3.1.3. Broken manifold and broken discs. The geometric objects that are obtained as a result of
neck stretching can be intuitively imagined to be broken manifolds, which we explain in detail below.
As before, assume (W, ω, J, L) be a symplectic manifold with a contact type hypersurface, Z such
that J, L are cylindrical near the hypersurface Z. Conceptually as τ →∞, the neck of the manifold
gets longer and longer and one can view the ‘limit’ to be given by adding positive and negative
symplectization of Z to the two boundaries in W \ Z. If we further assume that the hypersurface Z
divides the manifold W into two connected components W in, W out with contact type boundaries, a
broken manifold W[k] with k necks is given by the collection
d
Win, R × Z, R × Z, R × Z, . . .
|
{z
}
k times
, [
Wout,
where b
X denotes symplectization of the contact type boundary of the manifold X and Wi refers to
either the ith neck piece or the corresponding symplectizations. When we want to refer to a broken
manifold without specifying the number of necks, we use the notation W.
Similar to a broken symplectic manifold, one has a notion of broken Lagrangian submanifold in
a broken symplectic manifold. We can construct L from a Lagrangian L if we assume that L is
cylindrical near the hypersurface Z. We define the broken Lagrangian L[k] with k−necks to be the
collection
d
Lin, R × Λ, R × Λ, R × Λ, . . .
|
{z
}
k times
, d
Lout,
where Lin and Lout denote the intersection of L with Win, Wout respectively and the hat b denotes
the extension to the symplectization by the cylinder of the Legendrian Λ and Li refers to the ith
neck piece.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
18
in
in
1
out
out
W[1]
Figure 9. Broken disc in W[1]
Definition 3.3 (Broken disc). A broken disc with k−necks (u, D) is a map from a nodal disk with
marked points D to a broken manifold with k necks with the following properties.
• D is a nodal disc with labels l ∈{in = 0, 1, 2, . . . , k, out = k + 1} such that neighboring discs
have labels differing at most by 1. We designate some nodes to be “puncture nodes” that
are the nodes in the disc between two components with different labels.We write the nodal
disks as D = (Din, D1, . . . , Dout) where D refers to a collection of discs.
• u = (uin, u1, . . . , uout) is a map from D to W[k] such that ui is a map from Di to Wi with
boundary on Li and near the puncture nodes of D between components of differing label ui
and ui+1 asymptote to the same Reeb chord or Reeb orbit.
• (Stability) for all i ∈[1, . . . , k], at least one of the component in each neck Di has to be a
non-trivial strip, or have enough markings to make it stable.
Remark 3.4. The labels in and out are chosen to refer to the “inside” and “outside” where inside
means where we do a local mutation and outside means where we don’t make any changes.
Now that we have defined broken discs, we will proceed to define the notion of convergence of
broken discs. We say a sequence of discs un : D2 →(W n, Jn, Ln) converge to a broken disc (u, D)
with k−necks if the following holds:
• there is a sequence of maps ϕn : Dn →D such that they are biholomorphic diffeomorphisms
except away from a certain circle or line that might get mapped to a node in D
• there is a sequence tn
i ∈R such that un
i ◦ϕ−1
n + tn
i converges in C∞to ui on every compact
subset. Here +t refers to translation in the R direction by t
Similarly, we say a sequence of broken disks (un, Dn) with k necks converges to a broken disk (u, D)
with k′ > k necks if the following hold:
• There is a sequence of maps ϕn : Dn →D such that they are biholomorphic diffeomorphisms,
except away from certain circles or lines that might get mapped to a node in D.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
19
• There is a sequence tn
i ∈R such that un
i ◦ϕ−1
n + tn
i converges in C∞to ui on every compact
subset. Here +t refers to translation in the R direction by t .
3.2. Asymptotic convergence to Reeb chords. In this subsection, we show that we can obtain
asymptotic data near the puncture nodes if the broken disc has finite Hofer energy. To that end, we
prove a version of asymptotic convergence of pseudoholomorphic strips in R × Z with finite Hofer
energy with boundary on Λ.
We start with recalling the assumptions on the contact hyper surface and the complex structures.
(Z, λ) is a closed contact manifold with contact form λ such that there is a free S1 action on Z that
generates the Reeb field1 i.e. the quotient Y = Z/S1 has an natural symplectic form induced from
dλ. Let Λ be a Legendrian in the contact manifold Z that is closed under action of −1 from the S1
action (i.e. −Λ = Λ). Also assume that the Legendrian Λ projects to an embedded Lagrangian LY
in Y and the projection map is a finite cover. Clearly, the Reeb dynamics of the contact form λ is
Morse-Bott in the sense of [Bou02].
We make the following assumptions on the complex structure. J is an almost complex structure
on R × Z such that J is translation invariant and is adjusted to the contact form λ. Thus, the
almost complex structure J descends to a compatible almost complex structure on (Y, dλ) that
makes the projection πY : R × Z →Y a holomorphic map. The complex structure J induces a
cylindrical metric on R × Z, call that metric gcyl.
Now, we explain our goal of this subsection in details. We begin by explaining the strips that
model the asymptotics of a holomorphic strip with finite Hofer energy. We define the map uγ on a
strip as follows
uγ(s, t) = (ms, γ(mt)),
where γ is a Reeb chord with end points on Λ and m > 0 is the length of the Reeb chord γ. From the
definition, we see that uγ is invariant of the R action on the target R × Z. We call such translation
invariant strips over Reeb chords trivial strips.
We can use classical removal of singularity and exponential convergence results of J holomorphic
strips to conclude exponential convergence of strips in the compact manifold Y . Since LY is a
compact embedded Lagrangian in the symplectic manifold Y , we have that there is a number δY > 0
such that any finite-energy pseudoholomorphic half-strip v : [0, ∞) →Y with boundary on LY , the
strip v converges to a point in the Lagrangian LY exponentially fast with speed O(e−δY s) where
(s, t) is the standard coordinate on [0, ∞). Rigorously, there is a C > 0 and p ∈LY such that
d(v(s, t), p) < Ce−δY s. Let iΛ = inf ( {δY } ∪{θ ∈(0, 2π)| ∃p ∈Λ such that eiθ.p ∈Λ}). Clearly
iΛ > 0 since Λ is a finite cover of LY and LY is compact.
Theorem 3.5 (Exponential Convergence). For any δ ∈(0, iΛ) and holomorphic strip u : [0, ∞) ×
[0, 1] →R × Z , that satisfies the following,
• EH(u) < ∞,
• u satisfies the boundary condition u ( [0, ∞) × {0, 1}) ⊂R × Λ,
• the projection on R , πR(u) is unbounded;
there is an s0 > 0, a trivial strip uγ over a Reeb chord γ and a C > 0 such that
(3.2.1)
dcyl(u(s, t), uγ(s, t)) < Ce−δs
∀s ≥s0.
We will break the proof of the theorem in the following steps.
1In literature such contact spaces are also called pre-quantum bundles
FLOER COHOMOLOGY AND HIGHER MUTATIONS
20
• Step 1 : Compactify R × Z to a symplectic manifold N with compatible almost complex
structure such that R × Λ compactifies to a cleanly self intersecting Lagrangian L in N.
• Step 2 : Show that πR(u) diverges to ±∞where πR is the projection of R × Z to R.
• Step 3 : Extend u to a map u to N with boundary on L.
• Step 4 : Use analysis done in [Sch16] to conclude convergence in N.
• Step 5 : Get convergence in cylindrical metric from convergence in N.
R × Z
C∗fiber
{r} × Z
Y
Figure 10. R × Z as a C∗fibration
Proof. Step 1 : Compactification of target
We will compactify our target manifold by adding two copies of the symplectic manifold Y . Since
Z is a principal circle bundle over Y , the cylinder R × Z is a R × S1 bundle on Y . The transition
functions between trivializations of R × Z over the base Y is given by rotation action of S1, thus
the cylinder R × Z can be viewed as a C∗bundle over Y . Moreover, we can extend this bundle to a
CP1 bundle over Y by compactifying each fiber to a CP1 and using the induced transition functions,
call this compactification N. Thus, N is a CP1 bundle over the base Y . Clearly N is compact as
Y is compact. Denote the zero section of Y by Y0 and the infinity section (y 7→(y, ∞) in each
trivialization) by Y∞. The complex structure J extends naturally to a complex structure JN on N
that restricts to the standard complex structure on the CP1 fibers. We can define a symplectic form
ωN that is compatible with JN by defining it in each trivialization CP1 × U for U open set in Y as
following,
ωN =

ωFS
0
0
dλ

,
where ωFS is the Fubini-Study form. The form ωN is a well-defined symplectic form on N as the
transition functions of N seen as a CP1 fibration are given by the rotation action of the S1 on
CP1. One can check from the construction of ωN and JN that they are compatible from a direct
computation.
We describe the closure of the cylindrical Lagrangian in the compactified symplectic manifold.
Denote the closure of the cylindrical Lagrangian R × Z in N by L. We can check that L is obtained
by adding LY in the 0 and infinity divisor of the CP1 fibration to R × Λ. Indeed, a trivialization
CP1 × U of N over some open U in Y such that U ∩LY is nonempty, we see that
L ∩(CP1 × U) = {0, ∞} × (U ∩LY ) ∪((CP1 × U) ∩(R × Λ)).
FLOER COHOMOLOGY AND HIGHER MUTATIONS
21
R × Z
Y∞
Y0
N
Figure 11. Compactification of R × Z to N
This directly shows adding two copies of the Lagrangian LY to the cylinder R × Z produces the
closure L. Since the Legendrian Λ is closed under the action of −1, we see that L cleanly self
intersects at LY in the 0 and infinity divisor. Call the intersection loci LY0, LY∞respectively.
Step 2 : Divergence of πR(u)
We now show that near the ends of the strip, the image escapes to infinity. We will prove that in
the limit as s →∞, u diverges to either ∞or −∞. The proof employs a version of monotonicity
lemma (Proposition 2.69 [Abb14]) and gradient-boundedness of finite Hofer energy maps.
We state the monotonicity lemma without proof.
Lemma 3.6 (Proposition 2.69 [Abb14]). Let (W, ω) be a compact symplectic manifold, E0 > 0, let
J be an ω-compatible almost complex structure and let L ⊂W be a Lagrangian submanifold. Let
D =

z ∈C

|z| < 1
	
, N ∈N and Ik = {eit|2π
N (k −1) ≤t ≤2π
N k} ⊂∂D for k = 1, . . . N. Then there
are constants δ0, c0 > 0 such that the following holds:
Let u : D →W be a J-holomorphic disk with E(u) ≤E0 so that u(Ik) ⊂L for k even. Let
z0 ∈D \ ∪kI2k+1 and 0 < r < δ0 so that u(∪kI2k+1) ⊂W \ Br(u(z0)). Then
Z
u(D)∩Br(u(z0))
ω ≥c0r2.
Another ingredient in the proof of divergence of πR is a slight modification of Proposition 2 in
[Bao12]. Define the norm ∥∥L∞for a map u : H →R × Z as follows
∥∇u∥L∞:= sup (s,t)∈H|∇u(s, t)|,
where the norm | · | is taken with respect to the standard Euclidean metric on H and cylindrical
metric on R × Z.
Lemma 3.7. If v : H →R × Z is a holomorphic map with boundary on R × Λ with zero horizontal
energy, Eω(v) = 0, and bounded derivative, ∥v∥L∞< ∞, then v is a constant map.
Proof. Since Eω(v) = 0, we have that πY (v) is a constant map. Thus, the map v lies in a fiber
R × S1. The map v maps the boundary R ⊂H to R × {∗} for some ∗∈S1 . Since H is simply
connected, v factors as follows v = eh where h : H →C is a holomorphic map. The map h sends the
boundary R ⊂H to R + iy for some y ∈R. We can use a doubling trick using Schwarz reflection to
FLOER COHOMOLOGY AND HIGHER MUTATIONS
22
extend h to C, thus we can extend v to a map from C. The rest of the proof follows from Proposition
1 in [Bao12].
□
Lemma 3.8 (Proposition 2 [Bao12]). Let u : R × [0, 1] →(R+ × Z, R+ × Λ) be a holomorphic map
with finite Hofer energy, EH(u) < ∞, then we have ∥∇u∥L∞< ∞.
Proof. The proof is the same as the proof of Proposition 2 in [Bao12]. The only change one needs
to do is to use Lemma 3.7 in place of Proposition 1 when the rescaled maps converge to a map on
H.
□
The idea behind the proof of divergence is that if a semi-infinite strip u does not diverge to
infinity, it needs to keep coming back to some compact subset of R × Z. The monotonicity lemma
states that every time the strip comes back into such a compact set, there is a ‘cost of energy’,
hence a strip with finite energy can’t keep coming back to any compact subset. We now state and
prove the required divergence.
Lemma 3.9. lims→∞|πR(u(s, t))| = ∞
Proof. Assume the contrary, that there exists M > 0 such that there is a sequence (sn, tn) that
satisfies |πR(u(sn, tn))| < M and sn →∞. Since πR is unbounded, there is also a sequence (s′
n, t′
n)
such that s′
n →∞and πR ◦u(s′
n, t′
n) →∞. In addition, we can assume sn+1 > s′
n > sn by taking
subsequences.
From Lemma 3.8 we know that |∇u| < C for some C > 0. Set W = [−M −C, M + C] × Z and
select a symplectic structure ωf on W of the form d(ef(r)λ) where the function f : R →(0, 1) is a
diffeomorphism such that f is linear on [−M −1, M + 1]. Now use monotonicity lemma 3.6 on the
symplectic manifold with boundary (W, ωf) with N = 4 to get c, R. Choose r0 < min{R, 1
2}. Let
Σn be sub-strips of the format [αn, βn] × [0, 1] where s′
n−1 < αn < sn < βn < s′
n such that u(αn, ·)
and u(βn, ·) lies in [M + 10C, ∞) × Z. We can now apply the monotonicity lemma to each Σn. We
have, for all n,
(3.2.2)
Z
Σn
u∗ωϕ ≥cr2
0.
Then from summing over n in equation (3.2.2), we get Eωϕ(u) > P∞
1 cr2
0 = ∞which contradicts
that Hofer energy is finite since EH ≥Eωϕ. Thus, we have lims→∞|πR(u(s, t))| = ∞.
□
Without loss of generality, we will assume from now on wards that the πR(u) goes to ∞as s goes to
∞, ie. πR(u) →∞as s →∞. The case of πR(u) →−∞would follow by similar arguments.
Step 3 : Extending u in N
We will now show that the map u, when considered as a holomorphic map to N, can be extended
over the punctures. Under the biholomorphism z 7→e−πz, the half strip [0, ∞) × [0, 1] is mapped to
the punctured half disc D+
0 where half disc D+ denotes D ∩H for a disc D centered at 0. From
this step on wards we view the domain as a punctured half disc using the identification z 7→e−πz.
We will show that the map u can be extended by removing the boundary singularity at 0. As of
now, u can be viewed as a map of the half strip to N with boundary on the cleanly self-intersecting
Lagrangian L. Note that πY (u) is a holomorphic map from the half strip, such that the boundary
of the strip lies on the Lagrangian LY . As the Hofer energy EH(u) is finite, we have that the
horizontal energy EHor(u) = Edλ(πY (u)) is finite, thus from classical removal of singularities with
Lagrangian boundary in compact symplectic manifold, we have πY (u) can be extended over the
singularity at 0, denote the point πY (u(0)) ∈LY as q. Assuming that πR(u) →∞as s →∞, we
FLOER COHOMOLOGY AND HIGHER MUTATIONS
23
can extend u to D+ by defining u(0) = q∞where q∞is the image of q in Y∞. This can be checked
by taking a trivialization of N over some neighborhood U of q, then u|[R,∞) for large R > 0 is a map
to CP1 × U as πY (u)|[R,∞) lies in U. Since πR(u(z)) →∞as z →0, we have that u(z) →(∞, q) as
z →0. Thus we have shown that u can be extended. This gives us the following lemma.
Lemma 3.10. If u : [0, ∞) × [0, 1] →R × Z with boundary on R × Λ, has finite Hofer energy
EH(u) < ∞, then u has a limit as s →∞in the compactification N of R × Z and also finite energy
EωN (u) < ∞with respect to the symplectic form ωN.
Step 4 : Exponential convergence to a point in N
We will use results from [Sch16] to show the exponential convergence of u to Reeb chords. In
Theorem 3.1 and 3.2 the exponential convergence of finite energy strips with boundary on clean
intersecting Lagrangians is proved.
To use Schm¨aschke’s result, we first need to ensure that the map u on the boundary of the strip
lies on at most two Lagrangians that cleanly intersect. Since πY ◦u converges to q, there is a
small neighborhood V around q∞in N such that L ∩V is diffeomorphic to cleanly intersecting
Lagrangians and u has boundary lying on at-most two of them, denote these Lagrangians as L0, L1
that cleanly intersect at LY∞∩V .
Now, Schm¨aschke’s Theorem 3.2 gives us an exponential convergence in terms of eigenvalue
of an asymptotic operator. We have that u(s, t) = expq∞(e−αsζ(t) + w(s, t)) where ζ(t) is an
eigenfunction with eigenvalue α of the operator
Aq∞: Tq∞P(L0, L1) →L2([0, 1], Tq∞N), ξ 7→JN∂tξ,
where Tq∞P(L0, L1) = W 1,2(Tq∞N, Tq∞L0, Tq∞L1), the Sobolev space of paths from [0, 1] with
boundary on Tq∞L0, Tq∞L1. As Λ is a finite cover of LY , we can arrange a trivialization U × CP1
of N over a neighborhood U of q such that L0, L1 are determined by two sections of Z over LY .
Call those sections s1, s2 : LY ∩U →S1. From definition of iΛ we see that d(s1, s2) > iΛ under
the standard S1 metric induced from [0, 2π]. As JN splits into a direct sum of JY and J0 in each
trivialization, we obtain the eigenvalues and eigenvectors separately from the Y and CP1 component
in the trivialization U ×CP1. In the CP1 component we see that the eigenvalues of Aq∞is determined
by the difference in angle between s1(q) and s2(q) that is at most iΛ. Denote the angle difference
s1(q)/s2(q) by θq, then the eigenvalues are given by 2kπ + θq for all integers k. Since JN restricts to
the standard complex structure J0 on CP1 a direct computation shows that the eigenfunctions are
eit(2kπ+θq)v for v ∈Tq∞L0.
We can now collect the results of the previous paragraph to obtain the required exponential
convergence. When θq̸ = π, v lies in the vertical component T∞CP1 of Tq∞N = T∞CP1 ⊕TqU in
the trivialization CP1 × U as the only eigenvalues in the horizontal part are kπ. When θq = π,
the boundary of u lies on a single Lagrangian branch. Thus, we can do a doubling trick to obtain
a holomorphic cylinder in a neighborhood of q∞, then the exponential convergence follows from
[Bou02] since the Reeb dynamics in our case is Morse-Bott. From now we assume θq̸ = π, thus from
Theorem 3.2 in [Sch16] we get, for some vertical v ∈T∞CP1 ,→Tq∞N , s0 > 0 and any δ ∈(0, iΛ),
(3.2.3)
u(s, t) = expq∞(e−(2kπ+θq)(s+it)v + w(s, t)), ∥w∥Cl = O(e−(δ+2kπ+θq)s) ∀l ∈N, s ≥s0.
Step 5: Convergence to a strip in cylindrical metric
Here O(e−(δ+2kπ+θq)s) means that there is a cl > 0 such that ∥w∥Cl([s,∞)) < Cle−(δ+2kπ+θq)s. We keep using the
big-0 notation from now on to avoid notational clutter.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
24
L0
L1
LY∞
u(s, t)
θq
q∞
Tq∞L0
Tq∞L1
Figure 12. Angles between the Lagrangians L0,L1 at q∞.
So far, we have proved exponential convergence of a J−holomorphic strip in a compact manifold.
In this step, we will prove exponential convergence in the cylindrical manifold R × Z with respect to
a cylindrical metric. We will use the convergence in the compact manifold N to obtain exponential
convergence in the cylindrical manifold R × Z.
The choice of metric in N in (3.2.3) to define the exponentiation is not vital, since exponentiation
is an analytic local diffeomorphism and derivative at 0 is identity. From a Taylor-series computation,
we see that changing the metric doesn’t change the leading order decaying term in the equation
(3.2.3). Let g
expq∞denote exponentiation at q∞with a different metric. The Taylor-series of
g
exp−1
q∞◦expq∞is as follows,
g
exp−1
q∞◦expq∞(ev) = d(g
exp−1
q∞◦expq∞)0(ev) + O(|ev|2)
= dg
exp−1
q∞0 ◦dexpq∞0(ev) + O(|ev|2)
= Id ◦Id(ev) + O(|ev|2)
(3.2.4)
Thus, from equations (3.2.3) and (3.2.4) we get that u converges exponentially to the strip
g
expq∞(e−(2kπ+θq)(s+it)v).
We choose a metric on the compactified manifold N that lets us easily obtain trivial strips from
geodesic exponentiation. Choose a metric in g for N such that in the trivialization U × CP1 in a
neighborhood U of q, g = g1 ⊕g2 where g1 is the restriction of some metric on Y and g2 is a metric
on CP1 for which an open disc B∞centered at ∞is isometric to a disc B0 in C with standard
Euclidean metric. Since v in (3.2.3) lies in the vertical component, we have that
expq∞((e−(2kπ+θq)(s+it)v)
FLOER COHOMOLOGY AND HIGHER MUTATIONS
25
is a trivial strip uγ over a Reeb chord γ given by
γ(t) = eitθq.s1(q).
Thus, from the exponential convergence in (3.2.3) we get the following estimate with respect to the
metric g:
(3.2.5)
dg(u(s, t), uγ(s, t)) < Ce−(δ+2kπ+θq)s
∀s > s0.
We now show that the exponential convergence with respect to g in the compact manifold N
would imply our required exponential convergence in cylindrical metric, as proposed in (3.2.1).
Choose a trivialization U × CP1 of N. We claim that we can arrange g, such that it agrees with
gcyl on the contact distribution ker λ. Indeed, since πY induces an isomorphism of TπY (p)Y with
the hyperplane (ker λ)|p ,→TpZ, we can assume g agrees with gcyl. From our choices of g, gcyl we
have that in the trivialization U × CP1, πU ◦u converges exponentially fast to πU ◦uγ in O(e−δs).
It remains to check is the convergence of πCP1(u) to πCP1(uγ) in O(e−δs).
We fix parameterization, which we use in the upcoming estimates. We use the radial parametriza-
tion [1, ∞) × S1 →C∗, (r, θ) 7→(reiθ). In this parametrization, the restrictions of the metric to
[R, ∞) × S1 for large R > 0 direction are given as follows :
gcyl|C∗= 1
r2 dr2 + dθ2
g|CP1 = 1
r4 dr2 + 1
r2 dθ2.
The
1
r2 coefficient shows up in the formula of gcyl since the radial to cylindrical parameterization is
given by (r, θ) 7→(log r, θ). Also note that the metric g|CP1 is isomorphic to the Euclidean metric
on the punctured disc via the map (r, θ) 7→(1
r, θ). Denote the metric induced from these by dg,dcyl.
Lemma 3.11. There exists s0, C > 0 such that
dcyl(πCP1(u(s, t)), πCP1(uγ(s, t))) < Ce−δs
∀s > s0.
Proof. In the proof, we drop the arguments (s, t) from the maps to avoid notational clutter. Denote
πCP1 ◦u and πCP1 ◦uγ in radial coordinates for C∗by (ur, uθ) , (ur
γ, uθ
γ) respectively.
From
dg(u, uy) = O(e−(δ+2kπ+θq)s) we get for r ∈[R, ∞),
dg((ur, uθ), (ur
γ, uθ
γ)) = dD2
polar(( 1
ur , uθ), ( 1
urγ
, uθ
γ)) = O(e−(δ+2kπ+θq)s).
In the last equation dD2
polar is the Euclidean distance between two points in polar coordinates. We
now prove the estimate in R direction in R × S1.
| 1
ur −1
urγ
| = O(e−(δ+2kπ+θq)s)
=⇒|ur
γ
ur −1| = O(e−δs)
=⇒| log ur −log ur
γ| = | log ur
γ
ur | = O(e−δs)
Here, the first equality follows from |r1 −r2| ≤dD2
polar((r1, θ1), (r2, θ2)) and the last equality follows
from the Taylor expansion of log(1 + x) and the preceding line.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
26
Now we prove the estimate in the S1 direction.
We have that 2r1r2(1 −cos(θ1 −θ2)) ≤
(dD2
polar((r1, θ1), (r2, θ2)))2. Thus, we see that,
2
1
ururγ
(1 −cos(uθ −uθ
γ)) = O(e−2(δ+2kπ+θq)s)
=⇒1 −cos(uθ −uθ
γ) = O(e−2δs)
=⇒|uθ −uθ
γ| = O(e−δs).
In the above equations, we use that | log ur
urγ | = O(e−δs) implies that ur(s, t) = O(e(2kπ+θq)s) and
that the Taylor series of cos x.
Recall that the radial-to-cylindrical parametrization is given by (r, θ) 7→(log r, θ). We see that,
(| log ur −log ur
γ|2 + |uθ −uθ
γ)|2)
1
2 = dcyl((ur, uθ), (ur
γ, uθ
γ)) = O(e−δs).
Thus, we have
dcyl(πCP1(u(s, t)), πCP1(uγ(s, t))) < Ce−δs
∀s > s0.
□
Combining the exponential convergence of πCP1 ◦u and πY ◦u we get our required exponential
convergence,
dcyl(u(s, t), uγ(s, t)) < Ce−δs
∀s ≥s0.
□
Remark 3.12. We can prove an exponential convergence for strips with boundary on La in R × Z
where La projects to the Lagrangian LY in Y and La is asymptotically close to the cylindrical
Lagrangian R × Λ so that closure of La in N is a Lagrangian with clean self intersection. We
encounter such a boundary condition in the case of TR+iϵ. Steps 1,2,3 and 5 follow verbatim for this
case. From a direct computation of eigenvalues and eigenfunctions of Aq∞in this case we get the
necessary counterpart of equation (3.2.3) of Step 4.
3.3. The SFT compactness theorem. We state the version of SFT compactness for discs in our
case of neck-stretching here. We avoid adding marked points and perturbation of domain just for
sake of notational clarity, the theorem still holds true with them.
Theorem 3.13. If un : D2 →(W n, Jn, Ln) is a sequence of Jn holomorphic disc to the n−stretched
manifolds, with boundary on Ln, and with bounded energy, i.e. E(u) < E < ∞, then there is a
subsequence of un that converges to a stable broken disc.
This theorem is mentioned in Section 11.3 in [BEH+03] for the case of non-degenerate Reeb
chords. Our case is a Morse-Bott version for Reeb chords. The proof in this case is the same as the
usual SFT compactness theorem apart from some analytic changes in the lemmas in section 5 in
[BEH+03]. We prove the necessary counterparts of the analysis in section 5 in the following lemmas.
Lemma 3.14 (Bubbling). There exists a ℏ> 0 such that the following is true. Let Fn = (an, fn) :
D2
+ →(R × Z, R × Λ) be a sequence of holomorphic maps from the upper half disc with Lagrangian
boundary such that E(Fn) < C for some constant C and an(0) = 0. Then there is a sequence of
points yn ∈D2
+ converging to 0 and sequences of real numbers Rn, cn such that the rescaled maps
F 0
n(z) = (yn +
z
Rn ) are functions on the half-disk of radius Rn and have a convergent subsequence to
F 0 in C∞
loc such that EHor > ℏ
FLOER COHOMOLOGY AND HIGHER MUTATIONS
27
Proof. If |∇Fn(0)| →∞as n →∞. As usual with bubbling analysis, we apply Hofer’s lemma to
obtain yn ∈D2
+ and ϵn ∈R such that yn →0, sup |∇Fn(z)| ≤2|∇Fn(y)| where the supremum
is taken on |z −yn| ≤ϵn and |∇Fn(yn)|ϵn →∞.
Now consider the rescaled maps F 0
n(z) =
Fn(yn +
z
|∇Fn(yn)|). This rescaled map is defined for |z| ≤ϵn|∇Fn(yn)| and has upper bound on
the gradient by 2, thus by Arzela-Ascoli we get a convergent subsequence that converges to a
non-constant function F 0 on the upper half plane H or the complex plane C depending whether yn
was on the boundary or in the interior. Clearly we have E(F 0) ≤C. If the image of F 0 is bounded,
F 0 maps to a holomorphic sphere or a disc with Lagrangian boundary and from standard energy
quantization result we have EHor(F 0) > ℏ> 0 where ℏdepends on Z. for some fixed or else it maps
asymptotically to a Reeb chord or Reeb orbit. If F 0 has unbounded image, from Lemma 3.15, it
has Reeb-orbit/chord asymptotes . Since we are in the contact case, we can directly compute EHor
and see that it is bounded below by the smallest length of the Reeb chord, thus π/n for our case.
Thus choosing a smaller ℏwe can ensure that EHor(F 0) > ℏwhere ℏdepends only on Z.
□
Lemma 3.15 (Asymptotics of strips). Let F=(a,f) : R+×[0, 1] →(R×Z, R×Λ) be a J holomorphic
map of finite energy EH(u) < ∞, assume that image of F is unbounded, then there is a number T
and a Reeb chord γ of length T such that
lim
s→∞f(s, t) = γ(tT)
and
lim
s→∞
a(s, t)
s
= T
in
C∞[0, 1].
This lemma is a direct consequence of our asymptotic convergence proved in Theorem 3.5.
Lemma 3.16 (Strip with long neck and small energy). Given E0, ϵ > 0 there exists constants σ, c > 0
such that for every R > c and for every J holomorphic function F = (a, f) : [−R, R] × [0, 1] →
(R × Z, R × Λ) satisfying the inequalities,
EHor(F) ≤σ
and
E(F) ≤E0,
we have
f(s, t) ∈Bϵ(f(0, t))
for all s ∈[−R + c, R −c], t ∈[0, 1].
Proof. Assume the contrary, so we have an ϵ0 and Rn > cn such that cn →∞and sn ∈[−kn, kn]
where kn = Rn −cn such that EHor < 1
n and d(fn(sn, t), fn(0)) > ϵ0. If we select σ small enough
such that any holomorphic disc v in Y = Z/S1 with boundary in the Lagrangian L = Λ/S1 has
EY (v) > σ then for n large, we see that EHor(Fn) = EY (πY ◦Fn) ≤
1
n . From the bubbling
quantization lemma 3.14 we know that there must be a uniform gradient bound or else EHor
has to be at least ℏ. Thus, by Arzela-Ascoli we can take a convergent subsequence Fn →F 0 in
C∞
loc(R × [0, 1]). Clearly from considering the horizontal energy we see that F 0 is a strip whose
image lies in a trivial cylinder over a point p ∈L with the same Reeb chord as its positive and
negative asymptote. Thus, we can consider F 0 to be a map to C∗with boundary on R+ and
ekαR+. From exponential convergence to Reeb orbits at the asymptotes we see that F 0 has to
be a trivial Reeb strip i.e. f0(s, t) = γ(t) where γ is the Reeb chord at the asymptote. From
convergence on compact sets, we have that fn(0, t) →γ(t). Now consider the sequence of translated
maps F n(s, t) = Fn(s −sn, tn), possibly taking a further subsequence we get a C∞
loc convergent
subsequence to F
0. Potentially F
0 can be a trivial strip over a different Reeb strip. It is classically
known (see Lemma A.6 in [Fra03] and Lemma 3.8 (ii) in [Sch16]) that long strips of small energy
have diameter bounded by the energy. Thus, from the horizontal energy bound we get, πY ◦Fn →p
as n →∞since πY ◦Fn(0, t) →p, thus F
0 = F 0, thus fn(0, t) = fn(sn, t) →γ(t). One way to
see this is to apply Lemma 3.8 (ii), since |sn| < kn, |sn| < Rn −cn
2 . As cn →∞, we have for
large n, d(πY ◦Fn(sn, t), πY ◦Fn(0, t)) < ceµ cn
2 . Thus d(fn(sn, t), fn(0, t)) tends to 0 in limit, which
contradicts our assumption.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
28
□
Once one has the last three Lemmas we proved above, the proof for SFT compactness from
[BEH+03] works in our setting. We give a sketch of the proof in [BEH+03] for continuity.
Sketch of Proof of 3.13:
The proof is broken into four steps.
• Step 1: Gradient Bound
• Step 2: Convergence from gradient bound away from nodes
• Step 3: Convergence near the nodes aka ‘thin-part’
• Step 4: Labelling of the components in the nodal disk
Step 1: Gradient Bound
The first step in showing SFT Compactness is to pick a subsequence so that the domain converges,
for sake of clarity lets assume that our domain is constant for all n and have no marked points.
Then Lemma 10.7 in [BEH+03] and Proposition 3.7 in [Abb14] prove that after removing a finite
number of points from, D2 we get a uniform gradient bound for all n.
Lemma 3.17 (Gradient lemma). There is a natural number K(E) and a sequence Mn of 2K(E)
marked points on the disc such that after removing these marked points from D2, we have a uniform
bound as follows
|∇uin(z)| ≤
C
ρ(z)
∀z ∈D2
n,
where D2
n = D2 \ Mn and ρ is the radius of injectivity with respect to the standard hyperbolic metric
on D2
n and uin is a subsequence of un.
Proof: Assume xn ∈D2 such that |ρ(xn)∇un| →∞. We can assume after taking a subsequence
(and still indexing it by n) that either of the following conditions hold :
(1) un(xn) ∈W n \ ((−n, n) × Z),
(2) un(xn) ∈(−n/2, n/2) × Z.
For case 1, after rescaling our domains and using usual the bubbling lemma we can add two
marked points xn, yn, d(xn, yn) →0 such that the bubble captures horizontal energy at least ℏ.
For case 2, after translating to ensure un(xn) ∈{0} × Z and rescaling the domain and lemma
3.14, we see that there is a bubbling of a possibly punctured holomorphic disk or sphere which
captures at least ℏhorizontal energy. Thus, in either can choose xn, yn , d(xn, yn) →0 such that
the EHor(un) < E −ℏon D2 \ {xn, yn}. From positivity of horizontal energy, we see that if we
inductively keep adding marked points, our process will end in at most E
ℏsteps.
Step 2: Convergence from gradient bound away from nodes
After putting in the marked points to get gradient bounds, take a further subsequence of un such
that the domain with the marked points Mn converge to a nodal disk with marked points. From
the bubbling lemma (Lemma 3.14), we have that un converges on the components containing the
markings Mn. The gradient bound on the components not containing Mn lets us use Arzela-Ascoli
to get a convergent subsequence of un that converges on every piece of the nodal disc.
Step 3: Convergence near the nodes aka ‘thin-part’
Near the nodes in components with marked points Mn, we know that the maps u are asymptotic
to Reeb chords or points. It might happen that the asymptotic limit at the nodes might not match.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
29
Let’s fix a node and pick a sequence of parameterization on a neighborhood of D2 which degenerate
to that node, call the neighborhoods Vn. We can arrange the parameterization such that
• Vn becomes a strip or a cylinder as n →∞,
• un|Vn has bounded gradient, thus bubbling can’t occur ,
• un(s, t) →Reeb chords/strips γ± as s →±∞.
There are two cases, either Ehor(un|Vn) →0 or Ehor(un|Vn) > δ > 0 for a fixed lower bound δ. For
the first case, from Lemma 3.16 we obtain that if there is no concentration of energy near the node,
the asymptotes match i.e. γ+ = γ−. Thus, the only case left is if there is some energy concentrating
near the nodes. in such a case one adds more marked points which results in formation of a new
spherical/disc component which captures at least ℏhorizontal energy, and the new nodes which are
formed are treated inductively. The new nodes will eventually have no energy concentration. Thus,
finally, we get a nodal disc with matching conditions on the nodes. The limit we obtain finally is
denoted by (u, D)
Step 4: Labelling of the components in the nodal disk Pick points xC
n for every component
C of D. Label the components C such that if un(xn) ∈W n \ (−n, n) × Z then label it in or out
based on which component it lies in. If un(xn) ∈(−n, n) × Z, order the components such that
Ci ≤Cj if limsup (prR(un(xj
n)) −prR(un(xi
n))) →∞. Set Ci ∼Cj if Ci ≤Cj and Cj ≤Ci. Label
the collection of the minimal components as D1, then remove them and label the collection of the
new minimal components as D2 and keep going. In the case of such labeling, it might happen that
across a node, the label just by more than 1, in such a case add trivial sphere/discs between and
label them such that the difference across nodes is at most 1.
□
3.4. Compactness for strips bounding pair of Lagrangians under stretching. We now
return to our specific situation where we want to apply the neck stretching construction. Since
the differential in the Floer complex CF(L, K) is based on the count of holomorphic strips, we
will need a version SFT compactness of strips under neck stretching. Recall that a holomorphic
strip in M bounding L, K from x+ to x−is a holomorphic map u : R × [0, 1] →M with boundary
conditions u(R × {1}) ⊂L and u(R × {0}) ⊂K and asymptotic conditions lims→±∞u(s, t) = x±
where x± ∈L∩K. If L is a locally mutable Lagrangian and K is another Lagrangian that intersects
L transversally and lies outside the mutation neighborhood B ie. K ⊂M \ B, we can do a neck
stretch of M along the contact hypersurface Z = ∂B since near a tubular neighborhood of Z, the
Lagrangian L is of the form (−ϵ, ϵ) × T± (see Equation ( 2.3.1) for definition of T±). Since K is
outside the mutation neighborhood, after neck stretching, K naturally lies in the outside piece c
Mout
of the broken manifold M. The analog of a broken disc in the setting of a strip is called a broken
strip.
Definition 3.18 (Broken strip). A broken strip (u, D) from x+ to x−is a broken disc where one
of the components of Dout is a strip R × [0, 1] with puncture nodes P on the boundary R × {1}
and uout satisfies the boundary condition uout(R × {1} \ P) ⊂bLout and uout(R × {0}) ⊂K and
asymptotic conditions lims→±∞uout(s, t) = x±.
We can use an exactly similar technique as in the proof of Theorem 3.13 to get the following
compactness result about holomorphic strips.
Theorem 3.19 (SFT compactness for strips). If un : R × [0, 1] →(Mn, Jn, Ln, K) is a sequence
of Jn holomorphic strips from x+ to x−in the n−stretched manifolds, with boundary condition on
Ln and K, and with bounded energy, i.e. E(u) < E < ∞, then there is a subsequence of un that
converges to a broken strip.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
