import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:frobenius-codim-universal",
  label: "rem:frobenius-codim-universal-interpretation",
  title: "Physical content: the tower residual as $\\tau(C_{\\dim_q})$",
  tags: ["frobenius", "tower-residual", "fibre-functor", "m_e", "universality"],
  uses: ["thm:frobenius-codim-universal", "prop:partition-sum-proton-residual"],
});
