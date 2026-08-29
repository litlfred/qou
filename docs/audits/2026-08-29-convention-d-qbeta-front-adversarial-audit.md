# Convention-D Q_β/c₃ derivation front — adversarially-verified audit

**Date:** 2026-08-29 · **Method:** 5-lane derivation workflow (15 agents:
5 derive + 10 red-team, 2 adversarial lenses each), all analytical /
corpus-grounded / exact-arithmetic (sympy, mpmath dps≥50); **no Lean
compiled** (a cache reseed build was running). 0 agent errors.
· **Tier:** mixed — one **proved-lean** structural verdict (lane 2), three
**symbolic-exact** results, the magnitude/parity gates **open**.
· **Discipline:** anti-fit, formalize-first, scope-(a)/(b), corpus-grep, tiered
status. Every number below is either a corpus citation or an exact symbolic
identity — **no numerical hunting**.

Adversarial outcome: **9 of 10 red-team verdicts survive.** The single failure
(lane 1, `status-invariant` lens) correctly caught a convention-independence
**overclaim**; that lane's two load-bearing conclusions survive and are recorded
in their corrected form below.

## The unifying result — every lane blocks on `qou-cds1`

All five gaps converge on one upstream blocker: **there is no convention-D
`c₃` (or `c₂`, or bar-parity, or magnitude target) until the Q_β ladder is
RE-DERIVED from the D Markov trace** — and the C→D move is **not** a z-swap.
This is now **proved-lean** (lane 2, both lenses survive), from three sorry-free
theorems:

- `decayLadder_zC_threeRow_ne_zero` (`MarkovZFullBarCondition.lean:214`) with
  `threeRow_ne_zero_of_ocneanu_ne`
  (`QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean:147`): any faithful C-frame
  decay ladder carries a **nonzero three-row weight** `y_(1³)` for every
  `s=√q>1` — it does **not** factor through Temperley–Lieb.
- `markovWeights_eq_jones_of_threeRow_eq_zero`
  (`MarkovTraceTLUniqueness.lean:97`): `y_(1³)=0` ⟺ `z=z_D` (the two-row /
  TL / Jones trace). Strengthened by the red-team: `qou-06wh` / PR #5925 now
  Lean-proves `y_(1³)(z)` has exactly two roots `{q, z_D}` with `net`
  **excluded**.
- Eigenphase bar-parity **flips**: under C, `α` is bar-odd (defect 0); under D,
  `bar(2α)+2α = h²` exactly (z-independent, `eigenphase_bar_defect_of_fullBar`).
  So **every** `c_k` bar-parity fact (H1 `c₃^even=−Vol(4₁)`, `S_leak`, `q*_S`,
  KC13) rests on `α` bar-odd and is **C-scoped**.

