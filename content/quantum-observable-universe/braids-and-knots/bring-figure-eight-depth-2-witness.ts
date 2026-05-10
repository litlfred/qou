import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-figure-eight-depth-2-witness",
  title:
    "Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)",
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/gb_depth_period_bring_fig8.py",
    witness:
      "folio-assistant/computations/gb-depth-period-bring-fig8.witness.json",
    status: "verified",
  },
  uses: [
    "conj:gb-depth-period-correspondence",
    "def:brings-coordinate-ring",
    "rem:figure-8-archimedean-illustration",
    "prop:q-dilogarithm-exists",
    "conj:kashaev-volume-conjecture",
  ],
  cites: [
    "thurston1978",
    "neumann-zagier1985",
    "bloch2000",
    "suslin1991",
    "kashaev1997",
  ],
  tags: [
    "depth-2",
    "figure-8-knot",
    "bring",
    "hyperbolic-volume",
    "bloch-wigner",
    "clausen",
    "graded-mikusinski",
    "numerical-witness",
    "50-digit-precision",
  ],
});
