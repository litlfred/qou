---
# qou-yfro
title: 'AUTHOR CALL: relabel the two crossing-energy channels (which, if either, is electromagnetic)'
status: todo
type: task
created_at: 2026-08-08T13:48:08Z
updated_at: 2026-08-08T13:48:08Z
---

Blocked on an author decision. Raised by the downstream propagation of the
`def:coulomb-charge` decomposition correction (PR #4760 / branch
`claude/coulomb-decomposition-downstream-2026-08-08`).

**The situation.** The corrected split is

    E_cross = n+ q - n- q^-1 = (1/2)(n+ - n-)(q + q^-1) + (1/2)(n+ + n-)(q - q^-1)
                                 ^ bar-even = Q             ^ bar-odd = half total crossings

The upstream fix withdrew the identification of the bar-odd term as *the
electromagnetic correction*, because the decomposition supplies no route from
`Q` to that term: the bar-odd coefficient is a crossing count (sign-blind,
non-negative, so it cannot flip with chirality), while `Q` sits on the bar-even
side. Upstream explicitly left relabelling as an author call.

**What is waiting on the decision.** These carry the old labels; each was
scoped channel-neutrally or flagged open rather than relabelled:

- `observations/crossing-energy-interpretation.md` — the "Physical force"
  column was removed and the identification flagged open.
- `observations/pair-creation-energy.md:85-99` — "net Coulomb repulsion".
- `observations/hydrogen-knot-structure.md:62` — "acts as the EM-to-strong ratio".
- `climax-volume-mass/skein-crossing-asymmetry-prop` — title is "Crossing
  asymmetry and per-crossing Coulomb correction"; body has `delta_Coulomb`.
- Lean: `QOU.Braiding.emStrongRatio` + `em_strong_ratio_tanh`
  (`observations/crossing-energy-decomposition.lean:115,122`). The *identity*
  is correct; only the name asserts the identification.

**Three coherent options.** (1) Keep bar-odd = EM and supply the missing route
from `Q`. (2) Move the EM label to the bar-even channel, which is the one `Q`
actually scales — but then check every "EM/strong ratio" reading, since the
ratio inverts. (3) Drop force names from the decomposition entirely and let
`prop:em-coupling-projection` (which uses the Hecke *eigenvalue* `-q^-1`, a
genuinely distinct object) carry the EM content alone.

Full analysis: `docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md`.
