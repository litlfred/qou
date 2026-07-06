# Infrastructure audit — H_3-vs-H_{3A} hardcode + similar n-locked APIs

**Date**: 2026-05-25
**Branch**: `claude/jm-atlas-full-plus-infra-audit-2026-05-25`
**Trigger**: Author direction "do infra audit for similar" — extends sibling
audit `docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md` (commit `c70707397`).

## §1. The original bug (sibling's finding)

`tools/pyhecke/python/pyhecke/atom.py:555-605` `atom_per_generator_volumes`
function hardcodes H_3 Wedderburn weights (w_sym, w_std, w_alt with quantum
dimensions 1, [2]_q, 1) for ALL atoms. For A > 1, the algebra is H_{3A},
not H_3 — weights are wrong by structural factor that varies with A.

Deprecation warning landed in main commit `c5e4a575a`. Migration to
`mass_at_3A_proper.per_generator_V_hat_3A(weight_scheme="normalized_plancherel")`
NOT YET DONE for the 15+ callers.

## §2. Similar bugs — pyhecke-native ABI surface is n=3-only

Surveyed every public Python function in `pyhecke_native` (the Rust PyO3
bindings). **The entire NF-basis API is hardcoded to n=3 (6×6 NF basis
size for H_3).**

| Function | Lock |
|----------|------|
| `pn.gram_matrix(q)` | "Gram matrix G_ij = tr_M(b_i · b_j) as a **6x6** list of lists" |
| `pn.gram_inverse(q)` | "Gram inverse as a **6x6** list of lists" |
| `pn.trace_weights(q)` | "Markov-trace weights on the NF basis as a **length-6** list" |
| `pn.hm(...)` | "NF multiplication: multiply NF vector by `(c · σ_gen + d · 1)`. Takes the **6-element** NF vector" |
| `pn.nf_tr(...)` | "Markov trace of a **6-element** NF vector" |
| `pn.nf_net(...)` | "Sum of NF coefficients" (6-element) |
| `pn.build_atom_nf(...)` | "Build the full atom NF for (Z, N) via Hecke multiplication. Mirrors `hecke_core.build_atom_nf`: proton / neutron **B_3** co..." |

Where 6 = |NF basis of H_3| (3 sym + 2 std + 1 alt). For H_n with n > 3,
the NF basis grows as Σ_λ d_q(λ)² = [n]_q!.

| n | |NF basis of H_n| | Required ABI shape |
|---|--------------------|---------------------|
| 3 | 6 | 6×6 (current ABI) |
| 4 | 24 | 24×24 |
| 5 | 120 | 120×120 |
| 6 | 720 | 720×720 |
| 12 | 479M | 479M × 479M (impractical) |

**Practical implication**: the n=3 hardcoded NF ABI is OK for **proton-only**
(single Borromean = single H_3 evaluation), but **systematically wrong for
every atom with A ≥ 2** (deuteron onwards uses H_6+).

## §3. Functions that ARE n-generic (the workaround path)

The just-wired Phase B character-evaluation functions ARE arbitrary-n:

| Function | Generic over n? |
|----------|-----------------|
| `pn.chi_lambda_braid(shape, word, q)` | ✓ YES — shape determines partition λ, word determines β, any n |
| `pn.chi_lambdas_braid(shapes, word, q)` | ✓ YES (batched rayon-parallel) |
| `pn.chi_lambda_braid_mpfr(shape, word, q_str, dps)` | ✓ YES (MPFR variant) |
| `pn.lr_coefficient(...)` | ✓ YES (Littlewood-Richardson) |
| `pn.tr_m_word_lq(word, n_strands)` | ✓ YES (n_strands explicit) |
| `pn.tr_m_atomic_mpfr(...)` | ✓ YES |
| `pn.partitions_of(n)` | ✓ YES |
| `pn.markov_z(q)` | ✓ YES (z value, n-independent) |
| `pn.hecke_h(q)` | ✓ YES (h = q - q⁻¹, n-independent) |
| `pn.chi_q_atomic(...)` | ✓ YES (general q-character) |

The **generic-n character path** is what my Jones-Markov atlas
(`pyhecke_jones_markov_atlas.solve_jones_markov_h_n`) exclusively uses —
sidesteps the n=3 NF-basis ABI entirely.

## §4. Bug instances in production-callers

Per sibling audit (`c70707397`): 15+ production scripts use the H_3-locked
NF-basis path. Cataloguing the worst:

