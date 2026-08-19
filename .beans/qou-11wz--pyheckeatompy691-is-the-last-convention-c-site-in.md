---
# qou-11wz
title: pyhecke/atom.py:691 is the last convention-C site in the producer layer — and it reaches the mass table
status: completed
type: task
priority: normal
created_at: 2026-08-16T11:18:21Z
updated_at: 2026-08-16T15:06:32Z
---

Parent: qou-cdx1. Surfaced by qou-2ixd's producer-audit bucket split; left open
by qou-cdh2 and qou-cds2, both of which closed around it.

## The site

    tools/pyhecke/python/pyhecke/atom.py:691   z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)
                                        :713   Vs = z_mark * a_arr[i] + b_arr[i]

Convention C, float64, live, inside `atom_per_generator_volumes(Z, N, ...)`.
It is in `pyhecke.atom` — a DIFFERENT module from `pyhecke.gram`, which is why
`intra_module_split_waivers` never covered it and why the blanket
"tools/pyhecke — unexplained" bucket hid it behind gram.py's three until the
audit's buckets were split.

After qou-cds2 migrated the gram mpmath path, this is the **only** actionable
convention-C site left in the producer layer: `convention-c-producer-audit.py`
reports `1 site / 1 file`, ACTIONABLE.

## Why it was not migrated with the rest — measured blast radius

Unlike the gram mpmath path (4 consumers, all probes/demos), this reaches
production. Live callers, excluding `_deprecated/`:

    computations/mass_table_comprehensive.py:337
    computations/brane_tower_isospin_diagnosis.py:177
    computations/li2q_fbor_expansion_probe.py:174
    computations/probes/adjacent_vs_full_probe.py:276,278,287

Live witnesses naming the path:

    computations/pyhecke-h3-vs-h3a-impact-comparison.witness.json
    computations/hecke-core-symbolic-migration.witness.json
    computations/vhat-per-crossing-chain.witness.json
    computations/p2-5-symbolic-q-audit.witness.json
    computations/rho-k-graded-atomic-mass.witness.json

And it reaches the SHIPPED package: `gram.py` exports the function in `__all__`
(:501) and falls back to this Python implementation (:888-891), which
`hecke_core.py:138` and the generated `qou-mass/src/qou_mass/_internal/hecke_core.py`
both import.

## Two gates before touching it

1. **The native/Python pair is the qou-j6il shape.** `gram.py:888-891` dispatches
   to `pyhecke_native` and falls back to this. qou-j6il was the trap where the
   installed .so returned `markov_z(q0) = 0.4993203341836945` (C) while its Rust
   source read D. Compare both implementations at q0 BEFORE migrating either, or
   you will migrate one arm of a pair and not know it.
2. **Order the cascade.** qou-eea0's lesson: producers read each other's
   witnesses, so a stale upstream propagates into a freshly-migrated downstream
   and the downstream output looks clean. Five live witnesses here, at least one
   (`rho-k-graded-atomic-mass`) in the mass chain.

## Why this needs sign-off rather than a hygiene pass

It moves mass-table numbers. The 2026-08-15 ruling makes D canonical, so the
DIRECTION is not in question — but the binding channel already got worse on
aggregate under D (mean |err| 37.39% -> 43.85%, recorded in the ruling audit as
the anti-fit discipline working as designed), and a mass-table movement should
be measured and reported deliberately, not arrive as a side effect.


---

## 2026-08-16 — migrated, and gate 1 found something bigger than a stale site

**Gate 1 (the `qou-j6il` shape) fired.** The installed `pyhecke_native` returns
`markov_z(q₀) = 0.6126880371464652` — convention **D**, matching its Rust source,
so the stale-`.so` trap itself is resolved. But comparing the two *arms of this
function* at q₀ for (Z,N) = (1,0), before any change:

| component | python | native |
|---|---|---|
| `sym` | 1.88038767606 | 1.88038780844 | agree |
| `alt` | −0.537616027272 | −0.537615990711 | agree |
| **`std`** | **1.14610143246** | **1.2824205802** | **DIFFER** |
| **`full`** | **0.989007228447** | **1.08021529448** | **DIFFER** |

