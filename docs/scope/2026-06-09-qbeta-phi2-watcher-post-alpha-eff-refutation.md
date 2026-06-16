# Φ₂ scope sync (post-α_eff-refutation) — what remains pinned, what doesn't

**Status:** post-merge scope sync. All three cited PRs (#1887 / #1871 / #1900) merged to main 2026-06-05/06; this doc is the constraint-survival record for the next agent to read, NOT an active watch.
**Owner direction:** 2026-06-09 session — engagement with Φ₂ work confirmed despite cluster-sprawl risk. This is a scope-only follow-up (no probe code, no new constraints).
**Disciplines:** *corpus-grep* (refutation commit `89616febbe` localised), *coordinate* (no file overlap; new filename).

---

## Why this doc exists

The standing scope doc
[`2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md)
opens with a strong bridge claim (§1):

> **`α_eff(u) = Φ(u)`** — PR #1887 supplies the leading symbolic data the recursion
> block is missing: `Φ₁ = √2` (exact), and the open `Φ₂` is the kernel's leading
> coefficient up to `√2`.

This bridge was **REFUTED** by `89616febbe` (2026-06-06):

> `cos(α-u/2)(1-u²)` gives `c_2 = −9/8` STRUCTURALLY (α-independent, both anchors),
> vs the proved #1887 `c_2 = −1` (leading phase 3/2 vs √2). No single ladder
> rescale fixes both `c_1` and `c_2` (2 d.o.f. needed, rescale has 1). **The
> on-main `α = (z−1)h/2` is the single-wrap angle of the N=2 APPROXIMATION, NOT
> the proved ladder phase; `Φ₂` does NOT follow from it by reparametrization.**

A future agent reading the standing scope doc could re-derive constraint 4
(`a_1 = √2·Φ₂`) on the now-stale bridge assumption. This doc pins which
constraints survive verbatim, which survive with updated justification, and
which (if any) need outright re-derivation.

## Constraint survival after `89616febbe`

| # | Constraint | Standing | Post-refutation | Why |
|---|------------|----------|-----------------|-----|
| 1 | Depth ≥ 2 unconditional | ✓ | ✓ holds | Independent of α_eff identification |
| 2 | `a_2 = c_2 = −1` | ✓ | ✓ holds | Depends only on `f_2 = c_2`, not on the cos(Φ) ↔ cos(α_eff) bridge |
| 3 | `a_1 = −c_3` | ✓ | ✓ holds | Same — bar-odd pinning from `f_3 = c_3` |
| **4** | **`a_1 = √2·Φ₂`** | ✓ | **✓ holds (justification updated)** | Used `Φ₁ = √2` from #1887 *and* `c_3 = −Φ₁·Φ₂` from cos(Φ) reframe. The reframe itself is intact (PR #1887); the bridge from α_eff is gone. The conclusion `a_1 = √2·Φ₂` still holds via the direct #1887 path (`c_3 = −Φ₁·Φ₂` is the cos(Φ) Taylor expansion, not the α_eff-via-bridge identity), but the **proof** routes through PR #1887 alone, not through α_eff. |
| 5 | `a_1` bar-odd | ✓ | ✓ holds | Inherits c_3's bar-odd parity (PR #1887 wall, NOT the bridge claim) |
| 6 | Constant depth-2 REFUTED | ✓ | ✓ holds | Numerical refutation independent of bridge framing |

**Read:** all 6 constraints survive — 5 verbatim, constraint 4 with updated justification (PR #1887 alone, not PR #1887 + α_eff bridge). No conclusion is overturned.

## Cited PR landing status

All three cited PRs are merged. This is not an active "watch landing" task — the work landed, and this doc is the post-merge constraint-survival record.

| PR | Title | Status | Merge date |
|----|-------|--------|------------|
| #1887 | cos(Φ(u)) reframe + Reeb-sinh parity | merged | 2026-06-05 |
| #1871 | Step-9 SW-residue / jet-filtration / q-difference | merged | 2026-06-05 |
| #1900 | Φ₂ formalize-first kernel constraints | merged | 2026-06-06 |

## Open path — the single remaining keystone

The Φ₂ value is pinned by the kernel coefficient `a_1`. Post-refutation, the
direct path is:

```
PR #1871 (merged) — single open keystone:
  conj:qdifference-kernel-prolongation-symbol
    "R(q, ξ) is the jet-prolongation operator symbol"
      → R(q, ξ) closed form (the open keystone)
        → depth-d recursion coefficients (a_1, …, a_d)
          → a_1 = √2·Φ₂ (constraint 4, justification per PR #1887)
            → Φ₂ value
```

The α_eff bridge was a hypothetical shortcut from PR #1887's leading symbolic
data → kernel coefficients. Without it, the kernel SW-residue derivation is the
unavoidable path — and that derivation is exactly PR #1871's
`conj:qdifference-kernel-prolongation-symbol` keystone (the single remaining
(E)=(B) item on PR #1871's P1 scoreboard).

## Re-engage criteria

This session does NOT open a new probe. The next concrete re-engagement is when
the PR #1871 keystone (the jet-prolongation symbol that closes the kernel `R`)
moves from §3b-cond conjecture to derived theorem. At that point:

- `R(q, ξ)` is in closed form
- Constraints 2/3/4 from the standing scope mechanically produce `a_1`
- Constraint 4 pins `Φ₂ = a_1 / √2`
- A fresh derivation branch (NOT a probe) lands the value

## Anti-patterns guarded against

- ❌ **Re-deriving the α_eff bridge.** Refuted by `89616febbe`. The N=2 single-wrap
  α from `(z−1)h/2` is the *approximation*'s phase, not the proved ladder's.
- ❌ **Constant depth-2 kernel attack.** Already refuted (standing constraint 6:
  predicts `c_4 ≈ −3.28`, observed `≈ −0.97`, sign-preserving factor-3 gap).
- ❌ **Symbolic search for `Φ₂` without the SW-residue derivation.** The H₃(q)
  kernel is the *cause*; a numerical fit without the kernel is the
  fit-based-ansatz trap. CLAUDE.md applies the explicit *"do not
  propose a seventh fit-based ansatz"* rule to the Δ_λ gate (six
  closure ansätze refuted on the deuteron); the same discipline
  applies here — symbolic-search fits without a structural derivation
  are forbidden regardless of which ansatz number Φ₂ would be on. See
  the `mu-thread-pivot` precedent for the structural-derivation
  re-engagement pattern.
- ❌ **New sibling `claude/qbeta-phi2-*` probe branches** before the keystone
  derivation lands. Constraints 1–6 are already proved; another constraint PR
  is redundant.

## Cross-references

- Standing scope: [`2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md)
- Refutation commit: `89616febbe`
- Refutation witness: [`computations/qbeta/qbeta-alpha-eff-ladder-reconciliation-probe.witness.json`](../../computations/qbeta/qbeta-alpha-eff-ladder-reconciliation-probe.witness.json)
- Refutation scope: [`2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md`](2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md)
- Q_β master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- CLAUDE.md Φ₂ context: §"Q_β c_k is a TRUNCATION ORDER"
