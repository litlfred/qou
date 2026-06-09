# Φ₂ watcher (post-α_eff-refutation) — what remains pinned, what doesn't

**Status:** watcher, NOT a new attack. Tracks PRs #1871 / #1900 + on-main refutation `89616febbe` against the standing scope doc.
**Owner direction:** 2026-06-09 session — user confirmed engagement with Φ₂ despite cluster sprawl. This is a scope-only follow-up (no probe code, no new constraints) per the cluster-sprawl anti-pattern guard.
**Disciplines:** *corpus-grep* (refutation commit `89616febbe` localised), *coordinate* (no file overlap with active PRs — different filename, scope-only doc).

---

## Why this doc exists

The standing scope doc
[`2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md)
opens with a strong bridge claim (§1):

> **`α_eff(u) = Φ(u)`** — PR #1887 supplies the leading symbolic data the recursion
> block is missing: `Φ₁ = √2` (exact), and the open `Φ₂` is the kernel's leading
> coefficient up to `√2`.

This claim was **REFUTED** by `89616febbe` (2026-06-06):

> `cos(α-u/2)(1-u²)` gives `c_2 = −9/8` STRUCTURALLY (α-independent, both anchors),
> vs the proved #1887 `c_2 = −1` (leading phase 3/2 vs √2). No single ladder
> rescale fixes both `c_1` and `c_2` (2 d.o.f. needed, rescale has 1). **The
> on-main `α = (z−1)h/2` is the single-wrap angle of the N=2 APPROXIMATION, NOT
> the proved ladder phase; `Φ₂` does NOT follow from it by reparametrization.**

A future agent reading the standing scope doc may re-derive constraint 4
(`a_1 = √2·Φ₂`) on the now-stale bridge assumption. This watcher doc pins which
constraints from the standing scope survive and which need re-derivation.

## Standing scope doc — constraint survival after `89616febbe`

| # | Constraint | Standing | Post-refutation | Why |
|---|------------|----------|-----------------|-----|
| 1 | Depth ≥ 2 unconditional | ✓ | ✓ holds | Independent of α_eff identification |
| 2 | `a_2 = c_2 = −1` | ✓ | ✓ holds | Depends only on `f_2 = c_2`, not on the cos(Φ) ↔ cos(α_eff) bridge |
| 3 | `a_1 = −c_3` | ✓ | ✓ holds | Same — bar-odd pinning from `f_3 = c_3` |
| **4** | **`a_1 = √2·Φ₂`** | ✓ | **NEEDS RE-DERIVATION** | Used `Φ₁ = √2` from #1887 *and* `c_3 = −Φ₁·Φ₂` from cos(Φ) reframe. The reframe itself is intact (PR #1887); the bridge from α_eff is gone. `a_1 = √2·Φ₂` should still hold via the direct #1887 path (`c_3 = −Φ₁·Φ₂` is the cos(Φ) Taylor expansion, not the α_eff-via-bridge identity), but the **proof** routes through PR #1887 alone, not through α_eff. |
| 5 | `a_1` bar-odd | ✓ | ✓ holds | Inherits c_3's bar-odd parity (PR #1887 wall, NOT the bridge claim) |
| 6 | Constant depth-2 REFUTED | ✓ | ✓ holds | Numerical refutation independent of bridge framing |

**Read:** 5 of 6 constraints survive verbatim. Constraint 4's *conclusion* still
holds; its *justification* is now PR #1887 alone (not PR #1887 + α_eff bridge).

## What's actually open

The Φ₂ value is pinned by the kernel coefficient `a_1`. Post-refutation, the
direct path is:

```
PR #1871's open frontier:
  Hoefsmit-H₃(q) SW-residue kernel derivation
    → R(q, ξ) closed form
      → depth-d recursion coefficients (a_1, a_2, … a_d)
        → a_1 = √2·Φ₂ (constraint 4)
          → Φ₂ value
```

The α_eff bridge was a hypothetical shortcut from PR #1887's leading symbolic
data → kernel coefficients. Without it, the kernel SW-residue derivation is the
unavoidable path.

## Watcher role

This session does NOT open a new probe. It tracks the in-flight work:

- **PR #1871** — canonical depth-`d` q-difference recursion home; the kernel
  `R(q, ξ)` lives here. Watch for kernel closed-form landing.
- **PR #1900** — kernel constraints PR (Lean-verified). Watch for constraint
  set extension beyond the standing 6.
- **PR #1887** — cos(Φ(u)) reframe (already lands `Φ₁ = √2` exact). The post-
  refutation reading: PR #1887's leading-symbolic data is intact; its bridge to
  α_eff was the over-claim.

When the kernel `R(q, ξ)` lands (PR #1871 frontier), the standing scope doc's
constraint 4 becomes actionable: `a_1` from the closed-form `R` directly pins
`Φ₂`. Re-engage at that point with a fresh derivation branch, not before.

## Anti-patterns guarded against

- ❌ **Re-deriving the α_eff bridge.** Refuted by `89616febbe`. The N=2 single-wrap
  α from `(z−1)h/2` is the *approximation*'s phase, not the proved ladder's.
- ❌ **Constant depth-2 kernel attack.** Already refuted (standing constraint 6:
  predicts `c_4 ≈ −3.28`, observed `≈ −0.97`, sign-preserving factor-3 gap).
- ❌ **Symbolic search for `Φ₂` without the SW-residue derivation.** The H₃(q)
  kernel is the *cause* — a numerical fit without the kernel is the 8th-ansatz
  trap (cf. CLAUDE.md "no 7th ansatz" + the `mu-thread-pivot` precedent).
- ❌ **New sibling probe branches.** Opening claude/qbeta-phi2-* probe branches
  while #1871/#1900 are open re-fights a moving target. Defer.

## Cross-references

- Standing scope: [`2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md)
- Refutation commit: `89616febbe`
- Refutation witness: `folio-assistant/computations/qbeta-alpha-eff-ladder-reconciliation-probe.witness.json`
- Refutation scope: [`2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md`](2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md)
- Q_β master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- CLAUDE.md Φ₂ context: §"Q_β c_k is a TRUNCATION ORDER"
