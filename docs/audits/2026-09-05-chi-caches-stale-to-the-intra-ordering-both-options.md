# The chi caches are stale to the 2026-09-05 intra-ordering change — both options explored

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

**Nothing detects this**, and that is the sharpest part. The caches carry
`scriptFile: None` and a `scriptHash` (`c36a8a393fcd`) matching no file in the
tree, so no checker knows what to hash and ordinary `scriptHash` drift — which
would have caught all three producer edits — cannot fire. This is the
"bare producers" class `AGENTS.md` names.

**Confirmed against the detector that exists for exactly this.**
`computations/witness_import_cone_staleness_audit.py` was run over the corpus:
**3,610 witnesses scanned, and not one of the six chi caches flagged.** So the
invisibility is measured, not inferred — the tool built to catch import-cone
drift cannot see this instance, because the missing `scriptFile` denies it the
one thing it needs.

## What it moves — measured, not estimated

Over the five atoms cheap enough to recompute (proton, neutron, deuteron,
tritium, helium-3):

| finding | GROUPED (committed) | BORROMEAN (live) | |
|---|---|---|---|
| `argmin(t) == argmin(w)` | 5/5 rows | **4/5 rows** | ← moves |
| `w` monotone in content sum | 28/28 | 28/28 | invariant |
| `conc(w,\|χ\|) == conc(c(λ),\|χ\|)` | 5/5 rows | 5/5 rows | invariant |
| anti-correlation `conc(w,\|χ\|)` | 4/28 | **16/28** | ← **changes sign** |
| `dim`~`\|χ\|` concordance | 24/27 | **12/27** | ← moves |
| worst selection margin | 2.108× | **10.069×** | ← moves |
| product flattened on every row | True | **False** | ← moves |

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

**What it costs.** Far less than first thought. All five A≤3 atoms regenerate in
**under three seconds combined** on the non-incremental path. The 1352-second
figure in helium-4's own witness is the *incremental* path, which persists each
partition as it goes; `incremental=False` is a different cost.

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
