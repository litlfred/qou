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
