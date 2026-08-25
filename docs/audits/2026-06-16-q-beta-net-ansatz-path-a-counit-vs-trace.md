# Q_β net-ansatz — Path A outcome: counit vs Markov trace (2026-06-16)

**Attempt**: "try the postulated relation" — execute **Path A** from
[`2026-05-24-q-beta-net-ansatz-fitting-finding.md`](2026-05-24-q-beta-net-ansatz-fitting-finding.md):
derive $Q_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$ from the canonical
per-braid mass tower at leading order in $h = q - q^{-1}$, or show it cannot
be so derived. Path A had **never been executed** before (corpus triage: 65
audit files; the $z$-weight discrepancy below was unrecorded).

## Result (one sentence)

The relation is **exact for the Frobenius counit $\varepsilon$** (which is
what "net" is) but **not for the Markov trace $\mathrm{tr}_M$** (which is what
the per-braid mass tower is built on); the two canonical functionals coincide
on the nucleon difference only at the trivial loop $z=1$, and at the
framework's actual Markov loop $z\approx 0.499$ the trace gives $Q_\beta$
about **2× too small** — so the $+0.17\%$ match is a property of the
**counit**, not of the mass-formula functional.

## The two canonical functionals

The $N{=}0$ nucleon normal forms give the neutron$-$proton coefficient
difference, in the NF basis $[\gamma,\sigma_0,\sigma_1,L_+,L_-,e^-]$:

$$
(n-p) \;=\; \big[\tfrac{h^2}{2},\,-\tfrac{h}{2},\,-\tfrac{h}{2},\,0,\,0,\,0\big].
$$

Note the leading $L_+$ term (coefficient $1$ in both) **cancels** in the
difference; what survives is carried by $\gamma$ (the identity) and the
$\sigma_i$.

