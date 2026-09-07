---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br"
section_id: sec-009-5-conclusion
section_title: "CONCLUSION"
section_number: 5
pages: 7-7
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
doc_brief: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br — The Geometric Buchberger algorithm is a specialization of the clas- sical"
---
In this paper, we introduced a new efficient criterion for trunca-
tion of Grébner basis elements for integer programs with binary
variables. We have also introduced a new Grébner basis implemen-
tation of an integer programming solver with the package IPGBs.jl,
which we have empirically shown to be more efficient than the
previous state-of-the-art, specially in cases where our new binary
truncation criterion applies.

Even so, our experiments have shown that pure Grébner ba-
sis methods have difficulty solving even moderately sized integer
programs in reasonable time. We believe that, for the majority of
integer programming applications, this is inevitable, but that it is
still possible to both improve these Grébner basis methods and
to integrate them with classical integer programming algorithms
profitably. Moreover, current applications in integer programming
with non-linear constraints [10] and multiobjective integer pro-
gramming [12] are already able to profit from the improvements to
Grébner basis computations available in IPGBs.

Further improvements to the Geometric Buchberger algorithm
may be possible by adapting other ideas developed in the context
of Grébner bases of arbitrary ideals to the particular case of toric
ideals, such as the use of sparse linear algebra for reduction [7] and
signature algorithms [6, 8]. However, such specializations are not
guaranteed to lead to good empirical results, since reductions and
useless S-polynomial elimination are already much more efficient
in the toric case.

340

ISSAC ’24, July 16-19, 2024, Raleigh, NC, USA

In order to expand the applicability of Grébner basis techniques
to a wider variety of optimization problems, it would be interesting
to be able to work with mixed integer programming, containing
both real and integer variables. A step in this direction was given in
[13], where finite representations of Graver bases for mixed integer
programs were defined. Other open questions include potential uses
of partial Grébner bases as primal heuristics in branch-and-bound
algorithms and as generic neighborhoods in local search meta-
heuristics, as well as using group relaxations as a way to tighten
dual bounds in branch-and-bound. We consider that using Grébner
bases in such a hybrid fashion with classical integer programming
methods is the most likely path to the usefulness of Grébner bases
in general-purpose integer programming.
