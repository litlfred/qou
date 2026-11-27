import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hkr-theorem",
  title: "The Hochschild–Kostant–Rosenberg theorem, and what it does not say at $q \\neq 1$",
  interprets: "def:classical-limit-obstruction",
  uses: ["def:hochschild-homology", "def:classical-limit-obstruction", "rem:hochschild-kummer-connection"],
  cites: ["hkr-1962", "loday-1998", "kontsevich-2003", "hartshorne-1977"],
  tags: ["hochschild-homology", "hkr", "classical-limit", "deformation-theory", "lifting"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): At $q = 1$ the algebra is the enveloping algebra of a semisimple Lie algebra, and Whitehead's lemmas make $HH^2(\\mathcal{U}(\\mathfrak{g}), M)$ vanish for finite-dimensional $M$, so the obstruction space of the classical fibre is zero, not a line." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): The [classical limit obstruction](#def:classical-limit-obstruction) is $HH^2(\\mathcal{U}_q(\\mathfrak{g}), \\mathrm{Ad})$, the Hochschild cohomology of a *noncommutative* algebra at $q \\neq 1$, and the Hochschild–Kostant–Rosenberg theorem says nothing about it." },
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Owner proposal 2026-09-15, enacted: HKR is stated as a CITED THEOREM about the commutative (classical) fibre, and the identification the corpus was using at `q != 1` — the arrow labelled HKR in `rem:hochschild-kummer-connection` — is named as an assumption and folded into `conj:wigner-axiom` rather than presented as a comparison theorem. The corpus-grep for a literature theorem doing this job at `q != 1` found none: formality (Kontsevich) needs a formal deformation parameter, and `q - 1` is evaluated at a real number.",
    },
  ],
});
