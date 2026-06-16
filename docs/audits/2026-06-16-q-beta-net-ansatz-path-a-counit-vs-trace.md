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

The $N{=}0$ nucleon normal forms (audit step 5) give the
neutron$-$proton coefficient difference, in the NF basis
$[\gamma,\sigma_0,\sigma_1,L_+,L_-,e^-]$:

$$
(n-p) \;=\; \big[\tfrac{h^2}{2},\,-\tfrac h2,\,-\tfrac h2,\,0,\,0,\,0\big].
$$

Note the leading $L_+$ term (coefficient $1$ in both) **cancels** in the
difference; what survives is carried by $\gamma$ and the $\sigma_i$.
Apply the two canonical functionals on $H_3(q)$:

| functional | def on basis | value on $(n-p)$ |
|---|---|---|
| **Frobenius counit** $\varepsilon$ | $\varepsilon(e_i)=1$ | $\dfrac{(q-1)(q+1)(q^2-2q-1)}{2q^2}$ |
| **Markov trace** $\mathrm{tr}_M$ | $\mathrm{tr}_M(e_i)=z^{\#\text{cr}(e_i)}$ | $\dfrac{z\,(q-1)(q+1)(q^2-2qz-1)}{2q^2}$ |

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

All symbolic identities (`net = ε`, `ε = tr_M|_{z=1}`, the two factorized
difference forms) are sympy-exact; the numeric table uses the framework's
`PROTON_NF`, `NEUTRON_NF`, `TR_M` constants and $q_0$ from `qou_substrate`.
No fitting, no scan — a single pre-registered comparison of two named
canonical functionals.
