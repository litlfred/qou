---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-005-4-stuff-types
section_title: "Stuff Types"
section_number: 4
pages: 14-14
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
We have described a structure type as a functor F∈ Set[Z], where the image
of each ﬁnite set S is the set of structures “of type F ” which can be put on S,
but it should be obvious that the category Set is rather larger than we need, since
for most sorts of structures we can think of, almost all sets will no t appear in the
image at all - most are not sets of F structures on an n-element set for any F orn.
If we think of a category X whose objects are precisely the structures of type F ,
and whose morphisms are those maps which arise from bijections of t he underlying
sets, we have a category better suited to F . This category is, in fact, a groupoid
(i.e. a category in which all morphisms are iso), since FinSet0 is.
If we do this, however, we now have not sets of F structures as objects, but
F -structures themselves, and there are many such structures c orresponding to each
n. So now it is more natural to think of F as a functor:
F : X→ FinSet0
where each object of X is taken to its underlying set, and each morphism to the
underlying bijection of sets. So every morphism in the image, FinSet0, then comes
from morphisms in X under this F . A functor with this property is called faithful.
Why should we make this changed to the deﬁnition of a structure typ e? There
are at least two good reasons to take this approach. One is that, w hile the previous
deﬁnition ﬁt well with the view of formal power series in which we are int erested
in ﬁnding the coeﬃcient of the nth power of z, this deﬁnition allows us to think
of F as corresponding to a power series which we evaluate at various (po sitive)
real numbers to get other (positive) real numbers. To see how th is works, we ﬁrst
remark that it will make sense to think of a structure type F being evaluated at a
groupoid, and so we need some useful facts about these.
