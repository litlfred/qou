import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:frobenius-codim-universal",
  label: "rem:frobenius-codim-universal-interpretation",
  title: "Physical content: the tower residual as $\\tau(C_{\\dim_q})$",
  tags: ["frobenius", "tower-residual", "fibre-functor", "m_e", "universality"],
  // def:quantum-universe added 2026-08-14: the new §"What the theorem does and
  // does not supply" locates the content in the Wedderburn-semisimplicity
  // axiom rather than in the identity, and cites it directly.
  uses: [
    "thm:frobenius-codim-universal",
    "conj:partition-sum-proton-residual",
    "def:quantum-universe",
  ],
});
