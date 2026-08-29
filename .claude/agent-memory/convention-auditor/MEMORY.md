# convention-auditor — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`. Confirm entries as you use them.

**The rule governing this whole file: cite the rule, re-measure the
instance.** Three named instances in `AGENTS.md`'s own convention section went
stale between being written and being read.

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

## TRAP — `markovZ` is one name spanning both conventions

It was 5 declarations (3 C, 2 D), then **13** (3 C, 10 D). Two files
`AGENTS.md` names as C `markovZ` are **now D**. A name that spans two
conventions keeps accreting declarations while the question underneath it is
being settled — a naming defect that migration does not fix. Bean
`qou-961o`. **Always resolve a `markovZ` to its own definition** before
reasoning about its value.

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

The 2026-08-10 drain swept `content/` only. Re-measured 2026-08-15: **54
sites across 35 files** remained (5 `content/`, 28 `computations/`, 21
`docs/`; **0** in `.lean`/`.ts`). Bean `qou-zdz5`.

Most survivors compute the RIGHT value under the WRONG name — e.g.
`VOL41 = 2*mp.clsin(2, mp.pi/3)` is 2.0299 ✓ annotated `# Vol(4₁) = 2Λ(π/3)`
✗. **A grep for the bad name does not imply a bad number**; check the
arithmetic beside it before "fixing" a value.

**Do not borrow this guard's "0 in `.lean`" as a convention-C all-clear.**
The two were conflated once, by shape rather than subject.

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

## STABLE — the migration is authorised, with four bought constraints

Owner, 2026-08-15: *"we want proton unless for an explicit reason (like
comparison on proton vs muon results). otherwise pin proton"* / *"fix all,
even if not visible."* Scope: bean `qou-1c4y`. The first attempt broke
`main` for **208 producers** (`qou-m9xp`). The constraints:

1. **NEVER re-pin an anchor-DEFINING witness.** Re-pinning
   `q-pinning-50-digit.witness.json` redefines what "muon" *means* — 262
   `Q0_FLIP`s, and `q_parameter`'s guard then hard-fails every `ideal_muon`
   producer including the one that would regenerate the anchor.
   `q0_repin_sweep.py` excludes it by name; do not remove that.
2. **The muon anchor keeps its definition.** Something must still hold the
   muon 50-digit string or the ideal/CAL-2 layer becomes unstatable.
3. **A comparison producer needs BOTH pins**, via a per-process override,
   and belongs under `physical_proton`.
4. **Do not split the change.** The manifest reclassification and the
   witnesses it re-pins are one change. PR #5049 merged the witnesses and
   held the manifest; the half that landed is the half that broke `main`.

**Do NOT "migrate" by emptying `ideal_muon` in
`computations/q0_anchor_manifest.json`.** `q_parameter.py` selects by
membership, so an empty list means no producer ever resolves to the muon
anchor and the anti-corruption guard can never fire. It also relabels every
already-emitted muon witness as proton. The list does not end at zero:
several producers refuse a proton run *by design*
(`atomic_tr_m_mpfr_50dps`, `he4_stage2_ranking_seminormal_xcheck`,
`cross_check_trM_1ppb`), and `q_pinning_50_digit` defines the anchor.

## BASELINE — re-measure, do not quote

Every number below is a *method*. `AGENTS.md`'s own table of these moved on
every re-measurement, in both directions.

| what | command | last seen | when |
|---|---|---|---|
| `.py` C by shape | `python3 scripts/convention-c-producer-audit.py` | 9 actionable (7 registry-blocked on `qou-cds1`) | 2026-08-29 |
| `.py` C by value | `python3 scripts/convention-c-value-audit.py` | 85 in `computations/`, 21 invisible to the shape audit; `tools/` 0, `content/` 0 | 2026-08-29 |
| `.lean` C defs | `python3 scripts/lean-markov-convention-audit.py` | 14 defs, 0 actionable / 14 deliberate; 38 D defs | 2026-08-29 |
| `markovZ` declarations | that script | 13 (3 C, 10 D) | 2026-08-29 |
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

One line per audit: what you measured, with which script, and any TRAP you
added. Keep under ~200 lines — prune the log, never the TRAPs.
