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
`library/1-s20-0040938385900047-main/1-s2.0-0040938385900047-main.pdf` = Neumann-Zagier, "Volumes of
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
    source of the corpus's `no_cubic_rung` and `no_odd_rung`
    (`QOU/Knot/NeumannZagierParity.lean`). Those are faithful. (An earlier draft
    of this line cited `V_41_even`; no such declaration exists anywhere in the
    corpus — see the verification section at the end of this bean.)
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

---

# THE c₃ ARC CHECKED — 2.65 ppm is NOT live, and the arc hands ϑ a hard filter (2026-08-08)

Ran the reorientation this bean recommended. Both halves answered.

## 1. The 2.65 ppm Habiro result is FALSIFIED, not live

The bean said "check whether it is live or was retracted; the c_3 arc has a
flip-flop history — do NOT assume." Correct caution: it was falsified **the next
day**. `docs/coordination/ck-dk-canonical-registry.md` §c_3 records:

  c_3 | EMPIRICAL — near-match, **REFUTED as real-q fibre element**
      | 2.65 ppm (`[3]_q/25` at proton **ONLY**)
      | cross-anchor: **NO** — swings −2.88% to muon; `dc_3/dq ≈ 4.6e6`
      | falsification: `2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`

The 06-03 audit that reported 2.65 ppm itself says the `[3]_q/25` factor is
"empirically discovered, not predicted". It is a single-anchor fit. Registry also
notes a B1 re-run with the canonical GGM V₃ = −7.693 gives **0 assembly hits in
180 candidates** — the old near-misses were artifacts of a wrong V₃.

**So there is no closer-to-closure c_3 result to inherit.** The real-q family is
dead on both sides.

## 2. But the c_3 arc's OBSTRUCTION transfers to ϑ, and it is a strong filter

