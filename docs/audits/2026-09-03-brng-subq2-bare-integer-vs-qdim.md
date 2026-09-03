# qou-brng sub-question #2 — why mutual is a bare count while self is the q-dim `lw` (status + why it is not one-session closable)

**Date:** 2026-09-03 · **Bean:** `qou-brng` · **Arc:** bk-crossing mass-binding (Δ_λ extensive-term
frontier). **Scope:** an evidence-based status of the one open *structural* target on this frontier,
and a precise statement of what would close it — written so the next agent does not (a) re-attempt
the two gated magnitude shortcuts, or (b) land a finset re-encoding that *launders* the open
assumption. **No new Lean or compute is added; this is an assessment.**

## Why this doc exists

`qou-brng`'s open kernel has one surviving *structural* sub-question (its update of 2026-08-30, PR
#6125):

> **#2 — why does the surviving count/mutual channel enter as a BARE INTEGER while the self/mass
> channel keeps the full q-dim self-trace `lw`?** (self = closed quantum trace over Wedderburn
> channels; mutual = pairing of two fixed components, no internal channel sum — *plausible but NOT
> proved*.)

This session surveyed the frontier to pick a non-duplicative angle and found sub-q #2 is the only
clean, non-gated positive target. On close inspection it is **not honestly closable in one session**,
and the reason is worth recording precisely, because the obvious "formalize-first" move here is a
laundering trap.

## What is already proved (the delta to sub-q #2 is narrow and specific)

All sorry-free on `main`:

| result | file | says |
|---|---|---|
| `QOU.Mass.SelfMutualPartition.binding_eq_neg_mutualEnergy` | `Mass/SelfMutualPartition.lean` | crossing energy partitions self + mutual; `binding = −(mutual)`, self-energies cancel |
| `QOU.Mass.SelfMutualPartition.binding_indep_of_self` | ″ | binding is independent of every self-crossing (falsifiable content) |
| `QOU.Mass.BrunnianBindingChannel` | `Mass/BrunnianBindingChannel.lean` | the mutual energy splits signed (writhe/linking, `n₊−n₋=2lk`) + unsigned (count, `n₊+n₋`); for a Brunnian pair the signed channel is 0, so binding is the **unsigned count** channel |
| `QOU.Mass.BindingMassRung.bindingOverMass_eq` / `_tendsto_zero` | `Mass/BindingMassRung.lean` | `binding/mass = (M/lw)·ℏ_q²` → 0; mass multiplier `lw/ℏ_q²` is an order-2 pole (residue `lw`) |

So the corpus already has: (i) binding = the mutual channel (theorem), (ii) the mutual channel is
the *unsigned count* `n₊+n₋` for a Brunnian carrier (theorem), (iii) the O(ℏ_q²) rung dichotomy
(theorem). What remains for sub-q #2 is exactly one link: **that the mutual count carries no internal
Wedderburn-channel sum (so it is a bare integer), whereas the self-energy closes to `lw = Σ_λ qdim`
(the q-dim-weighted channel sum).**

## The two shortcuts — both forbidden, for different reasons

### Shortcut A (magnitude): DO NOT attempt `b_αα` or force the `≈ℏ_q²` saturation

Recorded here so the next agent does not confuse sub-q #2 (structural, in scope) with the magnitude
targets (gated):

- **`b_αα ≈ 2.41 MeV` — do-not-attempt** (`qou-ebs6`): one parameter fitted on two points (¹²C, ¹⁶O),
  zero out-of-sample support inside its own domain (`QOU.Mass.EquilateralBound` proves the
  complete-graph bond count `C(n_α,2)` is geometrically unrealizable for `n_α ≥ 5`, so only
  ⁸Be/¹²C/¹⁶O qualify and ⁸Be≈0 is *excused*). "The single easiest place in this arc to land a fit
  dressed as a derivation."
- **The `≈ℏ_q²` saturated-binding-fraction** — its one candidate mechanism (volume-defect) is
  **refuted** (`binding_volume_defect_route_refuted.py`, overpredicts 102–250×); on current evidence
  "more likely numerology than a derived prediction." Do not wire, do not force to `1·ℏ_q²`.

### Shortcut B (structural, and this is the subtle one): DO NOT re-encode sub-q #2 in finset algebra

