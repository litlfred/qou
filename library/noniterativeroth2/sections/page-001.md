---
doc_id: noniterativeroth2
doc_title: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS"
section_id: page-001
section_title: "Page 1"
section_number: null
pages: 1-1
source_pdf: noniterativeroth2.pdf
source_sha256: 83bbcdf45da069e5
toc_source: undetermined
doc_brief: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS — We present a proof of Roth’s theorem that follows a slightly diﬀerent structure to the usual proofs, in that there is not much iteration."
---
A PROOF OF ROTH’S THEOREM ON ARITHMETIC
PROGRESSIONS
ERNIE CROOT AND OLOF SISASK
Abstract. We present a proof of Roth’s theorem that follows a slightly diﬀerent
structure to the usual proofs, in that there is not much iteration. Although our proof
works using a type of density increment argument (which is typical of most proofs of
Roth’s theorem), we do not pass to a progression related to the large Fourier coeﬃcients
of our set (as most other proofs of Roth do). Furthermore, in our proof, the density
increment is achieved through an application of a quantitative version of Varnavides’s
theorem, which is perhaps unexpected.
1. Introduction
Given an integer N ⩾1, let r3(N) denote the size of any largest subset S of [N] :=
{1, ..., N}, for which there are no solutions to
x + y = 2z, x, y, z ∈S, x̸ = y;
in other words, S has no non-trivial three term arithmetic progressions.
In the present paper we give a proof of Roth’s theorem [4] that, although iterative, uses
a more benign type of iteration than most proofs.
Theorem 1.1. We have that r3(N) = o(N).
Roughly, we achieve this by showing that r3(N)/N is asymptotically decreasing. We
will do this by starting with a set S ⊆[N], |S| = r3(N), such that S has no three
term progressions, and then convolving it with a measure on a carefully chosen three
term arithmetic progression {0, x, 2x}. The set T where this convolution is positive will
have very few three term arithmetic progressions; and, by making use of a quantitative
version of a theorem of Varnavides [7], we will show that r3(M)/M is much larger than
r3(N)/N, for M = (log N)1/8−o(1). This will clearly imply that r3(N) = o(N). Alas,
the upper bound that our method will produce for r3(N) is quite poor, and is of the
quality r3(N) ≪N/ log∗(N).
Many of the other proofs of Roth’s theorem, in particular [1], [3], [5], and [6], make use
of similar convolution ideas; however, none of these methods convolve with such a short
progression as ours (three terms only), and none use Varnavides to achieve a density
increment. Furthermore, it seems that our method can be generalized to any context
where: (1) the number of three term progressions in a set depends only on a small
The ﬁrst author is funded by NSF grant DMS-0500863; and, the second author is funded by an
EPSRC DTG through the University of Bristol.
