import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-observable-universe",
  label: "rem:seiberg-witten",
  title: "Geometric resolution and the Seiberg--Witten differential",
  uses: [
    "rem:brings-smoothness",
    "rem:lagrange-resolvents",
    "rem:chiral-bundles",
    "def:quantum-observable-universe",
    "lem:volume-from-rigidity",
    "rem:holonomy-trefoil",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/seiberg-witten-0.svg", blockIndex: 0, hash: "c74a7197e9db" },
    { mime: "image/svg+xml", url: "rendered/seiberg-witten-1.svg", blockIndex: 1, hash: "70f466e71bad" },
    { mime: "image/svg+xml", url: "rendered/seiberg-witten-2.svg", blockIndex: 2, hash: "d6db2b56da68" },
    { mime: "image/svg+xml", url: "rendered/seiberg-witten-3.svg", blockIndex: 3, hash: "43dc77c4fa70" },
  ],

});
