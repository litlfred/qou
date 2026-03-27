import { remark } from "../../schema/builders";

export default remark({
  label: "rem:force-knot-identification",
  title:
    "Force carriers from the involutive structure and saturating generators",
  interprets: "prop:torus-embeddable-complete",
  tags: [
    "force",
    "electromagnetic",
    "strong",
    "weak",
    "involution",
    "dagger",
    "torus-knot",
    "crossing-energy",
    "coulomb",
    "symplectic",
  ],
  uses: [
    "rem:unmapped-torus-knots",
    "rem:torus-knot-prime-powers",
    "prop:torus-embeddable-complete",
    "prop:torus-knot-generators",
    "thm:embeddability-closure",
    "def:categorical-proton",
    "prop:antiparticle-crossing-reversal",
    "def:electron-knot",
    "def:positron-knot",
    "def:up-quark",
    "def:down-quark",
  ],
});
