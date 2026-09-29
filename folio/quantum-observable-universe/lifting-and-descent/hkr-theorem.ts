import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hkr-theorem",
  title: "The Hochschild–Kostant–Rosenberg theorem, and what it does not say at $q \\neq 1$",
  interprets: "def:classical-limit-obstruction",
  uses: ["def:hochschild-homology", "def:classical-limit-obstruction", "rem:hochschild-kummer-connection"],
  cites: ["hkr-1962", "loday-1998", "kontsevich-2003", "hartshorne-1977"],
  tags: ["hochschild-homology", "hkr", "classical-limit", "deformation-theory", "lifting"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Owner proposal 2026-09-15, enacted: HKR is stated as a CITED THEOREM about the commutative (classical) fibre, and the identification the corpus was using at `q != 1` — the arrow labelled HKR in `rem:hochschild-kummer-connection` — is named as an assumption and folded into `conj:wigner-axiom` rather than presented as a comparison theorem. The corpus-grep for a literature theorem doing this job at `q != 1` found none: formality (Kontsevich) needs a formal deformation parameter, and `q - 1` is evaluated at a real number.",
    },
  ],
});
