import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rj-canonical-inner-product",
  title:
    "Canonical bilinear form on $R(H_r(q))$ via Schur orthogonality",
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
      kind: "note",
      date: "2026-10-10",
      body:
        "Until 2026-10-10 this proposition used the excised convention-C parameter $z = (q^{1/2} + q^{-1/2})^{-1}$, with values in $\\mathbb{Q}(q^{1/2})$, half-integer $q$-integers and the quantum dimension $\\prod [h(\\Box)]_q/[h'(\\Box)]_q$; under that convention the form had no radical. The same revision corrected two statements. Part (iii) previously read $J(\\tau(r,s)) = \\sum_{\\lambda \\vdash r} d_\\lambda(q)\\, q^{c_\\lambda s}$: that sum runs over all partitions rather than the hooks, omits the Adams-operation signs, and uses the exponent $c_\\lambda s$ in place of $2 c_\\lambda s / r$. In exact arithmetic over $\\mathbb{Q}(q)$ it agrees with the directly computed trace only for $r = 2$ with $s$ even, that is, for two-component torus links, while the formula above agrees for every coprime pair tested ($r = 2, 3, 4$). Part (ii) previously asserted that every diagonal form compatible with $\\mathrm{tr}_M(1) = 1$ is a scalar multiple of $\\langle -, - \\rangle_{\\mathrm{RJ}}$, which is false as stated; the uniqueness is that of the Markov trace.",
    },
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
        "part (ii) at `r = 2` (`old_form_ii_false_r2`). Part (iii) at `r = 3` for every `s` is " +
        "computed in `H_3(q)` from the Hecke, braid and Markov relations (`h3Trace_rossoJones`, " +
        "`h3Trace_rossoJones_coprime`, `h3_markov_rossoJones`), and Markov uniqueness on `H_3` is " +
        "proved (`H3.markov3_unique_adjoin`). Part (iii) for general `r` and Markov uniqueness " +
        "for `r >= 4` are not formalised; (iii) is cited and checked in " +
        "exact arithmetic for `r = 2, 3, 4` by `computations/probes/rj_inner_product_conventionD_torus_probe.py`. " +
        "Bean `qou-q425`.",
    },
  ],
});
