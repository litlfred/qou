# Why the eight item-5 violations are unflagged — instrumented, not inferred

**Date:** 2026-09-04 · **Bean:** `qou-tmmt` · **Producer:**
[`content/pipeline/lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
(`detectSelfAssuming`, line 898)

Eight content blocks were adjudicated by hand as AGENTS.md §3b-cond **item-5**
violations — the conditional class carries the block's own *conclusion* as a
field, and the "theorem" projects it rather than deriving it. None of the eight
produces a candidate from `proof-no-self-assuming-projection`, the criterion
built to catch exactly that.

A prior version of this analysis (bean `qou-tmmt`, commit `f6d02a6123`)
*hypothesised* the mechanism and said so explicitly. This document replaces the
hypothesis with a measurement: `detectSelfAssuming` was temporarily instrumented
to log which gate rejects each declaration, the producer was run once over all
3578 `.lean` files, and the instrumentation was reverted.

## The gate order

```
GATE-1  provable kind, or a Prop-valued `def`        → else reject
GATE-2  body contains any DERIVES token              → reject
GATE-3  body matches one of four projection patterns → else reject
GATE-4  field name escapes CONCLUSION_FIELD          → require
        projectionTypeMatchesConclusion (character identity)
```

## Result — eight files, eight answers

| block | consuming theorem | body | rejected at |
|---|---|---|---|
| `knot-factor-borromean-composite` | `knot_factor_borromean` | `decouple.decouples` | **GATE-4** type-match false |
| `lr-tensor-character-bridge` | `lr_tensor_character_bridge` | `h.bridge ν β` | GATE-3 no pattern |
| `atom-knot-mass-derivation` | `atom_knot_mass_derivation` | `h.atom_knot_mass_derivation cert T_w` | GATE-3 no pattern |
| `markov-trace-recursive-reducer` | `markovTrace_disjointProduct` | `hmT.disjoint_product k n hk α β` | GATE-3 no pattern |
| `rho-k-h3a-refinement` | `rho_k_h3a_refinement` | `inst.identity data Δ partitions` | GATE-3 no pattern |
| `sigma-shell-from-beta-chain-derivation` | `sigma_shell_from_beta_chain` | `inst.identity data` | GATE-3 no pattern |
| `hecke-branching-trace-decomposition` | `branch_trace_character` | `branch_trace lam I Iid Iid` | GATE-3 — **not a projection** |
| `gb-residue-spectral-sum` | `classical_limit_descended` | `rw [S.spectral_decomposition]; simp [hres]` | GATE-2 `rw` — **correctly** |

## The pattern gap is real — and catches none of the eight

`PROJECTION_BODY` and `EXACT_PROJECTION` anchor `\s*$` immediately after the
field name, so they match `inst.identity` and reject `inst.identity data`. The
one applied-projection pattern in the file, `APPLIED_TUPLE_PROJECTION`, requires
the projection to sit inside a `⟨…⟩` tuple. **A bare applied projection — the
commonest way to consume a conditional class whose field takes arguments — has
no pattern at all.**

Closing that is a genuine widening. Measured, by adding an experimental
`APPLIED_PROJECTION` pattern and re-running the full producer:

| | candidates | CRITICAL | EXEMPT |
|---|---|---|---|
| baseline | 78 | 41 | 36 |
| with bare applied-projection pattern | **106** | **68** | 37 |

**+28 candidates, 27 of them CRITICAL — and zero of the eight.** Five of the six
GATE-3 rows move to GATE-4 and are all rejected there. So the pattern gap is
worth closing on its own merits, but it is *not* what hides these eight.

## The mechanism, now measured: GATE-4 cannot see a ∀-quantified field

Six of the eight die at GATE-4 (one unaided, five once the pattern exists).
`projectionTypeMatchesConclusion` compares the field's declared type against the
theorem's conclusion **as normalised character strings**. Worked case,
`sigma-shell-from-beta-chain-derivation.lean`:

```lean
class SigmaShellFromBetaChainDerivation : Prop where
  identity : ∀ (data : SigmaShellAtMagic),
    data.y_target =
      data.C_lambda * data.y_lambda * data.abs_chi / data.abs_tr_M

theorem sigma_shell_from_beta_chain
    [inst : SigmaShellFromBetaChainDerivation] (data : SigmaShellAtMagic) :
    data.y_target =
      data.C_lambda * data.y_lambda * data.abs_chi / data.abs_tr_M :=
  inst.identity data
```

The field and the conclusion are the same proposition; they differ by the
`∀ (data : SigmaShellAtMagic),` prefix. A string comparison can never match
them.

This is not an accident of these files. A §3b-cond class field must be
∀-quantified over the theorem's binders in order to be usable by more than one
theorem — so **the canonical, correctly-written conditional-class shape is
precisely the shape GATE-4 is blind to.** The gate fires only in the degenerate
case where the field is *already* instantiated at the theorem's exact binder
names, which is what the 41 baseline CRITICAL hits are.

## What my earlier hypothesis got right and wrong

It named GATE-4 correctly, and that covers 6 of 8. It named the wrong
sub-mechanism: it said parameter *renaming* defeats the character comparison
(`composite_factor = component_factor ^ k` vs `composite = (1 - h ^ 2) ^ k`).
That is true of `knot-factor-borromean-composite` — the one row that reaches
GATE-4 unaided — and it is not the general case. The general case is
∀-instantiation. So the reading published in `qou-tmmt` was right about the
gate, right for one file, and wrong about the class.

## Consequence: this criterion cannot be repaired with another regex

`detectSelfAssuming` has been narrowed four times in its history; each narrowing
was a regex. Matching a ∀-quantified field against its own instantiation is
elaboration — stripping leading binders, substituting the theorem's binder names
into the field body, then comparing — and a string-level approximation of it
would either miss (as now) or over-match any theorem whose conclusion resembles
a class field. The honest options are:

1. **Close the pattern gap only** (+27 CRITICAL, none of them these eight) and
   accept that ∀-quantified item-5 violations stay agent-adjudicated.
2. **Move the type match to a Lean-side check** — `#check` the field's type at
   the theorem's binders and compare elaborated terms. Correct, and it makes the
   criterion depend on a working Lean build, which CI here does not have.
3. **Leave it**, and record in the review ledger that this criterion has a known
   structural blind spot so a clean run is not read as a clean bill.

Options 1 and 3 are compatible and are what this document recommends
(*judgement, not a finding*): close the pattern gap in its own PR with the 27
new criticals triaged, and record the ∀-blindness so the next agent does not
read `proof-no-self-assuming-projection: 0` on a file as evidence of anything.

## Reproduction

The instrumentation is not committed. To repeat it: log at each early return in
`detectSelfAssuming` (line 898), gate the log on an env var and on the file
basename, run `bun run content/pipeline/lean-vacuity-axiom-audit.ts`, then
`git checkout` the producer **and**
`docs/audits/2026-06-17-lean-vacuity-axiom-audit.json`, which the run rewrites.
