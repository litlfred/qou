import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-universe",
  label: "rem:axiom-independence",
  title: "Independence of the QU axioms",
  uses: ["def:quantum-universe", "def:frobenius-hopf-substrate", "def:snake-identity"],
  cites: ["deligne1990", "woronowicz1988", "woronowicz1989"],
  tags: ["axiom-independence", "pedagogy"],
});
