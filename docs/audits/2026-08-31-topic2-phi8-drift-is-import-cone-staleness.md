# The topic2 Φ_8 drift is import-cone staleness across an owner-ruled convention migration

**Bean:** `qou-wc8f`. **Date:** 2026-08-31.

Bean `qou-wc8f` recorded that `topic2_mirror_pair_phi8_boundary_scan.py` does not
reproduce its own committed witness on `main`, that the fresh `mult(Φ_8)` column
violates a documented scaling law, and concluded the **committed** column should be
kept because *"the refreshed numbers are probably wrong."*

That conclusion is **not safe**, and this note records why — together with what is
established, what is not, and the one experiment that would settle it.

## 1. The drift is import-cone staleness. MEASURED.

The producer has **not changed**. Its live `scriptHash` is `53b875ca8953`, byte-identical
to the `scriptHash` recorded in the committed witness. So the producer is not self-stale
and a file-local `git diff` on it shows nothing — the AGENTS.md import-cone class exactly.

What moved is the data underneath it:

| | computedAt |
|---|---|
| `topic2-mirror-pair-phi8-boundary-scan.witness.json` | **2026-08-18** 22:04:20 |
| all **18** upstream `habiro-coefficients-<slug>.witness.json` | **2026-08-25** 21:49–21:57 |

All eighteen, in one batch spanning eight minutes, **seven days after** the topic2
witness. Zero of eighteen predate it. The committed column was computed from a_m data
that has since been entirely replaced.

## 2. The regeneration was a sanctioned convention migration, not a regression

The regenerated witnesses say so themselves. From
`habiro-coefficients-helium-3.witness.json`:

> "tr_M(A=3, q) = Σ_m a_m·(u;u)_m (u = q^{1/2}) via the Phase 5q closed form … under
> the canonical **`bring_color_weighted`** pn-convention (**owner ruling R3,
> 2026-08-15**)."

R3 is the owner ruling AGENTS.md records: *"`bring_color_weighted` canonical as the p/n
convention."* The a_m family was regenerated to comply with it.

## 3. Therefore the bean's central inference has the causality backwards

The bean argues: the committed column matches the documented scaling law on 9 of 9 rows
and the fresh column on 0 of 9, so the fresh numbers are probably wrong.

But the scaling law
(`docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md`, **2026-06-01**)
and the committed column (**2026-08-18**) **both predate the R3 migration**. They agree
because they were computed from the same generation of a_m data. That is not independent
confirmation of either — it is one datum counted twice.

The parity observation is real: the law forces even multiplicity at even A, and five fresh
values are odd. But under this reading that is evidence **the law's form does not survive
the convention migration**, which is precisely what AGENTS.md says to expect of C-frame
results — *"must be RE-DERIVED under D, and that is not a z-swap"* — not evidence that the
computation broke.

## 4. The fresh column is not lawless — it obeys an exact law of its own

Extracted from the bean's own table, exact on all 9 rows:

| | relation |
|---|---|
| odd A | `fresh = 2 × committed = 2A − 2` |
| even A | `fresh = 2 × committed + 1 = 2A − 3` |

A clean doubling with a single-unit even-A correction is a mechanism signature, not
corruption. Any account of this drift has to explain that structure; "the numbers are
wrong" does not.

## 5. Eliminated: the commit that looks like the cause

`721ab7b812` (2026-08-30, *"regenerate Habiro witness at muon"*) is **not** responsible,
on two independent grounds. It touches only `habiro-coefficients-extended.witness.json`
and `cross-check-trM-1ppb.witness.json` — **not** the 26-file `habiro-coefficients-<slug>`
family the scan reads. And its claim that regenerating *"re-stamps the pin honestly with
identical coefficients"* is **verified true**: the entire non-provenance diff is timing
fields in seconds (`symbolic_trace`, `together`, `to_u_poly`, `cyclotomic`,
`reconstruction_check`).

## 6. METHOD WARNING: git history cannot be used for cone scans in an agent clone

A `git log --since=<date> -- <path>` scan of the import cone returned the **same** commit
`37fce6c8d2` for the module, the extract script and the witness family — which reads as
"one commit changed everything."

It is an artifact. `37fce6c8d2` has **zero parents and 45,571 files**: it is the **root
commit of a shallow clone**, and `git rev-parse --is-shallow-repository` returns `true`.
`--since` returns it for *every* path because that is where every file first appears.
The scan was measuring the clone's depth, not the corpus's history.

AGENTS.md warns that a sha can be missing because history was never fetched; this is the
same trap one step further on — history-based *change attribution* is unavailable here,
not merely incomplete. Use recorded `computedAt` on the artifacts instead, which is what
§1 does and why §1 is solid.

## 7. What is NOT established — stated plainly

**Which column is correct is still open.** Two symbolic reconstructions were attempted
here and **both failed**, in different ways:

- a first model returned `τ_p = τ_n = 1`, because `canonical_interface_kinds(1,0)` yields
  no interfaces at A=1 and the real τ values live in the atomic witness;
- a second, using the real `tr_M_in_q` for p and n, returned `mult(Φ_8) = 0` under **both**
  conventions.

Neither reproduces the scan, whose object is the **denominator-weighted** difference
`d_X·t_X − d_Y·t_Y` (per its own source comment), not the plain difference both models
built. Their valuations are artifacts of the models and are recorded here only so nobody
repeats them as results.

What *was* shown symbolically, and is worth keeping, is that **the convention controls the
cyclotomic content of the interface factors**. Under `strict_averaged` the numerators carry
a clean factor — tritium `(q⁴+1)/(2q²(q²+1)²)`, helium-3 `q²(q⁴+1)/(2(q²+1)²)` — while
under `bring_color_weighted` the δ term from `flavor_split_leading` leaves irreducible
degree-8 and degree-10 numerators. So a convention change moving a Φ_8 valuation is
mechanically plausible, which is the hypothesis §3 rests on.