The tempting formalize-first move is to extend `SelfMutualPartition` with a channel index: give each
component a Wedderburn index set `Λ` with weights `d : Λ → K`, define `selfWeight := Σ_{λ} d λ` and
`mutualCount := (|crossing set| : K)` (no `Λ`), and "prove" they differ / that `mutualCount` is
independent of `d`. **That is laundering.** The proposition to be *derived* is precisely that the
mutual functional has no `Λ`-sum; defining it without `Λ` and then observing it has no `Λ` assumes the
answer. Per the repo's "define ≠ derive" / anti-laundering discipline (`AGENTS.md` §"Defined residual
≠ derived decomposition", §"Axiomatization is NOT a Proof"), this would satisfy a checker while
proving nothing, and is explicitly the failure this doc exists to prevent.

## Why `BindingMassRung` does not close it either

`BindingMassRung` treats `M` and `lw` as **free real parameters**; it proves the O(ℏ_q²) dichotomy
*given* `binding = m_e·Vol·M` and `mass = m_e·Vol·(lw/ℏ_q²)`. Its own docstring is explicit: *"It does
NOT derive why binding lacks the cusp factor — that residual kernel is the open item."* The dichotomy
forces binding to be **q-regular** (order ℏ_q² ⇒ regular at `q=1`); it does **not** force `M` to be a
**bare integer** (q-independent). A q-regular quantity can still depend on `q` (e.g. any polynomial in
`ℏ_q`). So the proved lever gives half of "not q-dim-weighted like self" (regularity) and none of the
positive "bare integer, no channel sum." It is not a shortcut to sub-q #2.

## What would actually close it (the honest requirement)

Sub-q #2 is a **ribbon-category** statement, and closing it needs the categorical trace / S-matrix
structure:

- **Self** (one component closed into a loop): the quantum trace `tr_q(id_X) = qdim(X)`. For
  `X = ⊕_λ n_λ V_λ` this is `Σ_λ n_λ qdim(V_λ) = lw` — the sum runs over the object's *internal simple
  summands*, because closing a strand takes the full endomorphism trace, which decomposes over the
  decomposition of `X`.
- **Mutual** (two *fixed* components linked): the Hopf/linking pairing of two fixed simple objects
  `a, b` — a single S-matrix entry `S_{ab}` (or a bare inter-component crossing count), with **no**
  internal decomposition, because `a` and `b` are fixed simples, not a composite being co-traced.

The difference "closed trace over an internal decomposition" vs "pairing of two fixed simples" is
where the `Σ_λ` appears in one and not the other — and it is a fact about the ribbon/braided
structure, not about a chosen index set. **Mathlib has no ribbon/braided-fusion categories, no
quantum dimension, and no S-matrix.** This is the *same* infrastructure gap that blocks the R2 lift
(`ArchimedeanTraceBridge` carries Jones/Markov multiplicativity as a hypothesis; `qou-301d`), and it
is a multi-file formalization project, not a one-session close.

## Recommendation (judgement, marked as such)

1. **Leave sub-q #2 open and unfabricated.** The honest state: binding = the unsigned mutual count is
   proved; that the count carries no Wedderburn-channel sum (bare integer) vs the self-trace `lw`
   (q-dim-weighted channel sum) is a ribbon-category fact requiring infrastructure Mathlib lacks. Do
   not launder it via a finset re-encoding.
2. **The tractable adjacent formalization is the shared infra**, not sub-q #2 directly: the
   quantum-trace / connected-sum multiplicativity project (`qou-301d`). Closing that would give both
   sub-q #2 and the R2 lift a real foundation. It is large but honest.
3. **Do not touch the magnitude targets** (`b_αα`, the `ℏ_q²` saturation) — gated per shortcut A.
4. **Default if nothing is done:** nothing changes; sub-q #2 stays the named open kernel of
   `qou-brng`, the magnitude stays gated, and no number moves. That is a safe no-op.

## The genuinely open, higher-leverage item this frontier sits under

Recorded because it dominates the magnitude question: the framework currently **binds the diproton
and dineutron** (a wrong-sign prediction; `QOU.QBeta.single_crossing_binds`). Per the arc's own
"signs before digits" — *no magnitude work reaches L2 while a predicted observable has the wrong
sign.* Every in-algebra unbinding mechanism tried so far is excluded; the un-attacked route is a
non-separable (S,L) coupling (`qou-vbyi`, route 1). This is not sub-q #2, but it is the reason the
extensive-term magnitude is not the top priority on this frontier.
