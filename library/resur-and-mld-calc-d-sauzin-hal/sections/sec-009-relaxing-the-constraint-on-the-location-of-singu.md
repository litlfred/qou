---
doc_id: resur-and-mld-calc-d-sauzin-hal
doc_title: "Resurgence and Mould Calculus"
section_id: sec-009-relaxing-the-constraint-on-the-location-of-singu
section_title: "Relaxing the constraint on the location of singularities."
section_number: null
pages: 8-9
source_pdf: Resur_and_Mld_Calc_D_SAUZIN_HAL.pdf
source_sha256: b33f24cc76102f33
toc_source: outline
doc_brief: "Resurgence and Mould Calculus — 18 sections: Front matter; Introduction; ``Simple'' version of Resurgence T"
---
singularities.
Deﬁnition 8. We call endlessly continuable any bϕ(ζ)
analytic near 0 for which, for every real L > 0, there
exists a ﬁnite subset FL of C such that bϕ(ζ) can be
analytically continued along every Lipschitz path of
length < L starting in the initial domain of deﬁnition
of bϕ and avoiding FL.
Variants are possible—see [CNP93;
KS20],
or
[´Eca85] for the most general deﬁnition (‘continuable
with no cut’). The point is that singular points are
possibly very numerous but, in a sense, still isolated.
This leaves room for a behaviour such as the one en-
visioned by Voros [Vor83b]: there may exist a dense
subset Ωof C such that, at every point of Ω, at least
one of the branches of the analytic continuation of bϕ is
7
singular (but, in any given region of C, one ‘sees’ only
ﬁnitely many singularities at a time: you need longer
and longer paths of analytic continuation to see more
and more singularities in that region).
Denoting by eRs the space of all eϕ(z) ∈B−1(C δ ⊕
C{ζ}) for which bϕ(ζ) is endlessly continuable with at
worst simple singularities for all the branches of its
analytic continuation, we can now deﬁne the alien op-
erators
∆+
ω ∈EndC( eRs), ∆ω ∈DerC( eRs),
for ω ∈C∗
(37)
as follows: given eϕ = B−1(C δ + bϕ) ∈eRs, Deﬁnition 8
allows us to ﬁnd a ﬁnite subset of ]0, ω[, the points of
which we denote by ω1 ≺· · · ≺ωr−1 (with reference
to the natural total order on the line-segment), so that
Deﬁnition 2 can be copied verbatim, except that the
ωk’s do not necessarily lie on any lattice (take any L >
|ω| and {ω1, . . . , ωr−1} := FL∩]0, ω[ in Deﬁnition 8).
Much of what has been said in the case of a lattice
can be generalized to the case of eRs; in particular, this
is a diﬀerential subalgebra of (C[[z−1]], d
dz) and, in the
summable case, we have a passage formula generaliz-
ing (33)–(35):
S {θ} = S {θ′} ◦
 X
ω∈Ω′
P ω
θ,θ′ e−∥ω∥z∆ω

,
θ < θ′,
(38)
(at least in restriction to the simple resurgent series for
which the action of the right-hand side is well-deﬁned),
with a scalar mould Pθ,θ′ deﬁned by
P ω
θ,θ′ :=







1
if r(ω) = 0
1
r1!···rs!
if θ < arg ω1 ≤· · · ≤arg ωr < θ′
0
otherwise,
(39)
where, in the second case, ω = ω1 · · · ωr̸ = ∅, s counts
the number of pairwise distinct arg ωj’s, and r1, . . . , rs
count their multiplicities (r1 + · · · + rs = r).
