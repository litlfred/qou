---
# qou-6gf9
title: 'Class I: derive a correction to m_mu/m_e = Vol(4_1)/hbar_q^2 (the 11.5 ppb mu-p residual)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-08T09:31:00Z
updated_at: 2026-09-03T05:22:25Z
---

Attack the Class I mu-p residual on the **muon carrier** `m_mu/m_e = Vol(4_1)/hbar_q^2`
(distinct angle from the Q_beta `c_k` ladder and from the `F_Bor` `c_4` dressing).
Hypothesis: the carrier is the leading term of a series and the ~11.5 ppb q_0 tension
(= +209.755 ppb on m_mu at the proton pin, 9.53 sigma) is its first correction.

Route stays on the right side of the permanent 2026-08-02 owner gate (`qou-eic1`):
it corrects a **mass-ratio relation at fixed q_0**; it does not derive `q_0`.

## Outcome (2026-08-08) — NOT CLOSED. Three prunes landed; the front is bounded.

Audit: `docs/audits/2026-08-08-mu-p-residual-carrier-order-and-bar-parity-prune.md`
Probe: `docs/audits/scripts/mu_p_carrier_order_window_probe.py`
Lean:  `content/quantum-observable-universe/lean/QOU/BraidKnot/MuPCarrierBarParity.lean` (generic)
     + `content/quantum-observable-universe/lean/QOU/BraidKnot/MuPCarrierOrderWindow.lean` (archimedean)
       (`lean`-direct exit 0 on both + real 4-module import cone via
        `lean-direct-cone.sh`; 0 sorries; `#print axioms` clean on all 11 decls;
        `check-sidecars.sh` clean)

Measured at the proton pin: `t = 2.09754920524e-7` (+209.755 ppb, 9.534 sigma),
`sigma_exp/t = 10.49 %`.

1. **Order window** (Lean `order_window`, scope-(b) vs the stated class). A monomial
   `t = |c|*hbar_q^k` with small-height `|c| in [1/5,5]` forces `k in {6,7}`
   (`c_6 = 0.22169`, `c_7 = 2.23747`). Kills the Ohtsuki / volume-conjecture reading:
   1-loop overshoots 4.7e5x, 2-loop 4.7e4x. NOT claimed: the `|c| in [1/2,2]`
   emptiness — knife-edge (`c_7` -> 2.003 at -1 sigma).
2. **Bar-parity selection rule** (Lean, generic `[Field K]`). `hbar_{q^-1} = -q*hbar_q`,
   so the bar-even monomials are exactly the tower of `w := q*hbar_q^2 = [2]_q - 2`.
   Consequence, proved against the *production* defs: **`delta_R9` and `delta_V9` of
   `MmuR9V9Closure.lean` are bar-MIXED** — they fail the same precondition that
   disqualified the projector shift (#2584). Exclusion is *conditional* on that
   precondition, which is argued (4_1 amphichirality) not proved. And the bar-even
   `w`-tower admits **no** order with a small-height coefficient (j=3 -> 0.16211,
   j=4 -> 14.877).
3. **Entropy bound.** `t` is a **0.98-significant-digit** datum; the indistinguishable
   order-6 window `c in [0.19844, 0.24494]` is 21 % wide and swallows 12/12 hand-listed
   small-height constants — including 0.2075, the coefficient of an *already-refuted*
   mechanism. Matching cannot identify a closure; only an a-priori coefficient can.
   Corollary: `delta_V9` is **19.45x below** the resolution of the datum it closes, and
   `R9+V9` (-1.418 ppb) is five times *worse* than `R9` alone (-0.287 ppb).

Stays clear of the permanent q_0-derivation gate (`qou-eic1`): `q_0` is held fixed.
Touches neither `F_Bor` nor the Borromean trace, so no exposure to the unconfirmed
6.7 % `tr_M_atomic` convention gap under `qou-3qrv`.

## GAP (open) — what would actually close this

A **bar-even** correction, not a single monomial (requirement 2 above rules pure
monomials out in both `hbar_q` and `w`), whose coefficient is **fixed before the fact**.
The only surviving route named in the corpus is the Sigma(2,3,5) WRT / s5-so3 Habiro
series (bean `s5bb`), whose coefficients come from quantum topology rather than from
matching. Nothing here advances that route; it only shows every cheaper route is closed.

## Follow-up filed (not actioned — out of scope for this branch)

Relabel the `MmuR9V9Closure.lean` m_mu rungs to record (i) bar-mixedness and
(ii) that `delta_V9` is sub-resolution, and re-measure its quoted "0.036x L2 miss" at
the documented proton pin (not reproducible there: R9+V9 gives -1.418 ppb).



## 2026-09-03 (session tender-keller) — consolidation pass, claimed

Owner picked the s5-so3 / GAP-A-4 lane ("4") among four. Corpus-grep before
acting: the WRT line for W_lambda reached its deflationary terminus 2026-06-22
(s5bb: WRT data and W_lambda are Schur-Weyl DUAL, not equal); qou-2v7k names the
real wall as the Beasley-Witten S^3/2I localization construction (class
BWVacuumRowIsHecke, no genuine instance) with NO in-session tractable probe. So
there is no honest first step on the CONSTRUCTION this session. What IS bounded
and formalize-first: consolidate this bean's three prunes into one Lean
exclusion — a bar-even monomial in (hbar_q, q) with small-height coefficient
cannot carry the 209.755 ppb residual at the proton pin (bar-even forces the
w-tower, w = q + 1/q − 2; the w-tower has no small-height order: t/w^3 ≈ 0.162,
t/w^4 ≈ 14.9). The w-tower half was MEASURED here, never Lean-proved. Target
file: QOU/BraidKnot/MuPCorrectionAdmissibility.lean (additive; does not touch
GapA4MuonBranching.lean). Scope (b) on that class; constructs nothing.
