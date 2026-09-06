---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-008-handlebodies-as-conformal-blocks
section_title: "Handlebodies as conformal blocks"
section_number: null
pages: 24-34
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Let us now discuss how handlebodies contribute to the path integral of 3d gravity. As
explained in [11], 3d gravity with a negative cosmological constant on a hyperbolic
3-manifold is related to two copies of Virasoro TQFT (VTQFT). The gravitational
partition function is just the product
Zgrav[M; Ω, ¯Ω] =Z Vir[M; Ω]Z∗
Vir[M; ¯Ω].(3.6)
Here Ω, ¯Ω are complex structure moduli fixed at the conformal boundary. For a
genus-ghandlebodyM C with conformal boundary Σ g, the VTQFT amplitude is
given by the vacuum Virasoro conformal block:
ZVir[MC; Ω] =F C
g (1; Ω).(3.7)
HereCdenotes a choice of contractible cycles (i.e. an identity channel) that is part of
the data specifying the handlebodyM C. In general, the genus-gVirasoro conformal
blocks are defined as solutions of the conformal Ward identities [54] but forg >1 and
c >1 they are not known analytically (although recursive representations exist in
special cases [79–81], using the plumbing construction). In [12], the relation between
the gravitational path integral on a handlebody and the square of the identity block
was verified, forg= 2, in the semiclassical (c→∞) limit, including the one-loop
– 24 –
determinant (in a perturbative expansion around a degenerating locus of moduli
space). See also [82, 83]. In this match, one uses the Brown-Hennaux relation [84]
c∼ 3ℓAdS
2GN
(3.8)
between the gravitational coupling and the central charge. However, we stress that
the identification between the gravitational path integral and the identity block (3.7)
is exact incand does not rely on a semiclassical approximation. This is striking, be-
cause it shows that the gravitational answer is fully determined by the representation
theory of the Virasoro algebra, which is universal to every 2d CFT.
Action of the mapping class group.The fact that 3d gravity partition functions
are given by representation-theoretic objects holds more generally: in VTQFT, the
partition function on any 3-manifold with boundary Σ g can be expressed as a state
in the Hilbert space of Virasoro conformal blocks. This Hilbert space is spanned
by non-degenerate blocks, which have internal conformal weightsh i ⩾ c−1
24 . The
identity module is a degenerate representation of the Virasoro algebra withc >1,
but the identity block can be expressed in the basis of non-degenerate blocks in a
dual channel through the crossing kernels introduced in section 2:
Fγ·C
g (1; Ω) =
Z ∞
0
d3g−3PK γ
1PFC
g (P; Ω).(3.9)
Here we introduced the convenient Liouville parametrizationh i = c−1
24 +P 2
i,where
the Jacobian factor is implicit inK γ
1P , and used the notationP= (P 1,...,P 3g−3).
This corresponds to a non-normalizable state in the VTQFT Hilbert space. So the
handlebody partition functions, labeled by the mapping classesγ, are particular
(non-normalizable) states in the Hilbert space of Virasoro conformal blocks whose
expansion coefficients are the crossing kernelsK γ. Here the relevant kernels are the
identitykernelsK γ
1P , whose definition requires the subtraction of null states by hand
to account for the fact that the vacuum module is a degenerate representation [20].
Through equation (3.9), these identity kernels implement the action of the map-
ping class group on the set of handlebodies (3.5). We can find the action of a Dehn
twist generator, twisting along some non-contractible cycleC, by crossing to the
channel whereT C is diagonalized (acting on the conformal block as multiplication
by a phase), and then cross back to the original channel. For example, consider the
genus-2 block, withCthe dumbbell channel:
FC
g=2(P,Ω) =F C
g=2


P1 P2
P3

 .(3.10)
