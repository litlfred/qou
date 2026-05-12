# Lean Phase 4 — P4.B discharge + §6 escalation on P4.A scope

**Date:** 2026-05-12
**Branch:** `copilot/feature-coordinate-pr-644`
**Coordinates with:** [PR #644 — 1 ppb mass closure plan](https://github.com/litlfred/qou/pull/644)
**Companion:** [`2026-05-12-lean-handover.md`](2026-05-12-lean-handover.md)

This note records (a) the P4.B discharge and (b) one §6 inconsistent
finding versus the handover doc that the next agent / author should
arbitrate before promoting downstream propositions out of
`conditional-on-class` status.

## 1  P4.B — discharged with framing fix

**File:** `content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.lean`
**Lines (post-fix):** 500–508

### What changed

The skeleton instance was previously:

```lean
instance canonicalCrossCoupling [_M : MagicShellStabilization] :
    MagicShellCrossCoupling where
  ...
  cross_decomposition Z N := by
    show _M.delta_shell Z N
            = _M.delta_shell Z 0 + _M.delta_shell 0 N + 0
    sorry
```

It is now:

```lean
instance canonicalCrossCoupling : MagicShellCrossCoupling (M := canonical) where
  delta_coupling _ _ := (0 : ℝ)
  cross_decomposition _ _ := by simp
  coupling_non_magic_z _ _ _ := rfl
  coupling_non_magic_n _ _ _ := rfl
  coupling_z_n_symmetry _ _ := rfl
```

### Why the previous form was unprovable

The handover doc (§2 P4.B) claimed cross_decomposition would be
`simp`-discharged "because the canonical instance sets
$\Delta_{\mathrm{shell}} \equiv 0$, so cross_decomposition reduces to
$0 = 0 + 0 + 0$."

That claim is correct **only** when the instance is specialised to
the `canonical` `MagicShellStabilization` (the one declared at line 172
with `delta_shell _ _ := 0`).  The original instance signature
`[_M : MagicShellStabilization]` ranges over *every* implementation
of the class, not just `canonical`.  For an arbitrary `_M`:

- `magic_only_support` only gives `delta_shell Z N = 0` when **both**
  `Z` and `N` are non-magic.  It says nothing about
  `delta_shell Z 0` vs `delta_shell Z N` in general.
- `z_n_symmetry` gives `delta_shell Z N = delta_shell N Z`.  Also no
  additivity.
- No third axiom forces `delta_shell Z N = delta_shell Z 0 + delta_shell 0 N`.

Hence `cross_decomposition` is genuinely unprovable in the
universally-quantified form — no tactic can close it, and the original
`sorry` was not a §3b conjectural placeholder but a real proof gap.

### Effect on instance synthesis

All downstream theorems that consume the cross-coupling
(`he3_no_cross_coupling` line 457, `tritium_no_cross_coupling` line 465,
`cross_coupling_mirror_symmetry` line 474, `doubly_magic_he4_with_cross_coupling`
line 437, plus the bound consumers around lines 573, 604, 627) take
`[Cross : MagicShellCrossCoupling (M := M)]` as an **explicit**
hypothesis — they don't rely on instance synthesis from a bare
`[M : MagicShellStabilization]`.  So narrowing the canonical instance
to `(M := canonical)` does not break any downstream lemma.

A user who supplies a non-canonical `MagicShellStabilization` must now
also supply a matching `MagicShellCrossCoupling` — which is correct,
because the cross-decomposition is genuine substrate-derived content,
not free.

## 2  §6 escalation — handover doc P4.B claim was inconsistent

**Sibling claim** (handover doc §2 P4.B, line ~"Suggested first tactic attempt"):

> If unfolding doesn't fire, add explicit `unfold MagicShellStabilization.delta_shell` and then `ring` or `linarith`.

This implies the obligation is closeable for an arbitrary `_M`, which
is not the case (see §1 above).

**This branch's claim:** P4.B's `sorry` is closeable iff the instance
is specialised to `canonical` (or to any other `MagicShellStabilization`
that happens to satisfy additivity).  The handover doc's "for-all-`_M`
+ unfold" path is mathematically incorrect.

**Resolution requested from author:** confirm the specialised-to-
`canonical` framing.  If a different framing was intended (e.g. add
an `Additivity _M` hypothesis to the cross-coupling class), this
branch will rebase.

Tagging `@litlfred` for arbitration.  No downstream work is blocked —
the discharged form preserves all existing downstream lemmas — but
the §3b-cond status of `MagicShellCrossCoupling`-dependent
propositions in
[`conjectural-propagation-audit.ts`](../../content/pipeline/conjectural-propagation-audit.ts)
should NOT be promoted until this is confirmed.

## 3  P4.A — deferred

**File:** `content/quantum-observable-universe/braids-and-knots/prop-rigid-monoidal-structural-gap-invariance.lean`, line 224.

The handover doc's proposed closure path requires designing a
`MarkovTraceAxiomatic` Mathlib typeclass bundling
(a) the Markov axiom interface,
(b) Jones-Wenzl projector existence, and
(c) the uniqueness lemma.

That is a multi-PR research item:

- The typeclass design must be coordinated with upstream Mathlib's
  `MarkovTrace.lean` (in `Hecke/`) — already partially landed per
  handover §3 finding 2 ("T1 canonicalisation is settled").
- Jones-Wenzl projector uniqueness in Mathlib is itself a lemma
  whose Lean formalization status is `not_started` per the QOU
  proof-objects manifest at the time of writing.

A separate PR scoped to `MarkovTraceAxiomatic` (and a separate
coordination round with the agent who owns `Hecke/MarkovTrace.lean`)
is the right vehicle.  This branch does **not** touch
`prop-rigid-monoidal-structural-gap-invariance.lean`.

## 4  Build verification

Lean toolchain is not installed in the sandbox where this PR was
authored.  Verification of the P4.B fix is deferred to:

- CI: `lean_ci.yml` will run `lake build QOU` on push.
- Local: per CLAUDE.md §0a, run `lake build QOU` from the repo root.
- Spot-check: per CLAUDE.md §6 ("Use MCP tools, not shell commands"),
  the next session should run `lean_diagnostic_messages` on the file
  to confirm the `simp` closes cleanly with no auxiliary unfolds.

If `simp` does not close (e.g. because instance projection on the
`canonical` field does not reduce as expected), the documented
fallback is:

```lean
  cross_decomposition _ _ := by
    show (0 : ℝ) = 0 + 0 + 0
    ring
```

## 5  What this PR does not do

- Does not touch `prop-rigid-monoidal-structural-gap-invariance.lean`
  (P4.A — out of scope; see §3).
- Does not touch the other Lean `sorry`s tracked in handover §4
  (`Kashaev.lean`, `Hecke/OneDimChiBridge.lean`,
  `Hecke/Hoefsmit.lean`, `Hecke/MarkovTrace.lean`).
- Does not change any narrative content blocks; the §3b-cond
  status manifest update is left for the next coordination round
  pending §2 arbitration.
- Does not promote any downstream propositions from
  `conditional-on-class` to fully provable, even though the
  `MagicShellCrossCoupling` skeleton is now `sorry`-free —
  promotion requires the §2 arbitration to close.
