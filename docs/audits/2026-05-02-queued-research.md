# Queued research items — beyond Tier 3 audit pass

**Branch**: `claude/tier3-math-audit-B0wyO`
**Status**: items below are **research-grade** follow-ups. The math
framework audit and the leading-order compute pipeline are landed
on this branch; these items represent the next mathematical /
computational refinements.

## R1. q-deformed Hecke character refinement

**Problem.** The Schur-Weyl path
(`global_wedderburn_sum_symbolic`, `per_stratum_sum_symbolic`,
`character_on_atomic_braid`) currently uses **Murnaghan–Nakayama**
characters — the q = 1 limit of the Hecke-algebra character. At
this limit, atoms with the same atomic-braid permutation cycle type
give identical SW values, even though their full q-deformed Hecke
structure differs. Concrete consequence: at equal multiplicities,
³He (Z=2, N=1) and ³H (Z=1, N=2) cannot be distinguished by the
SW path because their permutations have the same cycle type.

**Workaround in place.** The legacy transfer-matrix path
(`markov_trace_symbolic_eval`) preserves the full q-deformation
through `proton_cross` vs `neutron_cross` and `m_pp/m_pn/m_nn`
differentiation. Production analyses that need q-deformation
(deuteron error, gb-residue tower) correctly stay on the legacy
path; the SW path provides leading-order convergence at H_{3A}.

