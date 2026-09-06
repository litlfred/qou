# The chi caches were stale to the 2026-09-05 intra-ordering change — explored, then REGENERATED on owner ruling

**Bean:** `qou-92u9`. **Probe:** `computations/probes/chi_caches_predate_the_intra_ordering_change_probe.py` (6/6).
**Related:** `qou-hu1f` (the ordering change itself), PRs #6841 / #6847 (the result this refutes), #6854 (this work).

## The finding, in one paragraph

The six `chi-<atom>-h<n>-at-q0-50dps.witness.json` caches were computed
**2026-08-10**. Their producer `chi_at_q0_via_hoefsmit_mpfr.py` changed **three
times** since (2026-08-15, -23, -30 — the last, `d151898dd6`, a fix *about these
caches*), and its callee `atom_braid_word_3A` changed its intra-nucleon ordering
on **2026-09-05** by owner ruling (`qou-hu1f`). The producer calls it at line 96
with **no `intra_order`**, so a fresh run yields `borromean` while the committed
caches are `grouped` — matched to `~3e-50` against `~1.2–1.3` **relative** for
borromean, across all five atoms measured. Not a drift: a different number.

**🛑 My explanation for why it went undetected was wrong, twice, and is corrected
here.**  I first wrote that the caches carry `scriptFile: None` with a
`scriptHash` matching no file, so *"no checker knows what to hash"* — and
proposed emitting `scriptFile` as a cheap fix independent of the regeneration
choice.

The observations were right and the inference was not. `save_witness` writes a
**`producer`** field; every stale cache carried
`producer: chi_at_q0_via_hoefsmit_mpfr.py` beside `scriptHash c36a8a393fcd`
against the producer's then-current `815a026e9591`. **The drift was plainly
visible** to ordinary detection keyed on the field these tools actually use. It
was not undetectable — it was *undetected*, which is what the dispatch-only
workflow posture (owner directive 2026-06-30) predicts. The proposed
`scriptFile` fix is therefore unnecessary.

