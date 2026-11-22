import { remark } from "../../schema/builders";

export default remark({
  label: "rem:three-euler-characteristics",
  title: "The three Euler characteristics, and the trace that is not one",
  interprets: "lem:brings-euler-characteristic",
  uses: ["lem:brings-euler-characteristic", "rem:hkr-theorem", "conj:wigner-axiom", "def:hochschild-homology", "def:chern-character"],
  foreshadows: [
    "def:archimedean-condition",
    "rem:chern-character-and-riemann-roch",
    "rem:euler-characteristic-of-the-regular-representation",
  ],
  cites: ["hartshorne-1977", "loday-1998"],
  tags: ["euler-characteristic", "hochschild-homology", "quantum-dimension", "notation", "brings-surface"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): | $w(A)$ | obstruction class of the Wigner axiom | the substrate | pairs to $\\chi_{\\mathrm{eu}}(M_0) = -6$ under the axiom |" },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): **The obstruction class** $w(A)$ of the [Wigner axiom](#conj:wigner-axiom) is the fourth object. It lives in the classical-limit obstruction space, is a class rather than a number, and becomes an integer only through its archimedean image, the Euler class $e(TM_0) \\in H^2(M_0; \\mathbb{Z})$, whose integral is once more $\\chi_{\\mathrm{eu}}(M_0)$. That the obstruction space is a line is the axiom, not a consequence of the axioms of a quantum observable universe." },
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Written for the 2026-09-15 separation (owner selection A: separate by name). Until then the corpus wrote a single `chi(A) = -6` for what are four objects: the topological Euler characteristic of the base curve, the sheaf Euler characteristic of a bundle on it, the quantum dimension `tr(id_X)`, and the obstruction class of the Wigner axiom. Only the first is the `-6` that downstream consumers use. The regularisation figures are from `computations/audits/dimq_regularisation_schemes_probe.py` (16/16) and the identities are proved in `QOU/Information/DimqRegularisationIdentities.lean`; the Hochschild dimensions of the base are the Lean ledger in `QOU/Brings/S5CharactersOnBringDeformations.lean`.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): It is the integer that the [Descartes condition](#def:archimedean-condition) fixes, through the genus:" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([regular representation](#rem:euler-characteristic-of-the-regular-representation))" },
  ],
});
