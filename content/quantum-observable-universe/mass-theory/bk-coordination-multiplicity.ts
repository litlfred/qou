import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bk-coordination-multiplicity",
  title:
    "The light-nucleus binding multiplicity is the coordination number of $\\mathcal{B}_K$",
  interprets: "thm:binding-manybody-eq-jet-filtration",
  uses: [
    "thm:binding-manybody-eq-jet-filtration",
    "prop:magic-A-binding-formula",
  ],
  tags: [
    "binding",
    "many-body",
    "coordination-number",
    "link-volume",
    "alpha-cluster",
    "isospin",
    "exploratory",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-11",
      body:
        "**Exploratory — scope-limited (a).** The $z=A-1$ match for the A=3 pair is fit-free, but the overall closure of the open multiplicity $M_n(A)$ is NOT derived from the 13 categorical drivers. The $\\alpha$-cluster per-bond constant $b_{\\alpha\\alpha}\\approx2.41\\,\\text{MeV}$ is a single empirical residual (the classical Hafstad–Teller value), not a derivation. Compute: [`computations/bk_crossing_coordination.py`](../../../computations/bk_crossing_coordination.py); witness `bk-crossing-coordination.witness.json`; audit [docs/audits/2026-07-11-bk-crossing-coordination-multiplicity.md](../../../docs/audits/2026-07-11-bk-crossing-coordination-multiplicity.md). Do not wire into production dashboards until $b_{\\alpha\\alpha}$ and the $n_\\alpha\\ge5$ geometric-packing coordination count are derived.",
    },
  ],
});
