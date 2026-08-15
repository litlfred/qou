# Diagonal-gauge prune: C1 kernel vs GGM eq 49 — workplan step 3 (2026-07-20)

**Question.** Can an m-dependent diagonal gauge `b_m = g_m(q) · y_m` map the
proved C1 kernel `[m+2]_q · b_{m+2} = b_{m+1} + b_m` (q-involution / q-Borel
form; c(q)=1 exact per
[`qlift_kernel_candidate_crosscheck_probe`](../../computations/probes/qlift_kernel_candidate_crosscheck_probe.py))
into the GGM descendant kernel `y_{m+1} − (2 − q^m)·y_m + y_{m−1} = 0`
(eq 49, Garoufalidis–Gu–Mariño, arXiv:2012.00062, `library/arxiv-2012.00062v3/2012.00062v3.pdf`
p. 14)? Formalize-first: the consistency condition is derived symbolically
before any numerics.

## 1. Derivation (by hand)

Align three-term windows at index m: C1 reads `[m+1]_q b_{m+1} = b_m + c·b_{m−1}`
(generic constant c = c(q); the proved case is c = 1). Substitute
`b_m = g_m y_m` (g_m ≠ 0) and divide by `g_{m+1}` (monic normalization is WLOG
— any overall nonzero rescale of the equation preserves its solution set):

$$
y_{m+1} \;-\; \frac{g_m}{g_{m+1}[m+1]_q}\, y_m \;-\; \frac{c\, g_{m-1}}{g_{m+1}[m+1]_q}\, y_{m-1} \;=\; 0 .
$$

Matching GGM eq 49 coefficient-by-coefficient gives **two** constraints on the
**one** free ratio sequence `g_{m+1}/g_m`:

- **(A)** from the y_m coefficient: `g_m / g_{m+1} = [m+1]_q (2 − q^m)`;
- **(B)** from the y_{m−1} coefficient: `g_{m−1} / g_{m+1} = −[m+1]_q / c`.

Chaining (A) at m and m−1 into (B):

$$
\frac{g_{m-1}}{g_{m+1}} = \frac{g_{m-1}}{g_m}\cdot\frac{g_m}{g_{m+1}}
= [m]_q (2-q^{m-1}) \cdot [m+1]_q (2-q^m) \;\stackrel{!}{=}\; -\frac{[m+1]_q}{c},
$$

and cancelling `[m+1]_q` yields the **consistency condition**

$$
c \cdot [m]_q \,(2 - q^{m-1})(2 - q^m) \;=\; -1 \qquad \text{for all } m .
$$

**This fails identically.** The LHS is non-constant in m (at q = 1 it equals
c·m; for real 0 < q^m < 2 it is c·positive and strictly varying), while the RHS
is the constant −1. One gauge freedom, two coefficient constraints: the system
is over-determined, and no choice of the sequence g_m — nor of the constant
c(q) — resolves it. An index shift `b_{m+s} = g_m y_m` only replaces `[m]_q`
by `[m+s]_q`, still non-constant in m; same failure.

## 2. Numerical verification (probe)

[`computations/probes/qlift_ggm_diagonal_gauge_prune_probe.py`](../../computations/probes/qlift_ggm_diagonal_gauge_prune_probe.py)
(mpmath dps = 50, q ∈ {0.9, 1.05, 1.10998}, m ≤ 15; kill criterion pre-stated:
survival iff max_m |C_m| < 1e-40). Witness:
[`qlift_ggm_diagonal_gauge_prune_probe.witness.json`](../../computations/probes/qlift_ggm_diagonal_gauge_prune_probe.witness.json).

| Check | Result |
|---|---|
| P1 consistency residual `C_m = [m]_q(2−q^{m−1})(2−q^m) + 1` | min\|C_m\| ≈ 0.90–2.1, max up to 222 — fails at **every** m, every q |
| P2 direct: g built from (A), y = b/g, eq-49 residual on the proved b_n = I_q(n)/[n]_q! | relative residual 0.68–1.5 at every m — the y_{m−1} coefficient misses everywhere |
| P3 constant-c(q) / index-shift rescue (s ∈ [−2, 2], c free) | spread(S_m) ≈ 3.3–221 ≫ 0; best-over-s max\|C_m\| ≥ 1.01 — no rescue |

