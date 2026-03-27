import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-observable-universe",
  label: "rem:adjoint-trace",
  title: "Adjoint trace and the categorical inner product",
  uses: [
    "def:quantum-observable-universe",
    "prop:fiber-adjoint-involution",
    "def:frobenius-pairing",
  ],
  tags: ["adjoint", "trace", "inner-product", "frobenius"],
});
