---
# qou-5zl1
title: 'slz5 S1: general-z Markov bond formula in Lean'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T15:10:00Z
updated_at: 2026-10-10T15:30:00Z
parent: qou-slz5
---

Stepping stone 1 of the qou-slz5 story (B_log on the faithful window).

**Claim.** For a Markov trace tr_z on the Hecke tower, with a, b avoiding sigma_i:
tr_z(a (c sigma_i + d) b) = (c z + d) tr_z(ab).
Proved so far only at z = 0 (QOU.Hecke.TwBasis.tau_bond_letter, PR #7612). Verified exactly in H_6 at general z (scratchpad markov_check). A background worker is proving the general case on PR #7612.

**Why it matters.** Every B_log value at z != 0, including convention D, rests on this formula. Without it the bond-factor product prod(z + d_k) is a verified computation, not a theorem.

Done when: sorry-free Lean, lean-direct exit 0 with -DautoImplicit=false, axioms = propext/Classical.choice/Quot.sound.

## 2026-10-10 — proved on the abstract carrier (PR #7612, ee91fe75ebb)

`QOU.Hecke.MarkovBondLetter.tr_bond_letter`: for a Markov trace on any braided tower (generic CommRing R), with a, b in the subalgebra avoiding g_i (both sides of i allowed),
tr(a (c g_i + d) b) = (c z + d) tr(ab). Sorry-free; lean-direct exit 0 with -DautoImplicit=false -s 65536; axioms propext/Classical.choice/Quot.sound. Proof: far-commutation puts avoiding(i) inside below(i)·above(i), then the disjoint-block law twice plus cyclicity.

**Still open:** the bridge to the concrete H_n(q) (TwBasis IwahoriHecke) Ocneanu trace. The production trace (SchurWeyl ocneanuMarkovTrace) is not yet packaged as an OcneanuTrace.MarkovTrace on a braided tower (the gap bean qou-0fmb names). Once bridged, the theorem applies directly and z = 0 recovers tau_bond_letter.
