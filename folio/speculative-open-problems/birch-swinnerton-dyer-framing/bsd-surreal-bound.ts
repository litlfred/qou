import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bsd-surreal-bound",
  title: "Surreal $\\omega$-order heuristic for Birch and Swinnerton-Dyer, and why it is not a proof",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "conj:q-birch-swinnerton-dyer",
    "rem:rh-surreal-bound",
    "quantum-observable-universe:def:reeb-epsilon",
    "quantum-observable-universe:def:q-from-epsilon",
    "quantum-observable-universe:prop:surreal-rate-calculus",
    "quantum-observable-universe:lem:surreal-squeeze",
    "quantum-observable-universe:rem:conway-normal-form",
    "quantum-observable-universe:rem:calculus-up-to-epsilon",
    "quantum-observable-universe:rem:adelic-tate-squeeze",
  ],
  cites: ["conway1976", "tate1974"],
  tags: ["surreal", "birch-swinnerton-dyer", "heuristic"],
});
