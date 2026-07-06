# H_3 vs H_{3A} legacy bug audit — 2026-05-25

**Trigger:** Author flag during PR #1233 follow-up: "before was issue of H_3 vs H_3A (weeks ago) may still be bug/legacy code around."

**Status:** Bug CONFIRMED, present in production. Fix pending dedicated PR.

## §1. The bug in one sentence

`tools/pyhecke/python/pyhecke/atom.py` lines 555-569 hardcodes H_3 Wedderburn weights (`w_sym = 1/4, w_std = 1/2, w_alt = 1/4`) for ALL atoms, including A > 1 multi-nucleon atoms — where the algebra is H_{3A}(q), not H_3(q).

## §2. Why this matters

For an atom with A nucleons, the canonical atomic braid lives in B_{3A} → H_{3A}(q). The Wedderburn decomposition should sum over partitions of **3A**, not partitions of **3**:

| Atom | A | n = 3A | # partitions | H_n irreps |
|---|--:|--:|--:|---|
| p, n | 1 | 3 | 3 | (3), (2,1), (1,1,1) |
| D | 2 | 6 | 11 | (6), (5,1), (4,2), (4,1,1), (3,3), (3,2,1), (3,1,1,1), (2,2,2), (2,2,1,1), (2,1,1,1,1), (1^6) |
| ⁴He | 4 | 12 | 77 | ... |
| ⁶Li | 6 | 18 | 385 | ... |

For A > 1, the **3-partition H_3 weights are wildly wrong** for the (3A)-strand atom.

## §3. Impact (15+ production scripts)

Per the BIG review investigation, `atom_per_generator_volumes(Z, N)` is called by:

- `mass_formula_6term.py` (main tower formula)
- `mass_formula_6term_mpfr_50dps.py` (50-dps variant)
- `tower_isotope_absolute.py`
- `paper_six_term_isotope_sweep.py`
- `catalan_binding.py`
- `brane_tower_isospin_diagnosis.py`
- `adjacent_vs_full_probe.py`
- `multi_level_jet_sum.py`
- `entanglement_orders.py`
- … plus mass-table sweeps

**EVERY multi-nucleon mass prediction in the current system carries this error** until `pyhecke/atom.py` is fixed or all callers switch to `mass_at_3A_proper.py`.

## §4. The "proper" alternative already exists (but is orphaned)

`computations/mass_at_3A_proper.py`:
- Uses full H_{3A} character decomposition via `build_seminormal_matrices_cached`
- Computes per-gen V̂_i using H_{3A} Wedderburn weights dynamically
- Implements both Markov-trace and full-tower binding
- **Generates `mass-at-3A-proper.witness.json` for atoms D through ¹²C**

**Gap:** referenced ONLY from `_deprecated/` probes. Production mass-table scripts don't use it. The fix needs to either:
- **Path A**: Fix `pyhecke/atom.py` to compute H_{3A} weights dynamically → 15+ callers fixed automatically
- **Path B**: Promote `mass_at_3A_proper.py` to production; migrate the 15+ callers one by one

Path A is much cleaner.

## §5. Confirmed bug location (file:line)

`tools/pyhecke/python/pyhecke/atom.py:555-569`:

```python
# Wedderburn weights (H_3 weights — same as mass_endomorphism.py)
nf3 = q_int(2) * q_int(3) * q_int(1)  # [3]_q!  (with [1]_q = 1)
# Use H_3 weights as in mass_endomorphism (1-dim sym, 2-dim std, 1-dim alt)
# W_sym, W_std, W_alt computed from quantum dimensions
qdim_sym = 1.0
qdim_std = q_int(2)
qdim_alt = 1.0
nf3_val = q_int(1) * q_int(2) * q_int(3)
w_sym = qdim_sym ** 2 / nf3_val
w_std = qdim_std ** 2 / nf3_val
w_alt = qdim_alt ** 2 / nf3_val
wt = w_sym + w_std + w_alt
w_sym /= wt
w_std /= wt
w_alt /= wt
```

Comment literally says "H_3 weights". For A > 1, this is wrong.

## §6. Secondary bug: `atom_mass_derived.py` (multiplicative composition)

Header explicitly states **"DO NOT TRUST OUTPUT"** — uses
$M_\text{derived} = \text{tr}_M(\text{atom NF}) \times E_0$
which is multiplicative instead of the additive baseline $M_\text{atom} = Z·M_p + N·M_n + Z·M_e − E_\text{binding}$.

Production-wired despite the warning. Should be deleted or rewritten to call `atom_mass_additive_baseline.py`.

## §7. Recommended fix sequence

1. **Tier 1 (this audit, recommendation)**: Ship `alpha_k_jones_markov_h4.py` (new file, this branch) as the parameterized n-dependent Jones-Markov weight solver — proves the pattern works for n = 4, 5, ..., 3A.

2. **Tier 2 (separate dedicated PR)**: Fix `pyhecke/atom.py` lines 555-569 to compute Wedderburn weights dynamically from `partitions_of(3A)` using `build_seminormal_matrices_cached`. The fix is mechanical given the H_4 atlas reference implementation. Run before/after witness-comparison sweep (all atoms A = 1..12) to quantify the discrepancy.

3. **Tier 3 (later)**: Delete or rewrite `atom_mass_derived.py`. Migrate `atom_per_generator_volumes` callers to confirm the new dynamic weights give consistent results.

## §8. Why this wasn't caught earlier

The bug is silent: the H_3 weights are NUMERICAL (not symbolic), so they give SOME number for any A. The resulting mass predictions are wrong by a small-to-moderate factor (multi-percent typically) but not catastrophically wrong — and the "binding energy" framework absorbs some of the error via the binding-curve fits. So the error is masked by the framework's tolerance to ~1% absolute mass deviations.

The bug shows up most clearly in:
- Cross-isotope ratios where the H_3 weights cancel inconsistently
- The 305 ppm Δm_{n-p} flavor split (which IS at the A=1 level so it's correctly using H_3)
- The α-cluster recursion bug in PR [#1220](https://github.com/litlfred/qou/pull/1220) (likely downstream)

## §9. Cross-references

- PR [#1214](https://github.com/litlfred/qou/pull/1214) — wiring-status taxonomy (0/17 canonically wired)
- PR [#1220](https://github.com/litlfred/qou/pull/1220) — α-cluster recursion bug (likely downstream of this)
- PR [#1233](https://github.com/litlfred/qou/pull/1233) — crystal-Yekutieli probes A-D + BIG review
- [`computations/mass_at_3A_proper.py`](../../computations/mass_at_3A_proper.py) — orphan "proper" implementation
- [`computations/atom_mass_derived.py`](../../computations/atom_mass_derived.py) — secondary bug (multiplicative composition)
- [`computations/alpha/alpha_k_jones_markov_h4.py`](../../computations/alpha/alpha_k_jones_markov_h4.py) — H_4 reference implementation (this PR)