We have drawn the dual graph ΓC in gray and labelled the edges by Liouville momenta
P1,P 2,P 3. Now chooseγto be following product of Dehn twists, where we twist along
– 25 –
the non-contractible cycles (B 1,B 2,A) highlighted in red:
γ=T B1TB2TA :
B1 B2
A
.(3.11)
One can convince oneself thatγacts on the contractible cycles as shown in figure 1.
The corresponding kernelK γ
1P can be found by usingFandSkernels to cross to the
dual channels, whereTacts by a phaseT P = e−2πihP , giving:
Kγ
1P1P2P3 = (STS)1P1(STS)1P2(FTF)1P3.(3.12)
More explicitly, we have:
(FTF)1P3 =
Z ∞
0
dPF 1P
P1P2
P1P2

TP FPP 3
P1P1
P2P2

,(3.13)
(STS)1P1 =
Z ∞
0
dPS 1P [1]TP SPP 1[1] =S 1P1[1]T∗
P1,(3.14)
where in the second line we used the PSL(2,Z) identitySTS=T ∗ST∗ andT 1 = 1.
This example shows how Dehn twists are represented by crossing kernels acting on
identity blocks. The expressions in terms of Dehn twists can always be re-expressed
in terms of the Moore-Seiberg generatorsB,F,S, as we will see below.
Action of the handlebody group.We can ask when a mapping class, repre-
sented byK γ, is in the handlebody groupH g. On the level of conformal blocks, a
handlebody group element leaves the vacuum block invariant up to a phase:
Fγ·C
g (1; Ω) = eiθγFC
g (1; Ω), γ∈H g.(3.15)
The overall phase is a manifestation of the framing anomaly familiar from Chern
Simons theory. Since the gravitational partition function on the handlebody is the
absolute value squared of the identity block (recall (3.6)), this phase factor drops
out. Hence, any two handlebodies that are diffeomorphic have the same gravitational
partition function, as they should.
On the level of the crossing kernels, the condition in equation (3.15) can be
translated using the block decomposition (3.9) to the statement that forγ∈H g, the
associated crossing kernel is the Dirac delta up to an overallh-independent phase:
Kγ
1h = eiθγδ(h), γ∈H g.(3.16)
We can be more explicit in the genus-1 case. There, the vacuum block is simply
the Virasoro vacuum characterχ 1(τ) =q −c−1
24 1
η(τ) (1−q), and the handlebody group
– 26 –
consists of the Dehn twists around the contractible cycleτ→τ+n, wheren∈Z.
These act on the vacuum character as multiplication by a phase:
χ1(τ+ 1) = e−2πi c
24χ1(τ),(3.17)
where the phase is just the conformal anomaly determined by the central chargec.
3.3 Fixed-Ppartition functions
Instead of working with the ‘canonical’ partition functions, with fixed values of the
complex structure moduli at the asymptotic boundary, in Virasoro TQFT it is useful
to define the corresponding ‘fixed-P’ partition functionZ C
Vir[M;P]. We define it by
stripping off the non-degenerate blocks and including a normalization factor:
ZVir[M; Ω] =
Z ∞
0
d3g−3P ρC
g (P)Z C
Vir[M;P]F C
g (P; Ω).(3.18)
This equation is analogous to the gluing of trumpets to fixed-length partition func-
tions (i.e. Weil-Petersson volumes) in JT-gravity [68]. Let us explain the notation
used. First, the integral in (3.18) is only over the heavy part of the spectrum, which
we parametrized by the Liouville momentaPas before. In other words, we have
expanded in a basis of non-degenerate conformal blocks in the channelC. (This
heavy channel should not be confused with the identity channel that defined the
contractible cycles of the handlebodies discussed above.)
Second, the normalization factor is defined as:
ρC
g (P) =
Y
ea∈ΓC
ρ0(Pa)
Y
vijk∈ΓC
C0(Pi,Pj,Pk).(3.19)
The product is over all edges and vertices of the dual graph ΓC, with known functions
ρ0 andC 0 that are related to the modular S-kernel and fusion kernel (see App. C).
This normalization appears in the inner product on the space of conformal blocks
derived in [11] and will be convenient later. Indeed, one may interpret (3.18) as
the resolution of the identity in the VTQFT Hilbert space associated to the genus-g
boundary, which implements the change of basis from fixed-moduli to fixed-P:
⟨Ω|ZVir(M)⟩=
Z ∞
0
d3g−3P ρC
g (P)⟨F C
g (P)|Z Vir(M)⟩⟨Ω|F C
g (P)⟩.(3.20)
Concretely, in the case thatMis a handlebodyM γ, labeled by some crossing
transformationγ, the fixed-Ppartition function can be read off from (3.9) to be:
ZC
Vir[Mγ;P] = 1
ρC
g (P) Kγ
1P .(3.21)
Plugging this into (3.18), we see that the corresponding identity channel isγ·C.We
stress that the choice ofCis arbitrary once we sum over allγ’s in section 3.4. In
– 27 –
practice, we will choose the basisCto be ‘simple’, in the sense that the dual graph Γ C
has the minimal number crossings. At genus 2 and 3, this will be one of the planar
graphs in equations (2.5) and (2.6). 17 With respect to this simple choice of basis
C, the complexity of the handlebodyM γ is visualized by a VTQFT diagram, which
represents theembeddingof Γ C in a closed 3-manifold, as we will explain below.
Again, an example will clarify the above formalism. At genus 2, consider the
crossing transformationγ=S◦S◦F, where one S-kernel acts on the left dumbbell
and the other on the right. The corresponding dual graph Γ C is the sunset diagram.
Using the definition (3.21), its fixed-Ppartition function evaluates to:
ZVir

 P1 P2 P3

 =
