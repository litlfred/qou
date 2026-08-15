# g₂ derivation attempt — cosh/crossing-count, BCH/Bernoulli, and the parity puzzle

**Date:** 2026-07-25 · **Branch:** `claude/binding-mass-derivation-gaps-0f61i6` · **Axis:** Δ_λ binding
magnitude — the `E_unit` −9.2% closure, follow-up to
[`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md) · **Object:** the bar-even
gap coefficient $g_2 = (\text{gap on } E^{+})/h^2 = 1.00865$, $h = q - q^{-1}$ — NEAR-MATCH,
underived (committed `eunit-magnus-order2` witness) · **Tier:** exact structural probes, scope-(a)
where numeric, class-(b) only where an invariant is cited; **no fit, nothing wired, no AME
inversion**. This is a separate doc (not an in-place edit of the committed 2026-07-24 audit) so the
committed report stays a clean record of the Magnus-route result; that doc gains only a one-line
follow-up pointer.

Probe: [`eunit_g2_derivation_probe.py`](../../computations/probes/eunit_g2_derivation_probe.py),
witness `eunit-g2-derivation.witness.json` — 18/18 assertions, sympy exact + mpmath 50 dps, both
q₀ pins (shift $< 10^{-6}$).

## 1. Mechanism 1 — cosh/crossing-count (exact; verdict: predicts C ≠ 1.0087)

The counit character on a crossing splits exactly as $\varepsilon(\sigma) = q = \cosh\theta +
\sinh\theta$, $\theta = \ln q$: bar-even part $\cosh\theta$, bar-odd part $\sinh\theta = h/2$.
The $h/2$ — not $h$ — is forced by the corpus normalization $\mu_0 = m_e/(3h/2)$
([#4102/#4117](2026-07-19-eunit-source-is-the-counit.md): 3 crossings × $h/2$ per crossing). So the
**per-crossing bar-even coefficient at order 2 is $\tfrac12\theta^2 \approx h^2/8$ — i.e. $1/8$,
not the naive $\tfrac12 h^2$** (which would require per-crossing weight $h$). The deuteron word
$\sigma_1^3$ is single-generator, so the holonomy is *coherent* ($\exp(3a)$, no ordering effects):
the candidate ladder, all pre-registered shapes, none tuned (probe M1a–M1e, leading coefficients
proved by sympy limits, exact values at q₀ mpmath):

| candidate (structure) | leading coeff | exact $C$ at $q_0$ | $\lvert C - g_2\rvert$ |
|---|---|---|---|
| per-crossing $\cosh\theta$ | $1/8$ | 0.12466 | 0.884 |
| incoherent product $(\cosh\theta)^3$ | $3/8$ | 0.37602 | 0.633 |
| **coherent $\cosh 3\theta$** (the counit's actual bar-even part on $\sigma_1^3$) | $9/8$ | **1.13011** | **0.12146** |
| naive weight-$h$ incoherent $\cosh(h)^3$ | $3/2$ | 1.53873 | 0.530 |
| naive weight-$h$ coherent $\cosh(3h)$ | $9/2$ | 4.64946 | 3.641 |

**Answer to the "3/2, 1, ½, or something else?" question: something else — the counit functional
actually produces $9/8$ (leading) / $1.1301$ (exact) on $\sigma_1^3$**, because the per-crossing
even coefficient is $1/8$ (counit weight $h/2$) and the single-generator word adds coherently
($n^2/8$ at $n$ crossings — no integer $n$ gives 1).

**Verdict (scope-(a)):** no candidate is within $h^2$-order of $g_2 = 1.00865$ — the closest,
coherent $\cosh 3\theta$, overshoots by $0.1215 = 2.78\,h^2$ ($E^{+}\cosh 3\theta$ would leave a
$+0.53\%$ residual on $B_D$ vs the near-match's $-0.036\%$). Mechanism 1, *alone and as-is*, does
not derive $g_2$. Recorded observation (not a match): the overshoot is $0.581\,h$ — inside a
*loose* $O(h)$ budget, so a coherent-cosh completion with one $O(h)$-suppressed structural
correction is not excluded; no such correction is derived here, so it stays unclaimed.
Two structural by-products (proved): (i) $2(\cosh 2\theta - 1) = h^2$ exactly — "$g_2 = 1$" is
the *2-coherent* cosh shape at weight 2, an exact restatement recorded as shape observation only;
(ii) the 2-dim Hecke-rep **trace** of $\sigma_1^3$ is $q^3 - q^{-3} = 2\sinh 3\theta$, purely
bar-ODD — the bar-even cosh channel is a character/eigenvalue-functional effect, invisible to the
plain rep trace (probe M1g).

## 2. Mechanism 2 — BCH/Bernoulli (exact statement + citation; verdict: predicts C = 0)

From `library/phys-rep09/phys-rep09.pdf` (Blanes–Casas–Oteo–Ros, *The Magnus expansion and some of its
applications*, Phys. Rep. **470** (2009) 151–238), read directly, not paraphrased from memory:

- **Theorem 1 (Magnus 1954), eq. (32):** $\dfrac{d\Omega}{dt} = \sum_{n\ge0} \dfrac{B_n}{n!}\,
  \mathrm{ad}_\Omega^n A$ with **Bernoulli** weights $B_0 = 1$, $B_1 = -\tfrac12$, $B_2 = \tfrac16$,
  $B_4 = -\tfrac{1}{30}$, $B_{2m+1} = 0$ ($m \ge 1$) (§1.4; generating function $x/(e^x-1)$
  verified symbolically in the probe, convention-independent).
- **Explicit terms:** $\Omega_2 = \tfrac12\int\!\!\int [A_1, A_2]$ (eq. 43, weight $\tfrac12$ from
  $B_1 = -\tfrac12$); $\Omega_3 = \tfrac16\int\!\!\int\!\!\int\{[A_1,[A_2,A_3]] + [[A_1,A_2],A_3]\}$
  (eq. 45); $\Omega_4$ prefactor $\tfrac1{12}$. **Every order-$k\ge2$ term is a Lie element** —
  the Bernoulli tower attaches its weights to *commutators only*; there is **no scalar quadratic
  term at any order $\ge 2$**.
- **Surface-ordered NA-Stokes version** (`library/arxiv-math-ph-0012035v3/0012035v3.pdf`, Broda, math-ph/0012035v3, §2.1
  operator approach): $P\exp\bigl(i\oint_{\partial S} A_i\,dx^i\bigr) = \mathcal P\exp\bigl(
  \tfrac{i}{2}\int_S \mathcal F_{ij}\,dx^i\wedge dx^j\bigr)$ with the twisted curvature
  $\mathcal F = U^{-1} F U$. The bar-even quadratic term of the surface-ordered exponential carries
  the **plain Dyson $1/2!$ weight** on $\bigl[\tfrac{i}{2}\int_S \mathcal F\bigr]^2$ under the
  surface ordering $\mathcal P$ (§2.1.2 "Ordering", Dyson series) — no Bernoulli dressing at this
  order beyond the $\tfrac{i}{2}$ per curvature insertion. Evaluating it requires the
  Seifert-surface discretization the corpus lacks (the wall already named in the 2026-07-24 audit
  — unchanged).

**Verdict (class-(b) for the braid-word connection; invariants: Lie-element structure of every
$\Omega_{k\ge2}$ + $[X,X] = 0$):** for the single-generator deuteron word $\sigma_1^3$ the entire
Bernoulli tower vanishes (re-verified numerically to 50 dps), and for *any* word its terms are
killed linearly by trace/counit functionals. The BCH/Bernoulli mechanism assigns the bar-even
quadratic gap coefficient **exactly 0** — it cannot produce $g_2 = 1.0087$. The −9.2%'s bar-even
piece must come from *outside* the inter-crossing commutator tower (per-crossing structure, or the
surface pairing behind the wall).

## 3. The parity puzzle (exact enumeration; verdict: the residual is NOT a next-order unit)

Residual $r = g_2 - 1 = 0.0086520$ (env pin; muon pin 0.0086516, shift $< 10^{-6}$). Ladder units
are Laurent monomials $m(a,b) = (v-v^{-1})^a\,[2]_v^b$, $v = \sqrt q$; bar-parity = parity of $a$
($\theta$-powers are not ring units and are excluded by construction). Sweep $a \in [0,6]$,
$b \in [-6,6]$; everything within 30% of $r$:

| unit | value at $q_0$ | vs $r$ | bar-parity |
|---|---|---|---|
| $h^3 = (v-v^{-1})^3[2]_v^3$ | 0.0091372 | **+5.6%** | **ODD — parity-blocked** |
| $h^4[2]_v^2 = (v-v^{-1})^4[2]_v^6$ | 0.0076617 | −11.4% | even |
| $(v-v^{-1})[2]_v^{-4}$ | 0.0064889 | −25.0% | ODD |
| $x = (v-v^{-1})^2$ | 0.0108969 | +26.0% | even |

(For scale: $h^4 = 0.0019102$ is $0.22\,r$ — too small, as the task noted.)

**Findings (asserted in the probe):** the closest unit of *any* parity is $h^3$ (+5.6%) — but it
is bar-ODD, and gap$/h^2$ is bar-even, so it cannot appear with a real coefficient unless the
frame itself is parity-impure; **no bar-even monomial lies within 10% of $r$** (closest:
$h^4[2]_v^2$ at −11.4%). **Structural finding, recorded as it fell: the residual $r$ is not a
next-order bar-even ladder unit.** It therefore lives in the $E^{+}$ *frame definition* (the
parity-projection prescription — the one structural assumption the 2026-07-24 audit flagged) or in
the *crossing-count arithmetic* (the $n = 3A$, $j = n/2$ frame), not in the $(v-v^{-1}), [2]_v$
unit ladder. This narrows where a $g_2$ derivation must look: not "one more unit," but the frame.

## 4. Literature — q-deformed rotor nuclear spectroscopy lineage (index-verified, abstracts only)

Verified via web search-result metadata (no bulk downloads; the arXiv-fetch 403 constraint stands;
no dedicated paper-search MCP was available in this session):

- **P. P. Raychev, R. P. Roussev, Yu. F. Smirnov**, *The quantum algebra SU$_q$(2) and rotational
  spectra of deformed nuclei*, **J. Phys. G: Nucl. Part. Phys. 16 (1990) L137–L141** — the q-rotor
  $E_J \propto [J][J+1]_q$ (second-order SU$_q$(2) Casimir); VERIFIED (venue + pages from index
  metadata). The companion **D. Bonatsos et al.**, *SU$_q$(2) description of rotational spectra and
  its relation to the variable moment of inertia model*, **Phys. Lett. B 251 (1990) 477** —
  title/venue verified from index (ScienceDirect PII 0370269390907822); author list beyond
  Bonatsos–Raychev–Roussev–Smirnov to-verify.
- **D. Bonatsos, C. Daskaloyannis**, *Quantum groups and their applications in nuclear physics*,
  **Prog. Part. Nucl. Phys. 43 (1999) 537–618**, arXiv:nucl-th/9909003 — VERIFIED (abstract +
  index metadata; covers the SU$_q$(2) rotator model and its extensions).

**Comparison caveat (mandatory):** in that lineage the deformation $q$ is typically a **phase**
($q = e^{i\tau}$, unit circle) fitted per band to deformed-nucleus spectra, whereas QOU's $q_0
\approx 1.10998$ is **real**, substrate-pinned, and not fitted per nucleus. The lineage is cited
as precedent for $[J][J+1]_q$-form rotational spectra, not as an equivalence.

## 5. Verdict (honest — the constraint table IS the deliverable)

| mechanism | predicted $C$ (exact) | $g_2$ measured | verdict |
|---|---|---|---|
| 1 · cosh/crossing-count, coherent $\cosh3\theta$ | 1.13011 ($9/8$ leading) | 1.00865 | **scope-(a): alone, as-is, does not derive $g_2$** (off $2.78\,h^2$; within loose $O(h)$ — unclaimed) |
| 1 · incoherent / naive variants | 0.125 / 0.376 / 1.539 / 4.649 | 1.00865 | scope-(a): excluded at $h^2$ tier |
| 2 · BCH/Bernoulli inter-crossing tower | **0 exactly** | 1.00865 | class-(b): Lie-element invariant + $[X,X]=0$ — cannot produce $g_2$ |
| 2 · surface-ordered quadratic (Broda) | Dyson $1/2!$ weight; value needs surface data | — | wall (unchanged) |
| 3 · next-order unit for $r = g_2-1$ | no bar-even unit within 10% | — | **structural: residual lives in the $E^{+}$ frame / crossing-count, not the unit ladder** |

No mechanism predicts 1.0087. $g_2$ **remains NEAR-MATCH tier, underived**; the derivation search
is now constrained to (i) a per-crossing/coherent structure with an $O(h)$ correction (mech-1's
0.12 overshoot), (ii) the surface-curvature pairing behind the Seifert wall, or (iii) the $E^{+}$
frame definition itself (parity-projection prescription / crossing-count arithmetic — where the
parity puzzle says the residual lives). Nothing closes; nothing wired; no fit performed.

## Files

- Probe: [`computations/probes/eunit_g2_derivation_probe.py`](../../computations/probes/eunit_g2_derivation_probe.py)
- Witness: [`computations/probes/eunit-g2-derivation.witness.json`](../../computations/probes/eunit-g2-derivation.witness.json) (audit-only, 18/18 assertions)
- Parent audit: [`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md) (one-line follow-up pointer added there)
- Refs: `library/phys-rep09/phys-rep09.pdf` (Phys. Rep. 470 (2009) 151, Thm 1 eq (32), eqs (43)/(45), §1.4);
  `library/arxiv-math-ph-0012035v3/0012035v3.pdf` (Broda, operator NA-Stokes + §2.1.2 Ordering); §4 citations above.
