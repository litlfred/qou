---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 3-5
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
For a linear space W⊂ Rn, g∈ W is an elementary vector if g is a support minimal nonzero
vector in W , that is, no h∈ W\{ 0} exists such that supp( h) ⊊ supp(g), where supp denotes
the support of a vector. A circuit in W is the support of some elementary vector; these are
precisely the circuits in the associated linear matroid M(W ). We let F(W )⊆W andCW⊆ 2n
denote the set of elementary vectors and circuits in the spac e W , respectively.
Elementary vectors were ﬁrst studied in the 1960s by Camion [ Cam64], Tutte [ Tut65], Fulk-
erson [ Ful68], and Rockafellar [ Roc69]. Circuits play a crucial role in matroid theory and have
been extremely well studied. For regular subspaces (i.e., k ernels of totally unimodular matri-
ces), elementary vectors have ±1 entries; this fact has been at the heart of several argument s in
network optimization since the 1950s.
The focus of this paper is on various circuit imbalance measures . We give an overview of
classical and recent applications, and their relationship with other condition measures. We will
mainly focus on applications in linear programming, mentio ning in passing also their relevance
to integer programming.
Three circuit imbalance measures There are multiple ways to quantify how ‘imbalanced’
elementary vectors of a subspace can be. We deﬁne three diﬀere nt measures that capture various
fractionality and integrality properties.
We will need some simple deﬁnitions. The linear spaces {0} and Rn will be called trivial
subspaces; all other subspaces are nontrivial. A linear subspace of Rn is a rational linear space
if it admits a basis of rational vectors. Equivalently, a rat ional linear space can be represented
as the image of a rational matrix. For an integer vector v∈ Zn, let lcm( v) denote the least
common multiple of the entries |vi|, i∈ [n].
For everyC∈C W , the elementary vectors with support C form a one-dimensional subspace of
W . We pick a representative gC,W∈F (W ) from this subspace. If W is not a rational subspace,
we select gC,W arbitrarily. For rational subspaces, we select gC,W as an integer vector with the
largest common divisor of the coordinates being 1; this choi ce is unique up to multiplication by
−1. When clear from the context, we omit the index W and simply write gC . We now deﬁne
the fractional circuit imbalance measure and two variants o f integer circuit imbalance measure.
Deﬁnition 1.1 (Circuit imbalances) . For a non-trivial linear subspace W⊆ Rn, let us deﬁne
the following notions:
• The fractional circuit imbalance measure of W is
κW := max
{ ⏐⏐⏐⏐⏐
gC
j
gC
i
⏐⏐⏐⏐⏐ : C∈C W,i,j ∈C
}
.
• If W is a rational linear space, the lcm-circuit imbalance measure is
˙κW := lcm
{
lcm(gC ) : C∈C W
}
.
• If W is a rational linear space, the max-circuit imbalance measure is
¯κW := max
{
‖gC‖∞ : C∈C W
}
.
For trivial subspaces W , we deﬁne κW = ˙κW = ¯κW = 1 . Further, we say that the rational
subspaceW is anchored, if every vector gC , C∈C W has a ±1 entry.
3
Equivalently, in an anchored subspace every elementary vec tor g∈F (W ) has a nonzero
entry such that all other entries are integer multiples of th is entry.
The term ‘circuit imbalance measure’ will refer to the fractional measure κW . Note that
1≤ κW≤ ¯κW≤ ˙κW and κW = 1 implies ¯κW = ˙κW = 1. This case plays a distinguished role
and turns out to be equivalent to W being a regular linear space (see Theorem 3.4).
Another important case is when ˙ κW = pα is a prime power. In this case, W is anchored,
and κW = ¯κW = ˙κW . The linear space will be often represented as W = ker(A) for a a matrix
A∈ Rm×n. We will use F(A),CA,κA, ˙κA, ¯κA to refer to the corresponding quantities in ker( A).
An earlier systematic study of elementary vectors was done i n Lee’s work [ Lee89]. He mainly
focused on the max-circuit imbalance measure; we give a quic k comparison to the results in
Section 3. The fractional circuit imbalance measure played a key role in the paper [ DHNV20] on
layered-least-squares interior point methods; it turns ou t to be a close proxy to the well-studied
condition number ¯χW . As far as the authors are aware, the lcm-circuit imbalance m easure has
not been explicitly studied previously.
Overview and contributions Section 2 introduces some background and notation. Sec-
tion 3 gives an overview of fundamental properties of κW and ˙κW . In particular, Section 3.1
relates circuit imbalances to subdeterminant bounds. We no te that many extensions of totally
unimodular matrices focus on matrices with bounded subdete rminants. Working with circuit
imbalances directly can often lead to stronger and conceptu ally cleaner results. Section 3.2
presents an extension of the Hoﬀman-Kruskal characterizati on of TU matrices. Section 3.3
shows an important self-duality property of κW and ˙κW . Section 3.4 studies ‘nice’ matrix rep-
resentations of subspaces with given lcm-circuit imbalanc es. Section 3.5 proves a multiplicative
triangle-inequality for κW . Many of these results were previously shown by Lee [ Lee89], Appa
and Kotnyek [AK04], and by Dadush et al. [ DHNV20]. We present them in a uniﬁed framework,
extend some of the results, and provide new proofs.
Section 4 reveals connections between κW and the well-studied condition numbers ¯χ studied
in the context of interior point methods, and δ studied—among other topics—in the analysis
of the shadow simplex method. In particular, we show that pre vious diameter bounds for
polyhedra can be translated to strong diameter bounds in ter ms of the condition number κW
(Theorem 4.8).
Section 5 studies the best possible values of κW that can be achieved by rescaling the vari-
ables. We present the algorithm and min-max characterizati on from [ DHNV20]. Further, we
characterize when a subspace can be rescaled to a regular one ; we also give a new proof of a
theorem from [ Lee89].
Section 6 shows variants of Hoﬀman-proximity bounds in terms of κW that will be used
in subsequent algorithms. In Section 7, we study algorithms for linear programming whose
running time only depends on the constraint matrix A, and reveal the key role of κA in this
context. Section 7.1 shows how the Hoﬀman-proximity bounds can be used to obtain a b lack-box
algorithm with κA-dependence as in [ DNV20], and Section 7.2 discusses layered least squares
interior point methods [ DHNV20, VY96].
Section 8 gives an overview of circuit diameter bounds and circuit aug mentation algorithms,
a natural class of LP algorithms that work directly with elem entary vectors. As a new result, we
present an improved iteration bound on the steepest-descen t circuit augmentation algorithm, by
extending the analysis of the minimum mean-cycle cancellin g algorithm of Goldberg and Tarjan
(Theorem 8.4).
Section 9 gives an outlook to integer programming, showing the relati onship between the
max-circuit imbalance and Graver bases. Finally, Section 10 formulates a conjecture on circuit
decompositions with bounded fractionality.
4
