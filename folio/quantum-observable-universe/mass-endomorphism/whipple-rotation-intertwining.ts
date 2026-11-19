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
    {
      kind: "note",
      body: "Lean declarations in `whipple-rotation-intertwining.lean` (`QOU.MassEndomorphism`): primary conjecture class `WhippleRotationIntertwining`, derived theorems `nuGrade_square` and `gradingPair_intertwines_swap`, structure `ChannelIndexedLadder`, and reduction `channelIndexed_swaps_windings` (via `rotation_step`).",
    },
  ],
});
