---
# qou-sgv5
title: 'chi-matrix-m family does not distinguish proton from neutron: tr_M identical, so Delta(n-p)=0'
status: todo
type: task
priority: normal
---

## The observation

In the `chi-*-at-q0-50dps-matrix-m` family, proton and neutron carry the
**identical** `tr_M(q₀)`, to every stored digit. Same for tritium and
helium-3:

    OLD (convention C, as committed)      NEW (convention D, regenerated)
      proton  : 1.6331535900562524882…     proton  : 1.8843194672549750250…
      neutron : 1.6331535900562524882…     neutron : 1.8843194672549750250…
      tritium : 1.0860240058218428921…     tritium : 2.5115533409057651119…
      helium-3: 1.0860240058218428921…     helium-3: 2.5115533409057651119…

**Not a regression from the convention-D migration** — the old committed
values were equal too. It is a pre-existing property of this path, surfaced
by regenerating it (`qou-lt8x`).

## Why it matters

`Δ = tr_M(n) − tr_M(p)` is not incidental. It is the quantity the
operator-valued split uses to set the energy scale — cf.
`probes/homflypt_operator_valued_probe`, which computes

    E₀ = Q_β / |Δtr_M|

and whose whole premise is that the averaged crossings **break** the
amphicheirality that makes the pure-braid HOMFLYPT give P(p) = P(n). In this
family that break does not happen: Δ = 0 exactly, so any consumer reading
these witnesses for a p–n asymmetry gets nothing, and an E₀ derived from them
would divide by zero.

## The likely mechanism, not yet confirmed

The `matrix-m` route goes through the Rust engine, whose wire format carries
a **sign** per crossing. `canonical_braid_crossings.sign_for_ctype` maps
BOTH averaged interfaces — colour-blind `averaged` and colour-weighted
`averaged_weighted` — to `0`, because a sign cannot carry a magnitude. That
projection is documented (`qou-gdtb`, `qou-8zjd`) and is exactly where the
p–n colour weighting `-h(1/2 - δ/4)` is unrepresentable.

But that alone does not explain it: the proton and neutron braid words differ
in their σ / σ⁻¹ counts (measured: p `{σ:6, avg:2, σ⁻¹:3}`, n `{σ:5, avg:2,
σ⁻¹:4}`), so even a sign-only encoding should distinguish them. Either this
producer's word source (`_word_for_braid_word_3a`) is species-independent for
A = 1, or the distinction is lost further down. **Confirm before acting** —
this is a hypothesis, not a finding.

## To close

1. Print `_word_for_braid_word_3a(Z, N)` for (1,0) vs (0,1) and diff them.
   If identical, the degeneracy is in the word builder, not the engine.
2. If the words differ, trace where equality is introduced — the sign
   marshalling is the first suspect.
3. Decide whether this family is *supposed* to carry the p–n split. If the
   sign wire format genuinely cannot, say so in the witness description
   rather than letting a reader infer that Δ = 0 is physics.
4. Cross-check against a path that does carry it (the bridge / exact-triple
   route, which matches markov_peel to 3.6e-51 per `qou-gdtb`).

Related: `qou-gdtb` (representation decision still open — a `(gen_idx, ctype)`
pair cannot express an operator-valued interface), `qou-pb4c` (downstream
sweep of this family).
