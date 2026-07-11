---
# ccas
title: 'Analyze: Kibler q-deformed periodic table (SU_q(2), SO_q(4,2)) — screening as q-deformation'
status: completed
type: task
priority: normal
created_at: 2026-07-06T04:46:39Z
updated_at: 2026-07-06T04:48:09Z
parent: 4lss
---

Kibler et al.: q captures electron-electron screening; SO_q(4,2)/SU_q(2) reproduce ATOMIC magic numbers. KEY DISTINCTION (critical-distance license): our q₀ is a FIXED derived substrate constant, NOT a per-atom tunable screening knob. Do NOT blur derived-q₀ into their fitted-q. Compare to appendix-transfer-matrices/tm-heavy-atom-examples + magic-numbers-from-q. Deliverable: literature-comparison remark clarifying fixed-q₀ (derivation) vs Kibler tunable-q (phenomenological screening fit).

## Resolution (2026-07-11)

Source located (owner ask "arxiv link kibler?"): the q-deformed atomic periodic-table
work is Négadi & Kibler, "A q-deformed Aufbau Prinzip", J. Phys. A 25 (1992) L157 =
arXiv:quant-ph/0409177 (SO(4) ⊃ SO(3)_q chain, reproduces the Madelung (n+ℓ,n) filling
for atoms and monoatomic ions). Added CSL ref `negadi1992` to references.ts and a new
§"q-deformed atomic Aufbau" subsection to q-deformed-nuclear-models-comparison.md with
the critical-distance framing the bean demanded: q is a per-scheme deformation parameter
imposed to organize the ordering, NOT derived — vs QOU q_0 as one fixed substrate
constant shared by every atom and nucleus; atomic magic numbers read from the same
many-body Hecke trace at q_0 (prop:magic-numbers-from-q), not a separately deformed
atomic symmetry. Characterized conservatively (abstract-level source only): did not
assert per-atom fitting, only that the deformation is imposed rather than substrate-derived.
