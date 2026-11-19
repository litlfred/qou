import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-universe",
  label: "rem:quantum-universe-axiom-motivation",
  title: "What each axiom buys",
  tags: [
    "quantum-universe",
    "braiding",
    "frobenius-hopf",
    "spherical",
    "motivation",
    "so3",
  ],
  uses: ["def:quantum-universe", "def:frobenius-hopf-substrate", "def:snake-identity"],
});
