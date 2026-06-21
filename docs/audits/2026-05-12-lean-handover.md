# Lean handover — Phase 4 of 1 ppb plan

**Date:** 2026-05-12
**Companion to:** [`2026-05-12-1ppb-implementation-plan.md`](2026-05-12-1ppb-implementation-plan.md)
**For:** Lean agent picking up Phase 4 (sorry discharge for
conditional-class results in the magic-shell + structural-gap
chains)

This document collects all findings from the Phase 1/2 audit that
are relevant to Lean formalization, plus pinpoint locations and
mathematical content for the two `sorry`s the plan targets.

## 0  Scope

The 1 ppb plan's Phase 4 has two named tasks:

- **P4.A** — discharge §3b `sorry` in
  `prop-rigid-monoidal-structural-gap-invariance.canonical` via the
  proposed `MarkovTraceAxiomatic` Mathlib typeclass.
- **P4.B** — discharge `sorry` in
  `MagicShellCrossCoupling.canonicalCrossCoupling` (canonical
  instance with $\Delta_{\mathrm{shell}} \equiv 0$ should be `simp`-
  provable).

Both are **conditional-class instances** in the §3b-cond sense (see
AGENTS.md §3b-cond). The remaining `sorry`s record the conjectural
backing; closing them would either prove the conjecture or replace
it with an explicit Mathlib dependency.

## 1  Pinpoint locations

### P4.A — Layer-1 Jones-Wenzl uniqueness

**File:**
[`content/quantum-observable-universe/braids-and-knots/prop-rigid-monoidal-structural-gap-invariance.lean`](../../content/quantum-observable-universe/braids-and-knots/prop-rigid-monoidal-structural-gap-invariance.lean)

**Sorry location:** line 224, inside `instance canonical (α : Type*)`
(starting at line 212).

**Surrounding context** (lines 198–224):
```lean
  instance below records the §3b `sorry` for the Layer-1
  ...
  The §3b `sorry` marks the Layer-1 Jones-Wenzl uniqueness step
  ...
instance canonical (α : Type*) :
    ...
    sorry
```

### P4.B — `canonicalCrossCoupling`

**File:**
[`content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.lean`](../../content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.lean)

**Sorry location:** line 496, inside
`instance canonicalCrossCoupling [_M : MagicShellStabilization]`
(starting at line 485).

**Surrounding context** (lines 485–496):
```lean
instance canonicalCrossCoupling [_M : MagicShellStabilization] :
    MagicShellCrossCoupling where
  ...
    -- Under the canonical Δ_shell ≡ 0 + canonical additivity (also
    -- canonical instance), cross_decomposition should reduce to
    -- 0 = 0 + 0 + 0.
    -- Use canonical Δ_shell ≡ 0; both sides reduce to 0.
    sorry
```

The plan asserts P4.B should be provable by `simp` because the
canonical instance sets $\Delta_{\mathrm{shell}} \equiv 0$, so
`cross_decomposition` reduces to the trivial identity $0 = 0 + 0 + 0$.

## 2  Mathematical content of each sorry

### P4.A — what needs to be proved

The structural-gap invariance proposition states that
$|\tau(\beta)|$ for the QOU production braids is independent of
the rigid-monoidal-category convention chosen to host
$\mathbf{Rep}(\mathrm{SU}_q(2))$ (Type B folded vs unfolded etc.).

The full proof is layered:

- **Layer 1:** Jones-Wenzl uniqueness — the Jones-Wenzl projector
  $p_n$ in the Temperley–Lieb subalgebra is unique up to scalar in
  any Markov-trace-equipped rigid monoidal $\mathbf{C}$ admitting a
  fibre functor to $\mathbf{Vec}_q$. This is the load-bearing piece
  that `instance canonical` records as `sorry`.
- **Layer 2:** Markov axiom invariance — the trace $\tau$ on
  $H_n(q)$ is uniquely characterised by the Markov axioms (M1, M2)
  given $z = 1/(q^{1/2} + q^{-1/2})$ and a normalisation. **Done**
  in upstream `MarkovTrace.lean`.
- **Layer 3:** Functorial transfer — once Layers 1 and 2 hold, any
  fibre functor $\tau : \mathbf{C} \to \mathbf{Vec}_q$ gives the
  same numerical $|\tau(\beta)|$. **Done.**

**Proposed closure path** (per the plan): introduce a
`MarkovTraceAxiomatic` Mathlib typeclass that bundles
(a) the Markov axiom interface,
(b) the Jones-Wenzl projector existence, and
(c) the uniqueness lemma.
Make `instance canonical` an instance of `MarkovTraceAxiomatic`
under the canonical definition. The `sorry` is then discharged by
the typeclass instance, with the typeclass itself becoming the
sole conjectural input (per §3b-cond).

### P4.B — what needs to be proved

`MagicShellCrossCoupling.cross_decomposition` (declared around line
467 of `conj-magic-shell-stabilization.lean`) states:
$$
  B(Z_1 + Z_2, N_1 + N_2) \;=\; B(Z_1, N_1) + B(Z_2, N_2) + \Delta_{\mathrm{shell}}^{\mathrm{cross}}(Z_1, N_1, Z_2, N_2)
$$
under the canonical instance with $\Delta_{\mathrm{shell}} \equiv 0$
(declared in `instance canonical` at line 172 of the same file) and
canonical additivity (declared at line 373). With both
$\Delta_{\mathrm{shell}} \equiv 0$ and additivity in scope, the LHS
and RHS each reduce to $0$ by `simp`. The plan claims this should
close immediately via tactic `simp [...]` with the right lemma list.

