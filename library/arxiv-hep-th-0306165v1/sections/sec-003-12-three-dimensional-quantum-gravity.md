---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-003-12-three-dimensional-quantum-gravity
section_title: "Three-Dimensional Quantum Gravity"
section_number: 1.2
pages: 4-6
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
toc_source: inferred
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with complex gauge group SL(2,C), which has many interesting connections"
---
1.2. Three-Dimensional Quantum Gravity
As we already mentioned earlier, there are several intriguing connections between
three-dimensional gravity and Chern-Simons theory with complex gauge group GC =
SL(2,C) and imaginary values of the parameter s (for convenience, in what follows we
shall use a real parameter σ = is).
Thus, SL(2,C) appears as the Poincare group in
three-dimensional Euclidean gravity with negative cosmological constant2. Moreover, by
writing the complex gauge ﬁeld A in terms of the real and imaginary components one can
relate the Chern-Simons action (1.1) to the usual form of the Einstein-Hilbert action of
three-dimensional gravity with negative cosmological constant [6,7]. Speciﬁcally, writing
A = w + ie and A = w −ie one ﬁnds
I = k
4π
Z
M
Tr

w ∧dw −e ∧de + 2
3w ∧w ∧w −2w ∧e ∧e

+
+ iσ
2π
Z
M
Tr

w ∧de + w ∧w ∧e −1
3e ∧e ∧e

(1.5)
The second term in this expression is indeed equivalent to the Einstein-Hilbert action3
with negative cosmological constant, Λ = −1, written in terms of the vielbein e and the
spin connection w. We can also write it in the standard form:
Igrav = −1
4π
Z
M
d3x√g

R + 2

(1.6)
As will be shown below, the ﬁrst term in (1.5) also has a nice interpretation. It is
related to the Chern-Simons invariant of the three-manifold M. Therefore, it is convenient
to denote this term as ICS. In the new notations, we can write the original action (1.1) as
I(k, σ) = kICS + iσIgrav
(1.7)
1 See e.g. exercise 6.32 in [4].
2 More precisely, Isom+(IH3) = PSL(2,C) = SL(2,C)/{±1}, but according to [5], a repre-
sentation of PSL(2,C) corresponding to a complete hyperbolic structure can always be lifted to
SL(2,C), and it is SL(2,C) with which we shall work.
3 In our notations, the length scale ℓ= 1 and the Newton constant GN = 1/(4σ).
3
Summarizing, following Witten [7], we conclude that the real and imaginary compo-
nents of the SL(2,C) Chern-Simons action (1.1) have a nice physical interpretation. In
particular, a theory with k = 0 represents, at least (semi-)classically, a three-dimensional
Euclidean quantum gravity with negative cosmological constant4. However, this equiv-
alence does not readily extend to quantum theories due to a number of subtle issues,
typically related to degenerate vielbeins etc. (see e.g. [10] for a recent discussion of these
questions). For example, in the Chern-Simons theory, it is natural to expand around a
trivial vacuum, A = 0, which corresponds to a very degenerate metric, gij = 0. Also, in
the Chern-Simons path integral (1.2) one integrates over all (equivalence classes of) gauge
connections, whereas in quantum gravity one takes only a subset of those corresponding to
positive-deﬁnite volume elements. Nevertheless, one would hope that, for certain questions,
the relation to gravity can still be helpful even beyond the classical limit. Thus, in order to
avoid the above problems throughout the paper we shall mainly consider the semi-classical
expansion around an isolated critical point, corresponding to a non-degenerate metric on
M. Then, the quantum ﬂuctuations are small, and both theories are expected to agree.
So far we discussed a relation between SL(2,C) Chern-Simons theory and pure gravity.
Now let us add sources representing point particles. Assuming that particles don’t have
any internal structure, they can be characterized by two numbers: a mass and a spin. As
we will see later, it is natural to combine these numbers into a single complex quantity,
which labels an inﬁnite dimensional representation of SL(2,C), see [11,12]. Interacting with
gravity, matter particles produce conical defects in the geometry of the space manifold M
[13,14,15]. In particular, light-like particles correspond to cusps in M. We shall say more
about this aspect later, when we will be talking about the relation to hyperbolic geometry.
The coupling of point-like sources to gravity can be described by Wilson lines in the
Feynman path integral (1.4), see e.g. [16,17,18,19]. For example, if we introduce extra
variables pa and xa, which represent momentum and coordinate of a particle in space M,
then the Wilson line operator for a spinless particle can be explicitly written as [16]:
WR(γ) =
Z
Dxa(s)Dpa(s)Dλ(s) exp (iIW )
(1.8)
4 Chern-Simons theory with SL(2,C) gauge group and real values of the parameter s is also
related to three-dimensional gravity, namely to de Sitter gravity in 2+1 dimensions [6,7]. This
theory can be treated similarly, and many of the arguments below easily extend to this case. For
work on quantization of this theory see [1,8,9].
4
where s is a parameter along the “world-line” γ, and IW is the action
IW =
Z
γ
ds

pa
Dxa
Ds −λ(⃗p2 −m2)

(1.9)
In this action, λ is a Lagrange multiplier that enforces the on-shell condition⃗p2 = m2, and
the coupling to gravity is encoded in the covariant derivative
Dxa
Ds = dxa
ds + ws
a
bxb + ies
a
where (es, ws) denotes the restriction of (e, w) to γ.
Eqs.
(1.8) - (1.9) deﬁne an inﬁnite dimensional representation R of SL(2,C) cor-
responding to a spinless particle in three dimensions. In a similar way, one can deﬁne
a general class of inﬁnite dimensional representations corresponding to massive spinning
particles [18] and black holes, which is precisely the class of representations we are going
to assign to Wilson lines WRi(γi) in the Feynman path integral (1.4). Below we shall give
an equivalent geometric description of such system.
