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
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (see witness assertions). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
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
