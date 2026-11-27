import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-topological",
  title: "Proof of the standard-representation matrix inequality",
  uses: ["prop:confinement-topological"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Rewritten (`qou-6hm4`) to prove the exact statement of `prop:confinement-topological` " +
        "(`QOU.Interactions.gram_indefinite_witness`: $L_+^2 + L_-^2 \\neq 2 L_+ L_-$ over $\\mathbb{Z}[t^{\\pm 1}]$ " +
        "by comparing the degree-$4$ Laurent coefficients at entry $(0,0)$). " +
        "Excises the refuted Part (i) $v_-$ LP-descent claim ($t \\cdot v_- = 0$ identically and $G v_-$ has a " +
        "negative component, while $t \\cdot x = (Gx)_0 \\ge 0$ across the feasible cone) and the refuted " +
        "Part (iii) $4^6$ enumeration (`confinement_b3_enumeration_recheck_probe.py`).",
    },
  ],
});
