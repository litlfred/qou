---
# qou-cblw
title: 'p-n interface factor: colour-BLIND z - h/2 where canonical is z - h*(1/2 - delta/4)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T21:35:00Z
updated_at: 2026-08-25T23:05:00Z
---

Found 2026-08-25 while validating an exact-rational evaluation pipeline for the
Habiro chi cache (bean `qou-lrnd`). My own first implementation had this exact
bug, which is how it surfaced: I mapped every non-`sigma` crossing to
`-h/2` and all 11 cached deuteron characters came back wrong — by a
*different* ratio per partition, not a global scale, which is the signature of
one wrong factor rather than a normalisation slip.

## The two forms

    colour-WEIGHTED (canonical)   z - h*(1/2 - delta/4)
    colour-BLIND                  z - h/2

with `z = markov_z(q) = q^3/(q^2+1)` (convention D), `h = q - 1/q`, and

    delta = flavor_split_leading(q) = (q-1)^2 * (1 - q^-4) / 3

(`computations/_li_2_q_util.py`, and `flavor_split_leading_sym` in
`computations/tr_m_algebraic_q.py`). Note delta is a RATIONAL function of q —
which is what makes an exact-arithmetic evaluation of the whole atom possible.

AGENTS.md records the owner ruling of **2026-08-15 (R3): `bring_color_weighted`
is the canonical p/n convention.** So `z - h/2` is wrong wherever canonical is
intended.

## Why it is a trap rather than a typo

`closed_form_tau_M.py` (~lines 305-330) documents the mechanism in its own
comments: `canonical_interface_kinds(...)` by default emits only
`{positive, negative, averaged}`. A consumer dispatching on those three and
mapping `averaged -> z - h/2` **silently gets the colour-blind factor**. In the
file's own words it "fails by returning a slightly smaller number rather than
by raising". The `averaged_weighted` label exists, and is opt-in via
`weighted_labels=True`, precisely so a consumer either handles the weighting or
raises on an unknown kind.

`interface_factor(kind, q)` handles only the three blind kinds and raises on
anything else — so it **cannot** emit the weighted value at all.

The Rust side documents both forms in
`tools/hecke-engine/src/color_weight.rs` (`z - h/2` for `strict_averaged`,
`z - h*(1/2 - delta/4)` for `bring_color_weighted`), with the comment that the
delta-aware value "lives in the factor layer, not the label layer".

## Scope of the sweep

A background agent is sweeping `computations/`, `tools/`, `content/` for:
1. p-n / averaged interface factors computed as `h/2`;
2. three-kind `{positive, negative, averaged}` dispatches with no
   `averaged_weighted` branch in factor-computing code;
3. callers of `canonical_interface_kinds` that omit `weighted_labels=True`
   and then compute a factor from the labels;
4. Rust callers hardcoding the strict/blind form where canonical is intended.

**Not every `h/2` is a defect.** Deliberate `strict_averaged` implementations,
C-vs-D comparison probes, and tests asserting the blind value on purpose are
legitimate and must be separated out. That separation is the substance of the
sweep, not the grep.

## Open

Sweep results pending. Any genuine finding changes a NUMBER, so each needs the
usual treatment: confirm the site intends canonical, check whether a committed
witness carries the blind value, and fix at the producer.


---

# 2026-08-25 — CONFIRMED 11-0 against the committed cache

`computations/probes/exact_rational_chi_gauge_probe.py` settles this from the
corpus's own numbers rather than from the ruling. Running one exact-arithmetic
pipeline over the deuteron's 11 cached symbolic characters, at three
independent rational `q`:

    colour-weighted   d = -h*(1/2 - delta/4)     11 / 11 match
    colour-blind      d = -h/2                    0 / 11 match

So the **committed chi cache is colour-weighted**. A consumer using `h/2` for a
p-n interface therefore disagrees with the corpus's own recorded numbers — not
merely with a convention preference. That raises the stakes on the sweep: any
genuine finding is a number that contradicts a committed witness.

The blind arm is kept in the probe permanently as the control; without it the
weighted result would be an assertion rather than a discrimination.


---

# 2026-08-25 — SWEEP RESULTS: 9 genuine, 24 benign, 3 borderline

Sweep complete. **9 genuine findings / 8 distinct defects**: 2 Python probes,
2 Rust sites (one module), 5 content blocks. 24 `h/2` sites were examined and
**excluded with reasons** — that separation is the substance; a raw grep would
have reported ~36.

I independently re-verified the four highest-stakes claims rather than taking
them on trust. All four hold.

## The finding that matters most

**`tools/hecke-engine/src/color_weight.rs` implements `PnConvention::
BringColorWeighted` and has ZERO callers.** Verified: its only mention anywhere
in `tools/` is `lib.rs:53: pub mod color_weight;`.

Meanwhile the blind form is what is actually wired, twice:

    gram.rs:726   nf = hm(&nf, 1.0, -half_h, 0, h);   // pn/np: mixed
    gram.rs:888   (1.0, -0.5 * h, m_pn.unwrap_or(crossings_per_pair))

inside `build_atom_nf` and `atom_per_generator_volumes`, both exported to Python
(`pyhecke-native/src/lib.rs:119-121, 139-151`) and dispatched from
`pyhecke/gram.py:994-1000`. Neither takes a `PnConvention` parameter.

**So the engine ships the canonical convention dead and the superseded one
live.** That is a sharper defect than a stale formula: someone wrote the
canonical module and never connected it.

