import { proof } from "../../schema/builders";

export default proof({
  label: "prf:spectral-sequence-collapse",
  title: "Proof of spectral sequence collapse",
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/probes/centre_frobenius_pairing_is_diagonal_probe.py.",
    },
    {
      kind: "note",
      date: "2026-08-16",
      body:
        "The in-prose **Gap** note (a grading of the centre by partition depth read off a proposition that stratifies by the curvature rank of words) was dated in the prose; the date moved here per the P4:date-ref voice rule. Analysis: `docs/audits/2026-08-16-three-gb-filtrations-one-name.md`.",
    },
    {
      kind: "caveat",
      date: "2026-08-26",
      body:
        "The **Frobenius duality of strata** paragraph is refuted on the centre (bean `qou-xsv8`): distinct central primitive idempotents mutually annihilate, so the pairing on idempotent-spanned strata is diagonal, not anti-diagonal. Measured exactly in ℚ(q) at n = 3 by `computations/probes/centre_frobenius_pairing_is_diagonal_probe.py`. The in-prose note states the mathematics; this records the provenance.",
    },
  ],
  uses: ["prop:spectral-sequence-collapse"],
});
