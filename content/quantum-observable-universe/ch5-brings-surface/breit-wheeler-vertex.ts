import { remark } from "../../schema/builders";

export default remark({
  label: "rem:breit-wheeler-vertex",
  title: "Breit--Wheeler vertex: photon polarisation states as Hecke generators on the exceptional divisor",
  interprets: "prop:antiparticle-crossing-reversal",
  uses: [
    "def:exceptional-divisor",
    "def:reeb-bundle",
    "def:vertex-operator",
    "rem:chirality-trefoil-electron-positron",
    "prop:antiparticle-crossing-reversal",
  ],
  tags: [
    "breit-wheeler", "photon", "polarisation",
    "pair-creation", "exceptional-divisor", "reeb-bundle",
    "hecke-generator", "trefoil",
  ],
});
