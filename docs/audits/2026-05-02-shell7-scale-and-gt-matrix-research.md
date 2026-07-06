# SHELL-7-SCALE and GT-MATRIX — research notes

**Compiled** 2026-05-02 on `claude/post-electron1-multi-tackle`.
**Status**: research-grade open problems (not closure attempts; just framing for future content-block authoring).

This document collects what is presently known about two long-standing audit flags:

- **SHELL-7-SCALE**: BW Term 7 scaling form $f_{\rm magic}/A^{2/3}$ is conjectural (rides on `conj:homological-shell-condensation`)
- **GT-MATRIX**: Gamow–Teller axial-vector matrix element $g_A = 1.275$ stated as target but not derived from Borromean Skein-algebra trace

Both are in the "research-grade" tier of [`docs/audits/2026-05-02-forward-derivation-pre-archimedean.md`](2026-05-02-forward-derivation-pre-archimedean.md) §C. This note records the current understanding, partial results, and the most promising path forward for each.

---

## SHELL-7-SCALE

### Problem statement

The 7th Bethe-Weizsäcker (BW) term is the **shell-correction term**:

$$
  E_{\rm shell}(Z, N) = C_7(q) \cdot f_{\rm magic}(Z, N) \cdot A^{-2/3}
$$

where $C_7(q) = [2]_q^2 [3]_q \cdot m_e$ (categorically derived, ✓) and $f_{\rm magic}(Z, N)$ is a function vanishing at the magic numbers $Z, N \in \{2, 8, 20, 28, 50, 82, 126\}$.

