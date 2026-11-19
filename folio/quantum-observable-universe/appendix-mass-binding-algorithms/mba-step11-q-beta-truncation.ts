import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:q-beta-truncation",
  title: "Convention-D $\\beta$-decay $\\mathfrak{Q}_\\beta$, weak axial coupling $g_A(q)$, and neutron lifetime $\\tau_n$",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:q-beta-cos-resummation",
    "prop:hadron-half-life",
    "alg:mass-identity",
  ],
  tags: [
    "mba",
    "step-11",
    "q-beta",
    "convention-d",
    "axial-coupling",
    "neutron-lifetime",
    "canonical-chain",
  ],
});
