# Covariance-kernel proof epic (qou-x631) — Phase 3: β-ensemble reframing + Stein reduction

**Date:** 2026-07-24 · **Branch:** `claude/deltalambda-covariance-epic-phase3-2026-07-24` ·
**Tier:** analytic attack + reframing (exact + 60-dps) · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`. **Follows:** #4150 (Phase 2).

## The epic (recap)

Prove the sole open input of the Δ_λ super-exponential growth bound (#3939, via #3959):

> `cov(k) := Σ_{λ⊢k} (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0`  (⇔ `Cov_Planch(f^λ, Σc²) ≤ 0`).

Phases 1–2 (#4008/#4150) eliminated five certificates (holonomic recurrence, β-monotone family,
sub-family truncation, MN-peeling, tabulated closed form). Phase 3 opens the analytic attack.

## Headline — the kernel is one instance of a β-ensemble inequality

Let `ω₃(λ) := Σ_□c(□)² − C(k,2)`, `G(β) := Σ_{λ⊢k} (f^λ)^β ω₃(λ)`, and
`H(β) := G(β)/Σ_λ(f^λ)^β = E_β[C₂] − C(k,2)`, where `E_β` is the **β-biased (Jack–Plancherel)**
average `E_β[X] = Σ_λ (f^λ)^β X(λ) / Σ_λ (f^λ)^β`. The kernel is exactly `G(3) ≤ 0`, and the **whole
family** holds empirically:

> **`H(β) ≤ 0` for all `β ≥ 2`, with equality `H(2) = 0`** — i.e. **β = 2 (Plancherel) maximises the
> β-biased expected content-spread `E_β[C₂]` over `β ≥ 2`.**

Boundary/asymptotic data pinning `H` on `[2,∞)`:

| datum | value | status |
|---|---|---|
| `H(2)` | `0` | exact (Plancherel content mean `E_2[C₂] = C(k,2)`) |
| `H'(2)` | `Cov_Planch(ln f^λ, ω₃) < 0` | verified all `k ≤ 19` (strict) |
| `H(∞)` | `< 0` | `β→∞` concentrates on the max-dimension diagram, which is balanced ⇒ `ω₃ < 0` |
| `sup_{β∈(2,60]} H` | `< 0` | 60-dps, all `k ≤ 16`; global sup `−5.4e−11` (attained as `β→2⁺`, i.e. no interior excursion) |

**Why this matters.** It moves the kernel out of the bespoke `(f^λ)³` average and into the
**β-ensemble / Jack-polynomial literature**, where the monotone-concentration heuristic (larger β ⇒
mass on higher-dimension, more balanced diagrams ⇒ smaller content-spread) is standard. The surviving
proof target is a clean β-monotone-*sign* statement, not a bespoke third-moment identity.

## Route 1 (Stein / log-covariance) — PARTIAL

Kerov's CLT makes `(ln f^λ, Σ_3)` jointly asymptotically Gaussian under Plancherel; for jointly
Gaussian `(X,Y)`, Stein gives the **exact** `Cov(e^X,Y) = E[e^X]·Cov(X,Y)`, so asymptotically
`sign Cov(f^λ,ω₃) = sign Cov(ln f^λ,ω₃)`. Findings:

- **`Cov_Planch(ln f^λ, ω₃) < 0`** for all `k ≤ 19` (the log-dimension is negatively correlated with
  the content-spread — this **is** `H'(2) < 0`).
- The transfer factor `A/(E[f]·B)` (with `A = Cov(f,ω₃)`, `B = Cov(ln f,ω₃)`) is **positive and
  bounded** (≈ 0.55–0.88) but **not → 1**: the finite-`k` law is non-Gaussian, so the naive Stein
  identity is only approximate.

⇒ A rigorous Route-1 proof needs (a) `Cov_Planch(ln f, ω₃) ≤ 0` [tractable — it is `H'(2) < 0`] plus
(b) a proof the transfer factor stays positive; (b) does **not** follow from naive Gaussianity and
needs error control — or the β-family route, which subsumes it.

## Route (Descartes / variation-diminishing) — RULED OUT

`G(β) = Σ_λ ω₃(λ) e^{β ln f^λ}` is an exponential sum, so the variation-diminishing property bounds
`#{real zeros of G} ≤ #{sign changes of ω₃(λ) ordered by dimension f^λ}`. That count **grows with k**
(`1, 1, 1, 3, 3, 5, 7, 5, 15, …, 111` at `k = 21`), so the bound is vacuous — a dimension-ordered
Descartes certificate cannot close the kernel. (Dimension ties are exact conjugate pairs `λ, λ′` with
equal `f` **and** equal `ω₃`, since `Σc²` is conjugation-invariant — no spurious sign changes.)

## Net + Phase-4 target

The kernel is now the `β = 3` case of the β-ensemble inequality `E_β[C₂] ≤ C(k,2) ∀β ≥ 2` (equality
at β = 2), with clean boundary data (`H(2)=0`, `H'(2)<0`, `H(∞)<0`, no interior excursion). The
surviving attack is to **prove β = 2 maximises `E_β[C₂]` on `[2,∞)`** — a Jack/β-Plancherel
concentration statement — e.g. via a log-convexity / concentration argument on the partition function
`Z(β) = Σ_λ (f^λ)^β`, or a literature match in the β-ensemble corpus. Coordinate with the Specht/S_n
Lean epic `sp00` for the eventual Lean carrier.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase3.py`](../../computations/deltalambda/wlambda_covariance_epic_phase3.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase3.witness.json`

## Cross-references

- Phase 2 (routes 3–5 + R₄ affine): [`2026-07-24-covariance-kernel-proof-epic-phase2.md`](2026-07-24-covariance-kernel-proof-epic-phase2.md) (#4150)
- Phase 1 (routes 1–2): [`2026-07-18-covariance-kernel-proof-epic-phase1.md`](2026-07-18-covariance-kernel-proof-epic-phase1.md) (#4008)
- Literature: Śniady (PTRF 2006, arXiv:math/0305423), Biane (Adv. Math. 1998), Ivanov–Olshanski; Jack/β-Plancherel: Okounkov–Olshanski, Matsumoto
