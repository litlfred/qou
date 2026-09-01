# convention-auditor — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`; confirm entries as you use them.

**The rule governing this whole file: cite the rule, re-measure the instance.**
Named instances in `AGENTS.md`'s convention section go stale between being
written and being read — four so far.

---

## STABLE — the rulings

- **R1 (2026-08-15).** Convention **D** (`z = q³/(q²+1)`) canonical;
  **C** (`z = √q/(q+1)`) excised. Largely a re-affirmation of 2026-08-09;
  R1's new work was the `qbeta-decay` channel registered `disputed`
  (PR #5111) and the registry's one `owner_decision_required`. It removes
  the *convention* question from `tools/pyhecke/gram.py::z` but **not** the
  Gram singularity under D — that is a numerical blocker, bean `qou-cds2`.
- **R2.** **Proton pin canonical** for all compute. The ideal CAL-2
  definition is untouched.
- **R3.** **`bring_color_weighted`** canonical as the p/n convention.
  Six live non-comparison files were still off-canon (bean `qou-cds4`).

At `q₀`: `z_C = 0.49932…`, `z_D = 0.61268…`. Same name, opposite values.

## STABLE — the detectors, and what each can and cannot see

| script | sees | blind to |
|---|---|---|
| `scripts/convention-c-producer-audit.py` | `.py` **shapes** — assignment targets and (since 2026-08-16) return forms | `.lean` entirely (four `rglob("*.py")` walks, no Lean path); sqrt-variable spellings |
| `scripts/convention-c-value-audit.py` | `.py` **values** — evaluates each binding at two sample points | nothing shape-based, but it is per-binding |
| `scripts/lean-markov-convention-audit.py` | `.lean` defs, C vs D, actionable vs deliberate | non-Lean |

**Quote `defs`, not total sites** for the Lean audit: a `q³/(q²+1)` inside a
proof *mentions* a convention; one inside a `def` body *defines* it.
Conflating them inflates the count several-fold (150 sites vs 14 defs).

## TRAP — a clean detector run is never an all-clear

The producer audit once reported **0 actionable** C producers. Real but
narrow: it keyed on *assignment targets*, so a C value **returned from a
function** was structurally invisible. Seven files returned
`1/(√q + 1/√q)`, which is `√q/(q+1) = z_C` exactly.

`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues **sixteen**
distinct detector-blind spellings — several found *by* detectors written to
catch the previous blind spot. Closing one shape does not close the class.

## TRAP — value-blindness hides BOTH buckets at once

The shape audit reports `computations/` at single digits actionable. Measured
by **value**, `computations/` holds **85** confirmed C bindings, of which
**21 are reported by the shape audit NOWHERE** — not actionable, not
deliberate, not at all. All 21 use the sqrt-variable spelling
(`1/(sq + 1/sq)` or `u/(u²+1)` with the variable equal to `√q`).

Confirmed from the other side: five such sites were registered in
`blocked_on_rederivation` and the shape audit's printed count did **not**
move, because it never counted them. So draining the shape audit to zero
would not end the excision. Bean `qou-t9r1`; the four sites that cannot be
migrated by substituting `z_D` at all are `qou-pmkh`.

## TRAP — the name, the docstring and the body can all three disagree

`qou-961o` (`ae8098c3`) made bare `markovZ` mean convention D uniformly. But
the rename left a case-only twin, and under it a worse defect:

`markovZc`'s docstring read *"z = 1 / (√q + 1/√q)"* — C, `0.4993203342` —
above a body computing `q³/(q²+1)`, D, `0.6126880371`. The **name** said C
(lowercase twin of `markovZC`, which really is C); the **docstring** said C;
only the **body** said D. A reader checking name against docstring gets
agreement and is still wrong by 0.113.

Fixed 2026-08-29 (#6015): renamed to bare `markovZ`, docstring corrected to
the body. `markovZC` now has no case twin.

**The generalisable rule: agreement between two labels is not evidence about
the third thing.** Only the body is evidence — the `Λ`/`Cl₂` failure below,
one level deeper, because here the prose agreed with the wrong name.

## STABLE — the counter-move: test the ANSWER, not the source

When the result is exact and symbolic, the algebraic form of the result keys
on what it *is* rather than how it was written. The Markov peel's deuteron
denominator factors as `192·q²³·(q²+1)³` — one `(q²+1)` per peel, because
`z = q³/(q²+1)`. Convention C leaves half-integer powers and cannot produce
it. So *"`(q²+1)` divides the denominator"* is a complete convention test
needing no source, no `z` grep and no anchor
(`computations/markov/peel_anchor_identification_probe.py`, #5190).

A value cannot be stale, mislabelled, re-spelled, or inherited from a stale
record and still factor correctly. Reach for this first.

## TRAP — the `Λ` vs `Cl₂` naming guard is NOT clear, and is a different defect

`Λ(θ) = Cl₂(2θ)/2`. One regular ideal tetrahedron is `Cl₂(π/3) ≈ 1.01494`;
the figure-eight complement is `Vol(4₁) = 2·Cl₂(π/3) = 6Λ(π/3) ≈ 2.0299`.
`2Λ(π/3) ≈ 0.6766` and `3·Cl₂(π/3) ≈ 3.0448` are **both wrong** — each keeps
one function's coefficient with the other's name.

The 2026-08-10 drain swept `content/` only; re-measured 2026-08-15, **54 sites
across 35 files** remained (5 `content/`, 28 `computations/`, 21 `docs/`; 0 in
`.lean`/`.ts`). Bean `qou-zdz5`. Most survivors compute the RIGHT value under
the WRONG name — `VOL41 = 2*mp.clsin(2, mp.pi/3)` is 2.0299 ✓ annotated
`# Vol(4₁) = 2Λ(π/3)` ✗ — so **a grep for the bad name does not imply a bad
number**; check the arithmetic beside it before "fixing" a value. And do not
borrow this guard's "0 in `.lean`" as a convention-C all-clear: the two were
conflated once, by shape rather than subject.

## STABLE — the two q₀ layers, and the straddle hazard

- **Package layer** `tools/qou-substrate/.../constants.py` (`Q`, `q_at()`,
  `Q_50_DIGIT_STR`) is **proton-pinned**, `q₀ ≈ 1.1099785827513808`. This is
  the default for all new compute.
- **`computations/` layer** historically carries muon-q₀ witnesses;
  `computations/q-pinning-50-digit.witness.json` holds the muon value and is
  the **anchor-defining** witness (`witness._q0_value_for_anchor("muon")`
  reads it). These remain valid as recorded but are not the default to reach
  for.

**Never straddle.** Worked case: the μ₃ Fréchet probe took `y_λ` from the
then-muon-built cache while evaluating `χ_λ` at the proton `q₀` — an
11.54 ppb layer separation (the μ–p substrate tension itself), ~1e-7
relative. If you touch a producer consuming a muon-built cache, move the
*whole* quantity, not one input.

**Shape to watch for:** a cached-witness accessor that serves precomputed
data *when the caller's `q` matches the value the cache was built at* — that
gate is satisfied trivially when the caller passes the package constant, so
the boundary is crossed with no signal. Audit with
`computations/audits/cached_accessor_shape_audit.py`, which keys on
**provenance** and requires the gate to involve a caller argument; measured
live instances: **zero** (2 hits, both the dead historical function and its
generated mirror).

## TRAP — `y_lambda_at` is anchor-NEUTRAL; do not "fix" call sites

`AGENTS.md` described it as serving the muon-built cache on a `q`-match.
That is **pre-2026-08-09** behaviour. The live body is
`y_lambda_su_n(n, mpf(str(q_val)), 2)` — the *caller's* `q`, no
`.witness.json` anywhere in the cone. The gate moved into
`_y_lambda_at_convention_C_HISTORICAL`, which is dead.

Measured cost of acting on the stale wording: promoting `y_lambda_at` to a
muon *identifier* in `q0_producer_pin_classifier` reclassified **56
producers** proton → `BOTH`, and `BOTH` shields a producer from triage as a
possible deliberate comparison. It would have hidden 56 clean files.

## STABLE — the re-pin migration is authorised, with four bought constraints

Owner, 2026-08-15: *"we want proton unless for an explicit reason (like
comparison on proton vs muon results). otherwise pin proton"* / *"fix all,
even if not visible."* Scope: bean `qou-1c4y`.

