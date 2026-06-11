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

- [x] **1 — block-swap S_atom (⁴He).** `block_swap_binding.py`: S_atom=0.535 ≠
  S_free=0.374 (sign-only), so the binding signal `log(S_free/S_atom)=−0.358 ≠ 0`
  — the bonds break block symmetry; the symmetrization does NOT cancel. Bound
  traces split swap_p=0.401 vs swap_n=0.419 (bonds break p↔n). Block-swap braids
  self-verified.
- [x] **2 — binding wiring (honest negative).** `symmetrized_binding_closure.py`:
  the shift `scale·log(S_free/S_atom)` = −0.28 MeV (Q_β) / −1.50 MeV (E_0) is only
  1.1%/7.7% of the 20–27 MeV AME gap and points the wrong way. The symmetrization
  is a real but SUB-DOMINANT correction; the binding form/convention is the
  dominant gate. Rules out symmetrization as the gap-closer.
- [~] **3 — ⁷Li/⁸Be χ.** Registered ⁷Li/⁸Be/⁹Be in `per_irrep_pole_atom.ATOMS`.
  ⁷Li (H₂₁, 792 λ) running; ⁸Be (H₂₄, 1575 λ) is a multi-hour compute (deferred).
- [x] **4 — lake-cache diagnosis (root cause found).** The 811M
  `lake-cache/qou-v4-24-0` (built ~2026-06-04) is STALE: main migrated to the
  root Lake workspace + re-pinned Mathlib on 2026-06-10 (commit `4eb95ac1`;
  current rev `f897ebcf…`), so the cached oleans don't validate and `lake`
  correctly rebuilds from source. The cache did NOT auto-refresh because
  `lake-cache-refresh.yml` is blocked by the **GitHub Actions billing** outage.
  FIX: clear CI billing → the designed auto-refresh reseeds against the current
  rev. A manual agent reseed is a discouraged ad-hoc multi-GB stopgap (skill
  §PRESERVE THE BUILD) and is NOT a partial-cone reseed (would regress Mass
  coverage). Workaround used this session: build-to-completion once (oleans then
  valid locally for the session).
- [x] **5 — Lean formalization.** `IdenticalParticleSymmetrization.lean`
  (675-job build green): `newton_h3/e3/h4/e4` (Frobenius `Z!·h_Z/e_Z` vs power
  sums — the content of `frobenius()`) + `orbit_relabel_invariant` (cyclic-trace
  conjugation-invariance = the orbit identity, isolating the gap to the Young
  symmetrizer).

## Notes

- Branch off `main` post-#2103-merge (2104a31a).
- Wheel rebuilt; Lean env built to completion (cache stale, see task 4).