S1P1[1]S 1P3[1]F 1P2
P1P3
P1P3

ρ0(P1)ρ0(P2)ρ0(P3)C0(P1,P 2,P 3)C0(P1,P 2,P 3) (3.22)
= 1
C0(P1,P 2,P 3).(3.23)
In the second line, we used thatρ 0(P) =S 1P [1], as well as the relation:
F1P2
P1P3
P1P3

=ρ 0(P2)C0(P1,P 2,P 3).(3.24)
Now we can find the corresponding identity channel by acting withγon the sunset
diagram. Doing so, we see that the identity channelγ·Cis the dumbbell channel:
Z ∞
0
d3PS 1P1[1]S 1P3[1]F 1P2
P1P3
P1P3

FC
g=2

 P2
P1 P3


=F γ·C
g=2


1
1 1

 ,(3.25)
where the ‘bells’ (sub-tori) are in the S-dual channel. The contribution of this han-
dlebody to the statistical moment is just the universal density studied in [3]:
ρ1ρ2ρ3C123C∗
123⊃|ρ 0(h1)ρ(h2)ρ0(h3)C0(h1,h 2,h 3)|2.(3.26)
As before, we used the notation⊃to indicate that the left-hand side is given by a
full sum over topologies, and the right-hand side is only one term in that sum. We
also used the notation|·| 2 as a shorthand for the product of left- and right-moving
17However, at genus 4 and higher there are contraction patterns that cannot be made planar:
an example is the contraction in equation (3.46) of [12]. That is why we defineCby requiring the
minimal number of crossings of ΓC. These simple bases are in 1-1 correspondence with the distinct
contraction patterns of OPE coefficients introduced in section 2.
– 28 –
contributions, as in equation (3.6). Furthermore, we used the shorthandρi≡ρ(h i, ¯hi)
and changed variables from Liouville momenta back to conformal weightsh i.
As a second slightly more involved example, consider the crossing transformation
γthat was illustrated in (2.8). Additionally, we add two S-moves acting on the bells
of the dumbbell. So the total mapping class is:
γ=S◦S◦F◦B 2◦F,(3.27)
where the two S-kernels act on the two dumbbells andF◦B 2◦Fonly acts on the
centrally embedded 4-punctured sphere. The associated VTQFT graph is the linked
dumbbell channel, where the two bells have been linked as in (2.8). We can find the
fixed-Ppartition function associated to this handlebody by representing (3.27) by
its genus-2 crossing kernel:
Kγ
1P1P2P3 =S 1P1[1]S 1P2[1]
Z ∞
0
dPF 1P
P1P2
P1P2
 
BP
P1P2
2
FPP 3
P1P1
P2P2