`std` is exactly `z_mark * a + b`, and `sym`/`alt` — which never touch `z_mark` —
agree to float64 noise. So the divergence tracked the convention precisely.

**And it was not merely native-vs-fallback.** The two import routes are
permanently split, because `hecke_core` bypasses the dispatcher:

```
computations/substrate/hecke_core.py:132   from pyhecke.atom import (... atom_per_generator_volumes ...)
```

- `from hecke_core import …` — `mass_table_comprehensive.py`,
  `brane_tower_isospin_diagnosis.py`, `li2q_fbor_expansion_probe.py` → the raw
  **Python** implementation → **convention C**
- `from pyhecke.gram import …` — `probes/adjacent_vs_full_probe.py` → native
  dispatch → **convention D**

Two callers of the same named function, getting different physics, decided by
which module they imported it through. The shipped
`qou-mass/src/qou_mass/_internal/hecke_core.py:131` carries the same direct
import, so the package was on the C route too — and since it imports the real
library rather than vendoring `atom.py`, this fix reaches it.

**After the migration the arms converge:** worst |python − native| across
(1,0), (0,1), (1,1), (2,1), (2,2) and all four components is **1.3e-7** —
float64 noise.

`convention-c-producer-audit.py` now reports **ACTIONABLE: 0 sites**. That is a
measured zero from the detector that scans return forms, closed-form
specialisations, half-argument reciprocals and registry-derived buckets — not
the 2026-08-09 "0 actionable" that this campaign spent a week retracting. The
one remaining closed-form flag, `qbeta_5two…probe.py:132 ocneanu_weights`, is
the documented false positive: the file declares `t = symbols("t"); q = t**2`,
so the `sqrt` is its working variable and its `z` is D.

## STILL OPEN — the artifact cascade

The code is consistent; the artifacts are not yet. Five live witnesses name this
producer and were generated through the **C** route:

```
computations/pyhecke-h3-vs-h3a-impact-comparison.witness.json
computations/hecke-core-symbolic-migration.witness.json
computations/vhat-per-crossing-chain.witness.json
computations/p2-5-symbolic-q-audit.witness.json
computations/rho-k-graded-atomic-mass.witness.json
```

Movement is material: per-generator `std` moves ~+11.9 % at (1,0). Not
regenerated here — gate 2 (qou-eea0 ordering: producers read each other's
witnesses, so a stale upstream propagates into a freshly-migrated downstream and
looks clean) needs a deliberate cascade, and `rho-k-graded-atomic-mass` is in the
mass chain. Leaving them stale is taxonomy row 10 and is tracked, not ignored.