**And my "3,610 witnesses scanned, none of the six flagged" was a third
misreading.** That audit's header says `SELF-stale (already caught): 597
(excluded below)` — it *excludes* self-stale witnesses by design, deferring to
the validator that covers them. Their absence from its report is the exclusion
working correctly, not the tool being blind. Three wrong inferences in one
investigation, all the same habit: treating an absence as evidence without
checking what produced it.

What survives is a two-class split, and only the second half needs new tooling:

| class | detectable today? | status |
|---|---|---|
| **SELF** — producer's own three edits (2026-08-15/-23/-30) | **yes**, `producer` + `scriptHash` | was never checked |
| **IMPORT-CONE** — callee `atom_braid_word_3A` changed 2026-09-05 | **no** — producer byte-identical across it | genuinely needs the cone audit |

## What it moves — measured, not estimated

Over **all six atoms** — helium-4 included, measured separately because it is
the slow one:

| finding | GROUPED (committed) | BORROMEAN (live) | |
|---|---|---|---|
| `argmin(t) == argmin(w)` | 6/6 rows | **4/6 rows** | ← moves |
| `w` monotone in content sum | 49/49 | 49/49 | invariant |
| `conc(w,\|χ\|) == conc(c(λ),\|χ\|)` | 6/6 rows | 6/6 rows | invariant |
| anti-correlation `conc(w,\|χ\|)` | 9/49 | **25/49** | ← **changes sign** |
| `dim`~`\|χ\|` concordance | 43/48 | **21/48** | ← moves |
| worst selection margin | 2.108× | **10.069×** | ← moves |
| product flattened on every row | True | **False** | ← moves |

All six committed caches are GROUPED, helium-4 included (`9.56e-50` against
`1.201` relative). Its `|χ|` ratios spread **51.2×** with `[11,1]` and `[8,4]`
changing sign.

**Which two rows flip, and where they land, is not incidental:**

    tritium    argmin(t)  [5,4] -> [7,2]      argmin(w) stays [5,4]
    helium-4   argmin(t)  [6,6] -> [7,5]      argmin(w) stays [6,6]

`[7,2]` and `[7,5]` are **exactly two of the three partitions previously
identified as carrying a `dim`-vs-`|χ|` inversion** under grouped. The O3′ probe
had already flagged this shape as where a flip would come from — *"a discordant
partition that also happened to be the runner-up is what a flip would look
like"* — written before this measurement existed. The prediction was
directionally right; deuteron's `[4,2]`, the third discordant partition, does
not flip.

The split is not arbitrary and was **predicted before measurement**: `w` is a
function of the partition and `q` alone, so every `w`-side finding is invariant
(verified identical to `<1e-45`), and every `χ`-side finding is exposed.

**The reversal is the serious one.** The anti-correlation between `w` and `χ` —
the central structural claim of the O3′ arc, 4/28 concordant under grouped —
becomes **16/28** under borromean, i.e. *above* the 14/28 independence
expectation. It does not weaken; it changes sign.

And the headline falsifier fires: `o3prime_selection_is_atom_independent_probe.py`
states *"a single row where argmin(t) != argmin(w) would refute it"*. Tritium
under the live ordering is that row — `argmin(t) = [7,2]` against
`argmin(w) = [5,4]`.

## Option 1 — regenerate the caches

**What it means.** Re-run `chi_at_q0_via_hoefsmit_mpfr.py` for all six atoms so
the caches carry the ordering the corpus actually uses.

**What it costs — measured, and far less than I first told the owner.** All five
A≤3 atoms regenerate in **under three seconds combined** on the non-incremental
path, and **helium-4 takes 423 s (≈ 7 minutes)**, not the 22.5 I quoted. That
1352-second figure is from helium-4's own witness and describes the *incremental*
path, which persists each partition as it goes; `incremental=False` is a
different cost. **A full six-atom regeneration is about seven minutes.**

**What it risks.** 84 live scripts and 48 committed witnesses read these caches.
Their numbers move, and the O3′ arc's central finding is then refuted outright
rather than conditionally. Nothing is *hidden* by this — it is the point — but it
is a real change to published numbers across the binding arc.

**What it commits to.** Accepting the borromean ordering as governing this
surface, and re-deriving anything built on the `χ`-side facts.

## Option 2 — leave the caches, keep the scoping

**What it means.** The staleness stays documented, gated by a probe, and beaned;
the numbers do not move today.

**What it costs.** Every `χ`-side number downstream stays GROUPED-CONDITIONAL,
and the only thing preventing a reader from taking them at face value is prose —
the probe's banner and this document. There is **no mechanical gate**, because
`scriptFile: None` makes one impossible to write.

**What it risks.** The failure mode is precisely the one `AGENTS.md` catalogues:
a number measured once, written down, and quoted months later as current. Two
merged PRs (#6841, #6847) already carry the refuted headline, corrected only by
comments.

**What it commits to.** Nothing — it is the reversible option, and the no-op if
nothing is decided.

## They are not exclusive, and there is a third thing worth doing either way

**Emit provenance from the cache producer.** `scriptFile: None` is what makes
both the self-staleness and the import-cone staleness undetectable, and fixing it
is cheap, uncontroversial, and **independent of the regeneration decision**. With
`scriptFile` populated, ordinary `scriptHash` drift catches the next producer
edit automatically — including the three that have already happened unnoticed.

Under option 2 this is what converts "documented in prose" into "detected by a
gate". Under option 1 it is what stops the same thing recurring after the
regeneration.

## Recommendation, marked as judgement

**Do the provenance fix now regardless**, and take option 1 for the A≤3 atoms
where the cost is seconds. Helium-4 can follow separately. The reasoning: the
`w`-side facts are proven invariant, so the regeneration destroys nothing that
was solid; and leaving a sign-reversed structural claim in the corpus behind a
prose banner is exactly the state this repository's disciplines exist to prevent.

This is a judgement, not a finding. The measurement stands either way, and the
no-op is safe and reversible.


## Outcome: regenerated (owner ruling, 2026-09-05)

The owner ruled **"regen"**. All caches from this producer were rebuilt with
`--fresh` on the canonical producer path.

**`--fresh` is load-bearing and its absence would have been silent.** The
producer's resume check compares *stored-vs-current `q₀`*, and `q₀` did not
change — only the word ordering did. Without `--fresh` the run would have
resumed and kept every stale partition while stamping the result as current.
The flag's own help text describes exactly this trap.

### The stale set was EIGHT, not six

Regenerating surfaced two more witnesses from the same producer and the same
stale generation — `chi-diproton-h6` and `chi-dineutron-h6`, both built
2026-08-16, both carrying `scriptHash c36a8a393fcd`. They were invisible to this
investigation because they are not in `aK_via_lp_dual_full.py`'s `ATOM_CHI` map,
which is the consumer list I had been reasoning from. They are in the
*producer's* `ATOMS` map, which is the right place to enumerate from, and both
are now regenerated.

**The lesson generalises:** enumerating a producer's outputs from one consumer's
list undercounts by whatever that consumer does not use. The producer field is
the reliable index — `producer == "chi_at_q0_via_hoefsmit_mpfr.py"` finds all
eleven witnesses it has ever written.


## Downstream: what the regeneration propagates

75 committed witnesses come from scripts reading a chi cache and predate the
rebuild. **64 carry absolute-looking fields and move; 11 are ratio-only and are
predicted immune.**

Measured on `a-K-via-lp-dual-full`, before/after in git: `tr_M` scales by
1.82 / 2.08 / 3.78 / 7.87 / 6.89 / 14.32 — matching `qou-hu1f`'s `R_quark`
(3.785 / 7.868 / 6.891 / 14.325) exactly where that bean lists it — while
**`a_K^C`, the quantity the producer exists to report, does not move at all.**
That confirms `qou-hu1f`'s immune/scaling split on a producer it never examined.

**The scaling rule stops at the aggregate.** Re-running
`delta_lambda_2row_stratum_analysis.py` moved 181 numeric fields by factors from
**11.8× to 51.2× within one witness** (51.24 being the helium-4 `|χ|` ratio
spread). Per-partition characters move by per-partition factors, with sign
changes. So a per-λ witness must be **re-run, not rescaled** — only the
aggregate trace has a closed-form factor.

The remaining 63 are a scoped follow-up, tracked in `qou-92u9`. So are the
muon-anchor chi caches, which this regeneration did not touch.
