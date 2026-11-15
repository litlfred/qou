import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:im-q-physical-role",
  label: "rem:qstar-decay-sector-q0",
  title:
    "The $S = 0$ point $q^{*}$ is conditional on $c_3^{\\mathrm{even}} = -\\mathrm{Vol}(4_1)$, not an independent determination of $q_0$",
  uses: ["conj:im-q-physical-role", "rem:c3-s-imq-decay-projection"],
  tags: [
    "im-q",
    "decay-width",
    "q-beta",
    "c3-bar-odd",
    "substrate-anchor",
    "mu-p-tension",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "An earlier version of this remark claimed q* was an independent third determination of q₀.",
    },
  ],
});
