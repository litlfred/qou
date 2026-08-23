# Route D: formal q-Borel transform of C1 vs GGM eq 49 (2026-07-20)

**Question.** The diagonal-gauge prune
([`2026-07-20-qlift-ggm-gauge-prune.md`](2026-07-20-qlift-ggm-gauge-prune.md))
left "q-Borel / summation-type transforms" on the not-excluded list. Route D
tests the **formal** q-Borel transform: apply it to the proved C1 kernel
`[m+1]_q · b_{m+1} = b_m + b_{m−1}` (the q-analogue, on the generating-series
level, of Borel-transforming `f′ = (1+x)f`) and compare the transformed
recurrence to GGM eq 49 `y_{m+1} − (2 − q^m)·y_m + y_{m−1} = 0`
(arXiv:2012.00062 p. 14, `library/arxiv-2012.00062v3/2012.00062v3.pdf`) — exact match, match up
to diagonal gauge, or still distinct.

## 0. Convention (RSZ) and why

Ramis–Sauloy–Zhang (`library/arxiv-0903.0853v3/0903.0853v3.pdf`, **Definition 2.3.3**, §2.3.1
p. 23, under their standing convention |q| > 1) define the level-1 formal
q-Borel transform by the **theta-kernel** coefficient map

$$
\mathcal{B}_{q,1} f(\xi) \;=\; \sum_n \frac{f_n}{q^{n(n-1)/2}}\, \xi^n ,
\qquad\text{i.e.}\qquad f_n \;\longmapsto\; f_n\, q^{-n(n-1)/2} .
$$

RSZ §1.2.1 notes explicitly that q-Borel/q-Laplace kernels are **not
canonical** — the q-exponential-kernel variant divides by `(q;q)_n` instead.
We take the RSZ theta convention as **primary** because (i) it is the one the
referenced text actually defines, and (ii) the theta weight `q^{m(m−1)/2}` is
exactly the growth unit of GGM eq 49's dominant solution at |q| > 1
(`y_{m+1} ≈ q^m y_m`), so it is the transform that absorbs the C1↔GGM growth
mismatch. Both variants, **and both directions** (Borel `w_m = q^{−m(m−1)/2}`
or `1/(q;q)_m`; inverse/q-Laplace `w_m = q^{+m(m−1)/2}` or `(q;q)_m`), act on
coefficients as a **diagonal weight** `y_m = w_m b_m` — the conclusion below
is convention-independent, proved via a gauge invariant (§2).

## 1. Transformed recurrences (by hand)

Substitute `b_m = w_m^{-1} y_m` into `[m+1]_q b_{m+1} = b_m + b_{m−1}` and
clear the m-slot weight. Exponent bookkeeping for the theta weight:
`m(m+1)/2 − m(m−1)/2 = m` and `(m−1)(m−2)/2 − m(m−1)/2 = −(m−1)`.

| Variant (weight `y_m = w_m b_m`) | Transformed kernel |
|---|---|
| **B: RSZ theta Borel**, `w_m = q^{−m(m−1)/2}` | `[m+1]_q\,q^{m}\; y_{m+1} = y_m + q^{-(m-1)}\, y_{m-1}` |
| **L: theta Laplace (inverse)**, `w_m = q^{+m(m−1)/2}` | `[m+1]_q\,q^{-m}\; y_{m+1} = y_m + q^{m-1}\, y_{m-1}` |
| **L′: q-exponential Laplace**, `w_m = (q;q)_m` | `y_{m+1} = (1-q)\, y_m + (1-q)(1-q^m)\, y_{m-1}` |

(For L′ use `[m+1]_q/(1−q^{m+1}) = 1/(1−q)` and
`(q;q)_m/(q;q)_{m−1} = 1−q^m`.) **Shape comparison with GGM eq 49:** the L′
form is structurally the closest — monic after trivial rescale, constant
middle coefficient, `q^m` entering linearly in exactly one slot — but the
`q^m` sits in the **y_{m−1} slot**, whereas GGM carries it in the **y_m
slot**. The B and L forms retain m-dependent outer coefficients. None is an
exact match.

## 2. Diagonal-gauge matching on the transformed kernel — the invariant

Write a three-term kernel as `A_m y_{m+1} + B_m y_m + C_m y_{m−1} = 0`
(all coefficients nonzero). A diagonal gauge `y_m = g_m \tilde y_m` rescales
`(A_m, B_m, C_m) ↦ (A_m g_{m+1}, B_m g_m, C_m g_{m−1})`, so

$$
I_m \;:=\; \frac{C_m\, A_{m-1}}{B_m\, B_{m-1}} \qquad (m \ge 2)
$$

is **diagonal-gauge invariant**, and it is **complete**: fixing the middle
coefficient via the ratio `g_m/g_{m+1}` (constraint (A) of the prune doc)
uses up the entire gauge freedom, after which the `y_{m−1}` coefficient
equals `I_m × (\text{target } B_m B_{m-1}/A_{m-1})` — two kernels are
diagonal-gauge equivalent **iff** their `I_m` agree for all m ≥ 2.

Computing `I_m` for every presentation of C1 (the q-power/`(q;q)` factors
cancel telescopically — e.g. for B: `(−q^{1−m})·[m]_q q^{m−1}/((−1)(−1)) =
−[m]_q`):

