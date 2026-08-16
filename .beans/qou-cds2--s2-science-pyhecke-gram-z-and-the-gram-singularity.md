---
# qou-cds2
title: 'S2 (SCIENCE): pyhecke.gram.z and the Gram singularity — the ruling answers the convention, not the singularity'
status: completed
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-16T11:29:16Z
---

Parent: `qou-cdx1`. Predecessor: `qou-wgta` item 11. **Highest-risk item in the
plan.** Blocks `qou-cdh2`.

## The state the ruling inherits

`trace-convention-registry.json → blocked_migrations[0]` was the registry's only
`owner_decision_required: true`:

> `tools/pyhecke/python/pyhecke/gram.py::z` **stays C**, because
> `G_INV = np.linalg.inv(G)` runs at **module import**, and under D the
> Markov–Gram form on the `H₃(q)` NF basis is **SINGULAR** — exactly one null
> direction (the row-cap one).

Measured at the proton pin: bilinear eigenvalues
`−0.752702, 0, +0.752702 ×3, +4.230339`; `det 3.998e-17`; `cond 4.9e16`.
**numpy raises nothing** — it returns entries up to `7.6e15` with
`‖G·G_INV − I‖ = 1.64`. Switching that one line silently corrupts every consumer
of `G_INV`.

**The 2026-08-15 ruling removes the convention question. It does not remove the
singularity.** That is the whole content of this bean.

## Corank accounting

`n=3` corank 1; `n=4` corank 10 (`3²+1²`); `n=5` corank 78 (`6²+5²+4²+1²`).

## The named repair

Quotient by the radical — `QOU/QBeta/GramSignature.lean`. Post-retraction the
quotient is a genuine **positive-definite** inner product, so the repair is more
attractive than it first looked. The supporting Lean already exists in
`QOU/QBeta/MarkovGramDegenerate.lean`:

1. `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the pin forces `y_(1³) = 0`
2. `block_mem_radical` — a zero-weight block lies in the trace radical
3. `gram_det_eq_zero_of_radical_combination` — hence `det G = 0`
4. `TemperleyLiebTower.traceRadical_two_sided` — the quotient is a ring
5. `pairing_descends` — the pairing is constant on radical cosets
6. `mem_radical_of_pairing_zero` — and is non-degenerate on the quotient

## Signature caveat — quote only the post-retraction statement

Quote `QOU.QBeta.GramSignature` **only after** its in-file retraction (commit
`748ba9b1`). The original *"(5,1) under C, (4,1)+null under D, LORENTZIAN"* used
the **bilinear** pairing and is **WITHDRAWN**. The Hecke `*`-structure is
`T_w* = T_{w⁻¹}`, giving C `(6,0,0)` positive definite and D `(5,0,1)` positive
semidefinite. The **singularity** under D is common to both pairings and is the
only thing the dependent blocks rely on.

## Blast radius

`G_INV` is **exported at import**, so every consumer of `pyhecke.gram` is
affected — that is the 13 re-exporters + 13 consumers of `qou-cdh2`, plus
whatever imports `gram` directly.


---

## ⚠ PREMISE CORRECTION (2026-08-16, `qou-cdh1`) — READ BEFORE STARTING

**The repair this bean names has already shipped.** S2 is scoped as
"`pyhecke.gram.z` and the Gram singularity", with the named repair *"quotient by
the radical, `QOU/QBeta/GramSignature.lean`"* and `G_INV = np.linalg.inv(G)`
running at module import. As of commit `6086572c4` (2026-08-15, *"gram.py:
convention D, quotient inverse — library core done"*):

- `gram.py:175` → `z = q0 ** 3 / (q0 ** 2 + 1)` — **convention D**
- **`G_INV` is deleted**, deliberately left undefined and explicitly "not a
  rename" (`gram.py:20,91,401`); `G` is inverted on the quotient `H₃/rad`

That commit **precedes** the ruling audit's own commit `c8796c283`, so the
audit's §2.2 premise was already false when written — it was measured from the
registry's stale `blocked_migrations[0]` row rather than from source. Full
correction in `resolved_migrations[0].premise_correction`.

**What is actually still open.** Not the float64 `z`, and not `G_INV`. The
50-dps **mpmath path** is unmigrated and still convention C — `z_mp()` (L622),
`tr_m_mp()` (L637), `gram_matrix_mp()` (L719), `tr_m_mp_strings()` — with
`tr_m_mp()`'s docstring still asserting it is "in lockstep" with the float64
path it now diverges from by 18.5%. `6086572c4`'s own message says **"TWO
coupled sites found"**. Two live consumers: `computations/atom_dual_q0_mpfr_demo.py:47`
and `computations/probes/qbeta_braid_nf_sdp_offset_probe.py:127,232`.

The singularity analysis in `resolved_migrations[0].reason` is still the
clearest statement in the repo of *why* the full Wedderburn Gram cannot be
inverted under D, and is still true — it is the justification for the quotient,
not an open question.

**Suggested re-scope:** S2 becomes "migrate the `pyhecke.gram` mpmath path to D",
and it is not `qou-cdh2`'s blocker.


### Addendum (2026-08-16, `qou-cdh1`) — a fourth C site, in a module no waiver covers

Surfaced by splitting the producer audit's pyhecke bucket into
*blocked* / *declared* / *unexplained*. The old blanket "unexplained" label was
hiding it behind `gram.py`'s three:

```
tools/pyhecke/python/pyhecke/atom.py:691   z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)
                                    :713   Vs = z_mark * a_arr[i] + b_arr[i]
