import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:toroidal-harmonics-delta-lambda",
  title: "A toroidal-harmonic change of variables and the Markov loop values",
  // `is_mathematics: true` was written as a top-level field. No schema
  // declares it, so zod stripped it silently and the parse succeeded — the
  // declaration reached nothing. Moved into `meta`, the declared escape hatch
  // (`Record<string, unknown>` on `BlockBase`), so it survives validation
  // verbatim rather than being discarded or guessed at.
  meta: { is_mathematics: true },
  lean: { ref: "qou:QOU.QBeta.toroidal_ode_to_markov_w" },
  computation: {
    engine: "sympy",
    script: "computations/qbeta/toroidal_harmonics.py",
    status: "verified",
    witness: [
      "computations/delta-lambda-fr-identity-phase5c.witness.json",
      "computations/vdw-pskew-sinh-probe.witness.json",
      "computations/inter-knot-decoupling.witness.json",
    ],
  },
  uses: [],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-10-10",
      body: "Until 2026-10-10 this block used the excised convention-C weight `z = sqrt(q)/(1+q)` with `q = e^{-eta}`, identifying `w = z^2 = 1/(2(cosh eta + 1))`, so `x = cosh eta`; that identity is exact for convention C only. Under convention D (`z = q^3/(q^2+1)`) it fails (`z^2 = 0.375387` vs `0.249321` at the proton q0), and the block now uses the bar-invariant product `w = z z_- = 1/[2]_q^2`, giving `x = cosh 2 eta`. " +
        /* <!-- literal-source: closed-form Legendre ratios P_{-1/2}/P_{1/2} at sqrt(5)/2 and 3/2 and AME ratio 0.943503 --> */
        "The superseded golden-ratio evaluation `P_{-1/2}/P_{1/2}(sqrt5/2) = 0.944649` (0.12 % from 0.943503) depended on the C identification; under D the same anchor maps to `x = 3/2` and gives `0.804485` (-14.7 %). The ODE change of variables and its Lean proof are convention-independent and unchanged. The producer `computations/qbeta/toroidal_harmonics.py` still states the C framing in comments. Bean qou-nxjw.",
      see: "qou-nxjw",
    },
  ],
});
