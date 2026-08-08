---
# qou-5nzf
title: 'FORK: is the T5 channel''s u the substrate-matched Murakami meridian, or not?'
status: completed
type: task
priority: critical
created_at: 2026-08-07T22:22:06Z
updated_at: 2026-08-07T22:22:06Z
---

The derivational probe (`qbeta_qnnq_theta_is_im_u_probe.py`, PR #4513) closed
the "what IS theta_K" question and opened a sharp two-branch fork.

WHAT IS SETTLED. theta_K is not a search target. `DeltaLambdaT5Assembly.lean`
(`s_channel_at_substrate`) gives S = A_omega*kappa*(Re^2 u - Im^2 u) with
Re u = ln q0 proved (`meridian_holonomy_boost`), so

    theta_K = Im(u(q0))

and `SDeformedVolumeChannel.u : R -> C` is documented as "the substrate ->
deformation map u(q0) (LOG MERIDIAN HOLONOMY)". The ln^2 q0 - theta^2 shape is
just Re^2 u - Im^2 u.

THE COLLISION. `FigureEightDeformedMeridianWinding.lean` proves SORRY-FREE that
the substrate-matched Murakami meridian is u = N*t - 2*pi*i*k, so Im u = -2*pi*k.
Conjoined with the above, theta_K is QUANTIZED in units of 2*pi. Tested:

  - k_mu = 0 rows STRADDLE ln q0 — the first readings in the whole arc to pass
    the necessary condition that all nine measured readings failed — then miss
    the A-free ratio by >= 890x.
  - common k = 0 forces theta = 0 at BOTH anchors, so S has the same sign at
    both, contradicting the MEASURED sign flip S_mu > 0 > S_p.

THE FORK — exactly one of these is true, and both are cheap to settle:

(a) THE TWO u ARE DIFFERENT OBJECTS. The T5 channel's `u` is a class FIELD —
    any function R -> C — while the Murakami quantization arises from the
    specific matching q_eval = exp((u + 2*pi*i)/N) to a real substrate. If the
    channel does not impose that matching, its u is unconstrained and the
    quantization simply does not apply. In that case the T5 docstring's "log
    meridian holonomy" wording is MISLEADING and theta_K needs a stated
    alternative definition — which is then the real open question, and a much
    better-posed one than "find a geometric quantity of the right size".

(b) THE T4-INVERTED THETA VALUES ARE INCOMPATIBLE with the proved meridian
    quantization. They are A_omega-conditioned anyway; this would be a second,
    independent reason to distrust them.

HOW TO SETTLE IT: read whether any instance of `SDeformedVolumeChannel` imposes
the Murakami matching condition on `u`, or whether `u` is left free. That is a
Lean-reading task, not a compute task, and it decides which branch holds.

WHY THIS MATTERS MORE THAN ANOTHER READING: branch (a) reframes the whole gap —
it says the arc has been searching for a quantity whose DEFINITION is not yet
pinned, which is why no reading fit. Branch (b) invalidates the targets every
probe has been compared against. Either way the next step is definitional, not
exploratory.

Guard recorded in the probe: the (k_mu,k_p) = (1,2) row's |ratio| = 0.24995 sits
1.9% from |r| = 0.24539 and looks like a hit. It is not — the ratio tends to
k_mu^2/k_p^2 = 1/4 identically as L -> 0, |r| merely lies near 1/4, and the sign
is wrong (r < 0 requires straddling).

---

## SETTLED 2026-08-08 (PR #4513) — branch (a), by Lean reading

The fork is closed in favour of **(a): the two `u` are different objects.**
Three findings, all proved sorry-free in
`QOU/QBeta/ChannelMeridianIdentification.lean`:

1. **The channel constrains `u` not at all.** `SDeformedVolumeChannel` has
   ZERO instances in the corpus — every occurrence is a hypothesis binder —
   and its only axiom is `S_eq`. `channelFree` proves the class is inhabited
   for ANY `u`, `V`, `A_ω`, so no theorem stated over a general channel can
   impose the Murakami matching. "Log meridian holonomy" is a docstring
   phrase attached to a free field, not a definition.

2. **The `hRe` citation is a PHANTOM.** `DeltaLambdaT5Assembly` attributed
   `Re(u(q₀)) = ln q₀` to `meridian_holonomy_boost`. No such declaration
   exists anywhere in the corpus (repo-wide grep: 3 hits, all citations —
   the T5 docstring, this bean, and the probe docstring; zero declarations).
   `hRe` is an undischarged hypothesis. Corrected at all three sites.

3. **The identification costs the degenerate colour.** The substrate-matched
   meridian's real part is `N·t`, NOT `t`, so `hRe` forces `N = 1` — the
   colouring at which the coloured Jones is identically 1 and the deformed
   volume conjecture (an `N → ∞` statement) is empty
   (`color_eq_one_of_re_eq_log`). Both the probe and this bean had combined
   `Re u = ln q₀` with `u = N·t − 2πi·k` without noticing they agree only at
   `N = 1`.

The measured-sign refutation stands and is now Lean-proved:
`winding_eq_zero_of_boost_dominated` (boost dominance forces `k = 0`, since
`2π` is 60× `ln q₀`) + `no_sign_flip_of_theta_zero` (`ϑ = 0` at both anchors
puts `S` at the same sign at both, contradicting `S_μ > 0 > S_p`).

**Scope (a)**, per AGENTS.md §"Before declaring refuted": the Murakami
theorem and the T5 assembly each stand; only their CONJUNCTION is excluded.

**What this leaves open** — and it is better posed than what it replaces:
`ϑ_K` has no stated definition. The arc spent nine measured readings hunting
a quantity whose definition was never pinned, which is why no reading fit.
Successor bean filed for the definitional question.

**ID note:** filed originally as `qou-5nze`, which collided with an existing
bean on `main` (`Prove Specht.specht_isSimple`); renamed to `qou-5nzf`.
