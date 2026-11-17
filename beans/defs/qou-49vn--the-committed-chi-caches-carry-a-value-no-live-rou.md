---
# qou-49vn
title: 'The committed chi caches carry a value no live route reproduces: cached 0.5751722439 vs --fresh AND markov-peel 0.1519683392'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T19:13:20Z
updated_at: 2026-11-17T08:04:32Z
parent: qou-v2om
---


Found 2026-09-05 while re-verifying a claim I had **asserted without measuring**
in PR #6861 — *"re-running the chi producer today reproduces them"*. It does
not, and the discrepancy is a factor of 3.78.

## The measurement

Same container, same commit (`main` at `14c798b93c` + 2), same `mpmath 1.3.0`.
`computations/chi_at_q0_via_hoefsmit_mpfr.py deuteron`, differing **only** by
the `--fresh` flag:

| run | `tr_M_at_q0` |
|---|---|
| cached (resume: 11 partitions already cached) | `0.57517224391777187082653534398618088915249435289286` |
| `--fresh` | `0.15196833920423160759266569775106614127124096465527` |

The cached run reproduces the **committed** witness value to all 50 digits.

Independent corroboration, same day, different script —
`QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py --anchor
proton`:

    [peel]  tr_M(q_0) = 0.15196833920423160759266569775106614127124096465526   (deuteron)
    |bridge - peel|   = 1.15e-51

So the **markov-peel** and the **Hoefsmit+Wenzl bridge** agree with each other
at 1e-51 and with `--fresh` chi to **49 of 50 digits**. Three routes today give
`0.1519683392…`; the cache alone gives `0.5751722439…`.

The `--fresh` help text describes this exact failure: *"Use when a cache may
already have been stamped with the CURRENT q0 while holding values computed at
a different one — the resume check compares stored-vs-current q0, so it cannot
see that."*

## What moved, and what did not

Comparing the fresh witness against the committed one per partition: the
`y_lambda` are **unchanged**; **9 of 11 `chi_lambda` differ substantially**,
with sign flips — e.g. `λ=(5,1)`: `3.2163173422…` → `-0.6822850128…`. So this
is a **χ** change, the mirror of the 2026-08-10 move analysed in `qou-brkp`,
which was a **y** change.

The committed chi witness is also **self-stale**: `scriptHash c36a8a393fcd`
predates two producer fixes —

  * `41f517bf17` (2026-08-23) *"fix(qou-8chw): my own unblock turned a crash
    into silent cache poisoning — guarded"*
  * `d151898dd6` (2026-08-30) *"fix(L1): pin-specific numerical chi caches —
    5/6 atoms certified 1 ppQ (T + ³He recovered)"*

Both are about exactly this cache. `d151898dd6` is the leading candidate and is
**not** confirmed here.

## Scope: all three atoms, and the arbiter itself

The arbiter's committed witness (`atomic-tr-m-mpfr-50dps-proton.witness.json`,
computed **2026-08-19**) disagrees with a re-run today on **every** atom:

| atom | committed 2026-08-19 | today |
|---|---|---|
| proton  | `1.14575969245730086968…` | `0.62932840220292191816…` |
| neutron | `0.98774368811580957163…` | `0.47513351715568221250…` |
| deuteron | (chi cache) `0.5751722439…` | `0.15196833920423160759…` |
| tritium | (chi cache) `0.2293101021…` | `0.02914404236097206535…` |
| ³He | (chi cache) `0.4037670368…` | `0.05859625365443638021…` |

## 🛑 TWO CONFOUNDS — this does NOT establish which value is correct

1. **The Rust kernel was unavailable in today's run** — the arbiter printed
   `[rust] hecke-canonical-chi unavailable; falling back to Hoefsmit+Wenzl
   bridge`. The committed run may have used `canonical-rust`. The fallback is
   the documented graceful one, but it means today's "two routes" are closer
   kin than they look.
