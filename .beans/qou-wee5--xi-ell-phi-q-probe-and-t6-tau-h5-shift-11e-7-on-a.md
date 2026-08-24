---
# qou-wee5
title: xi_ell_phi_q_probe and t6_tau_h5 shift 1.1e-7 on a manifest entry they never reference
status: completed
type: bug
priority: normal
created_at: 2026-08-23T22:25:49Z
updated_at: 2026-08-24T13:11:37Z
---

## What

Two probes change their computed output when a stem is added to
`computations/q0_anchor_manifest.json` — **a file neither of them references**,
directly or through any visible import.

Isolated properly, one stem at a time on an otherwise clean tree:

```
ideal_muon += {"xi_ell_phi_q_probe"}      # nothing else changed
-> max_abs_V   0.3164349897485959  ->  0.3164350254931353     (1.13e-7 rel)
   m_li2q_sym  0.29449812380443614…  ->  0.29449815487914650…
   m_phi_direct, m_log_phi, and 38 further fields also move
```

`t6_tau_h5_embedding_probe` behaves the same way, 15 fields.

## Why this is a straddle, not a re-pin

Both probes derive q₀ **inline**, from the muon ratio:

```python
from codata_2022_source import M_MU_OVER_M_E
cal2_target = M_MU_OVER_M_E
hbar_q_sq   = Vol_4_1 / cal2_target
hbar_q      = mp.sqrt(hbar_q_sq)
q0          = mp.mpf(1) / (mp.mpf(1) - hbar_q)
```

That is `q_muon_at()`'s closed form retyped, and it does **not** consult the
manifest. So the q₀ these probes use is muon *whatever the manifest says* — and
yet a manifest entry moves their numbers by 1.1e-7. **Something else in their
import cone resolves through the anchor**, and the two sources are combined in
one computed quantity. That is the layer straddle AGENTS.md calls a defect
regardless of size.

Grepped and confirmed absent from `xi_ell_phi_q_probe.py`: `q_parameter`,
`qou_substrate`, `Q_50_DIGIT_STR`, `q_at(`, any `from constants` import. So the
dependence arrives through the cone (`_path_bridge`, `codata_2022_source`,
`_precision`, or a sibling probe), and **which input carries it is not yet
located** — that is the open question here, not the existence of the effect.

## Scale

1.13e-7 relative is ~113 ppb: about **10× the 11.5 ppb μ–p substrate tension**
and ~1e8 × the 1 ppQ L1 compute-precision target. Large enough that any
conclusion drawn from these probes depends on a manifest entry nobody would
think to check when reading them.

## Not fixed here, deliberately

The guard in the `qou-bdkx` re-bucketing run caught this and **reverted** both
(the rule being: keep a manifest move only if the stamp moved and no
mathematical field did). Both stems stay out of `ideal_muon`. Re-bucketing them
would be a *migration* — it changes numbers — not the label correction the rest
of that arc was.

Their sibling `t6_three_halves_factor_probes`, with the **identical** inline
derivation, was stamp-only and was re-bucketed. So the dependence is not a
property of the shared formula; it is something these two reach and it does not.
That contrast is the cheapest lead.

## Next

1. Bisect the import cone. Add the stem, then re-run with each cone module
   swapped for a stub, until the 1.1e-7 moves or stops.
2. Diff the cone against `t6_three_halves_factor_probes`, which does **not**
   show the effect despite the same q₀ derivation — the difference between the
   two cones is where to look first.
3. Once located, decide whether the correct fix is to pin the second source
   explicitly or to remove it. Do **not** re-bucket the stems until then.


---

## LOCATED (2026-08-23) — a defaulted parameter, three modules down

The carrier is found, and the chain is verified end to end rather than inferred.

```
xi_ell_phi_q_probe.py
  |- q0  derived INLINE from M_MU_OVER_M_E                    -> muon, always
  `- per_generator_V_hat_general.py:94
         _cached_seminormal(shape)            <-- NO q ARGUMENT PASSED
           `- mass_at_3A_proper.py:64
                  from q_parameter import Q as Q0             -> MANIFEST-RESOLVED
```

