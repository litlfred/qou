import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:whipple-rotation-intertwining",
  title:
    "Whipple–rotation intertwining: the channel rotation acts on the toroidal family as the degree–order (winding) exchange",
  lean: {
    ref: "qou:QOU.MassEndomorphism.WhippleRotationIntertwining",
  },
  uses: ["prop:hoefsmit-toroidal-ladder-locus"],
  cites: ["whipple1917", "ismail-masson1994"],
  computation: {
    engine: "python",
    script:
      "computations/substrate/whipple_rotation_involution_probe.py",
    witness:
      "computations/substrate/whipple-rotation-involution-probe.witness.json",
    status: "verified",
  },
  tags: [
    "whipple-transformation",
    "channel-rotation",
    "toroidal-harmonics",
    "winding-exchange",
    "bar-involution",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling\naxiomatises exactly this as a primary conjecture class\n: the rotation swaps\n\ngradings and is involutive on ladder data. Both fields are\nparameter-quantified in the shape of the claim; no instance is provided\n(the conjecture is open).\n\n*derived from* the class (provable modulo it, no\ninstance):\n\nThe grading-swap field is moreover *not primitive*: `channelIndexed_swaps_windings`\n**derives** it from\n\n proves. A `ChannelIndexedLadder` carries the two\n\nThis does not close the conjecture (no instance is produced): it" },
  ],
});