```

**Live and consumed**, inside `atom_per_generator_volumes(Z, N, ...)`. It is in
`pyhecke.atom`, **not** `pyhecke.gram` — so `intra_module_split_waivers`
(`["pyhecke.gram"]`) does not cover it, it has no `blocked_migrations` row, and
it is not in `evaluators.z`. Nothing declares it anywhere.

It has reach: `atom_per_generator_volumes` is in `gram.py`'s `__all__` (:501)
and `gram.py:888-891` dispatches to the native implementation and **falls back
to the Python one**, with `hecke_core.py:138` and the generated
`qou-mass/src/qou_mass/_internal/hecke_core.py` both importing it. Note that
the native/Python fallback pair is exactly the `qou-j6il` hazard shape — a
binary returning one convention while its source reads another — so the two
implementations should be compared at `q₀` before either is trusted.

Not migrated here: `pyhecke` is your scope. Recorded so the count stops
understating it — the producer audit now reports it as `1 site / 1 file,
tools/pyhecke — C with NO registry row (unexplained)`, ACTIONABLE.


---

## Done 2026-08-16 — the mpmath path is convention D, and the risk was mis-located

**Claimed after `qou-w8zz` closed**, which removed the "pyhecke is someone's
active scope" reason this sat.

### The premise, once more, and where the real risk was

The plan called S2 *the highest-risk item*, on the grounds that `G_INV =
np.linalg.inv(G)` runs at import and goes garbage under D. That was already
false when written (`G_INV` was deleted in `6086572c4`; see
`resolved_migrations[0].premise_correction`). What was actually left was the
**50-dps mpmath path**, still convention C:

```
z_mp()            L622   1/(q^½ + q^−½)        -> q³/(q²+1)
tr_m_mp()         L637   same substitution     -> same
gram_matrix_mp()  L719   same substitution     -> same
```

`z_mp`'s own docstring justified staying on C as being *"in lockstep with the
module's float64 `z`"* — and that justification **outlived its premise** by a
day: the float64 `z` moved to D on 2026-08-15. A stale justification is harder
to see than a stale value, because it reads as a reason.

**The migration was safe for the reason the plan could not see:** `gram_matrix_mp`
only BUILDS G and never inverts it, so the corank-1 singularity that forced
`G_INV`'s deletion is not a hazard on this path at all. Verified: `z_mp()` and
the float64 `z` now agree to **4.1e-18**, i.e. to float64's own limit. The
18.5 % divergence behind one import is closed.

### Consumers: four, not the two I claimed earlier

My earlier count grepped only `tr_m_mp*` and missed the `gram_matrix_mp`
consumers. All four re-run:

| consumer | result |
|---|---|
| `probes/qbeta_lorentzian_gram_offset_probe.py` | exit 0, 3/3 — **Lorentzian (4,1) signature survives D** |
| `probes/qbeta_confinement_sdp_offset_homogeneity_probe.py` | exit 0, 2/2 |
| `atom_dual_q0_mpfr_demo.py` | exit 0 with PYTHONPATH set; its bare-run `ModuleNotFoundError` and skipped witness emission are **pre-existing** (confirmed by stashing) |
| `probes/qbeta_braid_nf_sdp_offset_probe.py` | **exit 1 — see below** |

### The one real downstream consequence, and it is the singularity

`qbeta_braid_nf_sdp_offset_probe` asserts `G x* = nf` to `1e-40`. Under C, G was
invertible and it met that. Under D the residuals are **2.127e-10** (muon 4₁) and
**1.313e-10** (proton 𝔹₃) — the solve did not fail, it **lost thirty orders of
magnitude of precision**, which is the fingerprint of the corank-1 null direction.

So the singularity IS live, just not where the plan put it: not at an import-time
inverse, but at a downstream probe that solves against the mp Gram. The named
repair — quotient by the radical, `QOU/QBeta/GramSignature.lean` — is what that
probe needs, exactly as the float64 side already got.

**Not attempted here.** Changing an SDP probe from solving on the full NF basis
to solving on H₃/rad changes what it measures (x* is unique only modulo the
radical), and that is a science decision about the probe, not a library
migration. Its witness is committed **with the failure recorded**: a witness
claiming 1e-40 consistency the code no longer produces would be the stale-artifact
defect (taxonomy row 10), and the probe exits 1 and says so, which is the correct
failure mode.

### Registry

`evaluators.z` `pyhecke.gram.z_mp` and `tr_m_mp` C→D; `evaluators.derived`
`tr_m_mp[3]` and `tr_m_mp[5]` C→D — **R11 caught those two**, which I had missed
in the first pass, and that is precisely what R11 is for.
`intra_module_split_waivers` is now **empty**, not waived: the split is closed.
Validator `PASS (0 errors, 22 warnings)`, down from 23 — the R10 warning is gone.
Producer audit ACTIONABLE **4 → 1**; the survivor is `pyhecke/atom.py:691`.
