import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unit-modulus-eigenvalue",
  title:
    "Eigenvalues of even braids on $V_{(2,1)}$ and the Borromean trace",
  uses: [
    "prop:borromean-markov-trace-closed-form",
    "prop:hoefsmit-binding-amplitude",
  ],
  lean: { ref: "qou:QOU.BraidsAndKnots.borromean_trace_standard" },
  tags: [
    "eigenvalue",
    "unit-modulus",
    "borromean",
    "meson",
    "wedderburn",
    "standard-rep",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body:
        "**Corrected 2026-11-16 (QA finding: da-non-sequitur, critical).** The block " +
        "claimed unit-modulus eigenvalues for every even word and " +
        "$\\chi_{(2,1)}(\\beta_{\\mathrm{Bor}}) = -2$ (eigenvalue $-1$). Both are false: " +
        "$\\sigma_1^2$ has eigenvalues $q^{\\pm 2}$, and the Borromean trace is " +
        "$-(q^4-q^2+1)(q^8-2q^6-2q^2+1)/q^6 \\approx 1.994$ at $q_0$ (Lean-proved on an " +
        "explicit model). The Lean theorem that derived $\\lambda = -1$ from the false " +
        "hypothesis is removed. **Mass-derivation note:** the block's claim that the " +
        "factor $\\dim V_{(2,1)} = 2$ in the proton substrate identity comes from a " +
        "subtracted $(2,1)$ channel is withdrawn; no producer reads it. Two exploratory " +
        "probes use a Reeb phase $\\arccos(\\chi/d)$ and silently clamp $|\\chi/d|$ to $1$ " +
        "(`e0_lambda_composite.py`, `h2o_angle_knot_correction.py`), so on a growth block " +
        "they report $\\theta = 0$ instead of flagging it. Neither is a production producer.",
    },
  ],
});
