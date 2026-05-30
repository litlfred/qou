# Coordination ledger — clarabel compute + orbit-trace (2026-05-30)

**Goal:** land the LP/SDP→Clarabel compute work and unblock Tier 1.B
(nucleon-orbit reduction) by proving the orbit-trace identity.

## Scope map (18 open PRs at sweep time)

| PR | Theme | Relation to this track |
|----|-------|------------------------|
| **#1483** (mine) | orbit-trace identity proof | unblocks Tier 1.B; independent of all siblings |
| **#1458** (mine) | clarabel LP/SDP + witness env + scipy pins | **core already merged to `main`**; 4 follow-up commits remain (versions+pin, wheel-ship, moment-SDP wiring, CI) |
| #1062 | docs: Python/Rust library reuse workplan | **thematic overlap** — posted a coordination note (clarabel landed, Tier 1.B unblocked, roadmap correction) |
| #1463–#1480, #1477, #1479, #1475 | α/(4π), Q_β, Bring, meson | **different domain** (α_em / Q_β derivation) — no file or scope overlap; no coordination needed |
| #1467, #1482, #1481, #1476, #1474 | snappy vol, beable remark, dirac cites, bloch-wigner | unrelated |
| #650, #411 | old copilot WIP | stale; out of scope |

## Actions taken

- **Review triage (§5)** — #1483 Gemini review (2 comments): both **accepted**
  and fixed (vacuous `(c,d)`-only test → non-vacuous per-species/interface
  checks + M1 cyclic test; `float` → 50 dps). Consolidated reply posted.
- **Intent (§3)** — one note on the single overlapping sibling (#1062).
- **Watch main (§8)** — `#1458`'s core merged to `main` by another
  session/process; rebased my branch onto it (4 unique commits remain).

## Key finding (escalation-worthy)

The Tier 1.B roadmap states `tr_M(β) = |orbit|·tr_M(rep)`. **This is wrong**
— it's `tr_M(β) = tr_M(rep)` (the canonical word *is* the representative);
`Z!·N!` is reduction-tree dedup, not a trace multiplier. An implementation
following the roadmap literally would produce **wrong masses**. Corrected in
`docs/audits/2026-05-30-orbit-trace-identity-proof.md`.

## Next non-overlapping task

Implement Tier 1.B: `atom_braid_orbit_representative(Z,N)` + memoise
orbit-equivalent reduce states (correct `tr_M(β)=tr_M(rep)` semantics),
cross-check A≤6 before ⁷Li/⁸Be. No sibling is in this scope.
