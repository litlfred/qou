Beyond the dilogarithm, Clausen, and Bloch--Wigner infrastructure catalogued in the preceding remarks, the Tier-A extension layer contains two self-contained algebraic and geometric modules engineered for direct upstreaming into Mathlib4:

| Target Mathlib4 namespace | Tier-A module | Core formalised result | Axioms & status |
|---|---|---|---|
| *RingTheory.LaurentSeries* / *AddMonoidAlgebra* | *LaurentUnits* | Characterises the unit group of the Laurent polynomial ring over an integral domain $D$: $(D[q, q^{-1}])^\times \cong D^\times \times \mathbb{Z}$, specializing to $(\mathbb{Z}[q, q^{-1}])^\times = \{\pm q^m : m \in \mathbb{Z}\}$ via valuation-degree additivity. | $0$ unresolved goals, standard axioms |
| *Topology.PiecewiseLinear* / *GeometricTopology* | *PLPolygonalLink*, *PLConeMap*, *CechGenus4Nerve* | Formalises finite polygonal embeddings in $\mathbb{R}^3$, elementary $\Delta$-moves (triangle Reidemeister ambient isotopy), affine cone maps, and Čech nerve degree invariants for genus-$4$ surface covers ([lickorish1997](#cite:lickorish1997), [rolfsen](#cite:rolfsen)). | $0$ unresolved goals, standard axioms |

Together with the five-term unit-circle restriction (*Cl2PentagonFromBlochWigner*) and the braided monoidal trace helpers (*BraidedQuantumDimension*, *BraidedSlide*, *BraidedTensorDual*, *CauchyBinet*), these Tier-A modules depend exclusively on Mathlib4 and carry zero model-specific vocabulary.
