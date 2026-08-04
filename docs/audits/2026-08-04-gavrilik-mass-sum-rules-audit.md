# TG audit: Gavrilik mass sum rules — fit vs derivation

**Date:** 2026-08-04
**Bean:** `qou-rjx4` (TG), epic `qou-8lxd`
**Branch:** `claude/eightfold-tg-t3f-2026-08-04`

## Bottom line

**VERDICT: FITTING, NOT DERIVATION.** Do not wire Gavrilik's mass
sum rules into the QOU framework. The q-deformation parameter is
scanned/fitted, not derived. The coincidence with the Cabibbo angle
is suggestive but not derived either.

## 1. Paper summary

Gavrilik (hep-ph/0103325, 2001) proposes replacing the classical
Gell-Mann–Okubo (GMO) mass sum rule with a q-deformed version using
$\mathrm{U}_q(\mathrm{su}_3)$. The q-deformed GMO formula replaces
integer quantum numbers with q-integers $[n]_q$, improving the residual
from ~0.58% to ~0.07%.

The deformation parameter $q$ is related to an angle $\theta$ by
$q = e^{i\theta}$ (or $q = e^\theta$ for real deformation).

## 2. Anti-fitting assessment

### 2a. The angle is SCANNED, not derived

The paper tests $\theta = \pi/m$ for $m \in \{\infty, 30, 12, 8, 7, 6\}$
and picks the best fit ($\theta = \pi/7$). This is a **6-point scan
with selection** — a fit with $k = 1$ free parameter and $n = 6$
candidates. The p-value for getting 0.07% from a 0.58% residual with
6 tries is not impressive.

### 2b. The baryon sector uses explicit fitting

Section 6 of the paper (baryon mass relations) states that $q$ is
"fixed by a fitting only" with $q = \pm 1.035$. This is an explicit
admission that the baryon-sector q is fitted, not derived.

### 2c. The Cabibbo angle connection is an observation, not a derivation

The paper notes that $\theta_C = \pi/14$ is close to the PDG Cabibbo
angle ($\theta_C \approx 13.04°$ vs $\pi/14 \approx 12.86°$), a 1.25%
discrepancy. This is:
- Not derived from any principle
- Not exact (1.25% is worse than many other numerological coincidences)
- Conflated with the scan selection (choosing $\theta = \pi/7$ for
  mesons and $\theta = \pi/14$ for the Cabibbo angle is two different
  uses of the same number family $\pi/n$)

## 3. What IS valuable from Gavrilik

### 3a. The [n]_q - [n-1]_q identity

The identity $[n]_q - [n-1]_q = \Delta_{T(2,2n-1)}(q)$ (symmetrized
Alexander polynomial of the $(2, 2n-1)$ torus knot) is **genuinely
proved** in the corpus (bean `qou-rftd`, T8,
`QIntegerAlexanderTorus.lean`). This is pure algebra — it does not
depend on Gavrilik's fitting of $\theta$.

### 3b. The cross-check structure

If QOU independently derives a $q$ value from the Bring surface (which
it does: $q_0$), then Gavrilik's **formulas** (not his fits) become
cross-checks:
- Evaluate Gavrilik's q-deformed GMO at $q = q_0$
- Compare residuals against PDG masses
- If the residuals improve, that's independent evidence
- If they don't, it's a falsification of the connection

This is the proper anti-fitting workflow: derive $q_0$ from geometry,
then test Gavrilik's formulas at that specific $q_0$, and compare.

## 4. Recommendations

1. **Do NOT wire** Gavrilik's fitted $q$ values ($\theta = \pi/7$,
   $q = \pm 1.035$) into the corpus. They are fits.
2. **DO test** Gavrilik's mass sum rule formulas at $q = q_0$ (QOU's
   independently derived parameter) as a **cross-check computation**.
   This is a clean anti-fitting test:
   - If the q-deformed GMO at $q_0$ improves the residual over
     classical GMO → evidence for the framework
   - If it doesn't → honest negative result
3. **The Cabibbo angle** connection should be listed as an "observed
   coincidence" in the open-problems ledger, not as a derived result.
   QOU has its own CKM-related content in `sm-params-ckm.md` which
   should not be contaminated by fitted values.
4. **The [n]_q - [n-1]_q identity** is safe to cite as a mathematical
   theorem (it's proved in Lean). Gavrilik's observation that this
   connects q-integers to torus knot polynomials is historically
   valuable attribution.