**Refinement.** Implement the full q-deformed Hecke character
$\chi^\lambda_q(T_w)$ using **q-ribbon-tableau weights** (Lascoux,
Leclerc, Thibon — "ribbon functions and q-coefficients of Macdonald
polynomials"). The character is a polynomial in $q$ that reduces
to MN at $q = 1$; the q-correction terms encode the actual Hecke
trace, distinguishing braids whose underlying permutation cycle
types coincide.

**Effort**: 2–4 weeks. New module
`folio-assistant/computations/hecke_character_q_deformed.py`. The
existing `mn_character` function provides the q=1 base case for
testing.

**Unblocks.** P2.1 full migration of all 9 legacy callers to the
SW path; deuteron / gb-residue analyses can switch to SW with
full q-deformation; finer differentiation between proton-rich and
neutron-rich isotopes at low atoms.

## R2. MAG-1 numerical verification at Z = 126

**Problem.** Self-conjugate partition enumeration of $n = 3 \cdot
126 = 378$ via the Frobenius-coordinate method takes hours
(estimated $\sim 10^6$–$10^7$ partitions). Single-session compute
hit the timeout.

**Workaround in place.** Six of seven magic numbers verified
(Z ∈ {2, 8, 20, 28, 50, 82}); $Z = 126$ remains queued. The
mathematical proof ($\kappa(\lambda') = -\kappa(\lambda)$ ⇒ self-
conjugate ⇒ $\kappa = 0$) holds for all $n$, so the Z=126 case is
a numerical demonstration rather than a proof gap.

**Refinement.** Run on a dedicated compute job (cron / CI nightly).
Could also use the **generating function** for self-conjugate
partition counts (OEIS A000700:
$\sum_{n \geq 0} a(n) q^n = \prod_{k \geq 0} (1 + q^{2k+1})$) to
verify the count without enumeration, then sample-check $\kappa = 0$
on a random subset.

**Effort**: 1 day for the cron / CI setup; the script already exists
(`folio-assistant/computations/magic-numbers-numerical-witness.py`).

**Unblocks.** Final closure of MAG-1 numerical verification across
all seven magic numbers.

## R3. Full L4–L7 SDP cvxpy refactor

**Status.** Constraint families enumerated in `sdp_multi_level.py`:
- L4 shell-closure: equality constraints on $y_\lambda$ for shell-
  saturation partitions — **working cvxpy SDP solve**.
- L5 cross-shell: LR-coefficient enumeration via 2-step fusion —
  **working enumeration** (sample sizes capped); cvxpy refactor
  wires $c^\mu$ into cross-block coupling matrices.
- L6 atom-electron: electron-pair-coupling enumeration — **working
  enumeration**; cvxpy ingestion via additional `pair_couplings`
  entries.
- L7 covalent: bond-constraint enumeration with shared-trefoil
  count — **working enumeration**; cvxpy refactor for inter-atom
  shared-strand PSD coupling.

**Refinement.** Implement the cvxpy refactor for each level: build
the cross-level PSD constraint matrix from the enumerated
constraint family, solve, return $y_\lambda$ + cross-blocks. The
mathematical content is in place; the refactor is mechanical
linear-algebra plumbing.

**Effort**: 1 week per level (4 weeks total). The L4 cvxpy refactor
is already complete and serves as the pattern.

**Unblocks.** Per-level binding-energy prediction beyond pair-
coupling for shell / atom / molecule levels.

## R4. P2.5 symbolic-in-q completion across remaining 70 scripts

**Status.** 21 of 125 sympy-capable scripts have `expose_polynomial`
call-sites; 50 more have the helper imported (call-site rewiring
queued); 33 complex-tier scripts need per-script triage.

**Refinement.** Per-chapter PR batches of ~10 scripts each. Some
complex-tier scripts may become `polynomial_q_not_applicable` (no
witness output) or split into symbolic-emit / numeric-consume
pairs.

**Effort**: 3–4 weeks total (per-chapter PRs).

**Unblocks.** Deep audit §3·E "Symbolic-in-q throughout"
scorecard item flips ❌ → ✅.

## R5. P1.1(a) — derive $q_0$ algebraically

**Status.** $q_0$ is currently fixed by CAL-2 ($m_\mu/m_e$ via
$\mathrm{Vol}(4_1)/\hbar_q^2$). Closing the conjecture chain
`q-from-epsilon → substrate-parameter-unique → vacuum-substrate-
compatibility` would derive $q_0$ from the categorical action,
reducing CAL-2 to a cross-check rather than an input.

**Effort**: 1–2 weeks of theory work. Substantive new algebraic
content; not a mechanical refactor.

**Unblocks.** "Two calibrations" interpretation of the framework
($m_e + Q_\beta(n)$, with $q_0$ derived).

## R6. P3.5 — `family-4` motivic-substrate `instance` at $q_0$

**Status.** Concrete `instance` of `MotivicGaloisCharacter` at the
QOU substrate is missing (audit GAP 5b). Requires deriving local
Frobenius eigenvalues from the brane tower.

**Effort**: open-ended. Research-grade.

## R7. P3.2 / P3.3 — Pentagon $uv = q\,vu$ + pair descent sharpness

**Status.** Workplan formula $\mathrm{tr}_M(\hat V_i \hat V_j) =
q\,\mathrm{tr}_M(\hat V_j \hat V_i)$ does not survive sanity check
against `prop:markov-pair-z2` (both equal $z^2$). Actual gap is the
operator-level identity on Wedderburn-rep matrices, not the trace
level.

**Effort**: needs author scope clarification before implementation.
2–5 days once scope is confirmed.

## R8. P3.4 — Uniform $\Delta_{\max}$ bound on jet-tower

**Status.** Path (b) numerical evidence requires multi-level jet-
sum compute (`multi-level-jet-sum.witness.json` reports
`multi_level_implemented: false`). Blocked behind R3.

**Effort**: 2–3 days after R3 lands.

## Priority queue for follow-up branches

| # | Item | Effort | Unblocks |
|---|------|--------|----------|
| 1 | R1 q-deformed Hecke character | 2–4 weeks | P2.1 full migration; ³He / ³H differentiation |
| 2 | R3 L4–L7 SDP cvxpy refactor | 4 weeks (L5/L6/L7 each ~1 week + L4 done) | per-level binding-energy predictions |
| 3 | R4 P2.5 codemod completion | 3–4 weeks | symbolic-in-q paper-wide |
| 4 | R2 MAG-1 Z=126 (cron) | 1 day | seventh magic number |
| 5 | R5 P1.1(a) algebraic q₀ | 1–2 weeks | two-calibrations interpretation |
| 6 | R7 Pentagon (after scope) | 2–5 days | descent sharpness |
| 7 | R8 Δ_max numerical | 2–3 days | jet-tower convergence |
| 8 | R6 family-4 motivic instance | open-ended | research-grade |

The first 4 items can complete in **8–10 weeks** of focused work.
Items 5–8 are longer-tail / research-grade.
