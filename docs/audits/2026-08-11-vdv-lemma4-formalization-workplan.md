# vdV Lemma 4 formalization workplan (epic qou-u1b5)

**Date**: 2026-08-11 · **PR context**: #4971 (W6 majorant rate) · **Source**:
`library/arxiv-math-0611181v2/0611181v2.pdf` §3, proof of Lemma 4 (read in full 2026-08-02).

## State after W6

The `b = 1` Whitehead-link volume limit is now **conditional only on the
class `VdVWhiteheadLemma4`** (`whiteheadLink_volume_of_lemma4`,
`WhiteheadMajorantRate.lean`): everything elementary — the majorant rate,
the triangle bound, the log-squeeze — is machine-proved sorry-free. The
class's single field `phase_cost` (`majorant ≤ N^p · ‖J_N‖` eventually)
is the analytic essence of van der Veen's Lemma 4: the Fresnel phases of
the outer `n`-sum cost only polynomially.

## Why this is a multi-session epic, not a brick

vdV proves `J_{N,a,1,c,d} ∼ C·N^{(c+d+3)/2}·S̃_N^{c+d}·e^{iCS/2π}` with
`C ≠ 0` in six steps (his §3). Formalization difficulty, in dependency
order:

| Brick | Content | Difficulty driver |
|---|---|---|
| L4-1 (`qou-xzlt`) | Refined log-sine sum expansion `s_n = (N/π)Λ(nπ/N) − ½·log(n·sin(rπ)/(rπ)) + O(1/N)` | **The crux.** Our masterErr controls `s_n` to `O(1)`; Lemma 2 needs the *second-order* (Euler–Maclaurin) term. New machinery beyond the E5c bricks. |
| L4-2 (`qou-vy77`) | Lemma 2a/2b: `S_{n,k}/S̃_N = exp(−π(n′²+2n′k′+2k′²)/N)+O(N^{3δ−2})` (central), Gaussian decay (far) | Consumes L4-1; 2-variable Taylor of `f` at `(π/2, π/4)` with explicit remainder. |
| L4-3 (`qou-kc8h`) | Far-sum kill; `(2n+1) → N` swap | Elementary counting given L4-2. |
| L4-4 (`qou-wzmi`) | Phase algebra: `χ_{N,n}·e^{Nπi/8} = exp(n′²πi/(2N))·exp(nπi/(2N))`, `φ_N` limit | Self-contained `Complex.exp` algebra — a good first brick, no analytic prerequisites. |
| L4-5 (`qou-epy2`) | Gaussian sum → integral (block comparison over unit cells, `x = √N·w` rescale) | Riemann-block machinery at the Gaussian scale; Mathlib has `integral_gaussian_complex` (re > 0) but the Fresnel boundary case needs care. |
| L4-6 (`qou-9r2q`) | `Q_∞ ≠ 0`: erfc infrastructure + vdV's Im-part domination (the sine-positive half-periods dominate) | Mathlib has no `erfc`; the nonvanishing argument is a genuine analytic lemma. Ends with `instance : VdVWhiteheadLemma4`. |

Note the class only needs the **rate-level** statement (polynomial
comparability), which is weaker than vdV's full asymptotic with the
constant — a formalization may shortcut Steps 4–6 if a direct
`‖Σ‖ ≥ N^{−p}·Σ` argument for the Fresnel-phased sum is found; no such
elementary argument is currently known (the quadratic-phase sum genuinely
concentrates on `√N`-many terms, so the naive single-term floor fails —
this is scope-(a): the elementary bricks alone do not reach it, nothing
structurally excludes a smarter route).

## What was deliberately NOT done

No `sorry`-scaffold of the six steps was committed: per the Strict Lean
Discipline, stating the bricks without proofs adds nothing the class
does not already honestly express. The epic beans carry the plan; each
brick lands only when it lands sorry-free (L4-4 first).
