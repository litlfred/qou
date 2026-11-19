import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:boltzmann-constant",
  label: "rem:gas-constant-derivation",
  title: "Gas constant from $q$ and the Borromean volume",
  tags: [
    "gas-constant",
    "avogadro",
    "borromean-volume",
    "carbon-12",
    "fundamental-constants",
  ],
  uses: ["def:boltzmann-constant"],
  computation: {
    engine: "mpmath",
    script: "computations/snappy_borromean_volume.py",
    witness: "computations/snappy-borromean-volume.witness.json",
    status: "verified",
  },
});
