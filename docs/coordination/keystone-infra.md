# Coordination ledger — keystone de-abstraction (epic `08a2`)

**Goal:** make the QOU categorical-keystone `§3b` conjecture classes
genuinely faithful by wiring/building real Mathlib + QOU infra, and
honestly bound the research-grade walls. Tiered breakdown in bean epic
`08a2`.

## PR log

| Date | PR | Phase | Status | Cherry-pick |
|------|----|-------|--------|-------------|
| 2026-06-25 | #2779 | triage: 10 spurious-stub deletions + 14 keystone beans | merged | NSym/AppendixSurreals shadow-deletion pattern |
| 2026-06-25 | #2791 | §3b maturation: 3 spurious GS deletions + 11 faithful classes | merged | §3b faithful-class template |
| 2026-06-25 | #2797 | de-abstract 3 → `YoungDiagram`/`InvolutiveStar`/`Filter.Tendsto` | merged | minimal-import `lean`-direct recipe |
| 2026-06-25 | #2801 | `gbDepth` (max `hookLength`) + tiered epic `08a2` | merged | `gbDepth`/`hookLength` on `YoungDiagram` |
| 2026-06-25 | #2803 | `JointGalois`→`Equiv.Perm` + jet/AlphaK→`QPlancherel` | merged | `jetWedderburnWeight`/`_nonneg`, `Equiv.Perm` braid wire |
| 2026-06-25 | #2807 | Gaussian binomial `qBinom` + 4 proved lemmas | merged | `qBinom` + lemmas in `QPartitionCombinatorics` |
| 2026-06-26 | #2817 | `qBracket_add` `[a+b]=q^b[a]+q^{-a}[b]` + if-guard removal | open | `qBracket_add`/`qBracket_eq_formula` (q-Pascal primitive) |

## Tiered status (epic `08a2`)

- **Tier 1 — DONE.** `0bt9` gbDepth · `ckkv` JointGalois→`Equiv.Perm` ·
  `xteb` jet/AlphaK→`QPlancherel` · `m1j2` resolved-by-coordination ·
  `5e79` deferred (its only infra `Cl3Zeta5OrbitSum` is a *different*
  identity → honest-abstract).
- **Tier 2 — DONE.** `5ldf` `qBinom` (q-int/q-factorial pre-existed; only
  the Gaussian-binomial gap filled).
- **Tier 3 — research-grade walls:**
  - `60iz` **Jones polynomial** — *coordination-gated*. The Jones layer is
    `H_n(q)` Markov-trace → knot invariant, complementary to (not
    duplicative of) #2743's `k[S_n]` (q = 1) Wedderburn build. Intent +
    boundary posted on #2743; awaiting scope confirmation before building
    on `Braiding/HnMarkovTrace`. The main-landed `KnotRegistry` /
    photon-as-4-term-Hecke-element work also assembles knot+Hecke building
    blocks.
  - `6chz` **geometric-Langlands** (q-opers/eigensheaves/LocSys/Bun_G) —
    **BLOCKED**: no infra in Mathlib *or* QOU. q-GL family stays
    honestly-abstract §3b.
  - `hhl9` **motivic-Galois** (Goncharov periods) — **BLOCKED**: no infra.
    JointGalois Galois-side stays abstract.

## Coordination findings (2026-06-25)

- **#2743** (`maschke-sn-semisimple`): adds sorry-free `k[S_n]`
  semisimplicity + Wedderburn `∏ Matrix` + `Σ𝔫ᵢ² = n!`
  (`QOU/BraidKnot/{MaschkeSnSemisimple,WedderburnSn}.lean`). HIGH overlap
  with Tier-3 `60iz`; complementary boundary (q = 1 symmetric vs q-deformed
  Hecke). Intent posted (`#2743` issuecomment-4805045194); `60iz` build
  held pending their scope answer.
- **#2795** (`sw-lambda-jet-prolongation`): name-collision only — "jet" =
  Seiberg–Witten λ differential prolongation (z2bn Lever-1), not the
  Hecke jet-level of `jet_filtered_knot_factor`. Independent; no file
  overlap; no comment posted.
- **main** `KnotRegistry` / photon-as-4-term-Hecke-element / 6-dim operator
  basis (72c2308b, 6ecfd1a2): knot+Hecke infra landing — Tier-3 Jones
  building blocks; fold in if/when `60iz` proceeds.

## Coordination findings (2026-06-26, `5ldf` follow-on — #2817)

- **`5ldf` was marked Tier-2 DONE, but two gaps remained** (not a reframing
  of #2807 — a follow-on):
  1. **No q-Pascal primitive.** `qBinom` shipped with only `zero`/`self`/
     `symm`/`pos`; the recurrence `[n+1;k] = …` (needed for the Rogers–Szegő /
     continuous q-Hermite three-term recurrence, the concrete instantiation of
     `QOU.Mass.BindingQHermiteOscillator.FollowsRogersSzego` from #2800) was
     unreachable. #2817 adds the **balanced addition identity**
     `qBracket_add : [a+b]_q = q^b·[a]_q + q^{-a}·[b]_q` (the relation behind
     q-Pascal) + `qBracket_eq_formula` (if-guard removal). lean-direct exit 0.
  2. **Three parallel q-binomial defs still live** — a genuine consolidation
     gap (#2807's "no duplication" only audited its own module):
     `QPartitionCombinatorics.qBinom (q n k)` (canonical),
     `Machinery/QPochhammer.qBinomial (n k q)`,
     `GaugeFieldFluidDynamics.qBinomial (q n k)`. Low-priority but real
     `5ldf` residue: pick the `QPartitionCombinatorics` canonical and
     `uses[]`/alias the other two (separate follow-on, not in #2817 scope).
- **No open sibling overlaps #2817** (its predecessor #2807 is merged; nobody
  else is touching `QPartitionCombinatorics`'s `qBracket`). No intent comments
  posted — clean follow-on infra.
