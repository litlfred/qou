# `crt_markov.py` multichannel extension — design doc

**Audit ID:** §3·A from
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
**Branch:** `claude/refactor-computation-framework-Dmvva`
**Date:** 2026-05-02
**Status:** design + partial implementation (sym + std + alt at H_3 Wedderburn).
H_{3A} CRT reconstruction (§3·B) flagged research-grade; not started.

## 1. Current state of `crt_markov.py`

[`computations/crt_markov.py`](../../computations/crt_markov.py)
(592 lines) holds **two** Markov-trace evaluators that diverge in
ambition:

| Function | Lines | What it computes | Status |
|----------|-------|-------------------|--------|
| `markov_trace_at_q` | 39–65 | `Π V_s` over generators (std channel, descended only) | legacy float path |
| `markov_trace_symbolic_eval` | 142–166 | same as above, mpmath | **the legacy descended-only function — most callers use this** |
| `tower_mass_symbolic_eval` | 169–329 | full tower `desc + Σ Φ_q + z² Σ Φ_q` with sym/std/alt | added later, **but only 1 caller migrated** (per AUDIT-crt-k-level.md refresh) |
| `markov_trace_schur_weyl_eval` | 365–411 | proper H_{3A} Schur–Weyl sum (descended) via `schur_weyl_mpmath.markov_trace_mpmath` | descended only; tower terms still H_3 per-generator |

The "channel" picture currently lives **only inside
`tower_mass_symbolic_eval`**, lines 184–219:

```python
# H_3 Wedderburn weights (additive Wedderburn, per mass_endomorphism)
nf3 = qint(1) * qint(2) * qint(3)
qdim_sym = mpmath.mpf(1)
qdim_std = qint(2)
qdim_alt = mpmath.mpf(1)
w_sym = qdim_sym ** 2 / nf3
w_std = qdim_std ** 2 / nf3
w_alt = qdim_alt ** 2 / nf3
# normalised, then per generator:
sp = sp * (c * q + d)         # sym eigenvalue σ_i ↦ q
ap = ap * (-c * qi + d)       # alt eigenvalue σ_i ↦ -q⁻¹
Vs = z * a + b                 # std (2-dim) Hecke trace
V_full = w_sym * sp + w_std * Vs + w_alt * ap
```

So **all three channels** (sym, std, alt) are already implemented at
H_3 weights inside `tower_mass_symbolic_eval`. What the audit
[`AUDIT-crt-k-level.md`](../../computations/AUDIT-crt-k-level.md)
calls "missing" is the **per-channel breakdown** at the witness
level: the function returns a single aggregated number (`desc`,
`single`, `cross`, `total`) without exposing the contribution of
each Wedderburn channel separately, so it is impossible to verify
which channel dominates which tower term, and the existing legacy
callers (`canonical_isospin_pyhecke.py`, `derived_only_extended_A12.py`,
`deuteron_error.py`, `gb_residue_tower.py`,
`paper_six_term_isotope_sweep.py`) all still call the descended-only
`markov_trace_symbolic_eval`, never the tower path.

## 2. Gap analysis (per-term, per-channel)

| Term | Symbol | Currently in `tower_mass_symbolic_eval` | What's exposed in witness | What's missing |
|------|--------|------------------------------------------|---------------------------|----------------|
| **Term 1** descended | `\|Π V̂_i^full\|` | yes (lines 234–255, with SW fallback) | aggregated `desc` only | per-channel split: \|Π V_sym\|, \|Π V_std\|, \|Π V_alt\| |
| **Term 2** depth-1 single-gen | `Σ_i Φ_q(\|V̂_i^full\|)` | yes (lines 270–313, with SW fallback) | aggregated `single` only | per-channel split + Φ_q evaluated channel-by-channel |
| **Term 3** depth-2 adj-pair | `z² Σ_{\|i-j\|=1} Φ_q(\|V̂_i V̂_j\|)` | yes (lines 286–323) | aggregated `cross` only | per-channel cross + per-pair breakdown |
| **H_{3A} Wedderburn** at all λ ⊢ 3A (§3·B) | `Σ_λ w_λ χ^λ` | descended-only via `markov_trace_schur_weyl_eval` | descended only | tower terms (Σ Φ_q, z² Σ Φ_q) at H_{3A} weights — still H_3 per-generator |

