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
| the deformation term $(q_0-1)^2/q_0$ | **structure DERIVED (§2b, this branch); one physical identification remains** | the #3407 audit doc's "three routes converge uniquely" claim was *not* backed by computation — its probe [`categorical_linking_reeb_flow_probe.py`](../../computations/probes/categorical_linking_reeb_flow_probe.py) restates the formula in one line (*"Or simply g = 1 / sqrt( 5 + (q-1)^2 / q )"*), and no Route A/B/C artifact exists. §2b now supplies the actual structure: three exact identities reduce the formula to derived constants, leaving **one** named physical identification. Probe: [`reeb_g_structural_identity_probe.py`](../../computations/probes/reeb_g_structural_identity_probe.py) (4/4 assertions). |
| the **linear law** $B = 5g$ | **ASSERTED** | code comment "Binding is strictly 5*g" only; not in the #3407 doc; dimensionally implicit ($5g$ is dimensionless, used as MeV); not the $A{=}2$ case of the pinned $b_4 = -\ln\det(I+G)$ form (§3, Q1) |
| the pn **sign** | **still open** | #3407 landed magnitude only; the sign enters squared at $A{=}2$ and is unresolved for [1⁴] |

*(Correction, same day: an earlier revision of this table said the deformation
term "appears nowhere else in the corpus" — a too-narrow grep pattern missed
the LaTeX `\frac` form in the #3407 audit doc. The corrected finding is
sharper, not weaker: a claimed derivation exists but its supporting probe is a
restatement.)*

## 2b. Derivation of the formula's structure (this branch)

With $v = \sqrt{q}$, $[2]_v = v + v^{-1}$ (balanced quantum integer), and
$z = 1/[2]_v$ the **derived** Markov-peel bond factor, three exact identities
(verified to 50 dps, [`reeb_g_structural_identity_probe.py`](../../computations/probes/reeb_g_structural_identity_probe.py), 4/4 assertions):

- **I1 (polynomial, ring-provable).**
  $5 + (v-v^{-1})^2 = 1 + (v+v^{-1})^2$ — it is $(a+b)^2-(a-b)^2 = 4ab$ with
  $ab = 1$; both sides equal $(v^4+3v^2+1)/v^2$. So the "mystery" deformation
  term is nothing but the ceiling identity rewritten.
- **I2 (deformed criticality).** The classical [1⁴] ceiling $\sqrt5$ is the
  ss-sector eigenvalue of $\begin{pmatrix}1&2\\2&-1\end{pmatrix}$
  ($\sqrt{1^2+2^2}$: pp−nn asymmetry 1, pn-degree 2). Quantum-deforming the
  integer pn-degree $2 \to [2]_v$ gives
  $\begin{pmatrix}1&[2]_v\\ [2]_v&-1\end{pmatrix}$ with eigenvalues
  $\pm\sqrt{1+[2]_v^2}$, and **$g = 1/\sqrt{1+[2]_v^2}$ exactly** — the landed
  magnitude sits **at criticality of the q-deformed ss-sector exchange**, not
  merely "below the classical ceiling". The classical-$S$ headroom is the
  substrate deformation: $1-\sqrt5\,g \approx (v-v^{-1})^2/10$
  ($1.088\times10^{-3}$ vs $1.090\times10^{-3}$).
- **I3 (projection).** $g = z/\sqrt{1+z^2} = \sin(\arctan z)$: $z$ is the
  *tangent* of the linking inclination (crossing density per unit base
  parameter), $g$ its *sine* (per unit arc length) — unit-vector
  normalization, which automatically enforces $g < 1$ and $g <$ ceiling.
  Consequently the $A{=}2$ det factor is $1-g^2 = \cos^2\theta$.

**What remains assumed** (the honest residue): the single physical
identification *magnitude = arc-length-normalized transverse component* (I3)
$\equiv$ *deformed-criticality value* (I2). One assumption replaces the three
unsubstantiated #3407 "routes". A Lean lemma for I1 (pure `ring`) + I2
(2×2 eigenvalue) is queued.