.(3.28)
Using the expression for the braiding phase (C.1), we note that this kernel is precisely
equal to the Dehn twist representation (3.12), and indeedγdefines the same mapping
class as (3.11). Furthermore, we note that theP-integral can be expressed in terms
of the one-point S-kernel by using the integral identity (C.22). Dividing by the
normalization factorρ C
g=2, we thus obtain:
ZVir

P1 P2P3

 = Kγ
1P1P2P3
ρ0(P1)ρ0(P2)ρ0(P3)C0(P1,P 1,P 3)C0(P2,P 2,P 3) (3.29)
= SP1P2[P3]
ρ0(P2)C0(P2,P 2,P 3) = 1√C113C223
bSP1P2[P3].(3.30)
In the last equality we rewrote the fixed-Ppartition function in terms of the sym-
metric S-kernel, cf. (C.19), in the so-called Racah-Wigner normalization [85]. The
prefactors are useful shorthands for theC 0 function:
Cijk≡C 0(Pi,Pj,Pk).(3.31)
In this example,Cis the dumbbell channel, and we have represented the non-trivial
topology of the handlebodyM γ by the VTQFT diagram where the bells are linked.
To find the corresponding identity channelγ·C, we follow the sequence of moves in
(2.8) and apply the additional S-moves. The resulting identity channel is also the
linked dumbbell diagram:
Z ∞
0
d3PK γ
1P1P2P3FC
g=2

P1 P2P3

=F γ·C
g=2

 1 11
′′

 .(3.32)
– 29 –
Here we used the prime ′ to indicate that the bells are now in the S-dual channel.
The linked dumbbell in (3.30) has a counterpart where the over-under cross-
ings of the bells are reversed [16]. Their VTQFT partition functions differ by a
complex conjugation, which leads to a phase bSP1P2[P3]∗ = e−iπh3bSP1P2[P3]. The sum
of these two distinct handlebodies projects onto even spinJ 3, compatible with the
permutation property (2.3), and contributes as the following non-Gaussian moment:
ρ1ρ2ρ3C113C223⊃(1 + (−1)J3)

ρ0(h1)ρ0(h2)ρ0(h3)
p
C113C223bSh1h2[h3]

2
.(3.33)
As an aside, we note that the linked dumbbell diagram is also known as the ‘knotted
handcuff’ in the literature [15, 16], and it is often depicted as such:
.(3.34)
As a third and last example of a more complicated handlebody, we study a
diagram that is in the mapping class group orbit of the sunset diagram. We can
obtain it from the linked dumbbell by acting with a braiding and a fusion move:
B−1 F .(3.35)
The right-hand side indeed has the same graph type as the sunset in (3.22), but one
of the edges ‘loops’ around one of the other edges. We can also view this diagram
as a particular fragmentation of the trefoil knot, in the sense of [17]. The associated
genus-2 handlebody has a fixed-Ppartition function that we compute as before: first,
we write down the crossing kernelK γ that representsγ=S◦S◦F◦B 2◦F◦B −1◦F,
and then we divide by the sunset normalization factor. This gives:
ZVir

P1
P3
P2

 = 1
C123
Z ∞
0
dP ρ0(P)bSP1P2[P]B P2P2
P
P1 P2 P3
P2 P1 P

