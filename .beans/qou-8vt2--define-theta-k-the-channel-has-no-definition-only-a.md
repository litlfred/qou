---
# qou-8vt2
title: 'DEFINE ϑ_K: the channel has no definition for it, only a docstring phrase'
status: todo
type: task
priority: critical
created_at: 2026-08-08T00:00:00Z
updated_at: 2026-08-08T00:00:00Z
---

Successor to `qou-5nzf` (settled, PR #4513). That bean asked whether the T5
channel's `u` is the substrate-matched Murakami meridian. The answer is **no**,
and the reason reframes the whole ϑ arc:

> **`SDeformedVolumeChannel.u` is a free class field.** Zero instances exist in
> the corpus; the class's only axiom is `S_eq`. `channelFree`
> (`QOU/QBeta/ChannelMeridianIdentification.lean`, sorry-free) proves the class
> is inhabited for *any* `u`. The words "log meridian holonomy" in its docstring
> are a **phrase, not a definition** — nothing in the corpus constrains `u`.

So `ϑ_K = Im(u(q₀))` names a component of an unconstrained function. Every
reading tested against it was being compared to a quantity that had no
definition to be right or wrong about. That is why nine readings across four
SDP probes all missed, and why the scale filter (ϑ is `O(ln q₀)`, logarithmic)
was the only thing that ever bit: it is a property of the *shape* `ln²q₀ − ϑ²`,
not of any defined `ϑ`.

## THE TASK

State a definition of `ϑ_K` — i.e. pin `u` — from an object that is itself
derived, then check it. Not "find a geometric quantity of about the right
size": that is the search this replaces.

## WHAT IS ALREADY EXCLUDED (do not re-run)

* **`u` = the substrate-matched Murakami meridian.** Excluded three ways, all
  Lean-proved sorry-free in `ChannelMeridianIdentification.lean`:
  its real part is `N·t`, so the T5 hypothesis `hRe : Re u = ln q₀` forces the
  degenerate colour `N = 1` (`color_eq_one_of_re_eq_log`); boost dominance then
  forces `k = 0` hence `ϑ = 0` (`winding_eq_zero_of_boost_dominated`); and
  `ϑ = 0` at both anchors admits no sign flip
  (`no_sign_flip_of_theta_zero`), contradicting the measured `S_μ > 0 > S_p`.
  Scope (a) — the Murakami theorem and the T5 assembly each stand; only their
  conjunction is excluded.

* **Any ratio-shaped candidate.** `AfreeThetaConstraint.ratio_attained` proves
  a witness `A` exists for every `y > 1`, so ratio-shaped candidates are
  unfalsifiable. `exists_angle_assignment` proves more anchors never help:
  `n` anchors give `n` equations in `n+1` unknowns for every `n`.

## THE CONSTRAINT ANY CANDIDATE MUST MEET

`hRe` is **not free either** — it is undischarged, and its only cited
justification (`meridian_holonomy_boost`) does not exist. So a candidate `u`
owes **two** things, not one: the imaginary part `ϑ_K`, *and* an actual
derivation of `Re u(q₀) = ln q₀` — or an honest replacement for the T5 shape if
its real part is something else. Pinning only `Im u` and inheriting `hRe` on the
strength of a docstring repeats the error this bean exists to correct.

## GUARD

A `u` obtained by inverting the anchors is a **fit** and is already covered by
`ratio_attained`. It may be labelled a candidate; it may not be wired as
canonical, and it does not close this bean.
