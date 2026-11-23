import { proposition } from "../../schema/builders";

/**
 * The SU(N) framing of the Hecke generator, and the one-gluon color factors.
 *
 * The Hecke generator sigma (eigenvalues q, -q^{-1}) is the gl_N braiding.
 * Rescaled by q^{-1/N} it becomes the SU(N) braiding, whose log-exponents
 * are exactly twice the one-gluon color factors (C_2(R) - 2C_F)/2. The
 * rescaling is forced by requiring the color singlet Lambda^N V to braid
 * trivially with V; it is not chosen to match the color-factor ratio.
 *
 * ANTI-FITTING: the scalar q^{-1/N} is fixed by the singlet-transparency
 * condition alone (forced_framing_eq_inv). The ratio (N+1)/(N-1) = 2 at
 * N = 3 is then a consequence. The color factors are standard SU(N) group
 * theory.
 *
 * Created 2026-11-15 (bean qou-sl3f, PR #7830). Owner ruling G5 = (a),
 * relayed by the qou-qs0e coordinator: adopt the SU(N) frame for color
 * observables only.
 *
 * Lean: QOU/Braiding/SlNFramingColourFactor.lean, sorry-free, nine
 * declarations. lean.ref names the forcing lemma, which is the block's
 * load-bearing claim; the exponent identities are slExp_sym_eq /
 * slExp_anti_eq / glExp_*_eq / sl_ratio_eq_two_iff in the same namespace.
 * The equality of the monodromy with q^2 is checked on explicit Jimbo
 * matrices (N = 2, 3) and by Young contents (all N) in
 * computations/probes/sl_n_framing_colour_factor_probe.py, not in Lean.
 */
export default proposition({
  label: "prop:sl-n-color-framing",
  title: "The $\\mathrm{SU}(N)$ framing reproduces the one-gluon color factors",
  uses: ["prop:color-su3-from-g2"],
  cites: ["kassel1995", "jimbo1986"],
  lean: { ref: "qou:QOU.Braiding.SlNFraming.forced_framing_eq_inv" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The arithmetic of items 1--4 is machine-checked." },
  ],
});
