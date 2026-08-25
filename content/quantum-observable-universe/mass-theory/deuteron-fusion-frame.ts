import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:deuteron-fusion-frame",
  title:
    "Fusion frame of the deuteron law: the $5$ is forced by $[2]_v^2 = [3]_v + 1$ and $g$ is the marginal-stability rate",
  lean: { ref: "qou:QOU.MassTheory.DeuteronFusion.fusion_identity" },
  uses: [
    "prop:three-strand-color-winding-rigidity",
    "prop:hoefsmit-toroidal-ladder-locus",
  ],
  cites: ["jones1987", "wenzl1988c"],
  computation: {
    engine: "python",
    script:
      "computations/substrate/deuteron_tower_fusion_frame_probe.py",
    witness:
      "computations/substrate/deuteron-tower-fusion-frame-probe.witness.json",
    status: "verified",
    // Round-tripped "verified" -> "failed" -> "verified" on 2026-08-23, and
    // unlike the other blocks in this sweep NOTHING HERE WAS WRONG — the
    // witness was stale.
    //
    // The one red assertion, `z_canonical_equals_pyhecke_gram_z`, is a
    // deliberate tripwire: the probe's own comment said "expect this to stay
    // red until qou-w8zz lands", because `pyhecke.gram.z` was still convention
    // C while the check compares against the D closed form. That witness was
    // written 2026-08-14 — one day before `gram.z` moved to D. The tripwire
    // then held its red for nine days with nobody re-running it, which is
    // precisely what it was built to do and also why the block sat at a
    // "verified" nobody had checked.
    //
    // Re-run: 7/7 pass, `gram.z` and `q0^3/(q0^2+1)` agree to 0.0, and
    // qou-w8zz / qou-5wpk / qou-9d6h are all completed. The only change to the
    // witness is `z_live_pyhecke` 0.4993203341836945 -> 0.6126880371464652 and
    // the two booleans that follow from it. The tripwire stays in place.,
  },
  tags: [
    "deuteron",
    "binding",
    "fusion-rule",
    "markov-trace",
    "marginal-stability",
    "quantum-dimension",
    "channel-projection",
  ],
});
