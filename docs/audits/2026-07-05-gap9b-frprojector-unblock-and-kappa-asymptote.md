# Gap-9b: FR-projector compute unblocked + κ-leg asymptote formalized

**Date:** 2026-07-05
**Branch:** `claude/gap9b-frprojector-kappa-2026-07-05`
**Bean/frontier:** Step-9b per-isotope binding (cheat-sheet §0 9b row) — two of its surviving open
legs.

## 1. FR-projector compute: UNBLOCKED

The step-9b workplan
([`2026-07-02-step9b-gap-approaches.md` round-3 leg 2](../workplans/2026-07-02-step9b-gap-approaches.md))
recorded the H_{3A} per-partition FR test as **BLOCKED**: `pyhecke_native` unreachable and the
local `cargo` build 403'd on the litlfred Clarabel fork
(`github.com/litlfred/Clarabel.rs`, outside session scope) — the `[patch.crates-io]` git source
resolves at metadata time, so even `--no-default-features` failed.

**Resolution (2026-07-05):** the owner added `litlfred/Clarabel.rs` to the session scope
(`add_repo` → clone to `/workspace/clarabel.rs`). With the fork in scope, the git source resolves
(clean `cargo fetch`), and the wheel builds end-to-end:

```
apt-get install -y libgmp-dev libmpfr-dev      # GMP 6.3.0 / MPFR 4.2.1 (rug also builds its own)
pip install maturin                            # 1.14.1
cd tools/pyhecke-native
maturin build --no-default-features -o /tmp/wheels   # seminormal/Gram/trace — no LP backend needed
pip install /tmp/wheels/pyhecke_native-0.9.0-*.whl
python3 -c "import pyhecke_native"             # OK — chi_q_atomic_all_partitions_mpfr, build_atom_nf, …
```

`--no-default-features` drops the clarabel-mpfr LP backend (not needed for the FR-projector's
character/Gram primitives); `rug` still compiles GMP/MPFR from source (~few min). The FR-projector
Python test (`fr_pullback_k3_test.py` over Borromean atom words; A ≤ 4 cheap, A ≥ 5 hours) can now
run. **The compute is enabled; the actual FR run is the next step.**

## 2. κ leg: the isovector-slope asymptote is the trace ratio (Lean, sorry-free)

The Phase-5q closed form
([`b_pred_mirror_slope_closed_form.py`](../../computations/probes/b_pred_mirror_slope_closed_form.py))
gives `b_pred(A) = log_{q₀}(τ_p/τ_n) + log[(1−ε(N,Z))/(1−ε(Z,N))]/((N−Z)·ln q₀)`, with
`ε(Z,N) = z^{Z−1}(z−h/2)(z−h)^{N−1}` and measured `z ≈ 0.4994`, `z−h ≈ 0.2903` (both `< 1`).
[`QOU/Mass/KappaWritheAsymptote.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KappaWritheAsymptote.lean)
formalizes the derived mechanism:

- `epsilon_tendsto_zero` — `|z| < 1 ⇒ ε(z,h;a,b) → 0` as `a → ∞` (geometric vanishing).
- `correction_zero_of_eps_eq` — when the mirror interface terms coincide (the `ε → 0` limit) the
  correction term is exactly `0`, so `b_pred = log_{q₀}(τ_p/τ_n)` (the **plateau**).

**Refutation (scope (a)), now Lean-backed.** The asymptote is the p/n **trace ratio**
`log_{q₀}(τ_p/τ_n) ≈ 1.37181` (⇒ `κ_FW ≈ −0.34295`), **not** the interface-only near-match
`log_{q₀}(z/(z−h)) ≈ 1.2998`: interfaces enter *only* through the vanishing `ε` term. `κ_AME ≈ −0.094`
(Coulomb isovector) stays experimental — so `κ` overall remains near-match, not fully derived.

Verified lean-direct `LEAN_EXIT=0`, sorry-free; wired into `QOU.lean`.