So the "tower is missing" framing in §3·A is *not literally* true —
the code exists. The **practical** gap is twofold:

1. **No per-channel witness exists** showing how much of the mass
   each channel contributes. This makes empirical falsification of
   channel-mixing weights impossible.
2. **No callers** of `tower_mass_symbolic_eval` produce a witness
   that survives onto disk; the refresh paragraph in
   `AUDIT-crt-k-level.md` calls this out.

The H_{3A} extension (§3·B) is a separate, much harder problem and
is **not** addressed here.

## 3. Proposed architecture (v2)

New file: `computations/crt_markov_v2.py` (≤ 500
lines). Re-imports helpers from `crt_markov` (`_build_crossings`,
`_Phi_q_mp`) and `mass_endomorphism` (`proton_cross`,
`neutron_cross`, `electron_cross`).

### 3.1 Public API

```python
def per_channel_volumes(Z, N, include_inter, m_pp, m_pn, m_nn,
                        q_val, precision=50):
    """Per-generator Wedderburn volumes split by channel.

    Returns list[dict] over generators, each dict has keys
        {"V_sym", "V_std", "V_alt", "V_full",
         "w_sym", "w_std", "w_alt"}
    where V_full = Σ_λ w_λ V_λ at H_3 Wedderburn weights.

    H_3 Wedderburn weights: w_λ = (qdim λ)² / nf3, normalised.
    Per generator the eigenvalues / 2-dim trace are
        V_sym  =  Π (c·q + d)             (σ_i ↦ q)
        V_alt  =  Π (-c·q⁻¹ + d)          (σ_i ↦ -q⁻¹)
        V_std  =  z·a + b                  (2-dim Hecke trace)
    where a, b accumulate via the Hecke recursion.
    """

def tower_per_channel(Z, N, include_inter, m_pp, m_pn, m_nn,
                      q_val, precision=50):
    """Full tower mass with per-channel breakdown.

    Returns dict with keys
        desc_per_channel  : {"sym": …, "std": …, "alt": …, "full": …}
        single_per_channel: {"sym": …, "std": …, "alt": …, "full": …}
        cross_per_channel : {"sym": …, "std": …, "alt": …, "full": …}
        total              : desc_full + single_full + cross_full
        V_per_gen          : list[dict] from per_channel_volumes
        weights            : {"w_sym": …, "w_std": …, "w_alt": …}
        H3_consistency     : bool — sym + std + alt sum equals full?
    """

def witness_for_atom(label, Z, N, include_inter, q_val, precision=50):
    """Build a witness JSON entry for a single atom — per-channel breakdown."""
```

### 3.2 H_3 channel eigenvalues (per Hecke relation)

The Hecke generator $\sigma_i$ satisfies
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. The two eigenvalues
$+q$ (sym) and $-q^{-1}$ (alt) are the 1-dim irreducibles; the
2-dim std rep gives Hecke trace $V_s = z\,a + b$ with the
Markov coefficient $z = (q^{1/2} + q^{-1/2})^{-1}$.

Per-generator accumulation, given crossing list `[(c_k, d_k)]`:

| Channel | Closed-form per crossing | Aggregated |
|---------|---------------------------|------------|
| sym | factor `c·q + d` | `V_sym = Π_k (c_k·q + d_k)` |
| alt | factor `-c·q⁻¹ + d` | `V_alt = Π_k (-c_k·q⁻¹ + d_k)` |
| std | Hecke recursion `(a, b) ← (a·c·h + a·d + b·c, a·c + b·d)` | `V_std = z·a + b` |

These are *exactly* what `tower_mass_symbolic_eval` computes
inline; v2 separates them out with a clean API.

### 3.3 Performance

- `per_channel_volumes`: O(n_gens · max_crossings) at fixed
  precision — same as current code, just exposing more fields.