> **Which NF this is — citation repaired 2026-08-23.** This paragraph read
> *"(audit step 5)"*, a bare cross-reference naming no document; it resolves to
> nothing in the corpus, and no committed script recomputes the vector (the one
> probe carrying it,
> [`probe_path_a_net_vs_trm_leading_order.py:137`](../../computations/probes/probe_path_a_net_vs_trm_leading_order.py),
> comments *"from the .md"* — i.e. back to here). Repaired by naming the object
> instead of a step number.
>
> **This is the SINGLE-WRAP NF, not the typed 6-term NF.** The two are distinct
> corpus objects and
> [`2026-05-11-q-beta-residual-decomposition.md` §1](2026-05-11-q-beta-residual-decomposition.md)
> already names both and the **1.00579** basis-change factor between them
> (*"typed-crossings 6-term NF picks up nonzero $L_\pm$, $e^-$ contributions
> that exactly cancel at single wrap"*). The live `pyhecke.atom.PROTON_NF` /
> `NEUTRON_NF` are the **typed** ones, and their difference has **full support**
> — $\deg_z E = 3$, nothing cancels, $L_+$ least of all. So the sentence above
> about $L_+$ cancelling is true of the single-wrap NF **only**.
>
> Recomputed from `pyhecke.gram.hm` + `atom.build_nucleon_nf` symbolically over
> $\mathbb{Q}(h)$ and validated against the live constants to float64 $\epsilon$
> in
> [`qbeta_nf_single_wrap_vs_typed_probe.py`](../../computations/qbeta/qbeta_nf_single_wrap_vs_typed_probe.py)
> (8/8), which reproduces both counits — single-wrap $|\varepsilon| = 0.187207$,
> typed $|\varepsilon| = 0.188291$ — matching the 2026-05-11 audit's quoted
> $0.18721$ / $0.18829$ exactly. Which of the two is canonical for this chain is
> **open** (bean `qou-goc9`); the 0.579 % between them exceeds the 0.160 %
> $N{=}1$ ladder correction it is used to derive. Apply the two canonical functionals on $H_3(q)$, writing
$h = q - q^{-1}$ for the Hecke parameter and $z$ for the Markov loop:

| functional | def on basis | value on $(n-p)$ |
|---|---|---|
| **Frobenius counit** $\varepsilon$ | $\varepsilon(e_i)=1$ | $\dfrac{h^2}{2}-h \;=\; \dfrac{(q^2-1)(q^2-2q-1)}{2q^2}$ |
| **Markov trace** $\mathrm{tr}_M$ | $\mathrm{tr}_M(e_i)=z^{\#\mathrm{cr}(e_i)}$, so $\mathrm{tr}_M(\mathbf 1)=1,\ \mathrm{tr}_M(\sigma)=z$ | $\dfrac{h^2}{2}-hz \;=\; \dfrac{(q^2-1)(q^2-2qz-1)}{2q^2}$ |

> **Weight correction (M1).** The identity $\gamma=\mathbf 1$ carries Markov
> weight $\mathrm{tr}_M(\mathbf 1)=1$ (axiom M1), **not** $z$. The clean
> survivors are therefore $\varepsilon(n-p)=\tfrac{h^2}{2}-h$ and
> $\mathrm{tr}_M(n-p)=\tfrac{h^2}{2}-hz$, differing by $\varepsilon-\mathrm{tr}_M
> = h(z-1)$ — they coincide **iff $z=1$** (for $h\ne 0$). (An earlier draft of
> this row carried a spurious overall factor of $z$ from mis-weighting
> $\gamma$; the numeric table below — computed from the actual `TR_M`
> constants — was unaffected.)

- **"net" $=\varepsilon$.** The unweighted sum $\sum_i c_i$ is exactly the
  Frobenius counit (cited:
  [`2026-05-11-q-beta-residual-decomposition.md`](2026-05-11-q-beta-residual-decomposition.md) §2,
  "structurally-canonical projection — no weighting is missing"). It is a
  legitimate canonical map — **not** an arbitrary unweighted sum.
- **mass tower $=\mathrm{tr}_M$.** The per-braid mass tower
  [`prop:per-braid-mass-tower`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md)
  is $\mathfrak{m}(W)=|\mathrm{tr}_M(W)| + \sum_n[\dots\Phi_q(|\mathrm{tr}_M(\xi)|)\dots]$ —
  built on the **Markov trace**, with loop parameter $z$.

**They coincide only at $z=1$:** $\;\varepsilon - \mathrm{tr}_M|_{z=1}=0$
(sympy-exact). The counit is the Markov trace at the *trivial loop value*.
The framework's actual Markov loop is $z = \mathrm{tr}_M(\sigma)\approx
0.4993 \ne 1$.

## Numerical consequence (with the actual `TR_M` weights)

$\mathfrak{E}_0 = m_e/(q_0(q_0-1)) = 4.186$ MeV; CODATA $Q_\beta = 0.7823$ MeV.

| functional on $(n-p)$ | $|\Delta|$ | $|\Delta|\cdot\mathfrak{E}_0$ | vs CODATA |
|---|---|---|---|
| **counit $\varepsilon$** ("net", $N{=}0$) | $0.18721$ | $0.78365$ MeV | $\mathbf{+0.17\%}$ |
| **Markov trace $\mathrm{tr}_M$** ($N{=}0$) | $0.08253$ | $0.34549$ MeV | $-55.8\%$ |
| counit $\varepsilon$ (full numeric NF) | $0.18829$ | $0.78818$ MeV | $+0.75\%$ |
| Markov trace $\mathrm{tr}_M$ (full numeric NF) | $0.11789$ | $0.49347$ MeV | $-36.9\%$ |

The Markov-trace difference is $\approx 1.6\text{--}2.3\times$ smaller than the
counit difference, because the surviving $\sigma_i$ terms are weighted by
$z\approx 0.5$ under $\mathrm{tr}_M$ but by $1$ under $\varepsilon$. With the
mass tower's own functional, $Q_\beta$ lands $37\text{--}56\%$ low.

## Verdict — refines the 2026-05-24 (a)/(b) dichotomy

The original finding framed the $+0.17\%$ as either (a) genuine $N{=}0$
truncation residual or (b) numerical coincidence (fitting). Path A shows it
is **neither, exactly** — it is a **functional mismatch**:

- **Not pure fitting (b).** "net" is the Frobenius counit, a canonical
  categorical functional — not a tuned number. The $+0.17\%$ is the *counit's*
  prediction, and the counit is structurally principled.
- **Not the tr_M leading order (a).** The per-braid mass tower is built on the
  Markov trace, and $\mathrm{tr}_M$ on the nucleon difference gives $Q_\beta$
  $\sim 2\times$ too small. The ansatz does **not** expand the tr_M mass tower
  at leading order; it silently replaces $\mathrm{tr}_M$ with $\varepsilon$.

So the gap is now **precisely named**: the $Q_\beta$ ansatz is *$\varepsilon$-based*
while the mass formula is *$\mathrm{tr}_M$-based*, and these are distinct
canonical functionals that disagree on the nucleon difference. The
relation $Q_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$ is an exact
identity **for $\varepsilon$**; whether it is a *derivation* hinges on a
question no current content answers:

> **Why is the leading-order mass *difference* governed by the Frobenius
> counit $\varepsilon$ rather than the Markov trace $\mathrm{tr}_M$ that the
> mass itself uses?**

## Categorical grounding — trace = pair-with-unit, counit = pair-with-integral

Both functionals are the **same Frobenius pairing**
$\langle x,y\rangle_G = \mathrm{tr}_M(xy)$ (Gram matrix $G_{ij}=\mathrm{tr}_M(b_ib_j)$)
— they differ only in *which element they pair against*. The categorical
action lands in $H_3(q)$, a **symmetric Frobenius algebra** with the Markov
trace as symmetrizing form.

- **Trace $=$ pair with the unit $\mathbf 1$.** The dual-basis identity
  $G^{-1}t = e_\gamma$
  ([`2026-05-11-q-beta-residual-decomposition.md`](2026-05-11-q-beta-residual-decomposition.md) §2,
  re-verified here numerically) says the Markov vector $t_i=\mathrm{tr}_M(b_i)$
  is the $G$-image of the **identity element** $\mathbf 1=e_\gamma$. Hence
  $$\mathrm{tr}_M(\beta)=\langle\beta,\mathbf 1\rangle_G.$$
  Categorically this is the **loop / Markov closure** (cap the cylinder); a
  static mass is a closed loop, so the mass uses $\mathrm{tr}_M$.

- **Counit $=$ pair with the integral $\omega$.** The augmentation
  $\varepsilon(\beta)=\sum_i x_i$ is *also* a $G$-pairing, against a distinct
  element $\omega = G^{-1}\mathbf 1$ (computed:
  $\omega=(0.601,0.188,0.188,0.396,0.396,0.026)$, normalised so
  $\mathrm{tr}_M(\omega)=1$):
  $$\varepsilon(\beta)=\langle\beta,\omega\rangle_G,\qquad \omega=G^{-1}\mathbf 1.$$
  $\omega$ is the **(co)integral** — the Frobenius dual of the augmentation
  covector $\mathbf 1=(1,\dots,1)$.

The two are the *same trace at different loop values*: $\varepsilon =
\mathrm{tr}_M|_{z=1}$, and $z=1$ is the **$q$-stripped / topological limit**
(unreachable for real $q$, since $\sqrt q + 1/\sqrt q \ge 2$). So:

| observable | functional | pairs with | measures |
|---|---|---|---|
| mass $\mathfrak m=\lvert\mathrm{tr}_M\rvert$ | trace | unit $\mathbf 1$ | $q$-weighted **dynamics** (loop) |
| $Q_\beta=\varepsilon(\Delta)\,\mathfrak E_0$ | counit | integral $\omega$ | $q$-stripped **net topology** |

**Physical reading** (motivated, not proven): $\beta$-decay $n\to p+e^-+\bar\nu$
reroutes *conserved topological content* ($d\to u$), which the augmentation
$\varepsilon$ — braiding stripped — counts; a mass is the *dynamical* loop
amplitude, which the $q$-weighted $\mathrm{tr}_M$ measures. A transition
amplitude pairs with the integral; a partition function pairs with the unit.
That is *why* the difference (a transition) can be a counit while the masses
(loops) are traces.

## Forward direction (constructive, not a dead end)

This is a concrete lead, not a refutation. In the nucleon difference the
leading $L_+$ term cancels (both have coefficient $1$); the surviving part
lives in the lower-crossing sector ($\gamma,\sigma_i$). The counit
$\varepsilon$ and the Markov trace $\mathrm{tr}_M$ are related through the
Frobenius form on $H_3(q)$; it is plausible that the mass *difference* (where
the top-weight term cancels) projects onto a counit-like component while the
mass *itself* is trace-dominated. Making that precise — expressing
$\mathfrak{m}(n)-\mathfrak{m}(p)$ via the Frobenius pairing and showing its
leading term is $\varepsilon(n-p)\cdot\mathfrak{E}_0$ — would *complete*
Path A and convert the ansatz into a theorem. Until then the relation
remains an exact *counit* identity, not a *mass-tower* derivation.

## Reproducibility

All symbolic identities (`net = ε`, `ε = tr_M|_{z=1}`, `ε − tr_M = h(z−1)`,
the difference forms) are sympy-exact; the pairing facts (`G⁻¹t = e_γ`,
`ω = G⁻¹𝟙`, `tr_M(ω)=1`) use the framework's `G`, `G_INV`, `TR_M` constants;
the numeric table uses `PROTON_NF`, `NEUTRON_NF`, `TR_M` and $q_0$ from
`qou_substrate`. No fitting, no scan — a pre-registered comparison of two
named canonical functionals. The core algebraic identities are
Lean-verified in
[`qbeta_counit_vs_trace.lean`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_counit_vs_trace.lean).
