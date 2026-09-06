---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-006-6-tame-graph-enumeration
section_title: "Tame graph enumeration"
section_number: 6
pages: 16-19
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
Tame graphs are particular plane graphs that represent potential counterex-
amples to the Kepler conjecture. TheArchive is a list of over 5000 plane
graphs. The original proof generates the Archive with the help of a Java
program that enumerates all plane graphs. Tameness is defined in Section 18
and the enumeration is sketched in Section 19 of [22]. This section sketches
the formally machine-checked proof of Claim 3.13 and Theorem 19.1 in the
original proof [22]:
Theorem 1. Any tame plane graph is isomorphic to a graph in the Archive.
There are two potential reasons why an error in the original proof of this
theorem might have gone undetected: the publications only sketch the de-
tails of the enumeration, and the referees only made a passing glance at the
implementation, consisting of more than 2000 lines of Java.
We recast the Java program for the enumeration of all tame graphs in logic,
proved its completeness with the help of an interactive theorem prover, ran
it, and compared the output to the Archive. It turns out that the original
proof was right, the Archive is complete, although redundant (there are at
most 2771 tame graphs). Doing all this inside a logic and a theorem prover
requires two things:
• The logic must contain a programming language. We used Church’s
higher-order logic(HOL)basedon λ-calculus, thefoundationoffunc-
tional programming. Programs in HOL are simply sets of recursion
equations, i.e. pure logic.
• The programming language contained in the logic must be efficiently
executable and such executions must count as proofs. The theorem
prover that we used, Isabelle/HOL [37] fulfills this criterion. If all
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 17
functions that appear in a term are either data, e.g. numbers, or
functions defined by recursion equations, Isabelle/HOL offers the
possibility to evaluate this termt in one big and relatively efficient
step to a valuev, giving rise to the theoremt =v.
The enumeration of all tame graphs generates 23 million plane graphs —
hence the need to perform massive computations in reasonable time.
Now we give a top-level overview of the formalization and proof of complete-
ness of the enumeration of tame graphs in HOL. For details see [36]. The
the complete machine-checked proof, over 17000 lines, is available online in
the Archive of Formal Proofs atafp.sf.net [2].
6.1. Plane graphs. Following the original proof, we represent finite, undi-
rected, plane graphs as lists (= finite sets) of faces and faces as lists of
vertices. Note that by representing faces as lists they have an orientation.
The enumeration of plane graphs requires an additional distinction between
final and non-final faces. Hence a face is really a pair of a list of vertices
and a Boolean. A plane graph isfinal iff each of its faces is. In final graphs
we can ignore the Boolean component of the faces.
6.2. Enumeration of plane graphs. Theoriginalproofcharacterizesplane
graphs by an executable enumeration and sketches a proof of completeness
of this enumeration. We have followed the original proof and taken this enu-
meration as the definition of planarity. The enumeration of plane graphs in
the original proof proceeds inductively: you start with a seed graph with two
faces, the final outer one and the (reverse) non-final inner one. If a graph
contains a non-final face, it can be subdivided into a final face and any num-
ber of non-final ones. Because a face can be subdivided in many ways, this
process defines a tree of graphs. By construction the leaves must be final
graphs, and they are the plane graphs we are interested in: any plane graph
ofn faces can be generated inn− 1 steps by this process, adding one (final)
face at a time. For details see [22] or [36].
The enumeration is parameterized by a natural numberp which controls the
maximal size of final faces in the generated graphs. The seed graphSeedp
contains two(p+3)-gons and the final face created in each step may at most
be a (p + 3)-gon. As a result, different parameters lead to disjoint sets of
graphs.
TheHOLformalizationdefinesanexecutablefunction next-planep thatmaps
a graph to a list of graphs, the successor graphs reachable by subdividing
18 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
one non-final face. The plane graphs are the final graphs reachable from
Seedp via next-planep for somep.
6.3. Enumeration of tame graphs. The definition of tameness in the
original proof is already quite close to a direct logical formulation. Hence
the HOL formalization is very close to this. Of course pictures of graphs
had to be translated into formulae, taking implicit symmetries in pictures
into account. We found one simplification: in the definition of an admissible
weight assignment one can drop condition 3 (a condition on the4-circuits
in graphs) without changing the set of tame graphs. What facilitated our
work considerably was that a number of the eight tameness conditions in
the original proof are directly executable. The details are described else-
where [36].
The enumeration of tame graphs is a modified enumeration of plane graphs
where we remove final graphs that are definitely not tame, and prune the
search tree at non-final graphs that cannot lead to tame graphs anymore.
The published description [22] is deliberately sketchy, and the precise formu-
lation of the pruning criteria is based on the original Java programs. This
is the most delicate part of the proof because we need to balance effective-
ness of pruning with simplicity of the completeness proof: weak pruning
criteria are easy to justify but lead to unacceptable run times of the enu-
meration, sophisticated pruning techniques are difficult to justify formally.
Since computer-assisted proofs are still very laborious, simplifying those
proofs was of prime importance. In the end, the HOL formalization defines
a functionnext-tamep from a graph to a graph list. It computes the list of
plane successor graphsnext-planep g and post-processes it as follows:
(1) Remove all graphs from the list that cannot lead to tame graphs
because of lower bound estimates for the total admissible weight of
the final graph.
(2) Finalize all triangles in all of the graphs in the list (because every
3-cycle in a tame graph must be a face).
(3) Remove final graphs that are not tame from the list.
A necessary but possibly not sufficient check for tameness is used in the last
step. Hence the enumeration may actually produce non-tame graphs. This
is unproblematic: in the worst case a fake counterexample to the Kepler
conjecture is produced, but we do not miss any real ones.
Although we have roughly followed the procedure of the original proof, we
have simplified it in many places. In particular we removed the special
treatment ofSeed0 and Seed1, which is a fairly intricate optimization that
turned out to be unnecessary.
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 19
The following completeness theorem is the key result:
Theorem 2. If a tame and final graphg is reachable from Seedp via next-
planep then g is also reachable from Seedp via next-tamep.
Each step next-tamep is executable and an exhaustive enumeration of all
graphs reachable from a seed graph is easily defined on top of it. We call
this function tameEnump. By definition, tame graphs may contain only
triangles up to octagons, which corresponds to the parametersp = 0,..., 5.
6.4. Archive. Inordertobuildontheaboveenumerationofalltamegraphs
without having to rerun the enumeration, the results of runningtameEnump
with p = 0,..., 5 are put into an Archive and isomorphic graphs are elimi-
nated. This results in 2771 graphs, as opposed to 5128 in the original proof.
The reasons are twofold: there are many isomorphic copies of graphs in the
Archive and it contains a number of non-tame graphs, partly because, for
efficiency reasons, the original proof did not enforce all tameness conditions
in its Java program. The new reduced Archive is also available online [2].
FinallywecanproveTheorem1: if g istameplanegraph, Theorem2andthe
definition oftameEnum tell us thatg must be contained intameEnump for
some p = 0,..., 5. Hence it suffices to enumeratetameEnump, p = 0,..., 5,
and check that, modulo graph isomorphism, the result is the same as the
Archive. This is a proposition that can be proved by executing it (because
the HOL formalization also includes a verified executable test for graph
isomorphism which we do not discuss).
