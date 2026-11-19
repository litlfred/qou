import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:color-superconductivity-borromean",
  label: "rem:cfl-neutron-star-observables",
  title:
    "Observable signatures of the Borromean-to-CFL transition in neutron stars",
  tags: [
    "neutron-star",
    "CFL",
    "mass-radius",
    "gravitational-waves",
    "cooling",
    "falsifiability",
  ],
  uses: [],
  computation: {
    engine: "mpmath",
    script: "computations/borromean_volume_propagation_to_m_p.py",
    witness: "computations/borromean-volume-propagation-to-m-p.witness.json",
    status: "verified",
  },
});