`_cached_seminormal`'s own docstring: *"`q` defaults to the module-level
`Q0` (float64) … Seminormal (Young orthogonal) matrices for `shape`, built
**AT `q`**."* So the seminormal matrices — and therefore `V̂` — are built at
whatever the **manifest** resolves, while the probe's own `q0` is the inline
muon value. Two layers, one computed quantity.

### Confirmed by the anchor, not just by reading

```
QOU_Q0_ANCHOR unset      max_abs_V = 0.3164349897485959
QOU_Q0_ANCHOR=physical   max_abs_V = 0.3164349897485959
QOU_Q0_ANCHOR=ideal      max_abs_V = 0.3164350254931353     <- the shifted value
```

The env override reproduces the manifest-entry shift **exactly**, which pins the
mechanism on `q_parameter` resolution and rules out anything else in the cone.

### A false lead worth recording

`per_generator_V_hat_general.py:46` is `from q_parameter import Q as Q0_FLOAT`
— which looks like the answer and **is not**: `Q0_FLOAT` appears exactly once
in the file and is never used. A dead import cannot move a number. The live
path is the defaulted parameter one module further down, which is the more
invisible form: **nothing at the call site mentions an anchor at all.**

### Population of the same latent shape

`_cached_seminormal` call sites across `computations/`, `tools/`,
`qou-mass/` (excluding `_deprecated` and the def itself):

| | n |
|---|---|
| pass `q` explicitly | 6 |
| **default it** | **22** |
| total | 28 |

Every defaulted site inherits the manifest anchor silently. That does not make
them all straddles — a site whose *only* q is the manifest one is consistent,
not mixed. It becomes a straddle exactly when the caller ALSO has its own q,
which is the `xi_ell_phi_q_probe` case. Each needs the same check.

## The decision this needs, and it is not mine

Fixing it means passing an explicit `q` at
`per_generator_V_hat_general.py:94`, which **changes that probe's numbers**.
Which q is correct is a judgement:

1. **The probe's inline muon `q0`** — self-consistent with the rest of the
   probe, and makes `xi_ell_phi_q_probe` cleanly muon.
2. **The canonical proton pin** — the 2026-08-07 default for compute, but then
   the probe's own inline derivation is the thing that is wrong.

Option 2 arguably makes the inline re-derivation (`qou-5le1` Mode A) the real
defect across all 9 files that do it. Option 1 keeps them and fixes the call
site. That is a scope call about the muon layer, not a bug fix.

Secondary, and separate: `mass_at_3A_proper`'s `Q0` is the **float64** `Q`,
so the seminormal matrices are built in float64 regardless of which anchor wins.


---

## The method generalises — 3 of 9 inline-derivation producers straddle (2026-08-23)

Packaged as
[`computations/audits/anchor_flip_straddle_audit.py`](computations/audits/anchor_flip_straddle_audit.py).

**Why empirical rather than static.** A per-file scan of the 16 files holding a
defaulted `_cached_seminormal` call reports **one** candidate — and misses
`xi_ell_phi_q_probe` entirely, because there the manifest value arrives three
modules down through a defaulted parameter. Nothing in that file names an
anchor, so no grep can find it. Static analysis is per-file; the interesting
straddles are not.

**The test.** Run the producer twice, `QOU_Q0_ANCHOR=physical` then `=ideal`,
and diff its witnesses with ephemeral fields *and the q₀ stamp* masked.

Scope is what makes it a straddle test rather than a re-pin test: a producer
whose **only** q is the manifest one *should* move — it is following the
anchor, correctly. A producer with its **own** q that also moves is mixing two
sources. So the audit is run over producers that derive or hardcode a q of
their own (`--candidates` = the inline-derivation set, `qou-5le1` Mode A).

### Result over the 9

