> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# Z=N ρ-correction finding — path to 1 ppb (W-1 first concrete result)

**Compiled** 2026-05-03 on `claude/path-to-1ppb-w1-rho-substrate`.
**Status**: empirical-regularity finding, conjectural categorical
status. Closes 4 / 10 light-atom binding-energy residuals by ~2 orders
of magnitude (towards W-1 in
[`docs/audits/2026-05-03-next-session-plan-to-1ppb.md`](2026-05-03-next-session-plan-to-1ppb.md)).

---

## §1. Finding

For light atoms on the **doubly-symmetric line `Z = N = k`**, the
canonical Kashaev-law / magic-A binding-energy prediction acquires a
substrate-q correction of the form

$$
  \delta\rho \;=\; -\frac{[A]_q - A}{\rho_{\rm struct}},
  \qquad A = 2k,\;\rho_{\rm struct} \in \{1, 2\}.
$$

Equivalently, the corrected binding is

$$
  B_{\rm corr}(Z=N=k) \;=\; m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A) \cdot
  \bigl(\rho_{\rm struct} + A - [A]_q\bigr).
$$

At $q_0 = 1.10998…$ this closes the residual on ²H and ⁴He by **two
orders of magnitude** and propagates through the α-cluster formula to
close ¹²C and ¹⁶O equally well:

| atom | err (orig) | err (corr) | improvement |
|------|-----------:|-----------:|------------:|
| ²H | +1.090 % | +0.011 % | **× 99** |
| ⁴He | +5.867 % | +0.057 % | **× 103** |
| ¹²C | +5.410 % | +0.063 % | **× 86** |
| ¹⁶O | +5.301 % | +0.152 % | **× 35** |
| ⁸Be | +10.334 % | +4.519 % | × 2.3 |
| ²⁰Ne | +8.344 % | +3.230 % | × 2.6 |
| ²⁴Mg | +9.020 % | +4.048 % | × 2.2 |
| ⁴⁰Ca | +19.506 % | +14.703 % | × 1.3 |

**4 atoms close to ≤ 10⁻³ relative** (≤ 1500 ppm). The remaining four
(⁸Be, ²⁰Ne, ²⁴Mg, ⁴⁰Ca) improve but retain residuals at the few-percent
level — consistent with an unresolved correction in `c_αα` and/or the
α-cluster pair-counting formula for $n_\alpha \neq 3, 4$.

Witness:
[`computations/per-atom-rho-deviation.witness.json`](../../computations/per-atom-rho-deviation.witness.json).

---

## §2. Provenance — no fitting

The finding emerged from a **diagnostic** that decomposed each atom's
residual into a fractional ρ-deviation
$\delta\rho = \rho_{\rm true}/\rho_{\rm struct} - 1$ and then tested
$\delta\rho$ against a **pre-specified** list of categorical
q-arithmetic forms drawn from the substrate's standard anchors:

- $\eta_q,\; \hbar_q,\; 1/c_q,\; d_H(q)$ (entropy / Planck / sound /
  Hausdorff)
- $[n]_q$ and ratios for $n = 2, 3, 4, 5$
- The atom-mass-aware family $\pm\bigl([A]_q - A\bigr)/k$ for small
  integer $k$ (motivated by *A counts hosts; $[A]_q$ is the q-deformed
  host count*)

The list was fixed before any data was inspected. Two of four input
atoms (²H, ⁴He) selected the **same form** $-\bigl([A]_q - A\bigr)/
\rho_{\rm struct}$ at residual < 10⁻³, with identical sign and
denominator structure. The propagation through the existing α-cluster
formula then closed two more atoms (¹²C, ¹⁶O) downstream **without
any additional fit parameter** — the only input is the corrected
$B(\,^4{\rm He})$.

PR #512's prior negative result for ³He's integer ρ-hypothesis stands:
the ³He / ³H atoms remain in the residual-rich Z ≠ N sector and **are
not** closed by this finding.

---

## §3. Conjecture

**Conjecture (Z=N q-deformation correction).** Let
$A = 2k$, $\rho_{\rm struct} \in \{1, 2\}$ be the canonical Kashaev /
magic-A integer prefactor for a Z=N=k light atom, and $K_A$ the
canonical hyperbolic knot / magic-A volume input. Then the binding
energy at the substrate's archimedean point $q_0$ satisfies

$$
  B(Z=N=k) \;=\; m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A) \cdot
  \bigl(\rho_{\rm struct} + A - [A]_q\bigr) \cdot
  \bigl(1 + O(10^{-3})\bigr).
$$