`dc_3/dq ≈ 4.6e6` was the thing that killed the real-q c_3 family ("impossible
for smooth real f"). Via `S_leak = c_3 + Vol(4_1)` and
`S = A_ω·κ·(ln²q_0 − ϑ²)`, it lands directly on ϑ:

    anchors apart          1.28e-8   (11.54 ppb — the muon/proton PINS)
    dS/dq = dc_3/dq        3.84e6    (recomputed; registry quotes ~4.6e6)
    dϑ/dq                  −2.5e7 (muon)   −7.3e6 (proton)
    smooth geometric qty   d(ln q_0)/dq = 0.90  — O(1)

Seven orders of magnitude. **Lean-proved sorry-free** in
`QOU/QBeta/ThetaLipschitzObstruction.lean`, as a Lipschitz bound needing no
differentiability:

    |S₁ − S₂| ≤ A·κ·( |L₁ − L₂| + K·|Δq|·(|ϑ₁| + |ϑ₂|) )

with the numeric bite bracketed: every `K ≤ 1e7` is EXCLUDED, `K = 1.1e7` clears.
So the forced Lipschitz constant is in `[1e7, 1.1e7]`.

## 3. THIS IS A NEW UP-FRONT FILTER — use it like the scale filter

The scale filter (ϑ is `O(ln q_0) ≈ 0.1`) prunes by MAGNITUDE and excluded 8 of 9
readings before measuring. This one prunes by DERIVATIVE and is **orthogonal**:
it kills candidates the scale filter passes. Any ϑ of the right size that also
varies smoothly in q_0 is dead, whatever its value.

Apply it first, alongside the two exclusions already on main:
  * `opposite_sides_of_diagonal` — anchors on opposite sides of |Re u| = |Im u|
  * `u_ne_zero_of_S_ne_zero` — u is not the anchor's own NZ deformation
  * `ChannelMeridianIdentification` — u is not the substrate-matched Murakami meridian
  * **NEW: `ThetaLipschitzObstruction`** — ϑ is not Lipschitz-in-q_0 below ~1e7

## 4. Where that leaves the bean

The live reading is AGENTS.md's fibre-vs-observable distinction: c_3 (hence ϑ) is
**not a real function of q_0 at all**. Each anchor is a different archimedean
evaluation of one fibre-level object. So:

  ✗ do NOT look for a real formula ϑ(q_0) — the Lipschitz result now makes that
    a proved exclusion for the ϑ side too, not just a c_3 heuristic
  ✓ DO look for a fibre-level element whose evaluation at each anchor gives that
    anchor's ϑ

That is the same conclusion the c_3 arc reached, now inherited rather than
rediscovered — which was the point of noticing the two arcs are one question.

## Correction recorded

A first draft of the Lean asserted `K = 1e7` would clear the bound. It does not —
the threshold is `1.07e7`. The guess was wrong by that factor and `norm_num`
caught it; the file now brackets the threshold rather than asserting one side.

---

# FILTER VERIFICATION — all four exclusions confirmed Lean-backed (2026-08-10)

This bean's pruning strategy is its most reusable output: a later agent is meant
to inherit four exclusions as settled and not re-run them. That only works if
they are real, so they were checked against `origin/main` @ 69fb34e4 rather than
taken from this bean's own prose.

## The four filter files — all clean

| file | lines | real sorries | axioms |
|---|---|---|---|
| `QBeta/ThetaLipschitzObstruction.lean` | 195 | **0** | 0 |
| `QBeta/CompleteStructureExclusion.lean` | 166 | **0** | 0 |
| `QBeta/ChannelMeridianIdentification.lean` | 195 | **0** | 0 |
| `QBeta/SLeakZeroCrossing.lean` | 147 | **0** | 0 |

("real sorries" = `\bsorry\b` occurrences minus the phrase *"sorry-free"*, which
otherwise inflates the count — the trap that made `SeminormalBaseExists` look
sorry-bearing under `qou-2ryn`.)

## Declaration-level check — 10 of 11 cited names resolve

Every filter lemma this bean tells a successor to apply exists:

    ✓ opposite_sides_of_diagonal          CompleteStructureExclusion:145
    ✓ u_ne_zero_of_S_ne_zero              CompleteStructureExclusion:117
    ✓ color_eq_one_of_re_eq_log           ChannelMeridianIdentification:109
    ✓ winding_eq_zero_of_boost_dominated  ChannelMeridianIdentification:136
    ✓ no_sign_flip_of_theta_zero          ChannelMeridianIdentification:173
    ✓ channelFree                         ChannelMeridianIdentification:86
    ✓ ratio_attained                      AfreeThetaConstraint:107
    ✓ exists_angle_assignment             AfreeThetaConstraint:156
    ✓ signflip_forces_diagonal_cross      Knot/FigureEightComplexVolume:204
    ✓ no_cubic_rung                       Knot/NeumannZagierParity:86
    ✗ V_41_even                           DOES NOT EXIST

## The one defect: this bean carried its own phantom citation

`V_41_even` appears nowhere in the corpus — the sole occurrence was this bean's
own line 300. The *substance* is fine and lives under different names:
`no_cubic_rung` (coeff 3 = 0) and `no_odd_rung` (every odd coefficient vanishes),
both sorry-free over a generic `[CommRing R] [NoZeroDivisors R] [NeZero (2:R)]`
— correct §7c hygiene, no gratuitous `ℝ`. The citation is now corrected in place.

Worth naming plainly: this is the same defect class the bean itself polices two
sections earlier, where it faults `hRe` for resting on `meridian_holonomy_boost`,
"which does not exist". A bean that catches a phantom citation can carry one.

## `meridian_holonomy_boost` — the bean's claim is right, and already recorded

Confirmed absent, and the corpus does not merely lack it, it *documents* the
absence in two docstrings:

  * `ChannelMeridianIdentification.lean:40` — "...to a lemma
    `meridian_holonomy_boost`, which does not [exist]"
  * `DeltaLambdaT5Assembly.lean:27` — "an earlier version of this docstring
    attributed it to a lemma `meridian_holonomy_boost`; no such [lemma]"

So AV3's premise (`hRe` is undischarged with a phantom citation) is sound and
independently corroborated on main.

## The Lipschitz result is exemplary, and its self-correction is in the file

`ThetaLipschitzObstruction.lean` brackets the threshold rather than asserting one
side of it — `bound_excludes_K_1e7` and `bound_clears_K_1p1e7` are both proved,
pinning the forced constant to `[1e7, 1.1e7]`. The file records its own wrong
guess in a docstring: *"a draft asserted `K = 1e7` would clear. It does not — the
threshold is ≈ 1.07e7, and the guess was wrong."* It also carries the explicit
**scope (a)** label per AGENTS.md's refutation-scoping rule, so it excludes
"Lipschitz-with-moderate-constant ϑ", not "any ϑ".

## What this changes about the bean's state

Nothing about the open question. ϑ_K still has no definition; the fibre-level
route recommended in §"THE ACTIONABLE REORIENTATION" is still the live one, and
this pass produced **no** progress toward it. What changed is only that the four
filters can now be inherited on evidence instead of on assertion — which is what
saves the next agent the nine-reading search this bean was opened to stop.

Status stays `todo`.

---

# THE FIBRE-LEVEL ROUTE — what theory exists to derive from (2026-08-10)

Answering the owner's question directly: *what theory do we have to derive a
fibre-level element with?* Surveyed the corpus rather than reasoning from
memory. The answer is that **almost the whole apparatus exists and is proved;
exactly one object is missing, and it is a better-placed object than ϑ_K.**

## What exists, verified

**The fibre home.** `def:habiro-ring`, `def:z-habiro-ring`,
`def:qz-bicompletion` — the cyclotomic completion `ℤ[q,q⁻¹]^` where an element
can have different archimedean evaluations at each anchor. This is the formal
home AGENTS.md's fibre-vs-observable table demands.

**The engine.** `prop:q-beta-c-k-recursion-from-habiro-q-difference` states the
implication we need: if `F(qξ) = R(q,ξ)·F(ξ)` has depth `d`, then

    c_{k+1} = Σ_{j=1..d} a_j(q₀)·c_{k+1-j},   a_j ∈ ℚ(q₀) extracted from R.

**The engine's lower half is PROVED, sorry-free, over a generic ring.**
`QOU/BraidKnot/QBetaPreArchHeatDepthOneKernel.lean` (0 real sorries, 0 axioms,
`{R : Type*} [CommRing R]` — correct §7c, no gratuitous `ℝ`):

    jackson_fixed_shift_kernel          the fixed q-shift kernel
    heat_mode_depth_one_kernel          each heat mode is depth-1 Jackson
    two_mode_depth_two_composition      two depth-1s compose to depth-2
    heat_two_mode_composition           …for the heat modes specifically

So "the q-difference equation derives from the depth-1 Jackson equations of each
mode" is not a hope — the mode-level and two-mode composition steps are theorems.
Kernel-side constraints additionally live in
`QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean`.

**Free filters on any candidate kernel**, all already in the corpus:
  * bar-parity law — `a_j = e_j({r_λ})`, `r_λ = (q−1)μ_λ` bar-odd, so `a_j`
    alternates bar-parity;
  * cyclotomic self-reciprocality `Φ_n(1/q)·q^{φ(n)} = Φ_n(q)` ⇒ period-3 closure;
  * `prop:q-beta-q-eq-one-shadow-gate` + the machine-checked rule that
    `parity: exactly-odd` with a nonzero q=1 shadow is impossible
    (`fixed_eval_two_mul_kills_bar_odd`);
  * the proved seed `c₂ = −1` (Taylor-exact);
  * the worked precedent AGENTS.md points at: `prop:alpha-em-habiro-bar-involution`,
    i.e. `[2]_q(1 − h²α)`.

## The one missing object — and why its placement matters

The author's own status note on the recursion prop is explicit:

> "the compute scaffold demonstrates two toy kernels (depth-1 geometric, depth-2
> **underdetermined-from-seeds-alone**). The categorical `F(q)` construction
> remains the **open keystone** for the 1 ppQ target."

