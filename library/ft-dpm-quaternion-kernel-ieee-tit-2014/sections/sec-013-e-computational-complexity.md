---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-013-e-computational-complexity
section_title: "Computational Complexity"
section_number: E
pages: 7-7
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Table I illustrates the computational complexity of kernel
regression algorithms for scalar, quaternion, multikernel and
matrix-kernel approaches. Observe that scalar kernels are
simplest, whereas the complexity of matrix kernels grows
quadratically with the dimension of the signal.
In order to compare the complexity associated to vector- and
quaternion-valued kernels, observe that (i) μR involves four
pure real multiplications (real kernels, quaternion weights)
while μQ involves 16 (quaternion valued kernels and weights),
and (ii) the quaternion kernel evaluation can be seen as the
evaluation of four real functions. Consequently, by assuming
κQ ∼4κR, μQ ∼4μR, Table I shows that the computational
complexities of both kernel and quaternion kernel algorithms
are of the same order.
Therefore, the implementation of both vector and quaternion
kernels can beneﬁt from exploiting the similarity among sub-
kernels, as well as from an efﬁcient framework to perform
quaternion operations [46].
