# Electroweak vev fixed point: derivation attempt, piece by piece (2026-11-20)

**Question (owner).** Can the formula held as the conjecture
`ElectroweakVevFixedPointClass`
([`ElectroweakBringSchwingerBridge.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakBringSchwingerBridge.lean),
used by [`electroweak-higgs-torus-link-triplet.md`](../../folio/quantum-observable-universe/knots-particles-confinement/electroweak-higgs-torus-link-triplet.md))
be derived from proved corpus results?

$$
N_v = \frac{1}{\alpha_v} = \underbrace{q\,\tfrac{[2]_q}{2}\,[4]_q[6]_q[8]_q + \tfrac{1}{\pi}}_{T_{\mathrm{EW}}}
\;-\;\alpha_v\,H\,(1-\hbar_q^2\alpha_v),\qquad H=\frac{[2]_q}{8\pi},\quad \hbar_q = 1-q^{-1}.
$$

**Answer.** No. The formula does not follow from proved corpus results. One
piece is proved, two are partly reachable, and four are selections. Each of the
four selections moves $N_v$ by between 4.4σ and $4\times10^4$σ, where σ = 257 ppb
is the experimental uncertainty on $v/m_p$. The reported −29 ppb (−0.11σ)
agreement therefore depends on all four selections. Under the anti-fit rule
(AGENTS.md §NO FITTING), the formula is a conjecture whose discrete slots have
not been derived. It is not a zero-parameter prediction.

New Lean (sorry-free, `#print axioms` shows only `propext`, `Classical.choice`
and `Quot.sound`):
[`ElectroweakVevFixedPointDecomposition.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakVevFixedPointDecomposition.lean).
Numbers come from
[`ew_vev_fixed_point_slot_sensitivity_probe.py`](../../computations/probes/ew_vev_fixed_point_slot_sensitivity_probe.py)
(mpmath, 60 dps). The run uses the proton-pinned
$q_0 = 1.10997858275138080759166909561$, $v=(\sqrt2 G_F)^{-1/2}$ with PDG
$G_F$, and CODATA $m_p$.

## 1. Per-piece status

| # | Piece | Tier | Evidence |
|---|---|---|---|
| P1 | $1/\pi = 2\cdot(1+2+3)/(12\pi)$ as an arithmetic value | **proved** | `ewBringZeroMode_eq_one_div_pi` (existing) |
| P2 | Using the carrier-genus counting rule for the zero mode | **selection** | `no_single_zero_mode_rule` (new): neither rule serves both sectors |
| P3 | $[4]_q[6]_q[8]_q$ factor | **partly reachable** | `carrier_coeff_product_qInt` (new): $a_4a_6a_8\,[2]_q^3 = h^3[4]_q[6]_q[8]_q$ |
| P4 | Prefactor $q\cdot[2]_q/2$ | **not derived (selection)** | no proved route found (§3); the EM tree term has no $[2]_q/2$ although $T(2,9)$ is also 2-strand |
| P5 | Additive assembly tree + zero mode + loop | **conjectural** | field `assembly` of `EwVevHypotheses` |
| P6 | Loop sign $s=-1$ | **selection** | `loop_sign_both_imp` (new); the EM relation uses $s=+1$ |
| P7 | Loop parameter $c=\hbar_q^2$ | **selection, numerically inert** | the corpus contraction `hecke_skein_bar_contraction` gives $1-h^2\alpha$, not $1-\hbar_q^2\alpha$; the swap moves $N_v$ by 0.15 ppb |
| P8 | Self-consistency: loop coupling $=1/N_v = m_p/v$ | **conjectural** | field `self_consistency` |
| P9 | Well-posedness: the relation fixes $\alpha_v$ uniquely | **proved** (given P5–P8) | `ewShapeCubic_existsUnique_root`, `ew_vev_unique_in_window` (new) |

`EwVevHypotheses` (new, no instance) is the decomposition. Its seven fields are
`Nv_pos`, `assembly`, `tree`, `zero_mode`, `sign`, `c_loop` and
`self_consistency`. `ewVevHypotheses_imp_class` derives
`ElectroweakVevFixedPointClass` from them. This replaces one opaque hypothesis
with six named ones of separately stated tier. It does not shrink what is
assumed.

## 2. The derived value and its miss, with each selection varied

At the proton $q_0$, $v/m_p = 262.418176526721$ and σ = 257.206 ppb (from $G_F$ alone).

| Variant (one slot changed) | $N_v$ | miss (ppb) | σ |
|---|---|---|---|
| **as published** ($s=-1$, $c=\hbar_q^2$, $Z=1/\pi$, $[2]/2$) | 262.418168819231 | −29.37 | −0.114 |
| $c=h^2$ (the corpus skein contraction) | 262.418168858606 | −29.22 | −0.114 |
| $s=+1$ (EM sign) | 262.418778593762 | +2294.3 | +8.92 |
| $s=+1$, $c=h^2$ (EM relation transcribed) | 262.418778554387 | +2294.2 | +8.92 |
| no loop term | 262.418473706851 | +1132.5 | +4.40 |
| $Z=2/(3\pi)$ (surface-genus rule, as in EM) | 262.312065400516 | −4.04e5 | −1572 |
| no zero mode | 262.099858562787 | −1.21e6 | −4716 |
| bare tree $q[4][6][8]$ (no $[2]/2$, as in EM) | 260.997870278523 | −5.41e6 | −2.1e4 |
| $([2]/2)^3$ (one dressing per carrier) | 265.282023214615 | +1.09e7 | +4.2e4 |

Run with `python3 computations/probes/ew_vev_fixed_point_slot_sensitivity_probe.py`
(measured this session). The loop term is
$\alpha_vH(1-\hbar_q^2\alpha_v) = 3.0489\times10^{-4}$, about 1.16 ppm of $N_v$.
Its cubic piece is $1.1\times10^{-8}$ (0.04 ppb).

**The honest analogue value.** Transcribing the EM relation faithfully gives
$N_v = 262.41877855$, a miss of **+2294 ppb (+8.9σ)**. That relation is the one
written in `EmCouplingBringZeroMode`, $\alpha^{-1} = T + \alpha H(1-h^2\alpha)$.
The transcription keeps the published tree term and zero mode, so it is
conditional on P2–P4 as well. The published −29 ppb is reached only by flipping
the loop sign relative to EM. `BringSchwingerNormalizationDerivation` records
that flip as "broken non-abelian anti-screening". No corpus result derives it.

## 3. What was attempted for each piece

**(a) Tree term.** The Hoefsmit carriers $\sigma_1^4,\sigma_3^6,\sigma_5^8$
(`prop:weak-spectral-completeness`, proved) reduce by $\sigma^n = a_n\sigma + b_n$
with $a_n[2]_q = q^n-(-q^{-1})^n$ (`heckeCoeff_closed`). For even $n = 2k$ this
gives $a_{2k} = h[2k]_q/[2]_q$, so $[4][6][8] = ([2]_q/h)^3\,a_4a_6a_8$. Here
$a_4a_6a_8$ is the $\sigma_1\sigma_3\sigma_5$ coefficient of the carrier word.
This is the only route found that produces the product $[4][6][8]$ from proved
structure, and it fixes the scale as $([2]_q/h)^3$, not $q[2]_q/2$. The values
are $a_4a_6a_8 = 0.26390$ and $(h/[2])^3 = 0.0011237$. Nothing in the corpus
produces:

- the factor $q$. The EM tree term $q[9]_q[10]_q$ has the same unexplained $q$.
  Bean `qou-15sj` records that the EM $[10]_q$ itself rests on an asserted
  collapse. `t35_conventionD_rowCap_excludes_binomial` shows the collapse is
  excluded under the convention-D row cap.
- the "2-strand quantum-dimension dressing" $[2]_q/2$. This applies once, not
  once per carrier ($([2]/2)^3$ gives +4.2e4σ). It is also not applied to the
  2-strand EM carrier $T(2,9)$: $q\tfrac{[2]}{2}[9][10] = 137.5687$ against
  $\alpha^{-1} = 137.0360$, a 0.39% miss. So the dressing is per-sector
  dispatch.

The identity $([2]_q/2)^2 = 1+h^2/4$ (`qInt2_sq_eq_h_sq_add_four`) is true, but
it does not select the first power.

**(b) The $1/\pi$ zero mode.** The value is proved. The counting rule is not
derived. EM uses $b_1(\Sigma_4)/\mathrm{Area} = 2g/(4\pi(g-1))$, the surface
genus. EW uses $2\sum g(\text{carrier})/\mathrm{Area}$, the carrier Seifert
genera, whose sum $6 = -\chi(\Sigma_4)$. `no_single_zero_mode_rule` proves that
the carrier rule gives $4/(3\pi)\ne 2/(3\pi)$ on the EM carriers (both of
Seifert genus 4), and that the surface rule gives $2/(3\pi)\ne 1/\pi$ for EW.
A uniform rule fails in one sector, by −1572σ for EW under the surface rule.
This is a structural statement about these two rules (scope b for "one of these
two rules serves both"). It does not exclude some third rule.

**(c) The one-loop term and the fixed point.** What is proved:

- the cubic equivalence (`ewFixedPoint_iff_cubic`, existing);
- the normalization $H=[2]_q/(8\pi) = [2]_q/(\pi b_1)$ (`habiroNorm_tiling_derived`, existing);
- the skein contraction $1+\alpha S\bar S = 1-h^2\alpha$ (`hecke_skein_bar_contraction`, existing);
- well-posedness of the root (new). For $T>0$, $H\ge0$, $c\ge0$ and $4H<T^2$,
  there is exactly one root in $(0,2/T)$. At the EW data, $T^2\approx 6.886\times10^4$
  and $4H\approx 0.32$. That inequality is verified numerically here, not in Lean.

What is not derived:

- why the loop coupling equals $1/N_v = m_p/v$. In EM, $\alpha$ is the coupling
  whose loop is being summed, so the self-consistency has a physical reading.
  In the EW sector, $m_p/v$ is not a gauge coupling. The EW couplings are
  $g, g'$ with $\alpha_W\approx 1/30$. A Schwinger-type self-consistency in
  $m_p/v$ has no stated mechanism. This is a critical assessment, not a proved
  exclusion.
- the sign.
- the choice $\hbar_q^2$ over the corpus-derived $h^2$. This choice is
  numerically inert at the present miss (0.15 ppb), so the corpus-derived form
  could replace it without changing any reported figure.

**α_EM structure (PR #1511 `[2]_q·(1−h²α)`).** That form is not proved either.
The EM Bring-zero-mode class `BringZeroModeBlochClass` has no instance (bean
`qou-006b`), and its field is expected to be false. Bean `qou-93ap` records the
best derived $\alpha^{-1}$ at −468 ppb. So copying the EM structure gives no
proved backbone, and the EW formula departs from it in the sign, the zero-mode
counting rule and the dressing.

## 4. Implications

- The block's wording "zero fitted parameters" is accurate for continuous
  parameters only. It is inaccurate under the selection clause of §NO FITTING,
  because four discrete choices each move the result far outside 1σ. This audit
  does not edit the block's prose. That rewording is for the owner.
- The precision of the comparison is set by $G_F$ (σ = 257 ppb). The miss
  (−29 ppb) is 9× smaller than σ, so the comparison cannot distinguish the
  published form from any variant within ±257 ppb, for example the $c=h^2$
  variant.
- Consumers: only the block above, the probe
  `electroweak_bring_schwinger_bridge_probe.py` and its witness, and
  `BringSchwingerNormalizationDerivation.lean` read these definitions. No
  dashboard row (`per-observable-100x-status`) scores $N_v$, so no headline
  count changes.

## 5. Corpus-grep record

These paths were searched: `docs/audits`, `folio/`, `computations/`,
`docs/coordination`, `library/INDEX.md`, `library/*/sections`,
`library/*/ocr` (for "Fermi constant", "vacuum expectation value" and
"torus link"), and `beans/defs` (mounted, 5840 files). Hits: bean `qou-z3x8`
(the EW scale v gap, `todo`), `qou-15sj` (EM tree $[10]_q$ linchpin),
`qou-93ap` and `qou-006b` (EM status). The search found no derivation of the
EW tree prefactor, the loop sign, or the $m_p/v$ self-consistency. Absence was
measured on these surfaces only.

Beans opened: `qou-rpt1` (tree prefactor $q[2]_q/2$ not derived) and `qou-myxi`
(loop sign $s=-1$ and self-consistency $\alpha_{\text{loop}}=m_p/v$ not derived),
both `todo` under `qou-20sx`.