| Script | NF-basis dependency | Impact |
|--------|---------------------|--------|
| `mass_formula_6term.py` | calls `atom_per_generator_volumes` | wrong weights for D/T/³He/⁴He/...all |
| `tower_isotope_absolute.py` | same | per-isotope mass tower wrong |
| `paper_six_term_isotope_sweep.py` | same | published sweep wrong |
| `atom_per_generator_volumes` itself | hardcoded H_3 weights | THE bug site |
| `mass_at_3A_proper.py` | uses arbitrary-n path | CANONICAL but ORPHANED (only ref'd from `_deprecated/`) |
| `gram_matrix` consumers | inherit 6×6 lock | downstream multi-block work breaks |

Per-call migration required because the return shape differs:
```
legacy: [{"std": Vs, "sym": sp, "alt": ap, "full": Vf}, ...]
proper: [{"full": V̂_i, "gen_word": [...]}, ...]
```

## §5. The "fix" cascade

To fully resolve the H_3-vs-H_{3A} bug, three layers need work:

### §5.1 Layer A: pyhecke (Python) — the deprecation-and-redirect layer

**Status**: deprecation warning landed (commit `c5e4a575a`). Migration of
15+ callers NOT YET DONE.

**Action**: dedicated PR queued for migration sweep. Per-call required.
Need before/after witness regression comparison (sibling held back pending
this).

### §5.2 Layer B: pyhecke-native (Rust ABI) — the NF-basis generalisation

**Status**: NOT STARTED. All NF-basis ABI surface is hardcoded n=3.

**Action**: extend the Rust ABI to accept `n_strands` parameter for
`gram_matrix`, `gram_inverse`, `trace_weights`, `hm`, `nf_tr`, `nf_net`.
This is a substantial Rust refactor — the seminormal basis construction
for arbitrary n is already in `hecke-engine` (used by `chi_lambda_braid`),
but the NF-basis encoding needs to be lifted from "6 fixed columns" to
"per-n variable columns".

**Workaround until done**: use `chi_lambda_braid` / `chi_lambdas_braid`
(arbitrary-n) instead of `gram_matrix` / `nf_tr` (n=3 only). My
`pyhecke_jones_markov_atlas.py` demonstrates this.

### §5.3 Layer C: production scripts — the consumer migration

**Status**: 15+ scripts depend on `atom_per_generator_volumes` (Layer A
bug site) or `gram_matrix`/`nf_tr` (Layer B bug site).

**Action**: per-call migration. Each script needs:
1. Identify which n it's effectively computing (3A for atom A)
2. Replace `atom_per_generator_volumes` with `mass_at_3A_proper.per_generator_V_hat_3A`
3. OR replace `gram_matrix(q)` with cycle-type LP via `solve_jones_markov_h_n`
4. Regenerate witnesses
5. Verify no production-numerics regression (this is the sibling-held step)

## §6. The "in-disguise" same-bug pattern

Several other places in the codebase ALSO assume n=3 or hardcoded NF
shapes without explicit deprecation. Found via grep:

| Location | Pattern | Notes |
|----------|---------|-------|
| `hecke_core.py` `_q_gaussian_character_approx` | uses 6-element NF | already caveated for q>1 obstruction |
| `mass_endomorphism.py` | "H_3 weights — same as mass_endomorphism.py" (referenced in atom.py:587 comment) | likely same hardcode pattern |
| `mass_at_3A_proper.py` `_cached_seminormal` | arbitrary-n (correct) | but orphaned |

A full repository sweep for hardcoded `[3]_q!` / `1, [2]_q, 1` quantum-dim
triples + `length-6` array assumptions would surface more.

## §7. The atlas-based bypass

My `pyhecke_jones_markov_atlas.solve_jones_markov_h_n(n, q)` provides a
**generic-n Jones-Markov path** that avoids the entire NF-basis ABI issue:

```python
from pyhecke_jones_markov_atlas import solve_jones_markov_h_n, tr_M_via_atlas

atlas = solve_jones_markov_h_n(n=12, q=q_0)   # H_12 for 4He
tr_M = tr_M_via_atlas(atlas, braid_word)      # Σ_λ y_λ · χ_λ(word)
```

This sidesteps the entire NF-basis n=3 lock by using cycle-type Schur
orthogonality directly on the character matrix. Computation cost is
O(p(n)²) chi_lambda evaluations (each ~ms for n ≤ 24); feasible for
A ≤ 8 atoms (n ≤ 24, p(24) = 1575).

For A ≥ 12 (12C onwards, p(36) = 17977), the cycle-type LP becomes
impractical; needs closed-form q-Schur principal specialisation
(future work).

## §8. Recommended path forward

### §8.1 Immediate (single-session)

1. **My atlas + chi_lambda path** is the production-ready replacement for
   the buggy NF-basis path at A ≤ 8. Document this in the deprecation
   warning text (point users at `solve_jones_markov_h_n` as the workaround).

2. **Audit `mass_endomorphism.py`** for similar H_3 hardcode. Likely same
   bug. Document in this audit file.

### §8.2 Short-term (sibling-coord)

3. **Migration sweep PR** for the 15+ `atom_per_generator_volumes` callers
   (sibling has it held pending witness regression comparison). My atlas
   can supply the comparison data per atom.

4. **Sibling coord on Layer B** (Rust NF-basis ABI generalisation) —
   significant Rust refactor. May or may not be priority for sibling.

### §8.3 Long-term

5. **Closed-form q-Schur** for arbitrary n → opens A ≥ 12 atoms.

6. **Lake-package generalisation** of the H_3 Lean infrastructure to
   `H_n` parametric form — bar-symmetric pairing, NF normal form,
   trace, Gram all need to be n-generic.

## §9. Cross-references

- [`docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md`](2026-05-25-h3-vs-h3a-legacy-bug-audit.md) — sibling's original audit (commit `c70707397`)
- `tools/pyhecke/python/pyhecke/atom.py:446-587` — the bug site + deprecation warning (commit `c5e4a575a`)
- `computations/mass_at_3A_proper.py` — canonical replacement (orphaned)
- `computations/pyhecke_jones_markov_atlas.py` — my generic-n atlas (Layer C bypass)
- `tools/pyhecke-native/src/lib.rs` — Rust ABI surface (Layer B target)
- PR [#1241](https://github.com/litlfred/qou/pull/1241) — sibling's pyhecke wire-up PR
