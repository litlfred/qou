---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-003-24-hydrodynamic-limit-and-kpz-limit
section_title: "Hydrodynamic limit and KPZ limit"
section_number: 2.4
pages: 4-5
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
The hydrodynamic limit of TASEP is about h(x, t) when x and t are proportional. For the step initial
condition, h(x, 0) = |x|, Rost [77] showed in 1981 that
h(xT, tT)
T
→¯h(x, t)
almost surely as T →∞, where ¯h(x, t) = t2+x2
2t
for |x| ≤t and ¯h(x, t) = |x| for |x| ≥t. See Figure 6 for the
graph. The hydrodynamic limit ¯h is deterministic, and it solves Burger’s equation [62,63].
The KPZ limit is about the next term, h(xT, tT) −¯h(x, t)T. Setting x = 0 for convenience and following
the 1:2:3 scale, the KPZ universality conjecture suggests that
h(γT 2/3, τT) −¯h(0, τ)T
T 1/3
converges to a 2d random ﬁeld. If we do not set x = 0, then we should consider h(xT +γT 2/3, τT)−¯h(x, τ)T
in the numerator. The limiting 2d ﬁeld, the KPZ ﬁxed point, depends on the initial condition. The step
initial condition for the TASEP becomes the so-called narrow wedge initial condition for the KPZ ﬁxed point.
TASEP has interpretations as an interacting particle system, a random growth process, and a last passage
percolation model.
Each of these interpretations has natural extensions and generalizations.
The KPZ
universality conjecture is that a large class of models in these generalizations has a universal limit. The exact
class is not known, but for random growth models, three key features seem to be the locality of growth, some
smoothing mechanism, and lateral growths. For directed last passage percolation, the universality is expected
for all random variables ws with enough moments and without a large atom at the top of the support of the
distribution. The last condition is to prevent the situation that there is always a path connecting (1, 1) and
(m, n) using only the top value, making the last passage time too concentrated.
4
(t, s)