So `c₂ = −1` does not close even a depth-2 recursion; the `a_j` are needed, hence
the per-mode rates `μ_λ(q)` and the mode set `Λ` (which fixes `d = |Λ|`).

**Why this is a materially better position than the geometric route.** This bean
already established that `ϑ_K` "appears at **no step** of the canonical chain" —
it is a cross-link *between* two chains, which is precisely why it has no
definition and why nine readings had nothing to be right or wrong about.

`μ_λ` is not like that. It is a **Hecke/Wedderburn spectral quantity — squarely
ON the chain**, at the step that already produces `y_λ`, `χ_λ`, `d_λ`:

    … → H_n(q) Hecke → Wedderburn (λ ⊢ n) → Frobenius tr_M = Σ_λ y_λ χ_λ → …

So the fibre route converts *"undefined off-chain bridge"* into *"not-yet-extracted
on-chain spectrum"*. That is the whole gain, and it is why this route deserves the
next session rather than another ϑ search.

## Concrete next step (formalize-first order)

1. **Derive `μ_λ(q)`** as the q-heat-kernel rates over the Wedderburn blocks,
   from the Hecke module structure — not from the anchors.
2. `a_j = e_j({(q−1)μ_λ})` is then **forced**, and `d = |Λ|`.
3. **Filter before any numerics**, using the already-proved constraints above:
   the derived `a_j` must alternate bar-parity, must respect the q=1 shadow gate,
   and must satisfy period-3 closure. Any of these kills a wrong `μ_λ` for free —
   the formalize-first pruning AGENTS.md §3.3 asks for.
