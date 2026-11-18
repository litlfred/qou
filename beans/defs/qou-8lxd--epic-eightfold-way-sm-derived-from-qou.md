---
# qou-8lxd
title: 'EPIC: eightfold way / SM derived from QOU'
status: in-progress
type: epic
priority: high
tags:
    - 8f-index
created_at: 2026-08-03T23:27:15Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-0uga
---

## Reorganisation 2026-10-04

Now the epic for P4.SM under SM / eightfold way and physics scope.

---

## Index — written 2026-10-10

Entry point for the P4.SM arc. This body was **empty from 2026-08-03 to
2026-10-10**: the 2026-10-04 reorg parented 149 beans here and left no index, so
the arc had 117 open children and no way in. Parent `qou-0uga`; sibling
`qou-ddmn` (physics-claim scope audits).

**149 children — 117 todo, 30 completed, 2 scrapped.** Every one of the 117 is
now tagged with exactly one `8f-*` front, so each front is a single query:

```
beans list --tag 8f-mass --ready        # startable items, one front
beans list --parent qou-8lxd --ready    # everything startable
```

`--ready` excludes blocked and in-progress, so it *is* the chip-away list.

### What this epic is, and is not

**Is:** deriving the classical eightfold way (flavour `SU(3)` multiplets, GMO,
the decuplet relations, the octet/decuplet decompositions) and the
Standard-Model parameter set from QOU's categorical substrate.

**Is not:** a claim that any of it is derived. Per PR #4640's honesty pass, most
of the chapter's representation theory is tier **standard** — correct and
correctly applied, and true of *any* `SU(3)`, so **not evidence for the
framework**. Keep that register when adding to any front.

### Fronts

**🛑 The `ready` column is a DATED SNAPSHOT, not a maintained number.
Re-measure; do not quote.** The command, with the one trap that matters:

```sh
beans list --tag 8f-mass --ready | grep -oE 'qou-[a-z0-9-]+' | sort -u \
  | grep -vxE 'qou-0uga|qou-8lxd' | wc -l
```

The `[a-z0-9-]+` is load-bearing. **Not every bean ID in this arc is four
characters** — the atomicity chain is `qou-atsd-t0`, `qou-atsd-t2`,
`qou-atsd-t3`, `qou-atsd-t4`, `qou-atsd-t6-premise-triage`. A `qou-[a-z0-9]{4}`
pattern truncates all five to `qou-atsd` and `sort -u` then reports the front as
**1 of 5**. Measured, by making that exact mistake while writing this table.
The two excluded IDs are the milestone and this epic, which print as tree rows.

