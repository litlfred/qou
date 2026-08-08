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

---

# AV1 RESOLVED — NEGATIVE. And the corpus already had the answer. (2026-08-08)

**AV1's premise was WRONG, and I nearly re-derived an established result.**
Recording it in full because the failure mode is the one this bean exists to
police, and it caught me.

## There is no glyph collision

`conj:binding-qbeta-complex-volume` §"The S channel through Phi_b" states it
outright:

> "the conjecture's decay side takes the concrete form
>  `S(q_0) = Im frakV(u(q_0))`: the Chern-Simons part of the **deformed**
>  complex volume at the substrate deformation u(q_0). The deformed volume
>  itself is a theorem for 4_1 and explicitly computable via Neumann-Zagier"

So the corpus PROSE already commits the S-channel `frakV` to the GEOMETRIC NZ
object. The ambiguity I posited exists only in the Lean class field (`V : C -> C`
is unconstrained, per this bean's headline finding), not in the conjecture. The
"categorical reading gives no theta" alternative is not live.

## What is actually true, and was already in the corpus

`S` is not an abstract leak. It is

    S_leak(q_0) := c_3(q_0) + Vol(4_1)

— the **bar-odd residual of the Q_beta c_3 coefficient** after removing the
bar-even amphichiral `-Vol(4_1)` face. `QOU/QBeta/SLeakZeroCrossing.lean`
already carries the exact table:

    | anchor | c_3          | S_leak = c_3 + Vol(4_1) |
    | muon   | -2.02020024  | +0.00968298             |
    | proton | -2.06934258  | -0.03945936             |

I recomputed both from `S - Vol(4_1)` and got exactly these, then found the file.
That is a corpus-grep miss on my part: the identity was Lean-side the whole time,
and `SLeakZeroCrossing` even carries an explicit notation-collision guard warning
against conflating this `S` with `SRigidity.S = Q_beta/E_0`.

## AV5 (supersedes AV1) — theta_K and c_3 ARE THE SAME OPEN QUESTION

Under `S = c_3 + Vol(4_1)` and `S = A_omega * kappa * (ln^2 q_0 - theta^2)`,

    **theta_K is an affine reparametrisation of c_3.**

"Derive theta_K" and "derive c_3" are one question. And the two arcs have been
running on SEPARATE bean/doc trails without citing each other — which is why
this bean was posed as if theta were a fresh unknown. It is not: the c_3 arc is
substantially further along and carries structure this bean should inherit
before proposing anything new:

  * `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`
    — the CANONICAL framing. AGENTS.md says read it before any c_3 decision.
  * The 6-entry flip-flop history in `docs/coordination/1ppq-qbeta.md`.
  * AGENTS.md's own numbers corroborate the identification: it states c_3
    "swings up to 3.47% at m_p-pin q_0". My computed proton deviation from -2 is
    3.467%. Same quantity.
  * `docs/audits/2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`
    reports **c_3 = -2.069348 vs target -2.069343, 2.65 ppm** at proton-pinned
    q_0. If that holds up it is far closer to a c_3 closure than anything the
    theta arc produced in nine readings.
  * AGENTS.md names the intended permanent fix: the **Q_beta Habiro element**
    (parallel to alpha_EM's `[2]_q(1 - h^2 alpha)`).

## THE ACTIONABLE REORIENTATION

Stop searching for theta. **Read the c_3 arc first**, and specifically:

  1. Check whether the 2.65 ppm Habiro-template c_3 result is live or was
     retracted (the c_3 arc has a documented flip-flop history — do NOT assume).
  2. If live, push it through `theta^2 = ln^2 q_0 - (c_3 + Vol(4_1))/(A_omega*kappa)`
     and see what theta it implies — that would be a DERIVED theta, from the c_3
     side, not an anchor inversion.
  3. Carry this bean's exclusions across as filters on any such theta: it must
     put the anchors on opposite sides of |Re u| = |Im u|
     (`CompleteStructureExclusion.opposite_sides_of_diagonal`), and must not be
     the anchor's own NZ deformation (`u_ne_zero_of_S_ne_zero`) nor the
     substrate-matched Murakami meridian (`ChannelMeridianIdentification`).

## Lesson recorded

This bean's own headline is "theta_K has no definition". That remains true of the
Lean class. But the QUESTION it names was already posed, better, elsewhere. The
corpus-grep checklist (AGENTS.md) is meant to catch exactly this and I ran it
against "theta", not against "S" or "c_3". Grep the OBJECT's aliases, not the
symbol you happen to be holding.

---

# LITERATURE CHECK DONE — NZ 1985 read; AV2's premise is SOURCED (2026-08-08)

The owner uploaded the papers (commit abb217cb / c055a0f5). Read
`uploads/1-s2.0-0040938385900047-main.pdf` = Neumann-Zagier, "Volumes of
hyperbolic three-manifolds", Topology 24 (1985) 307-332. Three results, all from
§1:

## 1. `u = 0 <=> complete structure` — CONFIRMED, and it is an IFF

    "Let u_i = 1/2 log(lambda(m_i)) where m_i is the chosen meridian at the i-th
     cusp. Since lambda(m_i) = 1 for the complete hyperbolic structure on M, we
     may choose the branch of logarithm so (u_1,...,u_h) = 0 for this structure."

    "The hyperbolic structure M_u is complete at the i-th end of M (i.e. this end
     is still a true cusp) IF AND ONLY IF u_i = 0."

So `CompleteStructureExclusion`'s premise is NOT an inference from
`V_41(0) = Vol(4_1)` being real — it is NZ's definition, and the iff is stronger
than the exclusion needs. The exclusion stands, now sourced.

## 2. The half-factor sharpens AV3

`u = 1/2 log lambda(m)`, so the T5 hypothesis `hRe : Re u = ln q_0` is the
condition **|lambda(meridian)| = q_0^2**, NOT `= q_0`. Any candidate bridge owes
that factor of 2. Nothing in the corpus states it; a candidate that pins
`|lambda(m)| = q_0` would be off by a square and would look like a near-miss.

## 3. Two corroborations of surrounding machinery

  * NZ prove the cusp shape `tau_i(u)` is an EVEN function of each `u_i` — the
    source of the corpus's `V_41_even` and `no_cubic_rung`. Those are faithful.
  * `u` is a local coordinate valid only "in a neighborhood of 0 in C^h", and
    deformations are parametrized `2^h : 1`. That is exactly why the Murakami
    substrate-matched meridian at `|u| >= 2*pi` is off the controlled
    neighbourhood, independently confirming `FigureEightDeformedMeridianWinding`.

## NOT checked

NZ Theorem 1A/1B (`Vol(M_u) = Vol(M) - (1/2) sum L_i(u) + eps(u)`, `eps = O(|u|^4)`)
vs the corpus's quadratic `V_41(u) = Vol + a_2 u^2`. These are consistent in
principle — NZ's statement is about the REAL volume, the corpus's `a_2` is purely
imaginary so it contributes to CS — but the exact relation between NZ's potential
and the corpus's complex-volume Taylor coefficient was NOT verified. If a
candidate leans on `a_2`, verify that first. The OCR also mangled the displayed
formulae in Theorem 1A, so the constants there were not readable.