4. Only then evaluate at both anchors and compare to `c₃`, carrying this bean's
   ϑ-side filters across via `ϑ² = ln²q₀ − (c₃ + Vol(4₁))/(A_ω·κ)`.

**Guard, unchanged and it applies here too:** a `μ_λ` fitted to reproduce the
measured `c₃` is a fit, is covered by `ratio_attained`, and closes nothing. The
Lipschitz obstruction already forbids a smooth real `ϑ(q₀)`, so a `μ_λ` that is a
smooth real function of `q₀` inherits that exclusion — check it early.

## Defect found while surveying

`prop:q-beta-c-k-recursion-from-habiro-q-difference` carries
`lean: { ref: "qou:QOU.QBeta.CKRecursion.CKRecursion", validation: "not_checked" }`.
**No such declaration exists.** The only occurrence of that name is a *comment*
in `QBetaPerBlockChiClosedForms.lean:1108` describing it as a "Sibling on main
(2026-06-03)". The real, verifiable Lean is the two files named above. So the
note's "working recursion engine" is not checkable at the cited ref — the
manifest's own `not_checked` is the honest flag, and the ref should be repointed
to what exists. Not fixed here: repointing a `lean.ref` is a content change and
this is a beans-only pass.

Status stays `todo`. No derivation attempted; this records the route and its
one keystone.

---

# μ_λ FIRST FILTER — the parity law forces a half-integer power, and prunes the
# obvious candidate (2026-08-10)

Formalize-first pass on the keystone identified above, per AGENTS.md §3.3: find
the invariant that prunes the class **before** running any search. One was
available for free, from the recursion prop's own asserted law. No anchor input,
no numerics.

## The derivation

`prop:q-beta-c-k-recursion-from-habiro-q-difference` asserts two things:

  (i)  the rates `r_λ = (q−1)·μ_λ` are **bar-odd**;
  (ii) `a_j = e_j({r_λ})` **alternates bar-parity**.

Note first that `(q−1)` is *not itself* bar-odd: under `q ↦ 1/q` it goes to
`−(q−1)/q`, i.e. it is bar-anti-homogeneous of weight −1. So (i) is a constraint
on `μ_λ`, and solving it gives

    **μ_λ(1/q) = q · μ_λ(q)**

For a pure power `μ = q^a` this forces `−a = 1 + a`, i.e. **a = −1/2**. The
general solution is

    **μ_λ(q) = q^{−1/2} · g_λ(q),  with g_λ bar-even.**

