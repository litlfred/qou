import { simulator } from "../../schema/builders";

export default simulator({
  label: "sim:beta-decay-braid",
  title:
    "Beta decay as $T_{3,5}$ braid insertion: crossing budget and transfer matrices",
  tags: [
    "simulator",
    "beta-decay",
    "braid",
    "T35",
    "weak-vertex",
    "transfer-matrix",
    "hecke-algebra",
    "skein-relation",
    "interactive",
  ],
  uses: [
    "def:transfer-matrix-operator",
    "rem:force-knot-identification",
  ],
  html: "folio-assistant/simulators/beta_decay_braid.html",
  defaultView: {
    name: "default",
    title: "Neutron $\\beta^-$ decay braid insertion",
    params: {
      nucleus: "neutron",
      mode: "braid",
    },
  },
});