**Read `q0-pin-migration.md` in this directory before running any of it.** The
first attempt broke `main` for **208 producers** (`qou-m9xp`), and the four
constraints that came out of it are not optional: never re-pin the
anchor-DEFINING witness; the muon anchor keeps its definition; a comparison
producer needs both pins via a per-process override; and the manifest
reclassification and the witnesses it re-pins are **one change**. That file
also records why "empty `ideal_muon` in the manifest" is a disabling rather
than a migration, and the producers that refuse a proton run by design.

## BASELINE — re-measure, do not quote

Every number below is a *method*. `AGENTS.md`'s own table of these moved on
every re-measurement, in both directions.

| what | command | last seen | when |
|---|---|---|---|
| `.py` C by shape | `python3 scripts/convention-c-producer-audit.py` | 9 actionable (7 registry-blocked on `qou-cds1`) | 2026-08-29 |
| `.py` C by value | `python3 scripts/convention-c-value-audit.py` | 85 in `computations/`, 21 invisible to the shape audit; `tools/` 0, `content/` 0 | 2026-08-29 |
| `.lean` C defs | `python3 scripts/lean-markov-convention-audit.py` | 14 defs, 0 actionable / 14 deliberate | 2026-08-29 (post-`qou-961o`) |
| `markovZ*` family | that script **and** `grep -rn 'def markovZ'` — they disagree, see below | bare `markovZ` **10, all D**; `markovZD` 3; `cosKernel` 1; `markovZc` **gone**. `markovZC`: audit says **2**, grep says **3** | 2026-08-29 (post-#6015) |

`markovZC` 2-vs-3 is live and unexplained: grep finds three (all genuinely C),
the audit lists two; it predates #6015, so detector scope, not regression.
**Quote both with their method**; do not silently prefer one.
| muon-fingerprint witnesses | see the prefix note below | 477 | 2026-08-26 |

**State the METHOD when quoting the muon count.** Three different values are
all called "the muon q₀" — the frozen pin `1.1099785955573347…`, and the
lepton-tower derivation at CODATA 2018 and 2022 — diverging at the **13th**
significant digit, so the prefix length silently selects which you counted:
`1.109978595` (10 digits, all three) gave 477; the full literal (canonical
pin only) gave 149. Both measured 2026-08-26 with
`computations/audits/muon_pin_three_values_probe.py`. Quoting the wrong one
makes the migration look ~3× more complete than it is.

---

## Session log

One line per audit: what you measured, with which script, any TRAP added. Keep
under 200 lines — prune the log or split a section out, never the TRAPs.

- 2026-08-29 — re-measured post-`qou-961o`: bare `markovZ` 9, all D; found the
  `markovZC`/`markovZc` case collision and, under it, a docstring that agreed
  with the wrong name; fixed in #6015; split `q0-pin-migration.md` out.
- 2026-08-30 — live: value-audit 87 C / 348 D in `computations/`. TRAP: its
  "86 BLOCKING" over-states the DRAINABLE surface ~80× (subtracts only the
  1-entry comparison-ledger, not the 12 `blocked_on_rederivation` rows nor ~64
  deliberate-named). Safely-actionable C = ≤1, and that 1 is the forbidden
  z-swap on the cds1-blocked `qbeta_ck_cache.py`. Fixed one Λ-Cl₂ mislabel
  (`local-substrate-q.qa.json:1498`, `3Cl_2`→`2*Cl_2`). Never quote "BLOCKING".
- 2026-09-01 — bean `t7qv`: split `functional-and-bond-topology.md` out. Four
  live convention hazards, all measured. **(1)** Markov vs q-Plancherel is
  settled three ways — Plancherel is not a Markov trace, does not annihilate the
  q-antisymmetriser (so its Gram is nonsingular, a different cone), and fails
  multiplicativity on disjoint blocks 36/36 at `H_6`. The silver coincidence is
  a true all-`n` theorem about Plancherel; under Markov it moves to the
  supergolden `q^3 = q^2+1`. **Never transport a metallic result across that
  line.** **(2)** `atom_gen_chains` (C(A,2) bonds) and `atom_braid_word_3A`
  (A-1, chain) DISAGREE for every `A >= 3` and this was undocumented; the arity
  law needs the chain, the binding evidence favours all-pairs, and the choice
  moves numbers 16 % vs 4 % under mere relabelling. **(3)** the colour
  convention splits deliberately between scales — `pn` colour-weighted (`D_PN`,
  owner ruling R3), quark `ud` colour-blind and explicitly UNSETTLED in the
  source. **(4)** force channels are assigned by GENERATOR (`3k+2` strong,
  `3k+1` EM, `3k` intra) and the rate follows the generator, not `beta`: the
  same `sigma^-1` gives `+0.907` strong and `-0.600` EM, opposite signs. Scope
  trap: AME binding is NUCLEAR, so compare the strong channel ALONE.