Verified symbolically (sympy) on `g ∈ {1, q+q⁻¹, [3]_q}` — all bar-even, all
satisfy the μ-law and make `r_λ` exactly bar-odd — and falsified on `g = q`,
which is not bar-even.

## Claim (ii) is what forces the strict reading

There is a weaker reading in which `μ_λ` is merely bar-even and `r_λ` is
"bar-odd up to weight". The two readings are distinguished by (ii), and the test
is decisive:

| reading | `a_j` behaviour under bar | matches claim (ii)? |
|---|---|---|
| **strict**: `μ = q^{−1/2}·(bar-even)` | `a_j(1/q) = (−1)^j a_j(q)` — clean | **yes**, j = 1,2,3 |
| weak: `μ` bar-even | `a_j(1/q) = (−1)^j q^{−j} a_j(q)` | no — carries `q^{−j}` |

So the block's own clean-alternation claim **commits it to the strict reading**,
hence to the half-integer power.

## Consequence, and a fork the corpus should resolve

Strictly read, the per-mode rates live in `ℤ[q^{±1/2}]`, **not** `ℤ[q^{±1}]`.
That is in real tension with AGENTS.md §7a, which fixes the Hecke convention as
eigenvalues `(q, −q⁻¹)` — integer powers — and names Kauffman's
`(q^{1/2}, −q^{−1/2})` as the *wrong* convention for this corpus.

Two honest resolutions, and they give **different** filters, so this is a fork
rather than a detail:

  (a) the rates genuinely carry `q^{−1/2}` — the framing/Kauffman normalisation
      enters at the heat-kernel level even though the Hecke generators do not
      need it. Then every candidate `μ_λ` must be built in `ℤ[q^{±1/2}]`.
  (b) "bar-odd" in (i) is loose and the clean alternation in (ii) is the
      misstatement. Then `μ_λ` is bar-even and the alternation carries `q^{−j}`.

As written the block asserts both (i) and (ii), and only (a) makes both true.
Not silently picking one: this is flagged for the owner. Per
§"Conditional-proved ≠ premise-established", everything below is **conditional on
(a)**, which the corpus asserts and has *not* proved.

## The prune — and it hits the obvious candidate

The natural first guess for an on-chain `μ_λ` is the `C₂` / Jucys–Murphy block
scalar: `C₂ = Σ_k X_k²` acts on block λ as `contentSqSum λ · 1`. It is exactly
the object PR #4876's residual item 4 names, and it is squarely on the chain.

It is **excluded**, conditional on (a): `contentSqSum` is
`(μ : YoungDiagram) : ℤ` (`QOU/BraidKnot/JucysMurphy.lean:175`) — a plain
integer, entirely `q`-independent. A constant is bar-even, which is the *weak*
reading, so it cannot make `r_λ` bar-odd and breaks (ii).

**Scope: (a)-conditional, not structural.** The invariant used is the corpus's
asserted parity law, not a Lean theorem. If the owner resolves the fork toward
(b), this prune dissolves and `contentSqSum` returns as a live candidate. Stated
that way deliberately — this bean exists because nine readings were tested
against an undefined target, and a prune resting on an unproved premise must
wear that premise.

## What a surviving candidate looks like

`μ_λ(q) = q^{−1/2} · g_λ(q)` with `g_λ` bar-even. Bar-even objects already on the
chain: `[n]_q` (verified bar-even), the Wenzl/Hoefsmit q-dimensions `d_λ(q)`, and
sums of squares of `[content]_q` (bar-even, being a sum of squares of bar-even
terms). So the shape to try first is the **q-deformed** content-square sum,

    μ_λ(q) = q^{−1/2} · Σ_{c ∈ λ} [cellContent c]_q²,

which is the minimal q-deformation of the excluded candidate that satisfies the
forced law. That is a *prediction of shape*, not a fit — no anchor was used to
obtain it.

## Guard, restated

If this shape is then tuned to reproduce the measured `c₃`, it becomes a fit and
closes nothing. The next step is to **derive** `μ_λ` from the q-heat-kernel
construction and check whether it lands in this class — not to select within the
class by matching.

Status stays `todo`.

---

