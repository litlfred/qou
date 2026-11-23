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
  uses: ["rem:torus-knot-prime-powers"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "§III Weak force: the previous identity $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ cannot hold in $H_n(q)$, since its left side equals $(q - q^{-1})[2]_q P_+$, which is not a scalar. It is replaced by the corpus Skein relation $L_+ - L_- = (q - q^{-1})L_0$ (AGENTS.md §7a) and by the proved identities `QOU.QuarkState.Helicity.skein_asym_eq` (q-weighted difference $= (q-q^{-1})[2]_q P_+$), `skein_mirror_eq` (mirror weighting gives $P_-$) and `QOU.QuarkState.OneSidedWeakVertex.two_smul_oneSidedL_eq_skein` ($[2]_q W_L = [2]_q\\sigma - (q\\sigma - q^{-1}\\sigma^{-1})$). These are library declarations with no content block, so they are not `uses[]` edges. The crossing-count and W/Z-mass sentences are scoped as model statements without derivation (owner decision relayed 2026-11-15, bean qou-hlx7).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Under the definition of the left line as the eigenline on which $\\sigma_i$ acts with eigenvalue of modulus greater than $1$, the choice is no longer a separate convention: weighting the positive crossing by that eigenvalue gives a multiple of the left projector ([the weak vertex insertion](#prop:weak-vertex-left-projector))." },
  ],
});
