# Wiring proved propositions into production — mass & binding (2026-06-20)

**Branch:** `claude/lucid-curie-wmr42x`
**Request (owner):** *"we need to wire what is proved into production, particularly
for mass and binding."*
**Context:** continuation after PR #2349 merged (B_sym ¹⁶O wall + CODATA batch-1);
main had advanced ~470 commits, so each item was re-triaged against current `main`
before acting.

## Summary

| Bridge | Proved prop (Lean) | Production compute | Wiring status |
|---|---|---|---|
| **Mass = Markov trace** | `prop:hecke-mass-trace` (`qou:QOU.Braiding.hecke_mass_trace`) | `canonical_mass_table_extended.py` (computes `\|tr_M(atom)\|` via the canonical Rust MPFR trace) | **WIRED this PR** (was the unwired central bridge) |
| **Categorical mass / binding** | `prop:categorical-mass-markov` (`qou:QOU.CategoricalMassMarkov`) | `canonical_isospin_pyhecke.py`; `binding_canonical.py` cites it | **Already wired** (verified, no change needed) |

The mass bridge was the one genuine gap: `prop:hecke-mass-trace` was proved
(sorry-free Lean — `mass_markov_upper_bound`, `mass_markov_exact`,
`mass_markov_archimedean`) but had **no `computation` field** — the central
`m = |tr_M(Φ_mass)|` bridge had no production consumer (the audit's "the whole mass
pipeline lacks a certified entry point"). It now points at the production canonical
mass table, which computes the proposition's object `|tr_M(atom)|` via
`compute_tr_m_canonical` (Rust MPFR kernel, cross-checked bit-identical to laurent_q
at 1e-50).

## The honest realization caveat (discovered while wiring)

`prop:hecke-mass-trace` proves the **categorical FORM** `m = |tr_M(Φ_mass)|`. Its
**archimedean MeV evaluation for composite nuclei is NOT a clean `trace × calibration`** —
this was verified empirically while choosing a wiring target, and the negative
result is important enough to record so the next agent does not re-pitch it:

- **`atom_mass_derived.py`** realises `m = E₀·tr_M(atom)` with the single calibration
  `E₀ = m_p/tr_M(p)`. Its committed witness (`atom-mass-derived.witness.json`) shows
  it is **garbage for composites**: M(⁴He) = **−215 MeV** (negative), M(H) 1451 vs
  938. The full-atom Hecke trace does **not** scale with `A` the way the mass does.
- The **per-block** reading `m_e·vol_density_per_block(Vol, tr_M, q)` gives
  **−50 % … −97 %** residuals across p…⁴He (the documented RED verdict of
  `per_knot_mass_table_demonstration.py`).

So the production composite masses do **not** come from `|tr_M(atom)|` directly; they
ride the vol-density formula `m = m_e·Vol(K)·ρ(K)/ℏ_q²` with the per-atom Borromean
tower (`conj:borromean-baryon-mass-formula`, conjectural) for the nucleon scale, and
carry the documented **+2.89 % Vol(𝓑₃) archimedean gap**. The wiring therefore links
the **proved trace bridge** to the **production trace compute**; the MeV scale-up
retains its documented archimedean gaps and conjectural inputs. A probe claiming the
proved prop *reproduces* composite masses would be false — none was shipped.

## What this PR changes

- `content/quantum-observable-universe/mass-theory/hecke-mass-trace.ts` — adds the
  `computation` field (script + witness + `status: "verified"` for the trace
  realisation), with an inline comment flagging the proved-form / archimedean-
  realisation split. Closes the I1 no-probe gap for the central bridge.

## Status of the other requested items (re-triaged vs current main)

- **#1 — Per-nucleon Wenzl branching A≥3** (would unlock ¹⁶O exact `tr_M` without the
  `p(3A)` wall): **still open, multi-day, not attempted.** The recursion is A=2-only
  (`canonical_tr_m_via_branching.py` returns `None` for A≥3); the blocker is the
  rank-deficient H_9+ `A^λ_{ξν}(I)` extracts (least-squares under-fitted, 21–42 %
  error at A=3) plus missing H_12 pp/pn and all H_15/H_18 extracts. Scoped in the
  prior session's background analysis; deferred as a genuine multi-day task, not a
  this-session win.
- **#2 — Wire `B_sym` (log-trace binding) into production:** **blocked — not Lean-
  proved, so it cannot pass the "wire what is proved" gate.** The only B_sym Lean
  content is `archimedean_mass_commutes` (`standard-part-functor.lean`), a trivial
  `subst h_qclt_limit; rfl` that *assumes* `B_sym = B_qCLT`. `B_sym = −α·ln|tr_M|` is
  a definition + an empirical "reproduces measured binding" claim, not a theorem.
  The rigorous bridge that *is* proved is `prop:hecke-mass-trace` (wired above) — the
  Lean-backed version of what B_sym-wiring wanted.
- **#4 — CODATA literal consolidation:** **partial.** 7 files routed to the registry
  in PR #2349 (merged); ~74 live files still carry inline literals. Notable offenders
  surfaced here: `per_knot_mass_table_demonstration.py`, `atom_mass_derived.py`
  (`M_P_MEV` calibration), and the `phase5/*` probes. Follow-up batch.