**Suggested first tactic attempt:**
```lean
instance canonicalCrossCoupling [_M : MagicShellStabilization] :
    MagicShellCrossCoupling where
  cross_decomposition := by
    simp [MagicShellStabilization.canonical, MagicShellAdditivity.canonicalAdditivity]
```
If unfolding doesn't fire, add explicit
`unfold MagicShellStabilization.delta_shell` and then `ring` or
`linarith`.

> **§6 correction landed in [#645](https://github.com/litlfred/qou/pull/645)
> (2026-05-12)** — the `[_M : MagicShellStabilization]` signature
> above is **genuinely unprovable**: `MagicShellStabilization`
> exposes only `magic_only_support` and `z_n_symmetry`; neither
> implies `delta_shell Z N = delta_shell Z 0 + delta_shell 0 N`,
> so the `simp`/`unfold + ring` path cannot close the obligation
> for an arbitrary instance. #645's resolution: pin the instance
> to `MagicShellCrossCoupling (M := canonical)` so the canonical
> `Δ_shell ≡ 0` unfolds and `simp` reduces both sides to `0`.
> Full design rationale + author-input asks in
> [`2026-05-12-lean-p4b-discharge-and-escalation.md`](2026-05-12-lean-p4b-discharge-and-escalation.md).
> #644 (this branch) endorses the pin as the right minimal fix;
> the alternative "add `Additivity _M` premise" is strictly more
> general but unnecessary while `canonical` is the only
> production instance.

## 3  Audit findings from the Phase 1/2 work that touch Lean

These are facts the Phase 1/2 narrative-side audit established that
the Lean agent should be aware of:

1. **Three weight families remain disambiguated**: $w_\lambda$
   (classical Plancherel), $\tilde w_\lambda$ (q-deformed Wedderburn),
   $y_\lambda$ (Markov). They coincide only at $q = 1$ on
   self-conjugate partitions. Any Lean lemma stating "Plancherel
   weight = Markov weight" must qualify with these conditions
   (see AGENTS.md §7aa, `notation-collisions.md`).

2. **T1 canonicalisation is settled** — the Hoefsmit seminormal +
   Jones–Markov $y_\lambda$ via Wenzl bridge is the canonical T1.
   `MarkovTrace.lean`, `Hoefsmit.lean` already encode this; no
   sorries blocking T1.

3. **T4 per-3A formula is settled** — `thm:frobenius-codim-universal`
   is Lean-proved. The narrative side has a few stragglers using
   the legacy per-A heuristic
   ($A \cdot m_e \cdot (2 + 1/[2]_q)$); these are scheduled for
   migration in Phase 1 P1.C and do not affect the Lean side.

4. **Term 5 chirality has TWO competing forms** in the literature
   (closed-form sign-table vs Gram pairing $\tau(\beta\beta^{*-1})$),
   disagreeing by 2.2 % on the proton. P1.B in the narrative will
   adopt the Gram form. The Lean side should mirror this — if a
   `Term5Chirality` typeclass exists, its canonical instance should
   compute $\tau(\beta\beta^{*-1})$, not the sign product.

5. **Path B (Habiro single-trace) calibrates $\alpha_M$ from
   deuteron binding** — line 227 of `path_b_habiro_mass_probe.py`.
   This is a CAL-3-adjacent calibration. If a Lean `PathBPrediction`
   typeclass exists, its canonical instance must record the
   $\alpha_M$ as a parameter (not derive it from $m_e, q_0, Q_\beta$
   alone), and any downstream theorem must carry the
   `[PathBCalibrated]` typeclass hypothesis.

## 4  Other Lean sorries discovered during the audit

These are **outside Phase 4 scope** but worth tracking. Found via
`grep -rn "sorry" content/quantum-observable-universe/lean/QOU/`:

| File | Line | Nature |
|------|----:|--------|
| `Kashaev.lean` | 87, 98 | KVC values — left as sorry per docstring (until upstream Mathlib lands) |
| `Hecke/OneDimChiBridge.lean` | 153 | one-dim character bridge step |
| `Hecke/Hoefsmit.lean` | 199, 209, 210 | structural `(sorry : Partition n)` placeholders for instance arguments |
| `Hecke/MarkovTrace.lean` | 138 | extending `MarkovTrace` to carry the canonical normalisation |

These should be treated as separate work items, not blockers for
Phase 4.

## 5  Build / verification checklist for the Lean agent

Per AGENTS.md §0a, the workspace is the **root Lake workspace**:

```bash
# from repo root
lake build QOU                 # build the qou paper library
lake exe cache get             # fetch Mathlib cache
```

After each `sorry` removal, verify:
- `lake build QOU` succeeds with no new errors.
- The `lean_diagnostic_messages` MCP tool reports clean for the
  edited file.
- The corresponding content-block `.ts` manifest does not need a
  status update (status is derived at build time).
- `lake env lean --run scripts/check_axioms.lean` (if it exists) or
  the axiom report in CI shows the discharged declaration is
  `sorry`-free.

## 6  Coordination with narrative side

If P4.A or P4.B reveals that the canonical instance does NOT
cleanly discharge (e.g. `simp` fails on P4.B because additivity is
defined non-uniformly), the Lean agent should:

1. NOT silently add new typeclass hypotheses to make it work — that
   weakens the narrative claim.
2. Open a counter-finding doc under `docs/audits/` flagging the
   discrepancy and suggesting whether the narrative or the Lean
   should be updated.
3. Coordinate with the narrative agent via `local/coordinate` skill.

If discharge succeeds cleanly, update the §3b-cond status of any
downstream propositions (those whose `uses[]` cone touches the
now-discharged conjecture) — they may upgrade from
`conditional-on-class` to fully provable. The
`conjectural-propagation-audit.ts` script will surface candidates.