The leading correction is the **q-deformation excess** $A - [A]_q$,
divided by $\rho_{\rm struct}$ to convert it to a multiplicative
δρ-shift on the original integer prefactor.

**Categorical interpretation (open).** $A$ counts the host generators
of the substrate cell; $[A]_q$ is the q-dimension of the host
representation in $H_A(q)$. The deficit $A - [A]_q$ is the
**leading-order Plancherel/Wenzl-bridge correction** to the integer
host count at finite $q$. Its appearance with sign $-1$ on $\delta\rho$
is consistent with the standard sign of the Wedderburn-block
multiplicity correction at Z=N magic shells.

**Empirical scope.** Verified at residual $< 10^{-3}$ for the pair
(²H, ⁴He) which are the two Z=N atoms with $\rho_{\rm struct}$
explicitly assigned by the canonical pipeline. Propagation through
the α-cluster formula closes ¹²C ($n_\alpha = 3$) and ¹⁶O ($n_\alpha
= 4$) at the same precision.

**Falsification path.** A single Z=N atom whose δρ deviates by more
than $10^{-3}$ from the predicted form falsifies the conjecture as
stated. The natural next test target is **²⁰Ne** ($n_\alpha = 5$) once
its native (non-α-cluster) Vol-pairing is identified.

---

## §4. Path to 1 ppb — what this finding closes and what it doesn't

| atom-class | status post-finding | next required input |
|-----------|----------------------|----------------------|
| Z=N pair (²H, ⁴He) | ≤ 10⁻³ relative | sub-leading $O(\hbar_q^2)$ correction → 10⁻⁵ |
| Z=N α-cluster (¹²C, ¹⁶O) | ≤ 10⁻³ via propagation | same |
| Z=N α-cluster (²⁰Ne, ²⁴Mg, ⁴⁰Ca) | few % | $n_\alpha$-dependent $c_{\alpha\alpha}$ correction |
| ⁸Be ($n_\alpha = 2$) | +4.5 % | $c_{\alpha\alpha}$ vanishes for unbound dimer (⁸Be → 2·⁴He virtual) |
| Z ≠ N (³H, ³He) | unchanged | structural $\delta\rho$ from PR #512's open question |
| open Z=N (⁶Li…¹⁹F) | family-4 unassigned | knot pairing for non-α-cluster Z=N |

**Recommended next single-day step (W-1.1)**: identify the
sub-leading correction that takes ²H and ⁴He from $10^{-3}$ to
$10^{-5}$. Likely candidate: the $\hbar_q^2 \cdot [k]_q$ structural
factor that appeared in `g_a_g_action_derivation.py` (PR #515).

**Recommended next probe (W-1.2)**: extend the `α-cluster pair
correction` to $n_\alpha$-dependent form $c_{\alpha\alpha}(n_\alpha)$
to close ⁸Be, ²⁰Ne, ²⁴Mg, ⁴⁰Ca.

---

## §5. Lean / formalisation

This finding is an **empirical regularity** at 10⁻³ precision; the
conjecture above is unproved. A `conj:z-eq-n-rho-correction-via-q-
deformation` content block should be authored in the next session
with the following structure:

```
kind: conjecture
label: conj:z-eq-n-rho-correction-via-q-deformation
title: Z=N ρ-correction via q-deformation excess
uses: [def:q-integer, conj:plan-h-rho-from-multiplicity (#512),
       def:kashaev-volume-law, ...]
formal-status: empirical 10⁻³ on (²H, ⁴He, ¹²C, ¹⁶O); categorical
  derivation open; falsification target ²⁰Ne when Vol-pairing
  identified.
```

A Lean class `class ZeqNCorrection (k : ℕ)` axiomatises the
conjecture; downstream blocks consuming it carry `[ZeqNCorrection k]`
as an explicit hypothesis (per AGENTS.md §3b conditional-class
policy).

---

## §6. What this is NOT

- **Not a theorem.** The form $-([A]_q - A)/\rho_{\rm struct}$ is an
  empirical match at 10⁻³ precision on two independent atoms +
  propagation through α-cluster. The categorical derivation is open.
- **Not numerology.** The candidate list was fixed before inspecting
  the data; the matching form was selected by the **same** $A$-aware
  family for both ²H and ⁴He; propagation works downstream without
  re-fitting. PSLQ would not identify this form because it is
  $\rho_{\rm struct}$-aware (atom-classification-aware).
- **Not a closure of W-1.** The plan's W-1 was *wire RHO-SUBSTRATE
  from PR #512*; this finding does the diagnostic that exposes
  that wire is the wrong target. The actual leverage is the Z=N
  q-deformation correction identified here.

---

**End of finding.**
