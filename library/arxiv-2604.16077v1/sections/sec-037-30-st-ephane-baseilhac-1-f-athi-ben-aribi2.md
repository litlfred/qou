---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-037-30-st-ephane-baseilhac-1-f-athi-ben-aribi2
section_title: "ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2"
section_number: 30
pages: 30-31
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
where a′
0,N ∈ {0, 1,...,N − 1}. Deﬁne
(72) δN := 1
N min{ℑ(Log(u0)),π − ℑ(Log(u0))} and M := |ℜ(Log(u0))|.
We want to apply the reasoning preceding Lemma 3.8 to the term s ˆSN (z + 2kiπ/N ) on the
right side of (69), taking z = l0,N . We ﬁrst notice that δN > 0, and l0,N /∈ (2iπ/N)Z as
required (since u0 ⁄= 1). We then immediately see that
(73) l0,N, l0,N + 2iπ
N ,..., l0,N +
2iπ(N − 1 −a′
0,N )
N ∈ [−M,M ] +i[δN − π
N, 2π −δN − π
N ]
and
l0,N +
2iπ(N −a′
0,N )
N ,..., l0,N + 2iπ(N − 1)
N ∈ [−M,M ] +i[2π +δN − π
N, 4π −δN − π
N ].
These two sequences of scalars realize all the arguments on t he right side of (69) but the last
of the product, l0,N + 2iπ. We can directly apply the inequalities of Lemma 3.3 for z being
any one among the N −a′
0,N values of the sequence (73). The error bound is
(74) Log(c M ) + BδN
N = Log(cM ) + B′
δNN + B′′
N ,
which by (72) is bounded from above by a constant independent ofN . For l0,N + 2iπ or any
of the a′
0,N values of the sequence below (73), we need to modify the corre sponding terms
ˆSN (z + 2kiπ/N ) on the right side of (69), by re-shifting zk :=z + 2kiπ/N usingN times the
formula (52). We have
ˆSN (zk) =
ˆSN (zk − 2iπ)
1 −eNz k
,
each factor 1 −eNz k = 1 −u0 is raised at the power −1/N in (69), and these factors are no
more numerous than N . So the re-shiftings add at worst a bounded non zero term to th e error
bound (74), which changes only c M . Eventually, the ratio of (69) over (70), or equivalently
(71), is bounded from above and below by the product of N +1 positive constants independent
of N , with N of them raised at the power 1 /N. Hence the ratio (69)/(71) is bounded by a
constant. To conclude, it therefore suﬃces to prove that
(75) exp
(N
2iπ Li2(el0,N ) − 1
2iπN Li2(eN l0,N )
)
is bounded from above and below by constants independent of N multiplied withe
N
2π I(Li2(el0,∞ )).
But Li 2(eN l0,N ) = Li 2(u0), and l0,N = l0,∞ +ON →∞
(
N −1)
implies
Li2(el0,N ) = Li 2(el0,∞ ) +ON →∞(1/N)
by a Taylor expansion as in (60) (which is valid, since Li 2 is diﬀerentiable on C \ [1, +∞[, and
eN l0,N =u0 /∈]1, +∞[ implies el0,N /∈]1, +∞[). It follows
exp
(N
2iπ Li2(el0,N )
)
= exp
(N
2π I(Li2(el0,∞ ))
)
exp(ON →∞(1)).
This proves the last claim, and concludes the proof of the lem ma when ℑ(u0) > 0. Similar
arguments apply when ℑ(u0) < 0: take δN = π/N, and start the sequence (73) at l0,N +
2iπ/N. Only the arguments l0,N and l0,N + 2iπ on the right side of (69) are missing from
this sequence and the following one. With these changes one c an conclude by reasoning as
when ℑ(u0)> 0. ✷
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 31
