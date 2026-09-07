import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "caveat", date: "2026-09-07", body: "**Corrected (bean `qou-43co`).** This block asserted \"This reduction is confluent, making the normal form independent of rule order\" — uncited, and refuted sorry-free by this folio's own Lean at $n = 4$ (`UGB.GrobnerShirshov.HeckeGS.NotAGSBasis.hecke_not_gs_basis_four`). Two further defects were found in the printed rules while fixing it: far commutativity was stated symmetrically as $|i-j| \\geq 2$, which applies to its own output and does **not** terminate; and the Yang–Baxter arrow pointed in the shortlex-*increasing* direction, contradicting the block's own parenthetical and the Lean. All three are measured in `computations/hecke_normal_form_confluence_probe.py` (6/6), which also finds the failure is invisible below $n = 4$ — 0 of 504 words of length $\\leq 8$ over $H_3$ are order-dependent — which is how the claim survived. The completion is stated as the known repair but NOT claimed as established here: the probe's evidence for it is scope-(a) only ($n \\leq 5$, length $\\leq 5$), and the primary — Kang–Lee–Lee–Oh 2002, added this session as `[kang2002]` — is still not held (bean `qou-qspu`)." },
  ],
  label: "def:hecke-normal-form",
  title: "Hecke normal form in $H_n(q)$",
  lean: { ref: "qou:QOU.Braiding.HeckeNormalForm",
    validation: "not_checked",
  },
  uses: ["rem:hecke-algebra-from-braiding"],
  cites: ["bokut2001", "kang2002", "kimlee2018"],
  tags: [
    "hecke-algebra",
    "normal-form",
    "groebner-shirshov",
    "canonical-basis",
  ],
});
