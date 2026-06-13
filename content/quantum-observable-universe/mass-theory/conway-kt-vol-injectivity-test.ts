import { remark } from "../../schema/builders";

export default remark({
  label: "rem:conway-kt-vol-injectivity-test",
  title:
    "Conway--Kinoshita--Terasaka mutant pair: B1 Vol-injectivity sanity check",
  interprets: "rem:transcendental-accounting",
  uses: [
    "rem:transcendental-accounting",
    "prop:knot-indexed-convolution-grid",
  ],
  cites: ["thurston1978"],
  tags: [
    "mutant-pair",
    "conway-knot",
    "kinoshita-terasaka",
    "vol-injectivity",
    "ruberman-theorem",
    "sanity-check",
    "graded-mikusinski",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "The volumes above are quoted from SnapPy 3.3.2 (Conway:\n$11.31951569027316\\ldots$, KT: $11.31951569027316\\ldots$). High-\nprecision computation at 50 dps would require porting SnapPy's\nhyperbolic-structure routines to mpmath; deferred. The 14-digit\nagreement here is already at machine precision and confirms\nRuberman's theorem.",
    },
    {
      kind: "status",
      body: "**Sanity-check passed; falsification deferred.** The CKT case is\nconsistent with B1 but not a discriminating test. Future work:\nlocate a non-mutant Jones-coincident pair (Anstee–Przytycki–Rolfsen\n1989 has explicit examples; volumes via SnapPy are computable).\nA Bring-embeddable Jones-coincident pair would be the strongest\ntest, but existence is open.",
    },
  ],
});
