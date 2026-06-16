import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-integer-mass-table",
  title: "Atomic mass table: seven-term $q$-integer BW formula (MAE 0.020\\%)",
  interprets: "conj:q-integer-mass-formula",
  tags: [
    "mass-table",
    "q-integer",
    "zero-parameters",
    "AME2020",
    "exchange-coulomb",
    "shell-correction",
    "exceptional-divisor",
  ],
  computation: {
    engine: "python",
    script: "computations/channel_product_mass.py",
    witness: "computations/channel-product-mass.witness.json",
    status: "verified",
  },
});
