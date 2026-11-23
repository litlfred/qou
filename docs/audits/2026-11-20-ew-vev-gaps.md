# Electroweak vev fixed point: derivation attempts for the four open slots (2026-11-20)

**Question.** The previous audit
([`2026-11-20-ew-vev-fixed-point-derivation.md`](2026-11-20-ew-vev-fixed-point-derivation.md))
split the vev formula

$$
N_v = q\,\tfrac{[2]_q}{2}\,[4]_q[6]_q[8]_q + \tfrac1\pi \;-\; \alpha\,H\,(1-\hbar_q^2\alpha),
\qquad H=\tfrac{[2]_q}{8\pi},\quad \alpha = \tfrac{1}{N_v} = \tfrac{m_p}{v},
$$

into named hypotheses and left four of them open: the tree prefactor
$q\cdot[2]_q/2$ (bean `qou-rpt1`), the loop sign $s=-1$ and the loop coupling
$\alpha_{\text{loop}} = m_p/v$ (bean `qou-myxi`), and the zero-mode counting rule.
This audit tries to derive each one, or to exclude it, or to reduce it to a
smaller named hypothesis.

**Answer.** None of the four is derived. One (the zero-mode rule) reduces to a
single rule that serves both sectors. One (the sign) reduces to a sector
assignment plus a standard sign rule. That same assignment then conflicts with
the self-consistency. The tree prefactor splits in two: its factor $q$ is
excluded from every bar-invariant source (scope b), and its exponent $k=1$ on
$[2]/2$ has no rule. The two rules found force $k=0$ or $k=3$, and they miss by
$-2.1\times10^4\sigma$ and $+4.2\times10^4\sigma$.

