# Workplan — block-swap binding + Lean formalization (2026-06-11)

Follow-ups from [#2103](https://github.com/litlfred/qou/pull/2103) (per-isotope
binding-constituent infra). Owner directive: "1 2 3 4 5 / see skills on Lean".

## Tasks

1. **Exact block-swapped S_atom (task-1 exact).** Compute the S_Z×S_N
   symmetrized bound trace `tr_atom_sym = |G|⁻¹ Σ_{σ∈S_Z×S_N} tr_M(W_atom·β_σ)`
   for ⁴He (S₂×S₂, 4 block-permutations) — the actual binding signal
   `log(S_free/S_atom)`. The Young symmetrizer COMPOSES the block-swap braid
   `β_σ` (not relabeling/conjugation — distinct from the orbit identity, which
   `symmetrized_binding_probe.py` flagged).

2. **Wire the symmetrized constituent into production binding.** Once S_atom
   exists, test whether `B = scale·(h_Z h_N − tr_atom_sym)` (or the log-ratio)
   closes the per-isotope Δ_λ gate better than the naive `τ^Z τ^N`.

3. **Extend χ to ⁷Li / ⁸Be / heavier.** `chi_via_rust_lossless.py 7Li 8Be …`
   (arbitrary-n auto-extends the y_λ tower). Provides A=7,8 active-set inputs.

4. **Diagnose the lake-cache restore.** Why the 811M `lake-cache/qou-v4-24-0`
   cache didn't engage last session (a 682-job from-source rebuild despite the
   cache already holding Mathlib.Tactic.Ring + QOU.Mass/Hecke). Fix so future
   builds restore in ~2 min.

5. **Lean formalization (see Lean skills).** Formalize the structural results
   under `QOU.Hecke` per the `formalizer` discipline (every Lean theorem gets a
   matching narrative `.md` proof):
   - the general Frobenius power-sum decomposition `p₁^Z = Σ_λ f^λ s_λ` (extend
     the existing Z=2,3,4 to a general statement / Newton's identities), and
   - the orbit-identity ≠ Young-symmetrizer distinction (relabeling/conjugation
     vs. block-swap composition) as a precise lemma.

## Status

- [ ] 1 — block-swap S_atom (⁴He)
- [ ] 2 — production binding wiring
- [ ] 3 — ⁷Li/⁸Be χ
- [ ] 4 — lake-cache restore diagnosis
- [ ] 5 — Lean formalization

## Notes

- Branch off `main` post-#2103-merge (2104a31a).
- Wheel rebuilt; Lean env restored from `lake-cache/qou-v4-24-0` (task 4 in flight).
