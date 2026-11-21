import { remark } from "../../schema/builders";

export default remark({
  label: "rem:shell-threading-energy",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): **Connection to molecular chemistry.** The nuclear threading link $L_0$ is the same mathematical object as the molecular threading link $\\mathcal{T}_N = T(2, N)$ that binds atoms in a ring ([molecular Hopf ring](#def:molecular-hopf-ring), [threading link](#def:threading-link)). In benzene, the threading $T(2, 6)$ binds 6 carbons with Alexander weight $\\Delta_{T(2,6)}(q) = q^2 + 1 + q^{-2}$. In nuclear physics, the same construction binds nucleon clusters. The Alexander weight determines the shell correction." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): The threading link framework ([threading link](#def:threading-link), [molecular Hopf ring](#def:molecular-hopf-ring)) gives $\\Delta_{L_0}(q) > 1$." },
  ],
  interprets: "def:molecular-hopf-ring",
  title:
    "Shell energy from the Skein smoothing at the beta-decay vertex",
  lean: {
    ref: "qou:QOU.ShellThreadingEnergy.ShellThreadingEnergy",
    validation: "not_checked",
  },
  tags: [
    "shell-correction",
    "threading-link",
    "skein-resolution",
    "beta-decay",
    "half-life",
    "lambda-shell",
    "molecular-hopf-ring",
  ],
  uses: [
    "lem:pair-skein-mass-formula",
    "def:molecular-hopf-ring",
    "ex:half-life-shell-worked",
  ],
});
