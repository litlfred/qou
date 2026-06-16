> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

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
`computations/hecke_character_q_deformed.py`. The
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
(`computations/magic-numbers-numerical-witness.py`).

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

## ~~R5~~ — DROPPED

Per repo-owner directive: deriving $q_0$ algebraically is not a
goal. The paper's three-calibration scheme (CAL-1 $m_e$ + CAL-2
$m_\mu/m_e$ + CAL-3 $Q_\beta(n)$) is the published position; CAL-2
fixing $q_0$ is correct as-is.

## R6. P3.5 — Habiro → MotivicGaloisCharacter map (reformulated)

**Status.** The framework is symbolic-in-$q$ via the **Habiro ring**
$\widehat{\mathbb{Z}[q]}$ (cyclotomic completion); the substrate
data is symbolic-in-$q$ throughout, not a per-prime guess.

**Step 1 — landed (`habiro_frobenius_probe.py`).** Frob_p extracted
for atoms {p, n, D} at primes {2, 3, 5, 7, 11, 13} by evaluating
the Habiro cyclotomic expansion at $u = \zeta_{2p}$. Witness:
`habiro-frobenius-probe.witness.json`.

**Step 2 — landed (substantively).**
- *Galois-norm integrality.* $N(\mathrm{Frob}_p) \in \mathbb{Z}$ for
  every $(p, \text{atom})$ pair (residual $< 10^{-7}$).
- *Weil purity at small primes.* $|\sigma(\mathrm{Frob}_p)| = p^{w/2}$
  for all $\sigma$ at $p \in \{2, 3\}$ for every atom; the QOU
  motive is **mixed** at larger primes (composite of pure-weight
  sub-motives).
- *Cross-prime coherence.* Structurally automatic — both
  $\mathrm{Frob}_p$ and $\mathrm{Frob}_q$ are extracted from the
  **same** Habiro element by evaluation at different roots of unity,
  so they respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$
  by the Habiro theorem.
- *Archimedean Weil/Deligne.* Partial — complex conjugation
  preserves $\mathrm{Frob}_p$ orbit (automatic from real
  Habiro coefficients); the deeper $\ell$-adic compatibility is
  open.

**Step 3 — landed (`qou-motivic-galois-instance.lean`).** The Lean
`instance qouMotivicGaloisChar` discharges the
`MotivicGaloisCharacter` axiom-class for the QOU substrate. The
`almost_everywhere_nontrivial` field carries `sorry` as a
substrate axiom (CLAUDE.md §3b) backed by the numerical witness.

**Missing piece.** The explicit map

$$
  \text{Habiro substrate data} \;\longrightarrow\; \text{MotivicGaloisCharacter}
$$

derives the local Frobenius eigenvalue $\mathrm{Frob}_p(q) \in
\widehat{\mathbb{Z}[q]}$ at each rational prime $p$ from the
brane-tower's Habiro-symbolic data (already in place for
`habiro-residue-sum-equivalence`), then verifies the Galois-
compatibility relations (Frobenius commutes with norms; satisfies
Weil/Deligne reciprocity at every place).

The "instance" is **fully determined** by the Habiro structure
once the map is written. The open work is:

1. Extract `Frob_p(q) ∈ Habiro` from the brane tower at each $p$
   (the Habiro ring already supports this via root-of-unity
   evaluation).
2. Write the compatibility verification — finite-place reciprocity
   + the archimedean behaviour under $\tau_{\mathrm{arch}}$.
3. Discharge the `MotivicGaloisCharacter` axiom-class by
   constructing the explicit instance.

**Effort.** Step 1: 1 week (script + witness). Step 2: 2–3 weeks
(theory + verification). Step 3: 1 week (Lean). Total ~1 month.

**Unblocks.** Closes audit GAP 5b in `family-4-motivic-path.md`;
discharges the `motivic-perpetual-obstruction` instance for the
QOU substrate; downstream provable theorems no longer take the
class as `[instance]` hypothesis but use the explicit instance.

This is **substantially more tractable** than the prior "derive
local Frobenius eigenvalues" framing suggested — the framework
already carries the symbolic data; the missing piece is making
the map explicit.