Consequently the naive z-swap `z_C→z_D` giving `c₃ ≈ −974` is a **scope-(b)
excluded** operation, not a value: it keeps the C formula while silently
changing the trace and breaking bar-parity. (Cost framing corrected per
red-team: the −974 is a `1/u³` amplification — bean `qou-cds1` L583ff measures
the D phase residual at **0.895×**, *better* than C; −974 "measures the
amplifier, not the physics." Do not quote it as "D is catastrophic.")

**Compatibility clarification (lane 2):** the mass-channel three-row forcing is
**not** incompatible with a genuine D ladder. A real D ladder *must* factor
through TL, co-located with the mass channel in `TL_∞(q)`. The C-frame mutual
exclusivity was "keep the C-ladder-as-built" vs "two-row forcing", never
"D ladder" vs forcing.

## Two convention-agnostic structural handles

Amid a C-conditional cluster, two proved facts survive C→D and are the load-
bearing invariants going forward:

1. **The affine transport** (avt1 / KC19): `evalMap_ratio`
   (`CrossingWeightAffine.lean:62`, sorry-free, generic field) makes the
   counit→trace transport `L(w)=(h−2w)/(h−2w₀)` **affine** in the crossing
   weight; reparametrised by `α`, `T(α)=1−4α/(h(h−2))` is linear with **even
   part identically 1**. Convention-agnostic (α a free parameter).
2. **The braid-image eigenphase exclusion** (qb8e): `BraidImageEigenphase{Exclusion,Algebraic}.lean`
   (sorry-free, both the character and eigenvalue-pair cases) exclude any
   braid-word carrier of `α`, because `α` is non-constant/unbounded with
   infinite level sets of `2cos α` in `[−2,2]` — **in both frames** (verified
   this run: `α_C→−∞`, `α_D→+∞` as `q→∞`). The proof never reads `z`'s formula.

These are the `|c₃|`-side and the transport-side of the same phenomenon: the
structural skeleton is convention-agnostic; only the `z`-dependent phase is
C-conditional.

## Per-lane verified findings

### Lane `avt1-cos-necessity-under-D` — the cosine loses its justification under D (symbolic-exact; both lenses survive)

Under canonical D the Q_β **cosine correction is NOT derived**. Its sole
structural justification — Markov-cyclicity-via-bar-involution forcing evenness
in `α` — **provably evaporates**, because `z_D` is neither bar-even nor bar-odd:
symbolic-exact this run, `α_D(1/q)+α_D(q) = q²/2 − 1 + 1/(2q²) ≠ 0` (vs
`α_C(1/q)+α_C(q)=0`, bar-odd). The equality `α(1/q)=−α(q)` holds **iff**
`z(1/q)=z(q)`, true for C and false for D. The only convention-agnostic proved
transport is affine (even-part 1, zero O(α²) content), so the cosine's entire
O(α²) correction is **axiom-sourced with no D-valid backing**.

**Verdict:** `QBetaCosResummation` should be **dropped under D or explicitly
scoped convention-C-only** — scope-(a) ("not derived", not "false": an
undiscovered bar-odd `α_D` reproducing the H₃ `V_(2,1)` transfer-matrix spectrum
could rehabilitate it — that is the true fork). **Red-team strengthened this:**
there is a **second** cosine carrier, `QOU.BraidKnot.V21Eigenphase` /
`markovSymmetrizedV21Character` in `HoefsmitV21CosSymmetrization.lean`, **also**
built on the convention-C eigenphase — so the "no D-derivation" verdict is
*stronger* (two carriers, both C-only), and any C-scope/drop remediation must
cover both files.

### Lane `cds1-ladder-survival` — proved-lean; see "The unifying result" above.

**Next brick:** resolve owner-call `qou-99qc` — pin which counit `ε` the phase
`α=(ε−tr_M)/2` uses: one that **descends to `TL_∞(q)`** (annihilates the `(1³)`
ideal) *and* reduces to the corpus mass-channel `ε`. The current `net`
(augmentation) does **not** descend: `net(e)=q³(q−1)/((q²+1)(q²+q+1)) ≠ 0` on
`J_(1³)` (symbolic-exact), so the ansatz is not defined on the D GNS space
(`prf:algebraic-gns-embedding`, `qou-879g`).

### Lane `cds1-c2-structural` — c₂ under D is OPEN (the overclaim was caught)

Corrected per the failing `status-invariant` lens: the **expression** `1−u²`
for the *current (C-frame)* N=2 factor contains no `z` (symbolic-exact; z is not
a free symbol of `1−b²ℏ_q⁴`; stated in the `DecayLadderConventionDPositivity`
**docstring**, not a theorem — the sorry-free theorems there prove the
phase-coefficient sign separation `z_D>1/2`, `z_C<1/2`). **Whether the
D-rebuilt ladder's explicit N=2 factor is also `1−u²` is OPEN** — the ansatz has
not been rebuilt from the D trace. Do **not** state "c₂^D = −1, convention-
independent"; the registry marks c₂=−1's structural status as itself a C-frame
statement, and (AGENTS.md 2026-08-16) "PROVED" is already downgraded to
"structural" (a one-line `ring` re-reading of `N2_factor`, no derivation
theorem).

**What is closed:** the D "c₂ ≈ −9.299" is a **CODATA data-inversion**
`(Q_β^exp/Q_N1^D − 1)/u²` — an empirical re-extraction, **not** a structural
coefficient (scope-(a)). **Next brick:** derive the D N=1 rung phase directly
from the D crossing-weight construction on H₃ (not by substituting `z_D` into
the C phase); only then does "c₂ under D" have a structural referent.

### Lane `qb8g-parity-under-D` — OPEN, with a NEW derived discriminant (symbolic-exact; both lenses survive)

**New symbolic-exact structural discriminant** (the precise reason the C
construction does not port to D): the C-frame rung phase `α_C=(z_C−1)h/2` is
**pure bar-odd** — its bar-even part is exactly 0 — which is *why* the
`log R = E(ũ) + h·D(ũ)` construction can pin the even channel `E` with
normalisation fixed in advance. The D-frame phase `α_D=(z_D−1)h/2` is
**bar-mixed** (even part `(q²−1)²/(4q²) ≠ 0` *and* odd part ≠ 0), because
`z_D−1` is not bar-homogeneous (`z_D` has bar-weight −4, the constant 1 has
weight 0). So the pure-odd-phase mechanism that pinned the C split has **no D
analog yet**. This does not supply a c₃ parity; it identifies the exact
obstruction. (The exact `ũ`-ladder `e₁=3√3/4`, margin 9, is a genuinely-derived
decomposition of `log R`, **not** of `c₃`; the `+86.66` projection onto c₃ is a
projection artifact — see `qou-qb8f` adjudication.)

### Lane `qb8e-magnitude` — OPEN, blocked upstream; convention-agnostic prune (both lenses survive)

The `|c₃|` magnitude gate is untouched (only parity is settled) and **blocked
upstream on `qou-cds1`** (−974 is an artifact, not a target). The
convention-agnostic scope-(b) prune above (braid-word carrier excluded) is the
`|c₃|` analog of the avt1 handle. The sole surviving carrier is **branch (3)**:
a KZ/Kohno–Drinfeld holonomy of the H₃(q) braiding on `V_(2,1)` with `ħ=2ln q`
(scale fixed, not free) — but the red-team flags a possibly-fatal precision
obstruction (`qou-pdix`: the single-wrap-vs-typed-NF ambiguity 0.579% exceeds
the 0.160% effect branch (3) must derive, a 3.6× gap). The magnitude invariant
is itself conditional on the D-frame ladder-coefficient framing surviving cds1
(the re-evaluated D residual ratio N2/N1 ≈ 0.89 shows **no rung convergence** —
so `c₃` may not be a convergent-ladder coefficient under D at all).

## Ranked next bricks

1. **Land `QOU/QBeta/LadderCosClash.lean`** (avt1) — sorry-free, ~55 lines,
   generic field + ℝ, **convention-agnostic** (does not wait on cds1). Converts
   the avt1 symbolic-exact verdict to proved-lean: the affine transport's even
   part is the constant 1, so the cosine is the sole carrier of the O(α²) term.
   Then C-scope/drop **both** cosine carriers. *Immediately doable; drafted.*
2. **`qou-cds1` → resolve owner-call `qou-99qc`** (the counit `ε` descending to
   TL). Unblocks lanes 1, 4, 5 simultaneously. Owner call.
3. Record the **α_C pure-bar-odd / α_D bar-mixed** discriminant (lane 4) as a
   Lean lemma (symbolic-exact → proved-lean) — it is the structural obstruction
   to porting any C-frame bar-decomposition to D.
4. Branch (3) KZ holonomy (qb8e) — only after the `qou-pdix` precision
   obstruction is assessed; a magnitude match found by search is a fit.

## Provenance

Workflow `convention-d-qbeta-front` (run `wf_fab4875c-c61`), 15 agents,
2.59M tokens, 0 errors. Every symbolic identity was independently re-derived by
the red-team in sympy (no float64). No witness emitted, no fit, nothing wired.
Beans updated: `qou-avt1`, `qou-cds1`, `qou-qb8g`, `qou-qb8e`.

-- Ref: [manuscript] docs/coordination/ck-dk-canonical-registry.md §9
-- Ref: [manuscript] .beans/qou-cds1, qou-avt1, qou-qb8g, qou-qb8e, qou-99qc
