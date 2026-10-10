import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rj-canonical-inner-product",
  title:
    "Canonical inner product on $R(H_r(q))$ via Schur orthogonality",
  tags: [
    "rosso-jones",
    "representation-ring",
    "inner-product",
    "schur-orthogonality",
    "quantum-dimension",
    "markov-trace",
    "uniqueness",
  ],
  lean: { ref: "qou:QOU.Archimedean.rj_canonical_inner_product",
    validation: "not_checked",
  },
  uses: [
    "prop:cohomological-embedding",
  ],
  cites: [
    "rosso-jones1993",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**Lean status: partial, sorry-free.** `QOU/Archimedean/rj_canonical_inner_product.lean` " +
        "no longer carries the self-assuming `HeckeRepRingContext` (its fields " +
        "`claim_unique_up_to_scalar`, false, and `jonesPoly_eq_eval`, the convention-C sum, were " +
        "projected out as theorems). Proved over a generic field: `z = q^2/[2] = z_D`; the " +
        "hook-content dimensions `d_(r) = [r+1]` and `d_(m,1) = [m]`; part (iii) at `r = 2` for " +
        "every `s`, computed in `H_2(q)` (`h2Trace_rossoJones`); and the refutation of the old " +
        "part (ii) at `r = 2` (`old_form_ii_false_r2`). Part (iii) for general `r` and the " +
        "Markov-uniqueness content of (ii) are not formalised; (iii) is cited and checked in " +
        "exact arithmetic for `r = 2, 3, 4` by `computations/probes/rj_inner_product_conventionD_torus_probe.py`. " +
        "Bean `qou-q425`.",
    },
  ],
});
