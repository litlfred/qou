import { proof } from "../../schema/builders";

export default proof({
  label: "prf:c-equals-bar-iff-all-1dim",
  title: "Proof that charge conjugation equals the bar involution on characters",
  uses: ["prop:c-equals-bar-iff-all-1dim"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body: "Rewritten to prove the corrected statement. Scoped on 2026-11-21: the proof covers $H_3(q)$ on $(2,1)$ (explicit intertwiner, matching the Lean) and the one-dimensional characters. The general-$n$ argument by a bar-twist and Tits deformation is kept as a remark marked not formalised. The earlier proof's counterexample value $+1.892$ was wrong; the exact value equals the uncharged one. The section on the uniqueness of $H_2$ and the lepton-sector reading are removed.",
    },
  ],
});
