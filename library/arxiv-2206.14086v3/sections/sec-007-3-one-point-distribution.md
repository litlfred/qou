---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-007-3-one-point-distribution
section_title: "One-point distribution"
section_number: 3
pages: 5-5
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
One-point distribution
We discuss one-point KPZ limit theorems from [6] and [53] mentioned in the introduction, and extensions
to other models.
3.1
Poisson DLPP
Poisson directed last passage percolation is a variation of the exponential DLPP. Consider a realization of
a 2d Poisson process in R2
+. An up/right path p this time is deﬁned as the graph of a continuous piecewise
linear function of positive slopes connecting Poisson points, as shown in Figure 7. Let E(p) denote the
number of the Poisson points on p. For (t, s) ∈R2
+, deﬁne
L(t, s) = sup
p E(p),
where the supremum is taken over all up/right paths p from (0, 0) to (t, s). The next theorem follows from [6].
The main theorem of [6] is stated for the case of a ﬁxed number of points, but the paper proves the Poisson
points case ﬁrst, from which the main theorem follows. Since L(t, s)
d= L(
√
ts,
√
ts), the next result applies
to general points (t, s).
Theorem 3.1 ( [6]). For every x ∈R,
lim
t→∞P
L(t, t) −2t
t1/3
≤x

= FTW(x)
where FTW is the Tracy-Widom distribution.
The 1/3-power in t1/3 is consistent with the height scale of the KPZ universality: see (2.1). This result
shows that the one-point marginal of the KPZ ﬁxed point (for the narrow wedge initial condition) must be
distributed as the Tracy-Widom distribution. The Tracy-Widom distribution is the limiting distribution of
the largest eigenvalue of random Hermitian matrices such as Gaussian unitary ensemble matrices [86]. The
connection of the KPZ ﬁxed point and random matrix theory was surprising and unexpected. See Section
9.3 for more on this connection.
