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
| 2026-06-25 | #2812 | coordination ledger (this file) | merged | tiered-status template |
| 2026-06-26 | #2815 | T3 `60iz` Jones-Hopf layer (`JonesViaMarkovTrace`, sorry-free) | merged | Jones-via-Markov-trace + stabilisation-invariance pattern |
| 2026-06-26 | #2817 | `qBracket_add` `[a+b]=q^b[a]+q^{-a}[b]` + if-guard removal | open | `qBracket_add`/`qBracket_eq_formula` (q-Pascal primitive) |
| 2026-06-26 | (markov-trace-wall-unblock) | T3 `60iz` general-`H_n(q)` Jones layer on `IwahoriHeckeAPI`: `jonesOfBraid` + Markov move II (`MarkovTraceLinkInvariance`) | CI-gated | `jonesOfBraid` + `markovTrace_conj_invariant` (move II); element-algebra wall down |

## Tiered status (epic `08a2`)

- **Tier 1 — DONE.** `0bt9` gbDepth · `ckkv` JointGalois→`Equiv.Perm` ·
  `xteb` jet/AlphaK→`QPlancherel` · `m1j2` resolved-by-coordination ·
  `5e79` deferred (its only infra `Cl3Zeta5OrbitSum` is a *different*
  identity → honest-abstract).
- **Tier 2 — DONE.** `5ldf` `qBinom` (q-int/q-factorial pre-existed; only
  the Gaussian-binomial gap filled).
- **Tier 3 — Jones wall LARGELY DOWN (was BLOCKED):**
  - `60iz` **Jones polynomial** — **two layers landed/authored:**
    1. **Hopf layer** (#2815, merged) — `JonesViaMarkovTrace.lean` on the cached
       `Braiding/HnMarkovTrace`: `jonesHopf` (= `tr_M(σ₁²)`),
       `jonesHopf_invariant` (Markov-stabilisation ⇒ link invariant),
       `jonesHopf_canonical`, `jonesHopf_pos`. Sorry-free, in-build.
    2. **General-`H_n(q)` layer** (this PR) — the **owner-directed "unblock the
       Markov-trace wall" (option 3)** found the wall already largely down: a
       sibling landed the abstract **`IwahoriHeckeAPI`** (commits `c2035fb1`/
       `1fe4bc37`) providing the `H_n(q)` *element algebra* (`sigma`,
       `markov_trace`) + `MarkovTraceCyclic` + `MarkovTraceStabilisation` +
       the proved `markovTrace_stab_comm` (= **Markov move I**). On it,
       `MarkovTraceLinkInvariance.lean` adds `jonesOfBraid` (Jones value of an
       **arbitrary** positive braid word = `tr_M(∏σ_{w_k})`) and
       `markovTrace_conj_invariant` (= **Markov move II**, conjugation). Moves
       I+II together ⇒ `tr_M` descends to a link invariant at general `n`.
    - **REMAINING:** wiring `jonesOfBraid` into
      `jet_filtered_knot_factor.jonesQuotient` now needs only the **(Z,N) → quotient-braid-word map** (a *research-grade* identification, not infra) — the
      element-algebra blocker is resolved. Verification of layer 2 is **CI-gated**:
      the `IwahoriHeckeAPI` cone needs `Mathlib.Data.Nat.Dist` /
      `Mathlib.RingTheory.Idempotents` oleans, **absent** from the sandbox's
      partial `lake-cache` (and from `lake-cache/qou-v4-24-0`; 0 mathlib source
      on disk; network blocked) — so authored against the fully-read API,
      verified by CI's full-Mathlib build, not local `lean`-direct.
  - `6chz` **geometric-Langlands** (q-opers/eigensheaves/LocSys/Bun_G) —
    **BLOCKED**: no infra in Mathlib *or* QOU. q-GL family stays
    honestly-abstract §3b.
  - `hhl9` **motivic-Galois** (Goncharov periods) — **BLOCKED**: no infra.
    JointGalois Galois-side stays abstract.

## §7c base-ring follow-up (bean `z1lz`) — currency note (2026-06-26)

Re-checking the four "content-verified genuine leaks" listed in
[`docs/audits/2026-06-25-lean-library-tree-7c-coverage-gap.md` §3](../audits/2026-06-25-lean-library-tree-7c-coverage-gap.md)
against the live tree:

| file | audit flag | live state (2026-06-26) |
|------|-----------|-------------------------|
| `BraidKnot/H3HeckeIdempotents.lean` | ℝ q-integers/eigenvalues | **already generic** `{R} [Field R]` (line 42; §7c docstring present) — **flag STALE, no work** (in-build via `BraidKnot`) |
| `BraidsAndKnots/YLambdaQSchur.lean` | ℝ q-Schur weights | **still ℝ** — true **orphan** (0 Lean importers, 0 block refs ⇒ not in any build ⇒ a §7c fix there is CI-unenforced). Clean but low live value; generalise **+ wire into the `BraidsAndKnots` aggregator** to make its ~30 proved q-Schur theorems CI-enforced. |
| `HeckeAlgebra/MarkovTrace.lean` | `markovTrace_smul (c : ℝ)` | **cascade, not a clean fix** — `markovTrace`'s codomain ℝ is baked into upstream `HeckeAlgebra.Common`; generalising just `c` is incoherent in isolation. |
| `Shared/WedderburnBlockDecompositionContext` | `dim_q`/`w`/`w_tilde : … → ℝ` | **big** — ~15 extenders; structural refactor, defer. |

Net: the highest-value §7c member (the in-build `H3HeckeIdempotents`) is
**already compliant**; the remaining clean target is the `YLambdaQSchur`
orphan (generalise + wire-in).

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

### RESOLVED (2026-06-26 — #2823 + the consolidation/Rogers–Szegő PR)

- **Gap 1 (q-Pascal): CLOSED.** #2823 (merged) proves `qBinom_pascal`
  `[k+m+2 ; k+1]_q = q^{m+1}[k+1+m ; k]_q + q^{-(k+1)}[k+1+m ; k+1]_q` from
  `qBracket_add`.
- **Gap 2 (3 defs): RESOLVED — 2 balanced duplicates + 1 distinct standard.**
  Verified bit-for-bit (numeric + algebra): `GaugeFieldFluidDynamics.qBinomial`
  **≡** the canonical balanced `QPartitionCombinatorics.qBinom` (`qInteger ≡
  qBracket`); `QPochhammer.qBinomial` is the **standard** `(q;q)` form — a
  *different* normalization (`[2;1] = q+q⁻¹` balanced vs `1+q` standard), NOT a
  duplicate. Consolidation = canonical designation on `qBinom`, deprecation note
  on the Gauge duplicate, distinctness note on the Pochhammer standard (doc-only,
  no consumer breakage).
- **Concrete Rogers–Szegő: DEFINED, with the instantiation blocker pinned.**
  `rogersSzego q t n = Σ_k qBinom·tᵏ` + `H_0=1`, `H_1=1+t`,
  `H_2=1+(q+q⁻¹)t+t²` (balanced). It does **NOT** instantiate the standard
  `FollowsRogersSzego` (#2800): the balanced q-Pascal's `q^{±}` factors give a
  *scaled-argument* q-difference relation, not the standard `(1−qⁿ)` 3-term.
  Instantiating the standard class needs the **standard** q-Pascal (for
  `QPochhammer.qBinomial`) — the genuine remaining `5ldf` follow-on.
