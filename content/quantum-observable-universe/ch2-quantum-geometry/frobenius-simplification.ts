import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-universe",
  label: "rem:frobenius-simplification",
  title: "Frobenius structure of the C gauge algebra",
  tags: ["frobenius", "hopf-algebra", "gauge-theory"],
  uses: [
    "def:frobenius-pairing",
    "ex:instanton",
    "ex:irreducible-connection",
    "rem:q-torsion-existence",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/frobenius-simplification-0.svg", blockIndex: 0, hash: "2fc42ad51fa3" },
    { mime: "image/svg+xml", url: "rendered/frobenius-simplification-1.svg", blockIndex: 1, hash: "12ab0d58a12c" },
    { mime: "image/svg+xml", url: "rendered/frobenius-simplification-2.svg", blockIndex: 2, hash: "306594fef116" },
  ],

});