New Lean module:
[`ElectroweakVevGaps.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakVevGaps.lean).
It is sorry-free. `#print axioms` gives `propext`, `Classical.choice`,
`Quot.sound` on all twelve headline declarations (`loopShift_identity` uses
only `propext`, `Quot.sound`). It was verified by `lean -DautoImplicit=false -s 65536`
against a private olean cone; the cone sources are byte-identical to the ones the
previous audit compiled. The orphan gate reports no new orphans.
Numbers come from
[`ew_vev_gaps_probe.py`](../../computations/probes/ew_vev_gaps_probe.py)
(mpmath, 60 dps). Inputs are the proton $q_0 = 1.10997858275138080759166909561$,
$G_F$ and $m_p$ from `library/codata-2022/values.json`, and the PDG-2024
$m_W = 80.3692$ GeV, which is used only for the $\alpha_2$ reading in §3.
$v/m_p = 262.418176526721$, σ = 257.206 ppb, from $G_F$ alone.

Each rule below was written into the probe before its comparison was printed.
None was chosen by agreement. Where a rule was found by solving against corpus
values, the section says so.

## 1. Tree prefactor $q\cdot[2]_q/2$ (bean `qou-rpt1`)

**(a) The factor $q$: excluded from bar-invariant sources (scope b).** Invariant:
the bar involution $q\mapsto q^{-1}$. Every balanced quantum integer is
bar-invariant (`qIntF_bar`). The tree satisfies $T(q^{-1})\,q^2 = T(q)$
(`ewTreeF_bar`), so $T$ is bar-invariant only if $q^2=1$ or $T=0$
(`ewTreeF_bar_invariant_imp`). The probe confirms
$T(q_0)/T(q_0^{-1}) = q_0^2 = 1.23205245416676393$ to 60 digits. Consequence: no
expression built from quantum integers, quantum dimensions or other
bar-invariant data can supply the $q$. It needs a bar-breaking source, such as
a framing or writhe factor or the convention-D Markov parameter
$z_D = q^3/(q^2+1)$; note $q[2]_q = q^2+1 = q^3/z_D$. No such derivation was
found. The EM tree $q[9]_q[10]_q$ carries the same factor with the same bar
ratio (`emTreeF_bar`), so this is one shared open item for both sectors, not an
EW one.

**(b) The exponent of $[2]_q/2$.** Write $T_k = q([2]/2)^k[4][6][8]$. For
$q>1$, $[2]/2>1$ (`dressing_gt_one`), so $T_k$ is strictly increasing in $k$
(`treeK_strictMono`) and the choice of $k$ is not inert. Two rules with a stated
mechanism were tried:

| Rule | forces | $N_v$ | miss (ppb) | σ |
|---|---|---|---|---|
| EM tree rule $q\prod_i[n_i]$ applied uniformly | $k=0$ | 260.997870278523 | −5.41238e6 | −2.104e4 |
| one $[2]/2$ (quantum/classical dimension of the fundamental) per extra link component, $\mu-1=1$ per carrier, 3 carriers | $k=3$ | 265.282023214615 | +1.09133e7 | +4.243e4 |
| published (no rule found) | $k=1$ | 262.418168819231 | −29.371 | −0.114 |

Scope (a): each rule, alone, does not reproduce $v/m_p$. Neither is excluded as
an ingredient. No rule found yields $k=1$. Per-sector rules exist ("one dressing
per link sector"), but they are dispatch: they branch on the sector.

**(c) Markov-trace route (asked for in `qou-rpt1`).** The far-commuting factors
$\sigma_1^4,\sigma_3^6,\sigma_5^8$ give a product of $H_2$ traces
$\prod_n(b_n + a_n z_D)$ under the multiplicative Ocneanu trace. The value is
**3.70244669186027**, against the tree's 262.100163820667. Scope (a): the
convention-D Markov trace of the carrier word does not give the tree. Its scale
is O(1). This route is in the probe only. The multiplicativity of the Ocneanu
trace on far-commuting factors is the standard property and is not
re-formalized here.

**Status: the factor $q$ is excluded (scope b, bar invariant) from
bar-invariant sources and is open for bar-breaking ones, shared with EM. The
exponent $k=1$ is unreduced.**

## 2. Zero-mode counting rule

The previous audit proved that neither of the two rules then on record serves
both sectors (`no_single_zero_mode_rule`). A third rule does:

$$
Z = n_{\text{carriers}}\cdot\frac{g(\Sigma_4)}{\operatorname{Area}(\Sigma_4)}
= n_{\text{carriers}}\cdot\frac{\dim H^{1,0}(\Sigma_4)}{12\pi}.
$$

It gives $2/(3\pi)$ for the two EM carriers $\{T(2,9),T(3,5)\}$
(`perCarrier_em`) and $1/\pi$ for the three EW carriers (`perCarrier_ew`),
checked to 50 digits in the probe. In the unified relation's notation it reads
$G = 2n$, so $G_{EM}=4$ and $G_{EW}=6$. It is the **unique** rule in which each
carrier of Seifert genus $g_i$ contributes $a g_i + b$ to a common numerator
(`genusAffine_unique`: $a=0$, $b=4$). Each carrier contributes the same amount
whatever its genus.

**Caveat, load-bearing.** This rule was found by solving the affine family
against the two corpus values. It is two equations in two unknowns, so its
existence is not evidence. It shows only that $2/(3\pi)$ and $1/\pi$ are
mutually consistent under one simple rule. It inherits whatever selection went
into $1/\pi$, and it changes no number. A test would be a third sector with a
known zero mode and a different carrier count.

**Status: reduced to one named, cross-sector hypothesis ("one $H^{1,0}$ quantum
per carrier"). Not derived.** `EwVevReducedHypotheses.zero_mode` carries it.

## 3. Loop sign $s=-1$ and loop coupling $\alpha_{\text{loop}}=m_p/v$ (bean `qou-myxi`)

**Sign: reduced.** Take the standard rule that the loop sign is $-\operatorname{sgn} b_0$,
where $b_0 = -\tfrac{11}{3}C_A + \tfrac23\sum T(\text{Weyl}) + \tfrac13\sum T(\text{complex scalar})$
(positive means screening). For the SM $SU(2)_L$ content (12 Weyl doublets, one
Higgs doublet), $b_0 = -19/6$ (`b0_su2_sm`), so $s=-1$ (`signRule_su2`). Any
abelian group with a charged fermion has $b_0>0$ (`b0_abelian_pos`), so $s=+1$
(`signRule_abelian`), which is the EM sign. One rule therefore covers both
sectors, provided the vev sector's loop is assigned to $SU(2)_L$. That
assignment is a hypothesis (`EwVevReducedHypotheses.sector_group`). Under a
$U(1)$ assignment the sign is $+1$ and the miss is **+2294.3 ppb (+8.92σ)**.
The rule is standard physics, not a corpus derivation. It is also the reading
the corpus already gives ("non-abelian anti-screening"), so adopting it is not a
new choice made against the target. It uses only the sign of $b_0$ and not its
magnitude. A rule that took both would rescale $H$ by $|b_0|$, and the corpus
$H$ carries no $b_0$.

**Coupling: the sign reading conflicts with the self-consistency.** If the loop
is the $SU(2)_L$ gauge loop, its coupling is
$\alpha_2 = \sqrt2 G_F m_W^2/\pi = 0.033914389$ (≈1/29.5). The
self-consistency requires $\alpha_{\text{loop}}\cdot N_v = 1$, i.e.
$\alpha_{\text{loop}}\approx 0.00381$. Both cannot hold
(`su2_coupling_not_selfConsistent`: $\alpha_2>1/30$, $N_v>100$,
$\alpha_2 N_v=1$ is a contradiction). So the reading that justifies $s=-1$ is
the same reading under which the loop coupling should be $\alpha_2$, not
$m_p/v$. Loop couplings evaluated non-self-consistently, $N = T - \kappa H(1-\hbar_q^2\kappa)$:

| $\kappa$ | $N_v$ | miss (ppb) | σ |
|---|---|---|---|
| $m_p/v$ (published) | 262.41816881924 | −29.371 | −0.114 |
| $\alpha_2$ ($G_F$, $m_W$) | 262.415761084637 | −9204.55 | −35.79 |
| $\alpha_{\text{em}}(0)$ | 262.417889879881 | −1092.33 | −4.25 |
| 0 (no loop) | 262.418473706851 | +1132.47 | +4.40 |

**How sharply the data test $\kappa=m_p/v$.** By `loopShift_identity`,
$N(\kappa)-N(\kappa') = -H(\kappa-\kappa')(1-c(\kappa+\kappa'))$. The 1σ band on
$v/m_p$ admits $\kappa\in[0.002870741,\,0.0045580216]$, which is
$[0.7533,\,1.1961]\times m_p/v$. So the comparison confirms the sign and the
order of magnitude of the loop. It does not confirm the identification
$\kappa = m_p/v$ to better than about ±20 %. Per AGENTS §"Defined residual" check 2,
the agreement is *in range* rather than *forced*.

**Status.** Sign: reduced to the sector assignment `sector_group` plus the $b_0$
rule. Coupling: not derived. The one physical reading that fixes the sign
excludes it (scope b only relative to that reading, with the invariant being the
inequality $\alpha_2 > 1/30 > 1/N_v$). Otherwise it stays a named hypothesis
(`self_consistency`). The tension between the two fields is now a proved
statement, not a remark.

**$c=\hbar_q^2$ vs $h^2$.** Unchanged from the previous audit: the corpus
contraction gives $h^2$, and the swap moves $N_v$ by 0.15 ppb. Not revisited.

## 4. All slots set by uniform cross-sector rules

With $k=0$, the per-carrier zero mode, $c=h^2$ and the self-consistency:

| sign | $N_v$ | miss (ppb) | σ |
|---|---|---|---|
| $s=-1$ | 260.997870318328 | −5.41238e6 | −2.104e4 |
| $s=+1$ | 260.998483331389 | −5.41004e6 | −2.103e4 |

The uniform transcription is dominated by the dressing exponent. That is the
honest value of the formula without per-sector dispatch: about **−0.54 %**.

## 5. Reduced decomposition

`EwVevReducedHypotheses` (no instance) replaces three fields of
`EwVevHypotheses`. The zero mode becomes the per-carrier rule. The sign becomes
`sector_group` plus `sign_rule`. The tree gains an explicit
`dressing_exponent : k = 1`. `ewVevReduced_imp_hypotheses` derives
`EwVevHypotheses` from it. Open fields: `assembly`, `dressing_exponent`, the
shared factor $q$ inside `tree`, `sector_group`, `c_loop` and
`self_consistency`. `sector_group` and `self_consistency` are in proved tension
(§3).

## 6. Corpus-grep record

These surfaces were searched: `docs/audits`, `docs/coordination`,
`folio/quantum-observable-universe`, `computations` and `beans/defs` (mounted,
5844 files), plus `library/INDEX.md`, `library/*/sections` and
`library/*/ocr` in the shared checkout. Search terms: anti-screening, β/$b_0$
coefficient, per-carrier, carrier count. No prior derivation of the dressing
exponent, the factor $q$, a uniform zero-mode rule, or the loop coupling was
found on these surfaces. That is absence on these surfaces only. Related beans:
`qou-15sj` (EM $[10]_q$) and `qou-z3x8` (EW scale gap).

## 7. What this changes

No dashboard row scores $N_v$. The block
`electroweak-higgs-torus-link-triplet.md` and its prose are not edited. The
items for the owner are:

- whether "zero fitted parameters" should read "no continuous parameter; the
  dressing exponent is a per-sector dispatch";
- whether the vev sector's loop is an $SU(2)_L$ loop (which fixes the sign
  but contradicts the self-consistency) or a loop in $m_p/v$ (no stated
  mechanism and no sign rule).

These are recorded in the beans. If the owner says nothing, the formula stays a
conjecture with the decomposition above.