- `tower_per_channel`: identical asymptotic cost to
  `tower_mass_symbolic_eval`. No new scaling concerns.
- One-liner pure-add: each per-channel splitting adds ~1 mpmath
  multiply per generator. ≪1% overhead.

### 3.4 Testing strategy

1. **H_3 consistency** (in-process): for the proton's 3-strand
   atom (Z=1, N=0, include_inter=False), check that
   `sym + std + alt = full` per generator and after aggregation.
2. **Single-block character cross-check** — recover the
   H_3 single-block characters at $\sigma_1 \sigma_2^{-1}$ pattern
   and confirm consistency with the existing
   `alpha-k-jones-markov-h3.witness.json` weights.
3. **Backward compatibility**: when reduced to total, the v2
   tower should match `tower_mass_symbolic_eval` exactly to
   working precision (≤ 1e-30 relative).

## 4. Risk inventory

### Straightforward (implemented in v2)

| Item | Why it's easy |
|------|---------------|
| Per-channel split at H_3 | Eigenvalues already known; just product accumulation |
| Per-pair tower split | Same Φ_q machinery, indexed by (i, j) |
| Witness JSON per atom | Standard pattern from existing witnesses |
| Backward-compat check vs `tower_mass_symbolic_eval` | mpmath equality at high precision |

### Research-grade (NOT implemented; flagged for follow-up)

| Item | Why it's hard | Tracked at |
|------|---------------|------------|
| **H_{3A} Wedderburn coverage** | Need χ^λ(W) for all λ ⊢ 3A (i.e., partitions up to 60+). MN q=1 already wired in `schur_weyl_mpmath`; full q-Hecke χ^λ(q) is a `schur_weyl_q_hecke*.py` open project | §3·B |
| **Per-channel × per-stratum SW** | The `per_stratum_sum_symbolic` path inside `tower_mass_symbolic_eval` (lines 270–297) collapses across all λ; splitting by channel requires per-λ stratum sums | §3·B follow-up |
| **z² weight at H_{3A}** | At H_3 the Markov coefficient is `1/(q^½ + q^{-½})`; at H_{3A} the analogue is partition-dependent | §3·B follow-up |
| **Symbolic-in-q throughout** | Currently mpmath substitutes q_0 at evaluation; full $\mathbb{Z}[q^{\pm 1/2}]$ symbolic via sympy is bottlenecked at A=12 (per `schur_weyl_mpmath.py` header) | §3·E |

## 5. What v2 buys us

After v2 + the witness emitted by `crt_markov_v2.py`, the §3·A audit
gap is **closed for the H_3 case** with a falsifiable per-channel
witness:

- Each channel's contribution is logged.
- The 0.04–0.91% mass-error band can now be diagnosed
  channel-by-channel — does the missing 0.9% live in `sym`, `std`,
  or `alt`? Or does it live in the H_{3A} approximation gap
  (= §3·B)? The witness will tell us.

What it does **not** buy us: the §3·B gap (H_{3A} Wedderburn
weights) is unchanged. v2 is honest about that.

## 6. Implementation plan summary

| Step | File | LOC est. | Status |
|------|------|----------|--------|
| 1. v2 module | `computations/crt_markov_v2.py` | ~350 | done |
| 2. Witness emit | same file (`__main__` block) | ~80 | done |
| 3. Test (H_3 consistency + single-block cross-check) | inline `if __name__` test, plus standalone assertions | ~50 | done |
| 4. H_{3A} (research-grade) | not started | — | flagged |

Total LOC: ~480 of new Python. Below the 500-line cap.

## 7. References

- [`computations/crt_markov.py`](../../computations/crt_markov.py) — current code
- [`computations/AUDIT-crt-k-level.md`](../../computations/AUDIT-crt-k-level.md) — gap statement
- [`computations/mass_endomorphism.py`](../../computations/mass_endomorphism.py) — per-particle Wedderburn vols (the canonical implementation)
- [`computations/alpha-k-jones-markov-h3.witness.json`](../../computations/alpha-k-jones-markov-h3.witness.json) — expected H_3 weights for cross-check
- [`docs/audits/2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md) §3·A
