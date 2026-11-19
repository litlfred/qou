import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-identity-remark",
  title: "Value, trace, state sum and braid-class invariance of the inertial mass",
  interprets: "def:mass-identity",
  uses: [
    "def:mass-identity",
    "def:frobenius-pairing",
    "def:recursive-brane-tower",
  ],
});