# OWNER RULING + the q-content convention is now FORCED (2026-08-10)

## 🟧 Owner ruling: the heat-kernel rates MAY live in ℤ[q^{±1/2}]

Asked and answered. The fork left open by the previous section resolves to **(a)**:
half-integer powers of `q` are permitted for the per-mode rates, notwithstanding
AGENTS.md §7a fixing the Hecke *generator* eigenvalues at `(q, −q⁻¹)`. §7a governs
the generators; it does not forbid `q^{1/2}` in the heat-kernel layer.

Consequences, no longer conditional on the fork:

  * `μ_λ(1/q) = q·μ_λ(q)`, i.e. **μ_λ = q^{−1/2}·g_λ(q) with g_λ bar-even** — stands.
  * The `contentSqSum` prune stands: `contentSqSum : YoungDiagram → ℤ` is
    q-independent, hence bar-even, hence the weak reading; it cannot make `r_λ`
    bar-odd.

## Which q-content convention can supply `g_λ`? — measured

The corpus already has a q-deformation of cell content, and it is **`q^{cellContent}`**:

    QOU/MathlibExt/WenzlSchurElement.lean:78     a * (1 - X * Q ^ (cellContent i j))
    QOU/BraidKnot/QSchurWeightsGeneral.lean:54   weight λ = weight μ * q ^ cellContent i j / …
    QOU/HeckeAlgebra/JonesMarkovWenzl.lean:220   q ^ ((n : ℝ) * (cellContent λ i j : ℝ))

(The corpus's `jucysMurphy` at `JucysMurphy.lean:123` is over
`MonoidAlgebra k (Equiv.Perm (Fin n))` — the **classical S_n** element. That is
*why* `contentSqSum` is q-independent, and it is consistent with the prune.)

Tested both candidate conventions for bar-evenness, symbolically, over
λ ∈ {(1),(2),(1,1),(2,1),(3),(1³),(2,2),(3,1),(2,1,1)}:

| convention | bar-even? |
|---|---|
| `Σ_{c∈λ} q^c` — the corpus's | **only when λ is self-conjugate** |
| `Σ_{c∈λ} [c]_q²` — bracket form | **bar-even for every λ** |

The reason is structural, not numerical: the content multisets of `λ` and `λ'`
are negatives of one another, so `Σ q^c` is bar-invariant exactly on the
transpose-fixed partitions. `[c]_q = (q^c − q^{−c})/(q − q⁻¹)` is bar-even for
every `c`, so any sum of its even powers is bar-even unconditionally.

## The self-conjugate branch is REFUTED — scope (b), structural

