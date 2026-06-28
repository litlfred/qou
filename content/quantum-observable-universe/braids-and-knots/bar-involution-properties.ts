import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bar-involution-properties",
  interprets: "def:bar-involution",
  title:
    "Bar-involution properties: the $P_{\\mathrm{avg}}$ / $P_{\\mathrm{skew}}$ projections, the canonical classification of QOU quantities by bar-type, the key algebraic identities ($c_5$, Hoefsmit-Quantum-2, half-step factorization of $h$), the geometric / Kac–Sunada readings, and the $\\mathbb{Z}/2\\mathbb{Z}$ bar-grading proofs",
  uses: [
    "def:bar-involution",
    "prop:c5-involution-leibniz-decomposition",
    "prop:silver-ratio-beta-decay-null",
    "def:categorical-q-reeb-flow",
    "prop:chirality-residue-mass-term",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "categorical-action",
    "notation",
    "classification",
  ],
});
