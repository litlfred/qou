import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:strangelet-witten-stability",
  label: "rem:strangelet-merger-signature",
  title:
    "Strangelet deconversion energy in neutron star mergers",
  tags: [
    "strangelet",
    "neutron-star",
    "merger",
    "kilonova",
    "gravitational-waves",
    "neutrino-burst",
    "phase-transition",
    "falsifiability",
  ],
  uses: [
    "rem:strangelet-witten-stability",
    "prop:eos-borromean-cfl",
    "rem:cfl-neutron-star-observables",
  ],
});
