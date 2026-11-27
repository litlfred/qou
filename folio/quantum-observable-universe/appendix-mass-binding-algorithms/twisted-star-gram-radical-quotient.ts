import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:twisted-star-gram-radical-quotient",
  renamedFrom: ["alg:frobenius-pairing"],
  title:
    "Involution-Twisted $\\ast$-Gram Radical Projection and Nakayama-Twisted Frobenius Verification ($\\mathcal{L}_0\\text{--}\\mathcal{L}_1$)",
  uses: [
    "def:frobenius-pairing",
    "prop:gram-degeneracy-blocks-connes",
  ],
  cites: [
    "jones1987",
    "wenzl1988",
    "temperley-lieb1971",
    "gatermann-parrilo2004",
  ],
  lean: {
    ref: "qou:QOU.Nuclear.GramSignature.markov_star_nonneg",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_frobenius_gram_h3_probe.py",
    witness: "computations/qbeta/qbeta-frobenius-gram-h3.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "frobenius-pairing",
    "star-gram",
    "temperley-lieb",
    "nakayama-twist",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Replaces `mba-step06-frobenius-pairing` under `qou-mba8`, removing the false `S^2 = id` and untwisted Gram non-degeneracy claims on `H_n(q)` (`no_rlinear_hecke_inv_antihom`, `markov_star_nonneg`, `lip_kernel_forces_unbounded`, `TwistedFrobeniusTower`).",
    },
  ],
});