.(3.36)
HereB P2P2
P is the complex conjugate of the braiding phaseB P
P2P2, and we have ex-
pressed the fusion kernel in terms of the Virasoro 6jsymbol using the relation (C.5).
In this example,Cis the sunset channel, and acting on it withγone can show that
the corresponding identity channelγ·Cis again a linked dumbbell as in (3.32), with
the only difference that now one bell is in the S-dual channel and one bell is acted
– 30 –
on byST. Multiplying by the normalization factor and taking the absolute value
square as in (3.6), this handlebody is also a contribution to the statistical moment
ρ1ρ2ρ3C123C∗
123.
From the above examples, we see that the fixed-PVTQFT partition functions
are fully expressed in terms of crossing kernels only. We stress that, contrary to
conformal blocks, these kernels are known analytically as integrals over known special
functions [20]. Although the integrals may be hard to compute in general, they could
in principle be evaluated numerically, for any value ofc. What’s more, since we
stripped off the conformal blocks, the fixed-Ppartition functions are what actually
contribute to OPE statistics.
Geometric interpretation of the fixed-Ppartition function.There are sev-
eral ways to interpret the VTQFT diagrams that appear in the fixed-Ppartition
functions calculated above. First, one can view the fixed-PVTQFT graph as being
embedded in the 3-sphere S 3, and obtain a 3-manifold with boundary by taking the
complementof a regular neighborhood of the graph. Here is a pictorial example:
S3
.(3.37)
This is similar to the construction of a knot complement, but instead of embedding a
link (thickened into a union of solid tori), we have embedded a trivalent graph (i.e. a
network of Wilson lines). If this graph is connected, the boundary of the graph
complement is a genus-gsurface. The cycles inCare now non-contractible cycles in
the ambient 3-manifold, for complicated enoughγ.
More generally, instead of S 3 we could use any other closed 3-manifold as our
embedding manifold. For example, our notation of the prime in (3.32) to indicate an
S-transform should really be thought of as an embedding of the dumbbell graph in
S2×S 1 (or connected sums thereof, for multiple S-transforms). We will come back
to this point when we discuss Dehn surgery in section 3.4.
Geometrically, viewing the fixed-Pdiagrams as graph complements can be un-
derstood using the theory ofpleated surfaces. Namely, for a handlebodyM γ the
complete hyperbolic metric is always of infinite volume, and ‘flares out’ to the con-
formal boundary [9].M γ does not support any smooth finite-volume hyperbolic
metrics with totally geodesic boundary. However, we can put a finite-volume hy-
perbolic metric onM γ if we allow the geometry to end on a boundary surface that
is pleated. This means that the boundary surface has vanishing extrinsic curvature
– 31 –
everywhere except along a collection of geodesics, where the surface is allowed to
have corners. As explained in [15], the fixed-Ppartition function can be understood
geometrically as the AdS3 gravitational path integral with precisely such a boundary
condition, in which the fixed Liouville momentaP i are related to the lengthsℓ i of
the geodesics around which the pleated surface bends by the formulaℓ i = 4πbPi.18
We remark that such a geometric interpretation does not always exist, for a
number of ‘simple’ handlebodies. This happens if a closed curveC i dual to an edge
Pi bounds a compressible disk in the graph complement. An example is given by the
complement of the dumbbell graph, in which the middle cycle can be contracted in
the ambient S3:
P1 P2P3
S3
.(3.38)
This is reflected by the fact that the VTQFT partition function has support only on
the identity for the weightP 3:19
ZVir

P1 P2P3