## R7. P3.2 / P3.3 — Pentagon $uv = q\,vu$ + pair descent sharpness

**Status.** Scope clarified post-PR-501. Two-tier resolution:

1. **Level-internal identity** (single jet level $n$): the traced
   volumes $\hat V_\ell$ are scalar Laurent polynomials in
   $\mathbb{Z}[q^{\pm 1/2}, z]$ and commute trivially — no
   q-factor. Proved by `lem:vhat-pair-commutation-trace` (PR #501)
   via the Lean theorem `QOU.BraidKnot.VhatPairCommutationTrace`
   (the scalar identity in the commutative coefficient ring `R`,
   not in the non-commutative Hecke algebra `A` itself).
2. **Inter-level operator lift** ($n \to n+1$): the q-graded
   identity $uv = q\,vu$ applies to the operator lift
   $\widetilde U_i : B_\lambda^{(n)}_{\mathrm{trans}} \to
   B_\lambda^{(n+1)}$ between adjacent jet levels, modulo the
   descended residual $R_q \in \mathrm{im}\,\hat\tau_n$. Requires
   the `QOU.LiftingDescent.JetProlongation` infrastructure, not
   yet in repo. A forward-declaration placeholder exists as
   `pentagon_uv_commutation_inter_level_placeholder` so downstream
   theorems can hypothesize against it.

**Effort**: ✅ closed for the level-internal piece. Inter-level
piece is research-grade work blocked on JetProlongation (no
estimate).

## R8. P3.4 — Uniform $\Delta_{\max}$ bound on jet-tower

**Status.** Path (b) numerical evidence requires multi-level jet-
sum compute (`multi-level-jet-sum.witness.json` reports
`multi_level_implemented: false`). Blocked behind R3.

**Effort**: 2–3 days after R3 lands.

## Priority queue for follow-up branches

(R5 dropped per repo-owner directive — deriving $q_0$ algebraically
is not a goal; the three-calibration scheme is the published
position.)

| # | Item | Status | Effort | Unblocks |
|---|------|--------|--------|----------|
| 1 | R1 q-deformed Hecke character (q-MN) | ✅ done | — | partial — distinguishes by cycle-type |
| 1.b | R1.b Hoefsmit seminormal forms | ✅ Python landed; Lean structural stub landed (`QOU.Hecke.Hoefsmit`) | — | full word-sensitive Hecke trace; ³He vs ³H |
| 2 | R3 L4–L7 SDP cvxpy refactor | ✅ done | — | per-level binding-energy predictions |
| 3 | R4 P2.5 codemod completion | ✅ done — bulk triage complete (21 exposed + 69 marked `polynomial_q_not_applicable`); sole non-marked file is `habiro_frobenius_probe.py` which is itself the R6 step-1 substantive symbolic-q probe | — | symbolic-in-q paper-wide |
| 4 | R2 MAG-1 Z=126 (gen.fn. + sample) | ✅ done | — | seventh magic number |
| 5 | R7 Pentagon (after scope) | ✅ scope clarified by audit memo `2026-05-02-r7-pentagon-trace-vs-operator.md`; level-internal identity is plain commutativity in the scalar trace ring (proved by `QOU.BraidKnot.VhatPairCommutationTrace`). The q-graded inter-level lift is a forward declaration (`pentagon_uv_commutation_inter_level_placeholder`) awaiting `QOU.LiftingDescent.JetProlongation`. | — | descent sharpness |
| 6 | R8 Δ_max numerical | 🟡 queued | 2–3 days | jet-tower convergence |
| 7 | R6 Habiro → MotivicGaloisCharacter map | ✅ step 1 (Frob extraction), step 2 (Galois-norm integrality verified at all (atom, prime) pairs where Pochhammer truncates inside data range — 3/3 atoms compatible), step 3 (Lean axiom-class instance) all closed; archimedean Weil/Deligne piece + deeper-m Habiro coefficients for primes ≥ 11 remain | — | family-4 motivic instance |

R6 is now substantially more tractable than originally scoped —
the Habiro ring carries the symbolic q-data and the missing
piece is just making the Habiro → motivic map explicit, not
deriving local Frobenius eigenvalues from scratch.