That left a genuinely interesting possibility: keep the corpus's `q^c`
convention and let the parity law **select** the mode set, restricting `Λ` to
self-conjugate λ. It even resonates with AGENTS.md §7b (Type B folding; "stable
matter = fixed points of the folded crystal").

It is false, and cheaply:

| n | partitions | self-conjugate |
|---|---|---|
| 1 | 1 | 1 |
| **2** | **2** | **0** |
| 3 | 3 | 1 |
| 4 | 5 | 1 |
| 8 | 22 | 2 |

**`n = 2` admits no self-conjugate partition at all** — `(2)` and `(1,1)` are
each other's transpose. A mode set restricted to self-conjugate λ is therefore
*empty* at n = 2, making `Z_q ≡ 0` and the depth `|Λ| = 0`: no recursion, no
`c_k`, nothing. This is a **scope (b) structural exclusion** — an orbit-count
bound, which AGENTS.md accepts as justifying (b) — not merely a bad fit.

## Conclusion: the bracket form is forced

Given (i)+(ii), the owner's ℤ[q^{±1/2}] ruling, and non-emptiness of `Λ` at
n = 2, the per-mode rates **cannot** use the corpus's `q^{cellContent}`
convention. They must be built from **bar-even q-brackets**. The minimal
candidate in the forced class is

    **μ_λ(q) = q^{−1/2} · Σ_{c ∈ λ} [cellContent c]_q²**

— the bracket-form q-deformation of the (excluded) classical `contentSqSum`.

Reached with **no anchor input and no numerics against `c₃`**: purely from the
asserted parity law, the owner's ruling, and a partition count. That is the
formalize-first narrowing §3.3 asks for.

**Residual scope.** This narrows the *form*; it does not derive `μ_λ`. Two things
are still open and must not be conflated with the above:
  1. the actual q-heat-kernel generator whose block eigenvalue `μ_λ` *is* — the
     candidate above is shape-forced, not constructed;
  2. whether `[c]_q` or some other bar-even bracket (e.g. `[c]_q` vs `[2c]_q`,
     or a `q^{−1/2}`-twisted variant) is the right one — the parity law fixes
     bar-evenness, not the specific bracket.

**Guard.** Selecting among bar-even brackets by matching the measured `c₃` would
be a fit and closes nothing. The next step is to construct the generator and read
`μ_λ` off it, then check it lands in this class.

Status stays `todo`.

---

# THE GENERATOR IS BLOCKED ON MISSING INFRA — and the bracket ambiguity collapses
# (2026-08-10)

Went to construct the q-heat-kernel generator whose block eigenvalue is `μ_λ`.
Two results: the construction is blocked, but not on research — and the "which
bracket" ambiguity flagged in the previous section is smaller than stated.

## 1. There is no q-deformed central element in the corpus

Searched the whole Hecke + Schur–Weyl tree, including the `SW-1..SW-9` work that
landed today (`QOU/SchurWeyl/{HeckeAlgebra,HoefsmitRep,YoungTableaux}.lean`,
`QOU/HeckeAlgebra/{Common,Demazure,Formal,Hoefsmit,JonesMarkovWenzl,MarkovTrace}.lean`):

    q-deformed Casimir / central element / Jucys–Murphy family:  NONE

The corpus's only Jucys–Murphy is `JucysMurphy.lean:123`, over
`MonoidAlgebra k (Equiv.Perm (Fin n))` — the **classical S_n** family. That is
both why `contentSqSum` is q-independent (hence pruned) and why `μ_λ` cannot be
read off anything currently in the tree.

**So the generator is blocked on infrastructure, not on open mathematics.** What
is missing is the q-JM family `L_1 … L_n ∈ H_n(q)` and its seminormal
eigenvalues — standard, citable material (Dipper–James; Murphy; Ram), and the
`SW-4` Hoefsmit seminormal reps that just landed are the natural substrate to
build it on. That is a well-posed formalisation task, not a research gap, and it
should be filed as such rather than left inside this bean.

## 2. The bar-symmetrised JM sum is the principled generator

In `H_n(q)` the JM element `L_k` acts on the seminormal basis with eigenvalue
`q^{2c}`, `c` the content of the cell holding `k` (standard convention — **not**
currently stated anywhere in this corpus, so it must be cited when built).

A single `L_k` is **not** bar-even. Its bar-symmetrisation is:

    L_k + L_k⁻¹   ↦   q^{2c} + q^{−2c}          — the *cosh* form.

This is the first thing that **selects** a bracket rather than merely permitting
one, and it selects on a corpus-internal principle: the bar-even ↔ `cosh` /
bar-odd ↔ `sinh` dictionary AGENTS.md already uses for the meson scale (`m_π`,
bar-even cosh) against `Q_β` (bar-odd sinh). Bar-symmetrising the canonical
central family is the natural way to land in the bar-even class the parity law
demands.

## 3. The two bar-even candidates are the SAME object — identity

The previous section listed `Σ_c [c]_q²` and left "which bracket" open. It is
narrower than that. Per cell,

    q^{2c} + q^{−2c} = (q − q⁻¹)² · [c]_q² + 2

(immediate: `(q^c − q^{−c})² = q^{2c} − 2 + q^{−2c}`, and
`[c]_q = (q^c − q^{−c})/(q − q⁻¹)`). Summing over the `n` cells of λ:

    **Σ_{c∈λ} (q^{2c} + q^{−2c}) = (q − q⁻¹)² · Σ_{c∈λ} [c]_q² + 2n**

Verified symbolically per-cell, and numerically on λ = (2), (2,1), (3,1) where
the residuals are exactly 4, 6, 8 = 2n.

Consequence: the two candidates differ by a **bar-even scalar** `(q − q⁻¹)²` and
a **λ-independent** additive `2n`. The scalar is absorbed into normalisation; the
additive shift moves every rate equally, which in the heat trace
`Z_q = Σ_λ d_λ exp_q(−μ_λ t)` is an overall factor, not a change to the relative
spectrum. **So the bracket choice is not a real degree of freedom** — it is a
normalisation convention. One line of Lean.

## Net position

  * forced: `μ_λ = q^{−1/2}·g_λ`, `g_λ` bar-even  (owner ruling + parity law)
  * forced: `g_λ` is *not* the corpus's `Σ q^{c}`  (bar-even only on
    self-conjugate λ; refuted structurally at n = 2)
  * now also: the two natural bar-even `g_λ` coincide up to bar-even scale and a
    λ-independent shift, so no choice remains to be made there
  * still missing: the q-JM family in `H_n(q)` — **infrastructure**, and the one
    thing standing between this and a derived `μ_λ`

