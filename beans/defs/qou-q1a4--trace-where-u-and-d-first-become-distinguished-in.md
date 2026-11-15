---
# qou-q1a4
title: Trace where u and d first become distinguished in the γγ chain (photons → condensate → nucleons)
status: todo
type: task
priority: high
tags:
    - needs-owner
    - convention-d
created_at: 2026-11-15T18:54:18Z
updated_at: 2026-11-15T18:54:18Z
parent: qou-avtq
---

Owner, 2026-11-15: "dont we see u and d come into play as part of chain from photons -> quarks/gluon condensate -> protons/neutrons?" / "can we track/derive that?"

Context (n–p thread, PR #7966, bean qou-jwl8): every consistent model gives n − p = 0 until a u/d asymmetry is put in by hand: the γγ word (p and n are the same word V³), and pure two-colour Yokonuma–Hecke (colour flip t ↦ −t preserves the trace at the forced x = 0). The −18.5 % comes from mismatched words in the traced product plus the imported rule dd → σ⁻¹.

Goal: walk the chain step by step and record, for each step, whether u and d are distinguished, and by what (derived, census, or imported):
1. γγ vertex σ_g σ_{g+1}⁻¹ and the 6-letter core (qou-ales): no flavour label.
2. The 11-letter Q_β nucleon words: p and n differ only in the 3-letter tail; tail letters are census-derived (qou-99qc). Currently this is the FIRST place u/d differ, and it is not derived.
3. Level-2 Schur–Weyl (convention D = gl₂, Jimbo action, JimboActionKernel.lean): V = C² carries a two-valued label (isospin or spin, not decided). The quantum trace weights the two basis vectors by K = diag(q^{±1}), which breaks u ↔ d by construction. Candidate derived source, to be probed pre-registered.
4. Weak vertex / chirality (weak-vertex thread, PR #7960): tr_D is not ι-invariant (pullback is z_T); d = ι(u) is not forced by colouring.

Status: open. No fitted asymmetry may be used; any labelling choice (which basis vector is u) must be reported both ways.
