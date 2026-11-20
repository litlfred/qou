import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:planck-reynolds",
  title: "Planck--Reynolds number and the turbulence transition",
  uses: ["def:information-speed-of-light"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): At the physical anchor $q \\approx 1.110$, the fluid operates in the transitional zone: turbulence supports the structured [discrete vortex spectrum](#prop:discrete-vortex-spectrum) without obliterating it into a continuum." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , matching exactly the four observed [intensity levels](#rem:vortex-intensity-modes) ($j = \\frac{1}{2}, 1, \\frac{3}{2}, 2$)" },
  ],
  // Chapter overview (§0): both are results this block previews to situate
  // the turbulence dial, and both sentences state inline what they need (the
  // four intensity levels are listed on the spot). Forward pointers, not
  // prerequisites.
  foreshadows: [
    "prop:discrete-vortex-spectrum",
    "rem:vortex-intensity-modes",
  ],
  tags: ["reynolds-number", "turbulence", "planck-scale", "fluid-dynamics"],
});
