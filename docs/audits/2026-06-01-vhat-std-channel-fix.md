# Feeding the DERIVED "std" V̂_i into the brane tower — raw m_p, and why it diverges

**Date:** 2026-06-01
**Branch:** `claude/vhat-std-channel-fix-2026-06-01` (PR #1635)
**Scope:** Act on the merged item-2 audit
[`2026-06-01-vhat-per-crossing-transfer-chain.md`](2026-06-01-vhat-per-crossing-transfer-chain.md)
(verdict A + RED finding): the brane tower consumes the W-weighted
3-channel `"full"` Wedderburn average, not `thm:markov-trace-product`'s
genuine per-generator factor V̂_i = z·a_i + b_i (the `"std"` channel).
Switch the consumer to the derived `"std"` channel and report the RAW
resulting m_p / m_n. No fit, no tuning, no hard-coded correction.

**Compute:**
[`vhat_std_vs_full_tower_compare.py`](../../computations/vhat_std_vs_full_tower_compare.py),
witness
[`vhat-std-vs-full-tower-compare.witness.json`](../../computations/vhat-std-vs-full-tower-compare.witness.json).
Channel selection added (owner-gated, default `"full"`) to
[`derive_m_p_hecke_full_tower_50dps.py`](../../computations/derive_m_p_hecke_full_tower_50dps.py).

---

## VERDICT: the derived "std" V̂_i REGRESSES m_p — it DIVERGES the Rogers tower

Feeding the genuine standard-channel Markov-trace factor V̂_i = z·a_i +
b_i (the channel whose product reproduces tr_M to 4×10⁻⁶) into the
existing brane tower makes **m_p = +∞**. This is not a numerical
accident: the genuine proton σ₀ factor lies **outside the convergence
radius of the q-dilogarithm** the tower is built on. The current
`"full"` channel only converges because its W-weighting happens to
compress every per-generator scalar below that radius.

**This means the +2.89 % / +98.7 % headline numbers and the channel
choice are decoupled** — the tower-truncation under-prediction is a
separate issue from the channel mis-wiring. Production default is
**NOT** flipped; the std path is added owner-gated for review.

---

## 1. What "std" and "full" are (from the item-2 audit)

The upstream producer
[`terms_2_3_atom_per_gen_mpfr_50dps.atom_per_generator_volumes_mpfr`](../../computations/terms_2_3_atom_per_gen_mpfr_50dps.py)
emits, per generator, a dict `{std, sym, alt, full}`:

- **`"std"`** = `z·a_i + b_i` — the Markov trace of the per-generator
  reduced Hecke element in the standard (2,1) Hoefsmit block. This is
  `thm:markov-trace-product`'s V̂_i, DERIVED with zero free parameters;
  ∏V̂_i^std = tr_M (proton 1.065306, to 4e-6).
- **`"full"`** = `w_sym·λ_sym + w_std·V_std + w_alt·λ_alt` — the
  W-weighted 3-channel Wedderburn average (`w = {1, [2]_q², 1}/nf₃`,
  normalised to sum 1). NOT the per-generator Markov-trace factor;
  ∏V̂_i^full ≠ tr_M (proton 0.960).

The brane tower (`derive_full_tower` → `compute_t2_t3_from_vols`)
consumed `"full"`.

## 2. The switch (owner-gated)

`derive_m_p_hecke_full_tower_50dps.py` gains a `channel` parameter
(`"full"` | `"std"`) threaded through `_t1_t2_t3_from_per_gen` →
`derive_full_tower` → `main` (CLI `--channel std`). **Default stays
`"full"`**; running a non-default channel skips the production witness
write. The std-vs-full comparison is the dedicated script above. No
channel weight was tuned; no correction was added.

## 3. RAW result (zero tuning), MPFR @ 50 dps

| channel | m_p (MeV) | rel-diff vs CODATA | m_n (MeV) | rel-diff vs CODATA |
|---|---|---|---|---|
| CODATA | 938.27208816 | — | 939.56542052 | — |
| **full** (production) | **12.154434** | **−98.70 %** | 11.542440 | −98.77 % |
| **std** (derived) | **+∞ (diverges)** | — | 11.934486 | −98.73 % |

m_p MeV computed as `(m_p_hecke / m_e_hecke) × m_e`; only CAL-1 (m_e) +
CAL-2 (q₀) consumed. The neutron with the std channel is finite
(11.934 MeV); the proton is +∞.

## 4. Root cause — the q-dilogarithm convergence radius is q₀

The single-tower term is `T2 = Σ_i Li_2^q(|V̂_i|)` where `Li_2^q(z) =
Σ_{n≥1} z^n / (n·[n]_q)`. Per its docstring + a direct ratio test, the
**radius of convergence is |z| < q₀ ≈ 1.10998**;
[`_li_2_q_util.li_2_q`](../../computations/_li_2_q_util.py)
returns `+inf` for `|z| ≥ q₀`.

Per-generator magnitudes (RAW, from the per-gen witness):

| nucleon | gen | \|V̂\|^std | \|V̂\|^full | std vs q₀ ≈ 1.10998 |
|---|---|---|---|---|
| proton | σ₀ | **1.146101** | 0.989007 | **> q₀ → Li_2^q = +∞** |
| proton | σ₁ | 0.929504 | 0.971070 | < q₀ (finite) |
| neutron | σ₀ | 1.003852 | 0.854210 | < q₀ (finite, just inside) |
| neutron | σ₁ | 0.919690 | 0.975509 | < q₀ (finite) |

The proton σ₀ genuine Markov-trace factor (1.146101) **exceeds q₀**, so
`Li_2^q(1.146101) = +∞`, hence T2 = +∞ and m_p(std) = +∞. The neutron's
largest std factor (1.003852) is just below q₀, so m_n(std) is finite.
The `"full"` channel converges because W-weighting pulls every scalar
under q₀ (max 0.989).

## 5. Interpretation (honest)

- The derived `"std"` channel — the one whose product equals tr_M —
  **regresses** m_p: it pushes the proton's leading factor past the
  Rogers-dilogarithm radius. The current production accuracy figure is
  therefore **not** "depending on the correct channel"; the `"full"`
  channel is the one that keeps the tower finite, but its product is
  not tr_M.
- The two facts the item-2 audit established — (a) ∏V̂_i^std = tr_M, and
  (b) the tower eats `"full"` — are both confirmed here, and the
  comparison adds the operational consequence: **the tower's
  q-dilogarithm cannot accept the genuine std factors for the proton**.
- This is a structural tension, not a bug to "fix" by tuning: either
  the per-generator factor that enters T2/T3 must be a quantity bounded
  by q₀ (which the std Markov trace is not, for the proton), or the
  tower's transcendental kernel (Li_2^q radius q₀) is the wrong functor
  for genuine Markov-trace inputs. Flagged for the owner; no default
  flip, no fit.

## 6. What this audit does / does not claim

- **Does** wire the derived `"std"` channel through as an owner-gated
  path and report the RAW m_p / m_n for both channels.
- **Does** identify, with a witness, that m_p(std) = +∞ and pin the
  cause to the q-dilogarithm radius (|z| < q₀) being exceeded by the
  genuine proton σ₀ factor 1.146101.
- **Does NOT** tune any channel weight, add a correction, or flip the
  production default — all owner-gated.
- **Does NOT** claim the `"full"` channel is "correct"; it is the one
  that keeps the tower finite, but ∏V̂_i^full ≠ tr_M.
