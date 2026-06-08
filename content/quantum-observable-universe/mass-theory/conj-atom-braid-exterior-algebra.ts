import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:atom-braid-exterior-algebra",
  lean: { ref: "qou:QOU.BraidKnot.AtomBraidExteriorAlgebra.AtomBraidExteriorAlgebraStructure" },
  title:
    "Canonical atom-braid `atom_braid_word_3A(Z, N)` in `H_{3A}(q)` generates a sub-algebra graded-isomorphic to the exterior algebra Λ*(ℂ^{3A−Z}) with grade shift δ = Z−1; total dim = 2^{3A−Z}, k-th component dim = C(3A−Z, k−δ). Empirically verified across D, T, ³He, ⁴He.",
  uses: [],
  cites: [],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Empirically verified across 4 atoms (D, T, ³He, ⁴He) via the " +
        "R5-full ⁴He Rust solver extension** (this PR). Filtration shapes " +
        "are Pascal's triangle row (3A−Z) shifted by δ = Z−1; totals are " +
        "2^{3A−Z}. **NOT** the standard Wedderburn ⊕_λ V_λ^d_λ dim (which " +
        "would be n_0! ~ 5×10⁸ for ⁴He; observed is 2¹⁰ = 1024 — 8 orders " +
        "of magnitude smaller). The exterior-algebra / fermion-Fock-space " +
        "structure is a NEW categorical observation; categorical proof " +
        "open. Crystal-basis connection: Λ*(V) = q-deformed fermion Fock " +
        "space; the Z-shift looks like a charge-sector label.",
    },
  ],
  tags: [
    "tier:S",
    "atom-braid",
    "exterior-algebra",
    "fermion-fock-space",
    "schur-weyl",
    "crystal-basis",
    "hecke-algebra",
    "R5-full",
    "open-conjecture",
  ],
});
