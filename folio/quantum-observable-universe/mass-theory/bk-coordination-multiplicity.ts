import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bk-coordination-multiplicity",
  title:
    "The light-nucleus binding multiplicity is the coordination number of $\\mathcal{B}_K$",
  interprets: "conj:binding-manybody-eq-jet-filtration",
  uses: [
    "conj:binding-manybody-eq-jet-filtration",
    "prop:magic-A-binding-formula",
  ],
  cites: ["bezdek-reid2013", "hales-etal2010"],
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
    {
      kind: "caveat",
      date: "2026-08-30",
      body:
        "**Three different quantities in this corpus are written $A-1$, and the braid does not supply the one this block needs.** (i) The producer's `z_coord(A)` is the Python literal `A - 1` ([`bk_crossing_coordination.py:106`](../../../computations/bk_crossing_coordination.py)) — a function of $A$ alone, so $\\mathcal{B}_K$ does **not** enter it and $z$ is identical for ${}^3\\mathrm{H}$ ($8_{11}$) and ${}^3\\mathrm{He}$ (L6a4). The link-dependence of this block lives entirely in $\\mathrm{Vol}$, as the text says; the title's *\"coordination number of $\\mathcal{B}_K$\"* should be read as the coordination number of the $A$-nucleon cluster. (ii) $\\deg_{K_A}(v)=A-1$, the complete-graph degree $z$ *means* (`QOU.Mass.CoordinationBinding.coordination_degree`). (iii) The canonical atomic word `atom_braid_word_3A` has exactly $A-1$ inter-nucleon letters — but they form the **path** $P_A$ (bond set $\\{(k,k+1)\\}$, degree sequence $[1,2,\\ldots,2,1]$), so that $A-1$ is an **edge count**, not a vertex degree, and cannot derive (ii). Both are the same affine function of $A$, so no value of $A$ separates them. Proved sorry-free in `QOU.MassTheory.BraidPathNotCoordination`: the handshake identity forces $A\\le2$ if a cluster carries both counts, so the identification is impossible for every $A\\ge3$; and $P_A=K_A$ iff $A\\le2$. Measured by [`computations/probes/braid_inter_nucleon_adjacency_probe.py`](../../../computations/probes/braid_inter_nucleon_adjacency_probe.py). Scope **(a)** — the bond picture is untouched; the separate scope-(b) exclusion of the linear chain at $q\\neq1$ is `QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff` (bean `qou-m07y`).",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/bk_crossing_coordination.py",
    witness: "computations/bk-crossing-coordination.witness.json",
    status: "verified",
  },
});