Provenance worth recording: findings 3-4 are the byte-for-byte Rust port of
`hecke_core_legacy.py:598, 911, 1195` — which carries a `DEPRECATION-CANDIDATE`
banner saying "Symbols here are NOT on the canonical derivation chain". **The
port kept the numbers and dropped the banner.**

## Genuine findings

| # | site | note |
|---|---|---|
| 1 | `deltalambda/mu4_rhoF_cluster_derivation_probe.py:93` | `FAC = {"pp": Z, "nn": Z-H, "pn": Z-H/2}`; docstring calls these the "categorically-DERIVED" factors. Verified. |
| 2 | `deltalambda/wlambda_nuclear_braid_connected_probe.py:106` | p-n branch `(1, -H/2)` declared as *the* nuclear-quotient template |
| 3 | `hecke-engine/src/gram.rs:726` | `build_atom_nf` inter-nucleon crossing. Verified. |
| 4 | `hecke-engine/src/gram.rs:888` | `atom_per_generator_volumes`. Verified. |
| 5 | `mass-theory/canonical-braid-interface-composition-table1-data.md:4` | a **definition** block presenting blind as canonical |
| 6 | `appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md:225` | documents wire label `averaged` while citing a module that emits `averaged_weighted` |
| 7 | `mass-theory/eigenvalue-product-expansion-proof.md:12` | a **proof** block; its `[2]/2` eigenvalues follow only from `d = -h/2` |
| 8 | `mass-theory/knot-operator-transition.md:5-9` | every transition operator crosses p-n, all written blind |
| 9 | `mass-theory/crystal-bases-path-a-table1-data.md:5` | interface symbol, blind, unlabelled |

## Witnesses carrying a blind number

Discriminator at the proton pin: `z - h/2 = 0.50815788774…` vs
`z - h(1/2 - delta/4) = 0.50822978937…`, gap `h*delta/4 = 7.190163e-05`.

22 witness files contain the blind constant. Two are directly downstream of
genuine findings — `deltalambda/mu4-rhoF-cluster-derivation.witness.json`
(whose `description` calls the results "the DERIVED (0-fit, q0-only) rho_F
cluster integrals" — **verified**) and
`deltalambda/wlambda-nuclear-braid-connected.witness.json`. Three are
deliberate two-value comparisons and must NOT be drained. The remaining 17 are
unadjudicated.

## Not defects, recorded so they are not "fixed"

Three probes (`probe_9b_gate_interface_algebra`, `probe_9b_laurent_degree_10a5`,
`probe_9b_manybody_expansion`) key the label `"averaged"` to the WEIGHTED value.
They look exactly like the documented trap and are correct. `closed_form_tau_M.
py:238` is the *definition* of the blind kind and is right as written.

## Next

Not a sweep-and-replace. Each genuine site changes a number, so: confirm intent,
check the downstream witness, fix at the producer. The Rust pair (3-4) is the
highest-value single fix — wiring `color_weight.rs` in would close both, and it
is the one place where the canonical implementation already exists.

## 2026-08-25 — the two Rust sites now NAME their convention (`d85f1d581b`)

Not flipped — **named**. `gram.rs` open-coded `-0.5 * h` at both p-n sites
(items 3-4). They now call `color_weight::pn_offset{,_from_h}` under a
`GRAM_PN_CONVENTION` constant whose doc records that it is `StrictAveraged`
while canonical is `BringColorWeighted`, gap `h*delta/4 = 7.19e-05` at the
proton pin.

This also gives `color_weight.rs` its **first caller**. It was a fully ported,
self-checking, 50-dps-validated implementation of the canonical convention with
zero consumers outside its own tests — which is precisely how the blind form
survived next to it.

`gram_pn_convention_is_still_the_blind_one` asserts the live state, so the
eventual flip breaks a test by design: flip + corpus migration land in one
commit or not at all.

**Blast radius of the actual flip (measured, unchanged): 51 Python files, 18
committed witnesses.** Owner-scoped; not an agent edit. Item 3-4 is therefore
*prepared*, not closed.

### Verification lesson worth keeping

`cargo test --lib` reported **212 passed** and that proved **nothing** about
this change: the only atom tests in the suite are `build_atom_nf_vacuum` and
`build_atom_nf_hydrogen`, and **neither has a p-n bond**. A green suite over a
path no test crosses is not evidence, and I nearly reported it as if it were.

Established empirically instead: stashed the change and diffed `build_atom_nf`
+ `atom_per_generator_volumes` at 17 significant digits over deuteron / 4He /
7Li / 3He — identical. Now pinned in-suite as
`pn_offset_is_bit_identical_to_the_open_coded_form` (`assert_eq!` on `f64`,
deliberately not a tolerance).

### A structural note on `build_atom_nf`

It takes `(z, n, h)` — no `q` — so `delta(q)` is not directly reachable there.
That is a **soft** obstruction, not a structural one: `h = q - 1/q` inverts
uniquely on `q > 0` as `q = (h + sqrt(h^2+4))/2`. `pn_offset_from_h` does that,
is exact (no inversion) for the blind convention, and round-trips the
`q`-carrying form under both. Worth recording so the h-only signature is not
later cited as a reason the colour weighting *cannot* be applied there.

### One finding retracted mid-task

I planned to write a test asserting the two conventions differ by `h*delta/4`.
It **already existed** — `colour_weighting_is_a_real_shift_not_a_no_op`.
Corpus-grepped before writing, which is the only reason it did not become a
duplicate. Second time this session that the thing I was about to build was
already there.