**Guard.** Everything above is shape and structure. None of it evaluates `c₃`, and
fixing the normalisation by matching the measured `c₃` would convert the whole
chain into a fit.

Status stays `todo`.

---

# PARITY-SCOPE FINDING — the bar-parity law holds exactly for 2×2-box partitions
# (2026-08-22, claude/mu-lambda-heat-kernel-2026-08-12)

## The test

The content-Casimir formula `μ_λ = ℏ_q² · Σ [c]_q[c+1]_q` was tested numerically
(270 partitions, n=2..12, 50 dps) and symbolically (SymPy) for the bar-parity
property `μ_λ(1/q) = q · μ_λ(q)`.

## Result

The parity law holds **exactly** for partitions fitting in a **2×2 box**
(equivalently: max |cell content| ≤ 1). These are: (2), (1,1), (2,1), (2,2).

Symbolic proof for (2): `μ_{(2)}(1/q) / μ_{(2)}(q) = q` identically (SymPy,
exact rational simplification). The single contributing cell has content 1; the
product `[1]_q · [2]_q = 1 + q` transforms as `(1+1/q) = (1+q)/q`, and
`ℏ_{1/q}² / ℏ_q² = q²`, giving ratio = q.

For non-2×2 partitions the ratio is a q-dependent rational function ≠ q:

    μ_{(3)}(1/q)/μ_{(3)}(q) = (2q² + q + 1) / (q³ + q² + 2q) ≈ 0.949
    μ_{(1³)}(1/q)/μ_{(1³)}(q) ≈ 2.076

## Interpretation

The parity law from `prop:q-beta-c-k-recursion-from-habiro-q-difference` is
**correct but scoped**: it applies to the **SU_q(2)-relevant representations**
(partitions with at most 2 rows and 2 columns), not to arbitrary λ ∈ Ŝ_n. This
aligns with:

  - the QOU framework operating on SU_q(2) (rank 2)
  - the formalized Hoefsmit cases being exactly λ = (2,1) and (2,2)
  - the q-beta recursion involving only low-N modes (N ≤ 4)

The content-Casimir formula is **not excluded** by the parity law within its
applicable scope. The earlier exclusion of `contentSqSum` (q-independent Σc²)
remains valid — it is excluded for a different reason (bar-even, not the right
bar-weight).

## Consequence for the "normalisation convention" finding above

The claim that `Σ [c]_q²` and `Σ (q^{2c} + q^{-2c})` differ only by a bar-even
scalar + constant remains true and useful. The parity-scope result says that
the strict-reading constraint (`μ = q^{-1/2} · g_λ`, `g_λ` bar-even) is a valid
filter only on 2×2-box partitions. For broader λ, the content-Casimir has a
richer bar-transformation that depends on the cell-content multiset.

**Guard.** This is a structural finding (exact symbolic identity + exhaustive
numerical verification), not a fit. No anchor input used.
