# Reeb-flow pn-bond magnitude — provenance check + [1⁴] extension

**Date:** 2026-07-06 · **Branch:** `claude/norm-mass-binding-gap-fpdr4n` (PR #3436)
· **Discipline:** corpus-grep + (a)/(b) refutation scoping (AGENTS.md). Read-first
record for the ²H "reeb-flow" tier that landed on `main` 2026-07-06.

## 1. What landed (owner commits, 2026-07-06)

Commits `8275655551` (+ duplicate `d8f0b3b94d`), `17264f2a9c`, witness refresh
`e2ed15845d`, merged as `5990db457c` (branch
`claude/reeb-flow-mass-integration-2026-07-06`, no PR):

- **`computations/categorical_q_decay_ba_low_isotopes.py`** — the deuteron tier
  switched from `term-1-plus-4` to **`reeb-flow (pn-bond sub-ceiling magnitude)`**:

  $$g_{\text{reeb}} = \frac{1}{\sqrt{5 + (q_0-1)^2/q_0}} \approx 0.446727,
  \qquad B(^2\mathrm{H}) = 5\,g_{\text{reeb}} \approx 2.23364\ \text{MeV}.$$

- **`computations/mass_binding_dashboard.py`** — the pn entry of the per-bond
  log-suppression table is overridden by `(5·g_reeb)/α` in place of the
  `tr_M`-derived `ln(tr_free/tr_atom)`.

Actual accuracy: **+0.408 %** vs AME (2.23364 vs 2.224566). The landing
hardcoded `err_pct: 0.0` in the tier's return dict; fixed on this branch to the
computed value (the layer-1 caller already recomputed the correct error, so the
committed witness rows were unaffected).

## 2. Provenance findings (corpus-grep, all four paths)

| Piece | Status | Evidence |
|---|---|---|
| the **5** under the radical | **DERIVED** | it is $\lvert\mu_{\min}\rvert^2$ of the read-off [1⁴] sign pattern (pp = +1, nn = −1, pn = ±1): $\mu_{\min} = -\sqrt5$, physicality ceiling $g < 1/\sqrt5$ — [`b4_1four_complete_graph_writhe_signs.py`](../../computations/probes/b4_1four_complete_graph_writhe_signs.py) (PR #3426) |
| the deformation term $(q_0-1)^2/q_0$ | **ASSERTED** | appears nowhere else in the corpus (grep over `computations/`, `docs/`, `content/`); no derivation doc, no witness derivation field, no `-- Ref:` |
| the **linear law** $B = 5g$ | **ASSERTED** | code comment "Binding is strictly 5*g" only; not the $A{=}2$ case of the pinned $b_4 = -\ln\det(I+G)$ form (§3, Q1) |
| the pn **sign** | **still open** | the landing supplies magnitude only; the sign enters squared at $A{=}2$ and is unresolved for [1⁴] |
| Reeb-flow origin ($Lk_R^{(k)}$, #3407) | **not yet connected** | #3407 was a stub at the time of the #3426 spec comment; no corpus artifact ties $g_{\text{reeb}}$ to a computed Reeb linking bound |

**Scope note.** Nothing here refutes the landed value — at the ceiling itself
$B = 5g$ gives $\sqrt5 \approx 2.23607$ (+0.52 %), and the deformation term
moves it the right direction (+0.41 %). The finding is a **provenance gap**:
two of the three ingredients are currently asserted, not derived, and the tier
note should not be read as "derivation complete".

## 3. [1⁴] extension at the landed magnitude (new probe)

[`b4_1four_reeb_flow_magnitude.py`](../../computations/probes/b4_1four_reeb_flow_magnitude.py)
(+ witness, 3/3 assertions) consumes $g_{\text{reeb}}$ verbatim (no tuning, no
$w_{pn}$ selection):

**Q1 — deuteron reconciliation.** The determinant form at $A{=}2$
($\det(I+G_2) = 1-g^2$, sign-independent) gives
$E_0\cdot(-\ln(1-g^2)) \approx 0.932$ MeV (**−58 %**), while the landed linear
$5g$ law gives +0.41 %. **The two forms are distinct assertions**; the linear
law is not the $A{=}2$ specialisation of $b_4 = -\ln\det(I+G)$. Reconciling
them (or deriving the linear law independently) is open.

**Q2 — [1⁴] at $g_{\text{reeb}}$.** The sub-ceiling magnitude restores
physicality for the mixed-sign patterns (they were $\det<0$ at the naive bond
factor $z\approx0.499$), with headroom $1-\sqrt5\,g_{\text{reeb}} \approx
1.09\times10^{-3}$:

| $w_{pn}$ | $\det(I+G)$ | $E_0\cdot(-\ln\det)$ | vs $b_4=9.243$ | vs full $B(^4\mathrm{He})=28.296$ |
|--:|--:|--:|--:|--:|
| ±1 | 0.0017407 | 26.596 MeV | 2.877× | **0.940×** |
| 0 | 0.64070 | 1.864 MeV | 0.202× | 0.066× |

($w_{pn}=+1$ and $-1$ are isospectral — conjugation by
$\mathrm{diag}(1,1,-1,-1)$ — asserted in the witness.)

**Reading (scope-(a) throughout).** At the landed magnitude the mixed-sign
[1⁴] determinant lands at **0.940× of the full ⁴He binding** (−6.0 %) — not at
the connected-excess convention $b_4 = 9.243$ (2.877×). If the determinant form
is meant to produce the *connected excess*, the landed magnitude overshoots by
~2.9×; if it is meant to produce the *full* binding, it is 6 % low. Neither
match is claimed; the numbers constrain the (form, magnitude, convention)
combination, not the ingredients.

## 4. Open objects (sharpened)

1. **Derive** $g_{\text{reeb}}$ — i.e. the $(q_0-1)^2/q_0$ deformation of the
   $\sqrt5$ ceiling — from the Reeb $Lk_R^{(k)}$ bound (#3407) or another
   framework invariant, with a `-- Ref:`-able artifact.
2. **Reconcile** the linear $B = 5g$ law with $b_4 = -\ln\det(I+G)$ (Q1 above):
   one of the two is not fundamental at both $A{=}2$ and $A{=}4$.
3. **Pin the $b_4$ convention** the determinant form targets (connected excess
   vs full binding) before any further magnitude work — the 0.940×-full result
   makes the convention choice load-bearing.
4. The pn **sign** (unchanged from #3426).

## 5. Cross-references

- Sign/ceiling predecessor: [`2026-07-06 GAP-A-4 writhe design doc`](../design/2026-07-06-gap-a4-writhe-derivation-lit-review-and-framework.md), probe `b4_1four_complete_graph_writhe_signs.py` (PR #3426).
- Option-E ledger entries 2026-07-06 ([`option-e.md`](../coordination/option-e.md)).
- Norm-route disposition (this branch's theme): [`2026-07-03-qbar-norm-repitch-assessment.md`](2026-07-03-qbar-norm-repitch-assessment.md) §3–§3b (Gram-norm near-conservation / trace phase collapse).