| Kernel | `I_m` |
|---|---|
| C1 original (`A_m=[m+1]_q, B_m=C_m=−1`) | `−[m]_q` |
| C1 after theta-Borel B | `−[m]_q` |
| C1 after theta-Laplace L | `−[m]_q` |
| C1 after q-exponential Laplace L′ | `−(1−q)(1−q^m)·1/(1−q)^2 = −[m]_q` |
| **GGM eq 49** (`A_m=1, B_m=−(2−q^m), C_m=1`) | `1/((2−q^m)(2−q^{m−1}))` |

The formal q-Borel transform — any kernel, any direction — **does not move
`I_m` at all**: it is itself a diagonal gauge, and `I_m` is the invariant of
that class. Equality `I_m^{C1} = I_m^{GGM}` is exactly the prune doc's
consistency condition `[m]_q (2−q^{m−1})(2−q^m) = −1` (c = 1), which fails
identically (LHS non-constant in m). This re-derives the prune's exclusion by
an independent method (gauge invariant vs over-determination) and extends it
verbatim to the transformed kernels.

## 3. Residual difference operator (explicit)

Spend the full gauge freedom matching GGM's `y_{m+1}` and `y_m` coefficients
(always possible). The gauged C1 kernel — same for every q-Borel variant — is

$$
y_{m+1} - (2-q^m)\, y_m \;-\; [m]_q (2-q^m)(2-q^{m-1})\, y_{m-1} \;=\; 0 ,
$$

so the residual against GGM eq 49 is the order-0 tail operator

$$
\bigl(K_{\mathrm{C1,gauged}} - K_{\mathrm{GGM}}\bigr)\, y
\;=\; -\,\mathcal{C}_m\, y_{m-1},
\qquad
\mathcal{C}_m := [m]_q (2-q^{m-1})(2-q^m) + 1 ,
$$

with `\mathcal{C}_m` the prune doc's consistency residual — numerically
`|\mathcal{C}_m| ≈ 0.90 … 222` on the tested grid, never small. (Sign
convention: on a solution of the gauged C1 kernel, the GGM form evaluates to
`+\mathcal{C}_m y_{m−1}`; probe V4 verifies this identity to 1e−45.)

## 4. Numerical verification

[`computations/probes/qlift_routeD_qborel_transform_probe.py`](../../computations/probes/qlift_routeD_qborel_transform_probe.py)
(mpmath dps = 50, q ∈ {0.9, 1.05, 1.10998}, m ≤ 15; kill criterion
pre-stated: diagonal closure iff `max_m |I_m^{C1} − I_m^{GGM}| < 1e−40`).
Witness:
[`qlift_routeD_qborel_transform_probe.witness.json`](../../computations/probes/qlift_routeD_qborel_transform_probe.witness.json).

| Check | Result |
|---|---|
| V1 transformed-kernel identities (B, L, L′) on the proved solution `b_n = I_q(n)/[n]_q!` | relative residuals < 1e−45 at every m, q — §1 table exact |
| V2 invariance: `I_m` from all four C1 presentations vs `−[m]_q` | agreement < 1e−45 — the transform provably does not move the invariant |
| V3 mismatch `Δ_m = −[m]_q − 1/((2−q^m)(2−q^{m−1}))` | min\|Δ_m\| ≈ 2.7, max up to ≈ 610 — fails at every m ≥ 2, every q |
| V4 residual-operator identity: GGM form on the (A)-gauged theta-B solution equals `\mathcal{C}_m y_{m−1}` | identity holds < 1e−45; `\|\mathcal{C}_m\|` ≥ 0.90 |

## 5. Verdict and scope

**STILL DISTINCT — and the formal q-Borel route is CLOSED, negatively.**
Scope-(b) structural exclusion, sharpening the prune doc: the formal
(coefficient-level) q-Borel / q-Laplace transforms — theta kernel or
q-exponential kernel, either direction — are diagonal weights, hence lie
**inside** the diagonal-gauge class already excluded; the invariant cited is
the exact mismatch `I_m^{C1} = −[m]_q` vs
`I_m^{GGM} = 1/((2−q^m)(2−q^{m−1}))` at any two consecutive m (equivalently
the prune's consistency condition). No convention factor can rescue this:
`I_m` is convention-independent (§2 table). The transform *does* change the
kernel's shape usefully — L′ relocates all m-dependence into a single linear
`q^m` in the `y_{m−1}` slot, the closest diagonal representative to GGM —
but the slot mismatch is exactly the invariant obstruction.

**Bar-parity (secondary, scope-(a)).** Bar `q ↦ q^{−1}` swaps
`\mathcal{B}_{q,1}` with its inverse (the weight is bar-odd in the exponent)
and multiplies solution bar-ratios by the fixed q-power `q^{m(m−1)}`; since
the C1 solution's bar-ratio is not `±q^{\text{integer}}` (prior probe T3),
the transformed solution still cannot carry GGM's exact `±1` parity (Thm 9).
Consistent with, but not needed for, the §2 exclusion.

**Explicitly NOT excluded** (what "q-Borel" still leaves live): the
**analytic summation content** of q-Borel–Laplace — formal Borel, then
**analytic continuation in the Borel ξ-plane**, then discrete q-Laplace
along a spiral (RSZ ch. 5) — whose continuation step mixes all m and is not
diagonal on coefficients; plus the prune doc's non-diagonal 2×2 gauges,
Möbius-of-solution-ratio maps, and inhomogeneous shifts (the Stokes-matrix
route of workplan step 3).

**Discipline.** Formalize-first (both verdict routes derived by hand before
the probe; the probe only verifies displayed identities); no AME data; no
fit; the q-lift identification and `conj:qdifference-kernel-prolongation-symbol`
remain conjectures — nothing here derives them.
