import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-proton-properties",
  interprets: "def:categorical-proton",
  title: "Proton: NF construction, mass, charge, and computational backing",
  tags: ["proton", "hadron", "baryon", "color-tube", "knot", "categorical"],
  uses: ["def:categorical-proton", "conj:borromean-quark"],
  cites: ["leitner2026"],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: [
      "computations/codata-masses.witness.json",
      "computations/universal-ilp.witness.json",
      "computations/qbeta/qbeta-delta-net-four-values.witness.json",
      "computations/qbeta/integer-lp-gluon-convention-d.witness.json",
      "computations/probes/photon_electron/photon-electron.witness.json",
      "computations/atomic-chirality-residue.witness.json",
      "computations/qbeta/qbeta-convention-d-c3-and-tail-derivation.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**Withdrawn: the LP-stability paragraph** (bean `qou-jqjx`). Three " +
        "sentences are refuted under the live trace convention — that the bare " +
        "9-crossing element violates Frobenius positivity, that a Hopf link is " +
        "the minimum structure capable of restoring stability, and that the " +
        "gluon is strictly required by the LP dual. All three came from " +
        "`fsh-guts/deprecated/computations/integer-lp-gluon.py`, which computes the " +
        "Markov trace with `tr_M(e-) = z^3`. That weight was retired on " +
        "2026-05-19: the correct value by Markov recursion is `h*z^2 + z` " +
        "(`docs/audits/2026-05-19-trm5-markov-bug.md`), and the retired script " +
        "prints its own banner calling `z^3` the correction. The bare nucleon's " +
        "NF is dominated by its `e-` coefficient (about +0.997), so the weight " +
        "is nearly the whole answer.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "The measurement, on the retired script's own typed-nucleon " +
        "construction so that only the convention varies. Retired `z^3`: " +
        "`tr_M = -0.005936` — which is this block's `-0.006`, reproduced. Live " +
        "convention D (`z = q^3/(q^2+1)`, `tr_M(e-) = h*z^2 + z`, what " +
        "`pyhecke.gram` exports and what `computations/universal-ilp.py` " +
        "consumes through `hecke_core`): `tr_M = +0.544370`, and every " +
        "intermediate step of the typed build is stable too (`B_3` +0.998562, " +
        /* <!-- literal-source: intermediate step value from qou-jqjx scratch audit comparing retired z^3 vs live convention D --> */
        "then +0.605510, +0.279195, +0.544370). Nothing is ever negative, so " +
        "there is no instability for a gluon to repair.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "Convention D's Gram matrix is **singular** — `lambda_min ~ 3e-16` " +
        "against a next eigenvalue of 0.753, and the measured null vector " +
        "agrees with `pyhecke.gram`'s closed form `(-1/q)^len(w)` to 3.3e-16. " +
        "That is a real obstacle to inverting `G`, and `gram.py`'s own header " +
        "warns that fixing the trace alone drops a singular Gram into a path " +
        "with nothing to handle it. It does **not** touch this verdict: " +
        "Frobenius positivity tests `G x >= 0`, and `G(x - c*v) = G x` exactly " +
        "when `G v = 0`, so the test is already well defined on the quotient " +
        "by the radical. Measured: the proton carries a large radical " +
        "component (-0.431), and projecting it out moves `min(G x)` by 5.6e-17 " +
        "against a margin of +0.339.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "What replaces the withdrawn claim is not settled, which is why this " +
        "is a status note and not a rewrite. Under D the bare nucleon is " +
        "inside the feasible set, so the gluon LP has a 0-crossing solution; " +
        "under the `|tr_M|` tiebreak the optimum is a single `sigma_0` at one " +
        "crossing (0.339149), and this block's quoted `sigma_0 -> sigma_0` " +
        "falls to rank 10 of 41 at 0.615273 — worse than doing nothing. " +
        "Whether the gluon survives on some other ground (the SDP dual, the " +
        "crossing budget, the net-amplitude route) is open. See " +
        "`rem:gluon-stabiliser-ledger` and the neutron block, whose " +
        "4-versus-2 asymmetry does not survive either.",
    },
    {
      kind: "note",
      date: "2026-08-29",
      body:
        "**Names a different proton stabiliser than " +
        "`rem:stable-atom-properties` does.** This block says *\"a single " +
        "Hopf link $L_- = \\sigma_1\\sigma_0$ is the minimum additional " +
        "structure capable of restoring stability\"*; " +
        "`stable-atom-properties` says the ILP *\"finds the unique integer " +
        "solution $\\sigma_0 \\to \\sigma_0$ (2 gluon crossings)\"*. Both " +
        "are two gluon crossings, so the **count** agrees while the " +
        "**operator** does not. Recorded, not adjudicated: neither block " +
        "cites a computation for its choice. Bean `qou-vtlj`; adjudication " +
        "belongs to `qou-bg3w`.",
    },
  ],
});