Note also: `atom_per_generator_volumes` emits a `DeprecationWarning` for A ≥ 2
("H_3 weights for an A=2 atom; H_{3A}=6 weights are correct — migrate to
`mass_at_3A_proper.per_generator_V_hat_3A`"), so part of this cascade may be
better served by retiring callers than by regenerating them.


---

## CORRECTION 2026-08-16 — the cascade is TWO witnesses, not five

I wrote "five live witnesses name this producer and were generated through the C
route" in the commit and above. **Three of the five are not in the cascade at
all**, and I would have regenerated them without checking:

| witness | status |
|---|---|
| `pyhecke-h3-vs-h3a-impact-comparison` | **affected** — `pyhecke_h3_vs_h3a_impact_comparison.py:54` does `from hecke_core import atom_per_generator_volumes`, calls it at `:92`. The C route. |
| `rho-k-graded-atomic-mass` | **affected** — same import at `:54`, called at `:68`. The C route. |
| `vhat-per-crossing-chain` | **not affected.** Its only hit is a *note string* at `:253` naming `terms_2_3_atom_per_gen_mpfr_50dps.atom_per_generator_volumes_mpfr` — a different function in a different module. It imports `_PROTON_G0/_G1`, `_NEUTRON_G0/_G1`, `vertex_volume` from `pyhecke.atom` and never touches the changed surface; `z_mark` is function-local. |
| `hecke-core-symbolic-migration` | **cannot be regenerated** — its own provenance reads *"legacy — no matching producer found; provenance pending manual triage"*. |
| `p2-5-symbolic-q-audit` | **cannot be regenerated** — `scriptFile: None`. |

### The error, and it is the third of its kind today

The list came from `grep -rl "atom_per_generator_volumes" --include=*.witness.json`.
That matches a **mention**. It does not distinguish:

- a witness whose producer *calls* the function (2),
- a witness whose producer merely *names* it in a note (1),
- a witness with **no producer at all** (2).

Three instances this session of the same disease — **a count taken from a text
match rather than a dependency check**:

1. *"151 fully coverable"* — coverage by numeric match, which is not provenance. Real: 2.
2. *"two mpmath consumers"* — grepped `tr_m_mp*` and missed the `gram_matrix_mp` callers. Real: 4. (**Under**-count.)
3. *"five stale witnesses"* — `grep -rl` on a name. Real: 2. (**Over**-count.)

Text matching is wrong in **both directions**, which is why "the grep looked
about right" is never evidence. The fix each time was the same and is cheap:
resolve the import, then check the call site.

Two of the three published counts in this campaign that turned out wrong were
mine and were caught by me before anyone acted on them; the discipline that
catches them is checking a suggestion that looks *right*, not only one that
looks wrong.


---

## CASCADE COMPLETE 2026-08-16 — both C-route consumers regenerated

| witness | result |
|---|---|
| `pyhecke-h3-vs-h3a-impact-comparison` | regenerated after **2 h** of compute (D, T, ³He, ⁴He at H₁₂). Ten payload fields moved: `max_rel_pct` 32.115 → 37.847, `max_abs_delta` +28.7 %. |
| `rho-k-graded-atomic-mass` | regenerated in seconds. All five assertions pass. |

Both verified: `scriptHash` matches `sha256(producer)[:12]`, shape guard 1
modified / 0 collapsed, each diffed against a scratchpad snapshot taken before
any other command ran.

### The fit got worse, and that is the honest headline

`rho-k-graded-atomic-mass`'s two numeric assertions are **error metrics against
an expected 0.0**, and both degraded:

```
single_gen_mean_abs_err_pct   0.19417797975754 -> 0.31012197793723
single_gen_max_abs_err_pct    0.29598094064313 -> 0.41310743187684
```

They still pass, on a tolerance loose enough to absorb it. This matches what the
ruling audit already records for the binding channel under D (mean |err| 37.39 %
→ 43.85 %) and the reason it gives: the convention was chosen on a structural
forcing **against** the aggregate fit. A migration that improved every number
would have been the surprising outcome.

### Three sources were conflated in that diff and are separated in the commit

Of 68 changed fields: the two error metrics are mine; `engineVersion` /
`environment.mpmath` `1.3.0 → 1.4.1` is the container (pre-existing — `pip
install gmpy2` reported only gmpy2, and the *committed* witness is the one from
the older environment); and `m_p_facade_MeV` moving `938.2720881603788 →
938.2720894273243` is a **calibrated facade** shifting at rel 1.35e-11, not the
CODATA input (`M_P_MEV = 938.27208816`, unchanged).

### What this cost, and what it bought — taxonomy row 13

`scriptHash` on `pyhecke-h3-vs-h3a-impact-comparison` read **`2b01c1d6a433`
before and `2b01c1d6a433` after**. The producer file never changed; the
staleness came through `pyhecke/atom.py`, a **dependency**. So the corpus's
staleness check answered *"current"* about a witness that was materially wrong —
correctly by its own definition, and wrongly in fact.

That is worse than rows 6 and 10 rather than another instance of them: those are
a record and an artifact going stale, both catchable by asking a checker. This
is the **checker** going stale. Recorded as row 13, with the repair — hash the
transitive import closure, not the entry file — and the interim rule: a matching
`scriptHash` is evidence the producer is unchanged, **never** that the witness is
current.
