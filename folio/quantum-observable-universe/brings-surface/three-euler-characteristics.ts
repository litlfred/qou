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
