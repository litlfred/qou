---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-016-121-properties-of-growth
section_title: "Properties of Growth"
section_number: 12.1
pages: 40-41
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Let’s review some facts about the growth of wormhole volume that follow from the black
hole geometry. First of all, except for an early transient, lasting about a thermal time, the
growth is linear with time. In the two-sided case the rate of growth of the volume satisﬁes,
dV (t)
dt ∼ladsAT (12.34)
wheret is the anchoring time, A is the horizon area, T is the black hole temperature, and
lads is the AdS length scale. This is not hard to show using the AdS black hole metric but
an easier argument is just dimensional analysis. In the one-sided case the asymptotic rate
of growth is half that of the two-sided case.
Let’s deﬁne a geometric quantityC (yes, we will eventually identify it with complexity,
39
but not yet),
C≡ V
Glads
(12.35)
Then 12.34 gives
dC
dt = A
GT (12.36)
and using the Hawking-Bekenstein area-entropy relation
dC
dt =ST (12.37)
In a little while we will see that this is the expected rate of growth of complexity for a
circuit with K∼S qubits.
