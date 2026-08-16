---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-010-42-formal-products-and-composition
section_title: "Formal products and composition"
section_number: 4.2
pages: 20-20
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Suppose a and b are the relative homology classes of two open paths on ˜Σ. If the end
of a coincides with the start of b, we let a +b denote the relative homology class of the
concatenation of a and b. Then we introduce a product law on our formal variables:
XaXb =
{
Xa+b if the end of a is the start of b,
0 otherwise .
(4.3)
Figure 7 . Three surface defects connected by two interfaces. (This picture lives in the three-
dimensional space where the ﬁeld theory S[g,C,D ] is deﬁned; we have factored out the time direc-
tion.)
We can now state one of the key properties of the generating functions F (℘,ϑ ): if ℘
and ℘′ are paths on C which can be concatenated to make a smooth path ℘℘′ (with the
end of ℘ attached to the start of ℘′), and if both (℘,ϑ ) and (℘′,ϑ ) are generic, then
F (℘,ϑ )F (℘′,ϑ ) =F (℘℘′,ϑ ). (4.4)
Here is the physical reason for (4.4). We consider three surface defects Sz1, Sz2, Sz3,
connected by two interfaces L℘,ϑ and L℘′,ϑ, as shown in Figure 7. The Hilbert space H
of framed BPS states in this situation should be independent of the separation between
the interfaces. For large separations, since the framed BPS states are localized near the
interfaces,H is a tensor product between a space of framed BPS states for the interface ℘
and one for the interface℘′. On the other hand, by considering the limit of zero separation,
we see thatH is the space of framed BPS states for the interface ℘℘′. Equating these two
descriptions ofH gives (4.4).
(One could wonder whether there should be a ± sign on the right side of (4.4); this
amounts to asking whether our rules for ﬁxing the signs of F (℘,ϑ ),F (℘′,ϑ ) and F (℘℘′,ϑ )
are compatible with one another. Fortunately, it will follow from our explicit rules below
that there is no sign needed.)
