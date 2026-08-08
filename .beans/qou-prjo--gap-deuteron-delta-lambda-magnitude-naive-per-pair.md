---
# qou-prjo
title: 'GAP: deuteron Delta_lambda magnitude — naive per-pair z dead across A; surviving object is transverse NA-Stokes surface-curvature (not braid-word, not scale, not level, not edge, not DT-count)'
status: todo
type: task
priority: normal
created_at: 2026-08-02T19:09:10Z
updated_at: 2026-08-08T22:37:59Z
---

## State (PR #4615, 2026-08-02)

The deuteron binding magnitude is the Δ_λ Track-A gate. `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`
with the derived fragment `Δ_λ = (−1)^{n(λ)}·dim V_λ` gives `B(D) = 0.380 MeV` (−82.9%);
the closing `C_knot = 5.853` is FITTED and is NOT a DT count (#4601).

### What is now excluded (this PR + prior)

- **naive per-pair `z = 1/[2]_v` dead across A** (this PR, Lean-proved): scope-(b)
  EXCLUDED at A=4 (`5z²>1 ⟹ det<0`) AND insufficient at A=2 where it is PHYSICAL
  (`b₂(z)=−ln(1−z²)=0.287`, a reduction; no derived scale reaches `B_AME`, needs 7.76 MeV;
  master-Σ dressing needs non-integer exponent k=6.16). `g_reeb` same (k≈7.94 near-8 is a
  numerology trap, not chased). A=2 is not a `[1^A]` singlet (rank C(4,2)=6), so the
  He4-local `−ln det` cumulant has no reason to transfer.
- prior walls: single-universal `C_knot` / single scale (#4556); level-only rescale
  (Lean `mirror_cross_ne`); weight `y_λ` (Markov, #4543); dimension `f^λ`; writhe/framing
  (Lean `no_writhe_only_framing`); coordination-edge 3/2 (#4472); brane-tower LEVEL/WIDTH
  (three-walls 2026-07-26); geometric `W_λ` (#4392, ~30× overshoot); jet-order valuation
  (#4574); DT-count/concentration (external Springer geometry, Rossmann-CC/#4581/#4601);
  6 original ansätze; KL-positivity PROBE-4 prune.

### Surviving direction (next honest step)

The residual is per-knot χ^λ-magnitude / word content above a chirality-cancellation floor
(`C_knot` audit §5). Two open deuteron residuals — master-Σ `C_knot=5.85` and rotational
`g₂=1.0087` (E⁺(1+h²) closes D to −0.036%, D-unique, g₂ underived) — BOTH point at the same
surviving object: the **transverse NA-Stokes surface-curvature pairing** `½P∮∮[F_q,F_q]` on
the pn (σ₁³/trefoil) Seifert surface (`2026-07-24-eunit-magnus-order2.md` §2: the σ₁³
single-generator word makes ALL braid-word/inter-crossing Magnus corrections vanish, so the
missing order-2 term MUST be transverse). **Wall: needs a canonical discretization of the
Yekutieli surface 2-form on the trefoil Seifert surface — data the corpus lacks.** Building
that discretization (genus-1 trefoil Seifert surface, Seifert form) is the named next unit;
until it exists the deuteron magnitude stays open.

### Do NOT redo

Any single-scale / per-pair / level / edge / dimension / writhe / DT-count closure — all
walled. A `Δ_λ` fitted to `B(D)` is the forbidden 7th ansatz.



---
## SIGN sub-question RESOLVED (PR #4829, 2026-08-08) — bean stays OPEN (magnitude unclosed)

Ran #4817 §5's exact next unit: does sign(Σ_{λ⊢3A, ℓ≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ) cross zero on (1,q₀]?

VERDICT: **YES for the deuteron**. F_D = +8.05e-5 at q→1⁺ → −0.1950 at q₀, zero-crossing at **q≈1.05365** ∈ (1,q₀). T/³He (n=9) monotone negative, no crossing (scope-(a)). ⁴He (n=12) documented compute-limit (f64 seminormal, no mpfr kernel; disk quota). Char-free companion G=Σ y_λ·Δ_λ also crosses at n=6 (q≈1.024); n=9,12 don't.

Structural cause: 3-row block overtake — (4,1,1)[Δ=−10, +term near q=1] overtaken by (3,2,1)[Δ=+16, largest |Δ| in ℓ≥3, −term at q₀]; sgn F_D(q₀)=sgn(y·χ·Δ)_{(3,2,1)}<0.

CLOSES the sub-question 'where does the deuteron ≥3-row sign live' → the archimedean/q₀-dependent trace weighting (q₀-USE not q₀-derivation; derived not fitted; free_parameters=0; proton anchor; layer-pure). Confirms #4817 §5 / #4818 §5.

Does NOT close the MAGNITUDE (Δ_λ value-only; super-pairwise extensive term still open). Also NOT the cross-isotope (μ₃,μ₄)=(+,−) cumulant window (distinct surviving unit, §6.1). Files: docs/audits/2026-08-08-deltalambda-threerow-sign-crossing-probe.md; computations/deltalambda/threerow_sign_crossing_probe.py + witness.