**Scope note.** Nothing here refutes the landed value — the derivation above
*supports* its structure. What still cannot be claimed as derived: the choice
of the sine normalization itself (narrowed in §2c below), and the linear
$B = 5g$ law (§3, §3d).

## 2c. The sine normalization from the CWF unit-tangent structure (tranche 2)

The residual identification of §2b — *why sine rather than tangent* — reduces
to the structure of the Gauss/Călugăreanu–White–Fuller linking integrand
itself, which is the #3407 doc's (unsubstantiated) "Route C" made concrete:

1. The CWF decomposition $Lk = Wr + Tw$ writes linking through the **Gauss
   integral**, whose integrand is built from **unit tangent vectors**
   integrated **per unit arc length**:
   $Wr = \frac{1}{4\pi}\oint\oint \frac{(T(s)\times T(s'))\cdot(r-r')}{|r-r'|^3}\,ds\,ds'$.
   The arc-length/unit-tangent normalization is *forced by the definition of
   linking*, not chosen.
2. A pn strand whose categorical crossing density is $z$ **per unit Reeb
   parameter** (the Markov-peel factor: one inter-block crossing per unit
   base time) has tangent vector $\xi + z\,e_\perp$ in Reeb-adapted
   coordinates, hence **unit** tangent transverse component
   $z/\sqrt{1+z^2} = \sin\theta$.
3. Therefore any linking-derived magnitude — anything of CWF/Gauss type —
   sees the strand at amplitude $\sin\theta$, not $\tan\theta = z$. The
   "naive $z$ overbinds by ~12 %" of #3426 is exactly the tangent/sine
   discrepancy at $z \approx 0.499$.

**What this upgrades:** the sine normalization is now *derived from the CWF
integrand's unit-tangent structure*, conditional on **one geometric
identification**: *the categorical bond factor $z$ is the per-unit-Reeb-time
crossing density (the tangent) of the bond's inclination*. That
identification is natural (it is what the Markov-peel factor counts) but is
the honest remaining assumption. The three vague #3407 "routes" have
collapsed to this single named premise.

## 2d. The tangent identification from the Markov property (tranche 3)

The §2c residue — *why is the bond factor $z$ a tangent?* — reduces to the
Temperley–Lieb **Markov property**, which is a theorem, not a choice:

1. The bond factor is $z = 1/[2]_v = \delta^{-1}$, and $\delta^{-1}$ is
   exactly the **Markov conditional-expectation weight** of the TL exchange
   generator: $\mathrm{tr}(x\,e_n) = \delta^{-1}\,\mathrm{tr}(x)$ — the
   defining Markov property of the trace tower.
2. One inter-block crossing decomposes into the two TL channels, *direct*
   ($1$) and *exchange* ($e$). Under the Markov trace the channel amplitudes
   are $(1, \delta^{-1}) = (1, z)$: the bond strand's direction **in channel
   space** is the vector $(1, z)$.
3. The inclination of that direction is $\tan\theta = z$ **by definition of
   channel-space angle** — the tangent identification is the Markov weight,
   derived, not postulated.

Composing §2c + §2d: sine normalization from the CWF unit-tangent integrand,
tangent from the Markov property. The full derivation chain for
$g = z/\sqrt{1+z^2}$ now has **one residual postulate**, stated precisely:
*the Reeb linking amplitude of the pn bond is the CWF (unit-tangent,
arc-length) functional evaluated on the channel-space direction $(1, z)$* —
i.e. physical linking reads the TL channel decomposition through the Gauss
integrand. Everything downstream of that sentence is proved
(§2b I1–I3 + [`ReebPnMagnitude.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ReebPnMagnitude.lean)).

## 2e. Proof program for the ²H law — what is provable, proved, and forbidden (tranche 3b)

Owner asked for a proof of the ²H tier (option 1). Honest decomposition:

**Strong form is unprovable.** $5g = 2.23364$ vs AME $2.2245660$: the law
carries an irreducible **+0.41 %** residual, so no derivation can make
$B = 5g\,E_{\text{unit}}$ exact. The provable target is the leading-order
statement plus a correction ladder:
$B(^2\mathrm{H}) = \sqrt5\,E_{\text{unit}}\,(1 - x/10 + 3x^2/200 - \cdots)$,
$x = (v-v^{-1})^2$ — the same base-value-times-deformation-ladder shape as
the $Q_\beta$ $c_k$ series, with base $\sqrt5\,E_{\text{unit}}$.

**Proved now (Lean, sorry-free).** The dimensionless core is the
**marginal-stability characterization**: over any commutative ring
$\det(1 + g\,M(b)) = 1 - g^2(1+b^2)$ (`ss_det_marginal`), hence the landed
magnitude — which satisfies $g^2(1+[2]_v^2) = 1$ by I1/I2 — is exactly the
point where the deformed ss-sector determinant **vanishes**
(`ss_det_zero_at_criticality`). The deuteron's exchange sector sits at
marginal stability, matching its physical signature (barely bound, no bound
excited state), and AME lies on the bound side ($B_{\text{AME}} < 5g$,
correct sign). Both criticality candidates $5g$ and $1/g = \lvert\mu_q\rvert$
straddle within $g\,x \approx 0.0049$ MeV of each other; AME is below both.

**Forbidden step (entropy bound).** $E_{\text{unit}} = 0.99594$ MeV must
come from a structural argument, **not** a wider scan: at the law's own
0.4 % match precision, a two-factor scan over ~10 canonical energies × ~10
dimensionless dressings expects $\gtrsim 1$ accidental hit — a match found
that way carries no evidence (the PSLQ entropy-bound precedent, PR #1805).
The §3d single-factor scan stands as the only admissible search; the unit
identification remains the genuine open of this law.

## 2f. E_unit constraint ledger (tranche 4 — predicted-first gate)

For future attempts at the ²H unit anchor (the one genuine open of §2e).
Targets, exact to the digits shown ($E_{\text{unit}} = B_{\text{AME}}/5g$):

| ratio | value |
|---|--:|
| $E_{\text{unit}}$ | 0.995940 MeV |
| $E_{\text{unit}}/m_e$ | 1.949005 |
| $E_{\text{unit}}/2m_e$ | 0.974503 |
| $E_{\text{unit}}/(m_e [2]_v)$ | 0.973178 |
| $E_{\text{unit}}/E_0$ | 0.237921 |

**Gate (STRICT):** any candidate must be stated *with its derivation*
BEFORE numerical evaluation (predicted-first); a candidate matching to
$\sim$0.4 % carries no evidence by itself (§2e entropy bound) and must
additionally account for the +0.41 % AME residual's structure. Per the
Anti-Laundering rule (`compute-author.md` / `formalizer.md`, 2026-07-06):
no conditional class or axiom carrying $E_{\text{unit}}$ counts as a proof
or unblocks production wiring. The §3d single-factor class (m_e × bond-
algebra q-integers) is exhausted-negative; a successful bridge therefore
needs either a genuinely new derived energy (e.g. counit/transition-sector)
or the conclusion that the linear law is not fundamental.

**Excluded sources (corpus record):**

| source | disposition |
|---|---|
| m_e × bond-algebra q-integers (single factor) | §3d exhausted-negative |
| **counit / transition sector** (the specific defect functional $\varepsilon(\beta_K)-\varepsilon(\beta_K^{\mathrm{vac}})$, as defined) | **scope-(a) negative** — [`rho_k_counit_defect_form.py`](../../computations/rho_k_counit_defect_form.py) (bean `p7l6`): this functional supplies the binding *sign* robustly but its *magnitude explodes with $A$* (deuteron defect $\approx -30.3$ vs target $-4.35$; ratio $7\to515$ across the light series). A per-pair $E_{\text{unit}}$ is $A$-independent, so this $A$-exploding functional cannot supply it. **This is a scope-(a) negative on the specific counit-defect functional as normalized, NOT a structural exclusion of the counit sector under all normalizations** — a different counit normalization (e.g. an $A$-flattened / per-interface variant) is not ruled out by this result, only the one tested. The functional's durable contribution is the sign, not the scale. |

So the counit-defect functional *as normalized* is a scope-(a) negative
for the magnitude — an $A$-flattened counit variant remains a possible
route, as does the exchange sector's own $m_e$-scale bridge (still open),
or the conclusion that the linear law is not fundamental. The two-sector
split (§2g) sharpens which sector the scale must come from.

## 2g. Two-sector split of the pn-pair binding — trace binding is decoherence (tranche 5)

The deuteron $b_2 = 2.2246$ sits *between* the exchange-sector marginal
value ($-E_0\ln(1-g^2) \approx 0.93$) and the trace-sector suppression
($\alpha\ln(\mathrm{tr}_{\text{free}}/\mathrm{tr}_{\text{atom}}) \approx 3.9$).
Which sector does it live in? [`pn_pair_two_sector_split.py`](../../computations/probes/pn_pair_two_sector_split.py)
splits the trace suppression into its two physically distinct parts using
the Frobenius/Markov $\sharp$-Gram machinery (reusing `gram_norm_binding_probe`),
for the atom word (with pn crossing) vs the free word:

- $B_{\text{scalar}} = \alpha\ln(T_{\text{free}}/T_{\text{atom}})$ — total
  collapse of the **scalar (identity) channel** (what Term 1 counts);
- $B_{\text{norm}} = \tfrac{\alpha}{2}\ln(G_{\text{free}}/G_{\text{atom}})$ —
  **genuine loss of total $\sharp$-length** (all channels);
- $B_{\text{redist}} = B_{\text{scalar}} - B_{\text{norm}}$ — **decoherence**:
  scalar amplitude that moved off-diagonal without leaving the total norm.

| iso | $B_{\text{scalar}}$ | $B_{\text{norm}}$ | $B_{\text{redist}}$ | $B_{\text{exch}}$ | AME |
|---|--:|--:|--:|--:|--:|
| ²H | 3.890 | **−0.023** | 3.913 | 0.932 | 2.2246 |
| ³H | 9.068 | +0.108 | 8.960 | 0.932 | 8.482 |
| ³He | 6.797 | −0.231 | 7.028 | 0.932 | 7.718 |

**Finding (measured, not asserted; scope-(a)).** The **genuine
Frobenius-norm loss is $\approx 0$** for every isotope
($|B_{\text{norm}}| \le 0.23$ MeV, sign-flipping under the p↔n mirror) —
the word's total $\sharp$-length is *conserved* under binding. Therefore
the trace sector's apparent 3.9 MeV binding is **$\approx$ entirely
decoherence** (norm-conserving redistribution of scalar amplitude into
off-diagonal channels), **not** genuine size reduction. This is the
measured form of the §2e/§3c claim that Term 1 over-counts by booking
trace decoherence as energy — now quantified: the over-count is the whole
of it. Consequently $b_2 = 2.2246$ lives in **neither** pure sector — not
in the $\approx 0$ norm-loss sector, not in the 3.9 MeV scalar-collapse
sector — but at the exchange-sector **linear** value $5g = 2.234$
(the reeb-flow tier). The split independently corroborates the tier
choice: binding is an exchange-sector object, and the trace suppression
that a naive Term-1 form would bind on is a decoherence artifact.

## 2h. Crossing the E_unit bridge — the open-bond dichotomy (proved) and the scale-free wall (tranche 6)

Attempt to *derive* the linear law's unit $E_{\text{unit}}$ (§2f open). Two
halves — a genuine advance and an honest limit.

### 2h.1 Positive: why the linear form is the physically correct one (Lean-proved)

The two candidate exchange-sector forms — the **closed-loop determinant**
$-E_0\ln(1-g^2) \approx 0.93$ and the **linear** $5g \approx 2.23$ — differ
by $g$-order, and the deuteron picks the linear one for a structural reason
now formalized. For a $2\times2$ matrix
$\det(1+g\,M) = 1 + g\,\mathrm{tr}\,M + g^2\det M$; the ss-sector $M(b)$ is
**traceless** (`ssMatrix_trace_zero`), so the **linear-in-$g$ term vanishes**
and the loop binding is $O(g^2)$: $\det(1+g\,M) = 1 + g^2\det M$
(`ss_det_no_linear_term`, sorry-free). A single *open* pn bond contributes at
**first order** in the crossing amplitude $g$; the trace-free closed loop has
no first-order term. **The deuteron is one open pn bond, so its binding is
the $O(g)$ linear object ($5g$), not the $O(g^2)$ loop determinant** — which
is precisely why the linear form ($2.23$, matches AME) beats the loop form
($0.93$, under-binds). This upgrades the linear law from *asserted* (§2-table)
to *physically motivated*: it is the open-bond first-order amplitude, and the
loop form's under-binding is explained (traceless $\Rightarrow$ no linear
term). The $g$-**order** of the law is thereby derived.

### 2h.2 Honest limit: the exchange sector is scale-free — the unit is external

What remains is the **MeV unit** of that linear object, and it does not come
from within the exchange sector. The exchange amplitude $g$ and the ceiling
eigenvalue $\sqrt5$ (hence $5g \approx 2.23$) are **dimensionless** — matrix
data of the Hecke exchange operator, which carries no energy scale (the mass
scale $m_e$ enters the QOU chain only through the $\tau$-functor archimedean
evaluation, downstream of and orthogonal to the exchange algebra). So
$B = 5g\cdot E_{\text{unit}}$ *requires* an external $E_{\text{unit}}$, and
no canonical QOU energy supplies the needed $0.99594$ MeV to the law's own
precision:

| candidate | value | miss vs $E_{\text{unit}}$ |
|---|--:|--:|
| $2m_e$ | 1.02200 | +2.62 % |
| $m_e[2]_v$ | 1.02339 | +2.76 % |
| $E_0/[2]_v^2$ | 1.04365 | +4.79 % |
| $Q_\beta$ | 0.78233 | −21.45 % |

The nearest structural candidate ($2m_e$) misses by **+2.6 %** — six times
the law's own +0.41 % residual. (The apparent "+0.41 %" of a bare "1 MeV" is
not a candidate: 1 MeV is a human unit, not a QOU-derived scale.)

**Conclusion (scope-(a)).** The bridge, *as a derivation of $E_{\text{unit}}$
from within the exchange sector*, cannot be crossed to AME precision: the
$g$-order is derived, the numerical coefficient $\sqrt5$ is derived, but the
energy unit is scale-free and no internal QOU scale matches to better than
~2.6 %. The linear law is therefore a **physically-motivated near-match with
an external unit**, not a closed derivation — the §3f NEAR-MATCH label is
correct and now has a structural cause. This is *not* a global impossibility
(not a scope-(b)): the two open routes are (i) an external ~1 MeV scale the
framework does not canonically contain, or (ii) the $A$-flattened counit
variant left open in §2f. Both remain genuinely open; the exchange sector
alone is exhausted for the unit.

## 2i. Does the dichotomy decompose the many-body shell? — no; binding is collective (tranche 7)

The §2h dichotomy is a *single-bond* result (open ⇒ linear, loop ⇒
quadratic). The natural next question: does it **additively decompose** the
many-body binding — a sum of per-bond open (linear) + loop (quadratic)
contributions? [`light_series_open_loop_decomposition.py`](../../computations/probes/light_series_open_loop_decomposition.py)
tests it structurally: model each isotope as the complete graph on its
nucleons, take a pn-preferring spanning tree (open bonds, linear $5g$) plus
the cycle-closing loop edges (determinant, quadratic), fix the single unit
$E_{\text{unit}}$ on ²H, and *predict* ³H/³He/⁴He (one calibration point, no
tuning of tree/signs/magnitude).

| iso | additive open+loop | err | collective full-det | full-det / AME |
|---|--:|--:|--:|--:|
| ²H | 2.225 (cal.) | 0 % | 0.932 | 0.419 |
| ³H | 5.381 | −36.6 % | 6.281 | 0.741 |
| ³He | 5.381 | −30.3 % | 2.283 | 0.296 |
| ⁴He | 10.100 | −64.3 % | 26.596 | 0.940 |

**Finding (measured; scope-(a)).** The additive open/loop split
**under-predicts badly for $A>2$** (⁴He −64 %) — *worse* than the collective
full determinant (all edges as loops), which reaches **0.94× on ⁴He**. So
**many-body binding is collective** (the determinant's cross terms carry the
bulk), **not a sum of per-bond open + loop contributions**: the proved
dichotomy governs the *single-bond* g-order (²H) and does **not** additively
decompose the many-body shell. This closes the "extend the dichotomy
additively to A≥3" route.

**But the collective determinant is not a predictor either** — it is
*non-monotone* (³H 0.74×, ³He 0.30×): the A=3 mirror pair splits widely
(the p↔n asymmetry, $Z>N$ for ³He). So the honest state of the ⁴He /
GAP-A-4 magnitude leg: the **collective determinant is the right direction**
(all cross terms, 0.94× on ⁴He) but carries two open residuals — the ⁴He ~6 %
and the ³He mirror gap — neither of which the additive dichotomy repairs.
The reeb-flow tier's success is a *single-pair* (²H) phenomenon; the
many-body extension is a genuinely separate, still-open collective problem.

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

| $w_{pn}$ | $\det(I+G)$ | $E_0\cdot(-\ln\det)$ | vs $b_4=9.2431$ | vs full $B(^4\mathrm{He})=28.296$ |
|--:|--:|--:|--:|--:|
| ±1 | 0.0017407 | 26.596 MeV | 2.877× | **0.940×** |
| 0 | 0.64070 | 1.864 MeV | 0.202× | 0.066× |

($w_{pn}=+1$ and $-1$ are isospectral — conjugation by
$\mathrm{diag}(1,1,-1,-1)$ — asserted in the witness.)

**Reading (scope-(a) throughout).** At the landed magnitude the mixed-sign
[1⁴] determinant lands at **0.940× of the full ⁴He binding** (−6.0 %) — not at
the connected-excess convention $b_4 = 9.2431$ (2.877×). If the determinant form
is meant to produce the *connected excess*, the landed magnitude overshoots by
~2.9×; if it is meant to produce the *full* binding, it is 6 % low. Neither
match is claimed; the numbers constrain the (form, magnitude, convention)
combination, not the ingredients.

**Q3 — Ursell (body-order) cumulants of the det form at $g_{\text{reeb}}$.**
The corpus target $b_4 = 9.2431$ is the *connected 4-body cumulant* of AME
([`b4_value_cumulant_target_probe.py`](../../computations/probes/b4_value_cumulant_target_probe.py):
$B(A) = \binom{A}{2}b_2 + \binom{A}{3}b_3 + \binom{A}{4}b_4$). Decomposing the
det form the same way (A=3 shells sign-independent by the diag conjugation):

| cumulant | det form at $g_{\text{reeb}}$ | AME | ratio |
|--:|--:|--:|--:|
| $b_2$ | 0.9318 | 2.2246 | 0.419× |
| $b_3$ | 1.4868 | 1.4264 | **1.042×** |
| $b_4$ | 15.058 | 9.2431 | 1.629× |

The det form's connected **3-body cumulant lands within 4.2 % of AME** while
its 2-body is 0.42× and 4-body 1.63×, with the total at 0.940× — a specific
body-order profile (pair-weak, triple-right, quad-heavy), recorded as an
observation only. No claim that the 4.2 % is structural rather than
coincidental.

## 3c. Reconciliation verdict: linear $5g$ law vs det form (decisive, scope-(a))

Under $B = E_0\cdot(-\ln\det(I+G))$ the deuteron would need an effective
magnitude $g_{\text{eff}}$ with $1-g_{\text{eff}}^2 = e^{-B_{\text{AME}}/E_0}$,
i.e. $g_{\text{eff}} \approx 0.642$ — **above the classical ceiling 0.447**.
So *no uniform per-pair magnitude makes the det form fit both $A{=}2$ and
$A{=}4$*; the linear $B(^2\mathrm{H}) = 5g$ law is structurally a **separate
assertion**, not the $A{=}2$ case of the det form. Its own fingerprint:
$5g = \mu_{\text{cl}}^2\,g = \mu_{\text{cl}}^2/\mu_q$, whose $q\to1$ limit is
$B(^2\mathrm{H}) = \sqrt5$ **MeV** exactly — the MeV unit is implicit
(dimensionally unanchored; the dashboard divides by $\alpha$ treating $5g$ as
already-MeV). Two consistent readings remain open: (i) the deuteron is not a
[1⁴]-shell object and its binding lives in a different sector (then no
reconciliation is *required*, but the ²H tier's $5g$ needs its own derivation
and unit anchor); (ii) the det form's per-pair truncation is not the physical
pair binding (its $b_2 = 0.93$ is the *exchange* pair term only). Neither is
claimed.

## 3d. Unit-anchor bounded scan for the $5g$ law (tranche 2 — negative)

[`reeb_5g_unit_anchor_scan.py`](../../computations/probes/reeb_5g_unit_anchor_scan.py)
(preregistered 10-candidate list of canonical framework energies; no
open-ended search per Rule-14): the law would need
$E_{\text{unit}} = B_{\text{AME}}/5g = 0.99594$ MeV; **no listed candidate is
within 1 %** (nearest: $2m_e = 1.0220$ MeV, giving +2.6 % on $B$; then
$m_e[2]_v = 1.0234$). Scope-(a) negative over the list only. The linear law
stays classified **asserted** with its unit anchor open.

## 3e. pn sign closed for determinant-class observables (tranche 2)

`diag(1,1,-1,-1)` conjugation flips every pn entry of the uniform-magnitude
[1⁴] exchange matrix while fixing pp/nn, and has determinant 1 — so
$\det(I + S(a, w)) = \det(I + S(a, -w))$ **identically over any commutative
ring**. Formalized sorry-free in
[`QOU/MassTheory/ReebPnMagnitude.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ReebPnMagnitude.lean)
(`pn_sign_conjugation`, `pn_sign_det_invariant`), alongside I1
(`deformation_eq_ceiling`) and I2 in Cayley–Hamilton form (`ss_matrix_sq`).
**Consequence:** the "open pn sign" of #3426 is *unobservable* in any
$-\ln\det(I+G)$-class binding form at uniform per-pair magnitude — for this
observable class it is a non-question. Scope: uniform magnitude, complete
graph; a framing assigning per-pair non-uniform magnitudes (or entering
through sign-sensitive, non-conjugation-invariant observables) can still make
the sign physical.

## 3f. ²H tier status — owner-decision flag (tranche 3)

After §2b–§2d (structure of $g$ derived), §3c (linear-vs-det
irreconcilability) and §3d (unit-anchor negative), the honest status of the
**production ²H reeb-flow tier** is: $B(^2\mathrm{H}) = 5g$ [MeV] is a
**near-match, not a derivation** — its $q\to1$ limit is $B = \sqrt5$ MeV
(matching AME to 0.52 %) with the MeV unit implicit and no canonical anchor
found. Per the tiered-reporting discipline (the c_k precedent: proved /
near-match / fitted, never silently wired), the tier should carry the
**near-match** label until either (a) a unit anchor + derivation of the
linear law lands, or (b) the owner re-tiers ²H (e.g. back to
`term-1-plus-4`, +75 %, canonical-but-worse, or to a counit-sector form).
This is a framework choice, not an agent call — flagged for owner ruling;
the tier is left untouched.

## 3g. pn sign fully routed to the weak sector (tranche 3)

§3e closed the sign for determinants; tranche 3 closes it for the **entire
spectral / mixed-trace observable class**: for any operator $T$ commuting
with the p/n grading $D$ (every charge-diagonal observable),
$\mathrm{tr}(T\,S(a,w)^k) = \mathrm{tr}(T\,S(a,-w)^k)$ for all $k$ —
Lean-proved sorry-free (`conj_pow`, `pn_sign_conjugation_pow`,
`pn_sign_trace_blind`). Since any function of $S$ alone is similarity-blind
and any grading-commuting probe is trace-blind, **the pn sign is observable
only through operators that mix the p and n blocks** — isospin
raising/lowering, i.e. the weak/β sector. The #3426 "open pn sign" is
thereby *re-classified*: it is not a binding-sector open at all; it is a
weak-sector observable, to be read off β-decay-type couplings (consistent
with the framework's bar-odd ↔ decay-width assignment).

## 3h. Per-pair-type magnitude enumeration — z anywhere is unphysical (tranche 4)

[`b4_1four_pairtype_magnitude_profile.py`](../../computations/probes/b4_1four_pairtype_magnitude_profile.py)
(preregistered 4 options, type-aware Ursell inversion, no selection): the
question was whether principled non-uniform per-pair-type magnitudes (the
only two derived magnitudes: naive $z$ vs CWF $g$) flatten the uniform-g
cumulant profile (pair 0.42×, triple 1.042×, quad 1.63×, total 0.940×).
Answer: **no option survives** — pn=g/like=z, the control pn=z/like=g, and
uniform z all give $\det(I+G) < 0$ at $A{=}4$ (unphysical); only uniform
$g$ is physical. Scope-(a): the multi-body shell enforces the sub-ceiling
magnitude on *every* bond type, so within the $\{z, g\}$ palette there is
no non-uniformity available and the uniform-g profile stands as the det
form's honest output.

## 4. Open objects (sharpened)

1. ~~Substantiate the deformation~~ — **done (§2b–§2d, Lean §3e/§3g)**. The
   derivation chain for $g$ now has exactly **one residual postulate**:
   *linking amplitude = CWF unit-tangent functional on the TL channel-space
   direction $(1, z)$* (§2d); tangent = Markov weight (derived), sine =
   CWF unit-tangent (derived).
2. ~~Reconcile linear vs det~~ — **resolved as irreconcilable at uniform $g$
   (§3c)**; unit anchor **negative (§3d)**; ²H tier flagged **near-match,
   owner ruling requested (§3f)**.
3. **Convention pinned** (Q3): $b_4 = 9.2431$ is the connected Ursell
   cumulant; the det form at $g_{\text{reeb}}$ overshoots it (1.63×) while its
   $b_3$ matches (1.04×) and $b_2$ under-binds (0.42×) — any further magnitude
   work should target the full cumulant *profile*, not the aggregate.
4. ~~The pn sign~~ — **closed for the full grading-commuting observable
   class (§3e + §3g, Lean-proved); re-classified as a weak-sector
   observable.** Binding-sector work can drop it.

## 5. Cross-references

- Sign/ceiling predecessor: [`2026-07-06 GAP-A-4 writhe design doc`](../design/2026-07-06-gap-a4-writhe-derivation-lit-review-and-framework.md), probe `b4_1four_complete_graph_writhe_signs.py` (PR #3426).
- Option-E ledger entries 2026-07-06 ([`option-e.md`](../coordination/option-e.md)).
- Norm-route disposition (this branch's theme): [`2026-07-03-qbar-norm-repitch-assessment.md`](2026-07-03-qbar-norm-repitch-assessment.md) §3–§3b (Gram-norm near-conservation / trace phase collapse).
