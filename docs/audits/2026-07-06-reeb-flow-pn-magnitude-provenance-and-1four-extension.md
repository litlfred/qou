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

## 4. Open objects (sharpened)

1. ~~Substantiate the deformation~~ — **done at the structure level (§2b)**,
   **Lean-formalized (§3e)**; the sine normalization is now **derived from
   the CWF unit-tangent integrand (§2c)** modulo one geometric
   identification: *$z$ = per-unit-Reeb-time crossing density (tangent) of
   the bond inclination*.
2. ~~Reconcile linear vs det~~ — **resolved as irreconcilable at uniform $g$
   (§3c)**; the unit-anchor scan is a bounded **negative (§3d)** — the ²H
   linear law still needs a derivation or a re-tier of ²H out of the
   exchange sector.
3. **Convention pinned** (Q3): $b_4 = 9.2431$ is the connected Ursell
   cumulant; the det form at $g_{\text{reeb}}$ overshoots it (1.63×) while its
   $b_3$ matches (1.04×) and $b_2$ under-binds (0.42×) — any further magnitude
   work should target the full cumulant *profile*, not the aggregate.
4. ~~The pn sign~~ — **closed for determinant-class observables (§3e,
   Lean-proved)**; remains open only for sign-sensitive observables or
   non-uniform per-pair framings.

## 5. Cross-references

- Sign/ceiling predecessor: [`2026-07-06 GAP-A-4 writhe design doc`](../design/2026-07-06-gap-a4-writhe-derivation-lit-review-and-framework.md), probe `b4_1four_complete_graph_writhe_signs.py` (PR #3426).
- Option-E ledger entries 2026-07-06 ([`option-e.md`](../coordination/option-e.md)).
- Norm-route disposition (this branch's theme): [`2026-07-03-qbar-norm-repitch-assessment.md`](2026-07-03-qbar-norm-repitch-assessment.md) §3–§3b (Gram-norm near-conservation / trace phase collapse).
