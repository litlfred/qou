# Bean `zslh` is grep-inflated — mass-theory placeholder re-scope (2026-06-28)

**Bean:** `zslh` ("Resolve 103 placeholders/TODOs in qou/mass-theory")
**Follow-on to:** [`2026-06-26-lean-placeholder-bean-grep-inflation.md`](2026-06-26-lean-placeholder-bean-grep-inflation.md)
(which already names `zslh` in its inflated-bean list but carries no
mass-theory row). This doc adds the verified mass-theory row.

## Finding

`zslh`'s "103 placeholders/TODOs" is a naive
`grep -c 'sorry|TODO|placeholder|FIXME'` count over
`content/quantum-observable-universe/mass-theory/*.lean`. As established in
the 2026-06-26 audit for the sibling beans (`1osq`, `ekb8`, `b3pe`, `95jh`,
…), that count matches four classes of **non-actionable** strings:
`sorry-free` docstrings, comment-prose describing the §3b pattern,
`-- TODO upstream:` Mathlib-upstreaming markers, and **legitimate §3b
open-conjecture `sorry`s** (which per [`AGENTS.md §3b`](../../AGENTS.md)
*represent the conjecture* and must **not** be discharged).

## Verified counts (refined grep + hand-read, 2026-06-28)

| dir | bean | bean-claimed | naive grep | refined sorry | hand-read truth |
|-----|------|--------------|-----------|---------------|-----------------|
| `mass-theory` | `zslh` | 103 | 226 | 24 | **≈ 0 genuine free-standing TODO/FIXME**; the 24 refined are §3b conjecture-instances / honest out-of-scope research stubs |

- **233** `.lean` files in `mass-theory/`.
- **Refined sorry** = `(:= sorry | := by sorry | ^\s*sorry$ | <;> sorry)`
  minus `sorry-free | sorries | 'sorry' | "sorry" | comment lines` → **24**.
- **Zero** genuine `-- TODO` / `-- FIXME` comments (the actionable kind).
- **65** files use the §3b conditional-class pattern (the single cited
  `sorry` per chain *is* the conjecture — discharging it is wrong).
- **8** files carry honest, explicitly-flagged out-of-scope research
  placeholders.

## Why the 24 refined `sorry`s are not a fill-queue

Spot-reads of the representative cases:

- **`terminal-resolution.lean`** — each `qou_*_MeV` is a CODATA-pinned
  **placeholder** for the topological mass formula at `q₀`. Its honesty
  note states the genuine `Real.rpow` Skein evaluation is the
  framework's *declined* substrate-`q₀` problem (AGENTS.md "Precision
  goals" Subgoal-2, out of scope) and warns: *"do NOT fabricate a
  derivation by editing the literals."* Filling it is **forbidden**, not
  pending.
- **`conj-rho-prefactor-structural.lean`** — `q_int_placeholder` /
  `rho_eq_qdim_placeholder` are the §3b-cond conditional-class scaffolding
  (correct-at-the-classical-limit, conjectural for general `q`). Sanctioned
  pattern, not a stub.
- **`alpha-k-categorical-closure.lean`** — the `instance … := sorry` is
  explicitly *"the only `sorry` permitted in the dependency chain"* (the
  conjecture itself), per the file's own §3b-cond docstring.

A residual few (e.g. a `1 = 1 := sorry`, a `∃ v, True := sorry`) are
**lean-vacuity-audit** candidates, not placeholder-fill work — they belong
to the vacuity-review ledger
([`lean-vacuity-review-ledger.json`](lean-vacuity-review-ledger.json)),
not to `zslh`.

## Recommendation (owner closes beans per AGENTS.md §4a)

- **Re-scope `zslh`** to its verified count — exactly as `95jh`, `b3pe`,
  `ekb8` were re-scoped: *"track N intentional §3b / out-of-scope markers;
  ≈ 0 actionable; §3b open-conjecture `sorry`s excluded."* The "103" is
  not a remediation backlog.
- **Do not drain** the §3b open-conjecture `sorry`s — per §3b they are the
  honest representation of open conjectures; discharging them by editing
  would be a correctness regression.
- Any genuinely-vacuous residual is the **lean-vacuity audit's** scope, not
  `zslh`'s.

## Why this matters

This is the fourth-plus "stale/misclassified Lean placeholder bean" in the
`*-placeholder` family. The fix is a `sorry`-aware generator (exclude
`sorry-free`, comment lines, and §3b `ctx.holds` / conditional-class
instances) — or, better, the authoritative `lean`-direct *"declaration uses
'sorry'"* warning count — so future placeholder beans track actionable work
rather than sanctioned scaffolding.
