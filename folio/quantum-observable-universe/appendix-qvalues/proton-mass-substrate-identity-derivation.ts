import { remark } from "../../schema/builders";

export default remark({
  label: "rem:proton-mass-substrate-identity-derivation",
  title:
    "Proton-mass substrate identity — numerical verification, $h$-expansion, and precision frontier",
  interprets: "prop:proton-mass-substrate-identity",
  uses: [
    "prop:proton-mass-substrate-identity",
    "def:f-bor-borromean-observable",
    "prop:flavor-split-substrate",
  ],
  tags: [
    "proton-mass",
    "substrate-identity",
    "numerical-verification",
    "h-expansion",
    "precision-frontier",
    "appendix",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): See-also entry: - [`m_p_substrate_identity_50dps.py`](../../../computations/m_p_substrate_identity_50dps.py)\n  — production-grade compute script (50-dps MPFR)" },
  ],
});
