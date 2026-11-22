A topological link enters this paper only through a polygonal representative, and such links are tame. The :refterm[link type]{#link-type} of a polygonal link is a PL notion. Its relation to topological ambient isotopy has two parts.

1. **Smooth isotopies.** If two polygonal links are joined by a $C^1$ ambient isotopy, they have the same link type. This is proved in Lean as `C1AmbientIsotopy.deltaEquiv`, by sampling each component finely enough that the inscribed polygons remain simple and disjoint along the isotopy.

2. **Topological isotopies.** A topological ambient isotopy cannot in general be replaced by a $C^1$ one, because a $C^1$ diffeomorphism cannot carry the carrier of a triangle onto the carrier of a square. In dimension three, topologically ambient isotopic tame links are PL ambient isotopic. This follows from Moise's triangulation theorem and Bing's tameness theorem \cite{moise1952,bing1954}. The paper cites this comparison and does not prove it. In Lean it appears only as the named hypothesis `MoiseBing`, and `AmbientIsotopic.linkType_eq_of_moiseBing` states that topologically isotopic links have equal link type conditional on that hypothesis.

The link type defined here is distinct from the two-element type of [braid link types](#rem:braid-link-types), which enumerates only the unknot and the Hopf link.
