import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qou-motivic-galois-instance",
  title:
    "QOU $\\mathrm{MotivicGaloisCharacter}$ instance via Habiro $\\to \\mathrm{Frob}_p$",
  tags: [
    "motivic-galois",
    "frobenius",
    "habiro",
    "qou-substrate",
    "instance",
    "axiom",
  ],
  interprets: "def:motivic-galois-character",
  uses: [
    "def:motivic-galois-character",
  ],
  cites: ["habiro2002", "yekutieli2010", "tate1967"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-12",
      body:
        "**Lean status (2026-08-12):** the co-located `.lean` file (which contained a bare `axiom` laundering the perpetual obstruction into the `MotivicGaloisCharacter` class) has been deleted. The formalization now lives in `lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean` (Route A: prime-ideal-collapse proof, $C = a_0(-1) + 2 a_1(-1)$, sorry-free).",
    },
    {
      kind: "note",
      date: "2026-08-22",
      body:
        "**Block kind (2026-08-22):** demoted from `definition` to `remark`. A `definition` requires a Lean sibling, and the one this block had was the axiom-laundering instance deleted above — so the block asserted a formalized instance the corpus no longer carries. It is not retargeted at the theorems in `MotivicPerpetualObstructionFromTrace.lean`, because those conclude `¬IsUnit (4 : ℤ)` and `¬IsUnit (−32 : ℤ)`: statements about two integers, whose types mention neither the prime `p` nor the exception set `S`, and whose proof terms discard both binders. Pointing a definition at them would record it as formalized by something that says nothing about it. Tracked as bean `qou-lrnd`; the construction itself is unaffected and stays witnessed by `computations/probes/habiro_frobenius_probe.py`.",
    },
    {
      kind: "note",
      date: "2026-08-22",
      body:
        "**Follow-up (2026-08-22):** that same file now also carries `habiro_frobenius_not_unit` and its proton/deuteron instances, whose conclusion is `¬ IsUnit (frob p)` — the Frobenius itself, with `p` in the statement rather than as decoration. They are sorry-free and take the mod-`𝔭` collapse `reduce p (frob p) = C` as an explicit hypothesis, because that identity is derived symbolically in the probe and not in Lean. The block stays a `remark`: a conditional theorem is not an instance, and supplying the hypothesis is exactly the open step.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/probes/habiro_frobenius_probe.py",
    witness:
      "computations/probes/habiro-frobenius-probe.witness.json",
    status: "verified",
  },
});
