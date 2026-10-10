# km42 — m_can brane-tower dashboard "fix divergent impl": scoping (GATED)

**Bean:** `km42` — *Dashboard m_can brane tower: level-0 E0·Δtr + convergent higher
orders (fix divergent impl).*
**Verdict:** the "divergent impl" is the **owner-gated T2/T3 brane-tower trace-invariance
pathology**, not a clean dashboard bug. Making the higher orders "convergent" **is** the
open binding-closure derivation question. Parked; do **not** wire the pathological terms.
A narrow *display-only* robustness fix is the only non-gated slice (described below) and is
itself optional.

## Why this is gated, not a bug-fix

The m_can brane-tower mass is `m(ρ) = T1 + T2 + T3 + …`:

- **T1** (`|tr_M|`, level-0 `E0·Δtr`) is the convergent, canonical, already-wired part.
- **T2/T3** (the brane tower — *dominant*) **diverge at q₀**: the archimedean `Φ_q` is **not
  Markov-invariant**, so tiny p/n asymmetries amplify ~10⁵× (e.g. T−³He ≈ −737 MeV vs CODATA
  +0.019 MeV). All brane-tower compute lives in `fsh-guts/deprecated/computations/` for this reason.

"Fix the divergent impl" = make T2/T3 converge = find a **trace-invariant reformulation**.
That is the **open derivation question**, pinned in
[`docs/audits/2026-06-26-t2t3-trace-invariance-status-synthesis.md`](2026-06-26-t2t3-trace-invariance-status-synthesis.md):
*"Nothing wired … the genuine open question is structural, not numerical — the binding
prefactor `α_M` derived-from-substrate (rather than calibrated)."* It is the binding-sector
frontier (beans `z2bn`/`w5tg`/`thb7`), under the **standing "do not wire the pathological
Φ_q T2/T3 into the solver"** directive (bean `adhb` / PR #2846) and the **Subgoal-2 decline**
(2026-05-08; narrow reversal only for the s5-so3 keystone). Per `AGENTS.md §Precision goals`.

## Safe vs gated slice

| Slice | Status |
|-------|--------|
| Display **level-0 `E0·Δtr` (T1)** only, and **label** the higher-order brane-tower terms as *"divergent — T2/T3 trace-invariance open (gated)"* instead of emitting the pathological −737 MeV-class values | **safe** (display-only; no new derivation, no wiring of Φ_q T2/T3) — optional dashboard-robustness fix |
| Make the higher orders **actually converge** (the convergent-tower reformulation / `α_M` substrate derivation) | **GATED** — open derivation question; needs explicit owner sign-off; do not attempt without it |

## Recommendation

Keep `km42` **parked** as gated. If the owner wants the dashboard to stop showing divergent
garbage in the interim, re-scope `km42` to the **display-only** slice above (truncate to T1 +
a "higher orders divergent/gated" annotation) — explicitly **not** a fix of the underlying
divergence. The convergent-higher-orders derivation stays gated with the rest of the
binding-closure frontier.

This is a scoping record only — no code, no content, no witness, no q₀ change.