= δ(P3−1)
ρ0(P3)C0(P1,P 1,P 3)C0(P2,P 2,P 3).(3.39)
Since this is a distribution, it clearly does not have an interpretation as a classical
saddlepoint to a fixed-length path integral. For a more complicated handlebody,
like thelinkeddumbbell (3.30), theP 3 cycle is non-contractible, and indeed in that
case the fixed-length path integral exists and was analyzed directly in gravity in [15].
More generally, if the mapping classγthat defines the handlebody is complicated
enough (technically, a sufficient condition is thatγis “pseudo-Anosov” [86]), then
the fixed-length path integral exists, and the above geometric understanding of the
fixed-Ppartition function makes sense.
Fixed-Ppartition functions, wormholes, and OPE statistics.The fixed-P
partition functions that have been the subject of this subsection straightforwardly
encode the moments of structure constants in the dual statistical ensemble of CFT
data. The precise relation is made transparent by noting that there is a second
geometric interpretation of the VTQFT Wilson line diagrams: as Euclidean worm-
hole geometries with boundaries that are thrice-punctured spheres. That is, instead
of excising a regular neighborhood of the full graph embedded in S 3, we only ex-
cise a spherical neighborhood around each vertex. In replacing trivalent vertices by
18Herebis the Liouville coupling, which parametrizes the central charge asc= 1 + 6(b+ 1/b) 2.
19Here1meansP 3 = iQ
2 , which is equivalent to the real delta function settingh 3 = 0.
– 32 –
3-punctured spheres, we normalize each boundary component with a factor ofC 0:
P1
P2 P3
= 1
C123
P1
P2 P3
.(3.40)
This turns our trivalent graph into a Euclidean wormhole with 3-punctured sphere
boundaries and a (possibly knotted) network of Wilson lines in the bulk, where the
bulk Wilson lines have fixed holonomies parametrized byP i.
When the conformal weighth i is in the conical defect regime (defined e.g. in
[26]), the Wilson line has a semiclassical interpretation as creating a conical defect
in the bulk geometry. As an example, we see that the sunset graph is equivalent to
the Maldacena-Maoz wormhole:
1
2
3
0
⇔
1
2
3
1
2
3
.(3.41)
This was also the perspective taken in section 3.3 of [12]. The two perspectives on
the fixed-Ppartition functions are both useful to keep in mind. They interpolate
between each other by taking the conformal weights of the Wilson lines above the
black hole threshold, in which case the boundary of the graph complement becomes
a connected Riemann surface [3]. We then effectively ‘trade’ the Wilson lines for
tunnels.20 Likewise, the geometric interpretation of the conformal blocks that we
integrate against is that of ‘trumpets’, or flares, which trade the fixed momentum
labelsPfor complex structure moduli Ω at the conformal boundary.
Thus in order to extract the statistics of the structure constants in the boundary
ensemble it is sufficient to consider trivalent networks of Wilson lines in VTQFT.
While these are most naturally associated with contributions to the gravitational
path integral with a single genus-gboundary, they are also straightforwardly re-
lated to multi-boundary sphere 3-point wormholes which more directly encode the
OPE statistics without the additional baggage of conformal blocks. To extract the
contributions to the OPE statistics from the VTQFT Wilson line configurations we
simply replace the trivalent vertices with 3-punctured spheres via the replacement
rule (3.40) and square the associated VTQFT partition function. This gives:
Y
ei∈ΓC
ρ(Pi, ¯Pi)
Y
vijk∈ΓC
Cijk ⊃

ρC
g(P)Z C
Vir[Mγ;P]

2
.(3.42)
Crucially, the RHS of (3.42) is generically a non-Gaussian contribution to the sta-
tistical moment on the LHS, which does not factorize into a product of variances.
20See also [87] for a geometric description of the Euclidean wormholes in the heavy regime.
– 33 –
How to tell a handlebody from a non-handlebody.The fixed-Pformulation
of Virasoro TQFT is useful for computations, because we have all of the tools of 3d
topological quantum field theory at our disposal to evaluate the partition function.
A list of useful calculation rules is collected in appendix C. However, one drawback
of this formalism is that, given some random knotted trivalent graph, it is in general
hard to distinguish a handlebody from a non-handlebody. This problem comes down
to finding a Moore-Seiberg moveγsuch that the diagram can be untangled to a
simple diagram. 21 Thisγcould be a very long word in the generatorsS,FandB.
For instance, in the example below, the left diagram corresponds to a handlebody
and the right to a non-handlebody:
1
3
2
1
3
2
.(3.43)
The left is just the looped version of the sunset diagram (3.37) that we studied above.
The right, on the other hand, corresponds to a known non-handlebody that we will
study in section 5, called5 2 in our table 1. The two diagrams only differ by one
under-over crossing. Moreover, both diagrams result from a fragmentation of the
trefoil knot [17]: on the left, the edge 3 fragments the trefoil, and on the right the
edge 1 fragments the (mirror of the) trefoil.
This example illustrates that the fragmentation procedure of [17] obscures the
handlebodiness of a given 3-manifold in VTQFT. This is not a problem if one’s
perspective is to sum overall3-manifolds; but from the perspective of crossing
symmetry, we want to be able to distinguish contributions from the sum over identity
blocks from those that cannot be written as a mapping class group image of an
identity block. Fortunately, for trivalent graphs embedded in S 3, there is a simple
test for handlebodiness, which we explain in appendix A.3. A second method of
determining handlebodiness is to study the fundamental group using Wirtinger’s
presentation, and running Whitehead’s algorithm as explained in appendix A.2.