## 8. The experiment that settles it

`_habiro_coefficient_extract.py` **hardcodes** `pn_convention="bring_color_weighted"` at
two call sites (lines ~192 and ~237). Parameterise it, regenerate the a_m for a single
mirror pair under `strict_averaged`, and re-run the scan.

- If the committed column returns → the committed values are the **pre-R3** convention,
  the fresh values are canonical, and the witness should be refreshed while the
  2026-06-01 scaling law is re-derived under R3/D.
- If it does not → the convention hypothesis is refuted and the drift has another cause,
  which is then genuinely open.

Cost is small: the A=3 extract took ~2 s in the 2026-08-25 batch.

## 9. Disposition, unchanged for now

The witness stays as committed and the entry stays in the vacuous-green baseline until §8
runs. That is the bean's call and it remains right — **but for a different reason than the
bean gives.** Not "the fresh numbers are probably wrong", which is unsupported; rather
"which convention the published column belongs to is unresolved, and refreshing before
resolving it would silently migrate a number two audit docs cite."

`M_first_Φ_8 = 7` is unchanged on every row in both runs, so the probe's headline
universality claim and both audit docs' surviving claims are untouched either way.

---

# SETTLED, same session — the fresh column is correct and §§3, 7–9 above are superseded

Everything from §1–§6 stands. What follows replaces the parts of this document that
hedged, and it **reverses the disposition**. Three measurements did it, all on today's
tree, all reproducible in seconds.

## A. Today's helper on today's data reproduces the FRESH column exactly

| pair | old a_m-subtraction | current helper | committed | fresh |
|---|---:|---:|---:|---:|
| ³He−³H  | **0** | **4** | 2 | 4 |
| ⁵Li−⁵He | **0** | **8** | 4 | 8 |
| ⁶He−⁶Be | **0** | **9** | 4 | 9 |
| ⁷Be−⁷Li | **0** | **12** | 6 | 12 |

## B. The `qou-0ndb` helper fix is NOT the cause — my own leading hypothesis, refuted

Bean `qou-0ndb` was last updated 2026-08-18T22:10:15Z, **six minutes after** the topic2
witness was computed (22:04:20Z). That near-coincidence made the helper fix — which
replaced "subtract a_m coefficients" with "difference the traces over a common
denominator" — the obvious candidate.

It is wrong. Reconstructing the **old** a_m-subtraction shortcut against today's data
gives `mult(Φ_8) = 0` on every pair, not the committed 2/4/4/6. The helper change cannot
produce the committed column from this data, so it is not what separates the two columns.

That zero is itself informative: `mirror_trace_diff_numerator`'s docstring records that
under convention **C** the shortcut is accidentally valid, while under **D** *"every
cyclotomic multiplicity collapses to 0"*. Measuring exactly 0 says **today's a_m are
D-frame**.

## C. Therefore the committed column is a stale CONVENTION-C artifact

Neither method reproduces 2/4/4/6 from today's a_m. Combined with §1 (all 18 upstream
a_m witnesses regenerated 2026-08-25, seven days after the topic2 witness) and §2 (that
regeneration cites owner ruling R3 / `bring_color_weighted`), the committed column can
only have come from the **pre-R3, C-frame** a_m data it was computed against.

The convention hypothesis of §3 was right — but it was **unsupported when written**, and
is only now supported, by B rather than by the reasoning §3 actually gave.

## D. The decisive test: the fresh output IS a genuine mirror difference

The docstring supplies a necessity criterion the corpus itself states — Φ_1 **must**
divide a true mirror difference, because the two halves coincide at q = 1. Applied to
today's helper output:

| pair | v(Φ_1) | value at u = 1 |
|---|---:|---:|
| ³He−³H | 1 | 0 |
| ⁵Li−⁵He | 1 | 0 |
| ⁶He−⁶Be | 1 | 0 |
| ⁷Be−⁷Li | 1 | 0 |
| ⁹B−⁹Be | 1 | 0 |

5 of 5. Today's object passes the corpus's own correctness test.

## E. Disposition REVERSED

§9 above said keep the witness. **That is now wrong.**

- The **fresh** column is the canonical, post-R3, convention-D result, and it satisfies
  the Φ_1 necessity test.
- The **committed** column is a pre-R3 convention-C artifact, stale against inputs
  replaced on 2026-08-25.
- Bean `qou-wc8f`'s conclusion — *"the refreshed numbers are probably wrong"* — is
  **refuted**. The refreshed numbers are the correct ones.
- The 2026-06-01 scaling law (`mult(Φ_8) = A−1` odd, `A−2` even) is **C-frame** and does
  not survive the migration. Its D-frame replacement is visible in the data and exact on
  all 9 rows: **`2A−2` for odd A, `2A−3` for even** (§4). Re-deriving it is `qou-cds1`
  work, exactly as AGENTS.md prescribes for every C-frame result.
- The parity objection dissolves: odd multiplicities at even A are not a defect, they are
  what `2A−3` gives.

**Actions:** refresh `topic2-mirror-pair-phi8-boundary-scan.witness.json`; land slice C's
prepared assertion, which is unaffected; drop the baseline entry; and re-scope the two
audit docs' `mult(Φ_8)` columns as C-frame. `M_first_Φ_8 = 7` is unchanged on every row
in both runs, so both docs' headline universality claims stand untouched either way.

**One caution carried forward.** That the fresh column is *self-consistent and passes
Φ_1* does not by itself prove the R3 migration was physically right — it shows the
computation is faithful to the canonical convention the owner ruled for. Those are
different claims, and only the second is established here.