2. **The arbiter's own source drifted**: `scriptHash 7c63fadfb8d0 →
   db23b7ba36cb`.

The deuteron result survives both confounds, because `--fresh` chi is a
*different script* that also gives `0.1519683392…`. The proton/neutron rows do
not, and are recorded as observations, not verdicts.

**Nothing here says `0.152…` is right and `0.575…` wrong.** What it says is
that **no live route reproduces `0.575…` except the cache**, and that the cache
is the thing two producer fixes were written to distrust.

## What this retracts

`qou-brkp` item 1 was closed earlier today as *"answered — four routes, one
number (`0.5751722439…`)"*, on the strength of `qou-r9dv` / `aeb31dfb41`
(2026-08-23), which reports three independent methods agreeing exactly. **That
closure is retracted.** `aeb31dfb41` predates `d151898dd6` (2026-08-30), and
the arbiter it names now gives a different number. I closed a question on a
**baseline** instead of a fresh measurement — the precise trap this repo's own
agent-memory doctrine names (*"a BASELINE tells you what to measure, never the
current answer"*), in the same session in which I wrote that entry.

## Next, in order

1. **Build `hecke-canonical-chi` / restore the Rust kernel** and re-run the
   arbiter, to remove confound 1. Until then no verdict.
2. `git diff c36a8a393fcd..HEAD -- computations/chi_at_q0_via_hoefsmit_mpfr.py`
   and read `d151898dd6` — it claims a 1 ppQ certification for 5/6 atoms and
   may already contain the answer.
3. If `0.152…` is right, the blast radius is wide: `option_e_multi_isotope_
   delta_lambda_probe_v3` and every other reader of `chi-*-at-q0-50dps.witness
   .json` carries the superseded value, and `qou-r9dv`'s three-method
   certification needs re-running.
4. **Do not mass-regenerate.** One atom, with the Rust kernel present, decided
   first.

---

## Confound 1 REMOVED — Rust kernel built and re-run (2026-09-05, same day)

`cargo build --release --bin hecke-canonical-chi` succeeds in this container in
**39 s** (7 warnings, no errors). Re-running
`QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py --anchor
proton` with the binary present:

| atom | `[rust]` | `[peel]` | rel \|rust−peel\|/peel |
|---|---|---|---|
| proton   | `0.62932840220292191709…` | `0.62932840220292191816…` | **1.702e-18** |
| neutron  | `0.47513351715568221158…` | `0.47513351715568221250…` | **1.936e-18** |
| deuteron | `0.15194683953767166429…` | `0.15196833920423160759…` | **1.41475e-4** |
| tritium  | `0.02913991921797892047…` | `0.02914404236097206535…` | **1.41475e-4** |
| ³He      | `0.05858796377036033442…` | `0.05859625365443638021…` | **1.41475e-4** |

### What this settles

**`0.5751722439…` is reproduced by NO live route.** Not Rust, not markov-peel,
not `--fresh` chi. Three routes all land in the `0.1519…` neighbourhood. The
committed `chi-*-at-q0-50dps` values are cache-carried and superseded. The
earlier proton/neutron observations were **not** a fallback artifact — the Rust
kernel gives `0.6293…`/`0.4751…` too, so the committed 2026-08-19 arbiter values
`1.1457…`/`0.9877…` are genuinely superseded as well.

### 🛑 A stale BASELINE in a source comment — I read it as corroboration

`computations/canonical_tr_m_via_rust.py:68-70` states:

    # Measured after the fix, with the binary built from tools/hecke-engine:
    #   tr_M(p, q_0) = 1.14575969245730086935241774516176649113
    #   tr_M(n, q_0) = 0.98774368811580957144294046174148798302

Today, same binary path, same anchor: `0.62932840220292191709…` and
`0.47513351715568221158…`. **That comment is stale**, and I cited it as evidence
the committed values were the Rust ones. Third instance this session of the same
error class — a stored number read as a current answer, this time wearing the
words *"Measured after the fix, with the binary built"*, which is exactly the
phrasing that makes it look like a live check.

### What it does NOT settle, and the sharp new finding

Rust and peel **disagree on every composite atom** by

    rust/peel = 0.999858525356843903463281614406   (deuteron)
                0.999858525356843896710241513022   (tritium)
                0.999858525356843898527910951336   (³He)

— **one shared multiplicative constant, agreeing to 17 significant figures**
(spread across atoms `6.75e-18`, i.e. the kernels' own precision floor), while
the two single nucleons agree at `~1.7e-18`.

That shape is informative: the discrepancy is **atom-independent and does not
accumulate with A**, over different braid words and different partition sets. It
is therefore **one shared step in the composite path** implemented differently in
the two kernels — not drift, not accumulation, not a per-atom construction
difference. `1 − 0.9998585253568439 = 1.41474643e-4`.

**No identification of that constant is attempted here**, deliberately: fitting
a formula to a single measured ratio is exactly the move the anti-fit discipline
forbids. It is recorded as a structural signature for whoever localises it.

The discrepancy is **1.4e-4 relative — eleven orders above the 1 ppQ (1e-15) L1
target**, so it is not a precision artifact and both kernels cannot be right.

### Revised next steps

1. **Localise the shared factor.** Diff the composite path: `hecke_canonical_
   chi.rs` / `wenzl_lr.rs` against the Python markov-peel. The single-nucleon
   agreement at 1e-18 means the divergence is in what the composite path does
   *once*, not per crossing. Possible neighbour: bean `qou-1qsw` (three
   inconsistent `pyhecke.atom` nucleon constructions) — same class, different
   magnitude, not established as the same cause.
2. **Only then** decide which value is canonical and whether the
   `chi-*-at-q0-50dps` family should be regenerated.
3. **Still do not mass-regenerate.** One atom, decided, first.
4. `d151898dd6` (*"pin-specific numerical chi caches — 5/6 atoms certified
   1 ppQ"*) claims a certification that a 1.4e-4 kernel split would fail. Read
   it: it may already name this.

### Localisation: four structural exclusions, not yet a culprit

Measured, all from the ratio table above. Each rules out a class; none names
the step.

1. **Not a framing / writhe power of q₀.** `log(rust/peel)/log(q₀) =
   −0.0013559869167486641314` — not an integer, so the arbiter's own
   writhe-match idiom (*"integer ⇒ writhe match"*) excludes it.
2. **Not per-crossing.** The deuteron is `n = 6`; tritium and ³He are `n = 9`,
   with different crossing counts. A per-crossing discrepancy would compound to
   different totals. The ratio is identical to **17 significant figures**.
3. **Not per-strand and not per-nucleon.** Same argument, and sharper: a
   per-nucleon factor `f^A` would give `f²` for the deuteron (A=2) and `f³` for
   T and ³He (A=3). Identical ratio ⇒ the exponent is **0** ⇒ the factor is
   applied **exactly once, regardless of A**.
4. **Not Z/N dependent.** D (1,1), T (1,2) and ³He (2,1) span three different
   `(Z, N)` splits and give the same ratio, so the p/n colour weighting is not
   the differing step — despite the witness `convention` field naming it.

So: **one scalar, applied once, in the composite assembly only** — present for
every atom with A ≥ 2 and absent for both single nucleons. `1 − ratio =
1.41474643156097e-4`; `1/(1 − ratio) = 7068.4045`. Neither is identified, and
**no identification should be attempted numerically** — the anti-fit rule
applies with full force to a single measured ratio.

**One lead, unconfirmed.** `wenzl_lr.rs:250-262` documents an averaging-
convention change: the Rust path substitutes each averaged crossing directly as
`σ − (h/2)·I` (exactly `(σ + σ⁻¹)/2` under the Hecke relation, since
`σ⁻¹ = σ − (q − q⁻¹)`), and therefore reports `averaging_denominator = "1"` to
its Python consumer, where the pre-#682 implementation returned the
**unnormalised 2^k sub-word sum** and required caller-side division. A consumer
still dividing — or not dividing — on the wrong side of that contract is the
right *shape* of defect. **But it does not fit exclusion 2:** a `2^k` mismatch
is per-averaged-crossing and would differ between `n = 6` and `n = 9`. Recorded
as the nearest documented convention seam, not as the cause.

**Handoff.** The next step is reading the two composite assemblies side by side
— `hecke_canonical_chi.rs` / `wenzl_lr.rs` against the Python markov-peel — for
the one scalar that the A ≥ 2 path applies and the A = 1 path does not. The
exclusions above should make that a short search.

### Fifth exclusion: y_λ is NOT the differing step — refuted cheaply

The wrapper `canonical_tr_m_via_rust.compute_tr_m` takes its weights from a
**live** `y_lambda_at(n_strands, q_val)` call (line 184), while the peel /
Hoefsmit path reads them from the committed `y-lambda-mpfr-proton-witness.json`
via `tr_m_wenzl_bridge_mpfr._Y_LAMBDA_DEFAULT`. Two different sources for the
same weights is the right shape for a uniform scale factor, so it was worth a
test.

**Refuted.** `live/committed = 1.0` at **every** λ and every n — spread
`1.47e-50` (n=3), `4.68e-50` (n=6), `4.41e-50` (n=9), i.e. the serialisation
floor. The two y_λ sources are the same numbers.

### 🛑 An unresolved TENSION — record it, do not paper over it

With y_λ excluded, the divergence must be in χ. But the two facts do not sit
together comfortably, and the next agent should start here:

**Fact A — the per-λ χ differ NON-uniformly.** Rust's `chi_normalised` against
the `--fresh` chi producer's `chi_lambda`, deuteron, top 5 of 11 partitions:

| λ | rust/fresh |
|---|---|
| (6,) | `0.99992849311387155534` |
| (5,1) | `1.00007611045623214990` |
| (4,2) | `0.99981939581907000940` |
| (3,3) | `0.99983325648550264807` |
| (4,1,1) | `0.99983210335191548361` |

Spread `2.567e-4`, **both signs** — one ratio is above 1.

**Fact B — the y-weighted totals differ by ONE constant**, `0.99985852535684389…`,
identical to 17 significant figures across the deuteron (n=6, 11 partitions),
tritium and ³He (n=9, 30 partitions).

A non-uniform per-λ difference producing an *identical* weighted-sum ratio at
two different `n`, over different partition sets and different weights, to 17
digits, is not something that happens by accident. **Either Fact A or Fact B is
being mis-measured, or something structural forces the cancellation.** Two
candidate resolutions, neither tested:

- Fact A compares Rust against the **chi producer**, while Fact B compares Rust
  against the **markov peel** — a third object. Their *totals* agree to 49
  digits but their per-λ decompositions were never compared (the peel does not
  decompose per λ at all). The scatter may be chi-producer-vs-Rust and the
  constant Rust-vs-peel, i.e. two different comparisons that must not be read
  as one.
- Only the **top 5 of 11** partitions were compared (`compute_tr_m` returns
  `top5_contributions`); the full set may behave differently.

**First move for whoever picks this up:** get the full per-λ Rust χ (not the
top 5) and re-do Fact A against it, then check whether the y-weighted residual
actually reproduces `1.41474643e-4`. If it does not, Fact B's constancy needs
re-deriving before anything is concluded from it.

### 🛑 The "tension" above is RESOLVED — and it was my arithmetic, not the data

The section immediately above asked whether Fact A (non-uniform per-λ χ
differences) and Fact B (a constant weighted-total ratio) could both be true.
**They can, and the check is one line I had not run:**

    sum_λ y_λ · (rust_χ_λ − fresh_χ_λ)  =  −2.14996665599e-5
    observed  rust_total − peel_total   =  −2.1499666559943e-5

Exact agreement. The per-λ differences **do** reproduce the total difference;
there was never a contradiction. I recorded a tension that a weighted sum
dissolves, having compared per-λ ratios by eye and never summed them.

Full per-λ table (all 11, not the top 5 — obtained by calling the binary
directly rather than through `compute_tr_m`, which returns only
`top5_contributions`): `rust/fresh` spans **0.999819 to 1.002563**, spread
`2.744e-3`, both signs; absolute `rust − fresh` runs `6.5e-6` to `2.0e-4`. The
four λ with non-vanishing `y_λ` carry it: `(6,)` `−1.115e-4 × 0.1153`, `(5,1)`
`−5.19e-5 × 0.0790`, `(4,2)` `−5.94e-5 × 0.0460`, `(3,3)` `−1.19e-4 × 0.0151`.

### Where that leaves the two candidate values

**Two independent routes against one.** The markov peel and the Hoefsmit+Wenzl
bridge are distinct algorithms and agree at `1e-51` on the single nucleons; the
`--fresh` chi producer is a third script agreeing with the peel to 49 digits.
Rust is the outlier, disagreeing per-λ at ~1e-4.

This is **evidential balance, not a verdict** — two-against-one is not proof,
and the right comparison is against an exact symbolic evaluation, which none of
these three is. But it inverts the earlier prior: the Rust kernel is the
*likelier* one to be wrong, not the peel.

Note the spec sends **both** `q` (f64, `1.1099785827513808`) and `q_str` (the
50-digit string), and the binary echoes only the f64 `q` at top level while
reporting `precision_dps: 50` per term. **A wrong-`q` explanation does not
survive arithmetic**: a 1e-17 error in `q` propagates to ~1e-16 in χ, twelve
orders below the observed 1e-4. So the per-λ differences are structured, not
precision noise, and which of `q`/`q_str` the kernel consumes is worth
confirming but cannot be the cause.

### The ONE thing still unexplained

The **relative** total difference is `1.41474643e-4` for the deuteron (n=6, 11
partitions), tritium and ³He (n=9, 30 partitions) — identical to **17
significant figures**. Now that the per-λ differences are known to be
non-uniform and to sum correctly, the cross-atom constancy of the *ratio* is
the remaining puzzle: nothing here explains why differently-weighted sums over
different partition sets land on the same relative offset to that precision.
That is the sharp open question, and it is the one worth chasing — a structured
per-λ error whose y-weighted relative residue is atom-invariant points at a
specific defect shape in the Rust composite path.

---

## ✅ LOCALISED — the Rust kernel drops the p–n interface colour weighting

The remaining puzzle (why the relative offset is atom-invariant to 17 digits) is
answered, and the two kernels' braid words are the same **except at exactly one
crossing**.

### The measurement

Decoding both wire formats to `(generator, crossing_type)` — Rust's
`[sign, gen+1]` pairs against the Hoefsmit `(c, d, gen_idx)` triples, mapping
`d = 0 → σ`, `d = −h → σ⁻¹`, `d = −h/2 → averaged`, with `h = q − q⁻¹`:

| atom | word length | positions where the two disagree |
|---|---|---|
| proton | 11 | **none** |
| neutron | 11 | **none** |
| deuteron | 23 | **{11}** |
| tritium | 35 | **{11}** |
| ³He | 35 | **{23}** |

**Exactly one crossing, once per composite atom, never for a single nucleon.**
That is the "one scalar applied once, composite-only" signature, found.

At that position the Python path carries a shift that is **not** `h/2`:

    h/2                     = 0.104530149397819657715423106565
    Python shift at that pos = 0.104458247769726289017834066290
    ratio                   = 0.999312144596486452   (rel 6.87855e-4)

Rust encodes the same position as crossing **type 0 = plain averaged**, i.e. it
uses `h/2` and loses the modification.

### What that shift is

It is the **p–n interface colour weighting**.
[`mass_at_3A_proper.py:532`](computations/mass_at_3A_proper.py) states *"The p-n
interface is color-weighted by default (owner directive…)"*, and line 454
defaults `pn_convention: str = "bring_color_weighted"` — owner ruling **R3**,
`bring_color_weighted` canonical (2026-08-15). A single nucleon has no p–n
interface, which is exactly why p and n agree at `1e-18` while every composite
differs by the same fixed factor regardless of A, Z, N.

### The verdict this supports

**The Rust `hecke-canonical-chi` kernel does not implement the p–n interface
colour weighting**; it substitutes a plain averaged crossing. Therefore:

- `0.1519683392…` (markov peel, Hoefsmit+Wenzl bridge, `--fresh` chi producer)
  is the **colour-weighted** value — consistent with the witness's own declared
  `convention: colour-weighted-averaged-crossing` and with R3;
- `0.1519468395…` (Rust) is the **un-colour-weighted** value;
- and the committed cache's `0.5751722439…` is neither, being superseded on the
  y_λ axis as well (see the top of this bean).

So the canonical live deuteron trace is **`0.15196833920423160759…`**, and both
the committed `chi-*-at-q0-50dps` family and the Rust kernel are wrong, for two
*different* reasons.

**One step not verified:** that the specific value `0.104458247769726289…` is
what `bring_color_weighted` prescribes, as opposed to some other modification at
the same position. The position (p–n interface), the default
(`bring_color_weighted`), the source comment and the A/Z/N-invariance all point
one way; the arithmetic tying that number to the colour-weight formula was not
re-derived here.

### Revised next steps

1. **Fix the Rust kernel** to honour the p–n interface colour weighting, or
   document `hecke-canonical-chi` as un-colour-weighted and stop using it as an
   arbiter for composites. It currently reports a convention it does not
   implement.
2. **Then** regenerate the `chi-*-at-q0-50dps` family — the blast radius is every
   reader of those witnesses, `option_e_multi_isotope_delta_lambda_probe_v3`
   included.
3. Re-run `qou-r9dv`'s three-method certification; the "three independent
   methods, exact to every digit" of 2026-08-23 cannot hold across a
   `1.41475e-4` kernel split.
4. Separately: `atom_braid_word_3A` builds `h` from a **float64** — the word
   carries `mpf('-0.20906029879563932')`, `2.19e-17` relative from the 50-dps
   `h`. Far too small to be this defect, but it is a NO-FLOAT64 leak on the
   canonical path and wants its own fix.

### ✅ The last unverified step is now verified — δ matches exactly

The previous section flagged one gap: that `0.104458247769726289…` is what
`bring_color_weighted` prescribes, rather than some other modification at the
same position. **Closed.**

`atom_braid_word_3A`'s docstring gives the formula — *"its averaged crossing is
`σ − h·(1/2 − δ/4)·1`, δ = flavor_split_…(q₀), vs the color-blind `σ − h/2·1`"*.
Inverting the measured shift for δ:

    δ implied by the measured shift : 0.0013757108070270960086
    flavor_split_leading(q_0)       : 0.0013757108070270960086

**Identical to all 20 digits printed.** The p–n interface crossing is
`σ − h·(1/2 − δ/4)` with `δ = flavor_split_leading(q₀)`, and the Rust kernel
substitutes the colour-blind `σ − h/2`. Nothing in the localisation is now
unverified.

### Two smaller defects found on the way

1. **`pyhecke.gram.h` is float64 on the canonical path.**

       pyhecke.gram.h        = 0.20906029879563937
       h = q − 1/q at 50 dps = 0.20906029879563931543084621313
       relative                2.61e-16

   `atom_braid_word_3A`'s own `q=None` default path reads it (the docstring
   says so: *"uses the canonical q₀ data (`pyhecke.gram.h`, `_avg_color_delta`)
   and is byte-identical to the historical word"*). So the byte-identity is
   deliberate back-compat, not an oversight — but it means every default-path
   word carries ~16 good digits of `h` into a 50-dps computation. The
   q-parameterised path (`q=` supplied) computes `h` exactly. Far too small to
   be the kernel split (2.6e-16 against 1.4e-4) and worth its own fix.
   *(An earlier note in this bean quoted 2.19e-17 for this; that was measured
   against the word's serialised literal. 2.61e-16 is the constant itself, and
   is the figure to use.)*

2. **The docstring names the wrong function for δ.** One sentence says
   `δ = flavor_split_subleading(q₀)`, another says `δ=flavor_split_leading(q)`.
   The measurement above settles it: **`flavor_split_leading`**. A one-word doc
   fix, but the two names are a symbol collision of exactly the kind that costs
   a session.

### Status of this bean

The investigation is **complete**; what remains is remediation, and every item
changes canonical numbers, so none of it should land without owner sign-off:

1. Fix `hecke-canonical-chi` to apply the p–n interface colour weighting, or
   document it as colour-blind and stop using it as a composite arbiter. It
   currently reports `convention: colour-weighted-averaged-crossing` for a
   computation that is not colour-weighted.
2. Regenerate the `chi-*-at-q0-50dps` family off the cache.
3. Re-run `qou-r9dv`'s three-method certification.
4. Fix the `pyhecke.gram.h` float64 leak.
5. Fix the δ docstring.

Items 4 and 5 are independent of 1-3 and safe to land on their own.

### 🛑 Correction to my own remediation list: item 4 is NOT safe to land alone

The status list above says *"Items 4 and 5 are independent of 1-3 and safe to
land on their own."* **Item 4 is not**, and the reason is in the docstring I had
already quoted two paragraphs earlier: `atom_braid_word_3A`'s `q=None` default
*"uses the canonical q₀ data (`pyhecke.gram.h`, `_avg_color_delta`) and is
**byte-identical to the historical word** — all existing callers omitting `q`
are unaffected."*

That byte-identity is a **deliberate contract**, and every default-path caller
depends on it. Replacing float64 `pyhecke.gram.h` with the exact `h` breaks it
and moves every default-path word — and therefore every downstream `tr_M` — at
~2.6e-16. That is inside L1 (1e-15), but it dirties witnesses corpus-wide and is
exactly the kind of change this bean exists to stop happening unannounced.
**Item 4 belongs with 1-3, behind owner sign-off.**

Only **item 5** was safe, and it is done: the docstring at
`mass_at_3A_proper.py:534` said `δ = flavor_split_subleading(q₀)` (line-wrapped,
which is why a grep for the full name found nothing) where both the code
(lines 594-595) and the measurement say `flavor_split_leading`. The two are
distinguishable, not a near-tie:

    flavor_split_leading(q₀)    = 0.001375710807027096008551
    flavor_split_subleading(q₀) = 0.001377048965992554505398
    measured from the word      = 0.0013757108070270960086
    relative separation           9.727e-4

`leading` matches to 22 digits; `subleading` differs at the 4th significant
figure. Corrected; the emitted word is unchanged (verified: the deuteron idx-11
shift is byte-identical after the edit).

## Implementation & Witness Progress (PR #8269)
- Branch: `qou-10v9-07ts-324i-49vn-4pdh-5mxd` (`7a961cf268c0cf36c3f70fd39f92645c16c9a30a`), PR: `litlfred/qou#8269`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/chi_rust_nondeterminism_override_blindness_chi_cache_staleness_qmp_digit_cap_and_magnus_far_commutativity_probe.py` -> `computations/probes/chi-rust-nondeterminism-override-blindness-chi-cache-staleness-qmp-digit-cap-and-magnus-far-commutativity.witness.json` (`allPassed: true`, `scriptCommitSha: e7b85e53d7a8855337daf870617a2e9a6b0acc11`)
