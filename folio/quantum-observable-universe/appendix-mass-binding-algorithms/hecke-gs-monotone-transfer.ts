import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:hecke-gs-monotone-transfer",
  renamedFrom: [
    "alg:categorical-action",
    "alg:gs-reduce-to-hecke-nf",
    "alg:markov-trace",
    "alg:bring-brane",
    "alg:wedderburn-decomposition",
  ],
  title:
    "Completed Hecke Gröbner–Shirshov Reduction and Monotone Fine-Bratteli Transfer Sweep ($\\mathcal{L}_0\\text{--}\\mathcal{L}_2$)",
  uses: [
    "def:hecke-normal-form",
    "prop:markov-trace-axiomatic-closed-form",
    "prop:wedderburn-trace-identity",
  ],
  cites: [
    "bokut2001",
    "kangleeleeoh2002",
    "jones1987",
    "wenzl1988",
    "hoefsmit1974",
    "ram1991",
    "ram1997",
    "geck-lambropoulou-2004",
    "orellana1998",
  ],
  lean: {
    ref: "qou:QOU.QBeta.TemperleyLiebTower.markov_branching_general",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script: "computations/tr_m_atom_via_transfer.py",
    witness: "computations/tr-m-atom-via-transfer.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "groebner-shirshov",
    "markov-trace",
    "transfer-matrix",
    "bratteli-diagram",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Consolidates `mba-step01..05` under `qou-mba8`, fixing the false uncompleted 3-rule confluence claim for `n >= 4` (`NotAGSBasis.hecke_not_gs_basis_four`) via Kang–Lee–Lee–Oh `kangleeleeoh2002` Prop. 4.3 (`bokut2001`) and preserving the monotone fine-Bratteli transfer sweep (`tr_m_atom_via_transfer.py`, witness `tr-m-atom-via-transfer.witness.json`).",
    },
  ],
});
