import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:electroweak-higgs-torus-link-triplet",
  title:
    "$(W^\\pm, Z, H) \\leftrightarrow (T(2,4), T(2,6), T(2,8))$ — non-Bring even-twist 2-component torus-link triplet",
  lean: {
    ref: "qou:QOU.Archimedean.EWHiggsTorusLinkTriplet",
    validation: "not_checked",
  },
  uses: [
    "prop:electroweak-triplet-bring-embedding",
    "prop:force-carrier-bring-uniqueness",
    "prop:torus-knot-genus-four-unique",
    "conj:n-v-bring-action",
    "def:hecke-normal-form",
    "rem:hecke-algebra-from-braiding",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-05",
      body:
        "Top node of the electroweak identification conjecture lattice " +
        "(Lean file: five §3b classes — C1 selection [primary], " +
        "C2 enumeration [dependent on C1], C3 charge [primary], " +
        "C4 spin [primary], C_top identification [dependent on C1/C3/C4]). " +
        "The genus/enumeration/embedding half is discharged to the " +
        "sorry-free `prop:electroweak-triplet-bring-embedding`. Residual, " +
        "stated plainly: C1 selection has strong corpus grounding " +
        "(genus-4 saturation of {T(2,9),T(3,5)}); C3 (charge) and C4 (spin) " +
        "are OPEN — a link's Seifert genus does not see charge or spin, so " +
        "no genus/embedding argument closes them. C4 (scalar H vs vector " +
        "W/Z) is the deepest gap.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/probes/ew_higgs_sdp_probe.py",
    witness: "computations/probes/ew-higgs-sdp-probe.witness.json",
    status: "verified",
  },
  tags: [
    "electroweak",
    "higgs",
    "torus-link",
    "non-bring",
    "psd-feasibility",
    "weak-sector",
    "force-carrier",
    "open-problem",
  ],
});