| verdict | n | |
|---|---|---|
| **STRADDLE** | **3** | `per_generator_V_hat_general` (24 fields), `xi_ell_phi_q_probe` (36), `t6_tau_h5_embedding_probe` (15) |
| clean | 4 | flip moves nothing but the stamp |
| RUN-FAIL | 1 | `lepton_tower_probe_1_cinquefoil_muon` — **untested, not clean** |
| excluded | 1 | `q_beta_complex_q_test1_phaseA_v2` computes the *inverse* (`cal2_q0` from a given q₀, a consistency check), not an inline q₀ |

**The third one is new and is the interesting one.**
`per_generator_V_hat_general` is not only the module that carries the defect
into the other two — it is a **producer in its own right**, and it straddles:
24 fields move, including `/electron_V_hat_calibration_check/computed_value`. A
calibration check whose computed value depends on which anchor the manifest
happens to resolve.

All three straddle through the **same** defaulted `_cached_seminormal(shape)`
call, so one call-site fix closes all three — which is why the option-1-vs-2
decision below governs three producers, not one.

The audit restores every witness it touches and exits 1 when any straddle is
found, so it can gate.


## The named carrier is WRONG — measured 2026-08-24 (PR #5634)

This bean names a defaulted `_cached_seminormal` as the carrier of the 113 ppb.
It is not. Three hypotheses tested and refuted in order:

1. the defaulted call site         -> fixed (q now REQUIRED, 18 sites named)
2. the module's defaulted params   -> fixed (9 repointed to constants.Q)
3. `QI` / `HA_VAL`                 -> fixed (repointed)

After all three: `xi_ell_phi_q_probe` still moves **36** fields,
`t6_tau_h5_embedding_probe` still **15**.

**The real carrier**, from a cross-anchor diff of every module-level float in
the cone: the shim rebinds ~**20** derived constants (HA, Q_INV, HBAR_Q, LN_Q,
E_CROSS + _MP/_ERR variants), so every module importing ANY of them tracks the
entry point. `hecke_core` alone carries a dozen that move —
ALPHA_EM_INV_DERIVED 137.03593509 -> 137.03594594, E_HARTREE_EV, E_MOL,
FIG8_A_BULK. That is **qou-1c4y territory** with its sign-off gate.

**Blanket 'default to proton' is wrong for a muon producer.** Forcing proton at
`vhat_per_crossing_chain` flipped its internal `scalar_vs_matrix_agree`
True -> False (17 fields). Both muon producers now pass their own q; re-measured,
each moves 0.


## CLOSED — the carrier is the PLANCHEREL WEIGHTS, and the gate is drained (2026-08-24)

Fourth hypothesis, and this one holds. `per_generator_V_hat_general` builds its
Plancherel weights as `dq**2 / nfac` from `hecke_characters.qfac` and
`dim_q` — **neither of which takes a q at all**. They use the module-level
`q_int`, which closes over `q_parameter.Q`: the SHIM's Q, rebound to muon
whenever the entry-point stem is manifest-listed.

That is why two probes deriving q₀ inline from the muon ratio, referencing the
manifest nowhere, still moved 36 / 15 fields when a stem was added to it.

**Fix:** `qfac(n, q=None)` and `dim_q(shape, q=None)` gain an OPTIONAL explicit
q (backwards compatible — verified identical values with and without, so all 135
existing call sites are unaffected), and `per_generator_V_hat_general` names
`Q0_PROTON` for both.

**Measured after:**

    anchor-flip straddle audit --candidates:  clean=8, STRADDLE=0

versus 3 of 8 before. The blocking gate added in PR #5636 is fully drained.
Re-running the shared producer moves **0** non-ephemeral fields, so the fix is
inert under normal (proton) operation.

**Still open, and now sized:** `qfac`/`dim_q` have **135 defaulted call sites
across ~70 files** (dim_q 78 of 119, qfac 57 of 59). Those still track the entry
point. Threading q through all of them is a real migration, not a session task —
but nothing straddles today, because the only producers that combined two
layers went through this one function.
