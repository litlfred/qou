import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:skein-binding-lagrangian",
  label: "rem:skein-binding-lagrangian-derivation",
  title: "Derivation of the Skein binding Lagrangian from the canonical action",
  tags: [
    "lagrangian",
    "binding",
    "skein",
    "nuclear",
    "bethe-weizsacker",
    "canonical-action",
  ],
  uses: [
    "def:skein-binding-lagrangian",
    "prop:qou-canonical-action",
    "def:categorical-lagrangian",
  ],
  computation: {
    engine: "python",
    script: "computations/probes/hbar_q_order_of_binding_observables_probe.py",
    witness: "computations/probes/hbar-q-order-of-binding-observables-probe.witness.json",
    status: "verified",
  },
});
