# Mass-and-Binding-Algorithms appendix — maintenance contract

**Established:** 2026-06-02 via PR #1724
**Scope:** every PR touching mass / binding derivations or compute infra
**Rule reference:** [AGENTS.md §Canonical derivation chain](../../AGENTS.md) (the 🟧 STRICT block immediately after the cheat-sheet paragraph)

## The contract

Any PR that touches:

- **Step 9a** — mass identity `m(K) = m_e · VolDensity(K, q_0)`
- **Step 9b** — per-isotope binding `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ`
- **Step 10** — confinement SDP / canonical `T_w`
- **Step 11** — `Q_β` truncation ladder
- **Sidecar algorithms** — `Δ_λ` closure ansätze, `c_k` truncation ladder, LP/SDP dual-emission contract, witness-JSON pipeline

**must** update the matching `alg:`-block under
[`content/quantum-observable-universe/appendix-mass-binding-algorithms/`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/)
in the **same PR**. The expected diff:

| Field | When to update |
|------|----------------|
| `uses[]` | upstream proposition name or scope changed |
| `computation.script` | canonical script moved or was renamed |
| `computation.witness` | witness JSON path / format changed |
| `.md` *Algorithm* / *Correctness* / *Python API* | signature or correctness conditions changed |

## Enforcement points

| Layer | Where | What it enforces |
|------|-------|------------------|
| Author skill | `.claude/skills/local/compute-author.md §8` | pre-work checklist item |
| Audit skill | `.claude/skills/local/compute-audit.md` verification checklist | item 6: MBA-appendix sync check |
| Proof-editor | `.claude/skills/local/proof-editor.md §coordination rules` | mass/binding/SDP/Q_β findings include MBA-block diff in action plan |
| Coordinate | `.claude/skills/local/coordinate.md §2-bis` | intent comments on sibling PRs name the alg:-block they'll touch |
| Appendix self-doc | `mba-intro.md §Maintenance contract` | reader-visible declaration |
| Top-level | `AGENTS.md §Canonical derivation chain` | 🟧 STRICT block |

## Active sibling PRs (as of 2026-06-02)

Sweep performed via `mcp__github__list_pull_requests` open on 2026-06-02.
Classification per `local/coordinate.md §2`.

### Tier 1 — directly authoring in scope (intent comments posted)

| PR | Scope | alg:-block(s) needed |
|----|-------|----------------------|
| #1727 | Q_β 1ppQ closure | `alg:q-beta-truncation`, `alg:ck-truncation-ladder` |
| #1726 | A≥3 full-order θ_λ → Δ_λ gate | `alg:per-isotope-binding`, `alg:delta-lambda-closure` |
| #1725 | extensive per-bond binding sum | `alg:per-isotope-binding` |
| #1714 | KL recursion S_5/S_6 (Option-E PROBE 4) | `alg:delta-lambda-closure` |
| #1535 | q₀-repin witness regen | `alg:witness-json-pipeline` |
| #1516 | Option-E Phase 2 (Δ_λ) | `alg:delta-lambda-closure` |

### Tier 2 — coordination / audit only (no intent comment; logged for visibility)

| PR | Scope | Why skipped |
|----|-------|-------------|
| #1721 | mass-sweep A≥4 status refresh | coord doc, no code in MBA scope |
| #1556 | m_μ thread supersession audit | audit recommendation only |
| #1718 | m_μ supersession follow-up | close-recommendation PR |
| #1716 | wrapper-tests CI smokes | CI/test fixes only |

### Tier 3 — α_EM derivation tree (separate scope)

The α_EM PRs (#1463, #1477, #1480, #1484, #1487, #1489, #1491, #1495,
#1503, #1505, #1508, #1521, #1523, #1527, #1538, #1549, #1552) are
**not** in direct MBA scope today: α_EM feeds Step 11 (Q_β `c_k`)
indirectly via the Habiro element `[2]_q · (1 − h²α)`, but the chain
step is Q_β, not α_EM itself. When the α_EM Habiro element is wired
into production Q_β compute, the **wiring PR** (not the upstream α_EM
derivation PRs) will trigger the contract. No intent comments on the
α_EM tree at this sweep.

## Authoring status

| Step / Sidecar | alg:-block | Status |
|----------------|------------|--------|
| 1 — categorical action | `alg:categorical-action` | ✅ authored (PR #1724) |
| 2 — GS reduction → Hecke NF | `alg:gs-reduce-to-hecke-nf` | ✅ authored (PR #1724) |
| 3 — Markov trace | `alg:markov-trace` | ✅ authored (template, PR #1724) |
| 4 — Bring χ=−6 brane | `alg:bring-brane` | ✅ authored (PR #1724) |
| 5 — Wedderburn decomp | `alg:wedderburn-decomposition` | ✅ authored (PR #1724) |
| 6 — Frobenius pairing + Ψ=S² | `alg:frobenius-pairing` | ✅ authored (PR #1724) |
| 7 — GB filtration | `alg:gb-filtration` | ✅ authored (PR #1724) |
| 8 — Jet-prefix transport | `alg:jet-prefix-transport` | ✅ authored (PR #1724) |
| 9a — mass identity | `alg:mass-identity` | ✅ authored (PR #1724) |
| 9b — per-isotope binding | `alg:per-isotope-binding` | ✅ authored (PR #1724) |
| 10 — confinement SDP | `alg:confinement-sdp` | ✅ authored (PR #1724) |
| 11 — Q_β truncation | `alg:q-beta-truncation` | ✅ authored (PR #1724) |
| Sidecar — Δ_λ closure | `alg:delta-lambda-closure` | ✅ authored (PR #1724) |
| Sidecar — c_k truncation ladder | `alg:ck-truncation-ladder` | ✅ authored (PR #1724) |
| Sidecar — LP/SDP dual emission | `alg:lp-sdp-dual-emission` | ✅ authored (PR #1724) |
| Sidecar — witness-JSON pipeline | `alg:witness-json-pipeline` | ✅ authored (PR #1724) |

**All 16 blocks authored** (PR #1724 commits 4–9). Sibling PRs
touching any of the listed scopes should now diff their compute
against the matching block in the same PR (or post a follow-up
commit immediately after merge if a sibling lands first).

## Coordination ledger entries

| Date | PR | Action |
|------|----|--------|
| 2026-06-02 | #1724 | contract published; AGENTS.md + 4 skill files updated; ledger created |
| 2026-06-02 | #1727 | intent comment posted (Q_β + c_k) |
| 2026-06-02 | #1726 | intent comment posted (Δ_λ + per-isotope binding) |
| 2026-06-02 | #1725 | intent comment posted (per-isotope binding) |
| 2026-06-02 | #1714 | intent comment posted (Δ_λ via KL probe) |
| 2026-06-02 | #1535 | intent comment posted (witness-JSON pipeline) |
| 2026-06-02 | #1516 | intent comment posted (Δ_λ Option-E) |
