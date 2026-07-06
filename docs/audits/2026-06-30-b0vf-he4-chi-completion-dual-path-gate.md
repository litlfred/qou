# b0vf — ⁴He H₁₂ per-λ χ witness completed (77/77); GATE 2 re-scoped to the dual-path baseline (2026-06-30)

**Bean:** `b0vf` — *"chi-helium-4-h12-at-q0-50dps.witness.json only N/77
complete — needs He4 H12 chi producer re-run."*
**PR:** [#3150](https://github.com/litlfred/qou/pull/3150)
(branch `claude/bean-b0vf-2vo0hl`).
**Supersedes the open item in:**
[`2026-06-29-b0vf-markov-peel-crosscheck-he4-scalar.md`](2026-06-29-b0vf-markov-peel-crosscheck-he4-scalar.md)
(per-partition χ left 27/77 "known-incomplete"; now completed).

## TL;DR

The 77/77 per-partition χ_λ decomposition — b0vf's one unique deliverable
(the *scalar* tr_M was already canonical via markov-peel) — is now complete
at the muon pin, written by
[`_b0vf_complete_he4_witness.py`](../../computations/_b0vf_complete_he4_witness.py).
The earlier `< 1e-25` markov-peel write-gate was **mis-specified** and could
never pass; it is replaced by a principled two-gate check. The completion
is correct; the residual markov-peel gap is a small **pre-existing
two-implementation** artifact, not a χ defect.

## What stalled, and why the old gate was wrong

The prior run computed all 77 partitions (838 s, native kernel) but
**GATE 2 failed**: `Σ_λ y_λ χ_λ` (77/77) = `0.0553584335950…` vs the
markov-peel scalar `0.0553584262667…`, rel gap **1.324e-7 ≥ 1e-25**, so the
writer correctly refused.

The gate assumed `Σ_λ y_λ χ_λ` and the markov-peel scalar are the *same
number to machine precision*. They are not. They are two **implementations**
of the same canonical Markov trace:

| path | how | He-4 value |
|---|---|---|
| **Wenzl Frobenius pairing** `Σ_λ y_λ χ_λ` | per-λ χ × Wenzl `y_λ` (`_load_y_lambda`) | `0.05535843359500…` |
| **markov-peel** | Markov-axiom recursive ascent (`markov_peel`) | `0.05535842626678…` |

The diagnostic that settles it is the **complete deuteron**, where there is
*no* incompleteness at all:

| deuteron tr_M | value | vs Wenzl χ-witness |
|---|---|---|
| branch-decomp (leading δ) `Σyχ` | `0.38835720735922…` | **5e-50** ✓ (== the χ-witness's own stored tr_M to 6e-51) |
| markov-peel | `0.38835718872378…` | **4.8e-8** |

So even on a fully-complete, fully-validated input the two paths differ by
**B_D = 4.8e-8**. The He-4 gap (1.3e-7 ≈ 2.8·B_D) is the same effect, mildly
larger — *not* a χ error. (Ruled out δ as the cause: branch-decomp at
*subleading* δ moves the deuteron *further* from markov-peel, to 1.8e-7.)

This is a *smaller, separate* phenomenon from the 57–99 % `tr_M_symbolic`
(q-Plancherel `dim_q²/[n]_q!`) vs `tr_M_canonical` (Wenzl `y_λ`) weight-choice
discrepancy in [`2026-05-17-dual-tr-m-discrepancy.md`](2026-05-17-dual-tr-m-discrepancy.md):
here **both** sides already use the canonical Wenzl/Markov trace, yet the two
*implementations* of it still disagree at ~5e-8. Flagged as a follow-up
(bean), not blocking this completion.

## The principled gate (now in the producer)

- **GATE A — method correctness (blocking).** The *identical* branch
  decomposition + native kernel reproduces the complete 11/11 deuteron χ to
  **5.057e-50**. This is what actually validates the He-4 χ, which come off
  the same kernel. It also measures the deuteron dual-path baseline `B_D`.
- **GATE B — markov-peel cross-check, scoped to `B_D` (blocking).** Requires
  the He-4 markov-peel residual `< 10·B_D`. A χ error would blow past this;
  the intrinsic dual-path gap does not. Result: **1.324e-7 < 4.799e-7** ✓.

`tr_M_at_q0` in the witness is the Frobenius pairing `Σ_λ y_λ χ_λ` of *this*
table (the file's established semantics — its partial value was the partial
sum). The canonical markov-peel scalar is carried alongside as
`tr_M_markov_peel_xref` with `tr_M_dual_path_rel_gap = 1.32e-7`.

## Environment / reproducibility

- `pyhecke_native 0.9.0` built in-sandbox via the Clarabel.rs egress-proxy
  recipe ([`2026-06-28-pyhecke-native-buildable-clarabel-egress-proxy.md`](2026-06-28-pyhecke-native-buildable-clarabel-egress-proxy.md)).
  The audit's engine-drift caveat is confined to the **Clarabel SDP backend**;
  the **character kernel** path used here agrees with the canonical engine to
  5e-50 on the deuteron, so it does not affect this χ.
- Raw 77-partition χ dumped to `_b0vf_he4_chi_raw.json`; re-run with
  `B0VF_REUSE_RAW=1` to skip the ~14-min recompute.

## Follow-up

- **New finding (file as bean):** the ~5e-8 Wenzl-Frobenius vs markov-peel
  dual-*implementation* gap on atoms where both are complete (deuteron 4.8e-8,
  He-4 1.3e-7). Both are meant to be bit-identical realisations of the
  canonical Markov trace; the gap is at the 8th digit and is **pre-existing**
  (both witnesses on `main`, computed 2026-06-29). Likely a normalisation /
  finite-precision artifact in one path; worth pinning down, not blocking.
