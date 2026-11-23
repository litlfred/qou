import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:shared-denominator-cusp-holonomy",
  title:
    "Shared-denominator cusp holonomy: roots of $(x; q)_n$ enforce Thurston completeness",
  lean: {
    ref: "qou:QOU.QPochhammer.shared_denominator_cusp_holonomy",
    validation: "not_checked",
  },
  uses: ["conj:algebraic-geometric-dilog-equivalence"],
  cites: [
    "thurston1978",
    "neumann-zagier1985",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  tags: [
    "q-pochhammer",
    "thurston",
    "cusp",
    "holonomy",
    "gluing-equations",
    "newton-raphson",
    "open-problem",
  ],
  computation: {
    engine: "numpy",
    script: "computations/q_pochhammer_seed.py",
    witness: [
      "computations/q-pochhammer-seed.witness.json",
      "computations/snappy-cusp-seeding.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which\n`IdealTetrahedron.rotate` realises and `rotate_angles` proves leaves the\ntetrahedron unchanged" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **It is already a theorem.** `seed_is_not_the_cusp_shape` (conditional on the class below) gives $z_k \\neq r$ for every real $r$,\nbecause `im_pos` excludes every real shape and the seeds $q_0^{-k}$ are\nreal." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The producer pairs each seed against\n  `M.tetrahedra_shapes`, so what it measures is indexed by\n  **tetrahedron**, not by cusp." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean\nformulation\n`QOU.QPochhammer.shared_denominator_cusp_holonomy` is a conditional\ntheorem over the class `SharedDenominatorCuspHolonomy`, which\ndeliberately has **no instance**: the conjecture's open state is\nvisible in the type system.\n\nWhat makes the class unsatisfiable by fiat is" },
  ],
});