| tag | ready (2026-10-10, after the `8f-lean` triage) | front |
|---|---:|---|
| `8f-flavour` | 14 | Flavour `SU(3)`, `N = 3`, the flavour Cartan (G1-opt1..4), Bring structures. **The arc's gate.** |
| `8f-lean` | 7 | Lean scaffolds owed, vacuity/self-assuming projections, opaque carriers, float64 in `close_321_weinberg_gap.py`. |
| `8f-colour` | 15 | Colour `SU(3)` action and its construction routes (sub-epic `qou-8p1x`). |
| `8f-mass` | 10 | SM mass gaps: `m_u/m_d`, `m_s/m_c`, `m_b/m_t`, `m_tau`, neutrinos, `m_H`, the lepton tower. |
| `8f-ew` | 9 | Electroweak: `sin^2 theta_W`, Weinberg angle, vev `v`, Higgs mechanism, hypercharge `Y = B - L`, CKM + PMNS. |
| `8f-gen` | 8 | Three generations, chirality grading, what excludes `T(2,9)`. **FULLY TRIAGED 2026-10-10: 8 of 8 are `8f-open` research — 0 mechanical, 0 already-done.** All eight bodies read; one was title-only (`xtcl`, the front's keystone) and three were stale against a *sibling bean's* recorded result. |
| `8f-qcd` | 8 | Gluon flux tube (G2-opt1..3), lattice QCD from QOU, partition-function unification. |
| `8f-lit` | 7 | Literature + the four P4.SM queues (cite / cross-check / prove-lean / remark-interpreting). |
| `8f-tseries` | 5 | `T2`–`T6` derivation spine: hypercharge via ribbon twist, twist multisets, root-of-unity freeze-out, no-free-parameter certificate. **FULLY TRIAGED 2026-10-10: 5 of 5 are `8f-open` research — 0 mechanical, 0 already-done.** All five bodies read; two were title-only or stale-bodied and now carry their measurement. |
| `8f-atomicity` | 5 | The `qou-atsd` T0-T6 chain (`dim V = 2` crux, `Sp` rank, the hard Tannakian Mathlib gap). |
| `8f-arch` | 4 | Chapter architecture. Ch. `eightfold-way` **exists and is wired**; the restructure is owner-gated. |
| `8f-decide` | 11 | Owner decisions. **Grew 4 -> 10 on 2026-10-10** as triage moved owner-gated items out of `8f-lean`. Mostly *prepared* one-liners now: a drafted replacement, options with cost, a recommendation and a default. Cheapest front to shrink, and it shrinks by answering, not by working. |
| `8f-obs` | 3 | Observational cross-checks (kilonova Sr II, Reticulum II, actinide cosmochronometry). |

### Suggested order

**Re-ordered 2026-10-10 after triaging one front, and the re-order IS the
finding.** The original order led with `8f-lean` on the claim that it was
"mechanical, no research risk". Measured over **9** bodies read: **2** were
mechanical repairs (`qou-t88s`, `qou-8b0q`), **2** were already done and only
needed verifying and closing (`qou-an6y`, `qou-mjt3`), **3** became owner
decisions (`qou-skgn`, `qou-rydq`, and `qou-6766`'s four residuals), and **2**
are open Lean formalisation. So `8f-lean` is not the cheap front; triaging it
*produced* the cheap front.

1. **`8f-decide` — 10 items, and this is now the cheapest real shrink.** It
   shrinks by the owner *answering*, not by an agent working. Six of the ten are
   **prepared**: each carries a drafted replacement or a named option set, cost
   and risk per option, a recommendation marked as the agent's judgement, and an
   explicit default-if-unanswered. Four of those six
   (`qou-opjb`, `qou-dids`, `qou-652e`, `qou-j98x`) are one-line content calls
   split out of `qou-6766` and can be cleared in a single message. One of the
   ten, `qou-j3w6`, gates `8f-flavour` — ask before doing flavour work.
2. **`8f-lit`** — 7 items, mostly the four P4.SM queues; drains fast and unblocks
   citations other fronts need. **Untriaged**: the measured lesson above applies,
   read each body first.
3. **`8f-lean` — 7 items, and it is now FULLY TRIAGED. 2 are actionable; 5 are
   open research.** All 14 original bodies have been read. The actionable two:

   - **`qou-nmib`** — formalise the `Δ(1232)` isospin quartet as `Sym³` of the
     existing `N = 2` fundamental, `dim C(4,3) = 4`. A finite computation,
     **ungated by `qou-j3w6`** (the gate bites only on the full decuplet, which
     needs `N = 3` because `Ω⁻` is strange — split out as `qou-3oi0`). This is
     the one genuinely startable Lean item on the front.
   - **`qou-x0th`** — probably a *verify-and-close*: check whether the "Wigner
     `SU(2)` gap" is already carried by two existing sorry-free files
     (`WignerSU4FromSpinIsospin.lean`, `WignerSU4RowBoundInactive.lean`). Read
     before writing Lean.

   The 5 tagged `8f-open` are real formalisation research and should not be
   picked up expecting a repair:

   | bean | why it is open |
   |---|---|
   | `qou-0tiw` | needs a circularity broken — the hypothesis would need the conclusion |
   | `qou-006b` | needs a conjecture class restructured, and warns that a green file would mean nothing either way |
   | `qou-ibck` | needs a `Fin`-enumeration of `p(n)` partitions, or a route that is still sorry-blocked |
   | `qou-apma` | the clean half is **proved** (`VirtualProjection.lean`, `pi0_eq_zero_iff`); the residual needs non-normal spectral theory, shared with `qou-ud3o` |
   | `qou-d8de` | **wall W1** — construct `D_q`. Actively maintained; ends on "`D_q` is not constructed". Downstream home of the `qou-an6y` prune: *do not fit the weights to the recurrence, a fit always exists.* |

   ```
   beans list --tag 8f-lean --ready                    # 7
   beans list --tag 8f-lean --no-tag 8f-open --ready   # 2 — actionable
   beans list --tag 8f-open -q                         # 5 — open research
   ```
4. ~~**`8f-tseries`** then~~ **`8f-colour`** — ~~the research spine and~~ the one
   front where several routes are already excluded, so the survivors are known.
   **`8f-tseries` is now FULLY TRIAGED and is NOT a next step: 5 of 5 are
   `8f-open` research, 0 mechanical, 0 already-done** (2026-10-10). Struck
   through rather than rewritten, because it was recommended here.
5. **`8f-mass` / `8f-ew` / `8f-gen` / `8f-qcd`** — the 26-parameter gap map. Most
   are blocked on `8f-flavour` or `8f-colour` landing first; read the individual
   bean before starting, several say so explicitly.

> **Do not call any front "mechanical" before triaging it — including on my own
> recommendation above.** `8f-lean` is the one front triaged to completion: of
> its **14** bodies, **2** were the mechanical repairs the tag implied, 2 were
> already done, 2 are now actionable items of a different shape, 5 are open
> research, and 3 became owner decisions. Triage is cheap (read the body, ~1-3k
> chars) and a tag is a title's guess; the claim "this front is mechanical" has
> now been wrong once in this index and must be earned per front, not inherited.

> **Second and THIRD data points, and they CONFIRM this index's own prediction (2026-10-10).**
> `8f-tseries` is the second front triaged to completion, and the contrast with
> `8f-lean` is the whole finding:
>
> | front | named by | bodies | mechanical | already done | owner | open research |
> |---|---|---:|---:|---:|---:|---:|
> | `8f-lean` | *kind of work* | 14 | 2 | 2 | 3 | 5 (+2 rescoped) |
> | `8f-tseries` | *subject matter* | 5 | **0** | **0** | 0 | **5** |
> | `8f-gen` | *subject matter* | 8 | **0** | **0** | 0 | **8** |
>
> That is what §"the front tags came from titles" predicted — fronts named for
> **what kind of work it is** move; fronts named for **subject matter** do not,
> because subject matter says nothing about tractability. The prediction is now
> measured rather than asserted, and the practical consequence is: **do not
> expect a subject-matter front to yield closures.** Triage it anyway — it is
> cheap and it produced four body corrections here — but budget it as
> *scoping*, not as *draining*.
>
> **What the `8f-tseries` triage produced instead of closures**, all four worth
> more than a status change:
>
> - **`qou-s16e` (T5)** — its "half-built" framing understated the state (the
>   certificate is BUILT: 5 entry points, 17 modules, 0 unresolved, 4 of 5 at
>   **0 untraceable**, the 5th red by design) *and* its stated target is the
>   wrong target: `predict(obs)` is a **data lookup**, not a closed term, so a
>   literal-classifying audit cannot speak to it. Now detector-blindness
>   taxonomy **row 56** (was 55; renumbered 2026-10-10 when main appended its own 55th), with a committed guard. The trap is recorded: adding
>   `qou-mass` as a sixth entry point would print a clean `0` that **means
>   nothing**, because the path does no arithmetic at any closure size.
> - **`qou-db6w`** — title-only (294 chars) since 2026-07-31, which is why it
>   was never claimable. Body written; it is the **gap statement** whose one
>   candidate route is `qou-qhrw`, and nothing in the corpus recorded that.
>   Now `blocked-by`.
> - **`qou-qvpl` (T2) / `qou-kebu` (T2b)** — T2's body lists T2b's battery under
>   "BATTERY PASSED", which reads as T2b being **done**. It is not: T2b's own
>   body states the gap (*"proves CONSISTENCY … does NOT DERIVE"*). A reader
>   going by T2 alone would close T2b wrongly. Guarded from both sides, and the
>   dependency (`kebu` → `qvpl` → `htw2`) is now in the graph rather than in
>   prose.

> **🛑 `8f-gen`, and the pattern across BOTH subject-matter fronts is worth more
> than either front (2026-10-10).** 13 bodies read across `8f-tseries` and
> `8f-gen`; **0 closeable**, and **5 of the 13 were stale against a SIBLING
> BEAN's recorded result** — not against the corpus, against another bean:
>
> | bean | what a sibling had already settled |
> |---|---|
> | `qou-kebu` (T2b) | `qou-qvpl` lists its battery as "BATTERY PASSED", which reads as done; T2b's own body states the gap |
> | `qou-qvpl` (T2) | the converse — its own heading is what would mislead a reader about T2b |
> | `qou-jk6g` (V3) | its recorded blocker (*"BLOCKED BY V2: if L needs framing while Y needs framing-independence"*) was **dissolved** by `qou-h0zz` on 2026-08-10, in as many words — and `h0zz` also supplies V3's own ask, `L(β) = sign(writhe β)`, which is in the Lean |
> | `qou-t0hl` (V1) | its chain uses **`Y`**; `h0zz` establishes the separating datum is **`B` (μ̄₁₂₃), not `Y`** |
> | `qou-x4qm` | its roast says *"two filters, two counts"*; there are **three**, returning 4 / 3 / 2 |
>
> **The reusable rule: before working a bean, read the beans it cites AND the
> beans that cite it.** AGENTS.md's corpus-grep path 6 says to grep `beans/defs/`
> before declaring something open — this is the same discipline pointed inward,
> and nothing prompts it. Three of the five above were resolved by **one** bean
> (`qou-h0zz`) whose result none of them had absorbed.
>
> **And `8f-gen` has ONE ROOT BLOCKER, shared with `8f-tseries`.** There is **no
> per-chiral-fermion braid word** in the corpus (`htw2`; `qou-h0zz` caveat 2:
> *"The QUARK braid word is still NOT in the corpus; `w = 0` is ASSUMED …
> **Every quark row rests on it**"*). That one missing object blocks `t0hl`,
> `jk6g`, `h0zz` and `wqto`'s chirality grading on this front, and `kebu` plus
> `qvpl`'s sub-item A on `8f-tseries`. **It is the highest-leverage item in
> either front** — five beans across two fronts wait on one construction.
>
> **🛑 CORRECTED the same day — FOUR candidates, and the fourth reframes it.**
> The paragraph below says "three filters" and that is my own undercount. There
> is a fourth, `ex:archimedean-yekutieli`: generations as the three
> complex-conjugate **pairs of branch points** of the Bring fibration (the six
> points are listed numerically in `bring-fibre-qhalf-figure.md`), giving **3**.
>
> **It is not a fourth column — it counts a different object.** Candidates 1-3
> count *admissible torus-knot indices* (4, 3, 2); candidate 4 counts
> *branch-point orbits* (3). So the corpus holds **two independent countings of
> one physical quantity**, and that makes the open problem nameable where "three
> filters disagree" did not:
>
> > Construct the bijection between the branch-point pairs and the admissible
> > `T(2,n)`, or prove it cannot exist. Under candidate 1 it cannot (`4 ≠ 3`);
> > under candidate 3 it cannot (`2 ≠ 3`) — so at least one of the two
> > identifications is wrong.
>
> Two further things the paragraph below misses. **Candidate 3's exclusion is by
> LAGRANGE** — `|S₅| = 120 = 2³·3·5`, so `7 ∤ 120` and `9 ∤ 120`, i.e. no group
> of order 120 has an element of those orders; the corpus argues by inspecting
> the cycle-type table, and Lagrange is stronger and cannot go stale. And **the
> physical consequence**: `τ = T(2,7)`, so reading candidate 3 as *the*
> criterion **excludes the tau**, the top and the bottom.
>
> **🟧 OWNER DECISION 2026-10-10: option 1 — record as an open problem, adopt no
> criterion.** Enacted as
> `docs/audits/2026-10-10-generation-count-two-independent-countings.md`. No
> block edited, no number moved. The other two dispositions stay open.
>
> **The keystone, newly bodied: `qou-xtcl` and the THREE filters** (undercount —
> read the correction above first)**.** It was
> title-only (654 chars, body empty) and `qou-x4qm` is `blocked-by` it. The
> corpus carries three filters on the odd windings and they give three counts —
> Seifert genus `≤ 4` → `{3,5,7,9}` (**four**, and `torus_knot_genus_four_unique`
> is a real `interval_cases` theorem); continuant divisibility → `{3,5,7}`
> (**three**, on a criterion `qou-a5os` already established is unrelated to
> generation counting); `S₅`-equivariant embedding → `{3,5}` (**two**).
> **Filters 1 and 3 are two properties of the SAME object** — `Σ₄` is genus 4
> *and* has `Aut = S₅`, stated in one sentence of `brings-surface-def.md` — so
> the disagreement is inside one geometric object rather than between rival
> criteria, and **three generations is produced by neither of them.** Reading
> filter 3 as *the* criterion predicts **two** generations, which would refute a
> headline claim; nobody has written that down. Also recorded there: the `S₅`
> block's Lean is `trivial`/1-step by the corpus's own
> `docs/audits/lean-triviality.json` (2026-08-07), so the `{3,5}` count rests on
> the narrative argument, which **is** sound — and the removal of the
> `(odd primes)` parenthesis (Q1-D, this PR) matters here, because primality was
> doing filter 2's work in a parenthesis, `9 = 3²` being the only non-prime in
> the set.

> **A title-only bean is not a small bean — it is an unclaimable one.**
> `8f-lean` had three (`xlw1` at priority **high**, empty five weeks; `nmib`,
> twelve weeks; `eo5q`, ten) and now has none. Each took one measurement pass
> and each turned out to be a *different kind of item* than its title implied —
> `xlw1` a third argument about a sentence `rydq` already owns, `nmib` two
> halves with different dimensional requirements, `eo5q` an indexing shift plus
> two further defects. Give a new bean a body (what is wrong, where, measured;
> options with cost; a default) or it will sit, exactly as `qou-6766` did for
> eight weeks.

## The gate, stated once

**`qou-j3w6` — owner decision, asked 2026-09-03, dismissed, still open.** Every
single-fibre route to flavour `SU(3)` is closed by a proved invariant. The
missing object needs `Λ³W = 1`, which condition 5 (`Λ²V = 1`, `N = 2`) forbids
for `V`. Options A (keep `N = 2`, add a second fundamental `W` — recommended in
the bean) / B (weaken to epimorphism — breaks the convention-D forcing chain, 10
consumers) / C (top-power `Λ^N V`, forces the multi-universe picture) / D
(nothing). Frame: `docs/audits/2026-09-03-eightfold-axiom-5-decision-frame.md`.

**Default if unanswered: D. Nothing changes and `8f-flavour` stays parked.**

Why it binds: `QOU/Eightfold/RowCapObstruction.lean` proves sorry-free that at
`N = 2` the alternating channel `dim V_(1³) = C(N,3)` **vanishes** — no singlet,
hence no `8 ⊕ 1` and no `η′`, for **any** `q`. Scope-(b), invariant cited
(the Schur-Weyl row cap). It excludes `N = 2` from *hosting* the decomposition;
it says nothing against a route that produces `N = 3`.

### Verified state of the chapter (2026-10-10, post-rename paths)

`folio/quantum-observable-universe/eightfold-way/` — **16 blocks, 9 sections**,
wired at `quantum-observable-universe.ts:97`. All of §1–§8 exist, which is why
five Phase beans (`lsij`, `8mgu`, `wvao`, `o7o9`, `v2aa`) were closed in this
pass with their evidence appended.

Still in place and **owner-gated**, not undone: `appendix-standard-model/` and
`brings-surface/` (**181** blocks). PR #5023 states the 8 → 4 restructure
"needs author sign-off", so `qou-akee` and `qou-ywsk` are deferred.

### 🛑 The front tags were assigned from TITLES — treat them as a routing hint, not a verdict

All 117 were classified by reading **titles**, not bodies. That is what made a
one-pass reorganisation possible, and it has a measured error rate above zero:
the **first body actually read afterwards produced a re-filing.** `qou-skgn`
("prop:skein-generation is a self-assuming projection") was tagged `8f-lean`
because the title reads like a Lean defect to repair; its body states that
choosing among its three dispositions *"is the author's call, not a mechanical
repair"*, so it belongs in `8f-decide` and was making the mechanical front look
one item larger than it is.

**Re-measured 2026-10-10 after reading 9 of the 14 `8f-lean` bodies — the rate
is 3 of 9, not 1 of 14.** The three re-filings to `8f-decide`:

| bean | title reads as | body says |
|---|---|---|
| `qou-skgn` | a Lean self-assuming projection to repair | *"the author's call, not a mechanical repair"* |
| `qou-rydq` | a **FINDING**, i.e. measurement complete | the Lean landed; *"Awaiting the owner's pick"* on a corpus rewording |
| `qou-6766` | one review item | **seven** findings packed into the title; 4 residuals are owner calls, now `qou-opjb` / `qou-dids` / `qou-652e` / `qou-j98x` |

A grep over bodies for owner-gate language found only `skgn`, plus one false
positive (`qou-an6y` — its "owner decision 3" is the stalled-claim-reset policy,
not a gate on its content). **It missed both `rydq` and `6766`**, because
`rydq`'s gate language is the phrase *"Awaiting the owner's pick"* in its last
line and `6766` had no body at all. So the shape is not greppable: the only
reliable detector is reading the body.

**What to do with that:** before starting an item, read its body and re-tag if
the title misled. A front count is the size of a *queue to triage*, not a count
of confirmed mechanical work. Expect the research fronts
(`8f-flavour`, `8f-colour`, `8f-tseries`) to be more reliable, since those
titles describe subject matter; expect the disposition-flavoured fronts
(`8f-lean`, `8f-decide`) to be the ones that move, since those titles describe
*what kind of work it is* — which is exactly the thing a title gets wrong.

### Hygiene rules for this arc

- **Tag every new bean** with its `8f-*` front and set `parent: qou-8lxd`.
  Untagged beans are invisible: a title-grep for `eightfold|8-fold` finds 27 of
  these 149, and the seven beans PR #4640 spun out (`8pl1`, `8pl2`, `8pl3`,
  `mrel`, `sym2`, `sgd1`, `tup9`) contain neither word. **Never scope this arc
  by title-grep.**
- **`beans` rejects a `parent` on a `milestone`** — which is why the 2026-10-04
  reorg retyped `qou-vwu9` and `qou-20sx` from `milestone`/`epic` to `feature`:
  that is the move that let them be parented here. If you need a grouping node
  under this epic, make it a `feature`, not a `milestone`. (An earlier draft of
  this index asserted `vwu9` was "detached by schema"; it is not — it carries
  `type: feature`, `parent: qou-8lxd`. Corrected before this body shipped.)
- **Session beans are ephemeral.** Four (`a0gr`, `cl94`, `1qug`, `nc56`) sat
  `in-progress` for 5-9 weeks, one of them holding `qou-d7h1` — the arc's
  largest open item — as a child. All four are now closed.
- **Re-verify on `folio/`, not `content/`.** The tree was renamed
  (`content/` → `folio/`, `.beans/` → `beans/defs/`). An earlier pass of this
  cleanup measured a checkout 1245 commits behind and got two numbers wrong in
  opposite directions: `brings-surface` read 176 (is **181**) and `uploads/`
  read 23 (is **10**, i.e. the ingest queue *drained*, it did not grow).
- Per AGENTS.md rule 13a, **nothing whose subject is an open conjecture was
  closed here.** The five closures are all mechanical, each with its evidence.


---

## `8f-colour` — partial verification pass (2026-10-10), NOT a triage

A read-only sibling session pre-read all 15 open `8f-colour` beans at this branch's
`37bdbeef6b3` and left notes at `/mnt/project-files/eightfold/8f-colour-preread.md`,
stating explicitly that dispositions stay here and that **its own path checks were
run partly against `main` at `3a71395875` and its "sorry-free" judgements are
grep-only**. I verified five of its concrete claims on this branch. Scoreboard:

| its claim | verdict |
|---|---|
| `prop:color-su3-from-g2` empty-`uses[]` claim in `8p1x`/`8p1e`/`8p1h` is **stale** | **confirmed** — `uses: ["def:octonion-algebra"]` at `color-su3-from-g2.ts:23`, discharged 2026-08-29 |
| `8p1i` and `8p1j` are scrapped, so `8p1h` is gated on an abandoned route | **confirmed** — both `scrapped` |
| `gram-matrix-dual.py:45` prints the convention-C formula beside the D value | **confirmed** — label `1/(q^½+q^-½)`, value `pyhecke.gram.z = q0³/(q0²+1)`, 0.113 apart |
| `ozyt` is title-only | **confirmed** — 14 lines, and its *title* is the defect |
| `−80000` is mis-attributed to the sextic in `Brings/ColourCubicDiscriminant.lean` | **confirmed, after I first wrongly refuted it** — see below |
| its companion figure `−2^19·5^10`, flagged by it as unverified | **confirmed exactly** — it is the sextic's discriminant |

So **6 of 6 checked claims hold**, including the one I reported as refuted. The
pre-read's caveats about its own method did not cost it a single verdict.

### What this front actually yielded, and it is not a closure

No bean closed. One **false instruction** found and documented (`ozyt`'s title tells
the next agent to Lean-prove `disc = −2^7·5^4` of an object whose discriminant is
`−2^19·5^10`), one **new corpus number** measured (the sextic discriminant, nowhere
on record, which independently confirms `z03j`'s composite-chain item 3 via the
`2^12·5^6` ratio), one **detector blind spot candidate** (a convention carried in an
f-string label, invisible to both convention audits — one site only, so measure the
class before claiming a taxonomy row), and **three beans carrying one stale fact** a
fourth bean had fixed six weeks earlier.

That last is this epic's own recorded pattern for the third front running: fronts
named for *subject matter* yield scoping, not closures. `8f-colour` is now
**partially scoped, not triaged** — 9 of 15 beans unexamined.

### The rule this front sharpens

**Do not second-guess a path that resolves.** I treated the pre-read's verbatim path
`Brings/ColourCubicDiscriminant.lean` as an approximation of two files I had already
found — `Mass/ColourCubicDiscriminant.lean` (no `80000`) and
`Brings/ColourCubicBranchLocus.lean` (`80000`, correctly attributed) — and reported
the finding refuted. A **third** file exists with exactly the name given. Three of the
four names in `{Brings, Mass} × {ColourCubicDiscriminant, ColourCubicBranchLocus}` are
real files, two of them proving overlapping facts over different base rings. In a
corpus with that naming surface, `ls` the path before concluding it does not exist.


---

## 🛑 I RECOMMENDED A SCRAPPED BEAN AS THE ROOT BLOCKER, FOUR TIMES (correcting myself, 2026-10-10)

**What I asserted**, in three end-of-turn reports, two comments on PR #7553 (now
merged as `3c0351a40da`, so immutable), a `send_later` check-in prompt (since
deleted) and an earlier append to this epic:

> ROOT BLOCKER across both fronts: no per-chiral-fermion braid word exists
> (`htw2`). Blocks `t0hl`, `jk6g`, `h0zz`, `wqto`, `kebu`, `qvpl` sub-item A —
> five beans, two fronts, one construction. **Highest leverage.**

**What is actually true.** `htw2` is **`scrapped`** (duplicate of `qou-kebu`,
2026-10-04 reorg), and its 294-line body records that the lepton half was
**derived and closed on 2026-08-17**:

- A framed braid word exists — `beta_nu = sigma1 sigma2` in `B_3`, framing
  `(0,0,0)` — from the corpus's own *"fermions are knots, quarks are
  Borromean-linked unknots"*.
- ν = `{0,0,0}` and e = `{-1,-1,-1}` are **forced**, not selected;
  `{-1,0,1}` is **refuted** by a knot closure being unable to carry an
  injective framing, with no total needed.
- `d = {-1,0,0}` follows from `θ_V = q^{1/2}·id_V` making a `(+1,−1)` pair
  **ribbon-invisible**, so sign-coherence is a **normal form**, not the
  Bilson-Thompson import it was first labelled.
- Residual **1·2·2·1 → 1·1·1·1**.

Verified today on `main` `3c0351a40da`, not taken from the bean:
`ComponentFraming.lean` (304 lines) and `SignCoherentTwist.lean` (226) both
`lean -DautoImplicit=false -s 65536` **rc=0, 0 diagnostics**, 0 `sorry` /
`axiom` / `native_decide` each, and all 7 named declarations resolve.

**What that contaminates.** Every place I called this the highest-leverage next
item was pointing an agent at a closed result. The live carrier is **`qou-h0zz`**
(`todo`, title *"V6: braid words per chiral fermion — the actual blocker for
T(t)"*), now carrying the full correction and the narrowed open set; `qou-kebu`
(`todo`) is the designated successor and already cites both files nine times.

**What survives as genuinely open**, and it is narrower and better posed than
what I was recommending: the **total** twist is still pinned by the SM target
(`T = 3Q`), so `Q(f)` for a single chiral fermion is underived — the framework's
`Q = w/2` is hadron-level; the **quark** side is consistent-not-derived
(identity-π merely *leaves* `{0,1,1}` available); **chirality** is untouched
(`qou-wqto` — no braid word separates `u_L` from `u_R`); the `1/3` normalisation
is still the helon precedent; and `conj:sm-hypercharge-invariant` stays open.

**The rule this epic already carried, and I did not apply to my own
recommendation.** This epic says: *read the beans a bean cites AND the beans
that cite it, before working it.* I wrote that after measuring 5 of 13 stale
bodies across `8f-tseries` and `8f-gen` — then recommended `htw2` four times
**on its title alone**, never opening it. Sharpen the rule: a **`scrapped`**
bean is the highest-risk read, not the lowest. Its status says ignore me and its
body may hold a verified, sorry-free closure — exactly the case §path-6 of the
corpus-grep checklist was added for.

**Do not read this as the arc being further along than it is.** Nothing here
closes a conjecture, nothing is wired, and per rule 13a no bean was closed. One
stale recommendation of mine is withdrawn and one open set is stated correctly.


---

## The title-trap diagnosis was HALF RIGHT — it is the LISTING, not the status (2026-10-11)

The append above sharpened the rule to *"a `scrapped` bean is the highest-risk
read"*, after recommending `htw2` four times on its title. **That diagnosis is
incomplete, and I proved it incomplete within the hour** by doing the identical
thing to `qou-wqto` — which is `todo`.

`qou-wqto`'s title is *"no braid word distinguishes them"* (V9, 2026-08-10); its
body records the grading **constructed** (V10) and Type-B folding **excluded**
(V11), both sorry-free and both re-verified `rc=0` today. I propagated the title
into the `qou-h0zz` open-set list, issue #7711, PR #7712 and three chat reports
before opening it.

**Common cause: the title came from a LISTING.** `beans list` and the
session-start coord sweep print `id`, `status`, `title` — and no body. So every
front's "open items" read as their titles by default, whatever their status.
`scrapped` was a red herring; `todo` failed the same way.

**The rule, restated to cover both cases:** a claim about a bean that came from
a listing is **unverified** until its body is read. That applies to this epic's
own front tables, which are listings too.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

- **Round 89 (`https://github.com/litlfred/qou/pull/8408`, head `10a16c52a2f1ad211bfb233927428389e8e4dd3e`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
