import { definition } from "../../schema/builders";

export default definition({
  label: "def:gravitational-constant",
  title: "Gravitational constant from information geometry",
  tags: [
    "gravitational-constant",
    "information-theory",
    "jacobson",
    "entropy-area",
    "speed-of-light",
    "emergent-gravity",
  ],
  lean: { ref: "qou:QOU.Information.gravitationalConstant",
    validation: "not_checked",
  },
  uses: [
    "def:information-speed-of-light",
    "rem:gr-substrate-geometry",
    "rem:c-substrate-via-levi",
  ],
  cites: [
    "jacobson1995",
    "bekenstein1981",
    "mcmullen1998",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation twin-audit (`qou-x60n`): `2026-09-05-archimedean-twins-are-instantiations-probe.lean` proves compound `cellEntropyArch` equals `(q - 1)^2 / q^3` away from `q ∈ {0, 1/2}` (both unreachable under `1 ≤ q`).",
      see: "docs/audits/2026-09-05-archimedean-twins-are-instantiations-probe.lean",
    },
  ],
});
