# Deriving the 2n² shell capacity — diagnosis (genuinely open)

**Date:** 2026-06-16
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348)
**Class:** formalize-first diagnosis + content correction.

## The ask

Make the electron-shell σ_F peaks *emergent* by **deriving** the 2n² shell
capacity from the categorical structure (rather than inputting it) — the blocker
identified in the σ_F-inconsistency resolution.

## Corpus-grep first (what already exists)

| source | says |
|---|---|
| [`electron-shells-hopf.md`](../../content/quantum-observable-universe/predicted-spectra/electron-shells-hopf.md) open problem **1** | *"prove that the maximum number of trefoils in a closed sub-Hopf link at level n is 2n²"* — **explicitly open** |
| [`electron-shell-braid-capacity.md`](../../content/quantum-observable-universe/molecular-construction/electron-shell-braid-capacity.md) | asserted 2n² *"from the Hecke algebra dimension of the representation at that level"* — **unsupported overclaim** (softened, see below) |
| [`shell-structure-eigenvalues.md`](../../content/quantum-observable-universe/predicted-spectra/shell-structure-eigenvalues.md) | the shell operator is the **2×2** `T_γe`; "the entire shell structure is encoded in the eigenvalues of `T_γe` — a 2×2 matrix" |

So 2n² is **not derived** — the corpus's own open-problem list says so, and the
one block that claimed a source gave an unsupported one.

## Diagnosis — why the current structure cannot give 2n²

The target factors as

$$
  2n^2 \;=\; 2 \cdot \sum_{\ell=0}^{n-1} (2\ell+1)
  \;=\; \underbrace{2}_{\text{spin}} \cdot \underbrace{n^2}_{\text{orbital}}.
$$

- **The "2" (spin)** is what `T_γe` supplies: it is a 2×2 matrix, so `T_γe^n`
  has a 2-dimensional eigenspace — a 2-fold degeneracy. This is the only
  degeneracy the shell operator carries.
- **The "n²" (orbital)** is the **hydrogenic accidental degeneracy**: `n² =
  Σ_{ℓ=0}^{n-1}(2ℓ+1)` is the dimension of the `SO(4) ≅ SU(2)×SU(2)` Runge–Lenz
  `(j,j)` representation with `j = (n−1)/2`, which bundles angular-momentum
  levels `ℓ = 0,…,n−1` into one principal shell `n`. **`T_γe^n` (rank 2)
  produces no such n²-fold structure.**

QOU *does* have the angular-momentum reps `V_ℓ` (dim `2ℓ+1`): the Bring-quintic
`S_5 ⊃ A_5` action carries the `SO(3)` levels `V_ℓ`
([`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md)).
But they are **spent on lepton generations** — `ℓ=1 → V_1` (electron), `ℓ=2 →
V_2` (muon), via `V_ℓ ↓ A_5 ↪ S_5` — **not** on radial electron shells. There
is no `SO(4)` Runge–Lenz symmetry bundling `ℓ=0,…,n−1` into shell `n`; the
documented `SO(3)/SU(2)` symmetry-loss
([`2026-06-04-u1-su2-so3-symmetry-loss-audit.md`](2026-06-04-u1-su2-so3-symmetry-loss-audit.md))
makes even the single rotational symmetry partial.

## Formalize-first conditional (the precise gap)

> **If** the atomic dressing carried an `SO(4) ≅ SU(2)×SU(2)` dynamical
> (Runge–Lenz) symmetry whose principal shell `n` is the `(j,j)` irrep with
> `j=(n−1)/2`, **then** `dim = n²` and, tensored with the spin-`SU(2)` that
> `T_γe` already supplies, the shell capacity is `2n²`.

The missing object is exactly that second (Runge–Lenz) `SU(2)` and the functor
bundling `V_0 ⊕ V_1 ⊕ … ⊕ V_{n−1}` into principal shell `n`. The `V_ℓ` exist;
the bundling does not. **Verdict: 2n² is not derivable from the present
structure — genuinely open, matching `electron-shells-hopf` problem 1.** Not
faked here. Any σ_F-peak model that inputs 2n² is circular (demonstrated in
[`electron_sigma_f_marginal.py`](../../computations/electron_sigma_f_marginal.py)).

## Actions taken

1. **Softened the overclaim** in `electron-shell-braid-capacity.md`: "2n² from
   the Hecke algebra dimension" → "conjecturally 2n² (the open shell-capacity
   derivation); the 2×2 transfer matrix fixes shell energies but gives only a
   2-fold degeneracy, not 2n² = 2·Σ(2ℓ+1), which needs an SO(4) accidental
   degeneracy." Now consistent with `electron-shells-hopf` problem 1.
2. **Removed the vacuous shadowing stub** (the queued follow-up 2):
   `particle-interactions/shell-closure-stability.lean` (σ_F≡0, μ≡2) shadowed
   the real library decl. Per the lean-ref-resolution witness
   (`lake_root_exists/declares: true`, imported at `QOU/BraidKnot.lean:18`),
   deleting the sibling lets `qou:QOU.BraidKnot.ShellClosureStability` resolve to
   the real conditional-class formalisation. *(Validator absent in this sparse
   checkout — CI should confirm the ref still resolves.)*

## Open (research tranche — not this PR)

- **Derive the SO(4)/Runge–Lenz n²-bundling**, or refute it and accept 2n² as a
  topological input (the `electron-shells-hopf` linking-matrix conjecture). This
  is the genuine blocker for emergent shell peaks; it is *not* tractable as a
  cost-operator tweak.
