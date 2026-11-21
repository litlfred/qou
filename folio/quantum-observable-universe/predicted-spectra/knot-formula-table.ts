import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:knot-particle-generation",
  label: "rem:knot-formula-table",
  title: "Topological knot formulas for fundamental and composite particles",
  tags: [
    "knot",
    "formula",
    "notation",
    "particle",
    "hadron",
    "nucleus",
    "generation",
    "fermion",
    "boson",
    "torus-link",
  ],
  // Earlier `uses[]` listed `conj:higgs-t28`, which transitively
  // typed every block citing this remark as downstream of an open
  // conjecture (per `docs/audits/conjecture-cones.md` "Methodology"
  // — case (2) cleanup). The table is a forward narrative reference
  // ("Higgs as T(2,8)") that interprets the conjecture; the
  // conjecture's content does not feed the table. Citation moves
  // to prose only.
  uses: [
    "thm:embeddability-closure",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: the quark shorthand $\\mathfrak{u} = T_{2,3}$ etc. gave each quark its lepton partner's knot, genus and crossing number (Table 2). Changed: the shorthand now uses the dictionary's arrow, and Table 2 gives each quark genus $0$ and crossing number $0$ (the unknot, as in `ParticleKnots.lean` `UpQuark`/`DownQuark`) with its braid letter and partner. Needs re-scoping: any composite formula in this remark or its users that counted a quark's genus or crossings from the trefoil. The nucleon shorthand $[\\mathfrak{u}, \\mathfrak{u}, \\mathfrak{d}]_p \\oplus \\mathcal{L}_H$ is unaffected." },
  ],
});
