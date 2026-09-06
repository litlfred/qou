---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-012-the-gravitational-machine
section_title: "The gravitational machine"
section_number: null
pages: 46-52
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
The examples discussed above suggest a general procedure that systematically con-
structs a minimal set of 3-manifolds that should be summed over in the bulk, in order
to satisfy the constraints imposed in section 2 on the moments of the CFT data. In
this section, we will introduce this algorithm—the gravitational machine—in full
generality. It will generalize both the Dehn surgery and the Ω-loop computations
of the previous section and works for manifolds with arbitrary number of boundary
components of any genusg⩾1. We will formulate the rules on the level of the
fixed-Ppartition functions, i.e. for networks of Wilson lines in VTQFT. It is simple
to change the formulation into the canonical ensemble by thickening the Wilson lines
and considering the drilled out manifold with the asymptotic conformal boundary.
Cylinder surgery.The main topological operation in the gravitational machine is
what we will callcylinder surgery. This procedure can be described as follows. Given
a (possibly disconnected) network of Wilson lines in VTQFT, surround one of the
edges by a 2-punctured sphere, and carve out its interior to obtain a new manifold
with a 2-punctured sphere boundary. Do the same with another edge, and glue the
two 2-punctured spheres to each other with the opposite orientation:
P1 P2
glue
.(4.20)
We call this ‘cylinder surgery’, because the 3-manifolds in VTQFT are the comple-
ment of a regular neighborhood of the Wilson line network embedded inM E, so that
the 2-punctured sphere along which we glue becomes a cylinder. This was illustrated
in the introduction in figure 2.
WhenP 1 andP 2 belong to two disconnected networks of Wilson lines, corre-
sponding to disjoint manifoldsM 1 andM 2, the above construction is similar to a
connected sum of 3-manifolds, in which one removes two empty balls and identifies
the resulting S 2 boundaries. In this case, cylinder surgery is a generalization of the
connected sum ofM 1 andM 2, now including Wilson lines. We will denote it by
M1#P1∼P2M2 ,(4.21)
withP 1 andP 2 the Wilson line labels that get identified.
When theP 1 andP 2 Wilson lines are part of the same connected VTQFT dia-
gram, with corresponding graph complementM, we denote cylinder surgery by
M#P1∼P2.(4.22)
We will also refer to this as ‘self-gluing’ throughout the rest of the paper.
– 46 –
Reformulating Dehn surgery.Let us see how the above procedure generalizes
the Dehn surgery that we described in section 4.1. We can think of the modified
manifold in (4.3) as being obtained by applying cylinder surgery to the original
manifoldM 1 (with Wilson lineP 1), and a genus-1 handlebodyM 2 (i.e. one of the
PSL(2,Z)-family of solid tori). The fixed-Pversion of the genus-1 handlebody can
be represented in VTQFT as:
p/q
P
(4.23)
embedded in S 3. Thus, we can view the Dehn surgery operation (4.3) onM 1 as
the result of gluing a genus-1 handlebody toM 1 by removing a ball neighborhood
around a pair of Wilson lines and identifying the boundaries, that is,M 1#P1∼P2M2.
For example, whenM 1 is a genus-2 handlebody, we have:
p/q
∼=
p/q
glue
.(4.24)
This requires of course to identify the Wilson line labels of the two Wilson lines that
get glued together. On the RHS, before gluing, the genus-1 and genus-2 Wilson line
networks are embedded in two disjoint copies of S 3.
Reformulating self-contractions.Let us also see how cylinder surgery generates
the bulk manifolds discussed in section 4.1 that contribute to the index contractions
predicted by typicality. In the examples given in (4.11) and (4.16), we used the
Ω-loop encircling a pair of Wilson lines to produce the delta functionδ(P 1−P 2).
Topologically, this is equivalent to doing the cylinder surgery described above, see
also (C.38).
For example, the non-handlebody manifold (4.16) that contributes to the double
self-contractionC111C111 can also be constructed from the following self-gluing:
Ω Ω
2
1
3
∼=
1 2 3
.(4.25)
This can be seen from the figure (4.20) by slicing it horizontally through the
middle. In the top half of the figure, take the hemispheres punctured byP 1 and
P2 and puff up the Wilson lines so that the punctured hemispheres becomes annuli.
When we glue, these become a torus. Doing the same with the bottom half of the
figure, we get two tori that are glued to each other with the identity map, thus making
the background manifold S 2×S 1. This is precisely what the Ω-loop implements.
– 47 –
Cylinder surgery in VTQFT.In cylinder surgery, we glue along a 2-punctured
2-sphere. The corresponding Hilbert space in VTQFT is one-dimensional (provided
that the labels of the Wilson lines agree). Thus the gravitational path integral inM 1
andM 2 has to produce the unique state up to proportionality and we obtain:
ZVir[M1#P1∼P2M2] = δ(P1−P 2)
ρ0(P1) ZVir[M1]ZVir[M2].(4.26)
The proportionality constantρ 0(P1)−1 can be understood in two ways. First, after
surgery we have one edge less in the VTQFT diagram, so the normalization factor
ρC
g(P) should get one fewer factor ofρ 0. Second, we note that forM 1 andM 2 both
unknots in S3, the connected sum is also an unknot in S3. Using thatZ Vir(unknot) =
ρ0(P) explains the proportionality factor. 24
For self-gluing, the same reasoning gives:
ZVir[M#P1∼P2;P 1,P 2,...] = δ(P1−P 2)
ρ0(P1) ZVir[M;P 1,P 1,...].(4.27)
In the special case thatM=M 1⊔M 2 is a disjoint union, we recover (4.26).
Statistical interpretation.Cylinder surgery has a clear interpretation from the
boundary ensemble point of view. Namely, consider some momentXY, whereXand
Yare products of OPE coefficients and densities of states. XYnecessarily includes
the disconnected momentXY, which is described gravitationally by considering the
disconnected union of the set of manifolds computing the lower moments Xand Y.
Now, the typicality assumption also forces us to include connected contractions of
the indices inXandY, which are constructed in the bulk via cylinder surgery. That
is, letM 1 be a manifold contributing to XandM 2 a manifold contributing to Y.
Then we should add toXYthe manifold corresponding to the diagonal contraction by
excising a ball around two Wilson lines and identifying their boundaries, i.e. applying
the cylinder surgeryM 1#P1∼P2M2 as above.
Adding crossing transformations.Once we have added a new topologyMthat
was obtained using cylinder surgery, such as the4 1 handlebody-knot in (4.25), we
must also include its sum over mapping class group images in order to preserve
24We may regard (4.26) as the VTQFT analog of the identity for the partition function on
manifolds constructed as connected sums in ordinary TQFTs (e.g. based on a modular tensor
category). In particular, forM=M 1#M2, we haveZ TQFT(M) = ZTQFT(M1)ZTQFT(M2)
ZTQFT(S3) . This
equation is derived by carving out a three-ball from each ofM 1 andM 2 and gluing them along the
resulting S2 boundaries. This operation is not allowed in VTQFT: the Hilbert space on the naked
S2 is ill-defined, the total quantum dimension badly diverges, and indeed hyperbolic manifolds are
prime and so cannot be written as connected sums anyway. However the generalization with Wilson
lines (4.21) as implemented by (4.26) does (under certain conditions) lead to hyperbolic manifolds,
as we shall see below.
– 48 –
crossing symmetry. More precisely, we sum over the boundary mapping class group
modulo the bulk diffeomorphisms ofM, i.e. the coset [11]:
MCG(∂M)/MCG(M,∂M).(4.28)
Here MCG(M,∂M) is the bulk mapping class group ofM, containing the large dif-
feomorphisms ofMthat preserve the boundary setwise. On the level of the VTQFT
diagrams, this means we can act with any of the crossing transformationsB,Fand
S, as in equations (3.57), (3.59) and (3.60), up to the relations of the Moore-Seiberg
groupoid and the identifications by the bulk mapping class group.
Crucially, these crossing transformations map VTQFT partition functions with
delta functionsδ(P i−Pj) to partition functions without delta functions. For example,
recall the4 1 handlebody-knot (4.16), which is a contribution to the double contrac-
tion C111C111. If we act with S-transforms on its bells, we get a smooth function of
P1,2,3 that is a product of two S-kernels, written in (5.10) and further analyzed there.
Hence, crossing symmetry combined with typicality predicts a non-handlebody con-
tribution to C112C233, even whenP 1,2,3 are all different.
Similarly, recall the Dehn surgery (4.3), which was needed in order to reproduce
the correct factors ofρ MWK as in (4.9). Acting with crossing transformations on the
VTQFT diagram gives an amplitude that is no longer of the factorized form (4.2);
hence a new PSL(2,Z)-family of Dehn surgeries must be added for consistency with
modular invariance of the lower moments ρi. To illustrate this, consider the sunset
diagram (with Dehn surgery) and act with anFmove:
γ2γ1 γ3
2
1 3
F24
−−−−−→ 1
4
3
γ2
γ1 γ3
.(4.29)
Hereγ i specify the Dehn surgery parameters, which we assume to be non-trivial.
On the RHS, the VQTFT amplitude is not of the factorized form ¯ρ 1 ¯ρ3 ¯ρ4C114C334.
At the same time, the Dehn fillingγ 2 has resulted in a new non-contractible cycle,
namely the loop surrounding theP 4 edge. We can restore the factorized form by
adding a fourth Dehn surgery around this loop and summing overγ 4∈PSL(2,Z)/Z.
Iterating this procedure generates more and more complicated contributions to the
sum over geometries, e.g.:
γ2 →
γ2
γ4
→
γ5
γ2
γ4
→ ···(4.30)
This mechanism applies to any VTQFT diagram and will be an essential ingredient
in the formulation of the gravitational machine, to which we turn next.
– 49 –
The general gravitational machine.Having introduced all the necessary ingre-
dients, we come to formulate the general gravitational machine, which produces a
set of manifoldsMconsistent with all properties of the boundary statistical ensem-
ble that we imposed in section 2. The idea is to give a finite set of ‘moves’ which
inductively define a set of orientable 3-manifolds 25
M∈M.(4.31)
As an initial condition, we assume thatMcontains all handlebodies of genusg,
which is the minimal set needed for consistency with crossing. From this initial set,
we define a finite number of operations that produce new manifolds, which we also
have to include in the sum over topologies for consistency with the other conditions
imposed in section 2 (including the ones discussed above). We will again think of
the resulting manifolds at the level of networks of Wilson lines (i.e. in the fixed-P
formalism), but they can as always be thickened to pass to the canonical ensemble.
The three moves of the gravitational machine are as follows:
1. ForM 1 andM 2 inM, the disconnected manifoldM 1⊔M 2 is also allowed.
2. For anyM∈M, we are allowed to perform crossing transformations on the
Wilson line network representing the boundary data.
3. ForM∈M, we can apply the cylinder surgeryM# P1∼P2 on any pair of Wilson
lines, whereP 1 andP 2 are identified. This surgery can either glue different
connected components ofMor it can glue the same component to itself.
For the third move, we have to make some additional technical assumptions that we
discuss below. Next, for each application of one of these moves, one should check 26
whether the resulting topology is already part of the setM, and if not, add it toM.
This algorithm generates an infinite set of bulk manifolds. Then, when we compute
the average of any CFT quantity Z[Σ] (where Σ may be disconnected), we use the
dictionary (1.1) to sum over allM∈Mwith∂M= Σ.
This defines a minimal sum over topologies that is consistent with the statistical
bootstrap defined in section 2. From the point of view of the statistical description
of the boundary CFT 2, move 1 ensures that any statistical moment XYcontains
at least the disconnected contribution XY, which always exists. Move 2 ensures
crossing symmetry of each moment, as defined in (2.13). Lastly, move 3 ensures that
all index contractions exist as demanded by typicality (2.21).
25Mcan in principle also contain manifolds with conical defects described by light Wilson lines.
However, here we will restrict ourselves to the ‘pure’ gravity case without defects.
26Hyperbolic manifolds are completely specified topologically by their fundamental groupπ 1(M).
Since the machine generates only hyperbolic manifolds (as we will show), checking homeomorphism
comes down to testing for isomorphism of the fundamental group. This can be highly non-trivial
in practice, see for example the computation in appendix A.2.
– 50 –
There are three more technical conditions that we have to impose on the cylinder
surgery operationM# P1∼P2 in move 3. Namely, consider the Wilson linesP 1 andP 2
in the manifoldMbefore gluing, and letm 1 andm 2 be loops around these Wilson
lines. These loops define elements of the fundamental groupπ 1(M). 27 We assume
that these group elements satisfy the following conditions:
a)m 1 andm 2 are not contractible. In other words, the elements they define in
π1(M) are non-trivial.
b)m 1 orm 2 is primitive, i.e. not a power of another element inπ 1(M).
c) For self-gluings, i.e. wherem 1 andm 2 are in the same connected component,
⟨m1⟩does not have a non-trivial intersection with a conjugate of⟨m 2⟩inπ 1(M).
The first condition a) means that neitherm 1 norm 2 are Ω-loops, since they are
not contractible in the bulk. If eitherm 1 orm 2 would be contractible, i.e. bound a
disk, then the Wilson line label is projected to the identity Wilson line. 28 However,
the identity does not behave in a statistical way since it is constant throughout
the ensemble. In particular, for the typicality ansatz (2.20) it was assumed that
all operators are different from the identity, because for OPE coefficients with an
identityC 123 the right hand side is simply dictated by conformal symmetry. So
condition a) is natural from the ensemble point of view.
The second condition b) appears from requiring that we do not include discon-
nected moments more than once. To see why this is necessary, consider a Wilson
line that has already been Dehn filled, and apply a second Dehn surgery:
γ1
not allowed
−−−−−−→
γ1 γ2
(4.32)
Using (4.7), this Dehn surgery along parallel loops would lead to the enhancement of
ρ0(P)ρ 0( ¯P) to thesquareofρ MWK(P, ¯P), which does not make sense from the CFT
point of view. To see why the condition b) forbids the move in (4.32), we note that
on the LHS, after a single Dehn fillingp/q, the loop around the Wilson line admits
ap-th root and is no longer primitive as an element ofπ 1. The converse also holds:
if a loop around a Wilson line is not primitive, then we can write the geometry as a
Dehn filling of a simpler geometry where the loop is primitive. Thus primitivity of
the loop around the Wilson line formalizes the notion of a Dehn filling already being
present, which explains condition b). 29
27ForMdisconnected, sayM=M 1⊔M 2 withm 1 a loop inM 1 andm 2 a loop inM 2, they define
elements inπ 1(M1) andπ 1(M2) respectively.
28For example, this happens for the middle edge of the dumbbell diagram as illustrated in (3.38).
29We remark that it can be non-trivial to ascertain whether a parallel Dehn-filled arc already
exists, since this is in principle a complicated topological condition and the parallel arc might
be knotted in non-trivial ways. The cleanest way to formulate this condition is in terms of the
fundamental group, which is what we have done in condition b).
– 51 –
The third condition c) simply says that we are not allowed to glue the same Wil-
son line to itself, since that would clearly not make sense from a boundary statistical
viewpoint. The phrasing in c) of this simple statement is a bit technical, due to the
fact thatm 1 andm 2 are only defined up to conjugation and thus we have to demand
thatm 1 is not conjugate tom 2. In fact, we required the slightly stronger condition
that powers ofm 1 are also not conjugate to powers ofm 2. This says that we are
also not allowed to glue a Wilson line to a power of itself, i.e. to a loop that winds
several times around the same Wilson line.
