---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-023-63-multiple-shocks
section_title: "Multiple shocks"
section_number: 6.3
pages: 38-39
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Next, let us comment on states perturbed by multiple precursors as in Eq. 6.1. As
before, we will consider a compact boundary theory but this time perturbed n spheri-
cally symmetric shock waves described by shifts hi∼e− 2π
β (t∗±ti), with a “+” for i odd
and a “−” for i even. We will also assume that all the shocks are strong, hi≫ 1. One
can easily construct these geometries following the recipe of [29]. In [6], it was found
that the total complexity of the state, using CV-duality, is given by
C∼ tf− 2nsbt∗, (CV-duality), (6.16)
where tf is the length of the total time fold of the state, and nsb is the number of
operators that are inserted at switchbacks. A time fold is a convenient depiction of
the construction of an out-of-time order state, such as Eq. 6.1. The total length of the
time fold tf was deﬁned in [6] as
tf≡|t1−tR| +|t2−t1| +...|tL−tn|, (6.17)
and it was assumed that |ti−ti+1| > t∗. We already discussed switchbacks in §6.1.
From the perspective of the time fold, a switchback is an operator insertion where the
time fold “folds” back on itself. An example time fold is shown in Fig. 11. An insertion
could fail at a switchback if the (i + 1)th precursor in the state Eq. 6.1 cancels against
the time evolution of the ith precursor. See [6] for more details.
It’s easy to see, following the procedure outlined §6.1, that the CA-duality repro-
duces this result. Let us prune the list of precursors so that only those at switchbacks
are represented in the state Eq. 6.1. An example geometry with four shocks is shown
in Fig. 12. The gray “postcollision” regions are complicated and cannot be described
by the (u,v ) coordinates. (For more details, see [29].) However, if the strengths of all
of the shocks are strong hi≫ 1, these regions become small and have vanishing action.
37
Figure 11: A time fold with six operator insertions. This time fold depicts
the construction of the out-of-time order state with six precursor insertions:
e−iHLtLW (t6)W (t5)W (t4)W (t3)W (t2)W (t1)e−iHRtR|TFD⟩, where all the operators are
understood to act on the left. In this ﬁgure, all of the insertions except for t5 occur at
switchbacks.
The only contribution will be from the ﬁve-sided regionII s. With n shock waves, there
will be n + 1 ﬁve-sided regionII s contributing to the action. The contribution of each
one is given by Eq. 6.12, and the ith one (counting from the right) gives
Ai = 2M β
2π loghi−1hi, (6.18)
where we have abused notation so thath0 =v0,hn+1 =u0, we have assumedtL,tR > 0,
and we have assumed an even number of shocks for simplicity. Summing over all
regions, we get precisely that the action of the Wheeler-DeWitt patch grows as
An shocks = 2M(tf− 2nsbt∗) (CA-duality). (6.19)