## 3. Bar-parity remark (secondary, scope-(a))

The C1 kernel is **bar-covariant**: `[k]_{1/q} = q^{−(k−1)}[k]_q`, and the
prior probe (T3) found the C1 solution b_n(1/q)/b_n(q) is bar-**neither**
(not ±1, not a fixed q-power; non-integer log_q ratios). GGM Thm 9
(`library/arxiv-2012.00062v3/2012.00062v3.pdf` pp. 14–15) proves the eq-49 fundamental solutions
satisfy exact bar parity `G^j_m(q^{−1}) = (−1)^j G^j_m(q)`, while the eq-49
kernel is bar-invariant only jointly with m → −m.

Does parity **alone** obstruct a diagonal gauge? **Not decisively.** An
unconstrained g_m(q) can carry arbitrary bar-ratio, so the parity mismatch
only bites once the gauge is restricted to a bar-covariant class (e.g. g_m
built from q-integers/q-factorials, whose bar-ratios are signed q-powers) —
there the non-q-power bar-ratios of b_n clash with the ±q^{integer} × parity
structure a gauged GGM solution would impose. That is suggestive but was not
run to a clean exclusion; the decisive argument is the algebraic
over-determination of §1, which needs no parity input. Recorded as a
scope-(a) observation only.

## 4. Verdict and scope

**Scope-(b) structural exclusion — DIAGONAL gauges only.** No m-dependent
diagonal gauge `b_m = g_m(q)·y_m` (including index shifts and any constant
c(q)) maps the C1 kernel into GGM eq 49. Invariant cited (per AGENTS.md
§Before-declaring-refuted (b)): the exact derived identity of §1 — the
consistency condition `c·[m]_q(2−q^{m−1})(2−q^m) = −1` cannot hold for two
distinct m, since the LHS is non-constant in m. This is an algebraic
impossibility, not a failed numerical fit.

**Explicitly NOT excluded** (remain live for workplan step 3's
Stokes-matrix / prolonged-SW-monodromy route):

- **non-diagonal 2×2 gauge transforms** — `(y_m, y_{m+1})ᵀ → A_m(q)·(…)ᵀ`
  with A_m ∈ GL₂ (the natural home given GGM's 2×2 fundamental solution
  W_m(q) with det = 2);
- **Möbius transforms of solution ratios** (projectivized transfer-matrix
  action);
- **inhomogeneous shifts** `b_m = g_m y_m + h_m` (cf. the 4₁ colored-Jones
  recurrence being minimally order-2 *inhomogeneous*);
- **q-Borel / summation-type transforms mixing all m** (Ramis–Zhang kernels).
  **Route-D follow-up (2026-07-20):** the *formal* (coefficient-level) q-Borel
  transform is itself a diagonal weight, hence falls **inside** this doc's
  exclusion — verified independently via the complete diagonal-gauge invariant
  `I_m = C_m A_{m−1}/(B_m B_{m−1})` (= `−[m]_q` for C1 under every kernel
  convention) in
  [`2026-07-20-qlift-routeD-qborel-transform.md`](2026-07-20-qlift-routeD-qborel-transform.md).
  Only the **analytic summation step** (Borel-plane continuation + discrete
  q-Laplace, RSZ ch. 5) remains live under this bullet.

Consequently C1 (q-involution/q-Borel form) and GGM eq 49 are **genuinely
distinct order-2 q-lifts of the same classical depth-2 shadow**, and any
identification must be non-diagonal. This sharpens the prior probe's T2
"DISTINCT under scalar gauge" to "DISTINCT under arbitrary diagonal gauge."

**Discipline.** Formalize-first (derivation preceded and pruned the scan —
no scan was run); no AME data; nothing here is a "derivation" of the q-lift
identification; the conjecture-level status of the q-lift is unchanged.
