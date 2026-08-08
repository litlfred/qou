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

---

# ATTACK VECTORS — the canonical-derivation walk (2026-08-08)

Walked the chain slowly, asking at each step: does `theta_K` appear here?

## Where it pops out: NOWHERE ON THE CHAIN

    q_0 -> C categorical action -> Yekutieli non-abelian Stokes -> H_n(q) Hecke
       -> Wedderburn (lambda |- n) -> Frobenius tr_M = sum_lambda y_lambda chi_lambda
       -> confinement SDP -> canonical T_w -> Archimedean functor at q_0 -> MeV

`theta_K` appears at **no step of this chain**. What the chain produces, at the
Frobenius/SDP step, is the CATEGORICAL complex observable of
`conj:binding-qbeta-complex-volume`:

    frakV_cat(K) = E_0 * tr_M((Pi_free - 1) o M)  in  C,
    Re frakV_cat = binding,   Im frakV_cat = Q_beta.

`theta_K` lives somewhere else entirely: in `SDeformedVolumeChannel`, as
`Im u(q_0)`, feeding the GEOMETRIC Neumann-Zagier object

    V_41(u) = Vol(4_1) + a_2 * u^2,   a_2 = i*sqrt3/4  (purely imaginary),
    Im V_41(u) = kappa * (Re^2 u - Im^2 u),   kappa = sqrt3/4 = |a_2|.

## What it intervenes between

**`u` is not a step in a chain — it is the CROSS-LINK BETWEEN TWO CHAINS.**

    upstream    q_0, the substrate modulus        (algebraic / Hecke-Wedderburn side,
                                                   the H^1(Bring) datum, CAL-2 pin)
        |
        |  u : R -> C          <-- THE BRIDGE. theta_K = Im of it.
        v
    downstream  frakV_geo(u) = Vol + i*CS         (hyperbolic geometry / NZ side,
                                                   character variety of K)

It is the ONLY place the algebraic substrate and the hyperbolic geometry touch.
That is exactly why it has no definition: `conj:binding-qbeta-complex-volume`
NAMES the bridge (it asserts frakV_cat is "the QOU analogue of" the NZ complex
volume) without CONSTRUCTING it. The channel class then carries the bridge as a
free field. Naming an analogy is not defining a map.

## AV1 (highest value, cheap, possibly decisive) — the glyph collision

**`frakV` denotes TWO DIFFERENT OBJECTS** and the channel does not say which:

  * `frakV_cat` = E_0 tr_M((Pi_free-1) o M)   — categorical, Im = Q_beta
  * `frakV_geo` = V_41(u) = Vol + a_2 u^2     — geometric, Im = CS

`DeltaLambdaT5Assembly` picks the geometric one (`hV : ch.V = V_41`). But
`SDeformedVolumeChannel.S_eq` is stated abstractly as `S = A_omega * (V (u q0)).im`,
and the conjecture it cites defines frakV categorically. The two readings give
DIFFERENT equations:

    geometric   S = A_omega * kappa * (ln^2 q0 - theta^2)     <- theta appears
    categorical S = A_omega * Im frakV_cat = A_omega * Q_beta <- NO THETA AT ALL

If the categorical reading is the intended one, **theta_K is a notation artifact
and the entire nine-reading search was chasing a glyph collision.**

DECISIVE TEST, cheap: is `S_K / Q_beta(K)` the same constant (= A_omega) across
both anchors? Needs the per-knot Q_beta(K) = Im frakV_cat(K), which the
categorical side can compute. This is the single highest-value check on this bean.

## AV2 (STRUCTURAL, and it follows from work already landed) — the anchors sit at u = 0

PR #4513 + #4725 proved both anchors sit at the REGULAR IDEAL CELL (m004 = 2
regular ideal tetrahedra; L6a4 = regular ideal octahedron), i.e. at the COMPLETE
hyperbolic structure. In Neumann-Zagier coordinates the complete structure is
`u = 0` — and `V_41(0) = Vol(4_1)` is real, so `Im V_41(0) = 0`.

    => if `u` were the geometric deformation of the ANCHOR'S OWN structure,
       then u = 0, hence S = A_omega * Im V_41(0) = 0,
       CONTRADICTING the measured S_muon = +0.00968 and S_proton = -0.03946.

So **the channel's `u` is NOT the anchor's own geometric deformation parameter.**
This is a second exclusion, independent of #4513's Murakami-meridian one, and it
comes for free from the angle-structure work. It is one line to Lean-prove
(`imV_41` at 0) and should be.

Between AV2 and #4513's result, the "geometric reading" is now boxed in hard: u
is neither the substrate-matched Murakami meridian NOR the anchor's own NZ
deformation. Enumerate what is left before proposing anything new.

## AV3 — derive BOTH parts of u, not just Im

`Re u = ln q0` is the T5 hypothesis `hRe`, and it is UNDISCHARGED with a phantom
citation (#4513). A candidate that pins only `Im u` and inherits `hRe` on a
docstring's word repeats the exact error #4513 corrected. The bridge owes both
components.

Note the tension AV2 sharpens: the complete structure has `u = 0`, so `Re u = 0`,
but `hRe` demands `Re u = ln q0 != 0`. Any construction must say which structure
its `u` deforms, and that structure is NOT the complete one.

## AV4 — the cusp modulus already ties theta to geometry

`kappa = sqrt3/4 = |a_2|` is the magnitude of the purely-imaginary leading NZ
coefficient, i.e. a GEOMETRIC datum (cusp shape), not fitted. And
`signflip_forces_diagonal_cross` proves the measured sign flip forces `u` to
cross the diagonal `|Re u| = |Im u|`. That is a hard, A_omega-free constraint on
the bridge that any candidate must satisfy: **the two anchors lie on opposite
sides of |Re u| = |Im u|.** Use it as an up-front filter, the way the scale
filter was used.

## GUARD (unchanged)

A `u` obtained by inverting the anchors is a fit, is covered by
`ratio_attained`, and does not close this bean. Per `qou-qmnb`, any candidate
must yield theta ABSOLUTELY, per knot — not as a ratio.
