# Pre-registration: A≥3 Reeb/assembly chain on the #7741 γγ candidate word

**Owner ask (card, 2026-11-21):** run the A≥3 binding chain on the *unruled* γγ
candidate word from #7741 as a labelled comparison arm. Adopts nothing.

Written and pushed **before** any number below is computed.

## Word

`V = σ_a σ_{a+1}^{-1}`. Generators 0-indexed as in `atom_braid_word_3A`.

- **Nucleon k** (strands 3k..3k+2), proton and neutron alike: `V³` on
  generators (3k, 3k+1). #7741 found `V³` and `V⁶` the only reading-3 survivors
  in `Vᵐ, m ≤ 7`, and that p and n become the same word. `V³` is the minimal one
  and is used; `V⁶` is not run.
- **Free configuration:** the A nucleon blocks only.
- **Atom configuration:** after nucleon k (k < A−1), one bond `V³` across the
  junction. #7741's bond was between *atoms* (H₂), not between nucleons, so the
  bond site inside a nucleus is not fixed by it. Two arms, both reported, neither
  chosen:
  - **arm L:** `V³` on generators (3k+1, 3k+2);
  - **arm R:** `V³` on generators (3k+2, 3k+3).

So D, T and ³He have identical words at a given arm (A = 2, 3, 3; T and ³He are
the same word), and only the AME target differs.

## Chain

1. χ^λ for every λ ⊢ 3A, free and atom, at 50 dps via
   `pyhecke_native.chi_lambda_all_partitions_mpfr` at the proton q₀.
2. `binding_reeb_phase_decomposition.py` and
   `binding_a3plus_full_theta_assembly.py`, **unmodified**, run in a scratch copy
   whose `atom-chi-rust-*` inputs are replaced by step 1. Everything else they
   read (y_λ caches, volumes, ρ candidates) is the committed corpus.

## Reported

Per atom and arm: Σ y·dim·|Δθ|, and B_pred and |rel_err| for each ρ candidate
the assembly reports. The production (Borromean-word) values from
`binding-a3plus-full-theta-assembly.witness.json` are printed beside them.

## What would be read from it

Nothing is adopted. The γγ word is not ruled (#7876). The volume `Vol(K_bind)`
the assembly uses is the production Borromean volume, which is not derived for
this word either; that is a known mismatch, reported, not corrected. A good
number here is not evidence for the word: choosing an arm, an `m`, or a site
because it matches AME would be selection against the target.