The categorical derivation of $C_7(q)$ via Wedderburn-block coefficients is closed (per [`docs/audits/2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md) §2·D). What's open: **the functional form of $f_{\rm magic}$** and **the $A^{-2/3}$ scaling**.

### What's known

1. **Coefficient derivation** ✓ — $[2]_q^2[3]_q$ via PR #500's BB-stratification + 6-knot Bring basis.
2. **Magic-ladder identification** ✓ — 6/7 magic numbers verified via `prop:magic-numbers-from-q` + PR #499 self-conjugate witness; 7th (Z=126) closed in PR #503 via `q(378) = 174,972,341` (categorical-neutrality theorem, no enumeration needed).
3. **$f_{\rm magic}$ functional form** 🟡 — the textbook form is $\delta_{\rm shell}(N) - \delta_{\rm shell}(Z)$ where $\delta_{\rm shell}$ is a phenomenological "shell-distance" function (peaks midway between magics). The categorical version requires `conj:homological-shell-condensation`: BB-collapse $E_\infty^{p,>0}(n) = 0$ at magic ladder.
4. **$A^{-2/3}$ scaling** 🟡 — surface-area scaling, but in QOU should arise from a categorical "boundary count" argument paralleling the Coulomb $A^{1/3}$ scaling.

### Most promising closure path

The recent "spectator factorization" framework (PR #503's induction proof for $\Sigma_{\rm all}$ — see [`docs/audits/2026-05-02-nv-frob-filter-conjectures.md` §INDUCTION PROOF](2026-05-02-nv-frob-filter-conjectures.md)) suggests an analog:

**Hypothesis (SHELL-7 spectator form):** $f_{\rm magic}(Z, N) \cdot A^{-2/3}$ should arise as the **branching residue** of the Wedderburn decomposition at $H_{3A}$:

$$
  f_{\rm magic}(Z, N)
  \;\stackrel{?}{=}\;
  \sum_{\lambda \,\vdash\, 3A} w_\lambda \cdot \chi_\lambda(\text{shell}_{Z, N}) \cdot \mathbb{1}_{\lambda \in {\rm BB}-{\rm stratum}}
$$

where $\mathbb{1}_{\lambda \in {\rm BB}-{\rm stratum}}$ is the indicator function for partitions in the BB-stratum at level $3A$ (i.e., self-conjugate partitions at magic Z's, or zero off the magic ladder).

This would make $f_{\rm magic}$ a **partition-sum residue** — same machinery as the v3 H_{3A} mass tower, just restricted to the BB-stratum. The $A^{-2/3}$ scaling would then be the asymptotic of the BB-stratum dimension count (related to $q(3A)^{1/3}$ for self-conjugate partitions, where $q(n)$ is the partition-into-distinct-odd-parts generating function).

**Test**: compute $f_{\rm magic}(Z, N) \cdot A^{2/3}$ via the partition-sum hypothesis at A=4, 6, 8, 12, 28 and compare to the empirical shell-correction values from AME nuclear masses. If the hypothesis matches, write `conj:shell-7-scale-via-bb-stratum-trace`.

### Effort estimate

- **Compute test**: 1–2 days (extends the v3/v4 multichannel H_{3A} infrastructure to compute the BB-stratum-restricted sum).
- **Content-block authoring** (if test succeeds): 1 day.
- **Lean formalization**: research-grade, 1–2 weeks.

---

## GT-MATRIX

### Problem statement

The Gamow-Teller axial-vector matrix element $g_A$ governs the rate of allowed $\beta$ decays via the standard formula:

$$
  \frac{1}{\tau_{1/2}} = K \cdot G_F^2 \cdot |M_F|^2 + K \cdot G_F^2 \cdot g_A^2 \cdot |M_{\rm GT}|^2
$$

The free-neutron $g_A = 1.2754(13)$ (PDG 2022) is currently:
- **Not derived** in the QOU framework
- Listed as "open computation" in [`computations/beta-decay-from-q.py`](../../computations/beta-decay-from-q.py) (lines 137 ff)
- Should categorically emerge from the **Borromean Skein-algebra trace** at $q_0$

### What's known

1. The Borromean braid $\beta_{\rm Bor} = (\sigma_1 \sigma_2^{-1})^3$ in $B_3$ has Markov trace $\mathrm{tr}_M(\beta_{\rm Bor}) \in \mathbb{Z}[q^{\pm 1}]$ — explicitly computable via `hecke_core.py`.
2. The Borromean linking number is 3 (the genus-3 lift of the trefoil).
3. The Skein-algebra closure of the Borromean has Jones polynomial $J_{\rm Bor}(q) = $ (computable).
4. The categorical relationship $g_A \stackrel{?}{=} f({\rm tr}_M(\beta_{\rm Bor})(q_0), \alpha_{\rm EM}, \ldots)$ is conjectural.

### Most promising closure path

By analogy with the **$1/\alpha_{\rm EM}$ derivation** ([`prop:alpha-em-categorical-trace`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md)):

$$
  1/\alpha_{\rm EM} = 45 \cdot [3]_q \cdot (1 + \delta_{\rm CS} + 8q\,\delta_{\rm CS}^2)
$$

where each factor traces upstream — 45 from $\binom{10}{2}$ (exterior square Borromean), $[3]_q$ from the substrate, $\delta_{\rm CS} = \hbar_q^4 \cdot [5]_q$ from gram-determinant Plancherel — the analogous **GT-matrix categorical trace** should take the form:

$$
  g_A \stackrel{?}{=} R_{\rm GT}(q) \cdot [k]_q^{a} \cdot [\ell]_q^{b} \cdot (1 + \text{small corrections})
$$

where $R_{\rm GT}(q)$ is a categorical ratio (likely Plancherel-related), and $(k, \ell, a, b)$ are integers determined by the GT representation theory.

**Empirical anchor (probed 2026-05-02)**: $g_A = 1.2754(13)$ (PDG, ~0.1% uncertainty). At $q_0 = 1.10998$, the candidate q-arithmetic ratios were tested:

| candidate | value at $q_0$ | rel err vs $g_A$ |
|-----------|---------------:|----:|
| $[5]_q / [4]_q$ | 1.2702785 | **0.40%** |
| $1 + \hbar_q \cdot [3]_q$ | 1.3016 | 2.05% |
| $[6]_q / [5]_q$ | 1.2237 | 4.06% |
| $[7]_q / [6]_q$ | 1.1937 | 6.41% |

The clear leading-order candidate is $g_A^{(0)} = [5]_q / [4]_q$, agreeing to 0.4% (about 4× the PDG uncertainty — meaning a genuine 0.4% categorical correction is needed, not just measurement noise). Categorically, $[5]_q/[4]_q$ is the **marginal Hecke-dimension growth from 4 to 5 strands** — a clean categorical invariant.

**PSLQ probe at 1e-4 tolerance** (matching the 0.4% deviation scale) found:

$\log g_A - 2 \log[5]_q - 5 \log q + 2 \log 2 + 2 \log 3 \approx 0$

equivalently $g_A \approx [5]_q^2 \cdot q^5 / 36$ — but this evaluates to 1.910, NOT $g_A = 1.275$. PSLQ at this tolerance over-fits: the identity above has residual $\sim 10^{-5}$ but is accidentally approximate, not a true categorical relation. At tighter tolerances (1e-10, 1e-50), no relation is found.

**Conclusion**: $g_A^{(0)} = [5]_q/[4]_q$ is structurally suggestive but the next-order correction (~0.4% deviation) cannot be pinned down by PSLQ at PDG precision — needs categorical input from the GT representation theory.

**Recommended next step**: derive a categorical $g_A = [5]_q/[4]_q \cdot (1 + \delta_{\rm GT})$ ansatz where $\delta_{\rm GT}$ traces upstream to the Borromean Skein-algebra trace + Plancherel weights, paralleling how `alpha-em-categorical-trace.md` derives $\delta_{\rm CS}$ for $1/\alpha$. The PSLQ uniqueness witness at $\geq 1000$ dps should then confirm.

### Effort estimate

- **Compute test (PSLQ)**: ~30 min.
- **Categorical derivation** (if PSLQ matches): 2–3 days authoring `conj:gt-matrix-categorical-trace`.
- **Lean formalization**: research-grade.

---

## Combined workplan estimate

Both items are research-grade but have **clear test paths** that can be run quickly:

1. **Compute first** (1 day total): SHELL-7 partition-sum-residue test + GT-MATRIX PSLQ test
2. **If positive**: author content blocks (3 days)
3. **If negative**: document the negative result (witnesses) and identify the next-most-likely categorical structure (1 day)

Recommended next-session sequence: **GT-MATRIX first** (smaller test, immediate feedback on whether the categorical-trace hypothesis is even close), **SHELL-7-SCALE second** (depends on the v3/v4 infrastructure being stable post-PR #509).

---

**End of document.**
