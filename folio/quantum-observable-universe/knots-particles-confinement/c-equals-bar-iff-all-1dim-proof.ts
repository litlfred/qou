import { proof } from "../../schema/builders";

export default proof({
  label: "prf:c-equals-bar-iff-all-1dim",
  title: "Proof that charge conjugation equals the bar involution on characters",
  uses: ["prop:c-equals-bar-iff-all-1dim"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body: "Rewritten to prove the corrected statement ($C = \\mathrm{bar}$ on every irreducible character, by a bar-twist and Tits deformation). The earlier proof's counterexample value $+1.892$ was wrong; the exact value equals the uncharged one. The section on the uniqueness of $H_2$ and the lepton-sector reading are removed.",
    },
  ],
});
